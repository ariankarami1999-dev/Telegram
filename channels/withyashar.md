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
<img src="https://cdn4.telesco.pe/file/FY4jGW5iipWAZgJWAhlJPdRrvHjPPbvD858TKvnr9P8BFTJczgAAXu8bbZG7c7YT8pN16ChsEnWY3OpI9tqmrZv-PGBGODVaqtREc0i1aUHuqSGPXqokRpBAoxoWi0oEeq4VmK4Bez-frwRoT2FsHNURNo_oMSO5JOTBlhc-grpXHRD76joFs9TsrCmgF6Se2gl3YkQ1qTgSzGsMDNdOpIsXpRGYesCG9eglFboQnmMTcKySrDodyR0dDYh1no7tTU2x4Rv9ztg1OrwFTpvanV4vDOa2krr_O3XhArhpawvuE3P5iDRPanH1cMoNDoWKyNcaLasIHGY-nJiZZgs1yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 489K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/24996" target="_blank">📅 05:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/24995" target="_blank">📅 05:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gGy5rJmcNkhZHFT3fZwF5G4BF2yuwWR3QPxzoLgqPeyGM-m73s3k7uzs7HcQasgkGd7rKRiPeD5nL_ZKVN7ag1AZTTRYxlLo5yAS0cxUrwgLzf1IEBZJs04VG9jq9ufTjVVkausUsN3KVawOjfV8k96etSlZc9QYNLqZKMecFyHquDAvRwvqAa4vASQZm6wcaevcki0STiIIG5liMin0iEdGaVOmxKuJjG_Y19EHhkQdf-tiUiswhafGSkJcxV2wi4mSc8AWhtT4tEKI7Rhd_eQDQhY9WjeGaCqKCJba5mjPNIMJ7vkZ6-8Jy9imYRlQZkP4gK9fci52icvIBoiwL7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gGy5rJmcNkhZHFT3fZwF5G4BF2yuwWR3QPxzoLgqPeyGM-m73s3k7uzs7HcQasgkGd7rKRiPeD5nL_ZKVN7ag1AZTTRYxlLo5yAS0cxUrwgLzf1IEBZJs04VG9jq9ufTjVVkausUsN3KVawOjfV8k96etSlZc9QYNLqZKMecFyHquDAvRwvqAa4vASQZm6wcaevcki0STiIIG5liMin0iEdGaVOmxKuJjG_Y19EHhkQdf-tiUiswhafGSkJcxV2wi4mSc8AWhtT4tEKI7Rhd_eQDQhY9WjeGaCqKCJba5mjPNIMJ7vkZ6-8Jy9imYRlQZkP4gK9fci52icvIBoiwL7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص و قر تمام کننده ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/24994" target="_blank">📅 05:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=hfv5JC4w-h-1Dcp_agWrELaQ-j0SiV72NxEmpOR7Tg-W97cBWRrqKtdX0d70eHiMJixoLV4FVl5eUEHpfZ0Pn0QTUVTOBNMnnIwgCjK1p-T5zcCQ2SkL1wwuS_IVynyIBZ3eHd1VB_4g1iQ5gxhhFzkZOllK8F2Pwi3DArT6YSJFR7WG6144RhRLQDNjVQ144QV4bvgBBHnoOjnFi5f_mRRjXc_CqV7WbVIFznyXFOIGiv4ZG6EfcNB5N0KMTG3n4dmuF04ZBHe5m4UyH2EW8mb-Dr1iS26ICOonCnjrhBJBALE5hO1SeH7Fqqz9NHzC6CDZAooQQsDPbs7ya30t-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=hfv5JC4w-h-1Dcp_agWrELaQ-j0SiV72NxEmpOR7Tg-W97cBWRrqKtdX0d70eHiMJixoLV4FVl5eUEHpfZ0Pn0QTUVTOBNMnnIwgCjK1p-T5zcCQ2SkL1wwuS_IVynyIBZ3eHd1VB_4g1iQ5gxhhFzkZOllK8F2Pwi3DArT6YSJFR7WG6144RhRLQDNjVQ144QV4bvgBBHnoOjnFi5f_mRRjXc_CqV7WbVIFznyXFOIGiv4ZG6EfcNB5N0KMTG3n4dmuF04ZBHe5m4UyH2EW8mb-Dr1iS26ICOonCnjrhBJBALE5hO1SeH7Fqqz9NHzC6CDZAooQQsDPbs7ya30t-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: «فقط یادتان باشد، من دارم می‌دوم، باشه؟حقیقتأ به تمام معنا، واقعاً دارم می‌دوم.»
@WarRoom</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/24993" target="_blank">📅 05:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24992">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=HNmrYhQFWV_EoeaJDdkjGRC0Nf9kAsT2hoVPF4qkCCfWtVXiAUVNv0PQw8UKg7PGCpPAKrlDR7y9LgFhB88NeMTr5MJIB2OQiM-WIuoGyZAvk7VqXJTiYKXWVk4ptqmKlIDIE5O6U7ywZbp4AgJWAgAAlUQvZ9pt0p--trIx_56aFsKR2NL_3f1r7zv9eOIp712wwiPXjSU-JOpfR6p4r53M_3bnQOR1DYmdu3EhsOj8G-T67mbRlt_v9kECjqTG56TqHk6yPU4uf6bZR0MVCzx6rqeLFs48iCTpivTb-ko4ScTHZDXQDzVJIXooVG_7MK0WchyYYk1RgiZP39TDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=HNmrYhQFWV_EoeaJDdkjGRC0Nf9kAsT2hoVPF4qkCCfWtVXiAUVNv0PQw8UKg7PGCpPAKrlDR7y9LgFhB88NeMTr5MJIB2OQiM-WIuoGyZAvk7VqXJTiYKXWVk4ptqmKlIDIE5O6U7ywZbp4AgJWAgAAlUQvZ9pt0p--trIx_56aFsKR2NL_3f1r7zv9eOIp712wwiPXjSU-JOpfR6p4r53M_3bnQOR1DYmdu3EhsOj8G-T67mbRlt_v9kECjqTG56TqHk6yPU4uf6bZR0MVCzx6rqeLFs48iCTpivTb-ko4ScTHZDXQDzVJIXooVG_7MK0WchyYYk1RgiZP39TDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره احتمال حمله هسته‌ای ایران به یک شهر آمریکا: «میخواهید بگذارید این کار را بکنند؛ بگذارید لس‌آنجلس را از بین ببرند، بگذارید سن‌دیگو را از بین ببرند؟؛
این
گرانی بهای بسیار کوچکی است که باید پرداخت شود.
»
@WarRoom</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/24992" target="_blank">📅 05:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش چند صدای انفجار بندر عباس ۱۰ دقیقه پیش
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/24991" target="_blank">📅 05:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=SIxMGc736hh_aIBRxy_oD3laHDc56-xjp6wR0Z5FAQ7oi8kHqgQ-UKG4wpDjkBgeZitylPw8os6kYymQXTCOGnKJ7sehH1uej8NKjHkOeL3gBzIENKpeQEQZCwZ42QkK5kwsxzOnvpRHP__M4jcKMNzBIARfhi8Qq16ACNRE3kzOlzTix7RXngtIuno0Vd3tHHqh65n2fECO2ti81coVZFaLkHU2S4w-GKnXMj2_3w6c0Sw8qYCT7gu4PhmKiIiBJ77bnaN4m51cjR_v9jx2P8gzUUCeTS-kvLQLNbQ60_MJmd-4e109gaVI9yLIAmtcovXv21Ziw8x88RscW4Gp-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=SIxMGc736hh_aIBRxy_oD3laHDc56-xjp6wR0Z5FAQ7oi8kHqgQ-UKG4wpDjkBgeZitylPw8os6kYymQXTCOGnKJ7sehH1uej8NKjHkOeL3gBzIENKpeQEQZCwZ42QkK5kwsxzOnvpRHP__M4jcKMNzBIARfhi8Qq16ACNRE3kzOlzTix7RXngtIuno0Vd3tHHqh65n2fECO2ti81coVZFaLkHU2S4w-GKnXMj2_3w6c0Sw8qYCT7gu4PhmKiIiBJ77bnaN4m51cjR_v9jx2P8gzUUCeTS-kvLQLNbQ60_MJmd-4e109gaVI9yLIAmtcovXv21Ziw8x88RscW4Gp-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره عبور کشتی‌های آمریکا از تنگه هرمز: «کار نیرودریای ما حرف نداره ، نفت از قبل هم بیشتر از تنگه عبور میکنه ، هر از گاهی آنها یک موشک کوچک شلیک می‌کنند. ما هم می‌گوییم «بینگ» و موشک را می‌زنیم و نابودش می‌کنیم. به شما می‌گویم، خیلی خفن است! موشک می‌آید، موشک می‌آید، موشک دیگر نیست. تمام. و کشتی‌ها هم به حرکت خودشان ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/24990" target="_blank">📅 05:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دونالد ترامپ: «آنها شیاد هستند. دروغ می‌گویند. ما کاری جز پایین آوردن قیمت‌ها انجام نداده‌ایم و وقتی جنگ با ایران تمام شود، که خیلی زود خواهد بود، قیمت نفت به‌شدت سقوط خواهد کرد.آنها نمی‌توانند سلاح هسته‌ای داشته باشند، چون دیوانه‌اند. این کاری بود که رئیس‌جمهورهای دیگر یا کشورهای دیگر باید سال‌ها پیش انجام می‌دادند. ما همیشه مجبوریم کارهای سخت و کثیف را انجام دهیم، در حالی که این کار باید سال‌ها پیش انجام می‌شد. این وضعیت ۵۱ سال ادامه داشته است؛ زورگوی خاورمیانه دیگر چیزی ندارند همه چیزشان نابود شده است و تنها چیزی که دارد ، تورم ۳۱۰ درصدی است، کار را زود تمام میکنم احتمالا بعد از انتخابات میان دوره‌ای
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/24989" target="_blank">📅 04:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=lX-TjJ4YRMNLlOFIAzS9S4LIWIxrXBN9clVG7kblrcEW6Gb7rJn_9mPQgGQuKv2MKooO2Lsr-aJeABQICDeEeRgKQpyi7VY7UVS7Om9yYDuFbK28Kyb5LeTYCX_nSbp5KeN8WL3JPPnWHyQHxFTYwdJVsRGQZenzUYlLy90amucg-LIm7HojrIEyUt_2vTyAhvoXDPY251u2KzMq6fHjMbkpwmwKt6ORzPCYXAQw7mxIbpSA4_rHpssoSRQ9lbzxzPhLSny9joKlFw3XEu_LF8cekTn2EzpXDsV9246vdy-p1CM-nGDGnlI7QdN6WbkrQrfbwHX5M2gFm0sEJk7-R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=lX-TjJ4YRMNLlOFIAzS9S4LIWIxrXBN9clVG7kblrcEW6Gb7rJn_9mPQgGQuKv2MKooO2Lsr-aJeABQICDeEeRgKQpyi7VY7UVS7Om9yYDuFbK28Kyb5LeTYCX_nSbp5KeN8WL3JPPnWHyQHxFTYwdJVsRGQZenzUYlLy90amucg-LIm7HojrIEyUt_2vTyAhvoXDPY251u2KzMq6fHjMbkpwmwKt6ORzPCYXAQw7mxIbpSA4_rHpssoSRQ9lbzxzPhLSny9joKlFw3XEu_LF8cekTn2EzpXDsV9246vdy-p1CM-nGDGnlI7QdN6WbkrQrfbwHX5M2gFm0sEJk7-R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: راستی، ما داریم به ایران در کونی میزنیم ، اینو که می‌دونید، مگه نه؟
این ماجرا، به هر شکلی، به پایان خواهد رسید. خیلی زود تمام می‌شود و قیمت‌هایتان به‌شدت پایین خواهد آمد
ما خاورمیانه ، اسرائیل و جهان را نجات میدهیم, آنها هیچوقت سلاح هسته‌ای نخواهند داشت
@WarRoon</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/24988" target="_blank">📅 04:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان گزینه جدید وزارت دفاع را معرفی کرد.
مسعود پزشکیان،
مهرداد اخلاقی کتابچی
، از مدیران باسابقه صنایع موشکی و هوافضای وزارت دفاع را برای تصدی وزارت دفاع به مجلس معرفی کرد. او سابقه ریاست سازمان صنایع هوافضای وزارت دفاع و گروه صنعتی شهید باقری را دارد و نامش در فهرست تحریم‌های مرتبط با برنامه موشکی ایران نیز بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/24987" target="_blank">📅 01:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرمانده سنتکام، دریاسالار برد کوپر: «ارتش آمریکا همچنان با تمرکز کامل بر این مأموریت فعالیت می‌کند و علیه هر کشتی که تلاش کند محاصره را دور بزند،
سریعاً اقدام خواهد کرد.
نیروهای ما آموزش‌دیده، حرفه‌ای و مرگبار هستند.» به تمامی دریانوردان توصیه شده هنگام تردد در
دریای عمان و مسیرهای منتهی به تنگه هرمز
، اطلاعیه‌های دریایی را پیگیری کنند و در صورت نیاز از طریق کانال ۱۶ ارتباط «کشتی به کشتی» با نیروهای دریایی آمریکا تماس بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24986" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0rfEvo8OxF0rqUiFXLLF5F67JziapP4YYK08yka3RRvnkHa-nTy8jeSSUsioqeA9GbR126tfWhTt89M7zq103GyAIpycTPNw3Aea2sSBFbEkMD9b0WTOSUylgNbyrHrtYi7ALs260dydDiYv1U1zRl3OK_iza_0zRxavbmxbwmbdOSq8NnLAqknBcf9S9NugkC0SiaM2Pd2dHjzMug0oXv329WveJ6lueZI3v2v6VTdHfPS2-tD-MT4BxgwzH3rKDe73UgQ8e7Dld9WEONlKDwjF2xh77QFiTj5yUocHeEO7tAqxntZJSALnNVP_3Ef1b8IvM4MX4S-HnhYcyeFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی روز دوشنبه
صدوسی‌امین کشتی تجاری
را که قصد ورود یا خروج از بنادر ایران داشت، در چارچوب محاصره دریایی ایران، وادار به تغییر مسیر کردند. از زمان ازسرگیری محاصره در
۲۳ تیرماه
، نیروهای آمریکایی مدعی‌اند
۱۳۰ کشتی
را تغییر مسیر داده و
۳ کشتی
را که حاضر به تبعیت نبوده‌اند، از کار انداخته‌اند. همچنین به بیش از
۷۰ کشتی بشردوستانه
اجازه عبور داده شده است. سنتکام همچنین مدعی است طی ۱۲ هفته گذشته،
۱۳ کشتی تجاری
را که متهم به نقض محاصره یا فعالیت در شبکه چند میلیارد دلاری سایه سپاه پاسداران بوده‌اند، منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24985" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال 14 اسرائیل
: لحظاتی پیش نتانیاهو با روبیو، وزیر خارجه آمریکا یک تماس تلفنی اضطراری و ویژه برقرار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24984" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=Uzol0rfGuchVl8_Pj5EUnImY9TezMjaaHNJgQeOmysoLwAgwAvlsoEQMPG6YIwjc1iWNWCFDrw1ZI4-nGaZbib_qxclrOQ1Fadrm7gNi-zDn0mEjOFH0BBy0khGqt14CFkiYUVZHkiwhakQzHqL17DG17HyFWsawspU-wAVbiv2L0-5hwLYUJ1LLfH8yCeynMy_-3CsZjg_OdLVZ5_5b7nuDHsa55B-foguSICd6e0HzlrbxlCufq9daHuljPs24YC9kpeO8HY0f34vk8FbEl8LQAscMy_Gf8zlabmQQ1r6yylDnUcKVSFwjExompnwZv-_p6EqOWfMfigRra8Sqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=Uzol0rfGuchVl8_Pj5EUnImY9TezMjaaHNJgQeOmysoLwAgwAvlsoEQMPG6YIwjc1iWNWCFDrw1ZI4-nGaZbib_qxclrOQ1Fadrm7gNi-zDn0mEjOFH0BBy0khGqt14CFkiYUVZHkiwhakQzHqL17DG17HyFWsawspU-wAVbiv2L0-5hwLYUJ1LLfH8yCeynMy_-3CsZjg_OdLVZ5_5b7nuDHsa55B-foguSICd6e0HzlrbxlCufq9daHuljPs24YC9kpeO8HY0f34vk8FbEl8LQAscMy_Gf8zlabmQQ1r6yylDnUcKVSFwjExompnwZv-_p6EqOWfMfigRra8Sqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌های ترامپ: «این جمعیت از معمول بیشتره یا چی؟ دارم جذاب سکسی می‌شم؟ چه خبره اینجا؟ اینجا واقعاً آدم‌های زیادی هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24983" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=hluEDrz5r2p1bn-FPsz-BDzJH3KHQ41SnLCMi9azIGYBcCu0QFilEx8n0963U5PUYvtDXTB1qi5X8YlpIqcBr5Iterevhx2KtcQ7MLR7eWuYh9_EoVnYHqT6XbYpHevQ_Psi4_MYF5_CRUGs1t_BljoCSqTY8IlO-e0ImSCC4YZ8EF53enwOCjuoPFNFr-hpJ5-o1XPQYbDX_Hw37Qdcnuf0uHeizkgfj9p96yqscCAgKSxNpngAY7QD2heBROc4CRcq52lSarC4CAVqhL9I7HcKeMAYHUOGDrJOoVwhz0I5wk3vUlzvF_8PgxoIuTKfTpDgtNWjGzD92JIF5HSDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=hluEDrz5r2p1bn-FPsz-BDzJH3KHQ41SnLCMi9azIGYBcCu0QFilEx8n0963U5PUYvtDXTB1qi5X8YlpIqcBr5Iterevhx2KtcQ7MLR7eWuYh9_EoVnYHqT6XbYpHevQ_Psi4_MYF5_CRUGs1t_BljoCSqTY8IlO-e0ImSCC4YZ8EF53enwOCjuoPFNFr-hpJ5-o1XPQYbDX_Hw37Qdcnuf0uHeizkgfj9p96yqscCAgKSxNpngAY7QD2heBROc4CRcq52lSarC4CAVqhL9I7HcKeMAYHUOGDrJOoVwhz0I5wk3vUlzvF_8PgxoIuTKfTpDgtNWjGzD92JIF5HSDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوکاس فاکس، خبرنگار فاکس‌نیوز: «درباره فلای‌دبی، آیا فکر می‌کنید ایران مسئول این حمله تروریستی بوده است؟»
ترامپ: «بله، شخصاً همین‌طور فکر می‌کنم.»
با این حال، بازرسان هنوز در حال بررسی هستند تا مشخص شود مظنون با
ایران یا یک طرف خارجی دیگر
ارتباط داشته است یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24982" target="_blank">📅 23:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b58bc0dae.mp4?token=utcFrjzSeJv6REC-lR51K_dovMfWAYPJorJFWCbJ2viTZKD4YkM9xyimu1J1U0DcFF9dMsl-LteUomRxmf0aMdJW-n7G8skp5MnOdPKVwKJr-w7mFEXdDtIpa7FZUic-NXldSzS06EbEcgEiICBHckGuaI6Cwf2xk5hqx5Ew3yKBKqx0OxPqPUF56pz9Wuyc3HJbAUmI46xnseQ7NfBZHluSTeVdVUhFDTJmi-bte2VUEd-3SSBuTg-r6S5IyeSsUUuqgk0IP7JwRAJPwT5sR8cdjBpkraMSQgWCOBdqKLKEnKktMIEFrnlceZnvKgBK125LJZxKMbJVEkNKbofcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b58bc0dae.mp4?token=utcFrjzSeJv6REC-lR51K_dovMfWAYPJorJFWCbJ2viTZKD4YkM9xyimu1J1U0DcFF9dMsl-LteUomRxmf0aMdJW-n7G8skp5MnOdPKVwKJr-w7mFEXdDtIpa7FZUic-NXldSzS06EbEcgEiICBHckGuaI6Cwf2xk5hqx5Ew3yKBKqx0OxPqPUF56pz9Wuyc3HJbAUmI46xnseQ7NfBZHluSTeVdVUhFDTJmi-bte2VUEd-3SSBuTg-r6S5IyeSsUUuqgk0IP7JwRAJPwT5sR8cdjBpkraMSQgWCOBdqKLKEnKktMIEFrnlceZnvKgBK125LJZxKMbJVEkNKbofcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : فکر می‌کنی احتمال داره که ایران پهپادهای نظامی خودشو به بریتانیا انتقال داده باشه ؟
ترامپ: من نمیتونم راجبش به شما چیزی بگم.
اما اگه اونا اینکار رو کرده باشن، عواقب خیلی سنگینی رو متحمل میشن.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24981" target="_blank">📅 23:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار فاکس نیوز: در کاخ سفید، رئیس‌جمهور ترامپ به من گفت که معتقد است ایران مسئول حمله تروریستی به هواپیمای فلای‌دبی است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24980" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e53e579ac.mp4?token=e7bexvwxnUgGuMPc0KFV1idGhO-IrOpvOrPYLD_OVga-QtyHtvNA1fIwPKwZ5UOYPbgG7kZh9vHMIL-3AGV3o7Pbvr3zwkVAWYo52IBFmfYxCHP8vpJ74pAnmj3t28rDEnJT34ZJWeaDcDY_NjBogMCWcSbcNf4hpxUdVlxObpGWeZFbAZjVRXS5D3yoN55fYZWeU-27XeiIjK1JLw93Wx2aQ2Z-Vxn_BUK8Imy-zgXBMBjDzbvJdaqvXEwkl7SLhnkDN9LeKJNXFdMsi-lAGBs3DCdVukgNvzd-uJGdMxzy0hOjLVGIEchsl-2j7rXg94tKsLpYPk-TL_IcxyQ-R41WHRs0jAz9Oxa6o6i2DVriv_ro70TceTy_6zT-3JB2lY6FbD2qV3yfXxC7OAtNxi18jslTw1hOXIc5APA3olmTLdv0NEb__d3HDqjYZTASKCkz4YZyHDLFqeOWojUou8aWsLN2kpp7pBK7QJLapar6DowsKWS01H5ooApHHxxFPERQdSpTVbz0yvqRy4ixMKoZKENFIenXU844Ys_5zBeHDS1UteAoM98e2xu6unmlkLkCiu-6T5afUJulh75EZTzKvDSMLPimG4QRDlCwwpto943qQbkaXseWm_RZBnTBpbhwnmkRmooY3_tM5xqhknITH_T77tInMW1W77FvLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e53e579ac.mp4?token=e7bexvwxnUgGuMPc0KFV1idGhO-IrOpvOrPYLD_OVga-QtyHtvNA1fIwPKwZ5UOYPbgG7kZh9vHMIL-3AGV3o7Pbvr3zwkVAWYo52IBFmfYxCHP8vpJ74pAnmj3t28rDEnJT34ZJWeaDcDY_NjBogMCWcSbcNf4hpxUdVlxObpGWeZFbAZjVRXS5D3yoN55fYZWeU-27XeiIjK1JLw93Wx2aQ2Z-Vxn_BUK8Imy-zgXBMBjDzbvJdaqvXEwkl7SLhnkDN9LeKJNXFdMsi-lAGBs3DCdVukgNvzd-uJGdMxzy0hOjLVGIEchsl-2j7rXg94tKsLpYPk-TL_IcxyQ-R41WHRs0jAz9Oxa6o6i2DVriv_ro70TceTy_6zT-3JB2lY6FbD2qV3yfXxC7OAtNxi18jslTw1hOXIc5APA3olmTLdv0NEb__d3HDqjYZTASKCkz4YZyHDLFqeOWojUou8aWsLN2kpp7pBK7QJLapar6DowsKWS01H5ooApHHxxFPERQdSpTVbz0yvqRy4ixMKoZKENFIenXU844Ys_5zBeHDS1UteAoM98e2xu6unmlkLkCiu-6T5afUJulh75EZTzKvDSMLPimG4QRDlCwwpto943qQbkaXseWm_RZBnTBpbhwnmkRmooY3_tM5xqhknITH_T77tInMW1W77FvLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: «آیا نگران شیوع بیماری در روسیه هستید؟»
ترامپ: «بله، هستم.
شیوع ذات‌الریه، اگر بخواهید این‌طور صدایش کنید.
این بیماری چیزی بود که قبلاً می‌توانستیم آن را کنترل کنیم. اما به‌نوعی این میکروب‌ها قوی‌تر و باهوش‌تر شده‌اند. آنها مثل یک ارتش هستند. میکروب‌ها واقعاً نسبت به گذشته قوی‌تر شده‌اند و چیزهایی که قبلاً برای درمان ذات‌الریه مؤثر بودند، دیگر به همان اندازه مؤثر نیستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24979" target="_blank">📅 23:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c5518a59.mp4?token=ieYMoTa5wEQypqkq5OmpbNALmnZQ1auKbBsDYGyvD6ql8XhFwFROIt5h5oVcUMDssMyC9mD7DjMjS1stbT9j982tPz_8pn5TkB4AJur6TMWj-QXEwAjvSU9iIrc9hUN6gf-cFWrTz0rVl7vX2XcWjR87oZ7A89VSIOamJFDltAaW-3HuabLAq6xpB6LeZA1ZRtgtg98hnL5hyyw7eKVeegSxNK-xk2-n7LqtSfHumkhr_Ys8LRqnki2ogeUraL9U0hSOcQx_KHhiE-ceK7SX2Ehn3upDwd5ITJ7stplRtsD3RC00AhmJ7lfsONxlwnyGG1OXNvHQYa0I-wniG1HlBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c5518a59.mp4?token=ieYMoTa5wEQypqkq5OmpbNALmnZQ1auKbBsDYGyvD6ql8XhFwFROIt5h5oVcUMDssMyC9mD7DjMjS1stbT9j982tPz_8pn5TkB4AJur6TMWj-QXEwAjvSU9iIrc9hUN6gf-cFWrTz0rVl7vX2XcWjR87oZ7A89VSIOamJFDltAaW-3HuabLAq6xpB6LeZA1ZRtgtg98hnL5hyyw7eKVeegSxNK-xk2-n7LqtSfHumkhr_Ys8LRqnki2ogeUraL9U0hSOcQx_KHhiE-ceK7SX2Ehn3upDwd5ITJ7stplRtsD3RC00AhmJ7lfsONxlwnyGG1OXNvHQYa0I-wniG1HlBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «چه تهدیدی باعث شد هواپیماهای آمریکایی را از بریتانیا خارج کنید؟»
ترامپ: «ما به این نتیجه رسیدیم که ممکن است تهدیدی وجود داشته باشد و چرا باید آنها را آنجا نگه می‌داشتم؟ انتقال آنها هزینه بسیار کمی دارد. ما افرادی را که این تهدید را مطرح کرده‌اند می‌شناسیم و آنها
با ایران مرتبط هستند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24978" target="_blank">📅 23:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4307e8a523.mp4?token=SsUdPy6OckLApZ6CZmqRHPQMSnEq_uDDeaQnbW0mTrN5MTG1G7JeMM2JKvhWUVIvKLbqYcA2fzu_zHOaaPrUFn2_pFEKF9PD_eAFyGGDUvJw2uPBBXIwu-uWOy3kxniy4Ozhe9Uy8VFh3a041WF5i-lOq7NKNTlii0oTSyOSKymn2PrpwNbzmawdD7-gMsZDD9lY15qCl2-kADEj0d7spUV9KDaH4ZFqwkQ_q5Fes5vYrXptxPBcib6yJz3yxvdQIQLhdyt3uzdfwamOIdThah2CR87pOo6WY00gwP0TchwE3MvQiouRow7FR0GOityWUYCJ4SVQwjo9SkoKizcM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4307e8a523.mp4?token=SsUdPy6OckLApZ6CZmqRHPQMSnEq_uDDeaQnbW0mTrN5MTG1G7JeMM2JKvhWUVIvKLbqYcA2fzu_zHOaaPrUFn2_pFEKF9PD_eAFyGGDUvJw2uPBBXIwu-uWOy3kxniy4Ozhe9Uy8VFh3a041WF5i-lOq7NKNTlii0oTSyOSKymn2PrpwNbzmawdD7-gMsZDD9lY15qCl2-kADEj0d7spUV9KDaH4ZFqwkQ_q5Fes5vYrXptxPBcib6yJz3yxvdQIQLhdyt3uzdfwamOIdThah2CR87pOo6WY00gwP0TchwE3MvQiouRow7FR0GOityWUYCJ4SVQwjo9SkoKizcM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: «نظر شما درباره ضدحمله و عملیات تهاجمی عربستان و یمن علیه حوثی‌ها چیست؟»
ترامپ: «همه‌چیز درست خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24977" target="_blank">📅 22:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e845f43990.mp4?token=ZpaVFvjqeGHnJ2vA9mTAt4KfX7OmhMRLhWcyqQcgxz4__8n_B4cTgAIGsnXjNEyTKek3keOXRwZDuQOo_27WqJz9w2F_Seho6x5v7gJrFUrkhJv3Izkw_oiI_Z8bHHfsDq4oY6S4xMKzV0Bd89dSytntk4rR08m9pEYS8AesW1yha50px6z6Mh5yleFDiYb3DBLYI9ha7em-mR9W3JFouIE9AdQInPNhjt9z3CfXjUfHyyRBzYMcJo-5A8EjnZ53hiIFV1Rr_Ql3ARCrBoauPJgptaKHtDqJwZh16QGAauhqA211M9AxW1yG-k476xOWC4C3Lzf_Uukvg6GV9nYF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e845f43990.mp4?token=ZpaVFvjqeGHnJ2vA9mTAt4KfX7OmhMRLhWcyqQcgxz4__8n_B4cTgAIGsnXjNEyTKek3keOXRwZDuQOo_27WqJz9w2F_Seho6x5v7gJrFUrkhJv3Izkw_oiI_Z8bHHfsDq4oY6S4xMKzV0Bd89dSytntk4rR08m9pEYS8AesW1yha50px6z6Mh5yleFDiYb3DBLYI9ha7em-mR9W3JFouIE9AdQInPNhjt9z3CfXjUfHyyRBzYMcJo-5A8EjnZ53hiIFV1Rr_Ql3ARCrBoauPJgptaKHtDqJwZh16QGAauhqA211M9AxW1yG-k476xOWC4C3Lzf_Uukvg6GV9nYF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره پالایشگاه‌های نفت روسیه: «مشکل، کمبود پالایشگاه‌هاست.
حجم بسیار زیادی نفت از تنگه هرمز خارج می‌شود.
به‌دلیل جنگ، با کمبود پالایشگاه مواجه هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24976" target="_blank">📅 22:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال گسترش بررسی درباره تسلیحات فضایی است و کارشناسان هشدار داده‌اند که نبود مقررات روشن درباره سلاح‌های متعارف در فضا می‌تواند به رقابت نظامی جدید میان قدرت‌های بزرگ منجر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24975" target="_blank">📅 22:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیمان مکه فعال شد
وزارت امور خارجه پاکستان: پاکستان، پادشاهی عربستان سعودی و ترکیه توافق کردند که نیروهای نظامی و قابلیت‌های مورد توافق را فراهم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24974" target="_blank">📅 21:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ای۲۴نیرز تصاویر جدید و جزئیات جدیدی درباره خلبان مهاجم: او چندین بار در گذشته به اسرائیل سفر کرده بود و قصد انجام این حمله را از ماه ژوئیه برنامه‌ریزی کرده بود. در امارات متحده عربی، مقامات در حال تحقیق درباره کارمندانی هستند که به این خلبان اجازه ورود به "فلای دبی" را داده‌اند. همچنین، بررسی می‌شود که آیا او یک هدف جایگزین را در صورت شکست طرح اصلی در نظر گرفته بود یا خیر، که احتمالاً یک پایگاه نظامی آمریکایی در اردن بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24973" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پزشکیان: هربار بازرسان آژانس به ایران آمده‌اند، مراکز هسته‌ای و دانشمندان ما شناسایی و پس از آن این مراکز بمباران و دانشمندان ما ترور شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24972" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24971">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود @WarRoom
🤣</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24971" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYAIBCD9ngXnpm0UugA0N8jKCN_Q_rY7rRjSbF1qLW1bgJ0O-F__wn-aJbDJcFDDxPsePxIKhZQWhwd5VPpKU4evwnxNmmFQsO6cvHv1bbd8RzZSjCiQkgX7qyqnNM4n2fB7358LMFoVE21JzBA8_R6DANrq6zHzqJF8zB6JSMVe5hS1kTIa5-nBreHXp4SnZZlVu_OFiLuUSemh5BStx--Sh890Lq9G7RSL3yiCx7qQCYxi7BhxWD5eGw6Uh1SQZq3HEFCaTAY_uWLH2Z700zEYNf4kySGOYR784ZyMr1H6CC0EOjcYVn1HvnpG14PhVxA_SwntrtnrqZqBo79IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه ترکیه، حاکان فیدان، وزیر دفاع ترکیه، یاشار گولر، و رئیس ستاد مشترک نیروهای مسلح، سرلشگر سلجوق بایراکتاراوغلو، در ریاض با همتایان پاکستانی و سعودی خود دیدار کردند تا در جلسه کمیته سیاسی، دفاعی و استراتژیک شرکت کنند. این کمیته بر اساس توافق مکه برای همکاری‌های دفاعی تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24970" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24969" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoKByFNN67wTOHkIntRp-8sY1vZKVfKDGp9gLhGUkA0imMC8jMpkvGsdhRphSCxUnlrSvwBAhRVguKhdfUFdg5Y1__d4LAk4wkMLDRnF_qlKjg0BCQ-rkQpa42CUXuk2e0Ap5u6aVfAJCeEjKGRf_4vk_4HT-OEn0QGeqBFj5tQ6lyPAJ8ZHwbHI87nanlXk666tuK26-C9Ez6wdc5g95P8GrpTc97eNOuVbO9Tx4m_0TG2KoQlk2EzvjkNQTBpQOm9uEMLRS8bw5z7GWKBAUjbOw6MO2rWcdiBSgWbmwqeW0dVIiQ_vBAG4esYduPvj741fFizrl5P7J55Jx0-EgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : آنچه باعث افزایش قیمت بنزین می‌شود، دیگر تنگه هرمز نیست، چون اکنون تعداد بی‌سابقه‌ای بشکه نفت تقریباً به‌صورت روزانه از آن خارج می‌شود، بلکه این کلمه است: «پالایشگاه‌ها»؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی، مانند کالیفرنیا، توسط دموکرات‌ها تعطیل می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24968" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسرائیل هیوم: آمریکا محدودیت‌های عملیاتی پیشین برای فعالیت نیروی هوایی اسرائیل در حریم هوایی عراق را لغو کرده و به اسرائیل چراغ سبز برای حمله به گروه‌های مسلح مورد حمایت ایران در عراق داده است.
این گزارش به نقل از منابع ناشناس منتشر شده و تاکنون از سوی آمریکا، اسرائیل یا عراق به‌طور رسمی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24967" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca7496737.mp4?token=Viss_vr63Q7K6vs2C1lPVtU6BRyyywsd35d0VYPLGm0CwULeIemUWn1VtozXLgx8CNOUBBJQbUCEPy3Ond7h6w_5G8labM2oMXU8jzJ9ZmkVBbBK7dMdJevKcSzXomaV3-H2h2NX2T_zxVVGHToJnsJAHZlW5c1kEYF4KCRMvsJPulWxKnHl8FyQCHhzdhca5kvecw6p4f6IbMpfRbJYPAwEDd8EXWq8fgIl8A6PH4KWFi3JWR7sYOo2M8QbO2QGGwcvy-TcS6sW9QWt4HBRvrODq8P5CVi1iTahTK0x5f3_e6rTSlrS3NE_SNegfSm_BEDm9J04bS73R2lMrvWrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca7496737.mp4?token=Viss_vr63Q7K6vs2C1lPVtU6BRyyywsd35d0VYPLGm0CwULeIemUWn1VtozXLgx8CNOUBBJQbUCEPy3Ond7h6w_5G8labM2oMXU8jzJ9ZmkVBbBK7dMdJevKcSzXomaV3-H2h2NX2T_zxVVGHToJnsJAHZlW5c1kEYF4KCRMvsJPulWxKnHl8FyQCHhzdhca5kvecw6p4f6IbMpfRbJYPAwEDd8EXWq8fgIl8A6PH4KWFi3JWR7sYOo2M8QbO2QGGwcvy-TcS6sW9QWt4HBRvrODq8P5CVi1iTahTK0x5f3_e6rTSlrS3NE_SNegfSm_BEDm9J04bS73R2lMrvWrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور جمهوری‌خواه ریک اسکات:
من هم از قیمت‌های بالای بنزین خوشم نمی‌آید، اما نمی‌خواهم با یک سلاح هسته‌ای کشته شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24966" target="_blank">📅 19:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش رویترز می‌گوید پاکستان پیش از آغاز عملیات صبح امروز،
تجهیزات نظامی، سامانه‌های پدافندی، توپخانه سبک، پهپاد و تجهیزات ضدپهپاد
به عدن فرستاده و
مشاوران نظامی پاکستانی
نیز در محل حضور دارند. اما رویترز تأکید کرده که متحدان عربستان قرار نیست مستقیماً در عملیات رزمی زمینی شرکت کنند. همچنین
پهپادهای ترکیه‌ای
که عربستان قبلاً خریداری کرده، در عملیات به کار گرفته شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24965" target="_blank">📅 19:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو : ما مأموریت را تکمیل خواهیم کرد. می‌خواهم بدانید‌که ما هر روز آن را تکمیل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24964" target="_blank">📅 19:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364dd49e8.mp4?token=BcAgUmzb6Bq_Uc8v0ksh8-kHiKS9POdyVVRmn4jdjvNyyv5LMJjDV5-AyymYUtsYY9sjFSyDZHd1aizWczV7GmNiOtU-_x813eiW27bcb6PBJ0Kd2yTcN00_75UcFyxtXGGKeb4ebjYKCCPCwkSWvt6MZMeZWHcPfTbcJFisculOtnVjowFqpGYorYoT5EQk8ZDsTBvZuriIYB74708J-JlWcFH20nkqZhKnBmfx6kTAImWKDH9zT6WOf7voSRYRjnqSVwReN7eUHuLsV9nRxr_bhLwJjaM3K3kBGF0uVVZESrLsgyOcZUp0gDNjXBdxdFWA9yuttF4-S4LKoCGEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364dd49e8.mp4?token=BcAgUmzb6Bq_Uc8v0ksh8-kHiKS9POdyVVRmn4jdjvNyyv5LMJjDV5-AyymYUtsYY9sjFSyDZHd1aizWczV7GmNiOtU-_x813eiW27bcb6PBJ0Kd2yTcN00_75UcFyxtXGGKeb4ebjYKCCPCwkSWvt6MZMeZWHcPfTbcJFisculOtnVjowFqpGYorYoT5EQk8ZDsTBvZuriIYB74708J-JlWcFH20nkqZhKnBmfx6kTAImWKDH9zT6WOf7voSRYRjnqSVwReN7eUHuLsV9nRxr_bhLwJjaM3K3kBGF0uVVZESrLsgyOcZUp0gDNjXBdxdFWA9yuttF4-S4LKoCGEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسحاق هرتزوگ، رئیس‌جمهور اسرائیل: «رئیس‌جمهور ترامپ درباره تهدیدی که از سوی تهران وجود دارد،
حق دارد
. ما با یک
امپراتوری شیطانی
روبه‌رو هستیم که می‌خواهد جهان را به‌شدت افراطی کند، جهان آزاد را به تصرف خود درآورد و تا اروپا و ایالات متحده پیش برود.»این موضوع فقط نگرانی اسرائیل نیست و
تمام منطقه همین احساس را دارد
؛ چه آن را علناً بیان کنند و چه پشت درهای بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24963" target="_blank">📅 18:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3B5VQqDfWsa89u_wp8zaX-3xPx5Zoeo_YZgrLyCLCJdIwyCjbhDpPh0LH8I1P_93XaNOSzbE8XJHJbfdi6v3eUh1cGU4B-fNtXApbKtuBY2lZlrtuLGQcdWfa9y8YQdXMC1h0ePUY17TtvLQHdMhQijnktbwqL4QAkCPw_ng7NBOyBWUKGs__plWhfh1OqjCj71xcn47FMxIHhAnbYSO17-FRLE163wZFtd7zflnOrqN0M72Zuk6Fxw4xPRMcCXpbEdmneJwjOqKF-jzPXLP0c2d4Z_3zreyboytZUauTKa09i85N2nZRjwCTwVZ7B1_R94Rp052GXb294G9z-NzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور رژیم جمهوری اسلامی , اسکندر مؤمنی برای شرکت در مذاکراتی وارد دوحه قطر شد هم زمان ۶ سوخترسان و جنگنده های آمریکای با تمرکز بر تنگه هرمز در حال اسکورت کشتی ها از مسیر جنوبی تنگه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24962" target="_blank">📅 18:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adeQqHH4R8dF1Im5Z6XJQADjY_lD74614Soiofx12UTNDtT2rT-Gy_B6qscNE17oubHP6Hf8ENVMhLIPne3NLW9aCdX9Lh5F90mnCVGwzEzmI9SRp7RE1QMiTXXstzV0ljsCeLX039b_W9uW6VGT19ZahjTDBPWyZFKi-pBF0G9P4fB5pcmfwXm99RSWk15lwAqr_lAkDpdLQ6HOl4oyNgfDvQy4MVPWj1sD9ZKauckzTvGFWmridLPcVKNOs1x-AmTa8z9xJgSMygl8URpyvm4M_KI49j3sw8D6K3XHV52UeQi2ind4jkaxTV2Q5zJwWEzB9zIkeCn_902_98qSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است. یک منبع موثق گزارش داده است که یک نفت‌کش حامل نفت خام، در ناحیه‌ای بالاتر از خط آب‌خور، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
مقامات در حال بررسی موضوع هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24961" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب:
آیا آمریکا و استارلینک می‌توانند بدون همکاری حتی یک اپراتور یا نهاد ایرانی، اینترنت را مستقیم به گوشی مردم ایران برسانند؟
فناوری «Direct-to-Cell» برای همین نوع اتصال طراحی شده و گوشی معمولی می‌تواند بدون دیش و دستگاه اضافی مستقیماً با ماهواره ارتباط برقرار کند؛ ماهواره عملاً مانند
دکل موبایل در فضا
عمل می‌کند. در مدل فعلی، استارلینک عمدتاً از فرکانس و شبکه اپراتورهای شریک استفاده می‌کند، اما در سناریوی ایران می‌توان از
یک اپراتور خارجی یا معماری مستقل ماهواره‌ای
استفاده کرد؛ بنابراین همراه اول، ایرانسل و رایتل الزاماً نباید همکاری کنند. در این حالت می‌توان برای کاربران
eSIM
( آسان ولی نیازمند گوشی مدل بالا)
یا سیم‌کارت فیزیکی(
سخت در توزیع ، ولی راحت تر) صادر کرد، اما سیم‌کارت به‌تنهایی کافی نیست و باید شبکه ماهواره‌ای، احراز هویت و فرکانس موردنیاز از سمت استارلینک و اپراتور شریک خارجی فراهم شود که این هم میتوانند . از نظر گوشی، سرویس‌های ماهواره‌ای اپراتورها در برخی کشورها از
iPhone 13 به بالا
پشتیبانی می‌کنند(قابلیت‌های ماهواره‌ای اختصاصی اپل از
iPhone 14 به بعد
وجود دارد این دو سرویس با یکدیگر یکی نیستند) اما سؤال مهم‌تر این است که آیا حکومت ایران می‌تواند چنین ارتباطی را قطع کند؟
قطع دکل‌ها و شبکه اپراتورهای داخلی، ارتباط مستقیم گوشی با ماهواره را قطع نمی‌کند
؛ ولی هیچ تضمینی وجود ندارد که دولت نتواند با
پارازیت و اختلال رادیویی روی فرکانس مربوطه
یا روش‌های فنی دیگر ارتباط را مختل کند. بنابراین «کاملاً مستقل از زیرساخت ایران» از نظر فنی ممکن است، اما «غیرقابل اختلال توسط حکومت ایران» نیست.
اگر تصمیم و زیرساخت لازم آماده باشد، راه‌اندازی محدود می‌تواند در مقیاس چند هفته تا چند ماه تصورپذیر باشد، اما ایجاد اینترنت موبایلی گسترده برای میلیون‌ها نفر به زمان و ظرفیت بیشتری نیاز دارد و اگر در انتظار این سرویس هستید بهتر است گوشی با قابلیت eSIM هم آماده داشته
باشید
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24960" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب: ماجرای موسوم به «طاعون روسی» پس از مرگ یک پژوهشگر ۲۸ ساله در مؤسسه تحقیقات ضدطاعون در ایرکوتسک روسیه مطرح شد؛ اما
آزمایش‌های رسمی تاکنون ابتلای او به طاعون را تأیید نکرده‌اند
و علت مرگ، ذات‌الریه با منشأ نامشخص اعلام شده است. گزارش‌هایی درباره شکستن لوله حاوی باکتری یرسینیا پستیس منتشر شد، اما مقام‌های روسیه می‌گویند
هیچ حادثه آزمایشگاهی و ارتباطی میان مرگ او و عوامل بیماری‌زای محل کارش پیدا نشده است.
حدود ۲۰۰ نفر تحت مراقبت قرار گرفتند و در میان افراد بررسی‌شده
دو مورد کووید و دو مورد راینوویروس
شناسایی شده، اما مورد جدیدی از طاعون گزارش نشده است. کشورهای همسایه از جمله قزاقستان، تاجیکستان، ازبکستان و قرقیزستان
کنترل‌های بهداشتی مرزی را افزایش داده‌اند، اما مرزها بسته نشده‌اند.
کارشناسان نیز می‌گویند فعلاً هیچ شواهدی از شیوع طاعون ریوی یا یک بیماری جدید مشابه کرونا وجود ندارد.
طاعون ریوی در صورت تأیید بیماری جدی و بدون درمان می‌تواند مرگبار باشد، اما با تشخیص سریع و آنتی‌بیوتیک قابل درمان است.
بنابراین ادعای «طاعون مهندسی‌شده روسی» یا یک همه‌گیری جدید در حال حاضر
فاقد شواهد معتبر است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24959" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c88d29dc5.mp4?token=DKKHWH3DTZkPoTNMI4xWeN_6Wns5X66I6txyouV6SPzf9gLmZoXnvO1d1kfqUq8jTDKaKTBiNM6Bxv2GPWWkK_4yP1Q4rXSDlQP8ELk8LE-HeC03JLQmgyShjOMmMaLP1XRgBvowwPNfNXC-LEWaFFY9DCrFeKtX9ldyLvJz_KRfEBdjrcFO3Q-3SnmI7uc6hHazFwJ1w37pyUs29-rx_tyIPm_HexX2pwlBVQ2v9XaSi1YPQDNsnBuP5yRygCtPvsL0OKkkxVVAqKOCmtmEkZ_gKHn4PGESM8Au2BnGM57MzfBXg3cbaRow4toVLNWO8p7UEIJurIhpLIt_tk-59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c88d29dc5.mp4?token=DKKHWH3DTZkPoTNMI4xWeN_6Wns5X66I6txyouV6SPzf9gLmZoXnvO1d1kfqUq8jTDKaKTBiNM6Bxv2GPWWkK_4yP1Q4rXSDlQP8ELk8LE-HeC03JLQmgyShjOMmMaLP1XRgBvowwPNfNXC-LEWaFFY9DCrFeKtX9ldyLvJz_KRfEBdjrcFO3Q-3SnmI7uc6hHazFwJ1w37pyUs29-rx_tyIPm_HexX2pwlBVQ2v9XaSi1YPQDNsnBuP5yRygCtPvsL0OKkkxVVAqKOCmtmEkZ_gKHn4PGESM8Au2BnGM57MzfBXg3cbaRow4toVLNWO8p7UEIJurIhpLIt_tk-59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز:
نیروهای دولت یمن با پشتیبانی عربستان مدعی
تصرف منطقه راهبردی ذوباب و مواضع کلیدی مشرف بر تنگه باب‌المندب
شده‌اند. طبق گزارش‌ها،
فرودگاه ذوباب
نیز به کنترل این نیروها درآمده و مسیرهای تدارکاتی منتهی به باب‌المندب قطع شده است. درگیری‌ها همچنان در اطراف برخی مواضع نظامی ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24958" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز:
بانک HSBC میانگین قیمت طلا را برای سال‌های آینده کاهش داد؛ پیش‌بینی ۲۰۲۶ از
۴۵۶۰ به ۴۴۹۰ دلار
و پیش‌بینی ۲۰۲۷ از
۴۹۲۵ به ۴۸۲۵ دلار
در هر اونس کاهش یافته است. با این حال، HSBC همچنان چشم‌انداز بلندمدت طلا را مثبت می‌داند و معتقد است اگر قیمت به محدوده
۴۰۰۰ دلار یا پایین‌تر
برسد، احتمال افزایش خرید توسط بانک‌های مرکزی وجود دارد که می‌تواند از قیمت حمایت کند. در کوتاه‌مدت،
افزایش بازده اوراق آمریکا، دلار قوی و رشد قیمت نفت
همچنان از عوامل فشار بر طلا هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24957" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990c4f7388.mp4?token=NizgI2PH7IYjgCyqKiVkuteaiZfD68p1fW4_no1d1JZ6IT92E8jB00YSgXGM5w3h3HXApteZm0G94doHsQzVYc5ox6eJaSkaXf4GnMwmqSrt28Plt1IFMylh7gkcfw9EbbakFNYyACY65qkJ0nHubo8IJjiN2mKLOtWZSWV8RsK1FQ37ikCYMsKG-5xA9M91IoMha8kSoZ4JFbr256Nxc0nNK3e8sy1sCPBbkBayzkwst4HGQtWaHj4bw-4Rh024D8pIiGuclnGVOje8M_p8Y-DndYyjnvsWiUrnrvTMnjsj1vdK3ZdGtwt2PnorX1mpKKwu00yXtf6fsMEryYzeO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990c4f7388.mp4?token=NizgI2PH7IYjgCyqKiVkuteaiZfD68p1fW4_no1d1JZ6IT92E8jB00YSgXGM5w3h3HXApteZm0G94doHsQzVYc5ox6eJaSkaXf4GnMwmqSrt28Plt1IFMylh7gkcfw9EbbakFNYyACY65qkJ0nHubo8IJjiN2mKLOtWZSWV8RsK1FQ37ikCYMsKG-5xA9M91IoMha8kSoZ4JFbr256Nxc0nNK3e8sy1sCPBbkBayzkwst4HGQtWaHj4bw-4Rh024D8pIiGuclnGVOje8M_p8Y-DndYyjnvsWiUrnrvTMnjsj1vdK3ZdGtwt2PnorX1mpKKwu00yXtf6fsMEryYzeO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو تأیید کرد
بمب‌افکن‌های آمریکایی بلافاصله پس از طرح تروریستی، پایگاه ویرفورد را ترک کردند، اما این جابه‌جایی را «غیرعادی» ندانست: «چرخش‌های منظمی وجود دارد… من مستقیماً این موضوع را به جابه‌جایی انجام‌شده مرتبط نمی‌کنم. دیدن چنین چرخش‌هایی غیرعادی نیست.» تمام بمب‌افکن‌های آمریکایی مستقر در این پایگاه به پایگاه‌های اصلی خود در آمریکا بازگشته‌اند. هر ۶ مظنون این پرونده نیز آزاد شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24956" target="_blank">📅 17:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32f588d98.mp4?token=Uncz7JaInOTc9P7Wf_NFqsa3S0J1bJMIb7TTE9EzVnB1KRZ6_B8hTPd8xKZqWuZI_9d1DJjk5AkWIbWTq9_74WUAELo41_wJQ6GsGhpD-m3jHYoUVS_rJA0SJtzeyImhgppCaQW0FqzCMj_z9BldRB3bIiBYtuM868ozg6Zv2smmVMZtVfAjTEifXioIQx3mnI0yVA8NAaBrOTdA19BMRJZk4dsHIEECtqOHs0tMZ8qTJC7GD7SddNeQPMvJu7_wWUYkBzDb0zNGx6aZod9rRDOxvL-NrtsP2b34-qOPpYDgNS0beyF1G1NHWNTDh0dh0uYtsSYQ9I2zR93OoYJc8DYFWsgTc4y_iLA-WP2zQ_qOxiCFT9OOplLy-o0eVI4BBTi9q7tNrkebbqXtkswz86GqQbqOJfSyGX4IFXTXjqBcpYF8zayubGYWqHlpV-W01LRuXktbHmnQ2Jb5RzrC0cfTSued_oqV8Ty3XIyg0dGwJBp0FTlDB9x5LoxtdaTNEVwkm0bJMydl3z6O9rUtY_RbuAlyOmOMs6s4QXuGv8223oxZXTZTIYK6bwHs1Wdlc98lcvMru6lCYA7kzt7KvK5BFuL3zuXYWW1sE39K5onbOBTylDEuvtzCL0RwV-LPdQnNTI7bkpr7ubxFWTL128NgbHCeZcnkvjSZ0jFzIXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32f588d98.mp4?token=Uncz7JaInOTc9P7Wf_NFqsa3S0J1bJMIb7TTE9EzVnB1KRZ6_B8hTPd8xKZqWuZI_9d1DJjk5AkWIbWTq9_74WUAELo41_wJQ6GsGhpD-m3jHYoUVS_rJA0SJtzeyImhgppCaQW0FqzCMj_z9BldRB3bIiBYtuM868ozg6Zv2smmVMZtVfAjTEifXioIQx3mnI0yVA8NAaBrOTdA19BMRJZk4dsHIEECtqOHs0tMZ8qTJC7GD7SddNeQPMvJu7_wWUYkBzDb0zNGx6aZod9rRDOxvL-NrtsP2b34-qOPpYDgNS0beyF1G1NHWNTDh0dh0uYtsSYQ9I2zR93OoYJc8DYFWsgTc4y_iLA-WP2zQ_qOxiCFT9OOplLy-o0eVI4BBTi9q7tNrkebbqXtkswz86GqQbqOJfSyGX4IFXTXjqBcpYF8zayubGYWqHlpV-W01LRuXktbHmnQ2Jb5RzrC0cfTSued_oqV8Ty3XIyg0dGwJBp0FTlDB9x5LoxtdaTNEVwkm0bJMydl3z6O9rUtY_RbuAlyOmOMs6s4QXuGv8223oxZXTZTIYK6bwHs1Wdlc98lcvMru6lCYA7kzt7KvK5BFuL3zuXYWW1sE39K5onbOBTylDEuvtzCL0RwV-LPdQnNTI7bkpr7ubxFWTL128NgbHCeZcnkvjSZ0jFzIXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل: «رهبران جهان به من می‌گویند: تو از دل جهنم ۷ اکتبر برخاستی، افراطی‌های اسلام‌گرا را شکست دادی و به بشریت امید دادی که می‌توان نیروهای تاریکی را شکست داد.
سپس بسیاری از آنها اضافه می‌کنند: ای کاش جوانانی مثل اینها در میان ما هم رشد می‌کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24955" target="_blank">📅 15:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2091a813.mp4?token=hVC9bAR6Wz96Lw4qYNA6B_H3Ob4uc5AtemiPhQoqJwfgNnnTONT3ge5tENG_eKXqpX8R2oxDWihj0_gc-z_6MDg_HCyKFex740X6oF7Vhd926k0AOQC7AyQBF6AxI0d4PXtkj7ZR40l9-kgiLOfHS1QuiIl31SwwAzfhCfm3Jny5WC0iaB0BEqbhb78JehhKxaA7esQ_wXD7klC4g3Y6LT_cb_zzm3f3FirHQQ_jYwjCX1mDn9gzGUsHE0jjTi5mkOAPS6k0rt-tWdcfbmsrn7__cM1G8kITERjWkLTkw3YCjElSx-iSXj9uLLPkzb6trAJDkKOKIU9bb_a5jsbx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2091a813.mp4?token=hVC9bAR6Wz96Lw4qYNA6B_H3Ob4uc5AtemiPhQoqJwfgNnnTONT3ge5tENG_eKXqpX8R2oxDWihj0_gc-z_6MDg_HCyKFex740X6oF7Vhd926k0AOQC7AyQBF6AxI0d4PXtkj7ZR40l9-kgiLOfHS1QuiIl31SwwAzfhCfm3Jny5WC0iaB0BEqbhb78JehhKxaA7esQ_wXD7klC4g3Y6LT_cb_zzm3f3FirHQQ_jYwjCX1mDn9gzGUsHE0jjTi5mkOAPS6k0rt-tWdcfbmsrn7__cM1G8kITERjWkLTkw3YCjElSx-iSXj9uLLPkzb6trAJDkKOKIU9bb_a5jsbx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در مراسم گرانیداشت ۷ اکتبر : اسرائیل اجازه نمیده جمهوری اسلامی موجودیت این کشور رو تهدید کنه. رژیم تهران ضعیف‌تر از هر زمان دیگه‌ای از زمان تأسیسشه، برای بقای خودش می‌جنگه و در نهایت از بین خواهد رفت. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24954" target="_blank">📅 15:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو در مراسم گرانیداشت ۷ اکتبر : اسرائیل اجازه نمیده جمهوری اسلامی موجودیت این کشور رو تهدید کنه. رژیم تهران ضعیف‌تر از هر زمان دیگه‌ای از زمان تأسیسشه، برای بقای خودش می‌جنگه و در نهایت از بین خواهد رفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24953" target="_blank">📅 14:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0ikjLWcXOaReUO71gz3y-B8gxNi9Bh-pB-CD_jw0ElPY45b04MjQlclCkDWpZJF-BswTD7qCN4TyJw0AsawgFZvLMOvKPd8LOzmXa4aIz22XwgxeyZACKTKyzQ8Pqj7IQONwrFmk62WDh55T4KYYk6Xib696ktjb_8F1jo_zWzoxNXulBdF8jmSlYvWZfLlmoczvJwNGfiWseii8md2tEQgtDxYQZfcWoBQyH6su7Wk4iAf35e4xwIX9i0IerTXrFIoC5TPB22ofrfjPpxoSO_dvtsoYf8VRI158NzAIjYH9UVzVlQqa8P-5WM-Ly_hhX84mu-cFByqLG0PpZMUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم میهن بکش هر جوری که میتونی نا امید نشو … چیزی‌نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24952" target="_blank">📅 14:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سازمان دریایی بریتانیا :  گزارش می‌دهد که ایران یک نفتکش را که قصد داشت خلیج فارس را از طریق مسیر عمانی تنگه هرمز ترک کند، مجبور به بازگشت کرد و نفتکش از دستورالعمل‌های سپاه پیروی کرد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24951" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-lzNWMyx5SjsWVOo4VqRsN1X8SjlLJDVIpXcyJ34PrA1Yc7AmtBsc8TdjcloQU39uOC_KvFURNYulqq2sfUWABhp8zqqdIX2kycH6KePFmuS0Z0MRB2MCtJdFW-zbtjPGYBB4R9GfkRrvs5TC5Fi7QoNhrG4sifHCh14jF0_8ClVUnGJKcQgXY3-ZEntMIJ9uS-7BCOJ-kphmX1sVcJK40nCaFVpjJJ5dhIJXFRIGyyb8pMJHK3Kqi4EjUidAXa0kNLQdX33FdzdFmV0uaPbIG8uCuGyLS7BAJFQ7vQ6DLURF4VkYyqWhIZxo6zjpdEc6BFw3OpDOHMUuq3_8Xjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گشت‌وگذار یک دانشجوی عراقی با خودروی آمریکایی دوج چارجر در همدان، در حالی که تصویر تروریستها؛ علی خامنه‌ای، قاسم سلیمانی و ابومهدی المهندس (جمال جعفر محمدعلی آل‌ابراهیم، معاون پیشین حشدالشعبی عراق) روی بدنه آن نقش بسته است. @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24950" target="_blank">📅 13:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دایرک جای ، کامنت جای درد و دل و جای سوالی های  بی مورد و آموزش کامپیوتر یا پشتیبانی اینترنت شما نیست ! برای آخرین بار میگم ۹ ماه شد چرا ملت نمیفهمند ؟ مسیج پشت هم ندین در هم و جا بجا میاد !  فقط در‌یک پیغام ،الان این دو نفر‌هی دارن پیغام میدن یکی قبض برق…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24949" target="_blank">📅 13:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGRT6dwWE2VSc4kkqATmzplt4Bv2AFL29QnVxpq73IC-snIuBr2t3j6KQPrn-xkq1imE_LRGd6bSQLdHeX8WGdlJGqRXZ1yl9EFVp--iyGq8aNsCPo5YzSCkujXsf2b6K1JBXj1kZsXRPBWUFTbEDw4TjowzeLRMfH3NHJESiIpyqLNmoFrz3bj_1734iDviVQRbT436DwbVGmBpvJcOo2zsBbt5sDsnMMUv5p6oap0PLN3Q07Xaw1do-2ShvnmtcP1R06sFzzuaFa4C8rVO7E9V9sxu-pAH6IPccGgJzcQ704bP_Si4POnzGUuE3lS2SKy7m_6mRmrPGGWfgau5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرک جای ، کامنت جای درد و دل و جای سوالی های  بی مورد و آموزش کامپیوتر یا پشتیبانی اینترنت شما نیست ! برای آخرین بار میگم ۹ ماه شد چرا ملت نمیفهمند ؟ مسیج پشت هم ندین در هم و جا بجا میاد !  فقط در‌یک پیغام ،الان این دو نفر‌هی دارن پیغام میدن یکی قبض برق داده و اون هو میگه من کجام ، اخه یک بگه به تو چه ، چرا حالیشون نمیشه من نمیدونم !!!! من مشاور نیستم چیزی باشه برای همه میگم دایرکت جواب‌ نمیدم</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24948" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سردار حسین رحیمی، رئیس پلیس امنیت اقتصادی فراجا، در همایش سکوهای اینترنتی هشدار داد سایت‌ها و کانال‌های داخلی نباید قیمت‌های غیرواقعی ارز را که از سوی برخی کانال‌های خارج از کشور منتشر می‌شود، بازنشر کنند. رحیمی گفت انتشار این قیمت‌ها می‌تواند به التهاب بازار…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24947" target="_blank">📅 12:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سردار حسین رحیمی، رئیس پلیس امنیت اقتصادی فراجا، در همایش سکوهای اینترنتی هشدار داد سایت‌ها و کانال‌های داخلی نباید قیمت‌های غیرواقعی ارز را که از سوی برخی کانال‌های خارج از کشور منتشر می‌شود، بازنشر کنند. رحیمی گفت انتشار این قیمت‌ها می‌تواند به التهاب بازار دامن بزند و به مردم، مصرف‌کنندگان و کسبه فشار وارد کند و تأکید کرد پلیس با انتشار و بازنشر قیمت‌های غیرواقعی ارز برخورد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24946" target="_blank">📅 12:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24945" target="_blank">📅 12:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الجزیره به نقل از محمد الشرقاوی، استاد حل‌وفصل منازعات بین‌المللی، گزارش داد که با توجه به مواضع اخیر دونالد ترامپ و مقام‌های جمهوری اسلامی، احتمال روی‌آوردن آمریکا به گزینه نظامی افزایش یافته است. الشرقاوی پیش‌بینی کرده است که
ترامپ ممکن است از هفته پایانی مهر تا نیمه آبان، همزمان با انتخابات کنگره آمریکا، حمله‌ای غافلگیرکننده به ایران انجام دهد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24944" target="_blank">📅 12:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">در پی فعالیت نیروهای ارتش اسرائیل برای نابودی تونل ها و مخفیگاه های دشمن در ساعات آینده، احتمال شنیده شدن صدای انفجار و لرزش در مناطق غرب گلیل، مرکز گلیل علیا، دره الحوله، رشته‌کوه رِمام و احتمالاً در شمال جولان وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24943" target="_blank">📅 12:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw1b-BBuGmVvO64TeBFM3Ayzz-fGWFKzPxueqXs1It8WY3tmk_8hoT90bTSPDXwW3okG1mURBcEhXnHK7_1K0hqJSsArA6DJ7FP6xYrbF5x-x5kye4OkVLsXLMOlTDEGfGyarlan_NTMtzMIbIJgOLQw187kROoEmT2CpasTwwswmMQb2Ez9E5fBLWV18R3neikq3E8l2K435JMHwDNK3bdgfSeAiARuV7ktqs4sTVhDdOF5VPqijGhbuAwM3AlA2cloNSmtUU5jHrm2h3JWlHYBN6YyYm-3sBWine3TVc8cKCtSyKTYceZWGFRllsVy5ASuBKphgCjARZqw5WlXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون حقوق بشر ایران اعلام کرد
علیرضا سپاهی و علیرضا رئیسی
، از متهمان پرونده «میدان علیخانی» اصفهان، بامداد امروز دوشنبه ۱۳ مهر ۱۴۰۵ در زندان دستگرد اصفهان، همزمان با اذان صبح، حکمشان اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24942" target="_blank">📅 11:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ای۲۴نیوز : دولت ضداسرائیلی اسپانیا سقوط کرد ، نخست‌وزیر اسپانیا، سانچس، از برگزاری انتخابات زودهنگام در تاریخ ۲۹ نوامبر خبر داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24941" target="_blank">📅 11:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خودروی متعلق به دفتر نخست‌وزیری اسرائیل در یک تلاش برای ترور هدف تیراندازی قرار گرفت و مورد اصابت گلوله قرار گرفت. بر اساس اطلاعات موجود، به نظر می‌رسد هدف مهاجمان پسر آقای دومرانی (از مقامات دفتر نخست‌وزیری اسرائیل) بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24940" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GziCoMA0D5w4Gz1O-phhfYEmZhlHWoW70EHeerMlRX0jpN6O-O9uo3g1rviTDdx6eCnHEFugcBTjVGzRjoB-gnrhjmlzlqg2JDiccDXLTn7EDquB9Iw5OvyPsyl_bXd68bLT2eHySIOb1gI5LmEpeRRZbE0phuS2qdDkzmQMy-yVeZbkTnrdtLnNnklHTr1esxTSV2fiHaCj3w7kSbccz6QyHknAtpv303u5CedLfzVJA61UTqU4h3JosC69W5218zhu_sQo72VASY6Jfg29Z6DdLHullDAsp7ud4dDEJB3Syu2Ip_qDyYtLnLFQDP3UKfncjElxTq6vUJc-hIt-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQC4wnirnxSKCBHXrkS4_34ozInwPLg8DFFwQHLGDfY76rIFs8X8bM6Xsvj6Ok6MVEnxVPDOTQr4QAcvl7WDABnDlkqNiOP0VgEh2Z_Te7AZ-bP_0a6gDHI5v3OfFYc4gzCjgztf18s4Pf6ZN-cCnWA70qCxGLGKug17gUDyhB5ICkt7crKVFTLdHv_SqE_B791lzJt83QA9bcHyhHdqn-cmjq9Gyo6Ne1vdybDymYjZiWh5Hw53iCaR2kc43BQZyTXAUo48ovRCXDIfdYcqkUDjYgV7iyG-CW7z545koaNFPpLlP2IASIam1H6BnXfeQRf1j0Of7sQ1BVp_fkJqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE3-Kpa9P1ZLq6nC1GUbrX07OG41dEfLYuPd1q4eHot9TQFuBatlGZC_kFXEYrj2Wp-71NsCtm633AhQo9H69qUeVVc52EdnwcEnNKfscFwlI7tQmx4GlD74OxqQ51FszM6MPNWodI89bPbCcENxK5amR8lhra0pFld6hiFWWJhH4AICEVzRL1haUryiqqJanjeODkHZHlu1RA4HM3J05apYfeM7y-FOTWMkb-BmACpAx3PYdSsalzWaiIe8WlFfvD7wPWMuyMbO8PRrIgvXTPioS2bzzZqPPKXfQuBeKTTB8Ey9CG6YDZN1BCteS1hd_scYs_G7ZY4zIfsJxsDipg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568831ae66.mp4?token=PrKBCksf9UUnfINTJh-04bCK8vZe_A9UDJmFWvJj95uGh5cpyEYFoTJbCo3WDcQf_gLJ9J1E5TAAMDri6LGtpQHS_bcBToG5mKQ2KXUZ-LWzSIXYEhnr_U6XW-DY3FrUg0aJVW0AFVg3crljBn83_g8AdEOfIwrf-1d3jd7gBAoEthmCbCvcikBV2NV5jYYc4v0sStSaB2bidJjraNEO1W8RuBPIOL9TqjSTfvcmximfUZXvvMW0_V-6c2n1O01Gss_STbLsCp0cWLseXqhJSvN31R8CW0XFNPDBAXBhKgBRr5zzg4_guCmsVGEdXV4z60R-Zp328ZBITcPSGFFlMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568831ae66.mp4?token=PrKBCksf9UUnfINTJh-04bCK8vZe_A9UDJmFWvJj95uGh5cpyEYFoTJbCo3WDcQf_gLJ9J1E5TAAMDri6LGtpQHS_bcBToG5mKQ2KXUZ-LWzSIXYEhnr_U6XW-DY3FrUg0aJVW0AFVg3crljBn83_g8AdEOfIwrf-1d3jd7gBAoEthmCbCvcikBV2NV5jYYc4v0sStSaB2bidJjraNEO1W8RuBPIOL9TqjSTfvcmximfUZXvvMW0_V-6c2n1O01Gss_STbLsCp0cWLseXqhJSvN31R8CW0XFNPDBAXBhKgBRr5zzg4_guCmsVGEdXV4z60R-Zp328ZBITcPSGFFlMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس سیستان‌وبلوچستان: افراد مسلح به گشت انتظامی پاسگاه نوکجو در محور بمپور–ایرانشهر حمله کردند. در این حمله دو مأمور انتظامی کشته شدند. جزئیات بیشتری درباره مهاجمان و هویت گروه مسئول هنوز اعلام نشده است.  @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24936" target="_blank">📅 11:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هواپیمایی جمهوری اسلامی ایران :  پس از رفع محدودیت‌های عراق برای انجام پروازهای نجف، نخستین پرواز ایران‌ایر در مسیر تهران-نجف ساعت ۸:۱۵ صبح امروز از فرودگاه امام انجام شد ولی پرواز ماهان‌ایر‌ مسدود خواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24935" target="_blank">📅 10:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d83bdd494.mp4?token=I1x0CDTaqPhTpMc1swGe4nSgTWMtuGAiQhUwBi4Zf1-4kkWptdK-uY7824-1kHuGSw46E38bgcX2u02VvLbeYkxXDve9Qt-Gw8GUujAKlhDA68-2wCyWZIQOwME4v82Cqn90Bdob1zRAA9E0Ojrb6X2Mf7gLJRniynjtqKpe_9RUMFiK6g91ssYrFCSm4VkA4LpQQRc--R8-B6OqnRjv2AYybkAdC7jxhmo7GifbWPx2jQzQYR0Y4-6uy0AJvdJiJ62KaEFP_f5RR3ck_T0VSwXNM-mH4JZoc05XdfN310mcDeuzA9XDrxyqsgQV-oEtPiNJjzUghLXuu3KI-0nOfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d83bdd494.mp4?token=I1x0CDTaqPhTpMc1swGe4nSgTWMtuGAiQhUwBi4Zf1-4kkWptdK-uY7824-1kHuGSw46E38bgcX2u02VvLbeYkxXDve9Qt-Gw8GUujAKlhDA68-2wCyWZIQOwME4v82Cqn90Bdob1zRAA9E0Ojrb6X2Mf7gLJRniynjtqKpe_9RUMFiK6g91ssYrFCSm4VkA4LpQQRc--R8-B6OqnRjv2AYybkAdC7jxhmo7GifbWPx2jQzQYR0Y4-6uy0AJvdJiJ62KaEFP_f5RR3ck_T0VSwXNM-mH4JZoc05XdfN310mcDeuzA9XDrxyqsgQV-oEtPiNJjzUghLXuu3KI-0nOfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدئویی که امروز کانال های روسی منتشر کردند یک تیم پدافند هوایی متحرک روسیه با موشک دوش‌پرتاب 9K38 ایگلا / SA-18 سامانه‌ای فروسرخ برای مقابله با اهداف کم‌ارتفاع—به یک پهپاد اوکراینی شلیک می‌کند. بنا بر ادعا، پهپاد پیش از برخورد با تأسیسات ذخیره‌سازی نفت سرنگون شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24934" target="_blank">📅 10:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احراز هویت تصویری کاربران حقیقی ایرانی الزامی شد
مرکز ثبت دامنه‌های اینترنتی ‎.ir و دات ایران:احراز هویت تصویری سطح ۲ برای کاربران حقیقی ایرانی الزامی شده و ارائه خدمات تنها به کاربرانی که این مرحله را تکمیل کنند، انجام می‌شود
تکمیل‌ نکردن این فرایند، موجب محدودیت در دریافت خدمات خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24933" target="_blank">📅 10:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارشهایی از شروع اعتصاب در بازار تهران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24932" target="_blank">📅 10:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fExZlD1zR4Qk4bm1eE6vpMJxuLI3T1CQX0PcEfrUrcA91HBHftyMrVBZmW_nd6lYsJ7q5SbrAd4wh5e1_3sjds1f8xXh4dd0zguZMWK6jWtBRfyBYMo-BvhoZeDIneq6N0UrboQG6pjCHTuo1pRSMu6kWSEu1-HJht0gFIu4gdr7PRmDIaokto23gc0kSXN1JXaXR48BRgryOrySgJPfgug-EEIjYhBqb0eEi1YkYuiLueVQWgOcxhOa9HNrXg8YOtD_S30vstm5rU0JrsIbcno4c8YWzUpR6eeHsGDTO15MJUzVzf-1o9YOOuT74jy1h1TrTe3mHiI454zQUpTWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار پشت کوه صفه اصفهان ، شبهای جنگ اونجارو زیاد زدن،ولی به نظر من رژیم داره تونل‌های مسدود شده رو باز‌ میکنه( رنگ عکس‌رو کمی‌تغییر دادم ستون دود معلوم باشه مال همین الان هست)
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24931" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24930">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNNECpGZd4E2KVEf11bIohJvWAKk-lc6y2UQf8s6qPxexoNODT34o_uPOTFFRP9lQC7gwbENUBuPeVN4zSusDsDUQWpTJcjw5AcNyGjH-e8RYmAmt4ccXNHQjgCvuUs02NqcAf3VTNgEGP5GadsBzEUdKwB-bHmGFfNyuYSjd60hwcBxHn-dph0NVuGBZm-Cjk2fdJx97En-b-477MX-9jqWlitlBboOHFJETq1A1NSXuzl-Mddrl0_t0waIUX5n5XXgPVFxT10P0AVAt2b7dNZv-ZKq__cApO8nHA296p8CxHh8RofTl2vUsDj0YXVTg8GOKpOFMG4_A4x-m_ikhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24930" target="_blank">📅 10:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پلیس سیستان‌وبلوچستان:
افراد مسلح به
گشت انتظامی پاسگاه نوکجو در محور بمپور–ایرانشهر
حمله کردند. در این حمله
دو مأمور انتظامی کشته شدند
. جزئیات بیشتری درباره مهاجمان و هویت گروه مسئول هنوز اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24929" target="_blank">📅 10:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آی۲۴نیوز:
یک توریست آمریکایی در نزدیکی
ساختمان‌های دولتی اسرائیل در اورشلیم
پس از اعلام اینکه قصد انجام یک حمله تروریستی دارد، بازداشت شد. نیروهای امنیتی پس از دریافت اظهارات او، وی را دستگیر و تحقیقات درباره انگیزه و احتمال وجود تهدید واقعی را آغاز کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24928" target="_blank">📅 10:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیروهای دولتی یمن : عملیات‌های دقیق علیه مواضع شبه‌نظامیان حوثی در محورها و جبهه‌های صعدة، الجوف، تعز و ساحل انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24927" target="_blank">📅 07:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو، نخست‌وزیر اسرائیل: حوزه دریایی عملاً به یک میدان نبرد بین‌المللی تبدیل شده و ما این را در تنگه هرمز و باب‌المندب می‌بینیم. دشمنان ما می‌خواهند فضای دریایی اسرائیل در مدیترانه، بنادر و تردد دریایی‌مان را تهدید کنند، اما ما اجازه این کار را نخواهیم…</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24926" target="_blank">📅 07:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آکسیوس: آمریکا
۱۲ فروند بمب‌افکن بی-۱
مستقر در این پایگاه را طی آخر هفته به پایگاه‌های اصلی خود در خاک آمریکا منتقل کرد. پنتاگون با تأیید این جابه‌جایی اعلام کرد که تمام بمب‌افکن‌های ویرفورد به آمریکا بازگشته‌اند، اما همچنان برای انجام حملات دوربرد آماده هستند و بمب‌افکن‌های بی-۱، بی-۲ و بی-۵۲ می‌توانند از خاک آمریکا عملیات انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24925" target="_blank">📅 07:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiLosio-OT-ec_plcNLLoKSlFpuzRT-krWQh3A80kb8-kQ3rl1b5NlYw2cGJBaqh8OAx4ysIFQ4kUnhqdCWHBZRqu0LjlaOwPDq2RO_WfSTWHC6ej4w461VzsBizoy-DoePAT9BGltPeV2jB9sq9fY7BXVtmmg48Z20gNnfe9yIHBQpClX0kofVluyOcHt-vaMvDY2tdvg0oaqulSXFK41J5ZCimINV4oGvdgy2JSpFNVM7OL3dt-PaxVW3TZRoRiPyGmvIdNyuYwdWHd8d7TNxyAjKl9TfoQVYf0R9Z4LICd-LPSSpR9HzW-U7lV9_SPPnjONhdv1nbwGDYqT8kKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب تتلو
:
امروز دادستان و رئیس کل دادگستری با امیر تتلو صحبت کردند و به گفته او، این گفت‌وگو مثبت بوده است. او همچنین به بخشی از آهنگ «من و خدا» اشاره کرد که تتلو در آن می‌گوید «همین روزا دیگه باید بیاید استقبالم» و ابراز امیدواری کرد فردا خبرهای خوبی درباره وضعیت او منتشر شود و ممکنه که آزاد شود
@RapFA
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/24924" target="_blank">📅 00:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از یک مقام ارشد آمریکایی:
آمریکا از طرحی مرتبط با ایران برای
حمله به بمب‌افکن‌های آمریکایی و کشتن نیروهای نظامی در پایگاه ویرفورد بریتانیا
اطلاع داشت. به گفته این مقام، سپاه پاسداران
شهروندان بریتانیایی را برای اجرای یک طرح چندمرحله‌ای
استخدام کرده بود که هدف آن حمله به هواپیماهای آمریکایی و نیروهای مستقر در پایگاه بود. در این طرح قرار بود با ایجاد یک
انحراف در نزدیکی پایگاه
، زمینه حمله فراهم شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24923" target="_blank">📅 23:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4ILqyi3qPSOmp1nowj3NblkdHCuy37NUg8nQBqd4Vdgfd7QJ-ESx6erQIOVELr2tzDK5Pzku1fROgj8UQC-HWzDBsHpxdI--28qcPFUJ-GZRlL7COe-ujlvuCz-2BbRdO7QdJueuKveMwwAGKEOmt64YSiJXmOvxMdCC2mvItYHEQOoQZTg3piirNrvWJ0986I1BUz8KmW6c_gRncDHg6eAys6IzNyZ03YkDzLu2f3Y5c38mb2-vlkYnsBKsf0s_ZgTN49EcST-jqK24_SBamoiQgoRZb3I02SSUx-qC0wW-PkBiiigWV3q3rpW7A1dz3feoEf0caj-ElHYd5SVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس ختم خواهر عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/24922" target="_blank">📅 23:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/24921" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmBupiVMsMVK8N_ImyYkREuzbPNxAYIUu5mnFOwZUExZWfdRmNEL8Km8IDhC8uvGlOd8c9g4E6YiOOUQBRZ8WJTE9dquVR7IPmNKFC9wTs4WBTJiT2RH2hwkgzfuc2d-H8bpZV5k5aYPyHgD5bhsb3W5aaFhVc2zBiD4HdJjROQK1EHeSOQFID_jOeUhBr0ywqRSryPwgmbK2vK6ZMGG2T9bgjom6JfO0SsHMjB9iVhFCx4xZaUjaGQATjLOJNh3S7ZlJHoQAAWNFg1mMQuPIqKoz5y5tfCID2Cv9G_vtsBsHay0_r6X2D6Wyo0R8aaWAvEftGtMdlzQtrZxwwIRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ۱۲ فروند بمب‌افکن راهبردی B-1B Lancer نیروی هوایی آمریکا، پایگاه هوایی سلطنتی فیرفورد در انگلستان را ترک کرده‌اند تا به خاک اصلی ایالات متحده بازگردند. @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/24919" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تصاویر خبرنگاران از پرواز چندین بمب‌افکن راهبردی بی-۱ لنسر آمریکا از پایگاه نیروی هوایی سلطنتی فیرفورد در بریتانیا منتشر شده است. @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24918" target="_blank">📅 22:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا : حمله به یک کشتی در تنگه باب‌المندب
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24917" target="_blank">📅 22:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۵ درباره خلبان تروریست: مادرش اصالتی سوری دارد، و در حساب کاربری او ویدیوهایی از هواپیماهای اسرائیلی منتشر شده است
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/24916" target="_blank">📅 22:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تنگه صدای منصوره زن موشلی میاد @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/24915" target="_blank">📅 22:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24914" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24913" target="_blank">📅 22:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اصغر فرهادی، کارگردان سینما: اصلا چه کسی از آمریکایی‌ها خواسته بیان مارو نجات بدن؟
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24912" target="_blank">📅 21:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24911" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترابری بسیار سنگین از ۳۰ ساعت پیش تا همین چند دقیقه پیش که بازهم افزایش داشته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/24910" target="_blank">📅 21:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تنگه صدای منصوره زن موشلی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24909" target="_blank">📅 21:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f5cb10969.mp4?token=elWO_blZB5QsAVU8zoavmfDM9ywEMYIVWbmLG4HZKTirkx5BDzvb9fr-mMXoWj-26gAuSM9YTdIaIQQUAUNGifUwSuDqBgvQLRGiRA1QDpEi2_C16cCJ7mSZkAhyz4fkWfmM7QKut-pT9yoMWK_EF4mCW6d8HTXnWUOuqWM3bFpNZEjdW8RhxpONxvJn2-orXlTdMz4It4WVy6DPPQf6qhUskFJVRFeIJxeMNowDtg-hKhrVst_abdfkjj3JqqtnAd_5Veo0WX7IJU3Hrh5gUMnMbusIkwT9L6BPnQyn0ekUfJncw-VwAf3SFKoLTIjv7wRqpUVGLA6c4AYhLojd2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f5cb10969.mp4?token=elWO_blZB5QsAVU8zoavmfDM9ywEMYIVWbmLG4HZKTirkx5BDzvb9fr-mMXoWj-26gAuSM9YTdIaIQQUAUNGifUwSuDqBgvQLRGiRA1QDpEi2_C16cCJ7mSZkAhyz4fkWfmM7QKut-pT9yoMWK_EF4mCW6d8HTXnWUOuqWM3bFpNZEjdW8RhxpONxvJn2-orXlTdMz4It4WVy6DPPQf6qhUskFJVRFeIJxeMNowDtg-hKhrVst_abdfkjj3JqqtnAd_5Veo0WX7IJU3Hrh5gUMnMbusIkwT9L6BPnQyn0ekUfJncw-VwAf3SFKoLTIjv7wRqpUVGLA6c4AYhLojd2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا:
رئیس‌جمهور آمریکا کاملاً از خطری که حمله به ایران می‌توانست برای جریان انرژی خارج‌شده از منطقه خلیج فارس ایجاد کند، آگاه بود. او گفت: «دنیا نمی‌تواند یک ایران مجهز به سلاح هسته‌ای را تحمل کند و من قرار نیست اجازه بدهم چنین اتفاقی بیفتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24908" target="_blank">📅 20:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa-AzXrjFv4JqQspv02HIsX07GiKPHoB7jmEnM0sjpNv1DnmR7ueDqGJ7OsXGg2Vpit_bHTYzUcdFSwNF6CBzBR0VqbGH6NqKPMCWjyrBvap74_sybUZj-GAqYljZxxZTuZlkMzwj2njx_2OXisI3m8AKRzVhVX5J4vXWX0ZPwLQwZqofrmmHrVujUsnwyQuON47OJfMiAA-ZifdK0KcBwlHETWmVF4kT9o3WJhX1t6MOCT2TIeVSjaCX1zdlIw7Kq_MnO9ReHbQMesLCTNUyCJBxG5OlgeOAInW2ODp9AC8DI1Uot3UJf2FM4jnOcX46kMOMhy8Z-HgtYAC6EX0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پی-۸ پوسایدون ، ۶ فروند سوخترسان و یک فروند ترابری سنگین سی۱۷ در‌ محدوده خلیج فارس در حال انجام مأموریت خود می‌باشند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24907" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر نفت استعفا داد
طباطبایی معاون دفتر پزشکیان : با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24906" target="_blank">📅 20:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شبکه ۱۲ اسرائیل:
خلبان عمانی در جریان بازجویی گفته است که قصد داشته
هواپیما را به فرودگاه بن‌گوریون بکوبد
. به همین دلیل، او تنها زمانی به خلبان دیگر حمله کرده که هواپیما بر فراز اردن و در نزدیکی اسرائیل بوده است. او قصد داشته هواپیما را به‌طور عادی برای فرود آماده کند و در آخرین ثانیه‌ها، زمانی که دیگر امکان رهگیری وجود نداشته باشد، هواپیما را به ترمینال فرودگاه بکوبد. این نقشه تنها به لطف تصمیم سرنوشت‌ساز خلبان هندیِ مجروح برای باز کردن درِ کابین به هر قیمتی خنثی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24905" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">واللا:
حدود
۳۰۰۰ نیروی آمریکایی
هم‌اکنون در نقاط مختلف اسرائیل مستقر هستند و در حوزه‌های
پدافند هوایی، هوانوردی، لجستیک و فرماندهی
فعالیت می‌کنند. آمریکا طی هفته‌های آینده
نیروها و هواپیماهای نظامی بیشتری
به منطقه اعزام خواهد کرد. همزمان، اسرائیل برای احتمال تشدید دوباره درگیری با جمهوری اسلامی آماده می‌شود و هماهنگی میان ارتش اسرائیل و
سنتکام
برای مقابله با حملات موشکی احتمالی ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24904" target="_blank">📅 20:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb6bbf8c6.mp4?token=Y7MBxKj3hlulEnSUStvOCcJAWDaG5qftVkRicfjP9Qa4ubPcefa3YRbrikzTOt4cW9xFJTr_aCnvj5h2tDxG1uCYeE6mmNV_Rx3xT43h6t1V1tRhCafCrCHHGPDzT6qZqU6HrlSXGYapcAKfzdd6ORw9OVD01pVkM0GbcXEiViApFj_wTcDRUgnU7Y2igh2UYQyzL-OHuIoOmf3P87Otf8rZ-Ae2XlxBPa_-9-OanXJtFgAskvD5cCOBltfJoxgzKr_vCMrXsKiFsh1HeXbOdhC_Aqk8I_IPRlhEGZWbqF1SHTy3gJY58TCIR6hAvGrereH3W5C9N4IXhQesrWt0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb6bbf8c6.mp4?token=Y7MBxKj3hlulEnSUStvOCcJAWDaG5qftVkRicfjP9Qa4ubPcefa3YRbrikzTOt4cW9xFJTr_aCnvj5h2tDxG1uCYeE6mmNV_Rx3xT43h6t1V1tRhCafCrCHHGPDzT6qZqU6HrlSXGYapcAKfzdd6ORw9OVD01pVkM0GbcXEiViApFj_wTcDRUgnU7Y2igh2UYQyzL-OHuIoOmf3P87Otf8rZ-Ae2XlxBPa_-9-OanXJtFgAskvD5cCOBltfJoxgzKr_vCMrXsKiFsh1HeXbOdhC_Aqk8I_IPRlhEGZWbqF1SHTy3gJY58TCIR6hAvGrereH3W5C9N4IXhQesrWt0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی بی و مجید ، فرق دیروز و امروز
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24903" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24902">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ در تروث‌ :
نظرسنجی‌ها
همیشه حمایت از جنبش ماگا را کمتر از واقعیت نشان داده‌اند.
آنها تلاش می‌کنند رأی‌دهندگان را سرکوب کنند، اما من امسال هر ۷ ایالت نوسانی، آرای مردمی، ۸۶ درصد شهرستان‌ها و ۹۹ درصد انتخابات مقدماتی را بردم.
من روی برگه رأی هستم!
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24902" target="_blank">📅 19:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی وزارت خارجه:
تهران پیشنهاد مذاکره هسته‌ای واشینگتن را رد کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24901" target="_blank">📅 19:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24900" target="_blank">📅 19:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSVy1D2uW8YnQHCqdivFGYrYR8RIM5mDWsE1Odc4zlnSln6QdvfUHmwy-5SA7mA5f5VnCxvMW22qLMBtPW58qiH9DEiMcZSGyE6iyNDwBkZt4i5gG8rmax4vYD4ZPw6KhduEQsMi87QSAx-LJ8GeIxAVgTQrO9qnTEPp1sCY0kt4EJ6ELZ_YhKOyeE7GGd_bK2qyEe9JQk4pmPnIQxjLPTOfsPX0r9x4zNDpwLNDwY24JTjRcOwzxKiC80ixhTl4GnMvcGuuuH2PP7hGfHhSRNC6b3qKOEArB4sJYiuUwHoZ4WcIV7F4R_MzspmqcE1jQoSAV-21jg25o0sN7AA2Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrmvQnw8srlOJfsgzd3ygYtPtaHCYRSQbRjvuJto2SSgwe8CipGfaOFFcd8aUWZsvfmE8MP0vq0u2tOBSdMhYes2ROHZLamnDTE97GWTYrpyPQwfAREBaw0vL3M1FZClJKLuFHmum_jzG7XSTE9iOT77czL6yxjrCrJKcSWbWGrKu5xw37OwnhVlrk-RGfwuvISfW1HCNWUI-N5hXJJdLxK_9tYzs0SaVhDTEYCJVzsGGIQUB_WjhFTJlmXxjlsciUtn4PJfoYpv053gfW0UO_bn2thEsUtXuNER1Lmu73b2biaIR2os_irl-HVvtY_tw7E2utkDBxOrbuhr16vhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ag2bawDqmrHNjXigrn3pOvxpR0pldAVS5x_k6oIKDaDeMKqkT9MkLhu4e-fwR5509D8i6gWcSpq4pLCDw-UA2a1NRWyAbWUW5IEYeVatM1hdMx78sAm2rum2rY8AJ9XTggjjmVIephf9aCZb7VV82uoKKhqLVjXsYQDJDZ9ftDpRAo3-luc5lqsH3bmC3qoYVq6QpAMWAq_TTKXas9htShSfZBaKCsYYMLDTfBiHBluGPUKv6d5J1RQsz5pYrYc6WJJ0MERWybUuogB5fxwIU5-dunFQcNrS6eXNtNMC2BMtZvuWCzfLwg62yFQ_63tiL56C8UteyuEicQNRe_78UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGCRgqFUR9ABMk-UcO468wvxmFX5kLGG0kt0sP1filL2Jdvf88QkJv4xj-UsqVRID8fwndGbm1c-jh89O_ZaqtI7eSCyjWwaljreTRYkBs3dpI1HyYSu-Ok3Fym6vh9ZE_TT_49mOUTwRnQaIFFxio_DumDZx90OKEzjtIhssiI2pFGakb2kg75POqlQ2zzP06aoxocRlSgjiXnIHsfDtrfAL8mxREKan7oX5ZvKS91R-AZnkt9jpoEN7iYzM8gU_jYziwgs4q7DP-0GNMjZMK4VpZluNhBEu4_UhWjyJbW9zCSV7earaafI_ohxXX6WjDHKY2KbJe5nEvp64WecJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تخریب زندان رجایی شهر در کرج
@WarRoom
یاشار : حبس اینجا رو هم کشیدم … جایی نبوده نرفته باشم
😂
🙌🏾
ولی اوین بهتر بود</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24896" target="_blank">📅 19:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آکسیوس: نیروهای دولت یمن با حمایت عربستان ضدحمله علیه حوثی‌ها را آغاز کرده‌اند؛ هدف این عملیات بازپس‌گیری مناطق تحت کنترل حوثی‌ها، از جمله کنترل مجدد باب‌المندب و در نهایت بازپس‌گیری صنعا، پایتخت یمن، است ، آمریکا فعلاً در عملیات مشارکت مستقیم ندارد، اما در زمینه اطلاعات و شناسایی اهداف به عربستان کمک می‌کند و در صورت شکست عملیات، ممکن است وارد اقدام نظامی شود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24895" target="_blank">📅 19:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
ایران فعلاً با
درخواست حماس برای ازسرگیری کمک مالی
موافقت نکرده است. یک هیئت ارشد حماس اوایل شهریور به تهران سفر کرد و خواستار ازسرگیری کمک‌های مالی متوقف‌شده ایران شد، اما تهران هنوز با این درخواست موافقت نکرده است. به گفته یک منبع فلسطینی،
نارضایتی ایران از عملکرد حماس و ناتوانی این گروه در تغییر وضعیت امنیتی کرانه باختری
از دلایل این تصمیم است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24894" target="_blank">📅 19:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4841ab1e.mp4?token=k0GTb25leeG-3ZHIJ8DZvUqV83tXxYGiDkdp9GUM7pH7HB1iYzeSdQU28ivJd4oJ-x0xiq__bvehaLqOBameXPZpXSgARwJmDnmfqJhqphKDN0ix2iXxHYqeTR9QWPHJGAP8zxIYFAOoThotar4FVnx7SumLCte-spOkusWtHk2SRT7UH2sCr2Ar6zjhOa7tb64AcUPqQEM3B24c-VAMyy2nU0g7I65qRH3INutCyY9QJelS_Gk4jG8ea0AP0gySvNGPUnWu_TZwhuE9tYQH8jny-tRWlfctkUJq56f69Dk5r5h7RZzJtukn6WF3cfVYUK9RLAcg64i60J5REy4ZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4841ab1e.mp4?token=k0GTb25leeG-3ZHIJ8DZvUqV83tXxYGiDkdp9GUM7pH7HB1iYzeSdQU28ivJd4oJ-x0xiq__bvehaLqOBameXPZpXSgARwJmDnmfqJhqphKDN0ix2iXxHYqeTR9QWPHJGAP8zxIYFAOoThotar4FVnx7SumLCte-spOkusWtHk2SRT7UH2sCr2Ar6zjhOa7tb64AcUPqQEM3B24c-VAMyy2nU0g7I65qRH3INutCyY9QJelS_Gk4jG8ea0AP0gySvNGPUnWu_TZwhuE9tYQH8jny-tRWlfctkUJq56f69Dk5r5h7RZzJtukn6WF3cfVYUK9RLAcg64i60J5REy4ZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، نخست‌وزیر اسرائیل:
حوزه دریایی عملاً به یک میدان نبرد بین‌المللی تبدیل شده و ما این را در
تنگه هرمز و باب‌المندب
می‌بینیم. دشمنان ما می‌خواهند فضای دریایی اسرائیل در مدیترانه، بنادر و تردد دریایی‌مان را تهدید کنند، اما ما اجازه این کار را نخواهیم داد.
ششمین زیردریایی به اسرائیل رسیده
و ما به شناورها و توانمندی‌های بیشتری نیاز داریم. من می‌خواهم اسرائیل
هم روی سطح آب و هم زیر آب به یکی از کشورهای پیشرو جهان در این حوزه تبدیل شود.
ما از اسرائیل از دریا نیز محافظت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24893" target="_blank">📅 18:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی:
فرماندهی مرکزی آمریکا با انجام حملات مستقیم علیه حوثی‌ها در یمن مخالفت کرده است، زیرا معتقد است ورود نظامی به یمن می‌تواند
تمرکز و توان عملیاتی ارتش آمریکا را از جنگ و اقدامات علیه ایران منحرف کند
.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24892" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتاق جنگ با یاشار : چرا آمریکا و اسرائیل مجتبی خامنه‌ای را زنده اعلام می‌کنند؟
در جنگ اطلاعاتی، تأکید آمریکا و اسرائیل بر زنده‌بودن مجتبی لزوماً به معنی تأیید قدرت او نیست؛ ممکن است هدف، شناسایی زنجیره واقعی فرماندهی باشد: آیا او واقعاً دستور می‌دهد و چه کسانی با او در ارتباط‌اند؟ مهم‌تر اینکه
اگر خودِ سران جمهوری اسلامی هم نتوانند با اطمینان بدانند او زنده است یا مرده، این ابهام می‌تواند در رأس قدرت شکاف، بی‌اعتمادی و درگیری بر سر جانشینی و صدور فرمان با حتی یک  ارتباط ساده ایجاد کند.
هرکس می‌تواند مدعی بخشی شود و درگیری جدی جناح ها در ساختار شکل بگیرد. حفظ ابهام، هم برای رصد حکومت و هم در جنگ روانی می‌تواند ارزشمند باشد.همچنین برای خود رژیم تا مدتی کوتاه مؤثر است و بعد اثر خود را از دست میدهد و مضر هم خواهد بود. تاریخ نمونه‌های مشابه دارد؛
ملا عمر
سال‌ها پس از مرگش توسط طالبان زنده نگه داشته شد و
مسعود رجوی
نیز سال‌هاست با غیبت کامل و روایت‌های متناقض درباره سرنوشتش، به یک معمای اطلاعاتی تبدیل به مضحکه شده است. بنابراین الان شاید سؤال اصلی این نباشد که مجتبی زنده است یا مرده؛ بلکه این باشد که
نام او به ابزار چه کسانی برای اداره قدرت در پشت پرده تبدیل شده است؟
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24891" target="_blank">📅 18:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2269dc9c1.mp4?token=ALKv0pBlwVdGakESQDVzLwCj5TBgiVNfCxiKG-YAbtYquZZpsrghKrJUBlDo940Eis343IYtsd6xyAjnrW1EiMtz6cmlu0Z__l-EuVIu0mco8CdkiPQZMmjsGxrlwtEvAdIJPSAkDSYijkkhBzMoYhDpe241Y_qKPX-VRaErty8nUDyXi3yQVkXMABJCTmytx36jY07GGx3Y5dVE3cGnxN2AUFLvZuaW7ji6_E80zLMvJ_OoBL8SBcLgq5CmvA1dysefz0Eql4n5e2fsGSnIQYfIW_iY7Bv4khhdvyVFmSO4wLFr15O5-PInlrKytNZp5XCJ7k_Qg1qfmPn1xcRTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2269dc9c1.mp4?token=ALKv0pBlwVdGakESQDVzLwCj5TBgiVNfCxiKG-YAbtYquZZpsrghKrJUBlDo940Eis343IYtsd6xyAjnrW1EiMtz6cmlu0Z__l-EuVIu0mco8CdkiPQZMmjsGxrlwtEvAdIJPSAkDSYijkkhBzMoYhDpe241Y_qKPX-VRaErty8nUDyXi3yQVkXMABJCTmytx36jY07GGx3Y5dVE3cGnxN2AUFLvZuaW7ji6_E80zLMvJ_OoBL8SBcLgq5CmvA1dysefz0Eql4n5e2fsGSnIQYfIW_iY7Bv4khhdvyVFmSO4wLFr15O5-PInlrKytNZp5XCJ7k_Qg1qfmPn1xcRTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر «یو‌اس‌اس جورج اچ. دبلیو. بوش» (CVN-77) برای یک سفر رسمی از
۱۲ تا ۱۷ مهر
وارد بندر آب‌عمیق پوکت تایلند شد. این ناو و بیش از
۵ هزار خدمه
پس از
۱۸۶ روز استقرار مداوم
در منطقه، برای استراحت و تأمین مجدد تدارکات در این بندر توقف کرده‌اند. این ناو بیش از پنج ماه در محدوده مسئولیت فرماندهی مرکزی آمریکا (سنتکام) فعالیت داشته و در جریان این مأموریت،
عملیات نظامی علیه ایران انجام داده است
. این نخستین توقف بندری ناو از زمان آغاز عملیات آن در خاورمیانه محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24890" target="_blank">📅 17:19 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
