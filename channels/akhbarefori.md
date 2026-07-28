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
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 03:22:13</div>
<hr>

<div class="tg-post" id="msg-676233">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/akhbarefori/676233" target="_blank">📅 02:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676232">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
یک مقام آگاه نظامی در پاسخ به اظهارات وزیر دفاع عربستان هرگونه ارتباط پرتابه‌های شلیک شده از سایر کشورها به سوی اهدافی در سعودی با جمهوری اسلامی را قویا تکذیب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/676232" target="_blank">📅 02:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676231">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRnWjgnjftx2oN6-q986QckfqO9zy-YfbyiLIgYZx0wM3JOFrheoa3c5c2VrkTU9srSK_q1i2TEYGCpIaawfzRRv9FrRMD7INnwhgh3VUwHm5ch5_JWFhWFqv0VPxIq-nR1swJqn5aKUV1DfoMJvQSX2nLBXZse9KVCgFTgX0kdt4_PuEzEx8CO6MXxYdBWWG6XLw-PyeApQJfUkDNV1D6E05FaQVnNQdLlNtp2-SOio9I4Cu9Jk2sMaWk0Kyf2wXXFntuzm_kHDRARgn-8nbrFqe41dGXezIP68W5_zVko2qFbdjja1MUhb4fBr0uga3jOUWdvFZJh6UluIO5mHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت نفت پس از حمله ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/676231" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676230">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رسانه‌های عراقی از حملۀ پهپادی به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/676230" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای سنتکام: ساعت ۱۷:۴۵ به وقت شرق آمریکا امروز، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از خاک ایران به قصد حملهٔ غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه پرتاب کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری و منهدم شدند. نیروهای آمریکایی همچنان در حالت آماده‌باش کامل و هوشیاری بالا به سر می‌برند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/676229" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676228">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تعطیلی تأسیسات گازی در شمال قطر
🔹
در پی وقوع یک حادثۀ نامشخص در تأسیسات گاز و میعانات رأس‌لفان، فعالیت و صادرات این مجموعه به‌صورت کامل متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/676228" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676227">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای یک منبع آمریکایی در گفت‌وگو با  i24NEWS: ایران حداقل ۴ فروند موشک بالستیک را به سوی یک پایگاه نظامی ایالات متحده در اردن شلیک کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/676227" target="_blank">📅 01:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTRRzBKOHKrbtsofcv77MrqF0a_-KPm0sFQ49KzJt-RUzCZ--07c40p9BDRN3XKbmzcOk96KZ78TotdAlNEwKaZSMpnt3DKvijGRSssfwFhmHjMt25rpocQtKypghK1VjbFGqNKG0BWnhvwC_vPQcDuy0Dk7CkGuzc_NXlei-EMJXh7zphOUx5KnB-kW_e_v3EFjzaW4PVIs4uuWYM-i54zZy2y9_hzafkaa6eYYiWYZv6pzx5ONgjaaAn5NQlZX2wmp1lVE-ErX34vYc81SHfobGjL8aA4QWcmU_dDcJ1yRWIVqTDdJW3O84myFh2IchDIOHEEL5LDF7ggjJFznEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db00447bba.mp4?token=Qjm6Ym8eamxt1KtkGGSsITtpKriL8sMQJQDVmGqlVbzyw36bBGjLfxA0xE59d6nWxw7xsas6jBUdSpw_kVJnRvZj69DnJIHiXCEa5sw27loJ_1mzbpfs9tb_FpfxXYm5kXmMWnFtx4QGeLgTLVEw2YsEa8R40VSoQ70EqI79btDhYGKhMv96hf51p1zImGZXwDFj1yaELl6IHgrFyjrkHcF8x6pSVhd_AmYIMaoEfjVT_GFhEpWMKD3m2DBAcTd2NW517MW42gkYUr4rq0X84x8H4G1e4vAvkoOdn5pXms3KI7wRlBttwmhsjMOabL8RUv5cOeREY5eQRMTch7Dp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db00447bba.mp4?token=Qjm6Ym8eamxt1KtkGGSsITtpKriL8sMQJQDVmGqlVbzyw36bBGjLfxA0xE59d6nWxw7xsas6jBUdSpw_kVJnRvZj69DnJIHiXCEa5sw27loJ_1mzbpfs9tb_FpfxXYm5kXmMWnFtx4QGeLgTLVEw2YsEa8R40VSoQ70EqI79btDhYGKhMv96hf51p1zImGZXwDFj1yaELl6IHgrFyjrkHcF8x6pSVhd_AmYIMaoEfjVT_GFhEpWMKD3m2DBAcTd2NW517MW42gkYUr4rq0X84x8H4G1e4vAvkoOdn5pXms3KI7wRlBttwmhsjMOabL8RUv5cOeREY5eQRMTch7Dp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایرانی به پایگاه هوایی «موفق السلطی» در منطقه الازرق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/676225" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
یک مقام ارشد آمریکایی: ایران موشک‌هایی را به سمت پایگاه آمریکایی در اردن شلیک کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/676224" target="_blank">📅 01:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676221">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac506c8b95.mp4?token=DYlw5H1vx7sdYrICXDWdrfMd7PhdIxNfBzETkGNGj7lUJYak8i5_d8lvsMPcljjd17jdMJN3xxz5ZmK9lxL2es0gw6GQ9t-4oSQdMkUB-OrgC_DmZ07IppF0LRxhiFCdg6HUYlpQtBoeJij4Kv79DiPXiExml6fyR5z9fj0TIZfNLip30rRdmiNlhhwcQV0oVhdwiWgoZcrQWOeiS8TMN18x5NyZCKUuJipxaC51byKqkRjn_bqkPrcRNhneoES2PafgTlfzDHaL0hprJsRTykCAjs7ZyNUwPRPQs9YopoqCv_6WnGR5mPo9ej-YJ1-Fx5M4HkPsWeRtskE0UsKqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac506c8b95.mp4?token=DYlw5H1vx7sdYrICXDWdrfMd7PhdIxNfBzETkGNGj7lUJYak8i5_d8lvsMPcljjd17jdMJN3xxz5ZmK9lxL2es0gw6GQ9t-4oSQdMkUB-OrgC_DmZ07IppF0LRxhiFCdg6HUYlpQtBoeJij4Kv79DiPXiExml6fyR5z9fj0TIZfNLip30rRdmiNlhhwcQV0oVhdwiWgoZcrQWOeiS8TMN18x5NyZCKUuJipxaC51byKqkRjn_bqkPrcRNhneoES2PafgTlfzDHaL0hprJsRTykCAjs7ZyNUwPRPQs9YopoqCv_6WnGR5mPo9ej-YJ1-Fx5M4HkPsWeRtskE0UsKqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایرانی در آسمان اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676221" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676220">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f64ca23e6.mp4?token=jyPdm-Cwd59JwbvkqClg9DP8igvdJPzYoLCRuYm857XvA0jxbd25yPtU-FwTsQulsDYc8A3jbhqH8iDYs4vVoxZ4hEcKvYVFHMp_r78cc_uOIfm84dzbLACITP-sja0Asg7Flkf2BnLwsmEbsVNw-mNYM4_VZzo5sJowc0KxGmrPdPACB-JJft_G_zsIigPbm7-tCLCfwzSDe9DfBw-gOyT6m61qtLTQ71DBpd1F-JGPX1q2CxD8VkxHVQ63Zf7VtWDzyeMlM8xsnZn3n9-UCLjqn6kSjPMkoEmIDWF7PxSk4Y5Tzx8_ZQqgSKDf5E56jFxA6AJVceN1YIRoxApYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f64ca23e6.mp4?token=jyPdm-Cwd59JwbvkqClg9DP8igvdJPzYoLCRuYm857XvA0jxbd25yPtU-FwTsQulsDYc8A3jbhqH8iDYs4vVoxZ4hEcKvYVFHMp_r78cc_uOIfm84dzbLACITP-sja0Asg7Flkf2BnLwsmEbsVNw-mNYM4_VZzo5sJowc0KxGmrPdPACB-JJft_G_zsIigPbm7-tCLCfwzSDe9DfBw-gOyT6m61qtLTQ71DBpd1F-JGPX1q2CxD8VkxHVQ63Zf7VtWDzyeMlM8xsnZn3n9-UCLjqn6kSjPMkoEmIDWF7PxSk4Y5Tzx8_ZQqgSKDf5E56jFxA6AJVceN1YIRoxApYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت شدید پدافند اردن هم اکنون
/
برخی منابع می‌گویند پایگاه آمریکا در اردن هدف قرار گرفته شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/676220" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676219">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه آمریکا در اردن
🔹
رسانه عراقی بامداد چهارشنبه گزارش داد که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است./ فارس به نقل از صابرین‌نیوز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/676219" target="_blank">📅 01:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjFAgZW0RCf_vb-S1WTiSj9-0Af9NWkdKObTTfz7YzfLfleTXSuAWzjqt7X2DgTHAqJ4jPpyUBMom0uZR_dmlYpuY2eunXFsM2UvZpHlcGjCygySdTTv7fRvyFfuZ9SXSTDZ8pYOhsEbNdBt1DEUbhTlZra6PxfGpWqOAjtwb-UpGQ5Ng62m6hiMpAKgbf0-HKfsi7Q84fSKwcn2J_K7QO223_GmHcnqK5SmvQtaPywa8xm3-I8AY1NEXCLYFT-6G5TNfV9BgEnrOwng1fXGao52Ok3miTCPDyPsPzPMmLRi_TkIYhwebOHEu2nVzGLjeDqjhGFlVzBvcROLzcKKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYSldc6O0VK8SR-fj8ZL88aqFzuzO0iagWpCKkhlTFDn90ZDbOd6rWDKkWvoDbm34rfZYODs7MP-UWqUnhDjr9_UCnLTNUSsZjJfNJQyKTat0iNx3xA_aSmSNsaW_yWZDn53-sw9NXYoXJD9UPUGqunzbM410_lSPIYzjeyLRqNl9kphYDFtkzfsWrakMhsVjbW-Bf4TzpjGCKdQj_tafteAs5VR11am3Ne3apBpz_Qxx7NM-uY7AuxA7RDW9tYLgbeURwATTLQISWhlZDrsQWH3oNUWPs9VTFeU_9nKhspadlh-aAyu_Tud1U5txWogp810OmO-Bj16-yAiBibhYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=kWyHkqnmpinTvQlA_O0Q_gs1lCvi39mAf6r7wlE5LzS5SLBG5_OWyKz1Nvh0xLLxsqftIXyZuWchOawHYsaxLKytgXPEQXbEUWyPQ5GhNSAcFYPLubpBg7s5W-zNgX-FhpEu2VipbnpVKhJAZ2ucq3EHHR0LxyFGxNzIwLP9w02ie0iZ79s-V5r5CTGaJgNjOX8RakN8kLLirVuvn7lq6dPMsbK7ZidBS-r7mZtjroG7Z-qEXz24dke-9ZZxANUGY3q1LctvpM-ZNVqnJhoyS55IuXSgCTlLV35j9C5L_cAkL4ieqvOh2MyjhgdAnAX4flIazybcBgq-khsxrnuQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=kWyHkqnmpinTvQlA_O0Q_gs1lCvi39mAf6r7wlE5LzS5SLBG5_OWyKz1Nvh0xLLxsqftIXyZuWchOawHYsaxLKytgXPEQXbEUWyPQ5GhNSAcFYPLubpBg7s5W-zNgX-FhpEu2VipbnpVKhJAZ2ucq3EHHR0LxyFGxNzIwLP9w02ie0iZ79s-V5r5CTGaJgNjOX8RakN8kLLirVuvn7lq6dPMsbK7ZidBS-r7mZtjroG7Z-qEXz24dke-9ZZxANUGY3q1LctvpM-ZNVqnJhoyS55IuXSgCTlLV35j9C5L_cAkL4ieqvOh2MyjhgdAnAX4flIazybcBgq-khsxrnuQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که از آسمان اردن در منابع عربی منتشر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/676216" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5hNIRZUQnMZp70oo0sNCywKCeFLrUxByF_voIi6EPaCIOfLtgQWgefd6mPcoiTRUlKH7iMj4OdXwYnkABM_s3ykk6X1qPLfnYUcpbZuYlhCwarbJB2bVlEygf2pWeY5iEZzD8MPSwk6pD_tZiAAIBs84o0ISW0OknAYcv5uqAs5USQ16wNVV5ZkEDaVNMYGI1JtzTi8BvuHW6W-jGdZOn2nHxLbBc3rBL8pnhDpDJJc9sSY4voRQzxH7W_2jJLLaBzijrf3RniVStcA6VHbqJb1IxcdcVhGfyXC149ok-a5wNw-6fmeOqRtJwVi1n9viOwCagg3-uOHbRc2bCQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجارهای شدیدی در اردن رخ داد، همزمان  پدافند هوایی پاتریوت اردن فعال شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/676215" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه آمریکا در اردن
🔹
رسانه عراقی بامداد چهارشنبه گزارش داد که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است./ فارس به نقل از صابرین‌نیوز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676214" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روسیه به دو کشتی اوکراینی حمله کرد
🔹
روسیه دو کشتی اوکراینی شامل یک کشتی فله‌بر با محموله نظامی در دریای سیاه و یک کشتی دیگر در بندر میکولایف را هدف قرار داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان روسی دنبال کنید
👇
@AkhbareFori_RU</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/676213" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش و ترامپ قمارباز در کاخ سفید دیدار کردند  نتانیاهو کودک‌کش پس از دیدار با ترامپ:
🔹
درباره جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگوی خوبی داشته و بر هماهنگی کامل دو طرف تأکید کرد. #Demon #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/676212" target="_blank">📅 01:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7906f25da6.mp4?token=OPZ6XxiTxzmWdox293rn1bAL7A3umXUosW-rJEVUxh7yPOX-jgKLl4Ci9whZtuR4cjDXp02DiX6xJ_H03J1AdAmZNuG-muzxRKyWXL-UPoqsnfEGh6YSgxaFo5CUh24vK5KZPO6-mjl-seoKEe1BVDLBbdc48y5-MCcqtmR8e2CoEDK_bX0-i8o9LEAI-lp68R5F0QVIgGkzwq9lPS9DGaZXO2rWVtgf7Tq0avgvyoexfHdfq9nBIAvMQiiOQp11nObWaffOOj_EUSCGU7IJzqi9CM59u8_x23UBH7C_gujdJ5BIOYgPTgrCtRSvKPvWbnSKVJq6_6hx3E1w-l9obg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7906f25da6.mp4?token=OPZ6XxiTxzmWdox293rn1bAL7A3umXUosW-rJEVUxh7yPOX-jgKLl4Ci9whZtuR4cjDXp02DiX6xJ_H03J1AdAmZNuG-muzxRKyWXL-UPoqsnfEGh6YSgxaFo5CUh24vK5KZPO6-mjl-seoKEe1BVDLBbdc48y5-MCcqtmR8e2CoEDK_bX0-i8o9LEAI-lp68R5F0QVIgGkzwq9lPS9DGaZXO2rWVtgf7Tq0avgvyoexfHdfq9nBIAvMQiiOQp11nObWaffOOj_EUSCGU7IJzqi9CM59u8_x23UBH7C_gujdJ5BIOYgPTgrCtRSvKPvWbnSKVJq6_6hx3E1w-l9obg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر فقط ۳۰ روز قبل از خواب گوشی رو کنار بذارید چه اتفاقی می‌افته؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/676211" target="_blank">📅 00:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0ae10294.mp4?token=MClRjqp04HNBmrAhQGw-FpkBA3lCyhHXYiMerMRGsj_Lelajs52_IiXS64nSMx9KRcbDHNQa8hJZaZpM6PLXwz8BykqUBkHpOEWgO6D3AsWdQ-rCq6miLhYJDiHX34Kc1GDqj2whqetY7QpRmxSpIDG8nJVol-6cU3_FGLsNTtgvMRe9F5x_IUKlGC1Ws1kipNgQsFC3ZbJsXlFUulMw61-mNOj3fODnz7NKfLV-yb3Yg5R0X5mNMMqXWZqFUKMPdDzBO6Z6knGJWk8SPQcyAhl59yMhtDGr8giOsyn_xePJMYwOJReTnyNt75Nt8yjZuL5V7KQNyulgALE8ZCSFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0ae10294.mp4?token=MClRjqp04HNBmrAhQGw-FpkBA3lCyhHXYiMerMRGsj_Lelajs52_IiXS64nSMx9KRcbDHNQa8hJZaZpM6PLXwz8BykqUBkHpOEWgO6D3AsWdQ-rCq6miLhYJDiHX34Kc1GDqj2whqetY7QpRmxSpIDG8nJVol-6cU3_FGLsNTtgvMRe9F5x_IUKlGC1Ws1kipNgQsFC3ZbJsXlFUulMw61-mNOj3fODnz7NKfLV-yb3Yg5R0X5mNMMqXWZqFUKMPdDzBO6Z6knGJWk8SPQcyAhl59yMhtDGr8giOsyn_xePJMYwOJReTnyNt75Nt8yjZuL5V7KQNyulgALE8ZCSFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم منتشر شده از دفتر لیندسی گراهام در روز حمله به ایران #Trash
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/676210" target="_blank">📅 00:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc7b46a21.mp4?token=dvqa_JpnGl4O0UWQI11_7RPMV88h8-ALkQ1ppxtBSku-8U3zSuKOBBmuTagHwL7zp22r6ie2usMEWwOU71vk0h99bRn-5wT9K0QhYwlo8-9xnGpHIKRKbEzTvtHQRx5utspSJk6dT40i4PE42U2Z34j1IqA7ZvIpBOwNxN3Mvcfz0VMFSEkXkFD9O4MIunvLjVb2KeciXP4EK052At49kmsoJkCrfxBdKLwOzzamKZEZuQgdrJAYIxXcD_XhHPUqu4xxgulmd4xW6KABZCZBi1Ov23uvptVNwF3eYeBUwQFkQljHJywxdxDlxbOqD6516lGGGVHCg2x7NYGI-esNMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc7b46a21.mp4?token=dvqa_JpnGl4O0UWQI11_7RPMV88h8-ALkQ1ppxtBSku-8U3zSuKOBBmuTagHwL7zp22r6ie2usMEWwOU71vk0h99bRn-5wT9K0QhYwlo8-9xnGpHIKRKbEzTvtHQRx5utspSJk6dT40i4PE42U2Z34j1IqA7ZvIpBOwNxN3Mvcfz0VMFSEkXkFD9O4MIunvLjVb2KeciXP4EK052At49kmsoJkCrfxBdKLwOzzamKZEZuQgdrJAYIxXcD_XhHPUqu4xxgulmd4xW6KABZCZBi1Ov23uvptVNwF3eYeBUwQFkQljHJywxdxDlxbOqD6516lGGGVHCg2x7NYGI-esNMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر شهدای حمله آمریکا به پادگان ارتش در بمپور  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/676209" target="_blank">📅 00:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm8MRxRwYMsROOEeh5ykdPDPHXvKQphx7iOfH4qAFIbsvrkyhttJf8JXP7-JMpi-690qlCdgcqaf6Y0Q140HeoCJMFh7w-XiBgBvKyXr9ESGTYsPvOeID9-fG8y-Tu2i0p9pSeBnG47a48z4XLBpEMiI_gaByGJ-kMYTXxHtKyWiRvWgSCPK1utZHz6Eci5BTohLRBqMvhmK7-9EXm-gZCX2QUYpOvFwevN7Tr9-cd_O7F6XsZ4D5VHAA4CuaYQ7oyLWWgoi--OYKU3tyud2vbRheN1D2MjlBkcnsWLIFxbb0zyJbPzOwk8fRhQ362dTFRZA4POIrOlP0V-OnWm3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان رسانه‌ای خبرفوری در مسیر کربلا
🔹
کاروان رسانه‌ای خبرفوری روز گذشته وارد نجف اشرف شد و پس از زیارت بارگاه نورانی امیرالمؤمنین (ع) پیاده‌روی خود را در مسیر نجف به کربلا آغاز کرد.
🔹
اعضای این کاروان این روزها همگام با میلیون‌ها زائر، در مسیر عاشقی قدم برمی‌دارند و به‌زودی به کربلای معلی خواهند رسید تا در آستانه اربعین حسینی، به خیل دلدادگان حضرت اباعبدالله‌الحسین (ع) بپیوندند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/676208" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTu7ZOlf4BCRZGjWf3GyygHg2XvVnZn9a-c56eHOsbT7D-jVA4NJWytJw-YJDdT9BlamI9PTQSRocNJVtUq2oiLZ7uOv2qY0w7BHSOMpWeVooji2Ev4uNkJlclmLJ7uiStGbec8Z8crBrW7tk3BPAuKXLqhHnyWinFYtxRvy00HinHM2wlcFRbj8dtp6bVnKLzbkVvzcarI6sikUrG1u32SWgYpnLF5TjdotZN4A5CsTBWnuihdso63nUOXTmKuWUkiqFhhfZANGiPCsgHLnZaYjKtlcQLdxY77rOMzfio7NVYBhjm7FP7Cw6t4KC_eDg0_BRRT6dEobmZ8rwgY4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ اوکراین و ایران چگونه خواهد بود؟ / مقایسه توان نظامی تهران و کی‌یف؛ در جنگ فرضی کدام یک پیروز خواهد شد؟
🔹
بدون شک توان موشکی ایران به ‌مراتب از اوکراین بیشتر، متنوع ‌تر و راهبردی ‌تر است. ایران یکی از قدرتمندترین قدرت‌ های موشکی جهان و منطقه است، در حالی که اوکراین در این حوزه یک بازیگر نوپا و وابسته به کمک‌ های خارجی محسوب می‌ شود.
گزارش خبرفوری را اینجا بخولنید
👇
khabarfoori.com/fa/tiny/news-3233826</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/676207" target="_blank">📅 00:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676206">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJrsjnzQGOizezEeNrqW6RO-99i_GrGOqhb9-fioGxhv_uaBVl8aWvQ_dIf9UXEOIs-Ed5JV1urhU88lFCHBAKSo-3My13clkl3rwa8AYRMZTSuqQX4eGqWopc4wFSg08mOY-8rFbpMgghPeHmpgQlllsahHmBS7FfK1_T1kobSfJhzsoQYijXAmqi0gqTQXd8ZZgryvn37KTb1wrjtFGpsEaPaWpIpvMRpZivXXx0fO8h5v0FtdvwsSVpLXOHCGBwGTBOSH38oD91xiq491DC4GokRrQtjpJ1OXY3luvU8xDcxQjNe3WLltOTsayEa1bTG68nIEh08RN3iAifTr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/676206" target="_blank">📅 00:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676205">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqqhZppUlPRDo2LYpo58A0j74CccDVRagFz_2K7Owy-iMzXw5jpOCzLo02dq7kDXr4BA1pmh-zgpN_KXDU4ldZpb6jZl-Q1MKrDfsO4CvYTqoTroIHo7IhBqsnnUy21mtHLHzr5qU2BUgKcqOW-9vLLzC54svuGaMsbwIoFbT5FPAahyqiUa4JCz6-x_H8iU6ysUqbu4cIwv8fLviUIiJV1_TXSJdI7M3L5n-wbD46YXsWztPOsZ5Bp4nsDYu2kJPLxGtkd_zK0OAspl_qNJpg7cKGZPy3tXB6o4SB-htAM6Xso7EEJ_Yg1WI8JqS1pweEh6YxkwUQjAEUPvCRwVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت نفت ادامه دارد
🔹
قیمت هر بشکه نفت برنت به ۸۳ دلار کاهش یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/676205" target="_blank">📅 23:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676204">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فنی‌وحرفه‌ای موظف شد بیکاران جنگ را با آموزش به اشتغال برگرداند
غلامحسین محمدی، رئیس سازمان آموزش فنی‌وحرفه‌ای کشور در
#گفتگو
با خبرفوری:
🔹
سازمان آموزش فنی‌وحرفه‌ای طبق قانون بیمه بیکاری، موظف است کارجویان و افرادی را که به دلایلی از جمله جنگ بیکار شده‌اند، از طریق آموزش به اشتغال بازگرداند.
🔹
سایت سازمان فعال است و هر فردی که برای بیمه بیکاری درخواست دهد، به دوره‌های آموزشی معرفی می‌شود و امکان شرکت در این دوره‌ها را دارد.
🔹
این آموزش‌ها با توجه به نیاز بیکاران و کارجویان و همچنین نیاز معاونت روابط کار و سازمان تأمین اجتماعی، در سراسر کشور در دسترس است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676204" target="_blank">📅 23:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676203">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d58dc1ad.mp4?token=PgA7OzT1d5cCsHuHUgNWVVWx0MPYKpNCQZA4s1FQLhiGASDswzaOecjp_0_LQewGGNeEzVG8xbWbnIcYoUIlcNauaEh-0fk6ifX1I0WcLI88RbjvVYoXyMtb-uxPiBr3Rc31OBsIfqQOAZTn5tT9H8odlfK4XTzgFNzG2CGFYtS-R16QaW9Lt_6nfN7h7ptfuJbBS1u_UyZoMOoa0JoAyM6pFXUWq2li_Wq3y0LP20muN8WYSZJKO6eBABuHvS1RzuKlpwNnAtWKqyNzhw1hNMzL4R1YIEpbI6jjOvey8y9LMcffze7iKp4G7rC_L-uuDzAmriYtcT1TK2Or4BB2Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d58dc1ad.mp4?token=PgA7OzT1d5cCsHuHUgNWVVWx0MPYKpNCQZA4s1FQLhiGASDswzaOecjp_0_LQewGGNeEzVG8xbWbnIcYoUIlcNauaEh-0fk6ifX1I0WcLI88RbjvVYoXyMtb-uxPiBr3Rc31OBsIfqQOAZTn5tT9H8odlfK4XTzgFNzG2CGFYtS-R16QaW9Lt_6nfN7h7ptfuJbBS1u_UyZoMOoa0JoAyM6pFXUWq2li_Wq3y0LP20muN8WYSZJKO6eBABuHvS1RzuKlpwNnAtWKqyNzhw1hNMzL4R1YIEpbI6jjOvey8y9LMcffze7iKp4G7rC_L-uuDzAmriYtcT1TK2Or4BB2Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انقلاب رباتیک در چین؛ پیک‌های دونده رباتیک با سرعت ۵۰ کیلومتر بر ساعت از راه رسید
🔹
برخی از پیک‌های تحویل کالا از تجهیزات حرکتی مجهز به نیروی کمکی استفاده می‌کنند که می‌تواند سرعت جابه‌جایی آن‌ها را به‌طور چشمگیری افزایش دهد؛ به‌طوری‌که برخی از این سیستم‌ها بنابر گزارش ها قادرند به سرعتی تا ۵۰ کیلومتر بر ساعت برسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/676203" target="_blank">📅 23:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676202">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام‌های امنیتی مصر برای جلوگیری از تشدید تنش، راهی عربستان شدند.
🔹
عراقچی با مسئول سیاست خارجی اتحادیه اروپا درباره کاهش تنش منطقه گفت‌وگو کرد.
🔹
منابع عربی: صدای چند انفجار از منطقۀ کویه در اربیل عراق شنیده‌شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/676202" target="_blank">📅 23:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQfuaiDGlZdeNY2f7dMRgI8swqGGrEDbBBSFgNXKTHGguoGeAwWgVAtnl4Wrbw8D-o8sG9c84jJr1wwjD8Da6w2EI8b64bqjXUCegUZ5Pz4dIO51BKmtMqKX4RS2YuIazFkQVk9Pgvedl4Jgf-RV0bV6ydEYAX_0kWJaRlzWzFSLGfIfjiAeeoJjXv1IgGBbL8HzhXJNy0txLSpkenfEUbjcvndwWbXOkwNGX5RSoI4uVhAtJ4cdPsewA_VGmAxeHITYSyumOquQnhHIbHpvwS7ylehy2cspexQ6SO_LcGg5EWKGYhA-yO9pMti8xFwWGCQp-qCeuZM2OvrHrmJAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlIy5Zw-k5yqNtzhRBin73qRrQVQ084D68PSnjOIQRmBdzmncArhEPV9upB2f85GdyerDpax-eE0yipxKiLmQ50jLwS6fE69sYXQJPIjakY-ohy5DIEBckk_jCCAXhNhbrVU0clXhSsXvfCCTTa1FVI2SysgffLcGI9E7qfEHG2SLNDl7iD0Qoh8jXJEl8MsIaAXGoBpe80ps0uNrkoaJSU1_4NBzJJe8DETQDdkDzlFA9byMcjbpmn2vXmyNFMkqDumaPx1gDsfYhcvNfei_COWfvysTYY3UUsNOPWGbSmO-nyhZ6bTo8xwpBl-Atwh2WrssB1a4Y4DX6Xv2hHWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS9qXMK-3kBbl_md1yAUMvdqZ9Xw4hnna-erDsDXTHW4UcdolznIdJX8F5lxNtGHHa21qwR36pCHxIBG0q5orF_LonuGdMWXSNcWL636jTxAMKLg3_BK8qYUAGd-uzI9CW8HieBq6Gps-4QshEU-qXSNN2tFWypK15BNwTGqAuH7QKENUxgb_LLN-M273nehHv6848MDHQ9Zhby_whJaTAJa4bb3YkMRyCmJ8UJ29GJmq1oz4lufOHbpPgd5nU0GxzKzncSWV7-fS-zhiXfcCCdeSiaozLCtdLHidFD26QV3rViqhgpL4LFzi9eEnC9xGjcnvvQkt5XnOLmdguIHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yrj-BaksP7HAlnt1Gw_6HKysYchIGXPSF2VZCfhdYeLmGBYO15a0ieUl6fDsAkJXkKkXL7KdNKkmYfcrrlnoT2yqDTYQvm-2-978FjxvEClqu5npDwCeHS7Wwug6k4vhVl2jHDafpocjUMrH_o2UIKd6HJiZelE__1OTrhOAIE8Ri96VB9bBHMuxgWenu1iuH-Pp4RU2cRoZz46GjppiZ34r1Adyps5IEQrg_alYfoN2dCSxXr6k3KyBaHUMXFd-su9496m0DgDcTPncSPV2KkhNJysKyFIMM7DMvV-AcUKWatGpz_QVg8jTvub5A__3F1NCuiJlFleaJfhrRJgjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u--32MYhMtm5n8Qq9b9sUf61rTDeKr70yFK5_vMhseaqCXJUCyXd-_XF8CTRJ62xBHeg1Ig05GtZ1lYSIcvx2SyFQcwBh8bZpzo0GCk_8w1bgOmM6r6aDE0EovdyzPW2zsZ0wOURtedsXapHEOIAuD5SRhJcJnMDPBNXr-0ax3LxZakD2oOzyMbPELQP1wEoZ-xHIbv3na09XrVLKtTc-40KBDdrtt7n9ppGReaSvjIOk0Tg2dI1yl4xPNSOL_u96YFpDdUgjuDG3dJZi3gS7gqxlaRaUrgjfzkQErkjG665NHj6LEUD9ONk89J9c4i0P_clckMNl0-m52DIg5Eb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKSPWipy90pZsKa-Ha7kYVOEyJahbc0OQWGbiutWAnCZZYrhJMehagJmAXSA6RXS_lCQH7yI-P4u6mzJEtfAsbat2XGHt4t3Ka77WMrEY7ZJqLvY9pKCTrVvtKcYHf_KxB-PitlA2S5ssc-QzBoitkSwYQ9jP5ssMrDME2pGpmr7BL8PEuxS4DsKwkGoDNgTEPtHFOQBQLL8NRKHduakv5sZnfs9gB0aIJOe38ddH5g8jKDrEmAhnXdcaoaI10mQOyesiS4VnZTmznvCK1vf3XCbU6u5q75qYb2gBc3lx5uaHWp_u9a5Hm5-FXcJTTy3jB_S7v-Ms5rssSxvxxNtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4_Mz132qZ12Tgy46fXEvyggKoYd3mBuMCZ7YNlQ2VXlzeOewj5jep00063dZLY6PKYYTKmD0lPAUSzKG-Is5eFQtMGThB_EiPXAG22b7nx0Yua2_3m8I5N4jrILZNYJDJjAcrw6nK03Y0CwvUIQT9q2Sgg6eXji70gFz2qDusudJcPqNKYRf6qHYxMnV_uYZ51Bix4OK1MUGbvmO0rcScLaTJ7XbnY4qkWA9iHNlg0MlU5Hm4eDwU2MaaICm-73wHv82kkPVl4QKLOwPKtyabUJCIWT1Z9Mvmr7v-zpnddgoTHzCuhJc-eJgqXaERVVagd8ir3Y36LeNlw46rxgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ08rSmzwJM0skIsexKPzQPDd0w_SSL5FbPTcEo37i6WQR-nRyydmwxeGv088MT0EA2djfdzYpYExVvB_j9E6ewPFodCULyvfebFNCX6bzUwo5Z1xVL9A4VbLECD35oA2J8bhCN_UegJkhGwVKyUUtzuzRydD4k8MDKtqMRu2NwtCuzh84DJ_f0rAZt6z3EbytSgXpyJT5HhJHKn40uwrmFewZBWjX9wD3Tyw1bOUlRVg4D7AgoLWoQp1czzGvgvOF-t7Ub_sTh9IKfNcD2fdN82E6Qoug2SEGaayHc4giZ0gqB3zmpxigqdPU6ZgKvOx924ibzAqDvg0X1DVG5LZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4a94nhl4hgvlAekqV5y9XHPlyKE7uaZ1g5Q5lvERstZp20SUHnZF1lyMTmNxFGSYJDecsG-fzfZHgb61JTPeB8hLOKroE6w1aAHtaKGYZaSaRbwYfLyRfAyqC1iWK3nUNOW9W_eC7Uz5TMRZVCL7pxrYekAEM32WtrXXehAJdnJq6gOI5NmJUNT-XfqQCe39cJa3njN9hn1ZgYVWzai2t9S3b6oGxlPZG52Onvt4qDCV5piOvpDz8MEFPXHe2bpZamZreMYKgvTqAywxherySfT_j1ir8OB1mapM2GB6Y81Eu10K_6IvCpcH7U4fTv1WqkxZu1KuklTIcWqGZJZZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش تصویری روز اول حضور کاروان اهالی هنر و رسانه به نیابت از رهبر شهید در اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/676193" target="_blank">📅 23:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUJv0vqrMDauRI0iTOb0xIMQvsE8QEIPDKHNQ-8Wcw30b3pvz50YKaYzE5-HBTT0rdE3gd5iqZ1yMQyf1wBWISerVqxTqi_Wzd8u50zwyM1U1WCu0t9AUIbgCynJyChSS3Hwohi9S144aHrvFPaUrHHtQmerq7z5UvEDp1Su61jf34kANHw1jfYfJQlWWQS6pR-tP_bGLhAH_cRsVs_FMNGihLv7uE9Kij_oDu2jgV4X6SRoWg_lEvb1WX46LYMHdyjDWNeSThOWtG_Da82-ajj3FyQkueEXkZtTGVDBKllN3Wsf7KPXgzNN2jpIV7jw5t7Ajuhgmcc5Yro7vfY_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
خدا را چه دیدی! شاید همین برداشتن یک زباله کوچک از زمین ما را بهشتی کند
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/676191" target="_blank">📅 23:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676189">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
جزئیات دیدار نتانیاهو و ترامپ/ احتمال حمله به تاسیسات هسته‌ای بالا گرفت؟
👇
khabarfoori.com/fa/tiny/news-3233883
🔹
جزئیات جدید از اعدامی های امروز اصفهان
👇
khabarfoori.com/fa/tiny/news-3233879
🔹
حیله ترامپ بگیرد، ناتو هم به جنگ ایران ورود می‌کند
👇
khabarfoori.com/fa/tiny/news-3233738
🔹
خواننده مشهور دختر 14 ساله را کشت و تکه تکه کرد/ عکس
👇
khabarfoori.com/fa/tiny/news-3233863
🔹
تصویری از دریانورد ایرانی شهید شده در حمله اوکراین در دریای خزر
👇
khabarfoori.com/fa/tiny/news-3233697
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/676189" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-myQ_lBbo7ETsqLCybe5IGPMIN9DryDZNR-0um_NV5DXsy_Pt9ttqd7yyjzCEHxJmbP-7VQRaweNikctCiHcD-QXeiss1Crrd6jhI8OUmoYFnm4F-PlRvsk_lf3HvErN23HsIkpcEoJk-nHUZjqUvyVsq1huccCwGLs2NprOoxMUF2U0Q5NhMIgy4yk0oIGTeUUVlsLmhfuxfJYixCN0EDolgn-5X1H5-QsSVLLLPXZXUReEwzMjkuGdCCsfP25UMd41HX2Kr8r-ynUtrDggHtmD7VsP1JslNfC2IPE5RLqPPekk0hUlKoaoQ50weN6A7Qpdv2dmgZApCKaXaIKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j26fseNpZoQYwV4r0akapk0WcyQW9zqIi5Yb58NQxXobO1z_DlDVHLtN4kJyzUfBO7bUVuGK0kH5GNWSlVYZBGNok5ujX5hk22v68PHrArB2bs_5C_XB6aI8Vo2tpt3nfPBDWysekZiTf1eLduxFziI7bp3oIgAt4T9oU3k5gABDz7G2F0kO2LHhTBoeJwohlaO-IiMJd9Pr5cp3PDxtLVVDpTTxTYaf2EaBBrWwe2os1Yvo-H4TwnGdHBIemSljM3Y0MBSKDOI3Cujhi5hiRQ5MWt2FD-yVMcSETxkuuS8ixHPH14QTLgjyhRoWacHeUIz4rSXz7JLGmtaKP0VZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFxD0VpPm1zFjjD8ZOK8oQ2memVOD4rhNvab_aOPbwgdK_sZgZs1Jf1EBhN7kWD7yIMJlnH2La3CP-bM9-I0qazhEmBXAqeI2elvWM9OBizcyIq2-TF6ikZePFkQiQjArKBZAHzwY4awPfHIfD9yvSWgTYwyp1AYsejPUmM7x__is-1i-pYfdgplnktyWorDrj69wyhhsPnIEoJWvwHM11DYMGxHGVn_bVaIEl2I2KeODyf0CVjaRWr7OrTuKCaFTS01_o7gyN7ky_IkwdPGkEaMbHa4pgc9svXrK_V-8PbdxaNjc4B8vrQ6Tchqm02-fthZkiC1JR4jwZ-ExDbrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtHWv8Gk4Q3Z5CK2uz-S2kH6Pgz0TUQEbrh88oaeE_w9XaR4QrJzh_OV0Q1DBJ9dEXT8rHRoq43v7G-6VY_waJb2oRIM3u0CttQHHNcq9003pHDCggeDPXlnmyskQx8xtJ4Y0LLMdzlfumkw3koLNqu1blSa4sP-0iI82thR3BAs326ySX6EbuqE_DKGlUno8pERl-vPC0ZIVbeG3IKoTvjMZAqqGgDx93XmDOxuzu79ofp3YmL8lj2Yen9QLg2YA17NGVAnfab3K_T8CgQYyqvnw20xp62Cl0cEzuhGCpmi_5sit2xKCss2u0IiEZeLxkyXYzsid-Wk85A3ZPuEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpYHUFHp8_tkGvshEr7cK-VLf7HKgOoqXUi94K8rUFRG-1BN7vCZ2i2JT9gK_hf9mqcGjEY_DmoebzBP1Z5ErULzHpcAHtBKb0ZH9w42QArsoJV2dYVrm3b5RO-26s900KOitOe56YGQFGuhtodHU0CenOpEbr-uJK53kWYG3Q5umrjJdgZL86yj0nl0KVfwus9Ug-caa2Xwj3a97s0HV5VTdzjlPZ6y9qwJdVWlwdc0VNqlTcW7pCvXVo_YmbTbFQCUGZIILE47GLHNsaghB1MUMIUXd3kjPs-FJtadKPLo_741RulaTmvqECy_e-AHjDGsYnotSxaUvIdo9vl6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T73ySCQ5CAYwRq8aKRQHuajIs-pSpboi06RWyCteijp1WUPi9VbIUMvlydEIAdfcWeqDedEx0naZcVMeIS_4oQ7GqAn_bwbO_n4Hms9iHLFrluqKj2glVTFWOjrf4xSrHNlicn74AaOdWO2A1GyZKg7PSd7g_N0UHExZyG51m6WL9_rRDdOejMOcZf68Q_auFyQso1iIx6C9GdLE7w1ZjTqwZ_O2F39Z-geoLp2SHYUsbwADh1J-CaXYG-j0qLhPMfQ-UaWhBfQOz7GPVWO1FAa12iUZJ8VaQk-3FLnmY3TsIffeQvycMz_DRf4M8V_01Lj6WIAl5uSyq-xPmLT0rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ نوع کولفی خوشمزه مناسب تابستان
🍦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/676183" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
عراقچی: اوکراین اطمینان داد حمله به کشتی ایرانی غیرعمدی بوده است
🔹
سید عباس عراقچی با اشاره به گفت‌وگو با همتای اوکراینی خود اعلام کرد کی‌یف تأکید کرده که حمله به کشتی ایرانی غیرعمدی بوده و به‌دنبال تنش نیست.
🔹
وزیر خارجه ایران افزود تهران نیز به‌دنبال تشدید…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/676182" target="_blank">📅 23:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اینترسپت: ایرانی‌ها پدافند ارتش آمریکا را مغلوب ساختند
🔹
ایران از ۹ ژوئیه با پهپاد و موشک بالستیک به ۹ پایگاه آمریکا حمله کرده، پدافند آنها را شکسته و ادعای ترامپ درباره نابودی توان نظامی ایران را بی‌اعتبار کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/676181" target="_blank">📅 23:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=mz3tFwAC8xmtUCXbVbH9D1PmsineibONjUCMQz4pcFlMrNVKXcIMAVv_ulCFVLJxd13FKchE_LmrMn_UEmbDcViqKhyfuiTyIG0ipARJlSRk5Y_4b-I-o1wammjWyjF_k7UYFDM_fyB-FaWAENxK8ujbJNTDEOzO-l1nvCtJ97HzmrW2KH7FLpgX7yB1-KOffAxQoYBtTMfwXwaFvsoqStRNv9rphOJ_uCdJjYQ2QZLbN55g4gIJMD9EcuX3GLMCKRIz5Ticvkwpw-0YNfbC2W9dICI5uSe3KlxYElKneoU-mx2Xh2ONVANFBwp8wiQatbyNtekms0SzzsDAi8Ubgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=mz3tFwAC8xmtUCXbVbH9D1PmsineibONjUCMQz4pcFlMrNVKXcIMAVv_ulCFVLJxd13FKchE_LmrMn_UEmbDcViqKhyfuiTyIG0ipARJlSRk5Y_4b-I-o1wammjWyjF_k7UYFDM_fyB-FaWAENxK8ujbJNTDEOzO-l1nvCtJ97HzmrW2KH7FLpgX7yB1-KOffAxQoYBtTMfwXwaFvsoqStRNv9rphOJ_uCdJjYQ2QZLbN55g4gIJMD9EcuX3GLMCKRIz5Ticvkwpw-0YNfbC2W9dICI5uSe3KlxYElKneoU-mx2Xh2ONVANFBwp8wiQatbyNtekms0SzzsDAi8Ubgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطرهٔ فرزند شهید سیدحسن نصرالله از اولین دیدار با رهبر شهید انقلاب
🔹
ایران و حزب‌الله برادران واقعی هستند
🔹
آقا گفتند درجات سیدحسن هر روز در بهشت بالاتر میرود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676180" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef69034a0a.mp4?token=SICLPDbchzbmtyu9C1DLbtjBaTQZgAi1ohgbvi9MdaKm3NACalrBfed8_erd-4dEbnR5zW9vBADyanstyZNiOiJl5PZV8kVfjhk1TO9LvUHPmPxxonbQ1y4U2JIbF5IiGv-2OQDrro9Bi_hPU_5ZJRr2_ZJuPAROL7bSAEOpS-_tpOR4bnJCFexiQqBvSAPBCNEWnMBFfAVhpfIRDDo5tOKrBdGoarR_0l352ae7aZbOVqrvR758Wug73l30UoReFuLwTHqMidqGa6r51NFttb-oZNtzINLc2A5iwKEm2Ne2qY5JaXtE2iRCMuOHglKZXUj2YOkWPpJizVr19WF951D7NeKbHCi7wvvZlK5OKNPnDfdsU19HaM5MPtU1ZbxiSklbEQc5VCL0f_fNiQnuJztyzof-3730fE8QIndFnEdpBF0NA0vPbxAs3JtKCZa4Tz1-UrbrscXwcOfBh2wtPzMavcdPF1ZFyMUSNHn4xA1sDFDVzpqSEX6_J6ooIyB_i04_AyicnCTO-H_kprM03pS02nIJ02ifqm6o7sY6LWzrS22nj5Cn7aUmdVZgOruo4vb5BWHj8w_zYa6PTJV4Vy4nCEKy6_6qZpkLsoIBpPxUbGBUE2Eqts6cZjDGtt2dQB4MseeiYJ3texJU4oM6yVzQmx1unnn3lRvqh6afxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef69034a0a.mp4?token=SICLPDbchzbmtyu9C1DLbtjBaTQZgAi1ohgbvi9MdaKm3NACalrBfed8_erd-4dEbnR5zW9vBADyanstyZNiOiJl5PZV8kVfjhk1TO9LvUHPmPxxonbQ1y4U2JIbF5IiGv-2OQDrro9Bi_hPU_5ZJRr2_ZJuPAROL7bSAEOpS-_tpOR4bnJCFexiQqBvSAPBCNEWnMBFfAVhpfIRDDo5tOKrBdGoarR_0l352ae7aZbOVqrvR758Wug73l30UoReFuLwTHqMidqGa6r51NFttb-oZNtzINLc2A5iwKEm2Ne2qY5JaXtE2iRCMuOHglKZXUj2YOkWPpJizVr19WF951D7NeKbHCi7wvvZlK5OKNPnDfdsU19HaM5MPtU1ZbxiSklbEQc5VCL0f_fNiQnuJztyzof-3730fE8QIndFnEdpBF0NA0vPbxAs3JtKCZa4Tz1-UrbrscXwcOfBh2wtPzMavcdPF1ZFyMUSNHn4xA1sDFDVzpqSEX6_J6ooIyB_i04_AyicnCTO-H_kprM03pS02nIJ02ifqm6o7sY6LWzrS22nj5Cn7aUmdVZgOruo4vb5BWHj8w_zYa6PTJV4Vy4nCEKy6_6qZpkLsoIBpPxUbGBUE2Eqts6cZjDGtt2dQB4MseeiYJ3texJU4oM6yVzQmx1unnn3lRvqh6afxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو رو قطعا بیشتر از یکبار نگاه می‌کنید
🔹
حال و هوای گلزار شهدای میناب پس از دفن قطعات به تازگی شناسایی و دفن شده دانش‌آموزان شهید مدرسه شجره طیبه/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676179" target="_blank">📅 23:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZeaicmuMNpcQMsg4toHCOVGxkkyvOXCuxnuc1LSH3gwytaRQj1YE_MHcwtltKpEIi0WKLEE_xhEB3HzYERhSIOx22NxYRodj4OyIh3a8CTuA1ra7Zd4Xsm-JzDA36_NOGWvm2kRu9jkOCJUbceJbYFZhBjm5CYVQuFj6SsIz7oCBPyQgbQcv38fAN0K4p30K7NeOzPbRplMZHM2aXwhcDbUvVr8UjrH22oMEUB5sn5DiWaKGS6esw7xzZn1syqbAN0yi42RDRhUCP4ah6wixSIwY7eZH3yWBJQgN0YTW9HxfCF7ayPHzQZpZnvk5vKR24fx6bcWALD6vZmqv-JsKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdbCKuu45EwRF1-NCSRXL-bbz6KjINWrZHZJ06SlM5pf9oOkikVCl4QfocIcNQ4GzblgsjvLJiG3nUDol93cwlfno0argj8FrxkvqJ0-288mFdeWd9YbwFq575R9m7zZ1Tqu0YpoYbfX5lAz27tudM0_OoppTWIrPVu-pTfwGR6UPo5SrMJEhGcCenmLi9o-3FOHSPlIzteHQcuMoKEikVk-9vfH8fO583uZsZ9MtJSK4qmJ3M-mkZMOpZ5MRdShqBJ2IkZ4-h16h7laYFqK_k4f3jN6MUrPcw7UKkGrBT7t8_OJ2IONCuAKFnpfgf3tAFJC4C2AhCHeG3N-cI9luA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMQqoltqTIUlsKkOh9ulp4vGGRRfs0aVSwUg1eucJI2S8VZ9hTy7oq6HaXAEfjvPtai7HkjNKhRMGfW6Ava78MthgLPIrk-I355R2k0SNgHiQWKpPMmOK3eNeiTTIZWPiDzIugXB6GNHFoXDJ1xUYvKIrw2eP8Iqfq6kVr6Je8T6V8MM4_HfBxAxJkkJJqxbqQxcW9CVQDKBgb2v9d-Te-LGpyVRWEdljZAlslqsJ0m2wmSp5cyctMKgxl_KuZDaI5M3lpRis-F2DwzUWJs6rXBHtPMingAeul_Sqjv2wSVhPFc5_2ZAUK_Bwhy6o6MFBZcUKrZvKU5MjtEXtmiBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZADzJ1VF9DFWGy3qZu71niDuiaVxuRdSXUucPzR5XFpV_SXN62y7-RZydre8yqAazt7NPpguge2Qcsyz7W9V9rsO_hb7iFKItfG4lNNS1lONNtSgAHXMNNXWCWL4x0P2M38C288oSF2cdBFk1wgrOL0UFTvtwgLA9uvlNLFw7rFpPJWgEjapdXx1-AKOBjADkTfbjlDhctGJJ-L217jsBMF3_99AOAfH2WXE-RZ5hyoF7T88i2bKASd9kYEUGCdWxXRvVR2SBDhaFNaBV7qx0rr7LrSpkBkFj8YEjlzHVTUfI2RgxbbCXP8VS97b5_L3XzTgrcVay19ohjAtj-DSRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac68f6bd9.mp4?token=SdCVO73_jQkoWwr127t99LTeFHB2Kj-9Tg0DK6EVyT1qRgdiJ48VX2mqglEQsdTAe3VaKvtW8rLDH8pi-699SdMYufMoDkjgSgqJp1fcuG6kuomnsBac4WuiyNZES_puZeTSPEaGrrXnZBx9svXsa7AIxDcYY2WSKp32b_Z2LAGgnjKwIxZ0bbwmjdVZxTx7hiQBMPm2idHlf1Ih9gzGGvQGpobsZ5RhvkxRDHT72ggGbpJPOUQ3Ev_j7k3rdnTi5UYxudqDcNUDXQyDSRaJVB3zJ4BnV1z0Sap5APLEeVPbpgGg-S_Xk9lW86lDmjycLFuJnZ4_Ji_ztbp58c3XxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac68f6bd9.mp4?token=SdCVO73_jQkoWwr127t99LTeFHB2Kj-9Tg0DK6EVyT1qRgdiJ48VX2mqglEQsdTAe3VaKvtW8rLDH8pi-699SdMYufMoDkjgSgqJp1fcuG6kuomnsBac4WuiyNZES_puZeTSPEaGrrXnZBx9svXsa7AIxDcYY2WSKp32b_Z2LAGgnjKwIxZ0bbwmjdVZxTx7hiQBMPm2idHlf1Ih9gzGGvQGpobsZ5RhvkxRDHT72ggGbpJPOUQ3Ev_j7k3rdnTi5UYxudqDcNUDXQyDSRaJVB3zJ4BnV1z0Sap5APLEeVPbpgGg-S_Xk9lW86lDmjycLFuJnZ4_Ji_ztbp58c3XxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه خونین در جاده کاشمر به کوهسرخ
رییس اداره آتش نشانی کاشمر :
🔹
عصر امروز در جاده کاشمر به کوهسرخ، یک مینی‌بوس حامل مسافران به درون دره‌ای عمیق سقوط کرد.
🔹
این حادثه منجر به جان باختن ۶ نفر و مصدومیت ۲۳ تن دیگر شده است.
🔹
مینی‌بوس در کیلومتر ۱۸، با تپه‌ای خاکی برخورد و به درون دره سقوط کرد.
🔹
در این حادثه، تعداد زیادی از سرنشینان مینی‌بوس در داخل خودرو محبوس شدند تمامی سرنشینان این خودرو از زنان شهرستان گناباد بودند که در حال تردد در این مسیر بودند./ صدای خراسان
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/676173" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع عربی: شعله‌های آتش از پایگاه آمریکایی الحریر در استان اربیل عراق برخاسته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676172" target="_blank">📅 23:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676171">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عربستان باز هم پای عراق را به میان کشید
🔹
وزارت دفاع عربستان مدعی حمله پهپادی به تاسیسات نفتی در منطقه الشرقیه این کشور از مبدا عراق شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/676171" target="_blank">📅 23:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676170">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
با گذشت ۱۵۰ شب، حضور پرشور مردم همچنان حال‌وهوای شب‌های تهران را رقم می‌زند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/676170" target="_blank">📅 23:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676169">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c462fed8.mp4?token=uprrWAdxLv5ZJESI1h3dYe9boIMN3jggUZSJeTudQGxcDx7_DY8999EKLmIoGo6cUBo_QUJd3WXzlG6gYF0aN1JNcfQHb4BkWxm6fIH7b1q1HMDJZl0QKCpcxBMYlV9qnntBp50h0tWtvgeL2Kf8nXGd7V6TxVhQVxiPXDVskmyq1hQm3xo3DldYMaypEx33xzFIKJrdsKMM49QREJ_UeWemgkPMPlfGEuEJaZ-ZQPI9imbVi_vzGYkLHI1p5RvO3O0MsXwBAvcfHoEqbtsDf5EhD0Nc6YKi-u1X-kozEjqAVorAoPm43K-7qGafJHXmKs-_z3JuIkVaEUEWsNOqrYDBTEMbZl75MHgdAntMvXQDsK7eAduVzT33M_Mc76xxtXfgsFLi1znNV6RnM7AG1j5nsgbxQMm0wl38CHcuSG-TQcvQS3gS_BGa6Q0FylcoyqHt7eRiWlPyF-6-GCNO54iBQqazK4-cInvD0ITvCBwizEv9lfH7Lx5QfZVEPTomIKrYVUzydKa2aOqt8Vm48SkVmmQbyL66dE33Fj777TcTxzplUUqOns3iWr9LVdhFePW-w2EJn6xLekKWiPFpum1YKelnbnWAz1Mdi6nKCEvCNbpR6wHMc0vRJZa7VPOO43tNcCeDGfLJWv1eqLgWxxAg70PQ4XsbKoLwKeHFfdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c462fed8.mp4?token=uprrWAdxLv5ZJESI1h3dYe9boIMN3jggUZSJeTudQGxcDx7_DY8999EKLmIoGo6cUBo_QUJd3WXzlG6gYF0aN1JNcfQHb4BkWxm6fIH7b1q1HMDJZl0QKCpcxBMYlV9qnntBp50h0tWtvgeL2Kf8nXGd7V6TxVhQVxiPXDVskmyq1hQm3xo3DldYMaypEx33xzFIKJrdsKMM49QREJ_UeWemgkPMPlfGEuEJaZ-ZQPI9imbVi_vzGYkLHI1p5RvO3O0MsXwBAvcfHoEqbtsDf5EhD0Nc6YKi-u1X-kozEjqAVorAoPm43K-7qGafJHXmKs-_z3JuIkVaEUEWsNOqrYDBTEMbZl75MHgdAntMvXQDsK7eAduVzT33M_Mc76xxtXfgsFLi1znNV6RnM7AG1j5nsgbxQMm0wl38CHcuSG-TQcvQS3gS_BGa6Q0FylcoyqHt7eRiWlPyF-6-GCNO54iBQqazK4-cInvD0ITvCBwizEv9lfH7Lx5QfZVEPTomIKrYVUzydKa2aOqt8Vm48SkVmmQbyL66dE33Fj777TcTxzplUUqOns3iWr9LVdhFePW-w2EJn6xLekKWiPFpum1YKelnbnWAz1Mdi6nKCEvCNbpR6wHMc0vRJZa7VPOO43tNcCeDGfLJWv1eqLgWxxAg70PQ4XsbKoLwKeHFfdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری کوتاه بر آنچه در مجمع پتروشیمی امیرکبیر رخ داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/676169" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyZFx-8qbCg5I8TfrO71ObmiQp9Gtl9ADFCYCDlX2_2C0jrMgtBQHuH771uG0nGpsuahzt3QLdnfSS9e3NzQ8TnRYhCh2wK_kVRgsuyct0E13Twph0eWIARGNGaH8RR6PrmA570WkCJqVf3R4zBSa7fpAF04qKWiy59E8ss8EuOfV_3N-J7Ota_oEi5sLwMle3rJ5BMYs32EP1KuuUCyWvfEFn3q1QAkIeH52ko_woIAI0CAQKJJd83feTx_ZH0WmGE8i-SJmjXtC35viDY7M7pOtiCxI-IvWHZ0mZj2HSCIjofpYKZ7HNUxuATYxmHK7Z7o-PefZ0Drs2QVaZEEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک حادثه امنیتی در دریای سرخ؛
هدف قرار دادن یک کشتی در دریای سرخ در سواحل یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/676168" target="_blank">📅 23:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع عربی: شعله‌های آتش از پایگاه آمریکایی الحریر در استان اربیل عراق برخاسته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/676167" target="_blank">📅 23:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZwy2p9ZWrs4-y92EE0ta__ByvvR_WEAFfXlz-DhWJHXqAnIGZLz4aylkJSTXF_LrRio_fHbkCt15BORDxs3lI1f-Ak3ptvJLjwn9WfjfUSfuXPTL-RYNSQ6WiMoBW181b1UzORyNTuqZGi6_CrvShQLK-6j3ukcucbOIKiipQvTcP5NHZMEtghTe37hzmYPnLNUYPcbdHEaE3xufZYHjdBHNs611CWofyLkLKaPziripz99UkJeoWfUiE2HjkKCBSC8A7sZORso6OzI23flyGEdIIa-aC9Fqj3XqC1XH-jJxGxMJiHZ3-4qgVkRcpEukMJKbT4hKmHc1b9gW8pqSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wf6FTVU72pkWeLLQulFKC7INmPE91HQGJrP14-sEwZP2UjquXxe3zLqtr1rOXQkFoJoPmvJrnGVtAahWsA9CEvPncdiMWiJ0u69Hfq9Iw3ykm_3vEAwlZmgh-zLdjyXO8PhPWXBJ53i1AB4Jwb5eVgQEKZmBEtoRTCHfm8ROrqASosknqQyWiKAqW6YrieqR6v-udVNpmoZD_N8hUDTb_TAebKpYk6XUw_wvyNk-xwnzNZydE0NEYFE30DQwYoEQjoWxN_xlVOdeoAn2_pZBmOGIviNzS2eqa6eLzYbaFwJoWCTiOWXncaIKsHipsUhWBlcejptQ5qF3bZs7TKDlDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای، روایت ریاض از حمله به تأسیسات نفتی را به چالش کشید
🔹
تصاویر ماهواره‌ای خسارت به مجتمع عظیم بقیق (فرآوری ۵ تا ۷ درصد نفت جهان) و آتش‌سوزی در جازان و ینبع را نشان می‌دهد. / جماران
🔹
این با ادعای عربستان درباره انهدام کامل پهپادها در تناقض است و می‌تواند بازار نفت را متشنج کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/676164" target="_blank">📅 23:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-NNOrOi81rEely7g2VAWbsBc3U0qt2GHjnpczJMbnGs3pCCimIAKMeWxQsMIcnb2gUZC_VuX5Iaf17ZvMXvlDkjszKXimniOLstlMlCCdjMlxQZVkbi8lm5FwV3V_U7xLn931h3Eh5O-b1KVKSnCtwTjeKvZKPz2r3PxQgTlAoJTxUl398Tev9WBZJqeBfGKUjlcCS0EBfHWH8sW29W5LexGZ7DfJ--M_qGjZ9nQmO-S4uRRW4AJQyrF72xZAc5W4sV7Z8gEXemwe7p1Fq_mCTS3eOC4LQ8eoNUJVthhHTotC4CzE4Vbj7L_h-AKnUDNh6xO284WF9nsgLMZ9uK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در عربستان پول پارو کرد!
🔹
کریستیانو رونالدو در کمتر از ۴ سال در النصر ۶۲۵ میلیون یورو درآمد داشته که بالاترین قرارداد تاریخ فوتبال است.
🔹
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
🔹
پاداش برای ۱۲۹ گل: ۱۱ میلیون یورو
🔹
پاداش برای ۲۳ پاس گل: ۱ میلیون یورو
🔹
دو جایزه بهترین گلزن لیگ: ۸.۵ میلیون یورو
🔹
پاداش قهرمانی در لیگ: ۸.۵ میلیون یورو
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/676163" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMLfgo_YYEWaJvzo1y4LdVHfsVp3vA9Jy-t5qLi87sliFj9rAjETV1l_1lRPJyQup22aNjwuchM4W-d0yTnwrEmE2WV31l2NQLsqJCXQH6rC7L81E2sd7ZRPdpXAhY2mLc_sy2RoSJ2f8pZwYqcuVkGyOJESyAgjFtcBM_qktEPELsowwcvFVEhhjv3AaENtY3x0csLFT9D0dW4heOTEF_MdVNqKQUi-6wBzZVC8-gyQNt7VwwU2l--wwfYd-b76l3zEezQTH70HQaq20o8vB7rKo40oK18nDwlyxA3J1U-lRK1FzN0nMVJyhFASZyd9NC4rj-I9qwFZmBN-uoyjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار محرمانه پنتاگون؛ آمریکا روز بعد از شهادت لاریجانی ۷۰ زخمی داد
وب‌سایت آمریکایی Raw Story:
🔹
دا‌ده‌های پنهان پنتاگون از تلفات و زخمی‌شدن ۷۰ سرباز آمریکایی در یک روز از جنگ ترامپ با ایران خبر می‌دهد.
🔹
گروه «وار هورس» این سوابق را از طریق درخواست قانون آزادی اطلاعات مبنی بر درخواست اسناد دولتی  که شش هفته اول جنگ، از ۲۸ فوریه تا ۸ آوریل را پوشش می‌دهد  به دست آورد.
🔹
بزرگترین روز تلفات در این داده‌ها، در ۱۸ مارس، تقریباً ۲۴ ساعت پس از حمله هوایی آمریکا و اسرائیل که منجر به ترور علی لاریجانی شد رخ داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/676162" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای رئیس اداره دیپلماسی عمومی اسرائیل: تمرکز اصلی این دیدار بر پرونده ایران بود؛ موضوع «کوه کلنگ» اصلاً در این نشست مطرح نشد
🔹
هدف نتانیاهو تعمیق هماهنگی راهبردی با ترامپ بود، نه کشاندن ایالات متحده به درگیری.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/676161" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def029722a.mp4?token=YYomkrAZ09WODRlP59eGVPmTZYRwgS70IRG8r4OAuDUmpRjymDmKBBvpaU5DawBcB844DphjkPtYLNe_FxFnIk_4GBSDRJTlhQ5DzPoEn80BKA7nB6PsultULuG8Hn576omfxDqS75eTh1-QDRTrKL_C4kio1OByFNVPk7ZX9kCYOVgsaStejAnN5QodEkhvlxyfrkEa64Iq4gt3crAoOIQWsfeBes9qG9o8gTmeOINvUfS2E2yvIR7o524y0YLbfXR881zbdFuTuXcx7qyrizxNNVmbAPTrbaKA-O1Ai940AEsYdZqEYCEFCsU42X6FmuLKo1LT4XDXcQap7PwLfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def029722a.mp4?token=YYomkrAZ09WODRlP59eGVPmTZYRwgS70IRG8r4OAuDUmpRjymDmKBBvpaU5DawBcB844DphjkPtYLNe_FxFnIk_4GBSDRJTlhQ5DzPoEn80BKA7nB6PsultULuG8Hn576omfxDqS75eTh1-QDRTrKL_C4kio1OByFNVPk7ZX9kCYOVgsaStejAnN5QodEkhvlxyfrkEa64Iq4gt3crAoOIQWsfeBes9qG9o8gTmeOINvUfS2E2yvIR7o524y0YLbfXR881zbdFuTuXcx7qyrizxNNVmbAPTrbaKA-O1Ai940AEsYdZqEYCEFCsU42X6FmuLKo1LT4XDXcQap7PwLfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا ایران است؛ سرزمین مردمی که می‌ایستند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/676160" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e595e00fab.mp4?token=X8FX8RnS5jB8C6p3jkrnpqCpB1-GqR9B_suQ5tsySgHVSmQ8t_B1li3brAZXJ18PaWUokGB9N9uZZ05tnONK_Z-raiTpdYoQ8BtuBAzsFB-3uICthn3UrDi8Qoxjbh9HmKJ8xkuQL8fezRiLBMbHBfMnqme73o0UFmHsvdPAxTdoY7bslyeMbzvgvJFT030OAux4yVjd_GSEYHsi4HdaStvLAFKjWIJHSvt-UTmB4JbB6HakWhP1cyWsfn7CMsSBZbZdSeGkMgzVY2NMCq8eVBRgoJ8BHYTS4C3H-goUWuLmC_aYb-d3-G2bNYKItmyu-8o8SMc7vf2McMXok9eEySvSmptNZj8yChCjySn1MfqpV38roJIFZpJIHb7Dmgwtbfgd3d1SVpjRipvUkdxEqJYVNTg5O_OxyxcFg8ks3MX5CQWcYIu36-gcIKTZ5keMNQyILrqVk8gCb8MwQTDAUEvyeMFi7JMaSoxwdhkNKOAas6o9MR9YYqh_d3s7paoZjnj3mdZJcNu1tFQDc3LVObtWFkRueG0kNsSn8Ey6wQQ-Y8NqaX_ZR2CAHONnA6nQCCNrLEsu-Ve9nKiMFk8Eb-7nQk_7WMjmJlWNYHFglgUyssFSlbXQ-9SdsqHNjVcB4turMWctIBxAfmadhyDWVQw6Gv_wbaaa-WeY1ZFP5lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e595e00fab.mp4?token=X8FX8RnS5jB8C6p3jkrnpqCpB1-GqR9B_suQ5tsySgHVSmQ8t_B1li3brAZXJ18PaWUokGB9N9uZZ05tnONK_Z-raiTpdYoQ8BtuBAzsFB-3uICthn3UrDi8Qoxjbh9HmKJ8xkuQL8fezRiLBMbHBfMnqme73o0UFmHsvdPAxTdoY7bslyeMbzvgvJFT030OAux4yVjd_GSEYHsi4HdaStvLAFKjWIJHSvt-UTmB4JbB6HakWhP1cyWsfn7CMsSBZbZdSeGkMgzVY2NMCq8eVBRgoJ8BHYTS4C3H-goUWuLmC_aYb-d3-G2bNYKItmyu-8o8SMc7vf2McMXok9eEySvSmptNZj8yChCjySn1MfqpV38roJIFZpJIHb7Dmgwtbfgd3d1SVpjRipvUkdxEqJYVNTg5O_OxyxcFg8ks3MX5CQWcYIu36-gcIKTZ5keMNQyILrqVk8gCb8MwQTDAUEvyeMFi7JMaSoxwdhkNKOAas6o9MR9YYqh_d3s7paoZjnj3mdZJcNu1tFQDc3LVObtWFkRueG0kNsSn8Ey6wQQ-Y8NqaX_ZR2CAHONnA6nQCCNrLEsu-Ve9nKiMFk8Eb-7nQk_7WMjmJlWNYHFglgUyssFSlbXQ-9SdsqHNjVcB4turMWctIBxAfmadhyDWVQw6Gv_wbaaa-WeY1ZFP5lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت از آب شیرین‌کن جاسک بعد از حمله ناجوانمردانه آمریکای جنایتکار
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/676159" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg_b9OEhf1VIxyKsPcRPKn9l5jap3JTbI2dDMeJmB1Nlr4_-BKFrk7oilo9eTYFDyQpHPo8OXaI40JlVR4eNg4PEHIXHHcbD0pUT51SCsxN96db1qpn0aD6hO-j0P4ONmC1XOQdfQjpbwCqZtLg-Y1Xz36BTdjCR9WLK--agwPb09m1yq7b1TIzW4aPBgkQ4yYR4LyT8VqrWcYPcgUCMZ6527EY9tU-rmyZzfs0q7H5d7pVFoUgwnUGKlJninIa8Vzt7INDczxjqDOCDu1HWpEOgVaO0upJsc-QlxeBobljl8rQJs1PCil-ruv4QugY3ZsHSnhpTuB3R-LlpGICL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: اوکراین اطمینان داد حمله به کشتی ایرانی غیرعمدی بوده است
🔹
سید عباس عراقچی با اشاره به گفت‌وگو با همتای اوکراینی خود اعلام کرد کی‌یف تأکید کرده که حمله به کشتی ایرانی غیرعمدی بوده و به‌دنبال تنش نیست.
🔹
وزیر خارجه ایران افزود تهران نیز به‌دنبال تشدید تنش نیست، اما بر غیرقابل‌قبول بودن حمله به منافع ایران و لزوم جبران خسارت‌ها تأکید کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/676158" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آقای من (:</div>
  <div class="tg-doc-extra">حسین‌طاهری.. قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/676154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
