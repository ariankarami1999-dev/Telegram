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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 09:03:26</div>
<hr>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=lM6JzVc6xLmKxneUmQwTaN2RCzAep6AeemDmjYe-oYXNGFgV1bZv3hbGeaDnQg-EWgyjOkXDE4DDTY4TDTbVYMlx3d0H_dKNxeXxNPHVK9mHVM7ipQBRT2Z2cAKZqnx06Sm3ZweE61Q-VXrsyu9CRgdZbSHobLtI69Zj_NBCO-EcQaIFE3Yxl76somX6VhI4k86cjdAsmRUxAlL5n5Sw22wCIu-uB8xdqY7oL_IPI9DCLCOc2UlD0Hm5MEoXSWd1iWVKEjlMsmfJbivxVUyKdQE0Co1eH5JfcogWhSO3bsayfjwCCqICVlZFtR_eyY62d4px6TJV9bLlloemHYoawQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=lM6JzVc6xLmKxneUmQwTaN2RCzAep6AeemDmjYe-oYXNGFgV1bZv3hbGeaDnQg-EWgyjOkXDE4DDTY4TDTbVYMlx3d0H_dKNxeXxNPHVK9mHVM7ipQBRT2Z2cAKZqnx06Sm3ZweE61Q-VXrsyu9CRgdZbSHobLtI69Zj_NBCO-EcQaIFE3Yxl76somX6VhI4k86cjdAsmRUxAlL5n5Sw22wCIu-uB8xdqY7oL_IPI9DCLCOc2UlD0Hm5MEoXSWd1iWVKEjlMsmfJbivxVUyKdQE0Co1eH5JfcogWhSO3bsayfjwCCqICVlZFtR_eyY62d4px6TJV9bLlloemHYoawQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgps8NOQAYsHqo-C7w1TlHrRd9XL8LwNsfFZmHkgNogJTpgWoWF3EGCUGOlkitEOewg3HIpjSC0Q4O-Ohsk9q6YVMzHAccYh8bf6N7j-1n5tFMgyvtqXzqaNRTpZxKDG-knsvFwk6nau8bJlULZHUQm9eBc57QjbFXMllC77zxM6GiBuhV8Eu8CzFzSLpsbLrosxRFuiOiYu_2FxhqOSAMimmpWNULGEr836M0F8WrpwGL-GO8jahtedlfbqk25W_LC7DbcUqDn-PtN63KMkbmZIQZYu4HQYvGuDbxyqSiwDkI-K37ApVVxSvRMJtsOohrW-WXwgAafkG4xKVdc8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LRAaqsmHThwCVIappFeoKnMd3ljpwiCLf1P2EQ4ryev6LCVaLTHOHiZvQ6PlEqKbsEYAzPMuT1iXURduUBbP5cB9yt04W3SM32J7gyE9C5NtXJHfLz2fCq8LRkvb2ejfJljMuWIqSF_Q2vXNni3-MdLUR_VgF8g6m87-XQzl4xGSLsrjfvWhJe26tWItOtw2uaSOlKmlEzaUKjKtfolP0cNQocY3VimutH8F0Vx4C_jYvwM8QjNzX-wlgPdb4Zh9t7195cixej_LFQc1MfE96LLYiVKcRIiD2bOj5S3Yzg-fT2G-OY8LWdXRgukJzh8PVSf7-stNCHhCq3Qk7lESds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LRAaqsmHThwCVIappFeoKnMd3ljpwiCLf1P2EQ4ryev6LCVaLTHOHiZvQ6PlEqKbsEYAzPMuT1iXURduUBbP5cB9yt04W3SM32J7gyE9C5NtXJHfLz2fCq8LRkvb2ejfJljMuWIqSF_Q2vXNni3-MdLUR_VgF8g6m87-XQzl4xGSLsrjfvWhJe26tWItOtw2uaSOlKmlEzaUKjKtfolP0cNQocY3VimutH8F0Vx4C_jYvwM8QjNzX-wlgPdb4Zh9t7195cixej_LFQc1MfE96LLYiVKcRIiD2bOj5S3Yzg-fT2G-OY8LWdXRgukJzh8PVSf7-stNCHhCq3Qk7lESds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxCZqM90KVWnX2sBR0aPmmOl2LJFzVU8ry9RNId1sWC2ngzYKE1D4tre_Cv46WDTORTqmEp8G6UYBJtEFlxA4XyhLHhZ3h5ZI9DDqbGUj3GHtR6YeV_tD631Wp5p2dJdMBFp6FlaIkt355Qw318eDSC4dvfrUGpvTcZmcUIEamoua50ELP3nlBZ6w3qTzH8OGpFBjndCwEAV9dnorMOtUUrD0U58t0dg7jcPLmcTtdqTyQDnNkckCsd-1wq__3yvqhdcsvkOBRfb1NTEQ2TsaeBPl8mZwT-ox1wqsRS1fYjUW4Gl0GS9Iy-GSq0d_uRJfwZx-yhm944LQtz__QTZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rY4fepG24-lCTO8ulPpH1z0D6Njz-dEVo_WUAjzmA0VXF5HC9FxpIjg4Cbq4qlI12X6zks_4NtCLxH0k3g2oVuGqa_hX6h3EH5KzK09mK0tM9aEg7DSIJJ_R5Y5-dNfJmHWIBssBbk5RqZOqd71volqbvaVgwzOYVeJ0fMIybI73SfQKMlNlXc3WdYR5Nx7D-EYoiVkBHqc2doVwq_QFYP67HATAQu8aIj5oMb9kgDALWLw-CC1MQvQA5sPtedp7oiJp58ccM12tOChQh7ybjCwkvKNmqa9Z9MwvXzOOlCeBuXWPBMSU3HyUCawfotkRyEQdN8ZTm5AXSN9SQWdmIGiGMvrTTAGRwU5yZ6zLJEb25bgE8jAyZoqfvov7t-tzqY7VFnSpEmKQPKVEBrb9qfj_H5FuZogH-WN12DKFuODILIFV5lJAAYisPpFgVot7TKHw3H-VGyFIKAM0hXBno0kHAJ5XF1HNf72aOURyigRw3_Kj7tIk3QokAPZHOYZQAMm_Z3Z1nXPzy_HrkEFSzR3Zk6nUftxv8rnYa8jHsqAa-o-VUteKvmDWRYok3WudwSnQoqRi0RhKtfhkMG78t5awA1TT__Vw2NFSziowMwrq-ouz60SVYxJjDQisRtYvUHI-mUJOGFaPV1SairONwVQkSqLJrzPLu36JrMOcoM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rY4fepG24-lCTO8ulPpH1z0D6Njz-dEVo_WUAjzmA0VXF5HC9FxpIjg4Cbq4qlI12X6zks_4NtCLxH0k3g2oVuGqa_hX6h3EH5KzK09mK0tM9aEg7DSIJJ_R5Y5-dNfJmHWIBssBbk5RqZOqd71volqbvaVgwzOYVeJ0fMIybI73SfQKMlNlXc3WdYR5Nx7D-EYoiVkBHqc2doVwq_QFYP67HATAQu8aIj5oMb9kgDALWLw-CC1MQvQA5sPtedp7oiJp58ccM12tOChQh7ybjCwkvKNmqa9Z9MwvXzOOlCeBuXWPBMSU3HyUCawfotkRyEQdN8ZTm5AXSN9SQWdmIGiGMvrTTAGRwU5yZ6zLJEb25bgE8jAyZoqfvov7t-tzqY7VFnSpEmKQPKVEBrb9qfj_H5FuZogH-WN12DKFuODILIFV5lJAAYisPpFgVot7TKHw3H-VGyFIKAM0hXBno0kHAJ5XF1HNf72aOURyigRw3_Kj7tIk3QokAPZHOYZQAMm_Z3Z1nXPzy_HrkEFSzR3Zk6nUftxv8rnYa8jHsqAa-o-VUteKvmDWRYok3WudwSnQoqRi0RhKtfhkMG78t5awA1TT__Vw2NFSziowMwrq-ouz60SVYxJjDQisRtYvUHI-mUJOGFaPV1SairONwVQkSqLJrzPLu36JrMOcoM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjOPejWSUdi53qqqIFK70qjmiWOb1U8_H4ZLo0YfJaZtfUkPi2Sm2aHm3MQP1RiRFmapa6ocf_4yuf-QfCeLRFbNt1y07OkTjXJxmZIdz5cYZXmjfY9SdKtTgGA_GaCInhsSfbt-oZGRwmZyFwnk4oOhZmDIGCkkgmOhmvttSLB6vBetu3GJXYifRu5Jf6nnoEilX1FscbIMuXg7A97jmwO0YfL6kyK9SPdGlrMTyJTz4e3pPLsxekAn8NJKs_X9N8C1VpST2ioOBbv0dK3ufsCyv_CVSiTSuJJXxI6y91vMuIr1VUMmpRaP0YWKdGAthTPnEPdzxL4fAszjiOmNDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=SpH1oxXQXQADHnvydWzCJAKkHIl9vT_vZVM4Df7YTgyV9HOfdBDRWh738wO2xN5zo147tQb_QKa3XO3ORyo_wz_1OFxM5VkChItyLMygAlnbIH379XV3YKhC8ES08bzqtbS5FxkaL387fWCxUenNVIR-locFVCuBydDq5Cu7oW0_ij53BgbOui3cFZd_EKUY3DGVmFBmFTOgsvZP_uKBTVOe8f0ic7zgQ1rwCPr6pcE74M2P9AvlnBQCp9yUq6FfycHp4MvRScdxymg7D_DWPP7sHEYL3ENWFvohwV4UExKVDakcwwOw00YsPxf9IEwgSKvvK5_OJzO1k_hWdeTcyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=SpH1oxXQXQADHnvydWzCJAKkHIl9vT_vZVM4Df7YTgyV9HOfdBDRWh738wO2xN5zo147tQb_QKa3XO3ORyo_wz_1OFxM5VkChItyLMygAlnbIH379XV3YKhC8ES08bzqtbS5FxkaL387fWCxUenNVIR-locFVCuBydDq5Cu7oW0_ij53BgbOui3cFZd_EKUY3DGVmFBmFTOgsvZP_uKBTVOe8f0ic7zgQ1rwCPr6pcE74M2P9AvlnBQCp9yUq6FfycHp4MvRScdxymg7D_DWPP7sHEYL3ENWFvohwV4UExKVDakcwwOw00YsPxf9IEwgSKvvK5_OJzO1k_hWdeTcyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cEyh-c8YVYFsOfkfDj9u1-I9RT181bb0OFdHohpS0w83bAKVCngZrgcJku4SZvzNJ5Yu_bXrjOQahC2Fj8W2-jO66TSZbmlXKAF8Ah-C3yCAtvU3nOAqJNScu614-bmn5eHl-rZwuUN2OHMC2alAdNgf6xOlFPNmMPVedFsioykcqKW9CVenfYqtydUtgOtWhfrCQIsdluJ2quagron3IIlhLAsckN9vZT0KpyKlsZ1UgCc3DVNU9gBQprEBoPQuK3kvaSM_rHyVmwfBKfZVPXuEURVb5HTk2OjpcYOPOlV8DuGYy0wdYYgvZELR8uLVcYkFV2AQH4DjwyBSOGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djqt7jeTchA0KXPM7lqatwKNrBdLhkqgZ_1hnp2CpInXaUlH89WnjTeQuI4AeuFqjyfOgKMbTYO4A9bsvsmHFpWJ2h7Mw18uFbHJN9E9h0s2OTWKKuWbiHH5x0_ndgmmZpwqAnDNLdjjjBK5jH6kere1u_cW5wbe12EywgaIf8VjuquPrVmZ5QoGxCcv-avOC4Hm2D_wd5hySonDHtD8BSK51WPdioq_5gTJtzp3IUfV9zvRKlMNXKpd2ufeSj0BKUFQsYItOTz5w1Ufnk8-MQWw3ZvFbw7QQYAPhpMeWPjW5iVklAldgMuDRJYNhdDtX0sYwVW1yfYjZqVfVFv4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmi_K5Lt3QJA26TTMCHJ-nL5DV96LSjxrZ3QUDZTl67E6p4tEb_4PpHkCuex-eS0z4-De-DvgtdYUQpscYMrwX0ovHAmrjZ5y_MyhxGpURAS3PvprxafpO-iofkrnIMANF3_kjpErN7uDO86965dkDCwiN22nZYppOF-BbdS7-xqkGlW98ioVGZfmQ9KX_Hl0WSlAZ6eDo5YJXEb--O_uZ7VgcC7bqms5_CdkEG6K6k1qSXrvX_uBpJkXI4DGcYo80pKfPuQ-6ga5nYUV170l5fEBUI41X2iVFcKePpk9opMboNrsGnMNIIfr_7DrRIP-MKStRz0k1H8eGOwQCiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Uh4OIVpOrf0YtsBvNoCm1tKzbh5pW7Y7G4BCvfJuAwLXgRDChHng3dopZEVKX-mhgKXHEeOZIX1DfmbpCjjRZzkyfIMz2qLvixLdSAGq_YHmu7C58s-xvtkLBHXs2y5PDAKJQGGGMC71VBMKRPtZTx5sttG4eJ34n-LVdzR-zYG5DQ4aelXV8PjCFtHKiOOWvMsr5I2wptBqRXkUrovWztbOMIlL0JCh-tvFqvMSK_4tJFVcOmIufYiYAaUe615EtuifASj8rKm7IX4RKnPzZvFX9vv6SqpRtRcHtSTGyCFibw8koLgmIk7-Mmn3vqlKTZu0mB98Uuu92x0vIL7ITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Uh4OIVpOrf0YtsBvNoCm1tKzbh5pW7Y7G4BCvfJuAwLXgRDChHng3dopZEVKX-mhgKXHEeOZIX1DfmbpCjjRZzkyfIMz2qLvixLdSAGq_YHmu7C58s-xvtkLBHXs2y5PDAKJQGGGMC71VBMKRPtZTx5sttG4eJ34n-LVdzR-zYG5DQ4aelXV8PjCFtHKiOOWvMsr5I2wptBqRXkUrovWztbOMIlL0JCh-tvFqvMSK_4tJFVcOmIufYiYAaUe615EtuifASj8rKm7IX4RKnPzZvFX9vv6SqpRtRcHtSTGyCFibw8koLgmIk7-Mmn3vqlKTZu0mB98Uuu92x0vIL7ITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnF9zx8bpbTSGZxaQgyRVW3ApJgIi5nDs00GtPz6dQRjUEYRLctTArX4dTDWDEzeADgTCgLuGFWS__KKlFAwTGgP8U3tSPIr2PzTMd-qzxVotz7vggJrbFKieD1KQhPRcsS2_DhZG3XbHbF5nME10R6vYFf6fd9CLNiqtn_TI10glwGpxKBdKFVafSzTzHVCX8Yso7Fa2MV_Z0b6n3rfYeGfWL5w-pBSAbGikHPHJpX-rFa4q3TT7UAH_4kQBTB7G4NuvSYekie119A0S-T78TgX8h8f86bwQPJ-xodduC0IZBXDTvEU42kftnQHRM8M8n68PL-JlnOnynUGftQJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8ZfmM5fhnCfx1xNochfo5SPM8yBCFQYSkSGYDjaTzqDVtT5o4FSj_fuT02RnOPY-BLLdIfB5pbyFqhWGa1YaVWLKRNp1I3fsieClgFdZiNqQqUMr0zmr_xKN04KVieltDV3o8dY_AAoFdHDJAAV2T754JmTXZ6QxoAt9eqg-Z7oU_hGW0aIiXyqE83F5Lc4tujqDwiNZsb9oguC_C9RGfA1QIBHQczvSAk_tYaUlhOP9v8CS_EeodrWDOv58rfu0xU-j92VMuGGXxJtdu-3L135wtDJTVvWHCQb_Pd8WT_MkwPzHJDm7SvSdNoEd4CaggYlImL_DFX7p3S7-snhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=hQRaNKvsGGLaj5xrtfJsLXgu6MrAlIh8YiTay5N62UwzdifcH2e1tzHQ3U_BnrFFbHqp2glJx3UMr7CELeGsF6ytfiAzo4qE2CG48nZfLvqVm35bAUWzLaTh1YXLPGfyDMY_FCjhulzBCVueaIxRd3CAhbp9eiGFKEyTKRqXicAn1OJANzmTFiOncNNClzm3W2WOpva5ygZ76ce7qaaI1Lg9tsFb8iOqxBeC4R8W6_B3p_6jn0oavZIoPQePIxP2LDZk4NXwnhUdxARsvNfRVVjoat1hdfzh85gEfn43YhaBUmvz8uIour3dNjWK__6KO-Wltly-VjJaxxeIoCy_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=hQRaNKvsGGLaj5xrtfJsLXgu6MrAlIh8YiTay5N62UwzdifcH2e1tzHQ3U_BnrFFbHqp2glJx3UMr7CELeGsF6ytfiAzo4qE2CG48nZfLvqVm35bAUWzLaTh1YXLPGfyDMY_FCjhulzBCVueaIxRd3CAhbp9eiGFKEyTKRqXicAn1OJANzmTFiOncNNClzm3W2WOpva5ygZ76ce7qaaI1Lg9tsFb8iOqxBeC4R8W6_B3p_6jn0oavZIoPQePIxP2LDZk4NXwnhUdxARsvNfRVVjoat1hdfzh85gEfn43YhaBUmvz8uIour3dNjWK__6KO-Wltly-VjJaxxeIoCy_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=hI3MumDxQ41vXJI7MQ0iGm_geoqpUvC6a1MMG9RtHYvNlUBjt0awhRQXeA7kdMke_crqXA3Pj72ZR1e0egLkYwykMF_MXoJPiyHcPX_T5T3amFOulFJ1WeGxb-2XA-Hruhse6qSwyQFofD4E_3G7DlOaEEpnKBWPEpEr-ElgdCrkaoMOsEpwrKR6TnnArMZqGlQhsqg02NvH9E6stzyw69QmEsSAupcRvr6E08aocQyHc3taK3e-ZYQdMCQf76Lg0P2iyoukgGQuIeTuwfDOGcQ0aOiXx268he1XuM54Ci2pPqYHGifXrHtVg2CmovB-Y2m6ldWewi0UhESPPsanogE85vkK8A1b5XpyjlmjW_Hv6b3qpHc5JdSsQDN0h9UqkzBbTeH02-YMgFtyMIx3nzEimiu5mw896IvQoc46neypGtc4ISZ76-aToAYD3VJKkuFu_0gkuRslfSYDUyiSqhrfUrLEuGnC0_tKW7eM45uafJuZEgRXO0FB_BBc8b4N5G54u59IZpYCZpOOIH-i42vTVrSufk9fbTp8sghXJJC1DOaOlQJxAkf90dgHccXGfwIte5KXYOcRrezGuI23rtl2KrRkv3oKBKrvYuNpstfyVRkVo4G5i5zPyAfP6c_tlDNNBe-MLAQwPF_O1Fht4AYYw-_ou3O_CvXSv-JXsBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=hI3MumDxQ41vXJI7MQ0iGm_geoqpUvC6a1MMG9RtHYvNlUBjt0awhRQXeA7kdMke_crqXA3Pj72ZR1e0egLkYwykMF_MXoJPiyHcPX_T5T3amFOulFJ1WeGxb-2XA-Hruhse6qSwyQFofD4E_3G7DlOaEEpnKBWPEpEr-ElgdCrkaoMOsEpwrKR6TnnArMZqGlQhsqg02NvH9E6stzyw69QmEsSAupcRvr6E08aocQyHc3taK3e-ZYQdMCQf76Lg0P2iyoukgGQuIeTuwfDOGcQ0aOiXx268he1XuM54Ci2pPqYHGifXrHtVg2CmovB-Y2m6ldWewi0UhESPPsanogE85vkK8A1b5XpyjlmjW_Hv6b3qpHc5JdSsQDN0h9UqkzBbTeH02-YMgFtyMIx3nzEimiu5mw896IvQoc46neypGtc4ISZ76-aToAYD3VJKkuFu_0gkuRslfSYDUyiSqhrfUrLEuGnC0_tKW7eM45uafJuZEgRXO0FB_BBc8b4N5G54u59IZpYCZpOOIH-i42vTVrSufk9fbTp8sghXJJC1DOaOlQJxAkf90dgHccXGfwIte5KXYOcRrezGuI23rtl2KrRkv3oKBKrvYuNpstfyVRkVo4G5i5zPyAfP6c_tlDNNBe-MLAQwPF_O1Fht4AYYw-_ou3O_CvXSv-JXsBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCXwFBPzKMOumTHpWlqy5U29ZONbaX2jMe2S6aouDZEHhGMxOIR-On90dzabDGvQYSZQ4oCWS7aR28oRzHT9RA-8_LetkrEqdnN6ztT9pAgoL2UMjH4gEyzp3PgKSKoQ0502PpwfgV6llPo1ozqidOAqnzRQlKiz-DiUWSHOjUo6BhhqG1XGyVkZDshsdBzVhh4e1T2-l12INwd5zUcyXlRgHzecUtnltW4o13ljWaEa2BD3kktiTRosjOBekMl1ewg2S0ciEg4uX9VZrXm10LBgi59aGzgSTQrRSha6PwnNF0fxeLRutI4oDNU89FJIQVpFAJFiq0sboEszvInkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=PwXuFm1GSITryUmpxZ52LFD9AhdI-oKDjg6HDFDLXueJ72l8bX2L-yIKSJAPqhD1jtYw0bYpSaozX2lH9nYU0pqKWgLf8cIJ7Wp6X7_vngHYLjGSLjTFcAD2eBypA8zPBBYfcf8_caACleOsc0_GE-8TYWKW0P_2OZH7yuYAHwhZPOf4WjwbtOHU3fzbVxbQMrFwr_wmcnRCUoWrpf3tYwlGaWdbCri2AJuSZ-tRE-lQvWj8jA_rAGK_aMGbeU1IMRnOQv4EAjrmDR5UO1CHnrsP2WaLmz9krU7EKOj_D3Wu8jYZpAe0LcssvHMxBfDbL3r3GwHJc21mp9JJ8v1ZabmqXBcOiCrTqDL4lV2ce65OohWE-lRbayh_asaCV-MksRGAgdaVwrv-S8dZQfMOR7lhISUjjTtoR5qrH2sMV_wJG4WDYYfjJpuRe5rj8r-1dV3YhEaUbHnVtMBLY2Th_JWhdulZ8EPG6WzKuzLbRCJCIXoeGyGPVXbGX79ku5OiY14_loKXap_cL8YstBr5tHFyyeczLoVbiyVLjI9NwrBjES20dUXwYtdC_epVu5fsU_OLtb6BV9LCwEpd0gt1Hq9XSma_ErzcT7OldIsYTSq21sryOVnmP1Qn4x5pxPIx8bO2FVV0FdnyCIN8YBMqnp0NJJouN3Ej1uw3VXHLs3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=PwXuFm1GSITryUmpxZ52LFD9AhdI-oKDjg6HDFDLXueJ72l8bX2L-yIKSJAPqhD1jtYw0bYpSaozX2lH9nYU0pqKWgLf8cIJ7Wp6X7_vngHYLjGSLjTFcAD2eBypA8zPBBYfcf8_caACleOsc0_GE-8TYWKW0P_2OZH7yuYAHwhZPOf4WjwbtOHU3fzbVxbQMrFwr_wmcnRCUoWrpf3tYwlGaWdbCri2AJuSZ-tRE-lQvWj8jA_rAGK_aMGbeU1IMRnOQv4EAjrmDR5UO1CHnrsP2WaLmz9krU7EKOj_D3Wu8jYZpAe0LcssvHMxBfDbL3r3GwHJc21mp9JJ8v1ZabmqXBcOiCrTqDL4lV2ce65OohWE-lRbayh_asaCV-MksRGAgdaVwrv-S8dZQfMOR7lhISUjjTtoR5qrH2sMV_wJG4WDYYfjJpuRe5rj8r-1dV3YhEaUbHnVtMBLY2Th_JWhdulZ8EPG6WzKuzLbRCJCIXoeGyGPVXbGX79ku5OiY14_loKXap_cL8YstBr5tHFyyeczLoVbiyVLjI9NwrBjES20dUXwYtdC_epVu5fsU_OLtb6BV9LCwEpd0gt1Hq9XSma_ErzcT7OldIsYTSq21sryOVnmP1Qn4x5pxPIx8bO2FVV0FdnyCIN8YBMqnp0NJJouN3Ej1uw3VXHLs3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=DaPy9yz6cFs773bhsPguak2IsVZGszJ5OCZhPks2yaFFIVstcZ43UDRuoNb19dm_F8UMLq5uYTdII2ptoN-0wQe_Bkom5wTR9HYRFfanjEygUcmxVhcEm9AKC7WAZQNYnOwn0IugCZx2IYymI4fcqUHWOZvuEVR2037LxCpQThWaONKaVoHRwk5xXqBsxBKfCUS4wZ96DmTRdBWVeeVJw38LzfOF8_GegisjgJDkAq4eAXmFArHKj7Hrjh2YyoMr6IMyDVB5xymwgtqaeePgtoiJLlklffYEiP79JiWPeh_0P7hDdtneKFGeQNgcL4EifPAB8ucQOs5wRX78nKy6Fxq20tjsDhlwamKhL87_TC88N4T2KZLtQQfgHc7MiL7KiNNCaxgIqmw26HHJKASmd8aHBV3v53rXwMa101v09WH7hUpAKm-DSd14VJRMG6Jv-q6XoE469fnNmU9Km3yEfOmtYsKgRa39yP4gTRjDwJVQTzgNmXyd6bKtsnA7u5R71MJX1vTaoEwYaooDBfmR5CitFhOwxUoFD9DCtU9UMK00JprSdSRuCXe8H8YwWZ9GUOla8wYo86RUS_GMJWZdRtyE1Br4pEJD8DoYEzVZkqJQ2PjZVcbqWW7tn4v3QXE_OmDnLP2QpjkjY_V4DUMDiexpeUwJYkl0h5L2uGLv3-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=DaPy9yz6cFs773bhsPguak2IsVZGszJ5OCZhPks2yaFFIVstcZ43UDRuoNb19dm_F8UMLq5uYTdII2ptoN-0wQe_Bkom5wTR9HYRFfanjEygUcmxVhcEm9AKC7WAZQNYnOwn0IugCZx2IYymI4fcqUHWOZvuEVR2037LxCpQThWaONKaVoHRwk5xXqBsxBKfCUS4wZ96DmTRdBWVeeVJw38LzfOF8_GegisjgJDkAq4eAXmFArHKj7Hrjh2YyoMr6IMyDVB5xymwgtqaeePgtoiJLlklffYEiP79JiWPeh_0P7hDdtneKFGeQNgcL4EifPAB8ucQOs5wRX78nKy6Fxq20tjsDhlwamKhL87_TC88N4T2KZLtQQfgHc7MiL7KiNNCaxgIqmw26HHJKASmd8aHBV3v53rXwMa101v09WH7hUpAKm-DSd14VJRMG6Jv-q6XoE469fnNmU9Km3yEfOmtYsKgRa39yP4gTRjDwJVQTzgNmXyd6bKtsnA7u5R71MJX1vTaoEwYaooDBfmR5CitFhOwxUoFD9DCtU9UMK00JprSdSRuCXe8H8YwWZ9GUOla8wYo86RUS_GMJWZdRtyE1Br4pEJD8DoYEzVZkqJQ2PjZVcbqWW7tn4v3QXE_OmDnLP2QpjkjY_V4DUMDiexpeUwJYkl0h5L2uGLv3-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=CNfJSy-QdqTRreuoeZvooXIo09moXaGxD7evr57ilC020DsIy8TS8rVsNb-Hfcr0oPdOUy_O58rvA3F2YBnNlQDSlU2uNmeriNeZbHQFXlS03fuUjTxZWcDvuuPJsI7TfKVG25uXjoezTTP9oKfz_O_gUrVTT_ML0P4OP5qoC8DzhqdAtp2QtcpbTwiHHVsl6ofRumXshSxxwUCRLbEFLd3QMTx9ohx6gkGwKrHqzUr-CfIgj3cdM3Hv-VAjSYl476hqWohvbxUUYjgtZWC6AhA2syYXtzBLLrGTGBr_9fW31xMbiW7pIFBcLVqlASQ1c-5XLYXbR1MFFIWQV8V2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=CNfJSy-QdqTRreuoeZvooXIo09moXaGxD7evr57ilC020DsIy8TS8rVsNb-Hfcr0oPdOUy_O58rvA3F2YBnNlQDSlU2uNmeriNeZbHQFXlS03fuUjTxZWcDvuuPJsI7TfKVG25uXjoezTTP9oKfz_O_gUrVTT_ML0P4OP5qoC8DzhqdAtp2QtcpbTwiHHVsl6ofRumXshSxxwUCRLbEFLd3QMTx9ohx6gkGwKrHqzUr-CfIgj3cdM3Hv-VAjSYl476hqWohvbxUUYjgtZWC6AhA2syYXtzBLLrGTGBr_9fW31xMbiW7pIFBcLVqlASQ1c-5XLYXbR1MFFIWQV8V2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=KZFEsKeN-c1_djZKALXENlM9BRSlRXzLK0ElcWawmy6Z3z0TxPb1kp797umK65nzH97gPvmUiomvzxS3Qf2XhEQ-tblBvqM0rVeCb0qSJI0yIiwn1WGYRYUsENoCuP2_GAnZHqVCDOVlsKDI8qeJiSira8YCDYhT9FDEthxh-sOnkXzhnRJiAdfl3I97llsnPxIcM174G_3hUfv8YMiUTMyFhmvOwo_ixHmSqa4MiJjJh7U0J_IeMoS34eC2daM0I4egrmJMQbGRA3ufAIx6A0MrQK8q913zT1529Hjp5hsQ7zd4BsHjQb8zY0BGbLdkGrGxJ3NWBkCuAR2JaKbv9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=KZFEsKeN-c1_djZKALXENlM9BRSlRXzLK0ElcWawmy6Z3z0TxPb1kp797umK65nzH97gPvmUiomvzxS3Qf2XhEQ-tblBvqM0rVeCb0qSJI0yIiwn1WGYRYUsENoCuP2_GAnZHqVCDOVlsKDI8qeJiSira8YCDYhT9FDEthxh-sOnkXzhnRJiAdfl3I97llsnPxIcM174G_3hUfv8YMiUTMyFhmvOwo_ixHmSqa4MiJjJh7U0J_IeMoS34eC2daM0I4egrmJMQbGRA3ufAIx6A0MrQK8q913zT1529Hjp5hsQ7zd4BsHjQb8zY0BGbLdkGrGxJ3NWBkCuAR2JaKbv9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=dFKzIPyfNJAB_gRf8I43wIsTnpFdPPsWDIc6EPcJ_TaVwP1m0Mf278L9r0WRYzG5rz6ptDxbg8LVNKxlq-OJByW73v7YkNOrB88tKaOV_7ljXvgzHGxgmPaMcRcH4Fn4zVTKeHzXbUxiNO89IX39OBM2zwhrM04MGroiYlSEf7yjrFMy_iaJaRXoEPyzt9p_ula9DZLpZF8mWJOUopXHqzyvTyMqCU2z37ofukX8eYR3HowLcb8cobwswVZldSGfVPgiQdltv82lRiwHYL7S1tMFl4TOYn-BsKiQ46R_TO1_2slWfCsrRfkMwYuv7A56nmp6nMBoNokNCUuAJ2DVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=dFKzIPyfNJAB_gRf8I43wIsTnpFdPPsWDIc6EPcJ_TaVwP1m0Mf278L9r0WRYzG5rz6ptDxbg8LVNKxlq-OJByW73v7YkNOrB88tKaOV_7ljXvgzHGxgmPaMcRcH4Fn4zVTKeHzXbUxiNO89IX39OBM2zwhrM04MGroiYlSEf7yjrFMy_iaJaRXoEPyzt9p_ula9DZLpZF8mWJOUopXHqzyvTyMqCU2z37ofukX8eYR3HowLcb8cobwswVZldSGfVPgiQdltv82lRiwHYL7S1tMFl4TOYn-BsKiQ46R_TO1_2slWfCsrRfkMwYuv7A56nmp6nMBoNokNCUuAJ2DVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=LM2vSh2dTx_JURmuGCq3vuoU8vGuK54sfuqHmbwAwIHCg0ivLSm6v-CN7m0q583fFpRh4Y5lbNmy1KR5fUFgYTR5diYxwvlSH4iCFFNad1mGy5Q6FmSMH-JVP1Nh6aNMt-alGmGGvCdk-_7Q6kBkIpcyLcr3XGyIB3TbQyt4JhVl_i38stYRA3JJiQddWmSwGT6c_0bsI-vUx84zg2D39rquaPnr3TTK-JcM6wpl1G0cxiA19ganFBmcEhjzofJkdoqACx7C67rN5ivYWCKIxqGOYGhN654J1qy-NakPR9eYnasdXmg76jS1QtFPnLYixOx3dbniKZOJnSfCAJodZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=LM2vSh2dTx_JURmuGCq3vuoU8vGuK54sfuqHmbwAwIHCg0ivLSm6v-CN7m0q583fFpRh4Y5lbNmy1KR5fUFgYTR5diYxwvlSH4iCFFNad1mGy5Q6FmSMH-JVP1Nh6aNMt-alGmGGvCdk-_7Q6kBkIpcyLcr3XGyIB3TbQyt4JhVl_i38stYRA3JJiQddWmSwGT6c_0bsI-vUx84zg2D39rquaPnr3TTK-JcM6wpl1G0cxiA19ganFBmcEhjzofJkdoqACx7C67rN5ivYWCKIxqGOYGhN654J1qy-NakPR9eYnasdXmg76jS1QtFPnLYixOx3dbniKZOJnSfCAJodZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=OgYk83XMotlWZAVINCVrcFlx0Cq45GW4OfOmH5YuKhZvSWODh6uN7E_fA58QGESs3C4Ftgt5c6dBdeOonf6oAPWXFxsvPf-QRt-wqC7pC7Ok65nzB_vVsLsgID4Vtov40VvWGtTdU-dkW2s38a-V7Lv3NNm4Rj4LjPMwfYfT8rz4GQlJ7-F29vbuuVLw1LVOjv98EE_OTaO6aqbZ85g8H-4TRqHle3Ryq6Mdq3foskGtXpHkS3D0KpZ_LLGzOLFbS5mTePtqtkysX-S5TZMcZ4KmVS6AOoFDE3vTIaWsRhYlrg5lP3ORAn1ZPyw_jFPtX16509zlwIngNChhrFgiuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=OgYk83XMotlWZAVINCVrcFlx0Cq45GW4OfOmH5YuKhZvSWODh6uN7E_fA58QGESs3C4Ftgt5c6dBdeOonf6oAPWXFxsvPf-QRt-wqC7pC7Ok65nzB_vVsLsgID4Vtov40VvWGtTdU-dkW2s38a-V7Lv3NNm4Rj4LjPMwfYfT8rz4GQlJ7-F29vbuuVLw1LVOjv98EE_OTaO6aqbZ85g8H-4TRqHle3Ryq6Mdq3foskGtXpHkS3D0KpZ_LLGzOLFbS5mTePtqtkysX-S5TZMcZ4KmVS6AOoFDE3vTIaWsRhYlrg5lP3ORAn1ZPyw_jFPtX16509zlwIngNChhrFgiuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MfcH6_FP1aPSiwX4C6hTjHuzLR1ToOzpmvqgWC7TBYXsGxg7_S_mIMpWDdqIkyaNze3WJlJqnNIx_rT2GghmGYkbkxNKy3aZVy2uiV4vqHv4Tbh91Mqh6Pcv17V2kjG4hnat-RSOstELnA_LzFfsJrea-OrgCI4hX2qjj7Abf9yEvY8NgzLOX0XBwaafAlAbgW-L5EpKrtJZghhT1ipff9qjtGaBPLz9l5Pyten4KQ3lNWLZ6CDn1fPJDDcduHapkqbIFoXWmIClMRvkSXXmOV_AZjFQa35-eilAMBdxVfPkO3aC-m0pjuTnkgsw0z6I95DL7NReG2sStLCM2M4TvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MfcH6_FP1aPSiwX4C6hTjHuzLR1ToOzpmvqgWC7TBYXsGxg7_S_mIMpWDdqIkyaNze3WJlJqnNIx_rT2GghmGYkbkxNKy3aZVy2uiV4vqHv4Tbh91Mqh6Pcv17V2kjG4hnat-RSOstELnA_LzFfsJrea-OrgCI4hX2qjj7Abf9yEvY8NgzLOX0XBwaafAlAbgW-L5EpKrtJZghhT1ipff9qjtGaBPLz9l5Pyten4KQ3lNWLZ6CDn1fPJDDcduHapkqbIFoXWmIClMRvkSXXmOV_AZjFQa35-eilAMBdxVfPkO3aC-m0pjuTnkgsw0z6I95DL7NReG2sStLCM2M4TvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=X2Zm45R6SMqni25FIhy7lz_XyC6xKwThS-wQmaszELu168eUpRNaAjqQfbh5oTke94vb1PeKwsfp-KZCSbO7aKkz1StiGeJUbdEzWiAY5oNW3T-doIih1SVIMqFEfJWcJXMtL2DEETwVmvcTbWWUNIwVD5Of9Edbd2ohRzW8tTv_7WHP0afCatbKGQeDR8ULRmtjWIJ4MAxgMp896fNne8bRPL-zRCwpE1vBFiUorqDSi1LhMZ4BwvbDtLYp8GMKg-cngUvFp6cDEfb4vo_2lnQEydNoMmFW3JejdphtvbKvx8i67pkVOHHEp9BOl6PY27yjCz8Lu7rusPFWh3LsUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=X2Zm45R6SMqni25FIhy7lz_XyC6xKwThS-wQmaszELu168eUpRNaAjqQfbh5oTke94vb1PeKwsfp-KZCSbO7aKkz1StiGeJUbdEzWiAY5oNW3T-doIih1SVIMqFEfJWcJXMtL2DEETwVmvcTbWWUNIwVD5Of9Edbd2ohRzW8tTv_7WHP0afCatbKGQeDR8ULRmtjWIJ4MAxgMp896fNne8bRPL-zRCwpE1vBFiUorqDSi1LhMZ4BwvbDtLYp8GMKg-cngUvFp6cDEfb4vo_2lnQEydNoMmFW3JejdphtvbKvx8i67pkVOHHEp9BOl6PY27yjCz8Lu7rusPFWh3LsUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IisvfKfLixX1ImV49N-bGBaDLiNKqCgji39L1FWgia3bFr91jnC_LSHOr-1CN-wPqneKebPJ_8gan5f6JbIvZQ6lsPbaruiVZsJrqjaQA4P93q45k2f7WbRoC23a0iIWG7PD-WPp6MMz7fOxYfLBkYo2WuZvkFjmZbKcgsCZwCwTJJM8rlWgE_MxWEtsiaI4yzOFQC8QJqhI03UIK3_ik_Oas9lyJdBlgVi1JikCuCxu58kx2iDbiMi3KbYoKG62uazq-c8AnlpvWol-iP0B28akpzfD7BtlFQLkgmbDUBHGFR2cX8cpO1V9LGUM6-i0HL1II0NTeDpGQlETZ6At3Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fCVkTUP5ViMt-MI3CIiRAmAYuV7fdyFxcyF2jJvuywD0e1gYI-k_IRYVROi1vL_zbcp_HlC8NwtRJlPiOemaQrQxtiB3wB-7sSMAKTnDKixBsEq9DHKTCur1BdPpK4WHs0Q6LPwIzgo-pIvEhq8KGJ7GfTSf7OZz4YTAXI-zbl1HRNKoNJB9qtZi1j3r_apeAtUXyE_mze2eqhJgRJRXrgo83i1aMYEJG9fAGn6uZm_ap7rEEGTMxRFrHvDneLoV9ldgt4_THwZeRhWsTQdUM5FiggHCy337LibiARffhADypDg7jUG3I_ims4GqQoUgm2pL2YcfezhftRJZ3xXvqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fCVkTUP5ViMt-MI3CIiRAmAYuV7fdyFxcyF2jJvuywD0e1gYI-k_IRYVROi1vL_zbcp_HlC8NwtRJlPiOemaQrQxtiB3wB-7sSMAKTnDKixBsEq9DHKTCur1BdPpK4WHs0Q6LPwIzgo-pIvEhq8KGJ7GfTSf7OZz4YTAXI-zbl1HRNKoNJB9qtZi1j3r_apeAtUXyE_mze2eqhJgRJRXrgo83i1aMYEJG9fAGn6uZm_ap7rEEGTMxRFrHvDneLoV9ldgt4_THwZeRhWsTQdUM5FiggHCy337LibiARffhADypDg7jUG3I_ims4GqQoUgm2pL2YcfezhftRJZ3xXvqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fT_pk4FUKb5GRsZK7ZSeZbYj3kV0hHAEBlU8WUUcOEN250fXpJ8r7oDdoueZPAMUAWrevCU-xEzujGdCSSvUAEcBzHuBuov3a6YNkt2D0myructFtRDoHrTIj9CVasaPRZhb5OJ2iNbI-r6s5q63JoD3tJk2qRDW58QxIGFl4xTkYxwciQY-Yvs4n_yDfDtfpmO_DQorKR7HTFkfMX76Ro1AeHDoLKXGdNbLw4TRbmPiZJJg3ptp0yCTf8p3RAGQUQfU8M-cJpBumfh5QovxU_VSQ-OJhHINyWrk8xBaYhPaRLrr1dwWwpKpmA8R-FRoNRdLjlpComgBThDWrB3KgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fT_pk4FUKb5GRsZK7ZSeZbYj3kV0hHAEBlU8WUUcOEN250fXpJ8r7oDdoueZPAMUAWrevCU-xEzujGdCSSvUAEcBzHuBuov3a6YNkt2D0myructFtRDoHrTIj9CVasaPRZhb5OJ2iNbI-r6s5q63JoD3tJk2qRDW58QxIGFl4xTkYxwciQY-Yvs4n_yDfDtfpmO_DQorKR7HTFkfMX76Ro1AeHDoLKXGdNbLw4TRbmPiZJJg3ptp0yCTf8p3RAGQUQfU8M-cJpBumfh5QovxU_VSQ-OJhHINyWrk8xBaYhPaRLrr1dwWwpKpmA8R-FRoNRdLjlpComgBThDWrB3KgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fqQ1NO1cfbtFbMnT1TfTZrK0HIrDAYCuv5ydqns-hNIoo4Sv-r6huqnZTv9KNpf-wPDDCmtiQ0ppVwmxwpVDt1t9hmmGVv2J-otUG8yj0sqz8S5f1sMJUvUjn9clyRgsaKY580cWU6ZCsYwTEQ8prjETaXy7cydQGuzjZJ5zM1eGLtrQ7I2TLp5OJPR11vMfTrGBMjE3rRxHqUKsJIiCl6Ej1ADUOP8dSfns0CeyU6Z1Ky7Cp2zNbq4PfzAuMW-lJIj5i0HB2TS4pzgicbGeu-Z1ic2cFCXZj-IOI8-BLNDiH_JqZbgnNqTILIN-VrN-28yhKVhuQHkOKsYFpvi10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fqQ1NO1cfbtFbMnT1TfTZrK0HIrDAYCuv5ydqns-hNIoo4Sv-r6huqnZTv9KNpf-wPDDCmtiQ0ppVwmxwpVDt1t9hmmGVv2J-otUG8yj0sqz8S5f1sMJUvUjn9clyRgsaKY580cWU6ZCsYwTEQ8prjETaXy7cydQGuzjZJ5zM1eGLtrQ7I2TLp5OJPR11vMfTrGBMjE3rRxHqUKsJIiCl6Ej1ADUOP8dSfns0CeyU6Z1Ky7Cp2zNbq4PfzAuMW-lJIj5i0HB2TS4pzgicbGeu-Z1ic2cFCXZj-IOI8-BLNDiH_JqZbgnNqTILIN-VrN-28yhKVhuQHkOKsYFpvi10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=BpxNVeXtKMnD5kr_401O_7ecNvSOYvYUvn-qE3k7b3YAR4Qvx_PeKTi0QZ2U_Hmf4LWFfZw6EH0ttORzxphtO8CgAeHTdUL8sMCtmP8G7qulbJ5QTGKhtKjRBwWeLLeZAUeSJaJyOkvRgx7ERQKeVAnsHJvJ4frx2c5xx0OLmBh1DkknpQu9C3FpaQDRnl2ZIQUx5NABPoaBG01cG_beWdUt0QQ1mn-LguV29w1WMbG-71ebF7xun7cZU6YQuB8Z4BUJk1np59D7BzT4ad8NT3fHVAec0P6quv0xwsDE3xc49WQ-x19lbfimGgML7oGp9VJzu8aiiprbG2mHPrF5Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=BpxNVeXtKMnD5kr_401O_7ecNvSOYvYUvn-qE3k7b3YAR4Qvx_PeKTi0QZ2U_Hmf4LWFfZw6EH0ttORzxphtO8CgAeHTdUL8sMCtmP8G7qulbJ5QTGKhtKjRBwWeLLeZAUeSJaJyOkvRgx7ERQKeVAnsHJvJ4frx2c5xx0OLmBh1DkknpQu9C3FpaQDRnl2ZIQUx5NABPoaBG01cG_beWdUt0QQ1mn-LguV29w1WMbG-71ebF7xun7cZU6YQuB8Z4BUJk1np59D7BzT4ad8NT3fHVAec0P6quv0xwsDE3xc49WQ-x19lbfimGgML7oGp9VJzu8aiiprbG2mHPrF5Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prbyum7iV57SA3D0XE2gyMnc1_gcr7rFj_YQkdkWct0oSR2FoiC95xwov1_xpJTe9lWIpJPQ4jTBzJM0d0VyXrScgtTqRYywP0dtv798urVG566ffglaWXg0DyWoV41AuoZnlR9oMWsFW_K6bQgl49SJH5yq51EaKwMpP9kM3FuHntbSj8bXTt6sK-TsdIgFj6DwoEjeUaMoTRtgVEUhj74ZK_jSNSXtJBK26gGH3Rx33YgNeFiGOWD1Syi3mEdI6JvZTXuI4_0-L9HUoKn2mJwxiyH9teP2WCtiarwNWnn4mrtFc5bBJ4dnBnbX17O6efvfwfuh7W3zkAsNxneWfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TWKqYEJ3NE_gqOGMXDqYL9V9Sx6CQowBBZJs2yxlL3TM6rDwsPNZqENspIqpm9WwH56EXNCGm-1LXY4tg-SUDNraxEL91o7QxsXwKHi78Z_9XFXk1aH_QcCLCRxkJR93C-NIk7hvGru2U8W4npqh9Hzh3L7hKixt94zR0cNefwN-8Wu0uff9FQjEHu8H2w16Sb0Ks1rcFKfN1spLzOMkbIpuWlKaPsvYI4wCxsJu2nV-5cl-oHSL0OkTkOjbD70Cf_p96DFKvSwd0iCdIwLFGJELknk7IClkG4GDhQYEfeqf40eSPKrewYe-lve6lf0Sp1A6WYs7NPCE3xZxF46RmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TWKqYEJ3NE_gqOGMXDqYL9V9Sx6CQowBBZJs2yxlL3TM6rDwsPNZqENspIqpm9WwH56EXNCGm-1LXY4tg-SUDNraxEL91o7QxsXwKHi78Z_9XFXk1aH_QcCLCRxkJR93C-NIk7hvGru2U8W4npqh9Hzh3L7hKixt94zR0cNefwN-8Wu0uff9FQjEHu8H2w16Sb0Ks1rcFKfN1spLzOMkbIpuWlKaPsvYI4wCxsJu2nV-5cl-oHSL0OkTkOjbD70Cf_p96DFKvSwd0iCdIwLFGJELknk7IClkG4GDhQYEfeqf40eSPKrewYe-lve6lf0Sp1A6WYs7NPCE3xZxF46RmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sXdVbmhbu6yBrJ_XKLQ7ixrDczO6TcHv1kfrpw9BA2RgXVNflJ6oCbma_wkjm7hTd8zVjaVxd7UpniK1xAi3qUmMj2lXflC-5lvXO34cxSTXRLcvTXRanO98J0ShGb5kQN7gEBEiP_RarctBdEyLRv9xCMD9nQAJo37RpZRU49osdH2U6XHPCMhEJlUB3x52fHMGjYa4XucccpHz6LV57oE0W-I3JS54ET0-XWkz0dxychfTL2eHUJxYdZ8WYSk01dp1mcViNM3SY2nGz2xGR-CE8insswMkx1QKeCeNhfyNwxVHu8x6imUx2ONhDLKaxQRJJx6gMfr1aqyTC90P6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sXdVbmhbu6yBrJ_XKLQ7ixrDczO6TcHv1kfrpw9BA2RgXVNflJ6oCbma_wkjm7hTd8zVjaVxd7UpniK1xAi3qUmMj2lXflC-5lvXO34cxSTXRLcvTXRanO98J0ShGb5kQN7gEBEiP_RarctBdEyLRv9xCMD9nQAJo37RpZRU49osdH2U6XHPCMhEJlUB3x52fHMGjYa4XucccpHz6LV57oE0W-I3JS54ET0-XWkz0dxychfTL2eHUJxYdZ8WYSk01dp1mcViNM3SY2nGz2xGR-CE8insswMkx1QKeCeNhfyNwxVHu8x6imUx2ONhDLKaxQRJJx6gMfr1aqyTC90P6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2BqpkyPtxcoZ3ZDmf82YbHuJBbfg-_hj3btLVTmjuORcp-BADcPrKihnJpejkH6Sd5GBEIISJGwX183UKtc5gAXmMEl4qQ7sORfaZeTVsAw3xsWQ7YjPkIEV4TBC4YhAhedB2gDLM-kxqBOoVIWuRvQIF6Dh8Q2Dm-PHT6vL2F0JO4OLS8-1NIZp3ViqlO1cNX0o9b0SllhCmA1OTXZrmWgnX2zMHNgx6-EtoNybovWwz0R-mCKehZ_yVJg7a4KNP5w3l2a9ZGozXAFZ2qoYQ1I6LtcxoqleaiIKJFz3FCzZ8YWmwumlzjsWrluo5FUt0qNKcjkOa9iws8esAGrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9-WCBl1Gb8QgxDP_9p_ehUFd949FffUOL0RWLsixIfiTygvRjSQGUwaqAmg4PmkMTjzis_vfAzNuZb0E5snBxbwH-mqAWvOiZOO4u-sztpuEEex-Z9idTGsfMC6455EkfTCDOOD77X-SyhkB9oiLXpuTIjr_UXw4dgYAaZ4NBMHEOlWqlQuYuA4qhVFlUW1uh_tQAcere9JCGV76DSSbJVkMp9gnv9kE45Ikgxtl6G528jeC4NcnojaDXdZ1NPlVxEq0N96T4Y_PKDMB-ug0yBU8DFfS2FCwurGkb4cC7a_R_uvRvPbiIMX1d3haksBYjIsVJ2A-V_49maeZb81Tg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=WYmjBtR5k5lBzCX8WOSxrIhF4s6qn0huMZBVWc0U84XL-IH5o41tax_p-k85PrSYUXJ121UzDTBLJ3rm3W8IZDwDYWL1ooRhZiPMx6Iy6bHqcCkyUFqG8CIm_LtUD_3n_Ynt0D930hiRFsq9iafqdoc2NpicRhvD6FOn5U5EJz4cBtI9e7uDLqicT0wbZ7uirA59CyKFMxBtFrA74S0z02RipdvENnsukl3pW00_aJBPUujFIMRXM9dRhgxZsZlpDlHQI3oYF_KZAvY-j3BHWCEPIpL5i9hv6BWN7QfARh696YkeW4A2WSg51IKTjH-5JwQIf5kortlK8a5wKVqWfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=WYmjBtR5k5lBzCX8WOSxrIhF4s6qn0huMZBVWc0U84XL-IH5o41tax_p-k85PrSYUXJ121UzDTBLJ3rm3W8IZDwDYWL1ooRhZiPMx6Iy6bHqcCkyUFqG8CIm_LtUD_3n_Ynt0D930hiRFsq9iafqdoc2NpicRhvD6FOn5U5EJz4cBtI9e7uDLqicT0wbZ7uirA59CyKFMxBtFrA74S0z02RipdvENnsukl3pW00_aJBPUujFIMRXM9dRhgxZsZlpDlHQI3oYF_KZAvY-j3BHWCEPIpL5i9hv6BWN7QfARh696YkeW4A2WSg51IKTjH-5JwQIf5kortlK8a5wKVqWfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1PpQ3NdZDydwSJbTeuH_MdHgm25lFapA-drugr1sHj-gz4uQ93J7-NUIlQoeZOu50karu3tnDLjqPlgb8aenbViLWoAuD_A7ykFKUn9YeH3tWAybLtrL_pP_9zatD3H3yOnXNAARgSOxgfQ5Jv9SDpaMPOmHCkOojJvqMjBMkrwpN28MPvxxwNQ26WjnnaghlpjLSoCyD1ZfKIMnEmx1_O-4vhF4SRnTlg_XtiL3w8F0q60SUre7J47SY9Uyjtqg-kOdsX1D8wFigr-zPKbqoE09M_WJOvIUV4RauRsjom47NFAZt3JzZCBrvTplKDhj2_oQZdp-ey90CmIlul5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD0BXPtrMNizGylJZp5OERFFm9qQOp05qGTVzh2kHbXKhdmMeZiOCXdyz-0kH6d_dg19loaE5pH7V_I43kQeFCzaElVZ3fEyifUidcpX-lv0nZOF8nedV6bvozQ38hpCUC26wFgmULkdmx0Nv1vWwwqieR7fpHuqFt5ol0b-wTRvOBPVC565-ZiHVy03RhlR9vDKQGsx-b_pAHFkxIxo2rfX0vCcO2XzNAQV9kS_ak-XJ9saqkEtSYACv8SUp3Af-BXALDq3FyIYucnk4jLq1bbRqI3iVwX5wNsLt-5_qG_AlKnEZkGNqbciH17WYaqjXjzdGAr65pxKw5S3tEi3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_OsDxDISOMGBU_3PWoLlm69OgOuH67mtEU-FDkRwZm9Sw3SjnNtMZ3okeerGsGMERivqVkGtE_mxYtadl-lPaRv1rjVV_dogAmCqjp74P4ZmYKYVpBZW113M6loRG620dmoIMj01K6ptoEslscDVG9g4TD7_am6JlS0GpjwyK7gRd9_6IjhB69YDV9B4gs_VzTRcQhrRvAo956lFV32H7sQjMp3I0mGzv3S_K6mQvLFIhMYO8DqlvC3r-SVM_1zD_gWx3uMEzNuNgP6YRzsgQSAvpKAHvLdsx25whEuUqUAMDmUi7MaXOMqY-uO4cOZ4NolzjleHw6tldbDLT2_aA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Bv5Iq_qq3ukAiDGXBR0JrL4rkFiZcN9AHQRyZrHlZGvdoiDM0SpK0MIVsQoHBZmQsVi4M5TqH14sCzaXpc_k_zEsYOdPAL7w9iAGhZWkMRzmArNofOHgQhm2PTAjHA6g70EiZSkwxqh3QAO5jbWvvl_rzQN12u6hiaDRPOtsSdsg1WKgqN0sZfRIwwmlPkiMSYl-NfA5GzA1EfZxHlWgO7wePKP39yE6GrdqDmmT7-kQqXr63HHG6HnPSqJY8CJX9Jd-rQ9ubuJQ0Lk2H8T277ubqcunMsE5JwJDLnQyE-vtd_4Ch1O4o9fXsn0LJgwGWDDINLOPupDmhqMrKY6n4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Bv5Iq_qq3ukAiDGXBR0JrL4rkFiZcN9AHQRyZrHlZGvdoiDM0SpK0MIVsQoHBZmQsVi4M5TqH14sCzaXpc_k_zEsYOdPAL7w9iAGhZWkMRzmArNofOHgQhm2PTAjHA6g70EiZSkwxqh3QAO5jbWvvl_rzQN12u6hiaDRPOtsSdsg1WKgqN0sZfRIwwmlPkiMSYl-NfA5GzA1EfZxHlWgO7wePKP39yE6GrdqDmmT7-kQqXr63HHG6HnPSqJY8CJX9Jd-rQ9ubuJQ0Lk2H8T277ubqcunMsE5JwJDLnQyE-vtd_4Ch1O4o9fXsn0LJgwGWDDINLOPupDmhqMrKY6n4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QebTfMRf0GggcBmjkSWdIm0kyQNNwV6nU0-DqKAkPkDUqCgEYoOOs3tOH80VlwMpQwE05WmdoD_jvI2T6oIX1Z1DcC9QdKOwW1Tij5hgDoJgtY2xw4a9eHhiSeksQxpdHob_kJwOSPL1zbuSWusc6c2dxBDguLh6s-isTNO8Ez99M5hA_znaDEtIaUgRpmmQGKdekAfD9sZfi23wg5b8PcVUDmSxpu6K_f6pUNoK9NBz4VF84dJjOXS88LjVLKCDPvQb_bq6zHWY1cmniMoXmN03YTgF1jpUoOE8F6DKng4VbMHf2-sqtYaRloIs9sPP9jC3_3FWS6u7SwUVYsqg9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QebTfMRf0GggcBmjkSWdIm0kyQNNwV6nU0-DqKAkPkDUqCgEYoOOs3tOH80VlwMpQwE05WmdoD_jvI2T6oIX1Z1DcC9QdKOwW1Tij5hgDoJgtY2xw4a9eHhiSeksQxpdHob_kJwOSPL1zbuSWusc6c2dxBDguLh6s-isTNO8Ez99M5hA_znaDEtIaUgRpmmQGKdekAfD9sZfi23wg5b8PcVUDmSxpu6K_f6pUNoK9NBz4VF84dJjOXS88LjVLKCDPvQb_bq6zHWY1cmniMoXmN03YTgF1jpUoOE8F6DKng4VbMHf2-sqtYaRloIs9sPP9jC3_3FWS6u7SwUVYsqg9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hqV7bzUNKki5W43-0CJRK7-gxbkENOmxi3zSJJ02c_mA4Fib7L6r9oVdHmLDisgGz2qhoENYzW4N56YjZIA2lqLeIVQipqKTIfcXrGx74YZ0tB96kx9sIsHUt1kPMl-HcpBh-_NInb-6cQmJvE3rBJ4f44pEJD3MogOGQwHfXtflNdvDysBeEI-_PGpN9_xEDoQ2Y63sjQYVH4Hk1YbGIE7diHsF9aX-aoQMNnCUIeAgGwhrUf8BVOwOyWIQNg9TWoHhfTReDulIxGIb4p1PIHsiO1aa0Z7dOvl7hr3wVBjApbEA58KakCdf_hsdPEkiKpftKCVEARu54jvWl5L8QxlKw6M4980KTcqAiPA3rkrWxRIvn-f2fuq5mPTeMde1TGaRopZwmMf-AMHNoU_9DDo5OC4em3QaykORm_tVsSb316QAuBCzHM_1VWtvIqTJT2oe8A5c1su4QagDE3Zv4ogsfb1cZIel1LxAYPuwuCQ_LQnl0TRXybwccH9lKR6ND3eskMAGlUGe1_YsrE1afiV0nndlycdETc8szs_gfAxE_eAPJQQJkVlz_Gqd1-rBSzi970uep-lzp73hIy5OaUaIXJ7bCsU3Dxrvr_pdVZxYmpHurJU4i8isU-1VcuCE6waeOJ_pBqB-pIIiyYOt_aIjmhoNNzh6bFZ06b7Yfno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=hqV7bzUNKki5W43-0CJRK7-gxbkENOmxi3zSJJ02c_mA4Fib7L6r9oVdHmLDisgGz2qhoENYzW4N56YjZIA2lqLeIVQipqKTIfcXrGx74YZ0tB96kx9sIsHUt1kPMl-HcpBh-_NInb-6cQmJvE3rBJ4f44pEJD3MogOGQwHfXtflNdvDysBeEI-_PGpN9_xEDoQ2Y63sjQYVH4Hk1YbGIE7diHsF9aX-aoQMNnCUIeAgGwhrUf8BVOwOyWIQNg9TWoHhfTReDulIxGIb4p1PIHsiO1aa0Z7dOvl7hr3wVBjApbEA58KakCdf_hsdPEkiKpftKCVEARu54jvWl5L8QxlKw6M4980KTcqAiPA3rkrWxRIvn-f2fuq5mPTeMde1TGaRopZwmMf-AMHNoU_9DDo5OC4em3QaykORm_tVsSb316QAuBCzHM_1VWtvIqTJT2oe8A5c1su4QagDE3Zv4ogsfb1cZIel1LxAYPuwuCQ_LQnl0TRXybwccH9lKR6ND3eskMAGlUGe1_YsrE1afiV0nndlycdETc8szs_gfAxE_eAPJQQJkVlz_Gqd1-rBSzi970uep-lzp73hIy5OaUaIXJ7bCsU3Dxrvr_pdVZxYmpHurJU4i8isU-1VcuCE6waeOJ_pBqB-pIIiyYOt_aIjmhoNNzh6bFZ06b7Yfno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ep4pmErm2IMOfGFhT3iE0ECc9NBnEW3v01dNXf_FPvW_AykHVdQSi4sNiFum55W0Rb8xk46qQ4gLwlG8WFcV1z4eqdlo9LWSOzeG3GBytLS5gHd7OH67Ir8qDgkG5BBgWq-91gJb_WMJBY75GwJLEERLoIdjSgz9bQwPQ8j8_lSIxWaBPr1ygA3uM0jbJlYXDjtHU0_u5CHQQZliQSE1W7iFFnnsusN7LIf0soolEhGIT5-29KhXMxCAzo7X9qMH43nr57T0gzmNPPY-1xvbHZCW6tt6pCxvUnZeUm5CqdAu-PkwBAZleoAOKREvkVmKPdipPBZH2kqgrpl_9f_cDYcoqLyh_Lid3DsfbIHZQUDk7ZardWTY5vtPGdawfcoslhwzOiqFwY9_HvNQ1zx53JpCnN62XajITSuR6KtuuCx3tDAYW7MPeirxjtftnl-l3wAg26tBKVC0C14ek70XXV662i2RTaIqcTqNjZRAyEdToYFqj_LBwqWwngvVpQOVzGYtEzmZb8jNMg9Jm70GnbiGVpYrknkCbf-arindcWtAUOhS8V63FChmp0McwqvKAw77CuPtG40gcxWPdlcEweNZ-J6IPlgk44BhzH-YuIjOvihRWWg_NPTPI5AgOTcbVWE9ZY93SBV2Q0e_BqeLShNLEznYpftdRbodYJw3IK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ep4pmErm2IMOfGFhT3iE0ECc9NBnEW3v01dNXf_FPvW_AykHVdQSi4sNiFum55W0Rb8xk46qQ4gLwlG8WFcV1z4eqdlo9LWSOzeG3GBytLS5gHd7OH67Ir8qDgkG5BBgWq-91gJb_WMJBY75GwJLEERLoIdjSgz9bQwPQ8j8_lSIxWaBPr1ygA3uM0jbJlYXDjtHU0_u5CHQQZliQSE1W7iFFnnsusN7LIf0soolEhGIT5-29KhXMxCAzo7X9qMH43nr57T0gzmNPPY-1xvbHZCW6tt6pCxvUnZeUm5CqdAu-PkwBAZleoAOKREvkVmKPdipPBZH2kqgrpl_9f_cDYcoqLyh_Lid3DsfbIHZQUDk7ZardWTY5vtPGdawfcoslhwzOiqFwY9_HvNQ1zx53JpCnN62XajITSuR6KtuuCx3tDAYW7MPeirxjtftnl-l3wAg26tBKVC0C14ek70XXV662i2RTaIqcTqNjZRAyEdToYFqj_LBwqWwngvVpQOVzGYtEzmZb8jNMg9Jm70GnbiGVpYrknkCbf-arindcWtAUOhS8V63FChmp0McwqvKAw77CuPtG40gcxWPdlcEweNZ-J6IPlgk44BhzH-YuIjOvihRWWg_NPTPI5AgOTcbVWE9ZY93SBV2Q0e_BqeLShNLEznYpftdRbodYJw3IK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HxiD2dPT4KaHX-KXxM_J9oqNI8cyYngv2_dxD158LIH_WWOIj7eRICOGV8C1zzAX6tPqaWWyS8s1WNVRg3OMX7AWf9Yvazz9Qof2O-WQXjzZkTgqHuTAd68kbdHefzOIGXIVMOrUTp2UtFHuHOZtbxYEeG-qnt8TToOC-Eo5Vt2Uoxlwb49ETEPWYTuY3sioMhBPl9AeJpzOeNiRn1npc-hepHz2v697amNpJ-2Jeq-M8Uu-4rXrZ0o11ygbJLR_F_7WPDHypKFjE31cT-cVoktrenfzQjIGHZ7qPuTMKKY93RcQRjWyIepRA0Rjhb5Yeu8Xx9yczR13xHDjcUgALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HxiD2dPT4KaHX-KXxM_J9oqNI8cyYngv2_dxD158LIH_WWOIj7eRICOGV8C1zzAX6tPqaWWyS8s1WNVRg3OMX7AWf9Yvazz9Qof2O-WQXjzZkTgqHuTAd68kbdHefzOIGXIVMOrUTp2UtFHuHOZtbxYEeG-qnt8TToOC-Eo5Vt2Uoxlwb49ETEPWYTuY3sioMhBPl9AeJpzOeNiRn1npc-hepHz2v697amNpJ-2Jeq-M8Uu-4rXrZ0o11ygbJLR_F_7WPDHypKFjE31cT-cVoktrenfzQjIGHZ7qPuTMKKY93RcQRjWyIepRA0Rjhb5Yeu8Xx9yczR13xHDjcUgALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdfxNQLwjqc6buGuDCjlx-MlZWt4DR3V5sP1FPz6PWh-zjRBytUWsBgBeUKcJ7wFC0tb9NRtdnbFbpBtwy68Y2NKkYBquqRjS6UH6xpGt0_eI2yPdnFsQm95jfXU-dH4O0Si7hEI9rAhxWVznIwmgc6Lnvx22RqIlXciIb0HubD7orNzy6xH8PB9UA1Ae3MYeTsibMlc9kk9EEu-UQWdyPm-C5m0HIl1kNVktRkfRS_pdHlAZD-kYTOtVaTJHTdnx8bWvAua-MWTfczY0JkzC4NJt2GbxHfAshS4M6WNY_grgKegXof54ZPIhwDztmtQYGI_-gEsAiunXfUB0oATww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ZGlwyE58A2zC1qVP28JeknCd1sKUea7u0HWeyU9pw5G3hsaXheJMYUktct-zIrmufgL-BTYI6u5ku42bucn_MSVbYIFvrJWP6jlEfUVTDPEOUg28Jq4YR1OGdSuTsneIs680Rf9vqb79X6WBvvGmzU2neko8GhBkL9eAAL451MORd_fYpZqrwqGYMLgQwCa7icnEeuFG2DO63HQB_jpgiCWtRuiR5Ls9XEEpb7cVqGCSlFlDhMwXt5aaTKj6R4KfjrpRQsiqxHu6Raj_OEiDIg91FsaX7BCkbCbp-_LARhGEWcFsb5tw6zj_f381KWjgdn3J9qaIXMn7kTvd9sDbVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ZGlwyE58A2zC1qVP28JeknCd1sKUea7u0HWeyU9pw5G3hsaXheJMYUktct-zIrmufgL-BTYI6u5ku42bucn_MSVbYIFvrJWP6jlEfUVTDPEOUg28Jq4YR1OGdSuTsneIs680Rf9vqb79X6WBvvGmzU2neko8GhBkL9eAAL451MORd_fYpZqrwqGYMLgQwCa7icnEeuFG2DO63HQB_jpgiCWtRuiR5Ls9XEEpb7cVqGCSlFlDhMwXt5aaTKj6R4KfjrpRQsiqxHu6Raj_OEiDIg91FsaX7BCkbCbp-_LARhGEWcFsb5tw6zj_f381KWjgdn3J9qaIXMn7kTvd9sDbVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LcTkYFfG45wsE1FDGn-kOtyukPBrw_Qx1_zgMq3QArRtRSb_SVX6CXoaae-Iyj_Pyk34J6l7nzAXEqE80GCstdgJUFyGN9OJpro04msGXXHhRDhScsXHkx1hx2z34cOn9VDY-BQjBk2yteeoJTvLpbJHQIewXOYNXZHqXzIbAvQcSR-3l_jL5MknT5ZIfOPYY7kuAZasn1FQe9fLyR1hZu8jX6AcH56u6IqZoJH0UifoANyieYLKrMFVfHijrJM5D9WGXsjgfRZuoL6GWROBlFbMHt7N56WMpB6k9Dw2upI4MmLFW6EFP5qoQz7rr7BTXl5m9YGKlJo7ARajbj7irg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LcTkYFfG45wsE1FDGn-kOtyukPBrw_Qx1_zgMq3QArRtRSb_SVX6CXoaae-Iyj_Pyk34J6l7nzAXEqE80GCstdgJUFyGN9OJpro04msGXXHhRDhScsXHkx1hx2z34cOn9VDY-BQjBk2yteeoJTvLpbJHQIewXOYNXZHqXzIbAvQcSR-3l_jL5MknT5ZIfOPYY7kuAZasn1FQe9fLyR1hZu8jX6AcH56u6IqZoJH0UifoANyieYLKrMFVfHijrJM5D9WGXsjgfRZuoL6GWROBlFbMHt7N56WMpB6k9Dw2upI4MmLFW6EFP5qoQz7rr7BTXl5m9YGKlJo7ARajbj7irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tweJ4H64jbJI_6YwgIxRdYhgvUg06vQDX5aJ4eJN4eH3WhmYjU-3TTeT3jiSAIMIW2JidOhCqhN5y-mjYUS26FC8qNQllWnZa3zKXQ2SFKlXNqZr9OrA70hKxXofPgsHjxUQcc5H9yauTJUf7XyEG86L-aVsC67wE-RCGTRow2LqaPCyWnXPBWOuPral4SlfxAig6nqxquN2HyIi56wUIJcAmgIZGchs8RdryneYbGRAJYWjYCcC6DJqXKyy7lKEkXYeW4z7O_DzC2QFRCU4aA6TsDtlZYXIdTKIF4icj5eQ9Uv0OY8YHTcnlsC32wJ2G4gHCykcB5zG_HWAmOQgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxxYwmW7c3wKKdtoFtph13JLPlg5anTLnY2c65VkfNpfpl72kzgTGmKw9dai37zgu7x6lpPYswtzgIUTmMmaqDLkTOfIOaW-g2m2uWOzA3mdAs9GzGEa_4-s0jGJB1N3xh7EIM704s1X477auzyJkaHPFNbOC4sdzeXgsKuUFVlEQr8w97UcVqy1L0XdjHAK4kysXTxst97r9YTyFn72FYxkHM_Sp1XOAWyH-990JE2kzA6Q8K7mANXmlkHvyo6JD-WdmfNnnvu-9OIORtb6l0E8LMiYDJ9AwvIl4EopkKhiNHTrs8VmmMv4W_9P6O8-W3AAj2hEq1pTlROakuGpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-eAw26d9B9OuH3__DDfnfgBh_HzL4wV8ZteQk5OHl4WddqvmaZ6AsNBNGj0LcIFqdDKMIRIWBoh1fkEJX6xj-bp4wh5-pz3yy1qntB2dz5y0YOUVj5pStDuzdBUngN5UpuQWUkHY29rhSIhvEklIBO0pxzDr0Kb8i4MYynC_ZlLSwP6gXUZ8WMGdCoNZIBrciEMGXgb2BxFEXjTHuZNgIox4fTecvaskJ332U47C0rqn_ZUZSGdbdAF2hifRr4bB4a42eRkLVkcdjT0gEK3QD1gUpE0yLTHN-49gL2WI3Cfp7_wT8bx11NsF_Nb41PyWwQ6adfG9Z3625gM4NLm5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvMJBFbeWtbVwtPaZ4f9EYbm8jKOM58S6nWYewPJh62s5OAXg6d6ARvMeDNhJLldHUx5OjBY2O75Sxqsk0ul4lycntNshXm9KW9ptRvtCijke5LGllf5gndga8OqxwuS9gJX3zcKIGiuao5_SH0L6aE7SE9Q1mbRgNlQOoJQOdDwYfe_J7mWqBvp8tD_0EaUpA4s7iXGrHEUvaCVsMNQY-71uZ5uMQFeblR-pSzjtJIB6ckuj3NbbUmeQidJ0gMx7QAE4m5QNY3Dc8aE0ypJ9u2LLmRcH9m6v82rAleQJRhHTGK0ktO8j4FlZOms2UGFTkn54E9uKoE9YjEOdSCy_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuX-tIvb7OqzX1q5WZIXW1CUKzTv_4dkTrigAFgk4YMWsBvje_z7ioFOGI4EjJtk1cd2onW-bhjmmes9hZnO-wjWLHoQ-dXYIIGmco_TLw2_Q4Q6j5F0teen2PxENs7Sl8ogs2ERrllO_bjpgQ8sc_5-SZX27P_KzgeN5_bJZ_vM-fQw9NYxXUdKcReTX7y5vTL3AvMYtvKnQKKGOt6m3n5TdCM-MEUlStRWTCPFKtncFzTp-vDTaji8wTAcAcHlJJNWenwWGYt9tuXemtuObBhaX0LUUUYJyMYKcHsCGNGSU0bVpN-sUaOHvre6qmsdmR48FhFnKQZEIYh_iq7QJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tORJTDrHo6LBOyFS8AtTf_fdLLmIVto6Ri0IZbPI1SYX-7HacFdUauGCylptnkHiIrbnK4_V6pxlsep89hYAarx0z2yjE3G5qXUOoaB0RIBHU4ntJa9fwkLWO5V-x7f_cNqPW1zSc3umDwJOGx8yLePJe6avzNF093uWYKSZRa1lFLLSEhqY4jhC4mvNpWMJkhmVfJ5_0DyvawdjSIlO4w3E5C7T48PA-ctd9-3Vd1gDthCyIYqQ5NPDB0h7waO8ZwK0h8Xce0LHgvk4USz7T9_1WpY0SkTgII5XmMeO8Zt8U6pTDIlZx08DuabpynjODoq5vygWg_AOX_3qzUdobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGMM4B0IIfzIL7BgtHAj77NC4CSdMOwep63uUlVdR-qg_t8ARjjhP_3vwTM6nQxHlVGGUVaPOIaj-rHVcXzQMgVTCYcqFXQVPwlVg5CvLnzbHLXYKD9jZW3A2iPc0TTYoST2uVUeUjWA5LCyioR1Vb6Yhf6LA5C5wYYa-k-ligrh5TQPfT-e-CyHLTMFiIO5ZI1OaLEU1PwXI7hcCQdDv-VI5-Eh0CEvEUq0zQfrsWRf6MREA9-RTUSaoq8OJwR35XzwnJdO6UD7qzQModX2AviEQwk46YWUoD6lbpi9uC3RKVV4tnuuKKqzVbIyMbH4mmom2nkRJDTsW6oL2h8cvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqi8ZzwLy0WLF6geZSKidmlbrkzRL1QxQzuuQf-O0wQgPTi0m5HxfWpPHkTJsgOWCoJxn21-3yu4L_niD8gBgNoecq0Bm-E6vXEPtmmWYQh0KuHoyFo5raD-dSpAiqyFQV74O20sVWZlrGshKkadr14LdPmBBjioKzUfGfZfSSrLyDv8ZwE9llkB6ivwCu7Hc2b6th3sVJ4QEKZuIDlxYt-OI5YGIdToqb_r-EfzTLkPOJDLht48n7t8RzCE1pIfF1p_uRlSI20gP9eKp1ZA0PqhoHV5MlaagsxBlKT2zrIkwPxITcn6oGY5KgkN4WT5uFa6pjV5HDxj4Wrc7PREAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvxH8rzvnjSt7QcAcRG6j0SMqkifqW2xSHObpC9pTBlW_IXio9ziEPxy_57xVz4KTYwCSdSIRhnCmeptYt3Khfnodp38WIghe8oelRcWp2mdcC3GWHDGHYHvvLo4qlvy45zP3WETmkU0zJw_pJgbJ4_1INV95l2KPwCyOf1x48s5G-HFYrTRDHtzOXIDxDtbYCTV6eMZEFZpqMt1XjW01Ppni3_XS1n_qxmls4ojZRzzbBYmmG5aZeH8V0r5NwuSgAmlRi-SGv-mKan3uBGmZoqecYNUSO6mp8KGucixmkF8ySdx2T82rJJCJUtEP_mFfhd6FPN8ULqDo9cF7l2F4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wCQT81zp0_yh-7BhSt8EUh9pLjOF-fMDfyPMtsZmZbkXhbAmPR6fcflalKqUGneQ3eWXwCLRCLawqS6an3ezTjgQs8ZZqKPVSHfW2p_SnJqoPx-k3zcoavbbqPeLEzPW3Oov0LlzJFNXBH0-7dGrUgOtRAaoiWGb6-4tS9FZz0ZAeKqwuzdAEtx-E912RWfOagQp7-acIssrrtTOVsc1HA35ai7lGpRN45QT9IeZc_jU63f67UE5wwHcEhh8beYeX4uBtZVh-5gWiHPwX_bS5SEuH1W3ubfwITKhmyOHnNNukQ9S9_27T7Zm8FHd5E6AOUf2f5Vgd6naIPCObinHbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=IKzOK7uf1uZHmrKDFoyfDFunpR4zspSFJ6_-yrrdU0dYqUl3rtV9Rv0rZln4LmpI0pwiiOBs3iG91XM6qkqFVoVw6n5_oerWC2beOD4n24fpSKwWh-OZSPLduUr0QEWqGbw6P0AUJIThrjzKkA-gJuSe99CvYiq_jnqaeRLOeL5SJ1tHg26Ydi9ySRsMWXjCBNH_BPw8kwPkjieCYWvU-l3Fi-XcJGsCrIOWWu2p_p-WDi_WFFmOsfEjeVWrR0BOOzrJnWEP7Us-cBsj4_Otikl8weQUnM3XUj52ehVkt0E5PlpQl71sMWHbyfPXa8Ak7N4L22hJz_dYqLOugL_1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=IKzOK7uf1uZHmrKDFoyfDFunpR4zspSFJ6_-yrrdU0dYqUl3rtV9Rv0rZln4LmpI0pwiiOBs3iG91XM6qkqFVoVw6n5_oerWC2beOD4n24fpSKwWh-OZSPLduUr0QEWqGbw6P0AUJIThrjzKkA-gJuSe99CvYiq_jnqaeRLOeL5SJ1tHg26Ydi9ySRsMWXjCBNH_BPw8kwPkjieCYWvU-l3Fi-XcJGsCrIOWWu2p_p-WDi_WFFmOsfEjeVWrR0BOOzrJnWEP7Us-cBsj4_Otikl8weQUnM3XUj52ehVkt0E5PlpQl71sMWHbyfPXa8Ak7N4L22hJz_dYqLOugL_1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9Qido3tt8xhtaXt8UeGJzMZZREDu2FRjGRHAoCIpzMqdki7ksEH3XZRonvK_yMnAfseqYhPlMlgZR13tw9ixgzNvezy7kgmqjSCAxhoDvzOb-cp8IM8dtXH-nsVnj_ffZYmTuwdcCECNYnqT8X2JvXYAefvLkQOWUCAQNhpzdMZgGd0jxKWVkNtDnIAF2QZoEt_rpFXT4Fydd8yqdvrVhQBZ1ZLanHlIGTDZ_xkFHd0a44Z6wqlAPCbgZigJhuSWGaUhp-bwbfnkNDB-tIbEPI8Cx_u3US7Zd37AbrRVE9cNQM8KTXPO4UmIPql8hD4YsOj4xILlhqnOUX7uo0bvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0r9H2aroCwsWUc5zQVCvp9jSQh3WVOQXGivtv0KpIDWaq6jz7D9OkrCar6lrtB5dB9saZ02L44ILMAT0032T1Vz8BcHv9_CT4ksAQn-q2YJdlq2ZCWHJmpWj_8MqAnShAJlmI0WSev_j9seGp1b_bLUQWjI4nlWfnj8rxpS6zgrzCmlROUt_TDtVO9kwnThZYzMTO_EyOHPfslsT45Qp9g0YdRIkrI5lrKkBGqveDbLU7Z2RmxZBI-KVS6fMsPq_gLfdrkSfGlNurRd-vYoCNr4ZUWMLIaOE9nK2eXRRiDlhMRhkq3fl0mGfXMXekX5VYL5rV9dddHPsfoB1Ek6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=kBdnOpF8zsIzsiCVxrzY2igbbfcYMIBbfo90dYx3L10t9NtKCEp2ai2DJV-cBMVz0Ne3X_xdyTCwQcnIqxV23QxTuQR3kaHh-ykUHtFbUOMvwRGCBB0OY6hE12RUV47dQvMbLzjXqT5SUIQlR0xyhFjGR3W5Fvg7LVykhW9EAqmnXfE8IZYtoInnR2SkDvNgCwsApVXfKtmVKWEjocbZpR0n4F6anZPvk_DPEPVQskuluQZAQJNtLvcE8cLIillKzYk78pFzfv-VRTccI8x0TSHWgvfKjLicXw47eUe1Nc0wI6WOqEcWLgYwZXT_wgcL0kst1f3BTOt9OgYlZHqdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=kBdnOpF8zsIzsiCVxrzY2igbbfcYMIBbfo90dYx3L10t9NtKCEp2ai2DJV-cBMVz0Ne3X_xdyTCwQcnIqxV23QxTuQR3kaHh-ykUHtFbUOMvwRGCBB0OY6hE12RUV47dQvMbLzjXqT5SUIQlR0xyhFjGR3W5Fvg7LVykhW9EAqmnXfE8IZYtoInnR2SkDvNgCwsApVXfKtmVKWEjocbZpR0n4F6anZPvk_DPEPVQskuluQZAQJNtLvcE8cLIillKzYk78pFzfv-VRTccI8x0TSHWgvfKjLicXw47eUe1Nc0wI6WOqEcWLgYwZXT_wgcL0kst1f3BTOt9OgYlZHqdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Rj_p65PybwJ3UIQum9sstFeS-_2B-NvGx5c2wnxpiQvQ4JObhgsk28R7JstbBzUqVrrylWP2eob-kxPgRvvPOVb-N1L-xi0VIX-9MVlOxYBsj9cjA4W0UjiCeQgslTXx6azWK-pQa8z1D23DKqG3rL8zsP8EjvIbRVlnTBSC_2msmZROHUSjIgOV_swQpxD6vluobKJGbuN9mvelcenmHkEG83XlPR-QPtXgwyhlgAkmhU3dDN62nKPbIju_THC_p_YK7J8I_k4IRwB9FU-kZudimBcyb31ef4bXUxD9Gsodx70nj-clGK7ZNqhKs9UEs-hTtD2ByFHCFfCuCEZxrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Rj_p65PybwJ3UIQum9sstFeS-_2B-NvGx5c2wnxpiQvQ4JObhgsk28R7JstbBzUqVrrylWP2eob-kxPgRvvPOVb-N1L-xi0VIX-9MVlOxYBsj9cjA4W0UjiCeQgslTXx6azWK-pQa8z1D23DKqG3rL8zsP8EjvIbRVlnTBSC_2msmZROHUSjIgOV_swQpxD6vluobKJGbuN9mvelcenmHkEG83XlPR-QPtXgwyhlgAkmhU3dDN62nKPbIju_THC_p_YK7J8I_k4IRwB9FU-kZudimBcyb31ef4bXUxD9Gsodx70nj-clGK7ZNqhKs9UEs-hTtD2ByFHCFfCuCEZxrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikOnqeMARYE2nVI2CjrsTtP4pHafamMm6dsM7RdsfjsQZwTwej9Gukb2oj9EoXLkm82oUDL0PeodAX4JbGc8vAGrGQJL2PRgvB2s6Y7iKLCRQDCxu9GU6osvsTyxIG_ayISKP56-1c_HX7_fo8SSRzYox3OXlI0ouNNXQ_0M6ZDpKRWTDLOKKDckz6EuXr09VBqqVdb4dxuyq7AtMZO4c3QSgE71rAbwkvwFpSHEbI20slHmU_wxYCsvg67ezwFgkpcmm5JKJTX1RrS1zau_vGZ09rcLCNu4YcCTYGAHMh4x0pJwgxjRjqMb0NH5d9OQW9n6hOG92ssVOkpZxcGDtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-zwVpufpuEpYtfwiAXStLzCdgMRI_WXYeOoyUr8a1bR7IxqfNs0INFVxK84_M1VSE3vsM1zFldfvwl1AoaYz_WxNuk7InG7vFAkTzdzMStogU54zMaPCERXUsvpf20152hbUDa7xLRFL-0WNQUSFXCuluAGjR5L1aERwK6rowr2P7w2cL8gjymDdhCbXWcLkgt5nqKQlUyairfcmrbPqLaIK034WRamGtu6QcGtJ-TRwXSkaplw9ykdIBvnTuFxILp41EugZilmDz3RPhlESSuzIfHNmo7aqEykk5-QhRQ5oFRnQcEkhusoZHwF4ppLJ1ChKdlJxqQ3pQ1rHLhORA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBjopBlBHNdK29dVK_99LAyoKOGGlnKm1R99pfjd7aCFD6MVYNxJmOeNVMzJZvYb1eodJUtb_8sQQKOBYdqTzOtWnjsI1UHpV1mpp0pA-ftdRoSmIyK7HT5xnQtsFFw95dV0R1kE--324IOa5E_vUW8WuPrq1dGQHRqTY_Fx0amFNoyVYS2mezBa6GcV-H21vLvI06xWJ5SHqIg3yi8C-WtazqLIg-iA-pztwIVkvDKo3HCVaBI4pjTXhU4ti9l9pTYGYa68bkv-5wndEnKvA_SO-ohg-DMoO__dd2cbJJ8hHHVk36W2abemsLt7GmZvULETI-CiPW-Ycm5f75NXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrpBQ3SUn8Q96_7OUo1f5WGm4SobuZsK0QviBBlp48VlP7_eogURnS9LcbKQrT1b6g7YNnzBjo64LB5uCBqwoSo8N6K4vq4a-UYQksFrJJ0jfURzSfyMtogFr38Xob0t_3RzwUKZ6QMEdQzxZMRZtydg9CnWE7Fhj9nz_40TtiTfySP4fuC-epxkFiygb0vE7uc9oqldagrqLW9j13NmzHImIC-xqSdfGuZ0xhfETjku7g_pYmQ7juwoAzlh5f2IQrU7qxKsBwcb-HJRogif6Qu_47J2RFqnzOqE39nrr-us0DDKtmzS4rDOPui4uC9AECrQBi4VhEnApNQw2eY36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syxwrufwWyW2H5btHBYMWJg9rWRroZcOecRlKsNxIwYpn818LKltjTsa6xdI-ygA6lwdZF89qzIBUlH7WhA0m0QGJ_TI63wzIxQtCg62yHe0ocvnS6xAsZQ63phWtk2Bq6a9yrYx_N-7U-w7FZKhGBuQ5q9csJaUvGjQZsw0SkzYwfNx53QS5Rh5smJHSgLyd5k_CfnaEF3kzcSMrseJD7bWYcBZdsSE8twW7VLBUQDfY0PPSouUEzZfar-KZt7691TqRjVl68tT3plN0eh7p_HYj7quKzSw-gFEXUT50bUJ2VxY_6awP9IbobC-B098W_fTDA5356IEZ1Qt-eMssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwcIa9AOi4YbbtN6r_2Z428b2TuNAyCRhiPgMWdfLEFXs0u-iZLQYqUke2xWxkW_w53rwEJ0gsHXXSRgq9G0YSS6IW675tl3TiAbEKJRDBqNU38mITewFm3-i31hbx4mi4E5oJ1g6UGOcGShEjThFZNrt37TDW1nfhcRePdTM9GB4Uy-EkpOk1vl5ND8Dry4q3qJiW-vWpMlJWGPSksB2UbAupLIgQj4d2FtYWPyPUSU439TM4-Wbc1iAaZB2ebymv4tB9hiJ3CzVkgFb6gZjGz8oeoRlG0ytr8ChIz7Hr59BdHFM5Kr3kprlsQys-LhmPn5oDRzRmG1FU1Ug1dSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqWwThd9mM9U7qIYA5ba7i1OoMT-O9F-bcolc0Cqc2gxyMU1DhhjBaFhVWzbxG78SlGFPzPMd5gCEgrW6bXSNDFKrAPsa7KcnIfDL_E7JMOqP8Br_jAZJrAbQYg1147lS9_cyCbCxpsBQepVBGQpGB2-vGnR8PTjecvL9HOksai_gvC20VJtBHS5MypsZA23RS6tJpjTsLKgqzA0lMQW53AsC_WKJf15Kh8AER-YFRTd4YrDaLR3QmkaAlEqTwr9jLnQUZBaI665YjKDC1JegSf2BKEFm-chH6mZb2CL7z5IxvvqWvymsKCAzOtzxpg7Q5UEKpWgN9eUZicB4MrRgA.jpg" alt="photo" loading="lazy"/></div>
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
