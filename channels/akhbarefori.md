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
<img src="https://cdn4.telesco.pe/file/OaEZLafXy-CIBO_p8ktSRZ6anGhBcNNoXmZeA9oefFnC02loEluXwo2Q_0FQ2RJDOR9U60pGL4IuUSuG7ABH8kaGg6kUj63O0xVHXz0Zc2bLcMtGSDu8AnUMUOCfuNZHmmYGDaDraEqnr7Wc6yRJf8ws2WcUy1_Dec_xiPfZtBfwnrqHNvXuCzm89D6gqICNoDzSrLeLq1fqosAbLDwPLSbtbBr6SlAsQe8f6D16GOxCOIWQCjtEH36aiPHrTVljIeZRenkmrcgnk9srSTW0THMB5Qtr9y-MFtt7xkwog1ZKTjm1oRowYXgV1tlpbtxQRMPw4NFC91LWOlwXfChlhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 14:46:36</div>
<hr>

<div class="tg-post" id="msg-682532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZNHbWTtDUz6TBL4UIxB4zAfys0GYnlV-S5HIeDwf3qHfWWBZn6JQu9ndcvJNRUU0nBmloOzuwOREN5PtK8TsHhOX0JkV5s94rVA-N_xjYA1mk16AT3RgP01hKCC5OYq3HXTsLM3QLnl11zopzenq3vGZ7Bay5lyuHTozF8bb1TgxDjogBRzd-arlJgTS5Em0-zQD5kFBbSu6x0d7aLj9WK0jxuJYFbu2IR3lnMUD85pisAJn9BQ3AXQ4m3Q0w0Aeb8tRIYpZBuowDadSbfubZbJIyA-6bLPVkF-ZB0qjeGi3xOyq3h4DZ2G6pZ-k75ZvyAWIKHQ-mDYB94NQTLzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس کمیسیون امنیت ملی به فرانسه
🔹
دیشب وزیرخارجه فرانسه در اقدامی ددمنشانه از تصمیم خود برای اخراج دو دیپلمات ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/akhbarefori/682532" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMtJkjDbjittetz9r2frEvLg7vdJSNRVJsYQ-D6wM0XjkjCPUtyvgcxzURrJwpIIlVv1Sd9a9OLO0LhyY2xIvqhMnVmkuoJAmmFDGeOnrri2y27OUImFIyAn2Co5oHjAus9l3aPLEl1Ja0gVW-3qSXRfeXarX5Tybk3MlsUK9L3i5V3mzE4UnOYrPb5eTmsWdqlJ9Rv0NiYauOoC9ijT_LFhr7qxXW07ns19NfntkMoONcwv_fLqkqIpqxZMdeZXSlAJGqXspg7JiFNa9EOrI9WE2ujk04l_VU3sZiEBzeRfLGt4yZYJIvAzN4KH7owpIzzbHQ10alj_JLwDVXqrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: کاخ سفید همچنان در حال ارسال پیام به تهران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/akhbarefori/682531" target="_blank">📅 14:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای رویترز: جنگ منطقه، ژاپن را وادار کرده نفت عربستان را از مسیرهایی دو تا سه برابر طولانی‌تر منتقل کند
🔹
پالایشگر ژاپنی Idemitsu برای دورزدن ناامنی دریای سرخ و مسیرهای متاثر از جنگ، بخشی از نفت عربستان را از کانال سوئز و حتی دماغه امیدنیک منتقل می‌کند.
🔹
زمان حمل برخی محموله‌ها از حدود ۲۰ روز به ۵۰ تا ۶۰ روز رسیده و هزینه حمل افزایش یافته؛ نمونه‌ای دیگر از اثر مستقیم جنگ بر زنجیره تأمین آسیا./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/682530" target="_blank">📅 14:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682528">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b644451e1.mp4?token=oDK58xGTiK8RcaekNOrbvLg4b4xyXZn3V0EgyHB3PQeokqyxz90yw8oti-BN6uT1r8fF1EajbwZKZKwpK2huxJ9FgAePCM0VXK-dVCakrEAObjXqJb58R1sW7amFIFHM9fL8XNgmS8c_7xBOJmgLATw-TpJYZtqdQMep35YePD5RV0x3crEIeNXAeLUf9TVlXWVZEBRXxwa6LVrcASv41e0vdxSDU1szheUYotXsPkCMPmVB02-1796qSyZzZZxU-IOjLfueRxHSDb8UTUtzsEFk_FL9iIEhNqrBpmjZeXYSebwVKiqmLY-g0rdCGagdLCva5uMGr4-53JdnFwDTjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b644451e1.mp4?token=oDK58xGTiK8RcaekNOrbvLg4b4xyXZn3V0EgyHB3PQeokqyxz90yw8oti-BN6uT1r8fF1EajbwZKZKwpK2huxJ9FgAePCM0VXK-dVCakrEAObjXqJb58R1sW7amFIFHM9fL8XNgmS8c_7xBOJmgLATw-TpJYZtqdQMep35YePD5RV0x3crEIeNXAeLUf9TVlXWVZEBRXxwa6LVrcASv41e0vdxSDU1szheUYotXsPkCMPmVB02-1796qSyZzZZxU-IOjLfueRxHSDb8UTUtzsEFk_FL9iIEhNqrBpmjZeXYSebwVKiqmLY-g0rdCGagdLCva5uMGr4-53JdnFwDTjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استودلاگیل؛ شاهکار طبیعی ایسلند
🔹
دره استودلاگیل در ایسلند با ستون‌های عظیم بازالتی خود، یکی از شگفت‌انگیزترین مناظر طبیعی این کشور به‌شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/682528" target="_blank">📅 14:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90806f0a3.mp4?token=YY1fCGnpFRQ7_2Pp1B-hiSwFIV7wcKkTQ8w_ThywtmBen7iwOiqOrzyvfUt2TY6mJ77XWamA10kywL33x8OKzmnihT_dl53Jx4gxomal2hhaz2uxU3GKZwe7sfx9CIKUVA7LP_B5Ormg3v_QsezUqEvyvHJrm-cIRpzIT3PgJJiPPQmr2MYJWRnWMk1q-etYGZkNoT6idhKLLsxKmlTUsw_Vgf0YFuunB31py-OjeuZ5Dh05PqnxjtxeqKr8tlgS61OTHecAW3Gu9K8O_Z61nkzttg34GphuSj7oCSygChUV-nC_M4wbKey-LT2VXyfDgoalDwv1CsD-J1JLM8EjVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90806f0a3.mp4?token=YY1fCGnpFRQ7_2Pp1B-hiSwFIV7wcKkTQ8w_ThywtmBen7iwOiqOrzyvfUt2TY6mJ77XWamA10kywL33x8OKzmnihT_dl53Jx4gxomal2hhaz2uxU3GKZwe7sfx9CIKUVA7LP_B5Ormg3v_QsezUqEvyvHJrm-cIRpzIT3PgJJiPPQmr2MYJWRnWMk1q-etYGZkNoT6idhKLLsxKmlTUsw_Vgf0YFuunB31py-OjeuZ5Dh05PqnxjtxeqKr8tlgS61OTHecAW3Gu9K8O_Z61nkzttg34GphuSj7oCSygChUV-nC_M4wbKey-LT2VXyfDgoalDwv1CsD-J1JLM8EjVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل حملهٔ تروریستی به دادگستری بهبهان که عضو گروهک منافقین بود دستگیر شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682526" target="_blank">📅 14:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmUXvu2n-HNFALRtM2xpatAPycpjPYAibvtSXX8jSTmD9e3sNjP3pZxVGPDWVc5mu6ESgERTnDSfObDIyG2yvc3KGP4D4SiBkNPvvQfdQn8miUoI9w3s2Hu8LSVYLuqxeHGEABMyErM-iOVCcjCYkjB9EVJAZm3YOurphHW-MTHjfolqwXmOs0fWGCDoM7cnTt6IR5bAibeeSogOjY15Bqz3I6y-3HYpMSqo-rimnNSlTkBbsYyuuO6WQc-7Hpho1bsk14ku1Er4v7TXQ3F4bk5QFVkux6LF7LuQIFTxPGcYYomisUygC4LYJNuNPRTaC1RlDkpnUZS23HOJ9g-V8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDY5ipFYq0UmR9BIMObYD_eSBmcW5E13Uzs7LQkDAO_O18l6ezd6IpfzAlHaeaVWEL1XBrQMt1tOTaYSuHkV3aTEJWvxLduK1t6SQjJdkTsn97mYVe2ymNSgx0BX0dGDaYDv4A7WJN0jSmsTxhzzmPNj5h34N5TesiYqfnI5fNeOeFZLN4Uy5EBOuot0_4QhhFX7WkovxLSlUNYX94Di__QvE0TFtzkq4TgnHc1bryBqXqXSyXT_FoEe40hFLS96cS79asSKl2q4ec7SsbUHxqBdtJks3PrpustBEyw67LTYgrGd2KGnQFdOp9i43b7HPyckzsVVBaPiSV2_sTiyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfbr1i4NJzm09-OxP_MFMnV2AgjaXmfFn23SvVqT_59rbm8t27lrzxwj3RFXXJBLF5bVZQ9t79inVUFK7etpW2VVkt743mgNKAYkgLtZlNk3CcDnrCdNsQqHi14TglJ7WelqEQmotH7TIHrLyjGZDC3g0SW0JmLj5tvEeYNSZwC2Y4Pi9mHbb0gKXKXLD1INtxaczYL-RUXRxtS4T6JRhiCVYef6bXIBM-uT5h4Cwe9JLptd5F9anjz2KGpy5SDCNK_WXh1NOZrbXGiJQM973EK3dZvKeqWfiK0R8ewXjXLhwd6IFxKds4TVpeh_cAgATmuqp57F-POKBE-hOMQozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlDPPY59N1VzwjDhhifejbRvCUYHLbZQYDn7y8KBFF8hLkTQYN1uLTiUREeTqmudTURmZzOOJ6UD4Ma2wdJORrn8iotNJWgVuL78yAX05aCFnp4K7PlZxE6T75lSxjjeWNTnILzgxz0oUyyJJbPrXqtsgWTQbCpWGmvNpw09SxLZdvH1u75aiYc--pu7bjd3t-nr_i9Ycg1nXmJy7vLuONdc63DUx_179oPJ0LaQnSuRouzFzZ3hCkXR9MdNQO8YQa8Od3SNq6iFBBCyTZuOy7zg-2RRu-FsSZT6TvnPVFaNNFV9G0Khdaat9xlhJh-LmPvlig6RkFrPPjdJWTY56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s21rTIpr-9g5gag6FPTMfQAfFa9gzR2CI9q6sypTCzX9ru-KAAsbPldS61cU0J5P_5Qpx4yV8T45h319r3xHUzQLuSnxTfB__92IbD2qJRVXr3NFz2tnbntoGiSMLsdk6yLdtAHfSsLaXQJS5xCjmNbvtbbLEWN-8fBA09sdwmpHujxPSsVOT0MRbYbTL-wTUkxLZnhcJYOCjtPFyO7h3AgDEPXnA0pu3dh1gYImS3wGWKQrRg8yDNpMlcGlrpcj1Hg6EeVOYQPK9oJN3vIkehlR9cjiPyhr0HDxMs_V1EpVfEVID7SvhNtbIUW-U7XTv6Dqur1ppMVAQrwykdCdnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خیلی راحت ‌و آسون تی‌شرت‌هایی که دوست نداری رو تبدیل به شلوارک کن
🤩
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682521" target="_blank">📅 14:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
داربی استقلال و پرسپولیس ۱۱ شهریور از ساعت ۱۹:۳۰ در ورزشگاه نقش جهان برگزار خواهد شد.
🔹
سرنوشت ۱۳ صیاد بندرلنگه‌ای پس از یک هفته همچنان نامعلوم است.
🔹
فرمانده انتظامی اصفهان: در ۴ ماه نخست امسال، ۱۸ زن موتورسوار در حوادث رانندگی جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/682520" target="_blank">📅 14:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/682519" target="_blank">📅 13:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/682518" target="_blank">📅 13:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-voDZMLchGtLHZTzAVF7TfBkssSlSrmuLQ4boow2RXW89AINfYuE0PB1AvivER5NHMmCS9OrKERgadZFpIA-51x2wgDNR_OdB1OWedXxUNOmLNbCjpoQ9mE3m9GqHG1BS0GuAGo2sUnV7y2FC_Mhe6yy_I_mOa7hHgrlOo8w51ke8jNQD0DOl1gcbkGuDE8HA1x7NJLKpLtyB8zt5KgtIrbykusfAWt9q6pP5CbEe0v6tRc1NknLqBBWtsI7ipvJBDdLOI9mnCQ7O_nBarfUeO49KfT47myg8sqhgQkot-ZCroE_nokN_0eGdf3y8-l6eJPIWxP6egQZGVRjOaTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس کمیسیون امنیت ملی به فرانسه
🔹
دیشب وزیرخارجه فرانسه در اقدامی ددمنشانه از تصمیم خود برای اخراج دو دیپلمات ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/682517" target="_blank">📅 13:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682516">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtmFbKSTMd1O6lGVyMSCHbY_gx1uOjKxJma9QYm9IigOro4gle-Uxhaa7-nPdCoLY87QuMT3TUBkTSSyt9ZFnY5km4otm0nQuFmURRyzCHNWaLCX3ZRL1MAojYm1O-zVitiRaLaNJgT6-YEH7HLl3hx8rm3-_sW-Q2kIYPEXDZ2bHiYq_v8-T15SCsWGM4SSNXZABKptBH7Rm83cXa2o7veEgvd5C_PamTp9KKFqPQA5PXNuJPD7hRZ-jmO--RAI1edHz_cIcs4LRfT3ffVMIYRfP91wf7asVihjH8CiAuqd-ZYGoqHSfysMvJ0thN7GIuhZ1ZULHIRZfITIi7GdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غیبت ملانیا ترامپ از ترس ایران ۲۵ روزه شد!
وبسایت Wonderwall:
🔹
ملانیا ترامپ پس از انتشار ویدئویی که سرویس مخفی آمریکا آن را تهدیدآمیز و مرتبط با ایران اعلام کرده بود، ۲۵ روز است در انظار عمومی دیده نشده است.
🔹
مشاور او می‌گوید ملانیا آرام و قاطع است و این تهدیدها باعث عقب‌نشینی او از فعالیت‌هایش به‌عنوان بانوی اول آمریکا نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/682516" target="_blank">📅 13:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
عضو هیات رئیسه مجلس: واردات خودروهای کارکرده آزاد شد
🔹
واردات خودروهای نو و کارکرده ۳ تا ۵ سال ساخت با پیگیری‌های صورت گرفته، آزاد شد.
🔹
سقف واردات خودروی سواری در سال جاری به میزان ۲۰ هزار دستگاه تعیین شده است.
🔹
امکان استفاده از منشأ ارز سپرده خود یا دیگران باید در فرآیند واردات مورد توجه قرار گیرد تا متقاضیانی که منابع ارزی لازم را در اختیار دارند بتوانند بدون تحمیل فشار مضاعف بر منابع ارزی کشور نسبت به واردات خودرو اقدام کنند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/682514" target="_blank">📅 13:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: افزایش حملات دریایی ایران در تنگه هرمز
وال‌استریت ژورنال:
🔹
حملات ایران علیه کشتی‌ها در تنگه هرمز افزایش یافته و این اقدامات، آمریکا را تحت فشار قرار داده است.
🔹
واشنگتن تاکنون از واکنش نظامی گسترده خودداری کرده و تلاش کرده با فشار اقتصادی و اقدامات دریایی، بدون ورود به یک درگیری بزرگ‌تر با ایران مقابله کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/682513" target="_blank">📅 13:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d58320645c.mp4?token=LwGuwOC2KCVWHDFkWaiEoW_vwNuzkH0B_gqsfRpPDSPhb9hvPudz5xf32Gc_ZjtuFTq0hoFjE3yo-FQyruyuEmMrbmDdzwjDZaFDLXO9ia9CzAd4r_7C2CHBeiJL9VCa-OefnCCu0gmAsQINZsc6C-u-5sP01tMA0cKyviyTZStTBcnIxmmh0nOxdNTT4WNqrmobeaxLtD9ptYLB_Whye7x50py7_2MEbH5FU936G_O14X_J8zx_y7BZghbzcaTWLS87KbsvPpM5tJFbTaVeZ_Myvj1Zd8rc0e0lQ4y81jo6L7Z7qcr_xnsmqnp--RaiKF97QJvPyB3CxNLYL09pRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d58320645c.mp4?token=LwGuwOC2KCVWHDFkWaiEoW_vwNuzkH0B_gqsfRpPDSPhb9hvPudz5xf32Gc_ZjtuFTq0hoFjE3yo-FQyruyuEmMrbmDdzwjDZaFDLXO9ia9CzAd4r_7C2CHBeiJL9VCa-OefnCCu0gmAsQINZsc6C-u-5sP01tMA0cKyviyTZStTBcnIxmmh0nOxdNTT4WNqrmobeaxLtD9ptYLB_Whye7x50py7_2MEbH5FU936G_O14X_J8zx_y7BZghbzcaTWLS87KbsvPpM5tJFbTaVeZ_Myvj1Zd8rc0e0lQ4y81jo6L7Z7qcr_xnsmqnp--RaiKF97QJvPyB3CxNLYL09pRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش درست انجام کارها؛ مراقب ستون فقراتتان باشید تا سال‌ها بدون درد حرکت کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link‏</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/682512" target="_blank">📅 13:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682508">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس مجلس: مجلس در نامه‌ای به دولت آمادگی خود را برای اصلاح لایحه بودجه اعلام کرده است.
🔹
رئیس کمیسیون امور داخلی: جزئیات طرح مقابله با نفوذ بیگانگان هنوز در مجلس نهایی نشده است.
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۵ هزار واحدی به ۵ میلیون و ۹۵۲ هزار واحد رسید.
🔹
معاون سیاسی-نظامی ارتش روسیه: گسترش جنگ در خاورمیانه می‌تواند به نابودی اسرائیل منجر شود.
🔹
پروازهای فلای‌دبی و ایرعربیا بر فراز فضای هوایی ایران از سر گرفته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/682508" target="_blank">📅 12:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682507">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
جزئیات سهم «سوابق تحصیلی» در «کنکور» امسال
🔹
بر اساس مصوبات شورای عالی انقلاب فرهنگی و اعلام سازمان سنجش، در گروه‌های اصلی (ریاضی، تجربی و انسانی) سهم سوابق تحصیلی پایه دوازدهم حدود ۴۳ درصد با «تأثیر قطعی» و اما سهم پایه یازدهم (۶ درس نهایی) حدود ۱۷ درصد با «تأثیر مثبت» (یعنی فقط در صورتی اعمال می‌شود که به نفع داوطلب باشد و نتیجه را بهتر کند) است.
🔹
همچنین اگر داوطلبی در درسی سابقه نداشته باشد، نمره خام آن "صفر" در نظر گرفته و تراز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/682507" target="_blank">📅 12:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfe029831.mp4?token=JPN1JtI0OPCr2Kjio_-JlhVvtnk1mej9_kvRnhhMvQ_Exrckpf6My99_zlt48w8nNUzXtPCJfz0PuRTIhmgo7NWhk5Kl3WcAQLqj0SfaFzqArfeATmdrtZeFGj1glCL9bJe_D8_OY_CxphoeP11g-H9e4g5VfOANWTnUoODxh40M5s_Rgq5qagzFWYnASmz6S-xySA7CPnLAnRXqVJAlaaSNnNbQ55ip6s-EiGp9yzubMaI3ffHPtODSh6FeWgPZd3BD6Ol3AwFVxue-6gXbT-O9kI3hhVFMdDJW2eYXBrtPl0pQPBaIbMzfbe1MehMfIl1_e0DF7ESI4cFGUeKN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfe029831.mp4?token=JPN1JtI0OPCr2Kjio_-JlhVvtnk1mej9_kvRnhhMvQ_Exrckpf6My99_zlt48w8nNUzXtPCJfz0PuRTIhmgo7NWhk5Kl3WcAQLqj0SfaFzqArfeATmdrtZeFGj1glCL9bJe_D8_OY_CxphoeP11g-H9e4g5VfOANWTnUoODxh40M5s_Rgq5qagzFWYnASmz6S-xySA7CPnLAnRXqVJAlaaSNnNbQ55ip6s-EiGp9yzubMaI3ffHPtODSh6FeWgPZd3BD6Ol3AwFVxue-6gXbT-O9kI3hhVFMdDJW2eYXBrtPl0pQPBaIbMzfbe1MehMfIl1_e0DF7ESI4cFGUeKN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملیات نجات گنجشک
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/682506" target="_blank">📅 12:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6lWa8gsBgpi0aLvGIOl-yc-8ZrPIIs6KuJY8oPnYDkEzC8wlbpY86oHKyx9y51qP7ilBtow9ALhfnHB0fat7MNseGbc0DNp_c8JTL_mE8I7j72Cjuvtq7dbVn6YsNx2PSyDRQ3SUfYN9o3R69j_tjqYQ5fGzoZWOAvWKV5DVlZTGriPnIxzCDfGJgdXwVKEHzT-6flpUWcBav9M_x6DrsoBMyy-pfYRVYnIaY4-L8pFIxEtK_zcNCNAcWicIyheOfFCW1PNsQjGQ4xIQnYNDXNHfyRTWR4PdUlPEu-0CgBJdw7gVjc3Zdy8zv-CBTlRnFb3LywbN1XT8Jy4nKJ6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل رایتل:
#حجم‌خواری_اینترنت
خط قرمز ماست؛ در برابر آن مماشات نخواهیم کرد
🔹
مهدی فقیهی، مدیرعامل
#رایتل
، در واکنش به طرح گلایه «حجم‌خوری»
#بسته‌های_اینترنت
از سوی برخی کاربران گفت: با صراحت اعلام می‌کنیم که تا امروز هیچ موردی از حجم‌خواری و کسر عامدانه و غیرواقعی از بسته اینترنت مشترکان مشاهده و تأیید نشده است و اجازه نخواهیم داد چنین اتفاقی در رایتل رخ دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682505" target="_blank">📅 12:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای فرستادهٔ ترامپ در امور سوریه: دیروز یک قدم با درگیری ترکیه و اسرائیل فاصله داشتیم!
توماس باراک، نمایندهٔ ویژهٔ رئیس‌جمهور آمریکا در امور سوریه:
🔹
ما دیروز تنها یک قدم با رویارویی نظامی مستقیم میان ترکیه و اسرائیل فاصله داشتیم. حملهٔ هوایی اسرائیل به فرودگاه «ابوالظهور» در سوریه، زنگ خطری جدی برای شعله‌ورشدن یک درگیری نظامی مستقیم میان تل‌آویو و آنکارا محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/682504" target="_blank">📅 12:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خریداران چینی همچنان نفت ایران را می‌خرند
ادعای وال‌استریت ژورنال:
🔹
شرکت چینی هنگلی با خرید نفت تحریم‌شده ایران، به یکی از حلقه‌های مهم در دور زدن تحریم‌های آمریکا تبدیل شده است.
🔹
تحریم‌ها توانسته‌اند شرکت‌ها و کشتی‌ها را هدف قرار دهند، اما به‌دلیل انگیزه اقتصادی پالایشگاه‌های چینی برای خرید نفت ارزان، محدود کردن بازار نفت ایران همچنان دشوار است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/682501" target="_blank">📅 12:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a7f9e5a97.mp4?token=sac1KsikmIF_4MQ7xmNgwv1zG7WR4xM-LIPMUwDc-V4Zc-haEsfD-trkfBaaFm2ry_R9bqoYMrtTh5BkRWN6iTd-E3ePjZxoGZQhqTVNO3U8OfV5DvSlIYMyytCQYfzH0XyofnnqrPsYe1kFBM_mbu8CeYE_8AZCkI3C9YWVGbrOL_RmBOnjr8v9NvJ03_CSzm071lojNuJzERCA4BMFWXbocD3LsORKg1zl0MV4jRegjNvmsPXd3SqS-YF6D5f7CPGir6c8_HyCThAWOfT7ewTy2hqID8Fj-m-MhCSP8tI7tX5y0izBI0G4mAilxJq4tM-SeIdKYHzy2k1bu5mMaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a7f9e5a97.mp4?token=sac1KsikmIF_4MQ7xmNgwv1zG7WR4xM-LIPMUwDc-V4Zc-haEsfD-trkfBaaFm2ry_R9bqoYMrtTh5BkRWN6iTd-E3ePjZxoGZQhqTVNO3U8OfV5DvSlIYMyytCQYfzH0XyofnnqrPsYe1kFBM_mbu8CeYE_8AZCkI3C9YWVGbrOL_RmBOnjr8v9NvJ03_CSzm071lojNuJzERCA4BMFWXbocD3LsORKg1zl0MV4jRegjNvmsPXd3SqS-YF6D5f7CPGir6c8_HyCThAWOfT7ewTy2hqID8Fj-m-MhCSP8tI7tX5y0izBI0G4mAilxJq4tM-SeIdKYHzy2k1bu5mMaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جرم اسرارآمیز در خورشیدگرفتگی، هواپیما از آب درآمد
🔹
ویدئوی ناسا جرمی درخشان را هنگام خورشیدگرفتگی نشان می‌داد که ابتدا شهاب‌سنگ تصور شد، اما بررسی مسیر پرواز مشخص کرد این تصویر مربوط به رد یک هواپیما بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/682499" target="_blank">📅 12:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF1Pwib_vWKWHzd9r0psk1HvLjromgThe92ySpwQfo7Lhg0Tnwijoukr57vszE_FLCmg0HxmfAf2ICeWh5w1bfGnNUCezukS1Rcgdty6nhCSj2k-q6jng6M_SmpeQiBGBiFfdlpl_P8K2UJyssKUdTNAS2B0MfVc0jvnWSSM1u4TKWDOxdtgo60hokPYV_gZ_C6yVYwDPFbRKXxhfiYj01BZCKLl2b_kkB8zMRbM-g8IFFm05z3N06I9nCXTN6D4T5MSDewzJyQXQx_LxWak0yzk-BfCbT0tsxdKm3HcNkRjRzE-CFGNECmPpVvqLv56AhQuOBOKOpzIwHr8rEsJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فایننشال تایمز به نقل از منابع ایرانی: هدف قرار دادن احتمالی زیرساخت‌های ایران می‌تواند جنگ را از منطقه فراتر ببرد و به اروپا برساند
🔹
تهران حمله به دارایی‌های آمریکا در کشورهای جنوب‌ شرقی اروپا، از جمله بلغارستان را ارزیابی کرده‌؛ قبرس نیز در میان اهداف احتمالی قرار گرفته
🔹
ایران می‌تواند از موشک‌های بالستیک میان‌برد خود، علیه دارایی‌های آمریکا در جنوب و جنوب‌ شرق اروپا استفاده کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/682498" target="_blank">📅 12:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Roode Sookhte</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/682497" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
رود سوخته
🎙
محسن چاوشی
#آهنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/682497" target="_blank">📅 12:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان  مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/682496" target="_blank">📅 12:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwqHF_dntiZSFW31VDTs41-1IP8_Iyy6QYu2vrF5lWhvWYynGNx1RbDUsAg8Z-p2Dz21NPrpfs_qgw2PRk1kqwTmxzM1mhOY6EfyDcHB0XIw-B6JhGm1RXa1xE_z-ZJsazixI6ytJC76yYTtauve_qNynqDLm5JrOTnHWNTasMu-nHdFOD4XhYSFibq5G1q5U9yHCMb32ZdS2dJZ37YfPM4ZmNjvj-8ziTDq-0RU8g3IRkgKSqW2Hlwq-zpyOKbcpSQNF1B-GUg0_nnXYAULM_x22ZzWZHBOaZhBSacsjhs76FvErn0FcRayaO3z4c097HpX5uR51TOq1ExhFw_mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ال‌ نینو» امسال احتمالا رکوردشکن است
🔹
اداره ملی اقیانوسی و جوی ایالات متحده (NOAA) پیش‌بینی کرده است شدت پدیده «ال‌ نینو» در اواخر پاییز یا اوایل زمستان امسال به اوج خود می‌رسد و حدود ۷۰ درصد احتمال دارد که به قوی‌ترین ال‌ نینوی ثبت شده از سال ۱۹۵۰ میلادی تبدیل شود.
🔹
این پیش‌بینی نشان می‌دهد ال‌ نینوی امسال به سمت قدرت «رکوردشکن» پیش می‌رود و اوج آن در اواخر پاییز یا اوایل زمستان پیش‌بینی می‌شود.
🔹
کارشناسان هشدار می‌دهند اثرات گرمایش جهانی می‌تواند با ال نینو ترکیب شود و امواج گرما و شدت بلایای طبیعی را تشدید کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/682495" target="_blank">📅 12:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4HYOY_rnzRcNHMSsotk58L-6DbMB4OWno98xyyvo97VSJ90n_2ugeZflEvjR0f4HxqnXO7723_2MoA5A0LE6xT61kv6JycJ1Ajnkig0pvRwaafb3X0apnIrPQauS_RlpVVzinypXWPV3Nlyq76t1CtkKLvDxtElpPyuHj7pruoVV8GzL6vqE2ejao3mr1AN2jfLI3-jsO-N5BJ1A8Y-eDogc1hg-Jz9k1bOL9hWqcav7zvTRR0sNHdLf6BVv-hOu9DvJKgqontH-nEE9bdQq4ok41fKFYyy9SLIiYkMw6n_C9DRs6DXrk0pXzW37PnP5PTysc96HYoELek06_7QaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: چه کسی آن مدرسه ایرانی را بمباران کرد و ۱۶۸ کودک را کشت
🔹
ترامپ: «ما نبودیم. آن موقع کلی آدم تیراندازی می‌کردن. ما غیرنظامی‌ها رو هدف قرار نمی‌دیم.»
🔹
خبرنگار: «طبق گزارش اولیه، سیستم شلخته‌تون باعث اون حمله مرگبار به مدرسه شد.»
🔹
ترامپ: «تو خبرسازی. بیرون.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/682494" target="_blank">📅 12:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b2a38ba8.mp4?token=vV1fMWjVRssPGdZoKsRAXU1P5fSgI_ytTjTB8N3JGgc2ZC3u4tJUAlpZ2xDxlXhiDMMxWaKGv_ihsVN-1zdFGAgi6QLxZTVJHHcqfZssn_AXAJ4gpvBUZHVmKPFeNAxbn-rVY1oXwH0PYP-1YDj1qAxyp3Ajvi_TWwlyVwRtmBIAH82pu8cvHCyFYfUuVupwqmtFjIV35Igo2RB1TGapYNxdRrHWDv9cGGNomvnglz-T2jBBvQT3YhLhTbnAzKIHQa6R3UcQPF1co9ZiQ8O4v0w4NOz05H8RrHmX17XfmNNs3wcJCl_awmXMwl9YQDkI6CWipHrS2Z68UsqUDpIKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b2a38ba8.mp4?token=vV1fMWjVRssPGdZoKsRAXU1P5fSgI_ytTjTB8N3JGgc2ZC3u4tJUAlpZ2xDxlXhiDMMxWaKGv_ihsVN-1zdFGAgi6QLxZTVJHHcqfZssn_AXAJ4gpvBUZHVmKPFeNAxbn-rVY1oXwH0PYP-1YDj1qAxyp3Ajvi_TWwlyVwRtmBIAH82pu8cvHCyFYfUuVupwqmtFjIV35Igo2RB1TGapYNxdRrHWDv9cGGNomvnglz-T2jBBvQT3YhLhTbnAzKIHQa6R3UcQPF1co9ZiQ8O4v0w4NOz05H8RrHmX17XfmNNs3wcJCl_awmXMwl9YQDkI6CWipHrS2Z68UsqUDpIKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم‌های خودشیفته تو رابطه چه شکلی هستن و چطور باید باهاشون برخورد کرد؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/682493" target="_blank">📅 12:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=Z7n2UM0CSHRKC4l58wQOcUg4ZuwcVE3v4kq_btf7JXkvBrTap5Og8Rhelvg9o3H3tNiueWdEafs9nZ7ll2cwkG6zekPnhvRPCfn3a3taat7G36kadeYUMb4-4qtDx-CQxRwDyLdalWPjOo1lgDurTK16dCyWNDV9V_q9URGvu_9S0LDvSVZCd5isNjURvxPBjOYzutPypG0-ZPlN84t8e-DailSKryPS6WiIaxS8k0BQYCqTxIGvH09mXdJKE9M6BD9EygciPYc8_vk6GqQXi5H4h_yUlhzds8zzJ155hffspL9oTfGEkyWC1TEuiNZDOcZzhjaFIzkdiJ91omU-qKdIfTbOJ4MdfcVPcD5QiUFDLC9tGJYzxUw6lYcc5d9wnfZB24mIjapj0DghUOXWsA3oZ-tjn9k5G7CFzymZHssrV5N4iBPjCFOXjD1C_DyJYp8PjQtkWrbILimngREwuFylu_87SP8WsjEhhA27XuooBbIooPb3yYx4uSdWcIB6dKi8bujo0JNhccYhrrgKBhnqflnB-_auMItJvCJAdR3aVotLgJvA3et2cTHb_LOn3VZrDydwvx1qtfXPS7U-fGZ5kxrgshgIEg4NxbeHL3-MqpNuI-0io2vMgEXOS5-3sVLJEzVFUrzFUIz2rgRDCnF9oohb8POdMraWXD_HZKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=Z7n2UM0CSHRKC4l58wQOcUg4ZuwcVE3v4kq_btf7JXkvBrTap5Og8Rhelvg9o3H3tNiueWdEafs9nZ7ll2cwkG6zekPnhvRPCfn3a3taat7G36kadeYUMb4-4qtDx-CQxRwDyLdalWPjOo1lgDurTK16dCyWNDV9V_q9URGvu_9S0LDvSVZCd5isNjURvxPBjOYzutPypG0-ZPlN84t8e-DailSKryPS6WiIaxS8k0BQYCqTxIGvH09mXdJKE9M6BD9EygciPYc8_vk6GqQXi5H4h_yUlhzds8zzJ155hffspL9oTfGEkyWC1TEuiNZDOcZzhjaFIzkdiJ91omU-qKdIfTbOJ4MdfcVPcD5QiUFDLC9tGJYzxUw6lYcc5d9wnfZB24mIjapj0DghUOXWsA3oZ-tjn9k5G7CFzymZHssrV5N4iBPjCFOXjD1C_DyJYp8PjQtkWrbILimngREwuFylu_87SP8WsjEhhA27XuooBbIooPb3yYx4uSdWcIB6dKi8bujo0JNhccYhrrgKBhnqflnB-_auMItJvCJAdR3aVotLgJvA3et2cTHb_LOn3VZrDydwvx1qtfXPS7U-fGZ5kxrgshgIEg4NxbeHL3-MqpNuI-0io2vMgEXOS5-3sVLJEzVFUrzFUIz2rgRDCnF9oohb8POdMraWXD_HZKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسگاه پلیس ترکیه هدف پهپاد قرار گرفت
🔹
طبق گزارش رسانه‌های ترکیه‌ای یک ایستگاه پلیس در استان «ترابزون» که در ساحل دریای سیاه قرار دارد، هدف یک پهپاد قرار گرفت.
🔹
«ترکیه تودی» گزارش کرد که این حادثه دیشب در منطقهٔ آرسین رخ داده و تلفاتی نداشته است. فرماندار ترابزون هم پس‌از بازدید از محل حادثه گفت: «اطلاعات پس‌از تکمیل تحقیقات در مورد منشأ هواپیما ارائه خواهد شد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/682492" target="_blank">📅 12:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
فایننشال تایمز: اگر ترامپ تصمیم به تشدید جنگ بگیرد، ایران در حال بررسی امکان هدف قرار دادن اهداف نظامی آمریکا در اروپا است
🔹
بلغارستان
🔹
قبرس
🔹
کابل‌های اینترنت در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/682491" target="_blank">📅 12:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1CGWhAtFVk4z4eDAejuWbBJl7hOneqIQdCKK5z6xCaOWTGqEAR_TsJ80pSClienautagtSUoL7AN7X8yuRavfrfdLzVvHLbQBeV4Kj5WLKw6Lx9hBGsVl1FhtOpsZW5Nsh4ZYYWWFEM7Jjejyd6cFgHq7iaUz9PPf6QgwsbCTyY8ENTtHRmIrVF2UFOcQWF4m_l7fySaa4bm7ptRuFJYqM3B1uUQpu7hmMaf8hsEP-qiJECA2QMrV91hSx2OTmQ6nQlOsT5ZU448Amjz6bOXeZvEVc8uf1OseaHY55Mc_cFGhLRXTxvq62o-MpPrhdQm3KG_1VzXV_WE6f5nA_6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان نصب چهار اپلیکیشن‌ اصلی نمایش خانگی منتشر شد
بیش از 40 میلیون ایرانی شبکه نمایش خانگی را روی موبایل خود تماشا می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/682490" target="_blank">📅 12:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b94f2770c.mp4?token=pTuiW7HHPZFKskNRki2T0dFDiRqGc52mbE_b-ZqlsX9ST0Flj_cMsLVWNBGDGklBvMxPTB9PaGipsYS65tNkU9b8FIjjcaiXCc_Tm_lFkFtbyDpqwEHQvpPxZGEhjlxlNnK9918sTDhcbUac1fkOb3NbrDz16tyNBM5pvmNynrBEUlSWEExHw2dVtY_PX2YuiRnLwg5efvHCVn3A9Q820R6iPzQJtN77jThS8HgQJ4wkj6bqqSI8qB0xOtfKh6yyvFzEySvVmkF_ZtibndLx-nhqghuos8C5cUGhTPZY-Y1LFxwfQElTaaD4noq0vFDznlH3z1TECT7QhSKI31paIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b94f2770c.mp4?token=pTuiW7HHPZFKskNRki2T0dFDiRqGc52mbE_b-ZqlsX9ST0Flj_cMsLVWNBGDGklBvMxPTB9PaGipsYS65tNkU9b8FIjjcaiXCc_Tm_lFkFtbyDpqwEHQvpPxZGEhjlxlNnK9918sTDhcbUac1fkOb3NbrDz16tyNBM5pvmNynrBEUlSWEExHw2dVtY_PX2YuiRnLwg5efvHCVn3A9Q820R6iPzQJtN77jThS8HgQJ4wkj6bqqSI8qB0xOtfKh6yyvFzEySvVmkF_ZtibndLx-nhqghuos8C5cUGhTPZY-Y1LFxwfQElTaaD4noq0vFDznlH3z1TECT7QhSKI31paIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش گرافیکی و دقیق از جراحی تعویض مفصل ران که توسط هوش مصنوعی تولید شده است
🦿
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/682489" target="_blank">📅 11:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UykVuDF3xhH4TdkA4EAo4dy_kbhPuUwwfY676N7B-YjnO4WqxZ85g7ImeUXClTQEAxTdKI8u1ELGQeqeCyrh-6WPzRZx5SoGtfBm3miLRJYxfsg31o0-DZaUHEKKSk9ciTdqDgYs9aPeTk-CdgQQTQvky6mZv7TiluoTpcXcWSGVAp7MlZl7FlnEzXYP6SAPrNNPyHz0AtW-8d-EV0nljPocDIXdPLl3_zg-Yv9wksaR_ux1C3QyYleOWuCHBnCNCr2Geiwz-Owpg9epy4Uo7S5QHU3kY7o3c1Gfv45wwSAt6-8KWbxFaqW3Ub6-NYRgUM4Cahsb-mLQOnkrsglpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودپرداز طلا؛ مسیر تازه برای دریافت فیزیکی طلا
🔹
شبکه «طلاپرداز» با همکاری طلا کارت و توسن تکنو راه‌اندازی شده تا کاربران پلتفرم‌های آنلاین طلا بتوانند شمش طلای استاندارد خریداری کرده و آن را از دستگاه‌های تحویل طلا دریافت کنند.
🔹
این زیرساخت همچنین امکان تبدیل طلای آنلاین به طلای فیزیکی و دریافت آن از دستگاه را فراهم می‌کند. قیمت طلا توسط پلتفرم‌های متصل تعیین می‌شود و طلاکارت در این فرآیند نقش زیرساختی دارد.
🔹
طلاپرداز در مرحله نخست به‌صورت تدریجی در تهران و چند استان راه‌اندازی می‌شود و قرار است در ادامه، تعداد دستگاه‌ها و پوشش جغرافیایی آن افزایش پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682487" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8fdc35e9.mp4?token=UGAl404_Ydnc3dIn2W3UVpQKtkvTdYE9PFrLEGAtIeboDf3DofYGYMGLmP3VBKE8pEeFKa7QLDKidQMqP96Z9HYYuxUPluAVLLl57_XDrx4zZJJU48Qz-8uHkx_wSo8UuhW5NJKmuaXWmlPzSbJPg4sx1LQeP1DDdV2dEACpOXTH1T1OnDAXRSS8Zt2v7WHNITbY8BZNzxFErhzhVjVPCTU1f4gnF9-sP_1UcpnnCQ9UyiYWo-SKY-KOo2ReGmnVumrlpgD-mwAFGUWlrHEDRaVN8bszmPnz-layTrISHfBQNa0TePHg9pTxw7zp6LqGZxEy6MZhscRs3URjeX1WVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8fdc35e9.mp4?token=UGAl404_Ydnc3dIn2W3UVpQKtkvTdYE9PFrLEGAtIeboDf3DofYGYMGLmP3VBKE8pEeFKa7QLDKidQMqP96Z9HYYuxUPluAVLLl57_XDrx4zZJJU48Qz-8uHkx_wSo8UuhW5NJKmuaXWmlPzSbJPg4sx1LQeP1DDdV2dEACpOXTH1T1OnDAXRSS8Zt2v7WHNITbY8BZNzxFErhzhVjVPCTU1f4gnF9-sP_1UcpnnCQ9UyiYWo-SKY-KOo2ReGmnVumrlpgD-mwAFGUWlrHEDRaVN8bszmPnz-layTrISHfBQNa0TePHg9pTxw7zp6LqGZxEy6MZhscRs3URjeX1WVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ترفند ساده و کاربردی که جای کمدت رو دو برابر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/682486" target="_blank">📅 11:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_BS0cL5UHVon7qNmI8SbExyPRKBKBmANUjq9aQ5jVWRu-e7nYM80HvO55tL1tq-yZLq-EJYwfFm0bdNH3KwxCl3BkTj8H0xEsM3CBe5oRzkTSG_24yFBf269RO8hz8ZN02jufwBt7WashHD4TAo7Ch_cZzxB3FRf7WFFMnbJmgJ1vgkiXoZGquqJknqJlM_hhKsjfcLxdrZTYji5euMb68K7xT8UAtE3_AbLnBN6KGh3t5lPN4PO6T20Ae8154_E1U6uQIpWbvVp4Tq0FpSDybvchxc14DdDE8HQDEM2ZnlUrFcF9FcyFtNExe-OW1XlG3ineeo5MWFxY0-7v-xrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنک یوگور، مجری آمریکایی: ترامپ اعلام کرد که تنگه هرمز باز است و پس از اینکه ما ایران را شکست دهیم، به‌زودی به قلمرو آمریکا تبدیل خواهد شد
🔹
تنها کسانی که او را باور می‌کنند، سالمندانی هستند که فاکس‌نیوز تماشا می‌کنند و همه افراد در وال‌استریت.
🔹
اما یک چیز درست است: او امیدش را از دست می‌دهد و برای ادامه جنگ بیشتر، موضع خود را سخت‌تر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/682485" target="_blank">📅 11:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e00614052.mp4?token=EorqADlVoBbcJUILhS8j5Qq6TqLTgklohjALvmZdtMOBqNEAdCVoi_j-saAT6p144INuUWJdhjC00h_U6R8N2g52b8UTALH8rBo1L3mz4RSmd74jm5H8Kb2FlesVRvnDbyFOWX-iw7FKUJPI4Q6w8qvXU1UtGeOzW3bLeSH0CcRAuk49-DTG2zc7b9MKoqQv2UwMM-EVH-4A1ni58_3XpolnIvgkpGoz4ULPsYiiKecE0lVl67zFeWA1Ofdlhs0TFc1uycyAzUcj85-BZ1jnJHikF-EiBBe0vHDdGNV8HTF-H4sQR4TmfIHUsIeT5gxqW2Rpp4FMvPw_3ihLLd3C9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e00614052.mp4?token=EorqADlVoBbcJUILhS8j5Qq6TqLTgklohjALvmZdtMOBqNEAdCVoi_j-saAT6p144INuUWJdhjC00h_U6R8N2g52b8UTALH8rBo1L3mz4RSmd74jm5H8Kb2FlesVRvnDbyFOWX-iw7FKUJPI4Q6w8qvXU1UtGeOzW3bLeSH0CcRAuk49-DTG2zc7b9MKoqQv2UwMM-EVH-4A1ni58_3XpolnIvgkpGoz4ULPsYiiKecE0lVl67zFeWA1Ofdlhs0TFc1uycyAzUcj85-BZ1jnJHikF-EiBBe0vHDdGNV8HTF-H4sQR4TmfIHUsIeT5gxqW2Rpp4FMvPw_3ihLLd3C9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید آماده بود جان خود را فدای مردم کند
🔹
جورج گلووی، نماینده پیشین پارلمان بریتانیا در گفت‌وگو با پرس‌تی‌وی: خودداری رهبر شهید ایران از رفتن به پناهگاه‌، نشانه شجاعت و دلاوری او بود و جایگاه و اعتبار ایران را بیش از پیش تثبیت کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682484" target="_blank">📅 11:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مدیران جدید دستگاه قضایی معرفی شدند
🔹
ناصر عتباتی، رئیس دادگستری استان تهران
🔹
حیدر آسیابی رئیس رسازمان زندان‌ها
🔹
اصغر جهانگیر رئیس سازمان بازرسی کل کشور
🔹
دانش رئیس مرکز حفاظت و اطلاعات قوه قضاییه
🔹
سلطانی معاون قضایی قوه قضاییه
🔹
امیری اصفهانی معاون اجتماعی…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/682483" target="_blank">📅 11:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682481">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq4rpQThWlfNqJ59gUN9XMzwJ1GuCqzlu9yrXH0Ub0B3ulc4XyAS1oEFY0KWrITONmI4oGRfAtZTiI15Q0Ygljccr2H5VKhTme862qqjrw6X9HiiJJCR1EiC9eD5jvg9Ws1gqNfC22Q02bG14c4-Vk68OD8LCh_7DarxklJvSHEfdlWMCCUoKf4m03T6BoZ4fUWnE43fkkOcVP0t30oQ2VXFj7qhzSCGs23azPga5ubrePBg5e63nViRy7WztygBBejM2ozmn0oEhqSUqdXQHuIrLK7f6WBEGQjDBtbgNW4SQe2pXxOVew1BZSucmE1vSM6GkMomFzxqA4Xz18Vf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی؛ پاوربانک شیائومی + ایرپاد M10 هدیه
🔋
پاوربانک ۵۰۰۰ میلی‌آمپر شیائومی
🎧
ایرپاد بی‌سیم M10 با بلوتوث 5.0
⚡️
کیس ایرپاد با قابلیت پاوربانک اضطراری
💡
جمع‌وجور، کاربردی و مناسب سفر و استفاده روزمره
💰
قیمت: ۱,۶۹۸,۰۰۰ تومان
✅
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
🛒
خرید تلفنی
👇
https://memarket24.ir/product/fast/63564/180124/</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/682481" target="_blank">📅 11:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc52a7296.mp4?token=gF0mDEm61yp_tBWxIb6Rmd_8CiS1apm-r6BF7ReDMH8ssblhRHjYk6LSeK8xxBmamqKbwVeEXXjXMLnUduPEuaDo3LV4LYgZMQ0y1aIOgUWVYK2oszIE6vzjnT7pbbZf6pfkrRZhZnZassAqEMD1i_po8oGh3zQO2f5Bh831nnZn3Q7gGtq8enOK6kYw4MqdFpRUUIDU9PoD_8Ppkf6B3Qr9Led1y1vZU94a-7-vubjryJosSXP3H1LG8u6acisfRIMkfOhanvqz6VGuktcDfbn2GyUPqMwbmsAzMoxRQ3KnJgcyIKdI7HScTpjMWZlMHguGrLPGmZzUBfl1efpo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc52a7296.mp4?token=gF0mDEm61yp_tBWxIb6Rmd_8CiS1apm-r6BF7ReDMH8ssblhRHjYk6LSeK8xxBmamqKbwVeEXXjXMLnUduPEuaDo3LV4LYgZMQ0y1aIOgUWVYK2oszIE6vzjnT7pbbZf6pfkrRZhZnZassAqEMD1i_po8oGh3zQO2f5Bh831nnZn3Q7gGtq8enOK6kYw4MqdFpRUUIDU9PoD_8Ppkf6B3Qr9Led1y1vZU94a-7-vubjryJosSXP3H1LG8u6acisfRIMkfOhanvqz6VGuktcDfbn2GyUPqMwbmsAzMoxRQ3KnJgcyIKdI7HScTpjMWZlMHguGrLPGmZzUBfl1efpo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری یک حیوان‌آزار در تالش
پلیس راهور فراجا:
🔹
پس‌از انتشار فیلمی در فضای مجازی که در آن یک خودرو در تالش اقدام به کشیدن یک سگ کرده بود، رانندهٔ خودرو به مراجع قضایی معرفی شد.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682478" target="_blank">📅 10:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مدیران جدید دستگاه قضایی معرفی شدند
🔹
ناصر عتباتی، رئیس دادگستری استان تهران
🔹
حیدر آسیابی رئیس رسازمان زندان‌ها
🔹
اصغر جهانگیر رئیس سازمان بازرسی کل کشور
🔹
دانش رئیس مرکز حفاظت و اطلاعات قوه قضاییه
🔹
سلطانی معاون قضایی قوه قضاییه
🔹
امیری اصفهانی معاون اجتماعی و پیشگیری از وقوع جرم قوه قضاییه
🔹
حجت الاسلام سید محسن موسوی رئیس مرکز حل اختلاف
🔹
علی کاظمی سخنگوی قوه قضاییه
🔹
ذبیح‌الله خدائیان رئیس حوزه ریاست قوه قضاییه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682476" target="_blank">📅 10:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پرداخت معوقات همسان‌سازی و افزایش حقوق‌ها از ۱۰ شهریور
سخنگوی کمیسیون اجتماعی مجلس:
🔹
وزیر کار از آغاز اجرای احکام همسان‌سازی از دهم شهریورماه خبر و قول داده تا معوقات حقوق بازنشستگان پرداخت و همسان‌سازی انجام می‌شود.
🔹
همچنین مقرر شده است مابه‌تفاوت افزایش حقوق فروردین و اردیبهشت‌ماه نیز به بازنشستگان پرداخت شود./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682474" target="_blank">📅 10:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbwZ7s0erbqQZhkbJd2XdhlLPQ7jEzE1PUABVJnIU92tQyhFLSr2SjfwITmCADAbILQ96PqhACg91enX3-PysPkFi3fVq8-v_g_0mTrfrZoHGoFmPbOvZZtoZ2oLCFGvCXRq2OsS-qyf4bU9A9n1ZWfI5vr_TMWq0EK23pTBVgjWV-A75AK7Rytc3bM7wpR03YrrKhgXUi4W_JL8o0rB4SMTs9_fbW8u2PhxLLPFvwoBFppZ0TGtLYp7p_xUPZnuu33Rxm7yPv2gzKYmmq84q_h4CJhYt6d7v2mTQ8CUZ6IKGJWUxnncQlS3pESks6pFbPhwOl_dCYh47xNXVzC9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس رنگی شده، از شیراز؛ سال ۱۹۱۱ میلادی، هم‌زمان با پادشاهی احمدشاه قاجار
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682473" target="_blank">📅 10:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سازمان سنجش: همراه داشتن هرگونه وسیله شخصی در جلسه کنکور ممنوع است
🔹
ارائه كارت شركت در آزمون و همچنین اصل كارت ملی یا اصل شناسنامه عکس‌دار برای شركت در آزمون الزامی است.
🔹
فرایند برگزاری آزمون‌های صبح رأس‌ ساعت‌ ۷:۳۰ و آزمون‌های عصر راس ساعت ۱۵:۰۰ آغاز می‌شود و دربِ حوزه‌های امتحانی به ترتیب رأس‌ ساعت‌ ۷:۰۰ صبح و ۱۴:۳۰ عصر بسته خواهد شد.
🔹
متقاضیان از همراه آوردن وسایل اضافی از جمله مواد خوراکی و آشامیدنی، كیف دستی، ساك دستی، هرگونه دستگاه ارتباطی و الکترونیکی از قبیل پیجر، تلفن همراه حتی به صورت خاموش، تبلت، قلم نوری، ساعت هوشمند، دستبند هوشمند، انگشتر هوشمند، هندزفری، کیف، جزوه، كتاب، ماشین‌حساب، هرگونه یادداشت و نظایر آن و همچنین وسایل شخصی به جلسه آزمون اكیداً خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/682472" target="_blank">📅 10:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aom3qBl14wbT80_wb9Z0NKy3ruwSObRveZXtnEMSstxga1aDbwqkYiMnIysEp8ux7V8zU3HjoIbSb8oTGAfYiqQ287csLmbAUCsgb4oKfve2GA00RePNI-ZMrAZtsYVMuuxCyIsZvowXfpIPRs-jOkO1i4oD-RZwG4dPrPjaZF5zYSTsLdKpJdnnaTQlE0HMnJUYDBsV9NSOhzw7PAMhb1m8e6OnBqZCVOP1o6mB-yRwoNs5ujZsOWtIXIacneLoUQtzu2YCCyveU5oEH9KWhZSoN6p4zeiSSFqSp_5dV_eAEqbu8GilwHyyXPGkjl2Euq8F8FP1Bk-i2FOnXTaewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا فیلم جنجالی درباره زندگی امیر تتلو است؟ | راز شباهت عجیب امیر جدیدی به تتلو | شباهتی که نمی‌توان نادیده گرفت
🔹
از همان نخستین تصاویر و خبرها درباره فیلم «بیداد» به کارگردانی سهیل بیرقی، یک پرسش ثابت در حاشیه اثر تکرار شد: آیا این فیلم، روایت پنهان یا نیمه‌مستقیمی از زندگی امیر تتلو است؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3238851</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/682471" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af4bc85d6.mp4?token=vVMIYoPeM2XSlp--U_jVS44BFJqTAcLoEvn6LYbSQbK8kbIJwbxbBQpvNOEKjO_6Wym0EIEF7_NyWmuelPR9sbZoLWFgmGn4aLVHchp2DYhnUmyC3G8BQItYy8VAWNjVCagln9pBOKj2lZU36vvOstNPq4DoMWEvGXb-VuJISBhThyV7poNxOTvZdIBocYy451b1SfR5ka0Ao2wO5xjTXkSknulxZBY-1mY6bcJRjcqfQEOOonwPm99udY9INNRcHIj4XcEtT1wQKFtbAfqXszIVrmcJy-GHl3LXSghZgNLkNyoQSATqd2tzBk0x4qI_RaGlggA8XS0D6j_1MRWHHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af4bc85d6.mp4?token=vVMIYoPeM2XSlp--U_jVS44BFJqTAcLoEvn6LYbSQbK8kbIJwbxbBQpvNOEKjO_6Wym0EIEF7_NyWmuelPR9sbZoLWFgmGn4aLVHchp2DYhnUmyC3G8BQItYy8VAWNjVCagln9pBOKj2lZU36vvOstNPq4DoMWEvGXb-VuJISBhThyV7poNxOTvZdIBocYy451b1SfR5ka0Ao2wO5xjTXkSknulxZBY-1mY6bcJRjcqfQEOOonwPm99udY9INNRcHIj4XcEtT1wQKFtbAfqXszIVrmcJy-GHl3LXSghZgNLkNyoQSATqd2tzBk0x4qI_RaGlggA8XS0D6j_1MRWHHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علم منتظر معجزه نمی‌ماند!
🔹
واکنش کودکی که با استفاده از عینک برای اولین بار مادرش را به وضوح می بیند...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/682470" target="_blank">📅 10:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682469">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
📊
عملکرد هشت ماهه منتهی به ۳۱ تیرماه ۱۴۰۵ بانک سرمایه در یک نگاه
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/682469" target="_blank">📅 10:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682468">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
امارات تمام مبادلات تجاری و مالی خود را با ایران تا اطلاع ثانوی متوقف کرد
ادعای آناتولی:
🔹
خبرگزاری دولتی امارات به نقل از مدیر ارتباطات استراتژیک وزارت خارجه گزارش داد که امارات تمام مبادلات تجاری و معاملات مالی با ایران را «تا اطلاع ثانوی» به حالت تعلیق درآورد.
🔹
هنوز جزئیات بیشتری فاش نشده است. با این حال، این اعلامیه پس از آن منتشر شد که وزارت دفاع امارات مدعی شد دو موشک بالستیک ایرانی را که ناوبری دریایی را هدف قرار داده بودند، شناسایی کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682468" target="_blank">📅 10:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813058e1ec.mp4?token=fO8R1-iYkeN6JYt6WkJixrcDoEbHxXO_xsXyvEl8usoH8hv5CZk5kbLt6zM5LOK26vZcP00fixRMOC0JOZ9ippe7Nmh-szKRO8EyhPYdZn3vqhWdU-UIBnifGS98W3bmHbSqCFMHBKMDpYUX7SLkC7dL1lXuZn_ZjIOr4ekbcTHvT-wsUoe6t3rCmTheRR5artu0Kdo0m653ocDZfnnUyJvXI5ywnWMx1ISctglbppe6GeD2z2NnqraO8cXSAGzfNQYwn4FvRBgEGkmYC3JlY26wGZUoOay1_Gae6YsOJkhyOUXOjNHQVxdIjnLQxkPQfvRPtl9HhP6FfnSEWMsVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813058e1ec.mp4?token=fO8R1-iYkeN6JYt6WkJixrcDoEbHxXO_xsXyvEl8usoH8hv5CZk5kbLt6zM5LOK26vZcP00fixRMOC0JOZ9ippe7Nmh-szKRO8EyhPYdZn3vqhWdU-UIBnifGS98W3bmHbSqCFMHBKMDpYUX7SLkC7dL1lXuZn_ZjIOr4ekbcTHvT-wsUoe6t3rCmTheRR5artu0Kdo0m653ocDZfnnUyJvXI5ywnWMx1ISctglbppe6GeD2z2NnqraO8cXSAGzfNQYwn4FvRBgEGkmYC3JlY26wGZUoOay1_Gae6YsOJkhyOUXOjNHQVxdIjnLQxkPQfvRPtl9HhP6FfnSEWMsVUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزه بهشتی این مرغ تا مدت‌ها از یادتون نمی‌ره
😍
مواد لازم:
🔹
پیاز خلالی ۱ عدد نسبتا بزرگ
🔹
رب گوجه ۱ قاشق غذاخوری
🔹
رب انار ۲ قاشق غذاخوری پر
🔹
الو‌خورشتی چند‌ عدد
🔹
زرشک۲ قاشق غذاخوری
🔹
زعفران دم کرده به‌میزان لازم
🔹
آب نصف لیوان
🔹
ادویه‌ها نمک، زردچوبه، فلفل سیاه…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682463" target="_blank">📅 10:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682461">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4508f1e662.mp4?token=HebFdvHvgNcTb4o5evnaN36sjqur2lom7m4_J9YZPfW6mFGB3FyrFJWd_6i6sL2Dm3AnF8b8DbPaNEJL29-uiNYOItn2bfkDR3N8U5fxEnEI9nU7mj7Oni0ywhHbJL1oivxK_GOobmcrpbFhRUM8WC13Haf-glDYvwgXzt9X4pZ6Iru7USu5LvoqqixmJcEpTvfUdJ-9C5fSJpMoIDxFAC07bMJhGLNwBh5XX14xr93EkAg-iK7yWvV-kX04MyezctHoWORjHK0f3Zgh1EktLA6DYU4pmqbyh4z7WW9yrzK4B_pEuYAalyoXynTvYxFGlN-i-vT6Fuw3OuwuqBk-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4508f1e662.mp4?token=HebFdvHvgNcTb4o5evnaN36sjqur2lom7m4_J9YZPfW6mFGB3FyrFJWd_6i6sL2Dm3AnF8b8DbPaNEJL29-uiNYOItn2bfkDR3N8U5fxEnEI9nU7mj7Oni0ywhHbJL1oivxK_GOobmcrpbFhRUM8WC13Haf-glDYvwgXzt9X4pZ6Iru7USu5LvoqqixmJcEpTvfUdJ-9C5fSJpMoIDxFAC07bMJhGLNwBh5XX14xr93EkAg-iK7yWvV-kX04MyezctHoWORjHK0f3Zgh1EktLA6DYU4pmqbyh4z7WW9yrzK4B_pEuYAalyoXynTvYxFGlN-i-vT6Fuw3OuwuqBk-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد مرگبار کامیون با پل عابر در برزیل
🔹
دو سرنشین این خودرو، یک زن ۶۳ ساله و پسر ۴۰ ساله‌اش، جان خود را از دست دادند. یک نفر دیگر نیز به‌شدت زخمی و برای درمان به بیمارستان منتقل شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682461" target="_blank">📅 09:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682460">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe079e89c.mp4?token=FmFvix1UwGurDLE36OHzzcCJsPzFg_Ch_er97XDIiKC_bB3ClJvFGIw-oeb6S_E3ftxGEi75naDi4H2KgIIbxEHyMusxOXi-UPanpTjhvIyjnBVTB5LIEyVpFGGqi-pF3VxoGUSkybm89riL1LH1dmvK7aai3xNF1qWmxYKqv_zZwnEdFUX5bdZxhXkzlABKWvSWj7A11iQ0GyH-JmLOUJFyBMAmOhfLmFqZYI8yC69z2MbJHzhfnkGnXAIDf3r2BvIJ8oClAM5Vf2HZKyX1gjGjYWogEWL1BdWgqcTC5vJPlvK44HZxFTErJYm0_WNaAHoTMdXqNEzA1D-JTl__MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe079e89c.mp4?token=FmFvix1UwGurDLE36OHzzcCJsPzFg_Ch_er97XDIiKC_bB3ClJvFGIw-oeb6S_E3ftxGEi75naDi4H2KgIIbxEHyMusxOXi-UPanpTjhvIyjnBVTB5LIEyVpFGGqi-pF3VxoGUSkybm89riL1LH1dmvK7aai3xNF1qWmxYKqv_zZwnEdFUX5bdZxhXkzlABKWvSWj7A11iQ0GyH-JmLOUJFyBMAmOhfLmFqZYI8yC69z2MbJHzhfnkGnXAIDf3r2BvIJ8oClAM5Vf2HZKyX1gjGjYWogEWL1BdWgqcTC5vJPlvK44HZxFTErJYm0_WNaAHoTMdXqNEzA1D-JTl__MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات «سوپرمن» اینجاست!
🔹
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682460" target="_blank">📅 09:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682459">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=OOU9Zdj7BqkS-kjG5wnpFWJuZsoEGXksxHG7ZvYRvM2TSjiUZeYgQXVQj7Im6SLdmaDd35ERfSI_1eADsP_9q1yWir4VxS82eIcIXMcIH_flwAHtpzMBS9Y5C8ptkoMw0CMH45M9J3512vIpmPgBgjlsrqvr9MDAibKYF-HdQcCA3UWXt03FpCTSfnZqwfzK5YlzYnelavT8KdkNzNifAEamnNn1pkuY06rufzLJ1oes-Ayu6HenSyBbrpR7edGdvc1HaSGgdJIiU3a_KLCOa1rtdDvD3XYHLjpft2NBRtCVWSwNbbdojtrsAEnDzH5-yZEFtfh-Od6_r3DV87hCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=OOU9Zdj7BqkS-kjG5wnpFWJuZsoEGXksxHG7ZvYRvM2TSjiUZeYgQXVQj7Im6SLdmaDd35ERfSI_1eADsP_9q1yWir4VxS82eIcIXMcIH_flwAHtpzMBS9Y5C8ptkoMw0CMH45M9J3512vIpmPgBgjlsrqvr9MDAibKYF-HdQcCA3UWXt03FpCTSfnZqwfzK5YlzYnelavT8KdkNzNifAEamnNn1pkuY06rufzLJ1oes-Ayu6HenSyBbrpR7edGdvc1HaSGgdJIiU3a_KLCOa1rtdDvD3XYHLjpft2NBRtCVWSwNbbdojtrsAEnDzH5-yZEFtfh-Od6_r3DV87hCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
در جنگ رمضان قدرت مقاومت ایران را درک کردند/مقاومت از مرزهای ایران و عراق و منطقه فراتر رفته و جهانی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/682459" target="_blank">📅 09:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682458">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51d81de95.mp4?token=BIF2Ym-fY7asDG1u5csqfnSebxyNQzb-1N-PS2MqL5k0KbSDvE1K7DcQAdAh7A2x8PmJjB3L0YKjc-EegVmi9rUv5SGc_z-nqdXkqFrt4J9PaOP4OqM59kHOF_WeZDsc3e-rvf1DPy5wBLdFX0VARgn_nsY_9UjnchxXRbNRmVPiNOmzs4EKQEVfOnTsOu-IYagp_WF-INcN-asN_6QR19kDxiDmWNA9k49ZfmQfxolYbnEsL4ytf1a2PLbuB_M5Zu8qOKlPGGXcWoNJLnnlXfCdM0izkmpGYSMtCZCpm7ZCJXhAtL2VV27DFNtxmxQOxmwtarD3CNyrXGrrP3PPHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51d81de95.mp4?token=BIF2Ym-fY7asDG1u5csqfnSebxyNQzb-1N-PS2MqL5k0KbSDvE1K7DcQAdAh7A2x8PmJjB3L0YKjc-EegVmi9rUv5SGc_z-nqdXkqFrt4J9PaOP4OqM59kHOF_WeZDsc3e-rvf1DPy5wBLdFX0VARgn_nsY_9UjnchxXRbNRmVPiNOmzs4EKQEVfOnTsOu-IYagp_WF-INcN-asN_6QR19kDxiDmWNA9k49ZfmQfxolYbnEsL4ytf1a2PLbuB_M5Zu8qOKlPGGXcWoNJLnnlXfCdM0izkmpGYSMtCZCpm7ZCJXhAtL2VV27DFNtxmxQOxmwtarD3CNyrXGrrP3PPHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای تماشایی زمین از دوربین فالکون ۹ اسپیس‌ایکس
🔹
در این تصویر، زمین مانند تیله‌ای آبی در دل تاریکی فضا دیده می‌شود؛ قاره آفریقا و توده‌های سفید ابرها نیز به‌وضوح قابل تشخیص‌اند.
🔹
این نما در فاصله‌ای حدود ۳۶ هزار کیلومتری از زمین ثبت شده و یکی از تصاویر چشمگیر واقعی از سیاره ما در فضاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682458" target="_blank">📅 09:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682456">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس سازمان سنجش: نتایج اولیه کنکور در شهریور ماه و نتایج نهایی در نیمه دوم آبان‌ماه اعلام می‌شود./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682456" target="_blank">📅 09:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682453">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv9dDI1IBtl-nVIWPq4I05UV3sXkpHOtvi_DqU9mJDMN-3dTxKAAnndJpeY9mstrhfDroE1rZRK2EhJqBgpfc_onicLsv3lptL0C55O1KRxnN6LICcbnWf6dWsqOOoZffAOYkdXu4o-iYYrNp2k3ewr4qZehGDG976CxWgOPUrZlqvoNGrTPMtDV1heXH_bX0b8lvCYOnTYx5mDhZZtfTrm_NVZf_ukURpzJh0DaKyYmy_9htZkBWwaFbLUDmUw1GsOXSf3gkEmm3r3srIDCW_PI90PfzAVe_E6d8kek5WRoJkCI2VyCIsN6t_Y-e2w6BDRc0IdWGwNb2MmmtO4Dmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس ستاد کل نیروهای مسلح در خصوص کمک به ارتش متجاوز آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/682453" target="_blank">📅 09:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مزایای رفاهی کارگران معاف از مالیات شد
🔹
با رأی هیأت عمومی دیوان عدالت اداری، امور رفاهی و انگیزشی شامل (حق مسکن، بن ارزاق کارگری، حق اولاد، حق تأهل، هزینه ایاب و ذهاب، پاداش افزایش تولید و ... ) از پرداخت مالیات معاف شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/682451" target="_blank">📅 08:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCZpsJNzKQI4vfZONXwP_kVLPQOErThnf0oPTfHvlUXDFTCmnv71K8RdSIKrHoMdETCWecRPo9ZwDAO_rrXna5QFf3UDVRXaHhY1ptxrsmHvaXGXPEbUfHTkE8ytb3TD-DtQwqHyHWPIf_3viemOnKJCNXit2CytBlMVYa-X8f8TWpvmUkzbXSORs8Stq_f_cStvN0XuGE5GV3lSGQpBQr_PiW0v-I3Rcdu3Xnltm-qQxlcl6N4twGlDTgi4SZxehf_bpwuk-vd5ZH4cudXAoSe2a50xHTG_OKLs6hnTgdw6yl3NRiCIQgst_9PPDWaFoJqQdYxlY0me_T9Q1XWVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtH3p7D2Nza2H44NucsFZzIuwp7q2K-8Ufky760xItZn36YPvlXyEmMs51scKEolW0Bd3Mniab69-0uIUCtXeyRZntNxJDqG-IOuEDa7LUgpa0__OkDIHJYvtiqZffvHP0-VDTFkXFc782aJALojHZXppeXVntWTLRWG-zgM11Zcy3uVflYXJRJA8ffcDfQSyaSpetXwDLpBLBVo0GI1JRDoGpECQxTNGxSDrNYI4vPzOPODvTcs0CYsEDRyRQqesAToH3SnlK-sbONc73mlTu3Yfx7I9ziRhmqOcmpSFd8R4VyDOFpxoHP0E64TBIhGH2roE5k1zp93oNX7F-7saw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدام ایرانی اولین عکس «سلفی» را ثبت کرد؟
🔹
۱۹ آگوست (مصادف با ۲۸ مردادماه) در تقویم بسیاری از کشورهای جهان به عنوان روز جهانی عکاسی نام‌گذاری شده است.
🔹
برخی از اسناد تاریخی می‌گویند که نخستین عکس خودنگار ایران را ناصرالدین شاه قاجار با قرار دادن دوربین سه‌پایه مقابل آینه و ثبت تصویر خود و زنان حرمسرا گرفته است.
🔹
برخی هم نخستین عکس خودنگار ایران را به تصویری از ملک قاسم میرزا نسبت می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/682448" target="_blank">📅 08:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
انحصار وراثت غیرحضوری و خودکار شد
🔹
ازین‌پس، برای متوفیانی که تاریخ ثبت فوت آن‌ها بعد از سوم مرداد ۱۴۰۴ باشد، نیازی به اقدام از سوی ذی‌نفعان برای صدور گواهی انحصار وراثت نیست و گواهی به‌صورت خودکار و حداکثر ظرف ۲۰ روز صادر می‌شود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/682447" target="_blank">📅 08:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxtcBGFBTwd2BAwYIlXcpWZtxJVj9DrBlQtE0TXEv9iYhB1N_9z2higHj7qOfOqjnmn10ggyoYHomjijKPoYUE9ujUXLgTo07IkOArVN7_ICFA_c5bAsg-1dpRmI8tOKxqzpIOPKgHzrfsuW09akI7pkhkzXhiurUPh9BLPxFsm4hck10sKlsTGev4QNfYBr_7VXdp25uzjCjy9o4b5iK9fQQNjeV9eOR_ozbjBwayfB_9EFmZLOuSexvzCxGOfmy4WI02G5HwQlL2HqKNlF07DGDBJmaohgWYRk97MQbEJFbcU13I6SgE7FAopycrHDofHzFabIT9c5BaTc2xHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاج ابو الاء الولائی: نفت عراق به فروش می‌رسد اما عراق نمی‌تواند از آن استفاده کند
دبیرکل کتائب سیدالشهداء:
🔹
نفت عراق فروخته می‌شود اما آمریکا اجازه استفاده از آن را نمی‌دهد و آسمان ما نیز اشغال شده است.
🔹
آمریکا نمی‌گذارد برق از ایران یا ترکیه بخریم یا با چین و زیمنس قرارداد ببندیم؛ مصداق "نه می‌دهم و نه اجازه رحمت می‌دهم".
🔹
استقلال کامل عراق کجاست ای بزرگان؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/682446" target="_blank">📅 08:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های دلاری دولت، این رقم کفاف همۀ مخارج ارزی دولت از تیر تا دی‌ماه امسال را پشتیبانی می‌کند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/682443" target="_blank">📅 08:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
امکان ترمیم سابقه تحصیلی از امروز
وزارت آموزش و پرورش:
🔹
متقاضیان ترمیم سابقه تحصیلی سال ۱۴۰۵ می‌توانند از امروز (۲۸ تا ۳۰ مردادماه)، پیش از اعلام نتایج آزمون‌های نهایی، انصراف خود را در سامانه ثبت کنند.
🔹
ثبت انصراف در همان سامانه ثبت‌نام ایجاد و ترمیم سابقه تحصیلی و از طریق درگاه سنجش انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/682442" target="_blank">📅 08:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0838610e95.mp4?token=bXtreO7jI5jTQr04x2Q2VSHG0yqaxr72B5PWXfgFghIhxW8PjRkOVPcvUijRedaBpTP_96CBMJb_kq3Ot_Q6revUsUrhZVsP0cNye8wUnBGHe99ycM1nUSnu1I3kxucwF7PfN4evHE_O4GLgzF8UccRx7q-muFZAY7lTKu6SdjoLwsG7_4vQ4OmqLMXJ8LdK99hHpa8jH2zmIfItz7h1C31-Pr2cqEgxGR8_2X9wQoZbgOr34of5oLByjP0XIGSQWL12bTMIDQ8-BlaHqvSc2ZPBikWE4FK61vUBYn0PI5U6fQebSRsrZOVOys8bIwocKymiC4Vs0ToaxmrXlipBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0838610e95.mp4?token=bXtreO7jI5jTQr04x2Q2VSHG0yqaxr72B5PWXfgFghIhxW8PjRkOVPcvUijRedaBpTP_96CBMJb_kq3Ot_Q6revUsUrhZVsP0cNye8wUnBGHe99ycM1nUSnu1I3kxucwF7PfN4evHE_O4GLgzF8UccRx7q-muFZAY7lTKu6SdjoLwsG7_4vQ4OmqLMXJ8LdK99hHpa8jH2zmIfItz7h1C31-Pr2cqEgxGR8_2X9wQoZbgOr34of5oLByjP0XIGSQWL12bTMIDQ8-BlaHqvSc2ZPBikWE4FK61vUBYn0PI5U6fQebSRsrZOVOys8bIwocKymiC4Vs0ToaxmrXlipBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک کش پیلاتس تمرین موثر برای پایین‌تنه و تقویت عضلات رو شروع کن  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/682441" target="_blank">📅 08:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcAHESzcXbfLr36gXYRa2JDBJioveO-Cfi-sFjsfxh_QwsRCTfUnPaiL0MpubFMVHkFEeGl7PdmhjbKkf6fDlnQjHUyjdYNSJJ6cnQGw25B8T1jOAGSWw70wxEW-uB6G5RitorbfcAy6Bt74eeXICVB7FNwq8frO2z29UD4NqLhUxsTAE7p1XC1Rp3sTszLUViBwnnzqJfMkwdWIMiiOOI7xetOqku2dbKEwFsnf7xD1j_7lo-1n5gLaQzlW5z2kjOHsdEt94-PlPGgCbRZjQMvSNb_44edFswHx_lFa9r1duqvIv5v4QrAbBf5zTid_lM5OYhPAWxfVHW7LRGlUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش توقیفی امارات در راه بندرعباس
🔹
نفتکش توقیف شدۀ اماراتی که در کریدور شمالی تنگۀ هرمز توقیف شده بود، به سمت بندرعباس تغییر مسیر داد.
🔹
مقصد این نفتکش ابتدا بندرجبل‌علی تعیین شد اما حالا به سمت بندرعباس می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/682440" target="_blank">📅 07:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682433">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5HELbead846-TWh9TJzp0JUkhSBvIIxSUhiIEoZs3pG84vJMY9zSQPz9HBAP3jbLvbLGTshA4_EgULijGw5vO_FNFM7qn_C8PdK511k9OczmBdrufSJAFjJrIaBnS9ow0YMSCpIa5Pb1nhzLruejD5vLT4dWzfDzrVSagSe5Gpe9RqPocQhJOqWhzWVQ6spwyh53jt7AScWp9qea4COy0JxC6gJFOCFJlbGIO1hI3IvIZmGB18pUoK4n9D7NhNAXrqbTOi96g_y1qfbPAMbUELoYl16zOxJ-PfBiGX81d1lbh86vikO_EMb-vDOz27BVicjdnpiV53FdE1ldE9ccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۸ مرداد ماه
۶ ربیع‌الأول ۱۴۴۸
۱۹ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/682433" target="_blank">📅 07:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682432">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0v7kDK8d5zpsiIw2GaKpXBgfp24vvBiPqvqzipHdsZQ6G6pvYOtPhCzKq94lXRRGDe5pbAdz0Sr-HtWAW-4kFWxuJC9l58IEYLXzxBFJHxglQ-UEXWGLmcwZovBjjczvZpkCKNJBKve-DvFapDf_Vn7a-RcjOfi3qYHI9JJn25LB9SfYu0PfJxVSdQdreKAlvDtTLmUYCrRcEe2GMu4btLKlQFMclarrhPRy0VF_5VFwM4cgrt88LIVe3hXKKF0RL07Xq9VmYjqZwYYJIJn6tt4Z9smxoLkJC40PdVt7L1TTlySHzR4d13pXB6LojDWDuF4XfGbnVtjiuVf5iAe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی بزرگ ارکیده شاپ شروع شد!
🎉
این بار خرید از ارکیده شاپ می‌تونه براتون فقط به معنی خرید نباشه؛
شانس برنده شدن ۳ جایزه جذاب
رو هم دارید!
😍
🎁
🏆
جوایز قرعه‌کشی:
😍
👇
🥇
کرلی شیگلم | ۹,۵۰۰,۰۰۰ تومان
🥈
شیور صورت و بدن شیگلم | ۸,۳۰۰,۰۰۰ تومان
🥉
سشوار روونتا | ۷,۰۰۰,۰۰۰ تومان
🛍️
خرید کنید و شانس خودتون رو امتحان کنید؛ شاید برنده این ماه شما باشید!
💜
📌
ارکیده شاپ | انتخاب مطمئن برای خانه و آشپزخانه
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/682432" target="_blank">📅 02:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682421">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vsh7F22ywyRxuB3JqzHQTAng8w9irNvMnGd45pGfrH1MhqA4rkfcZBVmIl4gpZ-vWWM2amPCxD-33kZ_8wUM0DvgzN_S65H4pyeR76on1z2231_cAaxcv6jUFN4BzYEYvguH_6aqjwILsHyjGakgcIJz8NtPMlAw1Y-cqUaoh83xdT-NTMqD9SLNSYPrrTVqkgcnDOFR0A6GlPwUY8bn1JcqyKqbXJ1YlK-joUBIJ6PJwOMl_NcvtTJzKzKGPktegEoL68K_n3DEmCZgdzbR7Yr17ifOzP5-uwzcUd83grVJnet7kUT6JtMg1jKtAfrpolAb3151mSzWi7heJxaL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3Q_b52eUXlVkNZhmuhSLNE4o2HFxvikyWky5k-5CTJ20uOifEHd_qHiTlL2ssq7TiRAmrLRU0KzWllsFr2uCEpTZqeBbEOUSwCZH1g_17kZLl05Q7Zrku1pf_klk4YnKrxxjI2Ocyi3LibYKT95LdJI7eDq6-g2jN2e67B4uEYjwrk-2XXFHm2iHrfxLUYKku-A_4hXczMATB1lW2Nh_wrV6rGwtt1Ln8Rio8u19i-5-WIfBbgftppOqcPBDiAQpcMMujuXRslAvivxXniljY5xuQEN73kOaXlvcH3JpK8bQIRui2dv9Bze5tEA-_Soc9o5pT4quYDWdYjuzU8k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WenJgxIYGemhmqSeSMiPQu3LQMpi_L0tOaz0HidaTIPZwQp37WffRPIbds_ikel2zyuOceIOC_CEP674bxplBW1TWqcBH1XqFmQOICCHbPwFczZMzwcK6EHCyYlGZ2YXUt2gA5IrADF3OJLqWV2TxAGoAOv0faVLbbhY6Cr3v9uufUCA4NZqGK180giMfzBIRgdSbaJoUNDvtIHtRVSdbv9XI8UMiluLM8BV2odeqvmzt6_a-5ThsNF19HyGZ6vAGUwThTgezX-3OFkfdps0ph51yI3JntHD1u1NEE7gIE1O5_SeKyFWln-Rj1YNG0BIux50-GxEn5ALBNA4ADaKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd86yd0rL4iEU4kIm-LhR-xYY3uVzhQGXJu76akRrBfBkWZlGDBU7r_jjgKUghEqkIrGHdWqov3v6BKtmK_5mYb-vOnpPYimfOpzhkERQFrqPjC_CEUDlRe0lH56o74XlKFKTkzo37qLTTXHsEonhy0wwPJgzl2feYRa0aINJ8erNaglFsNnO1oTH0F4YnCS8KOOnuMfMNyVRJuRmxpp_aMYNHjAJq6uf88dlr867yEeOzOpRau1cRUGB1FcWBQCDCmJgiQ1ucahBE-KD6TgIucB8U73Pgb6iK_1gU5yubBTYXeS2a4gwb1L0UJSNbM_FAFe7HQ5b7qGMo_UpOKY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5b3epq1YSrS_fZF4CJwYOxrE39AQtQioE5CC56JRr4x5-U4sD9e_0tHw-OgHuKifLKPej4_NpKOp_LVm3r8WXOGDvv80co-yH5gUeBmj9gYi5X7rOlteUbZZAYu4PS0Su1niGYRuzJYIrcsjOaZ-DSaPQPI9ATiSnZ999ZFPGRtVjGk7obIUR9lHQg6j-XG1SXp3XWiehbuTZEOHWBleiNilJ785iPVDTh2BQdrY0BErnKyUXY1BQb3vG0KKdqxjdom1Td9yJd4RiEo9Axyn2S_nD42TrQ8a4LYlM0-UyHg5N7u8-t2YyZPbp2CcW7uGL4QGQmxEO7C4_OpjJ6qlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ سلاحی که واشنگتن دیگر به اندازه کافی ندارد
🔹
برای سردمداران آمریکا باورنکردنی بود که جنگ با ایران این‌گونه ذخایر نظامی آنها را تخلیه کند.
🔹
حالا همین داده‌هایی که در این اسلایدها می‌بینید به مهمترین نگرانی کاخ سفید تبدیل شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/682421" target="_blank">📅 01:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_cgjt2bSWTtL0DA8n6J5v0NlRKIkhgo3m6e03A8twVsxjNfRqxbvXZ5lIqspBrxI4IKB9zfk4BSYWXtBWRCBrptmE8HDG9FdKb8AWZbIJmVrieHF210KZZ0SS30GyvVtxHbKPvywjYOyYdqHPhLgzcO2FF3XndVuuQDjwWUAwk0O_KOaGUbrjwJJ4Rch-7bUs3YOU6eR4j1A3stAzNlt-sw4lHxjycA7hPS9IFoDfjOoT7dIVkK0pi3SEsS4a2q6G3fGXatu1my9yVGroFUttj8yD8HN5vRU_J_k0RnOSg5OuvMJyklFfZFQjeDY3rtLuFQt6QCPpbpdUR6RJhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوتیوب شمارش بازدیدهای ویدئو را زیر و رو کرد
🔹
از ۲۴ آگوست (۲ شهریور)، یوتیوب روش جدیدی برای شمارش بازدید در نظر گرفته است؛ از این به بعد همین که کاربر یک ویدیو را پخش کند، یک بازدید ثبت می‌شود و دیگر لازم نیست چند ثانیه از ویدیو بگذرد تا ویو محاسبه شود.
🔹
این سیستم که پیش‌تر فقط برای YouTube Shorts استفاده می‌شد، حالا برای تمام محتواها؛ از ویدیوهای طولانی گرفته تا لایوها اعمال شده است؛ درست مشابه روشی که تیک‌تاک و اینستاگرام استفاده می‌کنند.
🔹
یوتیوب برای محاسبه درآمد همچنان از معیار قبلی استفاده می‌کند. یعنی از این به بعد ممکن است یک ویدیو ویوهای بیشتری نشان دهد، اما این به معنی درآمد بیشتر نیست/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/682418" target="_blank">📅 01:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59505881fa.mp4?token=AoVKTCt6lm_3qpBTg21orBwa5CF-_i6P7L0f1t2uGIdrQNSk_OvFeitPfVngFoK0sQ1HUQ4t26MJpNpn7KvPmrj0CYc7UkqucDF3sbIeBhR1wzUmJtm3zmtoquzPdbjDB34T9KTRJbulUFvPf5_meHaM3UPUZTXN66Gb9EWJIY9BDAIoGXaaO1aDY3PwpUpqbpfKPEnH6-TncC1LPzNMxok1Bchprnpd-yAJXIQM4Coi2B6xHiyZBkhHYF3yhj2kwVbW9p5dbPRCOoMvgh1J9K1fZiqu5DPCthX7z6VTqEmtnqvjohUSII2DPSuyqY8a8CsoY1wa5ZYhjf_-p8YloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59505881fa.mp4?token=AoVKTCt6lm_3qpBTg21orBwa5CF-_i6P7L0f1t2uGIdrQNSk_OvFeitPfVngFoK0sQ1HUQ4t26MJpNpn7KvPmrj0CYc7UkqucDF3sbIeBhR1wzUmJtm3zmtoquzPdbjDB34T9KTRJbulUFvPf5_meHaM3UPUZTXN66Gb9EWJIY9BDAIoGXaaO1aDY3PwpUpqbpfKPEnH6-TncC1LPzNMxok1Bchprnpd-yAJXIQM4Coi2B6xHiyZBkhHYF3yhj2kwVbW9p5dbPRCOoMvgh1J9K1fZiqu5DPCthX7z6VTqEmtnqvjohUSII2DPSuyqY8a8CsoY1wa5ZYhjf_-p8YloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمریناتی ساده برای تقویت و هماهنگی چشم و دست، تمرکز و سرعت واکنش ذهنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/682415" target="_blank">📅 01:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMl9v39cAw7wO9VcRW061XFgfHPYKRSy00GCmCRG1QUDYKowfJCDeCMItQxQdeo5NO-9KyDkj1Gb1mJ5x5wOAHtv7j4Co4V43fntdtmNdNSIyOm8AXP7_mkZOFU0lVORWOfw8mq4A-dVgS7x7Xy_ofAjQIASlC_KgFwpEtxlvJh-Cq6fdttY1Fv5pXT9lWpkquCXV1yhaAkQHjEm9o7100ksSQgYOjsSmP0aT-eXSKZ1GoIimeqAV17NJ3MHQwt9iRv6I67kIcoaGsbs1utOfovToIcpKH1IXoFGW64dYZs0C7OFTUxQ4Vd9V7e_mXhBD1kz2X9fFdkSK78_y6NUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: هنوز لباس ترامپ بوی آشغال غذای هواپیما می‌دهد آن‌وقت ادعای تصاحب تنگه هرمز را می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/682414" target="_blank">📅 01:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ذخیره استراتژیک ۷۳۵ قلم داروی حیاتی در کشور
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
۷۳۵ قلم داروی حیاتی و ضروری برای ذخیره استراتژیک انتخاب شده که حدود ۲۴ همت برای تامین آن‌ها اختصاص یافته است.
🔹
بخشی از کمبودهای فعلی دارو ریشه در مشکلات انتقال ارز در ۴ تا ۵ ماه گذشته دارد.
🔹
هند در تامین دارو همکاری مناسبی داشته، اما محدودیت‌های دریایی و هوایی، انتقال برخی محموله‌های دارویی از هند به ایران را با مشکل مواجه کرده است.
🔹
۵۸ نوع شیرخشک، از جمله انواع مورد نیاز بیماران خاص، در ذخایر استراتژیک قرار گرفته است.
🔹
شهروندان برای پیگیری مشکلات دارویی می‌توانند با سامانه ۱۹۰ تماس بگیرند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/682413" target="_blank">📅 01:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682410">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae15cbe36.mp4?token=jnEGFiKxX5IBqKG4OSs9JnjX9i7tABRuKzXuFZXA0BkGUYmPicwweFPpOZQQZ8nMcfBCGz1c3qprWgdjtB2fgdYQ7nontDlh6fuCwTdg5g_zEPF1y5oQRdOWmfFphr23vLLyGpbwh7w_tNpr7JgSz0UznsR4kdwpZ4VPou6fDldbhQLolCbl8GK69JBwg_x8ehUG1dtgzF1tHncZ2rzUkuWjtNkBSMsexR8IpsVYhEUt_gDVgU98A2bjy8lY4WVK2oeQrf3XKSLunFDKhM8xXt0UaKCm5IK7jID3E_36Qv0IBwO6VetCYsPI9zwaIJ3EzPm2n-a5k92wHTGunrflig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae15cbe36.mp4?token=jnEGFiKxX5IBqKG4OSs9JnjX9i7tABRuKzXuFZXA0BkGUYmPicwweFPpOZQQZ8nMcfBCGz1c3qprWgdjtB2fgdYQ7nontDlh6fuCwTdg5g_zEPF1y5oQRdOWmfFphr23vLLyGpbwh7w_tNpr7JgSz0UznsR4kdwpZ4VPou6fDldbhQLolCbl8GK69JBwg_x8ehUG1dtgzF1tHncZ2rzUkuWjtNkBSMsexR8IpsVYhEUt_gDVgU98A2bjy8lY4WVK2oeQrf3XKSLunFDKhM8xXt0UaKCm5IK7jID3E_36Qv0IBwO6VetCYsPI9zwaIJ3EzPm2n-a5k92wHTGunrflig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی یک ویدیوی آموزشی؛ ۳۷ میلیون بازدید برای درس موز یک معلم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/682410" target="_blank">📅 00:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
وزارت خارجه امارات: تا اطلاع ثانوی، تمام مبادلات تجاری و تراکنش‌های مالی با ایران متوقف شد/انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/682409" target="_blank">📅 00:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وزارت نیرو: خاموشی‌های خانگی تا دوهفته دیگر به حداقل می‌رسد
مصطفی رجبی مشهدی، سرپرست معاونت برق و انرژی وزارت نیرو در
#گفتگو
با خبرفوری:
🔹
با توجه به شرایط فعلی و آسیب‌دیدگی بخشی از نیروگاه‌های کشور، خودمان را مکلف می‌دانیم برق صنایع را به شکل مطلوب تامین کنیم.
🔹
محدودیت‌های برق در بخش خانگی احتمالا تا دو هفته آینده به حداقل مقدار  می‌رسد، اما در بخش صنعتی همچنان محدودیت‌هایی را خواهیم داشت.
🔹
سازوکاری برای تامین برق صنایع فراهم شده و مشترکان صنعتی می‌توانند در شهریورماه، با خرید برق آزاد تا سقف تعیین‌شده از طریق تابلوهای برق آزاد و برق سبز و همچنین گواهی‌های صرفه‌، برق مورد نیاز خود را تامین کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/682408" target="_blank">📅 00:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682407">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQkXCXnFVvRj_F4x2GnB_YVh3kOnZdvt0x3svuVjKtJa7YiQSSyC3fJCEBQmtqSWU0h2kXCI0rFVynfxhZj9qsXqOivkgohkS6xXbL8hwHuN4n5oGDTvEbt_iBv-OTFh57091elHdnHVDCUwjmeFoQd401U3keszlL-jtX2s41sJUVSLR2fKEfcSYx0ut5gdBN5Y3lgYfwisq450t6VcHhiPcCAzWCfvKMqLZw6Tl2arokaD72F7o_0NkoYvF0qfV3dcrB7g2D6ynMJfba9pDs_vhcXYzYOq9FO2TOtscJOFQPYn1FP_rH8C9axBj7klOFFqsDjDqwnk-9NeIrAPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواستفاده از رنج مردم در اینترنشنال؛ اینبار بیماران پروانه‌ای
🔹
شبکه اینترنشنال پس از پوشش اخبار مربوط به حملات به زیرساخت‌های برق ایران، اکنون گزارش‌هایی را درباره وضعیت بیماران پروانه‌ای و تأثیر قطعی برق بر سلامت آن‌ها منتشر کرده است. اما جای سؤال اینجاست که دلسوزیِ امروز این شبکه، با توجیه بمباران نیروگاه‌ها در دیروز چه سازگاری دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/682407" target="_blank">📅 00:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سی ان ان: ترامپ استراتژی خود در قبال ایران را تغییر داده و به فشار بلندمدت متمایل شده است
سی ان ان:
🔹
ترامپ به نمایندگان ارشد خود دستور داده است که مذاکرات با ایران را متوقف کنند، که نشان دهنده تغییری عمده در استراتژی اوست.
🔹
کاخ سفید از تلاش برای تحت فشار قرار دادن ایران در بازه کوتاه مدت فاصله گرفته و به سمت تلاش بلندمدت‌تر برای خفه کردن تهران از طریق فشار اقتصادی و نظامی مداوم حرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/682406" target="_blank">📅 00:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
با فروش مهمانسراهای سازمانی کسری بودجه دولت صفر می‌شود! / حاجی‌بازاری یارانه می‌گیرد و می‌گوید «آقای احمدی نژاد گفته پول امام زمان است»
مهدی پازوکی، اقتصاددان در
#گفت‌وگو
با خبرفوری:
🔹
۳۱ استانداری و دانشگاه‌های علوم پزشکی در تهران مهمانسرا و ساختمان‌هایی دارند که نگهداری‌شان هزینه‌زاست و گاهی به محل اقامت بستگان مسئولان تبدیل می‌شوند. اگر جای دولت بودم، این‌ها را می‌فروختم و برای مأموریت‌های اداری هزینه هتل می‌دادم.
🔹
خانه‌های سازمانی در پایتخت و مراکز استان‌ها هم نباید رایگان باشد. به‌جز مناطق نظامی و عملیاتی، ساکنان باید بخشی از حقوقشان را بابت آن پرداخت کنند تا منبع درآمدی برای دولت شود.
🔹
با شوک‌درمانی مخالفم. اگر قیمت بنزین از سال ۱۳۹۸ هر سال ۲۰ درصد بالا می‌رفت، امروز حدود ۷ تا ۸ هزار تومان بود و بدون شوک، به منبع درآمدی برای دولت تبدیل می‌شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/682405" target="_blank">📅 00:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682401">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc736f68b.mp4?token=Zbc7L-5e3qVpPggdfAmtRWBv5u3ClCU-JHnYcU07a_Mto1rtkVIUL899ZiHdQ7VVD5igLEynTbcBp47kj2xlnzZPS7txDJCr0O64beJvkI9Z_t8IsRPtzEV3fDrqtvYJmJ-ihJq0dbwpYxwaTja_1eCgeALZU6-CsB7AUkY8rFj_5Ud3anG7x2jHMtrUsIBZvNbhS7Tg397nPPKPnHKPELJbVTLYcqxQ60VMN6cTWKkMatojnuctFS_97WAgCmXq-Pu3FKh0VkNtZXkyPZA4ytXxWEntumEKGUBjkD4LRcqt9VQwCGNORJ2q9c6RWg82h-1Amuo3NYBnSVmeAlEZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc736f68b.mp4?token=Zbc7L-5e3qVpPggdfAmtRWBv5u3ClCU-JHnYcU07a_Mto1rtkVIUL899ZiHdQ7VVD5igLEynTbcBp47kj2xlnzZPS7txDJCr0O64beJvkI9Z_t8IsRPtzEV3fDrqtvYJmJ-ihJq0dbwpYxwaTja_1eCgeALZU6-CsB7AUkY8rFj_5Ud3anG7x2jHMtrUsIBZvNbhS7Tg397nPPKPnHKPELJbVTLYcqxQ60VMN6cTWKkMatojnuctFS_97WAgCmXq-Pu3FKh0VkNtZXkyPZA4ytXxWEntumEKGUBjkD4LRcqt9VQwCGNORJ2q9c6RWg82h-1Amuo3NYBnSVmeAlEZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدمحمد خاتمی: فرصتی که در تفاهم‌نامه ایجاد شده اگر از دست بدهیم دچار مشکلات عجیب می‌شویم
🔹
تفاهم‌نامه نظیر ندارد، بعد از جنگ‌جهانی دوم هیچ سندی که به امضای رئیس جمهور آمریکا رسیده باشد اینقدر امتیاز به طرف مقابل نداده، ما در موضع عزت به این‌ تفاهم‌نامه رسیدیم
🔹
دو عامل باعث شد در جنگ شکست نخوریم؛ یک عامل سپاه، رزمندگان و مقاومت بود که کارستان کردند، عامل دوم، مردم بودند؛ همین ۶۰ درصدی که ناراضی هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/682401" target="_blank">📅 00:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlPLUmlCFb5yITVDbS6OKFs8VowSDbQZuO2GU-138LpEGG7JLjbY5AkSufg4MhldwD8qIDpZyoo1urKzy3Buc6P0hu1X28hQ-zWjS5shaVnB0MqbVQH_Y6XrV0nwYcB1UGmLmTTu0rbxOGUPkUmbabMkPiv_9ehb6lrBAuSXtx2DDJEVZiPdW3RNLFkjKKgYBePkMtHQNqjBmRtPPC8tPPw70WlMM3HMCkKlyLQRJxHiJeaexAHIesN24FaY062Wm3QSAnDq4FAqkw-gscqxFp4XFTDNikmNx5nNMYmDHZbQbI9mc9AduQeHVj2DVoEgxyMtYXJlx88F5CxaGvoYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/682398" target="_blank">📅 00:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbceb5ec7.mp4?token=kL-DrorHekY0xq1Zzf28_MMeGKGgWIfbYNgjkVuoEOwmTsuLIoQhjD5WcEwTp_pAf3FcZOPgVWJ3JDqG-OvxFtyzC7AjIZrbfuA9ONDrKicr6RX0BbGkVlnaSiPYjFFcVpNYCCCFkYSLMrjCxtioi7MMRYvJUUyMcsjsiUAV2v-eU7NcaCLtkUNFpB26RoUZaj_xqwOGIKpMO94Rtw0ozANQV5GBpbzm49rfGk8F4SKlXV3EKP8eIRiGlu_65EKFRa_t--4AvxwOxm-e8Fv5lKJOLT7k40mHIxz0BSUNVdaBzzQQMLA6dyt0if8ZctCyHNw2NngbgCRIdQYva5ygMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbceb5ec7.mp4?token=kL-DrorHekY0xq1Zzf28_MMeGKGgWIfbYNgjkVuoEOwmTsuLIoQhjD5WcEwTp_pAf3FcZOPgVWJ3JDqG-OvxFtyzC7AjIZrbfuA9ONDrKicr6RX0BbGkVlnaSiPYjFFcVpNYCCCFkYSLMrjCxtioi7MMRYvJUUyMcsjsiUAV2v-eU7NcaCLtkUNFpB26RoUZaj_xqwOGIKpMO94Rtw0ozANQV5GBpbzm49rfGk8F4SKlXV3EKP8eIRiGlu_65EKFRa_t--4AvxwOxm-e8Fv5lKJOLT7k40mHIxz0BSUNVdaBzzQQMLA6dyt0if8ZctCyHNw2NngbgCRIdQYva5ygMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر حالت خوابیدن روی کدام بخش از ستون فقرات فشار وارد می‌کند؟
🔹
روی شکم خوابیدن هم به مهره‌های گردن و هم به مهره‌های کمر فشار وارد میکند و به مرور باعث آسیب به آنها می‌شود.
🔹
بهترین حالت برای خوابیدن به پهلو با قراردادن یک بالشت کوچک بین پاها برای حذف فشار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/682397" target="_blank">📅 23:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682394">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در رنج مردم صرفه‌جویی کنید!
🔹
این روزها بیش از همیشه باید صرفه‌جو باشیم... اما نه فقط در آب و برق و سوخت.
🔹
باید در آزار دادن مردم صرفه‌جویی کنیم. در تصمیم‌هایی که بی‌دلیل زندگی را سخت‌تر می‌کنند، در بخشنامه‌هایی که جز اضطراب و سردرگمی چیزی به جا نمی‌گذارند.
🔹
در آزمون‌وخطاهایی که هزینه‌شان را مردمی می‌پردازند که خودشان مدت‌هاست با حساب و کتاب زندگی می‌کنند.
🔹
باید در ساختن دوگانه‌های دروغین صرفه‌جویی کنیم. در اینکه مردم را مقابل هم قرار دهیم، برای هر مسئله‌ای دشمنی بتراشیم و جامعه را میان «این» و «آن» تقسیم کنیم.
🔹
این سرزمین بیش از آنکه به شکاف تازه نیاز داشته باشد، به اندکی آرامش و همدلی محتاج است.
🔹
باید در حرف‌های اضافه هم صرفه‌جویی کنیم، در وعده‌هایی که عملی نمی‌شوند، در شعارهایی که سفره‌ای را رنگین نمی‌کنند و در تصمیم‌هایی که هزینه‌شان را مردم می‌پردازند.
🔹
این روزها کشور به تصمیم‌های بزرگ نیاز دارد، اما پیش از آن به عقلانیت، مسئولیت‌پذیری و ملاحظه حال مردم نیاز دارد.
🔹
صرفه‌جویی فقط کم کردن هزینه‌ها نیست؛ گاهی یعنی کمتر رنجاندن، کمتر تفرقه انداختن، کمتر تحمیل کردن و کمتر خرج تراشیدن.
🔹
در روزگار سخت، هنر مدیریت این نیست که بار بیشتری بر دوش مردم بگذاریم، هنر آن است که خودمان بارهای اضافی را از دوششان برداریم.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/682394" target="_blank">📅 23:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682393">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرسونه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUAcIIMabwG6TrMH-lPZitXW0X8yLhg6KX7_5P5XGRhnKWJw-sdznUiB6dMSQn849v5pCzFsG3xH83p1Brhqm6tHZOGA5kH5ZEs4z63qt4BDTe9PCeHkmhghYww7JK0Jn7nu9BAPVh8cfZErnIaVfe1YhWe8m_L0j5fIHqwcTfz_dAqw_I9x5L50Vi88PQzPgndQja3PYx9mU7_fWKb7Z7oCtXDgbsTaJm4pCYTitV3Iw-G6cElzdH8P-Pfrf00tDJ-NR9kod9z6FqpMl3X_dbFi19Y9sRxoCIHne1YmPCpCBuygNGazZhXKHd5xG1FA8XMyDvnDwnY8o3kQDCkhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکار بیک؛ حامی آموزش و یادگیری دانش‌آموزان ایران
🔹
آموزش تخصصی و رایگان پایه اول تا نهم
لینک کانال های درسونه
👇🏽
اول دبستان
👈🏼
@darsoone1
دوم دبستان
👈🏼
@darsoone2
سوم دبستان
👈🏼
@darsoone3
چهارم دبستان
👈🏼
@darsoone4
پنجم دبستان
👈🏼
@darsoone5
ششم دبستان
👈🏼
@darsoone6
پایه هفتم
👈🏼
@darsoone7
پایه هشتم
👈🏼
@darsoone8
پایه نهم
👈🏼
@darsoone9
آموزش زبان
👈🏼
@en_darsoone</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/682393" target="_blank">📅 23:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
باکو: خبر سی‌ان‌ان درباره استفاده اسرائیل از خاک آذربایجان برای حمله ایران صحت ندارد
ادعای آذرنیوز:
🔹
آژانس توسعه رسانه‌ای آذربایجان (مدیا)، سی‌ان‌ان را به انتشار اطلاعات نادرست در مورد ادعاهایی مبنی بر استفاده اسرائیل از خاک آذربایجان در طول جنگ با ایران متهم کرد و این گزارش را یک تحریک سیاسی علیه آذربایجان و امنیت منطقه‌ای توصیف کرد.
🔹
مدیا در بیانیه‌ای اعلام کرد که سی‌ان‌ان در ۵ ژوئن ادعاهایی را با استناد به آنچه «منابع» خود توصیف کرد، منتشر کرده و نوشته که اسرائیل در طول این درگیری از خاک آذربایجان استفاده کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682392" target="_blank">📅 23:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53e129d07.mp4?token=oB1-l0sOHw5benCcVGeXfTQXUgdZJsO0PTDmSlRCpRtLLzbLXa7o_MbPjD0z8Rc-9SCVxyIdSPRXDQ1E4VDS1W8awKwbTKzInvDMxh4EnNHV92ob-EV6m1ku8cesmpsVuKbioRy0lX6Csn0J2JecqUAABJb6gAEEohXiqN08NSWcxBs1LXsaecbBw3vlfWvoSDFekVm8582qj2-8JWdMf4bRG-LFlhk4oyQoFo1hQKvrIMm5ouV46H3wHSfRDxEAuM3i0zDF7NurLyK7wSr70EbH5sxX9_gETqQmzqce8rMdpFp4cKQeooQJvDf6gabf4ZUp_NTmGzuB5bP8u56TYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53e129d07.mp4?token=oB1-l0sOHw5benCcVGeXfTQXUgdZJsO0PTDmSlRCpRtLLzbLXa7o_MbPjD0z8Rc-9SCVxyIdSPRXDQ1E4VDS1W8awKwbTKzInvDMxh4EnNHV92ob-EV6m1ku8cesmpsVuKbioRy0lX6Csn0J2JecqUAABJb6gAEEohXiqN08NSWcxBs1LXsaecbBw3vlfWvoSDFekVm8582qj2-8JWdMf4bRG-LFlhk4oyQoFo1hQKvrIMm5ouV46H3wHSfRDxEAuM3i0zDF7NurLyK7wSr70EbH5sxX9_gETqQmzqce8rMdpFp4cKQeooQJvDf6gabf4ZUp_NTmGzuB5bP8u56TYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک گروه در آمریکا به‌جای توپ با ماکت شبیه سر نتانیاهو فوتبال بازی می‌کنن
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/682391" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682390">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d5136558b.mp4?token=a_UhoJKn3uV5wWXf4rNC-REGnmplCPk8YFDwJHtIns1CbgVx3U6HCd07VHXm4D8QsCPDbWDSuVu_T-1s8Hlh2OkyauMmefQD-Ac088ugd2AEN2g5ziQO0ysjBHnWbCTVENR6EMn5sG2CY3oncTqbXEWhKoTPqpd_5-OpIlnlEnYTKOYz1yZk3w4EWX_lDzVMea7lq6-4lJ_7QUJ8DitdnqedMXPUO4aiPZ3ioIPGxb1Gx253njQBVmHHFJ5BR07ju0iRwT_nqSSlxV8rFYd3rTK0SCvFk2fvUPtHs0y_ZdhfX-IUxNIgrr50Pd3jiRmDwfj5mljRIC8iGYJHcfPzXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d5136558b.mp4?token=a_UhoJKn3uV5wWXf4rNC-REGnmplCPk8YFDwJHtIns1CbgVx3U6HCd07VHXm4D8QsCPDbWDSuVu_T-1s8Hlh2OkyauMmefQD-Ac088ugd2AEN2g5ziQO0ysjBHnWbCTVENR6EMn5sG2CY3oncTqbXEWhKoTPqpd_5-OpIlnlEnYTKOYz1yZk3w4EWX_lDzVMea7lq6-4lJ_7QUJ8DitdnqedMXPUO4aiPZ3ioIPGxb1Gx253njQBVmHHFJ5BR07ju0iRwT_nqSSlxV8rFYd3rTK0SCvFk2fvUPtHs0y_ZdhfX-IUxNIgrr50Pd3jiRmDwfj5mljRIC8iGYJHcfPzXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده محیط‌زیست ایران در بریکس از خجالت اماراتی‌ها درآمد
🔹
خورسند، نماینده سازمان محیط‌زیست در اجلاس بریکس به سخنان وزیر امارات درباره حملات ایران به مواضع آمریکایی در امارات واکنش نشان داد.
🔹
هر کشوری با میزبانی از متجاوز و زمینه‌سازی برای حمله به ایران، بدون تردید با عواقب عمل خود روبه‌رو خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/682390" target="_blank">📅 23:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682387">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617832e930.mp4?token=nvALOG4CaiTNWaBrZir38PgXkmOtGQYCxvCi7hf4AXh-PulsGldfgBN8J6RrJfZBUCO4GXc8kOWGj97gS6aZy0wp6N_YoJOT-xkfXfHsop63rdx33gbxsHkOdqvP2hx_Zduoce2T-ApdW9_aJGfx6a555pt1HpHTk9T83VBz1ordjNaMVenoDxsweoVUHDmJ80yxVr7ctlpu6H7zG89RSriL_PI7g58jsLvR9PlfJ0YVICA8gg7A3X0S4afQDwencC-a69B-h2uAWyo9MZlJS9V0MgxyUnmfI4Ie3qDfyhdoQRT45-OiYUJ2Edjp4BsFVA4IP6wOx3ZFbSmB_iDmYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617832e930.mp4?token=nvALOG4CaiTNWaBrZir38PgXkmOtGQYCxvCi7hf4AXh-PulsGldfgBN8J6RrJfZBUCO4GXc8kOWGj97gS6aZy0wp6N_YoJOT-xkfXfHsop63rdx33gbxsHkOdqvP2hx_Zduoce2T-ApdW9_aJGfx6a555pt1HpHTk9T83VBz1ordjNaMVenoDxsweoVUHDmJ80yxVr7ctlpu6H7zG89RSriL_PI7g58jsLvR9PlfJ0YVICA8gg7A3X0S4afQDwencC-a69B-h2uAWyo9MZlJS9V0MgxyUnmfI4Ie3qDfyhdoQRT45-OiYUJ2Edjp4BsFVA4IP6wOx3ZFbSmB_iDmYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای بیلبورد جنجالی در اسرائیل که در فضای مجازی سروصدا به‌ پا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/682387" target="_blank">📅 23:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682384">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تلگرام در حال تبدیل حساب‌های کاربری به وب‌سایت است
🔹
مدیرعامل تلگرام در حساب شخصی خود نوشت که تلگرام برای گرفتن دامنهٔ سطح بالای «.gram» درخواست داده است.
🔹
اگر این درخواست از سوی سازمان آیکان (ICANN) تأیید شود، حدود یک میلیارد کاربر تلگرام می‌توانند دامنهٔ شخصی خودشان را داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/682384" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682382">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یارانه ۷۶ میلیون نفری وبال گردن دولت شده است/ هر کس یارانه می‌خواهد، برود تحت پوشش کمیته امداد
مهدی پازوکی، اقتصاددان در
#گفتگو
با خبرفوری:
🔹
پیشنهاد من این است که دولت اعلام کند هر کس می‌خواهد یارانه بگیرد، تا سه ماه دیگر برای قرارگرفتن تحت پوشش کمیته امداد اقدام کند. آن‌وقت خیلی‌ها، از حاجی‌بازاری و استاد جراح تا استاد دانشگاه و نماینده مجلس، دیگر مراجعه نمی‌کنند.
🔹
یارانه حدود ۲۰ میلیون نفر تحت پوشش کمیته امداد و بهزیستی باید حفظ و حتی افزایش یابد. اما چه دلیلی دارد به فردی با دو خانه، ویلای شمال یا سفر خارجی یارانه پرداخت شود؟
🔹
بودجه مجلس از ۱۶۰۰ میلیارد تومان در سال ۱۴۰۱ به نزدیک ۱۲ هزار میلیارد تومان رسیده است، اما در سیستان‌وبلوچستان هنوز دانش‌آموزان تخته‌سیاه و نیمکت ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/682382" target="_blank">📅 23:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682381">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dadb004324.mp4?token=t5bxXhe_KiXm7e4S2dunMBHgOPPdgprCqibXHbUs5UMg7YZO0Sv-vAF_Xw-d32MIGifN_FlLGmaYoetlQFYE17YN55a7qdUWe1BBW6bHOcmEuobh227I9Uc5x_MDy91HX2wAdHIYuC5yTcHQZXFsyp8j1xv4AboaHLamBQmKIRJaPvVt15PB6YkTVdQfp84PkjJ3bwVniz6nFke02XcOD-RCxYDEaj1YIZoUb-es5e2fj-acb15CBRORoe-8q8lSoklpA8CzVNWzjx3vQXfk2Hbm38yXGvzFGEM8wK0pN3HUHdLNmmcPnoZK4M0Qf_YlJBYyB_b_I6lM1_XGcMZ-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dadb004324.mp4?token=t5bxXhe_KiXm7e4S2dunMBHgOPPdgprCqibXHbUs5UMg7YZO0Sv-vAF_Xw-d32MIGifN_FlLGmaYoetlQFYE17YN55a7qdUWe1BBW6bHOcmEuobh227I9Uc5x_MDy91HX2wAdHIYuC5yTcHQZXFsyp8j1xv4AboaHLamBQmKIRJaPvVt15PB6YkTVdQfp84PkjJ3bwVniz6nFke02XcOD-RCxYDEaj1YIZoUb-es5e2fj-acb15CBRORoe-8q8lSoklpA8CzVNWzjx3vQXfk2Hbm38yXGvzFGEM8wK0pN3HUHdLNmmcPnoZK4M0Qf_YlJBYyB_b_I6lM1_XGcMZ-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش میدانی حسین پاک، خبرنگار حوزۀ مقاومت از تشدید حملات رژیم صهیونیستی در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/682381" target="_blank">📅 23:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682379">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLyIT1piYsePXtugDWWIFfzTDixW2Q9BNz6DTm2YkQjl27tmpPdnd-C_xoJ7_lTHkEd24vB8NyAhOIdWmfV80Hyl56nmjrFPyh8CYS81GPCI3da4TMpa6cQrU24X0N5HhfQyELo8NixoT_qKTpWg-M_vUCuYy0XuBQLgE4t8njGNLr1-OYj6VT4nwh_soQu3zcAWTCk7rY8Gf1LxGy0thhFpZYsjjgGk3ipJyWZrie2B5p_NBuGXSc-ETmsV-KVve0xHhnfdQZ8MLM9v4mRNytAqxCr8y1O6EQ5jL1wTaigdEOrwxI2HEe9uggqF8i6NWbNslQ_JnUY6RUF7aOi_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین مجتمع‌های پتروشیمی ایران بر اساس ظرفیت اسمی
🔸
پتروشیمی بندر امام با ظرفیت اسمی ۶.۶ میلیون تن در سال، در صدر بزرگ‌ترین مجتمع‌های پتروشیمی کشور قرار دارد.
🔸
پس از آن، پتروشیمی اروند با ۲.۸ میلیون تن و مارون با ۲.۳ میلیون تن در رتبه‌های بعدی جای گرفته‌اند.
🔸
در بخش محصولات تخصصی نیز پتروشیمی زاگرس با ظرفیت ۳.۳ میلیون تن، بزرگ‌ترین تولیدکننده متانول ایران و از غول‌های این حوزه در جهان است.
@amarfact</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/682379" target="_blank">📅 23:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682378">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963f08ec7b.mp4?token=QPwYiNj7Y4jjWjUE9_W-y5BaQVKyYtX-uP_duliP3mapFTQ8h3DCBWRv8C6rzRXQGqGaQdDhPS4NlF5S52Ayxk79cVS44xJOesPf97Kv11vm4G_4_0QBUUpwJRzgaMRV48XaYGwPo-SAR6obhBaOpqR8BoHjZkA7f_kwAVTQpWJLj3SaMdUE-qmjtDIW8IP8RF1ESmGAQryxDmD6BeEZ41YT6HRcAyFG7lSbLx_mbyk32aIExS_PYs4mqo5rgMugYme6z_lOaOu0t1O6bwa_QyydFFB9EEGXw6yduC6XHbUoDIdDWfo8M-Dzs0ScPs_fRHKNQj9x4i5bKYr3qA-DKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963f08ec7b.mp4?token=QPwYiNj7Y4jjWjUE9_W-y5BaQVKyYtX-uP_duliP3mapFTQ8h3DCBWRv8C6rzRXQGqGaQdDhPS4NlF5S52Ayxk79cVS44xJOesPf97Kv11vm4G_4_0QBUUpwJRzgaMRV48XaYGwPo-SAR6obhBaOpqR8BoHjZkA7f_kwAVTQpWJLj3SaMdUE-qmjtDIW8IP8RF1ESmGAQryxDmD6BeEZ41YT6HRcAyFG7lSbLx_mbyk32aIExS_PYs4mqo5rgMugYme6z_lOaOu0t1O6bwa_QyydFFB9EEGXw6yduC6XHbUoDIdDWfo8M-Dzs0ScPs_fRHKNQj9x4i5bKYr3qA-DKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قانون جالب پاسکال
🤯
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/682378" target="_blank">📅 22:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsCIq5Ax4IdyJYfGP1rhcELP-8tMk9uNEcygZ5-nCpnbLJBVHNVDm7BGqd7lZutq14aomCD1PUz00nPcx-Ok2ZJPx_n9KpDUx-FbzZVlo8jIrpVpY-TI_WTJKX4IGRHtY71a0UHrbwQfKuiURYJHRYfcqb9TUZ4W29r4BvFL8eaYVQ0o07poLPPdYzd1FchpuEt_GvXPG6_E57fx_5MC3qkMM7bBPqDmwMMcz3XowcMJL0Pxy-A_5uvMix1mM-W0A7UUhjFHPUAz54DFRlktjb8kNBGWpcXU2kI8r-acH250vKNQT-0aMCc31g0JcOIsqQKUp6hOK8oaQkO1N6d9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر رئیس جمهور تغییرات هلدینگ خلیج‌فارس را متوقف کرد
🔹
محمد شریعتمداری مدیرعامل گروه صنایع پتروشیمی خلیج فارس با ارسال نامه‌ای به رئیس سازمان بورس از توقف تغییرات مدیریتی این هلدینگ با دستور دفتر رئیس‌جمهور خبر داد.
🔹
صبح امروز، نامه‌ای از سوی سازمان بورس و اوراق بهادار به مدیران هلدینگ خلیج فارس ارسال شده بود که در آن از مدیرعاملی حسن عباس‌زاده در این هلدینگ، سخن به میان آمده بود.
🔹
بر اساسِ نامه ارسالی جدید، محمد شریعتمداری با اشاره به ابلاغیه شماره ۱۱۳۲۱/۰۴/۰۶ دفتر رئیس‌جمهور خطاب به وزیر نفت، تأکید کرده که تا اطلاع ثانوی، تمامی اقدامات، تصمیمات و ابلاغ‌های مرتبط با تغییر مدیریت این شرکت متوقف و وضعیت به پیش از تغییرات بازگردانده شود.
🔹
او خطاب به رئیس سازمان بورس تصریح کرده تا پیش از هرگونه اقدام، مراتب را از دفتر رئیس‌جمهور استعلام کند./منبع: فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/682376" target="_blank">📅 22:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682374">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291dd19206.mp4?token=KNbQYEmZQKPMSHpNPSTo6CZn7IU-exTmcZt2HEvueem_CkhphiqIpNvEzLsQFVybrB6-mkTU7tD3Z1jc4R8WZeIse5aMMbKYW4A3-2O2hPG-YNqF1d23IkMMbJnG2a7a_-Qp0bemzOFoPOuAXaVd3Kbt-36x6ht_xJtHtzq05Pzc-Jeb2Mmi1ILyl7NxB6rRlWkHobgzKWHYSddqtGsIZwRZJLfNn0Fnhh2LdrjOf3bCEe4J4dOj5EpFcpi_r6J5w3YO2w6sSJ-fJiGhUzpd8WIJvfDyTH2yswH_N73gyMJZ4sXGDqXxeXwIef7XX42gOzGTboxoDnRgD9bxM_DsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291dd19206.mp4?token=KNbQYEmZQKPMSHpNPSTo6CZn7IU-exTmcZt2HEvueem_CkhphiqIpNvEzLsQFVybrB6-mkTU7tD3Z1jc4R8WZeIse5aMMbKYW4A3-2O2hPG-YNqF1d23IkMMbJnG2a7a_-Qp0bemzOFoPOuAXaVd3Kbt-36x6ht_xJtHtzq05Pzc-Jeb2Mmi1ILyl7NxB6rRlWkHobgzKWHYSddqtGsIZwRZJLfNn0Fnhh2LdrjOf3bCEe4J4dOj5EpFcpi_r6J5w3YO2w6sSJ-fJiGhUzpd8WIJvfDyTH2yswH_N73gyMJZ4sXGDqXxeXwIef7XX42gOzGTboxoDnRgD9bxM_DsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاثیر بارفیکس بر بدن شما
💪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682374" target="_blank">📅 22:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682373">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh-WyfXYjrLwXeTk3XN0Kyc-rMO4JnNzKUDuw75UaZZIYRzO9o-41jP8XrqGDMPnUC1VQokom3wPEzWBf69YRJ8d_djCrU7N1p8ItCaZzSdpvLjMMZK386vCM1pkB7cp5RXpM5PJBwAyaWy5RpBiG6WjNwHgifNxeXBmw7YetgkLjUJCOiqbFaeVm9adWXoMWwALVTgmC7G2AkczQvUJwryRWz9WPhQb4dZetNC5R4i-eU0mYUNy-xfrqBvTnzZx8LS340rz8_qPXLOwSMFQwIgJZAXTiP2pe65RVS_3KyMVfg2rlLsHBAYV_NDN_Ph5-P6c23dB1KWoePRZ7TF6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرکت‌های بزرگ دنیا آینده‌ی مالی‌ات رو بساز!
🚀
فقط توی یکسال گذشته سهام گوگل 75 درصد و اپل نزدیک 38 درصد رشد کرده در حالیکه طلا فقط 25 درصد رشد داشته
!
هوش مصنوعی با سرعت زیادی در حال رشده و شرکت‌هایی مثل
انویدیا، گوگل و اپل
در مرکز این مسیر قرار دارن. حالا کاربران ایرانی میتونن خیلی راحت
سهام
شرکت‌هایی مثل انویدیا، گوگل، اپل و تسلا رو در بیت۲۴ بررسی و معامله کنن.
👉
توکن‌های سهام جهانی را در بیت۲۴ ببین.
https://l.b24.ca/o
https://l.b24.ca/o</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/682373" target="_blank">📅 22:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682372">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hao6yYbvzh5gsrgjpznQlPBJqJFhnEtJnsiiggZmQCxJp9lUfzWAg7ONzWtV4H-8uUOMX5--rEqrj7fOPwA43ka8KSL2dmBoHS4xdPuCuYJAeVsNWmrJzipWqY63NDl_9WiondFUWc2kQhOgS41hHEcAQAq7iIOMEvsZGscxHTMb10Nw3N2qMxd6cqiY5nsrk8csBP7ANIuNDRXIqDS6bhGpBonm_zJ4oH_uoAGk8gGqk1LFrIwap_-nXC12JL3MjBGE0hMqz8QSTOHd-rEzxAOalJFg32_Oxmx7oEo4d4YYL16CUgOAyGwnkDmI1J6nwhlYdkbSuGd44iwDPYiAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری مهر گزارش میدهد: هشدار مجلس درباره افشای اطلاعات فروش نفت
🔹
فرهاد شهرکی، نایب‌رئیس کمیسیون انرژی مجلس، با اشاره به نقش «تراستی‌ها» در فروش نفت در شرایط تحریم گفت: اختلافات و تعارض منافع میان واسطه‌ها نباید به افشای اطلاعات محرمانه‌ای منجر شود که ظرفیت صادرات نفت و منافع ملی را به خطر می‌اندازد.
🔹
او تأکید کرد استفاده از تراستی‌ها ممکن است در شرایط تحریم ضروری باشد، اما این موضوع نباید به معنای نبود نظارت و ضابطه باشد. واسطه‌ها باید احراز صلاحیت شوند و دسترسی آنها به اطلاعات حساس نیز صرفاً در حد نیاز عملیاتی باشد.
🔹
شهرکی همچنین خواستار بررسی دقیق هرگونه ادعای افشای اطلاعات شد و گفت صرف هم‌زمانی اختلافات داخلی با اعمال تحریم‌های خارجی برای متهم کردن افراد کافی نیست و باید موضوع بر اساس اسناد، سوابق دسترسی و شواهد فنی و حقوقی بررسی شود.
🔹
حفاظت از اطلاعات زنجیره فروش نفت، در شرایط تحریم بخشی از امنیت اقتصادی و منافع ملی کشور است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/682372" target="_blank">📅 22:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682371">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fc7d6d1e.mp4?token=fgpCxZp-Ph-mkqNfZzzylVrp-Hg21qFqPi2M33JbVQt-QYp87sdJOa4HOD6PSKSTzOqd-cpSbnTpm17QoVpYoTXp19Jsve4hgT7A3ZrxnrIOfXCeDrFlEKDZDYEiy2-ijOr9Mkh1sIHT5JCfEWW10gxsrHuo5aoA-YYzjRLr8s0L21VmGmC_6gSPWWDK4MEOdcaTa9gleJikRUFX7ZkEIvkX_d2249rN4VFKqZDe4t5oWth8EkkoyO1pqI2qN7wjTEYooxK4nH5ys9UlDWUndN7Q5GbQDzykf6f883jwiySnPmARGsGk9nrxqmtjzP4Rtt1wujS3kNvA6tiNdMDfKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fc7d6d1e.mp4?token=fgpCxZp-Ph-mkqNfZzzylVrp-Hg21qFqPi2M33JbVQt-QYp87sdJOa4HOD6PSKSTzOqd-cpSbnTpm17QoVpYoTXp19Jsve4hgT7A3ZrxnrIOfXCeDrFlEKDZDYEiy2-ijOr9Mkh1sIHT5JCfEWW10gxsrHuo5aoA-YYzjRLr8s0L21VmGmC_6gSPWWDK4MEOdcaTa9gleJikRUFX7ZkEIvkX_d2249rN4VFKqZDe4t5oWth8EkkoyO1pqI2qN7wjTEYooxK4nH5ys9UlDWUndN7Q5GbQDzykf6f883jwiySnPmARGsGk9nrxqmtjzP4Rtt1wujS3kNvA6tiNdMDfKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن تولد، لباس عروس و حتی آواز تولد برای سگ؛ تصاویری که نشون می‌ده سبک نگهداری از حیوانات خانگی برای بعضی‌ها دیگه فقط نگهداری از یک حیوان نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/682371" target="_blank">📅 22:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682370">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
واشنگتن‌پست: آمریکا بعد از جنگ ایران حضور در خاورمیانه را کم می‌کند
ادعای واشنگتن‌پست:
🔹
پنتاگون در حال بررسی کاهش حضور نظامی ایالات متحده در خلیج فارس پس از پایان جنگ با ایران است پنتاگون در حال ارزیابی کم کردن ردپای نظامی خود در خاورمیانه است که نشانه‌ای اولیه از پتانسیل جنگ ایران برای تغییر حضور ایالات متحده در این منطقه محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/682370" target="_blank">📅 22:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682368">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">🎉
۶۶ سال همراه مردم، از گذشته تا همیشه
🏦
شصت ‌و ششمین سالگرد تأسیس بانک رفاه کارگران را گرامی می‌داریم.
#بانک_رفاه_کارگران
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/682368" target="_blank">📅 22:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شهرهایی که قهرمان رمان‌ها شدند
🔹
برخی رمان‌های ماندگار ادبیات ایران خواستگاه‌هایی دارند که بسیاری از جذابیت‌های آن به خاطر همان شهرها و فرهنگ‌‌هاست.
🔹
در این ویدئو ببینید که این رمان‌های مشهور مربوط به کدام شهرهاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/682366" target="_blank">📅 22:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rydGLhCA4TARVG3Heq0Z3vBr6ek35SXFTG5G2PPCAh-DZjpmpqFpVFwf9dqE8QFGudSys_uU2dHZXrowp56yImiZRReTmVeGWj4UxZbopAMFhyGOhQ0zGHCjM84WMKmtJFAdContN2I0pLsFDMu50UPZ3VsU-M4znYRRC-V-oH4BC9MB_2w_ParBm63vm1y45FGv2fIaiGBdGd55pntnKl-SCvCjzMVQ-0WK7RMPS4GxurwNk_V3qBryNLtM_L7am1kxfStFi28bLU_lwk5ioc76GUUaNGqJDwCAXPlyMRlbhMoDXIhPuJCgNrBoHbeQevc-JUF0KSKvxALW9UkVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا داریوش اقبالی فُحش می‌خورد؟ | دعوا بر سر یک ما | چرا «توهم توطئه» داریوش جنجالی شد؟
🔹
انتشار ترانه تازه‌ای از داریوش اقبالی با نام «توهم توطئه» در فضای مجازی، فقط یک اتفاق موسیقایی نبود؛ خیلی زود به جدالی تمام عیار در میان کاربران فضای مجازی بدل شد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3238706</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/682363" target="_blank">📅 22:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17101087ed.mp4?token=o1JF7satjBgWFyzhwL0dA3b0XJS6-ijYboy_K4HPQ1cM8IbGO8drgw4zs3GdFRmGD3aM9fZV3aEgyWDqufl9iMCmi4wXMRaEMCh79_LxDOlvgf5XL809WQRsJKY6-0F77yrsneHRSt_6WVsTva8D-uXeqVm_-jtNdjzFdauLuDhzsHlSWtah6DNFQuCto6rmxTiUfOL0udMXHA3_PhkeYbb2RmyunylqMdVMrNZkfXpenqaFdRNg0oyuh7oUohrxyzT676BdxrS6uGBxKjJUnvU2CiyVPRe0r47In4cDPmzHbejXGRpXIUcjX7qpHpAEH2immFUnfsGi3Hjy3MSf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17101087ed.mp4?token=o1JF7satjBgWFyzhwL0dA3b0XJS6-ijYboy_K4HPQ1cM8IbGO8drgw4zs3GdFRmGD3aM9fZV3aEgyWDqufl9iMCmi4wXMRaEMCh79_LxDOlvgf5XL809WQRsJKY6-0F77yrsneHRSt_6WVsTva8D-uXeqVm_-jtNdjzFdauLuDhzsHlSWtah6DNFQuCto6rmxTiUfOL0udMXHA3_PhkeYbb2RmyunylqMdVMrNZkfXpenqaFdRNg0oyuh7oUohrxyzT676BdxrS6uGBxKjJUnvU2CiyVPRe0r47In4cDPmzHbejXGRpXIUcjX7qpHpAEH2immFUnfsGi3Hjy3MSf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تولد ۵۴ سالگی عمو پورنگ در کنار مزار مادرش
🖤
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/682362" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjbO0nEGnVtkIpaq4XX5jC293uPY6ELqjuiXUMjP-Q2Rtqn8eBnasUzsBJ79od2fMMw0G0begrURI4c3bzi2yuy9s7vmc5ysXXfFKw740SuFygHUr8uavg_tOV9yfL7vNb4jfaNy1bp00WfuFtAnCq0c1l2qjKHboYFvWInSX25_j1eE_MjxevaoK7X7HluhSV8Z-tOAcNivC_c0v4vTjr3XOwBPwBXYhvk5ZVxAKjgLU5Ved3o6wt5n8JCChRquiRP3eUndSjmkn5iVccbJr7s9TTPlZXI_F-0WLdwmIja-yrMK4wlhb-e4ZQBLCz_1dxO9YeONE3i0sRw2Mxs1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxKC0A3fKzRrH7FMim0DJn5Wp7WfJEYGKQCOnnn9MIvCVSD_MPznLSa9Ia4q9M9NtLS6BpDc6J3kHbLsU_B97KUPHYrZAvrbfsE9wueIMZFT9Uf4oDQGXuwCI_iAjo1d3H6NN09ufdpA1j32aRITj84NudeocVPb3B7wVCJwhxGaobKcwYP5_HVvLq_TbeBV_4wcr63LCpaa-XuiAs7PChOp0J--sKkfHF25WD9AvkZ5F65MiDqlhyR5cQx1osdEqvOtdAIzXitK-BrP6WQTX2AjpWRQ3J77RI-hSNlQyPfRtK3hoTSfEcFIB63bf8YMWcwH80W45h5qWL5Ml4B7gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba97f33e3.mp4?token=jdWStIy0zA5EaHxGZdR03v5AQFzjZuBFdaTQBgjcohwkR4TiqyAS9cb_yjMs1eNYJpOtUE7Zx4tpRyU9lfX94z0sNYvkV4CvYSHl729WohUhXOMSTd52NeEhncMz3pcUuLWJwk0kT21D0fH56jNW_ZjSGcQ-ubZ8TwgbPWMyj2XWsk2RKzBEdXvr1JlpL06a804AubQ3kjjD8SKdIHDUsdjYMSQuIVsd-Ks12goUVcwD64gv_gWsWeADxT7NUc9ipV8lRNXpzNcjuovEffEwEfOIqMi9oH2Kv_H5wPSR2go5Km8lxkgJBo1yfx-zvJtSNQBUQcYIJccchbUU7iWoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba97f33e3.mp4?token=jdWStIy0zA5EaHxGZdR03v5AQFzjZuBFdaTQBgjcohwkR4TiqyAS9cb_yjMs1eNYJpOtUE7Zx4tpRyU9lfX94z0sNYvkV4CvYSHl729WohUhXOMSTd52NeEhncMz3pcUuLWJwk0kT21D0fH56jNW_ZjSGcQ-ubZ8TwgbPWMyj2XWsk2RKzBEdXvr1JlpL06a804AubQ3kjjD8SKdIHDUsdjYMSQuIVsd-Ks12goUVcwD64gv_gWsWeADxT7NUc9ipV8lRNXpzNcjuovEffEwEfOIqMi9oH2Kv_H5wPSR2go5Km8lxkgJBo1yfx-zvJtSNQBUQcYIJccchbUU7iWoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این قانون مدیریت پول رو یکبار برای همیشه یاد بگیر #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/682357" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b4ed298.mp4?token=lsvb-_r1MKxMQNKWcDbnva24Hjwyz1DOdXHPhLTtSw85LxXmiThsxKDDlPeJav8S9dCUvv_nWRySrJErZNWIR5W8iPbnqI6yc8IFeqHRfHXy95c5oamtOrUH09tTmBU0YFulzCMpMObjwVaRyI1rsCTbLCDtHPw-7iJbBxBullmaL73rjig43vMP2HW4jevjIRJezuJwjllDfwpwqT8z-7FTaG6gboQzZ81TMyifwUelSvicY_Rv_vX-lfrWQw9FiQhZkcWWkstuDUScpKP7afqdiKqHDriVlDqKhgFetEIKH88_ud-nTnbBu54IkMRfZ1ox_6T0Gt0se4wrApIW7XU9AFYY9OcY_e-qgUB5CXTfTJ92D9Ud8vSLohS7ZSLcluGgMxDXtE7iyOc8pWJQDjnH6rFHsfMSJ-1oRsiJHNkYJ4loMetvFUPfFQp6BMFajGpUkeC_-I50Mjl2e_HNjpnyTMuc0RnbQgbq2UBNOdI3K3htiBEZuXrvFczLK5kplZxCTjZ0HmDMOZeEsPodV64E26pL7sBeRHk-sUTN86AXWNaXrRt_Nmb6HbirZJOfQ_e4ca4Gfjcd0h8ZFcfrLSBP23_FlMW6mSKQIq0AXVqh1DgwVrUDDImp3RDF2Zdqe-hlsv1hpSU_v_rAsUaXipbeuSgJs44g9i6CPmVr9PI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b4ed298.mp4?token=lsvb-_r1MKxMQNKWcDbnva24Hjwyz1DOdXHPhLTtSw85LxXmiThsxKDDlPeJav8S9dCUvv_nWRySrJErZNWIR5W8iPbnqI6yc8IFeqHRfHXy95c5oamtOrUH09tTmBU0YFulzCMpMObjwVaRyI1rsCTbLCDtHPw-7iJbBxBullmaL73rjig43vMP2HW4jevjIRJezuJwjllDfwpwqT8z-7FTaG6gboQzZ81TMyifwUelSvicY_Rv_vX-lfrWQw9FiQhZkcWWkstuDUScpKP7afqdiKqHDriVlDqKhgFetEIKH88_ud-nTnbBu54IkMRfZ1ox_6T0Gt0se4wrApIW7XU9AFYY9OcY_e-qgUB5CXTfTJ92D9Ud8vSLohS7ZSLcluGgMxDXtE7iyOc8pWJQDjnH6rFHsfMSJ-1oRsiJHNkYJ4loMetvFUPfFQp6BMFajGpUkeC_-I50Mjl2e_HNjpnyTMuc0RnbQgbq2UBNOdI3K3htiBEZuXrvFczLK5kplZxCTjZ0HmDMOZeEsPodV64E26pL7sBeRHk-sUTN86AXWNaXrRt_Nmb6HbirZJOfQ_e4ca4Gfjcd0h8ZFcfrLSBP23_FlMW6mSKQIq0AXVqh1DgwVrUDDImp3RDF2Zdqe-hlsv1hpSU_v_rAsUaXipbeuSgJs44g9i6CPmVr9PI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گوییم دیگر هیچ‌جا برایت امن نیست یعنی این
🔹
با این قسمت از انیمیشن «انگری بردز» همراه باشید؛ جایی که پرندگان ایرانی زندگی آرام ترامپ را از او گرفته‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/682356" target="_blank">📅 22:14 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
