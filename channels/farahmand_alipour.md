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
<img src="https://cdn4.telesco.pe/file/SepMfHyKSsnNNn-DqhS8P0aZbrxIyHWlV_CKhy3EflRsZIj76jcbAqwEPqnGLrAdBV_aYpOChwTMU_5k-z0z559iFKLpS1A3R8Plwu2l8L4wfFIQWJSkT_RTzrCj9v4EeNT_LdPINkZAmlD8z1-YgMXX34RqPJ4CRQ7IkpYDon4fmP-JqGeiJAoBSyjMsiUj2fIPwVQax68BMc5zT_EE_S8xt3M29N-taDtmxZyoytntb0IiEBX3IxGdJYKzGJunc8DQUgOGqCLvxxy19gvNRRSCI9J-wec8FGCaUzp-buFX98SKdXUGhq1-XLaDaJjuijisJddIGLpb7NOJevHy6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=WSXWH4OrIOevXv0ir4ZQ-CPWs6VIbU1yq_L02b3nRA-kVA4uJFCp9nCknhvgb3-94gAcqbqvnYUduKaLNVwIb2a5bGe7sIipZL1Vnp5NL8kDeQXPzhzFvLEWMYDJXtmhrHwLT6ItggGIALFrBNzJVpGkx02YrEZQYmGorSR4xB-G9K67GXMwp0BqTLsFhby0wOzPmlK-jtQsr9rHXB45zZ3v61c4I3xrb5aTLTYjURTv4u6ETa-fyooZwnNAugOM0YsFJH1mTTZpI8j7eZHlEKlODfwCDdw4H2Df4vj9hKVWVLaE7jgJzErDoMffYaBPQT58ybnyzUZXrptod8fHgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=WSXWH4OrIOevXv0ir4ZQ-CPWs6VIbU1yq_L02b3nRA-kVA4uJFCp9nCknhvgb3-94gAcqbqvnYUduKaLNVwIb2a5bGe7sIipZL1Vnp5NL8kDeQXPzhzFvLEWMYDJXtmhrHwLT6ItggGIALFrBNzJVpGkx02YrEZQYmGorSR4xB-G9K67GXMwp0BqTLsFhby0wOzPmlK-jtQsr9rHXB45zZ3v61c4I3xrb5aTLTYjURTv4u6ETa-fyooZwnNAugOM0YsFJH1mTTZpI8j7eZHlEKlODfwCDdw4H2Df4vj9hKVWVLaE7jgJzErDoMffYaBPQT58ybnyzUZXrptod8fHgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc-xv30h4RzEXN-kemBCnM_lTiz7OrVmECVyTAJZYrENACKbFlws6BpIZwkMcdqImWB2oLOUd5kvZ1k4kf_A8yx3AF0owcG1gyldXAwTb6Gb7g8inKintNZFzY7nRdo54qgBSR4aSPCvU12z4Ga7-fOMasgMA8Egtx0hEjPxF1Tjhb66DItayItxyv6i6mHszZP4RhGORZ42kAcrR023UROBZDXeyQz-fhPzTXCtFsCZEDxcc16Mkf2aGiY7Q9uK7ECIldXt2OQVQARRuJiV_zx-64Y2lqN9U0HBgz4RfopNBLfat46HwYj0KwxSiDE3et9IO9K3IsMqGjGUhT8tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DBSXdQvPCVJZO5mdmX84V8gV22pQqu-ija5g-z4X2nxRvyyT8z3XQQAf-yEf4Kd2kXHPCtecUcOLepXZRZPHNE2ro3IxQx1vgZykYwV2DLp1Td7isWFKreJ_OR7oEdXun6-BSEbGHwgDsTk1JIMLwK4s0mzOnypxI9Oqpt1ri8dwpJuEGWQuuCncdcmf1I2Hve2fFaDctzSg_qK3FZLWylNAZRwkyVZ2qxY2PvSCeaIU7NrYUn7R3sjuu3fgv5ysOrtD7FpeJpj-Hk5Xs1aAVnx5TeCpCd3jAWwBJ8qzWlRJnmgU6nHl3I61skVkzdq4_WuU7KLrFHBozPvV1Q7C4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DBSXdQvPCVJZO5mdmX84V8gV22pQqu-ija5g-z4X2nxRvyyT8z3XQQAf-yEf4Kd2kXHPCtecUcOLepXZRZPHNE2ro3IxQx1vgZykYwV2DLp1Td7isWFKreJ_OR7oEdXun6-BSEbGHwgDsTk1JIMLwK4s0mzOnypxI9Oqpt1ri8dwpJuEGWQuuCncdcmf1I2Hve2fFaDctzSg_qK3FZLWylNAZRwkyVZ2qxY2PvSCeaIU7NrYUn7R3sjuu3fgv5ysOrtD7FpeJpj-Hk5Xs1aAVnx5TeCpCd3jAWwBJ8qzWlRJnmgU6nHl3I61skVkzdq4_WuU7KLrFHBozPvV1Q7C4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=u2_TAJDOZe73SJ4oLzE51p-QMNaeVNWKcG0FyGYutoatsm2M2iWK5cDy1-9Sqf_hXuqR0HKmdudnue1Yp5Odr3Fj9QUkzjG_XDWrYrGNHypa2SRjYD6w6rdS5Ty_rqI4sSf8DVI5qOqgdOgZCUU_ol7MREqai2QDcx-r2oDBgxl5q9N7sTBa-Qm-tiJiQ-yQ7gH-DDfFidcmcFjj89AkBVV0z8zgbNhWnPfqAdBrWQsGuibX-zWbYo-ZYdUKmti3tHvIolh7mTGTHZAGUo1GZYVMpk-qZW8oeObvIdf2imm5ITYeRxqmC6pzBNl0h2iTVwZR17tOE83LdzXHFEz3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=u2_TAJDOZe73SJ4oLzE51p-QMNaeVNWKcG0FyGYutoatsm2M2iWK5cDy1-9Sqf_hXuqR0HKmdudnue1Yp5Odr3Fj9QUkzjG_XDWrYrGNHypa2SRjYD6w6rdS5Ty_rqI4sSf8DVI5qOqgdOgZCUU_ol7MREqai2QDcx-r2oDBgxl5q9N7sTBa-Qm-tiJiQ-yQ7gH-DDfFidcmcFjj89AkBVV0z8zgbNhWnPfqAdBrWQsGuibX-zWbYo-ZYdUKmti3tHvIolh7mTGTHZAGUo1GZYVMpk-qZW8oeObvIdf2imm5ITYeRxqmC6pzBNl0h2iTVwZR17tOE83LdzXHFEz3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrMq9Wzesq4_4qIkok0LNTAIB14CQSEIakyKX21gkiy6QjZabNqYmzz6EIYXEgVCzWSQ8i5gpnW6ttH98nPNBUNBgQChSJjPzrhx6TXqWxmPt1cEh9BlqIePYj5Hf1_vAlo-D7T0tuRgp5OxkHKi6Rc0IKl_gbnE4XOzHDyqskGJtOu3LNnwcP0MCBdNp4e2BoHVcWodBS5jOI_pOAwce-lvYG9NU5KivSYnZoizgHdfGgGf49ediMcszAmMT1snuVzRtn3w5W8F1plyjZcJgRs6q5SxOyXZKV8rwvE05KtdGrI9Be4cRL77BtfqRV34BhjixmtFO25_XCCth9WUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=l2jQvmbDJBQlNa1OwpLS5cU_bJUxNbHO4Iv535ylGb8pJyM1TTdMn1tArP8y70CVXPLGHhr8Qa5rsbforvn2h5UMEqUBswK033ez4ZCJUWp3jBmQqbEWvcQj5OnAr809fmqAuesvD8Ao9WwHjp1j9QRRV15INQTlEQjKWeMHmeZ_KcUJcaK4O5wTgujU8b9jx-Irn7-DacBzA4PXnYecV7_RSe5853BZR-x6esz_dnXWfI0q8UPApCuKXI0QmiPuZeqy5ChdopKCM5tyDif9F6n5jqrBo0A5t4J7rwPAmxPtkBBwFkIcpQzd2Npyqr3t5q1O3sMkYmSqfnu-EbjRyl8BbFOObA5rw1tCNCJbdWZxmz6lnnQ_YR0hlyEByg58BxMHvh8wu0iab10m8PH32lOoBS7R9Sp9xByfYu9DCZXMn60GacrdwHBCDm5lJz2d_Zf-CMubfM73jp-cbUpOcjeDSmmDqt9zAkLp9tRae0WP-q5OhtG0iU3wD7N8KXLuSQ4H9JkOfp5GsCkv1mdwita-9-PZLh07nC5DgAFrwOGrtUsP7oPRBu0LWJPUcmPDwPkaqSJDyb1E1L-8CIVvagM5OYHbCYJC5qoztNj-0GIx_ztvzPiAwh-RWcn30ScDdnC9W5iwqwkgrBxT1-_ioQfFVPUBSIUiU3c7TjhhSTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=l2jQvmbDJBQlNa1OwpLS5cU_bJUxNbHO4Iv535ylGb8pJyM1TTdMn1tArP8y70CVXPLGHhr8Qa5rsbforvn2h5UMEqUBswK033ez4ZCJUWp3jBmQqbEWvcQj5OnAr809fmqAuesvD8Ao9WwHjp1j9QRRV15INQTlEQjKWeMHmeZ_KcUJcaK4O5wTgujU8b9jx-Irn7-DacBzA4PXnYecV7_RSe5853BZR-x6esz_dnXWfI0q8UPApCuKXI0QmiPuZeqy5ChdopKCM5tyDif9F6n5jqrBo0A5t4J7rwPAmxPtkBBwFkIcpQzd2Npyqr3t5q1O3sMkYmSqfnu-EbjRyl8BbFOObA5rw1tCNCJbdWZxmz6lnnQ_YR0hlyEByg58BxMHvh8wu0iab10m8PH32lOoBS7R9Sp9xByfYu9DCZXMn60GacrdwHBCDm5lJz2d_Zf-CMubfM73jp-cbUpOcjeDSmmDqt9zAkLp9tRae0WP-q5OhtG0iU3wD7N8KXLuSQ4H9JkOfp5GsCkv1mdwita-9-PZLh07nC5DgAFrwOGrtUsP7oPRBu0LWJPUcmPDwPkaqSJDyb1E1L-8CIVvagM5OYHbCYJC5qoztNj-0GIx_ztvzPiAwh-RWcn30ScDdnC9W5iwqwkgrBxT1-_ioQfFVPUBSIUiU3c7TjhhSTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U03Tyxz-YyX7NipnIJK3_RyYk9UB1F2ju1L8vWjUHq5tzsL_2XI-QLTsHKu2e5paIMBqZCot0l6-ZevVWumrPY0aqoAoL3T9KvN_I__eUWwjbh6aa68Lp7WGXmdX_eZoq_Jla419Hh7zLBZOe6h2h2KbkAsdRyxQ5WhAHKP5100Fu9es6ufcyu3oeIP0YqM_ENfryLHlMwIlmhvP35pO7FmVHhTSLlxR-Nmr0cctn6SabcxGjLww8pAQW4s0I04D-zAgBiNH5LMPNvM2vlToAbRjG4BU7cGNhUmPqjqRZ7nf5GXVQzcfz9U40PLCO-vDFZeUKGzkHUUXUjaNodq_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=KlmCR4DBDyHqws_AdCli2bhNqi-cB7zcQIETnYdXyQOONbC78_kQhH0__WKK2VwW36Ar8Y88exWXWoxJcwNMuXAzcPQNBux1U6OJ0QRzU9mymjW5U40DlItvxIOnoomkQFiVVaC4ha6yT1ARL_Loj-kn1g_v6K0tDF3CuDrRI3JlCr0pnHNyK7ovHsyrw_z9D92i20HgR0MOuLj5VtB8qfhCkeEzadSzqWYWLnmXbSOREgz3u8G3vd7Pp8Vafj5xCVhjthRszYn_mi8GtPp5P9ZqFP8-M-uGv9VHM_WJGgCTJZOHeNpwBztb5mtubpw9f1adVRf9qlBQH-_YjbKUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=KlmCR4DBDyHqws_AdCli2bhNqi-cB7zcQIETnYdXyQOONbC78_kQhH0__WKK2VwW36Ar8Y88exWXWoxJcwNMuXAzcPQNBux1U6OJ0QRzU9mymjW5U40DlItvxIOnoomkQFiVVaC4ha6yT1ARL_Loj-kn1g_v6K0tDF3CuDrRI3JlCr0pnHNyK7ovHsyrw_z9D92i20HgR0MOuLj5VtB8qfhCkeEzadSzqWYWLnmXbSOREgz3u8G3vd7Pp8Vafj5xCVhjthRszYn_mi8GtPp5P9ZqFP8-M-uGv9VHM_WJGgCTJZOHeNpwBztb5mtubpw9f1adVRf9qlBQH-_YjbKUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ktOz-ivEjARKzIhjEikGyQgqsgEyCdW3InRpcux68fv85nCkUVy3yg7hhlrfAsbG_YSxx6FTsxwqsibwLdCnFyzFPM06NroqKyarkC4wffrRoP-TfaLqrGU2pwAnuZJPeu6xWifuREXungP6D8SSv2id0Sc55ipM7urrNT_y30EN_ycf3Qmuq24Ov3V9xKXXWnsuzM_xXcCVgHBXAFiUTIGafKOrXh26j_DIgRvsvzFMEz-drCaJoLxPxn3jzogaNNuZVLbcD-sljrbfa8Cf8h87TAqFr4raGX0r038PDVqwXr4SDdtP-nEmQPXQDdokO0fU1cAztFav4Q-SaZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJllLWqGcfN7Cq1cBHIoVVC8-HFT4o0dQEABs_V_LDKdEWjve0OjyWc603JbH4fyuoFSmh_Ieiy7Pe5ZlwfgD5d9INQpOxAryvAcAA2uAt3QWnw365JnejRgdj7ync2_eXT35Fh1sdwwH6jaPvvj47jouLA_hRNoAZVB85pKvhGKXaCb5TKJxhFYJHFvMSGb77jmD_-RuUDVh_hh-tNCzEypgrR2K-nb0KO8fzqQmR1XYCuH1V7Mhb2T7LpD_BOGW8TBvecVRHMn01hbYBoh8yR1ZcsqQdhwh-YYyIHTxXIExd6aMuAzx8EsH3WQgfzZTIe5X_VSTKbSeKSxejqWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRen3YIZczMjoZKUMZfD0VYilxG_2jkAL9hsevgRE5soBwEn14A-rdwS4g7EVMhlUxMWsH-PS4ppvaI3c0xDEBoyeR-NDX-YSUvs5zDs1SZSqQts7xXckNZyl5SBAyn55Tas_hrpnVBIVpLD9F5nBT7uwREa11cezX8Yc-4vo_BxM7WEObCgy0Qay7VSXU6TiuQK9-ylvFkbdEzvO61h6p19xrQWgODiRoRxupUmdBwBfqOrB2Enci7C4e81e7nE_h1_rzswg5KVnstN391vBvS40r5eLIcXR8Ag2k4owluAa5yHX2whvQaBId8Roa-nDwI2TxZbLtGNh2ko08dqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=pLxeaz7oI2uE-5lo8e2x3iGapfVcX3Tjy9dJ0_LNmaZ4Xn85cnzucs9Avvwv1pBYDvj6BPbzxzwozhQ6UYaUKnHimqI-0-rth7OWm5V213aON6v3yo_6hbQiG1yBx8xXMBDn08hOei8QNDefhzzJpPXMjfIGT-5YKF_QtcrLE8u146nLI2Xith1yjZ_hzeM-zG8OD6JAHLN9Dt6Ma1FmUHveUGg8b_3ddo7Hbp5aoB9ytzH55mGmmZvsXYrfC4onOh-AyfM70IeH7_WAc5tX6Tbqb9QGDkGHwojwDbkliF7xkUR6sg5YV6R2iUZVxFflYkwaXcINJBRUUjVo-035zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=pLxeaz7oI2uE-5lo8e2x3iGapfVcX3Tjy9dJ0_LNmaZ4Xn85cnzucs9Avvwv1pBYDvj6BPbzxzwozhQ6UYaUKnHimqI-0-rth7OWm5V213aON6v3yo_6hbQiG1yBx8xXMBDn08hOei8QNDefhzzJpPXMjfIGT-5YKF_QtcrLE8u146nLI2Xith1yjZ_hzeM-zG8OD6JAHLN9Dt6Ma1FmUHveUGg8b_3ddo7Hbp5aoB9ytzH55mGmmZvsXYrfC4onOh-AyfM70IeH7_WAc5tX6Tbqb9QGDkGHwojwDbkliF7xkUR6sg5YV6R2iUZVxFflYkwaXcINJBRUUjVo-035zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8Vow2FjnUqk1KK7Y09RtNGlHvYhkTHKyIsujeGN8pngecR9nRSBLHakrkJjmP_tUWYFplSicxf71LMnHfXYJMoE-FLPiG9m31JlDX7pepgQ-g0_HvqQ_-T4tM0nWqkRPEbHuRx_mhz68wJy27YQmKA7CEmoBqT3K_Kfr1N-eyftNClWCwcna7QpXnomeV23eh_73JQA7wiErOJlz4wM8gxXmC-0FfaH5vjST99QzRuejsrs4sTEIRRMsv9srRLcUd2-3f8UJH3d14LSYVF1dP6Rg6VevBxLJlk7z5GeoWvae7n1kjAS88AJQ__m3YSz2YmRWVuJ7q6zLWn7mtbAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2Ig1O0t1ISVkkbLCKqsB6lTE7uiqptktOdY13j7jkSvuNcDslO5Ad03jDxaW3guFGaZ1QLI_a4XTA9w6tLKI1iOcKYWs6bHqvQCX1mWhhkYntDPq-xltYzul91uhu2VmIuy1UI22HKoy8QKK_3odTbNShmaGgrvldRtFISJyjIYLWH0J2fQuaxhSRtwneJHBg51DfPWhudGp3UJuUtD1OEFqCxAz2AgP4OSlR78Vrt_hf2rSvNo37Veb6CAb4vEHF347WsH4BWQTppgkcCLkLnN-z5NUh8VxOF-orREhvU0weZL_5YNLRshL2TRZhUDjcAVgMHQ7hHCK2maVIBpnHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2Ig1O0t1ISVkkbLCKqsB6lTE7uiqptktOdY13j7jkSvuNcDslO5Ad03jDxaW3guFGaZ1QLI_a4XTA9w6tLKI1iOcKYWs6bHqvQCX1mWhhkYntDPq-xltYzul91uhu2VmIuy1UI22HKoy8QKK_3odTbNShmaGgrvldRtFISJyjIYLWH0J2fQuaxhSRtwneJHBg51DfPWhudGp3UJuUtD1OEFqCxAz2AgP4OSlR78Vrt_hf2rSvNo37Veb6CAb4vEHF347WsH4BWQTppgkcCLkLnN-z5NUh8VxOF-orREhvU0weZL_5YNLRshL2TRZhUDjcAVgMHQ7hHCK2maVIBpnHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6o5hNVxv16PXfsJ97SxVnL9HOk0m17X3q8xEaOQ7kFwZig6eM7L_95t3xMWG_L3AdtTmrLA3IqTEdmxUlueMPpgLyh8NobOqb5zf-zZWAioDwcz8otYxvFO0PEef8PZBCVDqH8GnWy2kpGSeXWtfi6KHUr2NW6BjDWm0OVK-cKq1kyZ1bovMwMFFrHRcXWsBjBGpCiA3A5aOb14LKyocGToNTgK6ZU5vM4nlKfOjdvXIF3GjRc35ypu9keTo5fAoqdzPCn_-suPCJNdMxkvJE56A7v238-QdzqMaGPV2dYOsq8Z6xZjhDFtahzcvDxG9oq5sK1_6UccH6-YHS2k-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6o5hNVxv16PXfsJ97SxVnL9HOk0m17X3q8xEaOQ7kFwZig6eM7L_95t3xMWG_L3AdtTmrLA3IqTEdmxUlueMPpgLyh8NobOqb5zf-zZWAioDwcz8otYxvFO0PEef8PZBCVDqH8GnWy2kpGSeXWtfi6KHUr2NW6BjDWm0OVK-cKq1kyZ1bovMwMFFrHRcXWsBjBGpCiA3A5aOb14LKyocGToNTgK6ZU5vM4nlKfOjdvXIF3GjRc35ypu9keTo5fAoqdzPCn_-suPCJNdMxkvJE56A7v238-QdzqMaGPV2dYOsq8Z6xZjhDFtahzcvDxG9oq5sK1_6UccH6-YHS2k-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=XqG6tp_ke9cdvkn204F848GrPn8patQku24fsSNzBAINoy-WGqjcOApi0B1vRaC9X7GyqfHG-dvxU1wzCB79eMUkjsiMwsAM0HlTwodzMYYS8btzA0z3HYlFK4uHvvdJj5gPy0JIuBrWchyq46UylwXM6xT0w45cDaClQWcI3-sg6HAkM1q_1b5XmAe9t5ehr-SWph11Lb6LEO5Q15I9Na8ghnrUm7j55YikmYFCZksMlQkTdISI7OSO80dQMYvWy8esbxNd-DGywRz2a6NSjC7gdZaMKWpJ63GeUyaanOe7H2UuaX6ttoyjWaqHOYqYWJLaj9P_YNPaXCLmqNJwDnM0tx3j-9FX3nJXkzGPGB5fu_DlppFHabbKZjrBGZY7AhKSiF-sPa9PMSeGXSGFmV3iQqiGC46YxgcF2n08pS0UoKHPaVqr3Q8r4QVVL2exSE_B_-PEIXaUFw3C5qd0JvIz9oxA4smYfgtQ2QBtcbgdyeoqzwX2AMhJZ8GYg2n_rn768TBLT4h35xG7jJ6_5feV3bc0KUr7qt3TLoLBtEYZaQf1eF38qAlIj95GMTS21tKoOi1niGHk_IR9-UEB4eRd1L9J5P0Rzg5lWveeTphBHbTPLKzbgXg20EbiysmjFoh52aE7f3Jq78jOe-r-Qt_tzH85d-dkM6Zym91T9l8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=XqG6tp_ke9cdvkn204F848GrPn8patQku24fsSNzBAINoy-WGqjcOApi0B1vRaC9X7GyqfHG-dvxU1wzCB79eMUkjsiMwsAM0HlTwodzMYYS8btzA0z3HYlFK4uHvvdJj5gPy0JIuBrWchyq46UylwXM6xT0w45cDaClQWcI3-sg6HAkM1q_1b5XmAe9t5ehr-SWph11Lb6LEO5Q15I9Na8ghnrUm7j55YikmYFCZksMlQkTdISI7OSO80dQMYvWy8esbxNd-DGywRz2a6NSjC7gdZaMKWpJ63GeUyaanOe7H2UuaX6ttoyjWaqHOYqYWJLaj9P_YNPaXCLmqNJwDnM0tx3j-9FX3nJXkzGPGB5fu_DlppFHabbKZjrBGZY7AhKSiF-sPa9PMSeGXSGFmV3iQqiGC46YxgcF2n08pS0UoKHPaVqr3Q8r4QVVL2exSE_B_-PEIXaUFw3C5qd0JvIz9oxA4smYfgtQ2QBtcbgdyeoqzwX2AMhJZ8GYg2n_rn768TBLT4h35xG7jJ6_5feV3bc0KUr7qt3TLoLBtEYZaQf1eF38qAlIj95GMTS21tKoOi1niGHk_IR9-UEB4eRd1L9J5P0Rzg5lWveeTphBHbTPLKzbgXg20EbiysmjFoh52aE7f3Jq78jOe-r-Qt_tzH85d-dkM6Zym91T9l8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=j_kcO8WYkHagtzLOBgY5QZmw3aXqC2MHgXHZ4ZctJfeDnx6kV5JzYjyz3rf_ozEDk7an-8VNhsXyD8ZiERSQzTwINLVI7Iodce1ilDXaC89AVlvAHd-7LTvjzgujwTul8cMG5TQEUGQllRbYZEJ6INMzM2W_Ci8z69DILMLXgwAct1Ak3ovRuqjk5NlxFi1v5Yn6_9Xr7rIZxBofc_yOVRxFYiLd_JXLXoTFFueJNdxZQ6Mzwc7MvSB-uw8tyrzCLam5Ul4-QGJrmiJGiUV3QWX_TIn7l1TVBtKee-6TrvNUxYoiWb6ScBi0zRTkX3g86wCPuHQrbhYvAh9DZTQxhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=j_kcO8WYkHagtzLOBgY5QZmw3aXqC2MHgXHZ4ZctJfeDnx6kV5JzYjyz3rf_ozEDk7an-8VNhsXyD8ZiERSQzTwINLVI7Iodce1ilDXaC89AVlvAHd-7LTvjzgujwTul8cMG5TQEUGQllRbYZEJ6INMzM2W_Ci8z69DILMLXgwAct1Ak3ovRuqjk5NlxFi1v5Yn6_9Xr7rIZxBofc_yOVRxFYiLd_JXLXoTFFueJNdxZQ6Mzwc7MvSB-uw8tyrzCLam5Ul4-QGJrmiJGiUV3QWX_TIn7l1TVBtKee-6TrvNUxYoiWb6ScBi0zRTkX3g86wCPuHQrbhYvAh9DZTQxhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afvz7cAF48R3Xg93oVE35ngUnssii5V3g30EmIVT-JiudTlWUfruhVvedsc4LHMz14FlJInuBV_DVZIHjkWlsHNsYV-i7bSmbiX9iOaXRKea2ytOE908I0HtfVm7zG0XMvmgUMMUbz2-Cag7B59LuJhW58Xm7HqhRJF8yqf1MURsmondou43q66L1D0gdvSDQZwkFa-cmB11WRjdEA2Ew-boPRS4jjVRf36thX_fQKaDq0AM50Hma7u84AAmQGrvkYiaLoGca4i8xTXzRu9KEUeXVoq35-9l_oVIBxJdBcwpNpXpUXnK7MLtHnRfbAmkYybfVvXwJnuaeonaoulzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=oXxBmZSYc9xmo3Nn9ITxrXpSoS-99TjsXuwYhFyFIlmNp1UwaGdIuATCzp_VI-fFSoURVoOxHhy6kMJyMWB4sisOYvDIFb7C4f3MbXVCVwE-hw2PDSn15mT8ctJt9Vkbsmsl1WJ9LRjl4Oo1YjLw-WEGLHNm5Xkut7kPzAWAOM5lZgxjQcCAa42bYvo9BIBTLjhsldyB7RdCCmL7SMhaJpomeHfh7aE7mJuumf4MCoq1o-oQlwC0gXW0w-7YxJYCgMJ7VrPJoePiLP-s7UBry5Phg8cPdjxIVtNVBZ8MyDl3xkgnZF9o-AYJKRyJb5wcDb5qoW2qXGrWueyL_nkQCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=oXxBmZSYc9xmo3Nn9ITxrXpSoS-99TjsXuwYhFyFIlmNp1UwaGdIuATCzp_VI-fFSoURVoOxHhy6kMJyMWB4sisOYvDIFb7C4f3MbXVCVwE-hw2PDSn15mT8ctJt9Vkbsmsl1WJ9LRjl4Oo1YjLw-WEGLHNm5Xkut7kPzAWAOM5lZgxjQcCAa42bYvo9BIBTLjhsldyB7RdCCmL7SMhaJpomeHfh7aE7mJuumf4MCoq1o-oQlwC0gXW0w-7YxJYCgMJ7VrPJoePiLP-s7UBry5Phg8cPdjxIVtNVBZ8MyDl3xkgnZF9o-AYJKRyJb5wcDb5qoW2qXGrWueyL_nkQCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=HmvSpNSEBnIqGERWXq6b3C21AqGVjU5hL6bA-AXXTdb0jgkTHRLYvTP-vHir-vzMLLMIZnEXYLUtIUhvRKWeVhwvPMHwn7fe3llB-K4aXHh7jFo62GHMXXaW7C6mUC1x8nGQNBKUiqipYBszYMd7h577i6mxoNDhkBwMWF_J7Eqbx-hBGKiM8M4td3TmZ8hRI3ugUzEkoykeKNBiBxb49ElrjqcppS-o3I_50xETJ23DdTNidOWYiG9srPj4LWkyJdBIkJyODCBwhs6PWZ6Irub3j1Ks3u1bxjpeXiJqDvZ-2pF53ZEbSz1n9hLLgI3mCabxG_UBX6YRbeWNinATjVadIeS-z7N5KvRbEh62C8ARkNXELzG_CxCbBpstw93HI94W1PYmpUEVmORFKa0gBOrV3F-CLfFBu_jnbddrBSwPF-3uilnGPToiIsYrgROO09WP8J4DrEbnq0vwCvuzgXPGW7l-1a275elf7YxSwY1WQtRbalg60pPHV-SG7M0mYp-JhiiMeUmASzjjll08JyvYVVeI_t1NMqthL0SEDXMNXU_wIj44dcWmrcsoA3xhpFckkG9psOxjlBZCFlUxTC1PXLCbalSb2go4UogLQnuR8pbYEUkbLL7rNSoZR8W9BJtqUY_kUyHJmGa8ZNNdc-6O-U2Dw2z-_m-YzOyKgjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=HmvSpNSEBnIqGERWXq6b3C21AqGVjU5hL6bA-AXXTdb0jgkTHRLYvTP-vHir-vzMLLMIZnEXYLUtIUhvRKWeVhwvPMHwn7fe3llB-K4aXHh7jFo62GHMXXaW7C6mUC1x8nGQNBKUiqipYBszYMd7h577i6mxoNDhkBwMWF_J7Eqbx-hBGKiM8M4td3TmZ8hRI3ugUzEkoykeKNBiBxb49ElrjqcppS-o3I_50xETJ23DdTNidOWYiG9srPj4LWkyJdBIkJyODCBwhs6PWZ6Irub3j1Ks3u1bxjpeXiJqDvZ-2pF53ZEbSz1n9hLLgI3mCabxG_UBX6YRbeWNinATjVadIeS-z7N5KvRbEh62C8ARkNXELzG_CxCbBpstw93HI94W1PYmpUEVmORFKa0gBOrV3F-CLfFBu_jnbddrBSwPF-3uilnGPToiIsYrgROO09WP8J4DrEbnq0vwCvuzgXPGW7l-1a275elf7YxSwY1WQtRbalg60pPHV-SG7M0mYp-JhiiMeUmASzjjll08JyvYVVeI_t1NMqthL0SEDXMNXU_wIj44dcWmrcsoA3xhpFckkG9psOxjlBZCFlUxTC1PXLCbalSb2go4UogLQnuR8pbYEUkbLL7rNSoZR8W9BJtqUY_kUyHJmGa8ZNNdc-6O-U2Dw2z-_m-YzOyKgjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLaluGiBWjm06Hr-m0PSnqWsjtZGhbzCRsrQ9zMeDV5tw1xUdcdWiVqYBjxaoG48JhpN6ak_LxRd7oGSXoPRGKqcogUwqFBHxbYToZo8vTdYzDfgq1E8qfSHBfiBDvS4jdIaWcVRABgYhxGxy6qpoubYIU0LW14FjGM0FYkxQOWnJ7Jq9pCSrO_V8qzA0M08TZzG8tlxAIcp7N8T9Kyq4ViWtcgZi599C00dndRd8OraYiiTvwxyFM9FHCIxq4jScqjplqFKuJe_lrCxPummBaiK7N4ZvOfs1pk7T4mrl72Lr5olvXdil-OoKxI8KPtLJ0zAR9EzNiDJqnp37DaaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=KavoGdU1WZwfY2EmunozCtYDeGUihv3hg-TEzetrVKpgdhpmfVjnWW7Wq4w8cl6-P_BJ0eEHz7xP-t07NvjcbtyEz0pY8Ycv9DvYoRlLf5Vm6zqq4F3dDC-lf4mipFxfDLn9MMfyZvKJWHBslvV4Gz4nlZnjPEho6zXWwL5cL4_xcD4N7IKxQJx0YeSNpTtKjomozLvgVH2032A9vF9h5gihVBzpLlXiAR9g6ReDc1nFZ4GkjpsGzvPVFOHZsiO0uX-vPAHG30xEbDZdYCoFswW-zlBYXM01GVfhTPD7EfveIScHAWaU9n_la4lMz_KWPwjSQopRXJiP6ymEPV_3urZVTweSeEn-GGEGjXY-TkGCqWEXblxBX4aJE8FYzci-CPxJKfO5ZIWQTqrd84lSjYXu3Hg3AD71fq3-rowWUQE-nRF4z9GSNYMRVAHXafQMnDN9c20onschJIhuefYV1w8nRRXxTZp81l7WdQodGExkv17pF5scq79GD4QVnC9qGv2wq0MY-EqVKDrkv69wc_2Scwo36jNmmumXUWA30vTjVKBXcmOfMXYtKfwTyvW5QXGW0uhbxGsD9gQY7xF0qcE8QAK4kerXSdCrgNbj75tvlH4Z9Rnsm_Z4Q03jZzWFgpTT8uT8Ly66PojPbVHAMxLY6fx8c-tIs7XMnR_burY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=KavoGdU1WZwfY2EmunozCtYDeGUihv3hg-TEzetrVKpgdhpmfVjnWW7Wq4w8cl6-P_BJ0eEHz7xP-t07NvjcbtyEz0pY8Ycv9DvYoRlLf5Vm6zqq4F3dDC-lf4mipFxfDLn9MMfyZvKJWHBslvV4Gz4nlZnjPEho6zXWwL5cL4_xcD4N7IKxQJx0YeSNpTtKjomozLvgVH2032A9vF9h5gihVBzpLlXiAR9g6ReDc1nFZ4GkjpsGzvPVFOHZsiO0uX-vPAHG30xEbDZdYCoFswW-zlBYXM01GVfhTPD7EfveIScHAWaU9n_la4lMz_KWPwjSQopRXJiP6ymEPV_3urZVTweSeEn-GGEGjXY-TkGCqWEXblxBX4aJE8FYzci-CPxJKfO5ZIWQTqrd84lSjYXu3Hg3AD71fq3-rowWUQE-nRF4z9GSNYMRVAHXafQMnDN9c20onschJIhuefYV1w8nRRXxTZp81l7WdQodGExkv17pF5scq79GD4QVnC9qGv2wq0MY-EqVKDrkv69wc_2Scwo36jNmmumXUWA30vTjVKBXcmOfMXYtKfwTyvW5QXGW0uhbxGsD9gQY7xF0qcE8QAK4kerXSdCrgNbj75tvlH4Z9Rnsm_Z4Q03jZzWFgpTT8uT8Ly66PojPbVHAMxLY6fx8c-tIs7XMnR_burY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=vOTGHGrgoumNi-53mNauprBlIGT_YrL-ksAHE6g4ajAOAhTtA5ALHV8rQpbXGOUcOLZBtjEM1byRFDxFP9_tvT4v1pog11MXTpykEpv0DrclwZvZSv7ejXDVP10yPBCE2OTgX_znzGdEx10RjYvHei3eBJFGvSPAJBv9KqeVQlCU6B8N_F8lG9ZNH8SD91DqEtqQbXfmmniURTLrFUnCiZPbdjuB6wwa2vchOy8rzEdzsThJGltxUET1zNC5PXn4x_bPL166sGv2JZf2gUEdlIYFa-V-F3wKHIVVHQG3fhTDJuOUODcyuQRrSY0TCwQejD94jQtBJoMRCVGujH8T_KUI9UiIGCVg0PIPIPRKOCJtJivLHhrzcC-0_-mfhIYrDfBTc0sZUvH1vMMBz_ZoTp9JE5ivZvNn0n9vn1_GceKl7hcHiD-H2SQ9CiW6kgt_Zge3N5Yq82QEuIrxnNdDe03lsAsSUOUoK-C_IZ5YUypo6gpPOL2Ju35NjtAohtSWHf2uMlUDPS9lZ8jFatQaGKWD1N0gdPBf8YikrHc1jJCsRZv2hylD29gzWnvgvUMR1ONEp0_RETWaxki4A0UDGSZ6Rlv8yOXoUbiffqTijkE2rN_jvnHauhR46HF3-hRo26pfpNNBman7sMER4sKyuG_uLXvXsT4PaHzOSosxQBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=vOTGHGrgoumNi-53mNauprBlIGT_YrL-ksAHE6g4ajAOAhTtA5ALHV8rQpbXGOUcOLZBtjEM1byRFDxFP9_tvT4v1pog11MXTpykEpv0DrclwZvZSv7ejXDVP10yPBCE2OTgX_znzGdEx10RjYvHei3eBJFGvSPAJBv9KqeVQlCU6B8N_F8lG9ZNH8SD91DqEtqQbXfmmniURTLrFUnCiZPbdjuB6wwa2vchOy8rzEdzsThJGltxUET1zNC5PXn4x_bPL166sGv2JZf2gUEdlIYFa-V-F3wKHIVVHQG3fhTDJuOUODcyuQRrSY0TCwQejD94jQtBJoMRCVGujH8T_KUI9UiIGCVg0PIPIPRKOCJtJivLHhrzcC-0_-mfhIYrDfBTc0sZUvH1vMMBz_ZoTp9JE5ivZvNn0n9vn1_GceKl7hcHiD-H2SQ9CiW6kgt_Zge3N5Yq82QEuIrxnNdDe03lsAsSUOUoK-C_IZ5YUypo6gpPOL2Ju35NjtAohtSWHf2uMlUDPS9lZ8jFatQaGKWD1N0gdPBf8YikrHc1jJCsRZv2hylD29gzWnvgvUMR1ONEp0_RETWaxki4A0UDGSZ6Rlv8yOXoUbiffqTijkE2rN_jvnHauhR46HF3-hRo26pfpNNBman7sMER4sKyuG_uLXvXsT4PaHzOSosxQBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=tCDCO-yObimVjF72OKIRCR9nmVJkHG1UYAdpzBqJ0_cuPtT0aEYI27WBXClyTshUoqXoETOhlfE9pf0DDWFNqend19iaKoxTxlan6tQsC5IvyonhQxvxaRvg2UOojFAfc5H2AkFqVAklb5eg_dxAI8s6BZcAiRuSuIFWfBgiBKQZqyA26EXQrfJgrc2nRPYmB2HxZVcbtkxyOqCXvj6og6Ypj0hUny8DojcbZxEW-byfodxK7KtPEwmw87d1hir2_S4z4CXDmZQuBt0wK6px5mtXAc_SeR3EOmNbUYo0vHJkfIcRqapjn-Dh_GXzGaBZpU88rBPMnvgG3iJ7wme7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=tCDCO-yObimVjF72OKIRCR9nmVJkHG1UYAdpzBqJ0_cuPtT0aEYI27WBXClyTshUoqXoETOhlfE9pf0DDWFNqend19iaKoxTxlan6tQsC5IvyonhQxvxaRvg2UOojFAfc5H2AkFqVAklb5eg_dxAI8s6BZcAiRuSuIFWfBgiBKQZqyA26EXQrfJgrc2nRPYmB2HxZVcbtkxyOqCXvj6og6Ypj0hUny8DojcbZxEW-byfodxK7KtPEwmw87d1hir2_S4z4CXDmZQuBt0wK6px5mtXAc_SeR3EOmNbUYo0vHJkfIcRqapjn-Dh_GXzGaBZpU88rBPMnvgG3iJ7wme7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=HDOVmrMRAL5DSm_EczpMIUvfe35NtfWNcQU33TS-rh7oxvVA2xkL4oWPHSlWqhCL7f4qDmKdacamqUu7zi8NNDcb8ZFqT12ZWXEO3nMCv76a9jAYBj2kMHe-2IEeSl5ivcGe162r0ZlyQLQ36ex3aJSiNLdBlrIUsmfZ421ZroUvvOyYCCiW57_XVc6uAHj3R3GGjjmZzRUvP8jg-ptxzlWcW4l9C3BlqSD9OqHw2ax68RvWxZZSoShpHxCTtaT8wHOmmObxmwn_BzWUHMN5osEQOCPEg-VpNVn3JQaAZWpRbBYhjikgl421AC0z0wV2qgdwdKIbB99FMp39GX9boQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=HDOVmrMRAL5DSm_EczpMIUvfe35NtfWNcQU33TS-rh7oxvVA2xkL4oWPHSlWqhCL7f4qDmKdacamqUu7zi8NNDcb8ZFqT12ZWXEO3nMCv76a9jAYBj2kMHe-2IEeSl5ivcGe162r0ZlyQLQ36ex3aJSiNLdBlrIUsmfZ421ZroUvvOyYCCiW57_XVc6uAHj3R3GGjjmZzRUvP8jg-ptxzlWcW4l9C3BlqSD9OqHw2ax68RvWxZZSoShpHxCTtaT8wHOmmObxmwn_BzWUHMN5osEQOCPEg-VpNVn3JQaAZWpRbBYhjikgl421AC0z0wV2qgdwdKIbB99FMp39GX9boQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=bF04VT1zQjJvv1MOIKyH8D2CBSa8Ty_obEUcIu5BQ_dkQVh_KpCRAuCyDalUFo6k73-rnzAPYJiAuAE0wlHEWHXMsFZRiK6dghSW6uhw1SNu9ktPRQ2EfAKeuOSm1LLMySj8j6e8WyRSTOixO5nkMouupQo1T7KAYoQCNbfcJ9NkcXM1H53ZbqOnzBeNAXhPuovE-BakmO8CfAotvYdsSIqzmFtVCug0gsLcfIjOyjRkEg9QGQzHBhuVDsabYug7tn54cAY9wp7SQ2hs7Z66XTmAZxke1z28TZ8_Pt5wXEX0CsmACyncah9hkkhdLLamIASHuKgFktlo1Ghz_P_Y8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=bF04VT1zQjJvv1MOIKyH8D2CBSa8Ty_obEUcIu5BQ_dkQVh_KpCRAuCyDalUFo6k73-rnzAPYJiAuAE0wlHEWHXMsFZRiK6dghSW6uhw1SNu9ktPRQ2EfAKeuOSm1LLMySj8j6e8WyRSTOixO5nkMouupQo1T7KAYoQCNbfcJ9NkcXM1H53ZbqOnzBeNAXhPuovE-BakmO8CfAotvYdsSIqzmFtVCug0gsLcfIjOyjRkEg9QGQzHBhuVDsabYug7tn54cAY9wp7SQ2hs7Z66XTmAZxke1z28TZ8_Pt5wXEX0CsmACyncah9hkkhdLLamIASHuKgFktlo1Ghz_P_Y8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=muiTPzjhwC0lO4C7W18ZAuGlHIE-_dLXznk922mRO9E45RIbSTBtAGIrphZTb1gNtSlyrhESHlFDvOraT72SH61c6k0zxMXdwzl1mHpoI53RrusAgZWok0ZNimKCnwgFut3RTc_ZD6OIAmldi3n7jEfXO710q7emnWK_MuCxs8_FRhRWiCvlsrzVS-8ZF3Gc3V-2ZU0BEMR0mCtc7-WhMWGEWrnyKTI4vSHOzrXop4pm6uI1UIdQkqNi22Tf3zdOMUHdMkwwIS3azZLWiTTyeXHBZDMyycvRlMYhtNagQ3ge3bAHvrTBpUzoHldsG_hMHHAtgfP5VLXNtN0f73PUMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=muiTPzjhwC0lO4C7W18ZAuGlHIE-_dLXznk922mRO9E45RIbSTBtAGIrphZTb1gNtSlyrhESHlFDvOraT72SH61c6k0zxMXdwzl1mHpoI53RrusAgZWok0ZNimKCnwgFut3RTc_ZD6OIAmldi3n7jEfXO710q7emnWK_MuCxs8_FRhRWiCvlsrzVS-8ZF3Gc3V-2ZU0BEMR0mCtc7-WhMWGEWrnyKTI4vSHOzrXop4pm6uI1UIdQkqNi22Tf3zdOMUHdMkwwIS3azZLWiTTyeXHBZDMyycvRlMYhtNagQ3ge3bAHvrTBpUzoHldsG_hMHHAtgfP5VLXNtN0f73PUMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=swl08C5yo_ijJ7FnCYNyg1bLWT8WIX6rF3mpSs66LV22-ndFjpiOX0wBHQ2_378cyZMxKR_rv_LBlL0NyjOLvgPSfAt91K8Tgnmxcg4zuf3_8g_ufBhzRlYmDg1nmfcHznM1ZmekFVo3pgQp7AJqA5mlM5PwhJv4wwXs_htAP2FSQwLDlkvJRHmNmv-FKFNalSt_m6rr7mz4ZAroGE-kNQlbJugWk-ESOiYbZjaie2nxXy2cW314F_LU86byX8ZqQy0dMvqU_3ZCAZN0pfxAZhRawmXCXSZCE1H2xnvY7JkG7Y8NDuU6pha93n-u7JnlJRsIcYHSyex6eq6JMOLN8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=swl08C5yo_ijJ7FnCYNyg1bLWT8WIX6rF3mpSs66LV22-ndFjpiOX0wBHQ2_378cyZMxKR_rv_LBlL0NyjOLvgPSfAt91K8Tgnmxcg4zuf3_8g_ufBhzRlYmDg1nmfcHznM1ZmekFVo3pgQp7AJqA5mlM5PwhJv4wwXs_htAP2FSQwLDlkvJRHmNmv-FKFNalSt_m6rr7mz4ZAroGE-kNQlbJugWk-ESOiYbZjaie2nxXy2cW314F_LU86byX8ZqQy0dMvqU_3ZCAZN0pfxAZhRawmXCXSZCE1H2xnvY7JkG7Y8NDuU6pha93n-u7JnlJRsIcYHSyex6eq6JMOLN8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MnMld5lZfGolRGKNgfUlbPenvSv-fegaQ5jzNlruveYUor1AcRnvxniBWhose6up_tcq6y48mKu1JSKliuds24utIsu7rXIyeY3kxJpSKHyO_IRtJ8H4-RPIJkQE_OgCtQcM5kcVNqrwgmJogsYjsrFbhqPrdsEqPRVNIJ15IUiAtnuvX-PCcRiM5VIM5Bc9YgFBwR0vKKhyxsJyssQoi5SedjRiTsytabcR8pOaZk3Kh6HjpnCYF_SX6H3-kQmnK6LHO_j0h-js2djZbdWXJxwwOkNuIWGDLxSDX4XbhHyLmxkq9aAf_jgojmAUpYDUWuIYs0LeEEDF8GL_rYNa0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MnMld5lZfGolRGKNgfUlbPenvSv-fegaQ5jzNlruveYUor1AcRnvxniBWhose6up_tcq6y48mKu1JSKliuds24utIsu7rXIyeY3kxJpSKHyO_IRtJ8H4-RPIJkQE_OgCtQcM5kcVNqrwgmJogsYjsrFbhqPrdsEqPRVNIJ15IUiAtnuvX-PCcRiM5VIM5Bc9YgFBwR0vKKhyxsJyssQoi5SedjRiTsytabcR8pOaZk3Kh6HjpnCYF_SX6H3-kQmnK6LHO_j0h-js2djZbdWXJxwwOkNuIWGDLxSDX4XbhHyLmxkq9aAf_jgojmAUpYDUWuIYs0LeEEDF8GL_rYNa0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ey0wtBrBzkUf8G7nN506smVO7xAq6NXPyfcecwv_UgNwvQLeaQsAougyAqKbwAcS-zraN6esymybT61yl5uMNwLITRy92ARp-yx8iOhACa7UIbkRSq94SvypiXc569qpHQ1aabfWdUQb7NoQvo5QluaOhT4WR4Vgdu_TjBBMTXoYTvWrI7dbTxXARrzW6aV26n5kTVatqRXdRT3_E6Lm4nZdcfYxkNKOLGa4yjZiojlhD_mNZwlz3berp2nOgRLlHohpsRLNwCyM0ORjYmBVv4FOCVhsaIUwFXqZgJtofjFp1X3jJ9Zfs2YGSzzmBgGt4POI9mNJERpCZ0_KnLzLfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ey0wtBrBzkUf8G7nN506smVO7xAq6NXPyfcecwv_UgNwvQLeaQsAougyAqKbwAcS-zraN6esymybT61yl5uMNwLITRy92ARp-yx8iOhACa7UIbkRSq94SvypiXc569qpHQ1aabfWdUQb7NoQvo5QluaOhT4WR4Vgdu_TjBBMTXoYTvWrI7dbTxXARrzW6aV26n5kTVatqRXdRT3_E6Lm4nZdcfYxkNKOLGa4yjZiojlhD_mNZwlz3berp2nOgRLlHohpsRLNwCyM0ORjYmBVv4FOCVhsaIUwFXqZgJtofjFp1X3jJ9Zfs2YGSzzmBgGt4POI9mNJERpCZ0_KnLzLfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxGv_u_hfLRVvIjoDIaGIXiTDAFoMzk5loskOBSlWzXpxb_hbOfJjdhkJe89ObKnuPiCKMQYbGq_x3lwG8zRyDQcThQIL0YaAYIIRd-dI0CY2VaQNwfWxzF5yD7nQYsYSWa9zs1rhtejY6XL9ecVeew0ca_btqg6uIGLA1Wp64VLrLJu0PmhoWHHyawZSZBFJi65UqisUn8wlrAHfR3UxNGooRQoSIQ92x2pds49NwZbPj2a_dIHxV0QxatELfajKv9z2v5hGoXz7kC7dtUPA1VF68t6FZvepZe1FGQo5VXhto04MLMFsIU4sgY1KWwiZpn0JaTpbuuk_Ke0H3uv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=m9rbBnxTSvQQ_ZuXK6ppwXRdG_wyXxYRVOcqIFN7-4pJ3M6Rko-fFXPv5kYLIh6jKerm_NoBZL49y9NS-0-bw4a_F_VqL8jvp3Eo5Zb_GE5ygDOaPppZU0PSeUBajoXbu0D8jTG2QrMzjRErjlrLqbzmLMKGcklKeCJaYpsvj8i0eqvLOWGYfSBK9miVOYfAnUCewcAXYtflZSxKhjtuiJwbZVR0VvWyUrX6L1knql01sqrx9nao700aXi4jitaKRiA5AycDXOldVNcCkttNjXTPcI1CosYSouBM_rIlOuWvecwiDLxtDGwhn91cpWkilYPQQTEYBzCTbSlvqa2Q1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=m9rbBnxTSvQQ_ZuXK6ppwXRdG_wyXxYRVOcqIFN7-4pJ3M6Rko-fFXPv5kYLIh6jKerm_NoBZL49y9NS-0-bw4a_F_VqL8jvp3Eo5Zb_GE5ygDOaPppZU0PSeUBajoXbu0D8jTG2QrMzjRErjlrLqbzmLMKGcklKeCJaYpsvj8i0eqvLOWGYfSBK9miVOYfAnUCewcAXYtflZSxKhjtuiJwbZVR0VvWyUrX6L1knql01sqrx9nao700aXi4jitaKRiA5AycDXOldVNcCkttNjXTPcI1CosYSouBM_rIlOuWvecwiDLxtDGwhn91cpWkilYPQQTEYBzCTbSlvqa2Q1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=sErCzSjPqvslOwaoQP7x6plhr1sikhPYRy1oehCMurDiJqJDgxSfJik3u2fyDH8Lq5Gcq7M_oacrEPbuP_GNeAh2FiEVjLRDtVDAzAn9QiR88EvqNeDTxAzVyvZoObgnLoBOgPiaTxFdJo75dGFHtITjIYLC16JabjF_yXu_twlYkpSy8UkhpKC2GvQSWB4dHs1_MRUSK6QmRkX_SVOVWxnDPZ7NRt6fgbNCHhHqADcT7w4QN27jmYDZrlj5V1ztwASWcOt_6luX68Em7oXr4V58TQBK4Wv5s0zVIjKmW7XaWMxZ3dPp0B8r1rBbhJL6lHZBGIebzK_RKcApUqNoYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=sErCzSjPqvslOwaoQP7x6plhr1sikhPYRy1oehCMurDiJqJDgxSfJik3u2fyDH8Lq5Gcq7M_oacrEPbuP_GNeAh2FiEVjLRDtVDAzAn9QiR88EvqNeDTxAzVyvZoObgnLoBOgPiaTxFdJo75dGFHtITjIYLC16JabjF_yXu_twlYkpSy8UkhpKC2GvQSWB4dHs1_MRUSK6QmRkX_SVOVWxnDPZ7NRt6fgbNCHhHqADcT7w4QN27jmYDZrlj5V1ztwASWcOt_6luX68Em7oXr4V58TQBK4Wv5s0zVIjKmW7XaWMxZ3dPp0B8r1rBbhJL6lHZBGIebzK_RKcApUqNoYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PAT2sVfFhhq5-Kll9mLJAyxvmReT-bIdKcmbM_eggvPB0wCd21qG5dAP36cU107ak7iP-EY5Kzkx4jNqJAl4DUcA_CfkbmVNMP149oh6EJtqx2YCkcz1fJJKyA48MbP7NMQcu70KNssrTjmAgdDqMtn0fYbfoXX4Wk0rORCzn0oNODSj3zRvvewFINiAtRELLI16dMCSrJCjH_aF6mZvN_w-JG3TEGS1RSwzJzNRQc_qA8TIS4cEmwVmVfN1aRAcMSUOGX7N9RzBlvB9XS8FvLJjUUuuSfPwSBlWV21UwEej8PNxA-oZ9_FGHPREzw7t_L-m7BRp9cXK4orFFaNxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PAT2sVfFhhq5-Kll9mLJAyxvmReT-bIdKcmbM_eggvPB0wCd21qG5dAP36cU107ak7iP-EY5Kzkx4jNqJAl4DUcA_CfkbmVNMP149oh6EJtqx2YCkcz1fJJKyA48MbP7NMQcu70KNssrTjmAgdDqMtn0fYbfoXX4Wk0rORCzn0oNODSj3zRvvewFINiAtRELLI16dMCSrJCjH_aF6mZvN_w-JG3TEGS1RSwzJzNRQc_qA8TIS4cEmwVmVfN1aRAcMSUOGX7N9RzBlvB9XS8FvLJjUUuuSfPwSBlWV21UwEej8PNxA-oZ9_FGHPREzw7t_L-m7BRp9cXK4orFFaNxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vdGwm5rfwrGFDrYKYrlsPn0MDGT9e_vxAp-Wdhc827xCUhIunBe-10YvgK1yAfO7VBcUB0waaqi9s7yGqQtlFZw399rX6KREYjhbBVCrt-DGBbQXJmcMfgo2Dl_gfccDOpp4jgSm3jHmNX88sqRgpiW7mlWs8UjBeXmGK0rEXxZOwbz4BGb6L_XF-kP3CTvPHcyVf9TU5J4e2bP1OznEek5R-fksUhS8J52w1Yjsd-yb12dpkg16bmwl3uBq140VJqrUASrpOu0gHh3RiMoEc02-fF0SgsU8O9s7YUbyGenNvlo9XEimrCRDp10sbB7RGQ_nHt4K7sK2AvdvAjPAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vdGwm5rfwrGFDrYKYrlsPn0MDGT9e_vxAp-Wdhc827xCUhIunBe-10YvgK1yAfO7VBcUB0waaqi9s7yGqQtlFZw399rX6KREYjhbBVCrt-DGBbQXJmcMfgo2Dl_gfccDOpp4jgSm3jHmNX88sqRgpiW7mlWs8UjBeXmGK0rEXxZOwbz4BGb6L_XF-kP3CTvPHcyVf9TU5J4e2bP1OznEek5R-fksUhS8J52w1Yjsd-yb12dpkg16bmwl3uBq140VJqrUASrpOu0gHh3RiMoEc02-fF0SgsU8O9s7YUbyGenNvlo9XEimrCRDp10sbB7RGQ_nHt4K7sK2AvdvAjPAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8ky0Ox3ROcDNdhMJXYaX9dwuMSEVYNnB9xSFFhmnHdNBrJ9PiaUNlUyFSbqzNsw_0O8xEpKUiwJG5pUXw-3nT3uTMF7AhQ6sPwU0ZN9chAgFswtFCmM_48FnfkqFy1-9aiCof8SSW4_Osm_NF9z94tbDdJ9AGPNOIh9m8kkbEPO2G3ZPdiIhODW9ukaXcY3WA89YfSogSJE7BdZ5JRmGrd52UmteLL-yPMBNAi6AhLjoqZq2si2eaZFZk6PwQPgAbEybyhIR2nwX9oe40l91z3lsPYCsG8cMnJF9pg5lh-DyySWCqs7DOuqDATUYwubY4RVdrMnUmxt4AmVnLUgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=g1pySpr_3kKtgvjnEIE_sCt34fobdYoNx8Xs6KELailqyTxXGYCyhuwtbPKVNBT5ruIo-Da4EpY_kZujjPAoKyqtoJ__2GUi4HV4lT-rKMcu0bKkqP3lC2oTWnV5jmT6yga528nzypmYlJVw7AFD8NyChUZH2eEt0BgrR0dCoVMQLcKKMXccy3LKemFnNdWW2efF55TYhjK-p5U4AwQQ6aBpZKe5AtOYe-VxEs0yXdh2HbVnqDoYYDfZdOv6sFGNsbtlBf_Dy-xXgREk5LNPqKbvuEIkOX7-N61UujvE8S_3jvM2kKbx6DTlYmItKZYeWgGeGHnXcpAn2K5sA3cNgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=g1pySpr_3kKtgvjnEIE_sCt34fobdYoNx8Xs6KELailqyTxXGYCyhuwtbPKVNBT5ruIo-Da4EpY_kZujjPAoKyqtoJ__2GUi4HV4lT-rKMcu0bKkqP3lC2oTWnV5jmT6yga528nzypmYlJVw7AFD8NyChUZH2eEt0BgrR0dCoVMQLcKKMXccy3LKemFnNdWW2efF55TYhjK-p5U4AwQQ6aBpZKe5AtOYe-VxEs0yXdh2HbVnqDoYYDfZdOv6sFGNsbtlBf_Dy-xXgREk5LNPqKbvuEIkOX7-N61UujvE8S_3jvM2kKbx6DTlYmItKZYeWgGeGHnXcpAn2K5sA3cNgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=N95vNBmDcCLsPiz4H_EYLxXi-L3TzHyPNhyznC2nUjlWC7n3Ju-7IknHT-AnmHNiWlyJMeqri2ig9La7IlorSnGNPU_tY4Q8mQ1cVl1Dbzi_S0zPg1fj0hubD4OCAW1J-eqhVy7cvxxBK-RbfO6mZnEa4mg_ihmVvPW1cwbcQujlgVPb9D31q9NJ_nyL4m38lsvX5-3TVDvOF67OnEot2rXSrcuco_14Xlwj0ULklH_sgvty7-pVCxJZyTbBkBluc1_bY-8OPTToU5e6vg88awMi7AMVfxQvJLM43vdfxw-2D9hGRH05csFZ_-16RGzXTxv7-hKjdeLzHPHaPnY3OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=N95vNBmDcCLsPiz4H_EYLxXi-L3TzHyPNhyznC2nUjlWC7n3Ju-7IknHT-AnmHNiWlyJMeqri2ig9La7IlorSnGNPU_tY4Q8mQ1cVl1Dbzi_S0zPg1fj0hubD4OCAW1J-eqhVy7cvxxBK-RbfO6mZnEa4mg_ihmVvPW1cwbcQujlgVPb9D31q9NJ_nyL4m38lsvX5-3TVDvOF67OnEot2rXSrcuco_14Xlwj0ULklH_sgvty7-pVCxJZyTbBkBluc1_bY-8OPTToU5e6vg88awMi7AMVfxQvJLM43vdfxw-2D9hGRH05csFZ_-16RGzXTxv7-hKjdeLzHPHaPnY3OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qY2S3SEEwVhTDDshIair-lBDSUOFFQ4m-Gs8cazSR8dOJlH5wTo6CMO8w6BNNSS5YPEEb4xL4hylYRIaABsM4iXvzFauA09azcyAGdcK_mHYIWCetjCqa6GZzC91YuACssHr3tGI-5INtWPMAJhaWdoz0OC-ymJxh05YuVAI4ZPfTl7L6AMrTiQ6FirYl2XANVOAQnf6o1NxnUa14U71p7Pytfb4k8OvehTJzf7mFBYrKsSoFEmTA9_Xzws_BejFGV2Xady3wner90e4ohbHNqZ1hrkPL_LBYfd4jQeOxYOI_5NKTnxhQC-WzajEJDVlXSQKe0Ul68ABSZI4gAnnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oepDliiW04K-njEGEsX_RjfPKpHJ17Av-dm-q87n-Tg3Ln8sA0lahuHLOK3gEBM2WNkMi6UKBKM4GI0tfNFAuka2U-jtggibpYnB-VLoaOUu-EWplLZ6ViBoF7XXrpKKO78DmuNnNiBioXU4YEQKNBHvM0NZXfzDmqlS9XRr6Go8Jnb5XIQElF86Jh_5Xr4DS45OF65v8F_r1w55jbgHdFjD_1wN37hfFAkZJsPHyhYPWnrlCBn8cu9qM5tHNFuln_TuYjxK7dtQtggEBo3u5p5xgTpjHmc0iElLE4mZRwlMhDeE4RNNQVPeIMW5dKggUQ4SPyYS2SQsUZKfU4XO-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mM9xdM385GkKpwfvrdKA8WU-DhpJsrlSA6iimwVjS589AZDtaAR6YfY5nEgiwZbF9wM3gJBSgOy7Rzyyj0DZrXIexoLnqqOwoovOPyOQydymhikBc1Y0t7cXtCy3pDhSyLhtsz8cI8IUVyX08zroYffVYskRZpF_xmI8n9UINIr2wzz_JUCr-CWvjEuDFa2pRVWhxA4QrWooWUBmqhgB0_Rpbjy6hDpHjyzjLPsc-2kAODlnt8mKKmUFlHRJRsZj3nR_RZ42koZ4Nr1fHiCVHbmZQ2iHb6tjilvN-X526xIsikmrIA4gCwptYvRm768YvrcST5gJWaNeeR1AUHtlqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mM9xdM385GkKpwfvrdKA8WU-DhpJsrlSA6iimwVjS589AZDtaAR6YfY5nEgiwZbF9wM3gJBSgOy7Rzyyj0DZrXIexoLnqqOwoovOPyOQydymhikBc1Y0t7cXtCy3pDhSyLhtsz8cI8IUVyX08zroYffVYskRZpF_xmI8n9UINIr2wzz_JUCr-CWvjEuDFa2pRVWhxA4QrWooWUBmqhgB0_Rpbjy6hDpHjyzjLPsc-2kAODlnt8mKKmUFlHRJRsZj3nR_RZ42koZ4Nr1fHiCVHbmZQ2iHb6tjilvN-X526xIsikmrIA4gCwptYvRm768YvrcST5gJWaNeeR1AUHtlqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAO0GRPQzDDsgwU0-gZJoggxyLUi690Ga3KuwrhsxHfNjQx1mwpEkvIzL4tabj3RjOxZx64Xg0OEOtNKFJETYtZ_NF0vBha1siT_ZUmShu-4YSltIkhgtawHkBc1N8l_l2hHHVRCinm-hnt2s4BsfIaNSz_DZ9lqhjB3TYDUVXTXS951gjIxCD7FMJOxTYBN7Em0JU_NIeaBEDEb8WW-gdhXxFHfL-2Xrl8hNEai6Y6CutWz9T940OtLBmqYQ-9zyFyjIL74Si-j09luRaMI0OpIkK_GdtqxWTYnAexjH_EYn0kHBKt1MWFIn1OOoKS_k08tn64eaMHgE2ginXQt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al_CXtMK1wDgtU7PxVyUwsGAliMopRLu9ep-teoLxc6fZHC4fbpOstsnmls3CjeiEyV0z_JvWKfTySk1rd9RmKISNU-0mZEAT2nRCdo0QhhxDM6vn2ugdbPPFFogfXadTF8vZcpXolZnhvi7Xn1Tb4s6lMMGOgUIN2JPE9aFOK5LwO4o6XSYwoF8686nufU_eAtQXDt7_3VlMIx4RStKAbKEfVw5h6FuGxhCwloBF7PBwd-QD2XLxf1BBSchyIFR48qmJNYtnFOeWuCmqey-TLClitduJ4Fo2b05VLr0HzQKYmhm3-kIqPYn76vh-CYqbROkwcfBaRvwmGhV8IAEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl7AwzmH5r5ZdT5p68D3oUMsQeXkOr5JiAz9_dlq2QG4cHvmOz8b7rPaOZMKPv7joHnKO6qPsraSB6LIGzetTQo-G23BpApdVZcjeD5TFkj-EUdO3nwJPl3P78Cb-8k9Ad5dJ0J64bZSGjhq_wzRqfZmEGslj4mN0Gs_kOk6z9hnKeK7lJG2Kw9eenTfo4oCgsbt2MhH1V-UGJ2KJ2ZNsaNwrM45x4lsAsbsk8lt8WiyhfghXzhESX2c2Eyala9uOvIbplQd6pQw2jdupGa3Auf7SJ5M92IuH4YAk71IJqwxp7wgSD4k5r6Cavjajcyk_kA0969iQQDQntLLfolY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=eBPa8yf6wU1BImDckOUQJHmScH0tIE1r1pXs2Vkc2dzn0ly4vpwoqMz_0O_oOT8uKDrbSnwTHVUwIPf3_yI1H7488Ujv7jSTWhNpnCNiHjrBQMvyCG6c552yXtXDXQdopIrN4BvoUOlXqeG4vjwNSi7ea4y5--6kvlruMIQreAkWvzIkYLNkAvUV0q35aFGOh_hB-HB5PXkWafV1wdSGYm2ECrxNUhjnXr-DJOIBdJMRKqduyu7SadJI45__-lzqilwVQt5SGXyB0fYm2OVDJS0WQpLTCtk_eNr_QQPp2hQ87gQ32vVs7PV-wqQuU_QfOebLmNe4f7_eYnX6DJ1gRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=eBPa8yf6wU1BImDckOUQJHmScH0tIE1r1pXs2Vkc2dzn0ly4vpwoqMz_0O_oOT8uKDrbSnwTHVUwIPf3_yI1H7488Ujv7jSTWhNpnCNiHjrBQMvyCG6c552yXtXDXQdopIrN4BvoUOlXqeG4vjwNSi7ea4y5--6kvlruMIQreAkWvzIkYLNkAvUV0q35aFGOh_hB-HB5PXkWafV1wdSGYm2ECrxNUhjnXr-DJOIBdJMRKqduyu7SadJI45__-lzqilwVQt5SGXyB0fYm2OVDJS0WQpLTCtk_eNr_QQPp2hQ87gQ32vVs7PV-wqQuU_QfOebLmNe4f7_eYnX6DJ1gRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=jXkInDDqrC5D_wxhcRgj5Z2jAIj1fVG4fsnoIRQGLKdCXCWthFV5BtCsyg3_txwrKOTkx_2HserklrLWpOxoZ2Q6H1oRulzHb0cZPMyr-IUecjsgZYUlXmEZnBmg8dzYi-8wpncp5rvVwoghUGmhk7NFMUKtM_2pEczF3uaCTgQJJYxa_zMBMK5vEpUi0VRUhoSMs8qliInaLqA7fbtr7QYMzlzlY_kVIEP86pN27IWXMEBZEN6TQGJb_IX6bzwQOBOUdQmL0m-wFSTDGG-RcUlLV3j1Jnvv2NxGvFZs7t8OS-DwGq6RsPCBFpr3FziCiNSgdwTkpcNrNjGqAkFrjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=jXkInDDqrC5D_wxhcRgj5Z2jAIj1fVG4fsnoIRQGLKdCXCWthFV5BtCsyg3_txwrKOTkx_2HserklrLWpOxoZ2Q6H1oRulzHb0cZPMyr-IUecjsgZYUlXmEZnBmg8dzYi-8wpncp5rvVwoghUGmhk7NFMUKtM_2pEczF3uaCTgQJJYxa_zMBMK5vEpUi0VRUhoSMs8qliInaLqA7fbtr7QYMzlzlY_kVIEP86pN27IWXMEBZEN6TQGJb_IX6bzwQOBOUdQmL0m-wFSTDGG-RcUlLV3j1Jnvv2NxGvFZs7t8OS-DwGq6RsPCBFpr3FziCiNSgdwTkpcNrNjGqAkFrjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Uoslj-AzB7K4TlNJ6z0-Kr1GQq6HcCqXa-e7yJsblvF8_jW074RF5ZoHhyOw55zvQSGItM0QqFQ4LocU9C2q3WI2VTFchKLqmdXfRP3QJUlTuie3dVNDNu7A2GltVv7tRgl-BKacJ1RxrNGp3Z-esooNTKya-QBd8oAPdK1Xy89FDYQaQBxrtAuLGudvcFMv2Q5YSimO-RL-SX0Yu_Q4Nu6QDj73l7bakY1bdtoD6A6TfiT-q5nmdRyHbba2bs_ChWhM6-scXuczG-eELl6Zbd2i7nYc3V69HmfANvi9H75LEsoN0bZk6_OQr1cOZOEvI4_YZTm8mKmyARVQJgXVRbpDhM2gxG3BsODajp_mq2x_oB4HypkxuOjiywpgHWpwiiT1-Aj5id6ImhhF6Ue-CRFSQ80oOsvTiTh-JdvnRNZUKVQyX9oHINlHK2icteRl62zzywu6lKOoEhUWzE99011rNyJsPQ1NSHlZyjn-NyeSy-9Ykts9fOmZsp8TgVABEdV9q5NFltquxfCMM-ZPqHwz7zJE79CqPSxXU890-gR3shW1Ch7vHs2ajXrXTExEKGaki1YoRhyNW4zrneQb1zUmCmg5qU0Zdxxd7xtGO1HzGgheaYKeIRBUj4Fi2_DnDbJ7FFaEDeAPJNF4DsLJGyj7-OuQAsCGOiEf97-G_Tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Uoslj-AzB7K4TlNJ6z0-Kr1GQq6HcCqXa-e7yJsblvF8_jW074RF5ZoHhyOw55zvQSGItM0QqFQ4LocU9C2q3WI2VTFchKLqmdXfRP3QJUlTuie3dVNDNu7A2GltVv7tRgl-BKacJ1RxrNGp3Z-esooNTKya-QBd8oAPdK1Xy89FDYQaQBxrtAuLGudvcFMv2Q5YSimO-RL-SX0Yu_Q4Nu6QDj73l7bakY1bdtoD6A6TfiT-q5nmdRyHbba2bs_ChWhM6-scXuczG-eELl6Zbd2i7nYc3V69HmfANvi9H75LEsoN0bZk6_OQr1cOZOEvI4_YZTm8mKmyARVQJgXVRbpDhM2gxG3BsODajp_mq2x_oB4HypkxuOjiywpgHWpwiiT1-Aj5id6ImhhF6Ue-CRFSQ80oOsvTiTh-JdvnRNZUKVQyX9oHINlHK2icteRl62zzywu6lKOoEhUWzE99011rNyJsPQ1NSHlZyjn-NyeSy-9Ykts9fOmZsp8TgVABEdV9q5NFltquxfCMM-ZPqHwz7zJE79CqPSxXU890-gR3shW1Ch7vHs2ajXrXTExEKGaki1YoRhyNW4zrneQb1zUmCmg5qU0Zdxxd7xtGO1HzGgheaYKeIRBUj4Fi2_DnDbJ7FFaEDeAPJNF4DsLJGyj7-OuQAsCGOiEf97-G_Tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Ivv2jv5fERZ50TxLpso0zNE0Neeb9bEzoQM48MQHvDGDJuwNxqHrVz6zGj9Wfj_wyiUFa4U6lC3_J2LLx-Mh0ND2LPPRUJmsWVVXQqBe7wbDkcLX5RWnR1EPW_p80Eq0kw-DSot6twfYzXYbqbS5KShmNnm32HTKdXo1lbu3eLwyEdCDGEjC3WVexB29VIPN7kVtn2jNhNlu5ek2UJYMXpfl6iDTg4pcQzj6VQ6nd5H3ONhHU1yG-iRc1JdcnuiFoLXvXweaoAG3HsZ4wgByl5jUezWFjIS-311ADNQzOC5JJr9C2CSvVcL_t9zQd_x9i9cDJ7Bay0FT2RmvjBubK15C-gLjeJFkuwBOgcSpYWxhA4wJ972A1RdQvKhUM37ikaaJrbSy5talF1i_85D4o_IXgarZeLPfP4vH3O4MQYGo2NlSDsQDY_76xy1SLGkC1lvF-WSpZ8c5wS6_qp8jAO0rrQVK_n0KBJmW8_IWOrmFA__SjqxRtoNfsKSgu_aVxg4_Ho8GkHDPgNp5jpafzjBlxNuvRe3Qhc4G7e2eXfDVn9af_4pcOtWfG9BGt0JJC_a4kb8yMH2wRoq132iWnsttj9pdqlU01DHUAPGLuIvbTJu94iCJ77_LMg9TcLae-MJtAQWEg2boDlwJKaW-8Rk3I8sxfJ1QRv1OxHWPsks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Ivv2jv5fERZ50TxLpso0zNE0Neeb9bEzoQM48MQHvDGDJuwNxqHrVz6zGj9Wfj_wyiUFa4U6lC3_J2LLx-Mh0ND2LPPRUJmsWVVXQqBe7wbDkcLX5RWnR1EPW_p80Eq0kw-DSot6twfYzXYbqbS5KShmNnm32HTKdXo1lbu3eLwyEdCDGEjC3WVexB29VIPN7kVtn2jNhNlu5ek2UJYMXpfl6iDTg4pcQzj6VQ6nd5H3ONhHU1yG-iRc1JdcnuiFoLXvXweaoAG3HsZ4wgByl5jUezWFjIS-311ADNQzOC5JJr9C2CSvVcL_t9zQd_x9i9cDJ7Bay0FT2RmvjBubK15C-gLjeJFkuwBOgcSpYWxhA4wJ972A1RdQvKhUM37ikaaJrbSy5talF1i_85D4o_IXgarZeLPfP4vH3O4MQYGo2NlSDsQDY_76xy1SLGkC1lvF-WSpZ8c5wS6_qp8jAO0rrQVK_n0KBJmW8_IWOrmFA__SjqxRtoNfsKSgu_aVxg4_Ho8GkHDPgNp5jpafzjBlxNuvRe3Qhc4G7e2eXfDVn9af_4pcOtWfG9BGt0JJC_a4kb8yMH2wRoq132iWnsttj9pdqlU01DHUAPGLuIvbTJu94iCJ77_LMg9TcLae-MJtAQWEg2boDlwJKaW-8Rk3I8sxfJ1QRv1OxHWPsks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dwYtPTQ2vRXqkS3-O3kzYty098HDhgW1RAc3KcCM0I5INGMhV8MT8sH1njZWrGaXvz98q8srYMyFR5G2KXVYMBOrV66FyILjWvYYOlxZjlWV1Dlsa-PQ8VwLH6UG__g5Pd-J_RecwH9C7M09-TWW_g_sJoFeDe-fxnyHZrI3Uk3AzJJqDNEA9PGXTAwgeC_QjBx9ELv5gr7NThhxYerjc2tyfPE3CKqX94M5n0yJF2pWpdAkvHg4KhqJqxJdmI-Uaq-AaTk58dIFY_6upRl6aP5Pg7hOhzyjwgJh_VcbrrOi_aOQdUOOVsOqmaIQ_k2rwNxvHyvsMps1VohsARAWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dwYtPTQ2vRXqkS3-O3kzYty098HDhgW1RAc3KcCM0I5INGMhV8MT8sH1njZWrGaXvz98q8srYMyFR5G2KXVYMBOrV66FyILjWvYYOlxZjlWV1Dlsa-PQ8VwLH6UG__g5Pd-J_RecwH9C7M09-TWW_g_sJoFeDe-fxnyHZrI3Uk3AzJJqDNEA9PGXTAwgeC_QjBx9ELv5gr7NThhxYerjc2tyfPE3CKqX94M5n0yJF2pWpdAkvHg4KhqJqxJdmI-Uaq-AaTk58dIFY_6upRl6aP5Pg7hOhzyjwgJh_VcbrrOi_aOQdUOOVsOqmaIQ_k2rwNxvHyvsMps1VohsARAWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKaeFe0Nv9XtZnk7jx8HunbPbRNE3-jLrZ_hn0pQKXBb4lnmQssIlj3-L-Bpbq0pBE-1YCTQPKkxGsClZkLIAOCnuO4GkCdWJxPHLJ5ElfRhdDunWA4fonLsqdEL9Sk6yk_u_86mE3Hun5332-BvBFyfpMrtmg2vld09v99XRpUDgLy0v_3ibjU-jV9xsK4nkq2qYqahzKnPwKUl2kCuP8ajuQGh8ucuIkrEoCigNd1TkMb8w-aQNd_eRBTggR1RFFOuLwwwgEO9wCQmCBefkzjy5K7EP83w3nbHJVKMtv-d5HSzTLb6gDghehjIJYLo98MSBiWi0y5jqeutHPZe2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=oFGXNwzqfMTqlR_78ZSqxESHMOD9yXhoO593LnVdLJUEPOqwbfeJFXgSwGCwpCTPCFRURLeUjNjxfA1COemh94h3E7v8rrM487Fm3u3uF-03fJWllkkXJjTkMl2cLZpIwNhxfRYuXqG4cs1MKzntH238ulvkWxt12jb19XQEELYqrvrLXTm1yxIcj-ysc_bv4EaTb_ToCL1ZUJIVHO45_C7XeLH03dGe48T303OqaaHFj_5GmxeASjt4Fu6H99peM2l7yKDUuX2shQxvrEhzTft17dX6G23uiCZ4a6hTsnREWGplAPKEtQOh-KTrqQcndIKwT3hQgy6Y6vn6Gf_foA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=oFGXNwzqfMTqlR_78ZSqxESHMOD9yXhoO593LnVdLJUEPOqwbfeJFXgSwGCwpCTPCFRURLeUjNjxfA1COemh94h3E7v8rrM487Fm3u3uF-03fJWllkkXJjTkMl2cLZpIwNhxfRYuXqG4cs1MKzntH238ulvkWxt12jb19XQEELYqrvrLXTm1yxIcj-ysc_bv4EaTb_ToCL1ZUJIVHO45_C7XeLH03dGe48T303OqaaHFj_5GmxeASjt4Fu6H99peM2l7yKDUuX2shQxvrEhzTft17dX6G23uiCZ4a6hTsnREWGplAPKEtQOh-KTrqQcndIKwT3hQgy6Y6vn6Gf_foA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=jQqXkJSXiflR7USiWGPS7fS29RRO84J_kXQujRkkjWKvstQkkBxk86Nhp7EGRcYNpdU7bcYhBPyAI_e7xvLg4A5aECnBBaU0wAIZftHSvx_Gj9Wnv_JWdrqzkUPANRFO4Td0_Gl-tX2mFjbQ97bYNLmea7tUO_vPEiqqdF5XzkvsirQffaH4yJeWHJdhrSoa0k0MwqB72QnxgKFReeiLuVx0mmIEcpLbNNd2n05gNm3EtVoR3gIEnaMq6MC4JXboiAZCgJKZWgb2ngnLJfcpKbm8xapHWqaDkbFEtjuWqad7RaybTYlbGXDzjUkBWGIhknp7Q-llcMG_QUltRFhU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=jQqXkJSXiflR7USiWGPS7fS29RRO84J_kXQujRkkjWKvstQkkBxk86Nhp7EGRcYNpdU7bcYhBPyAI_e7xvLg4A5aECnBBaU0wAIZftHSvx_Gj9Wnv_JWdrqzkUPANRFO4Td0_Gl-tX2mFjbQ97bYNLmea7tUO_vPEiqqdF5XzkvsirQffaH4yJeWHJdhrSoa0k0MwqB72QnxgKFReeiLuVx0mmIEcpLbNNd2n05gNm3EtVoR3gIEnaMq6MC4JXboiAZCgJKZWgb2ngnLJfcpKbm8xapHWqaDkbFEtjuWqad7RaybTYlbGXDzjUkBWGIhknp7Q-llcMG_QUltRFhU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxSlBblnyDjoM41yTtHJL4_JDxAediTJmEDdP1obAUJtAAM7sZlerpDp-z-DbmMU2z50AeggZxqZPBqGTgLW5locNy3zMQUj-XHoY5ipUsF6YB6lDkVWLKW52Hk7RHkt_Cc8noLcADESLk8HNxBoKaxWht1Yq5jIVBwAbRwY6neHVXm90VotuqsYpISCJsELfNlYOBr3QCnFfnuoIg3oyx-j4hD6WvA3cHfAgPZ9EE1bsYm8SSnI3XF60oYBZnL4546PyK_yPcDBGTztyzzNzOfgulHYajrg61Ic-fOvluCRUqJkpwXyskZVHY-jA-MbTNMyrVAvt4Lw8Z9joPwiYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXGxzPvPcudrXGtTuFSC_vUY8E063MoXwse9EnQgiM9DFnloYzW0PRVf2LBsA5Bj4wZgyU3ea7vOi85MP9uMPd5v4hLLiw2PrmfyAsHVX6fqB8MQ4NoQXyVrro_z4PDgHCUUR-73Sy4elI7n13UbSctODdiX5iWFnehrjeN_FN06XF-iRlwVT4FXObNgGOcon5uWsR5b7jjYpIbVVE8Vy1veyQzlmVmG6N-ml039lKmfp2FsPs1eLWb7q7bw3t4PoVLwot6QSFqkVxHRv-CTXNSQn9UNRZkjTScSOd-mLJ2poXxzD2U9gCwOSgsJSEHWwZg-5WCPppKVb6FH9mSo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvF5RLlY0cd6wsZIrz04L-goKq6DiogWEiTopa9QUBaEtNVCV8lfHbcIR9qjEKrdu9SQ7KPIrW7yZkytO9AhAmebmEXQSjo6j-OEMeI1g0SuNWrtF3fKKIkrxl-FXHqi984Ke_z4sbrPW-S8OOnto1R0lqCZzB9t8Pta_ZT0zf-7lnFx3TEN8de2CCgvNyRbkupAthZdoZ-hx1Wy1mAAfHumVCWJSb7QEMSlW40h--S-Ilji54uI-BZ-fIW7Z7xSAzbhBgsDiKfsg7fw_mhzPp0Al5UcRjOw6iBHYoUmMrSYJR-oLew6BAim4RdAprmQ-Ogm8NxJR8Uv7klA1Y235Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeB6pturvu9NIQXoE1PdaNGxY6ubnxtjtANAYSP8AjdqcC3_TB9KklrmF36dlchNvn98wuiFCoQFqj4_dUibrDzg0y8df0XmFvx8gxa1a6tCXeV4McZGj83DjyQJKJHvyJfngjlBKrl0rfLHFJGC-GAujc12PznbA6t-kmZnpgTdfuS3quHeUCbNP692rTaQOqPkJUsB3nQ0grsBTlC56dWVTBZ_gB_pheePCWZ84JxS71IXy4Hy-RSaqnY4QDILnPI_oA_kmDniOriipAeQRB7znai7INi_JlsjJrdvYF9B979nWpKrHl_hbvC3XaZZcH_Nuvy434arFLBBjbHaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PElAdddbKzfQSagDXjsSu_C6VEss_Ew-SwK1YaGOsyQOzkYaL29i33JA-4nZeqXhqVyE40F7a67jDq5j7Kl4gzxO5235eGkPGTZFH_4_Q7-X9OGEM1cfxW7OMJj99H6l1-rnWx7_Xyr31PkmLXxKFREwIRUUmcaPfsm8Uo0Cs0_PmNDmHbQPX_dOUSUOdC5nx-_vLgbK4LJjBnyppeAvRJn_qzDBlkgDnMOq_OVv9QXXuyfn_ZLjYr2DIbW-zlp7cE0fcOYpjQUWMOeMz3p0s1Q02bV9O8haJ1cmYUAJYE_DfTsW4GUVVbw-O2fV1xfEGwdynGqZfiv259j-DkcwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzYUpLC7m3KzcVk8jq9RcIF3zTSv3xRZ8Rk1k9a20wXDWSu9PklHT-_npYghP8cS0seT9S5hnlPuJHv0hpjVua98O5j7GfCESjtfrZEOtUn_uFr6Q_vsDvtzV4dEAKN8lIk-AowMWPr7fETsJjMTZeyocyYqPDmnx0Zi0SjzAsyJGLoCQ5e4jhvabUxRJf8cI4rXsu57TeED1Hp8h9x372aQoikXg4UNGNNfCcRMKagGEb0HiMuDACSygoZ8pITZiRZrSzPzMeE7Sihad9yMXwiMTOguyjyGMyvQ4y8OSkmSGC_macQu-7yMr2xcm2O0J_VecIvYoVjt_rRRbCqdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD10HgH2nUDP-AIsWEsO9H6wdsc5tulr4g9i_sxCmLZyynSaIl9zclZ6btcgPeNBRXwxmvolAsFb1ohH6RYn_TFRantXivSs8gzfiid6qnzpWSEPXAHFlqFN19IjS5NDxG3O0VCj2SPNXG1V1HtEa0j0cFy6bzVGzu_3dnhg0kvHfzcvtliKVanarfp1h_qIU-0uUsg03bTfU_IcWqooN2cqUnb4TM9-dge8SGnnvijA-zPH3SjjRg3JE0pnrXhIromKYApLrrUBAGEdZWoyWD--93kKvtjgcbdyJrtVGK2D05Bo2XNgzy5ERp9UKaqwwHixGDuavyz7gWFJZtW54A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWZ7k2wh_DAiBcg1BNV1Q60iQ0WktxJ7OAy8hy3FcpC_nbwxzwmEIm1WKbQd1hioNGG4iXtdvMpNUpo6O5FdQtZ_hpB13CDW7RitaSXYZnoDYzj25OmZo2YuenlapN-QkGa5g8lKRvtxrMmWLZWIUWJ4djO2EfioWJ7h6uIAnCtheUHievcAv_peft3qxZSC_8TwlcES9iJRv-N-KYAXKreayCs_lM7-McI596gPflpUUklDFMPzSNvQLk7uPW9kWx5xDkaQPMTtZT9aAISNvTYpafFZX5zye1XopzuJQVqaXmJvDDsTeKiv7VZJsv1q0QLFJf_lyXd4_egl5jSdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGxAgSflPz4eOoO5Sb-gTZ5a1cQX8p2U1VOwU-NDEImBE_3XKvM0yekXtWlyh90oFcoh4aVsRjCWVdw_cz0Pj2I3glr4ehkgFgJ7Z9jFdkz6XIEfOpATW13JGI4dCUXy6ivmlwuus5SUJIq3xeQHN-oGiFimZedC9PMcz7zXNa0b2ULIfTevcLyMxJQj5zKBZsakRVsCJ3YZKSnRyoPTLz4swuqM8KUJBsOVRMoHnb0tHQoQOibLmrZjd3TMC2mTvQV417uykrsspoeMUtV77dVTFyopmPY4XMiJj4638_Lsva_0_cEpHaNTd44vM6odYyoM7ysgGk8Cx4tt82ZtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIYnCsiGIE4DMw6wjGdAPF_JAbfQ-tD_5RCdDN3tjooReI1SRWLkCDdoGTUMrSy-anGI-Jac0wDGlORkKcbF6kV2yimG4BPWcQlUgg7VaODpjsnjCBA4RGyvAe2RmOog7DGXhsj6Lnemc8izaan1Fn1qfIau3U86wYeYolWgmyhlUd8AwkZ57PjQ29GjgzO1ssv9yUQzrwFWtGN__WvGWxhzCbkU7Ycwc87NPJ_5NwuU6Jrv5q3ikkBCCI6G-nBB24p4aKmt5snb6B_7UD4bioJQ2NJ7C3eUsNQW4WqiVRhHmldvCZZ3vsFsAC07OqTl50AUxNeX814QdchOQ-aAag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Kbht5dMWA74xjY-V995wrfsuGHoK7smrMVtAkevZFvruv5xKSnhUf3-V4jJLbrtw65iu48nK5YqJ2TrdqzQGe_TjFognrRblJjn-xAKm7PBf4HOzAZiAsTvvHacmfvgmuPDt2o9y9W-8csmdcdqa33tugfEDfhXI2Ca0lIj9DlrYqKwDOX-6tZlMyxiKDKB2ELk3YZup4eGWp0btvPrw1pCLalpdy-XfcrM9NwkNYDXzhQ6JgPrc3k-gvU2hrQ0zgcsExToKizu46Zga14xCxBlKaQmm9LVxvLIxv7eADYm1IA4mljeJaHeW3Pps5gMNDA8zDjJTOlVC3ROuQsPuGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Kbht5dMWA74xjY-V995wrfsuGHoK7smrMVtAkevZFvruv5xKSnhUf3-V4jJLbrtw65iu48nK5YqJ2TrdqzQGe_TjFognrRblJjn-xAKm7PBf4HOzAZiAsTvvHacmfvgmuPDt2o9y9W-8csmdcdqa33tugfEDfhXI2Ca0lIj9DlrYqKwDOX-6tZlMyxiKDKB2ELk3YZup4eGWp0btvPrw1pCLalpdy-XfcrM9NwkNYDXzhQ6JgPrc3k-gvU2hrQ0zgcsExToKizu46Zga14xCxBlKaQmm9LVxvLIxv7eADYm1IA4mljeJaHeW3Pps5gMNDA8zDjJTOlVC3ROuQsPuGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJNyR5ND2_NGhtBAc_8kl86miZkr6uSumJXp555JR_jLBEsPlk3fFEg4b8hI7-TSpZPAcaJkEOAckxqSf8LJ3IcmkYxq2pUZX_DOQrXUtW4x8cH000oqUAVLEiaVGrC7EgyaJm1Bgpx_RXUGBhcSeVg9xOFgH-QYyRX0IlF-twFeatS3nINot_fu9qJO6xuCtPFff6imXmh0Zcer7FpoKfERhWVHYnpt_fFeVxiyimLYzPqaGQYZYb4P1IO3yavgJuYchSMjNiwcwusEPBVkNzC377SUWhsQtqjUXz0-IG5bij8EBLlf3M8sV6MGrevMH3OVkNoJIcDb8Vd0tuXG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N76ocqeHXrspdZ6usJRyNU1FZhmlQrYWoiqgf5foLdcJXHe-9wkAvccBefvY5KQ3IIXHYxpXGmrjR-6-ANbERJc2tTX2vgfyKCAsIUcEjUD7q5O-rgxmoz1nq4XbH_UKeXkhbwXE_nqMHIsadYA0I7U9oJ0jhw4UHy6R3l2_oNu_HhzGmhv4h2-OIHQLm9InRB6XvQ7pZT71S_d2NnuNHMWguuWnz-0pnwTT_3XcdtnPL-8L913kwMl3r1LWkVWLSVef7ClmwgDf62giMwWsI-BJYDA6ViVUn7bpM4LqEbLyYNIF_hpcMj6p-4yXVLm2CjxbupxD0j37txox-rPHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ebM2YPdJiBH_xHlGotNjKQE4CLDGP1mV8dprq33kSS9hI49zKQHtMG3V8d5LweDiGOPxAC7MXnLPu1RK4TnCaugIGBQgib2TzLqdCmAQVMwwldnbmueKr9nksvjkxgHfxpCuUojEKuvhgGc-ffuExGwCA34SAZNLT4SzHwyNtUrezaf0ez_ZsRDycYd-8yP7rf2rpDhmGG-kmUK7n3ncJLSQHANG4Y7V5vS_7ivTcU6WyiV86Te1WTzUBvVgrkqy82LhwB7vwP0EWGFyRGX-M9L1qlX5b-z6GbbZlaiIJADrQYvNxfK5DufYHxUiDAsXuuOJRxPto18gUeMFnXMrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ebM2YPdJiBH_xHlGotNjKQE4CLDGP1mV8dprq33kSS9hI49zKQHtMG3V8d5LweDiGOPxAC7MXnLPu1RK4TnCaugIGBQgib2TzLqdCmAQVMwwldnbmueKr9nksvjkxgHfxpCuUojEKuvhgGc-ffuExGwCA34SAZNLT4SzHwyNtUrezaf0ez_ZsRDycYd-8yP7rf2rpDhmGG-kmUK7n3ncJLSQHANG4Y7V5vS_7ivTcU6WyiV86Te1WTzUBvVgrkqy82LhwB7vwP0EWGFyRGX-M9L1qlX5b-z6GbbZlaiIJADrQYvNxfK5DufYHxUiDAsXuuOJRxPto18gUeMFnXMrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=vZ_7NYmSCp3xQTFlfx8pQwJ60DKqF7IUCp6gdQyBgzsXMINUzd95jkN4_An2OnwqGOgdRrFz_sR75om5eQKhG4YWMeC46hm31xvlHWVbJpjoqtM_Fnxj_zxCSl3B5fyWeNqmFMgx2hNirQiTYkpqqeIFNLDKbPJplSQE2BAfilsAa0rpQdc9UBZo9n7JM5BXKJNMZrwP27VMvmZHQ63p_wZ6MH4IktxL0--VjegC0kIU3vaIV8Kx8hc_UPFvwUoYelUHrkDlIN2FqPtTtz7eeIoYXagY-2cjtKqPavQ1IwulY28SLMOpfR5ovMC1V0wEA1kTWuLr-BVFBlusEkjqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=vZ_7NYmSCp3xQTFlfx8pQwJ60DKqF7IUCp6gdQyBgzsXMINUzd95jkN4_An2OnwqGOgdRrFz_sR75om5eQKhG4YWMeC46hm31xvlHWVbJpjoqtM_Fnxj_zxCSl3B5fyWeNqmFMgx2hNirQiTYkpqqeIFNLDKbPJplSQE2BAfilsAa0rpQdc9UBZo9n7JM5BXKJNMZrwP27VMvmZHQ63p_wZ6MH4IktxL0--VjegC0kIU3vaIV8Kx8hc_UPFvwUoYelUHrkDlIN2FqPtTtz7eeIoYXagY-2cjtKqPavQ1IwulY28SLMOpfR5ovMC1V0wEA1kTWuLr-BVFBlusEkjqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4T4Cadqi3AoCC0rmSQKb55bL_pitHapFifNsNIXp0t3ftEaON9bisqz5o2Dyo8rT1zqbY48Pq2rLCAeAYhW_9aUflQlDnGiOCV6DLzyCyLDMdNxfdayn6FH7o8AhrDrWKEemazOw9QSLlOtXNQoeXIsw0IAz1j1xOvRx5ts6GYfSc_ZpEZ_ZWadY94VjIdusi_b42MMBFroSZGxwLyMwrVxPBIJ_v74NaTV4pZSxpZbu90Q3ohaTayipLoLUkAmJ6Iqc1uQFS7R11fb86Sr_XEGlgtpgrAPxo4kYMvkTisGzOS9mPjZujQpVLTjAlWwSSrIoORkUo5Lz2PN8FAbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De5Ljs8WSGTPCe7PdQz_DzNDh8uBNPLVFHIXM8EXfUUX3xcwPYcMzhwt0EcVmlc5MqqEk3nT8UAOhgLwg6X_ZuqhnbgiQy4QlgB4ozlFV-c3NQd3F9XngxBHmcYvdsva8OCNW4gbdpiiPcx7GyiCXHQk8TthEefGBnrsrWPiB2Qci4y2b1ycfMPx0JpwuYYrQnzuvorQJP7EH3FwiKEGChQtGU0hHgW7zL9isQZnj7ZKPh1THn_THf1KVyrvmrY2-VPhfz0N8-7GuwM32fkwnbFWqhU22oaJaCwC8vqvv-G9fvYBVJ97RwdFOtSHRnu9AYotGbUA1hXc9EyKFHyiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glNdiNmqy7knDyoY6o7vzmUirVetl1S--niBY69m4IsuP7HyZMQNomN53SyPkll9WkE0GDFTJ6QE9Em8yzBKquKxEMBy62SmAyAvZIx6igdJRhmsPoCabvioeGOPLoR_-O_m-hsZKnYPDYb5xx2FaBRULOLbhTb7RRzRi2SYB9qgoWGkHPf47NiZYPSjje7_Hb6xKO7gzpxai0u_uzoLTdyAxO8IDypBrL9gSobUjp3rgWbqn26fGYH1vpm-xp6gCAxCFSYu2F8chw7V6Kf5zQysl30YzM_CT_NQ0-jjiGECKyY4AmmMIl7JjRPuhMZurKLy04xtr4qiZ1NzmbnBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmjSUveO1ib6GyJslU8F4R-yEfrXDh9yF4gZ0kkUP76Skh2QBufbrRluS1BDWbrOyR-mgyFPZtrtj7nMYUYpcgPS0zFwgFXaFIDxE5DR09x2tftmt8OZSfpEKwUd6oc0f-k257w8OhvRDtC6k7Ig4hA_qnSFPpOoGbqmfPpSJ__zYkKMlNjp9il8OzMQj2_tj743V0Du_cXi76IEkIkeZJ-CoZicXTAzTQ5-lJ05calvDfZX_BfggkFDb2ecsfGlAG1jOktz_k9tFFtUbLSdpkR_K6TOP---on5UKYl6ga8UpWO4o52ACmYtq69xz2pX0sHWgdaugfQowZynW8bU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPg5BydQgDy2GI8osAIaYDDt_gN16eJu-Y2SqrNhvyXe-z03o04NjYBkGN7DW0fWWoJdzXiLgrTlgqTT9BnfxzF4n_lBeMAcKfsD2XfcVHOE6XqkOrswG9rNBhgluZx1RPUE8jO8cF2RHEZP-sNahhHtCvXswNvRWyhoAI1ahkLfI4Ed07px0IK-Fcu_rYWR0sM2A66MrpeIPrFbZZMa-wfXjcdVfa4w5t1OSsMDi5qLXkw_YBKdQDfNATFh7BW0ZnpbnH0FVIjSqri3ATkcRhEEgBVTxkc2gO03_EuYCZKCPnX7I1tdkOFNVsmVdSPGxZ31JxsoECKpEpV68HanXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vkk188QKo2xI0-IPFPNhCNyp3q2P-qzvNA5qRbKiYoEiRsu-nKvBdZDhEs8jSgeFZqAKHPRiH4QydcR-7NKsp0TsPrRh9zTI55z-uuZ3npg5kGsrwQNn5-JADv8GttkV8Fqns50bYX1UV3sim5WV_dD07elqsKEHY3yhKT0S5fxw4mD42MDBzsRvz_AVKWaxoSp7eTMS8GYjcVrP9gGfetOqKkxIuBbNZOErH5vPMk0emwtj3pDcEQeJhc7d8tjzxnYlp6Nd-ZV2m72cK2VF9yi-z1w5WIuv6isWR_VDunATQXr_WA9H4W_WHt0AoGgThroOrM3LlU9AqkKrc9lKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
