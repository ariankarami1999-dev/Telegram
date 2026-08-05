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
<img src="https://cdn1.telesco.pe/file/DN6k2gkvMnR3qnBOZ3VWZZaaIIVeBq7LYHzfFXv-XXd8da5FWv4Xds_rmzW4j5esXZc0Hr90sBGaKoeFsChkvJFVc0HfC-TL_4iS3yGUqblesv0-sm_pxDQ5eN2vtKhssp50Ml8B3cy5ABBe3zGivsHQytabYI6UnjksEQrT46XaYvfSmT07Om02Y0YrSBH6qLm1R_e8ui6HJfkbSBLCXamHpAlmYkCPwk7oAcyeJkXsHVyF70jLuPHrmKuaDFx7uCjMZJFpEnltUHDfThj1WKKGUwX76VW0P01DVuWdH56rlLADn6r1eGlEGrjtycHKjBc7Qfj_ixH9MgY29iAATg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m_7IqHswo5Mqnb4pMq-ixm69M5dTv9AS3LnMEhFAySqiPFms5nXTgr3WUrZoeOdsT0-G8sFEpC_hkHfowbuwj2tq5UMI9_1ah-gG8aIVu733jhsABCLea6u505Yki-5IfUM41vKnCE09y7ILXHVvVm2WNtFWtnUZNwFuBO_rGFn8dis7ELLxBlXIz5qO60Y6WmRGc9CRl41DIatvS8AJ-TWd3DKI79H_4JuB8cDbfoKdndvkdzw-IaLs8ht__SaoYg2VifnhVO4CxRLFZAIpS2l3MwY_kq_9W1J8wG7Dj4bNOjhwnb3Zr-5r0_x83znfC0gFht9UXljQ4Gte5xsJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pNh9QTv7Zqcnu7pjVmwQVc9ddiNkGBJJifGvXED1RE5S07oZ_sVm2IbnxznTVGw2SUbYzqiMcLAatkOPRwGrJCZE16TeUfuUNvnhyiG29I8rvIdKvju9z39NKiJGDuO5l_GkITIi9JqtBpepijppdgUFag7vfX_FdeaTYn5x7N6FWE7_TD45gEkOQxlyBCmIGZ2EdCf6XazN1D9DLImxqIy7SNJjf5POY-WZCtFBdwcL8zrhTbJcKu4TYdRAENlieP82sf5IqLuOFh3og9MGkxq1hNpWRDv2DrSE6YT1FCGBnQ8gXVMDGaVn5SSwVPrxEKafY5SNu3ax8zpet6hb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QrAAwgtdmTAODozktcWAauoU6rPAT0BVorJMHyJshyPd3d8_W4ULtiEpXYbpEKmKfToUBpKpeFfd_6uJGdEUHwps2QIDE9AQOjNg0o9lqdXeoc5089JCFhOULaaiwQ12SLuR8TJEAnB5v67hLdYbW6Mir1jIJNEarEuoR9w_eX1qckd1OaRfwwW0eHN3IC9z3JQh6mdlqaGd6cSXholRqesM1iTuKAzKZZZmapvf0icxGVJnSncUH0rpDesau2gR1X3PLpdYEPp-tkbZ6nRZfXO9e_cHIL9yXED18PI48D_YhzZdHG-n2JKUWgdmfqzfNQSNc8c2muYAJ8Ujtp7PGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkQM4h6TLRyHHH_ZvqSUh1j7ZuxWHKdCrwQDe2oypSqCV6u0KTNVX42TBglEKMUi98zv8sTTmPAh23jChbAE1NNsWEL8P_LY2ukUaK-R6DiXn7jfhMmKUDFqkNEY-LHULsWFB1NVvMTMsVSKKGdsx8L49REjL6q4KzZEr0UZ0ts0rjo2G3RoDW69RS5dXL9J27RiMu2u6vT76huaBGbk7A2QBz9TnVXuwQ228O85kAo8uZC6G-CGkS2fJLyJPMf3de_7JThvJzD1wAgwsTG8GFcZm_4EiDzMN_MVqRt8Fn4sDH7Q1wgYK6MrClxx0ZFijEcgMvUdkVZaKqG6YiJkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvMo7JeU2kdZkOWsVW6zkU3n39OoJHfXkAJt_xcGz7AUcekVO6zdu5W5XrdIlckNMw4fHyNJDLAGa72t0iqtIX9zHeP_HzI0J2cuDrTXR4jVtEqYDdNCoxCVlE8-ckWn5tJTBPDsXB1RXtXvoisA4bQ2ZbCAqqiiXT7siLlbEFyu-U2nFUPS8yDPpOLWjvlGbiKsvht3qnyxGK468AYSQcC6GEH4IL4COXa2P8_Yr-Fipzb1PYhczWCUc2KuTWXgaYsiThClUFFVAMF9qaI9KTFGhTnxNeHLJTaPX7T3iLKhoGf2u0bQswEweF7X9yRlJ6KzETPvXLNO-DfsKx5ovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjjsyJJ3VcmPQ5KTBhYpbOCpdgKprxcDXngg6eKaL-RJDA2yoIpiKiQd1QeoHZhaENohGkZaNmJ3l3cys_KtMH2NvbeCAyDAH62ih0i64ABRaaIRbAWzB9ZiULKoRwwDhibTYgzIcwKo1SlrcwWltViQxcMYiqZ408qsBtLput37kwbL0vPPBNl_g1VPGuUtag_v4T6kcZsABezuDf0IEKEMUMB3LrO5BYLNnsCr5eK9xBab3rEBZ9HH6li0i85bGE8syGKGIidQm28V86txNdgOkmJit6Henf0MC_Ka71vYGoRWl0HHFf3Ch72Cv_GloLvi8x75aYzMWY4PoGqWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSZ-NcNVD9MXBZ8BTl23VlTo81wY-oHLlQT6oKEjls9ALbk_w-xqkR6BC9oZvjUe6U1CMFBAEhfNwj_YTvrVCPC_4rQsAdVjLokgBKIQaodUTTCNuUvnVLV7J4NYmjt8d8zML8dfZmkBpwcmSBQMhS2YzjNQThKDA1g8_oje2KpuXW6EqL8_DLDNo9V0sxi4wmRKeR1yGwdv79xeVbEs-NuZ-QnFmws4pnlo9hJel7D4D5vCG3uR2aeaWS57b9daXuqXKP8srdAWs0tHos-8Wj7Vh5RKeS7Tgz3YZpkMVzj12GDaRY-RCuhqSrLhIAsPZkQfy9Q7v28Y8Mo3Zq_xQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hLeJXGlRqqDWj8yX6QRlJzYttUTud4dJry_lxMwd3bPe48xCsLaFpVjoH10RKj45lW4SJlMP4IvJ4EPZNlQUG6nW8d5sBMPMZkaS15rG0nyzJZhHmuUGSniacDfrAI2XW2Sl1aO7AW60bXIU8RkkPNl2GEanMIvk1XbryPxv13p0cWAvngYDYxCNYtQo7SV7oYFYjip3HMPSLuep4xCgmAGDeFjypzVcOKnKSVe8-Pd-Dyn6BOfgwnzTtFKZYq7SkFuWU42W7wPTny0uE9u8_o-luQqPJLv2TfycX_yum10GSSHerb9rUJnrfqkvJsBuvg1RwKBAnOqdjZ3xbrprmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1kROKzkD0WDntdRR9l35oxrRP_PrFUdbSNQsr7ICP4uQgMOC6BNRsKYyzH2DQWKPHCEq6OrtwG3MUd4vfcDwcCMFFF4oMwm6rtj3mOEJuxMIzWN6bHqc89aBAUBVDp-nFlvkNghsT6tB1PjVRBmVegNFAsTyABOOZvTLW97Bk45RDSIKAPvCk1hPUVQHUou1zePNxlwuu3BI5OT09u8U_dLUi5ghgy7pXnNXioK3GfNKa1VibOcIyrlXX4gSvR4YvpYVpouOHCZW0MMEJx5WnP-zlTkmQWFucn_5cfExG0xHPfJa1hv_vdKD2nAY1lQkZsEauj7H5Wrt4ZQ36Lz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o1LMWPd9pGWYNihZBEUmm69yMSrumFn4KGAGeclje1ZwdBQWLhTyiIR-EYCnlkm-tpadNOKE-hQvKejuAdIfyjWamHh_bWvRUXIjIjHxO53rZqpwtnRuqqmsMX290SBwVf61MsURKFhpxJW-TIrpkrN7V9fy3WSIj-RJyay3TUw2eQ1PbVeu1hajF0gV_nFnjaYuSSR2TSMBVEuEzBnM1LhQte21ygfL1dPxVmJ1gzMokfpRTv653txwEGWiax7RXc5cGS3Ey0xkS0yfWo8zoYxQQHHlNokeRuJZISnTuJYdQDlmrn-GuDTQ5HDyb_o67AZb8CbV_VOdf3OCt5ekrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eizpEGX7vgUwEVPuFybzueYe5wRftPqAjwiBaO-lVYog1L7yEaOOlF3E6OBDv_Llrdda3RduuioJpIUb0Ygm_0K63ePI-SYVVemzwdzbPRUI-bAjw0iiijXTS4WN2vc8-BXXCcvRXQND0G4PtXZ6-pkxvoA-5mjMJceiOKs8E-rSQyhZKQotrotsHBB4lfbgwMNR5qMmaYuli5tCO6QbvJcyWqWax8G0MU3R5G4WPzXy1peBnCIExjTZYJnp1erBu-M1mFQvfGENk3MmNsdNEpSzV0RkXgYQAQ6sOfj-xtFJERqUjFpcrodfgudkiUw7zUyZesMew-R1Lk63yZmDSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rmu3m6I3sXzwJ20RsLSDjaN2r7tnC4CzvsnvHM-7xINd7mVsMEAPFwNvbhq_J2BHNOsR1YLTonijwghlhfPX-Xxowq6g8J1Gmd7raCxD0U7nMr2EzqrKfVMQhNu-_nA7_FQ7Pk72hSYf4V2I4ojwmUKfBCKkF7pYp7nl4U5gsjEZr_eqijFelDhLB6DopOmlQN99Dq1Yh9Op4rbplsKpdDVlsHdzaxhm_hbpyuX3v83MuoS61kTsZirjVDEHf2EwIQtz9GpwEDWtNZkY2XZjDEcseaqnRs8BalZuRh40OCSAweW5S2kmmxfSdlqHxAV7cP0CJyklWKyqJY4niyJ1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G8Y9ljDBCMiwkwPKkl56lsjk8ajY67QIOx9sNLohR1CzendvB39gjRiDmQPhUjpNZ7zXhMPrnoB7xlRWRmX_-OepRQ1I8s_DhDWSEP1xF6bEF2_c-gaegT2G63do1IA4WvmK01zfRrKl-_4lXuBxBwGBzyYT5lMSAOBGCBiXgjV_48AE4fNBZ5uwqv_uS2JDUFAGBzPo7NPzxB644RzAY737S4DshNwbAMs2zxFpdnAaZZ6U73tEOymBIUNsBAPKG0nwt78kb2KrDAgaXmos-obeyiTDOF8UHUNjK4vwp-_v1U0f1s8LqHq3TNtgnwpMvijry7puFqKe-vb0SY6GAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CcsMeOzQO1K-zcmAHYN_-hK140213R-Wn4rNLiZMQBcvSyJxd8WJ8y_yX52vuYg4YdoaoMZP_L9RKYQgqSyrum04aERvXyEECjNZtofcPMNWIGj1ilWxsrpu5kZwUuEG6DsIgqmcJy0MemUNRiC7Hm2s00TqqSkiMSlahg4UQ4o2iJbzwCLXchFVlQUny8CfMgNQ7aYccwbCfq2bE9jywynINgHxv7sv1YdsLurSklcv37_7Bp99r3tyL2otpcrJ8xmbZQ8FaggSjGsFC7IdQkWDWEoNZ2AHWSSCeUefjY5MzeKK3sgOnoma8rJ77Gkv9quqtxr4ao38hCQP97KNFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRJFSON0-L89un1atsFIU6jRRSEGpOsL9BnnxA-kBz5ZboHk6pG12PYOQRQ9PaU3mcIRzqwnda3oVPtxb4uzFn2sLMi43SRT_Uh0l9aqjjH4xtT3tThinvrphYafSJ26QgiVlRQOqJQxTInbh5g5uwpcngB_hoH__cXT2IKtsvKIhkk1vzU-8VOabX2DxxdWb1sLYA21TD_DVrEqh5PDELYOhngqAIXNo68WdgMu7kZ-ZS7BK43B-TFKtv-uKpgJRnTlLP4WTwHRDrfj9vw2HhqVlcYByt1Bsm4pQqJsSDTUZfoK3l8zDvzGUW8NhWPn-hFOKTyYiacxKN_9ooUjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMMHUOlwqpoXQtAOvlxGMtktxvBr-0-S-b_X4b-OqhffFrwFp6120xY6eKWFxBZKWH-FpxqtzL5udz_5TCJUjH8y0wVXSnLwenCTp7WuFY7h6CWdl_DXptnx5XJKs6D3D6lfF_lToBk6UpkIoZZndFyydhTOOl4hsDvUgV2ouHNd8WAdr5dODeE2EokBcg8O2riRVGzwt7N1bb1-yadjd7QIee5KTU2U_wH8OPbFDXyPtP3X4MzTZg1Uk2h3uOykpFu9BgueXEjb6LVEyU2czFeGYnhrka-OjBP9c7Zi7XFRG4HAqZw8X-RnWev_5sRvIPHkoS7SWW7ZpedcTlYKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBlDs7LYNWWpH-OhCkxay_aVsFZQjiq7XbYLhFxCeZ0wEFVf0HevexSNkGVvgAtP0ODBJU1jwhEEAUz-kF0ECITmD6ztljzBFIiqTnNnK2SZpATDSZcn82y935ZJb1tIOK8dsDFlk6i5KX-1tSdmX-8FPk6NGuGQ5-PgAb5-O4AeuitqMv-8LidRiVFjO4HPeORMaFYU9uBzb0XSgAJYXe6E4_tzf-iKDsPM9y9d2ki6PS98Xf59-LTG-z79ATW1uM2XaZIl8eMHPVTBk9_8QIQJq1Yh2wqBgMa9BjAxR7iFdazyB1AFArzPpWlusR0sHd-wDUpp-J301TL8LYaisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=KhR2CxAoflGvmJJFvTBNVnAoS8tOXAY4VK94XAU9WexIbmogB_uihUBcvV33Uhmll6jwmgHH4-kNhqCzff7lKB2tlvLfmxZNYxBMORgGwasq5f-nP4KEypSw4knTgG_mnt0hREwKBaUE0LkCYxmV3xVUYoeMobt0oSh3wGFfvoOx251ZBrdgU9TYgv_tYnKmgapN_Mt2JoxA5uu7h326lAZxxMjUZYxy-0HFmKvuO4wSTRwDXgQOlaaOT3m7rd22rn0cd09UMMaGdk9fn6WIFx3SuflM-E7avY6jM2Yf7BNFbKAsUckTU0TzOXX1c_YJ9ysER1N93wmwLHNAO0VImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=KhR2CxAoflGvmJJFvTBNVnAoS8tOXAY4VK94XAU9WexIbmogB_uihUBcvV33Uhmll6jwmgHH4-kNhqCzff7lKB2tlvLfmxZNYxBMORgGwasq5f-nP4KEypSw4knTgG_mnt0hREwKBaUE0LkCYxmV3xVUYoeMobt0oSh3wGFfvoOx251ZBrdgU9TYgv_tYnKmgapN_Mt2JoxA5uu7h326lAZxxMjUZYxy-0HFmKvuO4wSTRwDXgQOlaaOT3m7rd22rn0cd09UMMaGdk9fn6WIFx3SuflM-E7avY6jM2Yf7BNFbKAsUckTU0TzOXX1c_YJ9ysER1N93wmwLHNAO0VImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZLLEgP6o8IDGmakl_kzwu5wWrU5hgSBc3QS0uUcxkCaalAjUB5pJecP7A3WHnuv5YpALfz_9Pa7djaOFcB1Nc-fzfp2BM6KrI6XWJcBZmfJr41c_bFdDzqqPhKsSg9kKiVj8kgM-rFznbz6iMhq11c0wOTNS_FZ6VfBRMABy_i0G13U9SxAwvkoW89PHSACj9DBXaQZU1XvZ5LYZAsnIVcIIBpmvNZZKqnjQB40vNjGfxJCRs7Lr-i-WglHDRzRjvcLKWe0GQ7Btz_XuPgXVSKHEwwVAi49tZswkj9lLxsvdc3uplfpVcBYpJo8h0mmCavLNxOrT_gVVF79reSW5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggolC_2BAFg7xzCaORfCvA70Dj6zemxUmuDVkRQ59QXcPWuUG3wDvu4Slgk-4GDFm2oP9Xt9tBG7AR1KQOsS69Xl7dFbbo4blDWj6cC4aQyZqifHOoYvzJwqtP02ELV3JWzublvsY9PzYCUKt15jm-RqUyt_170YhCXoTly_Mcne5VawGkjGKy9YmUuS8GpGxLl2_5c6rWe6u0MOEDth0lC0gYt6BlI8m6R1QuCR8Q5PYbjIZHOyJ4hPPiS4Wt4mlZEalFqokhJsq9i7AVrw1AFi4NdRmnHdwZ7uJECE1iVV_0RNu5fSbF1JZ8I1WJDesRDqdgEAxGkKB6G_V0OmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN0zUsbrpujoqy-37TnaxNu3uI80lOYWz5nHtemPQRJk94kN0guYy_VjyBrY-1vev2iUMpKkIcZtX7l2o8FzMIqdx8zap66YN-7vcv-4bWUvw60-67ppqrkZ6dBSOmOhAvD5AZvF4rxHGdEYeD7XHdcAWp0NmCstn8Szo71S7Hz37u2OJ2ImZN85XmPNMAYzSqEKC0iF4f5EEvyWBD1ozp8KP77B_udqdGJDqKiRRQBGxc3qkuFwsW_G0K_-zBS_wAuUZBAguOik736EnyOr_kYIE8maNxVu9ifr8SpOMo7ZdG40zM1tMSBi_Rb-AjxFxQ2oANOQBN3CEqvgLyfFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECQQMjsYWWBm954Bm6wcXcv5LuIhojBfmqTFhQzDzm4-aCH50LmGtoEDDaB7npRsoyyXMWh1wSFtAbqzS6euCLx1DdkQGr7qy24L4EJ0k6JktZDHCkB1QDU9eM4E_mKVHoxTX-ByGAZV_MbCEwM_YXliW8w2qeGX27uGGbFvUnBpXvkHIw49lKxTU80hOcF6RckANZDH9zxYZQCLG3kz6YQA1z4hNuv6ZoIlIQ6NhH2xnNh0LsRE-g1yjEWOVf3EJHrj1jdqYuraGnChK6NUm0Xlc-PQozig5I6LoZGRSu5tckmv60-K1tnhyp44mYoul4_gChn2ppQI_KSg37yPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQGqxGMLQA4nYlHoXdxaGqUlVlkKBJMTTJ5MQr_0H8Z5KLcC3XRykmYIU9KFTiHkXLIl-RjYYL5g6Mgs7e9o_WZRA2SOwuXhbhSpVYRib24MT75AUFExCbN29HbD2BBj6WxT5MQaLyHCwyKQVYAMxxy1Zn9EFrA4yoAC1zQqWNFp8EfDUfoSZmIXCKvfApyifSavu8T7C_O4XpEUpbyp_vYmwzrgmhtu2Pqny8IkbdDpodbdKtd_U_x2gqC8JFlMz16YCO0axOCQI20LStB2IzFgCoazcbefc1wTH87FYNPmlTwqbqIxkiRivFlFc2WwXzDEtsDRQJhVyFygC-ke1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D55kUR6_t9Gpl8uxjE8_zflSrEKFsSi2Uzz3_ycd0RxjRPTUcKlA8XduRTXJszlLjHImZjB88PcY3tZcJbx3XuWPOlK8NEraF-j0J7SlX5gBmjgkJipNVTIZ2bKiNP0CiYHg7MO89pyPqGDrl6CMvysFTR4KAZpj8mYDl2hTuPb-P01nRb4i8dtfNswDd49vq17r2Vmobi0-CzkkcJLhVGHi8zMUxwV8U4VvSIwCDrt6bERxbCRjW0RbkoD9MZYyyNR8HzXLPrs-lx9Vdn0TcUjYORzRV1OiK1OucI7eECQAuVk2JYCBBF8sDWU2_yZ4Smuemfq25C07u13ietx_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TKs8zv25t09ILA-A6bcuy-xD8Y1il7ZUucyoPOttkEFDp7wDNt8KkFkhqiyOzgGDgqsMqzapbhQ8whMbVZ6Rjw2NPxBMWRnulM_UH9N7oqeiEc-hC3WukkZkBamCH-ON2vfZf_PMuAv4sBgBRmTH_0xQFGEmDJ548B8qgq2ClfGTN1zlvp0StLmTxt8jzSVlH0khhcY1BCartUITTFPE1TA-SW4rVZmOFWHXoB13Xv-NA164JpJ9DSZ6-malHy9oyrLas0afCfh2ebhWJWqpWpQL2KgCRkmtHDHHgvmgBJr5YiSxXTbNhNFFv_udiSdundqUReT97iO7LqMKWFubfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gm4UQF8W1x5Mhgb6DUcggSiaHH9_P1N5mJitJP6aiCqlY4-8iRh7_WLbS1KK379MBBE16E7APkB9d9wICM31QR_q4JNY3LF-7Btv1y2menq2Rkhj2NIhiIUkLS9rKtaI7ss2l16N5MRPB2uvrMAx4WIi8C36gNkVYY3hHSi0roLJaxp0FRooKCei4QhgK0XlyqbrIWRalBiIeQQplLF4d1m8aLv3SVkLx-AMWF1EmNR5Swbv3SwzSrPN-eK4mdDnVl1yBR0SpkyIxBhWALGBqxR9HUfIMr6b6rWfHEIgvf5uQIPyorDWh9gFwCDa6z9l4DkCE913nOx_vSvPs12-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JSHft7PfEaEIqcOJjD8IL0u2vIvq3RkerHMjCg7sWh-84SGei6lf7r8EyErz55oblLFhCzPrv2QNySwK-UU3iMbVTeK_fKUB7q8l2eGgugfp_dl_wjxvbRNj1UST2v07sqV59EbxxhMDaJYh19yUztPX9W3zpZTfl_UMKLqIahHGmgPfqtAQ5u3PRIvjj9tqOmauDhsxZIzV0xbna6lfx9o8adCjIZaPNGQ9h5j35Azd7bm0jUw2rojCgCqzUgBb-81_k9gQsz9oqhWtykvPKI8gLCCtBl01Z5NUs9SkieiiiG9dTlEdWrxXA2YHIIxYOrjeLqh8SFSFJHhosOo90g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_sRcjDjBgkbj2KOTkeG5qDbmxg1pukE2fivK795PN5VV13860r8nJB8HQiGTIE-05YO2WtLUNhXCexd3c7bcD0Uht2kgON6U5Df7iZcNPRK1zQsEpMgOmVS7utXaAYL2LtM3zLlpuT3vxkQGHecqzAye0PcEJjca-ARbBsJFH5UaQjHxAevKoewTPWKpSUoo8wPUDLTKU_ZVrE_tCyF3VuOTYc0KzozUFM_wKle-B0WQ370sbo_GezPGJHvpgZaS04xL8NH9WlUFjRIKR9hrqT3c80S2K3cmY_QyMzVjr0KXh4Sy0e2reAhBGWDYbYLx-as4UEvvaWK3MEOVsBYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/El2FCppWe1eTHEx4AC2OIe7ueJluF5W8Du08nZ7fXKJsRfq2fQ7m1vEfmCuf0EjnQ5InZiuS2PjGQdQodoWreEmzHDctnLxEZLShD64zGrwoM7hZ_L-Ryhvh83Abqkfv8ZWVwLaPBGUNF6u0ijY1gnHTsNDAmepLOEPSrWNzfqdJb9ZoluZXZhc0Y-E-mGiPj0CQK_WkcQcFjS6PLFmr-EXy-FnL3Cmyoa7bZsVq2cXajiOu2-NgOVDAj0VOhq7n85qJxZnwBkodpyzOQPLmlgVhLcLnwZmCGEhJjlf0hIj7W9ZN7KBoe3xnlsoqJQMHykX8sy0YZQIefUrBdjkczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV7PIt52fLA3P1dMcuJDVtTLLGS8hSJgPT7hdx6dK_DRzajOIm8PFKuoRIlOW6Gn1Gcf-Fw670pe2OEznRZcZTrx__5YaDOgVr0TPuI7eAN6uopYPYL0exMv9uODAS6b-20e7WBDzEpPIoKUOzwbzgwVeMuWbYTgc4rRPZ_PZ4J1woE3TcssDT7RTViajcDll6F21V9kDOjjp2WCBKBtHaxosciDtrL2FjZ332NJNuAE2ysNxTqODWK_MzFBZUk_1s1NxqXjA8RKXblrcMw0xZfMyBtEI5ruD8hqG5UmEVx1ihWHOhgwV5Zjlqteg3KYIcbn0vgSugoicpse1TuSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_GBOOC9_tSeOD2AEpNjunRqUNGKLYY28DOhdX8JiJoTnS_H_mL6EdUcjpQZg48qH5Xf51p3eW095e1gQrrveFR3bc1sYQteJM7SBGhOBADn1-tP-f0rHL5CD4-PrgbNiPBl8xRR8SbXDmhzc1a_CUcCSg6qVVpNAlLPXOdUn6U9wzhTt3uvne1VazYFJPI1GyE27-qvfUP13zHjtyh8lGY19nHHRhvGTCl2jmzxLVstAXE1zgOTugXprunkeNn1vY6CLPD4kx1pesHxwg4ofOgYeso-F0rwT9K0QJ0oFn41yqKjpSSK7-p4A8k9rMrbK1lFX4R1hhyKTnDl_VDTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lC-rRo4gPm-uKoH7t0L6lbsJI4Q7wLQpu52V_ddVZS0ampdu5R6fT1QL0PDtHzC3ysAPP-9jbAggX0c06NLfXjUHL1ukOsdWy_NhdLSHDFmLBVddXYRd1fajjNb7DmF6LA1uHVZacSU3ec9o90pHku3f5CpJIktv-W3tPZq9ITD3kZs_4KDXGRasr4qax5KgbI8JmOeDQL1NqRnH5T54Ygokgc94mMHc4G4IKNZOKSdA7H_zUcUu-typ6z-JunZl1Rbjc1EiVLrpPEp05-vDOAbJCSPXJG5O600M1A6Mhqfwndj7JRkMF93S111lV1fwgkGPFvMZMzMylS_0eE5kbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LhGporK2ANNQFefdwa_U3WR8voIM2hdqC9ICf8sSsy9zQX49Iyzmkpwah0TCQBJ3JgyFpbEAFP1mOCV7cclKHEZwbusYZnXrctv8lHrHH64W25qi5FXUxGGWGo5oZGJp9ytRqQoYJMn6ycEOnScCdln7wZ_9NGjaLYjxs3I2oSIcWZDuATFj3HQh4Q8lOUmeTX-mf6AkgDZs7c1i2aR-yHr3kBb9iZlH63DuDDkqPAFqhCMzd0L4AMF06srOhKH_a4Xvou2DhqNyYlUiRzs71H8DrCMrxkMW2jnicxfdOZxwFvqYKnztVFB1qxVFX94CQoMyoev4McZ00wCMyWNLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OwCuJMkfdJV_KE5NHsR8XuGXkK4lMjqgahnelnf2USXFUPHZyYT0yQKHZZZxjKRhba9HEUnfl4EFawwXN0WNVe2UPhLtcHO83hhRPP0jsTE5Z914ky9QYCfRXgdYtyFh__6hnRNfuTLb_lQ1gbstFGasSur2bS-lm1hh4piLGRfrz9jvX0pBHDFTStbbxJ061uhfQHq2g-d5IqYQRbIK9o-dS_NsptyFFXm-VSm_rz07v57fNb0gBgYuqhU6XZYMnydg7sbOtchA-N1P-E6oyPr-R2UhU8Wlpa2qikYf0f--fa7zjBLFvUYXFzj6_kOrr362vWIOQqPSrt89ArEyCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R18OFAk_OgZC2DDsqXiLgoz7-RonlkYu8C7yxe9lyrXJPRPovUtqszQbD2vmjgYVLXJ1LmMgRWMlhWqukbG3v_gUAeZ5bAzZqYZi8b9oOYOOPKWsrd4oEXkEKodd_CFcMRCbDwltqy4P1bR0_vjqeSvG49Sm2qIqjXB6B9dwt2uketOdVsD0WvcxcQFmC36EevJT5jhjczVk3cooxLJxsAhr96aH_Myp2s7CotQ6pkLpnjSKTTZ9RcCZgTkPqZAdEX65P4jJfUM4IoQIDnLNp_z8Z5Y9fzhCjI6IMctsQ9usBV1NZS7QUYEbVZyoXm7J8itYfQ_tFWFo9Vx2K0aEuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sr7zU8_EZlpaX8sa67TFGZ60FiNVbQoFhENLzfdMbfvEG1oi4UHdTyPZxpIVHdObT0Ao1ddSLc2VK1y8BtOIyH_gLZ1QwmDZc6qT0RR1DmwY8asTDiIDXGhG-V3781kn2firxCEgmdFtvKf17iC_thVFlokcvURRVJAtwaZ9zLMsTo-2bXUXJ6DXOZvogY6eTQH5hmkhXA5DAhiq1JFNub8nyYWbyclt0Kg21UReaCOwqMmPIuA1uoJ5T-M7PIobYGZa5jdn6qbAvQfqfASp0vKuPZjPNb7bRrjIAmksiaiJlIemM5JQVd-Crf6TloAIgDm-j5OzZ4Olu8t2R8cajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MGxx1NSy-UxzUmWhNA8oaLnzNEuXikdvWCvkAIPpElcngL66UudOqzOAjYuJhJ6NGUgPtTgiCoToedRCPX5itS2qcogSymoPzdZpR-TyCG7W2yXVTc473BU5Beb_OxtqMhwH8KhJikTX8dB8xIlH3-74UwH-_YpSG_G2WlaAJyHNwNfJNYf_fE0a-qv0tRN7mtsRdWtv2pnAB3LlDHcSicUwKdIanfGHd8mEPu0rvPxyWRkhr8kO9Y4Rtpskx-2nv7BkgMfaWAFouwAXRTmdOZc2STt0ZFwkmm967nFp2883D5QJ4LY32QsKfFJnLZgEwnW-eV3rqto8za2izDw8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fVFJorWgAs_gsizDCP44syXzEJ4vJs9_x8BpLmuJctnHAVbPuGLfTd2MsGl-nI0Fsc0ZhI8lS2a3sGbRvhe9Ssz23fWv-bcCdtrt5rXQ-hW7YT_-98viZGcvb9x1Z5EacMoS9BU8Zc1yJgY9wsnzKYKQJOgeNXN6QmPlkxvtC39VNrtk28k67yndKUtUbVJ1iWl_qmvrjW8PnZOEB_YIIgJlNQZ_C16Pgw9pLV0k1oFj76NDkdG8ESb2T_41H6LOkPa8J4VsCE8yi2ihkhFuwfiUFuYhhtTAzmJTE7qTgWbH8hBOuAl9D-siPk2bhx3bviOhUPvj9mgMniBvh0IFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qDkfgyKM6HT3eFBBkDnNjpgPLW4C3kdrg8CZBedmdwJxigTOsrg4f78QcrboiqU_RDBZSKwQJ1942w1SbLRS4W1Zvw1p7LRT8EE572wBeJe_XAi9Xwy7af1vMMhihSPY5chN7dbPeynJYnU9nmLEs4sOWOmlRQ9-_9Cj1G5hZDGW4XLO-kgWJzC6KVIWXcvoFH7nPMmSCUE2LXregeMq9Jz751oh8qKzUD5kJ5sRBx_0jsGc2sUkbynnBnqvlLOF21jyf-qdvyolGZry3Yco3_13hqVlUoKPAy50R9CVRaNMYG8qH6akDq3TXxjIrFkTI6XOokWmITon46wPmhwf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6zqtLSEVz2F7ebaJ5VfvXENSljEX6WV2wyqcaxLvVkdetpdTo8ySVist34-oEsgJnF3B2zNlCJYlRk7VGpc-7d-m5b7KMwjLAWY-AavbQOKqwxRqqMgJStmWDaKT9fZUmHLGEeunpdAQqtBGHvIMj4ChSwp1purKT0giSkTpUgVT2SKPuzpAzpXHNy4AIxqhf0pxOHEYLBzK1UcpBuQ-6W4WmZKCOcnbpHGu4NtCt2CtiOLkmnvhIutGAWYN-SBtGjf7CYLMhK_X3zuN75WxImG8B9BOfUdu91ROlfL8P1UyDHIkgWO0gIFVEz8XYdLkHFFK0PdM9T67s1tFXXN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XnNxL5vbFCYbCp1dVzLL8Wtwgymd7eV8FY3ZZPcsMf06-RzLNKrxDoOUknvVtDPLwVQSE-f_4R7kiK02uCZq8PYTaSFv1ktE_zRpBVvdjyBFBu7uo_Vouc-dwrQuckY_gzB4nPJSPrgsfd_x-WvlqRXq-F31b6O9zHClyjMTLy74qg4LO3C_Zo8PGtx1JscJW6s9UruIcKZYmYY6AOFGi0dl1D0sf7P2aVnFaYXSSwMriarZC1rVjHGJFpFu82EcQGzqzyra_n2lENhak8z0x7xYE8x0W-9wL-qJRSzcA1tVsnFdE63y28jY3vD4t0sMZn5ShjA4RVv6vCm2LyFfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l1mZzzgYof4oFS64huiwSLTGmkifC86aFd8N06K6u_xpntLvy020l7zO_vVMYL6TezK7Rg94eRzqiMTU6h6vo_WpR72gvdH8-PnYHNC-AvX6KNpCnzeTtZBfcGYkEO-ldjnTuUzD3Kgw6KoEfdXxTPUqLm7eKKEo2wDH0FbyX5Qn0-NcSKA76cEMirOLPQVzd8ET00_xQcwkBQ-ad8Rq0JdLjoM30dSpe2Ip1zj8LvUIz5mk0q5WE6sOhvog698H4i7CBvPAdZEyDpU4hL4dvaH158AbnSLe8umQOcHjoE_kthQwUWXKGzo6LoaFYjwrIDvjDBTPLajiiUVRWifGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7B5YHo-qnsBGWEnJ9Ny8L6Mxt1SLKBxqjoSdk9EEKuqQpaq9rcSuRF_fqdnhFxcNIN4vCnXiEPg4_piEJKOrAHKp3JUYMLDtjLsk-iD7PbUEh9z1E1XVfDxs9nHZgCveZ6TAh5ROtfTnVulAWDXaARhHd7MuuqI6a-92VQSSJsAAIEbQPiUdQG5Fbxw3Wkij_s9qJcDJ7r3q9DpFEFl6e5te8_-Vj9PkDAK4zS-U8Ti3sO6mxG5QeI4pa-EnKdxUbx_rnnOraeRE9SAmII7hIODE6o2WY76LyDeHVKXxkKpzooH2iyxv2v9GU2i1O0KKW-icooHDoXQYijwy8buIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=T_Ku86sTv0kzsfYogCjEczy1K6jvyURcmIVTh9nmorNX1J2VGOEP_wUI2PVLg3YEJt8TeIuntJpl_p7ZFgL5iX5wLzh3FsOM7hwb5Ig1cQQBCNAkEkZ9Mj0LO2hHal9_i-AGZsoXbxURrJ9xyuY5MBvv8ruUKGN4Ebb20y96mTylPpKtSAz8ym1LZcIWMcTnUdF3N5V2CAHg5H9akyXQHQAA0JuyiPGV15GEH-hLYBdxjlgGeg4NypszROPtVPNtWNrGeOcSOCnmdIOfZ48ZI9ZszCumFh2muABThKZ9rWI_THLyXf0V5yaebgOPtlqrwnhgRbp5aC7IVlYl0cmVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=T_Ku86sTv0kzsfYogCjEczy1K6jvyURcmIVTh9nmorNX1J2VGOEP_wUI2PVLg3YEJt8TeIuntJpl_p7ZFgL5iX5wLzh3FsOM7hwb5Ig1cQQBCNAkEkZ9Mj0LO2hHal9_i-AGZsoXbxURrJ9xyuY5MBvv8ruUKGN4Ebb20y96mTylPpKtSAz8ym1LZcIWMcTnUdF3N5V2CAHg5H9akyXQHQAA0JuyiPGV15GEH-hLYBdxjlgGeg4NypszROPtVPNtWNrGeOcSOCnmdIOfZ48ZI9ZszCumFh2muABThKZ9rWI_THLyXf0V5yaebgOPtlqrwnhgRbp5aC7IVlYl0cmVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7Rn7nBIu5_kaXiEnYDmBD2Wfn5w7_eXnHMj6OQV2cx63KRqbY7-qJ6xuuUPym7TVrG7FGx4Jw7cu8mIvOjxyoDxLUch2qsWBKEze7I_IyihYfZBqd95W3COB-8n_gP5szWLKmLq4g4o10aw1OyaVTdTNctniuWx-kR7GO8YA7y2rrhXvKm0XKyY43LiORrkTftSrmseCS1IJiZX2qJ2HsZLVfFuUm4ahkRCpwYpDq0b_liRidFEchVUGIga46c7_EhG-QjHq9BQ2RpmdLrxw3aO62wbSJw1vaeCtwzEklL9TkzndhPRDHw3-S9n7teDa1Aop-HzU5vt-v6pLjvLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=Er3rRxvEsD0NX55tb7s_GLo2OLNBbZg-FiLh9JdbTQfgoFRsQrZPZfbjatNNgqyviWPABv9nLtGjru6Z_6LhI0ZyaDLXvlh68UYc97NsHSOiUNIHc3IXEDYARiT8fe_bIEJBpIUAn1DqMJJYVOGRZcyVtjWurnELygjDauLkWgxE24v8AIJkUP1qd---16-IZtalONXv5Nk6Ocu9q75KisQJUaYTbzUc_N6kktCzeatG32oYvsAFBLOewPIXSlr_BkLTQdRP-302gy05ICDUyaZ5tzCkne9LayTMOFGFUR5ygq4q1DIcvm_16XjzsnnWRNHVvROBzSDeqzXMlNufKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=Er3rRxvEsD0NX55tb7s_GLo2OLNBbZg-FiLh9JdbTQfgoFRsQrZPZfbjatNNgqyviWPABv9nLtGjru6Z_6LhI0ZyaDLXvlh68UYc97NsHSOiUNIHc3IXEDYARiT8fe_bIEJBpIUAn1DqMJJYVOGRZcyVtjWurnELygjDauLkWgxE24v8AIJkUP1qd---16-IZtalONXv5Nk6Ocu9q75KisQJUaYTbzUc_N6kktCzeatG32oYvsAFBLOewPIXSlr_BkLTQdRP-302gy05ICDUyaZ5tzCkne9LayTMOFGFUR5ygq4q1DIcvm_16XjzsnnWRNHVvROBzSDeqzXMlNufKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=tAi8WX_q6e154AXL0SpawgHXLMmysmXefDpCB3LwFsHGs601ZAsJvi3jRf1_YT1dOVyafdH-BJJLRRMB4kVyGdrRrBx-Etqjt9RnmsOH5prt2DsqGKKu0_x_4MRcvCH-VpejQ5kKK0MInsouNCyzF72T34TVJttLBNsWO13zF7tr05bR30xc0fc4lLVwFVHXrgTtT8P3o_8A1D47uGgT6SLeVfZ75QJdDxaYXTQNwlZLsoe7VaZ2I-XlnZY1i4WLIIuFU_Fpf6FNfM5NK1NyU3ZUCd7FLyPQK2gzcW_i0jeqiy8BlstYYWSKxVPEL7ypCqInB-cRdGQ8reqd-P_obA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=tAi8WX_q6e154AXL0SpawgHXLMmysmXefDpCB3LwFsHGs601ZAsJvi3jRf1_YT1dOVyafdH-BJJLRRMB4kVyGdrRrBx-Etqjt9RnmsOH5prt2DsqGKKu0_x_4MRcvCH-VpejQ5kKK0MInsouNCyzF72T34TVJttLBNsWO13zF7tr05bR30xc0fc4lLVwFVHXrgTtT8P3o_8A1D47uGgT6SLeVfZ75QJdDxaYXTQNwlZLsoe7VaZ2I-XlnZY1i4WLIIuFU_Fpf6FNfM5NK1NyU3ZUCd7FLyPQK2gzcW_i0jeqiy8BlstYYWSKxVPEL7ypCqInB-cRdGQ8reqd-P_obA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qimsBjdsiB7yrwI6gHgv0NXmgPyFCQRUA6zvlMsJ6-ftURoQi07JGwg07reqsm6wWHYuzxtKsOk-5psvEYfTmdlAcq21srnx8Ht-UovjwCu93ttqVpPQ7Wzp-Svlht-Gv2xjOSC-hQgSeGPrqeeraQa0ZiTKevfAeUS4EmbNNBe3Ukm1FkIDLnY0D0_K2b-ITS1BGjChX58Sklbblomhu4xhwdxZB2IiiJ-9FaNSI_lJhoFv3QTlLURXWjyrJxAftVsoETdKLnFb1FBJRT5DXxXh1i3rLYgGLbZjU18qH2tThfononposG6WAV9tg25k_TzRhc2osVKEWht1jO-IPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHX_ZBeq04JUmSg1vfOjKbTa46tnI_LvLK9N1QyC7ySg7W8qIL0AUvZf70FFawBEMixu2QSlaanXnbEGoXL471T1q0jiEYVXeau5hASc5N7bPcDGGqok_rV7a7hf852XIOu77ROiFYW_CbmM0lv9gNGoFY2j7tJJAw-ooQMvhBvpX5JXIg7fmLYk2EIMHKCvNv57w0mKlG-yqS5r1cXg1BFK9mY-SfkSuZLu2Q08QO_LCuohMXmxMUpV2Mr76Ur_vllBSHHRDToCuH3A0bEJ2cds_MT3YskQbQR3kYdnWkZX62SBf8ofv1-OsmzmUXu7-5mVAC9QRDc6gBGG9-kRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bdB5dJdfqs4YfQtSH1LwvW65NcXiTuId7Kl7-ByFDaSSqSs37tiax_MKaGd5E5VN7JHH1c7NrwEbeeA3AyB6s3IDHsYDdNsDSTGf93CtpblTDlKngHjFh2VVIRBemt4HlgcCjyRQzen5olbkT3Lb8RsKescX-RFKcBsN3nXuRPurB-0mKMPN2op_UrphPQW3mlMxOivdMfdkTTLbBYYkIzjsJU18sWeMQpG0bEE2QCDVmhw-Z6D-I_US5O-qGgmwvf7IIkDxJ3xWByDOVvFMIqY2tk5hMUVFqisenvIWPLZP2tHjmG8GrPAJD8UyKIJ7gmdElDNSCpkvZRAhMg3RTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwPj6vLoaU-BYTfzeRuahumiVA1LzDSJwpSpzO0oTvhMOrtE58xrjolC79UoywGqxQSz81_z_z7-8L4_Gs7RWWxC0KE6DTop0Ma6ulb2zjuuzAanV9iX6fmTKF1jqRGLM-M23DBpvxx9ewCExdfPQBCuCzfp5F9r0SzGwcnkid2e7nwXTRmOGEP5pYfbbPLregNx21d_MPv-RXhbyV5eC1M24XN0LpXuxvw8gEgcr_eBtfAiOzoFM1EDDX9GQSbE1jFnlWog9jmhJZFagJ34KFOIWz8YirBiLHB3vy0TZtbk8JEcsiUyD6Fg-p_P4HinwioVQrGZUAMQwvMeI4-CEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tW83KExUQpCK37mgOJX3VZJND35NaEDmqhim1G8-y_i7VOX-8GeO-2BoCPBrqnxmmG3MTBEe65rnrS1qhFcUa-eHRe4-5niEeYC6JtH5EtKJ49yJBcKgNLFtEmu1PcRgl43cHtdA397FyPQ9W7nxH0P0lpu6BD6JpPiAM9QJumEbSizJLe7Wd0sBgLXI2ezNKF1r4_XPA_KScAyO4XDZnWm_o0xn8FiiZmsmrg64_YqKDWT1gSS4qqqbrgQv8NGmV-L6xnkQsfQnVfARkvipvZF7kwgfW9yq4aZ1m6i3abxm9hdH4O0aCu8Jqu3QYyOrhrgwiiujpx6Yj8M0W16fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
