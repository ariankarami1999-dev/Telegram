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
<img src="https://cdn4.telesco.pe/file/Ryqj8MYsapvntTZpREfyy1ymTA70YeBMOZsBIgYH3ffSzlHmY8Ixo-wpTDE8EEmhiEo3kaxJLotocpdUs8o-NTNV05hTehGPSeSxeWMsS0YAocoqd5AHomTXkElPrykZeXi_PBMMBFdgstZQEZGdhBax1E9PeDdgYU4cOe9N894XFI7ZthQGCOG2XrHD-_n8nXHn4p1ahs7mrkn44ef199l9PJ0GSPciKtOuhFy3NyP492J9ZBiNTGYQD5CR0TBd4fdLCEm5HT6Fxw9rePBZnVG7dioBeJGdCfejNYIOId4Vw6RIsogm6KYYum2kxgSrApMBrRbBg7ZaULV2A00UMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 183K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 01:45:09</div>
<hr>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKFlxHNOKvVwVN5P7YpSoxzPcyjBpe3EtTT-OlG8kWAuW9z-2QV1Y8DrK9V2HJSO145sK58WATa3ZsZiHRZKxtuotMtv1eBBzNdLDuDfSujYTWgGWBYoK_BBxrebmz-uQf_RHubhF5xnS43pjwRxjYQnFqaPzNhPZ-XuUTuni0Ybtw9jiuPkZlOGVM67RDdiLwSE_kBEWqHYaO3BS_dUalDLdSjvX5_yywB3XyiupFT8yTe6D9KTwBXrlAqn3PS8V1TWtFLLnNFmeldlV94knkeGgXDh28soNqnKdsalBCWmmL4ZcnqlmsmjOXdDReVNH_5_7viqQ7Trz2H6YnfJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlQg3qP8cr8DJ6npHK9KVzLkoDHnygABJ6CHjpe7EeYVOsCw61Lugf0gK_mTdDsKd_k3iKFVNKUg0g36vEmTqnMUBMeJmNd84nmsWe2tk-DMRMfgKrIHrzLERc9YRLhUg05lgb52slng4df4TLYsf26LNbuE3dIqiLxr-S91xAVb9UNjie1TuVlEaUYGGM-fjdLmQS9SAtvNtKIHiWj-t1p_Y6vaQGQol3tCMK80zla4QbD7__sebDpQO6leiA6EMSB8pxpi7wr2ASc0FqIjwT22QI2Aw1W6gqmlo-swEMSHu3PI4D9xj2jTov6foOWPo6m-9F-aVtlZZikRvmmdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmmkXSpVTQNtIU29tC-p6klsnuVFxKvuNrrCreeFnGN1ipfeurS14pE7zhl1iDbUzb947ZjRWmU37MiOLhwHK4UCWO3Mxnk_fpk1LIHYS8gQdW9AUKA4VIWWCn0gWUNmdRcJB4rBq1_7yoDbYpx3fmbX3jKWOQ4D8223f_XgLdSV4sVeXZtbvP1QR8fBhkhi0XC8jiAnMNEWZtR_uFUqZCh1Cu2ZH5gLPfl64RLqKjDdHnXlnvRu0TatHLRdEhgPBhINgAqJTVwZ4FidykspQ4Fc4j3mqnsKElrJNAF5XOY-c6AZiv3m2r3WKP5aS4y27Pvn7nIFauICxI88eR8x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK4GqUTmHaOUCxxDZzwzCB_bttSs1CzYx-9hplGXUDumQb-JOznivvNlVyLehh_k2JU1vI5DmpeE7X8nblKSOctiepwfwc5z9Byrh1AOxH-BZDNOjnnPdAjEamCFriktQTF7Les6AjP7Yda9nNX0IRn0fjPAfnJTDGh0edndCeGrA4-YN6B1bEperPv7L9xsGgMx7dNuBgqd-UGFs2IBUx6Ff6a3hsj13QNrcdi2AwwVz9yF4oX2vu3TCpoYH5IncrS1RQzf5zOPcIDEtBSWLJfrrTwNqeds7BRuYLwPhmrT3SB83T0QFOf3ZJDdkfoDXxziXtMVDNCIJErm4yFtcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTbviV7AarefffcD50gVZ7cf3QklBiBa3KkKQ5nC5pyT585Roelsakf5v1IesWZ_nt6ZbfUXrO_FiZfGu50s8smpz_pVX5xqm3PZQcGk_V-NHx6y1gOERFBelbHOm3wlnDgxT_OFZ3iS8WaKZwDOEy4_Nbi3XfCjpiCbwWN3X5HIwsDKQsAgaF-hm9c-PbPcWcljL6-3EWxbf2IbuvcB5fAITjfcXeLFUa2KzNkoTZdap7IYjIMrPzp8LtturD97IhJq9F5suNvcxJ4PkT5qC6kofZ7zh_tm8FtDium5HLAbOoN6sQKXaxZCMdYuhAQ3W7DzPRSI703vDwApkx9DYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=udwH7wIYCyPoj-z30Lw0YAQXmPHR5vJeSQVCl4dWS2Imyb1C6EiUs4cWUtdifPA85vTzY_412xkngbEP-Gv_URPVeQdOQZIU4mbsQqD2iobFK4y92Exy0Rza7rMEpdfkG0zKcWyF6Wa7hspLA_SwroJ73tfzVKsdAho3I4AHG1GvKJ3o_xhyxd4iznhe5sc4l0NhUAz1Uzb1KMoPMuMpacEqvPJlU6paVI1IXue6lnffoNpfs2r9_vmZj5a9tb9NNiD_l-bXNPprbZIjbs19_CZkdMODyubLR8UP0JPqTppLQgT99uvAuOUqWNYFlUFS6LCH1lvBOHqwqYxJf0h8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=udwH7wIYCyPoj-z30Lw0YAQXmPHR5vJeSQVCl4dWS2Imyb1C6EiUs4cWUtdifPA85vTzY_412xkngbEP-Gv_URPVeQdOQZIU4mbsQqD2iobFK4y92Exy0Rza7rMEpdfkG0zKcWyF6Wa7hspLA_SwroJ73tfzVKsdAho3I4AHG1GvKJ3o_xhyxd4iznhe5sc4l0NhUAz1Uzb1KMoPMuMpacEqvPJlU6paVI1IXue6lnffoNpfs2r9_vmZj5a9tb9NNiD_l-bXNPprbZIjbs19_CZkdMODyubLR8UP0JPqTppLQgT99uvAuOUqWNYFlUFS6LCH1lvBOHqwqYxJf0h8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQXZsHiwe9pq_OdrHkmoCTm6KBc61CBqEtV5MB0twlW31XHo115f0QGugNl9I1rhrlBuM34X0HkkqaKhhjsbjFrwzEHTE7cvRXBygzQdKQRZctLv3oW1Bj9k4Y8-F0ri3JmWKkdXq0a4VlB9lfXYDYGCLXbtGjXrQ0l-qB9nqnSIAm2jslH3kO2FyhQDrcAOa0xxkPxpc4Zw5KDiccyL0RSvB1JWlutEdwxDKvLGKcAbjRxb69Q7feXaTQBZE6Hnja0x3Vx7qlVc2C6ssgpSp_puM4NkI_6kLWUHN_FRA54MINj3xP7tPrVZC1ImLE_FK1oPxmcUaTIYwdnFFO1kPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=EOdAg3FlGfUIq_iG299lTb-sg6zJkPyZWdgPDT9MI5cp2Fhdr4lBlt2ZFaVNjnvcnKvQ6QPUJI8I3ZDpaKyVDZBKNKrNrmr3wk-ZlZ7mRsDegaS83jsXgjlYbatmbJ6xP1QcJmt6tjL8I0M5ThxRuUEQ4_wtUnyCElGRRq83SLccOpU6aTOyvRMqeqZDoFoHodRggdsvXnRFcV8E1K5qx7egJ7uKrcY9y-SjZSFXG2SQUtnaj37RGGgeWEZlOlqwPhhTPUu4lXp66kDNXAzW-YaR2N9B1Lx6G6K7r8sGq8tZc7GKXP097C1-IBCmReJ3N2Pxuiz0qLphfAUI8YAu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=EOdAg3FlGfUIq_iG299lTb-sg6zJkPyZWdgPDT9MI5cp2Fhdr4lBlt2ZFaVNjnvcnKvQ6QPUJI8I3ZDpaKyVDZBKNKrNrmr3wk-ZlZ7mRsDegaS83jsXgjlYbatmbJ6xP1QcJmt6tjL8I0M5ThxRuUEQ4_wtUnyCElGRRq83SLccOpU6aTOyvRMqeqZDoFoHodRggdsvXnRFcV8E1K5qx7egJ7uKrcY9y-SjZSFXG2SQUtnaj37RGGgeWEZlOlqwPhhTPUu4lXp66kDNXAzW-YaR2N9B1Lx6G6K7r8sGq8tZc7GKXP097C1-IBCmReJ3N2Pxuiz0qLphfAUI8YAu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEVciEyW1Xo4-E8IWD_s2B9K_Pf8LdnYvbnFq0oKRhXPMgqTFkO8OxLnMnFZoUJMUtIzQwW_WxhcPAsi26uUt4HiNQkcOOr0L1HwXZYy5sNy6o_o5NXkxabFUahVjr4qK2uzwYJIDp7397_foRYOfAPijuSH8FjR80stGSqreM0cflXbXpKLU8MeZEW_LMVSrnJF-sf8qfodcjk87VZW6vo9SxUKGQKUnq4dqRb3Xi1A6AoxjPlicg5IVlCqu9YHh4tkAZEzabpsEnAcAFqcAvrpx5GWfk2Oid5SlWlPS4NSQGy_7gz7rd7AcSTyw1idbXMIlCDFZWJYV4xXAKVEg3RY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEVciEyW1Xo4-E8IWD_s2B9K_Pf8LdnYvbnFq0oKRhXPMgqTFkO8OxLnMnFZoUJMUtIzQwW_WxhcPAsi26uUt4HiNQkcOOr0L1HwXZYy5sNy6o_o5NXkxabFUahVjr4qK2uzwYJIDp7397_foRYOfAPijuSH8FjR80stGSqreM0cflXbXpKLU8MeZEW_LMVSrnJF-sf8qfodcjk87VZW6vo9SxUKGQKUnq4dqRb3Xi1A6AoxjPlicg5IVlCqu9YHh4tkAZEzabpsEnAcAFqcAvrpx5GWfk2Oid5SlWlPS4NSQGy_7gz7rd7AcSTyw1idbXMIlCDFZWJYV4xXAKVEg3RY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd0qm-qZZPV-ETQUO27BTwHj9f5GxM4gGSPk01LnnnzlNZY24eJndCPVCEWFlB0fE5A0aIhQZh82pozomJDaXI1P5EV2AWKVd0sFjjoE76N15Wy9Lufq44fI227V3KvFUG4UhQe55LFrEuCGsHgntI4Q-_q9rdWvfxvD0OHWGbqRL7y-MKsYdpOwLhc01iTUQS9kbzzt3Uu91gBn21Ke7icyQPlHcBX8wkx0zxJDhm2NLYjCZu408NqTFprE5UP_rEVKZWfmvhMTyzDUx8jsofLJSw4_fCeZ1Ken865l9n5Nmq2PwOUipALUikvt0BDza8McdMaAc9qPXl1WWz5zZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G00dNewW3HJG08WsC2aGYLY1dkvsmjXj_v8AxVKBbQQJihnajnBNmUpFMMy2fDybDwKWwmXupp5I9BAu8GwfZFohfbe-T6Hca7tLny3D76V9bmBkPttq3cUYNU2J4-AHVn7JJyuE61B6Y99X1w-nqtJO3gDAMeJWlOU47sOMOp9jd1O7Pb15ESIxQLApF0Cn56FP9dpi0eqmqwKqAtsAjzoATevmEXC4oRSlAxD2IxJg8Xx4ZQ2SLKRNPJ4vY9x8KZwuMSag5Ci_UkB2ODQ8x1GkHwa6rhbD3lHK7g9j7YBBMcoPdydh3VUfZnnhSfnF-2TZdn7Uigyd1ptVTIWYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط.عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان‌جایزه‌بده نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22392" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_hFD7oZzEj7rpz9wsR-BEvOpvrzShMR3YIG4WPiE23Sw4kx-5StIAm11_bU2nSYhdbuQ8PpP0jDY4CHEFwlDxSB3TXK1qaTo6Y8WhH-7cGNlCREElQCvdC7YpZBjs9p7Q7SZwBdIifOjQgwz9b3P7PiiZh0Ob530-xBdUgD0OtJ6F0WEAotbXI4VPOhQ4KzxYkMNhCjBJHYXY85s6mJjVHCcwgHTzPzGMmNT6tK-_EKILuODbRQklWEDCpAh5llGgqCIxGh3p5vYkh3Q4rWOQRsg6A-Ywtxcb6_dex5JzHm4an-8yt8gCkP9WVfjLNUXiRbzcLkS6oqsqt_B-1sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YafPWvLQQkHhYyJOnS0N9LkQzkYydtXwjq9T4ZKXJvjoO9KQrmZtRYSiAbuRm8cRzJqB7X0juwNAuXWW5tR68aHcgpwNk_aQUL8mcqJSy2CEFyOtyCfxSZV8u-qNmqhAOT7aEJ4AToWos-p7Q1NYTlG9OWIDOPATqus34VHHhk8Hr85DjimWwRZOJVTDEP4LFjBSVGxglxpJP05FpXVqh-XzRbvwQnefOP-w0-74OlQDLZDzEknrB_nUfmGtVRGY60vxB4eASD764Pgc88bQv4IFP-DlMwrgZU3aE1jF1Z_xYLeUzys3Z2Gd3J590by1BUhiuBHR3tv3ITUgAVcMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skdqExMqG85JDy7UowC9Z7jyEKY0XpfLJBsHSnSXPW4CSKsMauwcDkUQ9u9MvNXeCzwheHnMA-U9Egw6xoqxRYCAIvi2oeXj_RNfcUEnRitsU4B9h6tmocIcbRNpnDLS6QAUZtkqWv7hY4zBC8af71Wph_AW5MMkn00QlDhI8tcluvVojOZ4AubuKf0qrfeVrPuQ6_Q7y5ny10lCFI6-eVYwyL7cp9kPv7IwQmAFsU-HtfdJOvkGjt9qsyjFrRJL9jl3qq2TmWYiUGsHaltYuOZP4pfNEZ2vzuUthNwu94B5u576tL3NO0Mmd6hDbhIwxFP_1TdNewUBJeOMr2yRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyyrXZdDUPTxikXX-bF56HUVjtpTLv_aGuOESmm8NGpDyK1f4xQd1lapEnPQX_9aoKbqqF6ycB6aWgoWZZNC4KtQ7fgvWkDu7gd0QUOn_XEXCafh0dFvTe_tGuxEnd-BIo-SN1HUNrgLvaazHGdJkzBmHisaNumIHpCApG4nk7QzJlQXR62BCNJ00z84fqW1jDQQUr87EOzdvfkakliamHWwIhAozDEGC6-J4WVWkBKBjyX6H9PVIPG-3KK_4CCO4mBnH_3YAVswVx2gjFueyfy2o7BqsCNPAYD90ObD8dSMTRwzxYSFoVdWYGrgz7y25hGPtPMfXljXk4bSJLQ4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRapht_DQXRs1wQ06i065QIltxaSOnFFA0oUjX1rzDTXZ9lzUNciIFzSGGjrqu-wzlVBe6U6p0bPoS9TzU2ZAqo5Zjttqscoksxz6SbtuwC0mTKxa4fg2F0wNJcCSjw9Xk86T-DtmLl_UQHzPa0BkeFWxMJc6qeUBJktMIBrPbgatnuRfnl3ZIolrNrpSCge-FKThvgTFFRVNrpP_ZCfq1fHA1aJR_n98hn5b-j63hYF5hHn7pe7aNhMhewz2IzCnonSDWd3H0aUdApqetBnbkQlFWQe42ShSGOfBDepSkEMP7bxnuvWUUUPKuDrYOCT3vhO_GMfQ-mFQPs4RA8V1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qygIZNdq3sYN73f19X5NsftNMfHhYSU3PUYHjYTdRAk6vacMNxzwR4KxPns-6-vRzYlbjptAaze6rr5ZmzymfyV7-Ww2XYTQN2szqFh_IAfABSAaTAGXWoYZax4NUfmJxheE4jZyqptSXcPWbI2LwEABF_boMXk9Ztp0qm39q_2UkzmeGbpb9RI6Ri-Lhyux4SX_RHTyVHA0LMJXv5qTnSfEp3y-JmfwLMEmztiec6gZY7PmwyW7XUQ8ZKFht7T8SDSBx4Ua4NP7CXZQxx90B_YsrUC9j2hGam63yEJFZ0AsmKkAKE5GF--Iw_PsGhFUsFKKLr8x8MR2RvIDb8pWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC3IP1eMveuH-L4FkdaPjI_EO4XV1NpW0RBC-JlvLPukfXccsJSCiMi2lNcC_jrfShNXhqqrJrk6kH1hkXLjWZwy5H02191hABd-8LB6kdW9t9OwugV4IAB64sqVVGaH7eSjiOAfrl6FjMRmu5pTpRl8z2_a6lZusS7VB2BRc42imwQ5-9QBpoLHhH8RzLQY4ZBtnuNNLdMzytTbM98h_0m2cj5PbyQ7-OiLC_f__l1li1tn9Vj8kCEcpI9HEJs-owbIP4jMdxIxIbp5iDr8u8IY8BUhPntcEF2iDHWb24n_7CjcVkASc08odwtEcs1Ccdh4r7Uq2BYT5qtcwRrTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtWnV6AIKzVpJv6n2TDy77jwvB-Qem1rJYFjdGVesKNi42wFuBJJfYdk3r1yTfYdP49IKsarjTpUMjAfXfUqg3gsrnAceQ3zAFVt-hn9chiehzXT6sI-RzuAGDGha5pvMVYrziGsveNGX5mUv7uw96EfCpaW9cWRFwH99WHzcs8lutd5_J9VfQFuU_3brnnNsdw7E6VUedCrNDLjo4S5AOqAY8oj5Tgj4DYaGhYlnvSNJKF6e5BdzIC71GmCkNGEs4oL1uRuT7tTsIWR2fw1R1nuYVUhzxrM-yyelEa2CZOzaTQEfPauxjP-HtGcUnmJUd_5dhz3-QtBOSD3Gn6SCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBTqIzJAcFn76Vq_CabmqpyY81yEOXjJ0bGxdfbgb8ddmm_iZJqDOtQaqpEbPVC-67ukX1ApINcb-iQIVZsyfbnt94iielA3IxZkmgU1PUk38AZuVQAmRUXDKhKgXi-VHmkZqwMjHrbL_PjxcINxwqbmFMF7UyIX0QHiHMbxXdX7uIP7tn7PGOpzrz2XwxV9M3-2Vc3SZ7LFRX0VvMQCsp4sGXqp4NG0sDU2y7qTUOWHOddbEC1V27vYGDZFAsBlOJU9qH3yI3yqOC_RA6tejS6lp6DQohznkWykpYkWGpmTwUUNrKsYVky0RJQTY2mVp_1lRBwDyU6UJyO_PmZ6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Minxp1xQw3nyIxcTXVN2yzO1W36tCm2p4nw4FyYpnQKa7WG7iwboQk550b90URJ9heYNu_YJeQwV1VYRoe7B2IRgYACNG9snJjb5U_NobxCKFCK275LIjIJ_ridsheprd8ndIS80M54zOeGHUBXB8Uju0V-Lga-xnpG2RT06o2wRY3TqL0l9lDCQVlpx5KhMST-CWFopgvjbZIbivx7I6-3QJKIYJaZslNvz1mUiroW8wdS-2SAbs7DwsdKV7ofDrbAPruwlsfNt0vYR29fyyGX8SSma8wD9jT8i9ZexReTsOdBDabE5w8gPIwPABCtqj0oqIx7gtPLVqMhY1LTv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6q5J1cCWgCyNklCEgwOid28xn9nhiWegCcZkwFvqA2KOAGK3ZNvezWGuqD4l2FDwZzTva0VoRxM4C2IA8VdYhPQ46umBCg3ZsQordyIO0HyMBcyvX1aVQ9uDDaTcKPDPnAInMp67ilcsmQ-8JqP-OP6-JUg5qxlXVksYE61uB2FwvpSyHa6JtFGI1-kXXs_bjdeLnXV7-GcHRyVwVhKKAsi8kWb-DPwf3ZrB1hxiR2T4CIg8lrG3Po_--EZuzDq5iweKDgnsigz6yNDNmDMDgtpvd0jt1B28GSS0e1VRSk7Jh6S3aAeJ-1dMNfwnB5XxD2rijtKVCGaNSMqw7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنهاسایتیکه باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22378" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=FDueGNO3mJbqFLe3YGIYmApsVIQ4t-7ZZaeXu6AqRWQM0oNUbyEW-iF3xoVPPD1B9Hnx1BKW2WsvMvobMxaUJiD4UsDpkmrtAtcGPwe483Tl_i8Frw083zCtBDsgI7l_T8F6z710oR_gvB1blST18IpZB5m_fDC6Z1i1wlVdo_KWPng1fh1ftaJD23ni9vlRl0AxQQJJrczsH8UsMts1yIO3SmwSm8VOHAVOeoD99hTBHZXHljxqXyvdAduOD5bUXqku-GhAGvkk925kx3pILfV5X2b1xDGbb1QAiGLsyApwB8Th96pCzqRtmwcwKD0hFxlQROn3WSvwLPXbbjEx0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=FDueGNO3mJbqFLe3YGIYmApsVIQ4t-7ZZaeXu6AqRWQM0oNUbyEW-iF3xoVPPD1B9Hnx1BKW2WsvMvobMxaUJiD4UsDpkmrtAtcGPwe483Tl_i8Frw083zCtBDsgI7l_T8F6z710oR_gvB1blST18IpZB5m_fDC6Z1i1wlVdo_KWPng1fh1ftaJD23ni9vlRl0AxQQJJrczsH8UsMts1yIO3SmwSm8VOHAVOeoD99hTBHZXHljxqXyvdAduOD5bUXqku-GhAGvkk925kx3pILfV5X2b1xDGbb1QAiGLsyApwB8Th96pCzqRtmwcwKD0hFxlQROn3WSvwLPXbbjEx0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qujpee2BTT0paG-YbFPH9M7mPpjPLy2ER-bsUn6UWtVglPCa3vMYcgnletWqvhbV9u9MaGsfSG8NOztxR6ukYHdRUOyZ28CnHBIT9Pb8MI4WnAj9YG6NYUXaTY-4smiueZLkx6CUwwds7yR9nCIG_VtbAM6IneCZH1jHe-zredlW0wa95GRSPsHmLZ1_asxKRq3DMXuGlCYPpgiHuj5sFJE0rFqsOCF1-B2K5X2ueQyvd99JxUJYJXnHhtFZUq1_7P7uNWbalncP3W6PxTvPCo3KQHkbzvfduDh8cSQnFXQWG_5yWJ_X2gp4bgyvM5_FnmnCm6exPDKNPydDpj9inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxZauQ5taDCHT55uC5LYSH4ipchCH76RpVobtioqtDoK5KZOa8wjWhm-mETGMP0YXEuSp_fS0fKIHQUygELk9rl39UWQe1lwxLfux1OSf-1s9ImyPQ4Os4mMNQ6ZYJqQ0Zqx_4z-j_lrGDdf6r-pH220XmrFxm6VfUXF3wbmKwz1-4qxBkkvkH_JdJ_3l1OZDE-lDIXJ2X_TCtyL465mLQ6pn2DEZd9fnYm6EXGwv3OsDY5NXqvr-0ORYMELLqOvpsJGWBqOqvV_qndvDFaEoGOWrfkLsIDfKPgkhjzkJB93n_YQ_i_bQJiLukPHAKhGASnPqDEA2XX5tF9SZx0tAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW9rcCUVVtMuLcbxYKWo2W4HCT3XSrQXoP3fg2U9K5xTr0qYUS49xr55BOTlvRoS1s4A2iMt-3Fd2gf1QX8SYT0G38BJaffrDJvIYWcb8TLWH0gkTLF437QX26ziDX3G4q8YcbKzQrNF4UJoGM9FErCfDoW0sm8lTT0GBym6ICtlIZ07Jjr4apwMVFoF3AkfqFPB9X_T6wvDW0V0RxayZKt8K02rKvC-1381fT_xIBf7JKS566OKyr_-FpfNMoWjP1Hn7KumJwyl4v-1LzCab1k6rfvoFRbxk30RyGsLJzGfxVR8NGj8aJYVcZMH7tyhjXlR_Ba3z9dFVFGEorkfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PODm4P_hyTPAjv-AeU9d0ZEP4kmdk1-UgHVimX19GmiWcIdaA9clPG1UFz2s0cDRJitjze3RIrsXo0hcDBr4pdq0Qg8E7FMMLe9qSMmH1hsB5hcRcVL8b8lep7Bb5uAuKUJUo0BrmMR2OPcvGAAz-sexlTw568m6j5hU5_oYhrF2zCzzwW_bpnFv9nQBedOePOOV3gDmVADVgvI1znor1Fqw5hmreFtlsBYAKPfkcS3xutIqQf9qU4ZyJ2_pns1p5mN3Cs3xs-GFr-Df3iKdYyIxnJ6OZ6iEdSZaPBReEw46NLEvihfndLaVtpW9sb23ypRAHCWjqaX3gQajQvJeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=jF_5-ejSWh_aXW1czFBvh7TWjhHiHAc-cEehbhq63LXfdpA4z7yHyuwmFsU5ry6jaXRkQk7LkkM2BOKModnToSGWFGc-fmxt8v0msR4Y0pNBS18MLL8C-OxhiTtlmsNSRmJ-wERSNVkqonokjRcXKC0DPkdGZKmC2VtLkZHT51FvglZ99ZfeDPbkDjYQQjFcVPwZzBL7P3irW1bZESXOXujIQikzrZvnPl4VexjOY8B_TMUiJ1uBkXqJFuAPL926nrv3nKyJjvN3zvvlfh9YXRhQrd7J4drGMUbj2VKMvHVMvegT_rTHkj67HSczbBVRDH8DSg-HD7UKU6udJs6olg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=jF_5-ejSWh_aXW1czFBvh7TWjhHiHAc-cEehbhq63LXfdpA4z7yHyuwmFsU5ry6jaXRkQk7LkkM2BOKModnToSGWFGc-fmxt8v0msR4Y0pNBS18MLL8C-OxhiTtlmsNSRmJ-wERSNVkqonokjRcXKC0DPkdGZKmC2VtLkZHT51FvglZ99ZfeDPbkDjYQQjFcVPwZzBL7P3irW1bZESXOXujIQikzrZvnPl4VexjOY8B_TMUiJ1uBkXqJFuAPL926nrv3nKyJjvN3zvvlfh9YXRhQrd7J4drGMUbj2VKMvHVMvegT_rTHkj67HSczbBVRDH8DSg-HD7UKU6udJs6olg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtoilFKyJ_Qjv6tWgO50Wc1a0ZJp_81-gNA2spoxWOKLdstLRuntOlGw1gjinX41SjKgaR7A4uZuEHMCLE6YpJ79Yj_H664KqS2N_izs_5gtANSnYNX_8fInfJwoM5RIpNgsUx5InQMXE3l3pjYxpfP6oJSj-X4-VJD7GP-OtVfCvnS6k91FeGoHzc3hFlrB0UA6LMYR8TBVyhWkTDH1n6aqMC_02LV92QV5wF9vdnhjTzCbIvZ_JRWece_Ea8wlIhoZXYW27-8z7dXpXReP3-YbhVOyqsxSqyzoaxfkAs3LCWbnR0xiQc0RR4kFavGHbtqhwrzKW0cx6nko-rUVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmrhzxMwC-pM-jctc0ToRfjJbYfS88CKsNSDWsJW9BS9-0XFtPnmGu7mOGsd2ISovNFKpQPh_yzuklh3sHtn0tK7nMsRAZxr6kGLQcY79yeKD4c4Qqh-id4ncsEeoN5R3-rEvh0iE755vaF3WN5K32vBhK-wK6QJQrpG_SaCFEcPfrUyAMGL2_hI7GlxfhYN_z2xblglGYrji8OjPPv1HyGWPpGtIj5EFAv9Gf-YvlEyIw8FoMVqjHASb9olcfBL82HoKU_15XCu9nKME184ltjq9cY0MTA6Fg_bsxNorqusKnUbwm0V_bkSY7Gu82j9MKCPs_4J-FUfIT0Jd6_3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlANFjxiNY7_N8OSc_pyjn_QF52OZT4D2BtBtvc1BL7NoGJzv1klMMlt8m3I7VNblSmrvgTjTIq2RAlb6_dfBM4OLs5POnuO1JzG6wQBTLUpAASMsM5riH2CS9mFvfBM5fgrWFAKrAl96GBX1bEw5VRd0BQpolrVaJo-9oup4KGFIUtxWhBDlSjrvz1UbUX0DN0nN5ROlrCnsEuZfVc6GIFPf9n4xAa-3gbEBrgkTmR2tlL9sHSURcSqoz0_rwHrQzDZLtmsWFMtaKxtmTDtPBE_ruFH4Ch5ts3MZhgBix7jvzkeKFUX1nCJ0l9H68L-Gp6uysvckDBLH9XaTEmDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=jH6pBJXW_C8NFoFmC0MgnRcDatqLOqGNcFRrpG1R74eJtfZ--ZHD-oJO1yieGa2DK3z-wuqb6dfOdTyKdUDiF6QEFV3_SIr95HlLt2K0-PQARFk60EAVSlz0txwmkRh3OKXfH7fYy-BoWFhFcIN2mghkpB5VMU0LF0QdFxpIpRN5lio89GabIgsiSZ95ydpPs5Cupz1bfWoxM727TVtVgf1O5eP9dAxFVD7VhoM0epupSB-tQz4cMl3g9UCUvEShMhZWPNb6_rrRTyao5zWGeml-IKcvO3BeSJgSc_Bb1XkU0WJmGDuHteraUheUyGSSHTnvVd6XTmRDxo3tKhfmJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=jH6pBJXW_C8NFoFmC0MgnRcDatqLOqGNcFRrpG1R74eJtfZ--ZHD-oJO1yieGa2DK3z-wuqb6dfOdTyKdUDiF6QEFV3_SIr95HlLt2K0-PQARFk60EAVSlz0txwmkRh3OKXfH7fYy-BoWFhFcIN2mghkpB5VMU0LF0QdFxpIpRN5lio89GabIgsiSZ95ydpPs5Cupz1bfWoxM727TVtVgf1O5eP9dAxFVD7VhoM0epupSB-tQz4cMl3g9UCUvEShMhZWPNb6_rrRTyao5zWGeml-IKcvO3BeSJgSc_Bb1XkU0WJmGDuHteraUheUyGSSHTnvVd6XTmRDxo3tKhfmJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um0o9jzw8eOYO4XtLLb_rK6Gj2Ds2pwrlBWB6TNohaKN0GSj7hmjFI1NNQ7RehTzNn42fn_hrej8s7fl3iSEnUqyCD4JnjKpYBIH8L5fbVeS3yxss1LbXLNgnX65VKtxPjMHcgVJk7ouZB0ZreyVMdI-2ezuKwZHxKifg0Ym-wFMn2mYWgBuP02kHbaqVdhmwHj_nfQx2g8J1fgj_N2YUgy9HUGX5jmj3_frhEQpZxNcnJaRaF2VSbkkn_k0xMerwqJZDieb-DPLedr1yoLkO9rmeObkyvi8QvllvI-pxt5ALkDvt1aoKb1kdxsXCJIWCYQrzSpjTEyz9LQlMEo37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJxR_sgxCPNpnrSuCqpIqVcdngrunTwAvmq7t_B5A2VA7JcEYx5JNsWAyAqkHh4rAltVIpyYTaUaTZgGvuV9rcziKIE_lxFIefE6-to3WRrnXZ2lZnbeu2E5dYNI01lba-9q-drMdnvGnaZyDFODCd9umqL0gjNs1-H2njPCrmNLDeJG_Rl3RSyJ9z4bcDnHJWMbXuEWcK7RLVCmWsMjo3dBxZbpDM2LhHa14lY3xkp8jrQLgFJU8GRlxsDhOBz8qgqbdxf9BAPuCyqFfGQPkCi9Uq7gUfXHpjcd7dKn8Wb--kE6yT5Z3EWurmK4ylo-SZT1dhaGvV63RyuK3YrDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2vXxGmzNhBCSb0TOnVjtPXTftsCnXsrrXUT9x-QS6dShB1V5YxKQfvHhW4gUKEMuJkBXmPwPSf2uVIVLqKALbt5zwCX64ozXX8hyNmD5lVp8P-zP6TILcjAdMKHrGdhpfPjEXvS_xLJJm75sTfPUpQu9EK31sCh-bevdsA4O86zAkFlPhSzbK5Dj9_9bAaP-l_r5T4eQaJN4on_sNArYiHmSaZI8HXqW9obkO6ESqsdLC_Y-YhfjnTPvALoaBoxODjsF7jjMEt7DsnR0b1hKB615Ob1mZVMwLRlc7mbjAMkyo2G3h1Z_JH8Ons9ZZQbXAsVkw3OMMU47qXC3A-Aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UslMx1E-4_28bwmTKogVp2JX6VAoXg8OviNWsCm11Pie2trz7A6Dcps18sRNRadTj7Vy7T2wZXWMUshuNmoxZWlzTrNFMkKhbTmCyYiMrWdOc2mq4ur_92X5EPOeZe_QFJoR64nBRZ9mMTc1uhvvZewMuVB-o-LrUZct_QaB-sCHk3bHPFAaXXhF4CncnFi1iHGFSCSUjHEx3_9RMDf_WCCNEMw11W1IeFpBJNV9BQeaRZAnpDU8GONg9_6OfE-HWpOOAcGbvMFL-7htpBlWyCs6YhL-5cfdd8LFzhbXu95hwHbzCtSyWZIRaqIg0cwd-u-93SDvl7twsy7LXBtfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=GnXukwa1zfMeBi2oNkYnLb76v2SFgQYLKzS7T7H1k54LEkXsklxaSEaDctKRXj7toLqF5ujlfvJIyTMlomWvzK49ywXnNTsBYgnGtOeIbBYrP6GynWs6asNeUakROzZraKVVJpMvx0L03QW35ShRlrgYTOyXnWL_seHWtBw6oKXy9iETkpr9l4WmgEakc5gb4fKG-h0ltLZSgkT0Qmm8CLrlZXjnGDZXNWHJS06nd_QgUu1HAnSfaTWjpwwT42v9_gOAkjAOKf5jNMzDr8EY4Hla5ff9Y7OyQ0cI2eD4GhuQFaNWA0R93iFsnRFH_XQHjZF3OoIlz-xR1i7p2GP1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=GnXukwa1zfMeBi2oNkYnLb76v2SFgQYLKzS7T7H1k54LEkXsklxaSEaDctKRXj7toLqF5ujlfvJIyTMlomWvzK49ywXnNTsBYgnGtOeIbBYrP6GynWs6asNeUakROzZraKVVJpMvx0L03QW35ShRlrgYTOyXnWL_seHWtBw6oKXy9iETkpr9l4WmgEakc5gb4fKG-h0ltLZSgkT0Qmm8CLrlZXjnGDZXNWHJS06nd_QgUu1HAnSfaTWjpwwT42v9_gOAkjAOKf5jNMzDr8EY4Hla5ff9Y7OyQ0cI2eD4GhuQFaNWA0R93iFsnRFH_XQHjZF3OoIlz-xR1i7p2GP1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE73I94mkKUAEquFB7QZSmiJi1v_tF_5IZ6Zn8Zhosy8ECrp3O93VfmeNTZ3NT0DJ-pK9_S0XbK3D1ImZ7cj5R_9CzAECk8AdtzrbyK8Uy1GZkEfPvaKOTKK2GYovfFD9pw0NqDm11bFPQB9ljQ6N9tshRH7RTwHZEb9Tg0ZShJ4TY4PLep2Aqlp6p8Fv_DQom4PGBHaBEd81LqohcdlutgRuU7bj34dMlBVkiYo6e6EL6NImOUQpojQuzMAKfQQ-xbscqE-GV_I_tqK5PRww-fACV1R7pazHnF_YPuoJ7JVpNxAyKPLQ4a8P2FBnKlno5DbHSLDFa4SajB98hRjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=TRD-8CqG6LYbQFTQHpJMFWrRnkMWKrCSKLrgyS5FxSlig-OmrWU6Ot9DGygTUUxKC5Uk-lH7gug3ZddtTPdFv20op1olEfsrWIBxDU9LKNJfuV9WGelAksrEA_ZjzNcs0K9XJ7NDEaL6E-NHR0KTbyaJowtwY7DqSIpUwLHC9wgNcbTOOhtvqg4-e3bdRqphkakOmXPAEKWpjdua4E1K-iTlebY_jSf6C5KFyTNhEpJDeaHXxsLNvEtxouyZLowTSBZXh3Q2epIFWFfoXwoyG2W1Dyzn5cyO54rfzl_9I0powWmOjsL-wDi0Mm8m_jr1NU1DrToOtAATzw10hqUKOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=TRD-8CqG6LYbQFTQHpJMFWrRnkMWKrCSKLrgyS5FxSlig-OmrWU6Ot9DGygTUUxKC5Uk-lH7gug3ZddtTPdFv20op1olEfsrWIBxDU9LKNJfuV9WGelAksrEA_ZjzNcs0K9XJ7NDEaL6E-NHR0KTbyaJowtwY7DqSIpUwLHC9wgNcbTOOhtvqg4-e3bdRqphkakOmXPAEKWpjdua4E1K-iTlebY_jSf6C5KFyTNhEpJDeaHXxsLNvEtxouyZLowTSBZXh3Q2epIFWFfoXwoyG2W1Dyzn5cyO54rfzl_9I0powWmOjsL-wDi0Mm8m_jr1NU1DrToOtAATzw10hqUKOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCI1FixILmgK5yYjhxzrWi_RZb31_2v6GlGVDDb3-MJpwQNNC0IyXXoZ7W1dUppmiPfRTYZt_apaCRJIHar-YkG35_4PBhNOad6tyhqTbG7UH8xpGorKqzB3LInStcOZLLeqhFrAYWSj6iutj0Pa0LcLJIUHoz2JgHeGvLsv5t6aefZsrXNccfAaD5cd2WRkEDJYKt0FPiv-Xfsq14ooRujnDMN0S3Q7I2a50nl9MH0R6fClAZ8EJw5c3cIA1oiXGyrrYYTKw-SKRKTS-Y0vS-6wsvXvz00sgGyVHdZPRcZ4tlfN6rvqLIpLjp5xuGrngpoWeCb5QQzrf-xOWprJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRcW1NrL-wgC7-hzNisBqKSIFUheEEMlhFI9_GG8CuotCEyCZemT_DEBk01chocIYTOlZArRr3d-WPZJptPbVsHb1PUaLtzLydQZf6SGOiuHuQ_SYhbKSH8o1YBgdazoo_XGqwrRzPTEv3RkXCgPj3DZ-Mdd23-eW0YzFs_kR2BtkqdkzGZv29FgVy8Pt8bjKQ3ueyCs7gSgNXRI_DzqR9akNfnqGt-g4TYiOiTsAT9HvTGpLrlwPNUfOmyyfTy3EH3cZlcQ4VJ_QCMddv8mxAY30TrwIxvz_9EoXvlN2PKQ-OkaTUcNIE6moBB5uQmKc2HgI4FXykcI0xQwmXIhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMyXylbT18NtWK_OrVAYHRDmi1IwZsQiS5MgbWdzHoymrRYZ5iMRdwXM0BMSDSPTtU5Y63MWI-u79giW8EV6nfWHRFvbpL6SuKz0Gl4WMFAoYln1-ZnLJY45XZEajN5QElhpczZ0NbZpib7yNq92lCQJ0ZU8QAVEPAv3eT2xWk0AhQhcHfR7bd_6zWwlh2KuEOffpQJXRIYncgrqgiFMzz3QUY4rn08hDx7MAX_L-aJepeUrLZAe7XBrQq1ZzIOg9ng5HtsQgfOEukn8UHkBjVfaa3xnbJBwPrG8yurZRxFIWqmCC5q5zGuZlVeCay5o_CdUw3SApZ3c9Du8rjmoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2p0kB2yo6MdkAN-SR0IbojxxwUoHLYa91KifQE6ei4eavH6SELxqmU3mjXz9afYSmjzeXYO8HjUsCRJuAStbilv2Q3mPZV9v_2nxekzuEwAriXcsqmsWgdAwGkCyaBc344xHsR1Y80DcNpY1L5pZwhrO4J00mVXJ8bzt1MnYzYnWmWGoSfQWAzAGttZjflBuxk0ji3FSmehlK3iL7ixoMnr4Ao1pjALiWgLvh9RZHa6RsAiNp3qDAjcmIaj0TobD7ga5lB3OTZjeX61vGvBGMXWB-6Iz74V2Y8F6eyDG9CCYG_6-FRea4RYAJJ-JuW2eBy3cbC5nvWKEq_9a5SRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_9QRQp11zZpLwNbO0vYVt1l8sZ2WdL8M8stuzTKTseT8zQhM-KjXHPdQ58HoTWTM_mApcrVdlRA7-Cdtjld89m8CeMVpktXCbUIBdJi6ZxgNnsxf_wCdXx9qQY_kb5j0Isuns0PZKFz5uVCIYiPpqgk0C_pJ-ZaOUL1Rr8YLkoZ2VnA6Dm6zK0luy8ArZ5ceVeEdKezxVxVIA9-Ru161AYOrkHFt3R2QheXxogT5ikpCr5zOv0qKp9d9XevPJ04CuhUCIfSNoQySJAm9a68zcSY9dOggp0Zj4mFRQEWZDV9TdMLL6AGPM_X8AJFrHiw-59_z2bWleKyvv3r_Sdwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=UOQDwiCHGnYwVZD69Wyyiz0JEGzdde4VRs97wzok67J-2Brrz1XbB68Hv_5-oG4TXUghnmiQxoycvQjjodiXm8rwOf0zpd9AHngOBXEoQi-Afx4CMMjbwFxwlSkqLmfJDGBfcUeMqmivNkxATVEzhhl2e01aGeS0-EvJkBMco44TW4aVRr9kgaPk6Bs76B5Ior83rgLEMv8vDMSmqsh58Yv2DBfT36xWuDktcn_ZSsv17QMQFS-3sWNyY_QzahXhe3UNflWGNu5rsOI-HVT-3NccnloOZTFnD_IkuW7j3UH15O_dYPPDlQsMGt_b1nVSJ5hgFcBJfNvb7z8eUeuw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=UOQDwiCHGnYwVZD69Wyyiz0JEGzdde4VRs97wzok67J-2Brrz1XbB68Hv_5-oG4TXUghnmiQxoycvQjjodiXm8rwOf0zpd9AHngOBXEoQi-Afx4CMMjbwFxwlSkqLmfJDGBfcUeMqmivNkxATVEzhhl2e01aGeS0-EvJkBMco44TW4aVRr9kgaPk6Bs76B5Ior83rgLEMv8vDMSmqsh58Yv2DBfT36xWuDktcn_ZSsv17QMQFS-3sWNyY_QzahXhe3UNflWGNu5rsOI-HVT-3NccnloOZTFnD_IkuW7j3UH15O_dYPPDlQsMGt_b1nVSJ5hgFcBJfNvb7z8eUeuw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3oNyr7hGb99apL0JEY7zitNAGwV8XnT5hlZZiZ7dIxygPjKFH6Hsrh6F-wDVAGl_1Vc-SPfLFlWP9OKYS-nWPWx8bxq-HYN3zvRIp18P8kBuSPPyZH8lTs21OeVlqQNv_23YAp4ygiDIByE28o5lX8HiCzK2vTxvNjdfnvZ84mmYKxvxgo42mmp29_h-VT8FOjX9idhfWq8bg7kbdouW27nl0qkPRYlNbtjf_28AO-lHIpVCA0To1E3VTgBT-RnMzMtl6nRtxefz1KQiVG023UA0hxmh77wwofY6uFnxK9iOUrUeuzHZx9BQbjITslik21_fzDKudmlPFl12d7GJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBzJsJHUywi7RDwQmGQuC_pXBhgOV7gzledumxnJ2EgBhU77JN0qtchHknE6gjAAk6fj0jisvlxryKJDfpSbpi5evZdPbszAQROnlo2LptleD6ozcSfXSagp-kjC0aN5VQg2XBMC6iztzYa1Ju1Tn04RGhLLFKvJ7ac6eP1ht6e7ozEAvhPrklmMCigvABx-aWFh1DZAQk22_ktu31hAqOtyCGGX3q8MkhUgyhIYdZKwHZsj_8Ue6GohglAafRCOH4FOlvLUAZf8QiIM8xFS8pGdZ897Dq6c1ULVharkSXD85PQ-F8FRtGpcb0gGVWfehZHwsyOfDslW4LFgjQDQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=KZISIzmQEiLo-7JDpO2HR5KD2gjNQHtNWF3Mqm4NZaLwFsC1dpQsqYVmi6rRhSh-ac0oDPwdQULp_Ht6u_EWJM9zdhueeFzE5tGSwi1VZB6ieY_LW5Ag5g9V9t4B2Xf7l0Uo4cccrZP8EXPNTRlBOGp36-jCfp-jgchyEHzOlFpO1Q6Z3Ify25_CumpiJxiyDvNUH5V51r9XSv6kPL-tefnWiTgX_veNSHQL-u-af_vhtUTFZTq9J7XKJPckQxQ-_v3EtEIsFDYrHe169b10oZH3SRb84ArJLf6WPkGE4k8jSCADIrv3uGKTy1S70U-qS7kv8YF7ua7VJIIBjaMr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=KZISIzmQEiLo-7JDpO2HR5KD2gjNQHtNWF3Mqm4NZaLwFsC1dpQsqYVmi6rRhSh-ac0oDPwdQULp_Ht6u_EWJM9zdhueeFzE5tGSwi1VZB6ieY_LW5Ag5g9V9t4B2Xf7l0Uo4cccrZP8EXPNTRlBOGp36-jCfp-jgchyEHzOlFpO1Q6Z3Ify25_CumpiJxiyDvNUH5V51r9XSv6kPL-tefnWiTgX_veNSHQL-u-af_vhtUTFZTq9J7XKJPckQxQ-_v3EtEIsFDYrHe169b10oZH3SRb84ArJLf6WPkGE4k8jSCADIrv3uGKTy1S70U-qS7kv8YF7ua7VJIIBjaMr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwotTzfqJy6UX_f0Spao7bSHXxf3g6ZtI4TkYU-6TaLXIdnqBhnuUhLS-XIbILJ1La1Tl-hhzrsVcEGqt65oeAP2pPOAGoZ1ryb-zvKKHEMkwdWz7cVeuphFpdLB_lHIenrEPx27xlq-Q_GSEAunlubajNzYrkKZRAZqTgsWdZukeHuRhWXyd7ldl5QmTDZaJnZHbQWn6rL4qvUO23HEnmqKvMBqu8sGuTxTYn1YMjTGZ5DawFvU78fJsbPtHGUIiC-5lMk-GKdUhOVkhJWU1Hfu0f5oWjxl78dCzrGa59bhmY-C3UAThNwikwQ-AknIRSy5h8MzJlknnCeosJ2HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm3Qut-Kzsq-u1CviDr-k68b5EAmskVxbdxu0rj9HQZvZoJTStBd_5YBysS-McLMjLsjDrEwBd7V_fB2CQbdvWlP2nG_sXL0Is54HohsZt2uKNBrzjaXPpQxXQdzYoTCJPUxQ03MmKGS2goXtgnDIb2UPwV9zzPOYiA1_Kt9D0XCtcjLScDQWeF8tF10YcEVLQTbnTtgjvuzCfQaGkpSOCeywURpnZk3YD_EkcN2vWH7qfWec7JRkfOldD6A52a9yoA3qr5SAEBGjnz2G3qfKZ3Qvjd0Ie8oSIEBIL0BUOhCFW6s0TLmDACOD9kZHryieuDPby435z66TPD43PbmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGlUhwfuBx6c485fwWSsHAr7WtiOTI2fCD7OoTr_iBPPZQsHFcpMicP3Ljg2b8Iu-88S5RqJJMcabA38GktSvmt76lj3rjaYwGr63P0PNxbr9s9zDoQiiZCslKuKJk5CvaDniIYK65nDwnx0ZYVdEBv2eW4Z3eeLNnVPrsgEta5lF29UD5dg2QUVdvLexUbR696X1iMM4FwfdE_M16mxpH7UsnDj-XMVdAayECh7_-cpkTj3vwHD-xSYrcvOUsHa72VIXbStaV2vfPYVVCwxRNebiiike0VUP9I6oVqUZ-NMW4VXGdhtRsWg5szFR8pWPJ56T3-zdqmVMkhoU4BtMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTf650O6ulZVDTLynNhmp3GzpauyxSNp2Pt1ofIHW8Vwhsxt3uQZrVKAGPHIU1I9n2MrBHJTKwAHgfvz5wkh_mzMvwke2hJKUvWdE8ueSKpNalr7nCdahQf8NGQ59S6CTYQG6Kmzj2y4I-e8uaE6dv04ABpxC0RG7Pp4woP5V9ncmcUoxBFYiOgoZYXx6_QLjp2qYISpbM5V39zaInmRuZ14LHOfBW9oGFVhJPtoL8ungzvf89qFlVJMi0fj-xeN_IsMjgxRocEyaAFyVnxJSr-2CTd6r9jydGZ0Ez9ClyUnz4_6rObXbj3Albg0BCutp9lvJRnn713zjL-L7ykWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgnzvqCz7UPWOeyKNoq5XmMnd0SVhyMwy-1sPpPk_gYZ8im7p813gGAqK4IThUmIpDna4fRJAuLbqDgVnOQY4RWfB6sxj95Kb7Ce0pOwUcIzs-KIvUQgOnRwMWcYKtKu_VgmpmmxkZPG7yNh6SjOR7heEyplS6snOKh2yxZfs0_-OKm6owFHim2hPM5Ge-AOtix5Uv71tM3qJPv3Vw-DzVwnuDhm5vzuqB5JJdeE9pKaLDscthodqWSptIWBIqQn5U5RAUP3W8VcwNdP5dycbkL-EcYyC-SLRtUPddkQzxVxksW14uZ2xf2CK-AmBMmSx1W8xv8-j7TuGc8y6vsftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr8LIbB3A2AWDcA4vbDUQwCW0a23dhC7ND49GoXUgTXttpILNGbOQYY1RWNVZ6tuzETj9Fq4s5Tc8yf1slbIhQbqAVFKT29shrF772nal8qkipSp3f1M3P7PFwaXTznkfmHKa9Um19N6cvZ_8L9ZOryy9jaXXx0YY0ZN6Hbm2f6dZeoBeYKJ--UErnw1t92VMw62bIZxR1dDrT1HpL-4kutegi7xdI5S7sfA6kuh3vIPRBlgpZ4NH8OMzBcbn6XJ0zlC8sdpczxSuBpO5TBBMFBm1fzABAvtHoy04owrO1Mjsbhd8WnmXjFxZ8kp0iXD7NEXoOhBXXS2UqX4dCmefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3MmQOMraQ-M-TM_uBG5okR-W5tPymS57Ofq1HdJozsXTimwsAqhjEPH996XjseUBFoMBhwiwNvzur4rQ2W33glrwHcyVs69T62Fwfs7rem1JGXKzzA1NKaz8Cdqxo1f3zfPYulxFD0o9u3DVzb9USYVreG04kQw421S5qeqag-WCyTeuDmDa_7j9emcF_cUSf1RQ91T8kEt-bZE0ZvVccNPnR1_R8g-EInnNWqG-TfGdgoL6plZYfkbiMG6-SgDbv0h6t1ggaIv8f59a7s3W24THEgpdbZde0MwyLGbrs4zplmPSvtF8Sg3acqL4uO1xDt3W6EDj5ZRklOthBpZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Itveo-pG48u02-y6mA-vcp2HwcPKBpFzbkG5Ue9hfC95vPApG2SRQspH2LNppdBl1-XM_tAiUJKeOAMbdrEwW5v9MqeVHu6tBwY7c1li6mfnnLFTwbp9_vxX9pjs-ECo0eUN6cR7a4HEWJLbYXG3dzAQtLRADmZv1tBNcl6OYy72pcJmhCHR-EGrOR5uJit8s4ImVnviSiZqkUG_-yeADwEo8GPbKux2W9sZSsgdaK5bci7QeEWeutoiS6i2PStbarAIbUy3DKk91hG_-dAfgLBvkFaQD9kN6suMn0tZqc3-glUCWTKIHiWiAUKv_dee56lsylx1na6NQRyEUnPMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyN3xECcfEUndGNknNB5iQooNDKKc_dyfF0ZgVuJn4G5Z9c2XSsUdHNC_Px0lhyfE0H4YtakPsLPfrtecKD07FNU3KJtwPzdqRf0IZBEflzuokYSCfMlJaeHL9KmnEFjxLP-VInlmUliYos5CsmpdEjn2PUNAxwqSpLUU8KJeTj4NiOW9SPIEV6oTffylgRo-t7b-pZMbgfH5CTZ7MRWatpGUnG-_l0IKU3aZHvSPAp6JCQVEPjArvDuhGh2gAl08Rspz5OWZx2MorsDV1gNO7-66j1bjt6QgMqsZ06-40qXl_uW7H7C8vV5zNtiZJ62FLfkwSukD1vadUo_nannSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il_nGnUqlOy53NSAbBR_VxpeDhJB4HBQjGryEjtNc7gp-dh7jzTOUxh954aZQCXjjTpm-whZSR2dee_BenDlqJwrdMqRUW5bpj7eBzjgyLBNsYkkVcMoqc-8CZa0uKc224OnPHNGvoCVyS7fhPX0PmhCQ4RoApGy-eh_6gj4EE7DFxUpQyh3ZvlqIix5TvbJHNWfJ8VODGzipESEzCJMWOoj4_qmXTTt5z6ubW-6AIRsSlggthSzyhRvnP2rfBP7id0THyCsFMT1VkSoW1FbepUdXKsBR7nr1V2Omd8Gi4y97RoiIO07Ts8viUpCP0CYnaJg2W9WSL5W06l2sE6STg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=IiFUkWdGjfqvOyNBtmu0r5iMtsH7rJGmk8OPdRglYV71I4yS-esLM1aJ9QXmKlnTZm6Z3wiF8R3AZl1ywnAD7nVhefXtUbmsS6UT-6_ryrJcew-OwQpD1ePpfeNe3_dipoCmw6HJPimPj0JUb-jRW95FXuh0I3fXlYRilfIGyJuSKBhDTU4IEFmsyjWV5ahSHQkyu3-IEObqzMKCThGXqFYpWGaQ7qzEO5zYV2ChCj9bgYC5OsdjOYEoONkzXMFUg5xQLO7nOHF4-ILAqNckqWUhh3tRV64T7pgFcwyooqVfgE0LryavyYXcDNZC5aaG-5z4OVx3eSf6LVE00omgAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=IiFUkWdGjfqvOyNBtmu0r5iMtsH7rJGmk8OPdRglYV71I4yS-esLM1aJ9QXmKlnTZm6Z3wiF8R3AZl1ywnAD7nVhefXtUbmsS6UT-6_ryrJcew-OwQpD1ePpfeNe3_dipoCmw6HJPimPj0JUb-jRW95FXuh0I3fXlYRilfIGyJuSKBhDTU4IEFmsyjWV5ahSHQkyu3-IEObqzMKCThGXqFYpWGaQ7qzEO5zYV2ChCj9bgYC5OsdjOYEoONkzXMFUg5xQLO7nOHF4-ILAqNckqWUhh3tRV64T7pgFcwyooqVfgE0LryavyYXcDNZC5aaG-5z4OVx3eSf6LVE00omgAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zgtc-U4_D3pBdCKxrxIyE5PAZqKvzspGNt-EBq1IK9KfFbaejhKkbFn1LSKtQTQi2IToCs1BcG2llnDeGyDqGkgTAT7bdFVmbEi_MoHAsBRYkCgj3alAmHuhngIAjaijGeBxi2Bo_3Rb7vQICXg0Ix6_rK77xAJiLavRsTuWDlpjrV70uMxnHSpGVkIZpYTAmNG7Sz4rRRS8qM5AQ1nm04ysYlryZLx3UPvBkmhtHDbH3rHVFOhsbAqUDPR265YElUgZrslRtsZGsJqrUbnYnqBRxKOoLN1ttkhu4WqcuXLLY6AY8Ki-ayF-KCHu4sDMuOfxsK98GkQMSor2VQCybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndkoXdik3eKI6LPcNUl-jfbGPQfV0iab9Bys4TstbfhC1qtfpgSx7QNdnqOUO2MgQZSqndKTW7VbOh7HndFIdZ-v1kUA6QBrZ-R8ZuPBGwgVfyRiYtVl-nORQdhTUYSObikLmHuVRo8Zk6iXepeRafPAj16RrkxE-WtnizvL7wJxbuv5syOWqwUD1OvgCyTBLHB67sMw2OucUZT7aGFayU0eOIc5ZD9eGikQgQdaMU2358daBHIrqEct9CITXvmO7pW5CbhW23Mif7LcVigBqO4BwN2CEPgXADrHlvqayW1LHWObSCM6qQBbCPnbeNDsXOVHXxVu4T7LlKN0MPxBpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1k0C1f_Q5ahblAF6sSZycJ7jNIspTiiMhoNbrxdc7addxoUzv2_mA0Zt2mafWLIcW5SBoqecuBxIK9lyCuCqeUbBYv8ZkickSTuwvIb-_8vO4AiC2CL0IrfAyjvR5cACYfhTLnlLu5zgb6tvmvoLdopvKcLU64BChiLu9iXOyTh3HqGx0_DE3zBCmGQT6gXXQ9wGqPJ_RV1Y9v4e_fOCc4iX6En1fi4BZJI87W-f-DwtnHvEqhx2qbram0P90-eijp4CBBhMpGA3Hk18_73RziygFsne03gXmN557Bf1IeA-0SBU2v2h7_pSB6x0fHgRmMCk2D8AQ8Gu2DEHRMmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHQKEJTuKMwy-Gc7fHIYmwgstXv2O6d8v1HNcKr1YRjLahrGek4Im_lZzE0l_Us352oNjcCmwKLMn-hV4BAw7vYw_N7wZAhL2-19xufg1Nc3EM1XX0vKJMPqrCplinmRSKukW8b7FOTkbG_uV9GUc5EUfFV_PZLenwuD8wMeFkRkhlLtWVmXq7-tKbHDxjIyEUUKkoaWvnZ5m6OhRCJ9_kbBrNXzyY2kqqlJ5cQ9aKiZzV90adjmgarCzjJ82Mt9eQNH45WXxew_599Lp9g8HGavtF8Z6oBe8N2C2-nzvwLKx8qnF-P-jtwY_rEUqmswJ9IGZ1_YA2tSFcHMsZOQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAO_4TgWPYr0BLg_PJIgj32cz9uD58_3pCNhRKUi69av79oU__kr7PZTRH1NIW6NkQdU8cJQmYXb3jKCXdzLuG5Rslz2aPCVJtCkuNfnwYdGSie0Nv8tvj7zWX0tFSCGPGJjh31CeiIziGS79i-AUQmvp8lLpAqWC2HD_HJvJBXztwAZBLE_OTDrBAK7Xs6SX5le8M2pj0CEyvtKxipDvOxSzq8bHXPpWduee1TasOyrszFJDthWLr-3BRNKhgeAXp2spE8sO-oNiTOYyhcX7AQ22gkJaCh5I-LrQiGFQs-YAXtLe-CzP3sohDb72WN9m5fZbYj2HHBMBtf4r2vSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAZWTTPYsyO3uH40CzUdCgyfeW8ZWgtwTGrLCM5CeFWgSvSi1j5ABT0CXCTZPtDUZTHy30GVFmnbU584YPhg_mi27q6avmpoHoE05-aK_3msKxcMryU3JyCBx-BITrAYg-3TSgkxBSYOHFkZLtCErjmgnLEIBmlJWNyLva3O463ilEMouZNZyEwEyU4U5_LCD6V9LgS_LXR1J53JCG_CBR2wO9AsYIPbjAAbXN9B6_ToekDFmbmhGWeSSllmfHBCtztGOyNor_2VAyV8T6JpWhggWIGKIfBJCimsaabRvrn5S7-dhJuKMo6_C1cMBEKcSSXRfzchH_nrXqJi11ekQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKhqzkSkBvvKYqtNtrGhznkYSKk_Mo421jwoH-ezJoZSxQKS6u30yjt_NEFse7hT1oB-HncxNJJwRN99fJALHXJ0GU44tKseNPywfwJz1UmkNkAz8YggWuv9cgz-1ChGC-rnCM_yy4ceYUMFQZqQYDP1O9YJRJGYSCzUWwbBYcpbcFTaspEp6ZIb8Y7nTfgjk0SWETOhLkbc_ebed_vKLzoPHfWisMqth5YvIDRvajjQNOxaXNFa0BtJJ9EHHjG2luHO2szal2k_tZKvjG9gaiPKYa27YliY8ffU0E6RSk-lrEjLXZoeCMSSc7rUTyrvCPhUKCRqzWwwxfFS329N2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=B6eJQgAI1jZ_LMI4C3SzhnGlu_WV6dXyqgQryuz8rilcrk5astJJTJbG5jhd8KDbNNJohr6lbKzHel8H7s7dlZH5MmduB3G1Vx6mlQmi8j8Y38vX5N6XZjDT9RSpC0xm_R0xxLw0eCPHrwOrNs8exVqNGpX27Ld7ZtQKtIsSS8L7Wj9vNKSmCL_sE0b8X2MjH8wHLcYTkVgY6HL1DprZUvuaf4nBOPhrzeLP2AvNxJCy-r0Gn9Tb0z8D1W2bCqGwXaLm886C1z12iDBDX2pXKARfpvkuAbLBWiBuZV5Htq-3e9FlZQt8Rpflcsxu-yiBJ2wBb4zF4uG2s8BuMcb8gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=B6eJQgAI1jZ_LMI4C3SzhnGlu_WV6dXyqgQryuz8rilcrk5astJJTJbG5jhd8KDbNNJohr6lbKzHel8H7s7dlZH5MmduB3G1Vx6mlQmi8j8Y38vX5N6XZjDT9RSpC0xm_R0xxLw0eCPHrwOrNs8exVqNGpX27Ld7ZtQKtIsSS8L7Wj9vNKSmCL_sE0b8X2MjH8wHLcYTkVgY6HL1DprZUvuaf4nBOPhrzeLP2AvNxJCy-r0Gn9Tb0z8D1W2bCqGwXaLm886C1z12iDBDX2pXKARfpvkuAbLBWiBuZV5Htq-3e9FlZQt8Rpflcsxu-yiBJ2wBb4zF4uG2s8BuMcb8gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQBAgtrt-ovcCgCIDAqzXtD4SVs6BadiPeOFKnZu7NJeBZtxgkHXIGOq5tlQiXSqweZlUCSxsdRpjrzRu6qyGi47m7V7uAhfIBiDfZNHHHUi6-UZTrbkmK0BsdL-4Z2AUABgSYcfR66SOxHSoAl6NNUvIt-8CixpPWwuhQ-WzLDQPZiRtXQCrjtPTqW_TUx7bVKnjEtizv-5EIgy-OtuQvGzLBDLDlK5hobqsnbikTdsYYEA2WQF4LYKfY91lbeGt6cCZStjSxChwHOcRid2ekZNxaWeXcYlSLlyTAqMeYWq3xIgu2FK_WqNEsEwlTQdqCyyAJsnwW2jkty7IN7-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csg16eBPlTn3B7aZmq2hW1t4GkIsAVXo7sAlB816mNeaJ-4khj39zOqToJOy3eUteOSPHPs2idRASjCtX6Y0KmhLcowXQannVar5gzOJQy4x0EiCfr__5dfZzgV6DAIj4xXiWzq1f1kOHe-sSAFnzkEZjRizW9D6T45CoIUhdHk9jipALEouh_kf21mMCAIvxRauM8Rq0jNhfmlWsFuYVqhRPx8eOZhSm4TxRSk2NHtmAHjYQbLb7370jvowmJSci7v2RBCOKR5MQAj15OgTr0-T8oMKwfez0zw8_J-bklbpw2-K28GCSLqU1D6_AcH3StOikSJSa4bGyItvSGvA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=u7kF4LcDAsTU_m4eRMH6wkR7mNByuF12xoAnJihtp5OR-whquyKVLF8B2AsOc7_HsHfKRi0nqYH1awcuf4GunAyUBGAK_gFe09jKAy3uCcL7C0QBspTBCrJNwU5U32JVcB8sH9euO6OyEqHWY5uy0SOniM2-cnOlPBDUiw0taWIASkoRd-tQKYzxS-lOfvEaeYljmX8dRrnpqJuUGgF_Uz4GUJmIjLS49cOvBVu_WAYZaKF-AExe0Gc8AJ28Xg7DJf7fyGcY_kHXp7kBMXc4YZtpm-dSSttnXmzhRZg7Dd-_azRszInMDTBF9coBdvhexmFigZ5WaJQF3DfUETrWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=u7kF4LcDAsTU_m4eRMH6wkR7mNByuF12xoAnJihtp5OR-whquyKVLF8B2AsOc7_HsHfKRi0nqYH1awcuf4GunAyUBGAK_gFe09jKAy3uCcL7C0QBspTBCrJNwU5U32JVcB8sH9euO6OyEqHWY5uy0SOniM2-cnOlPBDUiw0taWIASkoRd-tQKYzxS-lOfvEaeYljmX8dRrnpqJuUGgF_Uz4GUJmIjLS49cOvBVu_WAYZaKF-AExe0Gc8AJ28Xg7DJf7fyGcY_kHXp7kBMXc4YZtpm-dSSttnXmzhRZg7Dd-_azRszInMDTBF9coBdvhexmFigZ5WaJQF3DfUETrWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_3vrEMWhZjiDxWsX15ycxEuM6LvUovvDPdz68PbUo_RFr0UiMPygFQwTYkHoJQaP-npTmQBWQwbeqzjZIMWcq1RgomrkZw6rHBNwCbJ4uMQ76kkWZAmICtlULV39SVh8gE3QjKOk5IlXg9IHKrhgIn55wsuj83axa3rJL8pLWrGHIiFk0rAqygyVXQ2-A0xRJFUvqa9W7NxOpieEpgU_HxqNtNVdQlmUcvce1LM7nTgJZOreVWdDWP9OFY2O2qAJz0RGMRB7GPXeEjlqcx0PqLwtxRcPt1ShFLtZiu9bakffjdAKZAn_gxdP8bPAIgkM62quxbl-6_E95i8U26HmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go1S7cSp32wgiqBJ5UUg7-pdDlX1P3HKGcsvcASG2uC60k6bjSvoV7DeciawtgRO-IJBVigtPZxEA_M9YUDSZVzi7gOZyuGgT4njtswD4XeXM1FXwey8q-581rIOjz66lfY0tlLz8cMXVaTduGUSisC7Ux0SAmUy1MgaOxlCnMgUdKDsF5cIoNzlrRjmOGQSMEsTzh-TGQAyMjyhsYQW_KjAw2RZvVo0GmZq6RvnpJFHiG1lFk_H6zqiXu_Z75UmD-z3qjrMFPw3VN8XY_ZSIJsKzw0OJ9MZ5QRI2mViGCNbS1S0W8wxfA1Y3TSx_55hinGDLFDlK73f4S1kGJnDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8F10XO0sPNZiNCso7HbsdlEqBnBVTxdjLSy-MmXGGBzDQLuV1vXzvi5Bnzz1OfV7HcmTMDzOO-jwKfAZOTCfc5Do3mxLOMFqBD_U9HsqtIEofpBw-yE8klCky1cAq-Oon07sPhPxxlGVko5o2QcCUgsVVO-yywNiaw2nfW48botbLcNqr6Pgnj09Jy4KXKbBz_xUFMZtUujsyU4dIw2YY4GLsOHbignLsyfmscPrctc2SGc1aQU4ge0JDUFo_p3hpJiDdLTTav3mabGUi0Z-uhxoVrFYuZfBAIdIB1iPbCgOcANL72zQ8Y2vPCiINtzx-Rs_jZvNXkM679w4IQaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2VceNPvzBQyoopieHiLGwUCV3fm19bB3cNaD_-ZyA3cgrzmAZgneTZAH6sKKWdlwuv5pMPMyynxDtxDbQzfuSe6dqiKLT6ZURRBuZDVKdUMBPr4M1UGa7qh4WftYingJNa7-YGYNQK7v3XrgJT_Uz9lJk3qDFCEqLEcPiXf3XOG1eZEtbVujqja1DzAJSdO69t8vq-VQObQWmCg8HgQLQIt7x9hBTFUhwuihXoCx271F31CDCO6FzccFTcugMu86YbhTLaA7qmql6-PTc9U9sJlmM_zAd_TTrcenqot0_ahM7lZc3BnZYbZKT1QubQZZ9gJI932mEJ1zPcsYHDypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=PNHuc7GYaiy7zhVlqO3UkENdmP_U6S7r7TssraQzjaA7julwxlqMz0Fpa039Do12bk-D3Zr6HZaIbLy9VwrXv15oiWyaxU1P-wrhQZW8cyELFnkvAeD29qRQgFcgzCCV37kFKOOuwLc5NNq1CCagWA8QENbDHBd5ooQaz3Kb-menHdYHfXPAiFi-LkrOCGE3F_BVwwLhwJ6B7yXR6bdstIzOgbwtOfzqkX92eL6_Acp9YQhTBcFT5SqLX6uhs30e1YEO_mLB_PL6J5znsBmVNziIuw3DkxFh3g89kDEfZwfUdxGwIuZawgUMYE6Y5y8jXXc2rEEWZ2bt9tFedyo0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=PNHuc7GYaiy7zhVlqO3UkENdmP_U6S7r7TssraQzjaA7julwxlqMz0Fpa039Do12bk-D3Zr6HZaIbLy9VwrXv15oiWyaxU1P-wrhQZW8cyELFnkvAeD29qRQgFcgzCCV37kFKOOuwLc5NNq1CCagWA8QENbDHBd5ooQaz3Kb-menHdYHfXPAiFi-LkrOCGE3F_BVwwLhwJ6B7yXR6bdstIzOgbwtOfzqkX92eL6_Acp9YQhTBcFT5SqLX6uhs30e1YEO_mLB_PL6J5znsBmVNziIuw3DkxFh3g89kDEfZwfUdxGwIuZawgUMYE6Y5y8jXXc2rEEWZ2bt9tFedyo0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1QpUpOL2tzXsJS93nTytvHcBuIlbKHIqfjXxMbYWiqjuUoH3VToIg9OWzYvSZFmVD7pRF--pZ0_U5Te3Xg09pxsAJrSxBAzLvKRnvsyLD5Ap0MdAbHUpUu2JjLP9oVPw_STGKpTZGDZRfratUhFvQKd8WtEaAV_AfOQm0pJ6f8DS7J42spL9m7UgHKC-js9aGo0WWx0ZPEQvoMPa4W2SULNuMqA2JaEMgktqZ_ifJr026kt9-yt53-OR5XKqgnEBf8CKlGWK2iZWo5yIKcN1pvOed0hk0AMrjsQF1BkvDtPKWMG_QNuoG6BS6bApdHnYqEbtKb4ymnD9jBUkkQeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/przbxBloxGnWI2dgiIwjfQ8g-m1CKCf7BB5GV-kQCT7bCCI2t7oTj2PlxEMehAPqqBfA2f1sJB0NNzfe9MKk1RnTfX1dRM4WKaeiTfad3W3X9AyBSOW9jLU5B8prS4ztD2LoSuScWFRXWgvQqiGGHsQf78lejzehB7jJNy-Uyo1344CSuspSbFGgM6TSLY43_xIu68T9RU1eeE69J06ouD1plPyMM-_uNcyEZCCFk_qE_VzNlcVo92DDLfVi6YmKgN544P3DsdWCe_GguxgQJ0dItoHB_viiWmDj_iWe2KFk-qIVjAJJOKzZFGaN83c6l8EpotOwkM5WWRBSlg1lzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqqWZxtmjB16lG6NBX2QHgVLrgo3nKzpJUTGPonpbOoSnaj-Z9fZdBr9vUDSoG-7V3rd2fV3j4jSB0Bkd2CBgNZstTM42ws1sOtfckcFEP5EwrQptdZ9CNXpQ5Vg9jnP2OtTW2ct5p69F7bj7r92yrZu38ueFnSdSRG5SvkWTE8zHNT7cGkwvKcRsyueMd6BwPLSrestgsGXd6Wl8hlaDHy7TK0mj96Am7CtNF0vmtBDFFdDHjDJNmUsu6MoWFbGqFCrAptc-8s7Lwi05gddBrMyEyNW61tH_Ikfa1elw59_-xRWc0YqT2OYoFFOV9WWJR9dF0wQEA434H53r_iLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT2S3kTBsBAiu7xtMNHacQYe4YulwxEOxzg8Ogbi1f61vR_p7PIWlHVShSeAI4sD4_LwJtrtBVBO8mSx97rwAwTffjeCRq5I3Dc6j9USoB7uF4KBvIwrkJOfzswE16xDicoSF45QiESxFfNBCpF3leKK4mYYjs6U7Gi0RUlKaw2iEPBFPTIcU3J1s_jn4kU_aq9PmEVfOtrIN65rFfkPrefw3B31Vx6e6SJpvY61DNEwtBwWjPmNL7xBXbjB-s5RZEWdhNZWcYZFbekAho4aePRJsR4Ei5cnizJNvbNA7I1KlNnT4d_eRd1tTPdXRtSr31oBfiPedJkr_SrkuTdhyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCPzPT3GVqNOvhWKclTEfkXz1WpiTHYGP7FNFz6Ny_tDxaGixQjUQ46NLBT7Gcq0NTU0ROMci3fyNk1jGul8LJTU8Jk9YDcKYgP_J3lgmifjxMSea7lKgGNGmmkzNxgGWcdUSDktl7sue2iQbu3aNwHWrb5U9wbRwwQYMPVuj9E5t20YPHrJpurvIZpIScTGdrQwK7ytVhGsAdNNpPbRqxDzf7EkAM9HJuKrdb_6phguvS7bmWJdIFWRX_BD7RVVtbbvuY8rANTifw-TAmjiM7RCsgBcDwuluo-HR9upMny9tyxxhxchv1CKQMXZz1mBj_zhVOKjfLcAaRvjD4irgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKxJSPPMv3s-R1Wld9qY_6Fb0L1Jx687_1oTHxTm4qn_3jsqqWZZtqFZ9Mc3wMz22CycyvD0wbraR1vXPi72xa5u0A1WJDqK-eEWpu9CkwlU3J89rwy7a_wi9k0b0PCyqSLam1KEnaNtxPiF620QhqyDlx8ugjI2h7zfTyARQpUgsuGDjHZHowYikEy41A5APwTC_s9r2iuW1p16jRnnCf5aPcwUUnx-p_h7c-Ksq0RnSpXy5rN-YJlr5c_hhpaA1UU25zIH7gj7Endd4w8yRnzIDZONXl_oQM3FlUyR5XHXdwfnS_PADJ-fiwpTv3z_XLUApmdNvVImcLVloUF1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1DKH56flXzTuKgl5vjFIqmgyn9xNiJ7aVnPDGLXc_kWlUimQB5M12LWwfQOBrDfnQi99LjcRZwBu-sJUoZ-FS_UHxanc4D4Mt0VV1-tX_a5SPnJcpIay3L5adTbgXxDmj-wffLZOGO5Uo5DifXKl9k772kIK21A2XrO3wRa3Vowh30maPgpOYqIjPYQHUuc4b33b8bUx8a76d5mQYTygoeJQTuo7EyhQzymXOy8TylkarnmBb51RWp5hURTIigdQbrqp1dWbI1LLUzJiQterNs-JLXTdNQsQ467EItuusdk9uheYrDo-OPrvptaCSy8QP5goYZLrr1xnxFaWXGtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auO07LLhlfAEsuNBdFCRJfFsbomBZwtGQtkD870weQYMoYxlerx4_XPXqI9UPpzwEvigYE5nAu7XFPxQUSuqs6wLUtNhIVSyP1eZrgM3bk7TRjPfLpK3TzGrl10icZeYva51qQfld4z3f3TIJsB9lFLzMiFDg0ucDA1E0EnE7Uj-Kj3X60TVygyXPPfGQTQLHeiuCiwzuWo2rVNPOjX474jE3ei8MgzZoeaW9OKYJtpddnbeN-7QqjVjkLkMiSwDgL9KUniJQYOxZ4KigUegqAxFNqu4TA9KXu40iVkQxKP8kJ1DLp1Lf01zCsHfKHvgMW0fZAlsRqlkos2eqPTPxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCc9gxi0BKwjfWBl0H28ph0fSBTiXxz811Zo4zbByQInYaZgkofh6SPxPne8sf37oQZTJkeX_vou0LuhCdn2Fs4CZnkeDz3OpgBjhPneWv2RcKXA1KKtLqM9yMzsW2A5CBuYCFM6Pel5wqNvsbd46TS9xg8fZ_HnCrot8m6JjfE_1MTKygj9gF8MSuQSajxh3t1IQ6tgIw9N8FtGLa-bL_gV8wxScrE2B2b9Peiab4K7Ul8vQPPA0UXgNlyKhmFX9bLGwtjI-dT_cpuyHcfrNjjOWaAgyteaVBMO-Qm4TTcEL6jsddrddGZoqhEAL9kHooBL3b1m267l2hVVCHCUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RV0oFAW_iwNyDpLA0CK5BJlsvzgTQMjJFLn4Bh0zZYXWIe79Q4fXKyaXlK9aYpJZoh_yEMseed9XRI6-atUrlv789CVHKoUZcwTSffDsZV6ExAtHJ-sLGXYYt7mMB6sA15hhpf-6sInDA0i5CVrvMAAfuLEZ3hhDDHGGUCRDTHbldHHWs3Rkt3uuixLyCEIhl0u1rzEU7HTKVRX5IMIrboqABNxYKW-L6_2zuYpwo3_rVHYg9aCn2liuHa7qs_x5gWQ1P0KSOf_toB-T_qvVcMTEy72OV4drqx-1HgCaGaKmHACacSIaeSRMNvuonqshovnSrmKoMi_Hu_oIQfqKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH7aWa7yR-8sUuZ9zd1yots42YgIcpWq0u-gRsINZ1RKMPn03HP-IhFvRKtBnYIlsovshPuv-9LUgESZYFF0D2rNBPry_6xFBWkV1LXKYOkgBoLWJccL856QDAD4vAhQADWn50cMKfdHficAHxb7_9_J80kBU4G998xD3dMmIu4CMaSf_ZjIe5IxsH61hxm9OyK2-6fztaBgtblDauoMva1bC2CzVBqoUWcGhrNQee9euje-BSMkFhyqlAe3SbYGBs8XHDazZMEwB-pO2r1BwmabsQM-YjJN-WKkBCRC7xeqoymJMT7zY6RIr8v67JvEWIvR8NkJNgp604ethwpptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgO73Elx6_BSCFz4XdMGFGcoOL1Ugjre03vs0Klrgi-x54Tf__5oq0xipl-2Bi3T5MgG8id6FCCJ3Vmo7s9zQnhued4mZw9AGrSkOWBPzr_v3mGcpweANyHZjiYhaXzqVN4rb1HA5UypsjcYG8HuLVOqt24KoIi403VTUxAaT55-B2sqSb77W4NNBmynb1ofSXMqy3-ibJ5aIKv26UdfcfcrtLGtGxv8aop1cesXVRPFwOGNIrTqxwzxkyRnrq8IPGedccmebkBuFVBd3ewfFU865iki5Y-kqrGFA9YkKiSlalAMUgJN76LV-a_5mCh5uwYvK-OhyWYFCXYuWSriqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb6O3cCAmXkqzzNIhelYzgzcC9XQiQF_XB7Z1Aqh1prcxBY9Iy_CI_a61mK-EmNUuU4egR3QdrZKU_Fv0t-x1FMDRfhSRmoL8SJYhnq_1ytEJAwvZ2gMshUb3DuYYbMjEthgduc-Wn7PkyqXVThELJuBe7S8RW_SFVk8mRxJLYDzdJ4R5xcMkeoAcj51QI8TyTUcHdG5JwClZ6KWt8XfvqDBKiEoTZF6LZ0MGhku75mVo7mKgOOynNRpG0mcxsRJ9ofIWK2HQ9nY3Pv34nx9WaozeiixFiXSjwddUGXNwm3opBvyFtmfoDiD9uAp642PbLy-x_zFGcPVv3v47_T2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tibK5FWzZQLFLpRulpMWrytGPcwJXfzC7JGVPScvGXtDz3OCnVL6tt4JGRYqmOPypSy5tw18u7RJeNuNuXR-pyYB4yildrnUkQ3Y9JDi4_i8lXBrbx7eDsqUTGSxFMbqfkBLAzd1n7fsi14S9mYj7jriIvjBU7cHkPCyGRbBr796cSLHnLiKBJIDvT3I-meIri6ZBKQPn3VBVU3hC6yIy6wEeSLDTE_FUdqwIDu1M_ZQMlXtoshDa-2UlCpF_w_-o6g3HNpe4BEx093KxKhWU3s_v6fzt-bujl7VoxDFCuCGqGSW1j2xM3RKRwRXWJJzj4nRGq9YEGUEXgnBRMeq1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0JnwmBblqrK62MCdPzhhO9lGVent7vEJDN2cflj5LEprXaCC3PuxeFlRuoBh9-X8_lvF_UvbJr-kZRJNsIz5uzRssnOkezhUW0QONA-vhEQeDoW6eaLDkuiJgQLnaLpupb7hoFjeqdohartiiyso8UOmDUAYgR2EHMPVIHY_c5Rc3jQfBNe6wMfSI5qfTFZlLJOc3NP8EPV0VSfIwG-DkjnNPk4IP7FVjjb-LVfIaWU_fTbuT4Tbeugs_AFMEWdtcfT3qIjfTbxeZtgeJGEH8KUVT_lUClXGa5MURwx6daAWy5LzGz4i_mPsOb0NxBDQh3c6sUApiD6qqpSfsxrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFs3Bd0kojFqJfDH2ReKsrF3ebM5pRWbLGqM54gNd-sa9KZCHSrUz-JSRIjHg7EzO7IHYTGbgIJH7byDF5gfIMQ1b0tU8J-chD_6jHrhWRhM3JyFT14CSFuPDgiNhD7uTn5QieefxiHHKrA_cq31CvD92ucboLESI_ZYhsmFRPhwr0ve7QTVP_J_E4sygG64NjTPwrNiB97cqOP7EQVGLNepCnTsLRev03HuNCcG1xgFpvJyyyk475cCyFLoyz59YtH_FkATSk10-AFy1ZNcHdiW8iKGhfbvXi8jU7ooUU7FW4Wq1jAZqIC1ckHjd2oXn13DRRfa2hyCw8EzNNjlTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsxr45nXvstgXARtz8w7mkPSDEdlY5aqAm28cnV-q0OJC8WBkQ7NZDEW0zKL-NaWg8i131J8baECqJk9pKNV61qq-NL_w7T0hdwLBea0XeEklYFzqJdr89xRbLq65xkI5dz6N9r0gUOpJQA3-CEw-gy3UPVTCykR3zggy7p3PYDUaKLFe2qSfd7HyC9afWpdsABD0iH-fFDX27S2KZ_4W7P6qnza77U0KK39_mW_e3xmqZVu67DHsOVlkfjI7NLIAMuf8avgcUaJdGpN97I-acMNDf9bvsq2VqttMgNtQL4extmb_k31ERUcl8S_iPcZTJl6RHj5PM965yhDnTDBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJT93GG2o77w_QAar12FW-UGCKMVxuejhmjHmuxAGva7WY8JhFNfymUEVd6ucnei6B1TkBuxIrIOg_Hca9fGJtL0m01i1IxyhtJ3stangNwUD99Y9Z8LBYbU9i-UsCExrkhB-l0Gu---uXedSKkGaQZKrwKdk3TPoxqH0KnPFoNHK8LDBYdKUcRStsKX4aPDgQ43q2gN9P4i0QqXOIeB0A0rBlk9-ba9GQH8woBONWu0W2NHQEF-JxToI3OACyiSMQv8447AnAOiugEZYN1PHDEtQNj2uz_0AqwisNjnOzeftm25qoEFBI8Vbg8tkz55GZrynAFFzuTsrIS0KJqoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKmUmo3MuXzqGU5uJWxfv9WMJ3ov1n7UiPSQhIEvGO-TjqLSuVHvs3Ro_gpjh7tM1Qerf4xvH9xJheduAueKdt-v2m7oitOFIlslhfLoR1l5CMNrjqUl-PkQYh__Udi0ZkzgmGedldAJcS1yM4jT4HID1W81Vg268bwlpBGObIyCpasee26slMxxnn-T4fni8_S-y477zR1E24GtMOoSaB6iLCm9pRzEVAXEJcHnIMbCrqUdOb5RygdSSh-5hh2SE51WfTqyn-xD-h0rHLWus3tbIDoFotBLO75jPGUceG9JQ-v0wYRboxPQwTQZBXhQo3QcWjuBwBi0lVYCpvcAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpqyReIo3I52psGKhJrq-KwlSM4FwEny4t9KP82EWV2znv7F4pWm_RbKg_lvtdUFEgr9gwMNDRyvQz0ln2JvDqTfg2NwEb3eLUTkysj6OuudipJedDDe77uBefC2EIVJfT8F9TBq59QxenLDcCH3gmT0W2_Pw-Tz33ZtjQKPTqd1ttCxYLDpeC1wZzjW3LPUGGhftRR8laNPxPhILSpf8kQZO3kn0nCKnTAf9efXwjPfyKFUATICUtdQqO61zOLlOpf0wlbPXlCOiIjdrjjZXMkmOAt6Yxa7-_fmd8FIStVKCi9KYxcKJ_KnQPEiOPrrZTj116jvH7rHt5NGJWZLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPbnrr5rv5x9VYJQ4IsCcG8uLKlUtKMxaExEeCoYnoEtcQd-OycURFSD1StYR5fqSn6Df8cVxuLqKcBvSLUNZ6svhjDt6klg1qGRK1Yo_Z0Oh15deR8A1AVfs08yefyUSdXMylThlacDtKPVa45RXaDIBRsd2lk5EpMzh0WvB9FbZ7pMghMY4e5MiA2nz9Z6z2TVSi_q12eLYb5DRUcGXhA4APNcBeyHdVq8MpXSgitvJNodwJqwK-SlSeZBVSKRoQcoX7pAKpEGV508CIU2RrOC0RRWHcGWUnDdUuXEtGJLORIlg4Jbdw2_R8MCphddDcVPUk4NNDuy8WKWvPMsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmLX2lSvXfJ8wInLiqccOeqBEYbCaNV-f7ZvLX-jLALd69iCe4Gm3MIjUATNFo1eK0lepqDBZQ26yaPURmNaZJcHDOihd6n6HLrWKSnN_qDDOVPAvBwbj5W61bbosUYo6MNrhNF3TqzkcP51k51OQu9fcm-2XNy7rfMgbdNOjdhPKqsvr8fQiBT3kjizJzHjAd7oysh1Lpj75xGxtzTpy8IhR_ndafXBlHoLmd1-L_Delq3e_7xLlovPZ2Z98uikWe1k60652WMC7SYcM6lo2ICSGxXs05DQGDgCKGyRKv3xmK7cFaBqzFWGPwNwAJAaPGK55eR3hz2SE3UpLCmsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBDapoiiTKnYu-iSffKF-2bCqHB1zm085GiTJIhnHhXYiFbD_FsbL8Rdoh2s1Lq6xg-lJt3gx6s8KZqwwxocnDBZeOshJM56zNpapQHN07JAHatXKNb2PXmaPkwoYcGm3Z_nnZu9NTeSACyG6fuXyFEmomiBIZCFnIS4dgOPu44R2yWuIKAVWVi-EH33587LiLA3ujZLpvtBFtgcUgGbPxwRGStrDgHYFuwMaGrL8fhFU49c23K4hpxl3wfosEOYnhmo73K40cLW9oSvO0N7AQicS7ZS7P3CaYSoNe30i5adTKWV79znvc6NvRboIpx_TqL66xhv0eVphsrvC2K9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzO4M3ow4zxt7GrwAX5AMzcMeiSttDiyjeLR3QInmX4jSvBaqIU4AdaE2DTjI2ah0fyJNWZPMw63hBC84SQ7zOf7xCBUxwb-ldbtJMRyAeIVWkwgYRStm-1hi6CgbV7E7nlShD_N4Q6YobqUJ6zNEdyJmDhTn8BtO5OjiwBnAxjBm5-4P0XcTcZ2NfhKHm63cSMF8V9tEGv3gw6oZb2lonUc3sjZb3TQWvqLm_W0xyLFoI5OKqdLNPR0XhGFE2eqgjlbXTQCLtK9qCHDBljeUdf0zH7TPQ3YHBiauSQ5AEu7ieXVtYI09B69jjmJfFEy_mmI8ekh7r-oMd8ywEhDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
