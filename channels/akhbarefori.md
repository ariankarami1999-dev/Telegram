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
<img src="https://cdn4.telesco.pe/file/j_MuSm4VCHnWYJY9oh6ywNqTDEVTm1ZuWZRuM19vddntOUWwPSv48URmqGAMyA7xCzrHIdaIPx_WtKqLxKn8kHnZWg1mthim-TxL-Ipwn4zBjTzsDFp1ZI3OLyW9b8rtuIdJGQHBQMqFQRehbOs9amQu1slc6rWZyUyIwJEzYbRCHPHZsknk_hcSIXlBNqnDV_XD0KlhTWhsGs6adA6V7GuPVfTkZvGDs8xQwNeLG29jJHVxxD5ZHtTByHGvNkn85dmVKcW5UXv3NfiOJe1IwCzVrPhRCbWqZPi7hhY-lPki1fHzn5V-xcy6N-YEmDYaU3Z0kU3IKTz1LXCMG2OSjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 03:11:27</div>
<hr>

<div class="tg-post" id="msg-686441">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
انفجارهای پی در پی در بحرین
🔹
منابع عربی از حداقل ۴ انفجار در پی حملات ایران در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/686441" target="_blank">📅 03:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی بامداد چهارشنبه گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گسترده ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/akhbarefori/686439" target="_blank">📅 02:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c94f0226.mp4?token=kFyqtiCBT2mvX8HMALopg6smj_fv8Cv9Txk-qEcs3eJTyiKG7kLXFr5svqVV5gsvF_7IX-2M4qmq_cNF-4CssvJzIWFWgWe8yrqELvkCvNLgPpmNdBl9nIWWjMaDtJAveuFB3SLcVac32S5nlfDyIfw4FY8xZGEZfxX4ojReXBL4ue_yFh7brE9hhD3AFbdD7HmT-6cPwzrSnpkYrgAlixHKoSYPPNaau1IQRua0Sx4qa_vuZnymeWYkUKSeAxMzSDsVyGYYODA6Yhsw8kb7TiIWql3DrRBL1DeUTXJ25qrjISPUVOBp1_SnNeRuxSHdjRfUcPoECwtugCAW1wv61w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c94f0226.mp4?token=kFyqtiCBT2mvX8HMALopg6smj_fv8Cv9Txk-qEcs3eJTyiKG7kLXFr5svqVV5gsvF_7IX-2M4qmq_cNF-4CssvJzIWFWgWe8yrqELvkCvNLgPpmNdBl9nIWWjMaDtJAveuFB3SLcVac32S5nlfDyIfw4FY8xZGEZfxX4ojReXBL4ue_yFh7brE9hhD3AFbdD7HmT-6cPwzrSnpkYrgAlixHKoSYPPNaau1IQRua0Sx4qa_vuZnymeWYkUKSeAxMzSDsVyGYYODA6Yhsw8kb7TiIWql3DrRBL1DeUTXJ25qrjISPUVOBp1_SnNeRuxSHdjRfUcPoECwtugCAW1wv61w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویر از قطعات موشک‌های اصابت‌کرده به مراسم عروسی در کوهستک سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/686438" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eClxYWejiSERhk7TaUeEaH3dvXa6CA4xVIJO-gqroXeD2UFG6vvWhJCIYi3O9UFr9JyZpEHVbExBRCykSilYgYCFlZK81cGtJj3Up9F63ogTcsdLyng6Wt9yfVEDBSUUuIkyCSp632NYQzu9heF-Dyp0rWcCXZk6qkvQ9gQkK8cNKXj3KRPoVz0txz0Z33yAQ9hkP3mGom5HFwQQ0UN4e4iiKbc8EEttzLZzijyFvMCP3UEEp2hvcbIB1j3ym8BZNv63bDC0JaKOXjbOYfNgxDP4qDY7_ffR1Pvo2e9TlzjzTHc5MVrV0QCzrMkW1TMtF65idvXmzHHzmGdGpr7jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4220f97c5.mp4?token=AJx2j-DLMfHj50uit_Gex0kqSfxTlgsnhtcaoi6_wkqaHBqV5WrEndRdMpwfVGOy82Zjvf-aJU_6k-IecEVaJy-VQ_UlaYWhgF8NETW-ABABlFQo-QpRxVk_iNKAOtszsuhCmSZ8GP3i-Bb00TH07UH_2akvSC7YN0Wr0bKBfQgU1n3PfcZZTPDXWuBDJ4ow5zBTR_QGicJxDa03eoT4JRVagwXEpD4YA2SRTH4br-tKutw-mWdZu4z7vj3kayCWz0q44mW-wFhEzR9FqjwhJyt1Lbxg0AMgwJfabx4LHCrWsTmiyAR6Pmd63hdC7JDcYtREFjlgDc5eO59zQ447nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4220f97c5.mp4?token=AJx2j-DLMfHj50uit_Gex0kqSfxTlgsnhtcaoi6_wkqaHBqV5WrEndRdMpwfVGOy82Zjvf-aJU_6k-IecEVaJy-VQ_UlaYWhgF8NETW-ABABlFQo-QpRxVk_iNKAOtszsuhCmSZ8GP3i-Bb00TH07UH_2akvSC7YN0Wr0bKBfQgU1n3PfcZZTPDXWuBDJ4ow5zBTR_QGicJxDa03eoT4JRVagwXEpD4YA2SRTH4br-tKutw-mWdZu4z7vj3kayCWz0q44mW-wFhEzR9FqjwhJyt1Lbxg0AMgwJfabx4LHCrWsTmiyAR6Pmd63hdC7JDcYtREFjlgDc5eO59zQ447nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در کنسولگری آمریکا در أربیل
🔹
رسانه عراقی با اشاره به حمله پهپادی به اهداف آمریکایی در اربیل، گزارش داد که انفجار بزرگی کنسولگری آمریکا در اربیل را لرزاند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/686436" target="_blank">📅 02:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: ایران محیط دفاعی و امنیتی خود را تعریف می‌کند؛ هر نقطه مبدأ تهدید باشد، مورد برخورد قرار می‌گیرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/akhbarefori/686435" target="_blank">📅 02:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3618e31c3.mp4?token=qfYVE9CrtT6QaO-uEWbJW-4WwMDPTRFVw9hYynYouGLxMSjXhQUoqqfLAH-89xTQ_3g3kiaJ66YYfUrDWdZA1nuXtllHC70Af8gtMqM39H9hjCGfNL0ic0fJFcCmySXAcWiLrIOGnqW8no1c4F-9-wExBGXMclLNelkfffdz9ypPdb_HR4tlWn3gXF-aCpej-XHcRkI-iB2CH1OIraO-8C24zwRBoFpAHCK8rRAkrLwqKPXxBBlJipM89eQ_jdzMcmewCs9ollYjW0PfxMGhLQP2Ad-C_r_J6PxdRTsiyzEDKzjjf7fVcRYoelWnPpl2ys_6uzTdxOX3VfGS3iq5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3618e31c3.mp4?token=qfYVE9CrtT6QaO-uEWbJW-4WwMDPTRFVw9hYynYouGLxMSjXhQUoqqfLAH-89xTQ_3g3kiaJ66YYfUrDWdZA1nuXtllHC70Af8gtMqM39H9hjCGfNL0ic0fJFcCmySXAcWiLrIOGnqW8no1c4F-9-wExBGXMclLNelkfffdz9ypPdb_HR4tlWn3gXF-aCpej-XHcRkI-iB2CH1OIraO-8C24zwRBoFpAHCK8rRAkrLwqKPXxBBlJipM89eQ_jdzMcmewCs9ollYjW0PfxMGhLQP2Ad-C_r_J6PxdRTsiyzEDKzjjf7fVcRYoelWnPpl2ys_6uzTdxOX3VfGS3iq5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: پهپادهای دشمن با اینکه از چهار روش مخفی کاری استفاده می‌کنند اما همچنان توسط سامانه یکپارچه پدافندی شکار می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/686434" target="_blank">📅 02:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کویت
🔹
رسانه‌های خبری از فعال شدن پدافند هوایی کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/686433" target="_blank">📅 02:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf136ebcb.mp4?token=oKHmSqHef1Qy79x3bwmnghcletBkkroR23D8_QI_q5z1LepQcf2OMya0D3GZeNhXxif7xzsAlYkJyL_Ei0FnP8LRntsW1gg0lSudUxYXK2q-fq_zvtqqvxoaWwEh6zoxeUWzZ-GenxDlkY2FRokVI_b6cN8d9l29lhXKpgZuuMS70XUwnugA-gPCzyr3LKRv_UzpThA6GnE2yS3EiJBVVfytTzXa_X4QABBkchh8e8Z-D2o4kwGxzY2T-bCqQ1syTKTbvgC0Bsf3u_rN96aD0WPfR0kRgwvJJtU5TnhnJ4eqTlX32uYsjUAmlZfaIFIB4qCelAZdjIukSQ_jh9cxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf136ebcb.mp4?token=oKHmSqHef1Qy79x3bwmnghcletBkkroR23D8_QI_q5z1LepQcf2OMya0D3GZeNhXxif7xzsAlYkJyL_Ei0FnP8LRntsW1gg0lSudUxYXK2q-fq_zvtqqvxoaWwEh6zoxeUWzZ-GenxDlkY2FRokVI_b6cN8d9l29lhXKpgZuuMS70XUwnugA-gPCzyr3LKRv_UzpThA6GnE2yS3EiJBVVfytTzXa_X4QABBkchh8e8Z-D2o4kwGxzY2T-bCqQ1syTKTbvgC0Bsf3u_rN96aD0WPfR0kRgwvJJtU5TnhnJ4eqTlX32uYsjUAmlZfaIFIB4qCelAZdjIukSQ_jh9cxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز پهپادهای انتحاری بر فراز اربیل
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/686432" target="_blank">📅 02:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی بامداد چهارشنبه گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گسترده ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/686431" target="_blank">📅 02:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بحرین اطلاعیه هشدار صادر کرد
🔹
همزمان با به صدا درآمدن آژیرهای هشدار در منانه، وزارت کشور بحرین نیز با صدور هشداری در تلفن‌های همراه، از مردم این کشور خواست به مکان‌های امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/686430" target="_blank">📅 02:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36224e669.mp4?token=Zh83phRBxx8Pih7nF90x6fPdryd0cQJk4HzXBEJREKmR7fZbVnwrHMMdxDxYQqilFxTDggFeBcX6eUZ8TyVxk0KPmvyIBdyU4TmlOC4qscl5pKy4DGuFRrRmazzjXfH5bfhbPGpPMUwosRZQAqdny5f3tlrK4GoCWa0bZzuHBlHFOizrc1hQygDQ9IFCKn9doi9rYMiXfD7ySvrGZ3x84YC1ELUSbkXue8ZVb85AgoEbj_K4tyDFRKrEN7TRd_XWwhCpBoG5ovbNNqTwdFRM9AMfY1XHHi-8cShxOdD1DTMadjU8x0FobXpNy-rIvi_xZfuHZqOU6zGJ0vi1_9MI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36224e669.mp4?token=Zh83phRBxx8Pih7nF90x6fPdryd0cQJk4HzXBEJREKmR7fZbVnwrHMMdxDxYQqilFxTDggFeBcX6eUZ8TyVxk0KPmvyIBdyU4TmlOC4qscl5pKy4DGuFRrRmazzjXfH5bfhbPGpPMUwosRZQAqdny5f3tlrK4GoCWa0bZzuHBlHFOizrc1hQygDQ9IFCKn9doi9rYMiXfD7ySvrGZ3x84YC1ELUSbkXue8ZVb85AgoEbj_K4tyDFRKrEN7TRd_XWwhCpBoG5ovbNNqTwdFRM9AMfY1XHHi-8cShxOdD1DTMadjU8x0FobXpNy-rIvi_xZfuHZqOU6zGJ0vi1_9MI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو هیئت رییسه مجلس: دیگر زمان مقابله چشم در مقابل چشم نیست، از این پس به در مقابل چشم، به سر حمله خواهیم کرد/ گزارش داده شده است که از امارات به ایران حمله شده است و اگر گزارش تایید شود، می‌دانند چه اقدامی انجام خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/686429" target="_blank">📅 02:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686427">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵/ حمله سنگین موشک‌های بالستیک به آشیانه‌ هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ در پایگاه پرنس حسن/ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ يَا أُولِي الْأَلْبَابِ
🔹
مردم شریف و انقلابی اردن؛
یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن،
اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/686427" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686426">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی به کویت
🔹
ارتش کویت در بیانیه ای اعلام کرد که این کشور مورد حمله موشکی و پهپادی قرار گرفته است.
🔹
در این بیانیه آمده است که پدافند هوایی این کشور در حال مقابله با این حملات است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/akhbarefori/686426" target="_blank">📅 02:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686425">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
معاون سیاسی سپاه خطاب به کشورهای منطقه: یا آمریکا را بیرون کنید یا پاسخ کوبنده بگیرید
سردار جوانی خطاب به کشورهای عربی:
🔹
بهتر است آمریکایی‌ها را از کشورهای خود بیرون کنید و پایگاه‌ها را پس بگیرید. در غیر اینصورت، نیروهای مسلح ایران ثابت کرده‌اند از هر نقطه‌ای در کویت، بحرین، اردن یا هر کشوری که به ایران تهاجم شود، با پاسخ‌های قاطع و کوبنده مواجه خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/686425" target="_blank">📅 02:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686424">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی پایان حملاتش علیه ایران شد
🔹
ستاد فرماندهی مرکزی آمریکا ادعا کرد: ما با موفقیت موجی از حملات علیه اهداف نظامی ایران را به پایان رساندیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/686424" target="_blank">📅 02:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ارتش: در بیست و نهمین مرحله از عملیات صاعقه، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین را هدف حملات پرحجم پهپادهای انهدامی قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/686423" target="_blank">📅 01:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
وقوع انفجار در کنسولگری آمریکا در أربیل
🔹
رسانه عراقی با اشاره به حمله پهپادی به اهداف آمریکایی در اربیل، گزارش داد که انفجار بزرگی کنسولگری آمریکا در اربیل را لرزاند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/686422" target="_blank">📅 01:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رسانه‌های عربی از اصابت موشک به پایگاه هوایی علی السالم در کویت خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/686421" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6ae37b97.mp4?token=OXaaoiSSyUr0KKGkOBJRQENN-zJVRbuAEE90oA2qd3i9hbJMRkhEWZdTmwobZ_iphVLYQ-i6lNFvhaxIjbUWvjuXXgXny9A33VPpF6MMbDmjZX_dhiAtJkt6HahQq3U9sM_MZorixriJdWi2JQyHrVyFog0ro54xP-mJiqAgwvLP1r70qzFss3qu83Z94HMuQNLCGaDg1eLLTy2jWIP_2MXMiBQj5cz9bZFQoOOpx8opNZBxM_TUer6WY1a5WQtQc2KntnLjz_CDZvhVmnZhjjIDjyAcE1uZ98M0a4c49_e4vg_PkKWIADVTr3qPI1fe8oFw0Yqgr9JHPn5l8WI__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6ae37b97.mp4?token=OXaaoiSSyUr0KKGkOBJRQENN-zJVRbuAEE90oA2qd3i9hbJMRkhEWZdTmwobZ_iphVLYQ-i6lNFvhaxIjbUWvjuXXgXny9A33VPpF6MMbDmjZX_dhiAtJkt6HahQq3U9sM_MZorixriJdWi2JQyHrVyFog0ro54xP-mJiqAgwvLP1r70qzFss3qu83Z94HMuQNLCGaDg1eLLTy2jWIP_2MXMiBQj5cz9bZFQoOOpx8opNZBxM_TUer6WY1a5WQtQc2KntnLjz_CDZvhVmnZhjjIDjyAcE1uZ98M0a4c49_e4vg_PkKWIADVTr3qPI1fe8oFw0Yqgr9JHPn5l8WI__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت در سراسر کشور‌ کویت از ترس موشک ها و پهپادها، قطع پخش زنده شبکه های تلویزیون کویت و اعلان آژیر قرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/686419" target="_blank">📅 01:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
صدای انفجار در بحرین و اربیل
🔹
منابع عربی از چند انفجار در بحرین در پی حملات ایران خبر دادند.
🔹
همزمان پدافند هوایی در اربیل عراق نیز فعال شده و چندین انفجار گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/686418" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
ارتش کویت اعلام کرد که پدافند هوایی این کشور در برابر حملات پهپادی ایران قعال شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/686417" target="_blank">📅 01:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
‏ارتش کویت: پدافند هوایی ما در حال حاضر در حال مقابله با حملات پهپادی متخاصم در پی تهاجم ایران است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/686416" target="_blank">📅 01:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
صدای انفجار در بحرین و اربیل
🔹
منابع عربی از چند انفجار در بحرین در پی حملات ایران خبر دادند.
🔹
همزمان پدافند هوایی در اربیل عراق نیز فعال شده و چندین انفجار گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/686415" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پیام سخنگوی وزارت امور خارجه درباره جنایت جنگی آمریکا در حمله به جشن عروسی مردم در بندر کوهستک شهر سیریک: هر روز بر سیاهه جنایات آمریکا علیه مردم ایران افزوده می‌شود
اسماعیل بقائی در پیامی در شبکه ایکس:
🔹
فهرست جنایات آمریکا علیه ملت ایران اکنون کامل‌تر از همیشه شد: امشب یک منزل مسکونی در کوهستکِ سیریک، در حالی هدف حمله قرار گرفت که مردم در آن مشغول برگزاری جشن عروسی بودند. بیش از ۵۰ زن، مرد و کودک بی‌گناه شهید و مجروح شدند.
🔹
این قساوت را نمی‌توان از زنجیره حملاتی که پیش از آن در میناب، لامرد، قشم و دیگر نقاط رخ داده است، جدا کرد؛ همان‌طور که نمی‌توان آن را از حمله به اهداف نظامی جدا دانست؛ حملاتی که با برچسب‌ها و توجیهات فریبنده پوشانده شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/686414" target="_blank">📅 01:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/686413" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4f370421.mp4?token=ejXaCHIeHh7vsCMdFLVYkPr9vcgAuyYv134rbv8MrH0MkoBZOt6LLyNi5QBhKhhDaFVwzgfqFh4sON-HtixHitVa9dPC9nnPpo5kLMGtD6Kh-kBtC-dYbQGUNKYBEQBv0uAxWcPap0b4ooVInyX3TLckUbq65bDapWJf94rwGe1vjTfFOMaCqBGJ-S963w5FUS7-cOPCSqaoZsKcCPZGp2XEG2DIlU6p9G3O5zhVX-Z_EzUdaHPxrrx2-KEdTbc10Kijz5-V-js9u8FsUQ9bqcc12i7lxU_CJ8tftO-MQm4npIuTZc-R3DL7-L_BUWqP-fPsrS7uXvLZdlBvmyZEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4f370421.mp4?token=ejXaCHIeHh7vsCMdFLVYkPr9vcgAuyYv134rbv8MrH0MkoBZOt6LLyNi5QBhKhhDaFVwzgfqFh4sON-HtixHitVa9dPC9nnPpo5kLMGtD6Kh-kBtC-dYbQGUNKYBEQBv0uAxWcPap0b4ooVInyX3TLckUbq65bDapWJf94rwGe1vjTfFOMaCqBGJ-S963w5FUS7-cOPCSqaoZsKcCPZGp2XEG2DIlU6p9G3O5zhVX-Z_EzUdaHPxrrx2-KEdTbc10Kijz5-V-js9u8FsUQ9bqcc12i7lxU_CJ8tftO-MQm4npIuTZc-R3DL7-L_BUWqP-fPsrS7uXvLZdlBvmyZEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری تلخ از عروسی که جنایتکاران مدعی حقوق بشر آن را به عزا تبدیل کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/686412" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/686411" target="_blank">📅 01:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
المیادین: پاسخ امشب ایران، ویرانگر بود
منابع امنیتی ایرانی بامداد چهارشنبه در گفتگو با شبکه «المیادین»:
🔹
پاسخ امشب ایران علیه پایگاه‌ها و مراکز آمریکایی در منطقه قوی، دقیق و ویرانگر بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/686410" target="_blank">📅 01:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2aac91e57.mp4?token=L83O5mCglK4BKZOmaGe3OyhkiyCHYgVE_7A9f0-Kpa-oUsi9Q30K1Vxu8Esq3UVJgq9ZtB_uuwmOxxSAJHfEjTsJ5omoH9xSNFzuXX07ru67PNMVDFgq8nXuWKyEfcbANkXir5hJ0egHIWJDhQKSmLtqyNtiDdduSf4UM880-fYB4CTJRhZ8z9DW3vgq2k_qWQM26xtmtmKz0mdhVfdGfechLIw_sNu71kvOdllRKk8A80SEsHjb8w6pBnmKKtrqA04dJhDpHjKll4GHEH5FyO3sPjWPoZbfAZBExqcvBCoxNNJB_5nMXAKp_xE3OSlyVsQvUcC-SXXyXlHncFcuZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2aac91e57.mp4?token=L83O5mCglK4BKZOmaGe3OyhkiyCHYgVE_7A9f0-Kpa-oUsi9Q30K1Vxu8Esq3UVJgq9ZtB_uuwmOxxSAJHfEjTsJ5omoH9xSNFzuXX07ru67PNMVDFgq8nXuWKyEfcbANkXir5hJ0egHIWJDhQKSmLtqyNtiDdduSf4UM880-fYB4CTJRhZ8z9DW3vgq2k_qWQM26xtmtmKz0mdhVfdGfechLIw_sNu71kvOdllRKk8A80SEsHjb8w6pBnmKKtrqA04dJhDpHjKll4GHEH5FyO3sPjWPoZbfAZBExqcvBCoxNNJB_5nMXAKp_xE3OSlyVsQvUcC-SXXyXlHncFcuZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو هیئت رییسه مجلس: هر کس در کشور به مذاکره دل ببندد و فکر کند که با این دشمن وحشی می‌شود مذاکره کرد و از ماجرا عبور کرد، دچار توهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686409" target="_blank">📅 01:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae470cfde6.mp4?token=iBjSTyg63jhJYKUH3S5pFaGMW46SQeBdt8b9kKMkQxLN53OwQwTYcAw8ZX2wtRMkMfvciEQvPupCbFEK6il_7x9c0mMYTfkciS2hueQ9VKfplFJqtplrAr3sivMWOCPfVRIVcqLKQHhQqQoC6xPyBN9_EOTmHJspu9dh_pX6OgfH8DPMgPmb25MzJDTlm3cXWt8QtJvtuAXWpS5l6u1_laoQSIt-at4v-SLTwTap8rdElkh8pxr79j8Zc5BCAk2y6AQBkJa07_aZJtwece1zdfoKrwP-mdr-JVbKtTBKE3x-9JsJBJC7upTBJ6d5PNJuulU5YN8SA05rSQ-7F4UoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae470cfde6.mp4?token=iBjSTyg63jhJYKUH3S5pFaGMW46SQeBdt8b9kKMkQxLN53OwQwTYcAw8ZX2wtRMkMfvciEQvPupCbFEK6il_7x9c0mMYTfkciS2hueQ9VKfplFJqtplrAr3sivMWOCPfVRIVcqLKQHhQqQoC6xPyBN9_EOTmHJspu9dh_pX6OgfH8DPMgPmb25MzJDTlm3cXWt8QtJvtuAXWpS5l6u1_laoQSIt-at4v-SLTwTap8rdElkh8pxr79j8Zc5BCAk2y6AQBkJa07_aZJtwece1zdfoKrwP-mdr-JVbKtTBKE3x-9JsJBJC7upTBJ6d5PNJuulU5YN8SA05rSQ-7F4UoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالگردهای تخلیه بر فراز اردن
🔹
این فیلم پس از تأیید بصری اصابت یک موشک بالستیک ایرانی به منطقه‌ای در نزدیکی کمپ تیتین، یک اردوگاه دورافتاده تفنگداران دریایی ایالات متحده واقع در خارج از عقبه، اردن، منتشر شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686408" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
یو‌اس‌ای‌تودی رسانه آمریکایی: ایران با استفاده گسترده از موشک‌های پیشرفته «خیبرشکن»، حلقه پایگاه‌های آمریکا در منطقه را به‌شدت آسیب‌پذیر کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686407" target="_blank">📅 01:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0CaJgIgKPFCn3o46Jj7-tp9sxU-75VuCirFgaG46YN-BsHlRUgE_vqi9onst5exlow6mQplsjWLKJJogWRIaqclHDKeAmG8l5zkF1h1Qw_Y1d1F1ItycK7iKcPBdIV4dcsahfgvL2onUtMlKk-o79kbxTApvewoSNdhNmoa2htRaQ6w560D9Z8lDNkGOeRAJoO_Ql16DNQarZJQXVyoEWVKOSwaljP6q_HSEssdlsTgaVSiiVpz0uUxtgjHxrlQd-DJItLJnorVlNjh-D1k4iCZotONG7ffsqsLi6qp41FSZepCBwRYZLINzzwA7UwZYLlDoJX0aIs3A4sU3Li__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: هدف قراردادن یک عروسی و قتل‌عام مردم بی‌گناه در کوهستک، گواه نهایی استیصال مطلق مدافعان دروغین حقوق‌بشر و تکرار جنایات آن‌ها در میناب و لامرد است
🔹
این جنایات بدون مجازات نخواهند ماند. هیچ‌چیز آن‌ها را از ارادۀ کوبندۀ نیروهای مسلح ایران محافظت نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/686406" target="_blank">📅 01:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0acdf5c71a.mp4?token=lMGbTtMN5kd5DalL6ZxwogQGIRUM10NLUrfGepTrnoGyzf5wIogEieVXxRMeyyQnjxodioy_akAAyD_tnIP6apcbgMyLarSH4ECfAqBnEhKzz932DhwJouWMdPNcg1GKmQu7ma9lwZXAQdAndRK_hrFAEwIYPvr7w83JxRD8nqkXKMSsWGmiKUVqH-OkBZF7yuKruWpdqLmID8keZgfDitVVEWBO1MTlZk6a7B5aisrADLOdJ7xbj-EkrDOIVnc05K9tckVZDpCa_n9L-RS_Pv1vqbcN0ScBMKRfLf0--5092O3BvDY0FYCKSr5mc1GvUpQS3aslbySUKxIGwcKm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0acdf5c71a.mp4?token=lMGbTtMN5kd5DalL6ZxwogQGIRUM10NLUrfGepTrnoGyzf5wIogEieVXxRMeyyQnjxodioy_akAAyD_tnIP6apcbgMyLarSH4ECfAqBnEhKzz932DhwJouWMdPNcg1GKmQu7ma9lwZXAQdAndRK_hrFAEwIYPvr7w83JxRD8nqkXKMSsWGmiKUVqH-OkBZF7yuKruWpdqLmID8keZgfDitVVEWBO1MTlZk6a7B5aisrADLOdJ7xbj-EkrDOIVnc05K9tckVZDpCa_n9L-RS_Pv1vqbcN0ScBMKRfLf0--5092O3BvDY0FYCKSr5mc1GvUpQS3aslbySUKxIGwcKm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک دسته‌های پهپادی ارتش ایران به سمت پایگاه آمریکا در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/686405" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73625973f.mp4?token=KH5mqnvR_v0hbKdqZTntYa6lw50qx7rYZTgMMA54940E-DvCT3AWVL43sCdmCoJipM1ERd3a8BZC5gdWij0jykIFNZIjKoCcjXooyAH-s7ju39HivJ3KHqvx99ABIAsxymnwYhdYp5GUj1cm1clZo7qz1W881cD3UYhGh_IiKPshtD6NK41j8yhL-Fh6WcT5Qu6ZNVH91VRpWBxuRSRE0yRm30oq0GPy20HUVjE2kn6DqhRvJpHR6l3s7SHaoyfjh_GVwb1wBITB6hZ8lDlIf2_MXygNl9Gg2z2vIJFpKalY-MpZF7V3125Lg22APfbL_gsJ6LNED7J0GHK5DE9W9xoQzmh9xfIq7TTS790GR2Ix0czZBWBReW0IpU5us4NEbum3MReIgJtNfreex9MHfuswaDyrLb3j05VQGvWnyyvlq2P4ZSauFjBTFaJEzdy6rRHrzjc1bAUZH3gntXOgqNkZMciGVWmchXUKSsG_ywzx1g4nBuRjEWfUpNwOqtIa6btlGIVm32MSJab2iQJ79TvevZKmPXePsWqYy0wNVWoS4DsF80Fn4nXAsDhNLyTUcnS1xjX6D1JKXbD6YXGF3LiF_wVF1XnudmfO6f8aW7cYji6YlOzQF434Z6M3-feIT09z0kf9r2xVkrxtal327GOdvOE_wYRwRZ9CCLvw8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73625973f.mp4?token=KH5mqnvR_v0hbKdqZTntYa6lw50qx7rYZTgMMA54940E-DvCT3AWVL43sCdmCoJipM1ERd3a8BZC5gdWij0jykIFNZIjKoCcjXooyAH-s7ju39HivJ3KHqvx99ABIAsxymnwYhdYp5GUj1cm1clZo7qz1W881cD3UYhGh_IiKPshtD6NK41j8yhL-Fh6WcT5Qu6ZNVH91VRpWBxuRSRE0yRm30oq0GPy20HUVjE2kn6DqhRvJpHR6l3s7SHaoyfjh_GVwb1wBITB6hZ8lDlIf2_MXygNl9Gg2z2vIJFpKalY-MpZF7V3125Lg22APfbL_gsJ6LNED7J0GHK5DE9W9xoQzmh9xfIq7TTS790GR2Ix0czZBWBReW0IpU5us4NEbum3MReIgJtNfreex9MHfuswaDyrLb3j05VQGvWnyyvlq2P4ZSauFjBTFaJEzdy6rRHrzjc1bAUZH3gntXOgqNkZMciGVWmchXUKSsG_ywzx1g4nBuRjEWfUpNwOqtIa6btlGIVm32MSJab2iQJ79TvevZKmPXePsWqYy0wNVWoS4DsF80Fn4nXAsDhNLyTUcnS1xjX6D1JKXbD6YXGF3LiF_wVF1XnudmfO6f8aW7cYji6YlOzQF434Z6M3-feIT09z0kf9r2xVkrxtal327GOdvOE_wYRwRZ9CCLvw8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه مشهد صرفا ترافیکی بوده است
روایت «سرهنگ موسی آبادی» رئیس پلیس راهور خراسان رضوی از حادثه امشب
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/686404" target="_blank">📅 01:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
وزارت خارجه یمن: حملات ایران، مشروع است، کشورهایی که پایگاه‌‌های آمریکا را میزبانی می‌کنند باید بهای آن را بپردازند
🔹
وزارت امور خارجه یمن اعلام کرد که تداوم تجاوز آمریکا علیه جمهوری اسلامی ایران، اراده و ایستادگی این کشور را تضعیف نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/686403" target="_blank">📅 01:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
استاندار خراسان رضوی دستور پیگیری به حادثه بلوار وکیل‌آباد را صادر کرد
🔹
بنابر اعلام پلیس راهنمایی رانندگی مشهد، ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و افزون…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/686402" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9f02e16a.mp4?token=s9CJvsslTKdksADsONhsQGzh_7Lx80VWKueKc19kVIvmPoUviABtYR4S940M-c8FPJ-4wGFwPrFgv0k9axSC77AkQ-P38kd9j2HBb02U46s9Bv82vXy91Zn21TblvzEeRMMSn-0d05IslDazFMzdmhEBQadJWEetBzIwgw1SC9Kv-GiyfiuVOTWwxHdI2aVu_PWNwUOGVGILBs_n3yY4lGW-tDjBbdqTYmBLAXTTmbojTsSYUfbO43E_FJ7UmeLQYuBoURZgN2RwXKK66-0w0jXrnNDLnvTBGts2wRMMpA-xGaiF18o_7WBj0JgmWuULEJY7IpQQDtkz7Hv5jpX0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9f02e16a.mp4?token=s9CJvsslTKdksADsONhsQGzh_7Lx80VWKueKc19kVIvmPoUviABtYR4S940M-c8FPJ-4wGFwPrFgv0k9axSC77AkQ-P38kd9j2HBb02U46s9Bv82vXy91Zn21TblvzEeRMMSn-0d05IslDazFMzdmhEBQadJWEetBzIwgw1SC9Kv-GiyfiuVOTWwxHdI2aVu_PWNwUOGVGILBs_n3yY4lGW-tDjBbdqTYmBLAXTTmbojTsSYUfbO43E_FJ7UmeLQYuBoURZgN2RwXKK66-0w0jXrnNDLnvTBGts2wRMMpA-xGaiF18o_7WBj0JgmWuULEJY7IpQQDtkz7Hv5jpX0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برق مناطق آسیب‌دیده قشم پس از حملات دشمن متجاوز آمریکایی در شامگاه سه‌شنبه پایدار شد
🔹
فرماندار شهرستان قشم از رفع قطعی برق در مناطقی از این شهرستان که در پی حملات شامگاه سه‌شنبه آمریکا دچار خاموشی شده بود: جریان برق اکنون در تمامی نقاط قشم برقرار و پایدار…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/686401" target="_blank">📅 01:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نیروهای مسلح اردن: شلیک ۱۳ موشک بالستیک به سمت اردن/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686400" target="_blank">📅 00:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حمله دشمن به برخی زیرساخت‌های تلفن و اینترنت در بخش‌هایی از هرمزگان
اداره‌کل مخابرات استان هرمزگان:
🔹
در جریان حملات آمریکا به مناطق غیرنظامی و زیرساخت‌های خدماتی در بخش‌هایی از مناطق جنوبی کشور از جمله کوهستک در سیریک، به تعدادی از دکل‌ها و سایت‌های مخابراتی و اینترنتی هم خسارات جدی وارد شد. حملاتی که موجب قطع شبکه ارتباطی تلفن ثابت و همراه و همچنین اینترنت در بخش‌هایی از این محدوده شده است.
🔹
در همین راستا و علیرغم تداوم حملات دشمن، عملیات تیم‌های اضطراری برای رفع مشکلات پیش آمده و وصل مجدد شبکه مخابرات و اینترنت درحال انجام است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/686399" target="_blank">📅 00:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شایعۀ حمله به کرمانشاه تکذیب شد
🔹
معاون استانداری کرمانشاه با رد شایعات مطرح‌شده؛ هیچ نقطه‌ای از استان کرمانشاه مورد اصابت دشمن قرار نگرفته و وضعیت در استان کاملاً عادی و تحت کنترل است.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/686398" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سپاه امشب کدام پایگاه آمریکا را هدف قرار داد؟
🔹
سپاه در موج دوم عملیات «یا رسول‌الله(ص)» کمپ تیتین آمریکا در اردن را با موشک‌های بالستیک هدف قرار داد؛ مقری راهبردی در نزدیکی عقبه که محل استقرار و اعزام سریع تفنگداران دریایی آمریکاست.
🔹
اهمیت حمله در این است که آمریکا پس از اختلال مسیر هرمز بخشی از نیروهایش را به این نقطه منتقل کرده بود؛ حمله سپاه، نمایش اشراف اطلاعاتی و توان هدف‌گیری این جابه‌جایی بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/686397" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686396">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMSs3L92GFfOAreGgUqnwvRMEh3jyXY5l3SXKWOzBxcnxWEW1Z_HcMr7gO5C_HIeZ1uv-DKAC-RIyKqJ-Jq20XdoDUC19DnO5l3iiXc-kxTFOd0gQ27EbkvsPC2rDLJU6gkJvbWU5sOd4QWV-P_fvtnemc8FxaEEwxDoAcnvK6-Iabq-6nYQNRO2RksTs9hFtHkQk-jEXCXFCURj6C2VXhwsY0uCqpvwfCY0t2JnKqPtAy1wbwQd_VQId5Y6KNH8zQzQQjt71DEi8QXGdsgQuTnLJE1X8USP_iaC37GZEnOPkYTvZraVzGVvXLrnNoicU9M96Plxxbm017UIldRqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از مصدومان حمله ساعتی قبل آمریکا به یک مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/686396" target="_blank">📅 00:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
چند نقطه از شبکه برق هرمزگان هدف حملات دشمن قرار گرفت؛ خاموشی تا کم‌تر از یک ساعت رفع می‌شود  مدیرعامل شرکت توانیر:
🔹
در ساعات گذشته، چند نقطه از شبکه برق در مناطقی از استان هرمزگان مورد اصابت دشمن قرار گرفته است.
🔹
در جزیره قشم و سیریک به علت اصابت و تخریب،…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/686395" target="_blank">📅 00:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
استاندار خراسان رضوی دستور پیگیری به حادثه بلوار وکیل‌آباد را صادر کرد
🔹
بنابر اعلام پلیس راهنمایی رانندگی مشهد، ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و افزون بر ۱۰ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686394" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/face74d2d6.mp4?token=aRRpaqqtJ6WS_B6nuDWuE69XX0fHiOUZ-83Bhssntw6IZHA_woZM-7BWyJShYjLXklnzUCGR71G0TljV5HPPsnGo7sy9ziyDcVWSxZtzQFl5OIi0Rrek1OXL-KcKbKEpSdneEH7yenr3UJvB6p3yE_e4qOm2Hhfpm37L25zmfQgTrApmLBhv9IBMMH91oOOnrE_eWT_fvUZul_PhrIi9nI9-v6klKelmFUgR_e6WW8r5VuLQ0Xd6xI4wK74btJP0ItMd8_qHnni3a06C9ChSdLgWCh7d5ow1o2fi_Paj4Ofaxb0ee6R4pHDPZi8_L6YtEPA6AfqojFPSxQcwXpILYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/face74d2d6.mp4?token=aRRpaqqtJ6WS_B6nuDWuE69XX0fHiOUZ-83Bhssntw6IZHA_woZM-7BWyJShYjLXklnzUCGR71G0TljV5HPPsnGo7sy9ziyDcVWSxZtzQFl5OIi0Rrek1OXL-KcKbKEpSdneEH7yenr3UJvB6p3yE_e4qOm2Hhfpm37L25zmfQgTrApmLBhv9IBMMH91oOOnrE_eWT_fvUZul_PhrIi9nI9-v6klKelmFUgR_e6WW8r5VuLQ0Xd6xI4wK74btJP0ItMd8_qHnni3a06C9ChSdLgWCh7d5ow1o2fi_Paj4Ofaxb0ee6R4pHDPZi8_L6YtEPA6AfqojFPSxQcwXpILYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی پیش یک خودرو به تجمعات مردمی در اقبال لاهوری مشهد برخورد کرد و تعداد زیادی از مردم را زیر گرفت
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242100</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686391" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17d416a8f.mov?token=dATTF6_pd0eEqDIEhK-QmdJUtylKWhBibxziTOjEHClZHAVdLNDgzNNmPYjp2UU_iSrNyw0rdA6GhdKcWCOkmyfBn2vJfzdlkG6IlHG8Go_bwwkYGIg-7fhQq4YD8fWNbW164p3qtKmItgi2seM4fimlQxFojWgxWV198eRwZlgp1vatYCo5y4UnNIK9pJddZwJQvWyi5egxdy1myJ2GeMI8nCbOVf3A2GyjxfAtyBwgpljWmSOMX6IUwjIPeDdefJWLzgxO-P3plKaXLS-xqWAGt4uhHqZP5vTBCpQjBwe9xMISFJbC3NKPjMzMXJK16p9fv92RsPrL0r15AVlpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17d416a8f.mov?token=dATTF6_pd0eEqDIEhK-QmdJUtylKWhBibxziTOjEHClZHAVdLNDgzNNmPYjp2UU_iSrNyw0rdA6GhdKcWCOkmyfBn2vJfzdlkG6IlHG8Go_bwwkYGIg-7fhQq4YD8fWNbW164p3qtKmItgi2seM4fimlQxFojWgxWV198eRwZlgp1vatYCo5y4UnNIK9pJddZwJQvWyi5egxdy1myJ2GeMI8nCbOVf3A2GyjxfAtyBwgpljWmSOMX6IUwjIPeDdefJWLzgxO-P3plKaXLS-xqWAGt4uhHqZP5vTBCpQjBwe9xMISFJbC3NKPjMzMXJK16p9fv92RsPrL0r15AVlpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از مصدومان حمله ساعتی قبل آمریکا به یک مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/686390" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNAjOfHsQC7HHjdLxEuFmFyl5vQpp6H2Vmxt86EREdp65oEsybhEpCCAvzWONgPzVts7Fp4O-1wNKsn2dzgpzqhEmJu2PxGjvt9SyLZRCpU91w_11M7aWmd5-oduEz04hX7kfVHsi93UlxNJ2OXbEwBkBTn74XRZL0qdcFhtkuSJTt_TAzGaStHsHaYhN34_-zcuzk3S0pFJVURyE8s7Nq3kVy6CpAcNomqRzJDShQKPjAh0CULPjvUBf1pYcaVBEC15iKCV6uZn9NcULgD-vpYEwCFAMrvnYFFSQm4UlFotiMWacQSyit-cpo1Swhp_UwYkIn7OUqMUytR7Wscb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف پروازها از فرودگاه نجف به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/686388" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e95424e8.mp4?token=vSfaKWvyBK0P-DkvlAqLzJ377qIX4AYU826Leif5xoAn_5J-yNAEREV1dXRyQvfAb_HZvkjpcVHWoxNqiDcDwjXqd-89AecXczdJ6zAHSTYcSR-2B3Va7ugTjIqUCyfFo8rNVemZZnw80Djz6A8P58QOXVvNcxGBpQ9hmy0O4r_A6P96SCDjMRZAAywKv-KhQAybSRiymVKFkZrRek-jvKd1_8bQHJtyIBENgQGX2zlYR_FZM3JsVW-QOa0gNUIG-WghCjKoq9QNcgYIa6b4IrxWYosNTkIoXUyPDi7Q96kE2lgrTOpatHcf0G3TxD3g3Y7_-rQqmewyF-HoPNtJRSGLIpj_fmYfaNA-USljHwWzhXpjhvFz4xCkA-2pLrI0f49SQkyyceaQmoPZJo2-23AuERTyFhIlEWSwHnzh9PwCOD47qvpIvLfgaWcuEQ1dT0A62Oyx9q-kNM-f0NAyb2KJDkP11OhiBjZ1pAsyWaOni6_IYJUcOt5zwAZtNcPIGeFSjZh9qXdgbmPC6q8LPwKm3sI9Bh2fmGgRgp1h-YPRBGcsUSupQWN-L0c66JOK2ITucDJdHMo1RcGPWSTuHy2I5BeHk-WQXtGmCgMl-D33qH6MIVYJAdQ63-gs8CUz4-zxkfXb5kjUuUDLD17JTfv7j0eB0ZIm1U7xg4p2sOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e95424e8.mp4?token=vSfaKWvyBK0P-DkvlAqLzJ377qIX4AYU826Leif5xoAn_5J-yNAEREV1dXRyQvfAb_HZvkjpcVHWoxNqiDcDwjXqd-89AecXczdJ6zAHSTYcSR-2B3Va7ugTjIqUCyfFo8rNVemZZnw80Djz6A8P58QOXVvNcxGBpQ9hmy0O4r_A6P96SCDjMRZAAywKv-KhQAybSRiymVKFkZrRek-jvKd1_8bQHJtyIBENgQGX2zlYR_FZM3JsVW-QOa0gNUIG-WghCjKoq9QNcgYIa6b4IrxWYosNTkIoXUyPDi7Q96kE2lgrTOpatHcf0G3TxD3g3Y7_-rQqmewyF-HoPNtJRSGLIpj_fmYfaNA-USljHwWzhXpjhvFz4xCkA-2pLrI0f49SQkyyceaQmoPZJo2-23AuERTyFhIlEWSwHnzh9PwCOD47qvpIvLfgaWcuEQ1dT0A62Oyx9q-kNM-f0NAyb2KJDkP11OhiBjZ1pAsyWaOni6_IYJUcOt5zwAZtNcPIGeFSjZh9qXdgbmPC6q8LPwKm3sI9Bh2fmGgRgp1h-YPRBGcsUSupQWN-L0c66JOK2ITucDJdHMo1RcGPWSTuHy2I5BeHk-WQXtGmCgMl-D33qH6MIVYJAdQ63-gs8CUz4-zxkfXb5kjUuUDLD17JTfv7j0eB0ZIm1U7xg4p2sOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پوتین برای حمله به تأسیسات انرژی اوکراین
🔹
رئیس‌جمهور روسیه گفت که دستور حملات گسترده به زیرساخت‌های انرژی اوکراین، در واکنش به حملات این کشور را صادر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/686387" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=WXE5USiv1J8CRg89982rhXE8y1hOCks9S0F_f033Imsy9fYDuk6DVSdK405wpTkrX8LqfRQb3SZfEn28JXfeAscWWRLyfjZqmnHL48fNrdHOElGMat-LME0CovGrOhlJRGfDvhYQcrVTWtxFxHkSkv4Vn7TAAs_j8U-bgwo70n84_ebGdZq_lULD7YQXdLqK2tqx2IotTq_P-XSxCnfm9FswMq_EtATXPJs0fQGNnJ9aRKegeCBYwotLhwFru8w1z_KFeaN5u_2oOqqEKVYIVkDNN5usUmTcPfcOIJXCinHemVXiTYagI92YVw97otzfy6fWTXJ6g5nT2xVPJnyPcg1l9Kx_LhVuSGJME88jG9QK1C6Uyy-qsmfUdrqnZ1wORRCsdx1zmEpeM3GivB3T1613viPA7KpoZzUN-_VAJIBZgjCM-bUo2VF6jo6xMluksJCNR70zalq21lhy6VQfVOGdKbCjoBq-MAyPkNSrFZaDuQ3eCT-J0ldnEfFvWT8FHfx2hfz_LdOW1_u017RtMRGqbZxQ6AUwHaDp2P3YBMnbL0lgVKWgTJ4P7-JaLbtp6wY5nsQXG2_z9yCp0kUp1r_m4knwc3e1QmHJjZ1OrvblFpSUVqJ35YgFFBbleZ51wiNCrvwMSwWHFF3tGKoCnCHmQCctcBcnxSwQ0R9PwkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=WXE5USiv1J8CRg89982rhXE8y1hOCks9S0F_f033Imsy9fYDuk6DVSdK405wpTkrX8LqfRQb3SZfEn28JXfeAscWWRLyfjZqmnHL48fNrdHOElGMat-LME0CovGrOhlJRGfDvhYQcrVTWtxFxHkSkv4Vn7TAAs_j8U-bgwo70n84_ebGdZq_lULD7YQXdLqK2tqx2IotTq_P-XSxCnfm9FswMq_EtATXPJs0fQGNnJ9aRKegeCBYwotLhwFru8w1z_KFeaN5u_2oOqqEKVYIVkDNN5usUmTcPfcOIJXCinHemVXiTYagI92YVw97otzfy6fWTXJ6g5nT2xVPJnyPcg1l9Kx_LhVuSGJME88jG9QK1C6Uyy-qsmfUdrqnZ1wORRCsdx1zmEpeM3GivB3T1613viPA7KpoZzUN-_VAJIBZgjCM-bUo2VF6jo6xMluksJCNR70zalq21lhy6VQfVOGdKbCjoBq-MAyPkNSrFZaDuQ3eCT-J0ldnEfFvWT8FHfx2hfz_LdOW1_u017RtMRGqbZxQ6AUwHaDp2P3YBMnbL0lgVKWgTJ4P7-JaLbtp6wY5nsQXG2_z9yCp0kUp1r_m4knwc3e1QmHJjZ1OrvblFpSUVqJ35YgFFBbleZ51wiNCrvwMSwWHFF3tGKoCnCHmQCctcBcnxSwQ0R9PwkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حملات گسترده موشکی به اهداف آمریکایی در اردن در موج دوم عملیات تنبیه متجاوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/686386" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686385">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c02b3ddf9.mp4?token=Y_LwUqIwMw-M9fmPdHaQxRdwS0EbNtCUA9hXkhXId9RKFvU5szkxWo2toFbI4ElwYLcQwa2epNDe_3MU02-mj-x6g9pFY-FqRykz0XlF8T3jn630MO-VpRwK4OoGeeRpMrHjFi2F_S4MAXK849ObIfPwSBdcn3mRuWQRCRri4atYGUtNXCXVGCJ2pqbIMwlh_PYr9XA8F29y_-m8p-rE_CfgX7vAZbjv3nq_eyyXTn93zN0BXyY6hLJdVXOi2IrI8OZOrru5Cf-bDxBmj5CNCPtmfw342T0sTUmXQp-7tJ5ZsSezLYVODE88PEFIT0eZXpVEQS8SPtZ-rceCXjmfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c02b3ddf9.mp4?token=Y_LwUqIwMw-M9fmPdHaQxRdwS0EbNtCUA9hXkhXId9RKFvU5szkxWo2toFbI4ElwYLcQwa2epNDe_3MU02-mj-x6g9pFY-FqRykz0XlF8T3jn630MO-VpRwK4OoGeeRpMrHjFi2F_S4MAXK849ObIfPwSBdcn3mRuWQRCRri4atYGUtNXCXVGCJ2pqbIMwlh_PYr9XA8F29y_-m8p-rE_CfgX7vAZbjv3nq_eyyXTn93zN0BXyY6hLJdVXOi2IrI8OZOrru5Cf-bDxBmj5CNCPtmfw342T0sTUmXQp-7tJ5ZsSezLYVODE88PEFIT0eZXpVEQS8SPtZ-rceCXjmfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دردناک از کودکان مجروح حمله موشکی امریکا به سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686385" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تکذیب صدور نوتام برای بسته شدن فضای کشور
سخنگوی سازمان هواپیمایی کشوری:
🔹
نوتامی برای بسته شدن فضای کشور صادر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686384" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت
؛
تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686383" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4cb478ba.mp4?token=OXfRYmIvmaLu8fLRp2uuK0PXVV6Z_KGAv43Bka_ellDPXU8s_8r4TjH9mWrtMztIToQ55aOt7BQBnCM-6_eYZra7Wo_C0zlQZ8BpnMGo6-zod_PfeGN9Z39yURx67l8Rk7o_FBPDXOlLhapxAra8OpnxaDpPPO1VZeJ9kSpBvZ9WuGZeBIP2Qem9mHaQxLx01KgrUOGazXQCni1olsUfdSk47JkiSyb3KSjGGGbj_KzXnmvcG7_Dnz290KRUa2VVemlx5xIMiT2uesP-ZNNbXhRB46TJqYBHxXQl6IkoWUvxo5uxgIMkJLOf6-CCTuwXCpg_4_SFMFqBmwDSNf-uPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4cb478ba.mp4?token=OXfRYmIvmaLu8fLRp2uuK0PXVV6Z_KGAv43Bka_ellDPXU8s_8r4TjH9mWrtMztIToQ55aOt7BQBnCM-6_eYZra7Wo_C0zlQZ8BpnMGo6-zod_PfeGN9Z39yURx67l8Rk7o_FBPDXOlLhapxAra8OpnxaDpPPO1VZeJ9kSpBvZ9WuGZeBIP2Qem9mHaQxLx01KgrUOGazXQCni1olsUfdSk47JkiSyb3KSjGGGbj_KzXnmvcG7_Dnz290KRUa2VVemlx5xIMiT2uesP-ZNNbXhRB46TJqYBHxXQl6IkoWUvxo5uxgIMkJLOf6-CCTuwXCpg_4_SFMFqBmwDSNf-uPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایرانی به اهداف خود در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686382" target="_blank">📅 00:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
چند نقطه از شبکه برق هرمزگان هدف حملات دشمن قرار گرفت؛ خاموشی تا کم‌تر از یک ساعت رفع می‌شود
مدیرعامل شرکت توانیر:
🔹
در ساعات گذشته، چند نقطه از شبکه برق در مناطقی از استان هرمزگان مورد اصابت دشمن قرار گرفته است.
🔹
در جزیره قشم و سیریک به علت اصابت و تخریب، چند نقطه دچار قطعی برق شده‌اند و همکاران با تمام توان برای رفع خاموشی در حال کار هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686381" target="_blank">📅 00:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
جلسه توجیهی فرمانده سنتکام برای اعضای کنگره درباره جنگ علیه ایران
🔹
وال‌استریت ژورنال خبر داد که فرمانده سنتکام برد کوپر صبح روز سه‌شنبه برخی از اعضای کمیته نیروهای مسلح مجلس نمایندگان را در جریان جزئیات مربوط به جنگ علیه ایران قرار داد.
🔹
نماینده ایالت آلاباما و رئیس کمیته نیروهای مسلح مایک راجرز با اشاره به محتوای این جلسه گفت که ارتش آمریکا «برنامه‌ای» دارد و او پیش‌بینی می‌کند که درگیری‌ها تشدید شود.
🔹
این جلسه توجیهی صبح روز سه‌شنبه به وقت آمریکا برگزار شده و تجاوزات علیه ایران در ظهر سه‌شنبه به وقت آمریکا آغاز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686380" target="_blank">📅 00:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686379">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
صدای شنیده‌شده در برخی مناطق ایلام مربوط به جدا شدن بوسترهای موشک‌های خودی است/مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686379" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlQPbHSoDqbO0Cu1hYMOfnYT3NXA1kU9irxbVulilNgCrGZJI8RtO6Fl2HFdSFi6386-jUTOqlbjNo_abSZONCqIvKL5fr88An-GiQr14WgLPgHkVjJ0TN5ErQ4BqdU7ooIbXgCbZgb7pkWKN3q8hzadlHrVWRARFcKFlMZg01g7x_frIUAcbWYjJ68ZugZ02ZqXVlvqxdFlJVmfV6wRjfzpq4jgrlXYVomMtOLarpfofiedATxGPWmm6AvwxierY444RlIjs14rrrfXWF5c4aI4aIqq24WNopRmRxw-ABr77Y-jJgUI0lnu09lo2Ya1GDLQUA8gWeEBlUjM7RsqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l72kKmi-1Uw8hDMks8VV3AUztVIMSvQghi23RT6LfjUROwO3Kn5VfZor8GQwXRgEM_BNf1WEjAFPmOnjzfyhLqp3N_Ol2wsStzq2OKWK48h7htNMt_V3Nzp0_9uhj7RjKUV2IMQl-n_X0WBI6bAWnEHWYtA4CPx15rFWl73NaFCMhktYd-YBBe8uK0BXAWleC69Ztczo6Hep3LC7PDQxBqxXh1FhTsqUoWzpEMisnZhnxAgBTm3yOSlDbIFsaNBv4nfaBcDZ0ZEvlpBkl8BkaqpOhP3B92WCdSCEPBk09nhYGdwI3YXIdd8N-aznUPp5RNU0SMJtADO2p5clPlH0fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندار عسلویه: اصابت به یک مقر نظامی در اطراف عسلویه خسارتی نداشت  فرماندار عسلویه:
🔹
اصابت در اطراف عسلویه به یک مقر نظامی بوده است و خوشبختانه این حادثه خسارتی در پی نداشته و گزارشی از خسارت دریافت نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686377" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSTW_7JHVVr-O1jtjHKuJUG9D7RQFxuCGWE6-PnWkUP99fQZ8nI8JmE9uphWerKSLjj40P4boBS6ptUq325NeZfpzNddS3PSn5WYIabr2TZQKzGbDwM_ibLXwfKqKh4AptPY8csbCRkFp9KS1lMjc-9aWGsJONVh20Ri-YNch4jQYe4UAbFo03jcKl13HEmo52UlN-koFs55G48KiOlZNLMLVVDMFNvtMg1Q6dMWJG5lNKUseypbBLEfMcrsD-MDazrB98qX5nHrvM2_C5R9UsRf-YzIRn7rqGUUO5tIJmIb9AIf0kxYoYg8HJyXoBNm_n9STHgZirff6Ehukbe6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/686376" target="_blank">📅 00:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686375">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686375" target="_blank">📅 23:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMxmAJG12D0FJIXNvIga8WGSB62lgLts2TgFIWbykdjILjHGQ9NJAoUuFDfE2xDuu2GC7kw4KawlxKh_5YkS9bA9vNj93TDjz1iIWzNhFyWKWTr1VQyFpLzHTiUUprs8m3zslxbCtfYfQ1wnq47eFZX6lsUlpdYxuVjL015yEsLD9LBCQ5rfE4Y1ZsjBRoQnW0i2_wZBjMYGG4CUsw5u0i1nm0v8_J3vN32I7OhebxpLriWD_otZU_DJOTerJlTgJP5oylD8SbVQK2f1mDL56BJd7FGSQa5CffYj1IhkoYvkxHzwqxB9dwd4IOi6F7dNlBDeb5UD_2YX_b3AmPA4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: بی تردید به زودی انتقام شرارت و تجاوز، از دشمن گرفته خواهد شد. سریع، کوبنده و گسترده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686374" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686373">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfgaiTgQ5-rmMIDhnHra2jEBZpHMoI0SWQxItmTRX0ROaKp1ZpO95bhThaXoKxy1-9fNczFa9R5G8mRFTn9fE095jwkulsbggvdiaC3qNi9MAFRKkcHdEJD8m3Inj7EvXQBL2DQH_LMe9DlAGQQU1-TWiOzg1aUPfveX2zv-JdeQj6QmAlSgpEni5vd1aGUp32BfSA94EIm57qGO_5WfB13wgN6l-qMw-JvCFaXvQeXI4Lc1j7-eztsqpe2cADCTOWr3_Au_wv7uiNwtjcltUKGHfRosFcTimmdo3VaDX3LRoz1voOA2e6Abh-uivo9ZWFThD7c8tBbvrWw1dFL8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری منتسب به اصابت موشک های ایرانی به پایگاه های آمریکایی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/686373" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByyvdwuFY4AdzdVEYhc8IYGbiU04hKX5s726I3VnyiwjdJ9xvT1c-4yN_S-ZJz4aMA1NCl-7dq6D5ASm5evA_aRPahYK_8hgUiDbkHoxeq-kFcO3IqlXaR-Jf2MQ1UX_5mOJX9ziRtGXEM7aGuAAbED-LuHeM5So6y4jCd-cQFlR33KgwSf8Zg0RokK4OstukJ-rfS1X3kpwMq8ejklZVhqlQ9A24T_Digp4V8kzMTsslRZlmDFvs2uYgn7DUHsvwwUIyazcGPtlO0CJvfyxpwb20RgB3m5ny0CwJSYVthFWHmUj-DfoGLHjgQ0ChatC7PHomd1ZdICpTf7y-Rzqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqAVz0S7VigdNnHOcLZ2DRGHNRrd3KXilDiF355LOKS8I70h6m1UUzMots3EBHHFTULy0CZWQxLlakwIyPhDXDfLyPsuHYkH0ziHQJWTiftf8WJa-i6fvknbt2ohGghPSq_a5JJNEr_r0ZO38fNclW3ODcfRecZ_DTtTsuvhmt4prAjwxbM5FhVx8oFu8kyny2rzVrtdawYHOarHQhmrZO9jSarzzXX2-0zZsHPopvvYp9Yufh6dddvL7fo7wDMIlaQalqM7HSEQqieByv76kAfz-tWtaYwNAY_OLG-DHolzRdQNEykeMTMK3tKfW0M2jy6xXQ6-9whpt6yNINrT5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر تائید نشده از اصابت مستقیم موشک به هدف خود در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/686371" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686370">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
🔹
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
🔹
اهداف مهمی که امشب هدف قرار گرفتند متعاقباً به صورت رسمی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/686370" target="_blank">📅 23:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ed2d5287.mp4?token=BhoqH6m0eBgBy2ghIF7DsOUHo0zXI2EVqZ2RQtXoKpbPFfa3jId9dbicpygmfsWw52VfX_bhWORzcY8083qCUHRU85TMmVNlQzgUoaltDzl40_yoY1W4Pe7HteJtYagQvJEejepVo14G-HeLai1h62pWVNfpntUaMiJOv8tmpXr8OTP7tx9fC9jniEe5-G-XGvpmXfAL6QiiZSpbNUCdR-B-dWCwbeIYVREU9p3_Dwid1vt_P9Nb7e0xQ73VGhCmuxiCJnYkQI-kpvqmf3EIV5N2oTi24SmhKyA3r9XRaZ5wMLQ-nLfgecM5-8O-Wam7nX3y2q_0A4GC8ia-c_nw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ed2d5287.mp4?token=BhoqH6m0eBgBy2ghIF7DsOUHo0zXI2EVqZ2RQtXoKpbPFfa3jId9dbicpygmfsWw52VfX_bhWORzcY8083qCUHRU85TMmVNlQzgUoaltDzl40_yoY1W4Pe7HteJtYagQvJEejepVo14G-HeLai1h62pWVNfpntUaMiJOv8tmpXr8OTP7tx9fC9jniEe5-G-XGvpmXfAL6QiiZSpbNUCdR-B-dWCwbeIYVREU9p3_Dwid1vt_P9Nb7e0xQ73VGhCmuxiCJnYkQI-kpvqmf3EIV5N2oTi24SmhKyA3r9XRaZ5wMLQ-nLfgecM5-8O-Wam7nX3y2q_0A4GC8ia-c_nw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تائید نشده از اصابت مستقیم موشک به هدف خود در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686368" target="_blank">📅 23:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در ایلات
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی گزارش داد که شهرک نشینان «ایلات» اشغالی صدای انفجارهای مهیبی را شنیده‌اند که به دنبال شلیک موشک از ایران به سمت اردن رخ داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686367" target="_blank">📅 23:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تصاویری از محل عروسی در بندر کوهستک شهرستان سیریک که هدف حمله آمریکا قرار گرفت  صداوسیما:
🔹
در حمله ارتش آمریکا به مراسم عروسی در سیریک، ۲۸ نفر مجروح شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686366" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686365">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
فعالیت  پدافند در شرق تهران ـ دقایقی قبل
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242065</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686365" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
حمله آمریکا به شهرهای مختلف ایران
👇
khabarfoori.com/fa/tiny/news-3242065
🔹
شلیک موشک های ایرانی به سمت مواضع دشمن
👇
khabarfoori.com/fa/tiny/news-3242084
🔹
فرود هواپیمای غول پیکر روسی در بوشهر
👇
khabarfoori.com/fa/tiny/news-3241987
🔹
حجاب فرماندار نیویورک جنجالی شد | چرا او روسری به سر کرد؟ | عکس
👇
khabarfoori.com/fa/tiny/news-3241953
🔹
پیدا شدن جسد رزیدنت بیمارستان بهارلو دو روز بعد از فوت
👇
khabarfoori.com/fa/tiny/news-3241853
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686364" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
این منابع همچنین خبر دادند در حملات نیروهای مسلح کشورمان، پایگاه هوایی شاهزاده حسن اردن هم هدف قرار گرفته است
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242084</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686363" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7iTHZfFfCljwxQ-kausdRbHxdiWmgUOy0lAyosk3sIxOsyrRioO00gYKugGQLwxxAKxqjjHjGP1s53QRhCsC8iLCRTtkjVdFUlEMaxpUBJLoNDza0BD7Pe_Z1OzSjjJUDRs_1cW24WKpBBRu-7iwjjbnkSQGF05KHNbeSOtCvLXtBrOmx6wGv0tCZInH7MxE85O0PI-3shLc_3gWPPGnJDmH_cdW-R1VMIsx9XwniAiaWKvTj4eKHxvnrvkLX42poU8bPLf_3deFoj5zblaNcWEXE8UgR2wqAYIacMdMYitSrgEq4rcwMLiqrA16NpH3pX9czg3fFahMeB1LBKIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب: ملّت عزیز ایران و جبهه‌ی مقاومت، درسهای فراموش‌نشدنی برای دشمن امریکایی دارد ۲۶/تیر/۱۴۰۵
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686362" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پایگاه هوایی «موفق‌السلطی» در اردن هدف حمله موشکی قرار گرفت
🔹
گزارش‌های میدانی از وقوع حمله سنگین و اصابت موشک‌های بالستیک به پایگاه هوایی «موفق‌السلطی» در اردن حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686361" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYBaTod2tcgyPx0UkZdlRumn2AMfQZe4MNad_Tsf24_cLasx6QTs2nQHM9_4Zto5d5B_Gbx267RtexhU192FRuZ7eWONuJDbwOORZREzVW7ctxDFXhwbSOZr5bda1EAcqmYjSM0wioRfi1Pvl3hxxyu5NCOCepGVWkp3tgTX-1yw0VYEYhvUuYuXFMgHf7QIybiWDX--SrX74GPKYagkS5Z-SNoQ0D148CKZmqe51Wzmh83Z9cUfN03lEwnOCBCHsV0uDFgb80mWm9Zz5jZSPQjvDwwQ2iWpRzkQ6Y__SbUZ0K8mSeXsh1gRKPPF8RlnIGpRraQjrIW_lsM4ovLmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1Kw8haPLsfleqIuDTF6X5mdCgXvqp7gZF1AoGtrHcCNOBz83JOQEmxWJQftcZmcVgKPrxXMSCYN9x0GH-ks65hsmKeHV77hh0mCJR9v4WS6I9OxpkjaX8Vl2QM7GA2P46iWyssUL6Y8Mz_l3QShAz21lXKrikEE6CaRoX7AQMC0_gkNNTTwhJkgfFXpAIDJZH3fgSyp8DCVU3jLY3oIvUAw28uO39VJCDn0NqKK7FgtLSIiXgNW43mKl4TzOkm3DVeBD-BGcWUsAYbZWDJKkBEie6Tnfb9g-8rERPtdevK269JiMOxnYaVzLhhZ-BuYXGdavYgs4efRo-eNJY_Ntw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c089fa9b89.mp4?token=WP5kKPnDnlGujX3g2vNgvVjTsQGY0yHDP3Yb2zsXt6VURTOPPrT8kkovwokDowmI7JllvzFBTaSydQYRER_QTj6417z1frVFGB7xdjzc4fVA_CO1dMogqoU12ZpJ9GZxLWWgxn37sCgXOSbN_W9EcbNJutCBEFDHEd1LsiVgGRbj_LNgrdXJE_iQGatXu3kW71AQb5d1lXXjoHfunpg96_tdMId3SucDCG8-PnbFNTaAkmPtuVHbJGZVn8BAj1WUMZHV1fD2kYjjs-uBbVBQ8aW9SCN0qAPqkm0WXUP8JUIaeV846SwUPqk5NMMVjb00mPaC61sYhtD8SsSAMmOwJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c089fa9b89.mp4?token=WP5kKPnDnlGujX3g2vNgvVjTsQGY0yHDP3Yb2zsXt6VURTOPPrT8kkovwokDowmI7JllvzFBTaSydQYRER_QTj6417z1frVFGB7xdjzc4fVA_CO1dMogqoU12ZpJ9GZxLWWgxn37sCgXOSbN_W9EcbNJutCBEFDHEd1LsiVgGRbj_LNgrdXJE_iQGatXu3kW71AQb5d1lXXjoHfunpg96_tdMId3SucDCG8-PnbFNTaAkmPtuVHbJGZVn8BAj1WUMZHV1fD2kYjjs-uBbVBQ8aW9SCN0qAPqkm0WXUP8JUIaeV846SwUPqk5NMMVjb00mPaC61sYhtD8SsSAMmOwJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفیسی، معاون سیاسی و امنیتی استان هرمزگان: در حمله به یک مراسم عروسی در سیریک دو نفر شهید و تعدادی از افراد نیز مجروح شدند  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686358" target="_blank">📅 23:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
آمریکا مدعی توقیف بیش از ۵۶۰ هزار دلار کمک رمزارزی به حماس شد
دفتر امور عمومی وزارت دادگستری آمریکا:
🔹
در چارچوب تلاش‌های این وزارتخانه، بیش از ۵۶۰ هزار دلار کمک رمزارزی که مقصد آن حماس بود توقیف شد و پلتفرم‌ها و وب‌سایت‌های ارتباطی مورد استفاده برای جمع‌آوری کمک مالی و جذب نیرو مختل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686357" target="_blank">📅 23:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">🔹️
می‌گویند دلار ۲۱۴ هزار تومان و نفت برنت ۹۵ دلار را رد کرد.
آمریکا به خستگی ما امید بسته چون برای خروج از جنگ نه طرحی در عرصه دیپلماسی دارد و نه نظامی، اما به تکرار ۱۸و۱۹دی و فروپاشی داخلی امیدوار است.
ترامپ جنگی فرسایشی را دنبال میکند که دلار را بالا بکشد و فشار معیشتی جای پرچم‌های خونخواهی و مقاومت ملّی را با پرچم‌های اعتراض و جنگ داخلی عوض کند. پاسخهای وسیع و شدید ایران هم معنای واضحی دارد؛ تنگه باز نمی‌شود و نفت و انرژی و اقتصاد جهانی روی خوش نخواهد دید.
ما زودتر خسته می‌شویم یا ذخائر نفت و گازوئیل آمریکا زودتر ته می‌کشد و اقتصاد رو به فروپاشی جهان آمریکا را زمین‌گیر می‌کند؟
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/686356" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s90mWyqdH2omJ5g1GIHImtpNb8YdZe-Vhe9aVnineIxO-vjTbZ4iCnbZV_CYlzNwjJt3vYQBU0h4FdeymY-2NWCZdjasZ01qCtWIFX4t7jblqo19O0W7Iq_S-7DPebYRO4AawXxxEt950_7pF2JtwSvNLehig_vGucJ_X2C8V_q98EyXdBIelPDFNTKqT3bx2a22h2Ua9hkQgFHTL8SvK2oGIMDhqUvBFlpVtL7TK8cSIKw0bZwUe-0DGh1Cs6k3rZ4MzyRScXX89b9QIjrQxfNd0-WYlzCwqJ-yYqk3-t_Xsgc-ND9l_pCfOnELsAb8jg-vCM9pdKvfVHC4xPFIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUyeDs1yXKO0ht3yKAp0eo0ROe7J2MV-zyDrU_qIlvew1iE9kLh8swxNkbPXEU4xgpFmeAjA-KBVcq2fHuplA3CVefGLi5BnB6hWaVHh64wnfspe4aD24TjxCUk9QPVR-eUc8EulrAsbuHn_qfXxbjVS6Jg4HtB9Zf2kfn55S_bKOZ8KH8Y_Vic0KlhMqSEmPxsAoW59PNAZFxMH4WQv_TBEEaNSTeg-yQTz2ALADS_wHMbpm-2_zhxR53gGS6yj7e71JiYu2FU8fzI9XJByEXrZd2e4N04mfV9LCrUGl18vCSEcrgM7y3yoJ01KDVAv1PftkMnkOdP-lGS8z4pbSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2b06490f.mp4?token=IqergZcW9fggxh9om3_6TRF1DuAr1AYmrBc-1B-iFV3gcTk83vpW-CCM_A6jmNHiu0dDNC7hGxnVMBGhzjWCgiVpTZgZ3hp4AXUWJoV5ZT1W23jpaH-Zjp-mvDIPIW6wiYp8kGErqgi0VDC5gnaMMI-aAoQ5guo5WoDcc8FxGVHogNc8f_R8VtCc31Gqxo98ZezKyPFdnMDzm44cdkzX9RxLDVZ0D0XVXbqXwO5-hOV_JbMs2ANzW2GzVDeSorPzqxHaNQwvjeg7vG43E630U2xEHdZiIzO9Y0wsSbsoSmewlFfkwva3bsEczex3L_5v75jWBlinxr1NIW0-jkxzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2b06490f.mp4?token=IqergZcW9fggxh9om3_6TRF1DuAr1AYmrBc-1B-iFV3gcTk83vpW-CCM_A6jmNHiu0dDNC7hGxnVMBGhzjWCgiVpTZgZ3hp4AXUWJoV5ZT1W23jpaH-Zjp-mvDIPIW6wiYp8kGErqgi0VDC5gnaMMI-aAoQ5guo5WoDcc8FxGVHogNc8f_R8VtCc31Gqxo98ZezKyPFdnMDzm44cdkzX9RxLDVZ0D0XVXbqXwO5-hOV_JbMs2ANzW2GzVDeSorPzqxHaNQwvjeg7vG43E630U2xEHdZiIzO9Y0wsSbsoSmewlFfkwva3bsEczex3L_5v75jWBlinxr1NIW0-jkxzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک دسته های موشک از ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686353" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پایگاه هوایی «موفق‌السلطی» در اردن هدف حمله موشکی قرار گرفت
🔹
گزارش‌های میدانی از وقوع حمله سنگین و اصابت موشک‌های بالستیک به پایگاه هوایی «موفق‌السلطی» در اردن حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686352" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570698fa51.mp4?token=IpgU893m_BC0KfW6z322U0Ftwc-1qy7JYaeDl8PqakwNcDjr_stznnk80xyzlCOsNh2cni9hZSzLpXyP4Qfv8kRrE__tZT8PlewYYEiqNh0Zv7al73kS0QISJY_uub7HqKz3WOMBWh_qAQ0l0WA9c-R_bGS0U1Gbh-r3ddh8vYTwamUxH5MNvhCoHDodvVckgcsvsVY8OX87iGtSZXH95XLPhaHhzjcxFfnLnJ-whDAKmaFzI0o7aiLJUU0H_I8NhowgQwo7LLRaKC1QNn9Hj8gJyoe0bsEz9zRKxxLCKf5uW1JKjhHocuWV5vo_csEYYl1Hek3ac4nIhztjldM1Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570698fa51.mp4?token=IpgU893m_BC0KfW6z322U0Ftwc-1qy7JYaeDl8PqakwNcDjr_stznnk80xyzlCOsNh2cni9hZSzLpXyP4Qfv8kRrE__tZT8PlewYYEiqNh0Zv7al73kS0QISJY_uub7HqKz3WOMBWh_qAQ0l0WA9c-R_bGS0U1Gbh-r3ddh8vYTwamUxH5MNvhCoHDodvVckgcsvsVY8OX87iGtSZXH95XLPhaHhzjcxFfnLnJ-whDAKmaFzI0o7aiLJUU0H_I8NhowgQwo7LLRaKC1QNn9Hj8gJyoe0bsEz9zRKxxLCKf5uW1JKjhHocuWV5vo_csEYYl1Hek3ac4nIhztjldM1Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حرکت بدون مزاحمت ۲ موشک‌ ایرانی در آسمان اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686351" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686350">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=a2PXNQi9mqCHOXhSqv2Ndm4Gb_Ski45V4lCAaFAElZtpaU2Rh_Nqyu9plz06kvTxNA8ZC28W15DqHqVy1bclmueyAsdqxCJGa1F9PUh5eIDokNrAxxOB5s_cND2Nit1rPtfB2LIPXw8YSH7A8hZuCC9584m1IHqtURuSpn78zGk3P6GO4p7I5W4yxqdWmkOsXtKMoDawKe6rOEcGZcJlGjIvpZvp_p6d9-vw4uXQ_yF3u5jTcTlHty5ZdGzBR2Mmi0DBTVAXjAVzPiS-gFXFKf2bHSkZWc-WWBhdKihnilXPoGwRb7lLKP2Tq0yeUh3shdOjIh_obnNEwRLt4ZLPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=a2PXNQi9mqCHOXhSqv2Ndm4Gb_Ski45V4lCAaFAElZtpaU2Rh_Nqyu9plz06kvTxNA8ZC28W15DqHqVy1bclmueyAsdqxCJGa1F9PUh5eIDokNrAxxOB5s_cND2Nit1rPtfB2LIPXw8YSH7A8hZuCC9584m1IHqtURuSpn78zGk3P6GO4p7I5W4yxqdWmkOsXtKMoDawKe6rOEcGZcJlGjIvpZvp_p6d9-vw4uXQ_yF3u5jTcTlHty5ZdGzBR2Mmi0DBTVAXjAVzPiS-gFXFKf2bHSkZWc-WWBhdKihnilXPoGwRb7lLKP2Tq0yeUh3shdOjIh_obnNEwRLt4ZLPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌هایی که از ایران به سمت پایگاه‌های آمریکایی شلیک می‌شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686350" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686349">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686349" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686348">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حملهٔ موشکی آمریکا به اطراف شهر اهواز
معاون امنیتی استانداری خوزستان:
🔹
نقطه‌ای در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686348" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686347" target="_blank">📅 23:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686346" target="_blank">📅 23:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55155e2342.mp4?token=u4wDBl8EzFSGkY9Aa8h_gEispgj-oPpOE-sA6Dd0VOfdvqZZUbCTx0FJNk3_Q-ECOluJN_debDQF8yYaHdLiD8YJja7p4XDoRTTEinN17HelnHVk7K2Xcp8rlEwD-oiHkIQRWhqO03gliAdrvcofIXhqho_zZgDPlNCb56nEsRtAK6EZ7tIhxbP5qe6ZFKbhjiYImazSsPqtqnassOgAVJzyF7t4X6jKAXDlr8KH64hyfMl9dpawjifMi3vOOL4pvIBQleselpnYp-HhnBgXQetZY72dBwO5_YQ0EP1kTDRcQEcDPi80hAt-xEsvQygqkz1YKXhYk_tnLuWzGOTSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55155e2342.mp4?token=u4wDBl8EzFSGkY9Aa8h_gEispgj-oPpOE-sA6Dd0VOfdvqZZUbCTx0FJNk3_Q-ECOluJN_debDQF8yYaHdLiD8YJja7p4XDoRTTEinN17HelnHVk7K2Xcp8rlEwD-oiHkIQRWhqO03gliAdrvcofIXhqho_zZgDPlNCb56nEsRtAK6EZ7tIhxbP5qe6ZFKbhjiYImazSsPqtqnassOgAVJzyF7t4X6jKAXDlr8KH64hyfMl9dpawjifMi3vOOL4pvIBQleselpnYp-HhnBgXQetZY72dBwO5_YQ0EP1kTDRcQEcDPi80hAt-xEsvQygqkz1YKXhYk_tnLuWzGOTSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.   #اخبار_مرکزی در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686345" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آمریکا پیش از انجام عملیات جدید، کشورهای حاشیه خلیج فارس را در جریان قرار داد
🔹
رئیس‌جمهور جنایتکار آمریکا در مصاحبه با فاکس‌نیوز گفت که متحدان آمریکا در خلیج‌فارس پیش از انجام عملیات جدید، از برگزاری عملیات جدید علیه ایران مطلع شده بودند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686344" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
بانک مرکزی آمادگی عرضه تا ۲ میلیارد دلار در بازار را دارد
🔹
بانک مرکزی با استفاده از ذخایری که در پی تغییر سیاست ارزی در دی ماه سال گذشته در اختیار دارد شروع به عرضه گسترده ارز در بازار کرده است.
🔹
به گفته مسئولان این بانک، میزان ذخایر از این محل بالغ بر چند میلیارد دلار است و رئیس کل بانک مرکزی امروز از آمادگی این بانک برای عرضه تا ۲ میلیارد دلار به صورت اسکناس در بازار ارز خبر داده است.
🔹
این اقدام بانک مرکزی برای جلوگیری از اقدامات سوداگرانه کانال‌های تلگرامی و اعلام نرخ‌های غیرواقعی برای دلار صورت می‌گیرد؛ نرخ‌هایی متفاوت که هر کانال تلگرامی برای خود اعلام می‌کند و اختلاف قیمت اعلامی هر کانال با دیگری به بیش از چند هزار تومان می‌رسد.
🔹
پیشتر و در مرحله اول، بانک مرکزی با عرضه ۵۰۰ میلیون دلار برای تامین نیازهای ضروری اقدام کرد که از این میزان صرفاً ۲۰ میلیون دلار آن فروش رفت.
🔹
در این خصوص، بانک مرکزی اعلام کرده هر شخص حقیقی می‌تواند تا سقف معادل ۱۰۰۰ یورو برای تامین نیازهای ضروری خود از بانک‌ها و صرافی‌ها اسکناس ارز خرید کند همچنین اشخاص حقوقی نیز می‌توانند تا سقف ۵۰۰۰ یورو اقدام به خرید کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/686343" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرهایی درباره شنیده شدن صدای انفجار در اربیل
🔹
پس از اینکه برخی منابع از حملات موشکی جمهوری اسلامی ایران به مواضع آمریکا خبر دادند، منابع عراقی از شنیده شدن صدای چند انفجار در شمال این کشور خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686342" target="_blank">📅 22:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
وضعیت استان هرمزگان کاملاً پایدار است
معاون امنیتی استانداری هرمزگان:
🔹
در ساعات ابتدایی کانون عمده صداها ناشی از تنش‌ها و درگیری‌های رخ‌داده در پهنه آبی خلیج‌فارس و محدوده تنگه هرمز بود.
🔹
با تشدید درگیری‌ها طی ساعات اخیر، مناطقی از نوار ساحلی استان هرمزگان هدف تحرکات و حملات دشمن قرار گرفت
🔹
جزئیات دقیق آن از سوی مراجع ذی‌صلاح در حال بررسی و پایش تکمیلی است.
🔹
در حال حاضر شرایط در تمامی شهرستان‌ها و مناطق مختلف استان هرمزگان کاملاً پایدار، آرام و تحت رصد است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686341" target="_blank">📅 22:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
یک مراسم عروسی در سیریک هدف ترکش های حمله وحشیانه دشمن آمریکایی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686340" target="_blank">📅 22:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezpZFiZLo2t3ZiXUsrGHiE2XPgXRW5VuNliC0DJ5O-Xmx2WrdpSlNx_3VwWq31nSXVnxrMYc3ZQzCasENwOa8ZhJFm7laYuX0YmqQ78T6UkfAil6YphswB_2ojMzk_Yu1E7ZKRi0Aj61zsR-GLg8lxCklOklsz_W6UrNUbjAGZVa1NTz7s9_POgK8KhvNmqx50bDWMtUjAYxnQZgEIcJMPzLUAl3SgBirzWWaAu8Rd9ngR2VBj_ELlOlH02SmAIX6G01UqEzayQ_YDaJiUcHayHsGRekpSkvAPcXCluvwLuliCID977uSpeYOYREEJ215TL2x05tayk__Fpp_2VELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران انقلاب اسلامی: تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/686339" target="_blank">📅 22:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgBEA2mV9uLfDZ4_ASe4iRugcEW9jiyFyY7by8CsMekYWzSVe3w6vzM8_QK_qSWd3be7gcUYwVsFQrFnpUKmUAaNxEdns94Gqe8qtGsGEkoFcNo6BYGnRuMjhzAuzW8XORR9nC_oa0KLCB_ObCncegH_TFGvus30wklwK3he2ZzvRsD5E1BjkQFuHE33oiypU59TTWvI_nez3VCanbqXKxQTZclVO3ZtM7dXWJBJX7gJ56jErCotxTSDRwGkflI3_zN7c_QivEdzjlYDgmKo3bSS9WfDmuG_XZtPbqCq3JUum1YwiLlyFewDHAdiSbL8vASN8yH_UTBtmFVxSDXgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در بغداد: هرگونه حمله با سرنوشت «اصحاب فیل» پاسخ داده می‌شود
سفارت جمهوری اسلامی ایران در عراق با انتشار پیامی در شبکه اجتماعی ایکس:
🔹
ایران هرگز مرعوب تهدیدات و لفاظی‌های دشمنان نخواهد شد.
🔹
هرگونه تعرض به خاک و امنیت جمهوری اسلامی، با پاسخی عبرت‌آموز و سخت همچون سرنوشت «اصحاب فیل»  روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/686337" target="_blank">📅 22:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.   #اخبار_مرکزی در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686336" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هم اکنون؛ شنیده شدن دوباره صدای انفجار در چابهار/ صداوسیما
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/686335" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تکذیب حملات دشمن به «جم»، «کنگان» و «لنگرود»
🔹
شبکه‌های اجتماعی از وقوع انفجار در ۳ شهرستان «جم»، «کنگان» و «لنگرود» خبر دادند که مقام‌های استانی اصابت هرگونه پرتابه و حمله دشمن آمریکایی را به این نقاط تکذیب کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/686334" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686333">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
بلومبرگ: ترامپ عملاً با بی‌اعتنایی جهان روبه‌رو شده است، چین عقب ننشسته، برخی ارتباطات بانکی ایران در امارات ادامه دارد و پروازها و تجارت با چند کشور برقرار مانده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/686333" target="_blank">📅 22:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686332">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/686332" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686331">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/686331" target="_blank">📅 22:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686330">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
یک مراسم عروسی در سیریک هدف ترکش های حمله وحشیانه دشمن آمریکایی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/686330" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686329">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
دقایقی پیش حمله دشمن آمریکایی به فرودگاه جیرفت
🔹
اطلاعات تکمیلی منتشر می‌شود  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/686329" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686328">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
استانداری هرمزگان:
🔹
دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان منطقهٔ مسکونی کوهستک را مورد حمله قرار داد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/686328" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686327">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686327" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
