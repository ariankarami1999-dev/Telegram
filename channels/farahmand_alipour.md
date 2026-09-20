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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc-xv30h4RzEXN-kemBCnM_lTiz7OrVmECVyTAJZYrENACKbFlws6BpIZwkMcdqImWB2oLOUd5kvZ1k4kf_A8yx3AF0owcG1gyldXAwTb6Gb7g8inKintNZFzY7nRdo54qgBSR4aSPCvU12z4Ga7-fOMasgMA8Egtx0hEjPxF1Tjhb66DItayItxyv6i6mHszZP4RhGORZ42kAcrR023UROBZDXeyQz-fhPzTXCtFsCZEDxcc16Mkf2aGiY7Q9uK7ECIldXt2OQVQARRuJiV_zx-64Y2lqN9U0HBgz4RfopNBLfat46HwYj0KwxSiDE3et9IO9K3IsMqGjGUhT8tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gr1NdhZ9qoo2OW83qMM0qw63xhY2NVXYwGjGOcjIhuQxi3gwn5qhJzjbT08AfwafjGz8GT-slbpSLBWugnbxKqdwBldBDs2gkA7I5RRvbx_pynfIm1LHXnTh07mWUWTM5dFZEpAwIHxQyXcn1Cy1LIODYPiLedDj7Xb7hWJ8AJ4XeF_mnpj2z3DNYW9jd3srbXQDWeMh6CtsIIncnn2bYdOxC9_nwUqTWEyK1sDETp52gIqgKCZ813OHszMdoP5GI1AByiYkIIohuuLqRFxPzB90dIbBgRy2QnBr0OHHAW47GyOp-pJ9DxsZJEYQbXK9QJjU_lmTe9rksOe9W62-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gr1NdhZ9qoo2OW83qMM0qw63xhY2NVXYwGjGOcjIhuQxi3gwn5qhJzjbT08AfwafjGz8GT-slbpSLBWugnbxKqdwBldBDs2gkA7I5RRvbx_pynfIm1LHXnTh07mWUWTM5dFZEpAwIHxQyXcn1Cy1LIODYPiLedDj7Xb7hWJ8AJ4XeF_mnpj2z3DNYW9jd3srbXQDWeMh6CtsIIncnn2bYdOxC9_nwUqTWEyK1sDETp52gIqgKCZ813OHszMdoP5GI1AByiYkIIohuuLqRFxPzB90dIbBgRy2QnBr0OHHAW47GyOp-pJ9DxsZJEYQbXK9QJjU_lmTe9rksOe9W62-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrMq9Wzesq4_4qIkok0LNTAIB14CQSEIakyKX21gkiy6QjZabNqYmzz6EIYXEgVCzWSQ8i5gpnW6ttH98nPNBUNBgQChSJjPzrhx6TXqWxmPt1cEh9BlqIePYj5Hf1_vAlo-D7T0tuRgp5OxkHKi6Rc0IKl_gbnE4XOzHDyqskGJtOu3LNnwcP0MCBdNp4e2BoHVcWodBS5jOI_pOAwce-lvYG9NU5KivSYnZoizgHdfGgGf49ediMcszAmMT1snuVzRtn3w5W8F1plyjZcJgRs6q5SxOyXZKV8rwvE05KtdGrI9Be4cRL77BtfqRV34BhjixmtFO25_XCCth9WUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=l2jQvmbDJBQlNa1OwpLS5cU_bJUxNbHO4Iv535ylGb8pJyM1TTdMn1tArP8y70CVXPLGHhr8Qa5rsbforvn2h5UMEqUBswK033ez4ZCJUWp3jBmQqbEWvcQj5OnAr809fmqAuesvD8Ao9WwHjp1j9QRRV15INQTlEQjKWeMHmeZ_KcUJcaK4O5wTgujU8b9jx-Irn7-DacBzA4PXnYecV7_RSe5853BZR-x6esz_dnXWfI0q8UPApCuKXI0QmiPuZeqy5ChdopKCM5tyDif9F6n5jqrBo0A5t4J7rwPAmxPtkBBwFkIcpQzd2Npyqr3t5q1O3sMkYmSqfnu-EbjRyl8BbFOObA5rw1tCNCJbdWZxmz6lnnQ_YR0hlyEByg58BxMHvh8wu0iab10m8PH32lOoBS7R9Sp9xByfYu9DCZXMn60GacrdwHBCDm5lJz2d_Zf-CMubfM73jp-cbUpOcjeDSmmDqt9zAkLp9tRae0WP-q5OhtG0iU3wD7N8KXLuSQ4H9JkOfp5GsCkv1mdwita-9-PZLh07nC5DgAFrwOGrtUsP7oPRBu0LWJPUcmPDwPkaqSJDyb1E1L-8CIVvagM5OYHbCYJC5qoztNj-0GIx_ztvzPiAwh-RWcn30ScDdnC9W5iwqwkgrBxT1-_ioQfFVPUBSIUiU3c7TjhhSTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=l2jQvmbDJBQlNa1OwpLS5cU_bJUxNbHO4Iv535ylGb8pJyM1TTdMn1tArP8y70CVXPLGHhr8Qa5rsbforvn2h5UMEqUBswK033ez4ZCJUWp3jBmQqbEWvcQj5OnAr809fmqAuesvD8Ao9WwHjp1j9QRRV15INQTlEQjKWeMHmeZ_KcUJcaK4O5wTgujU8b9jx-Irn7-DacBzA4PXnYecV7_RSe5853BZR-x6esz_dnXWfI0q8UPApCuKXI0QmiPuZeqy5ChdopKCM5tyDif9F6n5jqrBo0A5t4J7rwPAmxPtkBBwFkIcpQzd2Npyqr3t5q1O3sMkYmSqfnu-EbjRyl8BbFOObA5rw1tCNCJbdWZxmz6lnnQ_YR0hlyEByg58BxMHvh8wu0iab10m8PH32lOoBS7R9Sp9xByfYu9DCZXMn60GacrdwHBCDm5lJz2d_Zf-CMubfM73jp-cbUpOcjeDSmmDqt9zAkLp9tRae0WP-q5OhtG0iU3wD7N8KXLuSQ4H9JkOfp5GsCkv1mdwita-9-PZLh07nC5DgAFrwOGrtUsP7oPRBu0LWJPUcmPDwPkaqSJDyb1E1L-8CIVvagM5OYHbCYJC5qoztNj-0GIx_ztvzPiAwh-RWcn30ScDdnC9W5iwqwkgrBxT1-_ioQfFVPUBSIUiU3c7TjhhSTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=KlmCR4DBDyHqws_AdCli2bhNqi-cB7zcQIETnYdXyQOONbC78_kQhH0__WKK2VwW36Ar8Y88exWXWoxJcwNMuXAzcPQNBux1U6OJ0QRzU9mymjW5U40DlItvxIOnoomkQFiVVaC4ha6yT1ARL_Loj-kn1g_v6K0tDF3CuDrRI3JlCr0pnHNyK7ovHsyrw_z9D92i20HgR0MOuLj5VtB8qfhCkeEzadSzqWYWLnmXbSOREgz3u8G3vd7Pp8Vafj5xCVhjthRszYn_mi8GtPp5P9ZqFP8-M-uGv9VHM_WJGgCTJZOHeNpwBztb5mtubpw9f1adVRf9qlBQH-_YjbKUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=KlmCR4DBDyHqws_AdCli2bhNqi-cB7zcQIETnYdXyQOONbC78_kQhH0__WKK2VwW36Ar8Y88exWXWoxJcwNMuXAzcPQNBux1U6OJ0QRzU9mymjW5U40DlItvxIOnoomkQFiVVaC4ha6yT1ARL_Loj-kn1g_v6K0tDF3CuDrRI3JlCr0pnHNyK7ovHsyrw_z9D92i20HgR0MOuLj5VtB8qfhCkeEzadSzqWYWLnmXbSOREgz3u8G3vd7Pp8Vafj5xCVhjthRszYn_mi8GtPp5P9ZqFP8-M-uGv9VHM_WJGgCTJZOHeNpwBztb5mtubpw9f1adVRf9qlBQH-_YjbKUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ktOz-ivEjARKzIhjEikGyQgqsgEyCdW3InRpcux68fv85nCkUVy3yg7hhlrfAsbG_YSxx6FTsxwqsibwLdCnFyzFPM06NroqKyarkC4wffrRoP-TfaLqrGU2pwAnuZJPeu6xWifuREXungP6D8SSv2id0Sc55ipM7urrNT_y30EN_ycf3Qmuq24Ov3V9xKXXWnsuzM_xXcCVgHBXAFiUTIGafKOrXh26j_DIgRvsvzFMEz-drCaJoLxPxn3jzogaNNuZVLbcD-sljrbfa8Cf8h87TAqFr4raGX0r038PDVqwXr4SDdtP-nEmQPXQDdokO0fU1cAztFav4Q-SaZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJllLWqGcfN7Cq1cBHIoVVC8-HFT4o0dQEABs_V_LDKdEWjve0OjyWc603JbH4fyuoFSmh_Ieiy7Pe5ZlwfgD5d9INQpOxAryvAcAA2uAt3QWnw365JnejRgdj7ync2_eXT35Fh1sdwwH6jaPvvj47jouLA_hRNoAZVB85pKvhGKXaCb5TKJxhFYJHFvMSGb77jmD_-RuUDVh_hh-tNCzEypgrR2K-nb0KO8fzqQmR1XYCuH1V7Mhb2T7LpD_BOGW8TBvecVRHMn01hbYBoh8yR1ZcsqQdhwh-YYyIHTxXIExd6aMuAzx8EsH3WQgfzZTIe5X_VSTKbSeKSxejqWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRen3YIZczMjoZKUMZfD0VYilxG_2jkAL9hsevgRE5soBwEn14A-rdwS4g7EVMhlUxMWsH-PS4ppvaI3c0xDEBoyeR-NDX-YSUvs5zDs1SZSqQts7xXckNZyl5SBAyn55Tas_hrpnVBIVpLD9F5nBT7uwREa11cezX8Yc-4vo_BxM7WEObCgy0Qay7VSXU6TiuQK9-ylvFkbdEzvO61h6p19xrQWgODiRoRxupUmdBwBfqOrB2Enci7C4e81e7nE_h1_rzswg5KVnstN391vBvS40r5eLIcXR8Ag2k4owluAa5yHX2whvQaBId8Roa-nDwI2TxZbLtGNh2ko08dqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnF9zx8bpbTSGZxaQgyRVW3ApJgIi5nDs00GtPz6dQRjUEYRLctTArX4dTDWDEzeADgTCgLuGFWS__KKlFAwTGgP8U3tSPIr2PzTMd-qzxVotz7vggJrbFKieD1KQhPRcsS2_DhZG3XbHbF5nME10R6vYFf6fd9CLNiqtn_TI10glwGpxKBdKFVafSzTzHVCX8Yso7Fa2MV_Z0b6n3rfYeGfWL5w-pBSAbGikHPHJpX-rFa4q3TT7UAH_4kQBTB7G4NuvSYekie119A0S-T78TgX8h8f86bwQPJ-xodduC0IZBXDTvEU42kftnQHRM8M8n68PL-JlnOnynUGftQJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2Ig1O0t1ISVkkbLCKqsB6lTE7uiqptktOdY13j7jkSvuNcDslO5Ad03jDxaW3guFGaZ1QLI_a4XTA9w6tLKI1iOcKYWs6bHqvQCX1mWhhkYntDPq-xltYzul91uhu2VmIuy1UI22HKoy8QKK_3odTbNShmaGgrvldRtFISJyjIYLWH0J2fQuaxhSRtwneJHBg51DfPWhudGp3UJuUtD1OEFqCxAz2AgP4OSlR78Vrt_hf2rSvNo37Veb6CAb4vEHF347WsH4BWQTppgkcCLkLnN-z5NUh8VxOF-orREhvU0weZL_5YNLRshL2TRZhUDjcAVgMHQ7hHCK2maVIBpnHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2Ig1O0t1ISVkkbLCKqsB6lTE7uiqptktOdY13j7jkSvuNcDslO5Ad03jDxaW3guFGaZ1QLI_a4XTA9w6tLKI1iOcKYWs6bHqvQCX1mWhhkYntDPq-xltYzul91uhu2VmIuy1UI22HKoy8QKK_3odTbNShmaGgrvldRtFISJyjIYLWH0J2fQuaxhSRtwneJHBg51DfPWhudGp3UJuUtD1OEFqCxAz2AgP4OSlR78Vrt_hf2rSvNo37Veb6CAb4vEHF347WsH4BWQTppgkcCLkLnN-z5NUh8VxOF-orREhvU0weZL_5YNLRshL2TRZhUDjcAVgMHQ7hHCK2maVIBpnHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6o5hNVxv16PXfsJ97SxVnL9HOk0m17X3q8xEaOQ7kFwZig6eM7L_95t3xMWG_L3AdtTmrLA3IqTEdmxUlueMPpgLyh8NobOqb5zf-zZWAioDwcz8otYxvFO0PEef8PZBCVDqH8GnWy2kpGSeXWtfi6KHUr2NW6BjDWm0OVK-cKq1kyZ1bovMwMFFrHRcXWsBjBGpCiA3A5aOb14LKyocGToNTgK6ZU5vM4nlKfOjdvXIF3GjRc35ypu9keTo5fAoqdzPCn_-suPCJNdMxkvJE56A7v238-QdzqMaGPV2dYOsq8Z6xZjhDFtahzcvDxG9oq5sK1_6UccH6-YHS2k-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6o5hNVxv16PXfsJ97SxVnL9HOk0m17X3q8xEaOQ7kFwZig6eM7L_95t3xMWG_L3AdtTmrLA3IqTEdmxUlueMPpgLyh8NobOqb5zf-zZWAioDwcz8otYxvFO0PEef8PZBCVDqH8GnWy2kpGSeXWtfi6KHUr2NW6BjDWm0OVK-cKq1kyZ1bovMwMFFrHRcXWsBjBGpCiA3A5aOb14LKyocGToNTgK6ZU5vM4nlKfOjdvXIF3GjRc35ypu9keTo5fAoqdzPCn_-suPCJNdMxkvJE56A7v238-QdzqMaGPV2dYOsq8Z6xZjhDFtahzcvDxG9oq5sK1_6UccH6-YHS2k-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=HdzkjcsON1CdlOUf5kT_8VxIOPks2Ny0_luJ6TykhFzDOaJGgkEV-zuLFsn3BEeLj4wD9BRjmUX_AZp6TBZ4IJ7PBSCPB-BD3i5FKZZkOaBRI7t4CmW_YSyOTj0rAKfCqH7zAe19lHSMRm-cgYmQp9aPupkPmP6HdFEaMb336EwIsWNuFJ3CrpWLDmwXZlnTabrwsSf1cqUGBMxJec0gNekC791I8Qal7wRASIPA4Jd7SVz-ERWmZauqGKEXwJML6KmgPkBDquGHeLXGxeF1RgawrpXP1uCE0uTSUCQvTdqNduCasIUozwNHYAdSCkxfSAGwyON-kwDiy9pmQLr0oQK0DGz8x-UHWx7agGRAjGq4JegBrmZ_iop1Dlj9FFEErhPkbmcrLL8sltp04lkUrfGifKGbWJwgCPMvtb95T0ckGX2hx4BT4I4eyZvGESDCRjOIjUy3jmu_seMRPUMAIy3OsSs7Y5e8CqumWMMM0uLjUjNxgbQOhaiBY2CWQpIw0Z1JSzEa5KTYlqJ1VCZZySvgTPyDfWQSeoCnK3ZFR3xH5_6LXov13F_MhMvk5vs2F4flEDAcWx0PxQmsVA02ecdZ2UO3lj87h6T36iyM639q_fRGU-kRS6rErC0FRKa02wEr9dbGtiVMfVTUq15-ayrrggvPHJhXcr60X-XVUso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=HdzkjcsON1CdlOUf5kT_8VxIOPks2Ny0_luJ6TykhFzDOaJGgkEV-zuLFsn3BEeLj4wD9BRjmUX_AZp6TBZ4IJ7PBSCPB-BD3i5FKZZkOaBRI7t4CmW_YSyOTj0rAKfCqH7zAe19lHSMRm-cgYmQp9aPupkPmP6HdFEaMb336EwIsWNuFJ3CrpWLDmwXZlnTabrwsSf1cqUGBMxJec0gNekC791I8Qal7wRASIPA4Jd7SVz-ERWmZauqGKEXwJML6KmgPkBDquGHeLXGxeF1RgawrpXP1uCE0uTSUCQvTdqNduCasIUozwNHYAdSCkxfSAGwyON-kwDiy9pmQLr0oQK0DGz8x-UHWx7agGRAjGq4JegBrmZ_iop1Dlj9FFEErhPkbmcrLL8sltp04lkUrfGifKGbWJwgCPMvtb95T0ckGX2hx4BT4I4eyZvGESDCRjOIjUy3jmu_seMRPUMAIy3OsSs7Y5e8CqumWMMM0uLjUjNxgbQOhaiBY2CWQpIw0Z1JSzEa5KTYlqJ1VCZZySvgTPyDfWQSeoCnK3ZFR3xH5_6LXov13F_MhMvk5vs2F4flEDAcWx0PxQmsVA02ecdZ2UO3lj87h6T36iyM639q_fRGU-kRS6rErC0FRKa02wEr9dbGtiVMfVTUq15-ayrrggvPHJhXcr60X-XVUso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=sn4riaP0h1N4ZQMatEbc14Sql3f4_sxyBBx6ChYRc-wpioIOWFcEQ5_TDnxPYZDpFAQfvb99JVAOH_wMhB0mrGyWGSFIpGhBMmnsGh1xy25QKrtReFmGkrZiC4paSeewKPwBxzywNl59Ul_efMnsG8nqcUR5eGHhZbFBimRJsNelcgJNW8urkJ_7sL8ENPHeA7LxWV-DOHkN0fH0NduGmD2rbMlwK4CJiXumQenSKrRR8dRZTgt1FfpUymecrjqq7BMzHeG7MhbVPGGlHYpCb_5WKetwujOGHslFfp4SfRd2_0hq_8rJDcxfFMO6rZZHdYGYvETPoP32DZMtPXsWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=sn4riaP0h1N4ZQMatEbc14Sql3f4_sxyBBx6ChYRc-wpioIOWFcEQ5_TDnxPYZDpFAQfvb99JVAOH_wMhB0mrGyWGSFIpGhBMmnsGh1xy25QKrtReFmGkrZiC4paSeewKPwBxzywNl59Ul_efMnsG8nqcUR5eGHhZbFBimRJsNelcgJNW8urkJ_7sL8ENPHeA7LxWV-DOHkN0fH0NduGmD2rbMlwK4CJiXumQenSKrRR8dRZTgt1FfpUymecrjqq7BMzHeG7MhbVPGGlHYpCb_5WKetwujOGHslFfp4SfRd2_0hq_8rJDcxfFMO6rZZHdYGYvETPoP32DZMtPXsWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsrcp7BtBt5-bH9CMi5op1UlUJWUuldU0jZ8Gt2aoNe3FUyeyyCDyje6ahuAZMQ1OT9Mh8foftqcKiYeCG-3W_ucoQ3167A8m5yPHS6NmE1GsaN3DC_gSBC5qK1SNek61H_YMT0xzVpO8MJhf45Z0Mq1JEUjdlce7qTQRFiHt6zoceCgw0mPQ-HJOlSllhktuN5JzFFl0aEcIjuR8t-fVODBPHTBFmrmI2dxvk2TXS39ESz11pAYAJetIuCE5AW3Ugf_zoPIf_sQWXfYKUAfTszoaN0aBkJLPmsBIoYk-M7t7YvoyKJwg08XqsOIUkRtoHvDh2hQbcCkJUd3LAML8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=H8x96vli8GbxMwrcW3ddYC3pK_UTToCMLTwThanA2KT9lVJw-17UJRR0xWCgXcIDJwH66sEAGQDdIFO6A89rWqnzQn8mIfT893DAi5WJFojEKQSCizqk_JeOTqZxJyFojNriZpd4axD7k9YgfQCJtErSihePGSp8UBeB9TM5p0FLC-hNi-47h9KF2k2Vdg-5-HFao3UZw5jkvxvK7UejpUygKoZ-8h9flWWC4LpZ4eO2UkK-XpmAzHpdxKlTRgqqAlkKOTx_xwuYmlv1LaNnO4yRtT76IKU5MWD19fAzE3qu_onJc5ZaevkCIr1Q9D_uUNZqLmZLlAyRGg5KFAy_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=H8x96vli8GbxMwrcW3ddYC3pK_UTToCMLTwThanA2KT9lVJw-17UJRR0xWCgXcIDJwH66sEAGQDdIFO6A89rWqnzQn8mIfT893DAi5WJFojEKQSCizqk_JeOTqZxJyFojNriZpd4axD7k9YgfQCJtErSihePGSp8UBeB9TM5p0FLC-hNi-47h9KF2k2Vdg-5-HFao3UZw5jkvxvK7UejpUygKoZ-8h9flWWC4LpZ4eO2UkK-XpmAzHpdxKlTRgqqAlkKOTx_xwuYmlv1LaNnO4yRtT76IKU5MWD19fAzE3qu_onJc5ZaevkCIr1Q9D_uUNZqLmZLlAyRGg5KFAy_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=izssbVL-K6LXiIRSzpCzK7mK1yZ390LjhuIa6uTJwyTX9uSEF48sgpnGTyQKoj3Dj7XXN-5nbxRWthlttFCV_LhaxWThTnuGeNnXkrA6MPyd46XrjkoScKUvLsZo6438kXi_FLwQxtQOhPI7rUmAu5UaSh6x_sNZcktld1lOPslKKEYPCOmXbhNuSpD9zpvJmQgReLtfuYKmiU72zZfAZP6I7_ilcTzR2NMI8T3wuQqy2KH8hF97mulyyf4vPJ12rwWE2tAmldYVGC_s031jQhFEM20n8T5XJQ33DWhAK7czos6NKi-q9qUDMwWy0Jnh29GgOBlLJOhezpbGPRoFmBNK5T6K6VDcr0n578Y35nayPiRVugIQlYnWX0c077_IJ1Je7Rotn7_V4gWPQjJSy2xGZ6q0MkHHtoCerAt4yM7MKkm31sg5cg4QNIMceX3WcaYFpM61coUacZMwZaZyPImi5whO8kpRoZlFrwUmEKcKJBqx_BH_tfoVb-Z5jxjcQLAQSfd7yUPcAtQjMGKWCE9dBgCHhcf63mhuEmcW04Abj-rmBQTIzzvhsdKRe85ZgFDGC-nvTvr-uNDARBTs_qhCXXz92Z7FfgaQDJyAQgRyRJL-3OxJxqCKRjrOLdF5QUYvpQfqIpAGI_TLlHLfuRpu-nPKRW7YiZs_fNhuB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=izssbVL-K6LXiIRSzpCzK7mK1yZ390LjhuIa6uTJwyTX9uSEF48sgpnGTyQKoj3Dj7XXN-5nbxRWthlttFCV_LhaxWThTnuGeNnXkrA6MPyd46XrjkoScKUvLsZo6438kXi_FLwQxtQOhPI7rUmAu5UaSh6x_sNZcktld1lOPslKKEYPCOmXbhNuSpD9zpvJmQgReLtfuYKmiU72zZfAZP6I7_ilcTzR2NMI8T3wuQqy2KH8hF97mulyyf4vPJ12rwWE2tAmldYVGC_s031jQhFEM20n8T5XJQ33DWhAK7czos6NKi-q9qUDMwWy0Jnh29GgOBlLJOhezpbGPRoFmBNK5T6K6VDcr0n578Y35nayPiRVugIQlYnWX0c077_IJ1Je7Rotn7_V4gWPQjJSy2xGZ6q0MkHHtoCerAt4yM7MKkm31sg5cg4QNIMceX3WcaYFpM61coUacZMwZaZyPImi5whO8kpRoZlFrwUmEKcKJBqx_BH_tfoVb-Z5jxjcQLAQSfd7yUPcAtQjMGKWCE9dBgCHhcf63mhuEmcW04Abj-rmBQTIzzvhsdKRe85ZgFDGC-nvTvr-uNDARBTs_qhCXXz92Z7FfgaQDJyAQgRyRJL-3OxJxqCKRjrOLdF5QUYvpQfqIpAGI_TLlHLfuRpu-nPKRW7YiZs_fNhuB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX3-F_wEuEO1P8WhPTeO6X_kU3lb44tm11bNOftIgwR8mKjm5tALECYDhfIKTGpBoCfHtcbJ51cVkQKYZmzP05-stdfpc3vn6l9ZBL79nOUOcAWb86kvIignrN6toottqmlIVOyscPxyGvTi0x09xPWZeG2HQjZieIcIpa_dbA7OhEMFnWBZQhi2BGqqTHslCgsFBN_o0WYYpZE9e3ObiyuDbD7QJqapGQYAx9-9zURVZlfEebQOuKqIgLX8DGFCJwyad6xmTT1u7ZY0-gV2VFGZNRfnJUlxzE6mr6nAitIn7hfNL_pJNECYqMbzkFQ1SIchdAs3ly4GNiUSQ_Hl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kGWEr3Kmlh5wKqLj1mvWaFBEufbbDkyMHOFcI8U6_tkMxwziJ3pRwcVMg9luZ2Aa48hlq723gyPEN8fHDspblMNJYjXRGc4P3ALNb2lKwUOxbIcI2vdTaAKFoNM02RiZA452OOWs7JE6ugJKJLpyY7d89SisTH-YvEAxAjFSW1wH99BB5K9rTzHKD9HL-THw_iN1II5Xi3E64rAp3Be6vpdWWqFS55j_wKyO45mZFsgDWELkrDYCNu90DbHVJ4141aTAU1xD9AaEuMIvWdwWmZce2XKtgXLDNWqrPjA8loHm3AFEfmwi0ptUEGfGpTGajKEfGPptBu39Sqt26y9vDJ1SYXw-ujYRiriLHqmnmnn-KS2PQKSDgT-nvf2dDP8pjxaFLev5x9anXgyfBIZK87L1ZlR3n8jdtY6Aj2hl8eXV6ymHjwoB5okGxDG5PrM8boYr4Q696wLBUKPoQROH1qx5W4w3IAjpv2OfqQCXN0sFnsR8PwVOQPtV_EKuV3hkvNTStlHnhYwyBbeqhQcHLGBtfFm-WU6U2z-N__VD24HBeH_ZsmhmjLmmSnqh6bmdWaXjtbVMgCcc6puQAOFTt0SvonxRoOq-nCVsr7k2T9N8MUUYC9v07n2lYxU4x8u5K-agrbYhBX32zmxsCXh7V4q2b5bX3ivZzKiRRTb4kJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=kGWEr3Kmlh5wKqLj1mvWaFBEufbbDkyMHOFcI8U6_tkMxwziJ3pRwcVMg9luZ2Aa48hlq723gyPEN8fHDspblMNJYjXRGc4P3ALNb2lKwUOxbIcI2vdTaAKFoNM02RiZA452OOWs7JE6ugJKJLpyY7d89SisTH-YvEAxAjFSW1wH99BB5K9rTzHKD9HL-THw_iN1II5Xi3E64rAp3Be6vpdWWqFS55j_wKyO45mZFsgDWELkrDYCNu90DbHVJ4141aTAU1xD9AaEuMIvWdwWmZce2XKtgXLDNWqrPjA8loHm3AFEfmwi0ptUEGfGpTGajKEfGPptBu39Sqt26y9vDJ1SYXw-ujYRiriLHqmnmnn-KS2PQKSDgT-nvf2dDP8pjxaFLev5x9anXgyfBIZK87L1ZlR3n8jdtY6Aj2hl8eXV6ymHjwoB5okGxDG5PrM8boYr4Q696wLBUKPoQROH1qx5W4w3IAjpv2OfqQCXN0sFnsR8PwVOQPtV_EKuV3hkvNTStlHnhYwyBbeqhQcHLGBtfFm-WU6U2z-N__VD24HBeH_ZsmhmjLmmSnqh6bmdWaXjtbVMgCcc6puQAOFTt0SvonxRoOq-nCVsr7k2T9N8MUUYC9v07n2lYxU4x8u5K-agrbYhBX32zmxsCXh7V4q2b5bX3ivZzKiRRTb4kJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=QGDDFQusFES8M-kPwrhqt0Cg24IdCfc3-im_b3GCWvlD59ES5yoAgZLT3OSXGVl1V5n8VpenxpCD1rsSfDrsgNIzFYf0J1XdabS-u3wAQFu4KF2_DT4eYv-TZHCxa3PwNZqh8KqeKcWgT6YU3F7Fvlz9h2hopfp0sXxvV-9nuXzfdKpnadbn_i6zjokyDV4hqzlIzwOJdKVNdriIuS74rXwLRCPQtUQZP6Ia-Z9IaUuvdR75obW9FPoi7-fk30iyMMEt4upFpeRwtSeAKhogjrDrKBQWs8uYQGZ0yufKdSyEgjtCuYdWqqZ2RQyQunuzmIzxbMHHdZfU8mRK0K5qBQPM1vpZMzl0GIickhxT7DGs-NFgAUbGHrnWh21DYNqMsg6wYDl1Akooayj_pv26eG0J-P2N1kK3YCy6iAh4u81k7RPagqG7Pe6BZ55mOJP0Ele2D-nkNz2x1I9LWwbf5D8jvNoQuTprvzgdX_PzWNt9mhJW4P7_P4nii0ctg0cPa2-eItGxP6_zhUDtjjbN7S3FZELXMUWs-km_6Yl-Liy_S3M_bZDyKWBtxzsI4qvmTXvvH1iUO6a3DkJvijAA7SbBPOxUfrMoGF4tMEt_Yza9WPIlKjp-Na9C8-gDGL1EhFFrR3F0P5mWRbZHk3ShTdHeaKheUIgxKaDCATJdQVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=QGDDFQusFES8M-kPwrhqt0Cg24IdCfc3-im_b3GCWvlD59ES5yoAgZLT3OSXGVl1V5n8VpenxpCD1rsSfDrsgNIzFYf0J1XdabS-u3wAQFu4KF2_DT4eYv-TZHCxa3PwNZqh8KqeKcWgT6YU3F7Fvlz9h2hopfp0sXxvV-9nuXzfdKpnadbn_i6zjokyDV4hqzlIzwOJdKVNdriIuS74rXwLRCPQtUQZP6Ia-Z9IaUuvdR75obW9FPoi7-fk30iyMMEt4upFpeRwtSeAKhogjrDrKBQWs8uYQGZ0yufKdSyEgjtCuYdWqqZ2RQyQunuzmIzxbMHHdZfU8mRK0K5qBQPM1vpZMzl0GIickhxT7DGs-NFgAUbGHrnWh21DYNqMsg6wYDl1Akooayj_pv26eG0J-P2N1kK3YCy6iAh4u81k7RPagqG7Pe6BZ55mOJP0Ele2D-nkNz2x1I9LWwbf5D8jvNoQuTprvzgdX_PzWNt9mhJW4P7_P4nii0ctg0cPa2-eItGxP6_zhUDtjjbN7S3FZELXMUWs-km_6Yl-Liy_S3M_bZDyKWBtxzsI4qvmTXvvH1iUO6a3DkJvijAA7SbBPOxUfrMoGF4tMEt_Yza9WPIlKjp-Na9C8-gDGL1EhFFrR3F0P5mWRbZHk3ShTdHeaKheUIgxKaDCATJdQVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ldktk9tCRasJfxvVq-n9DJDWlai5l5EsP-300jgJeGOObSUAeOguxOpZOfljS69BAm229M8pQ7QK6u6I6Kh1nMtuxV0_lCFwXjYfo9epaQ6_hW0X5yIUBYhbtp7X8pLok5tGp7NHYJO_npy2lfQJMWG2ZDUFwlfzr04PDXjTmRvdtSoNkWB35e6l85eovo73CxRBOGlzRfvRAJeC23plJoFOEAsuIStjexscYKPyIwZwW0F-3fs1NJ0wgBK12R5-DjArZ6jfbNFdid8OV3OgmRzXEliTno9BwR50Ve609BlCNFq6JgLGfFqrsjl0lK9br3EQKPhKLYkx9B1BJx0NuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ldktk9tCRasJfxvVq-n9DJDWlai5l5EsP-300jgJeGOObSUAeOguxOpZOfljS69BAm229M8pQ7QK6u6I6Kh1nMtuxV0_lCFwXjYfo9epaQ6_hW0X5yIUBYhbtp7X8pLok5tGp7NHYJO_npy2lfQJMWG2ZDUFwlfzr04PDXjTmRvdtSoNkWB35e6l85eovo73CxRBOGlzRfvRAJeC23plJoFOEAsuIStjexscYKPyIwZwW0F-3fs1NJ0wgBK12R5-DjArZ6jfbNFdid8OV3OgmRzXEliTno9BwR50Ve609BlCNFq6JgLGfFqrsjl0lK9br3EQKPhKLYkx9B1BJx0NuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=brvZBZwwmY1l4r1yePEiNzSWqMiW2TpbCK5_uiRjxbCyt9RioE4-lDweswLHuxHV9cAdJbJpuNnQSKjP4SErH3vJMJ2pt4Cb5Y2OhscDPgo1591qpp8XCnDRD6F8QslsPEU5nsNgujoHI-fTu88si34Jewp-PfFYLOBF-wIs7svUbCSyRbs_j3weh-J7Frr8GTHcgu9l-o7niz_0uYtfC2Iw_xyqyIHzImyPcmhHvWY7tQ1BB7884Dc4XwHpPwEaFmNbvAHFTT4tz4qPXsK4bWOVK6X6UNFYSL5xeti8zx1l9cu-2u0O85oyXGSWbNxdfP8AUp928KrIEqjJmSd_eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=brvZBZwwmY1l4r1yePEiNzSWqMiW2TpbCK5_uiRjxbCyt9RioE4-lDweswLHuxHV9cAdJbJpuNnQSKjP4SErH3vJMJ2pt4Cb5Y2OhscDPgo1591qpp8XCnDRD6F8QslsPEU5nsNgujoHI-fTu88si34Jewp-PfFYLOBF-wIs7svUbCSyRbs_j3weh-J7Frr8GTHcgu9l-o7niz_0uYtfC2Iw_xyqyIHzImyPcmhHvWY7tQ1BB7884Dc4XwHpPwEaFmNbvAHFTT4tz4qPXsK4bWOVK6X6UNFYSL5xeti8zx1l9cu-2u0O85oyXGSWbNxdfP8AUp928KrIEqjJmSd_eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=lQNmEjuV2aeRVqqIWKxLzwywTlLBcr2E3_XBNuux3IRtBvabnEv8ibo90dcgdZNNNdwuxL-ZFzlt2xmNxpEtYbTbWMmHBFYFmVAww-ViwAWI5U-ikwTYo1EwD_MVmASDfOZWpPkZDSgt4U3k2HYLUW69JEWOKzAtmb1ZQ6qeWxrM4MW0ce1S6How3nfPjIfkn2NShEnhwKZQI1fvBO8aYPc9klkLpJ2Nsbu8-R2ZO936qeyZu-NOBhtBV-fiJ0cWhwVdGX9PFnVgdJCqzLXlXFg9FQL1WRk_GAfGTi02bCe3vcdAkW7w9cYCIA4aDZsKed46xeAN5NBnjR2TLQofmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=lQNmEjuV2aeRVqqIWKxLzwywTlLBcr2E3_XBNuux3IRtBvabnEv8ibo90dcgdZNNNdwuxL-ZFzlt2xmNxpEtYbTbWMmHBFYFmVAww-ViwAWI5U-ikwTYo1EwD_MVmASDfOZWpPkZDSgt4U3k2HYLUW69JEWOKzAtmb1ZQ6qeWxrM4MW0ce1S6How3nfPjIfkn2NShEnhwKZQI1fvBO8aYPc9klkLpJ2Nsbu8-R2ZO936qeyZu-NOBhtBV-fiJ0cWhwVdGX9PFnVgdJCqzLXlXFg9FQL1WRk_GAfGTi02bCe3vcdAkW7w9cYCIA4aDZsKed46xeAN5NBnjR2TLQofmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ZouYYTb_w3RYg8SU4GLop-FiMTIsEZpedDinIrYoMqR21nN_HwM6tOeDvdxJvQHjKWkcFdOnxJn6T85Ge6aPlTTwaMdjPQ3pJhDv5Re35MCZtDxFLtGTjiMOw6S12HwcoJbz6pr0T6NKH2iST2UjttZU1X8tv_43IqBHcyyIZZUqg1qX5XgWYSsxXN8U9Y7b_vt7_nyyLTD4b6SQXkMzte_skdAs3jb7EXuVoUo-bVnnB-eQMAiUDKKqtY2NX_K5l9fLqB0xRpHTRuzIP7iAAdm64dxWnfJKsYePwyWZXqUeUOPFiRM3aIlQ8r6rUUuZ-4s_BT-OPYIsnM4_FZxEhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ZouYYTb_w3RYg8SU4GLop-FiMTIsEZpedDinIrYoMqR21nN_HwM6tOeDvdxJvQHjKWkcFdOnxJn6T85Ge6aPlTTwaMdjPQ3pJhDv5Re35MCZtDxFLtGTjiMOw6S12HwcoJbz6pr0T6NKH2iST2UjttZU1X8tv_43IqBHcyyIZZUqg1qX5XgWYSsxXN8U9Y7b_vt7_nyyLTD4b6SQXkMzte_skdAs3jb7EXuVoUo-bVnnB-eQMAiUDKKqtY2NX_K5l9fLqB0xRpHTRuzIP7iAAdm64dxWnfJKsYePwyWZXqUeUOPFiRM3aIlQ8r6rUUuZ-4s_BT-OPYIsnM4_FZxEhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Oq-rxK24qityhcbt4ZkU1l5H4Z9B0LR0XXNEIvFRdztu-k_4C3ycq-C2Ea-Qie7gsciiIxNRTrWkIgM95pYndcbUfNhaMfn86umZIfLi4M3VP-du5EyYYPzMjlNMkGqZUckVsxksX97Qesr60SmwgDW4V-pKPmcY0M2RaZm5tKQ04Zuo25hkSE4Qt62DHHdJNCUIscYTpszyjG7iaR3VsliuJxREpBrkLRD0-0Ls0a8iO92A_fmBpN7sQgrDy52EGiJ5MCLT-zCrxMnf36JDK_5scNu5osKMT-b8eJFLyGHjRVNQrJ9QUNARhRMnMmkub9_hnm1AFQT5m9ASuJOEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Oq-rxK24qityhcbt4ZkU1l5H4Z9B0LR0XXNEIvFRdztu-k_4C3ycq-C2Ea-Qie7gsciiIxNRTrWkIgM95pYndcbUfNhaMfn86umZIfLi4M3VP-du5EyYYPzMjlNMkGqZUckVsxksX97Qesr60SmwgDW4V-pKPmcY0M2RaZm5tKQ04Zuo25hkSE4Qt62DHHdJNCUIscYTpszyjG7iaR3VsliuJxREpBrkLRD0-0Ls0a8iO92A_fmBpN7sQgrDy52EGiJ5MCLT-zCrxMnf36JDK_5scNu5osKMT-b8eJFLyGHjRVNQrJ9QUNARhRMnMmkub9_hnm1AFQT5m9ASuJOEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Rda41aJhfz_M-QxE_82_iFfYdLAv_U91aS5XeqSw1eH-PmvB0MvV-HN-9cZ_1PAVtt2WEnvJpJDcyBwHq8xL0cDrRGPzoS-ji2RWpYnyuQt42eMlKAe10O0Wfx2rNmQ2Qfezbt8gaCJyQhkNp16mGN0sEL9RNdTaU8UzpmLUJIeSZ0ttjvktIPPIT9Y5Hx0iqv6ANNSjWT_ycOexuHSYAVP0DarpPIrxw5vatRztZuX5N8OnRihLDQ6pkD9VfC3UmCLMAJesSDUYHg8qovJuhgFFHyYG25siDV4xbDBgHoggmB4_0xQaKg3lBuxfrGR2sf0wN-0_H2rYHm5os8gplw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Rda41aJhfz_M-QxE_82_iFfYdLAv_U91aS5XeqSw1eH-PmvB0MvV-HN-9cZ_1PAVtt2WEnvJpJDcyBwHq8xL0cDrRGPzoS-ji2RWpYnyuQt42eMlKAe10O0Wfx2rNmQ2Qfezbt8gaCJyQhkNp16mGN0sEL9RNdTaU8UzpmLUJIeSZ0ttjvktIPPIT9Y5Hx0iqv6ANNSjWT_ycOexuHSYAVP0DarpPIrxw5vatRztZuX5N8OnRihLDQ6pkD9VfC3UmCLMAJesSDUYHg8qovJuhgFFHyYG25siDV4xbDBgHoggmB4_0xQaKg3lBuxfrGR2sf0wN-0_H2rYHm5os8gplw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Odv9-7GDglVb_S_pdBOWJB0b8cBCL9Ud31kekbomyJeTVDDeUA4bHJf-mONxGXlC_Fg1CbDOe1VgaFjT_qjxuJPr_DxTRRJnlt68A4FpT3e3frPZN8NBeS3869avOYEN5RZ_Q4XORAfq0pq84dMP_-1Opju5RUSqJJGD51bLiNYoiC9zdsS28zafcbw25cwHf385d6UJT0n7zB6dnkO4b0AAs9bEU2drRE4rLpYptJsqlcjkHuOnwzQ1aWyV36Y1_EL9Q4HeKQRM3WSUv0NBY4GBB5IoZUJ3EbYZpYop_0GqTnv-UbiDOBft33RvU6Kz5d1jZePTTBliY021FqFfZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Odv9-7GDglVb_S_pdBOWJB0b8cBCL9Ud31kekbomyJeTVDDeUA4bHJf-mONxGXlC_Fg1CbDOe1VgaFjT_qjxuJPr_DxTRRJnlt68A4FpT3e3frPZN8NBeS3869avOYEN5RZ_Q4XORAfq0pq84dMP_-1Opju5RUSqJJGD51bLiNYoiC9zdsS28zafcbw25cwHf385d6UJT0n7zB6dnkO4b0AAs9bEU2drRE4rLpYptJsqlcjkHuOnwzQ1aWyV36Y1_EL9Q4HeKQRM3WSUv0NBY4GBB5IoZUJ3EbYZpYop_0GqTnv-UbiDOBft33RvU6Kz5d1jZePTTBliY021FqFfZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_IZAHYnG1CeEnVTpQLHRockZsR0pQoZEhFYRsDlszVOIR91tMRZf2lBJMe8vajjUQxcM_eHkV-QlmXiE7QTcJFR0z1U91XrCzGgNAu0bo4plTuJj1MHT78Hmq1pCDi9DOXqo5XEjqRDe7KGktasJtePUmN0fGoCuiaHNilEYeLHdCNwAKAD4pvPBBiWQxicP_1qV5hex0iqixbf8uXrht6zV-ykCMnTcFwuSktmjKd4vMj8OOsHQVw7tbXAFLP-21rG76-FJkSRPTwhyxWa0xsrHR39Eo4i-tuBOZsPSNc07pEfGD3FTMWN4tIeFrMlS_0Ur-xdgi2tgbRKy4pclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=FIjpAOZuhxJwc-n3oAeewvMHsE4J2RD2XT82T8gGqg5IffO8kXDYBnCViRjJzIP8cnWp8TCjxz1bP8DsNaUAD2ASux4zX72uJx3jNWdtKIvdEHlSqC4iXa2QUueEFJ6UEPlbQZkhTal6Df6NfWLrUY9Y1De7NavLD8yPtJ78d99K0Pz5TjLAaPiQIl-YP_5kb9s49PnSnkgeGwbNzvUwvsb1icGHMbgOWP7anLL1JoV3aMwzRfXopikh0Tlega_-ZlyZmozNXBXwtnQe_MBPYof7G2aQx-Y3ZknDNu4AiBVvt-rKuA_gvWnv3f4iLMH6Zd1alLpAxE9D8BHJapgAgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=FIjpAOZuhxJwc-n3oAeewvMHsE4J2RD2XT82T8gGqg5IffO8kXDYBnCViRjJzIP8cnWp8TCjxz1bP8DsNaUAD2ASux4zX72uJx3jNWdtKIvdEHlSqC4iXa2QUueEFJ6UEPlbQZkhTal6Df6NfWLrUY9Y1De7NavLD8yPtJ78d99K0Pz5TjLAaPiQIl-YP_5kb9s49PnSnkgeGwbNzvUwvsb1icGHMbgOWP7anLL1JoV3aMwzRfXopikh0Tlega_-ZlyZmozNXBXwtnQe_MBPYof7G2aQx-Y3ZknDNu4AiBVvt-rKuA_gvWnv3f4iLMH6Zd1alLpAxE9D8BHJapgAgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Uk3rOv8r7miQ5ZlKx16BBoZgHlpS1WCaVf7iNDoFosCTpXU6nUekApxRsRW3vs_pCQ0RgguIQWtWM0RvqZX5y1azNRxCGftw1tTvGiSHfsgaQr0K-0V2HNCvwahGvSe9YpGs9QnOvczO-YaGUVjvpsUO5w4Gwpuw78rTqZqbOmgum5q-0BoEAKmsm6yBdM-XtShFs-j2IKRF4aW4hdFURzXgGjQDq5sJH9DvY7xh2lQ43KMb7X5hd2NdBHuLL6zIgfK7s3p0iHp_RuC7uDbo7I_YaiICdTVb9htxRkTZQyKaehGUnp_x3IG1ZyGxr4zLJbayNXMdrBvNVG5y6t8ZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Uk3rOv8r7miQ5ZlKx16BBoZgHlpS1WCaVf7iNDoFosCTpXU6nUekApxRsRW3vs_pCQ0RgguIQWtWM0RvqZX5y1azNRxCGftw1tTvGiSHfsgaQr0K-0V2HNCvwahGvSe9YpGs9QnOvczO-YaGUVjvpsUO5w4Gwpuw78rTqZqbOmgum5q-0BoEAKmsm6yBdM-XtShFs-j2IKRF4aW4hdFURzXgGjQDq5sJH9DvY7xh2lQ43KMb7X5hd2NdBHuLL6zIgfK7s3p0iHp_RuC7uDbo7I_YaiICdTVb9htxRkTZQyKaehGUnp_x3IG1ZyGxr4zLJbayNXMdrBvNVG5y6t8ZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=kwK3qKQL0OrZLbD_9UqGuNvdUhVT8w0Vfr2lIq10lZjdlcexOIYgRKhC592yiMU9TOavQNZRGf_V0MDjece42easbAYBP9_hXoRfrm0u5kIxvYZ5d6EX12riNvboRpJGKceME9oc7SFdX4TDDW-vH9It4xZKnAuOyph8GxTgIBbbRH1C2SZs1DfUJoiNerr_Izl9hvH3y_GRybmjiBM0yLVIJTi6jmagEkTFoCxxNtDOTS0TkezWjcXihNg1gX9ixI3i2WLvwbxzGuKXB8O662bLOQdQwAZF7lVevv4jfh9ClNhGVxBJsaf0ugmsPsSWFyEOnN-bhZVqHikupFRqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=kwK3qKQL0OrZLbD_9UqGuNvdUhVT8w0Vfr2lIq10lZjdlcexOIYgRKhC592yiMU9TOavQNZRGf_V0MDjece42easbAYBP9_hXoRfrm0u5kIxvYZ5d6EX12riNvboRpJGKceME9oc7SFdX4TDDW-vH9It4xZKnAuOyph8GxTgIBbbRH1C2SZs1DfUJoiNerr_Izl9hvH3y_GRybmjiBM0yLVIJTi6jmagEkTFoCxxNtDOTS0TkezWjcXihNg1gX9ixI3i2WLvwbxzGuKXB8O662bLOQdQwAZF7lVevv4jfh9ClNhGVxBJsaf0ugmsPsSWFyEOnN-bhZVqHikupFRqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=aV7vjMoaruqOva8yGg5yNCniuzeXQRT2F3a3GWN14sh927fvzt1V_JahMMp1VcyEgyxAcfnN6u1A74cJWCfa84YOA2a2s5EQwgO2hiWOoF3xdkw1hfBLCUbIYjutO4v6fNA6CoEkonLPpAzMzf5TA0BOpLkALXfK5BBdKLYdabWOwRG2txuryF3ZRUw3n5NdzTbwYRIuzv30loDNbRYaCHsvi7HJwhv5NfTZ43g2tM8RCGuAYgabT1P4vKU5ba7sBuMNNUvZKmbXp_KFW7Hl3SeDP7EkcPZpFx9CfRNF2XsWRzDARixYFSE8HupTRrWiRxTNog-wCvsVGRtmf6gqgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=aV7vjMoaruqOva8yGg5yNCniuzeXQRT2F3a3GWN14sh927fvzt1V_JahMMp1VcyEgyxAcfnN6u1A74cJWCfa84YOA2a2s5EQwgO2hiWOoF3xdkw1hfBLCUbIYjutO4v6fNA6CoEkonLPpAzMzf5TA0BOpLkALXfK5BBdKLYdabWOwRG2txuryF3ZRUw3n5NdzTbwYRIuzv30loDNbRYaCHsvi7HJwhv5NfTZ43g2tM8RCGuAYgabT1P4vKU5ba7sBuMNNUvZKmbXp_KFW7Hl3SeDP7EkcPZpFx9CfRNF2XsWRzDARixYFSE8HupTRrWiRxTNog-wCvsVGRtmf6gqgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOSDXlTQEYi1lGYi-COWDzRL8sBmmaGsEnBOtQCNXjH868nkR5o9V_ZKQZC1J5m9kpBQZ0czukj0znEj6O68Frc4dcSoadj8erecvNWBn6isP0p_TihVqGiyfo3mV9X5dwSGE1FydtQtPDdADVhe846N-jkqnTLSp5OWARio57gqD4oVSdWBz4jWic0uaqII0cBtplxJyd_pG-hn220XzdR35TLH65V9eM_S9_hDzhJPA_CXfF8LRuB30G-CivxfdhbAA0Z8L4bXEXMhQACUuuv41MLSrwb35eh03uxUgB617vVJFf_K-lVpZsyIoGDZ2IhYrNcyzR_HoDURvdBT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HSsZUyCGcUOrep3QzVN1_lXYaHtQGtDaL4ri6YEDnOM4PpKDPeX5dO2raWMHMcXw6VRsKk9NWiiL8CJa625wkWQlNzC8UWkXHL2qRwitKi_m8kBrOC3k4taOBOx-Ko8dwnB94qY7LwhPYBlMuuoHmuxZoAdD792BKhivPxUrGRDXLUzvLwWnHoBtHgZfCBvZI4cXx6w31s6NNIgXkbVEH77YLWLHv_gNhb37vL83BhbOK5_eJdIGmWzqbLU1nzTQwVS2Ny7G3ld31PzRXDPU48RwIcKjTvJurf793Wf1p97hmhCH8OUB1UYMZubShvqx5wm8xjchqXWJA0DOZNzedzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HSsZUyCGcUOrep3QzVN1_lXYaHtQGtDaL4ri6YEDnOM4PpKDPeX5dO2raWMHMcXw6VRsKk9NWiiL8CJa625wkWQlNzC8UWkXHL2qRwitKi_m8kBrOC3k4taOBOx-Ko8dwnB94qY7LwhPYBlMuuoHmuxZoAdD792BKhivPxUrGRDXLUzvLwWnHoBtHgZfCBvZI4cXx6w31s6NNIgXkbVEH77YLWLHv_gNhb37vL83BhbOK5_eJdIGmWzqbLU1nzTQwVS2Ny7G3ld31PzRXDPU48RwIcKjTvJurf793Wf1p97hmhCH8OUB1UYMZubShvqx5wm8xjchqXWJA0DOZNzedzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=NiAQCZlazdsGblwIbYiPRAVeAYHw7tASe-d3-zPWXsWZOJW9r0SQhPEAslFSEbHvi4RMhXsdZxTSnjonrKSsY4Cs5EHcJP52su7oJdOusYBOprxNJnllQe8YjgoWGJL49Zywl06_bd7DfwKhgbFfQZ_-ydbVfByGdrKHK_jWEMRYbzi4cbVZkbkLobEZMqJdssmuKbDmuHMM2zDVkfdMU6Wz54vpYiRuE_j1WyBwCLgs002zRWaMtxUapwY844NGuBCKCHWtsJ9QCR7hPv4XqTYArvW3nKxJhthHFSYh-jdEzjtUAp2ZP3Z05UZgJX0n8evmpUBMn32Lfz9mPQSYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=NiAQCZlazdsGblwIbYiPRAVeAYHw7tASe-d3-zPWXsWZOJW9r0SQhPEAslFSEbHvi4RMhXsdZxTSnjonrKSsY4Cs5EHcJP52su7oJdOusYBOprxNJnllQe8YjgoWGJL49Zywl06_bd7DfwKhgbFfQZ_-ydbVfByGdrKHK_jWEMRYbzi4cbVZkbkLobEZMqJdssmuKbDmuHMM2zDVkfdMU6Wz54vpYiRuE_j1WyBwCLgs002zRWaMtxUapwY844NGuBCKCHWtsJ9QCR7hPv4XqTYArvW3nKxJhthHFSYh-jdEzjtUAp2ZP3Z05UZgJX0n8evmpUBMn32Lfz9mPQSYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZjUDgdW4-GXfkfF71GrTzlGx5-pina35pwrx45opCMqDVT3Bu2UYQepYPGcOze_77QVlrKmFelWZ_EfFsRizvQY5lDay58zcGzHw2JmI8NwpFPW28uTVmwUAZ5v3i_SBOqFIj-oNIX77reXcZ0fI-MxuvcyuZX32kv5fFDf7VC8lpjA_X7otWAuhSe5qME9IQmznBNaM1XZIW-MXMkS4eXl2cpG9pXOSIo0vrw2vqtAacmbRucUsleE6cmVlTc_qXTk1fLvdiLlqTXaPkdD3YRsBJAvMyD4vhAEsyawWqROK1q7LUkRdmDjFDT3b29WPYh4M7imXoUkTS3j62xtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0ijTwKvrWmyDgkkGDd8mCapTo2G-CW4WNoFlNkmGM9OQXdALT3CvQNuYi0CoSqejx3wYOQMLxixF1qqNydxW6-fezreDFCjv3eBSuFSVD84pgo6Y39lSIU77K3qf5J_PVm_ydSwHwAl2NU9eAUspxCvxdFKHKSXz30vdIijG4JMtc9nQ8vrEEI1Cn8JGgwdJGSY2fJffMPkt9PepzKHVo4E3De8SryUvH5YPQ6ozRcsfR9x4eoAAFKh7x9viL6LiCQSiO9IJRLC4c87NSvrNcA5rOtTc9uKsSADMs-zl5WIx2wXey-RzQj5H9fH74AoRShpTzEqlNbObSOkrE1dFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=l-eXHQH3mbKP-NwE8YkytrOhPbRCPo1oXA8ah4X6n2W0netkv9-J_fx__y76ktzLqjXNzB9dPaE3N86gjP69RE7yv8U7xdCFmCr-kJhO03XasexBX-NnH-YY-yM10GFAYFe88sjJI6Oi1DYcYtSVO4v4D6YSnisU9edY4AglHOtceuL1G3b1Ycx6TMGhigLUnIYuIr-X1kot_ktn586fof9jDndMmDcccqjtfUAe-Om1TYYjNjZT87K9CxCXqgtO1Lt1haCgDGhoGemFOofFpFbY9DwUQZ9Myp9voUP46vpVp7N3u0Xhe1L2wq62qUr7FocPsWiBXhWl-Oz9AMZZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=l-eXHQH3mbKP-NwE8YkytrOhPbRCPo1oXA8ah4X6n2W0netkv9-J_fx__y76ktzLqjXNzB9dPaE3N86gjP69RE7yv8U7xdCFmCr-kJhO03XasexBX-NnH-YY-yM10GFAYFe88sjJI6Oi1DYcYtSVO4v4D6YSnisU9edY4AglHOtceuL1G3b1Ycx6TMGhigLUnIYuIr-X1kot_ktn586fof9jDndMmDcccqjtfUAe-Om1TYYjNjZT87K9CxCXqgtO1Lt1haCgDGhoGemFOofFpFbY9DwUQZ9Myp9voUP46vpVp7N3u0Xhe1L2wq62qUr7FocPsWiBXhWl-Oz9AMZZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0378PosYTlRHKGWhs_MhlmSYYXOb154ZKT-rAO4zxEYnh9_7Jj88BOjUnbZ7SrI3B_gzEtdj3S5Wl-kkNsRmiW19hx35nAbEtp6kgLkhVMkf7rgYHJ4Ql4fluED46S2cXlTZePs708T-wz-ON8C_Yne4ALMviUmS-cNqGpC_aPms_LFpjsCEKc7I90O0CCHr8Wlm-_fCA7wRec5Q-jfZeE5RkHVOa_sbq-0M17XEqOpLMLvUXo0KZSdcRhsUAhCdKkpjaTfJvAEYOir-tykiG9baopP7Dm9BiGr8ZDNxycgGkkEcNDBYT2MXBh0fSai1XZ5-_DHQI311sxR57CuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPv77QAZzeSiSjBK6e9OtHzp6pmfmwKz5VidGM8lBQ8Aq5lxQlY61b5h0_fxPBIwy8eXNIAb4w75JMa1dwnR8TVTVlDOBdSTG5K7Zs0vXdMz2Ut1HANAIzh4MQSywn0nxFXqe5pmDnqBhMoG7zwamevMo1Z-yc-8vEW2QtzcfXFVlcXD2hlHQXjC7gwyDBbpcrbsseGgjG3SIjVQEZTz6i4FdUcjqYQgzRTUd_mfaDvq_m5A01vFgSbEtS8pxQ7iQfYZ6-bS0y6p__FGy_1NI-XcF8APt-zro1bffmMthS8vh-kpDMmhSX-WsRULPS5MnnLe4VyCxH7oKICA9AiV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPM0DVWxvPQA1sv_p3eloLAHB7zbcCGXzhcGDs-sKc6k_QTFCE8lI0PqJpgUm2DjO1iDuEkP5NUVU1RAws0bK8tMY0_45TmdoWZmWucGTO9s47nK0hZeeBNsBWgvq5FutJ_TaTqRHIQOM6aB57R18Qi22QKwhwAaCbouif2fE0xDwf_XJnF_F5qNX3dI3L9-SO-MtEf04iWUvQ7DU_qDhIuR0JwRgt_ztAyImF5BiuEWNL13keYvboeLKe5lTHrw-apaB4KJMQmBEqZPFrTpe3rdPvURpeLxee34Y9PXz0dqSf0AGDpid8FkjnSL1Eu5YGOyL66MQnPQyJkz3sXIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=KJXQUcp4_5I--dnSRyXR-9rDRs16Opdzu7t1GaoS92m1LL13q3nmBtVTVBQUvwJOrMkkGLsRsVnXIHX8yNpGTIIvzZUOD339woWGdpPD5zYfJqDFfSDDIdGQ4A528S7pihSzULr5fYlUTPc8BhzeC9v0-OkIf8IUO0RKJY3RhFUAK22qJUkDg2_oDu5r0ai0DHsvzsvYrx36W15qFwP1pTZMVf2zXvHc2lUpuDIaajgU3zdIBJ0M83L7zvMkOAHXeNkfNAsXZAk7gbu3rs9SfeKwbTUzfcSeVc63Ctjq58ujsntLTYDSHeHQ82qOTomBEjxk_4K8laqkwU1yaHX-Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=KJXQUcp4_5I--dnSRyXR-9rDRs16Opdzu7t1GaoS92m1LL13q3nmBtVTVBQUvwJOrMkkGLsRsVnXIHX8yNpGTIIvzZUOD339woWGdpPD5zYfJqDFfSDDIdGQ4A528S7pihSzULr5fYlUTPc8BhzeC9v0-OkIf8IUO0RKJY3RhFUAK22qJUkDg2_oDu5r0ai0DHsvzsvYrx36W15qFwP1pTZMVf2zXvHc2lUpuDIaajgU3zdIBJ0M83L7zvMkOAHXeNkfNAsXZAk7gbu3rs9SfeKwbTUzfcSeVc63Ctjq58ujsntLTYDSHeHQ82qOTomBEjxk_4K8laqkwU1yaHX-Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JhbbtmXz_AxceWJLlqaVwd5bU6mgXrHjN2_Uxlpc28jbb4LPewh707o5TWeAjjM4K-lT_0-f6rN1pKc2jSf5_Dwzyg5VfWUul5rFm1vsKLVdfuEP68OnuHBaKRxIWFB1Ketn4RJ9198eIqi1CkgfSoi2pCNZyjkx_D_RaLVpFa3xgOKfCc4UhdaUuFlnPIYT9NugYxDJOISuLCIXermx2N7srbU5u3gVNxlpLjtz4CibbGOir90l2LzFZA5jMY2Wu5IgPWLo7mO_B2h2rp3VU_hliyEV7RCmwyEZ1XLvtnD678FIaYxe4MkDSzjhlrLi_7Q2KPlzE1ZiyCAIpoOFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JhbbtmXz_AxceWJLlqaVwd5bU6mgXrHjN2_Uxlpc28jbb4LPewh707o5TWeAjjM4K-lT_0-f6rN1pKc2jSf5_Dwzyg5VfWUul5rFm1vsKLVdfuEP68OnuHBaKRxIWFB1Ketn4RJ9198eIqi1CkgfSoi2pCNZyjkx_D_RaLVpFa3xgOKfCc4UhdaUuFlnPIYT9NugYxDJOISuLCIXermx2N7srbU5u3gVNxlpLjtz4CibbGOir90l2LzFZA5jMY2Wu5IgPWLo7mO_B2h2rp3VU_hliyEV7RCmwyEZ1XLvtnD678FIaYxe4MkDSzjhlrLi_7Q2KPlzE1ZiyCAIpoOFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hkCtvi1gQr6kbx_9iTSA8EPWPJbOLv2qBZNeRZsS7QvDnO3dMMMFMvbQlbMXeJe8ZpES14v2Oxt6pUeyhUtSsCi-sYOR5H3QHNH-4Dtm_CxmfuhE7fd0eLryuVrk1PvDR2bpGnbFVvYB-b6d4buSvTUzoPdgf69YKWzFAB0QCR5gUn0UMxfXh6iTzhm5kyncjQTDGNmXNfh3bz79ljEOe9GwlVYatBXraGWHAne5VxHVnLneXHVqy_Ytq4QFRsYRzAdHrwLaS9KiJEFylWrPnQqu-1RQEsF_IrbkKlWjw24zSCzdeB9qwACzZgUr_pqsg-QogQVl05M0P4BChNq_iJpGFPHIBNaCxFuoJdhge861oSJeV42189fiYwd2mb3R1tOwW4jxQgVj0YyjVAWZhHYFMkhIHZd1CUPA0qNFvrWFrbhs76-cL_kBQKJWsTOVBBqY2EqSVY3Pq9xLQbrZDywQUxs2aWHEeq-YRbPp3SJh8rYT2Rhd-J77EfEiRMCqmgwc-qH9OMhIWxnmGQ7r_HTMdWEV7lRjR-VnHn6XI5HByhlWqQgio-O6rGrzt9IUxaP09albcuZhim5fZ71PoflmKfOno3Jct9T_xAcvaNXjXImKhkBq5mYGrzx5YnGk16A5dzyJeDir1BCkxpDTQAcRgAu5WN9jKWQpT_nmOGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hkCtvi1gQr6kbx_9iTSA8EPWPJbOLv2qBZNeRZsS7QvDnO3dMMMFMvbQlbMXeJe8ZpES14v2Oxt6pUeyhUtSsCi-sYOR5H3QHNH-4Dtm_CxmfuhE7fd0eLryuVrk1PvDR2bpGnbFVvYB-b6d4buSvTUzoPdgf69YKWzFAB0QCR5gUn0UMxfXh6iTzhm5kyncjQTDGNmXNfh3bz79ljEOe9GwlVYatBXraGWHAne5VxHVnLneXHVqy_Ytq4QFRsYRzAdHrwLaS9KiJEFylWrPnQqu-1RQEsF_IrbkKlWjw24zSCzdeB9qwACzZgUr_pqsg-QogQVl05M0P4BChNq_iJpGFPHIBNaCxFuoJdhge861oSJeV42189fiYwd2mb3R1tOwW4jxQgVj0YyjVAWZhHYFMkhIHZd1CUPA0qNFvrWFrbhs76-cL_kBQKJWsTOVBBqY2EqSVY3Pq9xLQbrZDywQUxs2aWHEeq-YRbPp3SJh8rYT2Rhd-J77EfEiRMCqmgwc-qH9OMhIWxnmGQ7r_HTMdWEV7lRjR-VnHn6XI5HByhlWqQgio-O6rGrzt9IUxaP09albcuZhim5fZ71PoflmKfOno3Jct9T_xAcvaNXjXImKhkBq5mYGrzx5YnGk16A5dzyJeDir1BCkxpDTQAcRgAu5WN9jKWQpT_nmOGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=jnZo_UjMlVq_QVzObAuXowCUOePO_CZdHFwLw9eLLA6BeqkFjV4R9IB8thK2XQw_0Y-HRNth-TXhRxTJw9FPtchxaz0RbhmSSoKuyECygYDUMIstR6H-GHl7n7G7F_Tdn7i_DRchEO0Osl4J2-U7oJF72AQo6n-LvxJrV7lc1f_O3bpZTyiYyFtNXg3ztrRizqgTAds83JJSW3qr7SDH9v6dHy3gcZ0DLwZCIjG84RI1Och1L7mP8lqLdLmw09D-0-V01QkgjgRYXFJ43BcaFX-AcG3vOZ7-K2b1bZROg11ifdBVD_GDC1PyLT0gDC87zlXo6jKRr3dJMbuh7orDf24sn8u_KPfghSWfgoasBMyGTHIi5IcflMF_nii-mpeUEpv7UZFziQ6_C4_vJ4F2oCEIMFHhGQ7fSMQUzaOkJDtvtzhQb8AyycS0biWIqxE5FuLrEy2XFrYGgd7u5Wjt4FEWaTB-0wtdhovTveRw_IazONQ8NHEOvK1c3rjcihhuq9l_WL7A4S3CpcBwfvWlgR93DwJVUB8QdErl13UMWiskkNCejU8RzPlJiHlZg4FnupKtIDtqDjH0JKVGnWengcwDhfKmRh-dVw-wq-sT9XI3Y1Au8IBL7uiokryXpgZHO8nIiG7bIPSo2ARJF_Y_-TlCz4kx4ZNIiDPgxdfOhVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=jnZo_UjMlVq_QVzObAuXowCUOePO_CZdHFwLw9eLLA6BeqkFjV4R9IB8thK2XQw_0Y-HRNth-TXhRxTJw9FPtchxaz0RbhmSSoKuyECygYDUMIstR6H-GHl7n7G7F_Tdn7i_DRchEO0Osl4J2-U7oJF72AQo6n-LvxJrV7lc1f_O3bpZTyiYyFtNXg3ztrRizqgTAds83JJSW3qr7SDH9v6dHy3gcZ0DLwZCIjG84RI1Och1L7mP8lqLdLmw09D-0-V01QkgjgRYXFJ43BcaFX-AcG3vOZ7-K2b1bZROg11ifdBVD_GDC1PyLT0gDC87zlXo6jKRr3dJMbuh7orDf24sn8u_KPfghSWfgoasBMyGTHIi5IcflMF_nii-mpeUEpv7UZFziQ6_C4_vJ4F2oCEIMFHhGQ7fSMQUzaOkJDtvtzhQb8AyycS0biWIqxE5FuLrEy2XFrYGgd7u5Wjt4FEWaTB-0wtdhovTveRw_IazONQ8NHEOvK1c3rjcihhuq9l_WL7A4S3CpcBwfvWlgR93DwJVUB8QdErl13UMWiskkNCejU8RzPlJiHlZg4FnupKtIDtqDjH0JKVGnWengcwDhfKmRh-dVw-wq-sT9XI3Y1Au8IBL7uiokryXpgZHO8nIiG7bIPSo2ARJF_Y_-TlCz4kx4ZNIiDPgxdfOhVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tE5q0gnhNdunqqOFBERmigzP1Js7YlUkAlt2PaMToMFoQb2f4bJONPvGn9idu57QzgbBbVPr2rh4CF94qFDnRvOSr8O3m-DiBGePntHt8IbYy8AVj0_0zwnqjYSBwHLry8GAi8ApT7N4pH_gi-rFeUp8Qwqini5WL_cmDCNoYoheAhOhxTtEIVf_S5WBiwr6i6VgxT-6PUXaj1cuUFzfmKrjsuM2QKp2pLIat-WIVBwjTM6Xrc-M27bl_ApOO5RMwcZ0wr3g3QILuN8rw0Cus8s-1RuiWoMWHuZlv0YeIfMpc97WA3bwHL0DDfUfvERAl2b7gZ3wN6F229MD6XL1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tE5q0gnhNdunqqOFBERmigzP1Js7YlUkAlt2PaMToMFoQb2f4bJONPvGn9idu57QzgbBbVPr2rh4CF94qFDnRvOSr8O3m-DiBGePntHt8IbYy8AVj0_0zwnqjYSBwHLry8GAi8ApT7N4pH_gi-rFeUp8Qwqini5WL_cmDCNoYoheAhOhxTtEIVf_S5WBiwr6i6VgxT-6PUXaj1cuUFzfmKrjsuM2QKp2pLIat-WIVBwjTM6Xrc-M27bl_ApOO5RMwcZ0wr3g3QILuN8rw0Cus8s-1RuiWoMWHuZlv0YeIfMpc97WA3bwHL0DDfUfvERAl2b7gZ3wN6F229MD6XL1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_spFxFTu_c8XG_ELkAKuNmg6rTwV9dkQUF2qvv1J4GinXjMnay-QwdTkR9comJnIP8M3BMV3noxNfdk-_ogsFgW-i1qeFONp2ytXTE4awkS2uMOH8V57SFZT3aehD8f1VXDsIyliA3DjqvfXFu9325axvksfLUn4GjxqQ77Uv5n6ydCXMQBwVwzwPlBTZEdAAB1CMkJsAf4Q8aAjOnoDabh7N3ouL7KLqCtqXcCJ70a-3rgu0QpECjmXmL7Eunz8uZoqAwpHnmj4vCn77i78sGytOEOPIdKntSHODSMwREcCcQtIA5lcNLwWop7yLedSQG2dFQBeDzJIGN7rUzSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=f1bWeUD2sAH-2xARHj0hnTBfjFfw6N0yUKuER4UE1K8iWVI86OZWis0_LUt2y8wQUKxu15guRfWdx8-6LBznreNnHkM1udaqjEQoZpZtbblMMaqGR3uI_jb6ybVA-zP8v8KtiKbr_5_92s-ZfFi00P2nBBYWz9OQ46mIc_fFJT2sJzK9JkAXXQm46Dyyb7AVtduFLPUHfuChnDE-mg092Hijm0HFgCgR8-m64s1MwphyYULyKHF3yjz0baGbY0XrPOXFPnCjy1iLxL1yIekgvltKuOKXkvG6HFbS-4QmK61hwv-OKSnk6V_G73r0xfgb-jSz0Y1Z1zjuaNDOzQZqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=f1bWeUD2sAH-2xARHj0hnTBfjFfw6N0yUKuER4UE1K8iWVI86OZWis0_LUt2y8wQUKxu15guRfWdx8-6LBznreNnHkM1udaqjEQoZpZtbblMMaqGR3uI_jb6ybVA-zP8v8KtiKbr_5_92s-ZfFi00P2nBBYWz9OQ46mIc_fFJT2sJzK9JkAXXQm46Dyyb7AVtduFLPUHfuChnDE-mg092Hijm0HFgCgR8-m64s1MwphyYULyKHF3yjz0baGbY0XrPOXFPnCjy1iLxL1yIekgvltKuOKXkvG6HFbS-4QmK61hwv-OKSnk6V_G73r0xfgb-jSz0Y1Z1zjuaNDOzQZqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=tyiRP8jYBl1xBV3XGEoXdP8V8eOvRc1CsAAM8rVflZfgkjPR98PTVFz5g54MZHk6WrgeySgv_nau8KEUgFOX7wvonG_TkUySIZNsuBJR7k_-d4g_JEMGZZPnTf9iZwR97LGTEFCPtX5OqSBUY4Fm3ScdqXSkIP7tjQZdpg6B5rHhGNNkF-oTF44AdnKk-HmQiF4yX-7BYzkCEw8jzXokRm8GuJtMHZPyM6GP1UQjf8AoCp8yyFaJkJvqNXaRyjHxEI9a3KWj4YfooFTgoc84wXF_MOl8AI0KUgdIEQG07_FI-AnEYjpVPvJ0kaUIdAfxu1Cde2JotmFh9wMGkRY4zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=tyiRP8jYBl1xBV3XGEoXdP8V8eOvRc1CsAAM8rVflZfgkjPR98PTVFz5g54MZHk6WrgeySgv_nau8KEUgFOX7wvonG_TkUySIZNsuBJR7k_-d4g_JEMGZZPnTf9iZwR97LGTEFCPtX5OqSBUY4Fm3ScdqXSkIP7tjQZdpg6B5rHhGNNkF-oTF44AdnKk-HmQiF4yX-7BYzkCEw8jzXokRm8GuJtMHZPyM6GP1UQjf8AoCp8yyFaJkJvqNXaRyjHxEI9a3KWj4YfooFTgoc84wXF_MOl8AI0KUgdIEQG07_FI-AnEYjpVPvJ0kaUIdAfxu1Cde2JotmFh9wMGkRY4zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkcJamdfEIss8PHlH-YzCOHKfvo7tH06cFC51d0KshJ3s39rF1aU0pQGvx4kGKiGHGNBbSLo2LbJDrgMCh_6wpRNOD-e1-2r2r7_sRTwGdRWCjFOymVacvG9YAeWn5QRd14LIem7G_LvMc5HG4A2sXGUXDQ-_kY4son2EGJv4NvFLFjIkmhYE9Y5ptHJwin645R5c_upEXOibN4AGzlBSAqkGV61x2430U8nH8-vYfwLfN20ip1vwJi0M0fBd53gkWdxXzezkOfgkpOm_PVmJAe7a6RJhJWHxTzP31-6qFdV8yNSAyY6Hv4aVmqi2iG0P8uwBhPpnucTDNBeCZTxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrsWnO2-aO0lK67lcuZBuQwRq_StXg_oQ9Og0OvoWoHi14igzzDgZAmVZ_V2nW5NyjaoTwV0fIQF9042CIUhuqRUCP2xm9dm0TrgKMPIOMqt34uPnRqbgy0s2-o6UYBi5MUQ3927I6EtUzq_4mm71rx97Qn_WSXHmE79wXwH-zusb5PpB70L2j7uCXGcrUrVs15ElabTIbfAXhYqmNRZfZHmIOAELByi-pVfd8UNVuM6JdSz66fc6nWyH7I9heA69AwVNYIhO_0OUJ1bkZAffTyjDHkNPH40UPwLyU_2HKiFf762r8rx1Ys09YGn8-h-Z7jmP327IPw76L0iblbQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9qVrkTOU-Sdas6Ym0fXFkYD5QW4zNIiVujbGMaJbLUy9nPCWMDQKyXpgvvMgGXxT-VHg2WGLbUBh61IBDXA7cqcKZU_rjml5tUpntFIrHH0g4H0vFfdiAweFLtTcExn0oriv37TyOHKHk4aLOAT7KkFdG2A2gY9etWPU11HqzagIT77dzh2VJp7EtwilZ9gFg0KG2vXAcLTZO7oeKvaIN9N59zYSYt3uG4aCIN0ebcIntDEioIvlPrtzxN1Q22Dqyg6YEKyn_xuKETfHwkOUZjfPk_3tKVdjlGx-MUXiivcB8MaK824-LfLj0u1zdpsKLFzXJ8Nh9nfmuvlKD4NuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur4cC_O4-rwZ8u_to40cSBqtKhJ1zz44ZP6UWsAX7cu0DG2TPpDFymWyZ31phm-YsV0k5l9Orb4AM3dBfC3IEuEzvMywBIh63Wd3klZmgMsHVZBvdAz9fhuGfFvgUJwQFffe6VgIo90LR5qHq005gc3ZSSQbpbAmqFNiEPSHDbrMAGyFSFbLLgPfllHphAENxDqXnIpP8daQhx8B8uiOirWjedpwVkgx3F-6KZWoxCpzizrf1iIHMSRPsi68xVs7SiOO_Z-2A9t-VaKMTH421NJoKMgm7j-0DitrrfRw43pR_QBshPx-JMauFGhOkz7a00DVK49L9Jsiw6lAykzo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2r43lNbw8eN_MD1cKjhDRR9fLQx_K5CZb7Yn-Gx69p7P80plkLF_q0rUyWNUEiV8e5XZqTtevJZ1kG9mlC_184RGGKNXyFREaYORHx6AOe92U5QxZu381i90z3uJjLwHRkKQhf0CT7djgx2LEw4lhAF5-zc32ImLy5oDg_nTCk2_B9v0V_qnfBRG0HKvG6vGLM-3SiOnEIADrPWznli-rQAJnXP2qH_BGGwoAhXzRFqbIVoGDN2tbIGiJkALPfPvvQjmLdtqpqaIoEzE8cXn1HShkQWaUTLQwa8TB6rPnWUCg2ljVP2OpvYFZsREqYF_-DiGmbcIXCUPORJnFLOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGbdf8fkqTO5hH8tgNOphKQ0Ldv7jtAdB_6KCT-E_nwdtFJUct6v8GRFA2ne7evkG_ORH1G5hYkzliyS8As_7fmbIF0nAr6HGBjkrI4z0bmPCadWSCZNb3gee07EcQ8DVeBvyWb9gqQAyOftIOdb3KICwyT7eTdzUVj_13081gJyscXAcfrrr65KXg4yaabvgPnyG-231l9cMmUc5UtGd7hVZelg9ikb9w4qRwXiWVcAi6Q35xmgX87rYNXfC3D-lb5mw5FLUhkcwbTm-Nmlsz6iqD-WXX8w0jiRPNbcsBBvbrmK4VTDT_r2Wip1FLvblPd7NuI9yyjMHJtAQV8UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYVy6nMWbTz2GNNI2_8qQMM06BcbaKSAZOUkVOrBV4AjHgS_nFBxToJhUTAwMyjW67rdVlvN3wn7V2sZFdnPJoaqe31fTIelR6okdSp4PtxX68MQP0Ahv_3L4uTcwa6TsPC6mqxdBmdLwMt2BGS4gnnMZJ8gH9OP_QeQhV2BTok4lqkUxx2CoYD7GwQxYJkTQNHNdpl99tzDE5YRutpOLWuh0OsO8PewnwbH7HqvZSx6kNd9oWlM36IiEu0MCCjJbxjeuwQWguPH_ZY3wtwC7giT4RZtONE5llbOj4dEBPQjTOu9ks1ChQ1HRGQfmsh_FSVuWLSc1WRgxy4GQGLYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRG8RQwCjikMa6GQNvrD5uHPKk0CuaugcaZvQ1WdOtGlCEyJvAzOGknFHBpbXak5sIdTf_3EfAwJDkdKRSJEkNEgZ-5WNkYFpXKhRWfUzI8S7G0VGalSneUZQ-PPr1DC1ArnNiQ-015KDPyZUEDFD0H_sLTMa_xQw2OlhNqyjv9LT46W9lRLNBZmaenREvo_rnNW7QRMzAiJAG-Dbpjd1qLgcrOkHGtdZfxDR1RJBOO4RBPUgGdouSzSoarCwQhHMOnMN99lkbADw9cf-kajzQWywoX4nDv8D3qLAnCmpkSiPXrcLRSUFfABcQRNeg6fBJ34C6O--_h2CGHi9ae_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTcmwhLe3H46GT56tw6IM6Z-XJ9B4WXekT0vY3LbIF-Gd6bjTe3kMuWRksj5m-N9dPhVc8WEqvTgkZKBBSHDu4UUtJxIbVZfZ7DHVB9BZtMOVMk72OLqCIvGjXfY6tu3hGb8A-vmpm8lrAhd-clx5YO0p-kcUKzQlYLHWDmSo3biQbqGC2Lh3Xu8eDDoQHHnHdFDJ7JJxzw-TWm8Bi_nlKUVPA-5j7XSOS_pQU7ImLIxhnupVMk7o5a6cDkSy1acrx33IckMiM9iDxFoqwyYrhZya43rA33keDbLjUY3a_qkugqmjpKMDBgdWevRNpnx3DF3HsdlAuC_pwTYZFiqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MErMS0z_89nnybSaGrCTzTOrMmfs01I-sR3YTQjIBG04jweVW4KZ-gVgpMQ_XkDm_xHvXSeaYA92eNyiuVMYWaIT5aQyHsy12o6TKqAeSovOVtNvuDQO6m5NG8dla6wnHE6GC8yDxmUCRjWrYIqZHnQ0P3uu99XmvjdVYpXdg404rE0TpB7JRn6gai1jjRX4oh3kuKGg8EZxeHA-rEAw1EddnCs7OKXQvt4eVoWSOKnbLSvnxo1KuRL-GPW2tXZCk2kdwync7_7Y2UERXuRwH87pmCnF1zrcg_P09A8PtpvweK8wfMeDvZllVTbXixSLg_DvwK6hNvkgTCCNHvuN9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=elRrUot0k_B1VHhqpymMJjaTQYIAei8NwPZjFxaeQwsQ1yct9ASJyXeIBp2PajdBi33LpA7p_MprqMJWNKjEh_G14dibelZrVymqdro8SjBKJjR9kkRiONu9Y_S0LnZn5o9iQ7Z-zfHo32wTZkd-zDiJ4L7oRnWFAiPtWYaT_NxNer_NEdyi9R4TlYUrKHRvBznSuviIDoEcW5uF-nTkvd1lf_uy--3GOiyTfQXWTr0ZN5l__Jk0hAgxd_PZNLoz7GajsvclH1FqCKddGjAn3-FGg-qKC8oCZq7dBO65m9--XzS2Qkyd2r4ZB7Ub32x9sAvJPHhYZsMB5Q0m268iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=elRrUot0k_B1VHhqpymMJjaTQYIAei8NwPZjFxaeQwsQ1yct9ASJyXeIBp2PajdBi33LpA7p_MprqMJWNKjEh_G14dibelZrVymqdro8SjBKJjR9kkRiONu9Y_S0LnZn5o9iQ7Z-zfHo32wTZkd-zDiJ4L7oRnWFAiPtWYaT_NxNer_NEdyi9R4TlYUrKHRvBznSuviIDoEcW5uF-nTkvd1lf_uy--3GOiyTfQXWTr0ZN5l__Jk0hAgxd_PZNLoz7GajsvclH1FqCKddGjAn3-FGg-qKC8oCZq7dBO65m9--XzS2Qkyd2r4ZB7Ub32x9sAvJPHhYZsMB5Q0m268iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcFaJjfyd7qXGtZmvMjhpckWrSprOylY8hTtFLM6BunrTbgzWgEG_erqzPfEcDoKXvGMYuKv6YWnMsXiQo7bGfJPwg4OLI1hnsU59JR47JPpTICMOrLg_jmWrz1rgpglWx13ZJdEw6wIZL9W1JQA8tzdWs7kzmF8JMt4o3SQuZ1B_M1p-4mCaHmHHr9EDnzilJaTXr-x8DcMhRQNQC8GcwdIWDGoRo5sJhQiY1Vmc-T7fwXM9Fo0t-Q6PfR8UCtmbpH2l1WBvtirdZpnGxt_-XLVf-uH4gK_dqMbKyyKsviHmcGFr3rqZ4V9R5k1TZSKS2drqI4fQ0XAuK4LDOAjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgQN4tBy55qARtsX18NhBU9iixay5165eRWzgWzXlE7DhFwaJZxggHJZMlE8F0aDf03DIHxZsd_KZeqgDa1HcFg6aqDCu7aIamaw6rlbsHYThh1Sx1hF5dUJCKSNbTMKuud_-IGsa-kZV7_vOt3XQ-4L7Exv_MDZkH8_i7quj6SF9wg7qlpKHXwXo0VDPBGafHVN9JEvfxwQkVFGhLsnZxJ3SzsnhzyQId80j5bnbBssTo5YhebM9brM7CAUPU-J1j437Jfu6x_EFk82-YyIsNVaMhwtAayyAvtdpoX4Ej2ZZXHaRNw1cRle8lj6FIJG8iLQkA2E_f2SpfoO-fjK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=egWvFxe5iD50FUTf3qnj01dQZKJrbGK0oHfCCd3bOQyT06jh6O8otJlPfY-3AKTyW05qkGHBYHJ4NO1kuNqDvs3Qm8wz8YBFeGl2G7GdON4rIxeRBTDJyB8qB-Pp8bF0qWCg1fCrxTsf-xhkNiaEr7xjdEwn7a-PdUOGT2M2GbTup9OK36CTrDv9xhxD9pgLvhi9CCD0vgEqIRr-5McGvJO5Hx8X52JPhttaLAcOjT6d5M1oP5bfNTuRyPAofw3_zV8RgLYcmAOK3ETrsX0nXsZihg0unTMbAqy_Md5Uqb-nJ44ZqME9pqybFTA_Oa1frzLX4kjfhPNdk3TDrTLpBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=egWvFxe5iD50FUTf3qnj01dQZKJrbGK0oHfCCd3bOQyT06jh6O8otJlPfY-3AKTyW05qkGHBYHJ4NO1kuNqDvs3Qm8wz8YBFeGl2G7GdON4rIxeRBTDJyB8qB-Pp8bF0qWCg1fCrxTsf-xhkNiaEr7xjdEwn7a-PdUOGT2M2GbTup9OK36CTrDv9xhxD9pgLvhi9CCD0vgEqIRr-5McGvJO5Hx8X52JPhttaLAcOjT6d5M1oP5bfNTuRyPAofw3_zV8RgLYcmAOK3ETrsX0nXsZihg0unTMbAqy_Md5Uqb-nJ44ZqME9pqybFTA_Oa1frzLX4kjfhPNdk3TDrTLpBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=MCmAMoqrycP21ojbvqDgeBSAMnMe9e4TxOIFy2PMYiGMn62fTsmvFg29RW7HLQXtToowSvxsX9JYVNMwgQHCPGfmmxwJQwJeKE6g4gWfdp9XH2ihzBYE_DpF5fCTwWZlPa7cfu7K3CrNKn-wA1xBGLb1Crk25f7mSiveJRcFPG7h7dJ5HQfSGneUwB0zOme8pu5T-qRoALYgppE-itbCt3Y4iacs7-4EMbvYQAttE5OKYttKHaPsXg-1QMwcBMBfcdDNtRa8bNpYlygDnz9SOykpdL4PDddrIUPvNUekYphLebxXwMFKN0yRZuES0j-ne3Ae0P2yVIeZTkArlhA4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=MCmAMoqrycP21ojbvqDgeBSAMnMe9e4TxOIFy2PMYiGMn62fTsmvFg29RW7HLQXtToowSvxsX9JYVNMwgQHCPGfmmxwJQwJeKE6g4gWfdp9XH2ihzBYE_DpF5fCTwWZlPa7cfu7K3CrNKn-wA1xBGLb1Crk25f7mSiveJRcFPG7h7dJ5HQfSGneUwB0zOme8pu5T-qRoALYgppE-itbCt3Y4iacs7-4EMbvYQAttE5OKYttKHaPsXg-1QMwcBMBfcdDNtRa8bNpYlygDnz9SOykpdL4PDddrIUPvNUekYphLebxXwMFKN0yRZuES0j-ne3Ae0P2yVIeZTkArlhA4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beo4gj8_NxOJyR14Lj1KABe5_X1MZnGOHrPLwshp7is5KfneewpAHSP3sc9EXw8HidXh5cgOjT13nOtpC0nABxKC_HDo3oqhgAZlyOJSRjLaG4Yg_riPXB2Mf80DUsEtOkLHgTtNeOt279zSqO8tkr59opHipaffeitoYmC4bVEl5SC10YxCpMulGLF9rFLdgQRyMr01bbRwDM4AzaipBm7ijHQEOzKhC3QDOUJlAzX_tHv4gY9T5u3Zu0fxs4I5er2KC6KbJaqG2tmgSSLfOFMFgcyNgshbW5L7tWQM9HzQMVItLqNaM9K5LdBMn74dpecIzcJgVTwA0joKkMagAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pikroo3oOEEFiBcDHEFtRsGxFRTtOKMysTxKH0XdIgC_U6qbhRTTS9ig-1_FBxMcG82bIv9k5JQxjLb3pYWRB4_e0AlT5cosAIiM0jxk066ifrMpdgHZml_AgMlff0ou5nabrTIgkvnEKCOse_JgV_WXe5skQHRXHgij0W4SlhdR4k2cS6Iu1GJM472R5qsY4QZAJ9vyyRbmIVVsjB5V5T-9CyA2nEXa2eLIxC22UPtd5Zh26MXq1k9Izf8Rcw1kDjqklOTofqeC-WaRaN9135IF_NBAwNToQU7xOFVruxZyrrZIr8KIQNrr7FsyvhH-q4Cexf-2vmzSiIwp6Sy8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcINHpDGYQ6ezk0uIa-gdxpPglLZkXibdObOSm9i3Mz4CecTFJDjpHJbeEbsLrOkifi0kgzEOioBiQVUgW7DFL4lyKOdx_Dzs-PTnMKHaNKqvppr2STFt2VCx8_p32Si9n3zXQG8iw528qzcX0MHxQle8pD3GwjPtmkacz1NeWy1M1e0l9c58ytBFfvtQ1tEbRFYUjcK1rhkmJsPxyJnpfpAx4ckd1PZX2N34M6wN4OzztP2j2rK61Vv7BtEaI56-BKEqolfQYVrKHB7RqhWmVLKKoATXk8yDBK5qBcrOvU4LELNTJdWVOeT3kvA3P4G2Rw6C9atro4mGoQTFHewXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvc0XcCBj5SjQdyvfJyoyF5t-T6U4SzqzY38y6Lc002i9tDQMX2pK4Zp9Uhy5MdWrsOvtoG5gX-nf7V9qWfeDOO5MfpodMpqwzSDSIhMNUV_8V4rl-WEYX28RdU9B7mARH4sURNRNPBUCUdTvpfDimW_tt77tksuf2Jb5J1-n7y2p5R1mBrBzGuW5MGeWrKQGKOEUrtBM34hlDedhJNB948wPkHpCuJ2jKQrDzRmyJTn-zfhXNUjZdbYPlfh20C7PHj36nMCmPHsjns9T6iaUSCwTAqGHPd-KOaDWKpum8cKD0JlQwKWStYZXWN1D1vw2GM1rowD5i4CDuXO5d7yLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjTrKy_43z3KKQmD0qqX2beakIp1IrditGTSJkZ-7Pqh-v56e-pAzl6nbTwyDwwI0HjgGQctrERGauLNxGNu6rPDLQGs-Gu3QtifwPomTE_luSa5AI8s-Pe5eprwxf3BXirSRCyPcFgZJ8b81j_E2RP9Ie8733jJJHclwv776_9wukmrr8r3noCzT6ZuLUID32CQLUKeNefmg3Ymm2rcrokbSbhpYtXtHGdM-YyVCBNpK6Ow-Ot3Yzr6dpv5PZmz6BYQmcFWKgJzjN5gn0AwIAVkqFtVzbfHgG7tD_THvoYyaX4y393zkFO-h1uldOQaPim77iojDhx4BpGMcmhmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjjFVhFU62CA_N87fKtWlo6sfatpYeRR5HtOk54UHw_ZnEIqqJe4mkO2Vyvn4ZVD7w_tzJdk8CtFXUS-8GOsWc96btAqilWcu_bdMjzAuhjAXW4V6m4__J2WCzjFsUqkqDEUIRMTURJauaUaMt17ZtvtVxCE9ri3x4YwVcah3r2wvRa53raVXP8iAQeghUcNmMXO-5K_8KVHxFxIAQugzmD2XQ0TtYpv-spgShqRCqTYjPYccN5icoR-w6s5U82toQAVYyV3fM4MB7GjJT5vDuOg7TSEWF8gIzoLOZDwQwJmA-mZzhH2oWr_BjoulM-wfAnDP1jV-QHS6O36TgzkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK_DcmpzIZgL8NnZ0-U6DUUJTLxApN9dJXUi544FrZtqXXNEiHEm9s_DsBTTgwHV7RGOZ0wH2i-nJdq-8-aX9d1HhNx0zPDN0aUVwUS-5TY39r-HbNG6VfNOm1ETti07euj0tNyl44NS6L3ZWxkP325xLC6oGFYeD9RplSpMXAceQ47sL6M0W-vrOcfTfk-A-EaE25KVtmMxeFOoDWOd8k6lEJCeCFoPBj3DxmNYSZRCxCDFTJe4hsIEdT50nhcGAP7Snm2KcdCIL0Y7QgjgOWWwRAWpwbZCMXBJqq_1_v9o5NO8AJcujyNmDwgK8tNQaBUB_vljtTBmlc9KctJQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg5b4lZU_SFdnagR6AmbZKJSm4GzG78T72RXe9Wvt5cPv61op52gNPuR5IkUY-KBuhOLUW94t13FLrhA1I-CoujuMTRpjYPsJc0wIDh6AF05nKEUFvm3V91a-N979Mx_crsH0anRYy1wNAlRZgDFFVwj3FfVS7inng_aKPIrcIrztbdWB05U7nsTPNj-BZSs-FNffiDe_e9xjfKFudC556XbkYsOw93l5E16ueHwpTfYtj0Z_MGS2qlLvvW76l1QCM9EC_v-joSJmHBWahZf0h89Jk6vD4VVQ8o3ynmdgowoLTDR2w_FACmKT_U5rp1jXWAm8VK75JZqEQnU4Kub1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
