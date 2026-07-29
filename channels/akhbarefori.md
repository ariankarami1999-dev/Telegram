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
<img src="https://cdn4.telesco.pe/file/dabobywK6JZYNhfYNRlQ1cviccLjfC2NQVQQOaI0Z4NZWE7DuWQ4Lq4_oFXEvycRg02-3T2k1yxuqI0UprOLScTa-W6MHS5mcpVmGP9yZW8H3zv2LmV4ChmbPGUeBY47vDwVJfEEmeAKAOjRAq1dOQR-ZQlhdZWQ6jz3rCdZrGAauob5MIcdz6u59dOBfNsGCUNZRSPoHKbrJ3iZToo1nAfISH4ESIttcPyNXh5A8XSFlwFpfUAN5tz4JcdZSs54-jh4AAnuhWpglwVzlqDX5uKMO-lQcsWALvwwMlIWvpPuvxksyJ4hd_7cjL-KZbd4yUizdS-NoBstsTmvmWczpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-676375">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f22a9d150.mp4?token=Wq3srqHJmLA7qNjjIdIQ4mLxDaaF82-l561Ss9UNQ1IvKc0iYaBFOddbNpQBZuaSw1dZq78HUxd59en0v2cc4bBLngA-qUFRrXPT4SxnRrqizp-2BaTsGZIfRG3SaFGhb-jwjjAYRdYdR9NGUlAVOuybEB9Fwae-X-DoLGf0ZUWOpoixea6p5NvkvQqkPl7-1c3Y1sec_sk9WfJYJNyzDIhtL2OVOOKgpAcX6PeCRMhvDQTUYKGq3gFSFJimu-PRY-UtJVja35pCZLtbDRr2UfVC3SxVaHEoMRSvjw0wFWKz0s6Tzsa75pc9XgMHfEKCsGL7EVNRNZWttiZ1M9Zh0kqZemE_WSIYSYctDzofbI20PEer_Go_zDJj_xaLEUW0GqMhFXCDojuVb7TgHIFeoGefXTQfLHGH1ewromv2z3G_FeKZUglKldhys2xyrls8gnhsDUfR52_uuF7l0wIMwIF_s8uYAvW6VAChiAjfR8Sdp6u63qjQdQcUeMDmTzmwuzUyZUqwzidXaT5O4Rdlxk4I2qMfGMqGAln4NyMUgSg3ppQji6_tBGaUV1bj-__3mQGcitMK1eheQ93AlRFkcxaEBU04Iz07FJsQjG2pop77mPr6gkUinbz7PRhyYuovweAoksUpmfkoHBYvfTMci-043OeQczUfExi3LFi2gxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f22a9d150.mp4?token=Wq3srqHJmLA7qNjjIdIQ4mLxDaaF82-l561Ss9UNQ1IvKc0iYaBFOddbNpQBZuaSw1dZq78HUxd59en0v2cc4bBLngA-qUFRrXPT4SxnRrqizp-2BaTsGZIfRG3SaFGhb-jwjjAYRdYdR9NGUlAVOuybEB9Fwae-X-DoLGf0ZUWOpoixea6p5NvkvQqkPl7-1c3Y1sec_sk9WfJYJNyzDIhtL2OVOOKgpAcX6PeCRMhvDQTUYKGq3gFSFJimu-PRY-UtJVja35pCZLtbDRr2UfVC3SxVaHEoMRSvjw0wFWKz0s6Tzsa75pc9XgMHfEKCsGL7EVNRNZWttiZ1M9Zh0kqZemE_WSIYSYctDzofbI20PEer_Go_zDJj_xaLEUW0GqMhFXCDojuVb7TgHIFeoGefXTQfLHGH1ewromv2z3G_FeKZUglKldhys2xyrls8gnhsDUfR52_uuF7l0wIMwIF_s8uYAvW6VAChiAjfR8Sdp6u63qjQdQcUeMDmTzmwuzUyZUqwzidXaT5O4Rdlxk4I2qMfGMqGAln4NyMUgSg3ppQji6_tBGaUV1bj-__3mQGcitMK1eheQ93AlRFkcxaEBU04Iz07FJsQjG2pop77mPr6gkUinbz7PRhyYuovweAoksUpmfkoHBYvfTMci-043OeQczUfExi3LFi2gxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی صدری‌نیا ، مستندساز و فعال رسانه‌ای: شهید لاریجانی روایت می‌کرد که برخی حکام عرب متوجه شده‌اند که آمریکا و اسرائیل خیر آن‌ها را نمی‌خواهند اما چون در مدلی از رفاه زندگی می‌کنند نمی‌توانند پای حق بمانند و مقاومت کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/akhbarefori/676375" target="_blank">📅 16:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676374">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh7DgAxtnPqCQFJdplT2mlSU4SAEsXJwpIy1P_-em4o-ZSrG3lwlWB2KidqCQBCvIhYKEH1ombiRrpKuX2Hkehl6kevrOzUgSCxXlua9-30Lr0qzZ2RP-9Hhqc6KFLfJaN6_j4HCmKLas9eSWPAPvm6iS8WxL-BIbTB1tuJ0IoMKnkdmbPguM3uWiRWXVWlYQXccqNJ8Jna397D2QwS_mhOEgFWOnvcRn13X3ATpbiOtez2Xtm0FUqGWkd_3gea7pyv7qY86AiWUhd2JAFwM_zQDEjDbrdwxdLdktF4sfn4O0JShOc4QuiF5wI0Pmdwii3FFK_rPDfeDUGDuift-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس حملات امروز ایران به اهداف آمریکایی قیمت نفت حدود ۶ درصد گران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/676374" target="_blank">📅 16:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676373">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc53bc3b80.mp4?token=m99VLmYAWHmxKEV-IYvg2hghodiVniNkhTmYUN7j2NaucIW56K34CF-86JjPkSuUwk0y81oNu5WMgTJ435tpWZhBZ8aAl-HIK-3QpyHMboPqlEptzCV74OstNUJtAcPF4S4JjLvuKqDts8gmNZrHf2_0R1BS0LWZ4exNtKS_JmB7gnQb6A7L_F685uUywLp01iZttfKUVVqv5FqVPDHALMmlBu4_b9RCZ7KGcLSuxzOKAhoBcLt2HmibkH77FgY_NWMNztFKzXGvvBbfPokJtVTXZo8R3b19L_jK4Uh1p1Vy0QPdi-T0vAZGyQ2eHOQM2BQ6NoBuoCzrVCihH5U9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc53bc3b80.mp4?token=m99VLmYAWHmxKEV-IYvg2hghodiVniNkhTmYUN7j2NaucIW56K34CF-86JjPkSuUwk0y81oNu5WMgTJ435tpWZhBZ8aAl-HIK-3QpyHMboPqlEptzCV74OstNUJtAcPF4S4JjLvuKqDts8gmNZrHf2_0R1BS0LWZ4exNtKS_JmB7gnQb6A7L_F685uUywLp01iZttfKUVVqv5FqVPDHALMmlBu4_b9RCZ7KGcLSuxzOKAhoBcLt2HmibkH77FgY_NWMNztFKzXGvvBbfPokJtVTXZo8R3b19L_jK4Uh1p1Vy0QPdi-T0vAZGyQ2eHOQM2BQ6NoBuoCzrVCihH5U9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معلم ایرانی که ضربه آزادش از روبرتو کارلوس هم عبور کرد؛ حالا پیج ۴۳۳ دنبالش کرده
🇮🇷
🔹
پیج ۴۳۳ یکی از بزرگترین و پر‌مخاطب‌ترین صفحات فوتبالی جهان در اینستاگرام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/676373" target="_blank">📅 16:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676372">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ترامپ اعتراف کرد که جنگ با ایران محبوب نیست
ادعای هاف‌پست:
🔹
کیلمید مجری مشهور فاکس‌نیوز در یک پادکست اعتراف کرد که دونالد ترامپ، کاملاً از عدم محبوبیت جنگ  علیه ایران آگاه است.
♦️
رئیس جمهور گفته است که سایر کشورهای خلیج فارس «در حال حاضر از یک حمله بزرگ هیجان‌زده نیستند.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/676372" target="_blank">📅 16:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676371">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای خوک هار: حمله ایران به اردن غافلگیرکننده بود، نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را ساقط کنند
🔹
در پاسخ به حمله غافلگیرکننده شب گذشته در اردن، حملات آمریکا علیه ایران انجام خواهد شد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/676371" target="_blank">📅 16:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676370">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای سگ زرد در مورد تجاوز به عراق: حملات آمریکا و عربستان سعودی با هماهنگی دولت عراق انجام شد
🔹
من در نظر دارم اخطارهای جدی‌تری را علیه نیروهای نیابتی ایرانی مطرح کنم  #DEVIL
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/676370" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676369">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c7a42a18.mp4?token=IaTbDU1Fo0sR4Dqq4mgdDCGeP7oV7mmBElQ4QDCKrwbNxj1qLkH5xe_olY1ND_i5aVMVY_RwYejcEnMfcb8TKKsdJrvx3Yb2juCyLlENMUTwLAqYpeJmFDm-6UfkNIfUYJmeaxUX8K2dLJWnXdZZ7s8qL76LzF0AlnkRxqhw6JKFWmV66eOcNSVAfu34Dr24wlpDnzKMmu7I3Kcr6BAiwM5ryxFTiICCEIpdvxv1TN8cZbOZKxsXv7g1Qv-RfINXO0Al9vzhDpu0jLwP4FR3yipkd5lQ2SWdoik4uwE1PgdB8hyxEkREiaFgVFLDeWa-1rBMdASLXltiKm67X-IPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c7a42a18.mp4?token=IaTbDU1Fo0sR4Dqq4mgdDCGeP7oV7mmBElQ4QDCKrwbNxj1qLkH5xe_olY1ND_i5aVMVY_RwYejcEnMfcb8TKKsdJrvx3Yb2juCyLlENMUTwLAqYpeJmFDm-6UfkNIfUYJmeaxUX8K2dLJWnXdZZ7s8qL76LzF0AlnkRxqhw6JKFWmV66eOcNSVAfu34Dr24wlpDnzKMmu7I3Kcr6BAiwM5ryxFTiICCEIpdvxv1TN8cZbOZKxsXv7g1Qv-RfINXO0Al9vzhDpu0jLwP4FR3yipkd5lQ2SWdoik4uwE1PgdB8hyxEkREiaFgVFLDeWa-1rBMdASLXltiKm67X-IPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا وام گرفتن برای یه نفر باعث ثروتمند شدنه‌، ولی همون وام برای یه نفر دیگه شروع بدبختیه؟
🤔
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/676369" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676368">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای خوک نجس: حملاتی به ایران انجام خواهد شد و ضربه محکمی به آن خواهیم زد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/676368" target="_blank">📅 15:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676367">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای خوک نجس: حملاتی به ایران انجام خواهد شد و ضربه محکمی به آن خواهیم زد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/676367" target="_blank">📅 15:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de24473e3.mp4?token=V6vVKWETm75T6KnA-MaTW5UhZHC1-6lfKaZ1sXdGKUoh1Zm938w3OGJGUcKdaFHXyywgB9iy5GVBGexNzajuZvyeBoqXhBsOYNlXN8s--d7m2IwOimv5bbw_ocVk0isIH2hdc0uq7EwwjrUhijK-EnPobHuFhztPaDgfULybiix-p-UcNZXtwyQu-6gPtIWRk1lgs7Wdys9YHI1DRqDeZcp-TZCChe0iXOQoVX5ia5SIgn6gYmOjNDjOqdLlHLqdGT5RosRKL753aXiY_YDqzOBSgA7G59HoyoMVdHqf11QYBdBuzfk9csxQSlIuAR1umHWFbqmWcFHFs7AoYp9clw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de24473e3.mp4?token=V6vVKWETm75T6KnA-MaTW5UhZHC1-6lfKaZ1sXdGKUoh1Zm938w3OGJGUcKdaFHXyywgB9iy5GVBGexNzajuZvyeBoqXhBsOYNlXN8s--d7m2IwOimv5bbw_ocVk0isIH2hdc0uq7EwwjrUhijK-EnPobHuFhztPaDgfULybiix-p-UcNZXtwyQu-6gPtIWRk1lgs7Wdys9YHI1DRqDeZcp-TZCChe0iXOQoVX5ia5SIgn6gYmOjNDjOqdLlHLqdGT5RosRKL753aXiY_YDqzOBSgA7G59HoyoMVdHqf11QYBdBuzfk9csxQSlIuAR1umHWFbqmWcFHFs7AoYp9clw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«قصه‌های جزیره» تا امروز؛ گذر ۳۰ سال بر چهره بازیگران این سریال محبوب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/676366" target="_blank">📅 15:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ریاست جمهوری عراق: حمله به مقرهای حشد شعبی، نقض آشکار حاکمیت است.
🔹
توصیه ستاد اربعین: زائران برای خروج، مرزهای باشماق و تمرچین را انتخاب کنند.
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: طرح دوفوریتی برای مقابله با ماینرهای غیرمجاز تدوین و بارگذاری شده.
🔹
استانداری قم: ساعت کاری دستگاه‌های اجرایی استان از روز شنبه ١٠ مرداد تا اطلاع ثانوی از ۷ تا ١٣ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/676365" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw2G2Riu-bEzS17yWXqY7hXWRGWGUGONrqE_1swLneO-4wYyB3dppNufUg9I9gym-BjCwTmNZR2F9gQCWqTijUZ40ydqKh02GZ_H-cFUBxrtX34mwT70TVTgD_QimkxndcsLQh9J0RkiUP0SE-WxmdsxMCYHSOR3jdzfTjbCCyvszpZtvfKGMOw7IL0V_L3wz0xBD2pbKfbYMRZQ2fOUQIi123u39U4s9L9jGr34F42jH7w4Hw-iXBVxp3idml-RenS1uii3uTp7nxgREhTIzHcgQ10aUJ2kcTFyJltzy8xcxekHoitHfI5C4H-5yZPtN6WLQg4BGx5ENRxZ3p46pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش پژمان (شرکت‌کننده برنامه عشق ابدی) بعد پخش برنامه‌اش در خط قرمز: من حرفم را از روی احساس لحظه‌ای نزدم؛ از روی باوری گفتم که سال‌ها به آن رسیده‌ام/ من به ایستادگی احترام می‌گذارم؛ به کسی که تا آخرین لحظه کشورش را ترک نکرد، مسئولیتش را رها نکرد و در همان مسیری که انتخاب کرده بود جانش را از دست داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/676364" target="_blank">📅 15:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4bf76e75.mp4?token=qRjBIL90Kl3rTZI6cu5S8q3RyvBpFDXe8-EM1uw16HbTrPHGaFCHEMRhmVeT5V6Z12OpVdeYKoi1sEUkr3s7q9ZltLbTMKQvG3GKZW_CgaS-I71qUUlmjL1mzjLfFSb9-uVQLeSPJwUDwkhtgYV51l8BGqvLPv7YkOIgwRzmvHgmyxkaTGITooZNDnQZHvUEvSefh5t90kdNxrNxAFdWUq_hy3yBo255-tjRW-uQSt2yf2fGkbsmt-6-8MG162lBr59Q7GRV3vHj49xwJkSe0zvtqzjZfaprB-1vHremE-Bo3zmLBkLZuX0rFPG6ZtWpo1wxC-mFP3HIzhoEOPuzWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4bf76e75.mp4?token=qRjBIL90Kl3rTZI6cu5S8q3RyvBpFDXe8-EM1uw16HbTrPHGaFCHEMRhmVeT5V6Z12OpVdeYKoi1sEUkr3s7q9ZltLbTMKQvG3GKZW_CgaS-I71qUUlmjL1mzjLfFSb9-uVQLeSPJwUDwkhtgYV51l8BGqvLPv7YkOIgwRzmvHgmyxkaTGITooZNDnQZHvUEvSefh5t90kdNxrNxAFdWUq_hy3yBo255-tjRW-uQSt2yf2fGkbsmt-6-8MG162lBr59Q7GRV3vHj49xwJkSe0zvtqzjZfaprB-1vHremE-Bo3zmLBkLZuX0rFPG6ZtWpo1wxC-mFP3HIzhoEOPuzWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ‌تمام گواردیولا برای کودکان فلسطینی
🔹
پپ گواردیولا، سرمربی اسپانیایی و حامی مردم غزه، ۲۸ کودک فلسطینی را به کمپ تابستانی خود در شهر ریالپ اسپانیا دعوت کرد تا چند روزی را در فضایی امن سپری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/676363" target="_blank">📅 15:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlQHDUo2necFHrR0_nFYtvKwFOvfwmwk0dvd7yaPreP1KKbEvJuWqnUT1T2igYIVoUzUV7yfPv1Lcgf6kr5v6CY5culZsudGxgmP1UEyxyq3VTvvq4SaeiZ9VBZ5WK_KbGKg0JcJxkd4kI1ozGXYudLFZIRE0jZvaQtMkfVopWdHlxdu7kbyYyPt-guS9m_QchtLCjxaWSqhfMiCJxDj1GRXV9WPcY73i2Iqsy_n6JlJMr-sbgNrKE462hFjq1O81NAahN2SXUWOOcyKbK2nDOzw-JJkHbUb8bsKoDAh-YbdyAWyeacqgZMfc_Sd4jhXP-dWDcrjF8xtSEM3LJZOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
گاها یک همراهی کوچک می‌تواند نام ما را در سیاحه خادمین اربعین حسینی قرار دهد
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676362" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هراس آمریکا از ایران؛ سنتکام: تلفن‌های همراه را کنار بگذارید
🔹
سنتکام به نیروهای آمریکایی هشدار داد انتشار ویدئوهای تلفن همراه می‌تواند به ایران در هدف‌گیری پایگاه‌های آمریکا کمک کند.
🔹
رویترز گزارش داد احتمال دارد به نیروهای آمریکایی در منطقه دستور تحویل تلفن‌های همراه داده شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676361" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afda39a823.mp4?token=Vd8bKVtoo5T3glz8oMElOdH6BaI9-S21TE4GOr0pcT_QhrVrrF8KfV2e9ZXxNc80eSlfhCBoEcnSuZ96tTI7rqIRaJhW_bCZpjE3_BbOW5Lutn5AKa_zjqVhEZtGL942Ce2ereNFrVbgMwemdv4sTjb77--eSY60uho1khnrNEyf0MxAKPhS_U4TgyfUCCucHnAh8v0SqZpkxi5VghrgTCrZAm_96xOwqRhRTQEnn5Ctpfx4zjwpJUgGFgG0eLtDuXwkuRWFV9tyWi4aXBm3RlLFSS3oXp43titl5CFAw0s-9bv31rZDbjXc7IK4YJiNlqYOuYUiatos8tznz1-VOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afda39a823.mp4?token=Vd8bKVtoo5T3glz8oMElOdH6BaI9-S21TE4GOr0pcT_QhrVrrF8KfV2e9ZXxNc80eSlfhCBoEcnSuZ96tTI7rqIRaJhW_bCZpjE3_BbOW5Lutn5AKa_zjqVhEZtGL942Ce2ereNFrVbgMwemdv4sTjb77--eSY60uho1khnrNEyf0MxAKPhS_U4TgyfUCCucHnAh8v0SqZpkxi5VghrgTCrZAm_96xOwqRhRTQEnn5Ctpfx4zjwpJUgGFgG0eLtDuXwkuRWFV9tyWi4aXBm3RlLFSS3oXp43titl5CFAw0s-9bv31rZDbjXc7IK4YJiNlqYOuYUiatos8tznz1-VOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چشمان بسته ترامپ در مراسم خاکسپاری گراهام خبرساز شد
🔹
تصاویر ترامپ با چشمان بسته در مراسم خاکسپاری سناتور «گراهام»، واکنش‌هایی را در شبکه‌های اجتماعی به دنبال داشت.
🔹
برخی کاربران با اشاره به سابقه انتقادهای ترامپ از جو بایدن به دلیل چرت‌زدن در مراسم عمومی، این تصاویر را دستمایه شوخی و مقایسه قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/676360" target="_blank">📅 15:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdbfc3d69.mp4?token=No46L8FJhmyIZ16GBHI0Bmee5FARo_etBuxeo0ft3ikKAxTInEUfPDo2EBl7-riJrHT7taFu6qDQiBvyGQiE-9_Q0n92NSaZ8eisPkhf7Qs1QjODh5fneqNZeNuVu5RDWBonFaydjiCwm6a8BJq7N8EQa9aLhJtwYPUO2XeUMniytq5ekm3VPKEO1NYPDhxrvs0LUtB4NbxuqcOlIZKn7kKYSCPsAzZKjELNvftgyN9DA4Ipo58AFMjJz-VdwD9geRxwVIj-bR4PpHXRVjxEI1Stm9vk4UE3vumNGhWGWZJAkryjHYiBo3Hg-WXWJvEEKr0ALtpc5lAFRg3Hl-6PXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdbfc3d69.mp4?token=No46L8FJhmyIZ16GBHI0Bmee5FARo_etBuxeo0ft3ikKAxTInEUfPDo2EBl7-riJrHT7taFu6qDQiBvyGQiE-9_Q0n92NSaZ8eisPkhf7Qs1QjODh5fneqNZeNuVu5RDWBonFaydjiCwm6a8BJq7N8EQa9aLhJtwYPUO2XeUMniytq5ekm3VPKEO1NYPDhxrvs0LUtB4NbxuqcOlIZKn7kKYSCPsAzZKjELNvftgyN9DA4Ipo58AFMjJz-VdwD9geRxwVIj-bR4PpHXRVjxEI1Stm9vk4UE3vumNGhWGWZJAkryjHYiBo3Hg-WXWJvEEKr0ALtpc5lAFRg3Hl-6PXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت علی صدری‌نیا، مستندساز و فعال رسانه‌ای از آخرین حضور شهید لاریجانی در مراسم اربعین در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/676359" target="_blank">📅 15:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bdd9158f.mp4?token=QorPa-qReztJ0r3dn-EiMb4jRoFbPBnrHDp-UkuNCT7aLGxxrJTalAuXpfqq_SVcx5letTfv5T8A-MvTNry4gM-mfGjvxrCnvGrNxDmaSr7hMJ37sDJr2JTalCyMv5UdC1UIBTpm9vihIeuTCLrSuX-v9JgBwearUM2A0AqbV7JVOwHjWdCoGwyxSt87v0mYnWLtrIrI_6QR0vQf51Kqj7h_aneXpWoerffp39aDCeTT9umPd2tx0cKlgf8be3gQ_6c6Ib_fWbfyVIUHJFvK8n95ccijVeX-lTigHqZLvxrg8veTYlURjm2nKhruINiOJHLVIMOO1f1Z_RmM-QwkWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bdd9158f.mp4?token=QorPa-qReztJ0r3dn-EiMb4jRoFbPBnrHDp-UkuNCT7aLGxxrJTalAuXpfqq_SVcx5letTfv5T8A-MvTNry4gM-mfGjvxrCnvGrNxDmaSr7hMJ37sDJr2JTalCyMv5UdC1UIBTpm9vihIeuTCLrSuX-v9JgBwearUM2A0AqbV7JVOwHjWdCoGwyxSt87v0mYnWLtrIrI_6QR0vQf51Kqj7h_aneXpWoerffp39aDCeTT9umPd2tx0cKlgf8be3gQ_6c6Ib_fWbfyVIUHJFvK8n95ccijVeX-lTigHqZLvxrg8veTYlURjm2nKhruINiOJHLVIMOO1f1Z_RmM-QwkWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احسان علیخانی با انتشار این ویدیو: ما یکی از ستون‌های خاطرات‌مان را از دست دادیم. ممنون برای تمام خنده‌ها…
🔹
خداحافظ عمو اکبر، خداحافظ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/676358" target="_blank">📅 15:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95677ca598.mp4?token=TwiohbXo2Gzhm_NvLsaM_RukrXbJQNQj8TwVpxzhEwb0cczBO4vwQA_Tf6f3MEwyGAipDPRj_qm7lIUbKWESBlPb9m6XRj5Vlbms-slLoOlcXKsvTcl3ebbsfRhswTEFYaJpDAk0e_uoeiycLjpnXXLVl9fbJwcXHRu346QmzvvHYtCKOzM0E02I25ZMLbZJrqa9c1VxWYGwKpcYUTs_DcfXERuFKWZm-dYuIYjQlONhf1lzGDl7dVPqT14aAO6tqXZEVOVyt-FEKgfhwMO-zSPU0fNZJ7FmiOzm1kcg46pINtS99DeYj71odz6VjzirntmoW0Gah7bXhgzZB1y7Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95677ca598.mp4?token=TwiohbXo2Gzhm_NvLsaM_RukrXbJQNQj8TwVpxzhEwb0cczBO4vwQA_Tf6f3MEwyGAipDPRj_qm7lIUbKWESBlPb9m6XRj5Vlbms-slLoOlcXKsvTcl3ebbsfRhswTEFYaJpDAk0e_uoeiycLjpnXXLVl9fbJwcXHRu346QmzvvHYtCKOzM0E02I25ZMLbZJrqa9c1VxWYGwKpcYUTs_DcfXERuFKWZm-dYuIYjQlONhf1lzGDl7dVPqT14aAO6tqXZEVOVyt-FEKgfhwMO-zSPU0fNZJ7FmiOzm1kcg46pINtS99DeYj71odz6VjzirntmoW0Gah7bXhgzZB1y7Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
📍
تهران
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
یا عدد 4 را به سامانه پیامکی
3000909030
ارسال کنید.
📲</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/676357" target="_blank">📅 15:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e8974532.mp4?token=mASrIAHG8f371s5a3L86Bs-kfRzihEKGp6Eosg6FMbkHVMcaPh47Ko4KjGkFAD5cSoB5sW2pZ2apD9YYlcwlsMXsXOmJVr7t17JGNXzJkd5DSWHu8_ma21fX5-Y2pLGfmMq9ir-vMPYMd0lQpvnQgr5SuOsbioJBJUNpl7uVOmsi6sDMP-DESQgB8fW31GMsGTcyKWyv4cKtGpRwtUVNHjdIvyZpK-Tj198C6_NpoYsqxVweWf9FHloi1NF74ux3InZCVQwM-m8WsxkD3V8rAa5LXHBd6RFnVDmARTd4CEE7sg-CYj4FBEQ-RVbnu3aLVPCAISM9o92QsE-xayHkYhYXRjOWaCcMYO_8VgJXL5Unp-ES17_HagLdsdGp4MKTX4J9uhb9UI2gL_8a5r0NN1-XoztFSqrNTeviDdtNpx09uLXEz13Yp0esKaQBvaTa-RoUuA1-bw1Exgl_H855Oea64cnlfJXRb69zmq_uLq_KVSY42QG9dpJ6n2wYkd1neWdEbY-Z2yCpdqTDN-chmRTCCEhP-ysBTY-dgiI_PqN-HfyTQ7yKLEBOaQxr0AORkDsj_aFbczGX1Qr8Mcdu3n1FM_scXQ7CZRyOxNdd7ghBQ94r4gtX4jqLa-d7Gt89sa3TJWDUosOyrwmiPgaqtXFegyJim1-RwsmbhFxcuRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e8974532.mp4?token=mASrIAHG8f371s5a3L86Bs-kfRzihEKGp6Eosg6FMbkHVMcaPh47Ko4KjGkFAD5cSoB5sW2pZ2apD9YYlcwlsMXsXOmJVr7t17JGNXzJkd5DSWHu8_ma21fX5-Y2pLGfmMq9ir-vMPYMd0lQpvnQgr5SuOsbioJBJUNpl7uVOmsi6sDMP-DESQgB8fW31GMsGTcyKWyv4cKtGpRwtUVNHjdIvyZpK-Tj198C6_NpoYsqxVweWf9FHloi1NF74ux3InZCVQwM-m8WsxkD3V8rAa5LXHBd6RFnVDmARTd4CEE7sg-CYj4FBEQ-RVbnu3aLVPCAISM9o92QsE-xayHkYhYXRjOWaCcMYO_8VgJXL5Unp-ES17_HagLdsdGp4MKTX4J9uhb9UI2gL_8a5r0NN1-XoztFSqrNTeviDdtNpx09uLXEz13Yp0esKaQBvaTa-RoUuA1-bw1Exgl_H855Oea64cnlfJXRb69zmq_uLq_KVSY42QG9dpJ6n2wYkd1neWdEbY-Z2yCpdqTDN-chmRTCCEhP-ysBTY-dgiI_PqN-HfyTQ7yKLEBOaQxr0AORkDsj_aFbczGX1Qr8Mcdu3n1FM_scXQ7CZRyOxNdd7ghBQ94r4gtX4jqLa-d7Gt89sa3TJWDUosOyrwmiPgaqtXFegyJim1-RwsmbhFxcuRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش سوزی گسترده جنگلی در جنوب غرب ترکیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/676356" target="_blank">📅 15:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
روزنامه کیدو ژاپن: خروج ۳ کشتی‌ ژاپنی از خلیج‌فارس از طریق مسیر ایران
🔹
نخستین نفتکش ژاپنی که از زمان جنگ علیه ایران از تنگه هرمز عبور کرد، نفتکش «ایده‌میتسو کوسان» بود که اردیبهشت اجازه خروج دریافت کرد و اوایل خرداد در سواحل این کشور پهلو گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/676355" target="_blank">📅 14:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رجیستری گوشی در مرزها همچنان ممنوع است
🔹
گمرک ایران با ابلاغ بخشنامه‌ای اعلام کرد شیوه‌نامه خدمات گمرکی اربعین، از جمله ممنوعیت رجیستری گوشی در مرزها، همچنان تا اطلاع ثانوی معتبر و لازم‌الاجراست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/676354" target="_blank">📅 14:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgD6IuQlW2KDVbcTozMpJpuLSmGdfHWhTByvQd9J_r0OAamIsEJ8sliEYSjGOiTEKDFc3PaItK9T40VkHg-sGvqx9OvYPUMVgUMSwt8GVtBqyJzDkSi0iT38hDPCIheEd6bB6mYYaeJggjPzbDfTl3EfLltgmWQtJbu2CkknyRnYVPLhC9Z9L-riujFPjOZsl_sp28i924RhhhB723kcOK1IoiGqc0qm02PY9ifQzd5VG8dCJ8RZ-fwuL7R4KRg07QYMJDpxyIC7LENFTHn9qEnthXuVLMKpmZ9476X6gF5RYIOV0z-eGgktdvVQg8aUgbN8zABr2oYr_FuRyW5HpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
شما هم زائر یکی از ۱۰۰۱ سفر کربلا باشید!
✨
همین حالا با شرکت در پویش «زیارت به نیابت»، عدد ۲ را به شماره ۳۰۰۰۱۱۵۲ ارسال کنید و شانس خود را برای برنده شدن یکی از ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/676353" target="_blank">📅 14:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sojvlaPCVqEgZ7lYVJprXDOqtZrH3NtT0gLeKsIGyfYADPyGkJpCxTtgtoskTGDm0xdLrUQ1jivt0VC_-QMoMRz3071Q0TmAiDnBQAYItfGA8_fkvxGxIGhRyYNcYyxcbuSLWkJl6b7wcZAn1M9nGzGoIMfi2UDlYC3ySNjLmMMt84ais_vYn8_QiITn9Eez5Y8aEfZoZ8CVNBpd6P9tr2OrfpfpAUNrDUxddftJFXdolxO7Mi8DkLkmEavWn2nED9NvjUNhR8rye3ctCuhsGRhr0NvLTxkEPP60z6K108Qb3sYxrF2tPTkWrRVOArGthyYFAjYSGg-j07biZhu-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e6dbca08.mp4?token=ukTMEcLtO7yhP8ueNpbBf6pXtoB40Tpve4qRqGxztCRTLs4PaXfqgTBhmnY26U3DsSLpQOuwn_OUpO9GoyQzV7Zyz-h6E-Ml11weaoYwJ5_tCyL9pyqW-NkOPJYycKs8mHspbLz0YsvuETtTDmnmAU_TjiHyaQRqn2_rK_kizTgV4a-K_0X7ZwVRnFFiweL9gB0QaGR90vRU1aLZwjSmmqCUdwAnvCBqyLQT_vyQmoZzHbmQENesXyLvUCW-l-wX61bvXJp20KI2WXP_InplpiDrd1eaIakxAG6pxQeaxDzv_-T-frSdtPXxTTBueah5-ZlaNmYEEk4vdWSibfXZKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e6dbca08.mp4?token=ukTMEcLtO7yhP8ueNpbBf6pXtoB40Tpve4qRqGxztCRTLs4PaXfqgTBhmnY26U3DsSLpQOuwn_OUpO9GoyQzV7Zyz-h6E-Ml11weaoYwJ5_tCyL9pyqW-NkOPJYycKs8mHspbLz0YsvuETtTDmnmAU_TjiHyaQRqn2_rK_kizTgV4a-K_0X7ZwVRnFFiweL9gB0QaGR90vRU1aLZwjSmmqCUdwAnvCBqyLQT_vyQmoZzHbmQENesXyLvUCW-l-wX61bvXJp20KI2WXP_InplpiDrd1eaIakxAG6pxQeaxDzv_-T-frSdtPXxTTBueah5-ZlaNmYEEk4vdWSibfXZKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول ۱۸ ساله دنیای بسکتبال؛ ۲۲۹ سانتی‌متر قد و هنوز در حال رشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/676351" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEXfvja-n5RMbw0A8xrr2yPvGvVt_XJe8ajx87OUtHe9dp6WLL4eyL6AnqHz-MYpOiLh8WmNAtEJXGaP1kHKD33iJfwcwIWVX700482EaBPy3NzH7PekCefDMha8K-x4fRs8iYNQhV57f0znoi3EmDDvMw6SUiCwjw0TCU4UWwYE7U5krl2lxzEDRH5VJnJgFNqmp7E8gZk8WK3B_End_6qpNoD8LpJnUHx7w6nrvafe0tSfGB-m3lFo1S9-qt9b57rLmX10fjOCuUm8a6kk-CBiEBDqp4DfOIRDgfPKR8X4HelxG2lwYstCUXAXdm6F7J1Rho1NKv_Uj_ZldQXyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در شاخص جهانی نوآوری چه جایگاهی دارد؟
🔹
در شاخص جهانی نوآوری ۲۰۲۵، سوئیس با امتیاز ۶۶ از ۱۰۰ برای پانزدهمین سال متوالی در رتبه نخست جهان قرار گرفته است.
🔹
ایران با امتیاز ۲۸.۵ در رتبه ۷۰ جهان قرار دارد و بالاتر از کشورهایی مانند کویت، آرژانتین، مصر، لبنان، آذربایجان، پاکستان، تاجیکستان و الجزایر ایستاده است.
🔹
با این حال، ایران همچنان فاصله قابل‌توجهی با کشورهای پیشرویی مانند سوئیس، آمریکا، کره جنوبی، بریتانیا و چین دارد که بخش مهمی از اقتصاد خود را بر پایه نوآوری و فناوری بنا کرده‌اند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/676350" target="_blank">📅 14:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdce95a76b.mp4?token=DiKEzY3A29XeMch1MtaibW1DYik0PeUEM--MhnVYlrn71nj9PTqfO0sumweSAYChxKzKozPYvJTnvkeaDUqqhLAKPxm5mCls-f4pr8K0Cy387ZEpqcFAJBYKrG-j7Y59uydpQ3NhzxekqXruPVZAFC9Pjuu10XEMVybpBK0ANDsecxoFogwliBlRixF9LyjU4vZyn1sEHa59KGFhg3jIr2nn3IYEgHM6CqFdfynCkSq3w3Qe-JjhMlkj1yR_rcn3KBE9PIwndeYG-DSqzlcM2KuXhf91eiA_wQ3Ow0r8aY_MTkz2ORWOp_zS15XdX56F7Iwvq9SNpAOQRSSnH6jV6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdce95a76b.mp4?token=DiKEzY3A29XeMch1MtaibW1DYik0PeUEM--MhnVYlrn71nj9PTqfO0sumweSAYChxKzKozPYvJTnvkeaDUqqhLAKPxm5mCls-f4pr8K0Cy387ZEpqcFAJBYKrG-j7Y59uydpQ3NhzxekqXruPVZAFC9Pjuu10XEMVybpBK0ANDsecxoFogwliBlRixF9LyjU4vZyn1sEHa59KGFhg3jIr2nn3IYEgHM6CqFdfynCkSq3w3Qe-JjhMlkj1yR_rcn3KBE9PIwndeYG-DSqzlcM2KuXhf91eiA_wQ3Ow0r8aY_MTkz2ORWOp_zS15XdX56F7Iwvq9SNpAOQRSSnH6jV6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمین قهرمانانی که شجاعت را نه در حرف، بلکه در نجات جان انسان‌ها معنا می‌کنند
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/676349" target="_blank">📅 14:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b77h6pqwHC8uneXqLngbQR2N4vM13vmC0GtMluXGbCjdd-mUZCoZ0COFkkKBLayiJkHGsQlFXVVgufG5RzSV-vVFe-D1Slk_UfGkC0x8mG16sOmcX3PjveHtpnxlhY4RFOm111_zjerAk81K-pICf8kKXdnFIe-TbG17h6qLdzMAOx51SZcPW88P4_4I4XYtHn8VVD_P4KaljhmgBWrg7DWZCT6dzJa_q1NMMh9sVDjMDJZOCwBpE1U0ejh50F6VRQjAWf9_DgWg-lCXzX2McpO0m3BoBOMoy4zHsI1oZPoauM5I-c6tcJC19zeaRfV1Ho9EAEQyMh8v4LDbSuvApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه حملات تجاوزکارانه آمریکا و عربستان علیه عراق را محکوم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/676348" target="_blank">📅 14:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676347">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxPxkB10eQFl7UgfpmffgpQDE7BpqBHwhaJaBas_0zWCSM1LLE6gi6gzO6kGC9y9Pebb3zVYCrG50JlC4MWq3RrhQ63-E37MZiDkZS7i-OBcVc8u1RC5xCtU9F7HJYkypDDnW_yzHTQPWMpyVqdGIwB1XQFPE51LW69IKPjVp9QxO9ESTzA5u6vfaBODYQF58vVOrhCxotZkTNVAqAQNhw93TPHgVrYPus_NxWITyhFbj-N8RYkQ3DitWl0x9b58nAl3F44xdG0DvbY7Dg4DvsBPw5060Qa1a929U9zIRWXtEQXRVe9weAKcxcraLYDJXYZVudEZRjcXDmcm5j0vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مبلغ وثیقۀ مورد نیاز برای خروج از کشور با هدف ادامۀ تحصیل از ۸۰ میلیون به ۲۰۰ میلیون تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/676347" target="_blank">📅 14:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676346">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coP6RSNWe_GLQT0GWKHDOoq-lwgcjtWywBDaqfM_cB7ZQKZmL_PnXlecJbJyLtSdIBtelSFZns9kC2CU-ZU8Y1bd_4cH_S2GQOoy1k0MSoy4sXBCs9WwF1ynMIWOAQ6T4I81xEWq-z7XFvGP9siM39CVEc63hS89ROZrtkFg7KGQFKoxmFu1_a05c5x0Fvcdo_l1Ybs6ohHjE406WwpguZDP6WWdRj9cOquPA9GfdQcLSNmsbkWwISTcXr3TnTTMOFVBUz_adYSSTo1esJy9HsLKvOOAr-3q4SMJWscUL_B1ZUUewKiBpAh_hJ2bwT-7h95oaeUk_LRHhF8MEjdeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندوق طلا چیست و چگونه کار می‌کند؟
🟢
صندوق‌های طلا در گواهی سپرده شمش و سکه سرمایه‌گذاری می‌کنند. پشتوانه این گواهی‌ها طلای فیزیکی اصالت‌سنجی‌شده‌ای است که در انبارهای بورس کالا نگهداری می‌شود؛ بنابراین دغدغه اصالت، نگهداری و سرقت وجود ندارد.
🟢
این صندوق‌ها علاوه بر کاهش هزینه‌های خرید فیزیکی، با مدیریت فعال و ابزارهای مشتقه می‌توانند برای کسب بازدهی بالاتر از طلا تلاش کنند. در روزهای جنگ نیز صندوق‌های طلا پس از چند روز بازگشایی شدند، درحالی‌که بازار فیزیکی و پلتفرم‌های طلا همچنان امکان معامله نداشتند.
🟢
صندوق طلای رز ترنج از ۱۰۰ هزار تومان و با جست‌وجوی نماد «رز ترنج» در تمام کارگزاری‌ها قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/676346" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676345">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd680441ef.mp4?token=e68lUvzogQXd8uwArPvIqo8AeseroWhbgAgq1i7zc5qUMQcIheukzKeJqjUCstEiW2scUUaqnPMSlVKlrhNweXMi4neCwhGnS7I17JKMkzSJ59ozSI2x-Ny8sOFHhdEe_I-B_yXg5WPT1DPj3H9PePqYXN9FclWSeYzwX3KUiOgW0KAkFpPab9WF0V9X4zfVgZJDkn_Jbcs6ylda0eAJ8ZtCD_xziJl46oxKFZWoY2YzqXjcZ8iQDu5McYL0_qwHx3btTPYKZasdz0FWlQ71PV1Ccsxyek62zchGTKuNHs6c2FpHmxKTUCGLZa0tAv2fqaMBPNgPAWEdLsYWZDDvJZ9xHCRmapP5OExFoknQXohBxxtKSaMyd4DzrlQsg3B0mizkN4aGtMX9tbK12erv6QdWqRYsYQWFyhaIglXMT60fa8aMIINmjzYFs3MtAoRkGXpRNk7iJdHWNuAWdw2-zc5OJ2bSnG3MsK2k563x7NO1t9Jfu5xET05dZX4rwHJO7BE-d4OxkYwHcG7wq3aCkwN5iPerZx8hjSbzXDT4sJM-RA29SeiZAAteaQL5FMJkNUHTZsw6OkQVJulvBHWi0JYCsa3O_qsz4kERAnjzG8RuF8a69dItdEivNWeUgUxvlQ8jVT7ScDOtEhjyrnIEHHZCJyRleEWUZIpJWxdozS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd680441ef.mp4?token=e68lUvzogQXd8uwArPvIqo8AeseroWhbgAgq1i7zc5qUMQcIheukzKeJqjUCstEiW2scUUaqnPMSlVKlrhNweXMi4neCwhGnS7I17JKMkzSJ59ozSI2x-Ny8sOFHhdEe_I-B_yXg5WPT1DPj3H9PePqYXN9FclWSeYzwX3KUiOgW0KAkFpPab9WF0V9X4zfVgZJDkn_Jbcs6ylda0eAJ8ZtCD_xziJl46oxKFZWoY2YzqXjcZ8iQDu5McYL0_qwHx3btTPYKZasdz0FWlQ71PV1Ccsxyek62zchGTKuNHs6c2FpHmxKTUCGLZa0tAv2fqaMBPNgPAWEdLsYWZDDvJZ9xHCRmapP5OExFoknQXohBxxtKSaMyd4DzrlQsg3B0mizkN4aGtMX9tbK12erv6QdWqRYsYQWFyhaIglXMT60fa8aMIINmjzYFs3MtAoRkGXpRNk7iJdHWNuAWdw2-zc5OJ2bSnG3MsK2k563x7NO1t9Jfu5xET05dZX4rwHJO7BE-d4OxkYwHcG7wq3aCkwN5iPerZx8hjSbzXDT4sJM-RA29SeiZAAteaQL5FMJkNUHTZsw6OkQVJulvBHWi0JYCsa3O_qsz4kERAnjzG8RuF8a69dItdEivNWeUgUxvlQ8jVT7ScDOtEhjyrnIEHHZCJyRleEWUZIpJWxdozS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریق نجات نوجوان، جان یک پسربچه را از دل امواج خروشان نجات داد؛ شجاعتی که حالا قرار است با اهدای مدال از آن تقدیر شود
🤯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/676345" target="_blank">📅 14:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676344">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aefb607a1.mp4?token=lVrUCJhKXLR4gBB226nsUvNthGfOZYxaW7-wyE_UWIfMQH6TtxpjvVpxxJRZ_MJKitQz5dNwuS48W-4TtvWLf-Z-RhUS6HSdJiM_dtOI7fYw6NvS06pwU2o0VGTbKXqK7IPbAjaZWW76dHVy8fv8y7Iq460eFACKXXrFpc0nm1UJyXptea1hoywSnTj-r3eunj0iIkyCP3XML8C6qchZ5CQ8ToIjSkpEwcNYirunDwlSNbeBEnR6J2Gozta1ifiioxfs91Fazdeik8AEQKmi-ExV-1ObyitSTF_KJcImXa2O57yu7DMtvcQMkIbaC8JiCjxYfH9uCYJL2WQPnxGz2V7KIwZPrTQkbWPPghY04Lb3kePo3wdEUHFm-PNSya-Jm8rz2N9XX-qM6SRXzv3ZYgWniYkN4LC0zz55BSwqSRMn54FE4A0j_iRUqjt8rCPo8EE4GKB9nWnf5dBH9qQy29I-Y5By-a5qGaHZx1GtiHTKmGw2xlcD8fA0YII1jPc_x8ocqP-XVpOm8OXefrT3_Cpi7JN7Bo_OSKOboIh0UmxRh0FKbJ8Q36SQjbyCM9dqO1XslbMuuixAaYdaXwEAbNmpLRx1Zr9j8B4YX_GIHxGTHoCmxdVO6k7Dgl2fD7vID_h2fixMrX3SwhrCAKmZfufCA1ADiMtiuTso38jcQYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aefb607a1.mp4?token=lVrUCJhKXLR4gBB226nsUvNthGfOZYxaW7-wyE_UWIfMQH6TtxpjvVpxxJRZ_MJKitQz5dNwuS48W-4TtvWLf-Z-RhUS6HSdJiM_dtOI7fYw6NvS06pwU2o0VGTbKXqK7IPbAjaZWW76dHVy8fv8y7Iq460eFACKXXrFpc0nm1UJyXptea1hoywSnTj-r3eunj0iIkyCP3XML8C6qchZ5CQ8ToIjSkpEwcNYirunDwlSNbeBEnR6J2Gozta1ifiioxfs91Fazdeik8AEQKmi-ExV-1ObyitSTF_KJcImXa2O57yu7DMtvcQMkIbaC8JiCjxYfH9uCYJL2WQPnxGz2V7KIwZPrTQkbWPPghY04Lb3kePo3wdEUHFm-PNSya-Jm8rz2N9XX-qM6SRXzv3ZYgWniYkN4LC0zz55BSwqSRMn54FE4A0j_iRUqjt8rCPo8EE4GKB9nWnf5dBH9qQy29I-Y5By-a5qGaHZx1GtiHTKmGw2xlcD8fA0YII1jPc_x8ocqP-XVpOm8OXefrT3_Cpi7JN7Bo_OSKOboIh0UmxRh0FKbJ8Q36SQjbyCM9dqO1XslbMuuixAaYdaXwEAbNmpLRx1Zr9j8B4YX_GIHxGTHoCmxdVO6k7Dgl2fD7vID_h2fixMrX3SwhrCAKmZfufCA1ADiMtiuTso38jcQYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵۰۰ سال بعد، همان دشمنی؛ پل‌های ایران زیر آتش متجاوز
🔹
دونالد ترامپ در حالی به پل‌های جنوب ایران حمله کرد که این اتفاق برای بسیاری یادآور حملات تاریخی استعمارگران پرتغالی به سواحل و جزایر ایران و تخریب پل‌های این سرزمین بود.
🔹
رخدادی که یادآور تکرار یک الگوی قدیمی است؛ اینکه دشمن، هر نام و پرچمی داشته باشد، در نهایت هدفش آسیب زدن به ایران و منافع مردم ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/676344" target="_blank">📅 14:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676343">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
گام بلند موسسه ملل برای تبدیل شدن به بانک با واگذاری املاک مازاد
🔹
موسسه اعتباری ملل با دهه‌ها فعالیت در ارایه انواع خدمات مالی، از جمله خدمات بیمه‌ای و واسپاری در حال تکمیل فرایند بانک شدن است که در این مسیر اقدام‌های مهمی را انجام می‌دهد.
🔹
در تازه‌ترین این اقدام‌‎ها ۲۴ مرداد در محل این موسسه از طریق مزایده عمومی تعدادی از املاک، مستغلات و قسمتی از سرمایه‌گذاری‌های مازادش را به متقاضیان شرایط واگذار می‌کند.
🔹
این مزایده که فرصتی ویژه برای سرمایه‌گذاران، فعالان اقتصادی و تمامی کسانی است که به دنبال خرید دارایی‌ها ارزشمند هستند.
🔹
این اقدام با هدف مدیریت هوشمند دارایی‌ها، تقویت ساختار مالی و پرداخت تسهیلات به هموطنان عزیز صورت گرفته است.
🔹
همچنین این موسسه که از بانکداری شرکتی رونمایی کرده در تلاش است تا مجموعه‌ای کامل از خدمات مالی، اعتباری و مدیریتی برای شرکت‌ها، سازمان‌ها، کسب‌وکارهای متوسط و بزرگ و مجموعه‌های پروژه‌محور را طراحی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/676343" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676342">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlC1orAtNIBlZe24R8vjHGFnLk6Qu9KIM4QUrTmhGt-NHvhmI2DqnHbKkLDEtHW70CSIo0s0Mbji8t0DkxdR9FYDumB2ULoA5jFiVAnS54L29SOf7qMS-gZQLx9ZHJ05P7aCKVt-MkiZIGGCvkIqmRVx9TNr4ZSDqDjUYPXmyXPFAkfGRMFwsSSCx5t_28Cau3wDccD8S-PIapdxqUpkIYapyvBrHXtf2AJJ1nRkT7T3dIJRTyp4w-lQgCJUbH2IT_oYpv40wAthKGGDx63a2I2ws7cz6QSF81_diySTl55H_lp7ntBROmV-sW6jP6SsX3vRd3msz0c4ja_Vsc6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای تلفات پنهان آمریکا؛ ۷۰ تلفات در ۱۸ مارس، ۲۹ تلفات در ۳ مارس و زخمی شدن دو ژنرال در بندر شعیبه کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/676342" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676341">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تیزر قسمت پانزدهم از فصل پنجم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ آقای حسین صاحبی بزاز که در این تجربه متوجه اهمیت بسیار زیاد محبت نسبت به هر موجود یا شی شده‌اند و اینکه هر انسانی مسبب تمامی اتفاقات خوب و بد زندگی خودش است و همچنین کسانی که از رزق مادی در دنیا گله‌مند هستند بخاطر سبک شمردن نماز صبح‌شان است و همه کسانی که مهر و محبت اهل بیت در دلشان جوانه زده باشد توسط بانوی دوعالم در آخرت مورد شفاعت قرار میگیرند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین صاحبی بزاز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/676341" target="_blank">📅 14:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8aaabca7.mp4?token=LaOj-s9H2-ZNaCMzdqMnTFVSVApAME0IvvNRZvgvbSuWm86OBFNLIZyNQ5wGmwbwjH1gxnqm7ChHhlILCXyp3E5ZetqFKW1SRp97zciccXNMUoJM2xVYOuXB7JrVbHgzxBV4iG84TMTaoZ0Q-U0FC7Vh4sIAFO346BV_N62NnRZkhBU3ijwWRyC46thc651i9bUzp-cL7zW33gl9iXLePuWgZ277u7jGxpa2-um579LzQs0oRncHGd0tATDjIUov0OTVR7G7XRqbulMNrvLCiLH6qwLQKSw-oIin0vKDeyimzZnADYcLXTQge1WcFQgGHI71odwKXfLLolPY_MpoGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8aaabca7.mp4?token=LaOj-s9H2-ZNaCMzdqMnTFVSVApAME0IvvNRZvgvbSuWm86OBFNLIZyNQ5wGmwbwjH1gxnqm7ChHhlILCXyp3E5ZetqFKW1SRp97zciccXNMUoJM2xVYOuXB7JrVbHgzxBV4iG84TMTaoZ0Q-U0FC7Vh4sIAFO346BV_N62NnRZkhBU3ijwWRyC46thc651i9bUzp-cL7zW33gl9iXLePuWgZ277u7jGxpa2-um579LzQs0oRncHGd0tATDjIUov0OTVR7G7XRqbulMNrvLCiLH6qwLQKSw-oIin0vKDeyimzZnADYcLXTQge1WcFQgGHI71odwKXfLLolPY_MpoGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این آموزش بفرست برای کسی که عاشق شال کشی و استایل کردنه
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/676339" target="_blank">📅 14:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مدیرکل مدیریت بحران آذربایجان‌غربی:‌ یک پرتابه به یک منطقهٔ خالی از ابنیه و سکنه در استان برخورد کرده هیچ تلفات جانی نداشته است
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/676338" target="_blank">📅 13:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2-TWfZtt86UJnoDiFEWwy2ZFm1R5PewJ_eLmMI528qrvpupCGj9eqsUZRcbb0J6h-f-EXtk3vmjaEBPKGYznZJj_gyGLhtCVV4TdM2xzqvWgYKExZfgbol1sCyCzfjPfvRW8vxJCzoy7onOxOZPzg8rd14ShXiZzdpHWtt33-miXcWEPhDeFOTVJzUEP5M-L0mQ9IbqGug7FYgZOQV7Nlns7KnVcdmKu3F4AlCpJFJ9n0EjlANhwPtAPOHhuKP5CDiUBc181EUujB9joRj62uUdj52iT-LGVdKk4iZWUZgzn32qg07W4AJ8jKDeuKfCWrdL73b3tg_roKcwizRQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: حوثی‌ها در نظر دارند برای کشتی‌هایی که از دریای سرخ از طریق تنگه باب المندب عبور می‌کنند، هزینه‌هایی وضع کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676337" target="_blank">📅 13:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پل B۱ کرج با تغییراتی در سازه، ترمیم می‌شود
🔹
دریادار سیاری: بدون اجازه ایران هیچ تحرکی در تنگه هرمز انجام نمی‌شود
🔹
چین خواستار کاهش تنش در دریای سرخ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676336" target="_blank">📅 13:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ممنوعیت واردات لوازم خانگی شکست خورد/ نماینده بندرعباس: وقت بازنگری جدی رسیده است
احمد مرادی، نماینده مردم بندرعباس در مجلس، در گفت‌وگو با ایسنا، سیاست ممنوعیت واردات ۴ قلم لوازم خانگی را عملاً بی‌نتیجه دانست و هشدار داد ادامه این روند به ضرر مردم، تولیدکننده و دولت تمام می‌شود.
🔹
شکست در عمل: «قرار بود ممنوعیت به تنظیم بازار کمک کند، اما نتیجهاش افزایش قیمت، کاهش تنوع و رونق قاچاق شد.»
🔹
نیاز بازار حذف نمی‌شود: «وقتی واردات رسمی بسته می‌شود، تقاضا به سمت کالای قاچاق و فاقد گارانتی می‌رود؛ مردم پول سنگین می‌دهند، اما امنیت خرید ندارند.»
🔹
معیشت ساحل‌نشینان در خطر: «در هرمزگان، زندگی مردم با ته‌لنجی و تجارت خرد دریایی گره خورده؛ نمی‌توان هم از اقتصاد دریامحور گفت و هم راه معیشت آنان را بست.»
🔹
تفاوت قاچاق سازمان‌یافته با تجارت مرزی: «یکسان دیدن این دو، خطای سیاستی است؛ باید برای تجارت خرد مرزی چارچوب قانونی مشخص کرد.»
🔹
تضعیف رقابت و تولید: «هیچ تولیدکننده‌ای در فضای بسته به کیفیت مطلوب نمی‌رسد؛ حمایت واقعی یعنی کاهش هزینه تولید، نه حذف رقابت.»
🔹
ضرر مالی دولت: «با توقف واردات رسمی، دولت هم درآمد گمرکی»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/676335" target="_blank">📅 13:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676330">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNHted_obOW1tmbCbX0JFvMvvbPGU3evoL-mZjHtr6GBxT93tzfz-zrxBIt547O7XXdaEQixzZWDlIr-klv0HT9iNpX1XgW0iaiqNCUXec1ah5vrsIuYYACd4OlPy_zt273I1g8whEsaSKQoV3uwrY4XJQwV80Pub9WIB0bMCMm9C6D3u2aCrP9XDg87TCL_6ofPkBLGAh5myINeSJ47bKWdFm316XIYHYxuvJN295rPC0gckwHmmCSaFBngxogLuGzm1SGWvxIc7wGpQk5aD4Dbouq014sAz9K7UXFUFIZea7IgLKqZpf7FHmpUlriIa6M_bqebYRQMB6ezYpBTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlMPeRZw9ygN36b_sKvMNNDvcD-Rb04D_V0K3VcXv04j-wD7-ClIftXLKZNvSLMvxI7Cfvzx0coiqMfDqG2pLP-AkoZHuOHium0Dfqqq_CNFe5HktEs6VWlMkzbvZSaj3hnFIL3QYWqFRDacG_HCWQil0LEQg80ZhXptnORLzuNtpx9AIUic1tpXey0pmoxVLiIHVLe7taY8Eu3AHmuTGedbugUbSBagqTIfPNCCu_tpfsHABr1HTA_6_p7R8HVnsL4wQxTjtdc9QHoyr9QsX3kWD2V7TtiRFvDykcqhdKsPhZ45QBTAlhAFm1QJSPVcZRYXrwUO_BV0dGLVNuw0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMLckFVF2GMUQ6vQE2mpfM4v_XG8Cp-CjKFuCdaoeALP8HUMLPm3bcaj1rsK23EWZTiBjICUIftX-zH4vRAX6dgSeAO-M85KSmfyCph38E7BUBWvQLgk698PatJGuPWHR8zmX8A6Q6bPdBC-pnUMPl9jtwMBhOUURz9s-2XW1bYwEBC7U-ghtR5FblWxiR0_vNRv0BxEFUhSeUNbdoJXSOcwVeSYRyvyKPXc6eLpqgvC5Nc1sx1B9jor9xVVWgPzETOT6P99rCdidNmmLsyXMDUGe3BVWmWFEBctpt8yuqqfps3m0U4bXQwmzuRLa2u6LAFzxEPhP13pgN7-wQr8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdIVGCk9DThjBpCa1C3YPzBezRJEXGuusaufGPWTOiR6bl1_0WEepQ7Ou1C6ZZTT10p0dlFTXwAJ2Nj5LrKjKJTheR7oBfwwIUH3CxXLv1S4ganaDRnDlcyQ1PInKWPLNm-trZfJMzkAHmv6_XAqXK7JoiJcM_zcUCaNT97gFEFNnKBQBl7aZGo9k-UA-RXBhpC-Pqe2DrPI8GhcxCqoY8XOKSP1fuymYf_rFc-2_Ml6bQrtxnOL586c4JYBPfC7qL0SpwT4stjoBq4bbSu62mEN5MsYrNqAnPB8ZC3YD2jRdgLj5Yz31i5PgO2qRZuv2zMJnqxWDWB-h883xOmDjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6_wtIp5vYCw0ZlV-II_ZVjJiiPDQdQgy6wZCJETh8PWaI0D-5k4hhma7BfrkRjb_P7Y9Iy2oJI1bmbvNzrIGTzxJixfk96TPJtWCSWuO1qTJ0XnemLCCFoRwPMngrtBFW8bHC4KGaVT9WEbwvkSo2A_pt5iIA8WYfeOxGs0KYFR9fnVUiTBw_rt9WhkoBLcNj9BHPkh5qzWs2oJjlRMbRIhoLyhEp7C0bFsuKxUpO0Txp1nOKAVcfO_L-ELK7AlXI_Jj3pgKLJdq8itSxYfCCccMy6SzZbKXwZNJWyYzDVfxgAAznOr9yiT_pJQw-FpWcj2IAzrvL1wWNFYHmiYsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر عاشق جوجه‌ای، این ۵ مدل مرینیت جذاب را حتماً امتحان کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676330" target="_blank">📅 13:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676329">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-text">◾️
اینجا عشق به اباعبدالله(ع)، در قامت خدمت معنا می‌شود؛ روایتی از خادمانی که در موکب بانک شهر، دل به میزبانی از زائران حسینی سپرده‌اند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676329" target="_blank">📅 13:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676328">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ویدئویی دیگر از جنایت آمریکا و عربستان علیه حشد شعبی در نینوا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/676328" target="_blank">📅 13:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676327">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ae969d5f.mp4?token=UUELgjh65Ed8n3wgm4hmKCk_u5f6DH8t_36mANOZMAyujeU9LjTMqecl-Tyr_gkZNieZTGtojejMKhmRQdxRe1CzqdkBPnHq_JbT7t2OQUwYYAt_oq5lU-K7wHwb2ZMqa3SvUg8KBUzZaSZIfnFtuYo7IXDbe-LmtbLxBSVnNAxC08RXznhP_FSG4icTGMnaFdakoEFE7oSODJMVVHiX-XVjb4qjHcit0Jt0U_oPqAwhm5GXbshMBHsnSAWNmgM8QY9plYhnmPEv6VYSdqqqDXp497heK2sZdAoNb7jN_akqKda6TcixSuqiDu79-qnkh9NMamg0jKE8kjVuSxrT5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ae969d5f.mp4?token=UUELgjh65Ed8n3wgm4hmKCk_u5f6DH8t_36mANOZMAyujeU9LjTMqecl-Tyr_gkZNieZTGtojejMKhmRQdxRe1CzqdkBPnHq_JbT7t2OQUwYYAt_oq5lU-K7wHwb2ZMqa3SvUg8KBUzZaSZIfnFtuYo7IXDbe-LmtbLxBSVnNAxC08RXznhP_FSG4icTGMnaFdakoEFE7oSODJMVVHiX-XVjb4qjHcit0Jt0U_oPqAwhm5GXbshMBHsnSAWNmgM8QY9plYhnmPEv6VYSdqqqDXp497heK2sZdAoNb7jN_akqKda6TcixSuqiDu79-qnkh9NMamg0jKE8kjVuSxrT5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع انفجار و بلند شدن ستون‌های دود در اردن خبر‌ ‌می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/676327" target="_blank">📅 13:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676326">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عاقبت همراهی با بیگانه
🔹
در مراسمی که برای لیندسی گراهام برگزار شد، ترامپ حتی توجهی هم به بازمانده خاندان پهلوی نشان نداد؛ همراهی با دشمن خارجی، نه احترام می‌آورد و نه جایگاه.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3234016</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/676326" target="_blank">📅 13:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676325">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX5TEeMY-CaLZK0riGU1-vbNswTkXHhOO6t_eAH3uwIpoC0OVsKgQJMVyWMzbTdTf6hqQhq-M3oRIczhWox7353CWR6H2teZNMceYZ-X-p1e2X-GAgUWW60ZES71x8v-wvvc5LNL8JWCeoMC7BBUmaY5BLlw3A_-BCM0-lf9Sh9dQFTFz2GkMP5BDDE1Nx2Lrmbty2Dkoi8dMDBuNxHTD53tE0t6GZvnGjaP5PRywG52k8-CEvqiazfmjYpLQJrv8YxqsCXKEwKoJw_tnBcdO_g7zuXyiWaUQtiw9Fv9TdrKBWGDlL-P7IdWzK78eAM_7P6V4BBK2nuvVVVuTt9Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۷ مرداد ماه
🔹
بازار طلای امروز با کمی افزایش نسبی در سکه تمام بهار آزادی و و ربع سکه مواجه شد.
🔹
قیمت‌های اعلام‌ شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/676325" target="_blank">📅 13:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676324">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حذف نام «ایران» از جمع رتبه بندی دانشگاه‌های تأثیرگذار تایمز سال ۲۰۲۶
🔹
با وجود اینکه در سال ۲۰۲۵ جمهوری اسلامی ایران با ۳۴ دانشگاه در جمع دانشگاه‌های تأثیرگذار رتبه بندی تایمز حضور داشت اما در رتبه بندی سال ۲۰۲۶ حضور ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/676324" target="_blank">📅 13:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676323">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
صدای انفجار در اربیل
🔹
گزارش رسانه‌ها حاکی از شنیده شدن صدای انفجار در اربیل مرکز اقلیم کردستان عراق است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/676323" target="_blank">📅 13:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676321">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05368b5b56.mp4?token=riW9YAObfiC5qFo3pcNiOxE6tMQpzGGxUD8MdIxZkcB8RbZ1BW1fGp5znpvIzRn_T7BuBohfWouu9nMqeTpJ0CIa6h3hLXYu9MN7tzhcxYJxckEcuzPeE8aGSXD7Wg4VJlq2U_1UfFzSRnM0ibrk10tkZWeQk_19f1MErtBVExtTcf3pQEIwZCAufC_U50_UJ-QVMoT8mv5nE2CtIPb8SP2v_4QvAik9o_Obsdlm2n1_APE-cUwm_wrsLcXJMu2_jb9ydd8Tndc52cAHqcR05F-lRRQNoyJqF6kzPNDfxRKAzCRugzeVkZ6zzy4g8Q1pePYboZub0nvF7-sp0HY7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05368b5b56.mp4?token=riW9YAObfiC5qFo3pcNiOxE6tMQpzGGxUD8MdIxZkcB8RbZ1BW1fGp5znpvIzRn_T7BuBohfWouu9nMqeTpJ0CIa6h3hLXYu9MN7tzhcxYJxckEcuzPeE8aGSXD7Wg4VJlq2U_1UfFzSRnM0ibrk10tkZWeQk_19f1MErtBVExtTcf3pQEIwZCAufC_U50_UJ-QVMoT8mv5nE2CtIPb8SP2v_4QvAik9o_Obsdlm2n1_APE-cUwm_wrsLcXJMu2_jb9ydd8Tndc52cAHqcR05F-lRRQNoyJqF6kzPNDfxRKAzCRugzeVkZ6zzy4g8Q1pePYboZub0nvF7-sp0HY7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظه پرتاب موشک‌‌های بالستیک عملیات سحرگاه امروز نیروی هوافضای سپاه، در ادامه عملیات نصر ۲ علیه پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/676321" target="_blank">📅 12:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676320">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
لحظه‌ای که یک تماس تلفنی با حضور ناگهانی خرس نیمه‌کاره ماند
🔹
مرد رومانیایی بدون آنکه متوجه نزدیک شدن خرس شود از خودرو پیاده شده بود؛ اما پس از مواجهه با حیوان، به‌سرعت به داخل خودرو برگشت و پناه گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676320" target="_blank">📅 12:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354c179b6c.mp4?token=GJybd7HS7aJ0LwpORoVKywoD1_2E46uOT2PqPVUHZjAFvp-O98qBysCYmrCo7Ya-cZiIG6dMFgf7YPoj14YcFI1WxyunIQ8YWSEMOccLvTjqDgu90syzKl6FKAvo_3T_Jfb9w8aKRjeMrmqiHtctHdnzxA8385vJ7DN-X3WXcwU1bYM6Y--st3o7P5gP5rxxQJYrTGa4M_gmEqhXUtXFFLvcPYaWR_45gRmEYlZThFGSqzDKvbyxRQZCmAJwPrvzIARxFPJ7YYjwLAKbKsDiOxACMKctVDtPEEtlTa-pWNU3aXa3uMUhVHrxzwxyuDCW1RUUnDsgnQQzsrFewadn8mEYt5IkYdybZZUoIu1tBwaVBNc0OYxBSMKrzetOF6xlpesyH5ajbA_2t4zQAgAqipSHenNln5NPIQI74n6A3ez7PQ3vpaqMNHRUkbNE0tCyW-d5PrUBdlNnb1BoX3JEWV-KQkzDq0FMeL3it4bccOIGdbj7Jd2_c3sjqKeKcDfKfHE43zUcLgaYW5_01638TgizTbrw5mcRZRJ4R3Xc2BXLZEdRFFpZAKcfpmFlNH-Myzlx0dOHb2_f6nla0hiS9kZKzGfT5nyb5Zadolp7ChtHdVewe_AVCYjzdwSGsBJcws4Qswo-RVAqh0HhqdqNGYS_PjFBm93tAy5aFg8Eoso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354c179b6c.mp4?token=GJybd7HS7aJ0LwpORoVKywoD1_2E46uOT2PqPVUHZjAFvp-O98qBysCYmrCo7Ya-cZiIG6dMFgf7YPoj14YcFI1WxyunIQ8YWSEMOccLvTjqDgu90syzKl6FKAvo_3T_Jfb9w8aKRjeMrmqiHtctHdnzxA8385vJ7DN-X3WXcwU1bYM6Y--st3o7P5gP5rxxQJYrTGa4M_gmEqhXUtXFFLvcPYaWR_45gRmEYlZThFGSqzDKvbyxRQZCmAJwPrvzIARxFPJ7YYjwLAKbKsDiOxACMKctVDtPEEtlTa-pWNU3aXa3uMUhVHrxzwxyuDCW1RUUnDsgnQQzsrFewadn8mEYt5IkYdybZZUoIu1tBwaVBNc0OYxBSMKrzetOF6xlpesyH5ajbA_2t4zQAgAqipSHenNln5NPIQI74n6A3ez7PQ3vpaqMNHRUkbNE0tCyW-d5PrUBdlNnb1BoX3JEWV-KQkzDq0FMeL3it4bccOIGdbj7Jd2_c3sjqKeKcDfKfHE43zUcLgaYW5_01638TgizTbrw5mcRZRJ4R3Xc2BXLZEdRFFpZAKcfpmFlNH-Myzlx0dOHb2_f6nla0hiS9kZKzGfT5nyb5Zadolp7ChtHdVewe_AVCYjzdwSGsBJcws4Qswo-RVAqh0HhqdqNGYS_PjFBm93tAy5aFg8Eoso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سکانس جنجالی سریال «رویای نیمه‌شب» که دیشب از شبکه سه پخش شد
🔹
ماجرای فرار «ابن سیرین» از دست زن هوس باز و بدکاره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/676317" target="_blank">📅 12:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvHOBfPT6jPm5G2GHXxa6_AP4oxLpvoYT-hxvzMw-Ir3oYZKWFMpviZq0Y765ENVrvHvU2OIztmIeNN1s5AqtA1J8pdl7r6kd0unJZlSFSlL0Hf4BPbnl3fFiowRiBiYxFH1GfcE949ruZiJmJJ-vjL7WGAuIosKy0qWeEWMmXempy8Xt62I4BPc31Yt43ho7JXDG9a6vvPFMZx5HaMiBI87pXLdQ3ayRRzyJS62oVxPOMe8S1u4LbdOsYl4TSLvKUoU9PrJlNDmPzt5xZ7nl3JjGMQtofQtU7xsHCWMZCRIyW8D1MOMWhAU-JUc8haWtTEwe4IxqhL0JW8ZekZTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا مخالفت با عملکرد تیم ملی به معنای وطن‌فروشی است؟ | چقدر تیم ملی را می‌توان جای «ایران» گذاشت؟ | آیا این تیم ملی چسبندگی بیشتری به حوزه سیاست داشت؟ | اصراری وجود دارد که کادر فنی، مردم را خشمگین کنند!
🔹
تیم ملی فوتبال ایران را چقدر می‌توانیم جای مفهوم خود این سرزمین در نظر بگیریم؟ عملکر تیم ملی فوتبال ایران در جام جهانی هنوز هم که هنوز است در میانه بحث‌ها و گفته‌های شهروندان دیده می‌شود.
بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3233786</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/676316" target="_blank">📅 12:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrIUfNCta29GE6cf46rlTstsur_YCK0-WFMzquhwRtTW9LIn18X6pdG5t-mwG5IfglxTvbFbfBCW7nAsERNbjIUwRGTz9Am_wguzNRwdpZ9cvqFR12ofH4wEQd6-66t7dp7NSD4Ac5V6A8iX7PNnmBRU_R8XhTWc5j236VAdf-qsfmOIlx7BH5lIwURy0xlUZBKkZISoLU2EPx5X4fmmf8OSJDsQH0E7NaUGYOnTqxL6XFR7iGnKG_7d-xlLKTb2FmajQ5HFJQxVNBx4t8ouHRFFRVLQ2xWyILBCzV1dUwkI4z9cIXQMrZ9Xi5frY1mCj-CwcyZEAqKq2XzToqVk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEIvj1sKzkdlqIDHSTRPYGKEgBBxZULoQ7XOi_Ta4z6ZVaK2VQOjx7CvS-nFYYsWhE2j6Cv3CmAaXRSOYGSx8rqG5oxLl96yQmvzf0f8xrBHL4gj9oozWecQuHqMPi3CkmdrXy3Gv4zjhgt7KcCWy77JFYATTqpjMt1-t4NAcYC2eBv8YTb-IGis-HCDG72PDwWH612c_Ni9b-d6i6L97Xq17eMLkcOinYf1KgFJtkt36m_74Ln6fATAatWxh6fsLGE6K4ccja8QEp4rXRNUFnJafbAj72T9DXbsA-ZQsMEpMSehj1X9nZAokgvmB-rPjum4H7FrWD9isNUD--4Ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTeHyhbH6-sjRcLNwC50_a3XYGHx5he1R4A_DeEFugr8TbI3lLuTDucSt802mItk98p6DAyHb2WcEu6n4YHl_NfJzBMotCo63xpx8EHN5wPvcZ-Yh4UWH1YU18AgUMIF8MGLhSrJ0OpI-XD9kj7p6YZ_dLcFhSeTJTGyrjxWtzX37VTkDcA0r63GgKOAyUc_qhx-FyKAHmfgZ807YI12apwroGzty0aXlDfI_bM5RbLIRFkwMHqDmBTWOA5L-O-u5LlTkDJMSEgHQLd005rts6XP4bd03TDDtZ1K6hHWVWHQOczNOU6F0v6ZnxdHjqwt1PjX4lom5E1ZEjS4w2TaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCHnp7y6kXBmPFHTMfqpYkids_IbsMKQYnJ4UkpvkulQHI_v5Tbww745fCpiHxi1iHVws-Y9mWzhaBbS8qVi5IqMI2I9xzxGRsnf6Rx7xdVqIxia7XZZ7VB_a6XMJAUXz9iFJZT5qylnp_4q1zRDYlghLHr1oyirx9w5lYWMnQEBTJImZdRkSz2KOj70msaC1UK4ady0GQqFSVE0vDICnFRUuu3Bn_g4ho_0bKQvJ8-UXwjAEpo90RK57-g8uDdyh_P96Wer7uP4BRLrcwQs9e9KC_NcztergUGhtkP2ghD_oLjnOQzf75NI8_shFrPkgBJKeUsOfra-YU1lvdI2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAuVvHChEpbCw7xe2zwqZXpzscUJttqHdWfAxzRnve4iELCQ9jwFZdpzvw66d0tte2J46O5EbXnc_1MhvYwZNmlimHLxZ1VggpqvcZeGb9tl-pbQeQQcnN_u_Yc5N9pAcROQBrcpR4B7cCw7mz91SuCyvFSorL6C246SYMlTxbfNSn5vnOm_UEIuUlgsRI9Y_SxFEIeI7DaDzfnxGyFoNXncH2JrQ1t5sUcIzn_XFeysErYgKva9r9kkUe3-EACAE4gFz9UJzjziUeTEq75UL9GotybMItRuY2QcS6vUNIt1Hp-zNqCOTNBuvrJQLvkdAwXIKYvTJ12Sz1fmKv5PQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
همه ما می‌توانیم با چند انتخاب ساده، در حفظ انرژی و تأمین برق پایدار کشور سهیم باشیم.
🔸
خاموش کردن سیستم روشنایی هنگام ترک محل کار
🔸
بررسی و خاموش کردن چراغ‌ها و وسایل برقی قبل از خروج از خانه
🔸
استفاده نکردن از اتو و جاروبرقی در ساعات اوج مصرف برق
🔸
قرار ندادن غذای داغ به‌صورت مستقیم داخل یخچال
🔸
جدا کردن شارژر گوشی از برق پس از کامل شدن شارژ
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/676309" target="_blank">📅 12:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2ed268.mp4?token=kcee6o3O7J9pgO08IXTWDw7rxXo4nEm1pa-xcojdzEDfVCALbC9RdKI9bUtHNW4uRdMvogpfqWewqsZ_4dP5P0bJ68BuY988Ug8nwzD6m2ZlLUkB9dOM0nsy4E_y1c-sj0_XTtACSXNIMkqDaWDCsJwW-ba0GJkj290nhSFmY9ymddpvVylRYKgDg3O9IPbdClEQ5IP2GoaQQWFply6C686e8gKlB9TBLbiuX-2Fw38I2UeDcy7rpUqE1iW7YNhqIKeqwmGx2t0uRFX8I2VPcuDt1QYfCWnPJKP_a_ctRwcNE7eAvJg2zlvEZtbYyulTh_rjVmmYjizR0I_U1a96ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2ed268.mp4?token=kcee6o3O7J9pgO08IXTWDw7rxXo4nEm1pa-xcojdzEDfVCALbC9RdKI9bUtHNW4uRdMvogpfqWewqsZ_4dP5P0bJ68BuY988Ug8nwzD6m2ZlLUkB9dOM0nsy4E_y1c-sj0_XTtACSXNIMkqDaWDCsJwW-ba0GJkj290nhSFmY9ymddpvVylRYKgDg3O9IPbdClEQ5IP2GoaQQWFply6C686e8gKlB9TBLbiuX-2Fw38I2UeDcy7rpUqE1iW7YNhqIKeqwmGx2t0uRFX8I2VPcuDt1QYfCWnPJKP_a_ctRwcNE7eAvJg2zlvEZtbYyulTh_rjVmmYjizR0I_U1a96ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پل ارتباطی لارستان به بندر خمیر بعد از حمله دشمن
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/676308" target="_blank">📅 12:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjAvXAP0xUj_ZKw2oZPe_iR-IoVf_PJAjQ9cft_WRd3AQ1Rka09qq7peirQMyRsQe7d5uGVtvziaxAIVt85XlNpUg6ImwpYiMmBdhlr5LixmXz1BOc_lIcVE0EvRMvAaaZRr4GzKE83x8fD-6tBgOXvTacUAO8qS77EGREHHZEMNzMN_M_f7xtwfYbB2djeZrMd3OiDx8Cg61FEKAd-KN3mW-_vX4mSuVLfgamiyOyUiC9PX0VOf-wA-XC_I7D_AMpgp2WAF1-GcIlgbKp5XFrtWczD1tfDSqKcOWa2kWA9ozbE0put9W40CBshTFZvaTQbxaD3RY0M6w40YCfa5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رؤیای رشد دوباره در غزه
خبرنگار ساکن غزه:
🔹
این دختر کوچولو هر روز از مادرش می‌پرسه: «مامان، پاهام کی دوباره رشد می‌کنن؟»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/676307" target="_blank">📅 12:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1130a19afd.mp4?token=C7ITcJXp9Cazer0KfAbZTKbyy7qCSipDkbZgnUB1SEhZoZxMisweSNpkW15gJ9l7Ti_2J0qq-9vUbI0NhJGr-IFCSKDj04Ng1p_9imerIJvJIMu9Z7U1S37R-UBDfrYbWWEZ8Fy0SKvT98lui6zrk_Chht_Zue7yx-ppMTcO7bIAPmk_oktIaDBkMTVxzPYVxnj2bADogv42X8O7JZEdNBl0GlDUawhXDkhZO0qO05SExjGp_pwEx-SAMimCmbwD8MzjVHAfLHP5ABHJRZBoX4DZFD6uIuyl1q68gNcYvkRC165Iy35DoDH5j79EpkGB0PBR5xndan6c_gTbooG6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1130a19afd.mp4?token=C7ITcJXp9Cazer0KfAbZTKbyy7qCSipDkbZgnUB1SEhZoZxMisweSNpkW15gJ9l7Ti_2J0qq-9vUbI0NhJGr-IFCSKDj04Ng1p_9imerIJvJIMu9Z7U1S37R-UBDfrYbWWEZ8Fy0SKvT98lui6zrk_Chht_Zue7yx-ppMTcO7bIAPmk_oktIaDBkMTVxzPYVxnj2bADogv42X8O7JZEdNBl0GlDUawhXDkhZO0qO05SExjGp_pwEx-SAMimCmbwD8MzjVHAfLHP5ABHJRZBoX4DZFD6uIuyl1q68gNcYvkRC165Iy35DoDH5j79EpkGB0PBR5xndan6c_gTbooG6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/676306" target="_blank">📅 12:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e952645be1.mp4?token=hmKjY9JKSSjAc_IYPonEDqhqvLvPZg4GDQwIgxHJZXBQJcOlB0IJ59-Jt8-qTCXgUz48tR7UTHj9B4mfc3BAdxr50wCcD0xGMaG1qemWuoi1OvjfybygqmIFmUtIONHXICQSWNSTktbF_Zx0UDd_ZdDu7ydhafEN0KeESP4lYQzxZvzskCSBv2PinJ_-nlKQehlFgSUMKMkAyJp62KmL6HA6UHc000BT1iof5ASGqh6_FGZEbJ--eeK0BfMNpq0zGmqX1U4P1w-vwt1bbihlaRdG7SyH3l8OpNUjT2APcpYyi5xQVLlGqFl5XfwxrmVyivHjC-oPhNfiv5lnNspN7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e952645be1.mp4?token=hmKjY9JKSSjAc_IYPonEDqhqvLvPZg4GDQwIgxHJZXBQJcOlB0IJ59-Jt8-qTCXgUz48tR7UTHj9B4mfc3BAdxr50wCcD0xGMaG1qemWuoi1OvjfybygqmIFmUtIONHXICQSWNSTktbF_Zx0UDd_ZdDu7ydhafEN0KeESP4lYQzxZvzskCSBv2PinJ_-nlKQehlFgSUMKMkAyJp62KmL6HA6UHc000BT1iof5ASGqh6_FGZEbJ--eeK0BfMNpq0zGmqX1U4P1w-vwt1bbihlaRdG7SyH3l8OpNUjT2APcpYyi5xQVLlGqFl5XfwxrmVyivHjC-oPhNfiv5lnNspN7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، خط مشترک تمام دل‌هایی‌ست که برای این خاک می‌تپند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/676304" target="_blank">📅 11:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رویترز: ایران در آستانه دریافت محموله‌ای از سامانه‌های پدافندی دوش‌پرتاب چینی است
🔹
تهران قرار است در هفته‌های آینده محموله‌ای شامل ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی دوش‌پرتاب ساخت چین، از جمله QW-12 و FN-16، دریافت کند.
🔹
وزارت خارجه چین در مورد این موضوع اظهار داشت: "گزارش‌های مربوطه کاملاً بی‌اساس است. چین به طور مداوم در ترویج صلح و پایان دادن به درگیری نقش داشته است."
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676303" target="_blank">📅 11:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676302">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXjrDbgjw0ydeWbkPwFZlMTK1Fz6iJSNPxlM4RlQHKTykWIGqXdjMG_bhA93F8Ad-RrCrJXUxRpEG3eW3_IO_8J9rlPGE75aqZFjkgju5YNPU3msqFWZPy5g6soRgWBnIBbbPCl-ctaR8YVO75flaKXzubzOaX6Dka-3Y1OV9GhT2Omt0ZtNZcYu7hhGUravTONXiUrbg16qLMoNaIpDY_iMNHu4FThpLrLl6ATfZw4BvKh_V0it7hWUITRybN9nUNpB1szC_A2tIfeOea7FojDyCc1CCYEZ535qT3WgIE5OdjL5uqHUpiUnypUUrXQIvPVszFA5RDrBAnfovw2q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
خدمت، از کوچک‌ترین کارها آغاز می‌شود؛ امسال افتخار خادمی را از دست نمی‌دهیم
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676302" target="_blank">📅 11:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e2199e5a.mp4?token=iYv3xUwdk-N2Te3Al5uh7xQR1AhcLQCxtfpZj65UINyWFQdGVsgpj39HoQe99gFw8t_Uzb7W3dEXbLpbtYhvJcCsjdbpFKwEzIcFpzo0oZhQiUG95ecbWTPbHYzAT-Nx35RPqFB0HRRMy6tn6v4SXhoyrCaex-RWyOqcqU5tdWU-e598mA9T128qaSeQi6lOnfi7oX6Yn5yu8uihCWiU8DTllwKizprw5TXceTl6PFOLOZNqBzS14fRggw9-jM8x2yNuKZyZ3lGDZuTd1mGIB3DSvEFjbPIZsq5S09h4ytCvCRrBjqBmn-4qV7ORaurl8J7SVNKFLp75i7mtvxUuAh2zMP5_ky0DPFBbedVnP-btavF73TtH1epr5GtGhJw-Ip_r6J-u7S0qCjGDefcSj2OyYk82qQCk58fzMGzg1KYde-5l8iw7oECi2Nak24fkVNOyQoxvQ9PQlXGJd5P0Qmnia-Wr_pSwaiWCNWnRmhbCGIuYpkBgX7GZfQMuJ1KPvftvUelo_ahgDNMb7mHBqcVdmwC1EinIncv3y9TWblVxNQ-TKgiPRr3XOVJuCow_meBZv7Flw_-jqUild638XXoZrpZkEbNtyPmalNdc7mzwHAE3objqFABhMZ4vpedSdXAW-6g-HRBDPNHzwew1ikjpfSlIW7A60bM99Rcb844" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e2199e5a.mp4?token=iYv3xUwdk-N2Te3Al5uh7xQR1AhcLQCxtfpZj65UINyWFQdGVsgpj39HoQe99gFw8t_Uzb7W3dEXbLpbtYhvJcCsjdbpFKwEzIcFpzo0oZhQiUG95ecbWTPbHYzAT-Nx35RPqFB0HRRMy6tn6v4SXhoyrCaex-RWyOqcqU5tdWU-e598mA9T128qaSeQi6lOnfi7oX6Yn5yu8uihCWiU8DTllwKizprw5TXceTl6PFOLOZNqBzS14fRggw9-jM8x2yNuKZyZ3lGDZuTd1mGIB3DSvEFjbPIZsq5S09h4ytCvCRrBjqBmn-4qV7ORaurl8J7SVNKFLp75i7mtvxUuAh2zMP5_ky0DPFBbedVnP-btavF73TtH1epr5GtGhJw-Ip_r6J-u7S0qCjGDefcSj2OyYk82qQCk58fzMGzg1KYde-5l8iw7oECi2Nak24fkVNOyQoxvQ9PQlXGJd5P0Qmnia-Wr_pSwaiWCNWnRmhbCGIuYpkBgX7GZfQMuJ1KPvftvUelo_ahgDNMb7mHBqcVdmwC1EinIncv3y9TWblVxNQ-TKgiPRr3XOVJuCow_meBZv7Flw_-jqUild638XXoZrpZkEbNtyPmalNdc7mzwHAE3objqFABhMZ4vpedSdXAW-6g-HRBDPNHzwew1ikjpfSlIW7A60bM99Rcb844" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر جبهه مقاومت: جمهوری اسلامی هیچ‌گاه حزب‌الله را تنها نگذاشته و حمایت از جبهه مقاومت همواره ادامه داشته است/ برخی تاکتیک‌های پس از آتش‌بس در پرونده لبنان، نتایج متفاوتی در میدان رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676300" target="_blank">📅 11:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Lsz7br1hi2IginFLYApMiCE5Eiik7MTHfW94PlcohQNYwfeWa62NoKYsBK7A9Og6nm9Ms4GYsOvQ22di9UHtvj_an79eQ9HI-32vwtOP7C5NxPzfraWCSK8Snq_4Bb9audshNlEZjT7NR8eZyGD6OVFRKAdT0JdUB5s7G2QI-k_dWpRaVsVz6Ji9S2Pu3344TqwadGTMqFZBnUcSDUC55mMYbJEM_1to7Jv8Itw6MxM1cIBfZsz3dFWkbO8VROK7rbGZCQXE06-MnpfmaBbBlBCqjBUcmwiJGKSyULE2yUU-cC-gqM4GaoFb-t58rw9iAM-quz4-EK_uvkCJTZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود معترضان به هتل نتانیاهو در واشنگتن
🔹
گروهی از معترضان به نسل‌کشی اسرائیل در غزه وارد هتل محل اقامت نتانیاهو شدند و علیه او شعار دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/676299" target="_blank">📅 11:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676295">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luwCJQO-HEJ9iUnQdg7FVI8XruzmX7gVFIDsnb2zpcnPNb9BdDYvDyrqU24DxIy5ZJz-F198k-XKDoTk8HEMKNZqIB6HW2NwgdsJ8Ro9AroDg54_ZIknXbnAdUV0shdu1luFllxRr1QKnkY4ZbSf-0mXOJmovmTNv1Y1gxctVz40MTrB5gaB06HSlBF-ZhG5sqRp6P0zU8GEhCfktXnS4W8fwsDPFVA9OmCet7XJGT6OcH01QdMgS0xk-rYSPrgIw0kARPmihA0k3k7693nbh32CNsRBbw_vSq6GqZTieUk4HeDr9GMe1s4KRTny7E8ZjlvERwpfpMWiISqj7sDz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5Ijbj9PB4cEY-qfBB-ie1g8h-ari9CcsXWfmSiwJyuepjf5mo2uDq_R0Ek1rKUt5ONdgT5NHWAPFYZDpJSX9c3lg0NnyTZimmZSlv51EhN-yUVqOAvT41hh5hJpdBe7h1mbU8ivJCOot3mF98yX-GG0hWQt_HfszOIJP50oM6LUsyY0tYxwhY9t3w2aRtYlTZlJlmAjWuO6SRJIdmTRliVTvS_-FhSNYCyyXqr9_lEy3r0nhrN5dUpxR5EULYkxTsvXDzs4-qAtsHgA6HT1YtRHeCzVLwJKWPi1aH3e6jvTjxGiNXd2cYblfhTEgOXDhQ-EBz_9D8JhRsIJxSelBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBOLZWRxGsIdth-zQY04G05HZWQtxUdJ91se50ezJrciurwO4Q12myExc6iLFRaExl46tKrXf0HBmu_EojregQHxHKoR9sW-a9KeT6ZaR5w1W03PZrvXiPZttXpdvUSx0sX3Z0QcDBQho5cjllp21Rcq-31JLmeKrMuKjAp2yQERNltms-58JGEU-rvtEbpiGu-V01K0VALEKH8auXrLvTRmrms0zmcZoueBo3tjNzevtzDXbRk9MXRkJNb-udjBuTyLPft5KngElTAT_e7TyIm-F6KlMVShaVRQcsOSRPBWrT91TdzmgfHa2Ai3wEiZ9KkxzZ4IrMkfvmPogiSqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVOvfBdM52YjcMt2RfRUfGtlcIBiGF5Q0nT6fLjYSGhd5Ri1wMd2rITlVJdVUKP900UJEXxpxWBBlTLWH-R_H8Rz6WIkMukpKYactMeJPBZ-PuE9p_pzvY3HofcjOYiIMbzLxwnDVTuM0saiDAfmA85pNynX96EcZ8cJy1x-rYXYZKP0c-LCPMJ1MQ8Kn4hW2PL318YWrrfMz1SyDTbVwDNYdHPcZ65MutOdrK_PharITwmG9sFiKKMUTn_JDcNghcfWGHY6ejjBh17Za2K8zpJeKP1GkZL4fI1rXTW88YUtUvJ6fH14eGOrHJBPR6A38Xfw3z0gtSt9v1VkvsMwVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویدئویی دیگر از جنایت آمریکا و عربستان علیه حشد شعبی در نینوا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/676295" target="_blank">📅 11:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676294">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pobd8mnXGErVGjb4gPhxScoia5fmwmMiP9TPFg3l9-I-YDL5K7MvXbTXGTmI8WorKqlaO4nzYjHf5bweuOXnMUQr55HSTRVlT-nYvoIWqawq4Bzljs0n93szk3UrvpdK8yK7sSjSkyq9KG1Jvr8hUVpMRJG7j5RPvdksDBqpXvZ1MQX7m2YBSVaG8AF1BKFJT8OCMPBsQJjbgKtyPNKAFKz0cWUqxl_yEECngqbZUH8rts-Oj1y0rAQCFH_1TekQYlK6jDUzkPBiOSaL-eXgpWCPfA2tamf1OOs8z4Ci-CGERQ1OWgCezN4wVQLrtuLO983MjREOo8z0x8bg1kzslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه اسرائیلی: نتانیاهو از ترس ایران مخفیانه از واشنگتن خارج شد
رسانه تایمز اسرائیل مدعی شد:
🔹
گزارش‌ها حاکی از آن است که تلاش ایران برای آسیب رساندن به مقامات ارشد اسرائیل، باعث خروج مخفیانه نتانیاهو از واشنگتن دی سی شده است.
🔹
ایران تلاش‌های خود را برای آسیب رساندن فیزیکی به مقامات ارشد فعلی و سابق اسرائیل، از جمله گروهی از وزرای ارشد فعلی، افزایش داده است./خبرفوری
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/676294" target="_blank">📅 11:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676292">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ورود معترضان به هتل نتانیاهو در واشنگتن
🔹
گروهی از معترضان به نسل‌کشی اسرائیل در غزه وارد هتل محل اقامت نتانیاهو شدند و علیه او شعار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/676292" target="_blank">📅 11:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676291">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82f8a748f.mp4?token=aptQa-_5IRZifBBamw9Fm4QWGJkeOTGCLXH5AXpQ6t1m00gsPsq0Up5kBAEp2sje5ixNzEMI4fGvPOTXUElRfvS0UI04BtFp3h05FpBDXPC23vGBhv8WFNQD7hjpcuIjjl9X4-Oh7l4Z2Hd_UF3O1Y_jC6K6aEwFARuTJ9iF4krX1kwkA41f_WJfZibByW9ZADP6cjCw7PY_UVEGUu_-p01U7EMFQdORvZA9zlEBO37o3qyc9eSX0mhQsckZ94s1gSDU6lLQPwt3rLxorss2AHDzS-poWfT8owPUV-dSDCKqQS3I6jAonn3uQdbiIJSGTbLtPZnbfalmCB-mjB5RAW6Ah5pg4FiZ9PeERW4W9peI8OPiJEWxKn3nnB0XU2_L2CyRmye4uW62M2yKnIeOcvQS9Gp-_BiBIV7ZOATY1UwOKOPzU3jLFf-Fwt6GH5sN-dmmiCum1WKmp6LAdwYassNtzaw8Pcmi9PYTHup27i6MEMlLnugfFT29H5jnhq6ioy9Ji0HRzoqBEzwJAyzcy2BNcnQvgJ3F2eCWmDx_t1zcbZzPjl_tyJCo62CicncRvfxKZLpafrtmFJLniApKjlhJ5tK-WeRyEkiELOMF-qL8O0jMCCBFAmF98v4hn-stPzOxP3W16B2T9EL3rH6lZrrNPtF2DBksvQ7333kMYeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82f8a748f.mp4?token=aptQa-_5IRZifBBamw9Fm4QWGJkeOTGCLXH5AXpQ6t1m00gsPsq0Up5kBAEp2sje5ixNzEMI4fGvPOTXUElRfvS0UI04BtFp3h05FpBDXPC23vGBhv8WFNQD7hjpcuIjjl9X4-Oh7l4Z2Hd_UF3O1Y_jC6K6aEwFARuTJ9iF4krX1kwkA41f_WJfZibByW9ZADP6cjCw7PY_UVEGUu_-p01U7EMFQdORvZA9zlEBO37o3qyc9eSX0mhQsckZ94s1gSDU6lLQPwt3rLxorss2AHDzS-poWfT8owPUV-dSDCKqQS3I6jAonn3uQdbiIJSGTbLtPZnbfalmCB-mjB5RAW6Ah5pg4FiZ9PeERW4W9peI8OPiJEWxKn3nnB0XU2_L2CyRmye4uW62M2yKnIeOcvQS9Gp-_BiBIV7ZOATY1UwOKOPzU3jLFf-Fwt6GH5sN-dmmiCum1WKmp6LAdwYassNtzaw8Pcmi9PYTHup27i6MEMlLnugfFT29H5jnhq6ioy9Ji0HRzoqBEzwJAyzcy2BNcnQvgJ3F2eCWmDx_t1zcbZzPjl_tyJCo62CicncRvfxKZLpafrtmFJLniApKjlhJ5tK-WeRyEkiELOMF-qL8O0jMCCBFAmF98v4hn-stPzOxP3W16B2T9EL3rH6lZrrNPtF2DBksvQ7333kMYeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرتضی سیمیاری،کارشناس مسائل منطقه: جامعه اطلاعاتی آمریکا، نتانیاهو را «پیک دروغگو» می‌داند و سفرهایش به واشنگتن را منشأ دردسر برای کاخ سفید توصیف می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/676291" target="_blank">📅 11:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ماجرای دستور فرماندار کاشان برای ازدواج فوری کارکنان
راعی، فرماندار کاشان در
#گفتگو
با خبرفوری:
🔹
ما برای بحث آموزش آمار می‌خواهیم برنامه‌ریزی کنیم و ببینیم آمار مجردها در ادارات ما چقدر است تا تسهیلاتی برای ازدواج جوانان فراهم کنیم.
🔹
همچنین آسیب‌شناسی کنیم به منظور شناسایی علتی که تا این لحظه نتوانسته‌اند ازدواج کنند و آموزش‌های پیش از ازدواج برای انتخاب آگاهانه را داشته باشیم.
🔹
برای اینکه پاسخ نهایی شود به ادارات اعلام کردیم یک هفته دیگر فرصت دارید این اتفاق بیافتد وگرنه قبلا مکاتبه شده بود.
🔹
فرماندار کاشان پیش از این دستور داده بود که ادارات باید ظرف یک هفته آمار کارکنان مجرد خود را احصا و برای تسهیل ازدواج آنان برنامه‌ریزی کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/676288" target="_blank">📅 11:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قلعه لک‌لک‌ها و کوه‌های رنگی ماهنشان زنجان؛ از بی‌نظیرترین و زیباترین نقاط ایران
🇮🇷
#ایران_زیبا
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/676286" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf3d7fe7b.mp4?token=UJLw02e4PMwgIAjkrB7Tm0SzlZbzNTuuyaa69CqiQy0l8SsqGpkoiR4xbyl-LxeWpJdS3nS16u1uvCTknMolpLzFzjchTMwBzIISmfabwOocKYBRjc5Qo6pzIgsR51rKPJU5Q44YsKkPf-UBth5YuZzvVgBWo7Smibbz70S27tuHTJa7-Z_U2E7lvrYrGdNfoNoMnlqKRPCuVBd8iWrcvsDY_XxoWfhBPGvaiqhDzQUEa1dWn0xzGRsTZFtGC9qcVJQRIRrKHxYhFJpFY0qSm-BY_yd1kUNC2UqSzvIYtWwEDv4KKYRFTEVAmQrJKTabbxesMcT30dOu7fVSLriL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf3d7fe7b.mp4?token=UJLw02e4PMwgIAjkrB7Tm0SzlZbzNTuuyaa69CqiQy0l8SsqGpkoiR4xbyl-LxeWpJdS3nS16u1uvCTknMolpLzFzjchTMwBzIISmfabwOocKYBRjc5Qo6pzIgsR51rKPJU5Q44YsKkPf-UBth5YuZzvVgBWo7Smibbz70S27tuHTJa7-Z_U2E7lvrYrGdNfoNoMnlqKRPCuVBd8iWrcvsDY_XxoWfhBPGvaiqhDzQUEa1dWn0xzGRsTZFtGC9qcVJQRIRrKHxYhFJpFY0qSm-BY_yd1kUNC2UqSzvIYtWwEDv4KKYRFTEVAmQrJKTabbxesMcT30dOu7fVSLriL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش شهدای حشدالشعبی به ۲۰ نفر
🔹
حشد الشعبی در بیانیه‌ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر شهید و ۳۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/676285" target="_blank">📅 11:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.
🔹
جنگنده‌های ایرانی در مسیر بازگشت مورد اصابت پدافند دشمن قرار گرفتند که با تأیید آزمایش DNA، پیکر خلبان سرتیپ دوم مجید کاظمی به کشور بازگشت؛ سرنوشت ۳ خلبان دیگر همچنان در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/676282" target="_blank">📅 10:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
افزایش شمار شهدای حشد شعبی به ۱۰ نفر   حشد شعبی:
🔹
شمار شهدای ناشی از تجاوز سعودی- آمریکایی به استان نینوی به ۱۰ شهید و ۶ زخمی افزایش یافته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/676281" target="_blank">📅 10:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676279">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfUGOXgYoEj0sAMafutXLi7G6ejLICAbxiVaw52b-JH16rE-CL67OuVJvyBRsU65YBb0bRMOvowS_s73NZ9cfDxfCL1eTlfsuezn1RDDOMiWY74NpGpw54ZEB3zmUqGz1C35QY59sNEYK7hKOxaGLjdLIakBAKAdHYPzNuJkMht736ofcwkLrk50tLV5gjyvRhFrHNudAIOyW56mp0mi6pCUi1tBewzR6w45-VQ6sGk0wjgh1MAkqogjCAmsI90rb2WWtin1WTRFxF6077bdG2ywZZMojxGMHZ4x6r3UcRbJKQ7leKbRSdpEiYvf2l_sP0FyTbse2wINg-B48cPcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
می‌دونستید طیفای رنگ بنفش چند تا اسم مختلف دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/676279" target="_blank">📅 10:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc587e9bbf.mp4?token=ARisnuazcYEK7gWIgULmjXFIoZebv5LOVLUSaLIQFi4_GoxghO0yGY9wwgxnhZswUqSkhnirtJw7VGyDC8gxQ9w9BGeVuM0ZtYi6KmLAS9DpLdEhCQfwfU-jkjuJN6DsNeDMV_R4Z8HlU6ValhH8TKL0dJrG8imBwDGD3lkwoP1fjuPXqXtasuuIWUxIY44sMJf9wdndo-rAIPOwhs-g-o67E9KK_fdsOSbo5gvwa5ZU-BXVX_oKOjlWy3dpteVBsvxlaLo9_BRGX7NWp6LX6iF4f47IOo7FnUSneBH4thh2Hc4isVqfOrGPrfl4ypJbSxJJYSKCQ0ovx7sSTWFK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc587e9bbf.mp4?token=ARisnuazcYEK7gWIgULmjXFIoZebv5LOVLUSaLIQFi4_GoxghO0yGY9wwgxnhZswUqSkhnirtJw7VGyDC8gxQ9w9BGeVuM0ZtYi6KmLAS9DpLdEhCQfwfU-jkjuJN6DsNeDMV_R4Z8HlU6ValhH8TKL0dJrG8imBwDGD3lkwoP1fjuPXqXtasuuIWUxIY44sMJf9wdndo-rAIPOwhs-g-o67E9KK_fdsOSbo5gvwa5ZU-BXVX_oKOjlWy3dpteVBsvxlaLo9_BRGX7NWp6LX6iF4f47IOo7FnUSneBH4thh2Hc4isVqfOrGPrfl4ypJbSxJJYSKCQ0ovx7sSTWFK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فکر می‌کنی بدون گوشت و مرغ نمی‌شه یه کتلت خوشمزه و پرپروتئین درست کرد، این ویدیو رو از دست نده
😍
مواد لازم:
🔹
عدس
🔹
هویج
🔹
سیب‌زمینی
🔹
پیاز
🔹
آرد سوخاری
🔹
نمک، فلفل سیاه، زردچوبه، پاپریکا و ادویه دلخواه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/676277" target="_blank">📅 10:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ونزوئلا سفیر ایران را احضار کرد
ادعای خبرگزاری فرانسه:
🔹
وزارت امور خارجه ونزوئلا در بیانیه‌ای اعلام کرد که این کشور سفیر ایران، متحد دیرینه خود، را احضار کرد تا به اظهاراتی که «تحقیرآمیز و نامناسب» تلقی شده بود، اعتراض کند.
🔹
مقامات ونزوئلا، مشخص نکردند که به چه اظهاراتی اشاره دارند، اما ویدئویی که به صورت آنلاین در حال پخش است نشان می‌دهد که عباس عراقچی، اخیراً گفته است که ایران در مورد مذاکره با آمریکا «ونزوئلا نیست»./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/676275" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران پیشنهاد عمان را رد کرد
ادعای وال‌استریت‌ژورنال:
🔹
ایران پیشنهاد عمان برای تقسیم تنگه هرمز را رد کرد و خواستار کنترل بیشتر شد.
🔹
عمان که در آن سوی تنگه و روبروی ایران قرار دارد، یک طرح موقت برای ایجاد خطوط کنترل مساوی پیشنهاد کرده بود. اما تهران رد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676274" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxpDq11L7v8NPAIpHSIZ17ee_pIBovzp2tmkF46BkrGbrImNPj7oXUT0k6FjAKeq-P723jbP42ih7KfBBybSvFUoV4SUiIc970xQ9-dD_QeXMlhjQOCHJi14fX_H1_XPoiE6qdL8C_TJhMowHkmUiFgJwSJPIhd10uqrp1Y6YPpimBI-UMD8UqXHMuBEywnicOUeD-msHBe80YkTpam-SJ-jxxYmUbrgVtMHpPTufafc3807xbkyPVGLq4WkOvai4q_XFaKjksV-OGuPSflvnqpMgkvswi8SaQ1WAcR5OVfZAP96Csl9NQXVfG1w-Vfn6JTw_OSrm2rHsXWluGh9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز سلامتی در یک فنجان چای ترش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/676273" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676271">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هشدار پلیس فتا به زائران اربعین: برای جلوگیری از هک شدن اطلاعات گوشی، روی لینک‌های مشکوک وام اربعین، بلیت و اسکان کلیک نکنید و از وای‌فای‌های مسیر استفاده نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/676271" target="_blank">📅 09:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676270">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsJKEwoE90engAUU7pG8Ar2sPPeRs4yUI9MCE0-baWJqHSr0pV0cweZ1VswB6GA-modhnGeSyZKcEu_u6dKdKMrimtfi30F1Cwn71WWjCOFPlrkoKtbbub4ALR3aIgsFlF-rkGTa_9Xlil74EABjFC11sKF0t2GSPPCgDEXwdPBG72LmApnb2RoCR5_Wy2hmIyGwK69CDKyHmQEkPYLkraZu3DxW7zm0AQS5F3pfqLDnPZ2AYBCuYrmwaxsTA9Nvj4-Y2KcZjuX6RWsCQEOB6cJ35d8BoohcSx00dmmeNY8OcPtE0jR8Qj5DHb2AHeIvnSCrKKd2NxHjIOUZoKqY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش شمار شهدای حشد شعبی به ۱۰ نفر   حشد شعبی:
🔹
شمار شهدای ناشی از تجاوز سعودی- آمریکایی به استان نینوی به ۱۰ شهید و ۶ زخمی افزایش یافته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/676270" target="_blank">📅 09:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676269">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59d89d7bb.mp4?token=WRhL0vR7MhCWKqjwYmybUBDRzvtnZQoFNdifqwzQ1VvCrOgy3IAXTle4Dc3bdyvCe-RTxNf4otvX5sRrfiu8Biaa4SWx-wzEgt5pbf0pnStL2edkEeb3sG2Y2vfCYdokvPP0mJH0akARO8HkFOUwiBegDD5oUBdrIGFDdjXGvlSO7Enw5ChHN0JZNq2z2BWML-ThFGVpmzVVZGUGZz_45I1qt3sAgbre7vFtXR-KfxW2losyP-Fc0MpnPKEsEUexYoDE_320y_n5dMpse3lY2DVphVZ_zNdsOlC9wBfFZYWmxIP7T4DeFUCdbhYBHaSV6ooZpmkYZBObFAaG6t5voQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59d89d7bb.mp4?token=WRhL0vR7MhCWKqjwYmybUBDRzvtnZQoFNdifqwzQ1VvCrOgy3IAXTle4Dc3bdyvCe-RTxNf4otvX5sRrfiu8Biaa4SWx-wzEgt5pbf0pnStL2edkEeb3sG2Y2vfCYdokvPP0mJH0akARO8HkFOUwiBegDD5oUBdrIGFDdjXGvlSO7Enw5ChHN0JZNq2z2BWML-ThFGVpmzVVZGUGZz_45I1qt3sAgbre7vFtXR-KfxW2losyP-Fc0MpnPKEsEUexYoDE_320y_n5dMpse3lY2DVphVZ_zNdsOlC9wBfFZYWmxIP7T4DeFUCdbhYBHaSV6ooZpmkYZBObFAaG6t5voQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از شدت زمین لرزه دیروز در ژاپن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/676269" target="_blank">📅 09:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
منابع عراقی: در حمله دشمن آمریکایی سعودی به مواضع حشدالشعبی در استان نینوا ۸ نفر شهید و ۴ تن زخمی شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/676267" target="_blank">📅 09:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad8f4b979.mp4?token=IOdhQ3BXDGJYT-nF_H9ka-RQGLXWcZUs7ay1FB7jBOlIPNCxiGMHcDIorTDhbB25XOIe4z2IEAqwlvlnq6pk1xK0-uZOkWeX7e1EPyYc7wh399JjRNegnfFE44XUY6bLN1y0Tz0cV_ENWQtyw6tCzZ_kr8iitoEGUe6FA5yAytL-hf3tI2spN856Z52ZXjtwuRkNvZuI7Idw9Db486AnMaQBrr80LhkBwuGe4U6tD-H5hkc7YvF9XaKsycqyajSuuyAjinVQwM9WQQMjH7gP0FOXOnvX23GxG8H74rt7znJ_diBvh2fEdjpzFeEUkTBGy5sJPegH3A90zPvZxei6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad8f4b979.mp4?token=IOdhQ3BXDGJYT-nF_H9ka-RQGLXWcZUs7ay1FB7jBOlIPNCxiGMHcDIorTDhbB25XOIe4z2IEAqwlvlnq6pk1xK0-uZOkWeX7e1EPyYc7wh399JjRNegnfFE44XUY6bLN1y0Tz0cV_ENWQtyw6tCzZ_kr8iitoEGUe6FA5yAytL-hf3tI2spN856Z52ZXjtwuRkNvZuI7Idw9Db486AnMaQBrr80LhkBwuGe4U6tD-H5hkc7YvF9XaKsycqyajSuuyAjinVQwM9WQQMjH7gP0FOXOnvX23GxG8H74rt7znJ_diBvh2fEdjpzFeEUkTBGy5sJPegH3A90zPvZxei6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پالت‌های رنگی اینگونه ساخته می‌شوند...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/676266" target="_blank">📅 09:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676262">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b0a8dc2d.mp4?token=G3vGTYmPIzVJAHeXNktC8NmchvneOtiLoxGjzhnMus0knHDSB4bf7AD7zCvEi32xRonJ8V9RgFq1t_h-8aIhp4Y5TYB8Jrj2o6RcvSJ8BQX1aHV8Dr6x15NV8Ah5TxQwHovd9kp6ax8QEN4oVx3udFQDbVId079GYNa4KpSjdNs-FCWjVf8v8pQTdW73OTN-M8VS6KyL2cUA9ExEAsGOFouu2-ptTqCvSuAaFFy7eNoSBLRnLPuB6n4ne7qdee_Edc4wKCDgcbs1QsudUajrp8ff3g9DJTBxABu_twWKWwMqbcTelcSNKF7ViI-q2_wlVbIWFnEm5YP1BU8M9HQVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b0a8dc2d.mp4?token=G3vGTYmPIzVJAHeXNktC8NmchvneOtiLoxGjzhnMus0knHDSB4bf7AD7zCvEi32xRonJ8V9RgFq1t_h-8aIhp4Y5TYB8Jrj2o6RcvSJ8BQX1aHV8Dr6x15NV8Ah5TxQwHovd9kp6ax8QEN4oVx3udFQDbVId079GYNa4KpSjdNs-FCWjVf8v8pQTdW73OTN-M8VS6KyL2cUA9ExEAsGOFouu2-ptTqCvSuAaFFy7eNoSBLRnLPuB6n4ne7qdee_Edc4wKCDgcbs1QsudUajrp8ff3g9DJTBxABu_twWKWwMqbcTelcSNKF7ViI-q2_wlVbIWFnEm5YP1BU8M9HQVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله
🔹
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/676262" target="_blank">📅 08:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شهاب‌های آتشین در راه‌اند؛ بهترین زمان تماشای آسمان فرا رسید
🔹
همزمان با اوج‌گیری دو بارش شهابی نادر «دلتا آکوارید» و «آلفا کپریکورنید» در بامداد ۸ و ۹ مرداد، آسمان صحنه عبور شهاب‌های آتشین خواهد شد.
🔹
رویدادی کم‌نظیر که با وجود نور شدید ماه، نوید یکی از جذاب‌ترین شب‌های رصدی سال را می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/676260" target="_blank">📅 08:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31262d9f8e.mp4?token=RYQ4HYUhIxM7wu9Mz-_XkHhVmQeCT8Pzh0XS3s_7IIzAQi8DIaYBF4xCJB_bq_mBqFINmN9ipMZuT1j3o6wzlddvjFZwv0rX3lQCrnt03HVw4zMWW2iOEVFKT5GP26uo0mH0un3_L6FBFu7_CvR6szFkraY61ntzqrg_o-iqcTKO-52Av3Hv34wDk8FcXA1qMfvRejh8WUsdX8CP4CO_d9ieUJwB0T23dmGw4W-90dgXbXszdauZOQZkwOPC17TZOa3A5ekOzqrAxfCvezAqTTfSNZ08m6UJo9pryZCCUHKKQaaWrxeyRvOmZ06bQo41KJQ6ewyZb8RknSwky8BpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31262d9f8e.mp4?token=RYQ4HYUhIxM7wu9Mz-_XkHhVmQeCT8Pzh0XS3s_7IIzAQi8DIaYBF4xCJB_bq_mBqFINmN9ipMZuT1j3o6wzlddvjFZwv0rX3lQCrnt03HVw4zMWW2iOEVFKT5GP26uo0mH0un3_L6FBFu7_CvR6szFkraY61ntzqrg_o-iqcTKO-52Av3Hv34wDk8FcXA1qMfvRejh8WUsdX8CP4CO_d9ieUJwB0T23dmGw4W-90dgXbXszdauZOQZkwOPC17TZOa3A5ekOzqrAxfCvezAqTTfSNZ08m6UJo9pryZCCUHKKQaaWrxeyRvOmZ06bQo41KJQ6ewyZb8RknSwky8BpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ حرکت ساده روی تخت که می‌تونه به بهبود گردش خون پاها کمک کنه
🔹
اگر احساس سنگینی پا، خستگی یا علائم اولیه واریس داری، این ۳ حرکت رو هر روز چند دقیقه انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/676257" target="_blank">📅 08:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
نتانیاهو به فاکس نیوز: من در مورد توافق با ایران شک دارم و این را آشکارا می‌گویم
🔹
هر بار که توافق نزدیک است، تندروها می‌آیند و به کشتی‌ها در تنگه هرمز حمله می‌کنند.
🔹
موضع ترامپ بسیار واضح است و ما تعهد مشترکی داریم. ما نمی‌خواهیم ایران سلاح هسته‌ای داشته باشد.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/676256" target="_blank">📅 07:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676254">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwq9XLuhOZc3uk-9pniJFB-MutSO-fGJWhbTgnRuheptzSPhf_kJev9CzR6OoybpCF_Uq35IY8obo73glXhFZjk27bQEyP5S2uMw7aXxf9U-zmdBXC1ho-6j6NEZeS37BvYpv6NXbsOW-LowL0Npjb6flO4XCtRFtxi_04KXWDcyQXSJXsLv2frCs4BNQwcBLZfIN7JezG1t-4DpwMgBptIpxHxsSB3u7oHcwiOUjFVjuNPkcvyXOB2rNQC2LxKSwmf_EYrdJZepzgXcjakXLOdDCr4i6vYHxvNbI7tFdhQNjAD_WGj825PRbAQNzrZqW-cyvfvhnSW9e9pEgvKVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۷ مرداد ماه
۱۴ صفر ۱۴۴۸
۲۹ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/676254" target="_blank">📅 07:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXLc-pnJrGCrW285JaKu1qJnjI102peDYXzYl6RugWLNUFYkSxlUThNl93UmAJP6HjnBeNBA3GS_Ft__oXceCTBKAXvOwyvtyhVXXAlSHAWIPgCjN_1CVAxK2fSQrNaQlIEzfwM1bqnqzEJtjF7tbWpCa3FSvIaTKM4SpTZG4lPujykuoYkbJfTEMiJKdqf8DuUuLhXnZ9tktvTpy_Ypb_DPVwxExaLaBFrJZJ6iSm456sqbHKJNoAa9tXZYZgSUNfYq-pD2a6CcErS6SsrlgzyngOgy8GdjMqEtvp1BHAHTN9dM4K9iyqI09kqwVlBtRnAKL229gnF6eZS0JPEYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyY2IvGzogpgNqoOqg4MG187i2QQsrj252iO6naCFKZApYjQfGpScs5HvlJsCs5hXFl4W6ZsY0kXSyQFDAa7wkb1_qd2fe-3D-UduXAZS2KKEDAvZ5nG4YV5REwGNj46K9RBJp7mJFMl4kRbD2L8PKVY9BkfmHIm9ESwJf258HJVWdeQxOGLEF7X6iyo6pZGAafT8pgkb6BnY8tSZe-eGNKTy0V9FrB_oRwzBL8datwa74-VSn7UzgQ1Im9Dvmw_P2JVNPM5uClg8pO-W5pHttpVw7Xiexzbs4wytmjWsp3Gfliw03o5fUeP209EccWX7yTyrmDuk7knW12WZJpyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIpxsgWXXLQgAGP9VWDJD6TmOZmbjHxN_XTeD_dB9g7lugjDkOiQjWIoxiVZ8Mbr26zUU2HIFU9va0wSxFWYgrpoJ3a1SCLCQxdJzPhjdFhQLLDvh2IuZ1wGJn-pPAR_IFBmjJ6CEJJmFO8r_s0EMKTLSmlaXlp8XIbxLnBb545DkODuX53GZxNx3E8qaceH4mIPqhCljYOnnYeOqF_DLFqaoL12HqEz8KbGSUXaXxk-hpX-svItpfa5eZK6SSGXbUFmqbrzpRwVRfXGZE-mYnmmLraOVNwRAecbQ-J_1EXgGcKm5euDYUUDNlmjDSmZQVaJzd0Ey9iq5Y7Fv9MAEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احراز شهادت یکی از قهرمانان سوخو ۲۴ ارتش/ ورود پیکر مطهر شهید امیر سرتیپ دوم خلبان کاظمی به کشور تا ساعاتی دیگر
روابط عمومی ارتش:
🔹
این شهید عزیز خلبان یکی از جنگنده‌های سوخو ۲۴ ایرانی بود که در جریان حمله ۱۱ اسفند سال گذشته، خسارات سنگینی را به پایگاه العدید آمریکا در کشور قطر وارد کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/akhbarefori/676250" target="_blank">📅 06:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اولین واکنش الحشدالشعبی به حملات هوایی آمریکا و عربستان سعودی
الحشدالشعبی در بیانیه رسمی اعلام کرد:
🔹
صبح امروز چند پایگاه رسمی سازمان الحشد الشعبی در نقاط مختلف عراق، هدف حملات تروریستی نیروهای آمریکایی و عربستانی قرار گرفت. بر اساس اطلاعات اولیه، این حملات منجر به شهادت و مجروح شدن چندین تن و همچنین وارد آمدن خسارات مادی به برخی ساختمان‌ها و اموال متناوب به این سازمان شده است.
🔹
ما این حملات را تنش‌آفرینی بسیار خطرناک، نقض آشکار تمامیت ارضی عراق و هدف قرار دادن نهادهای امنیتی رسمی کشور می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/676249" target="_blank">📅 06:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
منابع عراقی: در حمله دشمن آمریکایی سعودی به مواضع حشدالشعبی در استان نینوا ۸ نفر شهید و ۴ تن زخمی شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/akhbarefori/676248" target="_blank">📅 06:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۲/ پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن هدف موشک‌های بالستیک قرار گرفت    فرماندهی نیروی هوافضای سپاه پاسداران انقلاب اسلامی:
🔹
در پاسخ به اقدامات تجاوزکارانه ارتش کودک‌کش آمریکا، ساعتی پیش رزمندگان شجاع نیروی هوافضای سپاه،…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/akhbarefori/676247" target="_blank">📅 05:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676245">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۲/ پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن هدف موشک‌های بالستیک قرار گرفت
فرماندهی نیروی هوافضای سپاه پاسداران انقلاب اسلامی:
🔹
در پاسخ به اقدامات تجاوزکارانه ارتش کودک‌کش آمریکا، ساعتی پیش رزمندگان شجاع نیروی هوافضای سپاه، پایگاه هوایی و مرکز فرماندهی مرکزی ارتش آمریکا در اردن را با چند فروند موشک بالستیک هدف قرار دادند.
🔹
تا زمانی که تهدیدات علیه جمهوری اسلامی ایران ادامه دارد و اقدامات غیر قانونی و شرارت آمیز نیروهای آمریکایی علیه منافع ما در جریان است، مقاومت هم ادامه دارد. تهدیدات مقامات آمریکایی و مداخلات غیرقانونی علیه منافع ما باید متوقف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/akhbarefori/676245" target="_blank">📅 05:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676243">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76e22916a.mp4?token=fgHrraenjUCHAAGZoQKYx0U-hed3EyJxZ2HDnOjtkAW7Si43NX7q6JMWlfELqFeTymRM2gMrxC-N8kUersfGCEiuDTGB1qnT_a_VNKbZAgLXvp1RJ7GrqYnsKi9w9PPnBGe9-Z-eF7zks4R4BeuLvbaL5McE3pf5qqUPKpOXFqFYSoejle2G1h2C3RrOiu3_2CafnlSGzMP-FAP1qO0IyUOCVcRJPAZsWoFLfyBQb5Wk4Lzm6jnnY_yUZ2MDitekvJevUb110G_H4xeaWnTB0aehj3Rem9r1FVHwHtWx08T7C2smVxEdez15DMKjaitrcSkx94zB3YWXNbfmcHHsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76e22916a.mp4?token=fgHrraenjUCHAAGZoQKYx0U-hed3EyJxZ2HDnOjtkAW7Si43NX7q6JMWlfELqFeTymRM2gMrxC-N8kUersfGCEiuDTGB1qnT_a_VNKbZAgLXvp1RJ7GrqYnsKi9w9PPnBGe9-Z-eF7zks4R4BeuLvbaL5McE3pf5qqUPKpOXFqFYSoejle2G1h2C3RrOiu3_2CafnlSGzMP-FAP1qO0IyUOCVcRJPAZsWoFLfyBQb5Wk4Lzm6jnnY_yUZ2MDitekvJevUb110G_H4xeaWnTB0aehj3Rem9r1FVHwHtWx08T7C2smVxEdez15DMKjaitrcSkx94zB3YWXNbfmcHHsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی-سعودی به پایگاه تیپ ۳۰ حشدالشعبی در استان نینوای عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/676243" target="_blank">📅 04:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676242">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
منابع عراقی: هواپیماهای جنگی دشمن سعودی-آمریکایی همچنان بر فراز شهرهای کربلا، بابل و نجف در حال پرواز هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/676242" target="_blank">📅 04:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c0612bb1.mp4?token=mB5X4XANX5Icd_yy3AQBOutOyj9cyQBllqNAmdS95Z8WUz2ib9MLtbNLFfcIPgxfj78e_tmyaLJ6aFHFQDlqIGbfffrObv4SxoCwMUFlRqcmvrqRQOejzcGzsQURaJgkV_v8pDT1xnmo36VEN92FePPpCxw-HiNc0jFlxqowEAR7H4kfeiq0qTujGLMQRqd7_7ehAzh1NTOlgjZZrJWq9CSG7U_Ja-XLy09-bCNnsZRxDZrFt8ABm7ILzJvyee-EFCImRWTbs95iJVhjLn6lxDvWk7Jd1_J7EXcSYI_ldl7QTd-cnL62cQNrxEsBGwoNUCPuzgZ4SoD7uqgqgTdqMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c0612bb1.mp4?token=mB5X4XANX5Icd_yy3AQBOutOyj9cyQBllqNAmdS95Z8WUz2ib9MLtbNLFfcIPgxfj78e_tmyaLJ6aFHFQDlqIGbfffrObv4SxoCwMUFlRqcmvrqRQOejzcGzsQURaJgkV_v8pDT1xnmo36VEN92FePPpCxw-HiNc0jFlxqowEAR7H4kfeiq0qTujGLMQRqd7_7ehAzh1NTOlgjZZrJWq9CSG7U_Ja-XLy09-bCNnsZRxDZrFt8ABm7ILzJvyee-EFCImRWTbs95iJVhjLn6lxDvWk7Jd1_J7EXcSYI_ldl7QTd-cnL62cQNrxEsBGwoNUCPuzgZ4SoD7uqgqgTdqMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی می‌گویند که پایگاه‌های «الحشد الشعبی» در استان‌های کربلا و نینوا نیز هدف حملات سعودی-آمریکایی قرار گرفته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/676241" target="_blank">📅 04:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رسانه‌های عراقی: حملات موشکی و توپخانه‌ای موکب‌های حسینی و زائران را هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/676240" target="_blank">📅 04:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آمریکا: به همراه سعودی به عراق حملاتی انجام دادیم
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که به همراه ارتش عربستان سعودی، حملاتی را علیه پایگاه‌های مقاومت در عراق انجام داده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/676239" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
آمریکا: به همراه سعودی به عراق حملاتی انجام دادیم
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که به همراه ارتش عربستان سعودی، حملاتی را علیه پایگاه‌های مقاومت در عراق انجام داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/676238" target="_blank">📅 03:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109dca722c.mp4?token=Ivxbu5coZyDNcApHYB0K7aZjWutdCauklql1GnYeYCwXS37mO77ktivHpK7tPYaHPCA3hyMmVj1_VT5t0x0oUa7QIUztiYC6K4i9UoCjUkSDrG_fSmkKzVxClUK0Zabaalk5YdpVSRkT1j05w0IygY6_6frWA4xs09kVJdPKOm8erovcjBFgxlXsnp_0NWAXVMQjMiNtwvAlNkSMJcCMLG5bV1YbZTk3D9d4tFzeIZ0EClawG5WcGOhfRcFIbIheITWWhOGwbiR8iXCJ71rLXZByw7jN_6DbSTIE9PFgC3h-GhqI54lgr4j5kgswSJTyVHkcJHlOx9P0xtteMtHzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109dca722c.mp4?token=Ivxbu5coZyDNcApHYB0K7aZjWutdCauklql1GnYeYCwXS37mO77ktivHpK7tPYaHPCA3hyMmVj1_VT5t0x0oUa7QIUztiYC6K4i9UoCjUkSDrG_fSmkKzVxClUK0Zabaalk5YdpVSRkT1j05w0IygY6_6frWA4xs09kVJdPKOm8erovcjBFgxlXsnp_0NWAXVMQjMiNtwvAlNkSMJcCMLG5bV1YbZTk3D9d4tFzeIZ0EClawG5WcGOhfRcFIbIheITWWhOGwbiR8iXCJ71rLXZByw7jN_6DbSTIE9PFgC3h-GhqI54lgr4j5kgswSJTyVHkcJHlOx9P0xtteMtHzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی: عراق مورد حملۀ نظامی عربستان سعودی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/akhbarefori/676236" target="_blank">📅 03:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
منابع عراقی: عراق مورد حملۀ نظامی عربستان سعودی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/676235" target="_blank">📅 03:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
العربیه: همه پروازهای شرکت هواپیمایی امریکن ایرلاینز به دلیل یک نقص فنی (اختلال در سیستم فناوری اطلاعات) در سراسر ایالات متحده متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/676234" target="_blank">📅 03:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7a73c822.mp4?token=DfXCmuAFswpT40L17ICh0MMnyHDbSpG_r7F1-JdIwTsm74fyzz6gTBu5io35pbHmcgKKsB5Cer3ISIXeFSuYJ9ZrbI83cJeYDTOjvb4xTAiydpcdhvaqRuqXrxw64menfClHx-xLUO8g3mUKEAZKPmeaI-DmjEt0T90-geJ-mEpClriz9IiEt9kW4mZaOjC0cDS5KJn1gN7Scw4cwLowAf0yfN_0f7SOjC5Aql4I9QwhyI6oOlcj30jF62zKgTfvgO-vvNswJX182aQju4osxZQxSJOzenHmcb7OcgqoJLJqrmmDOpoM2qSnF3z_TRxeiVwLmgatWR5yCt-fjWAr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7a73c822.mp4?token=DfXCmuAFswpT40L17ICh0MMnyHDbSpG_r7F1-JdIwTsm74fyzz6gTBu5io35pbHmcgKKsB5Cer3ISIXeFSuYJ9ZrbI83cJeYDTOjvb4xTAiydpcdhvaqRuqXrxw64menfClHx-xLUO8g3mUKEAZKPmeaI-DmjEt0T90-geJ-mEpClriz9IiEt9kW4mZaOjC0cDS5KJn1gN7Scw4cwLowAf0yfN_0f7SOjC5Aql4I9QwhyI6oOlcj30jF62zKgTfvgO-vvNswJX182aQju4osxZQxSJOzenHmcb7OcgqoJLJqrmmDOpoM2qSnF3z_TRxeiVwLmgatWR5yCt-fjWAr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی از وقوع چندین انفجار در انبار مهمات یک مقر نظامی در استان بصرۀ عراق خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/676233" target="_blank">📅 02:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676231">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnWjgnjftx2oN6-q986QckfqO9zy-YfbyiLIgYZx0wM3JOFrheoa3c5c2VrkTU9srSK_q1i2TEYGCpIaawfzRRv9FrRMD7INnwhgh3VUwHm5ch5_JWFhWFqv0VPxIq-nR1swJqn5aKUV1DfoMJvQSX2nLBXZse9KVCgFTgX0kdt4_PuEzEx8CO6MXxYdBWWG6XLw-PyeApQJfUkDNV1D6E05FaQVnNQdLlNtp2-SOio9I4Cu9Jk2sMaWk0Kyf2wXXFntuzm_kHDRARgn-8nbrFqe41dGXezIP68W5_zVko2qFbdjja1MUhb4fBr0uga3jOUWdvFZJh6UluIO5mHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت نفت پس از حمله ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/676231" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
