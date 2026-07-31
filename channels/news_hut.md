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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 01:04:36</div>
<hr>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMQFNbbmuyn5It6LttqdteVTwTKCG-w26gU5jT7pNz3xIYNdC7BIVMybMleVphQpoo3sB4PAAwd3PENK30M5SQCELb6ys0g88mPY-iefrPW8fcTSXUus0K64j2qEYyn5dh9cvuRG4GDTGM_KsNfv2jA8Li9CaY5-3bD9VYTOPcBZUAvBbbYH14yBrnxpRnAPH-yQ02EfL5OPW3L_Nd9d_7lxkdBV94hn5gTSYVhN--oxgNp0QQ6jLc6n4Ck55TOV0wY-qhL3cnd71OTL_fYaAVSd9xz9CrAxjbVlqVukAcyGLvShiulBhJ7DUk6b2VR_qsCpxeAZHOcbf43w_ukoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=Jv1ted1NckymnvPw9h5hsSRTepCH6f6Ofk0MfLoUvWWLJZTjDnf_zgJGIORhdkqYc3w4DxSE8Kv-bRVDB7quZgje__qBNHRSLRD-bjyXSJuEQC6rTb4w4qMRdEA_A1XwcUXstUUmB-7KwW490M9x0P9tsin2muEisrHnizy-9f5lyqe-KF47UBkvRBRfQ8ma9k8qMdkCuackarbiXx4D5bNmTXMuEW5zPn86L5FKYbSSzzirF82KpFGmNPZAjmciXTk-pTLW7TKnM2hz6lmovAGzq-BK-sWeYAjdPy9Jg_E4ng2PqCDhFnP01UFeBTOFKV9goO_Q9rxjdsDeUowGyS3Tqlz2-ECj3AUo1Wo-mNIgnh5QKi80xcttXec3Y5hZ3hUOQA0COtxheFMfjVRmwX-oFeTO8YL6E_27_22ac9UYHmLGNOKYeMEl8s8znXzaUnv0oBCgzxUN0bQtMN691I3Bfxb9qN_eeO9WVB1IZCtuLovxXLJLyOTN_hf_OePdTZUv8-BLhXMoQtLCnlu02wBSKXPtUjfBGP-X1fmGDWzX9y-TFP5G44QOa1_rSUZGBa-MN8QTPpeoPzt4IAeFEcmIEfDWeCZqGfQYZiuRfiJv2NxFUckCFwp-D22yIxgQugR563TKpQF-PhWoWapLR4HMcN6cOkZ93W_75RcDWX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=Jv1ted1NckymnvPw9h5hsSRTepCH6f6Ofk0MfLoUvWWLJZTjDnf_zgJGIORhdkqYc3w4DxSE8Kv-bRVDB7quZgje__qBNHRSLRD-bjyXSJuEQC6rTb4w4qMRdEA_A1XwcUXstUUmB-7KwW490M9x0P9tsin2muEisrHnizy-9f5lyqe-KF47UBkvRBRfQ8ma9k8qMdkCuackarbiXx4D5bNmTXMuEW5zPn86L5FKYbSSzzirF82KpFGmNPZAjmciXTk-pTLW7TKnM2hz6lmovAGzq-BK-sWeYAjdPy9Jg_E4ng2PqCDhFnP01UFeBTOFKV9goO_Q9rxjdsDeUowGyS3Tqlz2-ECj3AUo1Wo-mNIgnh5QKi80xcttXec3Y5hZ3hUOQA0COtxheFMfjVRmwX-oFeTO8YL6E_27_22ac9UYHmLGNOKYeMEl8s8znXzaUnv0oBCgzxUN0bQtMN691I3Bfxb9qN_eeO9WVB1IZCtuLovxXLJLyOTN_hf_OePdTZUv8-BLhXMoQtLCnlu02wBSKXPtUjfBGP-X1fmGDWzX9y-TFP5G44QOa1_rSUZGBa-MN8QTPpeoPzt4IAeFEcmIEfDWeCZqGfQYZiuRfiJv2NxFUckCFwp-D22yIxgQugR563TKpQF-PhWoWapLR4HMcN6cOkZ93W_75RcDWX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=W5KUXZGiyEahOEexxHfoWgFUpNhHJzvcSjfEZUuwafcc8uNBxOJT579EwuZk-hyy8cTL2z0Su-hAAKc5_dwQVYk3XmzP8nsyZuM2Lw5AJj3Q6cjKj4etmhznfjALtHEzCjtoAjO1t6kGCzPMQ1nBKbhStdSmQhzxpXLiMpvkDkMK_DboDnzHKeFLk2qMu22hPWyligrMCrkQjaLkh9YE6E58kJf798bYMRHHXYtvVV_VJpxvux0_pJ5ws6dGllBQPRh2FwQNpKVqQ2iXqkrCj63HezVdP7bTe-2oZV-cyypwCZM4Ni7X9wb2UD3ej4IKIlMQndOyNP96lCljI2bzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=W5KUXZGiyEahOEexxHfoWgFUpNhHJzvcSjfEZUuwafcc8uNBxOJT579EwuZk-hyy8cTL2z0Su-hAAKc5_dwQVYk3XmzP8nsyZuM2Lw5AJj3Q6cjKj4etmhznfjALtHEzCjtoAjO1t6kGCzPMQ1nBKbhStdSmQhzxpXLiMpvkDkMK_DboDnzHKeFLk2qMu22hPWyligrMCrkQjaLkh9YE6E58kJf798bYMRHHXYtvVV_VJpxvux0_pJ5ws6dGllBQPRh2FwQNpKVqQ2iXqkrCj63HezVdP7bTe-2oZV-cyypwCZM4Ni7X9wb2UD3ej4IKIlMQndOyNP96lCljI2bzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=vpeGMwv53HQhGesQIAO9U8eFWUUyYHkpS61dbBVHziRAPt7KZy2N4wVYVbDL7JBYEVR0D8jo9zNuxFvtEOtXqjQOlBZcuChxXet26AjOii6pAUJyTxDPFgzeUGICGUkB1JrHWQ2d2skSboNzf4OgT8O6rkbQmb8Yjx6FhuOZfWWUqHekgpotjh1dF-oynomIVraufQLmD8fUzd9JXsUreUbPMVoLrDKgxt-QdQJ13Q7AuET1U6YD_dYl9I4K_J3udJrit0MyBCeitxRfVj-U2d_QZ8hD1ceuMAWW2zY7HJeIB1e1xWMoTs-QCDua2ti6uDSbAguuysXmsqFHXlH5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=vpeGMwv53HQhGesQIAO9U8eFWUUyYHkpS61dbBVHziRAPt7KZy2N4wVYVbDL7JBYEVR0D8jo9zNuxFvtEOtXqjQOlBZcuChxXet26AjOii6pAUJyTxDPFgzeUGICGUkB1JrHWQ2d2skSboNzf4OgT8O6rkbQmb8Yjx6FhuOZfWWUqHekgpotjh1dF-oynomIVraufQLmD8fUzd9JXsUreUbPMVoLrDKgxt-QdQJ13Q7AuET1U6YD_dYl9I4K_J3udJrit0MyBCeitxRfVj-U2d_QZ8hD1ceuMAWW2zY7HJeIB1e1xWMoTs-QCDua2ti6uDSbAguuysXmsqFHXlH5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXk1itqMaVm3o8CBdTqlkSC06THVgXuYb8ONC1DeiHRl4UY9NRJHGoygdf1jWk-wVXY3AmIsQS95OK2N168PUZVmOgAov2AeQwQYpnQK9RJSn4OG9hFWrtZRJl04rcs4_UgLMupowA7yFznAhLzob75dtdg-KtvdOu7bsc4JLDuzM96O3jt8XW0ZJytIExm64OKWymxl-8SOVtI8nbtUWzLJ3TQzAuPqUG6f2mlQRG40W5s45vfPXyVNQUh_fSfCgti5GNoVryOcQDZBuJ4ToaHuuvFPGKUlRZXTjHlXzDJoWdooUCWpnE3xw5XHO66IsnNsdaEfJVkyc6OSpnJKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=G7HQJSjJuUVAyW9zSVnhH6kt_DBxQR21bgtWE1A8MehMz-Zh07qBz6oZhjlcJCJuWfotWBNAZL16qcTRxf3dgx8AVYebDNpJKKTFuqAtbRM5EJ5u2MjyFeRgwCLwYWEY2QSCTHyYEpFTbdUIPblqyzZjrfBRB3Pvf1CaJeWRTDCzG9Ptpe076Lh02hfm-9B37uZ8B_5vT2IAgiXgJA1UA6M-Y7J0UBZ5a6Pl6sOW9OZbIBSJvp9Im2k33RsbW9snUF16_Ofa3Ni32AJj1oK4DncuAsM22_lhw4SgG6NrxUVZTuI5W8w1Lf4M7gi8krifg4t3hJcbE03FJ2Tl8K0giQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=G7HQJSjJuUVAyW9zSVnhH6kt_DBxQR21bgtWE1A8MehMz-Zh07qBz6oZhjlcJCJuWfotWBNAZL16qcTRxf3dgx8AVYebDNpJKKTFuqAtbRM5EJ5u2MjyFeRgwCLwYWEY2QSCTHyYEpFTbdUIPblqyzZjrfBRB3Pvf1CaJeWRTDCzG9Ptpe076Lh02hfm-9B37uZ8B_5vT2IAgiXgJA1UA6M-Y7J0UBZ5a6Pl6sOW9OZbIBSJvp9Im2k33RsbW9snUF16_Ofa3Ni32AJj1oK4DncuAsM22_lhw4SgG6NrxUVZTuI5W8w1Lf4M7gi8krifg4t3hJcbE03FJ2Tl8K0giQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUVBrwJwvItfhBxOzHC3vBF6I9kA75xgRWTImU1cvbzisGlt9XIBiTTtSAvKvtg_CZH9E1d7yrj6DXL34Q02GnkIPY8q8CY9v9aVz9d6WsvtxI9e3S7r4DO53dq6xJlXLbMj4yheIoeZ7LeYVPMBz7SjtubyqgDVZdaPUcl93WmQmXrzRRpGV3t8sSZnSAnYG_Axrw4KBqgiHfoacpcB_hxNTtLVayBzDhy-sFdJ6Lumd1rJtYfnZCh5FFqgsqxV5hldTrMFH9vAaKKEXkRYUKVOZgo2uNjRCgR6Wf9AZAz-iv_--vusLWzql5XwEWdi7K9uBIkxAUFNTSbtWMnoj8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUVBrwJwvItfhBxOzHC3vBF6I9kA75xgRWTImU1cvbzisGlt9XIBiTTtSAvKvtg_CZH9E1d7yrj6DXL34Q02GnkIPY8q8CY9v9aVz9d6WsvtxI9e3S7r4DO53dq6xJlXLbMj4yheIoeZ7LeYVPMBz7SjtubyqgDVZdaPUcl93WmQmXrzRRpGV3t8sSZnSAnYG_Axrw4KBqgiHfoacpcB_hxNTtLVayBzDhy-sFdJ6Lumd1rJtYfnZCh5FFqgsqxV5hldTrMFH9vAaKKEXkRYUKVOZgo2uNjRCgR6Wf9AZAz-iv_--vusLWzql5XwEWdi7K9uBIkxAUFNTSbtWMnoj8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=AvI_0iOjPaUPGOKYAhosLaWT2wbQm750Wz3Z5NqugBPr7icHo2yeQFfyQD6rPoXdGl3b7MBPrzM26vKi3RCtbgN1ia5DxWK_QNN1nthXIWM7_g0_Bet8U8BrdacVqfVe2szpq2UJHGuj5DiX9urXDLOvV8ZK3jws-JQ9vLOnTJGEiZm4Zf0KOGhhlNj2IsPTivvHEpCmb39tDlGcKsW37k9xQWqzurmBWar1GmR5Nt5v8HVkpBF5UUaFh6m0umzTuWVtOZz7ms_Touat0Srt53xZFQ4YuExYQaB4moAPFXqZnlwWPxlyVtYvPcxvv0kRw4IHMMhn7MIa_ltpIIEB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=AvI_0iOjPaUPGOKYAhosLaWT2wbQm750Wz3Z5NqugBPr7icHo2yeQFfyQD6rPoXdGl3b7MBPrzM26vKi3RCtbgN1ia5DxWK_QNN1nthXIWM7_g0_Bet8U8BrdacVqfVe2szpq2UJHGuj5DiX9urXDLOvV8ZK3jws-JQ9vLOnTJGEiZm4Zf0KOGhhlNj2IsPTivvHEpCmb39tDlGcKsW37k9xQWqzurmBWar1GmR5Nt5v8HVkpBF5UUaFh6m0umzTuWVtOZz7ms_Touat0Srt53xZFQ4YuExYQaB4moAPFXqZnlwWPxlyVtYvPcxvv0kRw4IHMMhn7MIa_ltpIIEB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XkbIQrD2N1wbmy1g3-Dd65Z7s5SbHxTK2Zz_jcJXcXmtgRB60YCE-juaXge2_55p8waeq4h2xkEgiOmi6tUVvBKGnaFtWvxjhRm5ZSTVVp-ip2UAfNQz44sJLXufdaeDS7p-nwN_etlLLdpdLpy150ojwGnCvYUro8VVZ03F5uS_0eUxEJi_0tvMgznuzv7vcgdCpsGiETlF0QdR7OCcu2FD-lYLrJD8znNnXPoUBFBpxrQcku3obTV2NwgbQS-w5RRWT0JY5UmT2sD4tT2ByDudtizuxyYCHjBok6Zy6v2UtgPcZ5OhRZvsPFJqsov7TlBXwBedE9T09RC5qcpR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XkbIQrD2N1wbmy1g3-Dd65Z7s5SbHxTK2Zz_jcJXcXmtgRB60YCE-juaXge2_55p8waeq4h2xkEgiOmi6tUVvBKGnaFtWvxjhRm5ZSTVVp-ip2UAfNQz44sJLXufdaeDS7p-nwN_etlLLdpdLpy150ojwGnCvYUro8VVZ03F5uS_0eUxEJi_0tvMgznuzv7vcgdCpsGiETlF0QdR7OCcu2FD-lYLrJD8znNnXPoUBFBpxrQcku3obTV2NwgbQS-w5RRWT0JY5UmT2sD4tT2ByDudtizuxyYCHjBok6Zy6v2UtgPcZ5OhRZvsPFJqsov7TlBXwBedE9T09RC5qcpR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=e07J-KyaHIPycX3xWtVxe8qrgaSQljVou0QsZNwQS7InjYaAgm8yfYurEodzeUFozkc7x8CWBY1hEUtZepsewgu7969Ol8c5z0ICKohwFWRiUbXhvBHabQMrtK4iQ5edZ3XUhQYaHQvyeysg71CAyD_RLjPybvntARXf0iRQU2HoX2UOlQaPL_loKHVAFnfqe3Vvh42Aijco6aM4FaEodrD1nlCZQAECyGjExPaqj7fDOoclm5LNi3R8EfLzrA9Hk9-Joh1HMiGVBXiB0EWPOHRpddfm9L_bwcGwB1NELR-avN-Da0E56cQukUrAAh2_hTNTbU8A94CP5g4xsqTnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=e07J-KyaHIPycX3xWtVxe8qrgaSQljVou0QsZNwQS7InjYaAgm8yfYurEodzeUFozkc7x8CWBY1hEUtZepsewgu7969Ol8c5z0ICKohwFWRiUbXhvBHabQMrtK4iQ5edZ3XUhQYaHQvyeysg71CAyD_RLjPybvntARXf0iRQU2HoX2UOlQaPL_loKHVAFnfqe3Vvh42Aijco6aM4FaEodrD1nlCZQAECyGjExPaqj7fDOoclm5LNi3R8EfLzrA9Hk9-Joh1HMiGVBXiB0EWPOHRpddfm9L_bwcGwB1NELR-avN-Da0E56cQukUrAAh2_hTNTbU8A94CP5g4xsqTnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=E4H1q2AJi7Xr_P0sPap6iGPtjJtpGXGSIXguFEReUhiWfbuGG9RiNvdkQAgISW4rXqPBWdfssoZawg45ZN3HGYYhG6UgwjE5DSPJ1hFcgPiw1xlKA7JAHoSw8Z8QrGzzYUTeUNtba9Yf2NwBJFf_jsmfszD5WpNFN-253_LIw4OIBy1h7AqVvtdKKbcskGdB6Ykx6__HX_0N7Q7VT5VRKEIUJ-HBLnn1snCnyVn-zDelLl4x_qvRS_Scxr5VRwKdqtkTj94V98G4lxbYqLLgkrR9CD8ZF3xCn1Qyb1WwbF2-Jh7gckENm8BOZ-H6DUr670Sr9zdzQSBXScE8JqNwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=E4H1q2AJi7Xr_P0sPap6iGPtjJtpGXGSIXguFEReUhiWfbuGG9RiNvdkQAgISW4rXqPBWdfssoZawg45ZN3HGYYhG6UgwjE5DSPJ1hFcgPiw1xlKA7JAHoSw8Z8QrGzzYUTeUNtba9Yf2NwBJFf_jsmfszD5WpNFN-253_LIw4OIBy1h7AqVvtdKKbcskGdB6Ykx6__HX_0N7Q7VT5VRKEIUJ-HBLnn1snCnyVn-zDelLl4x_qvRS_Scxr5VRwKdqtkTj94V98G4lxbYqLLgkrR9CD8ZF3xCn1Qyb1WwbF2-Jh7gckENm8BOZ-H6DUr670Sr9zdzQSBXScE8JqNwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQTmxReds7fgMeWH9GnXjd-JT4rmg9K2NKc6oLpyi0n6KoIMkvRT4dGsk6rTVIAJ_TqX6AjK18z2-XDYYje6Ls1uFUgOfJ-teHqVvZAFE5eAU2wgf4PNPBD9ZHmQcFRm2fcomp55ecGSvF6MYC3YuQGiqLwbTqufnbYi3Pzfv3S4kmodOuRxSjiMp5yS-AHX4c777pVxxhA0H_OkPhfcEdqnNjlmIZvRdJNOCuhVCZmu96GuPXcwoPASPD2_rNKs_C8mynKpY9z50BKujZrHOWTz3AjVAY9viyNe76uYCNRQC0ZzWn1dJCJ8QrhGcASEPylrqpzycLebbZynRdR_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqCy8ZAA6HL0F92EZE9p0YDCiJlnny-G1SoVJnXSUX0UfKvnaY0cI2HMpPFME_RuvmJPXlP1FSpgBhycsUjj8hS0uYfBLAm4ZHcrY7tfGywlixupyAVqmSXaBdiCEI5fmWuBb301KzFGB38J4Ptq3zID7H_K9Zy1szjl2FeZGl9Bom7YP8H-XwWC6C3bRUqb_n1a_h-qaBKPiM2VZE4_fWAzLdh0DxXm63skVg0AAunP6JFByqzSWFJm0Aaa70RD9qHiK2bnaDFMJbzvrHgY74WDgP4SudtBA2B8r_PZtGeDgtBYkwi0uCUhN5BvvkxD6jik1bNJ8fb7L2gnXmkYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=nqL1o3CD57Nay1zmQRLdZioWou-D9FenzmM16fOMaxNY9V-UCrGS0I8t0di99wH3dVbisCN8ZndOrbTLdkiTthzPq1HzTrLxbjxiKYvq4tKHMdG1y8wa8xuARrEQGCHxCMAMILYv9W6uZuNW11moeLFk7UfbHVXa_hUT7Ch_ew8fLTZ3tIWiBfeuCSXwN9NXK6uJlASyqOUlUSF7lEIHrvdMttRHtq7hX91CCmZyiFbtkg0dOvg9RinRotPF9qjP3GomSMhT-Df2iDb9zx0t4iwfhrpdNylh_3zObefgHDwuwqMA44HBvi729ttzSJqfwgpi7lCMtdLSlv2qGLJptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=nqL1o3CD57Nay1zmQRLdZioWou-D9FenzmM16fOMaxNY9V-UCrGS0I8t0di99wH3dVbisCN8ZndOrbTLdkiTthzPq1HzTrLxbjxiKYvq4tKHMdG1y8wa8xuARrEQGCHxCMAMILYv9W6uZuNW11moeLFk7UfbHVXa_hUT7Ch_ew8fLTZ3tIWiBfeuCSXwN9NXK6uJlASyqOUlUSF7lEIHrvdMttRHtq7hX91CCmZyiFbtkg0dOvg9RinRotPF9qjP3GomSMhT-Df2iDb9zx0t4iwfhrpdNylh_3zObefgHDwuwqMA44HBvi729ttzSJqfwgpi7lCMtdLSlv2qGLJptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=EI0auyaRKEFckshP2k9Ver8Yx7di4M8qGjkRZBqLjRuSe3-GfLDCsWfeNsIyYiejifPWXdorL98NEm6bf7DZKhkvBST1kvW94TpmC-xJia9EjD7C03luLWowxWIEP6OTYFRTTqBDZc8aCRPR_463J_ZM6WZaEvdDZwvNGo5fFOrbiBrWrSXIHMHLIU9YoKRbwwmnwLsaGZUQL4T2RteyoPFpejYW90NQGktCXoFlzY9v2926sQoK-4tC1sqJ4Plnlf9bKP-yM6f6vw0wT7deBgq_TY_kqciTB259gH-UQ_g-hrzXb3uFxujum88gFgvqSYtKA6JqFKEXNYATRKLMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=EI0auyaRKEFckshP2k9Ver8Yx7di4M8qGjkRZBqLjRuSe3-GfLDCsWfeNsIyYiejifPWXdorL98NEm6bf7DZKhkvBST1kvW94TpmC-xJia9EjD7C03luLWowxWIEP6OTYFRTTqBDZc8aCRPR_463J_ZM6WZaEvdDZwvNGo5fFOrbiBrWrSXIHMHLIU9YoKRbwwmnwLsaGZUQL4T2RteyoPFpejYW90NQGktCXoFlzY9v2926sQoK-4tC1sqJ4Plnlf9bKP-yM6f6vw0wT7deBgq_TY_kqciTB259gH-UQ_g-hrzXb3uFxujum88gFgvqSYtKA6JqFKEXNYATRKLMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSXBLqVaTEa8Gitv5WJzFk5yzHNgkz9aQADYG9rcG8PDndxLsjUEqCQEBJhqbIde8NpxiM11LN9tLHqYsVmneNUzOQeG0jFCmygkyBz6NYBjYkWftW-F0NuIqWb2sH8h2mZaMKcRAavrtQO274oRkzxXNlcTgYsQyI1lz_t-oEAbVhCfUCPSoqaYQNoA9CQqZYkMCQnvxp1St7117UpzbVSeBahUSFhXbdcv6MU3mBe50fgGx9IL6kfUNPMPoR8DhX3kTB4ah8CZ7in9k5fFQFPNGqljGK3WCYkz-G7EBdrmYowGmGE8NVgi-9eWzFLsIn3SQEdXpHrQ-JW2zjxyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxQI_ZKVKkrSbnUo4dzgEPEnX2fOgvGd8_HMc5RJoG_h9I0zzI8Qt_aGWrqpu0w5yUzpqIdHwsau7Y_GgOA7ZzaQwmfd6XfUdYwhe9JK_1I7p6xZRiqFFXdOsw5ekHeIcOHA662dsDz2OFqIyxE2gjKBTZGQ9PRO9As6_zOlSoU1LVg7UaqHdNnmvUriP9eJKifhxN71XhyuAKjWmKCcF6YWcKoVRtGr_bxe4gXtaSN_s8t4vnmTz9aHNu9ucazx6gprzqmDL3Fc9BcInNtB7pzwcMcdzyhDepowQZ0j0hALYMbzwQXqgMP3BYh0v8X8pZpW5PlVRiPehrkn5Ie17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmD6U9pVXgTGW_7wTLelFPIKmk1HlKHCxYAY0COoyHtLlyqTiry0XyzsLjIkk5aJltJDx4ZRBM1GJlNwu9vD2E9jgIw5EgJppXkioCb0iKyGoWSNBvEm4ItCwtg63Ov3eGDZS9V67O240-0UXP_o5h2fVzO8yuT6I6-xS9NYjahH4eI0Z1FjqmjLAhB4TzUPpsLgWxkXZ9XKv7VroGPgC0v_KrWJU8I2_V1KAX_kjoPiVJz7bmvumU0z7mUYxOEPF-7DP06wt72YrGTA4lyFL7q2oB1y02TyBQp4_dNQkaZsvzhrODFr81KY60ZqvRSi0-JEvYSPWch1JF_e3bxL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=nSXRi1IvyAWZPAYGoqxbVFiDWX3-afD2lZ6bDOn6sFEa84pkjdwZWfpPdQnL2j1GkHbBz8K08JfWl1aD12VGxPMd5Aq_3Jr9jA9X3rUFB4TsGPo0c4oyMauXE8zOLb1WL35dw75Xeh_4Np3u9hwCgQvR86C5eop89gaDv9336RLC9rvGZaD7pH7tDGQwHjbY8k160RN2oqFrUhvXR7tII5JdIApUUQ2xkugsT9IjikLQxbsKn8edclLdrrqCI5L1pha2J3Gk7P1a4FlMpoCCYLrc7lBL5ah_DTt1_KkabCUk4KDBlo2RipsDZ6SKco53ktAX4pXdglHrEGJ38S6bCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=nSXRi1IvyAWZPAYGoqxbVFiDWX3-afD2lZ6bDOn6sFEa84pkjdwZWfpPdQnL2j1GkHbBz8K08JfWl1aD12VGxPMd5Aq_3Jr9jA9X3rUFB4TsGPo0c4oyMauXE8zOLb1WL35dw75Xeh_4Np3u9hwCgQvR86C5eop89gaDv9336RLC9rvGZaD7pH7tDGQwHjbY8k160RN2oqFrUhvXR7tII5JdIApUUQ2xkugsT9IjikLQxbsKn8edclLdrrqCI5L1pha2J3Gk7P1a4FlMpoCCYLrc7lBL5ah_DTt1_KkabCUk4KDBlo2RipsDZ6SKco53ktAX4pXdglHrEGJ38S6bCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=jU3vEQ88Rl9dJVVFBhoDrqxDQpydxBpAItANs2ZFgHFGuBDHPaFYVMH_oiQSS2u2TSnbwbkNnEKYpRbkiUpXKYLCBwCAF398rkZnjIW1dlvdX9uTE4EqaOUDwoVwihqJEGmx8XcQhaOgVhLNf_MWBiUmNtff4F9x2M0j09hfKgjMafFO5YucslkMS2Pkoht1h0YPGC3510qgd3dQUszlc3rNNA-uyIRO24V0R6Yqin3XVIz7Pc8sNCBjdgXCooKZHC6kXrUx9zcCntNf1uf5hleX1ByPgOGWaE4slswmdNd7Uc0s9zH6ls0fqtvWxnQOW8QTuPl0Cn0XFtb5q46ojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=jU3vEQ88Rl9dJVVFBhoDrqxDQpydxBpAItANs2ZFgHFGuBDHPaFYVMH_oiQSS2u2TSnbwbkNnEKYpRbkiUpXKYLCBwCAF398rkZnjIW1dlvdX9uTE4EqaOUDwoVwihqJEGmx8XcQhaOgVhLNf_MWBiUmNtff4F9x2M0j09hfKgjMafFO5YucslkMS2Pkoht1h0YPGC3510qgd3dQUszlc3rNNA-uyIRO24V0R6Yqin3XVIz7Pc8sNCBjdgXCooKZHC6kXrUx9zcCntNf1uf5hleX1ByPgOGWaE4slswmdNd7Uc0s9zH6ls0fqtvWxnQOW8QTuPl0Cn0XFtb5q46ojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mk958IZRPwfdxOOY3CZ93SEUw9hCLeqiG4-zFeAmkfkfsIQFt1mLBf8VXKMQhuI9P51eeNBkFFRT1XHh6kACxyTkRhk2bf0A-LOKIF3xytdgGRegH-yO1ElUfU_ct8buTNqMZ3wId2s4dTBziigBBhoVtjC9Ty7Kka7Z3A8ocUq7_At08EV5UwntKFew2g7rO4s00S9ZPMKnz1HsZ447GtK-4lAFe1FmPGqhivP5l2QgEh3O0R4sjpnua5kQT3Phd5fXt3CyjFbLhLzLJqHl3VDmwybcS6C9yx8s_b81ZRabFbIpjEXmDfmqnvnkoFwvU3kTVdNpw3PSMnigREeQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=GPQUGaObmIzl2760Wz3-4ps_Zt91HEChTxkkBuDJwf3h8oQcBQdPvnPVDKC_htYPb0_dkRFixK_jUQ9NMb5-ovwFoDAbp2f26G2CS2ZpCXezNCTTlDwP5TMEr7q8KcuPc1pXIT1n4JcHBH4BIOrPlwV0B4fO2yzjQcQ8ZvjxShz2jZi0t7_AWWexp5hZu3uTF9W6MObM-pp-8tre_b_DgD-pIpv24CLpzAb4yowoelp0VH3_nq6Wmed-Pio-WfKPDj_UVlMBMbN2DPleCzhCy2NcrIrGN_IhpG6k-rchpok8vXutdjUw8VtrCCEssPvG-MvWAXJJJVm45D4gauFEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=GPQUGaObmIzl2760Wz3-4ps_Zt91HEChTxkkBuDJwf3h8oQcBQdPvnPVDKC_htYPb0_dkRFixK_jUQ9NMb5-ovwFoDAbp2f26G2CS2ZpCXezNCTTlDwP5TMEr7q8KcuPc1pXIT1n4JcHBH4BIOrPlwV0B4fO2yzjQcQ8ZvjxShz2jZi0t7_AWWexp5hZu3uTF9W6MObM-pp-8tre_b_DgD-pIpv24CLpzAb4yowoelp0VH3_nq6Wmed-Pio-WfKPDj_UVlMBMbN2DPleCzhCy2NcrIrGN_IhpG6k-rchpok8vXutdjUw8VtrCCEssPvG-MvWAXJJJVm45D4gauFEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEJsSakApHQn_fCvm3pE1ModjI90eBd_l07yzFJ-4sITWshtOyJJ4VWPj3n-ZcK_JO4qXMS2mXt6bXt_6oLtYmKfGPaPMH-SAowkbKN8e_dWn5or02wr7SlR_Uyp8hvR6AJyXGg8kfnd6zHeStaVtS1JNzr9_bUPnVOmzNfGVNCn2a42iMdgAI8Xk6KmNKWw8WpGmq0MD73cFKXruw_GkTAZVtxVogu-h6MUrZdIG2RDwsC37Eruy8wzKrBAll0kXtyToHJjmV53_Cb2-YNVmC7deRcc4ALe0EmX5kAB0teLLeU5cbppBucS1yCnKzNOvaKGbznTCFJIhOtII4fHFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4sSqw4Li3PgrW9pSF2smJMjcPphOeTjIxmoAbRrbGbbeeX8JwT5TIa7fpGq_OmQ4lgujywDCgElnXozqiKTjCmB2I7ELIGzu9_qE_X-OIBAGJDfZV50Ew8z4vv-jiefLdTvT0xoJTIljzItp7H3BO47CjaCfDdiieM4tzSxhCnuzL_peY-XzJnFgpyD5TgUQcnTsKYbuD2SfbE9KGuGP2ar_iW_NeaIqEO9Gs4eU0Hkz69P5I4M1OsqP7DzIu4ut0xwP8o_BKPPEg0iWekVK-EBbQkV_NpKOvpjOtvlfWlIVZDVJFk2b28jCqW_c54jhhqVnJwHuPEGPbhGAPAijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=gPGO3UnpOLHAteuIWBfodb77oJPjxLcFOOYH8PiAKIhX0qNhQ8Nwkd_1j3a7EdWbpUMpdQNyRGxac9Qdl3oOvVn1eWW4G2z0AS8hMxy5IWEX7RIWEngkoPuOKdXZKK_rxNoq-fFW4lmy7mvZoRm6ybEDe6CzKGpfiqzhAgU9_9qBtdg_B8BpSO94Fb0P5WT1QJZ-qoSlNvaoWaDwxUJtP4jUix1VV7nq0RkMPcisiW-1aYibAT75SWtKCwlJjEzY7zkhX0mgJKRyFEpMd9TpDikO5cDHglUPob25brnSpZI2CMndBJWrWwrZkkUiZZgneYmGliFfwWvgsYn9SYlPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=gPGO3UnpOLHAteuIWBfodb77oJPjxLcFOOYH8PiAKIhX0qNhQ8Nwkd_1j3a7EdWbpUMpdQNyRGxac9Qdl3oOvVn1eWW4G2z0AS8hMxy5IWEX7RIWEngkoPuOKdXZKK_rxNoq-fFW4lmy7mvZoRm6ybEDe6CzKGpfiqzhAgU9_9qBtdg_B8BpSO94Fb0P5WT1QJZ-qoSlNvaoWaDwxUJtP4jUix1VV7nq0RkMPcisiW-1aYibAT75SWtKCwlJjEzY7zkhX0mgJKRyFEpMd9TpDikO5cDHglUPob25brnSpZI2CMndBJWrWwrZkkUiZZgneYmGliFfwWvgsYn9SYlPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Ieut9sTHWkJ6nQtZvoNqWPBlTqRCIaoLMfbdVONptPBB3X9p_zzmEcj3Z2gE7Ifj7NPuGg_VpJqQCnnod2JDEQdCDbryB_JUKorOtwyaPzaK1D7xk-imlkGWALtehRUmk7xE75_9eOCRdZPki6Kasou9DhLg8uYT3a5yXvFvcct39_FtqCemmrxAy2A9pkF7y2vj-onvga074ITYWUD0FD_p4e9ABiJjQwbaCZd1n6IE5iXYf7EHTBsyo7Oszlrs6Dfbt11rkPaIl9MEoL8VrLyYgdKMSRVgS4Qu2lTh4yRGhGZffYJQwwPP8P4oDMMVzg8tuvYyLISQ6h0SjB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=SjdD3pvgKd3WZOhUJ5JBQDntArlpK3u4LVRWs33g4fG0m1edvLh0zFlll2He6Mar0_Ew51rfk2pxVeT110Hcd6V4lgmUPJD-VGhYUT1QzpkWNXQDHj1Mw9BpyYvw9f4bfLVmumPUR89YMLqEKKePcGehdGozuNSM6u96s6fgKHWLSe4o94r6_accvJJeeLFpnxp5RoNb2qjIBqVbT2_5R-sYRcevmCU6efbD1U5NCIz755DsfOOisH2IpQaQibPFZv3bHqo2-n2Ngt2zDg58v4zquQdV80z3htQlX1K5uUXPohMraXxKplOHFtytiZmu1ASmCLDhUM8PRz5X7cLokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=SjdD3pvgKd3WZOhUJ5JBQDntArlpK3u4LVRWs33g4fG0m1edvLh0zFlll2He6Mar0_Ew51rfk2pxVeT110Hcd6V4lgmUPJD-VGhYUT1QzpkWNXQDHj1Mw9BpyYvw9f4bfLVmumPUR89YMLqEKKePcGehdGozuNSM6u96s6fgKHWLSe4o94r6_accvJJeeLFpnxp5RoNb2qjIBqVbT2_5R-sYRcevmCU6efbD1U5NCIz755DsfOOisH2IpQaQibPFZv3bHqo2-n2Ngt2zDg58v4zquQdV80z3htQlX1K5uUXPohMraXxKplOHFtytiZmu1ASmCLDhUM8PRz5X7cLokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=FldTbxpAMZD8V4tXYaOmcq1h3iH4zQbxu3KWtzCApnJUzSRtEvfP3KRrMhTLsg2SHflm_Xgs158V5xPrQs_qTBx4DtPA2tYz15NvqYnG1q022jinuKIvrR9mmLJRQzp6J1lRnvPEATVTZzR-PEUS4pYvezFqzcYimOiK9ZmJtPXVAhqcA8OM0OkZxPZCZRUWhUPsUkhcjE3Tlf2BkvAEpaMXXzFHkCVMlJwHz5G9K-QXP_9xrbO7F_O5VhH9EOECPMoId3z4EvSXqY1dq2-Uw2HWSeji72VLnJOjxg_Obki4GmxNinZgfW3lRO3X6rL3JWKXBFakU1wHjD9Y9iUzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=FldTbxpAMZD8V4tXYaOmcq1h3iH4zQbxu3KWtzCApnJUzSRtEvfP3KRrMhTLsg2SHflm_Xgs158V5xPrQs_qTBx4DtPA2tYz15NvqYnG1q022jinuKIvrR9mmLJRQzp6J1lRnvPEATVTZzR-PEUS4pYvezFqzcYimOiK9ZmJtPXVAhqcA8OM0OkZxPZCZRUWhUPsUkhcjE3Tlf2BkvAEpaMXXzFHkCVMlJwHz5G9K-QXP_9xrbO7F_O5VhH9EOECPMoId3z4EvSXqY1dq2-Uw2HWSeji72VLnJOjxg_Obki4GmxNinZgfW3lRO3X6rL3JWKXBFakU1wHjD9Y9iUzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLk0gEtv2P2jE-ZYkBg6BmY-hkn2yRIf_Cd32qFQ9EVGRWsvl32iVm4wYxWlXH_EXwtdMKyDx-w_KTiOBPI1_C3c63qTPMM49fV8yg82byJT7QvmZU-9fiCd-iqqBX5q1JK08YJRmxU1l5hL_sMXgwxkzCSKv5JuwhWBISOF_dDBO_GeR6V2gIZpWBsfGV5u6ZjxicJrGJkLOLLVbzY3VKh7Q2UF9NnzvRS4CmdA3xktRoNeNEadQQP3gVeaOD1qlWa6cUQAAotfd1UMPE-uJnXlcaaa-hiuK0Y6_uANSllq7EipFRLY4qQ-VHjvc745ZEsoMTqPmRNAbrMepp8iCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyBV7DM-U_5GdW0ZQDP67v-iXZbWGAIwWDn_d_gjUymiSiqe2F22mJRky5KwrzcmeHST83VliRoa4xma5VvIyX2my0hYJu_ROmVai0F4E_56tTw_3MyfcGs8L81_wCGeKyE2gMeTyZJXejC86NZZ5tIytLUVZK_zcKfzZT50nH3VkeOSLJI1KoTiRX5tx0vItH5qIioCINqd__JifCM6U7kRyNYv0GZdlUzyy7cqILAHnREIK33Y-kyU4XNfRMIkPadXXrsqmVBD1wfGyl0CrPGO1x1Kx-9Sd6e1OSlxTihgHYrZ6_X6-BNcP35ezNfIlZgm7lALgTTm0f6ugYP86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=JM7YCYgk-mw4YSPt0mQy29d0sqfROU4A17MbEmId69WGahIG5j0GxyU87rxJucOrQH8Udlvq8rG4iXflxPyg4zb9fySeizrel_OrDLmS-BaCo6XJ6TDpQxbNh4bLFLzEZXQEg6lLnf2rSdTuyfsnIzyRpiPnHdo7lLj-HW4Tzr8-Mf541TaM4C3j73Q6U090XSCl3eONAkDNUEBcF-gFPMNUaKY2Nd9E3vRgtX37Ky0-044r3nvRcQrsPVGVE0RrJ0bW3QWCcSx1Gfry6vQHFxQJNtK8lPBcf3beYRY6WziSSQB5LOegubMsR5YgIdsk-cuHXlzoKqyN3DyHvBu3sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=JM7YCYgk-mw4YSPt0mQy29d0sqfROU4A17MbEmId69WGahIG5j0GxyU87rxJucOrQH8Udlvq8rG4iXflxPyg4zb9fySeizrel_OrDLmS-BaCo6XJ6TDpQxbNh4bLFLzEZXQEg6lLnf2rSdTuyfsnIzyRpiPnHdo7lLj-HW4Tzr8-Mf541TaM4C3j73Q6U090XSCl3eONAkDNUEBcF-gFPMNUaKY2Nd9E3vRgtX37Ky0-044r3nvRcQrsPVGVE0RrJ0bW3QWCcSx1Gfry6vQHFxQJNtK8lPBcf3beYRY6WziSSQB5LOegubMsR5YgIdsk-cuHXlzoKqyN3DyHvBu3sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-DgJ-x-uijSPoKRA8B2mskpmQ3d1LvZUrJ2fs2DAHgKWc02L9EztlzAsfvMgFbHmL9IJkPq426xCLpJrj4iNwpdZ8POyCSEKyBxnsYqC4kX48r--8xCvProcphPYLoKMGcbN7hUVWrhFR_wRh_C14Lu5M7L46xNQ5ObKwKhvRXLMaJWf1wYFdgPabcgqYmCImBk7r-KKzXBjDQEc31iMuxpdAFQeqG3SDqvuigYPHH_UuK_61gitluPoQ73kPdJhMtXBZ9v-4f5W1RdVTOLsx-05_KLmJjcK65PGcvTvW3sD9GaMNBjcSmZB1vLqGpYxC5K7M_2ziE7VvK-pTIcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=CDCeTx4S4gDrQ5nVkWux9TE7lzyF-K4QrvikzE2CrujE_pWCfs2J0mWfPEIHZwXhxaH-AZ2Tt6U_AUOxBjE0npKGepOXKEDIwjXqzpw_dJHs2Cd93F_VhgAiEcGboxAWiHpEcJME5Ke6miZqjiooJFs1_3xmRdQFHZ8P-DDCuHuKFOd91GRIB9UoXh9qO5j7vAyCYqHv-snC1kEt10-5TJL1EyoEupO78IByTOFTNGwlH8LBy4IEzcdNN1xyxLUiZFeBhQelQLEHsQQsidYkIK5kttdS0QOqrctOsrySZkUvOG19kHRANqoeVLuQk4CuNaG2sq24_OYywelUIAlM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=CDCeTx4S4gDrQ5nVkWux9TE7lzyF-K4QrvikzE2CrujE_pWCfs2J0mWfPEIHZwXhxaH-AZ2Tt6U_AUOxBjE0npKGepOXKEDIwjXqzpw_dJHs2Cd93F_VhgAiEcGboxAWiHpEcJME5Ke6miZqjiooJFs1_3xmRdQFHZ8P-DDCuHuKFOd91GRIB9UoXh9qO5j7vAyCYqHv-snC1kEt10-5TJL1EyoEupO78IByTOFTNGwlH8LBy4IEzcdNN1xyxLUiZFeBhQelQLEHsQQsidYkIK5kttdS0QOqrctOsrySZkUvOG19kHRANqoeVLuQk4CuNaG2sq24_OYywelUIAlM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxIpR53Bt9Sl20KACVGYqWt3e4bJhgSRAvWqjWE4n51zxaEwUwNHuW9Rs9Y2AmrT9lkwLWvsIL_J6elKBKDVADslsPhX6-15CC8zznSzSp8yO_yq_yglGUayaQitnZ2hiwvLOHhM6hZMOE1DCm2km4FBWYgkkuB-tZvqAjSUsTe01AGXEwLJAIDj-Pt93h1EAkmlDXfsDugLQRddsOul_1ZnYfBExKPVzlytByKQ9qlUACzhqn4RavkD3GI6ZiKYekQNMym-ieC7pXobLh9eoTXq_5SPjJ8RqpvjlTgcGMFeSf_bxcvY_HBXucruDqM9z-WFOmwqvj7M6ZlyESewjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=YLwIytqDzlpT8QHWVE7FitrePqa1w5zKodzNPgOvHRArWBQYUOcTi-pNMnrZCMrgNqIJ9yH4aSVy7DoRgcv2mwah-Oj8ryrgWJxMy3Ai-Z907qTfgypbFDSfM8mtdkb_pt4mkC1y2jwVR7rIJpYaJOzPzWjagzZSMAS7fB_iEQHaz0gl_S8f5DcBBlayi_MN7XZVEXdFwp2aPFSGuaadAswBUxFquHVu5RUrUiStbgtMmmV_92YrtlZLxuQVQF3ZehkhswSPVtdorPAUcydTUIPk9uexUKCAYMbLn-M60j1viaKNGVxqeAGczFYlHUwTdbia6qH0q0VM0TfxUmC9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=YLwIytqDzlpT8QHWVE7FitrePqa1w5zKodzNPgOvHRArWBQYUOcTi-pNMnrZCMrgNqIJ9yH4aSVy7DoRgcv2mwah-Oj8ryrgWJxMy3Ai-Z907qTfgypbFDSfM8mtdkb_pt4mkC1y2jwVR7rIJpYaJOzPzWjagzZSMAS7fB_iEQHaz0gl_S8f5DcBBlayi_MN7XZVEXdFwp2aPFSGuaadAswBUxFquHVu5RUrUiStbgtMmmV_92YrtlZLxuQVQF3ZehkhswSPVtdorPAUcydTUIPk9uexUKCAYMbLn-M60j1viaKNGVxqeAGczFYlHUwTdbia6qH0q0VM0TfxUmC9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=hK2zzTrH9wDBtWQSz3DPT2eORV3Kuix5N8U6suFT5-d87by6s7717tN6t6pOdGjdi9cRi94KfAEWtZUKQ_tZQovgJZtd7BPJJMQYXO6KXMLibtgFhXeFh6A8D37fDa2ci69swHi0Y3YL-7VkoH1FzeYZNy-BZJslOV24x6Pnorr9CbiEeercNeYsLI9ROnmI1R77rWvSWVyIZ1fztW0f0keIzs_1icd8gohg7il4g8akD8kmHuhzLCiWM2wcCfrPGjXCptcJikr8Kgeg9KeAeeIxL33wfN2uxjvHG6xbNU-mMVOfAQFA5gJwP40ECRxoXqCctJ2VVVpTeXrmsz-2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=hK2zzTrH9wDBtWQSz3DPT2eORV3Kuix5N8U6suFT5-d87by6s7717tN6t6pOdGjdi9cRi94KfAEWtZUKQ_tZQovgJZtd7BPJJMQYXO6KXMLibtgFhXeFh6A8D37fDa2ci69swHi0Y3YL-7VkoH1FzeYZNy-BZJslOV24x6Pnorr9CbiEeercNeYsLI9ROnmI1R77rWvSWVyIZ1fztW0f0keIzs_1icd8gohg7il4g8akD8kmHuhzLCiWM2wcCfrPGjXCptcJikr8Kgeg9KeAeeIxL33wfN2uxjvHG6xbNU-mMVOfAQFA5gJwP40ECRxoXqCctJ2VVVpTeXrmsz-2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi21iqSyVuw8zMRyqKKU73IsBkHnY9bqvBKth55Jlx5ix3YSIexdPFJesf2sPOGZOoRuLdXmMEnXnj1uLRRzHM4PMAcApuCoG1YgwE4apaavEKL4Cc-OC7vhKWxzplRvYAPsTFzUjUnQ5pMO6i9Ir_-coChZCTwX0Tbdfwu5LD7TG5T8NQlLiiu2YuaDAz7Oa1ND6wRj5_2NzjsRPMWjXwioEPro6IYN55A8557JgeWRxIm-Wpv947lGzrx1Bxy3xPZ_vHQpVnb7TJ4FV77_S7eqUGRHdUCxWJhUcCMvxltkVMohRUp-2qH6T0Z1vyrqChESxWrVu_gP6ctSQ68J6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6h5hcZFiWQnsmSPy7NK_HJ8uZ3w6JR1rIBLFKJNy3hV12sBB0bgU4nLvEB2nUZN3JJW1Dp79kaFrEj9XeeVUGnostUgf-kSZhAZfAm5G51mbCobdaKL0Wp9alSl-If3Hw8oTXIJAL2jM5vzycN4cQZTlcirxB83LkGK3rAQ_lcHirHFVDhd73befuXqYBr1Md6chaG_mPcNRp2wSqgh3MYCd1jZQNQSBO7ib1P-CzGiyIQOLecub45LDYHUaCXcS9yPUmE_Prqs4M_Kt_xRu8JO9GQxi0GWfBJmM25c9x8oGT00giOt7dFcI3BXTW3hjqZOzuNL5yI50BCP7DPbQfNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6h5hcZFiWQnsmSPy7NK_HJ8uZ3w6JR1rIBLFKJNy3hV12sBB0bgU4nLvEB2nUZN3JJW1Dp79kaFrEj9XeeVUGnostUgf-kSZhAZfAm5G51mbCobdaKL0Wp9alSl-If3Hw8oTXIJAL2jM5vzycN4cQZTlcirxB83LkGK3rAQ_lcHirHFVDhd73befuXqYBr1Md6chaG_mPcNRp2wSqgh3MYCd1jZQNQSBO7ib1P-CzGiyIQOLecub45LDYHUaCXcS9yPUmE_Prqs4M_Kt_xRu8JO9GQxi0GWfBJmM25c9x8oGT00giOt7dFcI3BXTW3hjqZOzuNL5yI50BCP7DPbQfNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYxaKqQE8O6NLtwikUjXyT1c71VSarXiX2pFcrHKib-25yZxaw0xJghHjdZvn08foKOyvaQ4t-Jh5g0eIP3N_xgjZ1LKVYz-XWbglu4185LDmm0LsqlM-vn8x2NQ_zpfeGuFCq0NC9rHJOZQRWXng3HwrK4fIDmjwmskiiZX9NCkmlq4jCioCDpu0ODe2y0UuhRsAXtZx2E_vipH_r66_dZcSqsLkPk4ZD2Cf4lCDF8PZpy8ogVCVyxtCbYCqdERbCcXdsySfw6FXTXO5wMdR58PMTao8oxp3N2TukrDvHyRmSZ3kF3Ia3Z0Sv_hBjYkmuW72CidXBDNf0nMDiyMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qd4m_5mZruVy-WBX4-Wh-Ipl1caDC2XnL6pUdkp-pUACFegIdGugeMR_oZbTTygYjkBoh5_ZjrIjxLKJQzG_KSArZtBiq7Q1gcjFjJ7hK-SL5GUUOKNyh5HvDou-gtn1BXj9M6s9X4pNOSP4Z0G4cUMs5J0GmR3vlVpS0x0FO3Du-cxx8IqPmHTPXF9Khi26At-kDMq7EkOeDzkid4U84cq-1gi8H0GPPIYPEX4PWAb-3IurqsrmFA3i7D0suTNkWqaYejl0vvmgAiLmFwf34SkzcnAG_CRZgvvzyWEJVRfxs4ET_lGVXjt8_hWDKqxA8R5NsR6oaz_jQ11eMJUbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=kthA0-h_i0TYdY0vDQZi-9qC0qKdELJrLXrogtYu_8LNMq8H72H4khMsSE8wHVRdQMsk7nXwId2hEBzC-aTdikbFHs76t7Sg9JUiHZMGflDSHKpRoYqFQ3xzORX-Hcg6yV7ypUou_vQ5GnWjypgEIjq12L1QzHY9A5zI1c-Hy_iGgi47yWKoPgymS17SSvYQvisayTLG6HSzgxpB62mHN-6pToQ6LHBxu9IRL82LFkDi5qPOzkz5dD-4qEANyBPX822rozhF8HI1cRo0wpyg-D9YEkZ2xLmtwQKBqtYQpbIR9NP2gwFXXvCBQgkAr71tu7Y43n3w5NjQv-Njp1VsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=kthA0-h_i0TYdY0vDQZi-9qC0qKdELJrLXrogtYu_8LNMq8H72H4khMsSE8wHVRdQMsk7nXwId2hEBzC-aTdikbFHs76t7Sg9JUiHZMGflDSHKpRoYqFQ3xzORX-Hcg6yV7ypUou_vQ5GnWjypgEIjq12L1QzHY9A5zI1c-Hy_iGgi47yWKoPgymS17SSvYQvisayTLG6HSzgxpB62mHN-6pToQ6LHBxu9IRL82LFkDi5qPOzkz5dD-4qEANyBPX822rozhF8HI1cRo0wpyg-D9YEkZ2xLmtwQKBqtYQpbIR9NP2gwFXXvCBQgkAr71tu7Y43n3w5NjQv-Njp1VsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MnMCBruDkaS5tJmM1rf3RpBfsEE1XDSMhsydqCzQrraPfY_5K08iOismLQRW0uqUcMHH4fKSBpAB-sW6-QqF9kBDtGOUKz6y2qXZArEZKDNbcmAJWFJKm4cSe-7Y2bkh9Mrw--lT4yB8CKjT13m5eqoWB8d389lIA4p5tkE5tTSdfNY_GhfJ2SYW9HnFQV9BquHhUrkqFa_3THo930YduuaAle2flQ8MMTYxd8Pn4OL1tIBTgEsGobW_oy2K8OUVok42XKW5C26XSGNQpmIKMGH6ohpYcRSVCFhrQw0TGB46FYBTAheCCbOqGyety3bFKYZ5dxOernVFM6e2Wh5HMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MnMCBruDkaS5tJmM1rf3RpBfsEE1XDSMhsydqCzQrraPfY_5K08iOismLQRW0uqUcMHH4fKSBpAB-sW6-QqF9kBDtGOUKz6y2qXZArEZKDNbcmAJWFJKm4cSe-7Y2bkh9Mrw--lT4yB8CKjT13m5eqoWB8d389lIA4p5tkE5tTSdfNY_GhfJ2SYW9HnFQV9BquHhUrkqFa_3THo930YduuaAle2flQ8MMTYxd8Pn4OL1tIBTgEsGobW_oy2K8OUVok42XKW5C26XSGNQpmIKMGH6ohpYcRSVCFhrQw0TGB46FYBTAheCCbOqGyety3bFKYZ5dxOernVFM6e2Wh5HMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=LE3q89N8oMCw0SDUJg7rBrPhfEdBnXkQI_U4J0AeU_v7MAsdhsEON236CYXKzdMW3kvi71_rylBDsNp96qnQ7lG2go2ABnwzUYyb1m60q-mFg00BziPFzi7RbcQE6Bwu-JAEGZGo1vzuwpuiXWOAPbOfE8gS2ct4Xp4tUbhGlCgJ4EKp57Iwb3bvDzsgdTiDLo6KRgHI8lMYSiLwzfkLM58P3MZBnbsJr6hq5-kYNQfVyI7qsUb0cQQSQ4EbYG5yMtmzTgdWJRNGbnKpHvaq6f-yJ1-kTibb0d0uKrcTx9oEHBt74ROJFYQUHY5bEIk623zFQfaudIc8nKc1CSOz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=LE3q89N8oMCw0SDUJg7rBrPhfEdBnXkQI_U4J0AeU_v7MAsdhsEON236CYXKzdMW3kvi71_rylBDsNp96qnQ7lG2go2ABnwzUYyb1m60q-mFg00BziPFzi7RbcQE6Bwu-JAEGZGo1vzuwpuiXWOAPbOfE8gS2ct4Xp4tUbhGlCgJ4EKp57Iwb3bvDzsgdTiDLo6KRgHI8lMYSiLwzfkLM58P3MZBnbsJr6hq5-kYNQfVyI7qsUb0cQQSQ4EbYG5yMtmzTgdWJRNGbnKpHvaq6f-yJ1-kTibb0d0uKrcTx9oEHBt74ROJFYQUHY5bEIk623zFQfaudIc8nKc1CSOz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=SdnB-T0hSwIhO8A_XtprMNK-yIEnD2P2l3jA4OECP3qoCwM30KO0VxbDC0FRH-OoN2Cxv7Nx41rpNHQ5UipWd1KYWT7h6WmCN-KNxBkdc7tjFm0dr7idfHVvvzHA0B4vjYrohEP5dCHOY3EPgYTtYo2JSCXY909VdcrXU2q9Q1kqWtoIddRwmFC_56SW71hULASMIxk8xncIPR_ncxdSSJwKjSFRSHeDvy210AHYyVetlY_EC3WwsjXdExC9rO2FL3r8NgbLWe54DxT-YrUGjSsDtqov23Q_FulQ7XQywQaPaHhIL-ALGwbL1EM3EC1y67uzSK4qexKaM9LByDRjqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=SdnB-T0hSwIhO8A_XtprMNK-yIEnD2P2l3jA4OECP3qoCwM30KO0VxbDC0FRH-OoN2Cxv7Nx41rpNHQ5UipWd1KYWT7h6WmCN-KNxBkdc7tjFm0dr7idfHVvvzHA0B4vjYrohEP5dCHOY3EPgYTtYo2JSCXY909VdcrXU2q9Q1kqWtoIddRwmFC_56SW71hULASMIxk8xncIPR_ncxdSSJwKjSFRSHeDvy210AHYyVetlY_EC3WwsjXdExC9rO2FL3r8NgbLWe54DxT-YrUGjSsDtqov23Q_FulQ7XQywQaPaHhIL-ALGwbL1EM3EC1y67uzSK4qexKaM9LByDRjqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE4aE5Qtp_L4Do_lttlaB_0kvJMKTFg8njBzqpYjuMIsYbNxFUBSqMFBQp3MRNUoZEvjwx_mPaow88jpDX-hSTPmlZmqN1IX1kR_3hxcxk3F5BsMeGyOyR33u3bqgCKRpybYyXKysX19KVZmZDCUGVSXavBdu52RoNOrjKEIW5GhACXhUdBjhbSYt_g5Y16yaak5c2y1dqLE2n2Qcr_PZxCJtybyITfm1YO9XSl0qYWz4_houBNhCQ4kbrOtH0lFomYbtAJw3OMeQNWYDLJHaWeycgx51ac_tNDYx00vIN-D-oSo7pUqko0qBDgo4lO0GDZcvYGyL8o9Awm_jPfdHq10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE4aE5Qtp_L4Do_lttlaB_0kvJMKTFg8njBzqpYjuMIsYbNxFUBSqMFBQp3MRNUoZEvjwx_mPaow88jpDX-hSTPmlZmqN1IX1kR_3hxcxk3F5BsMeGyOyR33u3bqgCKRpybYyXKysX19KVZmZDCUGVSXavBdu52RoNOrjKEIW5GhACXhUdBjhbSYt_g5Y16yaak5c2y1dqLE2n2Qcr_PZxCJtybyITfm1YO9XSl0qYWz4_houBNhCQ4kbrOtH0lFomYbtAJw3OMeQNWYDLJHaWeycgx51ac_tNDYx00vIN-D-oSo7pUqko0qBDgo4lO0GDZcvYGyL8o9Awm_jPfdHq10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=Ggo6QiIEoGnaMuYD9kTQtkefva-mpIT0avZzN70fO56ApKJlMrglgJBfgYXbcqpFcUJvrqfGW_85IJ5d4ycy6OlsQfFoaW1PLKVtlZF4AwZPVBXILLZUIYo1Va7hnsEmreSctyCRb-V-o6hVTTCDtWfFnlDYfWodUxEJ2D29LjPRRm0hnGFReB1e-xGsomjVE6yYt1wudgGQPCnv943-RsXEmGraZzk2ZSIEi_Sk8htZNzg20eSHCjKn65Nf4Yvhib-cC6aOpRKOfSsCOM_MCqtQzXk491ylEvxW0xwDXmwzTpZq2cybFAcOO5PoBnPKyCNTVoY9_TGl_T57M5RbsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=Ggo6QiIEoGnaMuYD9kTQtkefva-mpIT0avZzN70fO56ApKJlMrglgJBfgYXbcqpFcUJvrqfGW_85IJ5d4ycy6OlsQfFoaW1PLKVtlZF4AwZPVBXILLZUIYo1Va7hnsEmreSctyCRb-V-o6hVTTCDtWfFnlDYfWodUxEJ2D29LjPRRm0hnGFReB1e-xGsomjVE6yYt1wudgGQPCnv943-RsXEmGraZzk2ZSIEi_Sk8htZNzg20eSHCjKn65Nf4Yvhib-cC6aOpRKOfSsCOM_MCqtQzXk491ylEvxW0xwDXmwzTpZq2cybFAcOO5PoBnPKyCNTVoY9_TGl_T57M5RbsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=iboiWLBS-kFyjCWdZzh4LYCfT2biEwG3m1onJtmiujJ5_2THlYvYNO3QnVk0laoWtZK8u8jlyt22mZTvSjzWUVOEiR_GN87iAcRSVKpiBhEKswbCeLJwaFhs-NMKt6NuibIP1PO-XNVHGFO3e-WCAE9pS3VOccAWiDBcGryDDI7Ot2lCRXZlVuhw9BxdFFFcHmrlpbPV3L0D90u-eebEuo8GdyWZHFEg93mqNPUiYE2Ntb7zDpo9l9DMxiyEKKtHfuQtLYFaI6IbJN-R-GwGnlFuEnKDdGq2aetGKKTYdMdV9u2a70Gd90BZ53ORlaYsUtFhwrlivTo6DOCOR1k_7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=iboiWLBS-kFyjCWdZzh4LYCfT2biEwG3m1onJtmiujJ5_2THlYvYNO3QnVk0laoWtZK8u8jlyt22mZTvSjzWUVOEiR_GN87iAcRSVKpiBhEKswbCeLJwaFhs-NMKt6NuibIP1PO-XNVHGFO3e-WCAE9pS3VOccAWiDBcGryDDI7Ot2lCRXZlVuhw9BxdFFFcHmrlpbPV3L0D90u-eebEuo8GdyWZHFEg93mqNPUiYE2Ntb7zDpo9l9DMxiyEKKtHfuQtLYFaI6IbJN-R-GwGnlFuEnKDdGq2aetGKKTYdMdV9u2a70Gd90BZ53ORlaYsUtFhwrlivTo6DOCOR1k_7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqXwOzouMCxO-BMFNvT2AGcK6T-HHeNMjZLEikMWk6o29nPZ5zWaCjSbMKKNzd-TEpP4bCB7NRcQ1ThOo_0dg3v8n0st2RXzG6Y06GKrzEmcwaJUt4sS8ifQAkbv8Ga_8BHrYYcpFiTeif18LkEN6JfLlpI9t5g-Y_UqJWp23F9Wyhmjev3VPyDHE4wo5m3JXHRPHpA0rKM5KLsBMazy5Me6deRXcX7xscj84Ro7C2loUmjzQwc5KGjPfS1ocBYWXWOENfAxi9gUlMvDujZvs9Qr_mBbMp_KGj-BE2Z6b_pq3umgSn4CUiS372O5QivbUfbbmtJmDU3m-ZTAX-pDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoQa3rOoBpxFEiZqOGBM1OyrwTtOdG4-i9goF9PyxxTPHlxQdw1M8oUc4H5zDU-BSJ8h9Ll-lQOOTmGQM2sgp1Im7B-ZbW25OsmJ2b7qUVwTBxhEKB6-GQclwBMJM1KckCnRdShYmv52NsOoSMPJRzqV0MyBn6IcbThVHez_4GJoGamKJyP5yOuR6HkVgDtuP2hq5N3P9gs_PCIE3Y2xrgxvyjDdLzX-a0Mh0r66bQTxgH2MXrEslrtxFX8P_4l1WbmXIxytcbwLNqqb5imm62LeOpoPMl7OBTxstRguhe3eqa5R7k5n_3UN_0ywh5QWB5NO2E1LYI5TZtkcMlUJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=IWvw-zKc7bjIwDzPYDowPmGh91LzFgYP2HSd5W--Is4Owh-RZieeLcyhx1E9QNFZMi8X9YuLiJ2TArknjG1RZOtUBSIQ_vZJ9bcwQSNqPMUUAz4-WR7KMwcs8Xhs_Gnh6s5yRQC1jYXD0BYl0e71rbDvGMmbh7X7nuxtGrcEBJHgyYd_O5oWAJwxiPoFN-sOaDK_em3ecbanCZu0HPRoCvgxjz69vyN03oGgw9vkOpcgZL2hS8ZjN_TCK8meltYKD6k1Dfsyyrikk0H_QBUjOdhnDpF656YiF3gIPmCJi9FHlVB6htHI_XsawIe8oo2aHdaBtOss5gsRkcIz4RJBGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=IWvw-zKc7bjIwDzPYDowPmGh91LzFgYP2HSd5W--Is4Owh-RZieeLcyhx1E9QNFZMi8X9YuLiJ2TArknjG1RZOtUBSIQ_vZJ9bcwQSNqPMUUAz4-WR7KMwcs8Xhs_Gnh6s5yRQC1jYXD0BYl0e71rbDvGMmbh7X7nuxtGrcEBJHgyYd_O5oWAJwxiPoFN-sOaDK_em3ecbanCZu0HPRoCvgxjz69vyN03oGgw9vkOpcgZL2hS8ZjN_TCK8meltYKD6k1Dfsyyrikk0H_QBUjOdhnDpF656YiF3gIPmCJi9FHlVB6htHI_XsawIe8oo2aHdaBtOss5gsRkcIz4RJBGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=IlkbEU4PyEVj_BHCG-SjFlzwAhUcTxSIHIJR8rKFY7bucYTusotUXlMSBtoXeYPK8cYvt9NbJLfRKYd-KcvqxrKh39yAfBwrYoy_V8Uqzm9HJ47nlqKyACSPcqdnmFyFWjFHLxaOnDK0lxgVlqTPSkih-V8UaVDXSUnnxxzijdy0XgYM4TidKWsj9WNEd6QE0I_SqVCP9vOz4fhNbeqmqTGE04OyJXAgvxatMLicH-mDq4X-eiYFvJ0nE6ZGS4MuYCZQrz2DJLidas3J_tDTbrVPCnVnIxSBdjZyhpQ1e-4vb6iWj7cFFgqewIxUmaNAXK0ne5oMvVCdAJiNYzGI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=IlkbEU4PyEVj_BHCG-SjFlzwAhUcTxSIHIJR8rKFY7bucYTusotUXlMSBtoXeYPK8cYvt9NbJLfRKYd-KcvqxrKh39yAfBwrYoy_V8Uqzm9HJ47nlqKyACSPcqdnmFyFWjFHLxaOnDK0lxgVlqTPSkih-V8UaVDXSUnnxxzijdy0XgYM4TidKWsj9WNEd6QE0I_SqVCP9vOz4fhNbeqmqTGE04OyJXAgvxatMLicH-mDq4X-eiYFvJ0nE6ZGS4MuYCZQrz2DJLidas3J_tDTbrVPCnVnIxSBdjZyhpQ1e-4vb6iWj7cFFgqewIxUmaNAXK0ne5oMvVCdAJiNYzGI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=RYVf-NZ_KqiQbql-gaP_rOtDgdavxb5Rb30T1iZ7NWl8zHjUbrlv326NUgafFnhKfourR-7vVvLFLO5oTCJMVB5zJiSEY5JygYpzn8SvRz4crN3rXodHjCkNJJVW5gEGAUsnKoysw0HbieWIPhHR2P6Vx7OcY0hEYzSKgYqlPucOiZcXCmnUvlLlmad48cvw9ENAsAmPdPm5OLnK4GzXfPRnkbx9S-4ukwcqhCZhASGHysJ_YXeEneuCaO_uS-SZ7z059bM9F9LNffBqk_oU0vlE3fWSrkJeSVPzhyYrOQiomiqTS6-HclanOcE7yEeuBUVLap0b16mbR72qYRPIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=RYVf-NZ_KqiQbql-gaP_rOtDgdavxb5Rb30T1iZ7NWl8zHjUbrlv326NUgafFnhKfourR-7vVvLFLO5oTCJMVB5zJiSEY5JygYpzn8SvRz4crN3rXodHjCkNJJVW5gEGAUsnKoysw0HbieWIPhHR2P6Vx7OcY0hEYzSKgYqlPucOiZcXCmnUvlLlmad48cvw9ENAsAmPdPm5OLnK4GzXfPRnkbx9S-4ukwcqhCZhASGHysJ_YXeEneuCaO_uS-SZ7z059bM9F9LNffBqk_oU0vlE3fWSrkJeSVPzhyYrOQiomiqTS6-HclanOcE7yEeuBUVLap0b16mbR72qYRPIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=IwAICED87zVtzlGW-mONVZz_JmVXN8xIIOkyfFtJ3oX97OKNO6bTeLDu_HjU7PyNbyhmPhiGxbK2Ef-bBIkKA72VmSKF4J0tIhonFhC5XQ683oFYlylLysWGydr6VY4VvQ0A0k6cybGf0ctGrftJh9CtmNwD7vFLOBtcuLmLJdAXQXVRp2kRP1Eoych3hwxF0y4YWbUu8J8KmnLKuqEZegrM6CD6cNNiEE-zhbuXUZKwg_Jh3TvJHcC2PaqjM3oIOp8w3htZA4hBD1MbUd06KYYAfWOwfqNCB_FgzosqAaS_WhtLKgLooVyXGUx4bihoh47Sud4KqnACeJ17e0St7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=IwAICED87zVtzlGW-mONVZz_JmVXN8xIIOkyfFtJ3oX97OKNO6bTeLDu_HjU7PyNbyhmPhiGxbK2Ef-bBIkKA72VmSKF4J0tIhonFhC5XQ683oFYlylLysWGydr6VY4VvQ0A0k6cybGf0ctGrftJh9CtmNwD7vFLOBtcuLmLJdAXQXVRp2kRP1Eoych3hwxF0y4YWbUu8J8KmnLKuqEZegrM6CD6cNNiEE-zhbuXUZKwg_Jh3TvJHcC2PaqjM3oIOp8w3htZA4hBD1MbUd06KYYAfWOwfqNCB_FgzosqAaS_WhtLKgLooVyXGUx4bihoh47Sud4KqnACeJ17e0St7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=gf3UDtnXmqPM23q24_b0Fjj59G3Z8KgyH-Mgpt2g-nBcvyD9VVvhfnPaQTFM43xOrFqdMgE0f9UcsXEDnyMUG374K8pGLMzP40qLYPog-1XHjyKkI9OIw5-EswyQIujGjMrjQTMfpL4izg3z0o9hHvQ2wWepd6OfO0MsYFnXrRwmmYmN86a_UaVEwE4vGZz3egJs0TM-EPjYo7wCLriR_Ks5hkRmHqTqBTcRxvypmcvU4yZwHa-i3l1xLnZ7wuC_JojJVsPNN1u2E6C0GzjwoHkZ9ji59nIxsH4X65Z8VBTLXlIbRgCdawOHhhjNBo_ItSvKFsYYCsxlJUZ_J8KKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=gf3UDtnXmqPM23q24_b0Fjj59G3Z8KgyH-Mgpt2g-nBcvyD9VVvhfnPaQTFM43xOrFqdMgE0f9UcsXEDnyMUG374K8pGLMzP40qLYPog-1XHjyKkI9OIw5-EswyQIujGjMrjQTMfpL4izg3z0o9hHvQ2wWepd6OfO0MsYFnXrRwmmYmN86a_UaVEwE4vGZz3egJs0TM-EPjYo7wCLriR_Ks5hkRmHqTqBTcRxvypmcvU4yZwHa-i3l1xLnZ7wuC_JojJVsPNN1u2E6C0GzjwoHkZ9ji59nIxsH4X65Z8VBTLXlIbRgCdawOHhhjNBo_ItSvKFsYYCsxlJUZ_J8KKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQB76SC7bunG6UlfFoDxtWDdBUXHdkK9N3SZItjdxqaeQQ0bfCyvcIS7g9YY9vx-JobR1I9XJJHJW-35ArcMzT0RUiEtRVUOAUiCt94Gqsb24pk2bkan5AhjT5VtBhbG_gxRy_CI3CzxdJRDywXivUrsLBBZmTLJnxW3G-Mo9NOx5GCuX_b86gowxQgixN6cER-_Rmc1GRmEsw8hCCivOb-0TK6GJs8UosrbDeH4GzXFahT3PWTdE9N4S0gCuVCfrBVFK0tJfFTxoIWkrko1l8cRTj3Oax5EPmcM-4tRDOKanqbDPxDHbOOcQVA-8C1l_JbW-GesEoZTp2KVGYRSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=WbCQsCdn2b027TzrkLkjfVjQ4nZWvlxIHNhZpYLCQzfpEuzfcYqIj_Ho1DG4RjhU1zbMKPIxRX9UpNX2uD2DIzh3EENmD1yQ2vQ5JSDjTMwfatPvuX4M2bAAHmytQjtDxP3cD-C_wxDkYMxX1StHrmgq7jNPgNO2C7RZKPyJOwAz7IWKKvt2seP0DJKYOx3Ey4vztVYnzDGiaAnqds126MfbvZ-AoUHDeK6N9A1IxPjeE976DSnq1VMOMaT2dFZT0wbOBdLvnDgCA2locUmyeRM1KHo6yH0sLbep1WgcMd63Xx7TXSrEMtgc6k33TYSfHJgwswKAAevykmn64nClPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=WbCQsCdn2b027TzrkLkjfVjQ4nZWvlxIHNhZpYLCQzfpEuzfcYqIj_Ho1DG4RjhU1zbMKPIxRX9UpNX2uD2DIzh3EENmD1yQ2vQ5JSDjTMwfatPvuX4M2bAAHmytQjtDxP3cD-C_wxDkYMxX1StHrmgq7jNPgNO2C7RZKPyJOwAz7IWKKvt2seP0DJKYOx3Ey4vztVYnzDGiaAnqds126MfbvZ-AoUHDeK6N9A1IxPjeE976DSnq1VMOMaT2dFZT0wbOBdLvnDgCA2locUmyeRM1KHo6yH0sLbep1WgcMd63Xx7TXSrEMtgc6k33TYSfHJgwswKAAevykmn64nClPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hkipcefNHPc7bWeQEt4TN-EBYQbZKubquhirh96cP-5NW1X6YAGSuIXC9Uwr5egDSduxenvTMqwg-AiOdLEnmKgsxcTQZyizsGOdtDIdzhbvl_KvfcqcaOT_VBwgUMLY1EYx1f4althhE8JLUWzD6EC4KzPDDl56i2DR0PFtYz3OGgjrUVG3e9xGukIIGNwAWD789YERSvt8vkuI5PuL3t5cfsxWIdxYRI6h73T6vrabv_E3vWLUTZ7kL_zoOTTvVtDaJ5OIUXujRIdlB0MtfB_tf-tiND1wQ1FC_gj-kZHIy23JYYHhFHyYGL0jEFDo-CSJ8Mu4H63aJrpuS1Hqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hkipcefNHPc7bWeQEt4TN-EBYQbZKubquhirh96cP-5NW1X6YAGSuIXC9Uwr5egDSduxenvTMqwg-AiOdLEnmKgsxcTQZyizsGOdtDIdzhbvl_KvfcqcaOT_VBwgUMLY1EYx1f4althhE8JLUWzD6EC4KzPDDl56i2DR0PFtYz3OGgjrUVG3e9xGukIIGNwAWD789YERSvt8vkuI5PuL3t5cfsxWIdxYRI6h73T6vrabv_E3vWLUTZ7kL_zoOTTvVtDaJ5OIUXujRIdlB0MtfB_tf-tiND1wQ1FC_gj-kZHIy23JYYHhFHyYGL0jEFDo-CSJ8Mu4H63aJrpuS1Hqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8up8e8bOGc4WxHPVtUiOoSGBs4A-9pGtUQhsrsZTUdwj1MZsaDuhcsS9d9XmtXPadx_C1wOB-0VNvIqub7mtaRZ23v1UXTPPFEgMhoG4c0jtS37Gxuxizb91LiAc2njCHWCDO6mJx76wuzg4Ql2Nu45cRnbKtr8ihqNllR_mGXSmK79V0ngS2cmXhAAS8-20TRGs97V5Dbk43EKdaOKlQtBMqZ1uwJJEdYail8xVUWIQo3Y1Sl1OAHwb7jeXuVD-u96CZ7cb0Nh3mMLXxgc1uscv5Y59gtYmQq7xh5YSu1WeeowvXw8RFXlglzNId_w1BDTDmmfwcC_7e2SWNCobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=hBqX_xpTD4LzDalUm_u7pYiRJR87zvmN7-p-FgtUtkzcxBsCrA6_QPaFYdm7X65fT8G4aXFnBPP6OrFS7UVbxkxdxS78n1Rxyaawy8nq74S9MdkXjgklMNVwYUPw471eDOdvbxENNYBSLWu63xHRL1Qm0936OL1KBFYM9qsXteniaoXy4gN0P5JtBGWlDmfp9sGSa7dl0mnKZdEz8SsP69TeN4WTgvh3HlovFpYb-ZiP_gU5gvLTtYEfsQVSPACEGXn72-dDby_rd-PLSsVzUwZNUI6E9Ft2nW3AEmTrLl_KaDYAVbbfMvpbz9_XAwqgEKH5GOPEAoIcZyV1KhG9MCSAbYIKcDtJNXYGcv4EXqhRIafF6lF6KmB21imzZXPHsY1K9fFMSL96WW0gf_eBe5H8aySKWhRSuoOiIknwem_fP5o-8eFQ81Fxr4YmByD7By7kOb13FbDTEOXyG19efqGvbvktizefbqAU-B831EqiTKnvbj71nXg7gQa6zkqszJJFPNFTXPAd-AMhBK47Tvn0Agc31Dxd607SORptxvLYmHHAkWYRHcuqbxuC6xejAkmWmHQOr262VDweNIhhAnhSgjagP41b70N05FQEV68kqlEt47JS9GfPEUPOF4wNd7embcPLXyenrQEr5_KzTmw9mxEPByCjfGInC7BrIqM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=hBqX_xpTD4LzDalUm_u7pYiRJR87zvmN7-p-FgtUtkzcxBsCrA6_QPaFYdm7X65fT8G4aXFnBPP6OrFS7UVbxkxdxS78n1Rxyaawy8nq74S9MdkXjgklMNVwYUPw471eDOdvbxENNYBSLWu63xHRL1Qm0936OL1KBFYM9qsXteniaoXy4gN0P5JtBGWlDmfp9sGSa7dl0mnKZdEz8SsP69TeN4WTgvh3HlovFpYb-ZiP_gU5gvLTtYEfsQVSPACEGXn72-dDby_rd-PLSsVzUwZNUI6E9Ft2nW3AEmTrLl_KaDYAVbbfMvpbz9_XAwqgEKH5GOPEAoIcZyV1KhG9MCSAbYIKcDtJNXYGcv4EXqhRIafF6lF6KmB21imzZXPHsY1K9fFMSL96WW0gf_eBe5H8aySKWhRSuoOiIknwem_fP5o-8eFQ81Fxr4YmByD7By7kOb13FbDTEOXyG19efqGvbvktizefbqAU-B831EqiTKnvbj71nXg7gQa6zkqszJJFPNFTXPAd-AMhBK47Tvn0Agc31Dxd607SORptxvLYmHHAkWYRHcuqbxuC6xejAkmWmHQOr262VDweNIhhAnhSgjagP41b70N05FQEV68kqlEt47JS9GfPEUPOF4wNd7embcPLXyenrQEr5_KzTmw9mxEPByCjfGInC7BrIqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=aVAJUqja_G0mtaGeswm78mL0DuiYx2HP8O1UmEflWYaHNo1WCO8v1aDNQYLdbnZ4PA7vJsNo4NvOtgReoJI5kvaqHcW58UJi8voQS5efn-Ssl242Si7nLiMER9TwFzKYLvsifuUc0lr_5B6zbuOdo1rFngrs3nJtjs7ssdNrl0n7PseskHlgcM9DQC0uhdM0CCmP412fowyVABnWbArwJqLE7FhJw4udmKzBuKjlbHRzGnr1Cg2ogf1_ukO8QrImdK4s12gIHy2WC1NsABh_vp0SE3K_Ty3cjoOmVUlsGQEfGq7k-2piiJtiMuZjcRBR1TVgITDN8wQee6meNb0vDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=aVAJUqja_G0mtaGeswm78mL0DuiYx2HP8O1UmEflWYaHNo1WCO8v1aDNQYLdbnZ4PA7vJsNo4NvOtgReoJI5kvaqHcW58UJi8voQS5efn-Ssl242Si7nLiMER9TwFzKYLvsifuUc0lr_5B6zbuOdo1rFngrs3nJtjs7ssdNrl0n7PseskHlgcM9DQC0uhdM0CCmP412fowyVABnWbArwJqLE7FhJw4udmKzBuKjlbHRzGnr1Cg2ogf1_ukO8QrImdK4s12gIHy2WC1NsABh_vp0SE3K_Ty3cjoOmVUlsGQEfGq7k-2piiJtiMuZjcRBR1TVgITDN8wQee6meNb0vDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WverLp_X8IGBigLCTWTseLVo-rA-VJNNQ9c37fRAlRcTSYP1Hm2ky32cPf6JPQUQHheF1bISu84tE2hznKohdBcDETfFmtwZKZAO5p4a2bfQuQDGwM1Xk9armD7TXqwZ23iaslC2BHfrWADhX_2cKUzUYW4ofcbSyV1uHzdyfITV3tgMXXFwJr3-VEvdPNOVQVeRyMC6xbpuWcYR0G_nXNsw-lvfFfp1TgYVCR1fPQsydAYvQxuGpIUzFl3jK_5Hj9SH55mT6bSdEyoT81Yv-EMxpZgoBBw6I4sLau26EwZYKpb00tE5ZRrIf7hP6UuqlmEIQWG8V5RF3WQAWB0Liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFYjGcta3qFFhoO44k7o83sLgbKHhwnVYsxCCQkmAeMjMuBRh_sMLcAgB7aCuZW_8MFYoo2mWPsRHknsviKb2zcOKXcywtn9I1OU26FMJDHlqgxe-kGJKqEMEBQ0cC_jqfryHxL5mMGDcXjY7eqs1ZuO2ZvuaYiowuPv5dgh9ysmPNZSJS7ZkVaqmvAxkG8AzjPLgWFcjh7NQQUzWlZuIblI7yVYpCm8FZ-N_877eTNGvYtG72IFNVNoNsss3aphW5COFNS9gTgfsTnSMdv1sDWyFQsxNy1nnssq74O4S2yGgPbxvdGVt7cq_J9x22Qy8_l_Luv2M5j83rEEIuME1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=EBiPP6xd8pzHRABE2OdGguGRfmpBQsGpNPjpEdj2JN-jnnEGg136MEaHiAGjwR4ifO53c67DdfZcmBYUl8vnd_AC3KFtvmQMN4xhV0UlNXRxPWuLE8VIbvlEc7wCruW0D_zqkxea9-A7Y6dHu9dUho7ldHNw38Kca4Vrhgsv8Dr0deFSTOWCYlBHfPlynOxfNvmN-c6HJTAKDowde8gARrjjtITQauq1lOBRfRlzJeews9xrnePReT3r2w00NAS-AQTbR1TjyiWdyOgm0tEMH3mUdBbd77b2loUOgEndSBRKoMVat56nFdjRL4N6N_jjENHCRls4YINQz0Uk4NM5yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=EBiPP6xd8pzHRABE2OdGguGRfmpBQsGpNPjpEdj2JN-jnnEGg136MEaHiAGjwR4ifO53c67DdfZcmBYUl8vnd_AC3KFtvmQMN4xhV0UlNXRxPWuLE8VIbvlEc7wCruW0D_zqkxea9-A7Y6dHu9dUho7ldHNw38Kca4Vrhgsv8Dr0deFSTOWCYlBHfPlynOxfNvmN-c6HJTAKDowde8gARrjjtITQauq1lOBRfRlzJeews9xrnePReT3r2w00NAS-AQTbR1TjyiWdyOgm0tEMH3mUdBbd77b2loUOgEndSBRKoMVat56nFdjRL4N6N_jjENHCRls4YINQz0Uk4NM5yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=kdSFH9UvN2ygswQexD4RTwbL0-IPczdfkPS0LWu7UMJmdzXdD7P03TaGvrI_QFewjDqxDCwH4NU7_YJKvJ7_ajnQwqYQ6x5TynU5zy3rpffYOGFGYgwRUlHQCouINTBAo_2ROP79gCPszBkwdaYGZ1J6Wx_1nbnJuGqEnI5LtSakW5gTNpy8PrP_yODiCSMoMpUayKjzEmV66WsT2u0Z7_2uXKkZhLG9oQxNhrYFdlBe_DKNdGU4-rIQC9Qyf-MfLNvOyb4Q6VvlEi2NnZvbRbtD6dGtzbzX8oyi36gv_z0SP7LNLmAEXmkshzVnBa2jMcvmyxqCfnxMe_DTfwf3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=kdSFH9UvN2ygswQexD4RTwbL0-IPczdfkPS0LWu7UMJmdzXdD7P03TaGvrI_QFewjDqxDCwH4NU7_YJKvJ7_ajnQwqYQ6x5TynU5zy3rpffYOGFGYgwRUlHQCouINTBAo_2ROP79gCPszBkwdaYGZ1J6Wx_1nbnJuGqEnI5LtSakW5gTNpy8PrP_yODiCSMoMpUayKjzEmV66WsT2u0Z7_2uXKkZhLG9oQxNhrYFdlBe_DKNdGU4-rIQC9Qyf-MfLNvOyb4Q6VvlEi2NnZvbRbtD6dGtzbzX8oyi36gv_z0SP7LNLmAEXmkshzVnBa2jMcvmyxqCfnxMe_DTfwf3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=YTyEkHyBjFvETCotMbrLQXKYJtoceKPSZ4bKpP6H39FmiCc6odCgaOdyBjViEMJAnyKeKSOggLC7dMsCSz7i940ol0Y4jbXHguQ7pPAP2tVEB6VmA6l_WjRomFq0cM1dkQg8Jnw7wpfNlE90QXxxLx92c7fh3ovLI1E3EXNaV5SMb8gUaiuOlHhs1KcS4ROD5i38Ufg1K6t4bMez6pXvKlFIyggE69zmW9GBLdec2T0V6Xd3WdWH0ax1R6ND88AURQZN0H4pN4kPi3IN5a0kHmfvC1IV5yv99LoOI5KyS_hpeaYqefL9lJqMQftvUilcNjBCjA-BJcPs3nBhZum9HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=YTyEkHyBjFvETCotMbrLQXKYJtoceKPSZ4bKpP6H39FmiCc6odCgaOdyBjViEMJAnyKeKSOggLC7dMsCSz7i940ol0Y4jbXHguQ7pPAP2tVEB6VmA6l_WjRomFq0cM1dkQg8Jnw7wpfNlE90QXxxLx92c7fh3ovLI1E3EXNaV5SMb8gUaiuOlHhs1KcS4ROD5i38Ufg1K6t4bMez6pXvKlFIyggE69zmW9GBLdec2T0V6Xd3WdWH0ax1R6ND88AURQZN0H4pN4kPi3IN5a0kHmfvC1IV5yv99LoOI5KyS_hpeaYqefL9lJqMQftvUilcNjBCjA-BJcPs3nBhZum9HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbKTYNZYKrgH40h0SaGw0INLfuADr5q8GQh4UtbX5u-xu7sbR5GNb_fmBB1Zwlv7oSlMyT7fuZHv5xVhYHMtb_6aiaWyPeCD2jXPKodhce694XmNPBws1YyJtZfeXMqItw1dO8hKSPYQGUlTh13-8I_54mTazCh6--mDTg5EY7bVvhrmp1ju2ePGl9DOoMofIx_Ff8DdpilwLVVQcCoOmhkvzR1LrzuTVOwp4jPZuMfoBAQ1W7fsNBkfU4nJqyJIKLlirxa9Nlp96O1c_YbNi5WAZ0oqwcZW0hOn6Bu-qzuHQQfMQmRFEd2MaMb0e-Dyik9dixZIlhkFiXLI6s5bvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=mwVS1rym5JR9BrRpqdH6fq2IiyaR7oL2GSYSnDH3E79PnTnHFf4KGpIjxBzJ8GszXaAeQJSv8bvydNAHg5coEGmT6UjjGA0-bhiSKWx1ZPEXdLE0S-HOnLDJ-YDTOFZLfLtuFvhFzin9mr22barhgK9EDTwPXKQ3r-QmVfgM_k_iogzE3Chg4-2VqYLwjCqpJvdWQIn7cBCgAwm4G3oNiwUntWmrR0ex_QyqtwXIOUq2sfI_NL-ChZYBq0KHGO8cfZIFFeBSIuhGLqZo8khisZAqVWMM7kKOk6ga1175-yqaUc4MZg3KZJjcAHkLpDzI7m-c2A0_0wotfJUiAZ45qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=mwVS1rym5JR9BrRpqdH6fq2IiyaR7oL2GSYSnDH3E79PnTnHFf4KGpIjxBzJ8GszXaAeQJSv8bvydNAHg5coEGmT6UjjGA0-bhiSKWx1ZPEXdLE0S-HOnLDJ-YDTOFZLfLtuFvhFzin9mr22barhgK9EDTwPXKQ3r-QmVfgM_k_iogzE3Chg4-2VqYLwjCqpJvdWQIn7cBCgAwm4G3oNiwUntWmrR0ex_QyqtwXIOUq2sfI_NL-ChZYBq0KHGO8cfZIFFeBSIuhGLqZo8khisZAqVWMM7kKOk6ga1175-yqaUc4MZg3KZJjcAHkLpDzI7m-c2A0_0wotfJUiAZ45qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=SaSXFkrYzclTGrOSeFs2N9CWBDvyuiTJ-G8YM6c05S8YG7H1AypqrmfWargOc7kvKphD_IuR73u8C9HE8Msurol_696qBWrCJTaXpjnBRT3ajhIfY3y1R54lzhhWOk5aeyJdTK65mdvCmu4vZ8YKPGGSpIX-d91XNwM3HrRuCU9c9EzjoDNpz7sKPEasujry1vNDzvuqwJOjaaXBoLPDT5pbvlVdrWWFdzM8Je7Uae9D_PejHob_h7PL_YxUHf7XN1Jb3VWqXiPu5pYWx6MgKhQ6RRYajZJEtMN6hTVe8fmEK3IqSfT54w2c1w_4G7vsY-b0ny2SvkQ0U33bIh9tOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=SaSXFkrYzclTGrOSeFs2N9CWBDvyuiTJ-G8YM6c05S8YG7H1AypqrmfWargOc7kvKphD_IuR73u8C9HE8Msurol_696qBWrCJTaXpjnBRT3ajhIfY3y1R54lzhhWOk5aeyJdTK65mdvCmu4vZ8YKPGGSpIX-d91XNwM3HrRuCU9c9EzjoDNpz7sKPEasujry1vNDzvuqwJOjaaXBoLPDT5pbvlVdrWWFdzM8Je7Uae9D_PejHob_h7PL_YxUHf7XN1Jb3VWqXiPu5pYWx6MgKhQ6RRYajZJEtMN6hTVe8fmEK3IqSfT54w2c1w_4G7vsY-b0ny2SvkQ0U33bIh9tOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ss13Wj11SQU09g2JuJabxXdk38Jridz6MkEG-ArEMRyYz68bXSq3ewthLMo73ktgIDMvJsiTdqEI35wf7llyiY1iCTtSXbr1o64YaitziuYWAXMGNuq3n3vuUOX3E0I38FhLqnsWMwsWdQUKwUeGENDhWNrkxbwebGoD5kIOGdNrPxtyqYb-OxnJDT_-Bodl3bmTSU0NxjR64mW-iCaOrrj9nxQhMmp07LP_m9n3z9JYkl8EabQeo87eQAJ8M2Gxfyy1JYsBicK-SRZk0334hUhXyN4JV_s_oHVc6IMs9Z9v-JFU_Jf1Yv2q-4b3bNSDDF4BBNWCC5p_TeqLiLA8UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ss13Wj11SQU09g2JuJabxXdk38Jridz6MkEG-ArEMRyYz68bXSq3ewthLMo73ktgIDMvJsiTdqEI35wf7llyiY1iCTtSXbr1o64YaitziuYWAXMGNuq3n3vuUOX3E0I38FhLqnsWMwsWdQUKwUeGENDhWNrkxbwebGoD5kIOGdNrPxtyqYb-OxnJDT_-Bodl3bmTSU0NxjR64mW-iCaOrrj9nxQhMmp07LP_m9n3z9JYkl8EabQeo87eQAJ8M2Gxfyy1JYsBicK-SRZk0334hUhXyN4JV_s_oHVc6IMs9Z9v-JFU_Jf1Yv2q-4b3bNSDDF4BBNWCC5p_TeqLiLA8UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUmxKbe5lM2fjLZxgxAECOZchSDD3Sef9cfqzfOhmTJBajMR9UOHPc5QOtBzej9fYsdMAdkF_6ekSt71bGK5SEO6LmsCZV_pCkVk1EPKSJpYUCs5E9rEuTarxWsOjTc6-pjeRkpQbsyK1uyDB6uVah1qF51C0BriNr4Nuihx1mfUmuOKCi4JYummX5oYubjUi2I0oxQjErZ3FeDiqT7cXcE2qdBeHPcF_vHI3XK8sdg8zQv0OEo8eWByr87lDHbeyxu4RIeQJeWIECY18gPK7worn0d48iqpkpcT8rMkFrPNNW5Hv0AZ04cPBNBwoH6GtTcjuKbbkQFGNirQOhD0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPFKGNavkyoLwucDCtF1Jc0VKPM2SD3I7tODEjMdxw44uzt5LAf_YlOiDQ06v9OK1VGICcuCn4LLo_vQk4s8Ev8BDr91PgTmesRLIOBCratduGQnduHTud8p48T_t4Lvm3KbgKODKNM6QPs1Q_M-P-AnVEoaB97XRNNDkqh4AFanV-GqeQCViv_ZjTbOkptWmozm7njIawSbJOiGfYObUN1_sT0MgrB7fsfLdJ5UJZOiPXNnwlQyjMo9UtbrKqoVhHLDG1PChMpesYvd7l_-citcpVdBFrA1M8Q2_E7NxWqf6O77sRheHQYG1Ygw6ti_KJcazqcdvvCIq8o3SoAeJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imgt7BMEGBUeLKZCi4AiFVEi-GvPv3F65MYnvknGSO5I06rsjiUrJNpXWND7nWnhkqIN8HMzdAz5TbKRBkF0rpWRtN3NfO1aqfCBRfNzaOGhRSKnW-RzKNwUHqNKheglH-J1r0U9efMcv7lTQbNqkL0PMXmKvTLjpZYWgBORdD68yHIf3UYfYGKNScyDTS1P5_rmejUhV5Ew25CfYifbZ4MWYLlVersS79TPgRgJycXnSStCIXy5Hp_1dsooP9JTK4Yd6aMirgyY-e9XpvA_Fx8nPzs-WtNOpoP-ErjlaiPjRFhv2_Qo_9OPubn6cSy-p6XZyofVP_PDjFK-Drhk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUHx2X8hPU8QKj12xp-naYQC9iuxkPgXgQtmn97u-zgReMhz3pgB2udFjGzY2ugkY3pIONk5LUSWT1_AU-mMRqZqx6rsL6mQc-RaCXpYKo4CKfTaM0UJJuiuB6Eu9cqEL-gIGeJjaBKAQfxCNXXA79vfp_BRavjjChSBAWSBGuCNNZofezHaavNn8IC_mFiwcEEquj051ZG3fJ_7D6HKMBLElGc5M5NGj9FzHV66XtEHCrtY4cPv0XOCx6SnaQjvlQUBoit_-7AKSIrMYSysz-5j67ZkD0zofAEDOUMdNamsdjaedUd7zCla2fpaMy5kTixNB-Zpz4AvCKwZoyxkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEfY9C5CkEDiRCuUdTlajfu_OWwDX84B7WeisLjgsZ2s4LiABlRbjK8jNsfKlr0LPoaIl2Gg994mt7-5IFzE2TQe2eFrALBWxqDfb-X_N2Smo0sHnA8Uo6sVxHP87toWCc7Kv6EDPlHHDgBQCb3VJxyp9pkGwqWK6GW0jEgMJTqu8P5Y756L2CCmHR2el0WNYzuM94_XxKEO7FN9FZmlAwuVf1lrQxViDXJ-teNRWk6xNyZIL1fMn7HKT9T8RLmgn-qo9_Br44PcLAq5HOIOCnDdyCYcgLLiWEdGhOaz3UQ0oe51f6aEX5jeyHVghWx7V7yId5M96Yg-2gW8ndSvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3lL7s632V2nRb53fkiPfmemrPJK0kcRggT6b__Xp_vNRkKEC5FxBExKUjZz8-pQIlCJBNekoY1l6trzlSl3YZ_R2fu5KvRb15LsJBZv6Pz-G9qjgBSE3D_XyPgQ68EeUxlcscPPY2tNj4EqQcPLATyx00t1whrM8l5u8v4jl6JRAmdMstAUkIbny1YJ1MKTFlaQG4eWQThbCR2UrLrN-UBG42nDxLfgNVsMYZxnnEFOzfvHw9ffkYp9CeqV0mg5tlEus-1kF-OpejGA82DEP3Kj4zz_BsczRuSN5qX3Dul9y9qGgSqW77SxpFkod3RGda0KdOBTVXkZiAuZacBLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIGbiARmJTFAiNIjbGjc6g-fey7cbauEWazYMQKeFWTETV2LQQb6XH1Kjn0oVdv22eEV9pghZx3_5FXV1isaPS4jKb74jphyktU1Y6ynwZmZwo01RC9BUjsQ_EOmtRfKpRueXD3dxsjqR02khOcAnnsBx8Ca1H1aqnfLkpn1HAfSzxf1IqHWPjtHQiu6KgwrP3-RpnEAbwFq6v5UJK63j-rQhZ0akEUKxj_3QbRdaOCPzJD-hMOPrm8CRzT8GrhiUYZmz_nOUB5Kzy6ILo9EIzz-S4H5L6J18X90GJtPvpQHIXsf63l3dLQKA9I8rbYU6CDdHbwxOrbh0JyVP5BEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Puue9jAgEp07ZrbeOl6oPA4Np5jCP5qkMQIPMqFIwOsS2xt3o1678LkT_u8S1uWhVCWaa9L6Q9V-dvvKzEbDhukppt2qn0yr6LKJjbDFpEuGJNgTU69dv8algZLkf4wBI_2NYyFqOVv_RHIqzeI6kHzYRzLU30T58Yr2XgnYQkjjkWaIcCcgaYgz1dp_7B-lpnHitcZwdHml1-RD_d8mkYeEhRiujmTwSnLIqS14DeRIxV3kVapjaV8SZzUtqG1EMwBkRkszsnL9y4kynbYvhjhZM7pg7HeqAYyGGrygtSDlAeWNt48UFOSjSgCu89fpteXJnCSPbhkhuKpzCfql4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=vcnWg6JQItgA0ovEm-_2jiKnOLI72YeO1B4kvKImFMVEJCUJTuq7dEkRsmXG7jazZ5iWukG8BkKaRNDKGHamDqzGlSX7WBtJDCe8iPELNm50zgDhr0dAfXliLT46NJxquIaKKhV8my9PziMUJPV5Ma0xBhsTQQxbpENlSDr1hhs0FGqKo0-K-mtszc_1osJlMJ67cGtbQKWI-loMgpj0EHVPJyB3z49CoEJy1lxaHqx6cIhvlKFmYG7Fk5146fHoZLJWfbgrTR7_CER3AWw7L09D2xPqaLgQ9TeQ9i-4Weifmpl6JdWEWfm4rRAYRJejtOyW9s_uevMOuZAoF3IwqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=vcnWg6JQItgA0ovEm-_2jiKnOLI72YeO1B4kvKImFMVEJCUJTuq7dEkRsmXG7jazZ5iWukG8BkKaRNDKGHamDqzGlSX7WBtJDCe8iPELNm50zgDhr0dAfXliLT46NJxquIaKKhV8my9PziMUJPV5Ma0xBhsTQQxbpENlSDr1hhs0FGqKo0-K-mtszc_1osJlMJ67cGtbQKWI-loMgpj0EHVPJyB3z49CoEJy1lxaHqx6cIhvlKFmYG7Fk5146fHoZLJWfbgrTR7_CER3AWw7L09D2xPqaLgQ9TeQ9i-4Weifmpl6JdWEWfm4rRAYRJejtOyW9s_uevMOuZAoF3IwqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