بسته‌ی
#مداحی
#هیئت_قرار
ویژه
#اربعین
شماره ۲
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/676154" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بحرین برای حمایت از حملات ایران ۱۰ سال حبس گذاشت
دیلی‌تریبون:
🔹
دادگاه عالی جنایی بحرین پس از محکومیت دو متهم به جرایم مربوط به حمایت و تجلیل از حملات ایران علیه پادشاهی بحرین، هر کدام را به ۱۰ سال زندان محکوم کرد.
🔹
دادگاه همچنین هر یک از متهمان را به پرداخت ۲۰۰۰ دینار بحرین جریمه نقدی محکوم و حکم به مصادره اقلام توقیفی داد. این احکام در دو پرونده جداگانه مربوط به فعالیت در رسانه‌های اجتماعی صادر شده است که در آن متهمان تصاویر، ویدیوها و نظراتی را منتشر کرده بودند که از حملات حمایت و آن را تأیید می‌کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/676153" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676152">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc360cad4.mp4?token=MOJGabTqb_XPuCuXMsuJK-0GpCGsM6KtAl92SfI8SacqalTAAfRgrbRW31H0EnfdlkAAZZzYTuX3-JAGu0s3wvkH312NCDP-2ZPwxUSvszPPC0Y350okq_c78cuATbH-syQXE0WQxpje_4mFk9n0ioup_e2GgHJRoJKlf3MQHhqAIDoGaL0SSbe-5rcvZbwUeLPH7WKqlaWXFIzCprdsBspnMA4DX-Rpd-CcrmNo6PAwlUC6KqdtK_J4TeFuWUoe66Jb-L4t2s8iAi1etXAic_fAzGxk5SHM4hNqTY4oNMrd8Gl0J3MxoTeZhgEvn2_HQGM6YPatAl3Tpw2pZkmAYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc360cad4.mp4?token=MOJGabTqb_XPuCuXMsuJK-0GpCGsM6KtAl92SfI8SacqalTAAfRgrbRW31H0EnfdlkAAZZzYTuX3-JAGu0s3wvkH312NCDP-2ZPwxUSvszPPC0Y350okq_c78cuATbH-syQXE0WQxpje_4mFk9n0ioup_e2GgHJRoJKlf3MQHhqAIDoGaL0SSbe-5rcvZbwUeLPH7WKqlaWXFIzCprdsBspnMA4DX-Rpd-CcrmNo6PAwlUC6KqdtK_J4TeFuWUoe66Jb-L4t2s8iAi1etXAic_fAzGxk5SHM4hNqTY4oNMrd8Gl0J3MxoTeZhgEvn2_HQGM6YPatAl3Tpw2pZkmAYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی بود؛ هنوز هم هست
🔹
در مراسم رونمایی از طرح مهرورزی هنوز هم یاد عزیز از دست رفته برای خانواده‌های جان‌بخش زنده بود و در هر گوشه‌ای از مراسم برخی اعضای خانواده جان‌بخش قاب عکس را در آغوش گرفته و امیدوار بودند با اهدای عضو مادران و پدران دیگری شاد شده باشند؛ با این شعار که یکی بود و هنوز هم هست./اخبار تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/676152" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPAOJz423tvsmV4jI57HFSXybncsTMTxjf2kwdlnJt77-AWpX_gj18-_OFs2am9bvqmS9QtXRJT-WMWiGJpemGVSEslOwvXnEa_mBsUy5fMDvdIxBl7ogfizxU9CN5kPDCXK7H9-kCW5TOHpzRrBC-j14vIbBVc_One_6SC6E0m7Dsd9ds0_agpI3mT3hnB7LMJRi7I57bF4GSF82wP_PBTC8xlfO0zR96gw1BZSwk_yr39FQzHlM36dEI0Q6SsZD3suecDaBqAX3x8FrWkB97x0A7Zqr0M0LlWnXeCGAXkcUndgNENFTqUnY6f38ZF-STx6GO61WHMTDuPImvjHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد زلنسکی برای ترامپ: اوکراین، اسرائیل اروپا شود
پایگاه خبری Responsible Statecraft:
🔹
اوکراین از آن نوع شرکایی است که وقتی دیگران اقدامی نمی‌کنند، دست به اقدام می‌زند. هدف زلنسکی متقاعد کردن ترامپ برای پذیرفتن اوکراین به عنوان شریکی از نوع اسرائیل برای آمریکا در اروپای شرقی است.
🔹
جایی که می‌تواند در مقابله با تجاوز روسیه، مهار توسعه‌طلبی روسیه و محافظت از اروپا و ناتو مفید باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676150" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMTXAGevufCad6iX-VN1WrV_ffNos31HaZaFovMylxeKRoy2xlu33loI42SJjWGI_Zppk11d7dIzO1VCiE0hRz1KtVbcuCfCTZR65t7mvHrIGgFKjd2RgUaVFJ25e7SnjVOOcogF43jqo-D1DimlH2u-_PFxc5odjflPQsLaiG3QQkBv8hceXC_CUbnPf0D9rqicQoj91hQZCap0sU-usVIzbthHDtyrrCYrSOeqvpc1cVNSEpiKer_DOlbHjyQz01bibL21JaR9R4OTNTIXv9owTqkILIkC4xxCgXBLekrKyqHljYgYQfvbAl0Irp5H8WGVMk0V-30L-kpMmsMQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌹
یک قدم تا زیارت کربلا…
با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و فرصت خود را برای برنده شدن یکی از ۱۰۰۱ سفر زیارتی کربلا امتحان کنید.
✨
این سفر معنوی به همت هیئت قرار برگزار می‌شود؛ شاید نام شما یکی از زائران این کاروان نور باشد…
📲
همین حالا عدد ۲ را ارسال کنید و در این پویش حسینی همراه شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/676149" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اطمینان‌خاطر به مردم؛ تا آخر سال تمام انبارها پر است
پیمان فلسفی، عضو کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از جنگ دوازده روزه ما کمبودهایی در حوزه نهاده‌ها داشتیم؛ با تاکیدات رهبر شهید و مدیریت دولت، چند برابر نیاز کشور دپو انجام دادیم و تا پایان سال ۱۴۰۵ هیچ کمبودی نداریم.
🔹
طبق پیگیری‌های مجلس، وزارت راه و خانم وزیر قول داده‌اند اقدامات لازم را برای حمایت از ناوگان جاده‌ای انجام دهند تا جهش قیمتی رخ ندهد. همچنین وزارت راه و شهرسازی متعهد شده است تا کیفیت جاده‌های مواصلاتی و ناوگان ریلی را بهتر کنند تا جوابگوی بسته شدن بنادر باشند.
🔹
در خصوص خرید تضمینی محصولات استراتژیک مانند گندم، دولت همیشه چه امسال و چه سال‌های قبل با تاخیر پرداخت‌ها را انجام می‌داد. پرداخت‌های این بخش معمولا از درآمدهای نفتی تامین می‌شد که با توجه به شرایط فعلی ما از دولت مطالبه کردیم تا راه‌های تامین مالی جایگزین را پیدا کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/676147" target="_blank">📅 21:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f8d58e31.mp4?token=ZJJ874nPBFZYY5GTsgz9wS73br-VsIXqN5igFIyPP_lKpLajyCA0oG_KzlAaFpiSGpkJooTmCgzfH1paIjnXACmfYvn0M1m2uDSD2gLQg41xleLpC7sP8JuCy8xcQq07cXlYBPw9mKzyIFbE0TRKNHcp7IvaXkfqSYp8a9Wwqt1LjjkQ8e9fEE78LCVjtSfzVWAXAyRfthQlARvUTVHG6ms6M7ynWw3eZS2rcV4JlXLUpt5FtA1WgwUD_6-ERqEl3iDEAVNN1QDyMPCgtQIs8siw5EdlnTkQQCM1fFyoTHL0XwoGAi48gze2r7pEKjk_fnrSj_ocLDHE8B2SDpYEPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f8d58e31.mp4?token=ZJJ874nPBFZYY5GTsgz9wS73br-VsIXqN5igFIyPP_lKpLajyCA0oG_KzlAaFpiSGpkJooTmCgzfH1paIjnXACmfYvn0M1m2uDSD2gLQg41xleLpC7sP8JuCy8xcQq07cXlYBPw9mKzyIFbE0TRKNHcp7IvaXkfqSYp8a9Wwqt1LjjkQ8e9fEE78LCVjtSfzVWAXAyRfthQlARvUTVHG6ms6M7ynWw3eZS2rcV4JlXLUpt5FtA1WgwUD_6-ERqEl3iDEAVNN1QDyMPCgtQIs8siw5EdlnTkQQCM1fFyoTHL0XwoGAi48gze2r7pEKjk_fnrSj_ocLDHE8B2SDpYEPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: طرف مقابل فکرنکند که ایران مادام‌العمر عضو NPT خواهد ماند؛ همۀ گزینه‌ها روی میز است
🔹
ما با بحث دربارۀ خروج از NPT مخالفتی نداریم. جنگ و زدن تاسیسات هسته‌ای کشور فرصت مناسبی برای بررسی موضوع داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/676145" target="_blank">📅 21:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
غریب‌آبادی: در حال حاضر وضعیت ما مثل کشوری است که عضو NPT نیست
🔹
هیچ بازرسی از آژانس در ایران وجود ندارد و هیچ اظهارنامه‌ای نمی‌دهیم و تمام دسترسی‌های آژانس قطع شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/676144" target="_blank">📅 21:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش و ترامپ قمارباز در کاخ سفید دیدار کردند  نتانیاهو کودک‌کش پس از دیدار با ترامپ:
🔹
درباره جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگوی خوبی داشته و بر هماهنگی کامل دو طرف تأکید کرد. #Demon #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/676143" target="_blank">📅 21:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8946dc2c80.mp4?token=G_v3i8YH_vCtxBvbhuPU81KAlzYPjdsKUAfhJw-tf61djIk1PkaqElght4iHQ_TL8H8-668_IOrnMnKlonzhlB_LF-Yc2l6UJ7vREkKZn6wdhFEKTWBTzmotxHoKE1m-6dnNvrsn-XTSMCvVqXK3hperMgpQ7b-niVcXsatfaUf2gqPilP6SFgMGz4FBCDpzGu7GXzShEOnhjlfrsrgOWTtyN4ZQGV8K9LKuydVHUBvHyw7Z9dkw3vPyv3yMiwseJ0hhZ9Oe1uYdvCvFazVxCCW-K2QJrD5J7pr4YcPBK1hjNQdQd5Ap7q7QLcA9sOfuVc5iclI2MpBI8H3jnl3zUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8946dc2c80.mp4?token=G_v3i8YH_vCtxBvbhuPU81KAlzYPjdsKUAfhJw-tf61djIk1PkaqElght4iHQ_TL8H8-668_IOrnMnKlonzhlB_LF-Yc2l6UJ7vREkKZn6wdhFEKTWBTzmotxHoKE1m-6dnNvrsn-XTSMCvVqXK3hperMgpQ7b-niVcXsatfaUf2gqPilP6SFgMGz4FBCDpzGu7GXzShEOnhjlfrsrgOWTtyN4ZQGV8K9LKuydVHUBvHyw7Z9dkw3vPyv3yMiwseJ0hhZ9Oe1uYdvCvFazVxCCW-K2QJrD5J7pr4YcPBK1hjNQdQd5Ap7q7QLcA9sOfuVc5iclI2MpBI8H3jnl3zUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمک‌های ترامپ به مردم جاسک/ در پی حمله آمریکا به بندر جاسک، بیش از ۳۰ لنج صیادی مردم جاسک در آتش تجاوز آمریکا از بین رفته است و همین موضوع باعث نابودی معیشت ده‌ها خانواده شده است
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/676142" target="_blank">📅 21:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پشت‌پرده رسوب خودروهای وارداتی در گمرک/ پای شرکت‌های تراستی در میان است؟/ کنایه دادفر به روندهای دست و پاگیری اداری
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری:
🔹
از زمان ثبت سفارش تا ورود خودرو به کشور، به طور متوسط حدود ۶ ماه زمان لازم است. خودروهای بسیاری وارد کشور شده‌اند که به دلیل صادر نشدن کد ساتا، همچنان امکان ترخیص و شماره‌گذاری ندارند.
🔹
بسیاری از این خودروها با منابع ارزی خود و دیگران تأمین شده‌اند، اما همچنان با بهانه محدودیت‌های ارزی و موانع اداری روبه‌رو هستند. این روند زمینه‌ساز رانت و فساد شده و شرکت‌های تراستی نیز در این میان نقش دارند.
🔹
در دوره جنگ، روند خروج کالا از گمرکات روان‌تر شد؛ موضوعی که نشان می‌دهد تسهیل فرآیندها امکان‌پذیر است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/676139" target="_blank">📅 21:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1bc7e4c1.mp4?token=WuBbFYyq8usxA5QUdrJA8_bAQvGD22xHourKdntnZ9dcrTKnSVmYHff-xCJkBjuxGalc5uX4VLntD_p3qB3O39qUKAmAYRd2NXs5k0qGEd3RbXcSVIV70hNLRThQUxwl6FLqF5HFXE9NsD0DjOb2M6HzL1sRnciJidUnddtS8mT_Pqm4ktY7Um8FBLvCR0zMci2p4d5wFBNWDu5lwW27UyZOUmXfYMo8RYEoE99reHHqk5eJVOdmSppLJlqKBptT1MPVADcZZnC2Dc7Wuya7kZn7t3evirsPvATixMjhmvJzlqWsxmkq3eoZogv8QdRqMY4xtwgf4_JAmYxh8cFoWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1bc7e4c1.mp4?token=WuBbFYyq8usxA5QUdrJA8_bAQvGD22xHourKdntnZ9dcrTKnSVmYHff-xCJkBjuxGalc5uX4VLntD_p3qB3O39qUKAmAYRd2NXs5k0qGEd3RbXcSVIV70hNLRThQUxwl6FLqF5HFXE9NsD0DjOb2M6HzL1sRnciJidUnddtS8mT_Pqm4ktY7Um8FBLvCR0zMci2p4d5wFBNWDu5lwW27UyZOUmXfYMo8RYEoE99reHHqk5eJVOdmSppLJlqKBptT1MPVADcZZnC2Dc7Wuya7kZn7t3evirsPvATixMjhmvJzlqWsxmkq3eoZogv8QdRqMY4xtwgf4_JAmYxh8cFoWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: در حال حاضر وضعیت ما مثل کشوری است که عضو NPT نیست
🔹
هیچ بازرسی از آژانس در ایران وجود ندارد و هیچ اظهارنامه‌ای نمی‌دهیم و تمام دسترسی‌های آژانس قطع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676138" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd11c18a66.mp4?token=Nqbte164H0a_nAF-XHmbwjcc88lRxP1qKOvJvp3FW8mxiLRe57evcTAkKOwP8184UuVn2M-pHM_fj2HG0iHceuGHNRDnOCdndFy04dJXIM-HihoHmoXt3n9c_-WnXEogapZo08SP6A4nFXz6AtgQBl6JcB5LM0QP2arE7qXeim2-EvAXn0ouSaqs53gK0l4C32yy1yGbZT2WzIDRTSXoZpIQ7TsCoZX0Rt8_8axwHXCoLEcOz25IYW2hywsY_5JSPkMBUk5yr4hx6656fkEy60hxSvriHZ6yPZ7vdoAloGMjkJKE9GuyPVundJk8miaGUkk-HTYxEpgfWQVc8_822w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd11c18a66.mp4?token=Nqbte164H0a_nAF-XHmbwjcc88lRxP1qKOvJvp3FW8mxiLRe57evcTAkKOwP8184UuVn2M-pHM_fj2HG0iHceuGHNRDnOCdndFy04dJXIM-HihoHmoXt3n9c_-WnXEogapZo08SP6A4nFXz6AtgQBl6JcB5LM0QP2arE7qXeim2-EvAXn0ouSaqs53gK0l4C32yy1yGbZT2WzIDRTSXoZpIQ7TsCoZX0Rt8_8axwHXCoLEcOz25IYW2hywsY_5JSPkMBUk5yr4hx6656fkEy60hxSvriHZ6yPZ7vdoAloGMjkJKE9GuyPVundJk8miaGUkk-HTYxEpgfWQVc8_822w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواص آبمیوه های مختلف از زبون خودشون
😀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/676133" target="_blank">📅 21:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgxV-eomqDNTJggvnJUMDwqb6sCbqjPjVKtvDybevviTEE4vfVEMuQX-hgrx7YawDKl9k1q-hhSqrBGD-weV-jtQi5ZtJSq8n5dOiMLY7VWJx4Yo_p5VjoNmUJj9lyi5U__N3K1KAiOY-uNKiA1EpT8eo-RFTZUjyH_i_pTT52CT4Ikg-1NuENlC6nqMoPuD4rS6E5j-_xeUYkG_trw9tfzNeaDR64T3aiIaSzKjjfFCaTtZpIFolrvNiVQS4IZioXZ1zPY9bfDbJqL4XwK2cjor1Zkm7_OHbQBNXvRzVheZ4tnecYbrAp4sTuMyq7SRTSrFB4VEHjqTD6dqdjVY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاروان اهالی هنر و رسانه به کربلا رسید؛ زیارت به نیایت از رهبر شهید
🔹
کاروان اهالی هنر و رسانه به میزبانی ستاد اربعین شهرداری تهران روز گذشته دوشنبه ۵ مرداد ابتدا عازم نجف و سپس کربلا شد.
🔹
هنرمندان، سینماگران، کارگردانان و مجریان تلویزیونی در این سفر همراه شدند که از جمله آنها می توان به مهدی فرجی، منوچهر محمدی، دانش اقباشاوی، سیدعلی احمدی، محمود کریمی، محمدرضا شفیعی، سعید پروینی، جواد شمقدری، حسین شمقدری، وحید رونقی، احسان مهدی، حامد مدرس، علی صدری نیا، حبیب والی نژاد، محسن اسلام زاده، بشیر حسینی، هادی نائیجی، فاطمه افشاریان، محیا اسناوندی، راحله امینیان، فضه سادات حسینی، شهره پیرانی، محمدرضا باقری و همچنین چهره هایی چون حجت الاسلام شهاب مرادی اشاره کرد.
🔹
این سفر که به دعوت ستاد اربعین شهرداری تهران انجام شده، قرار است نوعی قدردانی از مردم عراق بابت اقدامات میزبانی همه ساله اربعین و برگزاری آئین تشییع باشکوه رهبر شهید و جنگ رمضان باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/676132" target="_blank">📅 21:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676130">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ6UaHZV3ZtMEqKlQVNXYPP-gqSRgQkIuwaqOyEEEP1vjvL-93pFgrJlGy3xB-WfY7SxLpycrvqngKOYW9H6CW-4IRcMMI5tkGzyw15KMFHCdlr-QCkJFMc2ZIKkjlUSbJfic6k2n_oj70TlHrkj3sBgDtly_Ad_8Ac6c8Mm_DQLCfScBu_CKmtdFsngczMNhJN8Ufne7ILIFQ3x4yGwjFWLxTZwEFAR_GNFchq0vYiOxZSs68P4Y3-GYgm1XqUgVvRJDmk59eabzEzJHJHBa9gzg8oR06pbHdScDncqLkgyRIVtYFLqD8bEE0Tmtfd4sAG5_nxiJM0ldhyNZi-YqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، هر جا باشی بیمه‌ای!
فرقی نمی‌کنه
کجای شهری
؛ پشت میز کاری، توی خونه‌ای یا حتی در حال سفری.
✅
با
بیمه‌بازار
برای خرید بیمه
لازم نیست جایی بری
...
کافیه وارد
سایت بشی
، بیمه‌ها رو
مقایسه کنی
و فقط در
چند دقیقه
بیمه‌ات رو بخری.
👈
برای مقایسه بیمه ها وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/676130" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676129">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
کی‌یف به تهران: قصدی برای تنش‌افزایی نداریم
وزیر خارجه اوکراین در گفتگوی تلفنی با عراقچی:
🔹
هدف این کشور تنها دفاع در برابر روسیه است و کی‌یف هیچ‌گونه قصدی برای هدف قرار دادن کشتی‌های غیرنظامی یا تنش‌افزایی با ایران ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676129" target="_blank">📅 20:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DttBGIiEQ1Ep1RfQ4mVCw5K6HRsLM2KXOosvGa1RnK2sUL_UoBo_YPd_vW9j8cuJd9nAZW3QUBukqGkmJraFjvE8SIapU9icxS6sZPgG8IRApkmggwR4r642kmjhWgTj1ouHj1QDnD8H3r4kV6jcFPT4QmQJFL_P5eXMOQBNOanXhilJbbJFi7Av-qWGM4TTf8EmJMalosIsYRp4oijNFAGBcWkd0yqfPFjrQYnWua0P496TL9RuEbbLFgr-jJMoi6tHRcB8gFMWJAxIN5Nl81thy3hjanhGOscypaYHVFMo85zb5jY8hQgnwcm6DX_jmf_y_Dr8h1r8Dxa6p1uqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1KV-qCC2Eizal5dAEOYfCslB6c-Mved_vyN9ChwujTYM3qrMqZI64nxpJ-595NCOSR_6ZYpeSROkHlBYqJyRuM5MWT3hWi4QpdqsjB6y4R2h6c1PuxZ_n-yj2VByi21MIG-GDAqKjc2WC32nCKvx_o7SFgVXXWn-tLhiGYw1xY5RIqRpKdL05RSJQkFS6cPTbmhdFYOoBqp0mQryc8uPc1NWaJtpgXn8Rmk2mUhCkaVL5XUl5-8Oy66F7Nd597KbVlp1DAGQYeBZpUPWVE5oaZ5dMsTy-1lH2kP8--9OWI89GpovliCBDp3SlxvSuNVFMTF793NUO_yGEDZptIWGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از هر چهار جوان ایرانی، یک نفر نه شاغل است و نه در حال آموزش
🔸
بر اساس آخرین آمار، بیش‌از ۲۴ درصد از جوانان ۱۵ تا ۲۴ ساله ایران در گروه NEET قرار دارند؛ یعنی نه شاغل هستند، نه تحصیل می‌کنند و نه در دوره‌های آموزشی حضور دارند.
🔸
این نرخ از میانگین جهانی ۲۰ درصد بالاتر است، اما نسبت به کشورهایی مانند هند، عمان، اردن، عراق، تاجیکستان و افغانستان پایین‌تر است.
🔸
کمترین نرخ جوانان NEET نیز به ژاپن، سنگاپور، روسیه، سوئیس و امارات تعلق دارد؛ کشورهایی که بخش بزرگی از جوانان آن‌ها یا در حال تحصیل‌اند یا وارد بازار کار شده‌اند.
📊
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/676127" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
غریب‌آبادی: مسیر موقت تنگه هرمز باید تحت کنترل ایران باشد
🔹
ایران با پیشنهاد مسیر مشترک ۵۰-۵۰ با عمان موافق نیست و تأکید کرد مسیر ورود باید کامل در اختیار ایران باشد و بخشی از مسیر خروج هم به ایران واگذار شود.
🔹
اگر با عمان به تفاهم نرسیم، مسیرمان در مورد تنگه را ادامه می‌دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676126" target="_blank">📅 20:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
یمن: حمله به نفتکش سعودی NCC GHAZAL
نیروهای مسلح یمن:
🔹
یک نفتکش سعودی را به‌دلیل نقض ممنوعیت کشتیرانی با چند موشک بالستیک هدف قرار داده و آن را مجبور به عقب‌نشینی کرده‌ایم./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/676125" target="_blank">📅 20:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676122">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از برزخ؛ از آب روان تا عذاب مال حرام
🔹
00:10:00 احساس حضور حضرت ابالفضل با نوشیدن آب از دست بانو
🔹
00:19:40 بسته بودن دست‌های کسی که او را نبخشیده بودم
🔹
00:33:00 طلب مرگ حتمی از خداوند به خاطر گریه و ناراحتی عزیزانم
🔹
00:45:30 رؤیت عذاب انسانی با چهره قورباغه و داشتن ظرفی پر از لجن
🔹
00:48:35 قطع شدن زبان شخص نمازگزار و متدین
🔹
00:53:00 در اتاقی پر از گل‌های زیبا، لباسی از طلا برای من دوخته می‌شد
🔹
01:00:45  بازگشت به جسم با روسری که توسط بانویی بر سر من گذاشته شد
🔹
قسمت سیزدهم (حق)، فصل پنجم
🔹
#تجربه‌گر
: نرجس اربابی
🔹
قسمت قبلی
🔹
قسمت بعدی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/676122" target="_blank">📅 20:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3798deff95.mp4?token=Bi3LxLghA0CfY8Qzox_chlRbhXuH7NNXLOwGgkKwHGHBvJhJVWwl79H4bTm_x0Ue7q4-1WPyns7w0L_cCXRW2qUbmd6XxYjWwfEjvhYDNFyp06zhlUF6welLQd3L8FYQ2Wcxs9HkxmkaWi4R920hBkJIansUQ8BFZgTEdynrJMh5KdGNrzS8n61ahHtxRJ4Ea3lGqdHbmuN-TTUZclWOIHNSKuZrpW_-j1IjQ6RorQfAA6AS0mQDB-9bsfcdugqWUhE2sUsTZreuzDs4qpU3FtibtC34tywnTt_xCxVcP2PUu-JQoH_x1kvsq3lbyUUiCiZIIpI96bfDLetsER12Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3798deff95.mp4?token=Bi3LxLghA0CfY8Qzox_chlRbhXuH7NNXLOwGgkKwHGHBvJhJVWwl79H4bTm_x0Ue7q4-1WPyns7w0L_cCXRW2qUbmd6XxYjWwfEjvhYDNFyp06zhlUF6welLQd3L8FYQ2Wcxs9HkxmkaWi4R920hBkJIansUQ8BFZgTEdynrJMh5KdGNrzS8n61ahHtxRJ4Ea3lGqdHbmuN-TTUZclWOIHNSKuZrpW_-j1IjQ6RorQfAA6AS0mQDB-9bsfcdugqWUhE2sUsTZreuzDs4qpU3FtibtC34tywnTt_xCxVcP2PUu-JQoH_x1kvsq3lbyUUiCiZIIpI96bfDLetsER12Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌ابادی: هدف ما در تنگه هرمز هم اعمال حاکمیت است و هم کسب درآمد
🔹
این‌که بگوییم کسب درآمد از تنگه اولویت ما نیست اشتباه است.
🔹
ما در زمان محاصره از طریق کریدورهای مختلف بخش زیادی از کالاهای خودمان را تامین می‌کنیم اما بسته‌بودن تنگه هرمز تقریبا به کل دنیا فشار وارد می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676121" target="_blank">📅 20:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676118">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxCOBL83jmEJPpMS-wwar6P7X7F6ZYZslTfmXFaimyBughax2BIsCRNTkQBe8Mz5GMZMpLzy4J4hNSGY9yE_TYAPaHTbfxPAm8ZJxBnQQjF3rE-Kv-hrO3zRx2P2KaQ1JcHa-8VWXZV0bWI9J0gMDYpp8ZENRagSwsts44LcoLneVpG1Vmq_stZbXQQwhWdHFWFjHyktR8ZpCYAGMR8h8bK86bFby9Jc0zoekdqsQRjgTS9O7cqinLz6dKDVNvdXEabZ8S4-I1FwCmarS9Yxq1_py7W_zX1jdaffJCCyrXDIXCD5xVXgGjqv7mhtwy6aBu6xhO8Xzji0MzAkKWLJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/676118" target="_blank">📅 20:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676117">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51060c4698.mp4?token=i0hX-R6V9SV1EXzZdLDN0Y1G_3fJgTqS56p2Xef7y0hNdJSbF7APOlsblhTqK8HoYyiv5cHgRs21-qVip9od-0Li2ciRC02MUkMeN5OVHrRDIQ1Dh4bLQWYiD86Y60Y7ceM-cilvOsT49SZGfB2KfOyvUMTjdopGQA9GqKcaEaj_JnsPCCI692AURI4ntCArLNvafVmRf35qwTcBa7bpgnU0f-Y4nUNCdGhVbWKR65IdZ4zJnRXvVoCGHMdd0GdkV5z9IAeg1BVe2pRefSZtMCn9I26DfnrAJdlzHE1O3JpotPo-uz8ngb7sf2wermf-upROlHAvcGBguRw1IqhZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51060c4698.mp4?token=i0hX-R6V9SV1EXzZdLDN0Y1G_3fJgTqS56p2Xef7y0hNdJSbF7APOlsblhTqK8HoYyiv5cHgRs21-qVip9od-0Li2ciRC02MUkMeN5OVHrRDIQ1Dh4bLQWYiD86Y60Y7ceM-cilvOsT49SZGfB2KfOyvUMTjdopGQA9GqKcaEaj_JnsPCCI692AURI4ntCArLNvafVmRf35qwTcBa7bpgnU0f-Y4nUNCdGhVbWKR65IdZ4zJnRXvVoCGHMdd0GdkV5z9IAeg1BVe2pRefSZtMCn9I26DfnrAJdlzHE1O3JpotPo-uz8ngb7sf2wermf-upROlHAvcGBguRw1IqhZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: ما هیچ تقاضایی برای مذاکره با آمریکا در ۱۵ روز گذشته نداشته‌ایم
🔹
آمریکایی‌ها از ما تقاضای گفت‌وگو کرده‌اند؛ آن‌ها همچنین از طریق عمان به ما پیام دادند که اقدامات نظامی علیه ما انجام نمی‌دهند.
🔹
عمانی‌ها می‌خواستند یک کشوری را برای مین‌زدایی از بخش جنوبی تنگۀ هرمز بیاورند اما ما اجازه ندادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676117" target="_blank">📅 20:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifebb-k4WOuYe3Z-W2W8zhJEGnytl5X7SO6vO5K4U42QMkOJQGLHAXsFIyoXiRc-GQdSI0SwMaGuK_3NbFmNXx7HCKLV0OZ_7f7xYOu8FKWZnmelyll3oCnP0rGeXHizkGlfdu0wn0HAYlXLWNT4Sae6BPUYKWTjDd9TRv7ScfzyuwlUEP7WTk2Qq3Jq0QonFWjlPOBL4Vp1cB3kVG_SYqor0jUh9VVfvyaRtCKkLqfFtUCudTHdlxdzKgchWri8uEhctgnAzrxsY8R8exqA7ejE8mxpvDvdANX13sUFYtdrfDDD_UySBMZm2hoNtp8ZoD_JvYfGxE2DvqHH7qhmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مثلث شوم
🔹
هم‌زمانی سفر نتانیاهو و زلنسکی به واشنگتن، آن هم پس از تنش‌های اخیر، گمانه‌زنی‌ها درباره شکل‌گیری هماهنگی‌های جدید علیه ایران را افزایش داده است. برخی ناظران معتقدند این تحرکات دیپلماتیک، به‌ویژه با توجه به حمله اخیر اوکراین به یک کشتی ایرانی در دریای خزر، می‌تواند نقشه‌ای برای افزایش فشارها بر تهران باشد. سوابق سفرهای گذشته نتانیاهو به آمریکا که با تحولات مهمی همراه بوده، موجب شده برخی تحلیلگران از احتمال شکل‌گیری یک «مثلث شوم» میان آمریکا، اسرائیل و اوکراین علیه ایران سخن بگویند.
🔹
هشتصدوبیست‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/676115" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa27eb9b0f.mp4?token=NlmoxEAkgTZZTw9yoPDQtocqW__O5gTG59puWXg3B4Fkj-x3lwlUourpL7HhIFHHnsfoClGSYVUkOk0sv5FLq3oRoYbVvVP5XZdYMUgQmbZ63VM2fz0w9z88RrOMwsEUHfFJ7MopDZkFz102nLAC9I7M5hpw-7dwgDkMNuHKZAVPk5QpQXggQlesO9oN3UsxmJyOapjvrNermmhC52g1KOL0fj6Y58_JkW8u-T8jIiaaWapNCImf8zz2OqTvTNb2wL3IWr5NSdb5OboHHvsJ4e2an2sEFYGkLI0w0K5Xh8pxNWu0IduzJU2I1wwhk72vOb2-8Y9oUPx2Rt97zre7blFUBu6GIIg8E1QRyGYgzI0E8urClHa0yxz35lY-XlynpAMCAXFiyWNyJfcFQ7EA81h1N_7g0aBN0NOkRx3RdirSnGhjQV4NnlPcmti6oDfFnzkDZ1Ycvde35gPqnlF2bNYH30cXOtllRo7oMQlOnQ8-lo8SSSad7TK0UNwhUDsDJxeNQMDDR5dagNu18bdiySxbjEz1-jFbqOdCY151VqCrfOWHRnoyMHR2dvJxkhxX4IFBsSO_uSGhBML4TM3PGfj_cKKEZab_e187bQTsNuSF0jxgOCGS_GJu2v4KCnTsE1gsaZYDhHoDYqKn2bxZ3cnZJCbR3n1ndIa16KBLQqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa27eb9b0f.mp4?token=NlmoxEAkgTZZTw9yoPDQtocqW__O5gTG59puWXg3B4Fkj-x3lwlUourpL7HhIFHHnsfoClGSYVUkOk0sv5FLq3oRoYbVvVP5XZdYMUgQmbZ63VM2fz0w9z88RrOMwsEUHfFJ7MopDZkFz102nLAC9I7M5hpw-7dwgDkMNuHKZAVPk5QpQXggQlesO9oN3UsxmJyOapjvrNermmhC52g1KOL0fj6Y58_JkW8u-T8jIiaaWapNCImf8zz2OqTvTNb2wL3IWr5NSdb5OboHHvsJ4e2an2sEFYGkLI0w0K5Xh8pxNWu0IduzJU2I1wwhk72vOb2-8Y9oUPx2Rt97zre7blFUBu6GIIg8E1QRyGYgzI0E8urClHa0yxz35lY-XlynpAMCAXFiyWNyJfcFQ7EA81h1N_7g0aBN0NOkRx3RdirSnGhjQV4NnlPcmti6oDfFnzkDZ1Ycvde35gPqnlF2bNYH30cXOtllRo7oMQlOnQ8-lo8SSSad7TK0UNwhUDsDJxeNQMDDR5dagNu18bdiySxbjEz1-jFbqOdCY151VqCrfOWHRnoyMHR2dvJxkhxX4IFBsSO_uSGhBML4TM3PGfj_cKKEZab_e187bQTsNuSF0jxgOCGS_GJu2v4KCnTsE1gsaZYDhHoDYqKn2bxZ3cnZJCbR3n1ndIa16KBLQqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی یک فعال صنعت دارو از نفوذ مافیای دارو به مطب پزشکان: به اسم تجویز مکمل، مردمی که به نان شب‌شان محتاج هستند را سرکیسه می‌کنند!!!
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
▫️
https://aparat.com/v/uov38ts
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/676112" target="_blank">📅 20:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
غریب آبادی: اگر بند ۵ تفاهم نمی‌شد، اصل یادداشت تفاهم اسلام‌آباد اصلاً شکل نمی‌گرفت
معاون حقوقی وزیر امور خارجه:
🔹
تنگه هرمز دیگر به ترتیبات پیش از جنگ بازنخواهد گشت؛ این سیاست قطعی نظام است.
🔹
مسئولیت مین‌زدایی بر عهده ایران است، اما نحوه مدیریت آینده تنگه هرمز کاملاً تغییر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/676111" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
غریب‌آبادی: اگر ما مسیر جنوبی تنگۀ هرمز را باز می‌کردیم دیگر به‌هیچ‌وجه نمی‌توانستیم در تنگه اعمال حاکمیت کنیم
🔹
ایران برای اینکه حاکمیت خود را بر تنگه تثبیت کند نگران هیچ اقدامی نیست؛ حتی از سرگیری جنگ.
🔹
هر ناو اروپایی که بخواهد نزدیک تنگه هرمز بیاید هدف مشروع ماست
🔹
سیاست جمهوی اسلامی ایران این است که تنگه هرمز هیچ‌گاه به حالت قبل از جنگ برنگردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/676108" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676105">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSNKwQ0ePWAlpszfFwL5JWm67o-YvZOIbQE63gkYcmrTp7q0AaYzdT1fnMZwpI2kDhl9qSSDjX7AsULPaESn_tKpaW4j-1f4inBJIsyGzU-b_bTJreSPGUrwDhAYHRqgX6M9L755lHWFWmN6D0AIew0O1uqQ4duuST25R8UWCCdAbrYCzN9Ij7pIk18adH0tD_mVomUyzMJoDB0pQWQiMPlEVHwltMcMeLTJC2--ccywkvyQZ7eg3nk8UiqGjEKxt0AuOsR93hXCe4J_H8u3BzTU28I7ZjPb6vJhwoPVLVuXSLOk7qIAEVDwJfm4-qON7mTiBwFNM9viNY_xTJikdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش و ترامپ قمارباز در کاخ سفید دیدار کردند
نتانیاهو کودک‌کش پس از دیدار با ترامپ:
🔹
درباره جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگوی خوبی داشته و بر هماهنگی کامل دو طرف تأکید کرد.
#Demon
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/676105" target="_blank">📅 19:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676104">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک کارشناس سیاسی: می‌توانیم با جولانی هم کار کنیم
الله‌کرم مشتاقی، دیپلمات ایرانی و کارشناس غرب آسیا در
#گفتگو
با خبرفوری:
🔹
ما می‌توانیم با نزدیک شدن به طیف میانه‌روتر در سوریه با دولت فعلی سوریه و جولانی هم کار کنیم. جنگ‌های خونین ما و سران فعلی حکومت سوریه باعث سخت شدن ارتباط برقرار کردن بین دو کشور می‌شود اما مردم سوریه هنوز حضور جمهوری اسلامی در سوریه را از یاد نبرده‌اند.
🔹
ایران تنها کشوری بود که هیچگاه سوریه را غارت نکرد. دولت جولانی نیز پالس‌های مثبتی به ایران میفرستد. مثل مصادره نکردن اموال ایران در سوریه و تعطیل نکردن حوزه‌های علمی شیعه در سوریه. به نظر می‌رسد دولت جولانی بدش نمی‌آید که ده هزار مسافر ایرانی به سوریه سفر کنند هم برای زیارت و هم برای تفریح.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/676104" target="_blank">📅 19:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676103">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e32faa19b.mp4?token=YdG8GtqbgQlaYPtFquv2BQ90UxnqDYlSS_L6EueD5dk5Z0VwEGk3Dld43t1mkBYjMyNi0L4Lr5vfr8rh5j0TvmCjaS8PHxzy8S9yyp0L1Omlj-oYXIbnQ2T8fTlKy24f1ELv_NTxtLl8l8-yr_Fmt5dXV70CUZwz0U5Bn_R-aBd_PpzU_8szfRt91Nf2ZAhxw4ohdvFcqaK8NXejxFatLxvHEg8Zzlqui24Ro_gxMsGGSyBzAY7sbRypYG6LssDwWcWSy9y_At1E47u3eUn9E6Kj60go1YV_myipZtxXQQn0SxQJlIFDlkbVpApHZ6VUISaU5g1UgYGgcfWJCW_FQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e32faa19b.mp4?token=YdG8GtqbgQlaYPtFquv2BQ90UxnqDYlSS_L6EueD5dk5Z0VwEGk3Dld43t1mkBYjMyNi0L4Lr5vfr8rh5j0TvmCjaS8PHxzy8S9yyp0L1Omlj-oYXIbnQ2T8fTlKy24f1ELv_NTxtLl8l8-yr_Fmt5dXV70CUZwz0U5Bn_R-aBd_PpzU_8szfRt91Nf2ZAhxw4ohdvFcqaK8NXejxFatLxvHEg8Zzlqui24Ro_gxMsGGSyBzAY7sbRypYG6LssDwWcWSy9y_At1E47u3eUn9E6Kj60go1YV_myipZtxXQQn0SxQJlIFDlkbVpApHZ6VUISaU5g1UgYGgcfWJCW_FQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای منتشر شده در تاریخ ۲۷ جولای از تأسیسات نفتی در ینبع عربستان سعودی منتشر شده که نشان میدهد بنظر این تاسیسات نیز هدف حملات نیروهای انصار الله قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/676103" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676102">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty-gBtpFshvHDhd0ua2XG9UqQBPxnaRFRwuTXOodt648wI0eVpj2gYu6lFiRA3_4DHv3URmmkhsro0kk9P6ZJIKM-UTriDQ_lrFBuBFB0hH7ynTsv1pQQzTOAf8nX6FykrS7FGVAM9ennD5gDPtdq8QrZt3t5qT8a-dPccPDKDqa5WzsocDtYU1802tqyKQqi6H6IMb0lnTu-yPcRIL9joJK8lxjRKUZeHHgZSTVP1654ZDqa7YQot-iVi0ZADBDNU7-hQw2SU7nKD12kK741ueRFAR3JZSBsOiQtf37PK5ZS3CRwt2u6iwkoQiCR-MfVcSJ0c_DOFukQGuuGpt-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افت ۱۶.۸ درصدی تولید خودرو
🔹
آمار تولید خودروسازان نشان می‌دهد مجموع تولید خودرو در سال ۱۴۰۴ به ۹۲۲ هزار و ۹۳۴ دستگاه رسیده که در مقایسه با یک میلیون و ۱۱۱ هزار و ۷۰۴ دستگاه در سال ۱۴۰۳، از افت ۱۶.۸ درصدی حکایت دارد.
🔹
در میان غول‌های خودروسازی، ایران‌خودرو برخلاف روند کلی بازار، تولید خود را ۶ درصد افزایش داد و از ۵۰۴ هزار و ۷۵۹ دستگاه به ۵۳۵ هزار و ۲۱۰ دستگاه رساند. اما سایپا با افت ۳۸ درصدی، تولید خود را از ۳۴۱ هزار و ۸۵۲ دستگاه به ۲۱۰ هزار و ۳۴۷ دستگاه کاهش داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676102" target="_blank">📅 19:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676101">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52551de2f4.mp4?token=ZjsZ0LdQfGur1TUcEBRpTrVoWVBANBaamof6OT7OMhpJ2gFNJrFMTbnjs8HHGmrDiGllFmF8wrXcr4G2-7XcQPc90eppyhmJyX5P71pi8naQADgxDVOog6SY5Awld9e-x-o76XhFXfrqVy1iOTUhvB9XXg5slUWMTAiPqyEu53lwy2wpILCrt9jaamptQ0-hMut7nKaomp-1NmWH9uf39lyVsOK3s2o8FdoI4Ax2f7zEUcr9boh6PnyLAvvzR2rVCKBgxlxpWqpgWqyvlFj6QP74TAlYrc6pMVtqXjUhbkvC9rLvdfBmmF43EIlwCuNwh07P990IKqooJW8MRL870A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52551de2f4.mp4?token=ZjsZ0LdQfGur1TUcEBRpTrVoWVBANBaamof6OT7OMhpJ2gFNJrFMTbnjs8HHGmrDiGllFmF8wrXcr4G2-7XcQPc90eppyhmJyX5P71pi8naQADgxDVOog6SY5Awld9e-x-o76XhFXfrqVy1iOTUhvB9XXg5slUWMTAiPqyEu53lwy2wpILCrt9jaamptQ0-hMut7nKaomp-1NmWH9uf39lyVsOK3s2o8FdoI4Ax2f7zEUcr9boh6PnyLAvvzR2rVCKBgxlxpWqpgWqyvlFj6QP74TAlYrc6pMVtqXjUhbkvC9rLvdfBmmF43EIlwCuNwh07P990IKqooJW8MRL870A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند راحت قارچ‌هات رو با سلیقه خورد کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/676101" target="_blank">📅 18:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3be888146.mp4?token=fwjz9CaeuKNblEN8KZykIVoBXAEc4NXUPDmoryqiC8JiHOoVQ1kafF76T-2m0Ol5yTwUJrkqSPcH_4aWAtJuIGTzlFl6qCrxh0TbRLLdDfN_JvqKndQFy4SlbX7YZ7LyAUaJxfymjpKOfHxHa_Hf68ghuUy8ACnojuc_9hEz5Y75glaaF8leKeX_2q_iK1mUC97l3GqqYEQNAH8EFjdOuDOJtVgnDAhvuDCKMOM3clBnIGxG16D9f8B0XkvQYqlmXpqv66KU70QKLv5MP__i9F4r82swhJ9HgLylWBBXlQeEkMSZC1BhjWtdGZfzMJOIexCPMeV44tU5nXpHw7zboolBtL8ydmcvv12BPPfKvHEhKrY9BLKaKZdM5xf5mQ0w8NnWIvHDRvPTs8HWL7XrNaZwOHMdXoyPAWkzxHhUFBWUkMfI3hWdme_lRTz4NiTbpvo0u_L2FvVwkWJ5h368uxC-ku22vKxxC7-15gq3bfyb1DRPNgLMiUCRc6NP9CrmfsKwbWwVWVkGUO8PxQt0pweNcBrR_znASgn8Rg6WckU6ueuCqnwI6ShFqBhkeEV4WnR8m71E9ew-UNyotErLYmbE5iWqdoAyGDq0ox_eaaqL9MTLIqybvytU6Mq5CqIy_FOivlkJxfk5vhDp0UB_nLGpm1QY5zOf1oxp93hEtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3be888146.mp4?token=fwjz9CaeuKNblEN8KZykIVoBXAEc4NXUPDmoryqiC8JiHOoVQ1kafF76T-2m0Ol5yTwUJrkqSPcH_4aWAtJuIGTzlFl6qCrxh0TbRLLdDfN_JvqKndQFy4SlbX7YZ7LyAUaJxfymjpKOfHxHa_Hf68ghuUy8ACnojuc_9hEz5Y75glaaF8leKeX_2q_iK1mUC97l3GqqYEQNAH8EFjdOuDOJtVgnDAhvuDCKMOM3clBnIGxG16D9f8B0XkvQYqlmXpqv66KU70QKLv5MP__i9F4r82swhJ9HgLylWBBXlQeEkMSZC1BhjWtdGZfzMJOIexCPMeV44tU5nXpHw7zboolBtL8ydmcvv12BPPfKvHEhKrY9BLKaKZdM5xf5mQ0w8NnWIvHDRvPTs8HWL7XrNaZwOHMdXoyPAWkzxHhUFBWUkMfI3hWdme_lRTz4NiTbpvo0u_L2FvVwkWJ5h368uxC-ku22vKxxC7-15gq3bfyb1DRPNgLMiUCRc6NP9CrmfsKwbWwVWVkGUO8PxQt0pweNcBrR_znASgn8Rg6WckU6ueuCqnwI6ShFqBhkeEV4WnR8m71E9ew-UNyotErLYmbE5iWqdoAyGDq0ox_eaaqL9MTLIqybvytU6Mq5CqIy_FOivlkJxfk5vhDp0UB_nLGpm1QY5zOf1oxp93hEtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های متناقض از وزارت صمت و انجمن واردکنندگان خودرو؛ ثبت سفارش خودروهای وارداتی متوقف شد؟
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری
:
🔹
از ابتدای سال ۱۴۰۵ تا امروز، هیچ ثبت سفارش جدیدی برای واردکنندگان انجام نشده است. اگر وزارت صمت نظر دیگری دارد، می‌تواند مستندات خود را ارائه کند.
🔹
در حال حاضر فقط ویرایش و تمدید ثبت سفارش‌های قبلی امکان‌پذیر است. ویرایش ثبت سفارش‌ها نیز پس از سه ماه پیگیری و جنگ امکان‌پذیر شده است. شنیده می‌شود به دلیل شرایط موجود، امتیاز ثبت سفارش‌های پیشین در حال خرید و فروش است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/676097" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تصاویری از نعش لیندزی گراهام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/676096" target="_blank">📅 18:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVNUORfr_aDaEgKXz5MdoKp1sqkN4mQKC_TIKB6wW5_QHJXxtOVDqRRvMBrVXVL77FxlzbhuLovGpJg7SwCCgOzSt1ARKOKUu-AUWAeI7bXxqdy4ZkVIlDxG6DAnya2geTgqVX1J1pAsB8f1Ju-pbK4AXV0nMKG8Yl9okNQV_djfjKFnyEYNXZkRkVGo8uBUsbJvol5gQ9a9IagMlrIMh8gAd5ZCtPDisF_mPNGcwI55sKJu5kfH69CIY4_Xf3txVUKvyaO3bC1sK4hDIngwxG_yH53HdhRw7aEWAkTbfQvrtarV_Cjyu-nZpZ1tQh95nJLliR3EzfjlUENNlRvFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سرمایه‌گذاری در طلا چه گزینه‌هایی داریم؟
🟢
خرید طلای فیزیکی با هزینه‌هایی مانند اجرت، مالیات و اختلاف قیمت خرید و فروش همراه است. همچنین نگهداری امن، احتمال سرقت و اطمینان از اصالت طلا از دغدغه‌های این روش محسوب می‌شود.
🟢
صندوق‌های طلا امکان سرمایه‌گذاری آنلاین با مبالغ پایین و بدون اجرت و هزینه نگهداری را فراهم می‌کنند. بخش اصلی دارایی این صندوق‌ها از گواهی سپرده شمش و سکه تشکیل شده و پشتوانه فیزیکی آن‌ها در انبارهای بورس کالا نگهداری می‌شود.
🟢
صندوق طلای «رز ترنج» با مدیریت فعال ترکیب شمش، سکه و ابزارهای آپشن، از طریق تمام کارگزاری‌ها و با حداقل ۱۰۰ هزار تومان قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/676093" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTvs2vBvZ8BZyQbAoRUmlzznPXB1fBoUnsX4aO52kZxrxCkasYJUQRPcHRgNY8UQCWvFATsPX45Oa2Elfuvw2q1MbPY-1-MWoSH5NI73ZNDOr1tcyiibsoiyGB59bb6vuk6fH8chY154HBE5p3hOla3CKtEC-45gKuPbkUlIxtVgG9R7mWixDMxkT7lBZpCvqiNk6J2kCSsKHNYCPgBxHrI3fJtbFJAtWBK5mgd2XxISEcXc-ruvQOtnO5div_r0Z2xazSBnxp80hHc1OGNG5aU4PCLs23_ErUUO4ysKuCR__Q2vcoq2_EoRfHFHq_9MxJhXhbrha21C9AiBqZ6h6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبیز پیکارجو رئیس ‌هیات
مدیره
#بیمه_البرز
شد
پيكارجو داراي مدرک دکترای تخصصی اقتصاد مالی و بین‌الملل بوده كه استادیاري و عضويت در هیئت‌علمی دانشگاه آزاد اسلامی واحد علوم و تحقیقات، مدیرعاملی و عضویت در هیئت‌مدیره بیمه آرمان، قائم‌مقامی بیمه سینا و همچنین مدیریت طرح و توسعه بیمه ملت از جمله سوابق علمي و تخصصي وي مي باشد.
#بيمه_البرز_توانگر_و_ماندگار</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/676092" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blzBT2lUDARgtytfXeXu26dxy-Iq1ae1_ZDV9L1KXlQzQjYZpSAeh_2HZ6i2QTEg5aPoEy3ijCESIb6FFEAMQFWTg-aHQHR9lJy3F_93AnsuyNxA8iL96FQwJphgKxpYADPqKYbbIMCPDimLB0TDAwwpsM9Ypdfx1YMYY_qRDe5uWTZcQ1mFH9v8MKRrK_IIy8D7Q1duDBwIf0RvWjXO-LtyvNIb0Jerh2KL6giYxEbRjxsKEQUKa3rx8Bc0QkL5GixyvDBziNgv-n5kj4hqKAI27GfbixcEcTAqMsxIWnAcqvIm73QQbfUG9B4Ih0VqW6uOYR9MyM0xL6M5cQFAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلزله در گوگل؛ قمار ۲۰۰ میلیارد دلاری روی هوش مصنوعی
🔹
رقابت نفس‌گیر در هوش مصنوعی، گوگل را به نقطه‌ای بی‌سابقه رساند. این شرکت پس از بیش از دو دهه، برای نخستین بار با جریان نقدی آزاد منفی مواجه شده؛ اتفاقی که نتیجه سرمایه‌گذاری سنگین ۴۴.۹ میلیارد دلاری تنها در یک فصل روی زیرساخت‌های هوش مصنوعی است.
🔹
گوگل قصد دارد طی سال‌های آینده نزدیک به ۲۰۰ میلیارد دلار در توسعه زیرساخت‌های هوش مصنوعی سرمایه‌گذاری کند. اقدامی که این غول فناوری را به استقراض بیش از ۱۰۰ میلیارد دلار و تأمین مالی گسترده از بازار سرمایه واداشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/676091" target="_blank">📅 18:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676085">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuxIKGqKqiXc2irPihLk_8BYDkheT5HuQ6v4gMibCiCL2JV21ja6oOWYPbTVj8iEqFj8TtWw8xOP3Hnm3xsK2whaFjI76pSOFZYBu1AXSaJ9cryZszqWKHkpdUtCB10kZAFPQWEoL8e-rZRzP56XVI134Rm5GD5fC-Z6vyvI_ZdYIrcnbEE0ALRgSqLE0TzBFiHOOun6_wj0sIf-xcmod4ct24XgS1qKJ3ZMTUn-xP9zmwDRwbT4cgoLs7AZcNkKIyNn-T8NFpxm9JrwxGBmkO0Mn-xni9oTbAglFaj8QW93MymdWjFC7tx594CYz37OBwPDbuJH6FRXiEJkpw6rDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ وابستگی جمعیت چیست؟
🔹
نرخ وابستگی سنی نشان می‌دهد به ازای هر ۱۰۰ نفر جمعیت در سن کار (۱۵ تا ۶۴ سال)، چند نفر کودک یا سالمند وجود دارد. هرچه این شاخص کمتر باشد، سهم نیروی کار در جمعیت بیشتر و پنجره جمعیتی بازتر است.
🔹
بر اساس آمار سال ۲۰۲۴، جمهوری آفریقای مرکزی با نرخ وابستگی سنی ۱۰۴.۷ درصد در صدر جهان قرار دارد. پس از آن افغانستان و نیجریه بیشترین نرخ وابستگی را دارند.
🔹
ایران با نرخ ۴۴.۳ درصد در رتبه ۱۸۵ جهان قرار گرفته و از کشورهایی مانند ترکیه، هند، روسیه، آمریکا، بریتانیا، سوئد، عراق و ژاپن وضعیت بهتری دارد.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/676085" target="_blank">📅 17:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676083">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
یارانه ۳۰۰ معاند خارج‌نشین قطع شد
دادستان کل کشور:
🔹
تاکنون ۳۰۰ تن از معاندین خارج‌نشین که در داخل کشور یارانه دریافت می‌کردند، شناسایی و در کنار شناسایی اموال این افراد، یارانه نقدی این اشخاص قطع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/676083" target="_blank">📅 17:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676082">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iedetnR1k4nXIin-7A-QbSvtB3h-VL9Bhs-VAjt4N2HpJQ-5zAWdf4-6FH1vJ23LgjJNAjWclur9SMD5fsJoH9aw0UbOOqp1oOanVKPxMO-hwn9tTFBL2FiigcTYJvKRr5lLxKizA_0voiEKA1fMn6x3lvHKsdFwhY23RTSWt_4UhY19Wkc27rmsT6SlaSzzSr6Jf3giiMSyrY8opHzFTKbQYQjZFWyi9iVFTF9Qr0TNDppk-Gb3xUtKiopx0TBj16J_4upTsfosr6D5FflfenLsLBsAO_N54yX1R94yfzf8BWAE-6pUIxdt4UvdaxUsZOtT5BSSqWk1A0UfZsLQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه جدید ترامپ برای ایران بعد از توقف حملات موشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/676082" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676080">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cf68d6ca.mp4?token=HItpdfBIiVPbIhHzFhkHOr5aTI52-xSXHup-oAR_yQbssJerNw-k_OWQ4XVk9lWrSMRG0U8CEZa5lK_tnByJ0IeuJlPgu4IITYt9uL55C--J6Y9fMrz7S2OJ49pwQy1udB0mCgmjrgcO3je0AIueP2CLMa5PPs9SFCxGIXiRprCNFBYU2xXSFFt6dcU6pbkCkm7K8mk9y_ddLuHVcTmavJgZ-yaau_uF453ooSUvLZoefWgskjlrCisOdipuaJHOq-WMZCFHmbViRxXdvoNLm-z-xiMJBI75XSP8f6UbfqaDwDzf9CMdI6eeCE-RTDzjwkj5yL0d_YQvEFAUYclfoVfprk2r6ubpVPi1uhW-CQtSuPNT2d0IER23IRk6yJ5jOzzgt4B32VAx0QegAp_pBD-hzKPRiM7aEkF6FXHAmieR2REji48bUeFjeXZ5UkfqnX9MQKPjcUaKdjYq2pkr01eVAlh6uv_6L0S5KuxvDzXbCkmTybeXibWIJTSPeCCjKN3YoNTFFsk_Tk6PqIh6zn8d6FBh7AO8_8XjbIDLFNixAKJUyTAMf7Pl11yUII77H2mwSjHWnkY7mtF1Pn5DL17_hP9kgO0KPzBattccu8drbT0fQjK8fqwS4SayluTvSzSh2rmsxecfhqIASSC4rim4_zrmugH7c54cLxd72Y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cf68d6ca.mp4?token=HItpdfBIiVPbIhHzFhkHOr5aTI52-xSXHup-oAR_yQbssJerNw-k_OWQ4XVk9lWrSMRG0U8CEZa5lK_tnByJ0IeuJlPgu4IITYt9uL55C--J6Y9fMrz7S2OJ49pwQy1udB0mCgmjrgcO3je0AIueP2CLMa5PPs9SFCxGIXiRprCNFBYU2xXSFFt6dcU6pbkCkm7K8mk9y_ddLuHVcTmavJgZ-yaau_uF453ooSUvLZoefWgskjlrCisOdipuaJHOq-WMZCFHmbViRxXdvoNLm-z-xiMJBI75XSP8f6UbfqaDwDzf9CMdI6eeCE-RTDzjwkj5yL0d_YQvEFAUYclfoVfprk2r6ubpVPi1uhW-CQtSuPNT2d0IER23IRk6yJ5jOzzgt4B32VAx0QegAp_pBD-hzKPRiM7aEkF6FXHAmieR2REji48bUeFjeXZ5UkfqnX9MQKPjcUaKdjYq2pkr01eVAlh6uv_6L0S5KuxvDzXbCkmTybeXibWIJTSPeCCjKN3YoNTFFsk_Tk6PqIh6zn8d6FBh7AO8_8XjbIDLFNixAKJUyTAMf7Pl11yUII77H2mwSjHWnkY7mtF1Pn5DL17_hP9kgO0KPzBattccu8drbT0fQjK8fqwS4SayluTvSzSh2rmsxecfhqIASSC4rim4_zrmugH7c54cLxd72Y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میوه قهوه یا coffee cherry
برداشت با دست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/676080" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=ApztiOsDY4a5kmJzcAQj1fYgFjsFnCEXzHaoeV_euMc2Xuxqxv42B2c_7fixP4FMBni1AUpLkWiel4ZfC8H-NcNilhrt8WoVahu6pIkLrKWhFsTphPoGm3XDZvhw7DlbQTY_6M-81B4t3jHn98-im3UbHqhAiHKltk-Q2ZwFn_NvpkKIDEH-I6U9h3K0Hf_tP3bG0r-WxnmKdQxCLAzEIZGefO2jha3gXSu4jApvnPpYgN7KskxIDd1-FEpWBWhxAHwDK8-aR5XObW77rED8o7VdP45Me-ILWMxKlBsz0Zb2fE9u-gGlcyyBzRZi-hrTjKA_SFUAo_WKqF56RS1sbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=ApztiOsDY4a5kmJzcAQj1fYgFjsFnCEXzHaoeV_euMc2Xuxqxv42B2c_7fixP4FMBni1AUpLkWiel4ZfC8H-NcNilhrt8WoVahu6pIkLrKWhFsTphPoGm3XDZvhw7DlbQTY_6M-81B4t3jHn98-im3UbHqhAiHKltk-Q2ZwFn_NvpkKIDEH-I6U9h3K0Hf_tP3bG0r-WxnmKdQxCLAzEIZGefO2jha3gXSu4jApvnPpYgN7KskxIDd1-FEpWBWhxAHwDK8-aR5XObW77rED8o7VdP45Me-ILWMxKlBsz0Zb2fE9u-gGlcyyBzRZi-hrTjKA_SFUAo_WKqF56RS1sbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماینرهای غیرمجاز یکی از عوامل اصلی خاموشی‌ها هستند؛ گزارش‌های مردمی می‌تواند جان بیماران را نجات دهد
🔹
مصرف برق هر دستگاه استخراج غیرمجاز رمز‌ارز معادل مصرف حدود ۱۰ واحد مسکونی است و ادامه فعالیت این دستگاه‌ها، فشار سنگینی بر شبکه برق کشور وارد می‌کند. این موضوع می‌تواند به افزایش خاموشی‌ها منجر شود؛ خاموشی‌هایی که علاوه بر ایجاد مشکلات برای شهروندان، در مراکز درمانی و بیمارستان‌ها نیز تبعات جدی به همراه دارد.
🔹
شرکت توانیر از شهروندان خواست در صورت مشاهده نشانه‌هایی مانند صدای مداوم فن‌های قوی یا مصرف مشکوک برق در همسایگی، کارگاه‌ها یا سایر مناطق، موارد را از طریق پیامک به سامانه ۳۰۰۰۵۱۲۱ گزارش کنند. این شرکت تأکید کرده است که هویت گزارش‌دهندگان به‌طور کامل محرمانه باقی خواهد ماند و مشارکت مردم نقش مهمی در مقابله با استخراج غیرمجاز رمز‌ارز و حفظ پایداری شبکه برق کشور دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676079" target="_blank">📅 17:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koENdkJ1ZiBqVusRg5j4fmhCHXXuhUgTAqujtxqVGQ20p1PajLZajOipIdctDTicd68Ktc4CRO0hy1-K9jHlNWvY9s4dp56-VAH16GXqCWb43XJahjVmxYQL3qnJHWCuTn3LkCxv5yRL4X_04Eqe8GLoJ_RxPNBZO9u0AKPUeHkGFWL_qkFCmHZyfseFW7rwBcv5OQYJdA7qz0fuhU8A12FFfrpsqWsSasri7OKmtzKqygW10dffQBckPVQML1jgeTVyoGdsIFlxPVf88a8G0QxlCW9DwL1xkiCcKHUr5SW1tQxnWSBXr89_kWWRXMN3lMVDqHao6Y_GoMxMzTN7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز درباره جزئیات طرح پیشنهادی عمان به ایران
ادعای رویترز:
🔹
عمان طرحی با حمایت کشورهای خلیج فارس برای مدیریت تنگه هرمز، از جمله دریافت هزینه‌های داوطلبانه برای استفاده از آن، به ایران ارائه کرده است.
🔹
منبع خلیج‌فارس و دیپلمات غربی که در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند که طبق پیشنهاد عمان، ایران کنترل انحصاری نخواهد داشت و هزینه‌ها داوطلبانه خواهد بود.
🔹
این سیستم مشابه سیستمی است که در تنگه مالاکا در آسیا وجود دارد، جایی که اندونزی، مالزی و سنگاپور از کشتی‌ها می‌خواهند که برای تأمین مالی ناوبری، حفاظت از محیط زیست و عملیات جستجو و نجات، کمک‌های داوطلبانه پرداخت کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/676078" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dacecfac.mp4?token=HwHuZozJnOLgrelEyK4hza3Kl9eyHyVQEUy79X8VQ5jLHLMbzbnZNsOkvxxWQMZgm9gEuLUagqEWI7sq7DJUhKcjHgUUv2MNBAFCIUfMeB6Ad855Dk12zouWZnZ5WRcGliasMb0WgalmInxxCpc1xeobLL7TbwhrumDnCLkg8P89qPKNuo_idIXaoalGaduo-46zq1bxj6XUZyDGzev06t6wr3PsDOgVxXgyyYHabLMCEt7beZybUmqQ3EMog2OuHFVi2qXfl5SEfhwG1DXYeYdCHf7Dn1swd2tWmCi431hAcMBaF_xXdT-S6a7UzbhOUCFojlvWnpvvKuQAwOtUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dacecfac.mp4?token=HwHuZozJnOLgrelEyK4hza3Kl9eyHyVQEUy79X8VQ5jLHLMbzbnZNsOkvxxWQMZgm9gEuLUagqEWI7sq7DJUhKcjHgUUv2MNBAFCIUfMeB6Ad855Dk12zouWZnZ5WRcGliasMb0WgalmInxxCpc1xeobLL7TbwhrumDnCLkg8P89qPKNuo_idIXaoalGaduo-46zq1bxj6XUZyDGzev06t6wr3PsDOgVxXgyyYHabLMCEt7beZybUmqQ3EMog2OuHFVi2qXfl5SEfhwG1DXYeYdCHf7Dn1swd2tWmCi431hAcMBaF_xXdT-S6a7UzbhOUCFojlvWnpvvKuQAwOtUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این پرچم، فقط یک رنگ نیست؛ روایت یک ملت است، خانه‌ای که قلب میلیون‌ها نفر در آن می‌تپد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/676077" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb85359332.mp4?token=Sm8r-t4XMePq1h6HDoatY8wG-fIfrEVsJ2pYmZ3bPpkMMj_7GKgG6ABlD5KFaFFbr578_c03ZRVdQASNKXz5MaeuQ95b3UNdo29-8NQZ1TuSg7NiHzOgnk7OErz-I6hZ1zQ5aMNpixRH_NW2icKFfaDE8yQEDDVVQuhFCydJm_-6kgSof5K8avvxjUBoSkYgj-TfDivY71zdhaUoCqFNTlLrpg_H9eaEl1velwKwmC8rm4x3TMZwJFpZUbb53VmbfxVfwcnZaNWqHs_zTOLD8UkO8jwTeJYAV8e2fuyi2FTZK92OVVvollA2BDhMI3T1-beQNQ_yM_pOHGg9LK59eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb85359332.mp4?token=Sm8r-t4XMePq1h6HDoatY8wG-fIfrEVsJ2pYmZ3bPpkMMj_7GKgG6ABlD5KFaFFbr578_c03ZRVdQASNKXz5MaeuQ95b3UNdo29-8NQZ1TuSg7NiHzOgnk7OErz-I6hZ1zQ5aMNpixRH_NW2icKFfaDE8yQEDDVVQuhFCydJm_-6kgSof5K8avvxjUBoSkYgj-TfDivY71zdhaUoCqFNTlLrpg_H9eaEl1velwKwmC8rm4x3TMZwJFpZUbb53VmbfxVfwcnZaNWqHs_zTOLD8UkO8jwTeJYAV8e2fuyi2FTZK92OVVvollA2BDhMI3T1-beQNQ_yM_pOHGg9LK59eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گور آمریکایی‌ها در خاک ایران آماده شده ...
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/676076" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRvGIMcNG3pIFq6gRfn73yRT4CRdgODWvYTPtHKFPthUXqfXNx370xuLDHP-lsFCogR77rZorGvScMq2BJo6l38bCCkoP2pbyWtE7bv1uSbNmPSI65xXijFdGslL_1OJeffY1aU0fkV1SdGYWJeSoHs3AfbTBCz2ag4McnnAqgIMqJkqKean7RMT8GDpUC4QmFqKVii5T13ro7uljbFHE1G8t-V44VviUCA7bAFspZWAIm74ePA2B86wn3-8my5CcyCPJq74tO8wfVXZl5h7qYsGE42oQ7D_Bo8b7cWsQNziWhMIO7xv3bO6Wrdbb9Fpgxx25PZt3EUgiR474hL1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
۱۰ گرم طلا، برای ۱۰ نفر!
🎁
تا ۹ مرداد با اولین خرید آنلاین طلا یا نقره آب‌شده از اسنپ‌سرمایه، هم سرمایه‌گذاری رو شروع کن و شانس برنده شدن ۱۰ گرم طلا رو داشته باش.
🤩
💛
✅
پشتوانه‌ِی امن و مطمئن
✅
نقدشوندگی راحت و سریع
✅
خرید و فروش ۲۴ساعته
✅
سرمایه‌گذاری حتی با ۱۰۰ هزار تومن
⏳
فقط تا ۹ مرداد فرصت داری
همین حالا شروع کن:
💰
👇
https://l.snpy.ir/50svu
https://l.snpy.ir/50svu
https://l.snpy.ir/50svu</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/676074" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtFpX-eyIWjvPI5qv1dQblnRHAAobFw7xKhQNpijezN050eAKGsyDT3EAZxpqVcftXq_ugoIGXChfoaVXnT01zTHN8KYtm_TvpLTPNhhLnwlt6TBOqB86QOZLDGmC5KYTLNNMCC-78ZmMmlRf24BbeGHVfWXPw0XynGbXShCrnVqrdZdWqATvl5Dzv2ohrKBMVJ9OHBaH1kLIRm_TKbIXxjJYa1vsgux9sjoYmgsa75VNuDpCcOLFwmi4g5UNpQJYNbN5y1yOFx5WAI65C4CFCB11SJovP66-4PZ8sPcltovgRnUkqFwiCrdl3SyskeArkdnRFLN-Is5kA22CAI0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5PQP5BYyy_0bX6K50Xb7rhLU0GBUJlWIxYSqbi0hKyON0yZPmPXTpswXIE-Ub-ruISR7Es-R-a948jmarLd7T1pE-1B5ngGpTRKMYbT2gKNbqKUm3BguR6cfEcyE-Gx16SNDMmBRSIeWEgJbIG5P5W2snIwT99P59YHY2uhL3wx2sM-4RKh93RkbimKKoww9S9J3hn3kJAI0Ruu4VqwchblkW8a1-IiIq8s1XsS4jPZIua57SkyksW5_0VhjzySARo77yzvJjFV_vl6a__c5LQhlIu41BY_VYpm28vM5aK1O6w1oGDGO2mZsFpFYNOjYDoPU63t0uWfyZujSmfaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hv6YsitITJbSaKUyCgHWfBSEkUFt37eM5HleJ0FE98nsA0Sg0asjJYoYzCmFV1ghsSil0B-tt2xf6-dM_jDj0JsBda6gmpGXwo1pl-bwmTIQdD8uy7x5v3Y7ZRrOF86f01XGZZ6d5uKDU_jyhNvNaY6IFs9FX-diDd8IRLmbfNSaZ8DDGhZbbVjemNwJShIR_zzwgIC4Zp1pRVocUQQobVpueKEqs3bgX9icXDYt0bJZA8ywZT-TdGvHTsE167iUUeqXVAl44T0F-HWNmTrVlGH7wayENd88YamoJ7klermFupYRgCNEH4Is1s5T34012TvFshHKTUXWAvau6yvZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amqcK62uQRJBPZxhn85aVRoLx8DtmEqzSawg0TrMBP91wdstE6sFZS79Me7KwMI3HBHGtolwhfBRC3YbXt8ZgnptU7eDP9y0J4-tccKZLFU9C4MpnvLeS0b53TAF-Cna-ohMDSlCF4AVfndlicslw8ucnGc1vPv2T7SpmWtXN6eMDoc3A-FUZa_pebF7AVoTMyeITYmfRg7I44FNaFfK_4wEhCvGndBfuopdztNVYfH-4llN-enNci5dEi2iG3WgVFoIY0kUfoF5uxxC5K0bXks6PGU9kz9nHgSgPsgsLWv3qtEN6qMV_IhytKHv06WwBW-iuruqBOz9CcrpcidXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aw_d_VUgE4KxKIkHXb2UtagrqX_MtHroWFoDDPHcsuA8OqtqlzYYumbmc-A5DTfQhDo3F91p2nNoBPpz5mJHQgEgTn5V-DDzO4_ia9fpSEX_7Sh1X0V7zYjGLHDS_RO_d9YOn9ctgBlub-f55Wbeol6kfQCgvcTxHMGxvJrGt2ur0mFUaIhMIkrMi7IgQ91JfkXVHBPGL5a3txWtSoFKHoAwDTCqEuTLe7tlbmLWd9ZjNOYa-yc6BlBUvfYJ7HnIsZ8izjdUHXUjrzXM-hS8l59MW_RhR1A55B2FVWbFZXWqvn66bPH1HRhIbobnQ1gFmi-hOomcOjVxbpaSl2Sk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKcPcuq0AIOxjAorsu4jh3M_sC5x5QaoaX8xJnrIJho9VVls8-RsmNchOYiRLL3mvg0kP44i7J7TTun5Uae_-zwc2WpxuOkIWxYSjCZGiMU3GXI5X1cE35r072Vi6JzKDjOY22RWamcTlV9lhOwEBEGHyqj0vdQgilLEMnpJ-uGjJoevgJdH8t5H3p7r9REj2GPhZalrz7LIBoUA4IQ99WGeWLNcwOFU1ABg7LllL9Tx79rVRY93utFdDbQeSIXtlDOq4CH76Hm67EIb94N_wlROf7SZcywhlvCSjau51dEMTWRegqdit0fHFoqHrMVsDxX-gxxhV9vkAEPtmyZ4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGBe9Dz_l_W6jZtqaCDz2gqqAZUGHfR_iGzzI5CKOOqa-1qdiWpiE3jTR1D9kx2oIYMqeKM7Vc0d17CKgnNBpRHGwhkoMRsiGeNYQyH9kT3wiyGsNLyjcHZNNDb0e93c-la_gUA2G_-es_o8hhL36aFJAWhGrv69X7NRccprnYS3Lx99iGfsMBtZZAXbeu1-Au8612hL4YENMjPeUqa2lk5ewd4QIxaOywKAK9ZzgjNZS-3IDX4mF6Y7Iw8YQoKKVAJPhJvlUHVs-QjqLUg8lEF7iYqy_DegjiKIy1Gtj6GT6EgBT3vJk4WyZPbKMOS8r6v3chiiT-Y-Ez5P8tDl-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pb-BQ42nKPwlKkUl-sSBSnrbk3uLX-lz_6YG1cRj7v9-NoCGTqKuvHo4uAIl9ghqhjKL8TJsVH4WBITK-Q3m0ZnXJCZzZ4issSW0384JXaczc5nA6j2NM_lgPYMxLkWk23PLVPaSNcNK1GpkgvrBrTWJyYfqU83V1UgodcO-9Vs_sxsrEQFczIttheu7BXsaCWut9usl5f-mDJu0UugU4bK1PqdqtYiio9D58u17PTSblp4IHSoRG7dpf7hT3WJDfIP1_lEvo8M2y0Dc6vMOwPuRz4_MkEM6TrnpRqas4nOQn8H8S7k7hUyu8vGASDdZ73DaIgBOZb9lrmwFNLWtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMzS1m7F00Q0NMxMskYXpp1OVdo8hqJo1sRTu7jvJA8kby9myq5M_LyxUyQHsDUczasp7M7uKig1aydSJ6MEa8kpP9HGp_kZJzlgKBUmyWmw589pO7v0GN-6yIoL6knN2zTvvtE1GIVfcEcI_Zi9fyio757E0N-E9QCgeWJf5r1OWS-n_AU6-Yh95qFjsdipwm8zH36S8F-BlM70ca5Iex_V-6hmccNNbe_Z6aay-ECh1gCZfJCIsxroVVHNp-TnHskgAou2pKgo5Avjru6ndE33CxX0FjaR7WUbMTmQp4eh22Pa3jG9K0hJmIsrh9-SC8laijjkiBhM_dqZz7AWuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۹ عادت ساده که حافظه‌تان را چند برابر قوی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/676065" target="_blank">📅 16:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfdreEfGesCeQBuctxkydTyQsxX1JbA81wdGPxBhdwaZ3xEBYnH354SkFdGVNytGYfuLqbtpUHf0CYrZMMMjNIZcd3jgb0MraZAYPlI_PKpqLt38o6LctRbHEe9xAwP93qppb3KUAHm_k-AHMIlPpRx2GhSGerghoVuc9THLYAn2PiX2wCEVFMfzpavhbvbZWZQhzTuMjlTnWwsoDPK06pOPioaFIrC8IBk_qGBMsAzVCRJc6g5po3efjZRsoFrd8FwoEz29mToMEBk269LaXrfe0cRaAaB34DXmlE2p4LejihfLk-rZ5W_fuJU4cOYV8aDEUjvoi6DmNeu7TnpqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTBMIO3UBgCEourJek5lV06IkRVkQTF7-Att3MS9q84GVHs6CWmG2fG3qhDn_TNXFhFtexYqDhRRX_xZskzs2lcGP1IOmeLwUN0LkPqKnTZ_YzkWrBd5SUcK0Wn-7tW8eR8JNKU5-w4tjCnzj39aXEvJ5LbZo3gvHIwycmFBbSMB5YSKh2Kp6Vla9EKSddUC-SeGqNwOqQMO8PpuLRrDoXRUu0C8b7k-MvJib3hdrYFM_Xgv1ZaNdoTk7nwoTQ0zpNdBsnrmYBvaphzsTtypzTUaLbds1ZU8N6RTtHz5SP-vS1pq7uIW3lxcxn4MT8b-S8SWDR05OaPJ4PYOR3lmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrtzyTxwMahU9Kqje7cjnChz1IPyQrUYQaECbYfrpcsWM2v0Ipvuuyl8XsDP5P92GHNeQjT0kb_Q8BbXLt7W-9nWB_MPB_8Ub4Hrdt2juuc3fjhYnXR7VPzdQFeuO73HgLE9OdeCvg8Pe4Lw9In2dTCYX_5NSm3nHcgtBfGfRaEogCIR_cuvmJQ76Y4UD60yD_-a0Jy4ls2t4KXK3LYVo-ad4k_KHjQTBH3VBEfld9UEUFDDrW85lqul39xhS0ziTEbmNpMJ4UUGUCTkFL_3p0ZKygaTcoZXjcVVNzW58lHuKO4iBTb_3HsUx9Vcn8ZBx3KngC0CjwxjLsFoCrNwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0UQtNzYqv0Z-gf0Q0PEt4uTGkW0D_xreSXXp5AFxT2-C-3G56sE5uRtdxFelh0MLuWXZMzY57vqv63n7YpuwH0pjADiwcx8X1DZngJkPFCpmN0vFbz_CJJN-Rqqh6tLf_3wKRlwdfO1Jfi4Y4g5446o0QJ9e8lLRDIOoo0-LskOpFqyQCtu9NqKvVfY9nN4f-b7VI2aMJmZRk6bDInXOMXi0zhGuT85awFeiSqMcx08nOxLQ1VAgMWeJrCaJFxwkeAUI7p3AlCdclltx-eeJpqSSs1tWwzxVZFivltO2aqKUXEJo1aTzUsmhEEdmOxHP-65U5HDFgXvKdZd31EBtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فکر چگونه ایجاد میشود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/676060" target="_blank">📅 16:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✨
تخفیف  ۵۵٪ ویژه هتل مشهد
در گروه هتل‌های لوکس درویشی
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
مجموعه آبی و گیم‌کلاب رایگان
💆‍♂️
ماساژ رایگان اتاق VIP
🚕
ترانسفر 24H فرودگاه و حرم رایگان
⏳
فقط تا ۱۵ مرداد این شرایط باقیست ، همین حالا تماس بگیرید
📞
05138080
‏
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/676059" target="_blank">📅 16:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نخست‌وزیر عراق وارد ترکیه شد.
🔹
نرخ تورم در ۱۲ ماه منتهی به تیرماه ۱۴۰۵ نسبت‌ به ۱۲ ماه منتهی به تیرماه ۱۴۰۴ معادل ۶۱/۴ درصد است.
🔹
پیش‌فروش بلیت‌ قطارهای مسافری نیمه دوم مرداد از فردا آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/676058" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=OrVGj_Z2jSDfX2MPyB9BGWB5y_2ryTCuuGP4jBMAk_ik0HYsp4aOnVW2MbgJuAPHJGnNHPunwF_tNdQnHLoYTuAwwMTldlQsp0Ma6RxA6Sl2B2pP6zKQVPoy-f-xPuYLXBxkLy_88AC3nwEBRu6Otv8Ax7PbAkr2OOWrU7WLkoN_sBAOS8XPOhp_kU2_pevreP1qcwA2zCqzJfi6RfmFkRUwXwXekVloJGUiYDdgeScVkLysYkrlxz314YhL64mBGIrK5xu_iCRe-PbFFsCQXBPek7xGuSS37oTtrmB4Ze6VqObajgXgOroFYRUl1EMkR2Nlly1iLEYK0YOvDhWC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=OrVGj_Z2jSDfX2MPyB9BGWB5y_2ryTCuuGP4jBMAk_ik0HYsp4aOnVW2MbgJuAPHJGnNHPunwF_tNdQnHLoYTuAwwMTldlQsp0Ma6RxA6Sl2B2pP6zKQVPoy-f-xPuYLXBxkLy_88AC3nwEBRu6Otv8Ax7PbAkr2OOWrU7WLkoN_sBAOS8XPOhp_kU2_pevreP1qcwA2zCqzJfi6RfmFkRUwXwXekVloJGUiYDdgeScVkLysYkrlxz314YhL64mBGIrK5xu_iCRe-PbFFsCQXBPek7xGuSS37oTtrmB4Ze6VqObajgXgOroFYRUl1EMkR2Nlly1iLEYK0YOvDhWC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم الانبیا: هر شرکت و کشوری که از محل دارایی های ایران مبلغی دریافت کند اجازه عبور از تنگه را نخواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/676057" target="_blank">📅 16:28 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
