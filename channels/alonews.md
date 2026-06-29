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
<img src="https://cdn4.telesco.pe/file/SAD2gRopAA04krslXDmRC2q2P7Njjv-B7xhn9_Gt6r8BhppH_VbnYRRMURnUWrxBzHbOlUE9Z6IX_N4VHIF8BP-ZsOh5njNZ3FlsBsjghsswC3RI_WUO4KkVYarF7-MGjx_flhitWnbeDx6993UlNojhYgh5AohVmw4EJxKlo8T8pgn2_8N2npGnIbLUhJ09IhK7vjertztabP1W7_bfYnAhl2_HoZeY2Qt7qf_Ro8hwjbQsKcmYcPn6f03dlKMn6l2EXP_3LyfbScqEWhjTtgb9csW8q3uN9JL7eB4WdwKRdmkPk7L8lU6gR9VgKf_KS9czwOEDyZHRxhnblaMHvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 929K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-130949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 28 · <a href="https://t.me/alonews/130949" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=NFxzZFgARXStIHcb5SXBIPVgNNehQ0DWA2JueSJqqXlUI8N4osKHdnru8llNYvMVXytroMI7gkE_aAao-iKv29sclo-kp8ziGe4ihUDLXDFb6NTl2jbhj6HLjg94c6C8t841u6JkJC0H8VSAR-wLgt0cJYWuVdcWWPBrfmfCWq8y5p-wVeT1TcMmc_blLgfSRFtB4JLClG1veMxlWV0ljFnnNv1H39reIaahrUfra5GFIDgQeLphuNqij6BPr0_wcATZRerQJj7lQcMXTP9S8mnWzOMsel99GvTMTkyCLY09-njjqJw7wV_zDpBzhgpAq5Bxi2VmuXZE1lMJ1-MNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=NFxzZFgARXStIHcb5SXBIPVgNNehQ0DWA2JueSJqqXlUI8N4osKHdnru8llNYvMVXytroMI7gkE_aAao-iKv29sclo-kp8ziGe4ihUDLXDFb6NTl2jbhj6HLjg94c6C8t841u6JkJC0H8VSAR-wLgt0cJYWuVdcWWPBrfmfCWq8y5p-wVeT1TcMmc_blLgfSRFtB4JLClG1veMxlWV0ljFnnNv1H39reIaahrUfra5GFIDgQeLphuNqij6BPr0_wcATZRerQJj7lQcMXTP9S8mnWzOMsel99GvTMTkyCLY09-njjqJw7wV_zDpBzhgpAq5Bxi2VmuXZE1lMJ1-MNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/130948" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJTVeSfDzEIThxlBMJ1V_u78JeI8VzJojRubYo6PFX_7-KokiDRf1SOdXU1OtEbACqPGpQKwYPpQb4bXFQXkDOKsezNJaY8UjGK4xGbWtlOdIFnoxqqa0MXu5NIRA2kssbKCZci0rHtqL1V0lJ7ol9DJJDUyLFpAG4uNuu3tGirWtzGr1M-ikf1OxPEcJCsgRkl1R3_R2curc6aXqim-p9CvlNwV94nXoH7dJp_3yWpEpXNxVBvO_jn7snKoRNdcXWVrdUE9ekHueA0DO3QVV9r7nzfyClWWLGNWY6AUKog_kaBaC0PDKwzVX-cbuLH98mTEpT2WZ9WmWxo0UWUs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژاپن موشک هایپرسونیک «تایپ ۲۵» را برای حملات دوربرد عملیاتی کرد
🔴
نیروهای دفاع زمینی ژاپن نخستین یگان مجهز به موشک هایپرسونیک «تایپ ۲۵» (HVGP) را عملیاتی کرده‌اند؛ سامانه‌ای که با هدف تقویت توان بازدارندگی و اجرای حملات دوربرد علیه اهداف دریایی و زمینی توسعه یافته است.
🔴
این موشک از فناوری Boost-Glide بهره می‌برد؛ به این معنا که ابتدا توسط یک بوستر راکتی به ارتفاع بالا و سرعت بسیار زیاد می‌رسد، سپس سرجنگی گلایدکننده آن با سرعت هایپرسونیک و در مسیر مانورپذیر به سمت هدف حرکت می‌کند؛ قابلیتی که رهگیری آن را برای سامانه‌های پدافندی دشوارتر می‌کند.
🔴
«تایپ ۲۵» به سامانه هدایت ترکیبی، ناوبری اینرسی و ماهواره‌ای مجهز است و برای هدف قرار دادن شناورهای سطحی و اهداف زمینی با دقت بالا طراحی شده است. ژاپن همچنین در حال توسعه نسخه‌های پیشرفته‌تر این موشک با بردی بین ۲ تا ۳ هزار کیلومتر و سرجنگی ارتقایافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/130947" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=Pooik50Y6iBXae71om9vWk4lpQw0-NRMK-4WplUf0KjCIMlpsKK69lIqMNspzm1AEhSOI598lFoM7g-Vq0VQKWN8hlKc9wMJdC0wc1-0pvYf8sBMne3L8eNMAxRFbmn7jJJ3yJV6tqYpUYxouDrkeXtmeATgz6-gaetr3XpihjWhe-Bk0GHVqWzogJVDlCm-PZA0NHftX8qfJlJ_BoKxOzpgc_x3uIeBFSXXrisx-t6FbiHkPzPe_AYNqcWJDxYwnP40oLNofw8lPxAk6TyX368a7lO34iS6N1nekO027ReWvWOMmJukYdCfYBvBcfM3pqJYbSgpZUS9HDjXqYNGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=Pooik50Y6iBXae71om9vWk4lpQw0-NRMK-4WplUf0KjCIMlpsKK69lIqMNspzm1AEhSOI598lFoM7g-Vq0VQKWN8hlKc9wMJdC0wc1-0pvYf8sBMne3L8eNMAxRFbmn7jJJ3yJV6tqYpUYxouDrkeXtmeATgz6-gaetr3XpihjWhe-Bk0GHVqWzogJVDlCm-PZA0NHftX8qfJlJ_BoKxOzpgc_x3uIeBFSXXrisx-t6FbiHkPzPe_AYNqcWJDxYwnP40oLNofw8lPxAk6TyX368a7lO34iS6N1nekO027ReWvWOMmJukYdCfYBvBcfM3pqJYbSgpZUS9HDjXqYNGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آزادی گروگان‌ها بدون پذیرش شروط حماس و خروج از غزه ممکن شد. فشار نظامی، فشار دیپلماتیک و حمایت آمریکا عامل این نتیجه بوده و اگر اسرائیل با خواسته‌های حماس موافقت می‌کرد، رهبران این گروه و دیگر گروه‌های هم‌پیمان همچنان در قدرت باقی می‌ماندند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/alonews/130946" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pANbjAFKV6dUmntHnNoMTXL85loK3ZNLddiFmM-ipUWDaxptRTu8bMloznRL-KpCECSDGCToDuHLRiUIJtbp6VhPnno3D_rMhsGaVemSQKXl9G7kat-iQlLZjWPKjzpdl4sXQt8zsYRl9d_cb1mEoWYQ4o4g3jq4k2M90PNREi_PyW8VVwAvIj66_H12dn3F5-Elk5Kx4Chs1b6il7NNrZx5IX2Wt6DcqF8oh2uc0GZNvJ7whs-8WMo1K3OmOuYnBvVPVSGlulpDotX7lcaiOdxuQgmwsYtbwuM2ts6sE6R0tMLxSB_dxekNOSruv6dqxFGuS43A3sigWxB8e3NaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری میکند. طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمیدهیم.
🔴
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آنرا با تحریکاتش پیچیده تر نکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130945" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ایران اعلام کرد که برخلاف ادعاهای مقام‌های آمریکایی، هیچ برنامه‌ای برای برگزاری مذاکرات مستقیم با ایالات متحده در این هفته وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130944" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی دولت عراق اعلام کرد:
دولت به کلیه گروه‌های مسلح در این کشور تا ۳۰ سپتامبر سال جاری،‌ هشتم مهرماه آینده، فرصت داده تا سلاح‌های خود را تحویل دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/130943" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsE9nGwaQ8V6hrFFQ9TOH_mmbt-zhfwa02xym-y5MagdRZdJQ9M5E7RtHaREe3MLAODXDMgYT8xYRhzMtn8SnqmV4i6pw77YEmh2JQGTpxCGsljbIzDjae4yP3E_uZqkVQy7AXZSmn8KwY98k-kDc3BmtJ5vkl8USdg3jOCFcIOqEyrvOVsnBvVDQRDg6z1r7W1fuMdSHVFHMV0y0Hp6mxIqeRvfgm4UsyjnGABN7qfNMVWE0A9FJkGlBt3GUcoIB56_Fuphkd9-i208eN3zhSlfwkrsFByVJ6XsORiQdCT2mBfFxlftK_h_5n82UlTWSrrt2u0Gf0fqZ31bdsCp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده روز دوشنبه با صدور حکمی، اخراج روسای نهادهای مستقل توسط «دونالد ترامپ» رئیس‌جمهور آمریکا را آسان‌تر کرد؛ تصمیمی که توازن قدرت را از کنگره به سوی ترامپ تغییر می‌دهد و می‌تواند نحوه فعالیت بیش از دوازده نهاد فدرال را بازتعریف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130942" target="_blank">📅 20:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=tThsbdsGid4qgVcQIyCAxmNPtwLUb-eul-5uI0pv-Lm5OdLRZZ5ryiH5U5idVext9sVkh6MGa-M4iByCH4mGaDm_V8jiLLmOHCjwe1sXLWr4IqQJ-lCnVIhzMVpwvvjDTH8xO8mXLq3onC4B7gsUB5A-zSiER3arbEYoViBInQrchCaTWv2mhGjO_TWt7SrGgt1vv__FQ4w5v9W3WnIc0vjcfGea59FPgd7DLhqVxTcNSLml-NpMzHsFZtQMC9-6ik_d1VuF17FW49dqa2lH5dtAwkpUN5sKuS-GIRN7_4ldpWrK4N60T3jtf3X3HgGzhTIdESayjzU4Fm4OJ1Vrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=tThsbdsGid4qgVcQIyCAxmNPtwLUb-eul-5uI0pv-Lm5OdLRZZ5ryiH5U5idVext9sVkh6MGa-M4iByCH4mGaDm_V8jiLLmOHCjwe1sXLWr4IqQJ-lCnVIhzMVpwvvjDTH8xO8mXLq3onC4B7gsUB5A-zSiER3arbEYoViBInQrchCaTWv2mhGjO_TWt7SrGgt1vv__FQ4w5v9W3WnIc0vjcfGea59FPgd7DLhqVxTcNSLml-NpMzHsFZtQMC9-6ik_d1VuF17FW49dqa2lH5dtAwkpUN5sKuS-GIRN7_4ldpWrK4N60T3jtf3X3HgGzhTIdESayjzU4Fm4OJ1Vrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال مکرون (رئیس جمهوری فرانسه) از سلطان عمان در کاخ الیزه پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/130941" target="_blank">📅 20:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=HGBKCRxJ94blGuZ8S-DVDvbnujiWlKrPM8CgkwNPkGEObiumFhmNJukKf6Gb1wwafHAQBajQbS9SzXMIWPM8pP2x-95Z8_sEky_LjvOw_caAVo5COzTQFoL55F3MDIb7IqOcJTyKY0wVZogaGkpYPqEKCXfMjqITLTs5fghOL2aSH65D7YsJp53_qwtXYY_HRPWZf7sZc_7lG57yfbjQoUsam6BH9lPn9rkSq3tzy97UF1IfTq04bLJvC_VZOYrE8GF0mLprF-qmcsT34Y9yC1rCDFROtQUST5_zqEW11bOE2hIBXb_3ZlcJf4aAIhAn_cXo_ECEpH2USmez3wirkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=HGBKCRxJ94blGuZ8S-DVDvbnujiWlKrPM8CgkwNPkGEObiumFhmNJukKf6Gb1wwafHAQBajQbS9SzXMIWPM8pP2x-95Z8_sEky_LjvOw_caAVo5COzTQFoL55F3MDIb7IqOcJTyKY0wVZogaGkpYPqEKCXfMjqITLTs5fghOL2aSH65D7YsJp53_qwtXYY_HRPWZf7sZc_7lG57yfbjQoUsam6BH9lPn9rkSq3tzy97UF1IfTq04bLJvC_VZOYrE8GF0mLprF-qmcsT34Y9yC1rCDFROtQUST5_zqEW11bOE2hIBXb_3ZlcJf4aAIhAn_cXo_ECEpH2USmez3wirkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروژه تانک ساخته‌شده توسط دانشجویان طالب دانشکده مهندسی در افغانستان: نصب دوربین مداربسته روی تانک کنترلی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130940" target="_blank">📅 20:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نیویورک پست، به نقل از یک مقام آمریکایی: ما به ایران روشن کرده‌ایم که تا زمانی که در موضوع هسته‌ای پیشرفتی حاصل نشود، دارایی‌های مسدود شده‌اش را آزاد نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130939" target="_blank">📅 20:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: اگر ایران به اسرائیل حمله کند یا ترامپ مذاکرات را بی نتیجه قلمداد کند، جنگ با ایران دوباره شعله ور خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130938" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
والتز، نماینده آمریکا تو سازمان ملل :
۱۱۵ کشتی که حامل ۲۵۰۰ دریانورد هستن از تنگه هرمز خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130937" target="_blank">📅 20:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7J1fT_nAhnewIHgM9J8Jpsca-_XRpmJGY4M0HRQ3NjY2DwlPt5P4hQLgjNVQL9oBoJjgk4rNBHMBaoTKHa575TLLpqJPI3PV_9sVfOECx5MqWlgFigHbaxgPplW7oTaJHN3LvI4g6Aj_9mlIz0V6WOyNgRLFeL9Z4-nWXmfZ6qgr8CNQuQdcH1w0etba-Dx8TEwbOuv1RXwcpS2du2uXJBKzuN8zgR4S4JsM11Kme5O6JWKxO38QkqdeqoiaiSQ2sw-insnWG259WB25N2hrc50Dw1QFZ8bgx_QSDkOF5LMjzoApPWbyZfTn58k3WWCjsarvjHdLqnwikvRiaGX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
دادخواست کوک، که مربوط به صلاحیت او برای نشستن در هیئت مدیره فدرال رزرو بود، به طور صرفاً رویه‌ای توسط دیوان عالی بازگردانده شد، ما فوراً اقدام مناسب را انجام خواهیم داد تا اطمینان حاصل کنیم که کسی که مرتکب تخلف شده است، تصمیمات حیاتی مربوط به رفاه ایالات متحده آمریکا را اتخاذ نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130936" target="_blank">📅 20:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پزشکیان: برخی تحلیل‌های صدا و سیما با سیاست دولت منطبق نیست و انتظارات بیجا ایجاد می‌کند و منجر به نارضایتی مردم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/130935" target="_blank">📅 20:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سفارت ایران در قطر: مقدمات مذاکرات با آمریکا در دوحه هنوز آغاز نشده است
🔴
ما تاکنون هیچ اطلاعات رسمی در این مورد دریافت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130934" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6iP1hIHIgKEilW-rPUT2-lsLFgRKtSB1LrmHsQmJfi5xJ6Us87xbq4tPWswehSVr_kwjrm0Zs3g5P7E7s1t8-pEqXjvjti_gynLn8egn39Nb3rEZrvxK4H7YVOFOfIKx-6e1HLb7EoxknQhEfkvfpBcHF17-alDYkLoVIliwn9SQxAwTCA9gqglr3ijdynu--f6pjLTNTFpmXGOV9Jhjh8fI_9yrFsLn5kN81c8_ce2Oz-3XcmjvFqbvcV0Zg1OldtAxQeyCaLT1hXCHIBezxHrd0cDc0RqHOSLsnumlWSA2umlgxJ_4yWjTixZ03pJTQekkPpOXGgRR2k8T_ie0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره امتناع دیوان عالی از بررسی درخواست تجدیدنظر او در پرونده افترا علیه ای. جین کارول:
به طور شگفت‌آوری، دیوان عالی از «بررسی» پرونده جعلی که توسط زنی که هرگز او را ملاقات نکرده‌ام علیه من مطرح شده بود، خودداری کرد (عکس چند دهه پیش از یک سلبریتی، ایستاده کنار همسرش، حساب نمی‌شود!).
🔴
من به مبارزه علیه این پرونده تسلیحاتی و حقوقی علیه خودم، از جمله ادعای مضحک افترا، با تمام قدرت و توانم ادامه خواهم داد.
🔴
این پرونده در واقع علیه ایالات متحده آمریکا و همه ارزش‌های آن است و هرگز نباید اجازه داده شود برای رئیس‌جمهور یا نامزد دیگری اتفاق بیفتد!
🔴
ایالت نیویورک قانونی را برای مدت کوتاهی، که به چند دهه پیش بازمی‌گردد، ایجاد کرد تا به ناحق مرا «گیر بیندازد». این قانون به طور خاص طراحی شده بود و این بی‌عدالتی نباید باقی بماند! از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130933" target="_blank">📅 19:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr76_XP1uGtUgjXOOAoKO9CFVtOSZ3tEiF17-s_tX-5qlC97cS0BzQqiMAWSJZE-3LE7EPHGO5kwY7T4y8LuWZMbFuNOx7tpHcYxQz3IGbOcHEELI7-QAPfR8EfjMAE9xdfNVMvYA8-IjSL2ETyPz9v8vYNcyREQr6duQ5RENisMxqJRaN_lQTfr-1gQvODEcSjc4IRU5ddE0X7rItpJke3rUI9RnvXMlgf6fA9UrtSZF2EN5WcnNsgkpVEfZgL6iB8Vup8RR1grB2wRKsoBSTU4gO93thXiYHMwkb94rhmFOzcwuNoGGEwM2N-5apu2E_5FKoTyspupPagva1n0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
با توجه به خسارت عظیمی که امروز در دیوان عالی کشور در مورد حقوق رأی‌دهندگان وارد شد و این واقعیت که رأی‌های «مردم» اجازه دارند مدت‌ها پس از پایان انتخابات شمرده شوند، تصویب قانون نجات آمریکا از همیشه مهم‌تر است، که عبارت است از:
🔴
1. همه رأی‌دهندگان باید کارت شناسایی عکس‌دار ارائه دهند (شناسایی!).
🔴
2. همه رأی‌دهندگان باید مدرک شهروندی ارائه دهند.
🔴
3. هیچ رأی پستی پذیرفته نمی‌شود (به جز در موارد بیماری، ناتوانی، اعزام نظامی یا سفر!).
🔴
هیچ بهانه‌ای برای یک سیاستمدار یا غیر آن برای مخالفت با سه الزام فوق وجود ندارد. تنها یک دلیل برای مخالفت وجود دارد — تقلب! مجلس نمایندگان این قانون حیاتی را سه بار تصویب کرده است. به نظر می‌رسد سنای ایالات متحده قادر به انجام این کار نیست. در زمانی که یک جنبش کمونیستی قدرتمند در کشور ما در جریان است، که خطرناک‌تر از جنگ جهانی اول، جنگ جهانی دوم، پرل هاربر یا یازدهم سپتامبر است، همه دموکرات‌ها و پنج سناتور جمهوری‌خواه ما، لیزا مورکوفسکی، سوزان کالینز، تام تیلیس، بیل کسیدی و میچ مک‌کانل باید به نجات کشور ما رأی دهند. دیگر هیچ بهانه‌ای پذیرفتنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130932" target="_blank">📅 19:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خارجه آمریکا و فرستاده کاخ سفید در منطقه قرار است کنگره را در جریان تفاهم‌نامه میان واشنگتن و تهران قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/130931" target="_blank">📅 19:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130928">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROtpKj-ajTKvd9ay4jepeMEeSNe-R0_KBmZDEQuegifBknGIIMJp4NcxKO0SGQIQ5ko6dJLJ3Aw95gNEFt_jDfx_S_72IiCBB-jFeiwMFi6iUnLiLYDsKpXBl1ktmKig2rTUU0pgqPTpmZgBrLazwzLd_pshG462pVIZaSDC2Au0l3EKPWQnKgEfvxZm0Gqeteo4Dlj3PAfbO72qM9BAbtGG-18lpglgPm-KEOqrj1PobCYn3vw854a2XHPwbqEgalnGKqR8DnNNn8iiNSMmTK8ia2nZZ9osWlDgun16fYcJGuFAvkU9KiIR5f8oNaDM1YINkhcvmvf1SPaAfxT06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_umhogsfXPlTFR463AKZCCJnUGBYH_WPHXtjWuINjJxQOycBGJtClZ7WEhgVnLE9d0bJwKSPkLBM9fIVxq7tNHFaCyqdu6YUEC7l_kkj0CoV7hj2MqjUqqbfv_OTORw8rZXfN8uATepW_ae0jb52DZS0uiA8MdhHxGaBs0I067sjw5e2pR8-0SpvU0Nsg9HRv6JygGh9Q24JqhlPehcjmKDx_dRoqFCJjZCSXKzHXiX3L9uuqxtlUuIOymEQ2eBMDtPGG9WBLbcHpBMAbOuD04pOZ_QmaQme9WZo0ZeFFpd-7STSCgAj2E7INB0s-JIPXzeHNoH4Dy7OJxPS5clAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO4ZIpwUcyG-WCtNIH8f5USJYdH2sXpEgTr5VDssK-j65_h1aTYJQCvbzZoVMz8VDs4UcyYB5rJULn3Or6L5L0DO-ftD_fBx6oqZOyxTHIHyhS615xXy2Unef24GA3dgj1-ogrFufPwzXR3Vu4XlRqhxL8f_gkCQan2xg8lmTmnYlLzGFhRMSO2eNTA3kbfO2kth0mg6N0U1c23R5w2e_FN9Ci2WVQelK8c1-vTIJaBIliQITf1HDSRANFDwBwXHfnOspBFI7eKxEVEjd_s2AYc81KB5_hS01tGp3wLhiIpARrsX7YfTB-3mnJN_lRqFsMhrC263U4FbeNXsLnkzjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از اجتماع تعدادی از قبایل یمنی در صنعا، در پاسخ به فراخوان عبدالملک بدرالدین الحوثی برای بسیج عمومی با هدف پایان دادن به محاصره یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130928" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130927">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_4xnI3H7rkDAYB_XQ3b5orOTyIlpf8P6M8L0aYX2b4FYWLenN9TmNE3KP23-68sV-bJk1SugK4eFjHHOTTxeYu8r57Vo_5My-Bss-LgCI2m0yJtx3U1M_28fY7MKoQI4V6WAb_lVw_cImXGzia0OxyZnC9RRiTECPzPmIKRV77ALA0bWXH_3NSdgdAZRX42DLbT0CQEx2khgeAyVCY8tfcBMahV8jABDRyPCbVworq6cMw4O3_58L2y9Wjhfhh7GQh_eB-wmr9bHjNUahnlsvZz-8m2IHonrWDQlZqC6kv2-sDHCQoKrpQUVSdgU01U0YxMjNJ03pCQLFos6tg_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داغ‌ترین شهرهای جهان در ۲۴ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130927" target="_blank">📅 19:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی | لگ‌لس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqePbPTSA0-rzkvKzeJ6hIVREo_8TMGhr-QQWfyWnwWOk9U3l6mBj7GoMcVYDo-5lu9ydr0jbAezzMXyIpHj8kvquaqueawmzOgU6Gttnntj7m9qeD8JSwQXUgiqOKW6_VCA4tZjjUwFmErmE8PqgI69XuxY1pZ0OTDZVdDm5nfmzp13WFY3QBw7IFBLXbj5fU29WV09x5Um5_WtQYRVy0ozFs7dFQWD3KhjLT1C2gK_nmlM_mMCkYIfzAPRvtTr4JsuPeF6J6hn4_8vZ0YJuw1vDCARbXxwUbFEw-D-b0V3M4b2crl7GZVlQrnjQ0dVu3XPICDdWGAP2ZYp9ezmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
لگ‌لس٬ سرویس هوشمند
کاهش پینگ
مناسب برای پیسی و موبایل
کاهش پینگ و جیتر روی همه بازی‌های موبایل و پیسی
با ۳ سرور قدرتمند اروپا٬آلمان و خلیج فارس
مخصوص بازی‌های آنلاین
پروتوکل قدرتمند وایرگارد٬ بدون قطعی و تضمینی
برای دریافت تست رایگان کلیک کنید
👇
@LagLessBot
@LagLessBot
@LagLessBot
@LagLessBot</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130924" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqFNZvL4XWkJiti0rmJjK-wUOhyDetPdb1wnhVgyvMIgyAHq196OzxxOf-cM9oDB97ZbWCnvdU5XUjKzTxzZIVkw0UzkyhrrWv2yLYpbOnPLlTKtjaVTMEDeQkDvENyqe9ev1C4mdBfynvN_N2eGtKMEFd-1OGNQayf0ombXW0JgAqT1zzvIt6tG_uIj8W8jVreR6CjT5OftGzVEsD9JcG4xL6cmDTowpHP0-Dq75Q0BzQwbjOtuOWj8FlSjnENr_ZgDfvoPOS1rbE5QRhiXg9p1nZtI2nNhqZoi2H79nflHJAR1jwxavhx8jZfde4i0VdonsTrJxu_HcIjLShX-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع خبری از وقوع یک انفجار در اطراف منطقه دیر میماس در جنوب لبنان خبر دادند.
🔴
تاکنون جزئیات بیشتری درباره خسارات یا اهداف این انفجار منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130923" target="_blank">📅 19:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سنتکام:
بیش از ۵۰ هزار نیروی آمریکایی در حال حاضر در خاورمیانه و در حالت آماده باش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130922" target="_blank">📅 19:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlAvpDMShpN2mk4DmLlRT3UCaVOVKFrg4ak0230v7p_kjtfyAqcroF0NgOE11NYchPnvtipu9vJ1l3smo0MtNyny6p6KMCtDLOsHm2TJxkKLNjGTPDvFsyRTD6Um9HbqK6sF8zCoun7nXOTuLeodJPPdskXl8ZbLth4eQ0DkZddTgw1q95r1NCeEs4kQbZ97SyKZkvdFO0ZMF1ziyDJxDWpGCq0tMnJ5-tKcf2Af5hewOX1wUSMv6ppmaorFpCWh6VlDtqhfmHPYCl5Vm4RqulNlKAzGrLQ2QpX3YavLE-WBlyK35iXWsK2Cau-WteE9IPd_Czj9KvqU521LkBeLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خراتیان،کارشناس حکومتی: ساز و کار انحلال سپاه در برخی محافل درون نظام مطرح شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130921" target="_blank">📅 19:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک مقام کاخ سفید: روبیو و ویتکاف تلفنی کنگره را از توافق پایان جنگ با ایران مطلع خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130920" target="_blank">📅 18:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سیمایی وزیر علوم : نام رهبر انقلاب آیت الله خامنه ای ، در کنار کوروش کبیر برای تاریخ ایران خواهد درخشید،چون مثل کوروش کبیر تسلیم نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130919" target="_blank">📅 18:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: ما چندین هدف آماده در داخل ایران داریم اما اکنون اقدامی نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130918" target="_blank">📅 18:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxK8hbNsMwfLUCQVQaq_e-baHlPaOOO3nqeFHAHxK4r23QN0VmBrahCQKThENCGVe-l_21y8-ZAecn_JJxZdZR3HSpKRhevrQs83m6F_yV8AGD_iTvdq5D8mkRrWlSxR_uYNIs16gOeeayYvrkCbxQlAMPXIcrYwekUdJHgQ2kBGWOgYV2HJKaNFVShUyUEoBNvDu2HAV5uCzzdWX_iwSpJY1j6TyEFjJdhBvtR8rNmx9OYuaJWWkcBeKkhsjHrzVgk9mH9D-b977MNe3VBw9nM6Rvf229i59dNUe1ApMwCS23HfiEL5lK1AwUTpUA_4yd_NX5aQfMoY5nmpHq75EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه قطر: حملات اسرائیل به لبنان قابل قبول نیست/ بندهای توافق اسلام آباد باید اجرایی شود/ ایران همسایه ماست و می خواهیم شکوفا باشد
🔴
"شیخ محمد بن عبدالرحمن آل ثانی"، وزیر امور خارجه قطر در گفتگویی با شبکه الجزیره ضمن انتقاد شدید از رفتارهای جنگ طلبانه اسرائیل علیه منطقه به ویژه لبنان، خواستار اجرایی شدن بندهای یادداشت تفاهم اسلام آباد بین ایران و آمریکا و صلح و ثبات در منطقه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130917" target="_blank">📅 18:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxra78p51o-s60d5Fsc8_ApFi0x_8Vq1C_dSQcfEl1LJVvJejW8PtintjkNtu5Hk8weeuln2-Rhy8O_hhVhL_Z0onUwGXccGp4mM6tJOH_0JUwYAetejoV2Waf78cDlSjc0atR3M7_Oex6uISxuwzoJrDQQHoJW2bvJcIR9LMJVYZIYjg-aGixK9F17MKPMPfjoGRK5BmL7gatAfMMXr8t-HvzUcKYTb3v4H-qeFBn3Rgti5Zhq2y1bLMDippCu9FmIkahyB4JBO0Bmfc5YnVbCHaa3QZgvosHgcMigTHJfp9fhw-az_72H_Ej24IJhS45D-hAtOwGOSEasPt6TF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه‌سازی تاج بعد از صعود نکردن در جام ۴۸ تیمی:
🔴
نه تنها در هیچ مسابقه‌ای شکست نخوردیم بلکه به میزبان جام جهانی هم باخت ندادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130916" target="_blank">📅 18:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
طبق برخی اخبار گویا به هر بازیکن تیم ملی فوتبال قراره ۲۰میلیارد پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130915" target="_blank">📅 18:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeP4f3Gzf5xmVDemhA162y9SnrgCuupdixQG87ixt1Kcmfh9W2GUYbJ4QrkhQ6RPvZfOU-uxZC24u6d5-rzD7dWNXfI6CamumLEJg0DhtUoXvtQ2r6ZiaR2W6gMCLYYzc2ta6n8yNUpjm0jFLAlSHLHfV9xYnSDoXs-7YqkN9XushIPDQMbzWNjSYEnl7wlEqL197gPaeQrKCswLWx9ao103-izVK8r2aoYrqjvLjomVPwvvB6FD1eOh0eBeBMVOproHSpkxPfEhzdWlIMw7ghSnsyBfIOeV6dulxI0GcbsSuiHi1VbYbiNCQMJ7wyZeGxeMJIj1MsVz5IBoQXJRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از 1500 سال تاریخ درحال تکرار شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130914" target="_blank">📅 18:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB4sF7yFDP4O6H308mei4v9iQMJiCgTYrftcU7J6MykiVP7HnKee-9xWYXYrHTVceYRIpivBWXjObdiTraGzdGU_S0zMqz2a9-QD_KQ_SEntctUqm5mYmtYBdcbV2bowjS0LUQLP3gN3B0sXZ9CvT1i7HjZ_LaO940lOatP9lChzxNK7uzvp74_-v0Up8uBcw0GAjEXzjHgpzwxYVNxLmjKC3rgRSaddF7d4zArp-0FpdDJZH_NCQ0Y4GI7ob7KGENGQqc5OwZQxj63ntyRn7TiJaEoT0gPK9M0JvW6i3_jR2n0te1GrdQDmDJdZtBuchTXb1s2gS6VKofQ7H1zEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با رئیس‌جمهور لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130913" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=fHlI_iGKBY6JkGHqtWFbWD4HLmAZH1QH8G-JP7g6m6zGC_658Ko0rhGWW3iVD1fYb0s0nhye8aNWjYTQ389GGuYpypLgzIBBFh39yIkrYR_SxNEay1KnGvK4HhcQLv3oZ7ZPZj7n9Mlm2ZRjxS2xhlEWK-WhO-8R-mo2V2QRiXCQq6SVZPslUlC2fTHfb_FN4JsDEtjfBeIPgQzLjclq-OHEtdSLIxVxqODyRUOO514We_y1TCXdlKuQaCBwv1NJVfHzxIyQ6l_yCPeD239JLxm8PZ_VVB8kc3DCo8FfjqpGKjeSNCPW6kGqlOkNsqeN-twdISKdBarjG2nSc5eYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=fHlI_iGKBY6JkGHqtWFbWD4HLmAZH1QH8G-JP7g6m6zGC_658Ko0rhGWW3iVD1fYb0s0nhye8aNWjYTQ389GGuYpypLgzIBBFh39yIkrYR_SxNEay1KnGvK4HhcQLv3oZ7ZPZj7n9Mlm2ZRjxS2xhlEWK-WhO-8R-mo2V2QRiXCQq6SVZPslUlC2fTHfb_FN4JsDEtjfBeIPgQzLjclq-OHEtdSLIxVxqODyRUOO514We_y1TCXdlKuQaCBwv1NJVfHzxIyQ6l_yCPeD239JLxm8PZ_VVB8kc3DCo8FfjqpGKjeSNCPW6kGqlOkNsqeN-twdISKdBarjG2nSc5eYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله خوارج با شعار مرگ بر سازشگر به عراقچی در کربلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130912" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130911" target="_blank">📅 17:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130910">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130910" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXmd4adKIJh9QGCmjQkwug3GA6AFjNGggOdic-wHmLoVbPAC8XR_LubdmYONbdA7aYc7KAkwWbDVgjiv6CrlGZD2xtKMN0uuyZ3O4z_y3Q_4t9B4PJLTIFf2kGsB5hCm2TtkJUelxBm45Ebrw_17jSBtKm_O68YEo4Vm_I9S1Q55PJc7Q0IJLjeev79i9cjIa4Ax4OxcKA2zmVS9fTeHjZbg8vWEIl0BqlTOSSGUEy0hno46puRu_cVCosg6ntjM-W0CMwjx2Jp5edFlYSBGZ4tMGdwHUrmb0NZaVadRqJTjXzd1W--FNt8rvc9bWT6MDGGAXL6qmFi_WT5D33pnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=U3YBVPlHfPchfJecVSxa1c-iXTDWZoR7IV53YZ-yRqEKkisund8mzWG1oyzuqqp3-E_Sl0_JUI3ubUeG4XzFdPMbRTz0U1loNce1j0DNSf8FC6yaurH8i7aIFOBpmWiWDtShq3H75I18MwoE-PZfHGwO_PQeBIyIzp2k2FnXfCi0T201EWq3ce31YcVc3YwUYCFkoyDtf8q3Y4viz3izaw4ARBk4_QWf9U-OhpGQ2_GMqlHd5nCpK1kNHuxTnPgW_Nl6950InrCFamPYHyBrfjxgGMhkmthBxmbONV0Wra36jBtq3_sPojHbBUSvbmdor_Ow00nadu-IGSuYvmLlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=U3YBVPlHfPchfJecVSxa1c-iXTDWZoR7IV53YZ-yRqEKkisund8mzWG1oyzuqqp3-E_Sl0_JUI3ubUeG4XzFdPMbRTz0U1loNce1j0DNSf8FC6yaurH8i7aIFOBpmWiWDtShq3H75I18MwoE-PZfHGwO_PQeBIyIzp2k2FnXfCi0T201EWq3ce31YcVc3YwUYCFkoyDtf8q3Y4viz3izaw4ARBk4_QWf9U-OhpGQ2_GMqlHd5nCpK1kNHuxTnPgW_Nl6950InrCFamPYHyBrfjxgGMhkmthBxmbONV0Wra36jBtq3_sPojHbBUSvbmdor_Ow00nadu-IGSuYvmLlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از ورود دکتر عراقچی به خاک عراق، از دیروز تاحالا تو این کشور داره کودتا میشه
🔴
بنا به دستور الزیدی، نخست‌وزیر عراق، عملیاتی برای بازداشت تعدادی از مقام‌ها و چهره‌های سیاسی این کشور که متهم به فساد بودن صادر شده.
این عملیات با کمک نیروهای ویژه عراق و سرویس مبارزه با تروریسم (CTS)، خودروهای زرهی، تانک، سلاح‌های سبک و سنگین انجام شده.
تا الان 47 نفر تو این عملیات دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130906" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPSnGfEFXRHBkoBe9IIWg8VH7NgqLsE9AY932GdlmJEps_bWOr7gcL3zGhg-ZKQU3N8bvrQoylseLHB5lMdi31YcNHtzOiU2SrcelFMPXY6T_wwFx0UEtLP0j9d502Dn5YmqvXLJmrmJtTbWkq5DDTcuav5Xq61DMlLe74GYh6XFXfXT2JZxJfgtHRWxoikaqtK9-CfVJs2g0NxyX4nYKSdHiEeCeFkXc0elozWhYQ0qTe50G7JU5MpAuHLYXs31c0dw8b7Dt4fRdvwDv0deXp0U5OWz6OK-0wSxzORtYa_FEt4nQntKUO5kdrcMNBG-aNUEMlk5BwTzxvTFlQ2daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید — هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130905" target="_blank">📅 17:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کاخ سفید: کوشنر و ویتکاف به دوحه می‌روند
🔴
سخنگوی کاخ سفید اعلام کرد که فرستادگان آمریکا به منطقه و مذاکره کنندگان آمریکایی، قرار است برای رایزنی با مقامات ایرانی راهی دوحه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130904" target="_blank">📅 17:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / ترامپ: ایران درخواست جلسه داده است. این جلسه فردا در دوحه برگزار خواهد شد!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130903" target="_blank">📅 17:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سپاه : انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130902" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130900">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyakWpzqya0NsYhDj9n8QpS0Dm4Oa-g2pNX-Iqc9-snliP7gXGIA_WczWBIRyNZVQzrg7BnVWDyu5AjKjkBQ7mZOP8FCCGcCjrAmfu81ZscW0Grl1zo393K71C_ewKEx2aOq30aIruVd1DNM38Qlulo-hjXwOu0iRbsRACbucArW8zqIM-IY4yQhMQs5rGsfVwtxgzvN4NcGM7C801NYFeMSo8b1urcvndZoXdsfRf6esgv5daa0UudTka30l-d8xhvSmDhzsq_htfWplcLjLxUbDBYp_JZLDw2LdPg9T2Z7yCaUc8DCp5iiLvljY1A4XsmXKOYS00e1JsHUmwcRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOg2bAugkvNkdKe4RS-aZ_q_UGWd47rHqRw7xqzRZnFSPt9JopTV43tFVEOftcDjtcfdGeJ7I_6ai8dGetpxHfYYKMixCAJyCgb3jkZwkv1444TgBhDuryTRpLj2Z_sOhNmeiDEGGugutoy9PKApv3K80OWNsyDURck4zVs9mhcqgNJqmNZQRdBQB8ar7ghUgb98UnRD32IYx83dtXFPM_hPsEaF8CaUmEtxHLeXrnbtHpdp6lLSCaSgJuYD-pEHLxmBGHMmeVQo7_G_W_cKkj_PvoxukhzIKTJoSgYSEEG6Bg1kkRiYJWP4ZT2mUK2W_ofVANeDyGkYfTcN6aWnRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعارا، با وزیر امور خارجه عراق، فؤاد حسین، در دمشق دیدار کرد تا درباره روابط دوجانبه و راه‌های گسترش همکاری در چندین بخش کلیدی گفتگو کنند.
🔴
دو طرف همچنین تحولات منطقه‌ای و بین‌المللی را بررسی کردند و بر ضرورت هماهنگی نزدیک‌تر در مواجهه با چالش‌های مشترک تأکید کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130900" target="_blank">📅 16:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130899">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هشدار نیروی دریایی سپاه به شناورها: تنها مسیر عبور از تنگه هرمز، جنوب جزیره لارک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130899" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130898">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwjQyd1873wd88BTxHfQ9Yy3XMR5dQIcS2HAUB3HrzUDWjK3_np3EfbYwraNQrhNQ-trBiDbv0oOII_lCfO1YBpKDzQfw_pJ4mhd9yo9l4AwMlTil6dH9GItcHZLIMbTFWNS8K2EpbFKQSxbIcH8p-3rlMGf-1rsLzsKz3tdXpedX9U2V-R0u-tqPYN8fBYAtODKjUqXyHMJcQs6j0cjcySNqthfEVAG7fSwP92A0oE4AQJf6fkGAVvBo9NGrInWO2qkj-A-N5bmWYM-HdGkurAbHrVx07jTl2PMHtaSMQTCJ6_u7JyJjpSllvja1m0HWTfz-H-yssPT-iPuhqD0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: کودتا در راه است؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130898" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130897">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0oWYsq6N_Y1QC2VgRE_5ayklCTakl_ysHZtOhyNMIVPXAXdOoRWUJSbyM4zl3CjC1UQI6dZhUF-yj89WVziUwe3wwlnuVXIxh1jzH7Dg9OlhPArLld0t05J6Gy5qief2tE30fWjfSR0vYxdGZcQKTo3bBr4ss5ELv27i03k9rDA9rqMKQj83BFvM8EVO0C_qtnK5vw92Xf08t8h2RdestRbK5Idpzdsq8_wZ4c9XLFmLFUkuQAbYJtl9h35NkdKcVuvgPRnXavsTUYeNN4cmzgiEzODR8VyPxLaTNSkpdNHvchxow4XlopdVGGTAMDAZXRUHK2Ep_lVN22F5yd49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی از کارشناسان صداسیما : تورم تو امریکا داره بیداد میکنه و کمر مردم رو شکونده، مسئولاشون بی عرضه ان
تورم امریکا تو 1 سال : 4.2%
تورم ایران تو خرداد ماه : 89%
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130897" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130896">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر کشاورزی آمریکا: محصولات ما آماده ارسال به ایران هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130896" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130895">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
دلارهای کشف شده از منزل حسین منیسِ!
🔴
ذات سیاست مدارهای اسلامی شیعه انگار دزدیه
🤔
به عکس های دیوار توجه کنید، برا اینه کشورهای منطقه دارن جون میدن تا جمهوری اسلامی سقوط نکنه. ولی میکنه.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130895" target="_blank">📅 16:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130894">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل و شین بت اعلام کردند که اسماعیل مصری، رئیس امنیت نظامی حماس در گردان رفح، در حمله‌ای اسرائیلی در نوار غزه در روز سه‌شنبه کشته شده است.
🔴
طبق اعلام ارتش اسرائیل، مصری یک شخصیت ارشد در گردان رفح بود که مسئول هماهنگی فعالیت‌های امنیتی و ضدجاسوسی این واحد، تلاش برای بازسازی توانمندی‌های امنیت نظامی حماس و پیشبرد تلاش‌ها برای «آسیب رساندن به آزادی عمل نیروهای دفاعی اسرائیل» در غزه بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130894" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130892">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUmFJS8ynDAZQ-7DBMsbgMj_wgzkKXlvZ6M_nJgSo0-XCUNvhm4PWbxRf4a3hdCgr8RsFfCPfiR80mGL-rjSqA4DPobgomyUo7AFZ5mg2Y5gXbIy1yFMQ_PuDNEJ_okRgri2ZArkzbMOSACTBsEtpkbG1aF-cCen5kamiL1FBmU5UtARfe_kptg14UxrW32RomN8tfW1wh4HSbK9BwftSlzQ1NVipXQe2sd60itU2Ic_HjRbEYJkYcUGo9La9s0jDpeX4RYmKafZlae0xwpaJKCaF6R96YLm6vB79cZ9XyFxIvsTH2AphJ0zC8ye3KWh52vFzj_ZeADpg4HGZHW-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BArh2YFJWA6ifEAReQO4fYpyV29wgYZ4R5w3BW_fOPFctLg8Rc87xyRRGmIXvThlQCnnXo_5I-O7895NPWrWSzVP97jUDV2ezLlx2BsdBh5OAen63kEQbOdwkZ_5aIGm9BcOonwsaKt3aCkLpYakF4IeY8Su41Gfsy8UcgVBAfAtwzyLbRa5vT8GQIybAqu1i2t2kpP82C9dUw-zxX4XLpyelyUEnt8kGpm2m1aBxiVIU1S65iQ5DA4K91kmYLujZG_yODY7cAynPgaw27D5PDws60F_-vCwy3Qv69r1s1-RU6nW3FDiX9KY4oifdnaLN05fgvrArBeumsCPEUhRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر ال‌ان‌جی روسی مجهز به توپ‌های دوربرد نصب‌شده برای محافظت در برابر پهپادها و تلاش‌های احتمالی برای سوار شدن شده است، گزارش تایمز.
🔴
تصاویر مارشال واسیلوسکی، یک کشتی کلیدی تامین ال‌ان‌جی به کالینینگراد، دو سلاح ثابت نصب‌شده روی پل را نشان می‌دهد که برد تخمینی آن حدود ۱ کیلومتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130892" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W1Qe7PpOIRMnI6qcxjzVEWYHuITuannfvSCKwUHdvYePm-iyGs6HoxWqBFqIT4oNV1SmxY0nTa40Wvsg27wH2pDWu-dkYqQsSKRN7Pad_85L-vj2Op1mYF_fjUF1HOwzEl844JHiIFhZqQ16wvDSBnIzb8JhH-4N7weSs3W0tkQrPlFprhzzXBakd5OqTovbIw5kat1FjmnQ7zQZyVZn9G0Kc2TX3HhTuhNQnfxp2KEO70PVBHTdV7JHPHb4RXD8OMoSW8xx52RuFwCSSKr3fVpnNvmHj3lZ047zX7iMc-hS_lPvJOiLKtg4BChF3EplNHzbqs7REwya74rPXzglGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/roXAD0redwXETZjz7deglHn5MMeQDeAUD8mXyZSGGgm5AVjLdE2wQosUMwEfaINkNtBRScAgrpxtqSPkn1WCBeL1m8CvvFtyXM3YmPweKpzHw16IMQ1N0Ov0yzAOlcPvXZaWVUcPl8wPIBO3_hszfLB7wE02DHhBz_pWsL2bat-jMyGAEvSaYwwjob1AWq1Rv0UuvTK3-z8AQG6aa38KY_JHMNhG-lcxemeEMAf54uZbGwNH0M7t8wLXiVygwMDrijol-KSD0fqbBU794M6CEFNbnOmmA2--1v8lchmQw2sD5tNd0gv3ZK9L9fwwgreVwswiPV2ZKOMDRa2eV25IfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به یک ریل پرتاب موشک S-200 (SA-5) ایرانی به همراه موشک متصل به آن
🔴
سامانه S-200 یک سیستم دفاع هوایی ساخت روسیه است که در دهه 1990 به ایران تحویل داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130890" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت خارجه عمان: کمیتهٔ مشترک عمانی–ایرانی در مسقط، نخستین نشست خود را دربارهٔ تنگهٔ هرمز برگزار کرد
🔴
دو طرف دربارهٔ راه‌های تقویت هماهنگی در زمینهٔ مسائل مرتبط با تنگهٔ هرمز و همچنین تأکید بر پایبندی خود به حقوق بین‌الملل گفت‌وگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130889" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMxmpwfIDXxgf7qgOiKb4TpzPnaPhAfxro9KqcEtHmuo8wpJELff9LNYoXdaqHpErZ_kZpm67lDaZsM6ia5xzBpWQKk5vjBd9q1gISBmzp3kSZqNXrcFo1F6JOK7K4X5COzbqU0Oa6BwiMLqKusqH-BhwRVR9iV4729Cg35xyECR2-tfBWeHO39arrIBjSoZtTNxZ3EYbje6aXGxN4l5pap0V58VmpQFomWQp8NMmSrrHM9fI_VXfx1dVymDy3BWtFk3VT0ZD5hWq1C1VSnIRUKvZKDfcOJDai-xjU2BWdCLtEwq1I6a7DJrOY_DdopUoBEr3l11fF8muNLxpZCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اینکه خودمون بریم تحویل بگیریم باید پول بدیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/130888" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnXNbJegqcvhoCbRWQFmCHWInHiRSWG1AEykR20Ilp9w7QIac-XAzRwn0lk5JNcp3QeJtu9usJHOoXNc_VKAgQ-zUq1NolOXHWNqwtL0cacT1WI3rinxXBrWNRNekdHOPME7Nnuybl8-DFhLuzD77IctxzwR5hduSEJlykU_W0HKoqqd4sBE2hQzU63A5jze0hqWTQO38bor_bhDBrt4SnEMaIlmvzf4RfgRO0nRYnMwm7HCWFweGDoMoTJRTXQvwT6LDwIfJHBXkhTqQlzRSxOe02rwH9_aD08RBp_bh_oByT_vgq1VpLLP3VScSH8WX7odZoQHH-_uujyGXZtyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7eHwmNw4O3ReuTTvOBdCgh-9DO3GofTMFsyTWmqcNWCYz6BB28CUAhsHuPBz4G8hbbqLLFU_nvrYkLG4zc4csJfu53sDdQFINlSGU17gVMv2nHidwt_D3YvoNb6g-e6SbMIRqlgido-Fm7l2bggz16Crn7VXxB2QAoEeLolxb3Iia4vXhfGgs5lmRWXQ5q28FsIM42T0ocmXt3poxY3jTGnT8DenrXMNiX9bRFRjQBVkXuYiU65hXSJ-vBOPkXLRTa2s7kk76Y9ksYVz0-o3uXt562XWNZZ1pZ0kjZWpn2VCEw640lPQxjDPU0uxw1azDnvS5McFMJFLIhEV97HrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
دلارهای کشف شده از منزل حسین منیسِ!
🔴
ذات سیاست مدارهای اسلامی شیعه انگار دزدیه
🤔
به عکس های دیوار توجه کنید، برا اینه کشورهای منطقه دارن جون میدن تا جمهوری اسلامی سقوط نکنه. ولی میکنه.</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130886" target="_blank">📅 16:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
لاپید، نخست وزیر سابق اسرائیل :  نتانیاهو دیگه تو اسرائیل نمی‌تونه دولت تشکیل بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130885" target="_blank">📅 16:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130884">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
دقایقی پیش فرمانده سنتکام وارد لبنان، بیروت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130884" target="_blank">📅 16:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130883">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ed4036e.mp4?token=VgVOZz7EieqwWEeGQWBoxVc_D1R8_LSC-Dum_McTTW33l7Lwx1MEFIiMTjsm3_wwPdrGuEdKjhEFK84Tf3_hZcunxImh8Hp8McrCVJQA7HA6mskRAyHydmWm9hVQ4shbknYSknTegCSdAXyDK3y-PFZE651ZmKT8PGTpH7X0uUq6SESZoeqkQYxHiUM4Tlh-_PRevv7egcTgz-feosH-iLSMoD4Atq7slfTBUEWR7r6CNQ5f-ZVB5zJXKZkeu5ToZQWWKLuUeQCSa0m883h6ath-jmLiQ3QkgH9YJ3NhYtM7ye5p7qJ_ffeC9iY1u_9hfgQnp_30CpXL-7ae2avdxlZYYOg0RSE6u5mo5TEAvfOEqNv4tO-wNp5hw0ceuH1CFVGvmZaQ42JFPGGYCkKw6pMvCMoGNtfxiw0aPx_6BxgL7M8PcLV5M-Xmlbq7WH5q--QszdRUg-3Vj9SJH2G0_KqgnpVS-qFaSZRM608jyIiwx748UO6Wu8umIpN4t55oxPLsBZA4foDaQcn3OgSney9_naNFYzn2Npn-mp5Akapme1RiJ-bfNIdLypVhNsnc-Kdm4jYYEdzcv8Yqtj7Op6AbMdSxqfFuWj1nAqWqyby2W9bjrN3UOd7L6LdAeBJrGbLFCv8W9WPZfEzx7qE5xTvluncWnPzBBDNjH6MRSKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ed4036e.mp4?token=VgVOZz7EieqwWEeGQWBoxVc_D1R8_LSC-Dum_McTTW33l7Lwx1MEFIiMTjsm3_wwPdrGuEdKjhEFK84Tf3_hZcunxImh8Hp8McrCVJQA7HA6mskRAyHydmWm9hVQ4shbknYSknTegCSdAXyDK3y-PFZE651ZmKT8PGTpH7X0uUq6SESZoeqkQYxHiUM4Tlh-_PRevv7egcTgz-feosH-iLSMoD4Atq7slfTBUEWR7r6CNQ5f-ZVB5zJXKZkeu5ToZQWWKLuUeQCSa0m883h6ath-jmLiQ3QkgH9YJ3NhYtM7ye5p7qJ_ffeC9iY1u_9hfgQnp_30CpXL-7ae2avdxlZYYOg0RSE6u5mo5TEAvfOEqNv4tO-wNp5hw0ceuH1CFVGvmZaQ42JFPGGYCkKw6pMvCMoGNtfxiw0aPx_6BxgL7M8PcLV5M-Xmlbq7WH5q--QszdRUg-3Vj9SJH2G0_KqgnpVS-qFaSZRM608jyIiwx748UO6Wu8umIpN4t55oxPLsBZA4foDaQcn3OgSney9_naNFYzn2Npn-mp5Akapme1RiJ-bfNIdLypVhNsnc-Kdm4jYYEdzcv8Yqtj7Op6AbMdSxqfFuWj1nAqWqyby2W9bjrN3UOd7L6LdAeBJrGbLFCv8W9WPZfEzx7qE5xTvluncWnPzBBDNjH6MRSKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید: بسیاری از آمریکایی‌ها نگران هستند که حزب دموکرات تا چه حد به سمت چپ می‌رود.
🔴
شما این نامزدها را می‌بینید—این حزب دموکرت پدربزرگ شما نیست. این‌ها کمونیست هستند. رئیس‌جمهور حق دارد آن‌ها را این‌گونه بنامد.
🔴
آن‌ها می‌خواهند پلیس را منحل کنند و می‌خواهند مالکیت خصوصی را منحل کنند.
🔴
این‌ها ایده‌های مارکسیستی رادیکالی هستند که در تاریخ جهان هرگز کارساز نبوده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130883" target="_blank">📅 16:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
منبع ارشد ایرانی گفت که دوحه و تهران در مراحل پایانی توافق بر سر جزئیات فنی برای آزادسازی اولین 6 میلیارد دلار از دارایی‌های مسدودشده هستند که به گفته وی در دو مرحله پرداخت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130882" target="_blank">📅 16:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikg-wNq-yPcz2PFcXxhQJMrCbaYCo31OT3HNPW9rUu-WsRL6bbOXfwMIyvA5aCWwMW6jS75QmShZHp2d773sVbuGkn3qQsXCV_r4jn2xBdOo5yeqSlqyKN6Cdi27v2TZKS5Oeh_4Q21dyZXoolCi_bXsCJKt67rTkAqctAbJlViyuqEG90LjZJ4r3X9BmuHXyC_iPgmK0XboTwKH1MBTkaBNEopL-BTmdTISp1dNEuF8rUppvsXiZ6EiNGmi5Y9XU5yDVy9LkymfIxh44F2uh4j7ZUK5DlcWIAQHlWCKMmu0eFTD6t3LeKsy7AS2YNAYPPdIX0PvY5BoGSXyWmcpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن ازغدی: ایران باید با کوبا و کلمبیا که آمریکا آنها را تهدید کرده ائتلاف ایجاد کند و علیه ناوهای آمریکا عملیات کند مثلاً با قایق‌های کوچک آنجا عملیات انتحاری کنند یا در آبهای اطراف آنها مین پخش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130881" target="_blank">📅 16:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فاکس نیوز به نقل از کاخ سفید: گفت‌وگوهای فنی با ایران در حاشیهٔ گفت‌وگوهای سطح‌بالا برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130880" target="_blank">📅 16:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عراقچی عراق را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130879" target="_blank">📅 16:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130878">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: توافق بر سر آزادسازی ۶میلیارد دلار از دارایی ایران در مراحل پایانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130878" target="_blank">📅 15:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6c51391.mp4?token=ltYh4wMqW6oyR3XlCGpIMYGuwuvwQ3cs7ndpTdNZOq7SX_MTd8ZOnGESUaJsgFK4ADzDyjgbWDd9d1PdY_-d_R0ElXxUvLnOdbM4wbAPZ6T_b8ynAuL5LMvvL1uiSjHo9UA5KotxKcHLjc-CqBl-M2jN8OFdCAwEOt8AJzN8oCZmn4ylBO4Wv94NqBbB-LH0Pe-7uN9OfPP8h5LnKal6na4H5gFIDSGJ3GdUS0DTRRhvUIC_-QgOCcOWY-Yhpu3t_W3_3vHWylT1TZZW3safs3fCyVK9uVYkX6A5atafLc_NsmhgT6nrH4w6fWwPq6txNFArdGoRHnNEuerhYGGjDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6c51391.mp4?token=ltYh4wMqW6oyR3XlCGpIMYGuwuvwQ3cs7ndpTdNZOq7SX_MTd8ZOnGESUaJsgFK4ADzDyjgbWDd9d1PdY_-d_R0ElXxUvLnOdbM4wbAPZ6T_b8ynAuL5LMvvL1uiSjHo9UA5KotxKcHLjc-CqBl-M2jN8OFdCAwEOt8AJzN8oCZmn4ylBO4Wv94NqBbB-LH0Pe-7uN9OfPP8h5LnKal6na4H5gFIDSGJ3GdUS0DTRRhvUIC_-QgOCcOWY-Yhpu3t_W3_3vHWylT1TZZW3safs3fCyVK9uVYkX6A5atafLc_NsmhgT6nrH4w6fWwPq6txNFArdGoRHnNEuerhYGGjDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید درباره ایران: ما به تعهدات خود در آتش‌بس پایبندیم.
🔴
حملاتی به کشتی‌های تجاری صورت گرفت و ما پاسخ دادیم.
🔴
خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130877" target="_blank">📅 15:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869b87835f.mp4?token=BT_i-N_GLOt1jgCjCQVRGqqXbg3QE01KyeIrcxry1yGnqDJQID_YTsN1iWl55fcl0QAhA6XXGHIMziiT4RVhsa-oWZkEsT0Qs9G5SQevtq16bMR_iZHGpL8ELbLYzwXBLfcw_tMbTrD5d3lT4ROKQh2sNUEXXWK6hkoAAQ0h_2MOLnGeqtnxOjVlIWCRN3arTir3XPX3gY0ko2Ptzq60Vn6cOpMV-Amn8ClJ_WL-gj2SvB0PPLtpiKeM5oKk2IiiFX9tFhqpo569ryGIIC21oQjz6Sd2ZxK-we8sJBpLLwlguNrMpPpZ8pks3E-YNW4wpuUUeqhYSvtugxF_E674Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869b87835f.mp4?token=BT_i-N_GLOt1jgCjCQVRGqqXbg3QE01KyeIrcxry1yGnqDJQID_YTsN1iWl55fcl0QAhA6XXGHIMziiT4RVhsa-oWZkEsT0Qs9G5SQevtq16bMR_iZHGpL8ELbLYzwXBLfcw_tMbTrD5d3lT4ROKQh2sNUEXXWK6hkoAAQ0h_2MOLnGeqtnxOjVlIWCRN3arTir3XPX3gY0ko2Ptzq60Vn6cOpMV-Amn8ClJ_WL-gj2SvB0PPLtpiKeM5oKk2IiiFX9tFhqpo569ryGIIC21oQjz6Sd2ZxK-we8sJBpLLwlguNrMpPpZ8pks3E-YNW4wpuUUeqhYSvtugxF_E674Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید: ایران درخواست جلسه‌ای در این هفته داده است.
🔴
ویتکاف و کوشنر برای جلسات سطح بالا به دوحه پرواز خواهند کرد.
🔴
در حاشیه این مذاکرات سطح بالا، مذاکرات فنی نیز برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130876" target="_blank">📅 15:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
‏این تنها بخش کوچکی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراق است.
🔴
‏اگر روزی خانه برخی مسئولان جمهوری اسلامی هم به همین شکل بازرسی شود، چه چیزهایی پیدا خواهد شد؟!
🔴
امروز در عراق بیش از ۱۲۰ نفر به اتهام فساد بازداشت شدند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130875" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سرکنسولگری ایران در دبی: نخستین پرواز تهران به دبی پس از جنگ در فرودگاه دبی امروز به زمین نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130874" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXTRZ9ASfvDxSqCXXO1XjZHog2Ey-ZSEmYdlMe2QGB9OHe9PAMq31vGN2wUJ0hx5j5mEZ3j_P3GL94XJ20FqzUktCK_UPjzxQU07M-ICsQ6XCaUw3PIf3wyXSF4SSzLIDdWtMVuiMMJuBpe7avKdWEB0NC7FHM2gQgC4oxlvZzwMfPaOmwSqWLFveHJgn6PIMWIOp8DVqvFuZfKUHmh5sETdlSiVGCtswoYGfb5KCTK7gfMVGREwF8IvrXsDOmuDkt5dkL6ieE8qW5w0s2E6CGl1YC8l0bVGF1_6r7R6j5lEepY3OePOHAbQemr0ViRcKqd3GtvaCD0Gi1uT2hkPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر برزیل برای بازی امروز مقابل ژاپن
عمو و مادر سوباسا
@AloSport</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130873" target="_blank">📅 15:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0906a59cec.mp4?token=i239j68kFNTfiQpYabLkL6S7TAxIfilyAEuJV-egQM4KQPwN-Gc0tEXRAgvB8rNrcTn64Nf_SatMmAggiVVpoaYyKtt-5c0CYgAEdBCur1-6FCcmWdxXIeKHe1H80QLX8LLGhlj1IOggPDpdNG5L-SD0reSrFdWMTbmAucHUSQnr4qDV0ovUSLOF5g6b6LimPC-IG9PpQNiZsHFOWAu8flVqwzDw0h0EF-el02w2I3qom5nOPVostbwdZGfhpBLc6jbIQEu99bO64U5_3bdzr1Kkza01nzWUXaMMk1sr7X1mwQ3D3_gveJnhw95bWO1LjATd_wrWFqnoCDc6JGnVYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0906a59cec.mp4?token=i239j68kFNTfiQpYabLkL6S7TAxIfilyAEuJV-egQM4KQPwN-Gc0tEXRAgvB8rNrcTn64Nf_SatMmAggiVVpoaYyKtt-5c0CYgAEdBCur1-6FCcmWdxXIeKHe1H80QLX8LLGhlj1IOggPDpdNG5L-SD0reSrFdWMTbmAucHUSQnr4qDV0ovUSLOF5g6b6LimPC-IG9PpQNiZsHFOWAu8flVqwzDw0h0EF-el02w2I3qom5nOPVostbwdZGfhpBLc6jbIQEu99bO64U5_3bdzr1Kkza01nzWUXaMMk1sr7X1mwQ3D3_gveJnhw95bWO1LjATd_wrWFqnoCDc6JGnVYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام عجیب تلویزیون کره جنوبی در اعتراض به حذف از جام جهانی
🔴
شبکه KBS کره جنوبی، پس از حذف کشورشان از مرحله گروهی جام جهانی ۲۰۲۶، تصویر هونگ میونگ‌بو، سرمربی تیم ملی را به‌صورت تار (محو) پخش کرد.
🔴
این اقدام معمولاً برای پنهان کردن هویت مجرمان استفاده می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130872" target="_blank">📅 15:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پلیس آلمان: پنج نفر در پی تیراندازی در شهر شتاده در شمال آلمان کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130871" target="_blank">📅 15:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: تهران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130870" target="_blank">📅 15:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d4a95a20.mp4?token=a4hCm5JKj2amhMoJB4Xm012iCaaK1VKMBcy9AqeDHWxcuSVF9364o3CDW41YxRCiGjxDPbpVojBpmBz62I7mH1SfPgz2Hi9fFsisIOsKJUzGt2EhezBZnREqyGK9JvC4M_znkG3QB_rlgM3W4og_EcUj6s1_EdXwZUVI5oTfHEN9cEuIeew_oKUX0nKquFrrpsZvLCr4BgtVKCIFzABzpnOjqqjr5MJm_zNF0l-DRgOj97AhY7QKn6CnmITWK4wRzoA_U7_Yl4RamgNMoGq_UoCyeKb6KEPHxAilQnLNfxwhEdv6XScgvYu1n9H2VgdHkqy3gmfHNDQGWFKHms5USQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d4a95a20.mp4?token=a4hCm5JKj2amhMoJB4Xm012iCaaK1VKMBcy9AqeDHWxcuSVF9364o3CDW41YxRCiGjxDPbpVojBpmBz62I7mH1SfPgz2Hi9fFsisIOsKJUzGt2EhezBZnREqyGK9JvC4M_znkG3QB_rlgM3W4og_EcUj6s1_EdXwZUVI5oTfHEN9cEuIeew_oKUX0nKquFrrpsZvLCr4BgtVKCIFzABzpnOjqqjr5MJm_zNF0l-DRgOj97AhY7QKn6CnmITWK4wRzoA_U7_Yl4RamgNMoGq_UoCyeKb6KEPHxAilQnLNfxwhEdv6XScgvYu1n9H2VgdHkqy3gmfHNDQGWFKHms5USQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه : فرق این تفاهم‌نامه با برجام اینه که تو برجام امتیازهایی دادیم که پس گرفتنشون راحت نبود، اما تو این توافق هر وقت بخوایم، می‌تونیم بریم به همون شرایط قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130869" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550d1e43a6.mp4?token=V9zHFslZRPPEwgFpc6DF8HHphgYYXZoVC-r6PEn_kbhMVmR22tIisoLRT9YLIsrFafh0Zb7elStOkYHGCvxbpUGdZEYlpzeysQRFI6X4ydRYXWz2RoffQQtAk8MiL29K8qMczJTnzFe2PM3xMcKWryLh_ywagEfwqTFWTrIDRCwpyDGZpGXGgrNEuJK1mOitPSLeOtb9sMoWzCp43DVkRHsf48u6tHzk6GdAzgJy33mhzwhPm8shnVNs_dm771-4SLIwLsMy262JLkF8vwhr3Ip8GCInbxH64YXE1BYwM-mOwW6DLWXKYyHZsH3dhgyzfb1zqDtT0eok0oEHGcEGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550d1e43a6.mp4?token=V9zHFslZRPPEwgFpc6DF8HHphgYYXZoVC-r6PEn_kbhMVmR22tIisoLRT9YLIsrFafh0Zb7elStOkYHGCvxbpUGdZEYlpzeysQRFI6X4ydRYXWz2RoffQQtAk8MiL29K8qMczJTnzFe2PM3xMcKWryLh_ywagEfwqTFWTrIDRCwpyDGZpGXGgrNEuJK1mOitPSLeOtb9sMoWzCp43DVkRHsf48u6tHzk6GdAzgJy33mhzwhPm8shnVNs_dm771-4SLIwLsMy262JLkF8vwhr3Ip8GCInbxH64YXE1BYwM-mOwW6DLWXKYyHZsH3dhgyzfb1zqDtT0eok0oEHGcEGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه اگه لازم باشه، ایران هنوزم می‌تونه تنگه هرمز رو ببنده
🔴
طبق توافقات موجود، ناوهای جنگی حق عبور از تنگه هرمز رو ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130868" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029bbf8e06.mp4?token=Hje-a-1DnVczoV0rOcHV0IPWU4pRoiacpDvAmvqT8tEUFBvGSjE8gzCo40SuzZjarterIVxHEL7Y8CzfBJeJVup-nHu-M9hIBzUbQZyebV1WpjQUnCrZDSKuhpSHAw2jU7kCcks0rDpbKnw9D8WVkhkhgYxm4_EVjQNlVHXCFY0yeAoaGoRcLDOA7q6w7ufHLRZK0skOXJBi6rOTwQuXqUkBxLcmmOONCxQ5FnU4R1OTemotBKbRB28MphdUeIxinjuvA-ZH5wWnqe3-vno-V1CN9tH71YOjOqTJHueZ8qFJw44rLOCB7EFc89Ynk_TULdVp3eioYplVwMkNen0vHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029bbf8e06.mp4?token=Hje-a-1DnVczoV0rOcHV0IPWU4pRoiacpDvAmvqT8tEUFBvGSjE8gzCo40SuzZjarterIVxHEL7Y8CzfBJeJVup-nHu-M9hIBzUbQZyebV1WpjQUnCrZDSKuhpSHAw2jU7kCcks0rDpbKnw9D8WVkhkhgYxm4_EVjQNlVHXCFY0yeAoaGoRcLDOA7q6w7ufHLRZK0skOXJBi6rOTwQuXqUkBxLcmmOONCxQ5FnU4R1OTemotBKbRB28MphdUeIxinjuvA-ZH5wWnqe3-vno-V1CN9tH71YOjOqTJHueZ8qFJw44rLOCB7EFc89Ynk_TULdVp3eioYplVwMkNen0vHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه، عضو کمیسیون برنامه و بودجه مجلس : برخلاف چیزی که دشمن تبلیغ می‌کنه، کنترل تنگه هرمز دست ایرانه و حتی برای این موضوع هم قانون تصویب شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130867" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دو زمین‌لرزه جدید صبح دوشنبه ونزوئلا را لرزاند.
🔴
اولی با بزرگی ۵.۱ در ساعت ۷:۰۰ صبح نزدیک ساحل آراگوآ رخ داد، و یک دقیقه بعد پس‌لرزه‌ای با بزرگی ۴.۲ در حدود ۱۰ کیلومتری شرق لا گوایرا ثبت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130866" target="_blank">📅 15:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رسانه اسرائیلی: ایرانی‌ها دارند آمریکا را مسخره می‌کنند و اظهارات یک مقام آمریکایی مبنی بر اینکه مذاکرات طبق معمول ادامه دارد را رد می‌کنند.
🔴
تلاش آمریکا برای نشان دادن اینکه «هیچ اتفاقی نیفتاده و همه چیز خوب پیش می‌رود» فقط باعث می‌شود رفتارهای بد بیشتری از خود نشان دهد. این یک نقطه قوت نیست؛ این یک نقطه ضعف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130865" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
العربی الجدید به نقل از یک منبع در ارتش لبنان: ارتش اسرائیل در شهرک‌های فرون، زوطر الغربیه و الغندوریه که به عنوان مناطق آزمایشی تعیین شده‌اند، حضور ندارد
🔴
در انتظار سفر فرمانده سنتکام طی دو روز آینده هستیم تا موضوع مناطق آزمایشی‌ را پیگیری کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130864" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLJ7HV7AXDy0IOzyUracJN13PjTniZjjkDcO804O90AovPYfsIIBLS79GVtXKsKpg9DTHnxbUjzkihctsA8WwAMyfucm4uwKtV8Wb2Ou6_vzbBLU4MNiFYaAtif-Uoa-U6QkSYFvlHoK9lnO0PTAJC0UXe4SQCWeVY6-b5YM92mXYQPuPahV-kkSsna745GwrgPqmyiHab0jukOeVVyNyNWSShF-R4CQw5hjR-I6M94UdU3CuAAQkZ4qArR9lVK7ClUYH3wIELXxQ5TJjwzL9ajdl_d4XhUxfDWPPwr9QmyZbI_r6t5yNyN4bWlRujFtVeiPnEfnkKbVfSTr7P9ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:نفت خام وست تگزاس اینترمدیت - ۶۹ دلار، و رو به کاهش است
🔴
این کمتر از قیمت قبل از شروع خلع سلاح هسته‌ای ایران است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130863" target="_blank">📅 15:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00245d127.mp4?token=NLnyMynKUVEn6xrYLYMa-o8spO4nbrGH8aUXYJ928BJEhD1WgFnahFOFaBlaEZYaWAzSf6TNSrQpdqRGp_Vs-zQCm58EHYvkF9cKXm2pKzr8jJ5CoHlMKwRqE5dFNK1F1-DymaqCggYeXD20adML3U-5qIdnMQFbhdv-_medn1GTR2DYbpsXbGJExta1x7lLiLng0-VYJWV9UDhLrSkpRMX8Z920yYkiD-rP8IiPFrrIHSzLco4EBwLgaom4il2bzLi7C_PXHTNgYg2bZcP__2YDKLaMFpu1T-t2AyjeFUx5erHfeMiP31-Zgzm0Gnye-sf7xPPSLQUXdCE2E78W4ldtknu8ipvlMNZBc7DPR5ufwD6ziCNNtbm_MFr36axgI55fC7u-BcP0XzKKpPjDq7ZZIcu5QwyIl7yyFyXEoIIAb0xlik821ThHWQ7D4GW5TR5T0w4NNnKMYj4Q6_u-1N7bBS69-7Zz1dni6TMLcFi3bSWJtz9yRRRQoRgH4gj021p3JqlLQDUsGRyEAvD7rBYHonZmZwajwV1ViVgmtwW-59V1XmxvepDrP37t6d8VNOfirI0K9uF78P7rDFGb9ENOynFk0GwWGxrv-947Wdjy3iM6c_JbQ94lzz1urAHWZmGMGEvbsyrxoMiJ8Vbt25BGXRbBCp1rxYuNTB8vDmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00245d127.mp4?token=NLnyMynKUVEn6xrYLYMa-o8spO4nbrGH8aUXYJ928BJEhD1WgFnahFOFaBlaEZYaWAzSf6TNSrQpdqRGp_Vs-zQCm58EHYvkF9cKXm2pKzr8jJ5CoHlMKwRqE5dFNK1F1-DymaqCggYeXD20adML3U-5qIdnMQFbhdv-_medn1GTR2DYbpsXbGJExta1x7lLiLng0-VYJWV9UDhLrSkpRMX8Z920yYkiD-rP8IiPFrrIHSzLco4EBwLgaom4il2bzLi7C_PXHTNgYg2bZcP__2YDKLaMFpu1T-t2AyjeFUx5erHfeMiP31-Zgzm0Gnye-sf7xPPSLQUXdCE2E78W4ldtknu8ipvlMNZBc7DPR5ufwD6ziCNNtbm_MFr36axgI55fC7u-BcP0XzKKpPjDq7ZZIcu5QwyIl7yyFyXEoIIAb0xlik821ThHWQ7D4GW5TR5T0w4NNnKMYj4Q6_u-1N7bBS69-7Zz1dni6TMLcFi3bSWJtz9yRRRQoRgH4gj021p3JqlLQDUsGRyEAvD7rBYHonZmZwajwV1ViVgmtwW-59V1XmxvepDrP37t6d8VNOfirI0K9uF78P7rDFGb9ENOynFk0GwWGxrv-947Wdjy3iM6c_JbQ94lzz1urAHWZmGMGEvbsyrxoMiJ8Vbt25BGXRbBCp1rxYuNTB8vDmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس دفتر نخست‌وزیر اسرائیل، ایدو نوردن: در جامعه اسرائیل اجماعی وجود دارد که بین رود اردن و دریای مدیترانه باید یک دولت وجود داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130862" target="_blank">📅 15:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usXR4Yk_pnuVn9o77Vz0Ax4ku0sA3Pry9VcyOjgSQLFTg-tLNT4KZEKTA8l8KOd0JdSc3KDXPZwOIQ3_ovFaz3Cr29NOZjrBpt8R_fzidO4E1xOvkJ5IXbags5IZ_VJ55Dvm6CAMDPo3Dq204g0az0g4F82WO697ZGc1eqfCtqsdMvlHmtYzXw3w61-ktlNFZyXGBCOxAe8YwR1-AOBHi0uUXU7kRyHubyc6m5qCX6CP6jbL1U6N0cYiLQc6IshzO8wxnyCTJBgl7hZwP9KibNG197jaX79-TzVpnbs_6MXPeSEtXqU7uki9960bioMt2D-k884zysIGVdP5EYnvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تصویری از یک فروند پهپاد مهاجر-۶ و ایستگاه کنترل ساخت ایران در کریمه روسیه منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130861" target="_blank">📅 15:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130860" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gst7ejs2ys3MPu-87R3IVoB7X5gKkE0MRo1EiTn6IvgCVweAPfyWCbwK_mUAJfILzB_rNoGHL5pshdXRI-NQEb10Y5H4Kim03wafSM9PWgHlAeToQHw1PwrgBD45LdVXDbpEavOSF-UCu4zx3qkQHBlwgiuHTiiwFM8wBAeP-XuHWZTUq7AmYBK2-hUrPKCLFm_e-E10Wc2iYilicdbg9_JS7SFRfXdYONPxsHOBDaTtEbUwJBs-3WzTM3yeIRH4NCVoErsnEvQIbOfNKgpjyCTVitjGsYa2A3WAiR-l0DbS5M5vYfA-Eg6r2AeqdpoLDANL1w7SlkFQPTg2E6h_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: ایران درخواست جلسه داده است. این جلسه فردا در دوحه برگزار خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/130859" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
عراقچی به نجف رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130858" target="_blank">📅 15:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بانک مرکزی: نرخ تورم نقطه به نقطه در خرداد ماه به ۸۳ درصد رسید
🔴
تورم سالانه ۵۷.۷ درصد ثبت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130857" target="_blank">📅 14:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آتش توپخانه ای اسرائیل، جنوب لبنان رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130856" target="_blank">📅 14:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fb964ef3.mp4?token=OilwteaUhzyg_YTcyPe260vQcA0OK9nlvpzT_6SMKJxxiWChJM5Psvxx8ii_YbBNvLUwCjJ_GmtMeBDwo57GoEZf2Ds-qPPOAIBr4YkMZ-V14Q-ea_JE9h1xJT6turxLmCX94XZWYWGm2rZ11jx4ht4QlGGvnQmDifQOKf1ZdhIuobBUh9CikYoF7BlWkmguyUAAuvnuUMcD5eHZxEpupXpDzKnbYaKsovFRIsx_Z6Mjgnvhn0CMxM9iP2gRaHYLJb9ZAYnWPBPoh_akmk9waWy7TNvzWYg1nKbfLlxjvLXwKhHEHMLzZ2Jf8ABBVBQPAf1C8Qtky9tkwRJFhlHdAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fb964ef3.mp4?token=OilwteaUhzyg_YTcyPe260vQcA0OK9nlvpzT_6SMKJxxiWChJM5Psvxx8ii_YbBNvLUwCjJ_GmtMeBDwo57GoEZf2Ds-qPPOAIBr4YkMZ-V14Q-ea_JE9h1xJT6turxLmCX94XZWYWGm2rZ11jx4ht4QlGGvnQmDifQOKf1ZdhIuobBUh9CikYoF7BlWkmguyUAAuvnuUMcD5eHZxEpupXpDzKnbYaKsovFRIsx_Z6Mjgnvhn0CMxM9iP2gRaHYLJb9ZAYnWPBPoh_akmk9waWy7TNvzWYg1nKbfLlxjvLXwKhHEHMLzZ2Jf8ABBVBQPAf1C8Qtky9tkwRJFhlHdAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوسدادو کابلو، وزیر کشور ونزوئلا، در لا گوایرا دیده شد که با تیم‌های نجات آمریکایی بحث می‌کرد و آنها را هنگام حرکت به سمت کمک به قربانیان زلزله‌ها متوقف می‌کرد.
🔴
یک آمریکایی شنیده می‌شود که می‌گوید: «این خوب نیست؛ من خوشحال نیستم»، پس از اینکه کابلو همچنان برخوردی خصمانه داشت و به آنها گفت عقب بروند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130854" target="_blank">📅 14:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فایننشال اکسپرس: تولید نفت خام در خاورمیانه در اوایل ژوئن در بحبوحه آتش‌بس میان ایران و آمریکا، به ۱۴.۶ تا ۱۵ میلیون بشکه در روز افزایش یافت.
🔴
تولید تا پایان سال، به طور کامل به سطح قبل از جنگ تحمیلی علیه ایران باز خواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130853" target="_blank">📅 14:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130852">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار صدا و سیما: نیروی دریایی امروز هم به شناورها هشدار داد فقط از جنوب جزیره لارک بگذرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130852" target="_blank">📅 14:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130851">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-D69m_jRCLkD6JR5N6vpgLcTY754Z7ZKDc7xTe5Yoy4hdT3eDO92J6uyH50eYq5vN_7t89uDhI05-5XaqspuRCyaL6MBNIpDhUGD7Y2m82SJuuVcGbGGeFMqF2TiIOXqVyhwbazxQnfR5jHpPy-C_iBePcwQazwGd0KY9PS_hUx9N2Y-a7fS14gP6NGbMihbIPW4TSrq07WRMrWz9QDr7wasI6feey8wTLNmpleqB0TgZkE-JxTkK9G2Kq-c0MLa7yw1yB7vWSWXcHNNm-t8sIBYY7M7TeEm4zb7Ph5Y6u7xPPbNHmO0PyBdOTBvhdgBDQS_Lj0-Z4AK2oaZva1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
🔴
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130851" target="_blank">📅 14:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130850">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee2c04f620.mp4?token=FIXQqH6GNNFBGaowhGmO8vxVfz3gc5PIy-ZAeO7rs88ZAZaiX95maU1kPwAn_9DuugVCgzeP4oculD0UuCbX8Y9HQ8_O3P314uNvsCHdHGGV5dbzWIDzYcucOsT2GowcSpQXkXPTzd22jJFH-W-Fpx0vgN8T0L6ozQShgY6jQeXd9yi5NDEEm9blWGzsk-FjlVXBTZ4wnrjexIzFrqcI3xYjCelA9kcqwhbBqhGd5IieAd8Lh44JI3BtUM44N5PS8KY19FGH9xVdVgu2ii6r-i3-a7vFSKw30Kt8Yy76a2HJ0yd-SMVcxGRuEPBjdlrGK2sP6fjzZQn4A7Rz2gNrbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee2c04f620.mp4?token=FIXQqH6GNNFBGaowhGmO8vxVfz3gc5PIy-ZAeO7rs88ZAZaiX95maU1kPwAn_9DuugVCgzeP4oculD0UuCbX8Y9HQ8_O3P314uNvsCHdHGGV5dbzWIDzYcucOsT2GowcSpQXkXPTzd22jJFH-W-Fpx0vgN8T0L6ozQShgY6jQeXd9yi5NDEEm9blWGzsk-FjlVXBTZ4wnrjexIzFrqcI3xYjCelA9kcqwhbBqhGd5IieAd8Lh44JI3BtUM44N5PS8KY19FGH9xVdVgu2ii6r-i3-a7vFSKw30Kt8Yy76a2HJ0yd-SMVcxGRuEPBjdlrGK2sP6fjzZQn4A7Rz2gNrbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان کری وزیر خارجه دولت اوباما: نتانیاهو به اجبار از اوباما می‌خواست که به بمباران ایران بپیوندد
🔴
او از اوباما اجازه خواست تا این کار را انجام دهد.
🔴
اوباما نه گفت و از شرکت در آن خودداری کرد، زیرا فکر می‌کرد این یک اشتباه بزرگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130850" target="_blank">📅 14:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8n6Hxv6iS8NmeDMSfw89Tjl00u-fBugNfb0O9d-S_j0wPZPUU47ofW47qpvpuNxXbDeDWLI8Wxq7Ss_I0imVE31FASbSjRLy3GpvKEoTj0XxNfdYjPKjNdqZq3yBLRZcajIdenajDAxtGQrujj75yXCKeMM_26EvmiJDBLkN0zoU12ItTWtL06wDDBrvRyyYx8v0Ar-9npv3y5NW1WBvL9KJDYpPu4qWq5fOpCpRXgQIwrTiPnX_a9nMdfU3W8CfULiKLIFO5CQLgXrORWDRLEGQFBi9p_EdCR452EtloLC-3YGNv-BvevPrgddf1GyYSQ3YxLDR3f0JJR20AJmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
آیا فکر می‌کنید مردم قدردان کاری فوق‌العاده‌ای که ما در ساخت و اداره نمایشگاه بزرگ ایالتی آمریکا در ملی مال انجام دادیم، پر از مردم خوشحال و همه عاشق آن بودند، هستند؟
🔴
از خودتان این سؤال ساده را بپرسید، «آیا فکر می‌کنید اوباما یا جو بایدن خواب‌آلود می‌توانستند این کار را انجام دهند؟»
🔴
پاسخ خیر است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130849" target="_blank">📅 14:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d3b8ad0e.mp4?token=qQlgYYNPJMLvHOsakAIQjo0F7OnMkHeIQz_6saL97DZ4HekqHMp92uwKoG_wNLPzC0lDjtGLHXvCFKvIL6VBJZjm2zwypf2tN1KePJbCLPixUVgvK_Uz3Fe4I9vBwdkLpPI39jaYnrZGCkIl_Vhxp13U9ZtKg8q9u5shVtkcWYENA60ls0DwsP32zu2pibAWacEMs1NLrQPXjFGX_zPsvZMOgm7dx_IFN06XS8sx84tqX2c9sA39Xhekk2vv-PtfLcasPaN2KZYu-189gryOjwKBYjSUR1UggNYf1qynKfCnkkeG4-fImqNvvimb7sPWwNeBcB37CCZRuiDSz7zZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d3b8ad0e.mp4?token=qQlgYYNPJMLvHOsakAIQjo0F7OnMkHeIQz_6saL97DZ4HekqHMp92uwKoG_wNLPzC0lDjtGLHXvCFKvIL6VBJZjm2zwypf2tN1KePJbCLPixUVgvK_Uz3Fe4I9vBwdkLpPI39jaYnrZGCkIl_Vhxp13U9ZtKg8q9u5shVtkcWYENA60ls0DwsP32zu2pibAWacEMs1NLrQPXjFGX_zPsvZMOgm7dx_IFN06XS8sx84tqX2c9sA39Xhekk2vv-PtfLcasPaN2KZYu-189gryOjwKBYjSUR1UggNYf1qynKfCnkkeG4-fImqNvvimb7sPWwNeBcB37CCZRuiDSz7zZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو از اعتراضات دی ماه به شدت در رسانه‌های دنیا درحال وایرال شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130848" target="_blank">📅 14:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRmGVB9Oy9WbgEsPsEOBm6hUKtOmXsNDZF9p69BXdBv0z7QoedcEY0rqFb_MmsI8ix-EFZo-NJ28yKpnw0tyHQ3HSlcJG_dqNupsRFrjUPQYQqqd_HzlfasUwRPvO6pTJKK_cydUgP1-0DOcCE3KAEMudwI_B8O1w8IGcQOAlKF7z9bfMDXHywzU5ARux41aRCJ3sCb_loKXtpwYEMbt38jcXGMj0BLlvTO70vw0gSzx8VyhgavVi2UbvezqTdydnfxAZnwxzi691gznUEvN-npCwk6qb8tP5ZUBV-lUMR-JHwpCZJ20ZUaDZvi7kMmGfjHH_L2YEWBPh-LvLfVZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / رویترز: ایران شرکت در مذاکرات فنی را لغو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130847" target="_blank">📅 14:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCrjTqgEAr3nt7M1AbkIhjHTgpxrDjeyieiq-bqJ34DstTr5jHxez_OT7vldk6CPm80Ygpqc7QKDMG2C_PxwaKZ8bVjKnC20_Q39_rQhXxOO77KeH9voCZk-S53uH8PYq7UOhlh7ff-MZ5s7tMkqWu4JVadFIpgFVcNYkn6mzV-8vD0crWehwybtkdyRXPvJpxtlHqlxng6lROVJxq9RZsjZJVEuLP6YZEfGxNFkIrNIo_FeL7Hw7j2d6nDQjmipDb0s_L_eUuFTpaK6nAto87OW87E_jpMZyQeUiAdZ0NrV5eNYzbWVG5Wmf-spDNwK3cDgmOqdDMz9T7OI_pjxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت‌الله مکارم: اگر بدخواهان مانع‌تراشی نکنند، توافق می‌تواند آثار مثبتی برای کشور داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130846" target="_blank">📅 14:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130845">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqVEzqTcHFbs-kg2NPEZEM-K2CL-nasvjU5OOo2y2OWZaFnQZM2eAF7tC6jqypKl2q4_pvpD7ywDv4G5JxtxrE41XXS9PcBq8pDeWXVRCAJE4I9yjRoV3p8wEbNJM18gK60JhAIXAgY2mIbdSVUWnCCyDKRxdPEk_eJiiVP5wIAKD4c_f1jaKtMvSi9SuNKof4Ili3fFy4JFHJEthr8IiZVltdHunLPzMgZ1J7B0H3Ac7kBMNp_nrmO8XVMuIBKMw0abllrPFEAj-hjS2v_K0e1cyqIicVzuMSC4dMq5XviU1IErD8zz2JFOAmkfcHTetZLRLuHrpgeNnrJZdjjnjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار ان بی سی:
یک منبع آگاه به من می‌گوید گزارش‌ها مبنی بر اینکه ایران در مذاکرات این هفته در دوحه شرکت نخواهد کرد، نادرست است.
🔴
او به من گفت: «تیم‌های فنی که روی اجرای تفاهم‌نامه کار می‌کنند، قرار است در روزهای آینده در دوحه دیدار کنند. کانال‌های ارتباطی ایجاد شده برای کاهش هرگونه حادثه‌ای برقرار است و مذاکرات فنی قرار است ادامه یابد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130845" target="_blank">📅 14:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رجا نیوز : پزشکیان عدم دسترسی ایران به پول‌های بلوکه تا کنون را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/130844" target="_blank">📅 13:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130843">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9n-8xX9Baf0uFWXoBxuRvXwJzr4Dg2FPWjh31tbgfx3XnXEAKwjHtIBA8P0Xh5egctMYBH4OjU8299PeVO_f5uA-HbMv3xFbpbiTQuYQaTHfc7jGULVcE_MeX7skMla2bfQXt_saWthzRtF5M0asUAIyutdyuSRc0mUIUVQZXqVWOCjzyF87SYAPUkxzWpLmaMEhALqLSKpBybOK_Qf4obTmdzqpz1i29QYQ1HmcZt9nRTKHjKzGgaiH8_eK56RZzZp8Z3bS1vqJOzmVJixRBewVOcoM2V53azYGbxX8yV7-hzr-ptpwKCI0Cd6M60A-YwAvnEqRBs9THhsZNVNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت یک وکیل دادگستری درخصوص پرونده عجیب پرداخت مهریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130843" target="_blank">📅 13:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130842" target="_blank">📅 13:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130841" target="_blank">📅 13:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130840">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ارتش: انفجارهای کنترل شده در شیراز به دلیل خنثی‌سازی مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130840" target="_blank">📅 13:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130839">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ce41f48.mp4?token=l3ZVkMPZyZ1ubHhqKLDQscd6R8zijUMkiwMavqOk85cn8IWRjb6yRwc_OCsqFj2hVqNyVnK5-NblGfFVzxj03GxN1ofcgn1_qSI8iawa3BoWDenvUKINalorRIn39NL6Nklhivgu4sVxoRGWa9yErDzBeOQF09_Jbgj7gwho95Cij2Ns9YGidbMh9yj6QRI3cw0YgH4ozpqqL3F_jF6zEN1LRx-s79EI3vFrrHHrLwnqwPDXSksS8pHVH9rVD1Y9LJJQFREcKR5Nm7lFuDGzgF2MPwFQ2lXrHI8xAD00B-DPhvgy6Ggwn4QsiJ6O5jjAoxGoPV6hBmrGC1WBE2H_vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ce41f48.mp4?token=l3ZVkMPZyZ1ubHhqKLDQscd6R8zijUMkiwMavqOk85cn8IWRjb6yRwc_OCsqFj2hVqNyVnK5-NblGfFVzxj03GxN1ofcgn1_qSI8iawa3BoWDenvUKINalorRIn39NL6Nklhivgu4sVxoRGWa9yErDzBeOQF09_Jbgj7gwho95Cij2Ns9YGidbMh9yj6QRI3cw0YgH4ozpqqL3F_jF6zEN1LRx-s79EI3vFrrHHrLwnqwPDXSksS8pHVH9rVD1Y9LJJQFREcKR5Nm7lFuDGzgF2MPwFQ2lXrHI8xAD00B-DPhvgy6Ggwn4QsiJ6O5jjAoxGoPV6hBmrGC1WBE2H_vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش پاکستان : تو عملیات «غضب‌الحق» به اردوگاهای گروه‌‌های مسلح داخل خاک افغانستان حمله کردیم
🔴
آدم‌های داخلش کشته شدن و انبارهای اسلحه‌شون هم نابود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130839" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130838">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a032IuY8wQd6u7odgEy4GG6CEVc4i4N1g3Dkxs9Z3NbL-nSK03DptRpX64eChkY8k5nTu5hzQEMtd7ubJhgkzIqNkt0fq8nU-PSdwSWJFrfU6SE6a5nZ1Xko40xbRvZr9A8PGBsbM5ThiAylkKlf9Ve01QNzxJOIkq5afNA5JKEk4Ce4Gw4Xsb8pGZfPkEy0ZdOmZZG8PQc16C2DiVWb35sZO4OOUoPIdqhSGnEtPCCh4Aqt5b9cBlEOdHQtITzNimx9-aGEvIuylg8ZpbK7RHCWJ9Fb-Rv9DQcmlvKfQZepDh3Gpd7z9gP3sHPOlCsaoI1GM7JKCEOp8yeHpnh0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حقوق بشری
هه‌نگاو
:
روز جمعه 6 تیر،
امیرمحمد کاظمی
، سرباز 19 ساله اهل نگارِ کرمان، که برای مرخصی اومده بود خونه، به همراه چندتا از دوستاش رفته بود بیرون که یه دوری بزنه؛
🔴
بعدش به خاطر اینکه صدایِ آهنگ ماشینشون تو ایام محرم زیاد بوده با نیروهای بسیج درگیر میشن و تو این درگیری به امیرمحمد شلیک میشه که گلوله دقیقاً به سرش می‌خوره و همون‌جا جونش رو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130838" target="_blank">📅 13:16 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
