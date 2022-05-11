const gulp = require('gulp');
const sass = require('gulp-sass');
const pug = require('gulp-pug');
const autoprefixer = require('gulp-autoprefixer');
const sourcemaps = require('gulp-sourcemaps');
const htmlmin = require('gulp-htmlmin');
const browserSync = require('browser-sync').create();

//scss to css
function style() {
  return gulp.src('assets/scss/**/*.scss')
    // .pipe(sourcemaps.init())
    .pipe(sass({
      //outputStyle: 'compressed'
    }).on('error', sass.logError))
    .pipe(sourcemaps.write())
    .pipe(autoprefixer('last 2 versions'))
    .pipe(gulp.dest('assets/css'));
}

// pug to html
function html() {
  return gulp.src('assets/pug/pages/**/*.pug')
    .pipe(pug({
      pretty: true
    }))
    .on('error', console.error.bind(console))
    .pipe(gulp.dest('pages/'))
    .pipe(browserSync.reload({
      stream: true
    }));
}

// Watch function
function watch() {
  browserSync.init({
    proxy: 'http://localhost/chatloop/html/index.html'
  });
  gulp.watch('assets/scss/**/*.scss', style);
  gulp.watch('assets/pug/pages/**/*.pug', html);
  gulp.watch('*.html').on('change', browserSync.reload);
  gulp.watch('assets/css/*.css').on('change', browserSync.reload);
}

exports.style = style;
exports.html = html;
exports.watch = watch;


const build = gulp.series(watch);
gulp.task('default', build, 'browser-sync');