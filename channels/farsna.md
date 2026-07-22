<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/Ml7TZqxbaiyyDsI-0ITTrK0lpT59cTsxjXnDQHGIjjpeEZ1cYn78JwS_B2gN7Virv6MT1fnrXY2duJxqYAqXYpXCSS2ZTJAr8VIyXcXkZzh4E9kSHEXApyMAqi6xnPB_CvbIBM3VPcAacmKlCVVgyb2XRSCx856OtAeUJZ9VJvJ9ZoUplQUUMU42_bGVlcHyt-HEC71SUox-xU6HBWtUBjkKptXr0BXs24YpNmxAXHKJ-chUNGTQMwZh0kNxwh4I-Z0JEkvcMx9O77u0l5tV9SZszdLkv6plL66TqWXsVzgdyq_JjOYWVvEZTEOWCgeUWOKk5svrnunin8fUSyP3zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-451966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHFng8fqhK5NhxsBa5p5FDVvf3btBK1O-YDpEByj5md8bYmC5bHjDEx6haszWQnViSvZuQFx4FeuXz_JP1GtCZshX7-PFb5evJ2YniqJJgRHVrvZmEfXtJAECZRPXDKR2Fd5IfCmsfEyYC6s_PGRPzoG0wzrOtnO0yWOPMecb33VoQDLl3yTBD7mhTYsc2uvY6Vz_8e7aP7A4ZZ8XqrKFvtNOEAXrVF8QPWA0tMn3h-__jd2CbBy1nn48A_71OAUUHyfswAC_fc-KaG8DZFruu6XhuyU21vDsNLP7pQnHtzi3yAqGYMblvmo8SKUU9uiB_p5KrPA63aIoF93UTmMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین پارکینگ زوار اربعین در خسروی پر شد
🔹
فرماندار قصرشیرین، از تکمیل ظرفیت نخستین پارکینگ مرز خسروی با بیش از ۲۰ هزار خودرو، پیش از آغاز رسمی عملیات اربعین خبر داد.
🔸
در قصرشیرین و خسروی، ۲۲ پارکینگ با ظرفیت بیش از ۳۰۰ هزار خودرو احداث شده که به برج نوری و دوربین مداربسته مجهز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/farsna/451966" target="_blank">📅 21:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e56a147.mp4?token=CBisMYaZseh2FyyigSgUZWhVQvLwzDNlWoYO27KsDX8TH_jnTFY38OQL3TI6KXG0zFvpcc8gT_h6tGMo-34Ab-Smfw4AeqnaWdSVMvF57ge4pwvwvl2yls8EJ3oTApnnt_Fh_LaZB5nxpMaf4gg2LNibHn5boHhIzGRWMN4z16L3zdQx80WFfnt4BEb5OfHNXWjjVZbe3MVwaizbEOMDxJYrGaJR-RNQ7Ow5YP0AuNAZ1BDQdumqLzKQao9cQGShMNlG4Wt0cmthYUxJh19CoYzMVNb8indrGtrBseT3vl6JjZVEWDGtmMVTGLx8sDILaaSsyakvzZvALdonXVMSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e56a147.mp4?token=CBisMYaZseh2FyyigSgUZWhVQvLwzDNlWoYO27KsDX8TH_jnTFY38OQL3TI6KXG0zFvpcc8gT_h6tGMo-34Ab-Smfw4AeqnaWdSVMvF57ge4pwvwvl2yls8EJ3oTApnnt_Fh_LaZB5nxpMaf4gg2LNibHn5boHhIzGRWMN4z16L3zdQx80WFfnt4BEb5OfHNXWjjVZbe3MVwaizbEOMDxJYrGaJR-RNQ7Ow5YP0AuNAZ1BDQdumqLzKQao9cQGShMNlG4Wt0cmthYUxJh19CoYzMVNb8indrGtrBseT3vl6JjZVEWDGtmMVTGLx8sDILaaSsyakvzZvALdonXVMSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب داغ تازهٔ میناب در فضای مجازی
@Farsna</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/451965" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cecb9a4af7.mp4?token=qvxJJZW6XWI11DxNKINreexJqY4DzA-x8KrfvGosUFUtgny1bdNkxUbtMFNVG91tc8c9ZxrGPbvl-nYHcLYtmMn6sqI3QAkgzU8FYu-BzvVvT7KEICO-X9bSWUhYtFln69nLKSGmWJ5H62acCiVzMQ4sgMWZxngi0yOL2qU_h0KRFFMM5oD_3LBvE4vy49K5KXbCq8HlLH8zLUg9qOeWe7RM0jq0kvR8VFo_odEwMamQdYusLhEjypdTs60usCRf_gyN4cdxTNv4_gqa7KX0tW9MOYNiTZxn3cibexhNxPKiDycNeElVI20MqVr5JEe-plY4FfC2lSu99R4FxXEAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cecb9a4af7.mp4?token=qvxJJZW6XWI11DxNKINreexJqY4DzA-x8KrfvGosUFUtgny1bdNkxUbtMFNVG91tc8c9ZxrGPbvl-nYHcLYtmMn6sqI3QAkgzU8FYu-BzvVvT7KEICO-X9bSWUhYtFln69nLKSGmWJ5H62acCiVzMQ4sgMWZxngi0yOL2qU_h0KRFFMM5oD_3LBvE4vy49K5KXbCq8HlLH8zLUg9qOeWe7RM0jq0kvR8VFo_odEwMamQdYusLhEjypdTs60usCRf_gyN4cdxTNv4_gqa7KX0tW9MOYNiTZxn3cibexhNxPKiDycNeElVI20MqVr5JEe-plY4FfC2lSu99R4FxXEAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیت‌کوین یارانه‌تان را قطع می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/451964" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6dQX2nTEFk4pgv7lSYfPAIGya1nueyI_ZeHgwTp41VJZhwjabvIqjkp0PJRWx01AAGHqN5PQfY7880RH9BtoPURhjxbC-o5NhhMdbMfoZs3Ne6sG-ds5utGfoDjF9wd8rplcEGRNT08E1JXhFqC8OdOFLW5thXd2NlgDV6W0VZlPWQwgInMeylBpjtmH9g0d_-z7Bb0JzVLrZU59jXNoxOxy3tLC2lFNgZDpBR4NinYRKdSZLpwJrf1QUcbRWiGjsPx2X2vJN6OeXyPKEldxF5LsoM_exLev7zY_eBeG-cefvKcFo8j63Zf9VYbW39mh3auZ7PnawRdYDnPotRnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: هرگونه خطای محاسباتی علیه ایران، بازار انرژی جهان را به آتش می‌کشد
🔹
جمهوری اسلامی ایران در مرحله جدیدی از بازدارندگی قرار دارد؛ تصورِ ضربه‌زدنِ کم‌هزینه به ایران، خطایی است که می‌تواند پیامدهایش بسیار فراتر از میدان نظامی به بازار انرژی و اقتصاد جهانی منتقل شود.
🔹
کاخ سفید  بداند که با تهدید ایران و بسیج متحدین منطقه ای و فعال کردن لابی اروپا، به امنیت و ثبات بیشتر نمیرسد بلکه پیامد خطاها را جهانی خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/451963" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccd5526f6.mp4?token=I2QzyPR61TRsHivZucYJRfEABvUK80qJKnnCZT0p_8VC2ronvmWiznZHXw6N2gaZK6OpbMbDOE4JOLmxRHYd1ct9z2NuYG62XndgMJncrjuxIKjuc9_BOVFEqiJtej22Gt3tzIg1kPZCtbC-pauDa0u_sxwN3PjNJh91QV4cCA0w2e-6G7CnqNdkjo5uOL1u-Hu-pIagjBwTj4u0nF6Jf6qafzoXoPITJQVUyyRBxIxma7W8A4oB-CBeI8I2DYr9n-j6EU8sAFOLXdti4hgWIS4sGASrwuaxXQ9mCvcD4yxH4_-99bXxmvqgD_NltAy7s3kIItHG3Y87nKAjbfCbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccd5526f6.mp4?token=I2QzyPR61TRsHivZucYJRfEABvUK80qJKnnCZT0p_8VC2ronvmWiznZHXw6N2gaZK6OpbMbDOE4JOLmxRHYd1ct9z2NuYG62XndgMJncrjuxIKjuc9_BOVFEqiJtej22Gt3tzIg1kPZCtbC-pauDa0u_sxwN3PjNJh91QV4cCA0w2e-6G7CnqNdkjo5uOL1u-Hu-pIagjBwTj4u0nF6Jf6qafzoXoPITJQVUyyRBxIxma7W8A4oB-CBeI8I2DYr9n-j6EU8sAFOLXdti4hgWIS4sGASrwuaxXQ9mCvcD4yxH4_-99bXxmvqgD_NltAy7s3kIItHG3Y87nKAjbfCbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: اگر واقعیت و جزئیات عملیات اصفهان منتشر شود، خواهید فهمید دشمن برتری عملیات زمینی نسبت به ما ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/farsna/451962" target="_blank">📅 21:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77170f3a.mp4?token=QFb-6WYRNK1rlpKXDn4HMVGvk_iFf-GPt-lqn6AVbAYalGBJq5EdQFRg5VACLQo87XCW95v0sr5lsg8q6oetI-MFuyMK6l9TveiRjWZ80Xc2ONk9lYqEvkSN6xMet2YzU5n40Rj8LIeLhSjrU8nEyiCqyYKm3kDA31ZAisWVqovYAF9BWE4Opbu-8ptvVpDB-w4Deal6cF_8P-ahXRogJHZia1G2zo-Y5-tdOMgvTR2CpI_kPviTFBT7Qjmazsqa0Rfp0P3ZUFvfq9dfoO0FLfvEPcGt6QabTjy_uuOFlAmB76n7vvks9k_XicSVSBawdoyg-_c50O0tYjAJvE9024aW2SKBvuYUpWLjvJQ4Bygrcvp1eWA5_gX_hciC9iQa-3k3MKsdgVRojPnT5mYgpN8gQDf1xiIb0aqpc3zShTzIKKaFwPg_ocpPOXuFLl74qlSBqPsSsB5xTllGwzD3QUy4p2_Cei03RTJ353b-ZU3phafiIYRRXc5I5Xfhw3YXA70T-fG4IvEnpc3RM9mEStTLqVfuHXN17_oEdVcV2IzQFlzHQEfQ0Ggje7zbcgqZN4QRqlCqgXxJqtyJM6a8stPr7YGNGu6jrOmMo5jM_LazYI7x2JdKO8jRc0hs6NpI9DhOf7gN3oklZSzKxmAnaeg5XAa80jWuac7yVPHxRs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77170f3a.mp4?token=QFb-6WYRNK1rlpKXDn4HMVGvk_iFf-GPt-lqn6AVbAYalGBJq5EdQFRg5VACLQo87XCW95v0sr5lsg8q6oetI-MFuyMK6l9TveiRjWZ80Xc2ONk9lYqEvkSN6xMet2YzU5n40Rj8LIeLhSjrU8nEyiCqyYKm3kDA31ZAisWVqovYAF9BWE4Opbu-8ptvVpDB-w4Deal6cF_8P-ahXRogJHZia1G2zo-Y5-tdOMgvTR2CpI_kPviTFBT7Qjmazsqa0Rfp0P3ZUFvfq9dfoO0FLfvEPcGt6QabTjy_uuOFlAmB76n7vvks9k_XicSVSBawdoyg-_c50O0tYjAJvE9024aW2SKBvuYUpWLjvJQ4Bygrcvp1eWA5_gX_hciC9iQa-3k3MKsdgVRojPnT5mYgpN8gQDf1xiIb0aqpc3zShTzIKKaFwPg_ocpPOXuFLl74qlSBqPsSsB5xTllGwzD3QUy4p2_Cei03RTJ353b-ZU3phafiIYRRXc5I5Xfhw3YXA70T-fG4IvEnpc3RM9mEStTLqVfuHXN17_oEdVcV2IzQFlzHQEfQ0Ggje7zbcgqZN4QRqlCqgXxJqtyJM6a8stPr7YGNGu6jrOmMo5jM_LazYI7x2JdKO8jRc0hs6NpI9DhOf7gN3oklZSzKxmAnaeg5XAa80jWuac7yVPHxRs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضری این پلاکارد را در دست بگیری؟
@Farsna</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/451961" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef0b91dab.mp4?token=dim1lMhdNs7Z4evSoCs9ENYdBWwrZCxqIvL5_qjU_YedfI9hrNx5jtgU97guKoEcQgBnOF8h-dMviKakTQ5Kf04lJ2B0WFtarGksCPHZoh3DmOQuEcnMBMiDa--k_tplbhnS-lqCzkS3pcnxYJgDqJjIdaVhUWUrbXeZLqYKANi_PkNEg4Hgr6_lYNbKLLrDZR0vvKGv25ZT7DtAYEPyQ1dRkItoNIr9kZuGmDe0E16IS975p9lUKiGM9CkBMj8RxSwC4S1qUwaqMP4n_kOhLghXZelPurm7GYBUcHlfgswfPOCjCZfwRs6Qsy_CnuG7E3LF3DDgy6P3lwx-fDBxQKa1H1lbsyepcK1ZdOQUqjao0eiXAsOArF5zV2L1L0dsdYjH3RILaoQvYxbCMIJk583g06pLg8WIpEIbBBVDwcYG1k1zUVkNj0UdjBqisY93sIuAmXxhaXmlHHTeH1sPnIhNNGz8qqtkqv_ZaRfsL1OS1ocQ8jxE8Vd9IIUG7ouwVYrwVdJgD87Gjtzt415brmJhkz50GzAdquFNFDjW1xaxIOlSb9dbDs_OBoRVOtaObbIlsZ1Wvr32DLLlJlbiJsDVOECKh0b2AnFI96PuP-9zWHbMR_qEq2Ers-nA_xzkLkFexLSAgd89sgeqXvLuD6s3jTE5MTeRQWZv_ze7awc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef0b91dab.mp4?token=dim1lMhdNs7Z4evSoCs9ENYdBWwrZCxqIvL5_qjU_YedfI9hrNx5jtgU97guKoEcQgBnOF8h-dMviKakTQ5Kf04lJ2B0WFtarGksCPHZoh3DmOQuEcnMBMiDa--k_tplbhnS-lqCzkS3pcnxYJgDqJjIdaVhUWUrbXeZLqYKANi_PkNEg4Hgr6_lYNbKLLrDZR0vvKGv25ZT7DtAYEPyQ1dRkItoNIr9kZuGmDe0E16IS975p9lUKiGM9CkBMj8RxSwC4S1qUwaqMP4n_kOhLghXZelPurm7GYBUcHlfgswfPOCjCZfwRs6Qsy_CnuG7E3LF3DDgy6P3lwx-fDBxQKa1H1lbsyepcK1ZdOQUqjao0eiXAsOArF5zV2L1L0dsdYjH3RILaoQvYxbCMIJk583g06pLg8WIpEIbBBVDwcYG1k1zUVkNj0UdjBqisY93sIuAmXxhaXmlHHTeH1sPnIhNNGz8qqtkqv_ZaRfsL1OS1ocQ8jxE8Vd9IIUG7ouwVYrwVdJgD87Gjtzt415brmJhkz50GzAdquFNFDjW1xaxIOlSb9dbDs_OBoRVOtaObbIlsZ1Wvr32DLLlJlbiJsDVOECKh0b2AnFI96PuP-9zWHbMR_qEq2Ers-nA_xzkLkFexLSAgd89sgeqXvLuD6s3jTE5MTeRQWZv_ze7awc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک مردم در وداع با جگرگوشه‌های ایران
@Farsna</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/farsna/451960" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmlDkZ_dhicVU4KbEXA3Hej1h_0TLejnL33AtQ_GC7vzWo1iWkqHP7IfF_tI7rMSUdsmVa8ZlXVIz3-nVkSLK5veQROc3XluWCo46RUw834TpB7ZvdNlFjmlsLfQawTqJ3dELB9xEmSlUcQXI9HMiIuN8Tfzh9SzZs0QV2UyKAW24kBh5ft4ytDCViluM_MLTSkMJchbQwY6xT1vD5N_Uup52SXA0f3P_WYNVMjpoDYquezD3NKCOqyJ_Q5XT5KX_zirbjPJCwc5Z5sghytq8zMpa-66mS8_jLL61GcIJhaMapQUFPKwC93HoLNJa-ZsTbHHUEwfQKKHTQUkoJKPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: اگر ما نفت نفروشیم، کسی در منطقه نفت نخواهد فروخت
🔹
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/451959" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fdcd5eb0c.mp4?token=OBeMMaysKIwsCWEr2JnJWmN4u1j356gaaQSKSR4aRz1zmKnKObntNI9woaVo8C_YnZy__GWPGiqpfbU566tZinn9VUpS7okMUDDeHJG39WdZYoIGQpqIRT3EDpY5SNj7Pdl0LPu0dwbHMDK-9UGUieG1D4uOLtgaFqSygaVnsvMpqR5quVlbxJYjjTuXEKIaC_-Ba28AeGrCqZ8u-3WBxBFzUp70W52zP0moJy8X9jirXMcb2_n2INZe4bdnNu-dF18Ph8f15rZ1bmHka__w1ypriKe_mK1CMmbweBvp1_O8PcJFlXhpMTc1PaIw1xPOwlZjIPaPZznbgOnSGk5fMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fdcd5eb0c.mp4?token=OBeMMaysKIwsCWEr2JnJWmN4u1j356gaaQSKSR4aRz1zmKnKObntNI9woaVo8C_YnZy__GWPGiqpfbU566tZinn9VUpS7okMUDDeHJG39WdZYoIGQpqIRT3EDpY5SNj7Pdl0LPu0dwbHMDK-9UGUieG1D4uOLtgaFqSygaVnsvMpqR5quVlbxJYjjTuXEKIaC_-Ba28AeGrCqZ8u-3WBxBFzUp70W52zP0moJy8X9jirXMcb2_n2INZe4bdnNu-dF18Ph8f15rZ1bmHka__w1ypriKe_mK1CMmbweBvp1_O8PcJFlXhpMTc1PaIw1xPOwlZjIPaPZznbgOnSGk5fMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این اهداف آمریکایی هدف حملات ایران قرار گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/451958" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۱.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/451957" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/451957" target="_blank">📅 20:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749211c579.mp4?token=nIkCmpmo6_jePV_ABqvu4J0bEqmj5k8597iKR73TsVm6lj3TjCZM8F39x-Ve4u-YnolrhlWg8T6Sxbh8sueOXrDlOYUO4S-vYMKLJ35VvMaKf3coAjXJcZYAPv_GyDD1oK8ssUf7W80vbI5eGf5p0D8zey8MEWLxJHskZas2ez9MIa22aTV1xPJEJ3hNzLZ1lyutDDUoOprNFsBENAbX5aIB41BBhUCxPnirmW4S5S9aJF7rBXPbXn8v0WcjHUNRvYHeUMFZEcY0rDQ-GvpbImmbiEbUHpL1p7wFo0KpypEP2qbMEonNAXL2WoQBpxpSEbPFrSyCB2E0R5gcdvbRJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749211c579.mp4?token=nIkCmpmo6_jePV_ABqvu4J0bEqmj5k8597iKR73TsVm6lj3TjCZM8F39x-Ve4u-YnolrhlWg8T6Sxbh8sueOXrDlOYUO4S-vYMKLJ35VvMaKf3coAjXJcZYAPv_GyDD1oK8ssUf7W80vbI5eGf5p0D8zey8MEWLxJHskZas2ez9MIa22aTV1xPJEJ3hNzLZ1lyutDDUoOprNFsBENAbX5aIB41BBhUCxPnirmW4S5S9aJF7rBXPbXn8v0WcjHUNRvYHeUMFZEcY0rDQ-GvpbImmbiEbUHpL1p7wFo0KpypEP2qbMEonNAXL2WoQBpxpSEbPFrSyCB2E0R5gcdvbRJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: تلفات دشمن در حملات به اردن و کویت چشم‌گیر بود؛ آمریکا جرئت اعلام تلفات خود را ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/451956" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee193ace1.mp4?token=KLSgUTS0UNAy_YNp6897OHNLG09Eitp9aMI3hjcN6GUlQSHE3F4sakZUf83x4temnSVxqG7RKKeUxc6fhPBSJvryQUDEFII6io4r4pA5Ueh-ITKM7UovUVn36rAQJxIcFOxizC4eP3I3Kke4epDrkVyvhaq0TsXoeEpCR-fImgyzwPW4Gjp5eDYol6pZWwyPX3Yxk-mOQu_QxTwgYZ3ue-WZA9WjTWsfzwE-j6aY355lviyfQXhezgC37Jv28RFV8OVCZqu1-3KlPxV2PLqOkHec9PY5p5hME4WDlB7ePIcdf9ytXCPaV4xA12PJ78qGSAWEnoUuInbhgRDDESFRcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee193ace1.mp4?token=KLSgUTS0UNAy_YNp6897OHNLG09Eitp9aMI3hjcN6GUlQSHE3F4sakZUf83x4temnSVxqG7RKKeUxc6fhPBSJvryQUDEFII6io4r4pA5Ueh-ITKM7UovUVn36rAQJxIcFOxizC4eP3I3Kke4epDrkVyvhaq0TsXoeEpCR-fImgyzwPW4Gjp5eDYol6pZWwyPX3Yxk-mOQu_QxTwgYZ3ue-WZA9WjTWsfzwE-j6aY355lviyfQXhezgC37Jv28RFV8OVCZqu1-3KlPxV2PLqOkHec9PY5p5hME4WDlB7ePIcdf9ytXCPaV4xA12PJ78qGSAWEnoUuInbhgRDDESFRcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: تلفات دشمن در حملات به اردن و کویت چشم‌گیر بود؛ آمریکا جرئت اعلام تلفات خود را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/451955" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f01fb34c9.mp4?token=uvwhg8fDEh9YNhdwtGQVvrZLunYm2JVdUWYjwTFaJXZG7ZPckisVCQQduRyHR3SUmoAhlOX5l4fbBm4zQ2yek_sY5tHxDYwLUd3W9Q-1B31J5iWgxDZ2nbvsD-Ey8T3rRL5F4CJCCQdhfdQi9Kblj2M3AxZZ75sicXT3pBowQtZB_jcLTwPuyLWf6oGzXUTso909cqfn9YqqQdy6nfNm29W7A3QBM5QGqrBhninZXVUHmibjNK7QeUgelQv6uvO92bJK_iv-VYZ2N1ZIad1oxgOsRaefFvyK4lpzukNRf0oVNxtTNoMjCgmqPNDO3pfWMXo-bkAVbAN8RWBSxEEM0XTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f01fb34c9.mp4?token=uvwhg8fDEh9YNhdwtGQVvrZLunYm2JVdUWYjwTFaJXZG7ZPckisVCQQduRyHR3SUmoAhlOX5l4fbBm4zQ2yek_sY5tHxDYwLUd3W9Q-1B31J5iWgxDZ2nbvsD-Ey8T3rRL5F4CJCCQdhfdQi9Kblj2M3AxZZ75sicXT3pBowQtZB_jcLTwPuyLWf6oGzXUTso909cqfn9YqqQdy6nfNm29W7A3QBM5QGqrBhninZXVUHmibjNK7QeUgelQv6uvO92bJK_iv-VYZ2N1ZIad1oxgOsRaefFvyK4lpzukNRf0oVNxtTNoMjCgmqPNDO3pfWMXo-bkAVbAN8RWBSxEEM0XTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار بومی ایران بر سر پایگاه‌های آمریکا فرود آمد
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/451954" target="_blank">📅 20:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1tFojNqsJmxjLlmEegochPGCKzSQLdXOTvqF9TvKNovLmznyh36EUnwaWACZ5eLr1TxzRsTXd0n_7BcSMxkAcXYilHJPkfXr_kih7UACicYmxp_Hqg0hRxh0saW1rXzthYprN78NCShCVyGR6Y-HqNbe0ZwnFeaKuuFTiq8c4U_VkgSYLHGCW7TayjbgmbPhWgkD9eIsJ_il9EbsF6eJRJoQvSDmMEyVzH8ZtH1sJOMFLz3kMaM8zy-5QZPMN-qdtYPEqfiZzyhOhS5LS-PUnQrOyssYG4VCLu03s1EUZCujwsxR0B--pqNLQtyiFnBcl2b2qz5jGNgi0WFTZOkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مورفی، سناتور آمریکایی: ترامپ به‌هیچ‌وجه در دستیابی به توافق هسته‌ای با ایران جدی نیست
🔹
توافق هسته‌ای ترامپ با عربستان برای غنی‌سازی اورانیوم در این کشور موجب به‌راه‌افتادن یک رقابت هسته‌ای در منطقه خواهد شد و انگیزهٔ ایران را برای محدودکردن برنامهٔ هسته‌ای‌اش بیش‌ازپیش کاهش می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/451953" target="_blank">📅 20:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78abbcf8a.mp4?token=R7xnaE5y8kIUCqntoGWOUKWL0LAGaN0G3AaNrgUSomt7djJKkP7-_BR_XmfMuh2KYqv0HTS18rblGWPRAsQyd6Q8stUTFpZnvLpb64ONURrI3P43vNnUZDASUSAegg4xeUjAmlUvHz-b1ks1sdjrY_ccrf3oFydMXg8eWIeL06qTMfckydYXnFbAnOvv3PtkUUmZRO6Y_MRljeRBg8HvYs6GY3vvF-BipIh1WWVyg-_PWX1gy69m-4MewfVtGuFrHj5RXbSpPd_df2s092aDNW599SVsvtnP6_BAji5vrmYTLw3xmylrnpDxpiOZIj86pXAGCAuIQGdsqT59YRop6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78abbcf8a.mp4?token=R7xnaE5y8kIUCqntoGWOUKWL0LAGaN0G3AaNrgUSomt7djJKkP7-_BR_XmfMuh2KYqv0HTS18rblGWPRAsQyd6Q8stUTFpZnvLpb64ONURrI3P43vNnUZDASUSAegg4xeUjAmlUvHz-b1ks1sdjrY_ccrf3oFydMXg8eWIeL06qTMfckydYXnFbAnOvv3PtkUUmZRO6Y_MRljeRBg8HvYs6GY3vvF-BipIh1WWVyg-_PWX1gy69m-4MewfVtGuFrHj5RXbSpPd_df2s092aDNW599SVsvtnP6_BAji5vrmYTLw3xmylrnpDxpiOZIj86pXAGCAuIQGdsqT59YRop6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همهٔ ایران، همدلِ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/451952" target="_blank">📅 20:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7S2Kgs6ZDNUIehYFMG8_LvFg6N2ciFUOAA-CYGBNdmvId4WeKR07FFyuhdyD0DIGV2EFhyUfMI4-6BDkHtvWDKSmrG4u8OQrETX7T7oyWUvF55qCHjwNgdzdvh_110aHsWqobuO2UjYDDBVfIJ_kOTYYYjZ3FU-l8r6Y2gfNsnDKZfFYOJ4DjNu7TiEztj0Bg35OKO_oXLRS3sxyM7MhgVyYNcZu-xjcl2j-bmyFs0gkWuK42eJQhmFuhhcnt9IijMO3g_VGyvphwCuSXqFtBmtH05hzrEKWkmsL3xkOpEwnY_f5XJ9WvZOjfZ_sMhQHH9PO_ACSPNVxVzosqcbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
مجمع عمومی عادی سالیانه با حضور همه سهامداران برگزار شد؛
🔰
مُهر تأیید بر صورت‌های مالی سال ۱۴۰۴ بانک مهر ایران
🔸
مجمع عمومی عادی سالیانه بانک مربوط به سال مالی ۱۴۰۴ با حضور ۱۰۰ درصد نمایندگان سهامداران برگزار شد.
🔸
سال ۱۴۰۴ نخستین سال اجرای برنامه جامع راهبردی بانک مهر ایران به‌عنوان سند چشم‌انداز افق ۱۴۰۶ بود و در این سال دستاوردها و توفیقات گوناگونی حاصل شد از جمله اینکه منابع بانک با رشد ۶۲ درصدی به ۷۰۳ همت رسید.
🔸
گزارش ارائه شده از سوی دکتر «غلامرضا فتحعلی» مدیرعامل بانک مهر ایران در مجمع عمومی حاکی از افزایش تعداد مشتریان به ۲۲ میلیون و ۷۰۰هزار نفر، پرداخت ۵ میلیون و ۳۳۷هزار فقره تسهیلات(بیشترین تعداد در شبکه بانکی کشور) به مبلغ ۵۰۶ همت، افزایش سرمایه به ۲۲ همت و حفظ کفایت سرمایه بانک در سطح مطلوب بالای ۸ درصد است.
🔸
در این جلسه گزارش حسابرس و بازرس قانونی قرائت شد و صورت‌های مالی مربوط به سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ به تصویب مجمع عمومی رسید.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/451950" target="_blank">📅 20:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🎙شرکت نفت سپاهان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjBQ8-aN6iAqSod6gm2E-1dOu7mqATpxEm1dsnyz11AfQlXSO4HhDLtN_QONzV5uRniD6UizdIqdqObsG3KHkX8_Cw4ZKSR6T1yKcBwbEHiXUZ426TeeK7ky7YLI2bDXFMtUOqykdOySsCxuQiio8OgbBg_Ia99WUT6Qfe0B5NvFYNxBQJFJdGhxWyPL_xag_7rKP9eeL0NZ5e1MFJWrgd5SprKUUwwppYxyCPt9deZt1Wdqp-X3VhqBUZ0BC3S1m1hWvRdq_SCy-tYr20oVYhmiKg4avyq1UJ4r4xzbdRT4l8SgJ3sN2rbl5DZKuiFxoHIv1tVA5lV0oI7PYoPVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خبر
📌
در مجمع عمومی عادی سالانه شرکت نفت سپاهان که روز چهارشنبه ۳۱ تیر ماه برگزار شد به ازای هر سهم ۲۰۰ تومان سود نقدی تقسیم شد.
💢
شگفتی سهامداران از رشد ۷۹۴ درصدی نفت سپاهان در بهار ۱۴۰۵
✍
بر اساس این گزارش مجمع عمومی عادی سالیانه شرکت نفت سپاهان (سهامی عام) برای سال مالی منتهی به ۲۹ اسفندماه ۱۴۰۴، روز چهارشنبه ۳۱ تیرماه با حضور حدود ۸۵ درصد از سهامداران در مرکز همایش های بین المللی ایران برگزار شد.
🔗
متن کامل این خبر را از طریق پیوند زیر مطالعه کنید:
👇
https://sepahanoil.com/NewsDetails/3422dd53-9ebe-459a-db6f-08dee7c0a1d1
●•• روابط عمومی شرکت نفت سپاهان
•┈┈••✾❀
🍃
🇮🇷
🍃
❀✾••┈┈•
🌐
www.sepahanoil.com
🔗
t.me/PR_sepahanoil
.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/451949" target="_blank">📅 20:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/451948" target="_blank">📅 20:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47a6f8361.mp4?token=kCwdKjLaNej372zJ-5jmyKXpv_Pn7uDUMkOLp4ioz12e_Xa9owesd6nYFwEqC-BwmUsFJqaftsR_ogFBiRrXnRj9z8A4CnkvWupeALf5UGjzgn3w6tfWYxwFmcqNkSUEB28EoGYxTEkoBHeHXPFEviIY507Z-tBTV_O8rrH19nmvDqn9TXwPUj5vggg5d94U30jK3mnq9PPL6AP3kQ0rb8JJSZykmeOXDCVvnG3fr2rmn7ylDowNHzr4k7hHlUqRKtPlsZ9i4Nw6Dq3FrrXRP-ZBpuwemCwOBLUTYQ3vpyI2muiNvxmYzjnqZ2uqwy055nFwO2WwIjYiSjVtt5baOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47a6f8361.mp4?token=kCwdKjLaNej372zJ-5jmyKXpv_Pn7uDUMkOLp4ioz12e_Xa9owesd6nYFwEqC-BwmUsFJqaftsR_ogFBiRrXnRj9z8A4CnkvWupeALf5UGjzgn3w6tfWYxwFmcqNkSUEB28EoGYxTEkoBHeHXPFEviIY507Z-tBTV_O8rrH19nmvDqn9TXwPUj5vggg5d94U30jK3mnq9PPL6AP3kQ0rb8JJSZykmeOXDCVvnG3fr2rmn7ylDowNHzr4k7hHlUqRKtPlsZ9i4Nw6Dq3FrrXRP-ZBpuwemCwOBLUTYQ3vpyI2muiNvxmYzjnqZ2uqwy055nFwO2WwIjYiSjVtt5baOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرنوشت سربازان آمریکایی؛ عمودی آمدند، افقی برگشتند
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/451947" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNPlEP5tJcXfILZlndIbW7ZwoRTtOU19cPTUGvv7ka2wbfu4FNJ3IDwatwYZIEnQOWd56BETeUaPRlAwUYQKWzBACezajg2RNsc0ZfOqdIUAZbpLHH_kYgzsv_80WKhzeUU0cIU-XIuHr30Q-9ciDHbjCzPYFr2WX-RjwU5XCWQkUoLnzEBXm6vWE8EWj3T-g5UEsaaNN1z7e68KV9Rm3gpcqCxKvLVABY_M_0HHqk2pDsEYYg-1uf8nA0n6sj6oA4Uh7pwepnd1SuNIhtGR11Ws3EQ_JRkmJG7TQ3dY3Z70-E2tcFbB1wrm_HoZihN-pN2-RWDh3fiAVKs18KZB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربانی اپستین از ترس انتقام ترامپ مخفی شده است
🔹
یکی از بستگان زنی که در پروندهٔ جفری اپستین، ترامپ را به تعرض جنسی متهم کرده، می‌گوید او از ترس انتقام ترامپ خود را پنهان کرده است.
🔹
این زن در سال ۲۰۱۹، ۴ بار با مأموران اف‌بی‌آی مصاحبه کرد. او گفت که در دههٔ…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/451946" target="_blank">📅 20:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT1tbbjkc1-Vk-or86OHD999kEIaue0mHl_cfUh7bCr0YdJeas1I7nQ-1Rcu4eXcBm3IpxE0UTaycTpxcpQPYujWlUPBMY5LOBMqCFy0dowqnt1SM5usUhfopgpGsXoZa1NHDjtFYXdLYtFY1rGUgnhbn4o4oFPR5geFkGTgXuGBr8Ny-RyxZ8Qq1CjQHj2HDaiQM2SvieyD-BLjgpNyTECT1AuOAi6vsPBia5Dtx9NYByaXf6ekEic9G9EwhmlHnUHxrcMtcsezZL2E8c7aeWn3N3_UMBAcWwoPZQDht99EBtFFyAgC88NPUJlyhJtG_pNyyLpK2bdrKAGb_sc2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ مصوبهٔ جدید دولتی برای کاهش قیمت گوشت
🔹
دبیر انجمن صنفی واردکنندگان فرآورده‌های خام دامی از ۳ مصوبهٔ جدید دولتی برای کاهش قیمت گوشت خبر داد.
چه اقداماتی تصویب شده؟
🔸
واردات گوشت از استان‌های مرزی بدون نیاز به مبادلهٔ ارز انجام شود.
🔸
ترخیص گوشت تنها با داشتن قبض انبار امکان‌پذیر باشد.
🔸
ترخیص کالا بدون نیاز به مجوز انجمن‌های تخصصی و مجوز شرعی سازمان دامپزشکی انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/451945" target="_blank">📅 20:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNrGVwSCTPe8InMccIW8m9mLfPc4vwgKYcIQ6zZkCjKfRf52RTK5nN8_Mseekaxbq3lixbt7o_afeK9gFkftqLNkav4dKBpdS_D1O_yql7HeoW46td9oCObg6w0cjkyljyz6ktVp_j4Qn-iELkqgZCjEZge3npk_1IXnoffVACAttx3siu_My7P7M-3NY8fxAYNV6YvVsExmPQHHy5JBrhGCt-EXjKP6Klumete3Wwt1UtxtlYNkBUfzzcEQH1rTN-KYCo6bsy6874iZs-HsZL5d04JTT579Xju4iHDIyJh4CvZnU1qIXhDqZoNp-yhGVF-4qXDpD0YEfvNZl-LGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت عادل فردوسی‌پور از دسترس خارج شد
🔹
وب‌سایت «فوتبال ۳۶۰» که زیر نظر عادل فردوسی‌پور فعالیت می‌کند، از ساعاتی پیش از دسترس خارج شده و کاربران امکان ورود به این سایت را ندارند.
🔹
همزمان گزارش‌هایی دربارۀ احتمال فیلتر شدن این رسانه ورزشی منتشر شده، اما تاکنون…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451944" target="_blank">📅 20:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeMSuz4EvNk5nAbb2DxNKumaShczHWQp3kAV0hAN_GaBXml0qOrHnu124112xZxLeaymBUCdWL_wxSUxQAzeLakM4pWhJskxOV4CVpjOnYZw4ZPZ2qpjC34Acozzff-wZHGnavFgwMZZfdRtZkCv_bOk5-fbUVpd4g1hF7nqGiJu0YhtCiqtw98f9jmnyoLn3Qt9MlkpLVQuly7ZtM318xKQ13bsblKp9KkuwZa62F0dbzDFDtX4h6z7cPD0MnHq6vWkOF0EjNWXLpuGGPC3iefvTtLW7I5xV9mN5xcGXm3PKLoJMqTuFpx79y2zDAaY3OKhu2XTM2YwmAH3lw6Qzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارکینگ بزرگ اربعین مهران آمادهٔ پذیرش خودروهای زائران شد
🔹
شهردار مهران: پارکینگ بزرگ اربعین شهرداری مهران پس از تکمیل مراحل آماده‌سازی، تجهیز زیرساخت‌ها و فراهم‌سازی امکانات مورد نیاز، برای پذیرش خودروهای زائران اربعین حسینی بازگشایی و آماده بهره‌برداری شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/451943" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451942">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bdecbfc87.mp4?token=E2E6TECgHHbjBDZa4BGpax4_mZUHC6HnQe_IN2O8d9TQ9hnsDRC16ZPaFGEErOS72R8QDxQEokoGtXevgOsawWpCPMS29Yvj1mtstk8vYJwL64TtDil4IIy9dU-VH8jnTGjCPLHIm7ixDxiBs1Cu1KNoAHYA6sXHQ9u3opPENEcgmZ84XqCnAyHiIxQztv0TP8zyqBU5ACYVEUdoRcboQIvJYgWX5Iw8LmMgqSVf0vPf3LEIdLucv6M0j9Lb5iFGP7uzyRSlMhM2IgE4gXwyxzWm1qzgTO4EFZ5vf1aX4Bh0mLVuqyBy0fUtMkc3OMkWlAu_2Ji1AgWFftFaIFZNQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bdecbfc87.mp4?token=E2E6TECgHHbjBDZa4BGpax4_mZUHC6HnQe_IN2O8d9TQ9hnsDRC16ZPaFGEErOS72R8QDxQEokoGtXevgOsawWpCPMS29Yvj1mtstk8vYJwL64TtDil4IIy9dU-VH8jnTGjCPLHIm7ixDxiBs1Cu1KNoAHYA6sXHQ9u3opPENEcgmZ84XqCnAyHiIxQztv0TP8zyqBU5ACYVEUdoRcboQIvJYgWX5Iw8LmMgqSVf0vPf3LEIdLucv6M0j9Lb5iFGP7uzyRSlMhM2IgE4gXwyxzWm1qzgTO4EFZ5vf1aX4Bh0mLVuqyBy0fUtMkc3OMkWlAu_2Ji1AgWFftFaIFZNQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالگرد ارتش آمریکا دچار آتش‌سوزی شد
🔸
یک فروند هواگرد ترابری نظامی MV-22 Osprey متعلق به ارتش آمریکا در جریان یک تمرین مشترک در فرودگاهی در آریزونا دچار آتش‌سوزی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/451942" target="_blank">📅 19:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451941">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
منابع عربی: مقر تروریست‌های تجزیه‌طلب در اربیل عراق هدف حملۀ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/451941" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451939">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شمال شرق تهران خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451939" target="_blank">📅 19:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnM-TP_wnQdXLg2cscTBMaRlrcVjqFJAIhNkc7Ol7xNTA6v_Tdh_fwEsucOlNCJScyCTBTkcHg787PScmMgo22LozmKHlyRdLBamjeQJRD_1a3YE19dRRNlhpJv85OBJdzyHHU_p0PAf-wwGfx_ghsNS9qRqSBzkCcbDf4OehAzs6zIy84erGueyu6ZukMg8HSbtTlcSFl82PImVh0UTkXKbHbqiwx5Qg13Z7L-6Jsl-7HfD-_wSLyCl4Z_NP9xCqXvMBFV1KrLs1y1WSJLsI5nINgjWl4MhnST1LhhCKnLLVOd0HOsgX5fNmiWxxli-Lbu_CXRwouNpp_zi_kV3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوی خارجی پرسپولیس لغو شد
🔹
شورای برون مرزی وزارت ورزش مجوز لازم برای برگزاری اردوی خارجی پرسپولیس که قرار بود در ترکیه برگزار شود را صادر نکرد و برنامه سفر سرخ‌پوشان در شرایط فعلی لغو شد.
🔹
کادر فنی پرسپولیس تصمیم گرفته تمرینات این تیم را فعلاً در تهران…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/451938" target="_blank">📅 19:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8943c4345a.mp4?token=XuXcpQfvC0kqV-nWPB_Qzwlxr0EPmw5bw0oozYr-VE1g1d-HJ2wXYyzQN9P-k8PRjpN8IJDoXuQ11JjxQVNOiLXk8_1xReH45QFGymo0OU4j0pDkTZVEW2x7cWRR4aCIHzwImUQtC4-B7rjkR9xJy4Lh32drs59cjCT0-6FM3EUX80zVOACMlnirdy21h0x13x5eXsfagZ3ih5rNvfTAThakX3at2N9QPxOoWksGP9uN3h_maJz3hOkqXpocraZvnODMgtxhP8oF7CeRmg5tJmPzSf63mW4dT9GPMD-H4z4sO_lD8gVqCcfl1qNj9XRxcGkPBUkB0KU97kG90Y_fS3G37YjKWWgH1TZTKBE1470OTlC1fmGfvfcYYDZDBjqZVDfmZEWLHadMDiiQ_aSRXULYNELL6swYzMPgnUjaxsUK7L3tUhWVLnYwlWi9JdboBgsS_h1YuiHsNv7P-9RjbeziNK_7OVrMQO63IWyOxWUdCGYArGXUpFdYOaCbE_0bNgb8pWwYmRxvyxuVtyqTZHAH-ub8dpoiYZjPSp3pSkeaSELm2yVA5r-1KykZ6hPXQyoZsHgp3NG8xfeE2mIyhnVs1c77_eTcMR-b3pGnulOU3CFuq_LQhs8580xg0_ZCDd1VA-BlrplC4ebwC-zDv3Y3GgLbbWmsqk4jv9SBWX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8943c4345a.mp4?token=XuXcpQfvC0kqV-nWPB_Qzwlxr0EPmw5bw0oozYr-VE1g1d-HJ2wXYyzQN9P-k8PRjpN8IJDoXuQ11JjxQVNOiLXk8_1xReH45QFGymo0OU4j0pDkTZVEW2x7cWRR4aCIHzwImUQtC4-B7rjkR9xJy4Lh32drs59cjCT0-6FM3EUX80zVOACMlnirdy21h0x13x5eXsfagZ3ih5rNvfTAThakX3at2N9QPxOoWksGP9uN3h_maJz3hOkqXpocraZvnODMgtxhP8oF7CeRmg5tJmPzSf63mW4dT9GPMD-H4z4sO_lD8gVqCcfl1qNj9XRxcGkPBUkB0KU97kG90Y_fS3G37YjKWWgH1TZTKBE1470OTlC1fmGfvfcYYDZDBjqZVDfmZEWLHadMDiiQ_aSRXULYNELL6swYzMPgnUjaxsUK7L3tUhWVLnYwlWi9JdboBgsS_h1YuiHsNv7P-9RjbeziNK_7OVrMQO63IWyOxWUdCGYArGXUpFdYOaCbE_0bNgb8pWwYmRxvyxuVtyqTZHAH-ub8dpoiYZjPSp3pSkeaSELm2yVA5r-1KykZ6hPXQyoZsHgp3NG8xfeE2mIyhnVs1c77_eTcMR-b3pGnulOU3CFuq_LQhs8580xg0_ZCDd1VA-BlrplC4ebwC-zDv3Y3GgLbbWmsqk4jv9SBWX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مامانی ۵ ماه دوریتو کشیدم
🔸
مادر شهید امیر علی کمالی از شهدای میناب، امروز بخش دیگری از پیکر فرزند کودکش را به آغوش خاک سپرد‌. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/451937" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451936">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">چین هم از محاصرهٔ دریایی یمن مستثنی نماند
🔹
ردیابی مسیر کشتی‌ها نشان می‌دهد یک کشتی خودروبر متعلق به شرکت چینی «کاسکو شیپینگ» نخستین شناوری بوده که پس از دریافت هشدار نیروهای مسلح یمن، از ادامه مسیر در تنگه باب‌المندب منصرف شده و تغییر مسیر داده است.
🔹
همچنین…</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/451936" target="_blank">📅 18:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451935">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajs1QBBmjHsUvDrya_b8IrllCfeIeEP2VQ3AkDC48bpWpmyCZ9-OXAg-LItr5f-1SBBbFJNeAuaYMZLMFcWhnAQumajDj6TlJRRjXKIkjTK-R1uRDWFzOj4E_bFC9ROkxc1HE8XNGdoBkaZ7ifgH_TY-CqVavurfXVpC02u4bNzqUh6EwKb21ifBJdTNiduakfnmV4KK8EeMy5yTGSIuEyxtuOORbY_-ZBQGoJfzZz9w9iPRATljMVBg8Lex_dKYxz32IDgvrt9krmBjCqhYh482KviLfnsp4U7xV_BkBgf9NfuQvoA5VUcUVhIeAefIPDup4QH4nKgEksQH3xtOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت ۱۴ ماه نقش‌آفرینی بانک صنعت و معدن در توسعه‌‌ی‌کشور
بانک صنعت و معدن در دوره ۱۴ ماهه منتهی به پایان اردیبهشت ۱۴۰۵،  با رشد شاخص‌های کلیدی عملکردی، مسیر حمایت از تولید، توسعه تأمین مالی، تجهیز منابع، گسترش ابزارهای اعتباری و پشتیبانی از اقتصاد دانش‌بنیان را با جدیت دنبال کرده است.
این اینفوگرافیک، مروری بر مهم‌ترین دستاوردهای این دوره و روایتی فشرده از عملکرد این بانک در مسیر نقش‌آفرینی برای توسعه کشور است.</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/451935" target="_blank">📅 18:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoPX4CffV3eGVnd424oZqSU2T9QQqfIRNRAlmpdnWmnQlchrCIaS-PT7haip1lrfLY3aoyaavYSZZEWWr4scGRx0jkuHETL4ZKJgTxhdR_w9R4QCMSCfDxdWYyYhTarpr0G2WeaaN79Afe2siOxTxPBG6oeKujOn0US8ab0iAeT7Rna1KRx4Eltwekln-PmUXlWbQloVRp5pxXa_dinkcBi1rC2Q81hH0kKk78iQsz4rfan3pPQfI2D-WYJJMQ-JGIzi-8D-xsnDA7letic8bWKZY9iYOuLuKE1fF5muRT867Mi6uYJgXIOyu3dIDU1IfFS2yuvfrfEZl7MfKzRNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان خرید ارز اربعین ۱۴۰۵ در اپلیکیشن بله
خرید ارز اربعین یکی از خدمات مهمی است که زائران سال‌ها در اپلیکیشن بله دریافت کرده‌اند. در اربعین سال ۱۴۰۴، بیش از ۹۵ درصد زائران ارز خود را از طریق بله تهیه کردند و امسال نیز این خدمت با هدف کاهش مراجعه حضوری و تسهیل فرایند دریافت ارز در اختیار کاربران قرار گرفته است.
زائران می‌توانند به‌صورت آنلاین و بدون معطلی، تا سقف ۲۰۰ هزار دینار عراق ارز اربعین خریداری کنند.
به صفحه خدمات در اپلیکیشن بله مراجعه کنید و ارز اربعین را تهیه کنید.</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/451934" target="_blank">📅 18:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/451933" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-9i2CYyQ_2lABY03BIkZgYX97PhC_E-TUYlbYoR9OlkBtqdwzEkZEJY0Ev1P3uIX_hB67MRnhcTzF2nLu5kzYlfXhxTFRvpZuQYLkdavPkmHz_SiKvq0PAsOAgj-pSmwjieWnzagExs6OvuVgW0ZdqegHdH0WMtukrHW27VW9M2LSV_319nIGtcc_oExplUC0HS_LxxrAsWO-0vSRF7WRGY-bMLq25Tpvaxb8G-b0pCRNOkX-cjlAUNL85fuPAAYahSSgAAkQrvTJEjOl5uZ52zjV-nyPXgkc1GjbIMpFHxluAzgDZiEcq6BVULS08zhqI2SRnyNUwgrCjhs5-tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX1vymeQVuaEWv1mS86WYHxl2tzOQviI_0jBKdpGMYqFfkU3e7Y8L82OcYf_vh3xdBuwVYMdkZ3RyXzvSa_xImnyQtSMTHw-kFyOjp0e1XdZk0c0w1Jg9skxmC31TlxCBksRgNJtuwief_5Ycmp0z47h26OL6MvNP4gqnamfgw2QeoWeQU2lWsBlh-Witgg8fDisNLKSG1lp0wFucAvP0HhZ6yrWdD_Y22W00WUq_ZqWDruLXC_vG6Dx5Xtq4MPsUAAURVXGAYJF26FR0U-knp2ljmgUkLen8KNq2hQJGb_ejsKA-ntpTZMkzXE5x3CIMsJzN-oo5a3O8YmULbONJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFyG8o1XxUdkdZ2wz5XCM0r6Jey_JazUnEhTVa_A8aqzW3gLOIRmgvemXkMJ6qfBv6gv6D3h7VvyzseVxL-tjuTt3FGP3bcWlz8OvwGQEpQpQ0spzyAi-L2B0qwXVUDcpbuqclkRtqQDncVJr--P0_UVoOn1uTv9zQ3fNT4GfiRRbgClvnjxlLIWz642R4r94EUModhtwjOSGhuVj3KGRIVJtnlIJDI1clU76FkZ93hF_gIWb6nZmvbMOnL8yBr7AfmJd0B9VXPHwbQxrE2uSokoNQovX_RoXhryE3eDLs1E35P-19o_V0IjtK22K1HI9JvNU3MoaEne87DCzsDGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPz3rJF9SN3hsNjyd87LIvNoFtI_yZsPzdiR99kpqQfcsH6FR9ed2L12ycEZITS77iPI4zczt6tPs2DRbXP6Ed_OFmOrHVs-xb2HWql9H8VrBd5_5HbRAGWFRnto_T2m9V1zRsZMhmKlR0FLvw3afEwi70QPf_yYYWb4Q04-F7SS1fA3bxrAuK1M-talXx0tffN0NWB1qIq3qDTxs2YnDiP1q5KszGt40UQR2s40oYn1dznRRyEqMnhifS75T5oyFEBQS0iuWideU9vFs9aufctG4bgonrSIy8ivW4ctfWRrSA6vpTdq0lmnMByACSgikWJQ61y1j2cogdqGqxudhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfFTRoaaMCX0EnLXDhobFm092G_JWxQjbPcvXFwBeSN3z5LB6NbVs7STcpyYUKAfstcP8P6qyxC6cSlg31kdl6sv6rUXE23kIzM6oQq4KgtrmwcLVhhlARnAZmQSnMMHJi7YIvvDIg6hLFVO9iQV1uCWZZP1Wc2O_X3IO8p4UuPE5tFSTlkKKEvr1SXldLhK9VLrnItcK_XVCT53vGvRr5TO9ss-JhXyK04kaAUlBsIMJ4AW0PYNXBUjZ61KoZdrmpHMjEmaLU8uFutw50UG8sBnZ51hIquhLlSXbd1gIqlMMzhtJ_bCiWkMXdw7V4dnausaqzyyF_2vwTn6Xezlfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDHH7FTEED4StdjF5VB6ujfNrPPELBPXTWR-vfy4TYfrFFej6tAD0u6PyZB-Fvetvg685XmjKGM-ved59wUfebigHsfzVOpPk8kIb-03NJgAZINQEyoAa5Q8ZRbbm_A3EGom2dDyr5DaoM7Zy5O7X7yWglZIvhs6uU1KwZ19s1p1rl4kSatmNRlgrDoOhHlg9PvCVokabrz4eG64mTNAOhmQ5CjqRQ7rZKI8pdNxcpkA3DWEG23SRKHapqXORSaR5-eGpciKuFaX_h1uforJpo7-wQRCKqmBeLP7XiGg4PCjcp0ZV4ketK0AA_xdbApbYUZWSpQ8qMkxjyoqMydGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRCnJ-RY-A2sl-lTrSP9T8vjqoPLxhIOwk8lawx9IqhHZShModtdd9uEtXHRW59YixNaRDrCMw43SCmzDVVKig8fD3D2L0KMpAwmhoG2ox--hl-m-PIlvmOvpPs1TmdNv-_zySXwfFpiHRVaBUlq7o-4tR2DDG0Pfz4ZcISOj0oHa4JRQY7YimrOODzVqMhM9Y7ZhcyZFUNu9sV15aDhetxxanywqXh0LtqADP14eXSBr3-j7b8XCuQkM-UsvszvL6QPFbkfdYtDudJAZrwtX4mQkMjCZlydGZQG1t67uZEHmg_UXJUEYCq4FmHc6-mKu-K3DkhFrBR96zVzcpBnQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رصد ماه در حرم حضرت شاه‌عبدالعظیم(ع)
🔹
شامگاه سه‌شنبه مرکز نجوم آستان حضرت عبدالعظیم(ع) برنامه رصد ماه با تلسکوپ را برای عموم زائرین برگزار کرد.
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/451926" target="_blank">📅 18:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxrhsggMckuUcw2JSzkioVDGPZ1cIb1KvIswnW4cswKGrEZJAI7T8BMEH6CuviZHQ2Yn8nHgO_jLbxutdCjgVd-UYLcDt8UxZ899i6YaCMPHAZvSYj3vJGoty6XOtfvfwW6XWE2PpiolgM4zpGh284TLPy9XTiO5TpJ_gh9re3rjoRGWovITTwDtDDn4B5KXqkPCacIr7MLdfHp8CbnEestdAuZ5waZ6se_CHiU2cgfi1AbMzDRjOnuGIYkArYmYisVuYhQezD2KbkAhAtEBH44bMUrs1L-_YjXnwYUTuUc1PwaWhq9HldbIVXcS6Mv8k10ZfMxL2cz4cEx4IWjb2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش‌مصنوعی در آزمایشگاه از کنترل خارج شد
🔹
رویترز: اپن‌ای‌آی اعلام کرد یکی از عامل‌های هوش مصنوعی این شرکت در جریان یک آزمایش امنیتی از محیط ایزوله خارج شد، به اینترنت دسترسی پیدا کرد و زیرساخت‌های پلتفرم «هاگینگ فیس» را هدف قرار داد؛ رخدادی که این شرکت آن را «بی‌سابقه» توصیف کرده است.
🔹
اپن‌ای‌آی در یک پست وبلاگی توضیح داد این عامل هوش مصنوعی برای ارزیابی توانایی‌های سایبری مدل‌های پیشرفته در یک محیط کنترل‌شده در حال آزمایش بود، اما موفق شد محدودیت‌های محیط ایزوله را دور بزند، به اینترنت متصل شود و برای انجام مأموریت تعریف‌شده خود به سامانه‌های هاگینگ فیس نفوذ کند.
🔹
هاگینگ فیس، که یکی از مهم‌ترین بسترهای میزبانی مدل‌ها و مجموعه‌داده‌های متن‌باز هوش مصنوعی به شمار می‌رود، هفته گذشته از حمله‌ای خبر داده بود که به گفته این شرکت، از ابتدا تا انتها توسط یک «عامل هوش مصنوعی خودمختار» انجام شده و با حملات پیشین تفاوت داشته است.
🔹
کلمان دلانگ، هم‌بنیان‌گذار هاگینگ فیس، پس از افشای این موضوع اعلام کرد این شرکت از ابتدا احتمال می‌داد حمله توسط یکی از آزمایشگاه‌های پیشرفته هوش مصنوعی انجام شده باشد و خودکار بودن کامل این عملیات را «شگفت‌انگیز» توصیف کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/451925" target="_blank">📅 18:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451924">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c667af1999.mp4?token=sL9T6P4yjv0Wkf_N2AdQVp4PLUCC_0dp_gEhXNGHEkmH1N8hosKQ8rbjLp_6rDRi0C00eyyx2MpoM_0BKaIOXfFZHFuFRbV_aP76KL1cxelPTLLcCCi4v5G4M9Q8Je5lgbfMvma0xndg_pWsK1jQthy-KHizVVkDFEdTNZM0df4awAXpJTvtS0DPxxAY30GBctjZ3fhQc5lFtQUgHrLl1CdesGO9pgxV5yMKgcbLwt0Fto5_7b2uiZA55TZTRGL_X1xy5n_3jkNAlYP9oFa5BJj2aqhE8KeXJH7aU_L_tlepOw3DK53ST87Dgv6DqTbIftVoTcaJforWsk1lMVVvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c667af1999.mp4?token=sL9T6P4yjv0Wkf_N2AdQVp4PLUCC_0dp_gEhXNGHEkmH1N8hosKQ8rbjLp_6rDRi0C00eyyx2MpoM_0BKaIOXfFZHFuFRbV_aP76KL1cxelPTLLcCCi4v5G4M9Q8Je5lgbfMvma0xndg_pWsK1jQthy-KHizVVkDFEdTNZM0df4awAXpJTvtS0DPxxAY30GBctjZ3fhQc5lFtQUgHrLl1CdesGO9pgxV5yMKgcbLwt0Fto5_7b2uiZA55TZTRGL_X1xy5n_3jkNAlYP9oFa5BJj2aqhE8KeXJH7aU_L_tlepOw3DK53ST87Dgv6DqTbIftVoTcaJforWsk1lMVVvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران اسلامی منطقۀ خلیج فارس را ایمن خواهد کرد
@Farasna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/451924" target="_blank">📅 18:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451923">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c2e067db.mp4?token=O61dkBlSl1PuOwUQHNRsdrjzJsAkFtKIDPEsCcLBd60kwSfOp12YIaFhelgF138mkT1F0BjBIrtxV5zgLMBTAj5ApMggNb9qLJ2zYi11MCfCGRRy-tLR0Fhsgn51m3fqeen_C3eCqYRsxOVzvrsZCkb9Q10TQbF7HGOLQ_2kGOPMFyPPYEQNNE5KvfLJid6LHaQb9-BT_n2PkLa9bLSeFIUT0ZCdNe6wUfLrjQxCmjQxj_BPCej1hy7A2O1IEuADsf9x339fr7DRGLRKFwCcIKWCINT-ytOS3TYFNmW1RbIPEAF61aA6m5ikaJcOSNNCNk4MNWtPa_JM39tkEg3NKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c2e067db.mp4?token=O61dkBlSl1PuOwUQHNRsdrjzJsAkFtKIDPEsCcLBd60kwSfOp12YIaFhelgF138mkT1F0BjBIrtxV5zgLMBTAj5ApMggNb9qLJ2zYi11MCfCGRRy-tLR0Fhsgn51m3fqeen_C3eCqYRsxOVzvrsZCkb9Q10TQbF7HGOLQ_2kGOPMFyPPYEQNNE5KvfLJid6LHaQb9-BT_n2PkLa9bLSeFIUT0ZCdNe6wUfLrjQxCmjQxj_BPCej1hy7A2O1IEuADsf9x339fr7DRGLRKFwCcIKWCINT-ytOS3TYFNmW1RbIPEAF61aA6m5ikaJcOSNNCNk4MNWtPa_JM39tkEg3NKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار‌هایی درباره جنگ و ازدواج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/451923" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451922">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از دوران مبارزات امام حسن مجتبی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/451922" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa912f51f.mp4?token=ZTRCa62qmUVr8PaeZ-JVrh7YJEgMWD4O7kBWtxJXz5Lh1DMeXEF2kE9URn0eLJ-efbDNk7MMCsv4kPsxD_it0B8d0-SZRhxD1Fw3LV7e_1kTzTSxhJuFkUexQug2LM_K2c1xbyHiv6iQKbSGtxYyx2BrRfncnFRbVhBoiizj867jHBPBhAZqDw3ijL_e899ra9HBNFHl71YtPiUNL91wNV96w98CCFqJIzr3_sDEwTB0YJBcwta31Jz6xb0VRlBBEz9273xlgSbAqoMvYWnXmwXMXysJqTJiJqfTquBtMtd8iAcML4rJCl8DDo8rwBnkXtmsPhaJ5ipqkFbKn0DLzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa912f51f.mp4?token=ZTRCa62qmUVr8PaeZ-JVrh7YJEgMWD4O7kBWtxJXz5Lh1DMeXEF2kE9URn0eLJ-efbDNk7MMCsv4kPsxD_it0B8d0-SZRhxD1Fw3LV7e_1kTzTSxhJuFkUexQug2LM_K2c1xbyHiv6iQKbSGtxYyx2BrRfncnFRbVhBoiizj867jHBPBhAZqDw3ijL_e899ra9HBNFHl71YtPiUNL91wNV96w98CCFqJIzr3_sDEwTB0YJBcwta31Jz6xb0VRlBBEz9273xlgSbAqoMvYWnXmwXMXysJqTJiJqfTquBtMtd8iAcML4rJCl8DDo8rwBnkXtmsPhaJ5ipqkFbKn0DLzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آمریکایی‌ها مخالف جنگ نیستند اما قیمت بالای بنزین را نمی‌خواهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451921" target="_blank">📅 18:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451920">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c390169b87.mp4?token=Bs976G1Fphr8lg6WSQYp5tdxqEc5bSBd9miTecrBS_PmQ0x4rWbV7oe-mJCVxBNDWdje6iZi6yOAjhGrJloSCHNWmAsLTj18HC_FBVM5cIsyLyoXJgNCSYaR1he1LrJduj6lKm1XWVBwwG6Rx_ob-HSQlY3iHROI9jUyO3DAb5q4AkH4AxQC9d0wRcVmrcwADS2L3JVNcMjjrqKA6pH4QmHSTIaCBLcSvgJvCAYqEdtOXPG067QiXaiYO_jR1kbHG60UR8TcltJyU-GTKLgJ1GpEzLAKaOLLHtw8D2qZArn0cNIZ3OG1WxFuDKdtFM6DGQKGIM3GFKiY1i2v64lgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c390169b87.mp4?token=Bs976G1Fphr8lg6WSQYp5tdxqEc5bSBd9miTecrBS_PmQ0x4rWbV7oe-mJCVxBNDWdje6iZi6yOAjhGrJloSCHNWmAsLTj18HC_FBVM5cIsyLyoXJgNCSYaR1he1LrJduj6lKm1XWVBwwG6Rx_ob-HSQlY3iHROI9jUyO3DAb5q4AkH4AxQC9d0wRcVmrcwADS2L3JVNcMjjrqKA6pH4QmHSTIaCBLcSvgJvCAYqEdtOXPG067QiXaiYO_jR1kbHG60UR8TcltJyU-GTKLgJ1GpEzLAKaOLLHtw8D2qZArn0cNIZ3OG1WxFuDKdtFM6DGQKGIM3GFKiY1i2v64lgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فاطمه امینی (مجری تلویزیون) از حملهٔ موشکی در پخش زنده برنامهٔ کودک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451920" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451919">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جزئیات یک‌طرفه شدن جاده‌های شمال در روز جمعه
🔹
تردد از ابتدای آزادراه تهران-شمال به سمت چالوس از ساعت ۱۴ ممنوع بوده و از ساعت ۱۵ نیز مسیر پل زنگوله به سمت چالوس مسدود می‌شود.
🔹
از ساعت ۱۶ تا ۲۴ مسیر شمال به جنوب مرزن‌آباد به سمت تهران به‌صورت یک‌طرفه در می‌آید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/451919" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451918">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d6d6eef1.mp4?token=ppF7pxSDUvr5RtGIe1aX6CWbCevk4zvoBj7FJJh7tZW_haGPQ13Ur5_PWAc0jYhk6DPPsLjVleRybwzYAdH3MObrrgdjLRIJv_dM8ckJVemyf83RxHSlQ-m0P3yuKzD8BKYKNnWkyRYvkn9SRTShJojVRaK_AuHRRJklHApELNgbkk2hMaWWnLxWzmBK4ZcGU2qEfuhQUAluE07p3vxx1hUDbbdZ53ko1lCY_TLMnAlBE_MVfOCGHTL3ejUMjn8ZFOCRR8zchoSE51dWQocoPQYzwKPLqbxAgvbg7I1-ZwjgAGbEKfvLsT9p74EkKPaVxpRrqaLUWKSD95mGAM6CHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d6d6eef1.mp4?token=ppF7pxSDUvr5RtGIe1aX6CWbCevk4zvoBj7FJJh7tZW_haGPQ13Ur5_PWAc0jYhk6DPPsLjVleRybwzYAdH3MObrrgdjLRIJv_dM8ckJVemyf83RxHSlQ-m0P3yuKzD8BKYKNnWkyRYvkn9SRTShJojVRaK_AuHRRJklHApELNgbkk2hMaWWnLxWzmBK4ZcGU2qEfuhQUAluE07p3vxx1hUDbbdZ53ko1lCY_TLMnAlBE_MVfOCGHTL3ejUMjn8ZFOCRR8zchoSE51dWQocoPQYzwKPLqbxAgvbg7I1-ZwjgAGbEKfvLsT9p74EkKPaVxpRrqaLUWKSD95mGAM6CHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آمریکایی‌ها مخالف جنگ نیستند اما قیمت بالای بنزین را نمی‌خواهند.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451918" target="_blank">📅 17:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451917">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH7bTf60m_HvdY2bSZrKBBj5-c9fDRC-VVtzizTrHL1vi4szgmAE0OZCA0BrI6K5yEFOuuYMrxWreho2ZWmILLopReOhjUO-lKdPdh-hL4Zxn9ZBWEoCbqLMGXE9ER8Cv6lNKZWmEwCOA5x7s1hdKU6FVqBlOfFImrSFLVO79pVqoVWEov7wSGH0xtSqhk1wpzvueb1g_JrkZcLguqzlV0eYzjPvYFAeF_zXWMFk0tjTcCC8-UZ4Rw2r-ePB0NMNuGDXn4EMXpNBqmSU8-ndlU29YGP0e7FmcKu6Xc-otjVheYaoOAnlJaLWz0-CmfSm-LVxUVXBaB5-E1UqFpDFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
انتشار ارزیابی رگولاتوری ارتباطات از مراسم تشییع رهبر شهید؛ تمرکز ایرانسل بر مسئولیت ارتباطی جواب داد
🔸
رگولاتوری ارتباطات با انتشار گزارشی، عملکرد شبکه ارتباطی کشور در مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی را تشریح کرد. بر اساس این گزارش، ایرانسل موفق شده است در محدوده مصلی و مسیرهای تشییع تهران، رکوردهای قابل توجهی را در زمینه سرعت دسترسی کاربران به اینترنت ثبت کند.
🔸
بر اساس این گزارش و ارزیابی‌های انجام شده، مشترکان ایرانسل در ۹۵.۱۳ درصد از مسیرهای این مراسم، سرعتی بیش از ۵ مگابیت بر ثانیه را تجربه کرده‌اند.
🔸
نتایج اندازه‌گیری‌های انجام‌شده توسط رگولاتوری در محدوده مصلای تهران، نشان می‌دهد متوسط سرعت نسل چهارم ایرانسل ۱۹.۳۸ مگابیت بر ثانیه و متوسط سرعت نسل پنجم ایرانسل ۱۶۱.۸۵ مگابیت بر ثانیه بوده است.
🔸
در مسیرهای تشییع تهران نیز متوسط سرعت نسل چهارم ایرانسل ۱۵.۲۴ مگابیت بر ثانیه و متوسط سرعت نسل پنجم ایرانسل ۱۷۱.۱۹ مگابیت بر ثانیه ثبت شده که بیانگر عملکرد مطلوب شبکه در شرایط پرترافیک است.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451917" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOeMoqyb_NhlddS7qmVY3kL7gWyh0RcHu27YqYOaDAOFcCf2bvSDe8mbiV1YtjuLAGfaUnU-JIGKwdQoHrP2w4Dqul7gaGpRNKcFBWNGc5MWJN6WEiFLSFyNuIJ_WR-mldXJa5BjKrNOyNfflp-Shx79A5T3fVrNcgr-bQbXgCYINgym1VGvS0TN2UTWR2Og7964MmJ4AmB94aiS3nGSVtSP58IMCe6jhIG0Gcz5SyWYyhb7anonSRUPNhffJ4b0sdbkqR8OdpcPQeYbqV1dFJcufG-Hdjj2J8IJ7OXPU8Leae6mS0gmAqom1WTdbo0sgJCHd-sgeprwSrpkVEIR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گام های اثربخش بانک رفاه کارگران در حمایت از نظام آموزش عالی
🔹️
بانک رفاه کارگران با هدف حمایت از فعالیت‌های آموزشی و پژوهشی دانشگاه شهید بهشتی با این دانشگاه تفاهم‌نامه همکاری امضاء کرد.
🔹️
این تفاهم‌نامه به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران و دکتر آقامیری رئیس دانشگاه رسید.
🔹️
دکتر للـه‌گانی هدف از امضای این تفاهم‌نامه را پشتیبانی از برنامه‌های توسعه‌ای این دانشگاه برشمرد و گفت: بانک رفاه کارگران به عنوان بزرگ‌ترین بانک اجتماعی کشور در سال‌های اخیر اقدامات قابل توجهی در راستای حمایت از نظام آموزش عالی کشور داشته و با استفاده از ابزارها و محصولات نوین بانکی، گام‌های اثربخشی در مسیر حمایت از دانشگاه‌ها و تامین مالی طرح‌های اجرایی آنها برداشته است.
🔹️
دکتر آقا میری رئیس دانشگاه شهید بهشتی نیز با قدردانی از حمایت‌های بانک رفاه کارگران از این دانشگاه گفت: امضای این تفاهم‌نامه نقطه‌عطفی در مسیر همکاری‌های مشترک این دانشگاه و بانک محسوب می‌شود و می‌تواند بستر توسعه خدمات آموزشی و پژوهشی دانشگاه را فراهم کند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/451916" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/451915" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451914">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e557418c.mp4?token=kJBkkf7FrhStjf8rXiQ9INcP0CqSIx9q0rXhZni3iWD688Q4WVemP0UObIeZZkBZIUvXV2c4VAOqzoGrOegnLx8oVZnmaqc-tgInFxaD7lLkD5eCKMqkIo92zJT53EWC818uY1gSLQHIPefWcy17er8nBpH0IJ91c4xTwYsQzL0by6pUBB2AGxKcVcpD5njJmphWI-_zuwXW7M6TpVRaDmN5Mp4P56JOVs0D1K4RU8shu7KwwQZEC4B9aUSG6ag0o2DrOZqE0BpxRv7nwBQaXZvdKk22ATDCWBYPLGLE3GfxSJLjDF0mR2eMogsIJVVlNnKZ3OLT5gpa9z9U04rnTgEYOWmIEWWPpVkou5By6dSBJymte_NV577yVyGEH3RHgkMqffnP2f3bz5p3cGrVSnFIJCNwJj3KR-NkEAfmA8yBoCO9DT5mf3LYO9QnX6x4BI-IxbZ9G0MlMSBb3vvkB4dBj1jmk8nzOFzIS_dktNbJJwJJDE0Yd0eOtWsrmi-zdcZRuA6jOYu95iaNLuZ4F28EZKF9yi1xjZHEk62HvcB0v9zbTulAgZ-EVg-8JKrjr8aQjZ233tM3X3EvE2tNuEUnH6PbUXwbcwquvCMYu36F7HDjZ-V3P_f1wO28OHnLXjdSFgXptek_cmom-nxQC9VJSMqjXblZc8UVlW_t4no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e557418c.mp4?token=kJBkkf7FrhStjf8rXiQ9INcP0CqSIx9q0rXhZni3iWD688Q4WVemP0UObIeZZkBZIUvXV2c4VAOqzoGrOegnLx8oVZnmaqc-tgInFxaD7lLkD5eCKMqkIo92zJT53EWC818uY1gSLQHIPefWcy17er8nBpH0IJ91c4xTwYsQzL0by6pUBB2AGxKcVcpD5njJmphWI-_zuwXW7M6TpVRaDmN5Mp4P56JOVs0D1K4RU8shu7KwwQZEC4B9aUSG6ag0o2DrOZqE0BpxRv7nwBQaXZvdKk22ATDCWBYPLGLE3GfxSJLjDF0mR2eMogsIJVVlNnKZ3OLT5gpa9z9U04rnTgEYOWmIEWWPpVkou5By6dSBJymte_NV577yVyGEH3RHgkMqffnP2f3bz5p3cGrVSnFIJCNwJj3KR-NkEAfmA8yBoCO9DT5mf3LYO9QnX6x4BI-IxbZ9G0MlMSBb3vvkB4dBj1jmk8nzOFzIS_dktNbJJwJJDE0Yd0eOtWsrmi-zdcZRuA6jOYu95iaNLuZ4F28EZKF9yi1xjZHEk62HvcB0v9zbTulAgZ-EVg-8JKrjr8aQjZ233tM3X3EvE2tNuEUnH6PbUXwbcwquvCMYu36F7HDjZ-V3P_f1wO28OHnLXjdSFgXptek_cmom-nxQC9VJSMqjXblZc8UVlW_t4no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زودباوری رضا پهلوی باز هم کار دستش داد
🔹
رضا پهلوی در مصاحبه با رویترز، ارتباطش با نیروهای بسیج و سپاه که پیش از این بارها ادعا کرده بود با این نیروها در تماس است را انکار کرده و ادعاهای قبلی خود را پس گرفته است.
🔹
پهلوی در این بخش گفته: «مدتی بود که در شبکه‌های اجتماعی پیام‌های مستقیمی از افرادی دریافت می‌کردم که می‌گفتند من یک بسیجی هستم، اما در قلبم با شما هستم، من عضو سپاه پاسداران هستم، از این حکومت متنفرم، با آن‌ها نیستم و فقط دنبال فرصتی هستیم که از آن جدا شویم و از این قبیل حرف‌ها.
🔹
وقتی به رسانه‌ها گفتم که با چنین افرادی در ارتباط هستم، منظورم همین نوع ارتباط‌ها بود؛ نه اینکه واقعاً با فرماندهان سپاه صحبت کرده باشم، اصلاً چنین چیزی نبود».
🔹
گفتنی است که حدود ۷ سال پیش، رضا پهلوی در گفت‌وگویی با شبکه اینترنشنال، ادعا کرده بود که با نیروهای ارتش، سپاه و بسیج در ارتباط است؛ البته هر بار که رضا پهلوی چنین ادعاهایی کرده، بلافاصله مورد تمسخر کاربران ایرانی در شبکه‌های اجتماعی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451914" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451913">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da88c1da.mp4?token=enPYZiza0HA6xrR7fFRlKzT4mrPoU5shmxbIMoeBwgMesEkp4ZSquBA3ldZafDsFyw9TZYEkh-oOGhNyAyGspowEVv2T1MgdQLBtOR5xhoxgobwDux9WLhseICkQm0DnRC4ezqysB0nmmWbbX0Uy62qI1Lm5P5gSjXBt5Wnsx6u7vFkoB92h1_SuOEAuex5mcrftYWcn9uyrW2CHdsL_nu_2CxTxmnVZKyTqmXxVfuA_2Ckh_-DWeUfnbuxzxyn_YkmdvyS4O1y9up0cokmDu4jqkf9exQLevDw0S5O_-hosMR6wEqUECH_CNyW1dC0sORFeqjFKEKpwi2VzIGXYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da88c1da.mp4?token=enPYZiza0HA6xrR7fFRlKzT4mrPoU5shmxbIMoeBwgMesEkp4ZSquBA3ldZafDsFyw9TZYEkh-oOGhNyAyGspowEVv2T1MgdQLBtOR5xhoxgobwDux9WLhseICkQm0DnRC4ezqysB0nmmWbbX0Uy62qI1Lm5P5gSjXBt5Wnsx6u7vFkoB92h1_SuOEAuex5mcrftYWcn9uyrW2CHdsL_nu_2CxTxmnVZKyTqmXxVfuA_2Ckh_-DWeUfnbuxzxyn_YkmdvyS4O1y9up0cokmDu4jqkf9exQLevDw0S5O_-hosMR6wEqUECH_CNyW1dC0sORFeqjFKEKpwi2VzIGXYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردهٔ طرح جدید آمریکا
چیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451913" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451912">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664d0747c0.mp4?token=rux5GTCl0o0e2CBA_99Oykgu12jA7NCGwRH_z51qZKEY4lj0CpMVFKFI7LzlBjk45nqLbvpmEtrNYZdDE_NP-_r4MNjfKikR0RKRANSzqXiX6OOUuOhbnzMurT-XF5p70VWgwDh0JfobP7cevXoe0hkv-dyMb6TykDAsCsXvgLUEfK8hTl2xQW2E0csi9nIX160GdCDzybT5JcCj7XnINOoaKClmA7Sir79khYkfZXzQxij-y2GdnRB4Ctn3UnTGmrGGY3kC0KcFfHlHS-MEX7JtC6wB9Zj79c_3Td75xN_MLWJ8qvNpGZeclsOblijuGr3eJrkIRie7ow8UUv3wVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664d0747c0.mp4?token=rux5GTCl0o0e2CBA_99Oykgu12jA7NCGwRH_z51qZKEY4lj0CpMVFKFI7LzlBjk45nqLbvpmEtrNYZdDE_NP-_r4MNjfKikR0RKRANSzqXiX6OOUuOhbnzMurT-XF5p70VWgwDh0JfobP7cevXoe0hkv-dyMb6TykDAsCsXvgLUEfK8hTl2xQW2E0csi9nIX160GdCDzybT5JcCj7XnINOoaKClmA7Sir79khYkfZXzQxij-y2GdnRB4Ctn3UnTGmrGGY3kC0KcFfHlHS-MEX7JtC6wB9Zj79c_3Td75xN_MLWJ8qvNpGZeclsOblijuGr3eJrkIRie7ow8UUv3wVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ به تهدیدهای ترامپ از نقطۀ صفر مرزی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/451912" target="_blank">📅 17:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d83b8117.mp4?token=eonDX1coMT00JTEg64Q7MoClCcFU1UYn17TGXTZ3NLXd4CBICgunRYggtO3fbhfb89kp1z5NoDoTU3UdB6HnduPzGyWWrEj7pr8wLabRGkBBO-hgcWMc3BdBdHOETgnj0_9hY4xMGTz12OTQs4YvX84nKjYr_kVgG5ExRQpheEJayC48H0UcPlRX31ppROcErncy43zwY-g-9KIW-K214ChEXcrksD0eYtekSCCzgM86MbxltFk5SAUU8eIyS9DR-wCdFKxcIn7oPGqF5UqxCzbtiFiBvZ95svpJb7TrtZQZUfeYtnQj1ztu_kwyVv9JJpD__QUXjpimilgjTAwZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d83b8117.mp4?token=eonDX1coMT00JTEg64Q7MoClCcFU1UYn17TGXTZ3NLXd4CBICgunRYggtO3fbhfb89kp1z5NoDoTU3UdB6HnduPzGyWWrEj7pr8wLabRGkBBO-hgcWMc3BdBdHOETgnj0_9hY4xMGTz12OTQs4YvX84nKjYr_kVgG5ExRQpheEJayC48H0UcPlRX31ppROcErncy43zwY-g-9KIW-K214ChEXcrksD0eYtekSCCzgM86MbxltFk5SAUU8eIyS9DR-wCdFKxcIn7oPGqF5UqxCzbtiFiBvZ95svpJb7TrtZQZUfeYtnQj1ztu_kwyVv9JJpD__QUXjpimilgjTAwZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ثریا از مقاومت مردم جنوب در مقابل حملات دشمن آمریکایی در بندر خمیر استان هرمزگان
‌
🔹
امروز ساعت ۱۷:۱۵، شبکه یک
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451911" target="_blank">📅 17:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451910">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: ملت عظیم الشأن و به پاخاسته ایران اسلامی؛ حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451910" target="_blank">📅 17:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451909">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مردم سایر نقاط ایران با صرفه‌جویی در مصرف برق، این هدیه را به هم‌وطنان خود در این مناطق می‌دهند تا این ۴استان از اعمال خاموشی معاف شوند.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451909" target="_blank">📅 16:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451908">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98f4cfc11d.mp4?token=MtL8j8hu6-t0RGUtNEEWkpetRrKMnprLTbBTw2fsW44nFG69ADKFyQDq0HoDYpqa98k-RbXFqhQPPDKlqDuN2a3UObzIm20XF1qXsLFc8dSiRqXRl43Oz1TFyQPDrXkFa2mf8Pfr5IBDZc2NH_P-0__bQQwwh8maa1fOr2jg1EVvr-FuGVclsc5LkoCB5-QX_uhhUlZsVsf4X0ZdS6laebMbkfK0_i1P29rgh3dGayi8r7wznJUB_16G08j7Cp9tYg44bsCg_TU0Yylbz9c3IBL0VjHpWvNck9xAJlJi-kvE1n6XxvbC9hOjoXSFY-4FSAQWqf6mzgTOwGoX4Bh77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98f4cfc11d.mp4?token=MtL8j8hu6-t0RGUtNEEWkpetRrKMnprLTbBTw2fsW44nFG69ADKFyQDq0HoDYpqa98k-RbXFqhQPPDKlqDuN2a3UObzIm20XF1qXsLFc8dSiRqXRl43Oz1TFyQPDrXkFa2mf8Pfr5IBDZc2NH_P-0__bQQwwh8maa1fOr2jg1EVvr-FuGVclsc5LkoCB5-QX_uhhUlZsVsf4X0ZdS6laebMbkfK0_i1P29rgh3dGayi8r7wznJUB_16G08j7Cp9tYg44bsCg_TU0Yylbz9c3IBL0VjHpWvNck9xAJlJi-kvE1n6XxvbC9hOjoXSFY-4FSAQWqf6mzgTOwGoX4Bh77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مامانی ۵ ماه دوریتو کشیدم
🔸
مادر شهید امیر علی کمالی از شهدای میناب، امروز بخش دیگری از پیکر فرزند کودکش را به آغوش خاک سپرد‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451908" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451907">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCAk3lT6u_yag2j06oMu7cKn6kpkDeV_vMZfaooDgbn-79ui-rzGD8wOZZUct2ZKpxnak7nZR6C8DJgsu4_e9wZOJhbc0ymGtufL3V0YAv-HiMPw2YIOmDj2opp4YuAvwzJhEcLg6zWcx3PIGraz4N2XME_jpKBNxNi2viOJjl5plU7pXcUboVtPyd9H6tm1_1fnhUkBmVc8AUOfPKqTxme1BTWxP8Y6lZOJ8BF7rbBMJ-tltfT0B3WFsI5XcMU63tk1V4zvGPEQ9crAhT1Gvh7JWKsXEpO7mOR3E3FS5s2DWOXm1aXP_ey1WX0n4koOp0YtyTF5zHa1OS0nvDUnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره به لفاظی علیه ایران رو آورد
🔹
درحالی‌که مقام‌های آمریکایی بارها مدعی شده‌اند ایران هیچ تسلطی بر تنگۀ هرمز ندارد و آمریکا «کنترل کامل» این آبراه را در اختیار گرفته است، اکنون با تداوم تحولات میدانی و ناتوانی آمریکا در مقابل حملات ایران، رئیس‌جمهور آمریکا بار دیگر به ادبیات تهدید و لفاظی متوسل شده است.
🔹
ترامپ گفته: «از این لحظه به بعد، هربار که جمهوری اسلامی ایران با موشک، راکت، پهپاد یا هر سلاح دیگری به یک کشتی در تنگۀ هرمز شلیک کند، آمریکا یک پل یا نیروگاه، از جمله در تهران، را هدف قرار خواهد داد.»
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451907" target="_blank">📅 16:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451906">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAky_iJprDsbziEFgEAcoaZHqzH4DFpmjTINs66td6ppyh-tc8R9-pPM3gXrx9fXymW6wee5vKuujblXgJC2AZN4zg868MHT_FogEyjDhTIfU7i8bCteY-MQZh8sNoZaFbqdP3dsV_9ukMwoZKDvOcDQP2SJi8y9VgDsenb3WCcErYy8yb5txMaURA7fE66jT2ttZP63kKZMyazfC5tdcCK4jbgh2_gKvkRnih0LhQ5wncD-DzpJJgTu6KxQwVnUY9P2JsggJyzSgUoVdj8iqAvMkBLA7SpYmFGGkDD6TJMx0F3EgEEhDUWJY9BQVAqBEY6b5hyAz2A7QSIs-YUFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلیمو سم‌های اینستاگرامی را به رسمیت شناخت
🔹
فیلیمو از برگزاری نخستین جشنواره ملی سریال‌سازی نوین با عنوان «ریلیمو» خبر داده است.
🔹
جشنواره‌ای که با شعار «داستانت را عمودی روایت کن» و با تمرکز بر تولید سریال‌های اپیزودیک با روایت عمودی برگزار می‌شود.
🔹
فیلیمو نخستین پلتفرم داخلی بود که این قالب را با عنوان «میکرودرام» وارد شبکه نمایش خانگی کرد و اکنون نیز با برگزاری یک جشنواره اختصاصی، گامی فراتر برداشته است.
🔹
این در حالی است که این پلتفرم نه‌تنها در انتخاب آثار این بخش حساسیت لازم را نسبت به استانداردهای فرمی و محتوایی نشان نداده، بلکه با توسعه پرشتاب «میکرودرام» عملاً در حال تثبیت و گسترش این جریان است.
🔹
به نظر می‌رسد «میکرودرام» در فیلیمو به فضایی تبدیل شده که کمتر نشانی از نظارت و ارزیابی محتوایی در آن دیده می‌شود.
🔹
برگزاری جشنواره «ریلیمو» را می‌توان تلاشی برای اعطای اعتبار و جایگاه رسمی به این گونه تولیدات دانست؛ روندی که در صورت تداوم، می‌تواند مسیر شبکه نمایش خانگی را بیش از گذشته به سمت تولید آثار سطحی و مبتذل، کوتاه‌عمر و مبتنی بر جذب مخاطب به هر قیمت سوق دهد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451906" target="_blank">📅 16:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451905">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqXEmL-b4-8fHMQuQfjPEqbMJFcY9MB0uy16x8fP9cF6y3Qi86x3pSGEtJgj4FfMDIiJtjlgSDr5y8NRT3r8BNqCJyYJ6Hn-LGD0VvF1V5ag2VKQRd308ktd0CI7jGHHbYR9HOTPWWPadAPh_khx7uYk85LP-t0EiB9xv2rR4brEDdCgxe93F_Xd5XY1P7JRHFOEbMuz0NBFseYODigi3VCqGhAnMjXEOZEOn2HCgFolfwokNVRJD_kANFPnbsVCoxvsOI-fYnR4tF0VhIpwFW3cYkYDHZCdzBDZUgl9zVQeeK22RRmLohLr1spX413HtPirK7nxOehRh7C1S3spgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حمله به مواضع آمریکایی‌ها در بحرین
🔹
تلویزیون بحرین: سامانه‌های پدافند هوایی در حال مقابله با حملات هوایی هستند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451905" target="_blank">📅 16:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451904">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4e35c361.mp4?token=PZV1nhavbwlzk0-iOW73u7R-x48QIAfMEyxYUjX5Tl6kux6_Rz6qbTHeLVTVdh3O2kbxfw_J23rIoU8y6punBuWiPHyzr7HGBlxKFf9phUwAWky4Cgcuaflm2sMYu6vwgCEqo5WvueTo9qYnG8uDkyckE6Qu9pnHI1wgO3fvtl4Uzxx1NGk8jn0hEWyzWg7vGm4crkPB2kmPk5Db1YsrQKcbciYGYcm7wVX0wp4BYGVkFuDWaND5f__mymCefIAmeUT1x0WE66SxomfDFZ60H9CjZbWLn0xs7mHGe02CN6rEmHg0eN8XJkjWdTpM-wLKv3MehKN1He6Jk-N7Ed-wcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4e35c361.mp4?token=PZV1nhavbwlzk0-iOW73u7R-x48QIAfMEyxYUjX5Tl6kux6_Rz6qbTHeLVTVdh3O2kbxfw_J23rIoU8y6punBuWiPHyzr7HGBlxKFf9phUwAWky4Cgcuaflm2sMYu6vwgCEqo5WvueTo9qYnG8uDkyckE6Qu9pnHI1wgO3fvtl4Uzxx1NGk8jn0hEWyzWg7vGm4crkPB2kmPk5Db1YsrQKcbciYGYcm7wVX0wp4BYGVkFuDWaND5f__mymCefIAmeUT1x0WE66SxomfDFZ60H9CjZbWLn0xs7mHGe02CN6rEmHg0eN8XJkjWdTpM-wLKv3MehKN1He6Jk-N7Ed-wcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به مرکز توزیع شرکت تجارت الکترونیک وایلدبریز کراسنودار روسیه  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451904" target="_blank">📅 16:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451902">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1420f27113.mp4?token=js1EGP4_z41i8iTSu_0tcDHrJnX04fQfBEBIjKI34930Sak0z2hv8p-sQCQNOJYPfH4aABGjdyfGb223Lwfn2OETMLaQYZywwzo2j9kKbxgo0he3xnI7WrRdawNupBuLS53r-UhYyAHuO8k3w3YxI1b-6jeHqhCazmf4qm1HeVmNhhzX-LZsPv-7M3V6poHAc3p6G3nIkFar9Ie5GlyTO1b3GB9eE7avNPEWvwZ9cmEM2NB61jilAMO7WSghsqS6ZHogJ3czg5Ro7ZxgcVkBWRP0isWrBHDUllNUlJbem84ZFoftZjSkBmyR4lDBW-HZhI6evjfC1K1nimCGFx-UGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1420f27113.mp4?token=js1EGP4_z41i8iTSu_0tcDHrJnX04fQfBEBIjKI34930Sak0z2hv8p-sQCQNOJYPfH4aABGjdyfGb223Lwfn2OETMLaQYZywwzo2j9kKbxgo0he3xnI7WrRdawNupBuLS53r-UhYyAHuO8k3w3YxI1b-6jeHqhCazmf4qm1HeVmNhhzX-LZsPv-7M3V6poHAc3p6G3nIkFar9Ie5GlyTO1b3GB9eE7avNPEWvwZ9cmEM2NB61jilAMO7WSghsqS6ZHogJ3czg5Ro7ZxgcVkBWRP0isWrBHDUllNUlJbem84ZFoftZjSkBmyR4lDBW-HZhI6evjfC1K1nimCGFx-UGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: حوالی ساعت ۱۴ امروز صدای ۳ انفجار در جزیرهٔ لارک و سیریک شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451902" target="_blank">📅 16:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451901">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171b9926fb.mp4?token=CRH2WRy1owd7bdErz0DdSnZxM75ILqOcOoKvae3QekV8OA52P_WaJ0P8ebJwcYAHhDyapp2qXONaLTptSUJtdu9fnUjoqXIBHl853LZiblNNbc0_ZZie0O5u2iyhHDbQzOfbbCGvVXXZdgvKYINJlOFU-wLNq6g5kNusts5c_KNUBCdt21Wz9hDo_4j5LJ5b_CY82sgMiAv1_2c0DVqIyKBCVjw9Ym757fI1efFk9rUOq8P_gAgUqF2VV1AVeYN7x0dLedx9J-KiyJ5zUPxTTb9bnGJqX-0qJ-IHKOvqavc58WVvVaklPE4cKIctq93eAoq_oh6J-hMzkv8qzjjk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171b9926fb.mp4?token=CRH2WRy1owd7bdErz0DdSnZxM75ILqOcOoKvae3QekV8OA52P_WaJ0P8ebJwcYAHhDyapp2qXONaLTptSUJtdu9fnUjoqXIBHl853LZiblNNbc0_ZZie0O5u2iyhHDbQzOfbbCGvVXXZdgvKYINJlOFU-wLNq6g5kNusts5c_KNUBCdt21Wz9hDo_4j5LJ5b_CY82sgMiAv1_2c0DVqIyKBCVjw9Ym757fI1efFk9rUOq8P_gAgUqF2VV1AVeYN7x0dLedx9J-KiyJ5zUPxTTb9bnGJqX-0qJ-IHKOvqavc58WVvVaklPE4cKIctq93eAoq_oh6J-hMzkv8qzjjk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی: انتقام، فاصله‌گرفتن از مراتب بدها و در مقابل بدی‌ها ایستادن است؛ نفرت‌ و خشم جمع‌شده در دل مردم، آثاری حقیقی نسبت ظالم دارد
.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451901" target="_blank">📅 15:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512f0a5170.mp4?token=TrLnksKHTe1BxF3g7mLKjCbZn9rfoKgSUtMRYo0qscBX2vtzoKDXHumeHx5Fn7MQrwhfICI0cZupG6F82Dg-6FTbWyCTEas0ZpdJUgwYHvsPGGq1psSVOysbmEGDcL6Uegs87zCqXGCjEcMwaxhMvV5RlKjCv_yd-Mb3jJFUzz99gAq-y77dc3efCB54Y6HHR9MQGILtS34MKPcMrM1AjNJk951jNdA84LcIx3sOpnLZ6rN6VU4iA2D7fj1zGA9cEJ5u9k1fpyBpqnYKlWDmQkWxrm4YM4XikL_AUX4E5K0BckQLhBWWo1g8vlzZ9W7on7ixdJ6yZEceilhlAywqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512f0a5170.mp4?token=TrLnksKHTe1BxF3g7mLKjCbZn9rfoKgSUtMRYo0qscBX2vtzoKDXHumeHx5Fn7MQrwhfICI0cZupG6F82Dg-6FTbWyCTEas0ZpdJUgwYHvsPGGq1psSVOysbmEGDcL6Uegs87zCqXGCjEcMwaxhMvV5RlKjCv_yd-Mb3jJFUzz99gAq-y77dc3efCB54Y6HHR9MQGILtS34MKPcMrM1AjNJk951jNdA84LcIx3sOpnLZ6rN6VU4iA2D7fj1zGA9cEJ5u9k1fpyBpqnYKlWDmQkWxrm4YM4XikL_AUX4E5K0BckQLhBWWo1g8vlzZ9W7on7ixdJ6yZEceilhlAywqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: با اخراج آمریکا از منطقه رژیم صهیونی محو خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451900" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c44a6e41.mp4?token=ebinTDFIAOwN-b2gOvzSoumhMwVLd-RL4w7tPPS8lw_ekPYc9azuoVV-Ie19Y_03mt54y0SY6yOCu9dYhWvJFYzziRzR-MLhwM6-_64BUSsWyrNbggbE-voyLD6CxOd6NF3he9cYRzE1sckiGaWF3riGbNmBYFVBnOMzqfw0v7393qPFfflvbEeS4q31CAotRQjF-2y24qklECGU-9pWUAyyGajNLxSTn2EInrYlV2y926Vh-sQNglfOsdnYk8jqEoEepifDm61JVLGg9f-aPpFTWn7KPJDvw-Ib_TWKTZy6MOlGg3AaS36TMJUmVjcwDCFxulZ4XMA6wtyWt3bWBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c44a6e41.mp4?token=ebinTDFIAOwN-b2gOvzSoumhMwVLd-RL4w7tPPS8lw_ekPYc9azuoVV-Ie19Y_03mt54y0SY6yOCu9dYhWvJFYzziRzR-MLhwM6-_64BUSsWyrNbggbE-voyLD6CxOd6NF3he9cYRzE1sckiGaWF3riGbNmBYFVBnOMzqfw0v7393qPFfflvbEeS4q31CAotRQjF-2y24qklECGU-9pWUAyyGajNLxSTn2EInrYlV2y926Vh-sQNglfOsdnYk8jqEoEepifDm61JVLGg9f-aPpFTWn7KPJDvw-Ib_TWKTZy6MOlGg3AaS36TMJUmVjcwDCFxulZ4XMA6wtyWt3bWBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: هیچ‌وقت تولید موشک و پهپاد متوقف نشده؛ حتی در طول جنگ نیز این موضوع ادامه داشت.   @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451899" target="_blank">📅 15:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎥
تک‌نواز پلنگ صورتی درگذشت
🔹
پلاس جانسون، ساکسیفونیست آمریکایی که به تک‌نوازی ساکسیفون در موسیقی «پلنگ صورتی» اثر هنری مانچینی مشهور بود، در ۹۴ سالگی درگذشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451898" target="_blank">📅 15:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGtvPuH9n3ZPpBkJ9pYH5_irVTyA_PajI3LphrxzW19dXWkmHdnOXRReu8sqJ0ELebiIEnDhr69nLpk3z4bp8sK6IJlVXC7uBHl_s-kcln9HYYxXlu8VlhtQbopqGCezmQzwlicicS2JUpc7_CkSglQ3ndXJMCoDRoKT2-2m38ODLWyICpSum78iPCnu_U_l_5SB6oYJuyQsaSi6QayMQ2hnxgXgHNrbqvHj6FZDS288X4CLWrBGr1d7dn9F9lVNf8f40PFQ3Xz3gIcsfYiGyvdnslb-okA0mkSfOm3d6nEIwJqZ1KBveg5VZMH4vdGQShg1o5QCdwWWcZhxTVJcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند برنده دادگاه CAS با گاف پرسپولیس
‼️
دادگاه عالی ورزش (CAS)، شکایت باشگاه پرسپولیس علیه علیرضا بیرانوند به دلیل فسخ یک‌طرفه قرارداد و همچنین شکایت این باشگاه از تراکتور با ادعای اغوای بازیکن را به دلیل عدم پرداخت به‌موقع هزینه دادرسی، مختومه اعلام کرد.
🗣
پرسپولیس موظف بود هزینه دادرسی این پرونده را حداکثر تا ۱۵ جولای(۲۴ تیر) پرداخت کند، اما این مبلغ با یک روز تأخیر واریز شد. همین تأخیر موجب شد رئیس دادگاه عالی ورزش از پذیرش پرداخت خارج از مهلت قانونی خودداری کرده و پرونده را به طور رسمی مختومه اعلام کند.
🗣
در روند پیگیری این پرونده، ۲ اشتباه بزرگ نیز توسط پرسپولیس رخ داده است. از جمله اینکه در یک مرحله شماره پرونده به اشتباه ثبت شده و مبلغی به پرونده‌ای دیگر واریز شده بود. همچنین در مورد اخیر نیز به دلیل بی‌توجهی به تاریخ‌ها، پرداخت خارج از موعد انجام شده است؛ موضوعی که در روند رسیدگی به پرونده بی‌تأثیر نبوده است.
🖥
ادامه مطلب را
در سایت فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451897" target="_blank">📅 15:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">از آغاز تیرماه بیش از۵۰ نفر از هموطنان در حملات آمریکا شهید شدند
🔹
وزارت بهداشت: در حملات هوایی ۶ تا ۲۸ تیرماه، ۵۱۷ نفر مصدوم و بیش از۵۰ نفر از هموطنان شهید شدند.
🔹
در میان شهدا ۵ زن و ۲ شهید زیر ۱۸ سال، در میان مصدومان ۳۵ زن و ۱۹ نفر زیر ۱۸ سال هستند، تاکنون…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451896" target="_blank">📅 15:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d7d5c206.mp4?token=CWnbOLcY-e7Uz7ykilYGWpHOpxUgBDOsv8iizMw1NUs7KYYtK1EhcXMVVQ7uKdrvqIgRhBmxWT1FQ04JcSbzoxJaSKhzx8IdYa4CsM0oGOa4OXu5-u4VcUcVgH1RzKAL9rWh7dOA_SV41TV7q4_0grsmbV5OXFkwOFayRyEEu5IZxpfZQ99A2QftetHzbXv2qhNKUyPaBvpbm4fur7Ymm8uo66MnrhtU66TUT6NCOmpdZzxVTce2v20ZUvKJ3lhPn6G45jC4oSUkaiwJnZ2611WqE8bUwqU68ixlnSrqRAt-PKRYv8dZEvqkKHwktsCcmEk3Rck9PCdS3MQ3VsONrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d7d5c206.mp4?token=CWnbOLcY-e7Uz7ykilYGWpHOpxUgBDOsv8iizMw1NUs7KYYtK1EhcXMVVQ7uKdrvqIgRhBmxWT1FQ04JcSbzoxJaSKhzx8IdYa4CsM0oGOa4OXu5-u4VcUcVgH1RzKAL9rWh7dOA_SV41TV7q4_0grsmbV5OXFkwOFayRyEEu5IZxpfZQ99A2QftetHzbXv2qhNKUyPaBvpbm4fur7Ymm8uo66MnrhtU66TUT6NCOmpdZzxVTce2v20ZUvKJ3lhPn6G45jC4oSUkaiwJnZ2611WqE8bUwqU68ixlnSrqRAt-PKRYv8dZEvqkKHwktsCcmEk3Rck9PCdS3MQ3VsONrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: دیتاسنتر عظیم دشمن در امارات در جنگ تحمیلی سوم نابود شد
🔹
این دیتاسنتر در طول ۲۰ سال با کمک و سرمایه‌گذاری اروپایی‌ها، رژیم صهیونی و آمریکا در امارات برای کنترل منطقه ایجاد شده بود.
🔹
همه سرمایه‌گذاری‌های آمریکا در طول ۵ دهه در منطقه با نابودی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451895" target="_blank">📅 15:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
عربستان از فعال شدن هشدارهای زودهنگام در شهر الدمام خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451894" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386a38abce.mp4?token=eT4TaNzdbu9_6OgoPmxMbRsdzaOrYjLftQivAnx0LM8AAuNsXJa4a0bsc7JwDMuLdvobScuO4ig7hq1DHeG4sw5WZcini0Sy0RNt5B1jUwzIgNG89SMnUhXFPe7ZznTnSXeaJ38_ayzN48FJVVHKXnAMZ1_0DOxCHYQA7u2QVZ9xiDOgfSTYqlAY6ABWTY7HCrIZnv4_cYvZCa4Yo4eejoVWCYlnxEtqQBf-747nS47SbVplePHeCYP6BNHjY2EcSj1TDKIPi4xLGxnUr2p3KhibSgp1Eew82IeWpYorRSWQoN3PneZHIf8ZKDrbngAu0oIJjKxOlc1AanGIIxCIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386a38abce.mp4?token=eT4TaNzdbu9_6OgoPmxMbRsdzaOrYjLftQivAnx0LM8AAuNsXJa4a0bsc7JwDMuLdvobScuO4ig7hq1DHeG4sw5WZcini0Sy0RNt5B1jUwzIgNG89SMnUhXFPe7ZznTnSXeaJ38_ayzN48FJVVHKXnAMZ1_0DOxCHYQA7u2QVZ9xiDOgfSTYqlAY6ABWTY7HCrIZnv4_cYvZCa4Yo4eejoVWCYlnxEtqQBf-747nS47SbVplePHeCYP6BNHjY2EcSj1TDKIPi4xLGxnUr2p3KhibSgp1Eew82IeWpYorRSWQoN3PneZHIf8ZKDrbngAu0oIJjKxOlc1AanGIIxCIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: آمریکایی‌ها هر سلاحی برای جنگ جهانی سوم کنار گذاشته بودند علیه ایران بکار گرفتند
🔹
سخنگوی ارشد نیروهای مسلح: دشمن در جنگ تحمیلی دوم فکر می‌کرد ظرف یک هفته نظامی جمهوری اسلامی را سرنگون و هفته بعد هم ایران را تجزیه می‌کند.
🔹
باتوجه به دو عملیات…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451893" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451892">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a82f3c1b.mp4?token=aLbD7-mgV9NnytDsrr_13c7A2dXALuYjlkMEM98kqIu_inyATgiOJ7VLLH0pAzYpAI5ExBJRdIEmUjHzCKI1vZV_Dc8k6tK-fpFjXUxqFeESnbPYjKcd43qQWi4ng96f_sKeSDMGl1uk7ryw2V2MdrnGsysajeHdP9__N5wvR3qIS1usOj2eOeylB2YnYqnx1auXkKERxPuC1ge1dSPLWbfb8rHBU3QLEhmgH_YDsREzZ1tpHwWmzqvLKaSsepd__OBL9RVud6nwPf82lQtL-H124wtrnspkTUR-5b_dGSh9_R0_3ixnWNgZb7Knn-FmzxjBYoMTPFN_Bd59n_vq8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a82f3c1b.mp4?token=aLbD7-mgV9NnytDsrr_13c7A2dXALuYjlkMEM98kqIu_inyATgiOJ7VLLH0pAzYpAI5ExBJRdIEmUjHzCKI1vZV_Dc8k6tK-fpFjXUxqFeESnbPYjKcd43qQWi4ng96f_sKeSDMGl1uk7ryw2V2MdrnGsysajeHdP9__N5wvR3qIS1usOj2eOeylB2YnYqnx1auXkKERxPuC1ge1dSPLWbfb8rHBU3QLEhmgH_YDsREzZ1tpHwWmzqvLKaSsepd__OBL9RVud6nwPf82lQtL-H124wtrnspkTUR-5b_dGSh9_R0_3ixnWNgZb7Knn-FmzxjBYoMTPFN_Bd59n_vq8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار شکارچی: آمریکایی‌ها هر سلاحی برای جنگ جهانی سوم کنار گذاشته بودند علیه ایران بکار گرفتند
🔹
سخنگوی ارشد نیروهای مسلح: دشمن در جنگ تحمیلی دوم فکر می‌کرد ظرف یک هفته نظامی جمهوری اسلامی را سرنگون و هفته بعد هم ایران را تجزیه می‌کند.
🔹
باتوجه به دو عملیات وعده صادق ۱ و ۲ و رزمایش‌های اقتدار آسیب‌شناسی کردیم و بانک اهداف تعیین شده و برنامه‌ریزی داشتیم.
🔹
دشمن در هفدهم و هجدهم دی‌ماه می‌خواست کودتا را با جنگ سخت ترکیب کند اما ملت ایران نقشه دشمن را ناکام گذاشت.
🔹
در جنگ تحمیلی سوم رهبر شهید برای جبران خلاء خودشان و فرماندهان کاملا برنامه ریزی کرده بودند.
🔹
هر سلاحی که در دنیا آزمایش شده بود اما به‌کارگیری نشده بود در جنگ با ایران استفاده شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451892" target="_blank">📅 15:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451891">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
عربستان از فعال شدن هشدارهای زودهنگام در شهر الدمام خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451891" target="_blank">📅 15:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451890">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451890" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451889">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd44dfad6f.mp4?token=W8s0eqdGTYNeHeApgBH6GOzM62EFPkKI0RDW7JG8cHV0vaPtQ-Agj5ZkHoCFXev7pxaIGSxf8rfLbFA-q2NrB66wDmjsCsw2n2z0p24z0xRDlnRfMzifUdR5sl0gl32-Nwb8bDxpnscK9x8n4cYQnuzMMvyrzNra7jXKQdSneuP8n0DYYPa7jq95H6Is6pRGg1hjU67pVOUhHRFhzTgaLNj5ijLz8GaXdAYIQCq9XpzaXigsLLgZM1ENnJA5Veoj4ZOsNRHO3eJ-Cw--n4bYVocuNbUfEr8wGH7JtcJ7PiKWrNArtys993FHBtTdkrxcwYw5CLZA70Yvea1Mfow2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd44dfad6f.mp4?token=W8s0eqdGTYNeHeApgBH6GOzM62EFPkKI0RDW7JG8cHV0vaPtQ-Agj5ZkHoCFXev7pxaIGSxf8rfLbFA-q2NrB66wDmjsCsw2n2z0p24z0xRDlnRfMzifUdR5sl0gl32-Nwb8bDxpnscK9x8n4cYQnuzMMvyrzNra7jXKQdSneuP8n0DYYPa7jq95H6Is6pRGg1hjU67pVOUhHRFhzTgaLNj5ijLz8GaXdAYIQCq9XpzaXigsLLgZM1ENnJA5Veoj4ZOsNRHO3eJ-Cw--n4bYVocuNbUfEr8wGH7JtcJ7PiKWrNArtys993FHBtTdkrxcwYw5CLZA70Yvea1Mfow2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: ما خرمشهرها در پیش داریم، اولین خرمشهری که باید آزاد کنیم ذهنمان است
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451889" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8785a722d0.mp4?token=vWOt4wzcMJWT2KZmZRhKwuFEb21ZVDW9IAxcf6ZdOlDEyPc01hTKwRovmiDaMPZbFXi8ssJ5s7SOK-tKVTurEBA7y-wWrkXkx0cjLHGlC8TlFiYZkWK6_3CQIw204wFzmX_nBqO3MBFAzxHA6Y8HIR3fPyJRnphUb5t5IL6XQIWt5vgg1ZB5F6le9fiF7G67KQ_0q12dOVDtFYKCXakijZVnPMAcxpWmGX-EgEgTyUvm3b0SfdLpSzaSIdvNCydVbkgVSJZ1vghUSFgLL_Nde7y6dkiWA-TmNNEvUn3Si-roxrYtgSqZ9fTjyQhPoyfQ5GgfA34EWO1CyOwWs9dOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8785a722d0.mp4?token=vWOt4wzcMJWT2KZmZRhKwuFEb21ZVDW9IAxcf6ZdOlDEyPc01hTKwRovmiDaMPZbFXi8ssJ5s7SOK-tKVTurEBA7y-wWrkXkx0cjLHGlC8TlFiYZkWK6_3CQIw204wFzmX_nBqO3MBFAzxHA6Y8HIR3fPyJRnphUb5t5IL6XQIWt5vgg1ZB5F6le9fiF7G67KQ_0q12dOVDtFYKCXakijZVnPMAcxpWmGX-EgEgTyUvm3b0SfdLpSzaSIdvNCydVbkgVSJZ1vghUSFgLL_Nde7y6dkiWA-TmNNEvUn3Si-roxrYtgSqZ9fTjyQhPoyfQ5GgfA34EWO1CyOwWs9dOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ چطور هر روز پیروز می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451888" target="_blank">📅 15:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
عربستان از فعال شدن هشدارهای زودهنگام در شهر الدمام خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451887" target="_blank">📅 15:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451883">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ec99538e.mp4?token=BcUOWEu3fDlChkVBh6617eN-3llGuU5Glskh62Swj60SciR9A6C9IqNTt4fPeHv_dGGUGtwHWiGOeDoRgKNaOyA1Pa1lMYFEGi56rUtD1M5ZIjisrmn4veh6N0uPKsUI9oiWMiaTQeNvrFDayolT4xlq4BlspbdwvpS6g9Y0cQdvxRmQgCwTLtAOCHk5i9anAzhqiBtSDjwNVFQgZeDh5i1f64KFXu32E44OaVaU84erg0hesVuPCFdct8SWRb12-ScCJGoPDos_qlrzhL99zHkLN0YPn8g5zSmZ1yl25l5kSk6LNMvMmUczsIqK_FVxXd7ySPawgEcZwXFebfBA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ec99538e.mp4?token=BcUOWEu3fDlChkVBh6617eN-3llGuU5Glskh62Swj60SciR9A6C9IqNTt4fPeHv_dGGUGtwHWiGOeDoRgKNaOyA1Pa1lMYFEGi56rUtD1M5ZIjisrmn4veh6N0uPKsUI9oiWMiaTQeNvrFDayolT4xlq4BlspbdwvpS6g9Y0cQdvxRmQgCwTLtAOCHk5i9anAzhqiBtSDjwNVFQgZeDh5i1f64KFXu32E44OaVaU84erg0hesVuPCFdct8SWRb12-ScCJGoPDos_qlrzhL99zHkLN0YPn8g5zSmZ1yl25l5kSk6LNMvMmUczsIqK_FVxXd7ySPawgEcZwXFebfBA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به مرکز توزیع شرکت تجارت الکترونیک وایلدبریز کراسنودار روسیه
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451883" target="_blank">📅 15:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451882">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451882" target="_blank">📅 15:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451881">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eccd805d5c.mp4?token=Cxt38npDg3bG7NDn5hV0Vd9TtAXW4633OY8TZ4qBF3i5AxnfmdaSOyy_4ia9eqGepvc5dTyyGb6II4qtVPdMQJnbCzzmd478pBpIsZFWXtHfd8tUu1PIbdTKxsw-WIBnIKr4rD6SORz63PupWT8hanma1ebc0N56-ZHV-FlW-1CAgTd5fMT1_Ea8J5jCXMeRI6FFQjph3-SwxiQ8tWq-jcQKJO3yDzsAQrdsbJnw0ENoZyWh5aWD00MSqikADkXfvdMIJByfgW1mhcTElHInPXkOBgkx4GGoe3Sdr-0hhiFu_XTOcTDzYM5fWjHncNTpXHm0czXQoHkY237LE7ze8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eccd805d5c.mp4?token=Cxt38npDg3bG7NDn5hV0Vd9TtAXW4633OY8TZ4qBF3i5AxnfmdaSOyy_4ia9eqGepvc5dTyyGb6II4qtVPdMQJnbCzzmd478pBpIsZFWXtHfd8tUu1PIbdTKxsw-WIBnIKr4rD6SORz63PupWT8hanma1ebc0N56-ZHV-FlW-1CAgTd5fMT1_Ea8J5jCXMeRI6FFQjph3-SwxiQ8tWq-jcQKJO3yDzsAQrdsbJnw0ENoZyWh5aWD00MSqikADkXfvdMIJByfgW1mhcTElHInPXkOBgkx4GGoe3Sdr-0hhiFu_XTOcTDzYM5fWjHncNTpXHm0czXQoHkY237LE7ze8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدافعان جزیرۀ بوموسی آمادۀ مقابله با گزافه‌گویی‌های ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451881" target="_blank">📅 15:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451880">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b20c00b5.mp4?token=sQ2SXz44pexFOjmoxBbwOUd7sM6a5D_zm1HycueFcrKAjpqDwVnQJICSZ44sTVbALjCsOilJJs7VufYbwmFutYpA6csbaHEULKSZho7ce6Bp0qoBqXbUujiO1mLOg3X4QBu8IWWDIowvn0vdJB-kh8p3wFEi_FFmF3hale_JtP6g5bAOUBQZ37AaOzpA2wnkzxMSAX-Mu93H2dyf_DNsO66OCdLst4u0xkv68mBSiTP8WJuCn4zuiA9K-wdvNm9s4X45Nh0Sf-d-tcOpC2LVgnWNvSo--VtW8DVMKMdtI5dLUfYXZmvU_HVBWd8wZE8_7QGhYB-0wCADsuOmFEfr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b20c00b5.mp4?token=sQ2SXz44pexFOjmoxBbwOUd7sM6a5D_zm1HycueFcrKAjpqDwVnQJICSZ44sTVbALjCsOilJJs7VufYbwmFutYpA6csbaHEULKSZho7ce6Bp0qoBqXbUujiO1mLOg3X4QBu8IWWDIowvn0vdJB-kh8p3wFEi_FFmF3hale_JtP6g5bAOUBQZ37AaOzpA2wnkzxMSAX-Mu93H2dyf_DNsO66OCdLst4u0xkv68mBSiTP8WJuCn4zuiA9K-wdvNm9s4X45Nh0Sf-d-tcOpC2LVgnWNvSo--VtW8DVMKMdtI5dLUfYXZmvU_HVBWd8wZE8_7QGhYB-0wCADsuOmFEfr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایگاه‌های آمریکا در منطقه زیر رگبار حملات پهپادی ارتش
🔹
روابط‌عمومی ارتش: در دور جدید حملات پهپادی عملیات صاعقه، از بامداد امروز «ساختمان‌های اسکان و رفاهی» و «انبار تجهیزات» ارتش تروریستی آمریکا در پایگاه الازرق اردن را هدف حملات پهپادی قرار داد.
🔹
همچنین…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451880" target="_blank">📅 15:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: ملت عظیم الشأن و به پاخاسته ایران اسلامی؛ حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451879" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451876">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbQpOGjdNuvzLNZ-OzF1DYD58ScX3_CQ8ar5BOSD3lokI4ihVUUA-4UHJUAmp4-3YQRO4NGca6PmXT0COzFTkyPEyNe38Vrsv0pft8fWos2sqBzWrtWPV8gJrCL3ZyWsO3BWrZG-Ir2JkFRxPGbExzPzUQZ9aqdfGRgo8jcQsdqEoIZQ6hO7ixRCWMV1oSpwacb3tuMyvIwESjUUDriix-mFW0ArkZmFcBCmt_SRa7nuUt_x4VP8jmkEOWJj10wMDtDNum_qLC7i4bIhYXp0watpkmsYgSnvcMyxTkE8McXdJopWTsn-CLX3IklDUoMd7kzmKXUXVL_Vo9m80b5AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: هیچ فعالیت هسته‌ای در کوه کلنگ وجود ندارد
🔹
سخنگوی وزارت امور خارجه امروز با بیان اینکه فعالیت‌های هسته‌ای ایران بر اساس تعهدات پادمانی به آژانس اعلام شده، گفت: تمرکز بیمارگونه آمریکا بر کوه کلنگ که هیچ فعالیت هسته‌ای در آن وجود ندارد، چیزی جز بهانه‌جویی برای تخریب و ویرانگری نیست.
🔹
بقائی پرسید: راستی، مدیرکل آژانس بین‌المللی انرژی اتمی و نامزد دبیرکلی سازمان ملل کجاست؟!
🔹
سخنگوی دستگاه دیپلماسی تصریح کرد: ایرانیان با تمام توان در برابر کینه‌توزی آمريکا و هرگونه تعرض به حاکمیت و امنیت ملی کشورشان می‌ایستند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451876" target="_blank">📅 14:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=bY_3Vz8prRrvtYRtHYlmqO1is-LosOpQi1sMA3atwvPNC9A5OFDv09TPZpH8vlD45uCC81fuJ7nP4DXHRJt1r5Ec6kUTKv8jr0ylW9qznrrjKKxqDx4avOC5lSzL-v6aJPWschkq3xaZZV3I5ylz3rQjY9zy8uT5RBMXuxbBnUzlz_lyNwkMkllznh6kkDwE8Mv4UZKLZ_qZexBtKq6POSnuKo9qfqZ2L7NZVFZc4s4a9NaEA1040Z1HwyW_5PY32E1rq5gX3a7NS0mZnUvrerpEy5qLxX7O503-GostviJfKWItJ8pi_gyIPTDW6aZFRt1-XO-MUQBCYQhE7uBujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3108cde4ff.mp4?token=bY_3Vz8prRrvtYRtHYlmqO1is-LosOpQi1sMA3atwvPNC9A5OFDv09TPZpH8vlD45uCC81fuJ7nP4DXHRJt1r5Ec6kUTKv8jr0ylW9qznrrjKKxqDx4avOC5lSzL-v6aJPWschkq3xaZZV3I5ylz3rQjY9zy8uT5RBMXuxbBnUzlz_lyNwkMkllznh6kkDwE8Mv4UZKLZ_qZexBtKq6POSnuKo9qfqZ2L7NZVFZc4s4a9NaEA1040Z1HwyW_5PY32E1rq5gX3a7NS0mZnUvrerpEy5qLxX7O503-GostviJfKWItJ8pi_gyIPTDW6aZFRt1-XO-MUQBCYQhE7uBujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: ملت عظیم الشأن و به پاخاسته ایران اسلامی؛ حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های گذشته به بهانه تلافی انفجار کشتی‌های متخلف انجام می‌شد.
🔹
شب گذشته هم که با وجود وسوسه خدمه کشتی‌ها، هیچ شناوری جرات آزمون عبور از مسیر غیرقانونی جنوب تنگه را نکرد، و طبعاً انفجاری هم رخ نداد، ارتش کودک‌کش آمریکا خوی تجاوزگری را کنار نگذاشت و حمله هوایی و موشکی به تعدادی از مراکز نظامی و غیرنظامی ما را تکرار کرد و اینک در حال دریافت پاسخ‌های کوبنده است.
🔹
با توکل به خدای متعال، رزمندگان شجاع هوافضای سپاه در پاسخ به تجاوزات دشمن در موج ۲۵ عملیات نصر ۲ با رمز مبارک یا حسن ابن علی (ع) و تقدیم به شهدای مدرسه شجره طیبه میناب، پایگاه‌های آمریکایی در اردن را یک بار دیگر در هم کوبیدند.
🔹
در اولین مرحله پاسخ در حمله موشکی و پهپادی به پایگاه‌های ملک فیصل و پرنس حسن یک سوله آماده سازی اف ۱۵ هدف قرار گرفت و همچنین در حمله به یک سوله آماده‌سازی پهپادها، هشت پهپاد MQ 9 نو و آکبند در بسته‌های خود قبل از آماده‌سازی به طور کامل منهدم گردید و به دو فروند از آنها که در محوطه بودند خسارت سنگین وارد آمد.
🔹
در حمله بعدی به سوله نگهداری بالگردها خسارت اساسی به دو فروند بالگرد سنگین آمریکایی وارد آمد.
🔹
در حمله به یک مرکز اسکان نیروهای متجاوز، تعدادی از آنها کشته و زخمی شدند.
🔹
عملیات تنبیه متجاوز ادامه دارد، چرا که اگر متجاوز تنبیه نشود و هزینه سنگینی بابت عهد شکنی و زیر پا گذاشتن توافقات نپردازد، تصور خواهد کرد که هر وقت اراده کند می‌تواند جنگ را از سر گیرد و هر وقت تحت فشار قرار گیرد به آن خاتمه دهد و چرخه جنگ، مذاکره و باز هم جنگ را تکرار کند و سایه جنگ را دائماً روی سر ما نگه دارد.
🔹
تنها راه احیای بازدارندگی و برقراری امنیت پایدار، اجرای فرمان قرآن است که می‌فرماید "و قاتلوهم حتی لا تکونوا فتنه".
🔹
برای دور کردن دائمی سایه جنگ از کشور جز ایستادگی و تحمیل هزینه سنگین به متجاوز راهی نیست اگر این پاسخ‌ها اکتفا نکند و تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451875" target="_blank">📅 14:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ee3caa25d.mp4?token=uf9dTfg1c0oen6LdMr6YGcje-e4hwRq6ykFbyN7hoQOZLWrWEQ4tRJIPMeRclmmBCCq2jYu-Eq7qHuef7AXLJSENP6h1yXLtJnJA6_9wEnFkKzn9Arbg114PhFfKtZbC3J_PfhvpYWg87Z6v1jD54HkJ6S5jdqmdm3aCwScF3LDL0QUNCufixGVk4M1fMX5wVTZx09ZlkgJKoNxoIFXEvWnfsPVUQ7zXDyK37dhqLSTzVBJEsXWUKhPhP8lZ9qZ1B1Q--po8aZgr_RCiUXVt9Ek46qAt3N6YAgM3hiXDOy4ruagKAa5GaL6onZhUGA1cs7qU5LUyNr4t9YK5fwnIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ee3caa25d.mp4?token=uf9dTfg1c0oen6LdMr6YGcje-e4hwRq6ykFbyN7hoQOZLWrWEQ4tRJIPMeRclmmBCCq2jYu-Eq7qHuef7AXLJSENP6h1yXLtJnJA6_9wEnFkKzn9Arbg114PhFfKtZbC3J_PfhvpYWg87Z6v1jD54HkJ6S5jdqmdm3aCwScF3LDL0QUNCufixGVk4M1fMX5wVTZx09ZlkgJKoNxoIFXEvWnfsPVUQ7zXDyK37dhqLSTzVBJEsXWUKhPhP8lZ9qZ1B1Q--po8aZgr_RCiUXVt9Ek46qAt3N6YAgM3hiXDOy4ruagKAa5GaL6onZhUGA1cs7qU5LUyNr4t9YK5fwnIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین اردوی دانش‌آموزان مدرسهٔ شجرهٔ طیبه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451874" target="_blank">📅 14:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45b08c6ac.mp4?token=igNUBW3QRle_MkZNRg3lKxZxPw1SgJuaYMBMcanCx36wyowoBGi9Wg6ivlj3nLbHC_5hXOkf0csqN1bQqtPRvVV_Mp_w_synrIb6cYzjc-avq54Ok6L-EspLZ29lLRQxUCcmiTqqKbtW1-KgA3DC6lQBv6W14v8Ywi7S4TFAo_68TjBUTrP_oOipCG9EBCGRLvkc-UlbvUS2AJWUhnPPMJAfZsbCcr-Ub5jvErm11MMgYZ6TVN6YsaOxeQyiI3wYeal2egRrbIT7Gwm1nY2tjA5vowb4qdyVmgnLUqrfVH_pPE8C6_o6l3rlF_UNDw36rbzQgOc74MEXgoXsgJa8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45b08c6ac.mp4?token=igNUBW3QRle_MkZNRg3lKxZxPw1SgJuaYMBMcanCx36wyowoBGi9Wg6ivlj3nLbHC_5hXOkf0csqN1bQqtPRvVV_Mp_w_synrIb6cYzjc-avq54Ok6L-EspLZ29lLRQxUCcmiTqqKbtW1-KgA3DC6lQBv6W14v8Ywi7S4TFAo_68TjBUTrP_oOipCG9EBCGRLvkc-UlbvUS2AJWUhnPPMJAfZsbCcr-Ub5jvErm11MMgYZ6TVN6YsaOxeQyiI3wYeal2egRrbIT7Gwm1nY2tjA5vowb4qdyVmgnLUqrfVH_pPE8C6_o6l3rlF_UNDw36rbzQgOc74MEXgoXsgJa8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر شهدای مدرسۀ شجره طیبه میناب  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451873" target="_blank">📅 14:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_GL8uKGlEV8OFZBAEtv5xI04WxmbujGjEOzcKXJog4Zu5UvNQqAUrHUOnv31rJOkgq9AvLUf6YjwNuS7nU_mtDmYVtDmkwnTJUyUCF1N64azxYyvzt-BPD43LHIq0WdT1AKsJ6gGnavQI4YnRv1ldXfhI_9g6bpEkQKWP3WGEFq4G20tPBmh5gJEUWzfDMFgk4667jjr2vBGvsJwzd2aMwgmvE2bAufPPLlq4OjPnERdCPQ_Ra8Ndv-74Hm2NyzMnMibNI219a2DR_BJ1raEW7zdsPVDFgUidJLhKQClhw8JMDTJdFJYu1pqEPQMxL2UEqYwL_CCR7d-D30KnNh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ace_diABzCTZ9RqfDfIeTjXzwTCABJE4QopFFsHkWRBHC8PhrRQLP36OHdsIGGKufA_VShao_8HHwEh1d_UjW-mw7kXUAqt-KwYci-ddT8fFyvBBqkjEpVc4J63NKRd9W9-zUv4W57FYbix7527DBaX5BeAEip7YGc1eAbcmT9J8ctpnHxR55hbeM2BGO0_VQ95dV8KIdalWCumL_6FH-L_b7Rcj4bF686ZLsFfSIfi3RZ9RoC_Urj9WMQFK-boZeAUOJfyUFu0KvBMMAPPAFzcaljLs2BSeXCkV1lG5LXmDdmo3oMv1A2ZNK4yjNhtFnouq2wmsxycam3vtO2_aGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C58mZIr6TQ57Gpa4J8dOtTmFevmoSPf_tBfKF7PO7Wf6cZ-54KhSHuzYM7tWndAFm8xiyii5n6-h_BNjwdyeyq0eHXMPG_iShN2LOjnXDvJrPD07lC9PoVng3bFUG9z8fJ15X_ZxUfYtlUWxYDk7A0dUKqJ5oBerWadcIwO0eaduPb-qSEFw1F5-L5fyZpeNCHgxflyLb4RBx2NXq7PQna5dbMPsgp5Dqba_L17vGfDObwsW5qEwzppGB9PcTzWPOItxz8W2DfF4qNeVBkQ5lREOSi9fP7ozoPMVD7421CndjB3sFVVqsY2N19d5avn9L22ab4zcrGX4xmOUJt4EkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصویب
۷ تصمیم عملیاتی برای تأمین برق صنایع
🔹
در نشست فعالان اقتصادی و صنعتگران، ۷ تصمیم مهم با دستور رئیس‌جمهور و در راستای حمایت از تولید، صیانت از اشتغال و افزایش پایداری تأمین انرژی صنایع و اصناف به تصویب رسید.
🔹
برخورد قاطع، قانونی و بدون اغماض با واحدهای صنعتی متخلف در حوزه مصرف برق و ابطال پروانه فعالیت واحدهای متخلف از سوی وزارت صنعت، معدن و تجارت.
🔹
ایجاد سازوکارهای لازم برای فعالیت واحدهای صنعتی در روزهای جمعه با هماهنگی شورای‌عالی کار، به‌منظور جبران بخشی از محدودیت‌های تولید.
🔹
کاهش برنامه محدودیت تأمین برق شهرک‌های صنعتی از دو روز در هفته به یک روز.
🔹
الزام مجتمع‌های پتروشیمی به تأمین برق مورد نیاز خود از طریق خرید برق سبز از بورس انرژی، به‌منظور آزادسازی ظرفیت شبکه برای تأمین برق صنایع.
🔹
الزام مگامال‌ها و مراکز بزرگ تجاری به کاهش مصرف انرژی از طریق کاهش ساعات فعالیت، به‌ویژه در دو ماه پایانی فصل گرم سال.
🔹
اجرای برنامه فراگیر اطلاع‌رسانی و فرهنگ‌سازی از سوی دستگاه‌های مسئول و رسانه‌ها برای دعوت مردم به مدیریت مصرف انرژی با هدف حمایت از تولید، حفظ اشتغال و پایداری اقتصاد کشور.
🔹
اختصاص ظرفیت‌های جدید ایجادشده در شبکه برق کشور به طرح‌های توسعه‌ای و واحدهای صنعتی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451870" target="_blank">📅 14:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSUG9zlE_ZNMnG0dO4rLZxxSz7YtHUHp4VYQBXgYAY929EhDtTIaG5HYFnKDzAbemhFCy8sJe8ShHC-x957WZ9n5n8DLH1JGcCqHwfTph7A51sSlnqvZ4v1vfWFXhHaQvmtBn4m7Vrb7UutgNm17Ftjl78dn1ezbpO6PEnwDCgSny_cXbxNCj-54kgQWzOqb1CO_s9AByhNxMNi-zrT7PFs0NtOgM3_x7S7Zq0JfbHdwCxLFSN9qO5i0RPXbhrSY_KToC5eDs-o-wDJ8IN3FvrRljfIooXbXSrA_brmeec2JtPvs-tvlUSKnAPPGpbPlFzTk4-MVMKYC_1W3gfi2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیفا آب پاکی را روی دست استقلال ریخت
🔹
‼️
فیفا در پاسخ به استعلام باشگاه استقلال اعلام کرده است که در صورت باز نشدن پنجره نقل‌وانتقالاتی، این تیم حتی اجازه ثبت و جذب سه بازیکن آزاد پس از پایان نقل‌وانتقالات تابستانی را هم نخواهد داشت.
🔵
این پاسخ در حالی ارائه شده که  تاجرنیا، پیش‌تر اعلام کرده بود آبی‌پوشان حتی در صورت تداوم محرومیت از نقل‌وانتقالات نیز می‌توانند پس از پایان پنجره تابستانی سه بازیکن آزاد به خدمت بگیرند.
🔵
طبق قوانین نقل‌وانتقالات فیفا (RSTP)، باشگاهی که با محرومیت از ثبت بازیکن مواجه است، تا زمان رفع این محدودیت امکان ثبت هیچ بازیکن جدیدی از جمله بازیکن آزاد، را ندارد.
🔵
بر همین اساس طبق پیگیری‌های فارس، مدیران استقلال درباره این موضوع از فیفا استعلام گرفته‌اند و این نهاد نیز در پاسخ اعلام کرده که تا زمان رفع محرومیت، امکان جذب و ثبت بازیکن جدید برای این باشگاه وجود نخواهد داشت.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/451869" target="_blank">📅 14:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IED01n8GAfZag9Q5Lx9KF8EsIBtFgiHWQSR_kdpc_vdPCscsIo0uJMNL3jrHaWty5Q8syHAJYuoV8Nx_hV5NTJas4JotV32zYvD5W4AoJHeqm2nhXNe-GP9CEdFme7iTksGgKJmdnm82aljOlkRdwfGnyizJx8_nLwZrlRKLK6JHQFET5FLSH4ezlNVBOKFo1la2VbAhDpBHVb-UyyUKyQG33jI1dmI3V_pcTcD2a7myTjsphVn1BCAiWFvTScAzod5fI1zEO_V19eBmRL08xYPBKg0CKo6xuOGzCsAFyVabsLOqKPoEGaOXdKU_SeRF9znYbAaUmyPHXYm01yXt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xx1e1rMFe08xfnYfvrwmoeq2ByvOGKcwYIviKvFojOiC7hSvorUEA43nWxjEOtt3Nk2_ffAX5Na-hupsOBzWImVncGBjFHRxQKU4lYjrpDWH19kamlhoGsdMZVzxICc19nksVM3MZvzEt8-9jw7I71L-MsI1JI4o7HqoYvNfeA_1r515cCx1VHJdgiMk5aGcJFH0BxvyzBNSjn_iHaqE15932aGNUrFe3uvv5q2fcL79fuIYeneRulKVfqKihilAx_M1wlCMRZETkjCrZdpqtwP1ZxcbU7mQBif9NKuHND3bqCH0MZBydxSEukmIiIC-BEeN_leBWYsejgG_57u16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUKCGSX-IxfrmBnXQDlxEgg9ZS9Rm6QxccG-5YiIYkBX6cKZGBJhHOXsCoWlu0Y9vZIYSSqR-UbUlobL5JCBBs6e978B7IigweGc1DLkbYILbcpdXnObpXkfSv6Jy2HEteCHAtDeGEQ-HMsDxB6bG1UlIRaAWraN6XKS8FHJMxw7PnyIbNxi2kAHFaZCupPm3CRgOadIhevn60ROeZgnRDg_6BmHlMVFhhlMwdain-lpfJoUlkGLjEUhCJlln5MjbDKEIMP8YZzR3VrJMEeHgSqKL49esVTRhKXVjbOywUNYdvzL-8-8Mwhbdc2PBMRQLg3SNXO1sElB67bIPUap_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLwIXa5EVBi9a3AJAtc4xrPvpoIRzsi_ZLMT-arPf4ZUtgBMA_wP1glutCRR7g5d3kjWr4YtZ-Jm1sMz_CPnaaL7dMGXasr4ffjHuFcmRrFc4EgrWQa62ZGVXhC1FasOeajTujBrPei7xNPmSzF2I1o6i6dTO2kvF1hbnixk6v-dumYjJiss3pSpyQD0NUe3vWGb0244Bc6kso2ybvF883KjeAvT7YNVP36iOWMD-UvG0DJaeKB7hWCxb1GEKcJVWjNmtgapu3H3CXS2mftdGnBOM7IsBjCLTC-qwXbUJ9BErDq3aS5yHxFfY2vHT4YSOryKaAz45vP7NjvHC-1UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J73-9VW714PNkEPXEjYpXqI7RTkb1_k-nbE66bYNRK2rWm3GWEYJ2OqSKppsNoO4y3kjOutIw6Wz078VlT7buDlrWVNMbOrnvShaET5aXhxKveuBplc3x9gniH7fJPK9vpPq03a3XuidPbk1MS85vadvsmlUrC24kX0OjzfAroepfp5_ZCcLS8xoCQF9mTWRlo2MEYrE0XZj1Qdn2kgSizgkUEUVLq5edT7xqwpE9qXNuTOCGdzMqTdDryb_nKEu7ZQbSXoSWkiFvLtDUSOfE9k5Aj48y-1LEAk8pkzqzBvAHrYUuLbKtUwiNRX1NGfw9qONj9_XHfcnhTbs4FGRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp_FJtVU3DnqyxITKNLhmcy2AKpjWmcn_OHVjrxySZIdulX9TCWNDI3x5SvvTBuj4cvAiTAiOYwp9BYmD8zYyFDm60oE5H4tx7oa0rqaC-BQzK-1vBFXgxF7IJDCUm46Ohu3dQXKoJ7cew3YK-jDbQkfWYPeVasGDCRnua-DbDGCOPvyHl_YYrkKe942tIi9lIEG8qn6uXAc1q_vuQLFUGZ1ebZUk06mQ2J8aa-ZVSj87CSGQzXA-MwL3QXSCgqYcuMJBl25YyHzWOnE6bQYWDKXTHfxS4elYwqAQRUYXNmfzE4C7rajOS9ZYl0u48Zrcy4yraEyVeU90eQ0Jxs8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7IyF2ctx2wZPpVKmnwzpfPvwP3QsdOPhhoxEpq7pvRgQphX-LJf2l_6Ospi5uQGQn4gMPP_pL0JBptNaDX8g6MbW0LXgKiQ1zzC5komBAAmbzA7tHPdGCMfOfpu_6ncE3EJgmqMUccHvIgIsOIQCqCNUkqf-TtrCIr6z5IWiSKXWCEZH8nBqh4vx9aEaab21CWPj91hqe451evGqYly6-QTPADGPkHWDwmrbAvYhwpok86ayxzwt3e0fSEJE1sdHdsKU5HhKxtst_66_tANpE0fIDl2QkbOhUcOl8N5JTvB2WzSTAzWguyjM0HOGVgph_mrCQie6T0RASZI1mXpig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایش از خیمه‌گاه کربلا تا آسمان میناب در قزوین
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451862" target="_blank">📅 14:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451860">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6918e70.mp4?token=fyxddGVSyeISu4i8VIgACbXljLl3wR3a6F6_eT7lwCfu7oHzvUNDLEQh38W9itZbmiPH0bSrEvUBaq2l0LAMFO22sLOYnZhufUORBZn3KVdUskZKyFyfgKpeN5Z43hw0d_pjqaVDBroETffOfRSKI16RlucNG-dRRBiWBoKPsVc0rvSXKZJ4pjtbmIYi2rsnnPPO8_G7kLoW9QUwLgLee2LxfQ2-ioBN6lRvdOj-UmLoojEwoyhfTqMacX31XjU2FHMp4e783gRxG5Hbt6PDqgy4-gr_HYiH5EkWvmOaLrFO7itZMeYkEN6vOeZqMiUBWoQuCzNdrZzkkDY6MkStuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6918e70.mp4?token=fyxddGVSyeISu4i8VIgACbXljLl3wR3a6F6_eT7lwCfu7oHzvUNDLEQh38W9itZbmiPH0bSrEvUBaq2l0LAMFO22sLOYnZhufUORBZn3KVdUskZKyFyfgKpeN5Z43hw0d_pjqaVDBroETffOfRSKI16RlucNG-dRRBiWBoKPsVc0rvSXKZJ4pjtbmIYi2rsnnPPO8_G7kLoW9QUwLgLee2LxfQ2-ioBN6lRvdOj-UmLoojEwoyhfTqMacX31XjU2FHMp4e783gRxG5Hbt6PDqgy4-gr_HYiH5EkWvmOaLrFO7itZMeYkEN6vOeZqMiUBWoQuCzNdrZzkkDY6MkStuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دسته‌های عزاداری امام حسن مجتبی(ع) در حرم حضرت معصومه(س) به‌راه افتاد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451860" target="_blank">📅 13:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OPL1BfA4ba0qz8fUB_APe21rtdO4-af4zmRzAwHHop2-ahFjP0ldkafalKIf76Ei96uSxUhzQNhsd2zrhBZBjzDy5SU1_xV0m3OfCo6R-VriBenmPMcM6FBXEHSyEnFrmV8qTH9kdThrwxZUq2nmpR5POkILGPMHjWajizVNKfMzNnP77ptQ9KAM9c0tAxhmLvOYHw2G8lXR-4MXImW2MPdKO9QQWJ1Vx4THDeTjwFHDkqSqdLPrQpGLuM963P-RSPLbOepqGbYR0NMvnMQ5LhgXfpREEYt4v2K9DrGVbvVbM53ADnT9GoOGdiV8se-dzMG7RpwJ3ttgrXb6JL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار ابن‌الرضا: نبرد اخیر به سکوی جهش فناوری‌‌های دفاعی تبدیل شد
🔹
سرپرست وزارت دفاع: در جنگ اخیر دشمن با برترین فناوری‌های جهان آمد؛ نوآوری ایرانی معادلات صحنهٔ نبرد را تغییر داد.
🔹
هرچه دشمن بر پیچیدگی فناوری‌های خود افزود، توان بومی ایران نیز متناسب با آن ارتقا یافت و میدان نبرد به سکوی جهش فناوری‌های دفاعی کشور تبدیل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/451859" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451858">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تکذیب فعالیت پدافند و انفجار بامداد امروز در پاکدشت
🔹
سپاه استان تهران: گزارش‌های منتشرشده در فضای مجازی دربارهٔ فعالیت سامانه‌های پدافندی و وقوع اصابت در پاکدشت، در بامداد امروز صحت ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451858" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451857">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
دقایقی پیش صدای ۳ انفجار از حوالی سیریک شنیده شد
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451857" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451856">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP0AZoMp9FAiKtqnlVp98xQaD72_xjD0TiJFOxCQqmROC4TG9E5SSgC4d2_YOv_2mvcjaPzIm4EFkC3zsFHNiLmlHL1rTPHyo5hThHXbMKdwku-BefPvGxoAVbdF1ZoqfXLusDEb-gMXJA_e5mT9ugvZitPxWrI1J59qxpFycH8JoYZsrZcv2T7g_iovHjs5N0ZZgl6LSM-hcTuNh52tveFCpKfEGbyA3y8RmoFNHPusr0vgsUEVaf9csBxubJHasffDxfKmUOFnDwhgkh08xLYG1jv8wVKcNin7iBMNR7_1S815684Ubp6lOZcihJYkue99ZuAqW41H_5BkpeA7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ کشتی سعودی مجبور به بازگشت از باب‌المندب شدند
🔹
خبرگزاری سبأ یمن به‌نقل از منبعی مسئول در وزارت دفاع این کشور نوشت: در ۲۴ ساعت گذشته، ۶ کشتی پس از هشدار نیروهای مسلح یمن و اعمال ممنوعیت کشتیرانی علیه «دشمن سعودی» از مسیر خود بازگشتند. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451856" target="_blank">📅 12:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohw1i6lSiHWhFiI-SoBmkIG6A1jrtblBip5MGwdV8eMRiMVrUedZ6gkUpAbk16tnHok2y637FvhKcZX-gCzcHrOWz7F4wVPGyy3WH9rlyTTWu84UnM6aDkf9KChrB6t4jtl0lwa_ZP087CpUR6N7CABk9Hm6PB_OB6xBdXBv9HqjSX5YiFe9WSYGhOjIKZNakv-ym55fm1HCr9IQIIW77e-ngx_VM41IV0DiRjjnfLtzw66RlqRVUv_8QgHAvY8KhG0aK-jvQI9bgW76EYaWPBFyPX91ohwsEZ8p1k8Ce5ooFYLJGRrgfwHV3HMmdNDrzeomi-TiCXRDW1gqR-WjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW-kFAVJR_HbJBwbNGF8ZMnqVWtMizl9ckvTzWF1SdrLai1ff4issHpPZjE1OIvLI4j49sB-3hl1YGkdtWYPEI-iXBdMdk68LhvcTzKEUKyLtOhoRA0qynA0c47hCUHFoj5YPixAzgdbIMgd76l71m7X0gFlqRqk25T-sv2NXxoHRpKMroL8eY-HhjHiyzDTsMbntmHhi4IcmtKPykMj1s8UTIYjfU5gFInPXZUfbu_BHn6zbiQlX8TUoYkmqVJoW40Ft6HiTjFBiMjhb9KtdoTPmBihdyAF9TBWEPFiena5d2v5CT3YUCDiBkgzxGT1bhMe6ZeN4VfXath4N7-6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN2ZUiEJT3-VxKN5ekGZgOGV3JrixSE7eQjYMSns09y9we0TprRjyWyWBnPpEZ2MdRDlgac2ryAdFjbndbvpsl5YmxtuuP_VVgjPk5vC3mcFmU78rrFpNVeCMeTIB1aq3LMz5MtzZgDSWy_s9R2iviW_LSrMJdxq73EEmsNW1ZhmIoYLSuqa2yLueIhlg_6g91bgOmW8rpEbWfo6GMjv6pDmS3ISDHOp3qmLf4T6ljwArm6BkBppLjC8O-j3ntLWPAAOzVx4AjaPtOOaLp8HzGcQlyH1e9qcF0Fe263wm4rvoF5c0QUOh3OimtA_gZqTFw7RW5H5zR2jsGKWrm9g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZZiqkWnPnAyPubY53Z1QLyIT6KNs1HYgM5gCJHiKFuEXHIvyaB32DC7DeJm0Y6cJ-b9bqOPLAj0RMc4_OfmNwxMcJtHujISnj97jAL3EZF6Nh83hWQeAajtdASpvIZzps8SPMeE8yYGzBgTHk6vQXYXOaF9HpksA9kmGJP__ALWvX9vCgPiz-d3ilYeJB-aznMYteWA_T6v46T297tlclmJn7SRySpaKkp7upeA9r2WLhok-eJA6gXblPUeFuJBiFojujLuRL-eMwAUIeARYzFiD-NmArzLoFtXd266z4eMYNZoPhplIgyKKbso1re4b57ekVjw-ladzOgLaf5pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrjdgmL2VCVrAPkY7v6GjzY1Ls0Ia_s11nxg6ZB7DhgIL3_6-YjeflKTr_Anst1APEVb3o9NayVPbfkN_pACkrKu8dHjY8Zmbew5kXKJh4L_n--AXx0GCAvx_RZvSXguPMKoDnrMo8m7xpLjJf2jJSqIlxVweC6Zwxt_Ml9A10czCEzCHOXUGyGPpuECiMM73TJR-18lEppz4lVL2-55OXtSKOwRkLEA9fswFnbaLYA9YTH-Peh90KWO2CO7Gb3diIwHnINB_0jVzcLpTi9otUEuOwgAWqWZkRbKpjDHjVJwXpq1nTNVRaLxC_5MXQGd0-wzRoFERvbdKOKn6t-Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnlO7180ZFwWIDvelJhl8wKkXv15XFTf6nIwvaR7ngBWd78z84LTiJ6XcGBp-a4FnNDvUdWXYJ0GbTImCDizmyc7J-ZbcD1t3zdC5gUFtBsCogIukvQgOs77XLkOFMA8DrfLsbG4WAfo12lV1n5KJG2raXSKglfQXQ_6sMl1wh2IjUc3-P73gBcByVqxYP_x13mWXxzDwJ70S4pL5BYpR4cbEFWkaDeResKomueUvt_TlR8vczdsT8LZICwv8B0p42JhicTxkFa_2LmHkPO2E3s7iSJI1eH0VM36gqfHClOaDkhkUAnIc8XCBOvF2Ep3mNoKKhXIK2fuMsqUiCjWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_icb74_GsiLmaWQ3_m7YgbkzksND6yrX0hxb_5QkxF8So-EyoGclJ3HYYI_JiB7i38lNhrRaN2Tk4H6NbPTnHP1sVH_NDRT4UkPGlr9nDK38-4kd39EqQj9Z3qQg3ColL7ouL3Msdg4SwdS7xACF365lqQ38xA2hQkElPV7VuijjG8W3bkMx-YTXuFq47T1Ib7olA_J8uCc5ZHbc_babjmcv_ZeHEPNbvROZWUstqv7nhLoy0cBFeJv2kQEFlIjXPHwUHvYjREH_CtSlEpyNG8oh0c6kN68wgt_PpqF8bbgcnDgE6BR8lkdQvjwwBz_7FunjNW1z3wtfsJdOOO_TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده کل ارتش: به اندازۀ سر سوزن به دشمن اعتماد نداریم
🔹
ما می‌دانستیم دشمن به تفاهم‌نامه پای‌بند نخواهد بود و مرتکب حماقت خواهد شد؛ بنابراین لحظه‌ای را از دست ندادیم و در جهت ارتقای توان رزم خود گام برداشتیم.
🔹
اگر دشمن پای کثیفش را به خاک ایران بگذارد،…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451849" target="_blank">📅 12:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYDQun4j8_FQA7S12GBEzY1QqghE1JZyW2_lOunyz5OQLqkgt2tyT2vg70SM1Tudbm0yC2OAmci8fDisI8nQSUH-cb3yUQ_KY8pbfQ6qTJ1xR00gHsr6R0knT89ffuB8yfyPKRlJfQPfIoMsRNhH0Mgb6mh-hZ8j5BeeXZOVZcerhhErGkU-wwTQVOx9vvxXXw9SDn58SZlcC4NTlJnLhlpx5sWhxZ_wSdG4N56pVhWYWC_4oh1N_l1nYKAYymrk8rijApZZuJZdnupJw9eB66agTjmKfysCSaoyZUpS1bMzDPUaBPSTwxrBlnHXzYmW9dgTrSZATI3DzXldBsvy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۴ هزار واحدی به ۴ میلیون و ۸۸۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451848" target="_blank">📅 12:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXLut2YCVS1x3Fb3SQ7j1uKusD-lre9Xv9F9UGUhCnh44UmpNtF7P8RvprwW-SwRE9_jAIpMVA8oHgFtru0nBbkpYyA9_wRrPiKyL-MvlPRj0lxd_tQRt1mkvnYXnATSSmH_aWF_t9_AbvPYfYYb5TYnv_jK-wJjnojT8-9I6_b6-6oou7qomI6MO9_2ymuJsSrmj75AcSGIJIHFrGAw2m3ZPcWy3NFg1MHTl6xIO_EakGdIMNFOdt02x0geJwz5PSQMwfEM6cAe-8PrkZgg1_5HwUh2oW_C9EjYA7xMkm9A9BcrLJLs-x1Glbonw26SaztdrCFev9UgcuoHfabOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
فرمانده کل ارتش: ارادۀ خدا پیروزی مردم ایران است
🔹
ما با ارتش‌های سران کفر جنگیدیم، آمریکا جای فرعون نشسته و تصور می‌کرد که هیچ ارتشی در جهان، حریفش نیست ولی ما ایستاده‌ایم، تنگه هرمز را کنترل می‌کنیم.
🔹
ما به آمریکایی‌ها شلیک می‌کنیم، آن‌ها باید بدانند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451846" target="_blank">📅 12:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451837">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">سرنگونی یک فروند پهپاد متخاصم در آسمان تهران
🔹
پیگیری‌های خبرنگار دفاعی خبرگزاری فارس حاکی از این است که شب گذشته یک فروند پهپاد متخاصم توسط شبکه یکپارچه پدافند هوایی خاتم‌الانبیا در آسمان تهران رهگیری و سرنگون شده است.
🔹
این اقدام در شرایطی صورت گرفت که بامداد امروز، مردم تهران از شنیده‌شدن صدای فعالیت پدافند هوایی در برخی نقاط پایتخت خبر داده بودند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451837" target="_blank">📅 12:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1fa10be9.mp4?token=BvLE_WpjtJW030wMxUMTwHSUoHJmBYrashif736YHGInQDHbQ308S1bRff8sW62WLmDzJn8KW8Igdnswjt1NYvxeug12okZDxLFDs9c8ou8WTA8qzq1CLYtw3tyAPaGmCsKzjq5MFWHhGT2_5nD0Ixpk48BplIDkXKMnNbLhnR4E5a4upbxVjJCsoq1wlEinqz2mtoW4njNvGWqPIsImJP4aCDvMglseUmSWVqnVmNko9Na3NJTqClJczHHAA8xHfBAbBLUPASDD6g8VfgakVc05A6jvY-ZRoWYe_3-IV7uKm2vP8gw16wmU3F2kYFWHhuLm0gwp-IkYDVuCSzWdzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1fa10be9.mp4?token=BvLE_WpjtJW030wMxUMTwHSUoHJmBYrashif736YHGInQDHbQ308S1bRff8sW62WLmDzJn8KW8Igdnswjt1NYvxeug12okZDxLFDs9c8ou8WTA8qzq1CLYtw3tyAPaGmCsKzjq5MFWHhGT2_5nD0Ixpk48BplIDkXKMnNbLhnR4E5a4upbxVjJCsoq1wlEinqz2mtoW4njNvGWqPIsImJP4aCDvMglseUmSWVqnVmNko9Na3NJTqClJczHHAA8xHfBAbBLUPASDD6g8VfgakVc05A6jvY-ZRoWYe_3-IV7uKm2vP8gw16wmU3F2kYFWHhuLm0gwp-IkYDVuCSzWdzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451836" target="_blank">📅 12:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/505093e0ab.mp4?token=hPWQIKWkcrHy4kE_dDWhceTqucl4oyqWENYMaFy9gT11_DI0T_7rjT9wv0YZMRmLnNh4n1B9rG8oQ9NB29EWfWO4L7AHQODhfpvn3ijRVEeFYzJuP-QX5MGT42qi3OkdppeO-H2V8jV02kzrN71UUYITJqavy7se4JzHFwCNUkodqg7PO-mryx2ui3ut6cEZK0QnD_ku7W-jcwSS_HzrMLiMuN9nh0f6MrXzqPsQPsG1QTxlqcfuSgAZkIUm5IvIzOak7x7gKzPHjphXjeOneT1XGRBAgCOJjvbY7Ad-jJp3DpAgX21_AptiE0EliHBPLiOjHB-pWArirlvx7JBF3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/505093e0ab.mp4?token=hPWQIKWkcrHy4kE_dDWhceTqucl4oyqWENYMaFy9gT11_DI0T_7rjT9wv0YZMRmLnNh4n1B9rG8oQ9NB29EWfWO4L7AHQODhfpvn3ijRVEeFYzJuP-QX5MGT42qi3OkdppeO-H2V8jV02kzrN71UUYITJqavy7se4JzHFwCNUkodqg7PO-mryx2ui3ut6cEZK0QnD_ku7W-jcwSS_HzrMLiMuN9nh0f6MrXzqPsQPsG1QTxlqcfuSgAZkIUm5IvIzOak7x7gKzPHjphXjeOneT1XGRBAgCOJjvbY7Ad-jJp3DpAgX21_AptiE0EliHBPLiOjHB-pWArirlvx7JBF3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکم اعدام عنصر فعال یک گروهک تروریستی در کودتای دی‌ ۱۴۰۴ اجرا شد
🔹
با گزارش مأموران سازمان اطلاعات فراجای البرز مبنی‌بر اینکه شخصی به‌نام «مهدی خانکی» ضمن عضویت در یکی از گروهک‌های تروریستی ضد انقلاب، اقدام به نگهداری اسلحه و مهمات جنگی کرده است با صدور دستور…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451835" target="_blank">📅 12:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451834">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=rGXC9hB972cxs_xrptbRoAqgoqC5N77q1YZmFspZtiBI2PtoMH8EY4lfWwJtYo-_4RculoZdXIDwbTKphfdOvc3VHQqmiPuvkycS7J86Dbgn-CYZGmA8_sor-043otdDHKdSdAObro8L5xBjaVwgXZmxpwj7H8lgmSHh_VlVlGMLfPw_z_57wzomBRIWUQ0lbScqkR-kSn5k5DgEglvf-QCGaEBxpDM4wMvO5IOZr3CHNiQTDx47iSAMq1QCg7hPAscsfNizfxVS2G4lFbqicKrI1CDvJWvC3wzul6Pi_WNSJvoPk6_4Ccjw486X7m1S7QpCbh2HzwXGnvGwk6y4Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=rGXC9hB972cxs_xrptbRoAqgoqC5N77q1YZmFspZtiBI2PtoMH8EY4lfWwJtYo-_4RculoZdXIDwbTKphfdOvc3VHQqmiPuvkycS7J86Dbgn-CYZGmA8_sor-043otdDHKdSdAObro8L5xBjaVwgXZmxpwj7H8lgmSHh_VlVlGMLfPw_z_57wzomBRIWUQ0lbScqkR-kSn5k5DgEglvf-QCGaEBxpDM4wMvO5IOZr3CHNiQTDx47iSAMq1QCg7hPAscsfNizfxVS2G4lFbqicKrI1CDvJWvC3wzul6Pi_WNSJvoPk6_4Ccjw486X7m1S7QpCbh2HzwXGnvGwk6y4Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451834" target="_blank">📅 12:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451832">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvpy1nNn0gsUVNKjiJnr6QCefVN0ZPR0mQmHDmzAAnfPjyE6dzTw9NKVKXkVcwC49Mtc9hnEzXfY7eeXY-FTjH_LHzJppnxqrLboLtbioWqfbQxgs1uBrIiBUY1p7wFDcfIqovjcmEbnVUMMXKaxoh4oLWToBvJJ7vONJSnBX2VQCoCc0Tc7vbzLGemylH_ySSJio4EDdeX3Qsm_YN5bk5xVTIPZhQ6tGC0ibTIcYFB8vpeY36CVq9RO6fmmYavaK-oEcS-D0o4A6mfzZW9KZEKe2lsLdl1g-uWWfm44H07zfOibefphLcHay-N3xp76G_jDgAHnVcyMZ41dBCAsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/getwCgfLX3BheQLksCfP6aJTr85AOjfBZvFLDGD_zZEsqc8y7iKEjVCUHUkf9l56u5kUaKNNNcXC17FXUf61plRnGQAdVplrHYp9CGN07DswLnGB42VIkSdY1UARMHwdq5HoJUp3JchzvDMZrgmR4Zqkz6ByFx34eGm9UeQ8FFjxyB2FajyRjMXf3_P-Ne62U-0gzLAicYONjsoSQ5Gr1mSP8i_3eyLUbu3-CQ8wTvfUqGZ4pKsNSF5xfsnK6IaYHnE-6GHjeXwGVIyoj5Fsa9eCEuQlGwhbmMWT6wNLDuJR_R5VVFBRqBBqLEmAKhJuz2gzLKMokKuTw8nSkTpwJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ پاکسازی راداری منطقه در ادامۀ شب سیاه سامانه‌ها و رادارهای آمریکایی
🔹
سپاه: فرزندان غیور ایران مقتدر ضربات کوبنده‌ای را به دشمن مستاصل وارد ساختند و با ادامۀ شب سیاه برای رادارها و سامانه‌های پدافندی آمریکا در منطقه، یک رادار هشدار اولیه، یک سامانۀ رادار…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/451832" target="_blank">📅 12:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv3PLTtc_c4LMghQ2-h7_2hPoZh-bhVAR8t8jeIhIO00lwVtAQdQ_GehpX9eF4a8Q9Y8uCfPLdJNzdvvSIl4Ru1EH7O5miABnlQzddnJp61J7PHIuKN1QwVjWXf6gXoGw7Xplsw9Isyov3uyAqJvAzZV_meULPgCBYkyXhQzt3lEgyfdEBjkMmvoksy6Y1255-_tH-hJNXP2QcoRaoUgIPmS-4gSX4Y4BOS3UFIDSki-J9nuugT4bEyAyFYwH_U_pQRJFZFdcfOS5OnxJz75ETdOBf8l8RW8sl1_6yQjEkuPmZFxfRhH7lTvt681zLuvOUBjTJUXU6YyMtoghHHtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر دیگری از بلندشدن ستون‌های دود در منطقۀ مرزی بین اردن و فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451831" target="_blank">📅 11:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451829">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQO9n3Tfg_Rj-HsS7Vkq5gBeSq834q8RlgLdINsrozUy1Q5XrzHgCiIMDj-GUIcetaDL5_-mGh898x56VdLe_-uTgNN6CK7mcqLGfD4BkwdJiqxBAufwtqHJJjFEQIi6k6FVTHFCKzogJuhZcIRH0R9jQtLMdPNFf5BIxtGBUgJbkEG1zhxh9xhxht_Y1nYD5MiA6M3ihtIoFthW7EyIoMCqFsUd7PJKlsCa-8eLjp4L8LWQzW0H-StkbieUuFNknVreX0ZrXUp8PK8NMXp7o_7mqwCMPRBGaWDNnGqKFeE40eVbag8NnIOyciWf9eCV-8ZTKoOjtJB7pXYgU8dyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h11S-fZO6KLdcjBRyCc6saDPlXdVbfQqG-gpQ7PtgCqhzZn9GAgXCW6BIo0FYyGEyYyydSY6xhPmq3lKbvoMj3dlODLicMke3mhtUouJE-cSoi0SU7qkrFbnnKKx0wGq0X5iXsJet7LV64YNDfUkkrSc1K99tiYJTplk6Bu8c0FAaIu20bU9tty-H-V47TtLgj2oF9KVHtyutnFkJmOuRFm_me-lW4_Sy6Scj5QgQwbtalQ9nANT3YKFDyByFZnKI0WDTvQV98g_5XI87pytMyHq9Gn9xznhSP0n8dkyxEd6OblqOxQI8bOFHrH4v_F5BTJ9Xwj16HlS78lWkjaVGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شبکۀ ۱۲ رژیم صهیونیستی: در پی شلیک موشک از ایران به‌سمت اردن، صدای چند انفجار در ایلات شنیده شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451829" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451828">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ac646b74.mp4?token=i1Z2HzXg5T-Y9BXpIWcEPPBsBoYeQyuOEzCM_MMdCefiGBCgq2YQgWEvdglcR_f9guLkP0BJTKSB8_4P6L-8l7YpBzjwNPHxy3zWJX04XsdfBNVg18fE9TJYccITvNfYnYqBiWonMYLE1qZHKbysHAa9dttp-xXGgUaqA_CTcOIKJr0glE-nWFviNmIJTf0W3wwgIsrQimQ11DLjpAOKG2d9CWAn8vaBcanWGsJsRrK_aJSFjBMYStodlPI-rnDC5xhxPGm4-kK65ICPTNzmry4KlDerDz74FI2lBBr0_Vmdr5_xyVtHcJ3ktOFvxookEQBbbpmCxRPmf0MsUAf8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ac646b74.mp4?token=i1Z2HzXg5T-Y9BXpIWcEPPBsBoYeQyuOEzCM_MMdCefiGBCgq2YQgWEvdglcR_f9guLkP0BJTKSB8_4P6L-8l7YpBzjwNPHxy3zWJX04XsdfBNVg18fE9TJYccITvNfYnYqBiWonMYLE1qZHKbysHAa9dttp-xXGgUaqA_CTcOIKJr0glE-nWFviNmIJTf0W3wwgIsrQimQ11DLjpAOKG2d9CWAn8vaBcanWGsJsRrK_aJSFjBMYStodlPI-rnDC5xhxPGm4-kK65ICPTNzmry4KlDerDz74FI2lBBr0_Vmdr5_xyVtHcJ3ktOFvxookEQBbbpmCxRPmf0MsUAf8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: دستورالعمل ما برای تجمعات همان فرمان رهبری است
🔹
فرمان و رهنمودهای رهبر انقلاب، دقیق‌ترین و منسجم‌ترین دستورالعمل برای مدیریت شرایط کشور است.
🔹
هیچ دستورالعملی برای پایان یافتن تجمعات شبانه مردم صادر نشده و این برنامه‌ها در چارچوب شرایط کشور ادامه دارد.
🔹
حالا اگر کسی پنبه در گوشش می‌گذارد که نشنود و بگوید منظور رهبری این بود و آن بود، کاری نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451828" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6e664d9d.mp4?token=phG0FvP955eHT0Yq2qhCPkfg59isoHmh2GdahMbSTHh1lzbTII2Zqyxf64fOgf4XSTp_uizhBT9P6eE__kO8Cwdx-ShuVINVZuuk89RyxMI4OtADg5vJ_TcX3QsVbvwXBaFbQtqXBT4036FxcJGWqJd45HTxCkvBbrKpYPA3Fnt8sKpND7hQJ9eC4SYh9a5qpYznbbtCA60xlwsLeTqLGUsus3tAUZ44Tz2Fuf8r0S5k-aakuAijJaO3i_6_uHMilhz88dgTqSP9EGppU3DBHP5j6Tg18Vu33gzfbJNAXRmOj_OrjvOZ_pciKgcLQ1kkgrT-tpLDKeDKtGpj0EoTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6e664d9d.mp4?token=phG0FvP955eHT0Yq2qhCPkfg59isoHmh2GdahMbSTHh1lzbTII2Zqyxf64fOgf4XSTp_uizhBT9P6eE__kO8Cwdx-ShuVINVZuuk89RyxMI4OtADg5vJ_TcX3QsVbvwXBaFbQtqXBT4036FxcJGWqJd45HTxCkvBbrKpYPA3Fnt8sKpND7hQJ9eC4SYh9a5qpYznbbtCA60xlwsLeTqLGUsus3tAUZ44Tz2Fuf8r0S5k-aakuAijJaO3i_6_uHMilhz88dgTqSP9EGppU3DBHP5j6Tg18Vu33gzfbJNAXRmOj_OrjvOZ_pciKgcLQ1kkgrT-tpLDKeDKtGpj0EoTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: دستمان آن‌قدر پر است که دشمن را سرجایش خواهیم نشاند
🔹
ما برای بدترین سناریوها خودمان را آماده کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451827" target="_blank">📅 11:28 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
