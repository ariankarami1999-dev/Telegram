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
<img src="https://cdn4.telesco.pe/file/DM4J-7KKmtvgmgL0Z6HKxyCJohe2UynowhQJpMw_MPnxqAe9oBbtEr_5MLCvkMvMzmC8WvID3-MKtN9EbfqsLvOUBVWgni_prH9FpX1KHLSZBINSAid4iOEuieBV_QXz5vLqRUx8ujdpxNkBI9ft-wWzfCqPvsFV8-m6h_bYxkEmXx6Kg2kNuOo_NrpyObRTq4wljlAANYfiXGLhrbesh61DHi4EXpzE-s_loASzmcQ8gKTyWd66Myjq4_u-erIimqjyVaUHlkk1S7jCSwVMyWZDs-w4evizlOtzZjJ-LhyCBdQXuaKdSk65enxbaIUaclE7lQJzKBFP0aqJZyCjrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgps8NOQAYsHqo-C7w1TlHrRd9XL8LwNsfFZmHkgNogJTpgWoWF3EGCUGOlkitEOewg3HIpjSC0Q4O-Ohsk9q6YVMzHAccYh8bf6N7j-1n5tFMgyvtqXzqaNRTpZxKDG-knsvFwk6nau8bJlULZHUQm9eBc57QjbFXMllC77zxM6GiBuhV8Eu8CzFzSLpsbLrosxRFuiOiYu_2FxhqOSAMimmpWNULGEr836M0F8WrpwGL-GO8jahtedlfbqk25W_LC7DbcUqDn-PtN63KMkbmZIQZYu4HQYvGuDbxyqSiwDkI-K37ApVVxSvRMJtsOohrW-WXwgAafkG4xKVdc8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxCZqM90KVWnX2sBR0aPmmOl2LJFzVU8ry9RNId1sWC2ngzYKE1D4tre_Cv46WDTORTqmEp8G6UYBJtEFlxA4XyhLHhZ3h5ZI9DDqbGUj3GHtR6YeV_tD631Wp5p2dJdMBFp6FlaIkt355Qw318eDSC4dvfrUGpvTcZmcUIEamoua50ELP3nlBZ6w3qTzH8OGpFBjndCwEAV9dnorMOtUUrD0U58t0dg7jcPLmcTtdqTyQDnNkckCsd-1wq__3yvqhdcsvkOBRfb1NTEQ2TsaeBPl8mZwT-ox1wqsRS1fYjUW4Gl0GS9Iy-GSq0d_uRJfwZx-yhm944LQtz__QTZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cEyh-c8YVYFsOfkfDj9u1-I9RT181bb0OFdHohpS0w83bAKVCngZrgcJku4SZvzNJ5Yu_bXrjOQahC2Fj8W2-jO66TSZbmlXKAF8Ah-C3yCAtvU3nOAqJNScu614-bmn5eHl-rZwuUN2OHMC2alAdNgf6xOlFPNmMPVedFsioykcqKW9CVenfYqtydUtgOtWhfrCQIsdluJ2quagron3IIlhLAsckN9vZT0KpyKlsZ1UgCc3DVNU9gBQprEBoPQuK3kvaSM_rHyVmwfBKfZVPXuEURVb5HTk2OjpcYOPOlV8DuGYy0wdYYgvZELR8uLVcYkFV2AQH4DjwyBSOGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djqt7jeTchA0KXPM7lqatwKNrBdLhkqgZ_1hnp2CpInXaUlH89WnjTeQuI4AeuFqjyfOgKMbTYO4A9bsvsmHFpWJ2h7Mw18uFbHJN9E9h0s2OTWKKuWbiHH5x0_ndgmmZpwqAnDNLdjjjBK5jH6kere1u_cW5wbe12EywgaIf8VjuquPrVmZ5QoGxCcv-avOC4Hm2D_wd5hySonDHtD8BSK51WPdioq_5gTJtzp3IUfV9zvRKlMNXKpd2ufeSj0BKUFQsYItOTz5w1Ufnk8-MQWw3ZvFbw7QQYAPhpMeWPjW5iVklAldgMuDRJYNhdDtX0sYwVW1yfYjZqVfVFv4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmi_K5Lt3QJA26TTMCHJ-nL5DV96LSjxrZ3QUDZTl67E6p4tEb_4PpHkCuex-eS0z4-De-DvgtdYUQpscYMrwX0ovHAmrjZ5y_MyhxGpURAS3PvprxafpO-iofkrnIMANF3_kjpErN7uDO86965dkDCwiN22nZYppOF-BbdS7-xqkGlW98ioVGZfmQ9KX_Hl0WSlAZ6eDo5YJXEb--O_uZ7VgcC7bqms5_CdkEG6K6k1qSXrvX_uBpJkXI4DGcYo80pKfPuQ-6ga5nYUV170l5fEBUI41X2iVFcKePpk9opMboNrsGnMNIIfr_7DrRIP-MKStRz0k1H8eGOwQCiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnF9zx8bpbTSGZxaQgyRVW3ApJgIi5nDs00GtPz6dQRjUEYRLctTArX4dTDWDEzeADgTCgLuGFWS__KKlFAwTGgP8U3tSPIr2PzTMd-qzxVotz7vggJrbFKieD1KQhPRcsS2_DhZG3XbHbF5nME10R6vYFf6fd9CLNiqtn_TI10glwGpxKBdKFVafSzTzHVCX8Yso7Fa2MV_Z0b6n3rfYeGfWL5w-pBSAbGikHPHJpX-rFa4q3TT7UAH_4kQBTB7G4NuvSYekie119A0S-T78TgX8h8f86bwQPJ-xodduC0IZBXDTvEU42kftnQHRM8M8n68PL-JlnOnynUGftQJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4HmQcSZ_AdPWPW-W9NjJmuNISye5s-u9xVtQH2BV3q20MmzuEOmGghWO6YVunGEMuMe4t9wUdr1CY54XmI2ZdaLjZTJmHMeaPYYPiHtz4CDe5esuJUmrhKJu31ldPxzxtl3NtTj3Kd1yAMJUAR69DnP7BpwQFmegqGA_NiRxl_VWoMr3KxRBBjeyv9IUafuB5pkMzFpEri31i80wkCLwUp7so8y8rnEBAVqGePg2Pw2MGdow9g9B7q5t6avRnwvkiGk-Obc6CPSFNN3tD8MIN8vloESZA5J8azJijKDaR0oRaDjqdqjZ1BkhlUePsLEHnAwyAiuVgZMuzMMcgxxvvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4HmQcSZ_AdPWPW-W9NjJmuNISye5s-u9xVtQH2BV3q20MmzuEOmGghWO6YVunGEMuMe4t9wUdr1CY54XmI2ZdaLjZTJmHMeaPYYPiHtz4CDe5esuJUmrhKJu31ldPxzxtl3NtTj3Kd1yAMJUAR69DnP7BpwQFmegqGA_NiRxl_VWoMr3KxRBBjeyv9IUafuB5pkMzFpEri31i80wkCLwUp7so8y8rnEBAVqGePg2Pw2MGdow9g9B7q5t6avRnwvkiGk-Obc6CPSFNN3tD8MIN8vloESZA5J8azJijKDaR0oRaDjqdqjZ1BkhlUePsLEHnAwyAiuVgZMuzMMcgxxvvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CSoEXXFPLg9wcUQ_nb7CV6nn6PVPpopqWSqMN0TwQ6Mq3NK59s6AkYLHbsuzDHqlznZsmIU2nHeMSMHgG__Kje5_eaOQj_4Xe7KMuQvMwCUy7bnlUChyRB8xk7IJzUUKtPGLyzp5FumpNTtKPkJQ9gStDeE8CQgdYfbniZxiObskP9bYuN_m5vadcbN-wucoOV3jjORYhemO85I42gdDqfWYeoqTd2AVvS6E1FuIiK-suM22HRSLjkl0X--RWbdP2XTS_5Lec6wnow4KXlyq1BqapF4-wdsjXwWG06nc0XSXBAj0JJhfK0-E_rBzByVUIZhvZxrf5eYUjF4jX6zLAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CSoEXXFPLg9wcUQ_nb7CV6nn6PVPpopqWSqMN0TwQ6Mq3NK59s6AkYLHbsuzDHqlznZsmIU2nHeMSMHgG__Kje5_eaOQj_4Xe7KMuQvMwCUy7bnlUChyRB8xk7IJzUUKtPGLyzp5FumpNTtKPkJQ9gStDeE8CQgdYfbniZxiObskP9bYuN_m5vadcbN-wucoOV3jjORYhemO85I42gdDqfWYeoqTd2AVvS6E1FuIiK-suM22HRSLjkl0X--RWbdP2XTS_5Lec6wnow4KXlyq1BqapF4-wdsjXwWG06nc0XSXBAj0JJhfK0-E_rBzByVUIZhvZxrf5eYUjF4jX6zLAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=gz66sPnXjYc3iqW8vC8ob8d_H9G7YyDpw9SsxAK4v6kXWbwfdYwIHrKuT0m3sWlc787kiW4MdKeWHhUEyk-1OBn9Kzn1uDgmKU_O8zti4MWuPaUxuqVmXlTCT76OvRanz3EG0biO9LQwW8_CPO1rudH30HzhtI1KofNKE045I78co3vpJbtloKTz5ETSUwaPVTMa9ga-BjqAOoC74TTD51_9672ydRg2d1YI2GDL-ShEs80Jl3MoiK8EXtyu3nqapDL5d3LIEotvkPPgINwAPIvEtZmyB60Y-xr8EBJ5Qw0BnaIaD4okVeov-ILHAd39NlnYvAxcZ7eu-0H92m5B7krrL5-5tpH-D04-U2JKvndEywlswbnT8Kv9cZya1VXMfZiue9fZ7UAUdBDAnwNbh-6GRxMN99qcmSGzzEIyU-etTHHYjpWbyis2c-7nyCIVKgi_pSP00sAqnuY0oXNmqlj0YJwUgjh6AjZOO98pDK7aYWg71AbDH9PSEGxMkQZkDUgC3VmdIBTqvQ3argA93tjQDglw8hUeqtAUcasQjme5mF-5PF4YJn25j366oWuhXRCrH5mHrnFtxYxC_-Zmg6qMvIubWi9QmeR-SN_CfvaYf-XCO_TIQkWvNIbb6tbFvMg3QYx5CSfDNagP0blNUVuvDks8QpDreZ4KWOtgzq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=gz66sPnXjYc3iqW8vC8ob8d_H9G7YyDpw9SsxAK4v6kXWbwfdYwIHrKuT0m3sWlc787kiW4MdKeWHhUEyk-1OBn9Kzn1uDgmKU_O8zti4MWuPaUxuqVmXlTCT76OvRanz3EG0biO9LQwW8_CPO1rudH30HzhtI1KofNKE045I78co3vpJbtloKTz5ETSUwaPVTMa9ga-BjqAOoC74TTD51_9672ydRg2d1YI2GDL-ShEs80Jl3MoiK8EXtyu3nqapDL5d3LIEotvkPPgINwAPIvEtZmyB60Y-xr8EBJ5Qw0BnaIaD4okVeov-ILHAd39NlnYvAxcZ7eu-0H92m5B7krrL5-5tpH-D04-U2JKvndEywlswbnT8Kv9cZya1VXMfZiue9fZ7UAUdBDAnwNbh-6GRxMN99qcmSGzzEIyU-etTHHYjpWbyis2c-7nyCIVKgi_pSP00sAqnuY0oXNmqlj0YJwUgjh6AjZOO98pDK7aYWg71AbDH9PSEGxMkQZkDUgC3VmdIBTqvQ3argA93tjQDglw8hUeqtAUcasQjme5mF-5PF4YJn25j366oWuhXRCrH5mHrnFtxYxC_-Zmg6qMvIubWi9QmeR-SN_CfvaYf-XCO_TIQkWvNIbb6tbFvMg3QYx5CSfDNagP0blNUVuvDks8QpDreZ4KWOtgzq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYQ4cupVgeWVhd27SyjsXrlzL5BSVoSS9KRaFysxlwGIpfUo82wygHi3K6At9Ynw4pXYBAYJUKmbgSAo-Shx371IoRo5JhpidvzCSdX7cpQ4RM3Pz-7koy4aoBSkxys75IMrqXID9SAOyE3lalDGMOs_fMkCjZL79X6w2vsF1MQjtfsUQwGMpol4Bwlou4ZiSVtURwdqZXt9PF2IhECehjkt_vrFCXk5sHcM5bQxPVzuFpz2RZGtY3A7F_0zyiHU5dYp7sVpRIfazCtV0cqjxKl5xY2UUYwFkQy9cOR10K4wMKIcZSO_hM5qT7y-xGl7rRilroTwLuzHhpilFFV1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=K8-ebwy0ZxGtlHMR3jPCqUcFrkRg94S3zjtIbxliEOPUJikIWex0HVGiTOvzsylfLq4rldvxJ8gOzJgh5O3GY6KwmGsNDl4kxTo07rILXr_T502Y5vyMa90rQR4oBBwI1lJEsn7llT9Dz6T2ubdiJfTu1L-dcS-jNyZ19imq-l1lwnm9PYztEev85IN-cFARHB-lwM2QT4gY_XPeiUJpVjT5ASzN6utmQOMPHlXBRRF8kXQYU7uyxdbFcOnyXv47F0eGahZa9hfgdvWHyvsLmLUZs-NJI4wRMAJuAfnigcyPYBAgnPNbu_F4QdU2XlqhxikSRUE8aSZ9LOLmR8ujyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=K8-ebwy0ZxGtlHMR3jPCqUcFrkRg94S3zjtIbxliEOPUJikIWex0HVGiTOvzsylfLq4rldvxJ8gOzJgh5O3GY6KwmGsNDl4kxTo07rILXr_T502Y5vyMa90rQR4oBBwI1lJEsn7llT9Dz6T2ubdiJfTu1L-dcS-jNyZ19imq-l1lwnm9PYztEev85IN-cFARHB-lwM2QT4gY_XPeiUJpVjT5ASzN6utmQOMPHlXBRRF8kXQYU7uyxdbFcOnyXv47F0eGahZa9hfgdvWHyvsLmLUZs-NJI4wRMAJuAfnigcyPYBAgnPNbu_F4QdU2XlqhxikSRUE8aSZ9LOLmR8ujyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=L6IvjPbfPdc2r5FsMVMxbKKH61eCtPG9OgmcRag_oWecNYuzZ1vfbieTOHvVTzNKxHkkuNRWyBi6DemI6w8-F-p5tfGr3zhfnZxtC1AYWRmzpb2mywRAY2R7B6fCkNkbgiNOxjFP_0_o8dHhy256zpYjxhHXXYEAbkpjeOxFTD1LDikA7acnbE6mcWNbwoF7oepaLuPcSkcJklQ1W4pk3RwisNoDn1kS-R14WPNB3HEDG4E4FW7FqaXP6Tz5SBZGAK2Bll2Mib5wsYUtA8uHjFe-Cbalu7fcOODYYEN47u97iUQPs6mZ8iu3y0-DdUSFTXEWv9AKNOOZuK3rOo1JGZ3KE8BMjuOU1oB-OR6MHpKd7LO0nLCVUbSgq9FMlvQtcAFdaFVUo5GZrMKobvT7nxZ6-Za28VQA06y0-oSDL65yTdm7QhspwvunU383_Lh8CvypsTvHvSUy6-9fdvgFFR-tz3OL1hW5_uQifxCIeZzneh6d2Ef02h2Sr2FLe1RA0v32H70ws5t9P5tiapgSTz8BVf19chuVK27cWeGSJsSl5KovliWp4OVCK-fo_6-6K3Ln6EdCec49YJDqfPUTcHxoUhF21NJxKdq2YHOV9RcQjEj1vXKte-s0swgvF7mwuSD0IUY6ZySIpJuYb8ka-9EGHEOTA-bECi8hPau8-AU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=L6IvjPbfPdc2r5FsMVMxbKKH61eCtPG9OgmcRag_oWecNYuzZ1vfbieTOHvVTzNKxHkkuNRWyBi6DemI6w8-F-p5tfGr3zhfnZxtC1AYWRmzpb2mywRAY2R7B6fCkNkbgiNOxjFP_0_o8dHhy256zpYjxhHXXYEAbkpjeOxFTD1LDikA7acnbE6mcWNbwoF7oepaLuPcSkcJklQ1W4pk3RwisNoDn1kS-R14WPNB3HEDG4E4FW7FqaXP6Tz5SBZGAK2Bll2Mib5wsYUtA8uHjFe-Cbalu7fcOODYYEN47u97iUQPs6mZ8iu3y0-DdUSFTXEWv9AKNOOZuK3rOo1JGZ3KE8BMjuOU1oB-OR6MHpKd7LO0nLCVUbSgq9FMlvQtcAFdaFVUo5GZrMKobvT7nxZ6-Za28VQA06y0-oSDL65yTdm7QhspwvunU383_Lh8CvypsTvHvSUy6-9fdvgFFR-tz3OL1hW5_uQifxCIeZzneh6d2Ef02h2Sr2FLe1RA0v32H70ws5t9P5tiapgSTz8BVf19chuVK27cWeGSJsSl5KovliWp4OVCK-fo_6-6K3Ln6EdCec49YJDqfPUTcHxoUhF21NJxKdq2YHOV9RcQjEj1vXKte-s0swgvF7mwuSD0IUY6ZySIpJuYb8ka-9EGHEOTA-bECi8hPau8-AU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhFHBM7V0tMakzc8l34Rts0hNrv_E8Zoy5iaSiYpq6s7QteWzsAz6qBpEsSmyeQnPREllgnRdP0MiLnK75WanQeTtuEW1If1c0anuGwNYg93EiPlu5a8r6wEDo6Z6w5cKh4mHm2podfIwgxDsjvOEta32vTRPbk4RHNITnfSJwOkcfTBRBo96JeAUtUmLwz1st4L2HzaBO62j4aUNBsrM4JTSqka_xmRenSk8w_DSE708r4uWs1rWwtlTcSIpnRmpQ2Ltxqso6ctlnHsdTGtJQT-G09tP6NC16Q-3GY4jo2OLtMJaDkm_cHiKKVWjOilUhgwLvPjUJbBVknVqbz7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sRnKOH970TpNGPA_omSIGNlnVwPxI_tzco2LyGa-eNMTj-ozj_sYhGSdv22c-FUWG4P_X7qZdWyYnhG_MfGou_-0v6qYIKF7XlPZEyZPzTQMB4vqSJ7k7QGY91umUO-0ZVJuPmHyG4gXpxmmqewQTAZd1_-GEFsEwJYnaPIL1pQJim4LV8jsnap4ffpTQvz-mVwmTKfMelWBC3w9gTjCFXB4ohxJxCv4mOUNs1x2Lpl5bIh4OZntgIlj_tpfCTzYT1OjqBM8ulnxEDdsLxH4Pqw5nAXuKxLWl8ljBi1g6mLO5-bOiHGBjPf2enF7BaJ5ZAlfbzSfI0ASZK7lnzJ3Ho3-qNi3hyRM6IL7rvMFcLZsMjBwup0IwERpoWBNzmx41VlFZPBvV9y8VD0ydi1l2ptkXinpnK_kceqdz3G0RzNpVqoiOlJWbgBZtc34d-H7gy_dHyGGGspxJOBqJWK5V2-qxXzxIOQoc1TR94OGLwcf7rSvB8iCafODQMEz5oYpdcfNTodesfl0ZG05W7ClfC8NeAKZ4ggw8_nbN8-DWwQgX4Liyt02ZrrC-ggYcJXfL0xq605Qh4H_1ruFH3t2zf6Vod94VyUoGTJSxUfQJ3KLm23qLI-RwwXE6RKhgRMvyUxL-wSDK_lfrSw5x2YN07dH0w4JqHyecmgIe9X9Nxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sRnKOH970TpNGPA_omSIGNlnVwPxI_tzco2LyGa-eNMTj-ozj_sYhGSdv22c-FUWG4P_X7qZdWyYnhG_MfGou_-0v6qYIKF7XlPZEyZPzTQMB4vqSJ7k7QGY91umUO-0ZVJuPmHyG4gXpxmmqewQTAZd1_-GEFsEwJYnaPIL1pQJim4LV8jsnap4ffpTQvz-mVwmTKfMelWBC3w9gTjCFXB4ohxJxCv4mOUNs1x2Lpl5bIh4OZntgIlj_tpfCTzYT1OjqBM8ulnxEDdsLxH4Pqw5nAXuKxLWl8ljBi1g6mLO5-bOiHGBjPf2enF7BaJ5ZAlfbzSfI0ASZK7lnzJ3Ho3-qNi3hyRM6IL7rvMFcLZsMjBwup0IwERpoWBNzmx41VlFZPBvV9y8VD0ydi1l2ptkXinpnK_kceqdz3G0RzNpVqoiOlJWbgBZtc34d-H7gy_dHyGGGspxJOBqJWK5V2-qxXzxIOQoc1TR94OGLwcf7rSvB8iCafODQMEz5oYpdcfNTodesfl0ZG05W7ClfC8NeAKZ4ggw8_nbN8-DWwQgX4Liyt02ZrrC-ggYcJXfL0xq605Qh4H_1ruFH3t2zf6Vod94VyUoGTJSxUfQJ3KLm23qLI-RwwXE6RKhgRMvyUxL-wSDK_lfrSw5x2YN07dH0w4JqHyecmgIe9X9Nxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ikIq9IGfakOPZ4UTV3AEEtUFT83rvSDomstGGjBfs07zkXZzPWPFUx7unqqNh5l-ZVIxKMMo3_GGC23keMGS9Ye4iVl2O6BXUSBVk0hH84P2BK2hNNynxQYeY3xweUfxwB62hbBszGyMSHLM4l8uDxDLbSGIuokZUnHqXSFTjouXh3rJ-QeTxpDMlwhFO95nWq499qMfW-slI36raQV9xiJVv8EkTOdwc1Bltj6NBbTQ0FedV8ZKaAnp04plMtwmYgNzelI2VQ1MArgZPALaPi3ufvZXtVXE4mla9o0VmvR2OoBzNKaS9LRVTgesF3sq5RlImlOMj_mTJBI6RxwNpoLgOIBiBAcmnL06GxyCjyS-4jOFHqk6pQMY7v2J-eJ_lXE1cZxbyOvJcSSTfLYF2yjbWEPy0ZFwFZqtnsArC5wza91mpzD-nxl9fOaKvinZnaxSv-caqTgKkcbMiBUAjfB1aV9mGJLw9b5oJ_3F_4IXx_EAtkPLYVQAyQ5Tq9OCJjzM4iLsR9oxe_V9qOZDWhfaDUprvmq76uxqythmFFrSvP3BNal5WBzkR_1foGQv-7H_BXQdILmI5x4mFKStUI27yM8VyaCpSOzuUrzm0R-vKsH3pLt5yBB5fRkYn4008bYQiB22sXs371gCGxXkoD0_bFJtom0SppSHQvFsvCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ikIq9IGfakOPZ4UTV3AEEtUFT83rvSDomstGGjBfs07zkXZzPWPFUx7unqqNh5l-ZVIxKMMo3_GGC23keMGS9Ye4iVl2O6BXUSBVk0hH84P2BK2hNNynxQYeY3xweUfxwB62hbBszGyMSHLM4l8uDxDLbSGIuokZUnHqXSFTjouXh3rJ-QeTxpDMlwhFO95nWq499qMfW-slI36raQV9xiJVv8EkTOdwc1Bltj6NBbTQ0FedV8ZKaAnp04plMtwmYgNzelI2VQ1MArgZPALaPi3ufvZXtVXE4mla9o0VmvR2OoBzNKaS9LRVTgesF3sq5RlImlOMj_mTJBI6RxwNpoLgOIBiBAcmnL06GxyCjyS-4jOFHqk6pQMY7v2J-eJ_lXE1cZxbyOvJcSSTfLYF2yjbWEPy0ZFwFZqtnsArC5wza91mpzD-nxl9fOaKvinZnaxSv-caqTgKkcbMiBUAjfB1aV9mGJLw9b5oJ_3F_4IXx_EAtkPLYVQAyQ5Tq9OCJjzM4iLsR9oxe_V9qOZDWhfaDUprvmq76uxqythmFFrSvP3BNal5WBzkR_1foGQv-7H_BXQdILmI5x4mFKStUI27yM8VyaCpSOzuUrzm0R-vKsH3pLt5yBB5fRkYn4008bYQiB22sXs371gCGxXkoD0_bFJtom0SppSHQvFsvCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=u6IjcGrqhK1taLFYB5vSfZXjYL54F-9j_qhgymwyQQwivFrbdNhIlbVsfmKglcs1KjGLhAchp62eSlqlSm38V6lGrPBBtKszqTWiujerR9lrAskR1xcrZVtRO3YvbzgYBQxakW0xdri_oMKme2NlkL2PBUXAIXgrM_KDjYTdUXsPQ6Pw7kECzARVHmRVN9OzrDQSoG4mIhhkA8oUWChQhfwYWLd6PDRvga4fu0V1aD1B2lPJqmjNGTE5mcrsR-7kNKvb_At4q46dOXIvMkkLuW-PKFOfwghdbuE5gYUEBC5EC2dzKYuBYLJw98oBNO6PnDtLCQpQLa0GWGNw6Ak57g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=u6IjcGrqhK1taLFYB5vSfZXjYL54F-9j_qhgymwyQQwivFrbdNhIlbVsfmKglcs1KjGLhAchp62eSlqlSm38V6lGrPBBtKszqTWiujerR9lrAskR1xcrZVtRO3YvbzgYBQxakW0xdri_oMKme2NlkL2PBUXAIXgrM_KDjYTdUXsPQ6Pw7kECzARVHmRVN9OzrDQSoG4mIhhkA8oUWChQhfwYWLd6PDRvga4fu0V1aD1B2lPJqmjNGTE5mcrsR-7kNKvb_At4q46dOXIvMkkLuW-PKFOfwghdbuE5gYUEBC5EC2dzKYuBYLJw98oBNO6PnDtLCQpQLa0GWGNw6Ak57g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GrFqvEObLD_lFOmdYVXIQNQGYD3SmmBtAGOydRnPUQt_kpGhdl0aIFOQ36pKz5IR69T4VNn5oG6sxkehxXzSD2F4ucmoatxw8VSO8PjHtseTGtH9BKS-CZAqIkTn9FJOF40RYTci7Pux4UU-qPKvrdjcOLmA605jysHrcAQaem5iDKj1OrL0u1e5487uzt2i2Y3ZOfoRqh6cSnIDg2nvxD2YODWJy9gJ6weLzzYnXtVXlRxcoqElHc1_WS4k3zVTfI6CURmxaT9K_nWWYVrwjUWjnoytxffkHMW1CqU4an6mLRe0zM2ZmR37GdXaSCZF66VD7FDrVcQi83i-QJT1mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GrFqvEObLD_lFOmdYVXIQNQGYD3SmmBtAGOydRnPUQt_kpGhdl0aIFOQ36pKz5IR69T4VNn5oG6sxkehxXzSD2F4ucmoatxw8VSO8PjHtseTGtH9BKS-CZAqIkTn9FJOF40RYTci7Pux4UU-qPKvrdjcOLmA605jysHrcAQaem5iDKj1OrL0u1e5487uzt2i2Y3ZOfoRqh6cSnIDg2nvxD2YODWJy9gJ6weLzzYnXtVXlRxcoqElHc1_WS4k3zVTfI6CURmxaT9K_nWWYVrwjUWjnoytxffkHMW1CqU4an6mLRe0zM2ZmR37GdXaSCZF66VD7FDrVcQi83i-QJT1mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=cZvkHfxZmUEARh-7_koa4W_8Z_WxIiw_Pf84Y6kig4fDXS35-1eZRY2cyBmxS54qISYvm-BjT96PnRkVBAfXxbRcnMdoYFgYyTmj65vOrOHtN20y_TfOiGsfGEtkRr9y9QRs1pv27IbdQKisXG5o6wDlziWSnTyAc6Qk-oUCm749FhcA6nroUK3EaVwx5aWzCfwpATFhx4hJSWYM3TjxRTpwytI_wwqu0xfzNwO5iCmURHH6uNfdrHTyae2y2eA8reLQpkjyb2pbGy9VV_rD5oZRkhbOTzrZzkG5OGhYLxwep4-7bohx54OVwUBHWIzhr5-5YV7s66fLd1E8K_ywFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=cZvkHfxZmUEARh-7_koa4W_8Z_WxIiw_Pf84Y6kig4fDXS35-1eZRY2cyBmxS54qISYvm-BjT96PnRkVBAfXxbRcnMdoYFgYyTmj65vOrOHtN20y_TfOiGsfGEtkRr9y9QRs1pv27IbdQKisXG5o6wDlziWSnTyAc6Qk-oUCm749FhcA6nroUK3EaVwx5aWzCfwpATFhx4hJSWYM3TjxRTpwytI_wwqu0xfzNwO5iCmURHH6uNfdrHTyae2y2eA8reLQpkjyb2pbGy9VV_rD5oZRkhbOTzrZzkG5OGhYLxwep4-7bohx54OVwUBHWIzhr5-5YV7s66fLd1E8K_ywFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=YJpOO_iF8i4tpKNJx9cyXCXBsrdw6jwVczhDMrzu7Lhqzh30umnGTGFw1VDIQ0B2dmfX6sFM_Wc0kkOfeJowPmNhSjL8ja6kOeqyvgbyxlRNSWHJffA2pTUWD3uoiZ9SIKgHXGEE5W0XPaB10BaYkta3GcLn2Mi8tSgyjN360dfqHicEuVq5AmN3s5Y2WAhCWmWbyj0P7FCC65mRuCVEzPdcp2DsRYCayKkUcec4PN3cNSXaM2l-6SYiaroI-jkEtlvUZjzGC9aFnY0SfJHPwdWYpqRRX6mvijIwBGfNEXH32XDO3hJ4KAC-Ix3RojPmNoLCVNG3r4EImo-2FzVwZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=YJpOO_iF8i4tpKNJx9cyXCXBsrdw6jwVczhDMrzu7Lhqzh30umnGTGFw1VDIQ0B2dmfX6sFM_Wc0kkOfeJowPmNhSjL8ja6kOeqyvgbyxlRNSWHJffA2pTUWD3uoiZ9SIKgHXGEE5W0XPaB10BaYkta3GcLn2Mi8tSgyjN360dfqHicEuVq5AmN3s5Y2WAhCWmWbyj0P7FCC65mRuCVEzPdcp2DsRYCayKkUcec4PN3cNSXaM2l-6SYiaroI-jkEtlvUZjzGC9aFnY0SfJHPwdWYpqRRX6mvijIwBGfNEXH32XDO3hJ4KAC-Ix3RojPmNoLCVNG3r4EImo-2FzVwZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Y7sGT5gDPRhaKqEG3q7Rf6sctwmMGepGsRnZdfzjqC-P9CHQtEJ_r_37v-EM_cOd0JR12xmFN5-T3L5AC-NUnrkh9rYeTqAFdnLqsqcszxHu31x3_lGBg5Ne6_n59hqfT9eAPmesCr0vhQL-XqZmRpsKunFg9Q3se5WNZnkYUtfwi_w1gKFhlvo_a8BOzP2VF_PmZ8J3HguWrrl7lwpptaqRaBNoUWuBPPAQ1ATviRMl5cVAW7CVvIgcW4Zcq_ugUYrkZrw2228AgZUiaLS2TVTug_i0QbLpfkyZScuVrsmit8PANE3V2Yuc6W7BhIIOmGHGzOHrOyfGPGjnmFewuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Y7sGT5gDPRhaKqEG3q7Rf6sctwmMGepGsRnZdfzjqC-P9CHQtEJ_r_37v-EM_cOd0JR12xmFN5-T3L5AC-NUnrkh9rYeTqAFdnLqsqcszxHu31x3_lGBg5Ne6_n59hqfT9eAPmesCr0vhQL-XqZmRpsKunFg9Q3se5WNZnkYUtfwi_w1gKFhlvo_a8BOzP2VF_PmZ8J3HguWrrl7lwpptaqRaBNoUWuBPPAQ1ATviRMl5cVAW7CVvIgcW4Zcq_ugUYrkZrw2228AgZUiaLS2TVTug_i0QbLpfkyZScuVrsmit8PANE3V2Yuc6W7BhIIOmGHGzOHrOyfGPGjnmFewuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MdLunp9DBoUV5KfsXgNUGDPjFcq1A572KHQ2gxbTwDM0qeS6XpeLY0RcNfmnd50uKEz863Lt71Tc8z37mNmNNZXfCr1457uSvtdLUWyBcWKTxJqJnZRWDY9u2r8uFjup7ouppjoEqVbYUZIWw482O1K-tiV6ORED57JYYnXJRl4Soh9ba09xpg-eq0LhnUvmyMuLjRempEczaGbGfCdjLm1dGl2mxpikHMp_FUoiuUbunYRlJUqtcENUg_bhwOH1UgsSDNoJswcGXjUiqRHt5-jVQ-iLdr5E8MMGaOQf46HBc0ntU9O4eZ-oGaPbN5dLg9lPIgS79yxxxnW3MzQwyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MdLunp9DBoUV5KfsXgNUGDPjFcq1A572KHQ2gxbTwDM0qeS6XpeLY0RcNfmnd50uKEz863Lt71Tc8z37mNmNNZXfCr1457uSvtdLUWyBcWKTxJqJnZRWDY9u2r8uFjup7ouppjoEqVbYUZIWw482O1K-tiV6ORED57JYYnXJRl4Soh9ba09xpg-eq0LhnUvmyMuLjRempEczaGbGfCdjLm1dGl2mxpikHMp_FUoiuUbunYRlJUqtcENUg_bhwOH1UgsSDNoJswcGXjUiqRHt5-jVQ-iLdr5E8MMGaOQf46HBc0ntU9O4eZ-oGaPbN5dLg9lPIgS79yxxxnW3MzQwyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=RcZgsH2eNiPGqOadIcss5zUvROQKHTwDZTfo2X5cwRV1DvIX6Eb66UzHPrFOutKhbSdP8jWwe_BsOULm4ioo7sTEWlXWcobQfLD0iooUQzGw_2wtMK7reIXjYisnYz1JpMmzBBe7Gwz3N-Ufo_LoOQmdwt3fhPYSkWzAwwnyUwCsD-UFfMASuRhevBAKNWPOPwuDVY3k6P2g5jMp1cXDaY40SKSzY5WQs0GQ7PBxdypWwEoz2SGp630OSZO2c27ipyMNC4P1V5XmjlBu75rdEx6PgP0iEYpdP1ZYRfz3Yx-hbhOp-8MLt9esw4dOUqyu_W0XOF7wkdAHdRU52MON2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=RcZgsH2eNiPGqOadIcss5zUvROQKHTwDZTfo2X5cwRV1DvIX6Eb66UzHPrFOutKhbSdP8jWwe_BsOULm4ioo7sTEWlXWcobQfLD0iooUQzGw_2wtMK7reIXjYisnYz1JpMmzBBe7Gwz3N-Ufo_LoOQmdwt3fhPYSkWzAwwnyUwCsD-UFfMASuRhevBAKNWPOPwuDVY3k6P2g5jMp1cXDaY40SKSzY5WQs0GQ7PBxdypWwEoz2SGp630OSZO2c27ipyMNC4P1V5XmjlBu75rdEx6PgP0iEYpdP1ZYRfz3Yx-hbhOp-8MLt9esw4dOUqyu_W0XOF7wkdAHdRU52MON2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSlGaYlOSY97QgJJdf8WNPT0UzwZUIAp2xR3WLN97HcvCZz5CAt3oP_9Quld5ozE-pja4Ve8n3Cq8lSuWzC99sRo3rESnktGAWVgHOQdXCSwXde65nz1Gy4UWEMLMIESMXnOzQfQd340EzddG6iDeJRi_4er0lUPNhGW4TCA8b2WBmf0tZlWepbpcB3n0VrtAWe1hgxO-RqOjFRCYgrO3KzffQH4iCSgfLVcB3FJh10Gk5fof2RpwOXCCg9cBWe3jAG1DV1_wuWYwO07mQoQscdbYzY2hQMwt4DeKBn1i3n_dtqglAj_CRYeXOgXvwWR5RY0zzhXBhC03FZ8qJ_HWA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Szc-dayRV5VvhWcu_YWPMbpCDDt5-6mDC1mrqcJD0qW3Hm8ja1vbinovBOCGWsDmEvCH1iVGesTHKeAHVq0dNu5mo4qu3q6JLfbLJfl3wz15_p8SSk9tP2P2J59LKfSppjq5gfEzDCdfOUA5aj2DqiClkfdF0c1qkM-Ln3nMiznVzMvsP3yglaoesxqrbZh2u6vtFBIOfc-erVg-lU0tlcenYlwzeXUOOgdm9G5huZyyTCSPqNoqWD0Z0JDerWSWst6rMZ_7TO4i-7yTJYdViKc2Rft8rbQSFCMnuDBeM3NfgeeXhgJXNQsS-moLRblTjCkyPYdMTr-gzzDEt5eVpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Szc-dayRV5VvhWcu_YWPMbpCDDt5-6mDC1mrqcJD0qW3Hm8ja1vbinovBOCGWsDmEvCH1iVGesTHKeAHVq0dNu5mo4qu3q6JLfbLJfl3wz15_p8SSk9tP2P2J59LKfSppjq5gfEzDCdfOUA5aj2DqiClkfdF0c1qkM-Ln3nMiznVzMvsP3yglaoesxqrbZh2u6vtFBIOfc-erVg-lU0tlcenYlwzeXUOOgdm9G5huZyyTCSPqNoqWD0Z0JDerWSWst6rMZ_7TO4i-7yTJYdViKc2Rft8rbQSFCMnuDBeM3NfgeeXhgJXNQsS-moLRblTjCkyPYdMTr-gzzDEt5eVpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=FRIbrqPKOrSRiot-tuV2zWebqlbtfZoY2BNoK2jrwKeiLYZHzHd-1u0oUrXSOMjgi93BcPrG7Lib8ORtQ4s2uZU-4eO8oj5xoJo8wpk-FcTXmiWmT80F1NrXahNcukb6oqiKPjNRPMRH4zqUZI-ZWuId4o6xQmPBk-GHYkNUqHjRz_jC3nFwKfFHdOTST9I_0u1A09f0Hr1XrRA67JJtO_hgVOGASZaq8MIQ2JCmtrUX8WOc4TwEqOeMUrQTEp4qvQHMnsw80CHyZik0ftV_8_TXqfgSinFSVpu-LHUKj4vl4TQTg0IT198uoy3e0EJy-zbpe62OF73-fDPfPFw4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=FRIbrqPKOrSRiot-tuV2zWebqlbtfZoY2BNoK2jrwKeiLYZHzHd-1u0oUrXSOMjgi93BcPrG7Lib8ORtQ4s2uZU-4eO8oj5xoJo8wpk-FcTXmiWmT80F1NrXahNcukb6oqiKPjNRPMRH4zqUZI-ZWuId4o6xQmPBk-GHYkNUqHjRz_jC3nFwKfFHdOTST9I_0u1A09f0Hr1XrRA67JJtO_hgVOGASZaq8MIQ2JCmtrUX8WOc4TwEqOeMUrQTEp4qvQHMnsw80CHyZik0ftV_8_TXqfgSinFSVpu-LHUKj4vl4TQTg0IT198uoy3e0EJy-zbpe62OF73-fDPfPFw4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=k97CMYacpzFDnfOhUhm7l9up1sKmS5AYwj8YycfC-ftCmt9UNj9_hNnFGGdTFR3-nSJclVPF8x8bUKgYDopNSzpTlG_5GaymF7DgwlaLjQMJ35UW1d620KEZjzTBJTi9iqilOOJRm16iAUM8px7wNViUYliabrq2H-KfFqchS60V6DYHR1cweOiXY3jXhx1VLubbwpy6vbIZmBU06Cdt5Il-qOLqIkmXIsmRLdJSHS-vrCVqir24Z9Sl4YDk7cixdlBqTVltUrpbsAazxPe5FFRp0bpwM4Awajn1iPDSJRM7B6QPQfL8EuBeqeKJayWDPGP3dE1nSGB6WhMyAC3w1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=k97CMYacpzFDnfOhUhm7l9up1sKmS5AYwj8YycfC-ftCmt9UNj9_hNnFGGdTFR3-nSJclVPF8x8bUKgYDopNSzpTlG_5GaymF7DgwlaLjQMJ35UW1d620KEZjzTBJTi9iqilOOJRm16iAUM8px7wNViUYliabrq2H-KfFqchS60V6DYHR1cweOiXY3jXhx1VLubbwpy6vbIZmBU06Cdt5Il-qOLqIkmXIsmRLdJSHS-vrCVqir24Z9Sl4YDk7cixdlBqTVltUrpbsAazxPe5FFRp0bpwM4Awajn1iPDSJRM7B6QPQfL8EuBeqeKJayWDPGP3dE1nSGB6WhMyAC3w1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ItnPhHQ5o_ZuAEzVi4RnrxC1IDBh_URJYsPI1yXXI2QD9PgcIKAyGnRT-eOkSB4aS8KiYpVcJPcz19q5Z0-Q0TSfe5NHFtADwLUkVxyikvuq9lBX_CD-9NEQ5SsnkIh96YMZZDzIns9u7RrMJ4kDDlLsCF1Bs1l6dhg6ffGJFL2MkWmQv78lq0nHaP3aPhanK3AYGvNBVLk4_nLxUk83NCHDk-VO_89Bwa3PD1buhLgfM50eqKdh2Bk5kwjy0HqUrpxV2aeZiTKkXd2wuz0rtxOVUCoibjicYxRe1gvNbTDlShrB00hEErGhV66pfD0iu_MLpX-APeO4bkQoeaOF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ItnPhHQ5o_ZuAEzVi4RnrxC1IDBh_URJYsPI1yXXI2QD9PgcIKAyGnRT-eOkSB4aS8KiYpVcJPcz19q5Z0-Q0TSfe5NHFtADwLUkVxyikvuq9lBX_CD-9NEQ5SsnkIh96YMZZDzIns9u7RrMJ4kDDlLsCF1Bs1l6dhg6ffGJFL2MkWmQv78lq0nHaP3aPhanK3AYGvNBVLk4_nLxUk83NCHDk-VO_89Bwa3PD1buhLgfM50eqKdh2Bk5kwjy0HqUrpxV2aeZiTKkXd2wuz0rtxOVUCoibjicYxRe1gvNbTDlShrB00hEErGhV66pfD0iu_MLpX-APeO4bkQoeaOF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD69BDvo9Q8kP_o_lK8jNDpVwpR_C4BhwFOyrRIUuykMuYgQD-C9E1HQiBrTpH8CGAXF07x_qJ6A29nYE-I3JBPYEjSKWCeUKgTbc4b5wJWYWhOirvPO2Lj-mu5elOk6ibKFXX8oZemkXgOd1FZ0hpAFRgNMOGegLzeziQfWvpGJKxLmPL09XRZPX_hbuLlWfWea4p--qQMcqqHC5By5T7essqgUzCi-Pg6A7iElLu2mEy7eNpFU8Hx0chMpLeJ86Xl_h9KAg1ckG17EOrUuPCM1L2ILaW9XHqYYExJV72m7x7maxAMSAb63iIRf_KgrvU1OfFGQiwtRpGF82dTRbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=r85I7tQ0Iwvgr2e-nbRsWFpLDn2sr45_53BKS5rj876PHPNr3P8UtdLvaKppntfholFhahOxcADluADdocvDQwQ1-8ZKCc_zfE4CpRRVM2rPAjLXKXXlSyUWhYqxI9ytY7t9x0kk8-bKvgRuZKT9VMcWQuO5YmFpWMtEayhDs_NLIbl_OMgOnqCX_zMGSQ6Kvtn7uyt4JHG1S36_Tu7fNYZLtmpyln3DUKDVZkW01uHxXoDfmfs4RSWZ2_ByliWmrHwhuD7cSiyHIfoR8xwzvBSRKHOcIaBWKf8OQmv94NGPmK5czyf2BVe_GaxX-Hr2CJSVLj2-_ym7ejg-5_vrOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=r85I7tQ0Iwvgr2e-nbRsWFpLDn2sr45_53BKS5rj876PHPNr3P8UtdLvaKppntfholFhahOxcADluADdocvDQwQ1-8ZKCc_zfE4CpRRVM2rPAjLXKXXlSyUWhYqxI9ytY7t9x0kk8-bKvgRuZKT9VMcWQuO5YmFpWMtEayhDs_NLIbl_OMgOnqCX_zMGSQ6Kvtn7uyt4JHG1S36_Tu7fNYZLtmpyln3DUKDVZkW01uHxXoDfmfs4RSWZ2_ByliWmrHwhuD7cSiyHIfoR8xwzvBSRKHOcIaBWKf8OQmv94NGPmK5czyf2BVe_GaxX-Hr2CJSVLj2-_ym7ejg-5_vrOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=oO9-XtrwbePDvKScMj9PIloADxz1nH2mkDfxxIWBr2BynlcvOBIlpbdCIo7frbw76QY2QIZFigwGwIkHdhPDqD7sLbVbaCG0KLiINd32-ULuZTWLsin04JFFC3u_uLrKK_wk5FBF573cmBt-Zm_pR6llzi3NwbMcMP_CGsL5zU4ZymPKiOjq6Hu_nQJJduq0__ZvFQlhLkK_EtyQq47wviGcY7zIH6hXHIE-kdu3f5fdbdE0kkR1jVKhpyuD4q7kKg6LFMwnzwalzxpHKPy8ltpZQeNdhujAfzCh0RbGz49hiu3uC0lF8iOHVTiVkWKVRQJkiSsQ7k27timVo9qd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=oO9-XtrwbePDvKScMj9PIloADxz1nH2mkDfxxIWBr2BynlcvOBIlpbdCIo7frbw76QY2QIZFigwGwIkHdhPDqD7sLbVbaCG0KLiINd32-ULuZTWLsin04JFFC3u_uLrKK_wk5FBF573cmBt-Zm_pR6llzi3NwbMcMP_CGsL5zU4ZymPKiOjq6Hu_nQJJduq0__ZvFQlhLkK_EtyQq47wviGcY7zIH6hXHIE-kdu3f5fdbdE0kkR1jVKhpyuD4q7kKg6LFMwnzwalzxpHKPy8ltpZQeNdhujAfzCh0RbGz49hiu3uC0lF8iOHVTiVkWKVRQJkiSsQ7k27timVo9qd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDbe7wvVQAXZ7ovGaO24DkAzYMs8zbEulutozb0HCVbTqCMhAx87oNB7t558Cb3ekoi0ubBsrFLPI2WbH7qlb34Udob-2--5tjwmQgfQX4Le1wsFbmoYussPkCOmLxd8s_uevQAO2DcSjn6JQIUmUSE3NIde0pXqsxIVsXDv6ETFVMVFcLeh63sl0gSO8_Seix6MZC2-KQkQ1wKqeVVKgE-FaIfcYeMdY5mYX4OLwLPc-Tgt9oSMhLk7N9oI9z1682xCaX30k238p9bnFLGzGTOCXKVJZXMSLtlC6Nl9b20erg0JXSfH1Pcl-K5dpma7xJKbxrCLoKySOA1HxXeeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdR3Eq0GCGfam0aHAgiJ9mBiI6KzEjzvWtRPw1gE98GYKlDn6ToOVBw4wvNErrkMtnIyJyixq182BuaItH__ZopvaAOEkAGH6JexY2WRuCGiThlIlnbLlMu24a7OHMBJP5Xxo21J0tTKFBW7Dif6eNNuJmZdLS96bu9rdE8ZFRZ2D7oR3uWV9r0j5Wp7mvGsv2GIHDvPwYx1eMPxqcihY0zXd0_zwVdEmWXUWc8SQz0SfdoceNNKRTc2pIDelYmtsQ8kpRjchfEMRm2rTNo3D0A7uFV9Mzl-fybV55LhbZan6TQlszAsxkJZ83yX8nnyXJ1yIv37-1_V-WxsH6jTew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=bQL_jWlRbYO3qJmRJIEA8E78Qg90Zn9kHOPPaxWxwUpEIT5XCMa3KEzW_BeGwsqHjkGUnvfqwxZ7eIKdFmtipFYAz1SPdqB9aoCc3mR_QgKRyuqntrjOBhvmowNExi54NPFu5lTppOE5bhUsSD1VKr4FkeAnvr3U7e2k6SYBMJcu3w8QaSNAKgzLazL--OMMhlBHPDCyuNItrzSnyi4byBGH5i_SdzKmf4vp924IE97IffXqEa5-20CEUJTovVBXL56FyzuLnbh00_JoARU8JtZDFoWcPnAm1KDAN6I_rL2udcc0qVGU2Ulyce-JKmDTM__R7m-jEragbcUAYqK1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=bQL_jWlRbYO3qJmRJIEA8E78Qg90Zn9kHOPPaxWxwUpEIT5XCMa3KEzW_BeGwsqHjkGUnvfqwxZ7eIKdFmtipFYAz1SPdqB9aoCc3mR_QgKRyuqntrjOBhvmowNExi54NPFu5lTppOE5bhUsSD1VKr4FkeAnvr3U7e2k6SYBMJcu3w8QaSNAKgzLazL--OMMhlBHPDCyuNItrzSnyi4byBGH5i_SdzKmf4vp924IE97IffXqEa5-20CEUJTovVBXL56FyzuLnbh00_JoARU8JtZDFoWcPnAm1KDAN6I_rL2udcc0qVGU2Ulyce-JKmDTM__R7m-jEragbcUAYqK1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHPzmtC_SFoOaaH71rOF3e3MDxejcQbZTJoSk4jZofXJurhuWqzjPFTyw4yLqsOUZYwNJlCheZcH2Br1EuFoJ-Og91d5iLGwnwOjsPImD8iRHWPss_HzBJfddu3fWMBCPX9AmOb9o6c2LMRox1DuKlEm7lFVIfIhpJaeXpaPoS0z55C_huezPU8bl5uu2JE8b4XmmgncOMP-d6WFB1Qgv0muta__A0WVOEqJ800D7UkBI9T1bhsrf_zcOWO6hEBOUcxzXOrDBMKHHpRJbtRmvGzILBN9OUwImmeTYT6SQZsAyBBgLlG3BWA4mEDA8QCDEmTF_FpQl-Un5mJESfKWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCiKXwh4XbvWVZ_paCjkT-FOynWfHBU-hd0DG9bAG45TL9JJ6ud8HlcH9VRIuceHVPdqJz4P-YeEiUdc4tG6vGn3pydpC_tVXD180W8_FXYbl1zrIfwacF-df_hye_Mt8rhCUxfNM30uaxrWkJMey3MJSoseyVMLDhFkvKh7n-rmJlmi3kTwkhk-Smt4xbxL0etSK9n5vmPZ8hZt-NAQnOvTVXIWeM-gLvzZOcIJ370PYmrZD3E1ftlNFomm88QYxJws1bYVgyivDQJ9FWIavmL-c5eRZuxphEG0juFiKC-UiQZI10OB14MA-wFvSVqdj-1qTt0XDMnGAt_dB6sTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEPWs71lMIoC2ld0tykX6YFLI25VIpOQVS-ABjMvginBtoKPz_0h4clVzSewgQK8x2zLOUrcYet6rhADKo1CwncXPWtBfQa44qW4QzWg_8AJV4YrDWWmA2CpSj13mt3iMtA6XpUkM7f6UjpScYgrJS55YjPmp69lr0S68ISlKVuTXM1Pvgf-4GqhriOoPEUnifj2EVqL9ZJJDUMktKZGiRBiq90qFvt8b4Rj-luBRH95lj1IvKq3eUX97eppUSFgPUE6a0Wq69MZbKgGWi4Z2F_opRQSeixIbsnlrOZ4Oyx8rFXJX2u1-SMUMljAvwg9YbtKUruL_j1ImJlgzg9gpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=GFsVQOvhkWQW68ulc6us4BmWC96IDsbyVFQRZsXE1dW5oOqD7qCC0wVvhx1f4JeJUtuQGRHiPs4mJDexXsDr1NYaiCSrOVK2KFAU7bT8K9v-fpaBQ4QGixdrR5tee9U7-_OoLT4f9UjFkcu331i8Uv8Yskg41JUe9LqoHv4V-fwwGlTBWW4kEoLrqkYIiFq2scXPe2wD_F-8IE6Veq-GKNjW4RSqxiBvLyoo7rUV0zBJ3sxXNtQ1Y6FHGRorDwdaLDeyybyXhhH2HGmWT-FEk2pGfJ9mvUcyL9mv5VIozP7w9iZdEs_zifAXTwL9i_eTCcoe3yhSgoFk2wzrZopzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=GFsVQOvhkWQW68ulc6us4BmWC96IDsbyVFQRZsXE1dW5oOqD7qCC0wVvhx1f4JeJUtuQGRHiPs4mJDexXsDr1NYaiCSrOVK2KFAU7bT8K9v-fpaBQ4QGixdrR5tee9U7-_OoLT4f9UjFkcu331i8Uv8Yskg41JUe9LqoHv4V-fwwGlTBWW4kEoLrqkYIiFq2scXPe2wD_F-8IE6Veq-GKNjW4RSqxiBvLyoo7rUV0zBJ3sxXNtQ1Y6FHGRorDwdaLDeyybyXhhH2HGmWT-FEk2pGfJ9mvUcyL9mv5VIozP7w9iZdEs_zifAXTwL9i_eTCcoe3yhSgoFk2wzrZopzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=IybxHLXIPDYJCmlqPZwcz255R5ygGE472MzbEbRRZzvyy-S_OCsXLJSMWtIxZq5OsTQCM2oWwAjsoKp-jc5R8lMrGTvStVRhrGe63iMo5kgF9avZAwOd-5hc72qMdmGAa946cvMryPAVfbKWwCpWum9t37x1vOFN1vucoWXrvKeZOPb6sGAmm-Puvap3LMFNqeYDg3_M5WxY5U2qahWuYgFbkByMBcjO3-Te5wOQcgtvScMLpYIzpRYnU6qGy9MRn_HYvmweh4ePX40U2NWsNUbYTciM7J4M0SgO3ZsS7FgdHgXqYxPcFr8l2-GAyTAXFRnPmHumBaU9mCe4fVeXxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=IybxHLXIPDYJCmlqPZwcz255R5ygGE472MzbEbRRZzvyy-S_OCsXLJSMWtIxZq5OsTQCM2oWwAjsoKp-jc5R8lMrGTvStVRhrGe63iMo5kgF9avZAwOd-5hc72qMdmGAa946cvMryPAVfbKWwCpWum9t37x1vOFN1vucoWXrvKeZOPb6sGAmm-Puvap3LMFNqeYDg3_M5WxY5U2qahWuYgFbkByMBcjO3-Te5wOQcgtvScMLpYIzpRYnU6qGy9MRn_HYvmweh4ePX40U2NWsNUbYTciM7J4M0SgO3ZsS7FgdHgXqYxPcFr8l2-GAyTAXFRnPmHumBaU9mCe4fVeXxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=YJYghwm_iFcJ4BXSrVqGjofmc5-VSr-QdAvfPxztPBtqe1cZLr5s1ybjLjWu0p2bc7A9EV9AJ-gVsmQql61xG9SaLLIm8IB8qg4oWJ8voZSCq4gvbtj5nmCcO9iryOD-vUh-D2nwq7IDsoqUmp7WEsnMn7zst3o9Yn1AiuFn_h_JpH7NovVr-t7tLAZbALD2yzkEjM5zPTqBEG2dlPjLLBXfyLZlYRec7WXoxhpVrv0Uteplc16o9Utry9xLjtGka7qO3ugpSG5rh8kOmI_zubWZq1vPWXA8XUNUzluvbdlGppV6D-JonkC8I1vKpzmrOYwlAaTzMKKN7vGyWDfG-r7slmbUQ149h8O6VYcoL8JzfqdsDxExrLPReqXOxcSkfNDjoThb6rFFhB6bTWp7yzsXAwsLggYTg0XDvMq-v__YZJ0uITO9nU89nmIBkjNppA1V0IP92FP8dHInWKtozqzZOH8RW-mm_s0gmHQyj82V943nFEwQ7c4oSlEmjjWEQnHQ9G22bDeNSFnPkOSDMBXfIIgz3YnEkHSwDSqqD9VUFPwWdIs03P9uI43v9bi3-sAHID6twgCTPDVGRfuODGqXM8fiCxpbUpX6Dha44lAar5rre5ax2Ka7_lEwUnixDQlu2gwbNodMn-WfhLWEhJZ4AWN0lGdb6FQ0XJQuzQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=YJYghwm_iFcJ4BXSrVqGjofmc5-VSr-QdAvfPxztPBtqe1cZLr5s1ybjLjWu0p2bc7A9EV9AJ-gVsmQql61xG9SaLLIm8IB8qg4oWJ8voZSCq4gvbtj5nmCcO9iryOD-vUh-D2nwq7IDsoqUmp7WEsnMn7zst3o9Yn1AiuFn_h_JpH7NovVr-t7tLAZbALD2yzkEjM5zPTqBEG2dlPjLLBXfyLZlYRec7WXoxhpVrv0Uteplc16o9Utry9xLjtGka7qO3ugpSG5rh8kOmI_zubWZq1vPWXA8XUNUzluvbdlGppV6D-JonkC8I1vKpzmrOYwlAaTzMKKN7vGyWDfG-r7slmbUQ149h8O6VYcoL8JzfqdsDxExrLPReqXOxcSkfNDjoThb6rFFhB6bTWp7yzsXAwsLggYTg0XDvMq-v__YZJ0uITO9nU89nmIBkjNppA1V0IP92FP8dHInWKtozqzZOH8RW-mm_s0gmHQyj82V943nFEwQ7c4oSlEmjjWEQnHQ9G22bDeNSFnPkOSDMBXfIIgz3YnEkHSwDSqqD9VUFPwWdIs03P9uI43v9bi3-sAHID6twgCTPDVGRfuODGqXM8fiCxpbUpX6Dha44lAar5rre5ax2Ka7_lEwUnixDQlu2gwbNodMn-WfhLWEhJZ4AWN0lGdb6FQ0XJQuzQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=PB2iYoI-oOV__bU3Dwk4xU7C8xfQhkfCcgxHYGPWP4LrNUFi2WhYkQwfslypc8tvUqvddgGipjohuBcLhrNFC1_YALTyt13acysGv0rzB66-uiTAe3NcBN3cIsL30rtAcWbB68RQvBMjchngwfdmJrz8-8scSU_1GN7L95umWD_5GYVrGby-aEIRrEjLlqBqUCylF3m_zLdFfk1game_n8zLCZpaWG0dmJeN_EBvS1TdxASjbJKdJFdgWHxogk5J6U6C1Gu29d8vjA3-emA_VL2wacmf_-awrVGWGRKeW1aL0WTBe2y5vbWNOVTVa-GyQ6bc7iS7YywJBfj32qvYzbR2cyIe7TiijzN6eVIBTvDTad72R_-YlbrDODEb6FI-13lvMrUP2_pBY4j1_ggau9KdJfUWNRqFZSLNgGb9ISfQRGje3lwy-t1VIqeeKETdlAMZD1c8wzKuzViG88o3Lmubj5n3h5C3E424MPwSxSlaTYRJy5X2vQDvnTEx6J2XWzY7u5hIe3BUOAhmRaDKxxmHdkBd2YI3nSXUCPCEAyanqYDSW14BKA3fBAR3lWZnHfTlN_einHzC11K67A1UPJqeMGYxaZCZGw4zmYzIC32HZ_LJ2TewEf68pGnDRNJXAYTDScrEgDde0rUyhHzVAooMk8gp_H3d6Mk990smo6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=PB2iYoI-oOV__bU3Dwk4xU7C8xfQhkfCcgxHYGPWP4LrNUFi2WhYkQwfslypc8tvUqvddgGipjohuBcLhrNFC1_YALTyt13acysGv0rzB66-uiTAe3NcBN3cIsL30rtAcWbB68RQvBMjchngwfdmJrz8-8scSU_1GN7L95umWD_5GYVrGby-aEIRrEjLlqBqUCylF3m_zLdFfk1game_n8zLCZpaWG0dmJeN_EBvS1TdxASjbJKdJFdgWHxogk5J6U6C1Gu29d8vjA3-emA_VL2wacmf_-awrVGWGRKeW1aL0WTBe2y5vbWNOVTVa-GyQ6bc7iS7YywJBfj32qvYzbR2cyIe7TiijzN6eVIBTvDTad72R_-YlbrDODEb6FI-13lvMrUP2_pBY4j1_ggau9KdJfUWNRqFZSLNgGb9ISfQRGje3lwy-t1VIqeeKETdlAMZD1c8wzKuzViG88o3Lmubj5n3h5C3E424MPwSxSlaTYRJy5X2vQDvnTEx6J2XWzY7u5hIe3BUOAhmRaDKxxmHdkBd2YI3nSXUCPCEAyanqYDSW14BKA3fBAR3lWZnHfTlN_einHzC11K67A1UPJqeMGYxaZCZGw4zmYzIC32HZ_LJ2TewEf68pGnDRNJXAYTDScrEgDde0rUyhHzVAooMk8gp_H3d6Mk990smo6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aeB7QfwenEY7HLk7atJL7iAOlg5Zr6jFkPrnl3cXa1E-gaItBb8Y9ELsy_pAxCIHOjpKkbKriFdGySmPyKu8q2TwvcDcrlxu-iHMwSKteu240HlyD5-QrFA0AG-S2aF1JIrGnAeYMWuOeOw-3-7UOH8N4gXqimrruPifYiazBmdINxDV0Iw-jvLSXfctUU7KbG4BTEaxhKHLdElibx-qxBTsaI6QoFyadgh-AvPWoCNzL0Yy-a4qaIxxvU9kX0EWXS2bJ_Hk4A_RliUFKsndDmoUbmFkcsVx9pk4H2lzzW_3qLS56xnRYM5oNzfwTVpJePVAnWl4Uf6xJjxuO5L82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aeB7QfwenEY7HLk7atJL7iAOlg5Zr6jFkPrnl3cXa1E-gaItBb8Y9ELsy_pAxCIHOjpKkbKriFdGySmPyKu8q2TwvcDcrlxu-iHMwSKteu240HlyD5-QrFA0AG-S2aF1JIrGnAeYMWuOeOw-3-7UOH8N4gXqimrruPifYiazBmdINxDV0Iw-jvLSXfctUU7KbG4BTEaxhKHLdElibx-qxBTsaI6QoFyadgh-AvPWoCNzL0Yy-a4qaIxxvU9kX0EWXS2bJ_Hk4A_RliUFKsndDmoUbmFkcsVx9pk4H2lzzW_3qLS56xnRYM5oNzfwTVpJePVAnWl4Uf6xJjxuO5L82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXPVqLo2Q9LjrccCWiPMvj6HnN7fwEJi7sH6aB3Yx0L_4xqJixTqpJj0djx1uwzPxqRwXvBGtVkgBd4sS4_dJpe3HdLMXaNSOz6BxlVPzO_PkV2NZLowarbjyOgTKblswOdtctBmcVU_-ZW7JcWrCW7l5ifUGmdBELl-3RpE2MHSk0AQDC7W56yHSL8-XTgvE84EKi1qQZGA2YD7IDLiQu7k_B2THTAohruq1An0rK3VQaXykBgUSnU9VqKHghIAMY3L52GlAOmIBtf8B9Pxkm_YYod0aWe3NWYLGmNpB6zg8QMDSoJp1hNysKm-9-ZOnV8Pq1EblCO30grVC7zAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=U0G_7pVl82D65kuBfSmTvg1-0lArLiPMIAWf3yOlI18MnptBf82qqxT528P7Abu4PeVtA1k_f4vA0Gdml3cauwB1X-ENbHOv-FVesvLyhIgV3uTlfTw57PQQrJaHBs2zb42OUqD0JYg4_4g73PGUK56I3ZhdKzgqA5QpPhtlLZbheY2TbbJujlBTAyiBzCZ0E7mjOj1QpIVC0w0h7fhuLLXhZf6cjkSiOkgtJ50wtisWVRlbX0yR5ev-7RxIFi5b7PwPsk0hYI_WITUxnKStvFG1H3p0GbBtt9T0jwtOblQfUb2rQiWkXkVTHsyJY2GLg1DbxN8zHE7Bv3AZ1MQZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=U0G_7pVl82D65kuBfSmTvg1-0lArLiPMIAWf3yOlI18MnptBf82qqxT528P7Abu4PeVtA1k_f4vA0Gdml3cauwB1X-ENbHOv-FVesvLyhIgV3uTlfTw57PQQrJaHBs2zb42OUqD0JYg4_4g73PGUK56I3ZhdKzgqA5QpPhtlLZbheY2TbbJujlBTAyiBzCZ0E7mjOj1QpIVC0w0h7fhuLLXhZf6cjkSiOkgtJ50wtisWVRlbX0yR5ev-7RxIFi5b7PwPsk0hYI_WITUxnKStvFG1H3p0GbBtt9T0jwtOblQfUb2rQiWkXkVTHsyJY2GLg1DbxN8zHE7Bv3AZ1MQZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ERVM1e_RJZl1NRcmVP1_r7XYQgHF2eS-H2Y_etC4JEtoUVrLlJV1fGQ9QWl-FKUj0JRMRn94Z8X7AslxyejydFFcYqhy4QpLgXMBsEQ4wlV2IVV6yznpj_IXDXYeXi7CeIfjIYOYPfNVdS-1BxewM569GTkQXVWFXXhKzk4BSNro0_KaK2pj2JfhfYtJpZf5hVZIde_IqsYfiHaMtwVaYYp0vnZX4xSaaCVMMj5En84KaIJrFG08DbW9xMCAsVUds0EHmANn9HihMfMq6p1mpgc4HYikw0unTUPb-z2D54907PHuJCjlbyXkV_ulSfaLio6y9c_0q16Fxn-7g9pq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ERVM1e_RJZl1NRcmVP1_r7XYQgHF2eS-H2Y_etC4JEtoUVrLlJV1fGQ9QWl-FKUj0JRMRn94Z8X7AslxyejydFFcYqhy4QpLgXMBsEQ4wlV2IVV6yznpj_IXDXYeXi7CeIfjIYOYPfNVdS-1BxewM569GTkQXVWFXXhKzk4BSNro0_KaK2pj2JfhfYtJpZf5hVZIde_IqsYfiHaMtwVaYYp0vnZX4xSaaCVMMj5En84KaIJrFG08DbW9xMCAsVUds0EHmANn9HihMfMq6p1mpgc4HYikw0unTUPb-z2D54907PHuJCjlbyXkV_ulSfaLio6y9c_0q16Fxn-7g9pq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixogtcpL02ybl9XdjMVni-6-CE7VFSpUnGk7RpskqLGSo0HSma0NlLKExwsmkkSBYYifYgw22mmiuS4Jb7-Up2W0ndwpLcrPkr4mbaA6vBywdsfzp4QpT60tXC0V4hsmpH4yfOSasR2YVjApJ2nR7hrnx2MxU_fd64WmsLTCPPBt7fSnaeDV3vmyjdmM5Ul4yB9bOHt3VhtYyhjvz7uUguxhVaO-xDNrk8_HTGbjKxEs7FhxsV-WE5DouXTGLZ37z5W0ZnQDjmN25IzMeAfJixP6KaUG6938Roo37fa9YZqcl02lZvYU1x-jYkUQfLNw4-qeW20OR8rtuZs5p0IPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChNVYCPxwi_QkJkCj3JdJ1z6d1WOEyQQkO2StX-Nku1mrATIdZmSUsGCAiCq3v6FLOT9xfyEugI7ByjPU9p73v9cFqTLza3kLvpfcfQmA_7RWbHPpXAyEUYTMuA-9Q5vA6o1eL2RCFYPiqk8hoTnqfj9zZdBs27dZq_IEHeIQsTZ-6IA2UVln-1kn7inpy1zGzG8IqDE-Mtd5DNo0nd5LSw1FvVCSXJonoSE9CIiqX1GYPcZP53lvt1cdLCEvACIcqMAWHsMJ94Z4xk3z01xhNVVRBvbrPhcA7-uLzP686BBRI9NNNm3jFPrFEei67Maz1o8VNEXhfC-RSrtAqWS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC5R3HKWq6Oo-k983s3oiTsQ6qawScnt10Ih_8kOQhQLLkGIxAOegsczc8hzH7U_sOw6wf7uZjJmzla97Pxd6gwEh1cKL56fAtcwqO3lbRFq_2PGrJ5AC5XUb-UXKrr--azpoMcqd0HK-mEE7zBwMTo7el9CnLJal_mSq02hmvjlFrzk3ga70YrhNnQXPJ1fTKSi9hoLnbFa_u64qLkVkUTCPlmN3JLs7McnoH5Zs25p_ynldZxS6bAVV_MFotLShJlWTiLEN6d5hPCxih57e6eCr6DLeFdTZmNcHZGtq4P4o157-K21g23-frzI25u3MnnmmGwlZt4R2j4qml0GOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcre7L_gKvuuw0HHy03wHRQdPXqns1v8lfyFOoTzXfNUEJN-c0W2CxCCkYJOWKYcC-xUIeibRJj359tkht0SI5AgtwEXk-pwZNpty_tJybttnaeCzxBb4JfdFlgmoSW06ytzI7_cDdgsU8aa4cmwBsCwAB54cPN9kfe2zLQyD_rZy6DJzy2rQixQ2RhccQMh508YbKuDvL4KHQLNRynkaiQLTt5PfmLT1nSwvfwDC1GOWOAHpkiGe4Xx030gf2Nc5FRqff66Twq1EEp26loqMZapIfD8DdxhGKRdi-38g4FpS_ZiYrJlAWrTb1IZsnD2b0kl3QfRjXeIpkfJG1Tm7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7ZqJJNWMQlbcD8bLyykBxxjSkxlzr_u6_j55q4j78-rfYMEuSAQu0kUEUGj8HP6ivUC-AcH1VjnSZUL6NpxyLucmFSSy588oByYGx4DfWFyYhR-6cDvTWoqoz2j5BaiHV3mFyqGBjxbmQoPcwZc1qvahPGaPk0nVCxJyBLEaHIZyStenJi-xYx9fNViGmXRCYq1njy4WCIWDU9yMPbrR4w1KSWp2BZT5JMOlfE077U5FTY3QRfhrEQ9iOR1pgPPEyHx41G8BrLwibyJIYhTSVJsvPiNiOgZqPFd3sQXykGbv5DSzwIm4QEI2I0NcLcs8eq1iU-4nk1aQIJuq_6ooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1JK-2PiMWzlFaf9PotZiJRAtw_zONGy6WaSEBoMFqVr6NXQp70RCFgiqQx4FfwC18DoHK6zFDi3p5f-SMJItTtQiTbt3vdnCKZ3mEpGtJfvxyQMbFdOD2OdESQUw52OkR0zilkCTU5qxVP8wa4Oo2fW8XpyzOa57uEXt10c_oHzWBZ_yvi7tF7sUhQuFBz6pkclYH6_C-lhNz1YSjcca3qWvk6Rn02YXW9YaChQTuaCnw9iXKxcnpATCRiS_SGly_Jyaj98kztKA-VlYG2hT6RbNVZNknBMFjAv4rSOUO_Pmzg7VaCsEYWj3Raqu1wjwi3FciB0v5XQuVDmYASCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y96cS1IhuvL-jWNTuUQv8TLq7akGmVjkSwB7yX1ncc-XcIbu9IPtT4X_7hshpTXieBRxJTboaIUTX1qIWWxWM1Vxj9mClYT73ZnyxzUGVTZi6EPjKgVv06aBEtspnNKcHXjL29q3m2xPN3V7qJmWOPvu6UnciY8sX81c6o144ck4H9DntBoqEevfUiFtKKvrQLXv_x8x6PfCTRv1C1VAPCnB_wi-FbXSv-6k8UdJOQcFLjeBT5iyyQx6hISJaTbD1mXuQNLe_ozWYyVFgQKi8h2wjzxmdXTRNMAkR-5Uc9jY3l521NE4IbdN_bx4xl6xHFb9AamEu_5WyoMFaYv28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKy0zMF3E5Nja0rj4taWTcQd16WlPX2Ge_OZbSq8kx--C90vSiFhHf7tNLCsSPSOHvfacltGJfdrU5mlF78x9vUBriCd59NPsQr0y7w6TOyLVvdaV5-WWuJym1L_WF3Q59kXX5RLc1Snl7-FynR5NM2bd70gOFujIkTKo8CrLs0iRPQYlox7iTW6-pu8zqiNTwKFnN3GeVzsTLbqIIbhjPDuUmBOc-1BcBVEf3B5KwgtqRenI9Cs65FmiDYx5hZG9W8EQghqtGA6oztbNbb2YwD18e2MLerBkrsbelLh6wHIpXd41F7fxltcwOBtwB8TNgVyxUSyCm9nuqnnuzk0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oewalLkPrQ4MGMIx5EAri-xd_Z9k5sXjwC_LdKbxaQ8QAy1rZAvquP_eoi1wNUITeg6TangOc8nhaQtjIVa_4lBt4r_Ky5vqeoaikxz5NFiNHJRilxzSQhq0Tfi_294drUmo1N7vOSaBnC9Ko1h5oIqvwgqNHCoS6_rPwEWbRs-SEseFbrmrtJKds-AXvn6ZP8Ym_6v-fimNLlyWi0w4VZl4RFuYt_gChKnU_ob3wwxeXCOZCpIfKGzxGcpPMHl_wVPjOAepmVUHr7Og4M6BQ5-xOUlRleBzSChsXTBjCn2HlCFJiengJReKCGsM3ju6Uy--BbZ-cLgjhvmlyOIAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGTsj3G8I6UCLMr9xOgHfAvO6twIiBCpcae0IVsmU4OIO5Nda4s4UUcZW4S3bfYdNsdad5iegwMB7Z7DYknI2Y3-mhzvn-zEmmBUPIV3PLaJVYBVtRO91u4-LuWUEIAvx7Qcp_fwvyOdytxKYH34sMJp67EnE-0XcqKY7iXMeTzoJmWjT1_XUYU7cuqIvgne43BEFzwyYbTDvCHOvJCkw7uSuetRgl-NpOzE7jWmp-5gHuFs_NhGLo67uG7IvT8EfTxDW7XjyDLoW_cx2svpHzF9oPhvcQ9-M6OjNZt2LHONQhJPRHvZVssJHCR1a1a_Irl-S8iZrDhOuu93lFuQbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=j2kzW3y5ySnlaP8vgD3juCEDq5c0VJjLuuNUnYkSYwXwOeYj8Ai69tqZ8iSiBEzcPX_eH6g72_beumyvbQaPNCbX9mnogHACFt9xGPSasfS9-h4aTHvlRElwARZgPbJt90inmpKc8OfODLoEw6_GoAemHhu7hW1mUpupXTFLJ6uT7GKYoV5Kwdn6J1aaHg-AV6vhLnPsRB0k0IpR51wdY4WcxCkFkM812OT-OzKx8Pa-dpAAFaZc8gyBT7kiscJ4nQ1r3GcAoSPqGSXHkURxQbjS_Yavhrna2SZfKv3DPyZ6c1fIyO51NVBR-E2m1kx2yc1CUYl2O7N1M3QATwULaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=j2kzW3y5ySnlaP8vgD3juCEDq5c0VJjLuuNUnYkSYwXwOeYj8Ai69tqZ8iSiBEzcPX_eH6g72_beumyvbQaPNCbX9mnogHACFt9xGPSasfS9-h4aTHvlRElwARZgPbJt90inmpKc8OfODLoEw6_GoAemHhu7hW1mUpupXTFLJ6uT7GKYoV5Kwdn6J1aaHg-AV6vhLnPsRB0k0IpR51wdY4WcxCkFkM812OT-OzKx8Pa-dpAAFaZc8gyBT7kiscJ4nQ1r3GcAoSPqGSXHkURxQbjS_Yavhrna2SZfKv3DPyZ6c1fIyO51NVBR-E2m1kx2yc1CUYl2O7N1M3QATwULaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCmrTb-yV8tyO0p1XdwGZwdJ8hftdkDFD1vVjrY-40r_6KD7L27VexUiUhwPB-WmFJ3ehMssW8DFV2UNEyXylAKbH7RrzoQiakzFD_23Sq5OlcE-7yttQtYLHwVE6tvlfqFZ75NfaxAvyP0lNy5nloO2uLkSq6KJCQKqczL35Lcrfx-MZGir1FqajKBs6IX2SI5PA0QlP_gdSWsp7VFYjkzj6VSV2l25DOjg5A_DQy8zhIZIVHkqyyVZsNE_9mPz2IiLxvHIaZrisHOVQtK0e2f87HJVuzVFlCeQIZrwvTYaY7EzlnW8_btlaxPs6YTwymeDCMIx2G3JQTog9DkFMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpc5jlqIc7scC72s_SaHs7Ak9i8jGoBShW7ARA6j-ZZHggvC1ZKg8V7TMfz80zZC2X_iEMgEQ_uxKzPz_13YjRktJ8k_4FXY1pkPCUM1qlIR8E0ALV4n0d1Zs-AXyNSYPupwGRhgjZuwBbib1K5IoyO-xl28GgatBwe2HonNvIear8SdjILclPWzDvTPW3XYBNGhi-8QckZvc730f2j2CD_I3zDuqI4YrPiJ3BgIHLMtW-qwOka83_yLveCXpwuTKrdP0mSxMsc1BfUfpr8b4SGsaEGMsGbmiqMBCC5Rz46sLvrTn973HvPHBrkWaG31JWPi96rxyV1Pef66uP-Ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=i1ihzudqyzcQagWjZqDDuDwp_vHvorxU93fvLwEur1FYOdQ3b8U6nbkf3E_zIfuOxlMTx14U5IsKxKrkmTSTtoVY-Uwq8RrTWtPYcA02gwKIKRWx4M0CkBeaU6BBgU4M_8wQihXO8_BN8LcejEDE6DXTghFLjBuIx5FjuGLg1Fxfs7y5yisB_4hYB2uzAVqe0H1FmZAbJwhwLobYptOvKZw8hrcyRpGGhp_4wEYy_gdPux503kYsJhyYEEoDAkSrUeaMysjnjn7RvqiQqUP8Hr1Fm0KgScgHdF43uaPHP1XFRcz-i07q5ss2G-_gLFsNyiGW5ComaN641yajczGiKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=i1ihzudqyzcQagWjZqDDuDwp_vHvorxU93fvLwEur1FYOdQ3b8U6nbkf3E_zIfuOxlMTx14U5IsKxKrkmTSTtoVY-Uwq8RrTWtPYcA02gwKIKRWx4M0CkBeaU6BBgU4M_8wQihXO8_BN8LcejEDE6DXTghFLjBuIx5FjuGLg1Fxfs7y5yisB_4hYB2uzAVqe0H1FmZAbJwhwLobYptOvKZw8hrcyRpGGhp_4wEYy_gdPux503kYsJhyYEEoDAkSrUeaMysjnjn7RvqiQqUP8Hr1Fm0KgScgHdF43uaPHP1XFRcz-i07q5ss2G-_gLFsNyiGW5ComaN641yajczGiKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=SMwJOLgb8ZJj177HPaMTbe_3Vqs7Pd2TtgEOIYc6OWpNXxn2uvB8L5PnxmSocXreZYr73FihzbkwyTb11Tw1-3MwbcxGKtzIefUdD8mDp1GwYTcBA9TMww0oYCI2xC7t5QoB0f5m_YUZ881kmU2ahGZApEohAQ4sULwLyjKuSotY_aXpX95-k1sc5pSC9ZF6ZY1m2qvXoCRQCtEkd65OLm4MUL8AY1zPNsrMaWIcKHjrry274-dmb38aFRc6rpZXgvhKaZxK6taEpBgqORuQ1CeihtCj4voFVhCTaA_Xx6VnLkwwZUIQG1cG-m4PldblrYI11HHXYnmust-LITZFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=SMwJOLgb8ZJj177HPaMTbe_3Vqs7Pd2TtgEOIYc6OWpNXxn2uvB8L5PnxmSocXreZYr73FihzbkwyTb11Tw1-3MwbcxGKtzIefUdD8mDp1GwYTcBA9TMww0oYCI2xC7t5QoB0f5m_YUZ881kmU2ahGZApEohAQ4sULwLyjKuSotY_aXpX95-k1sc5pSC9ZF6ZY1m2qvXoCRQCtEkd65OLm4MUL8AY1zPNsrMaWIcKHjrry274-dmb38aFRc6rpZXgvhKaZxK6taEpBgqORuQ1CeihtCj4voFVhCTaA_Xx6VnLkwwZUIQG1cG-m4PldblrYI11HHXYnmust-LITZFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-oG2EeWKCPPMd65DPQ7i5Fjv0bCd89H1hy0PdB4heZ8LK4WDZHkPI_gdbywTt7_Yqo_RkPWvCiIsOd6zV8_2ukySTgbF7ZSyWIx3Tz3O6HorgWQfrbW75YLaeWOTJMCj7zXugxYiqYKn6F-na1ss0MBv_r9z7UHm3f96U45xzL3OnPskwHJxqQ9FJ4K3zZUVVXNHWmAFV2a37kMTMIP1LpPiFLdsFQtY3qaIE2qAl2fvBHkSuJRZ4FPmV0o5nzQi6T4ko8F_tB3W_MF7XsxQAFX1NRPErCCh7VjeP9IYL0rq7CN1wSbWxOnRaHuNg-npNAGZtn8prCMi46QdKyjDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiEr2v56QduHW99hbR4e0OWHNUkdFKCkAEmgCg4ghOa3QhRRfGzWpQ4c_lpXyeAVMaO6drbuWwHPxCEOJKrAFQypNKcP4nXxzWOyZTVN5ViMO9S4rZnWfApIy0z0lRLFDE2rjWPmUerM2bebow23hGzdepgQBrgWd5z2R8iv6CGOrwaz6HFBITin05BoOlqIHlqD4Acb4cG3Jyj4vZuKV2QPnWCaR_pKVZyz_WGgDDKZMw1vacIymRxJllmLDiM20dwTzULtTIflAPxx7wcwNMEt7JyFxhIK8DACMq1X-KmJwGhiS7vU378o5CbjeFBiticPCP4hA1_O57LdvX6bSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0ErIrCjjjrLvgqSwJK8rnhudFzYJIi_RR5PlJ7np-Eo9BjflsBDD2knRt_2VX_0YzP90VXJjzCWg6BvyvTsWpFArD7ztQfjXPEe-Oeg-KhVdRxlmTWJ0j43iKHyiwfV2UT9Z23uwHr2CS66A9YIDHioyWswDMtmGBYEvoPFuX9uGKnvP_IQ7UW4B9sv-RnXg2Ikm6vdih_NvsW0EVjJdo2_tqXSfSvYtagpFB_gHapiGi2O8eVvr_EkynU2EDY3BXNGmiPHUBGuDJLh6E_CdQeqr3250FB9fJ_1xmXCg0pxhbvStdOPmuvlX75rf6xgyc52FhIq-YlkxoeGhE7N0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrjkyLOjVdUQW9kQ5cT2Vu8LZVv0P20schuG5RU69dmPVbm_1XX0j7KXwM0Kx78oh3sju69x1rZlDgjLIBxs15s1bOSUxf4Z_hlr2dhAxJog1sfXp4siTqdAgG3vi6LWttdutmDyLHLMma-ycsnSCwRNrzwpZMxyiQKmXPmii3hy-yj9BCLXB1lNX0fBS8DBIcdG6KZLCkb8tVdKsDxb0krKNMU8NNftOik-IkfNxSvg5JwqQbWRNcsHdJWBd0vPYl0n-WkgPeZl3pRSv64UZRA-E8BypO57OBXkVrAdIV_I6eSL4fntXUXb3RJLmt6vz8-GfB8yxoY5SmtPn4Ul0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSSCZ_vjO6CwW_-KmE4RP0O-Ji_StQkRC683uVf3-pFiqn9dNcFoV1MkdUnLzelMZxL1kVsvu9GPnA-e2p37p-wmRKLAfg1Mo5dbbcOl0NUuHpToiidEUD30DqRei26A-R6SAU7TBcoxqyHyFcKpMssS5GOPuxEiQQMv5KlAgiQ-StqBMApboFO7km5U9_2Y7kFJzRfjQe-xqOlRkU-odeyk1IHDPvkrmQoRhRnbm8ZAG_R4zsiA7xjHJUgTbnbhRRM2LsRUA1Vkf23tHkVSIcYl3Het14Y63U76qTX9Kp1vTVTTfutF_j7UQeZXliyQuwWzfd8XRucjNktNmovxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNSRZFGPMIDCN3yMn8YswBwLDvxfDJoJfnAS5KFpBVPXbVYCEWCn-5DL-TWGybpOC4O91WAy4fq3bJ79Uwa-dbWvopvag4utRs0J93glztl7iNpu2ViosDdDYOh-cd3LbF1mtVigB7VQ64DHg3Qu5WFJHiToDOHWYl_YUr2PO4ZWhceqIzNKidmBYr8T817elGyXg4JCJkDn5815RQ3RcKBqH87Q-8dfYVnXdEoO4uihpPtN-LmsgqCGQLSZsUvt8Fa1zbBQUeSuvssdOGumW_WmVFrPcrIc5yNxz5MRYATRZyRBI8QC7rCXbOChonIc4YGk7lxLvDlHtROyjotcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao8NvnBwbAPG8p2ePbxZoDiJXpT4pXxPnrTq6XUy9_H3ipbOz5XjktSzSzGIxz969trUvGr_DbjJDy-UZTEiUL9Sz7tMeSd2vYwqjw1EqOHzw-JFGyNTJJvbXuIfagoTkkBUF_xf9ALvZEG8r8U-2SfCIxlEOrZdRjEdO9BT13AV_uHTuTWFY99SjnOn4u1M4Wz7IqgtWd9jd4j3gWbs5xxdeD3Z7DR7QM5XNv5DY7G8ipKzKU6oUNM_MVM-0siNdMj57PZkI87mo0StiJvaOAhrJJZ_u9kVYOlke_DvAXCrIy6USXzO0qz_Np-KbFqNnD5hP-uV8sN0sjQZcPc1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4a0ssFwljubm9yVSrmmi3oFpBIYNlnHELatIy0OUH21OnjzYaa5KkASmFZh91XuoTFKB1MUnLsFgiu4MAu-wHMUtjwqPhOR6QwS_oMH0ubEAzWaQB3Trl5lKGRPMjYSJ8JjxsClmJjG3937YdUKP5WEIrVA5QJ6s6xkuBno5Txf3zKZp_dXcPSetd97vAFZ-DoqByFfj5LQlbBIWlRpNIrzfi0hMqS1nsD9tCujJuWKnIKGNtEmSCgFzXyMqbCN4XMlg-V8gHcqIHXUfcyrkZ21toRF1XkTDwuBzT4JRJw5b2RxOZ-Svbbg-URjCs20Pgwy8-WUAmYg-P6ydckZyg.jpg" alt="photo" loading="lazy"/></div>
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
