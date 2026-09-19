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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 19:05:31</div>
<hr>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgps8NOQAYsHqo-C7w1TlHrRd9XL8LwNsfFZmHkgNogJTpgWoWF3EGCUGOlkitEOewg3HIpjSC0Q4O-Ohsk9q6YVMzHAccYh8bf6N7j-1n5tFMgyvtqXzqaNRTpZxKDG-knsvFwk6nau8bJlULZHUQm9eBc57QjbFXMllC77zxM6GiBuhV8Eu8CzFzSLpsbLrosxRFuiOiYu_2FxhqOSAMimmpWNULGEr836M0F8WrpwGL-GO8jahtedlfbqk25W_LC7DbcUqDn-PtN63KMkbmZIQZYu4HQYvGuDbxyqSiwDkI-K37ApVVxSvRMJtsOohrW-WXwgAafkG4xKVdc8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxCZqM90KVWnX2sBR0aPmmOl2LJFzVU8ry9RNId1sWC2ngzYKE1D4tre_Cv46WDTORTqmEp8G6UYBJtEFlxA4XyhLHhZ3h5ZI9DDqbGUj3GHtR6YeV_tD631Wp5p2dJdMBFp6FlaIkt355Qw318eDSC4dvfrUGpvTcZmcUIEamoua50ELP3nlBZ6w3qTzH8OGpFBjndCwEAV9dnorMOtUUrD0U58t0dg7jcPLmcTtdqTyQDnNkckCsd-1wq__3yvqhdcsvkOBRfb1NTEQ2TsaeBPl8mZwT-ox1wqsRS1fYjUW4Gl0GS9Iy-GSq0d_uRJfwZx-yhm944LQtz__QTZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cEyh-c8YVYFsOfkfDj9u1-I9RT181bb0OFdHohpS0w83bAKVCngZrgcJku4SZvzNJ5Yu_bXrjOQahC2Fj8W2-jO66TSZbmlXKAF8Ah-C3yCAtvU3nOAqJNScu614-bmn5eHl-rZwuUN2OHMC2alAdNgf6xOlFPNmMPVedFsioykcqKW9CVenfYqtydUtgOtWhfrCQIsdluJ2quagron3IIlhLAsckN9vZT0KpyKlsZ1UgCc3DVNU9gBQprEBoPQuK3kvaSM_rHyVmwfBKfZVPXuEURVb5HTk2OjpcYOPOlV8DuGYy0wdYYgvZELR8uLVcYkFV2AQH4DjwyBSOGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djqt7jeTchA0KXPM7lqatwKNrBdLhkqgZ_1hnp2CpInXaUlH89WnjTeQuI4AeuFqjyfOgKMbTYO4A9bsvsmHFpWJ2h7Mw18uFbHJN9E9h0s2OTWKKuWbiHH5x0_ndgmmZpwqAnDNLdjjjBK5jH6kere1u_cW5wbe12EywgaIf8VjuquPrVmZ5QoGxCcv-avOC4Hm2D_wd5hySonDHtD8BSK51WPdioq_5gTJtzp3IUfV9zvRKlMNXKpd2ufeSj0BKUFQsYItOTz5w1Ufnk8-MQWw3ZvFbw7QQYAPhpMeWPjW5iVklAldgMuDRJYNhdDtX0sYwVW1yfYjZqVfVFv4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmi_K5Lt3QJA26TTMCHJ-nL5DV96LSjxrZ3QUDZTl67E6p4tEb_4PpHkCuex-eS0z4-De-DvgtdYUQpscYMrwX0ovHAmrjZ5y_MyhxGpURAS3PvprxafpO-iofkrnIMANF3_kjpErN7uDO86965dkDCwiN22nZYppOF-BbdS7-xqkGlW98ioVGZfmQ9KX_Hl0WSlAZ6eDo5YJXEb--O_uZ7VgcC7bqms5_CdkEG6K6k1qSXrvX_uBpJkXI4DGcYo80pKfPuQ-6ga5nYUV170l5fEBUI41X2iVFcKePpk9opMboNrsGnMNIIfr_7DrRIP-MKStRz0k1H8eGOwQCiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdCZkXWmAK-z-SCDarSmag5q-GnQW0tlVyecvNhue25Q0HCfaDbvpJD32j8xnP1m2Vv_PBgt0kqfcRbStoPwSOLMhmXAiSIRHGIhVTAaB10IYl7YmAIWjywrAweASsEYfwJjMb7jarYyS95GCSXafLfiHY9bNAmNH18aHUqlg1xmDGOWWHmvdwfxDv1ZkmS9VgC94F5n3vPme0BXiMnJjntyc7eKmM5hPqyHOGkUrAT3G_0WQH2c4K8vq7rAF6TUuROi03iL413UgXO9PxXQTku4HVogGQNIyTeh9BaJHY3X3-Bqw8roN0Z7rFKO3VtkelViTJPfUET0v9rsg8zxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNvJJtnqrYmnGNhbDOqN_fWq342poq9juwyrhessflz5G1bFJctVALlIqC7w64xM0VENWNtXe2qqAJasVO1zz9GvlZXQ_NwSQrdykkd66Xpk3TZ6-rApeQ0bn2dqTPW2o58r2Xw6rRV7ieYqcr6GRaLOeLdikj1VMxPzoS09Ls0mJI75C9unez8Zye1AVGkIOpXQ6Z5ybGNfbCaOdANprzMCFRguqQZEfuNtmNsZbSYkTDm23VOyXIG2sNX7_kNwM_Y3l61Q6lbsAE9q54aUpoae--ofcONXk2DqZDmoWvraAVsPYDvQqogc4KYTfZs3NpzOoiXfXPVRVSRpX1nC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=IzD2-Zm3SN9pzy0PS1D9hp5FPWvIRK1JCeE7AkcyFNYWtrAxqslP7gC6WQFz0cp05Tog7EE6sERCiBt1_RxOXYOVQV5vP5oIi4tUq4rMlrIBgvco682Bo9Fhxn7sDtRCroinBQZBfpryE3u3j6mSPiaCfzqm0_lPEle_GF2vh2WWW0oPt9OsiFtEPeec1vorP8DRJuMPmmbSSspe3XJHqVyfBIr4xRaalp-dwy0GYakSywIvaJWH8bdZ3njPs2f4vo0z98e4_CzaKGztxfSEOPTt3byGjJQievNExu00LSe4xPDaD7D6YvFMSSQuM7T6RhxmbkXCVPkyb3bSMt9n9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=IzD2-Zm3SN9pzy0PS1D9hp5FPWvIRK1JCeE7AkcyFNYWtrAxqslP7gC6WQFz0cp05Tog7EE6sERCiBt1_RxOXYOVQV5vP5oIi4tUq4rMlrIBgvco682Bo9Fhxn7sDtRCroinBQZBfpryE3u3j6mSPiaCfzqm0_lPEle_GF2vh2WWW0oPt9OsiFtEPeec1vorP8DRJuMPmmbSSspe3XJHqVyfBIr4xRaalp-dwy0GYakSywIvaJWH8bdZ3njPs2f4vo0z98e4_CzaKGztxfSEOPTt3byGjJQievNExu00LSe4xPDaD7D6YvFMSSQuM7T6RhxmbkXCVPkyb3bSMt9n9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=KHNEQv6-0pK1QmqLYZw9Tj5RXAlk9ohcmF-wJsv7L_GC9-0FIARBhwZe6_lJsCpjZPpQmlqKD-KKpfSWHLVCihXUqkTK6xnhvVQohC_xmSiVn7LeD0pz_grrNpmmWMf4njFfyiIi_Si7DPv3nh1teUFuaRMGsd6Z5Au59JZ_Ncde43Xqy1HlgAHhMhChVGcppYDdLBAM7i9tSLryp8RVGzCk51N2cX6EtTw2AQLglhVLFMAGsyF4A0uu0Npn_swUiGzbbXM_ICtKpSuvns9kwt6gf2SIpIImizmUPU3iqgAHsX-wwTAKchB58I-g6HQ8tKH403H2LKCvjelofqvCgmfuRiER9FQFERX97Nc1kGx27_uMB_YNM9XCyg6Sl3u2SleRKGtFvVujl3Pbmz4F0i55mwMrR1l28wPIsyjUVA2HUwnIxU0Cy_pP5y1rugShl_7gB-iAYl1nCxAnA54xP5LY2_vuNiBqiJ2kGsZEJLiz_vlka50RGMg_vC9eoti-PAjCArsX_EkoGPOIr919WjtZ7YbBHUAzvhnq9R_zip_pqNCg2s-VHoQMXaR1RvHN1A2MX5bIuDBCxR6DpdBv5aK8cYy6WW6dUOz54GU8QNwWX_d0QZeTegHGc9JWAHmqmbCzjg9O9z0AhgFxM41s6UkGtF_q3KEuEG0-9kGvI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=KHNEQv6-0pK1QmqLYZw9Tj5RXAlk9ohcmF-wJsv7L_GC9-0FIARBhwZe6_lJsCpjZPpQmlqKD-KKpfSWHLVCihXUqkTK6xnhvVQohC_xmSiVn7LeD0pz_grrNpmmWMf4njFfyiIi_Si7DPv3nh1teUFuaRMGsd6Z5Au59JZ_Ncde43Xqy1HlgAHhMhChVGcppYDdLBAM7i9tSLryp8RVGzCk51N2cX6EtTw2AQLglhVLFMAGsyF4A0uu0Npn_swUiGzbbXM_ICtKpSuvns9kwt6gf2SIpIImizmUPU3iqgAHsX-wwTAKchB58I-g6HQ8tKH403H2LKCvjelofqvCgmfuRiER9FQFERX97Nc1kGx27_uMB_YNM9XCyg6Sl3u2SleRKGtFvVujl3Pbmz4F0i55mwMrR1l28wPIsyjUVA2HUwnIxU0Cy_pP5y1rugShl_7gB-iAYl1nCxAnA54xP5LY2_vuNiBqiJ2kGsZEJLiz_vlka50RGMg_vC9eoti-PAjCArsX_EkoGPOIr919WjtZ7YbBHUAzvhnq9R_zip_pqNCg2s-VHoQMXaR1RvHN1A2MX5bIuDBCxR6DpdBv5aK8cYy6WW6dUOz54GU8QNwWX_d0QZeTegHGc9JWAHmqmbCzjg9O9z0AhgFxM41s6UkGtF_q3KEuEG0-9kGvI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqnqhC2kFRz13RUjyBAMfcTz7UseSwuyfQDq_E5iF51uQLN4hZ3mgtl9Hu-0PlEgzBLrJamMWCBF6IvJzBT0xo16y17brw-62xl-2wOylo-dllrfP0Js844Kr6cvIuZRKaf859bv_fSrGezYzSxrPFhY-hYGf7Impy6hWcT5XU59SbkSatVASxOx7BSr6Qhf7qYZkjZJBcdEeNkiPMNpWtpxkztXKpTNcAJ9jeF-OOM_nEGhbOiRY-odB3K0t6zp9KhEyG-Wjm-Ihcir1lTO4G17isFDTV14YWKFrXd5yAi173usCYaIuPj8La_X4ffw7wM_5ALTOfrrRjQ5g_KYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XhyXJx4Xuvv2wr7f1RLdDdsw5snUdomuTGYzvHl9fDeLv6trNM21-ItI5CLs9M8HzU_NcU3DJ9KnGABx0YUZbJDAEYKzo5YrsZzWQIpLi3y4E4C4rIDN0wFRxbmBaGl_5iNkZ0Sfs1FutVVAeD11il_Cx6VLqrILwMRL0BdMYiqeKV80hBZDqKYvk9o9uOFksSzTPHQ_L2tA4zdr0QPzyjE3Cglq6_VAOmWrnv7oY8dovJ36wO9_89p3oHRtnuU05CUm1eQp1BvgINOTaAn1FBc3QHrEkWsyEK1CuXS5mdb1n1AfFSPEBDBDApa49MTzNaj1AXeUhhFW3epr6ycig3_Q8EYkhwP3JIoOl1OE7XR-1Uyr2A7iUotiBxNQUpjaoARhaInesOvXCBu1ZI5a2iokesmiUittt_cvgFzgw1nAhCJspH4eXLYDYqUTNZY8K7C7PaJOwUFWBmxWQv5Do9crxWu4xFyncrCahTKitRv0X3GNwYYGjygOI4uA9CgFM-9F9jZbIHoqMTkoyFrDhWB4w-0-EGsEN9Vv079Qn36NHcRmbX9pxBEQUuApnHq-dD372c9AEIdJjaiAqwTBkZ6MNY3ZUvFbvzSm_-X7e2-fGVVxeBOESV-mInlTqH80O804u7qXMIkErlWuXeQczRROD3XGThTUGEV-Z8LQtZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XhyXJx4Xuvv2wr7f1RLdDdsw5snUdomuTGYzvHl9fDeLv6trNM21-ItI5CLs9M8HzU_NcU3DJ9KnGABx0YUZbJDAEYKzo5YrsZzWQIpLi3y4E4C4rIDN0wFRxbmBaGl_5iNkZ0Sfs1FutVVAeD11il_Cx6VLqrILwMRL0BdMYiqeKV80hBZDqKYvk9o9uOFksSzTPHQ_L2tA4zdr0QPzyjE3Cglq6_VAOmWrnv7oY8dovJ36wO9_89p3oHRtnuU05CUm1eQp1BvgINOTaAn1FBc3QHrEkWsyEK1CuXS5mdb1n1AfFSPEBDBDApa49MTzNaj1AXeUhhFW3epr6ycig3_Q8EYkhwP3JIoOl1OE7XR-1Uyr2A7iUotiBxNQUpjaoARhaInesOvXCBu1ZI5a2iokesmiUittt_cvgFzgw1nAhCJspH4eXLYDYqUTNZY8K7C7PaJOwUFWBmxWQv5Do9crxWu4xFyncrCahTKitRv0X3GNwYYGjygOI4uA9CgFM-9F9jZbIHoqMTkoyFrDhWB4w-0-EGsEN9Vv079Qn36NHcRmbX9pxBEQUuApnHq-dD372c9AEIdJjaiAqwTBkZ6MNY3ZUvFbvzSm_-X7e2-fGVVxeBOESV-mInlTqH80O804u7qXMIkErlWuXeQczRROD3XGThTUGEV-Z8LQtZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=BHtG6kIBxSFXYk6xJedd2XMgGPsq4o4452iThKedtKTpIyzOIDoWQGfPuDmJ1LwcQEO4oWapFK7L5bQtv0DseUQ1mwdMNRN5tHLGbg7hIHgL9tMvzS6jssJkrAz09OWvf_fX9TOmIGSd1c5RNhG67tfY9Q_VyeG6gYaV-IBSH-C1EFu2DqGJq9KLWM5xFrF4obOLTaC6a4lQzHVxe3C0VCPNHcJqVX-UDzj0qgrmkYlEWbmlUs7JQKRel6YlQMyOu1sUCOMrAp7vY8-8oARPrvasa7mAdUdZfUmJI9zJAzrlc274wd-4MmVp83jsEe0IjE8O_nY_Zq6mt7Oq4WgR5AO-q0Oppe9lPlMK7JV7SJ-9TEuBtOSpFaGIfDZrVCGKyBU24ogwz6-LplgpCijHOvy7H1EGp1Kqll5E8Q9rinrptm-sC6fVxQG4AyHFPjp58EpfBpVXwzMJsNRHAt8c2YNb284ieBE3wbz_KeUVOfeDWH5JPqvRh7oJ3ettSgHiN2GRiS3JbL1Z8PHwqVq0ViTYdb10A0-X-dloGc_LjPouhpgz7jaXJ83etiL4nmqvEZI95mcL-DBY_cnxu8HqKi6sFo1yz-N1o1fv_CYeW5Hws2xed1CXmHnvTYm5SGuIP4Hz7ht9yOGqHo6eFlAAxMydxDWryQj5C3UGwAGmeoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=BHtG6kIBxSFXYk6xJedd2XMgGPsq4o4452iThKedtKTpIyzOIDoWQGfPuDmJ1LwcQEO4oWapFK7L5bQtv0DseUQ1mwdMNRN5tHLGbg7hIHgL9tMvzS6jssJkrAz09OWvf_fX9TOmIGSd1c5RNhG67tfY9Q_VyeG6gYaV-IBSH-C1EFu2DqGJq9KLWM5xFrF4obOLTaC6a4lQzHVxe3C0VCPNHcJqVX-UDzj0qgrmkYlEWbmlUs7JQKRel6YlQMyOu1sUCOMrAp7vY8-8oARPrvasa7mAdUdZfUmJI9zJAzrlc274wd-4MmVp83jsEe0IjE8O_nY_Zq6mt7Oq4WgR5AO-q0Oppe9lPlMK7JV7SJ-9TEuBtOSpFaGIfDZrVCGKyBU24ogwz6-LplgpCijHOvy7H1EGp1Kqll5E8Q9rinrptm-sC6fVxQG4AyHFPjp58EpfBpVXwzMJsNRHAt8c2YNb284ieBE3wbz_KeUVOfeDWH5JPqvRh7oJ3ettSgHiN2GRiS3JbL1Z8PHwqVq0ViTYdb10A0-X-dloGc_LjPouhpgz7jaXJ83etiL4nmqvEZI95mcL-DBY_cnxu8HqKi6sFo1yz-N1o1fv_CYeW5Hws2xed1CXmHnvTYm5SGuIP4Hz7ht9yOGqHo6eFlAAxMydxDWryQj5C3UGwAGmeoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=HwWfyYkCCmN9GW7dczCQR_M-gy1td47iUd4VqTZmzxAJtaIJzXji3YKs3eVbnM5vW45VmmpTblndMN0F4dQvRWR1WwaJGb1-uD-Q1CE7hu1r4-1MUQVJnPGqfWWZlnnJwo5Z6yN8SoMMbA75crE4hp70vL6ojuZmrM9V_ASnZHecm9OEcGlGSIpLE5geBaQHNuzQKmToOi4w-NXdftoFk6LpWAZDZGMi99NNqOaDW8T0EmrNy29K2skJbMaS94vVO6OWO5R7T1Vp4F1e5xJzUXljkyGUJ09g3U3TEwK5pFO6QNZoVkBdiKbcsMNDwB9sKWKvtofR1HAEQYU6ocsNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=HwWfyYkCCmN9GW7dczCQR_M-gy1td47iUd4VqTZmzxAJtaIJzXji3YKs3eVbnM5vW45VmmpTblndMN0F4dQvRWR1WwaJGb1-uD-Q1CE7hu1r4-1MUQVJnPGqfWWZlnnJwo5Z6yN8SoMMbA75crE4hp70vL6ojuZmrM9V_ASnZHecm9OEcGlGSIpLE5geBaQHNuzQKmToOi4w-NXdftoFk6LpWAZDZGMi99NNqOaDW8T0EmrNy29K2skJbMaS94vVO6OWO5R7T1Vp4F1e5xJzUXljkyGUJ09g3U3TEwK5pFO6QNZoVkBdiKbcsMNDwB9sKWKvtofR1HAEQYU6ocsNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=jM06b2XDdbARXYsGJDELto96j67M85oDSdD-PY_1Fo_vuIRR9ttxcTIYqmMsBMI0AlK6Fi3FLMjMuU89dhb5T4js46C3yIhrWvvsnP1aj8_DyWmhl_fYy1I9lPkyDXVr1L5X84LK_S-dbWNRahI0mkeZ0tjyAp-_wxi4n2oFx9f0pWVOMOSuRuphGgur2p5XBDzNASD7Ml7D7IhwvetgqXNgwDzYZC8uw2DjWyRVuCgkdE4udfGM0lyhrLIxmEYYXZkaJ7F4qVSczA8QwTlWZ3ZolwhSdDfEJcqMt-a5I3qdeDFZQSaNjtRjI3Dbk_cFHVI2O-N88oDwywoqbqZstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=jM06b2XDdbARXYsGJDELto96j67M85oDSdD-PY_1Fo_vuIRR9ttxcTIYqmMsBMI0AlK6Fi3FLMjMuU89dhb5T4js46C3yIhrWvvsnP1aj8_DyWmhl_fYy1I9lPkyDXVr1L5X84LK_S-dbWNRahI0mkeZ0tjyAp-_wxi4n2oFx9f0pWVOMOSuRuphGgur2p5XBDzNASD7Ml7D7IhwvetgqXNgwDzYZC8uw2DjWyRVuCgkdE4udfGM0lyhrLIxmEYYXZkaJ7F4qVSczA8QwTlWZ3ZolwhSdDfEJcqMt-a5I3qdeDFZQSaNjtRjI3Dbk_cFHVI2O-N88oDwywoqbqZstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IMKI4m5BRWf6_LUn9OxDoIK31RJCN9larz7SZhmnZ2-6ldJBZUnQ_rOtdWUlsoRV9EEOi8egwdQuXYPhdDKHWooJWUg-2m5OO8R_d3a86UOvhdsoq1cQ1XzUPIpLAeKBhugQJ_sOTM6pwVJP_TGZvzdmPvQTHjEpLgnpltRDcxVPNAVE-RdUENe0XpBIPpDKnDfuCYVmudhgInJU2nz8aO3IYJE3FS-IpkctByN0qAG8Zhr13KLcKggOJu4lfXRJ7SKXcT9iaaBJ63gih7txqTdONT4IuSl-jP9_W5BePNiMfuKY6f-gzkBWxoIiJ6WvLr3fChGZMQvcwDZUooGvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IMKI4m5BRWf6_LUn9OxDoIK31RJCN9larz7SZhmnZ2-6ldJBZUnQ_rOtdWUlsoRV9EEOi8egwdQuXYPhdDKHWooJWUg-2m5OO8R_d3a86UOvhdsoq1cQ1XzUPIpLAeKBhugQJ_sOTM6pwVJP_TGZvzdmPvQTHjEpLgnpltRDcxVPNAVE-RdUENe0XpBIPpDKnDfuCYVmudhgInJU2nz8aO3IYJE3FS-IpkctByN0qAG8Zhr13KLcKggOJu4lfXRJ7SKXcT9iaaBJ63gih7txqTdONT4IuSl-jP9_W5BePNiMfuKY6f-gzkBWxoIiJ6WvLr3fChGZMQvcwDZUooGvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=JAa7N2O9686z77cjlPylm9PcHHMFA9-hpuGTqADVIeG5NEbDOOf8wB2URXk7UPjBjcv48t-O7WmWiNUDhfXeCidMwTq7EOT-AbCCZo_7HJ9kxEeFWZ7HUqPUuZnzjm5FbNKgdpxrYW66OrCRn16_l_UeL38j1004osNBXCH7zaGIPUzkeUsVI4zLTwLDmgAsI5WdLARxN46RhI3P0rGr_7z2ReBw_JuclmPzIh7Yf6pwXkwu0XmC6PICEQ0XF5J4q7S_4hyHgu96FTEuGnKnWUW5Rets891sTW6bE_8llFiXPpNkbpe17MYqAA6-E7QyJZG5iasGe3J4fcOKCoYPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=JAa7N2O9686z77cjlPylm9PcHHMFA9-hpuGTqADVIeG5NEbDOOf8wB2URXk7UPjBjcv48t-O7WmWiNUDhfXeCidMwTq7EOT-AbCCZo_7HJ9kxEeFWZ7HUqPUuZnzjm5FbNKgdpxrYW66OrCRn16_l_UeL38j1004osNBXCH7zaGIPUzkeUsVI4zLTwLDmgAsI5WdLARxN46RhI3P0rGr_7z2ReBw_JuclmPzIh7Yf6pwXkwu0XmC6PICEQ0XF5J4q7S_4hyHgu96FTEuGnKnWUW5Rets891sTW6bE_8llFiXPpNkbpe17MYqAA6-E7QyJZG5iasGe3J4fcOKCoYPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=MPE2PQqq7oFqu-oy2KGG1zSfWFAYQEoyenyibgYXjRqU_LZLDDBczPvKXeI8_lcGXsF7JjI4YB75N2iT8cq95YB95owRCX8TN1CcjOyXg7POeTDhOab8JdvBhZhG-739S0h5uppatV9pHxfKCZjrvt_i6EyJT5evjio9aGf4QGg08ghopKCmpdTWLtb06dSpHUi53ocM3YJR2x2dlpsc3ubfajNIi0o8t2rVUf6AgOmrhzKwxOVdE2StBdenSogGwIlDshdhMOuO2hA2QjNkhzmMLB8FOdXehYxo1cGp3JH32i4k4fN1JpPnu8aO1RVKct_ysSBUSTtpfmB2EIrIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=MPE2PQqq7oFqu-oy2KGG1zSfWFAYQEoyenyibgYXjRqU_LZLDDBczPvKXeI8_lcGXsF7JjI4YB75N2iT8cq95YB95owRCX8TN1CcjOyXg7POeTDhOab8JdvBhZhG-739S0h5uppatV9pHxfKCZjrvt_i6EyJT5evjio9aGf4QGg08ghopKCmpdTWLtb06dSpHUi53ocM3YJR2x2dlpsc3ubfajNIi0o8t2rVUf6AgOmrhzKwxOVdE2StBdenSogGwIlDshdhMOuO2hA2QjNkhzmMLB8FOdXehYxo1cGp3JH32i4k4fN1JpPnu8aO1RVKct_ysSBUSTtpfmB2EIrIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jONNmYvpZKb7QZh4zpThARdFsr_7UI6669hYJ7MXrn5DlK6cWGyGbBjBte9S5I7OjIq27pK3SvS9wjCxS_6QnkgTj3lPmKHHzUYcFDKIO4WlAZMM0taoIzDANvcvGETAtUwdd97yR71M6IIm_WkY6lVtl7Q1QFcGBNUg5C31Ydfhd-1iLgpnk8u3hfH9hPsB6aRinal1ES4nZFH1DvvdZjZm0Va3SKmtAIcWZhQInquXOlqWy6JHqYcuBSlsV7baRJ1OrBRul2QS3eFm_Q36DMxj0ciW2ORvtxVfBcwv-nazgmJddJ3HD3i2YnplxWZ1v6CgIfDsRGwx9jYtZ_oYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jONNmYvpZKb7QZh4zpThARdFsr_7UI6669hYJ7MXrn5DlK6cWGyGbBjBte9S5I7OjIq27pK3SvS9wjCxS_6QnkgTj3lPmKHHzUYcFDKIO4WlAZMM0taoIzDANvcvGETAtUwdd97yR71M6IIm_WkY6lVtl7Q1QFcGBNUg5C31Ydfhd-1iLgpnk8u3hfH9hPsB6aRinal1ES4nZFH1DvvdZjZm0Va3SKmtAIcWZhQInquXOlqWy6JHqYcuBSlsV7baRJ1OrBRul2QS3eFm_Q36DMxj0ciW2ORvtxVfBcwv-nazgmJddJ3HD3i2YnplxWZ1v6CgIfDsRGwx9jYtZ_oYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=OJlzaiopE2dUub3ADOL_HAWKHOpVUepYBo0noy7W1yNCbNSEJOC9X6h6krSYxQAlee0P4JNkdMkUuC51_caUfkQDA9JZfqz7CbIYcbuad6f-a82mKFCxj-eE1W8K5bvWh4CtpfMVvxUZcCtwwDqF-YsryGxsBdWIRpT3rKvGYy5t14rRBYbunP99uIYHCEXmTjttBX8s5t1iVoq4Fkcpbhig3NCJ9MWmFt1ujpMypQtw4es-60lFSwnp-fdnh3lF6HnAeQ5mrEacz7o0USLXTRdtUa1bwvk0ygdP8Ac1DB-ULyqLLIbNRfRQHUhqBljBKfuPDR-G6GSJHUygy1EJSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=OJlzaiopE2dUub3ADOL_HAWKHOpVUepYBo0noy7W1yNCbNSEJOC9X6h6krSYxQAlee0P4JNkdMkUuC51_caUfkQDA9JZfqz7CbIYcbuad6f-a82mKFCxj-eE1W8K5bvWh4CtpfMVvxUZcCtwwDqF-YsryGxsBdWIRpT3rKvGYy5t14rRBYbunP99uIYHCEXmTjttBX8s5t1iVoq4Fkcpbhig3NCJ9MWmFt1ujpMypQtw4es-60lFSwnp-fdnh3lF6HnAeQ5mrEacz7o0USLXTRdtUa1bwvk0ygdP8Ac1DB-ULyqLLIbNRfRQHUhqBljBKfuPDR-G6GSJHUygy1EJSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJtSYYXBURU1tkhNWFruisNz9qeyKrtZjTBe4cb44mzeOyQXolQWJTe4As5tCKnVQyeCOiaj76kMd2sUUGM5wIyETzN5ApjPHOzbRr-UwvQ3lBXMYmFWP7RUUVDGi_w4bNwfBH6PMHgmfTWzHMTedJjWCSSEDF62-hYiJWn6MRuAUGToT7GHxpj_JIsowhaOoHBEzvZ1NbjBiauc-59Tr4rbWkeoEU6ShkcQOaFh7yiQqzhv5X4n68FP8D4uEYWalsDq6XXEz9t8JCqPfTFkVEHJRvLrug-ECs5KdZWa053l-sdFadLyitBm4vmkiRkvqUSuRQedysvDcLjR2BTMTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=VLl0BiJ4uT1MKw_9UQkaWON4kpdtAbiusHxCQI3qRRomabW0eq0xhm7LREYtm9g0G-zycKd9_zO-y3hMwnvbTNEVN5PrEp_6cOlPDMri7otqMune2FSdKr3GSiWLveteebdrSSeOTf63TyX9bpt_Hk5rdR3TEsZCU-FbV6hv7nCJiOt6fTs7pUe7IqhqbsR51aEW1qbnGKfmcvSQaBUUApJ1Kj-mv0Tk2-u1xN80NgmE7Qi0PgG652oNFYC1K9iNhjSJ9XxZ3YkrqMrEnUqd2bumDapBGIFdqsTdiBaZRwIC5DFtxLLHf_fACbd2KyqHl3xgLAQXRDL5yt3myOKeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=VLl0BiJ4uT1MKw_9UQkaWON4kpdtAbiusHxCQI3qRRomabW0eq0xhm7LREYtm9g0G-zycKd9_zO-y3hMwnvbTNEVN5PrEp_6cOlPDMri7otqMune2FSdKr3GSiWLveteebdrSSeOTf63TyX9bpt_Hk5rdR3TEsZCU-FbV6hv7nCJiOt6fTs7pUe7IqhqbsR51aEW1qbnGKfmcvSQaBUUApJ1Kj-mv0Tk2-u1xN80NgmE7Qi0PgG652oNFYC1K9iNhjSJ9XxZ3YkrqMrEnUqd2bumDapBGIFdqsTdiBaZRwIC5DFtxLLHf_fACbd2KyqHl3xgLAQXRDL5yt3myOKeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XbwbaCrT7RvdPyHZaM_BFbnETYDu2UJEZgve2rMaFYdx5Rn34uO3wIPEeYoGEExrX_u8vB4QHD2sBas5A5ncIeW4fhuL5BgD1Qt2m1I8yCZ_uyN-3UQ8a7h6CKDts18vNM3BPYyGd7VIrfbLMOAlfLOIxejgBFAVh_W39bd7rANxJU9bBvgSR19-O_A5IbKHrzdniZPUMc8CpZyym30E9h9wgqwSl2q8BN9avPygEWNSj9m8rgbihNjl1xwXzrsFTbCZYdR1QEAdniSLppNEX3IeYk4y0dJ8n64gl3Tri1-u2H2EBHjV231ne7AvfGdKzi73dNesFVRQJbjTIWtDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XbwbaCrT7RvdPyHZaM_BFbnETYDu2UJEZgve2rMaFYdx5Rn34uO3wIPEeYoGEExrX_u8vB4QHD2sBas5A5ncIeW4fhuL5BgD1Qt2m1I8yCZ_uyN-3UQ8a7h6CKDts18vNM3BPYyGd7VIrfbLMOAlfLOIxejgBFAVh_W39bd7rANxJU9bBvgSR19-O_A5IbKHrzdniZPUMc8CpZyym30E9h9wgqwSl2q8BN9avPygEWNSj9m8rgbihNjl1xwXzrsFTbCZYdR1QEAdniSLppNEX3IeYk4y0dJ8n64gl3Tri1-u2H2EBHjV231ne7AvfGdKzi73dNesFVRQJbjTIWtDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=k5KRnRTFhg_BSOslSdHIimoM5ZtpSWgosxhDUDDGYj0_Y-AJxZuf5Db1KK7FYOE_o10S5jPpMkNoUkfOP0WXJE_9zoqwNhGbrZEITunL7beFsHyoXzbjkwdkGxBEx9IMHNvUXkfgI39NyA7rrMRc-V8an3rIPkknwkoJx5XeLH2SSLP3rd7QTEJvcmkokcixk8vm1Rr58Wpw8GLbIf4MyOpbVP3vaufpSLlbEpjfqdKdpjhf6XRjRnED5NnAlef1Gnn3YHO2mMUtxlor3HAqWO8dtIh-vVnBt7uv2b3dx7LuBF0flEqmuPvIhU_NaMJAjUOhve1a86qDWqCRfCUGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=k5KRnRTFhg_BSOslSdHIimoM5ZtpSWgosxhDUDDGYj0_Y-AJxZuf5Db1KK7FYOE_o10S5jPpMkNoUkfOP0WXJE_9zoqwNhGbrZEITunL7beFsHyoXzbjkwdkGxBEx9IMHNvUXkfgI39NyA7rrMRc-V8an3rIPkknwkoJx5XeLH2SSLP3rd7QTEJvcmkokcixk8vm1Rr58Wpw8GLbIf4MyOpbVP3vaufpSLlbEpjfqdKdpjhf6XRjRnED5NnAlef1Gnn3YHO2mMUtxlor3HAqWO8dtIh-vVnBt7uv2b3dx7LuBF0flEqmuPvIhU_NaMJAjUOhve1a86qDWqCRfCUGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Dj6Nf4X1PIWuHLITWB4DzW3ZOupd5ShQBSfQuw0GLbToBLCxa_N495sjWLiLt9O40lNZV1uRDElKWYK6zzRfY1L30ZDNfD-TFerLxJuNg2TvVccZZysBJwBlMAHb1IrcQAZ6nCooyES9qbsOJWSQQ1UZQH7ONv20Sa1NvbgcmUJYp9sC6xGywOiatfqZS5D_cFKCYDLYJnqrtCjj6th0GQnYV_e0mUzwxlmX7afHRNu0C9vBdlXr7FSYOtopD5UAN98gcLZRc_K3EEavjWH_cCvEzTRzN8VWMmlKGvV83tCiAbazQCN7NTdfkf6-poDT0Ch3xyD_vFTH5z9KhIrL0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Dj6Nf4X1PIWuHLITWB4DzW3ZOupd5ShQBSfQuw0GLbToBLCxa_N495sjWLiLt9O40lNZV1uRDElKWYK6zzRfY1L30ZDNfD-TFerLxJuNg2TvVccZZysBJwBlMAHb1IrcQAZ6nCooyES9qbsOJWSQQ1UZQH7ONv20Sa1NvbgcmUJYp9sC6xGywOiatfqZS5D_cFKCYDLYJnqrtCjj6th0GQnYV_e0mUzwxlmX7afHRNu0C9vBdlXr7FSYOtopD5UAN98gcLZRc_K3EEavjWH_cCvEzTRzN8VWMmlKGvV83tCiAbazQCN7NTdfkf6-poDT0Ch3xyD_vFTH5z9KhIrL0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD8omUb3uun9YMrmAzvZ8tt0TvI9f3bcNXFht9DjBEhvxkbIo4JisSZAVnrt27vAJ9SH9fe0jCMl4Cp9by52mgWv7OrTlQXge0ty_Us9YsowG0-Uhg6USEpG3VAxSOx-YWlZUEqxswcyWVjPW72c8EfzWvACRdaKExs0sT2ejxONkemzmhdKAnJfqIqYrMXrhnW9vhIoVYvLb9Q3ZmgAYjfkkf5T5cKznVCfM79-Ou57lugoECze4BidTB6_3UwjwmuSeYBXrh1HOoN38PFeORPQWGOAq5peYpuOxlM42DGYZAMOmfRUCx6_cjSNjSqISS8NrYdHZ1cxtzSj-R0iFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=iROMTLO_0ahdfvnRNuyqPWQV0keiRMJn2EUTE0_S_ocmzN4ibYEwLKOJ0Fp9paHYMOqURxlt4A85FRBRyit25rBD1WvKMlk_fJDxqnvEOUWjfU7kp3iYuO1InUas-_etQ9mEwR_UEci0qUlRZqWPEESYZmeeLAVvqwnD6R_mPi0M5YJCxcU-paAE1bKnOmfv09v7_nUl8gMvCKX7o1SJo4giFjJ6zRRq6fulMCs7diMWEseR6aZWnqBMnV3GfsPG_TP-U1dPvE1_9ac4gPUAZUuNALPzC9Xq5RaHqW-pmX31TIi9_fY-059mKQ4jyqba3TUPC7802awd8KhD9_1KPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=iROMTLO_0ahdfvnRNuyqPWQV0keiRMJn2EUTE0_S_ocmzN4ibYEwLKOJ0Fp9paHYMOqURxlt4A85FRBRyit25rBD1WvKMlk_fJDxqnvEOUWjfU7kp3iYuO1InUas-_etQ9mEwR_UEci0qUlRZqWPEESYZmeeLAVvqwnD6R_mPi0M5YJCxcU-paAE1bKnOmfv09v7_nUl8gMvCKX7o1SJo4giFjJ6zRRq6fulMCs7diMWEseR6aZWnqBMnV3GfsPG_TP-U1dPvE1_9ac4gPUAZUuNALPzC9Xq5RaHqW-pmX31TIi9_fY-059mKQ4jyqba3TUPC7802awd8KhD9_1KPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=M7JCPcx6AEyjzXETbOdZ5KgE3uM9Z7tOAVJ9dZfb3pxAsedS_smrB2577H-9qBuOkWonm26A_j4Cp-4HXurZ4aM3McenNBjtgR7f6N3E6ulgohijvhio-x6Js9ggAiI0y9yaRmbLb1vPZNENG7WJWCsuRia0V8R0x46OgEvBr5jah7zOcuPwYrOajUINqHRvGM5-bUPQNmjNIOIP3Aqf5Kr9Oe6FL5B5lo2ltnQ5KxU_YuHaGlM-xyTX9LXhZcCYRxZwDBBXepnGDIrBge5hCZBprQjrvpI17zoiA2mg1EWhxmJzjHKNLK5n379wDOSxlgJ75nwXkcCg1QcXUrTeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=M7JCPcx6AEyjzXETbOdZ5KgE3uM9Z7tOAVJ9dZfb3pxAsedS_smrB2577H-9qBuOkWonm26A_j4Cp-4HXurZ4aM3McenNBjtgR7f6N3E6ulgohijvhio-x6Js9ggAiI0y9yaRmbLb1vPZNENG7WJWCsuRia0V8R0x46OgEvBr5jah7zOcuPwYrOajUINqHRvGM5-bUPQNmjNIOIP3Aqf5Kr9Oe6FL5B5lo2ltnQ5KxU_YuHaGlM-xyTX9LXhZcCYRxZwDBBXepnGDIrBge5hCZBprQjrvpI17zoiA2mg1EWhxmJzjHKNLK5n379wDOSxlgJ75nwXkcCg1QcXUrTeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmygAcTE6Sc6fGxyA_nHf0SsYOjyAfR8i5MZl-AfTaownzAxjCiCZKGYoRW8Y2PmINXNml5NfU95uqyAjIuuTivveAYhMZBhmP9vrKTMdawEsZIcLj31IBbosUswvl7nkt6FGKVd7sgMcdo0NG8UvhBPw4sdOdUCzEGKpf2oR4eysSjYkEBMa9VhTFySvvmueyqnBZ3a455H7-mINZ0COKEchKZrdiFOocoxdfncT2yCwSzouceG5Ybv2Hm5MgtJm6vUiD_kif4cBPXBuMUKKwbCv0-w7Zex8kysGtBw8JUi-2aNMLzUjJ52HJ_bf_pzI3RACMSuBYmjczrH1_4A6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BimPzxJ5oY4oRQJUA03Z1lPzdtOQKtGzdf4EKz07i-XW4-bYEAtjwyS2EqjL0br6dX6XELiTqliIGm7iALn2t29VxJoU48iAZ0AJi5caDYoaMRI1-K5Xx8e7m67OeI8V6-KSdgVrLWRctcWV1t9hun6Yfdu52Ek0x8I_yBX3Wr7GAw2m9ThvcGfr47KOqq97IlvV6anN8NpvW8HVcLBn8rdyWB_kA86T3EBQKp4nr87Ba9-CMM4NDuiZ3YTbACThFfbFM8tamX_69gztrjXmsvVpwTyCdKB52FCsc5hnCY8JhADfqeN-dIXrTEh2sWIbBLuTfhBgcUBVEMB35ShLdw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=gSdAssoMO7UGFnGSfKDavmfZktHT0otVxgKid9DjaWlj-lH9X54fAcNsyzBuZWB_psDjcBqvlvqFF1Cx8bf_KitRGdZ794T_Ui_hbfg7H7oe_Zi6mlqloyML0_qNkZdth44UIgQjnmpikP4nQDqkFqil9Wv1ndus6IBhSOPCCOa3jNBdfwcjZz9NHhd-rqhQl6Q-TQL3I5qnSL4VvS-S0YVLNgSOBN_nZRmBE0liPYrL2douK8DMQrltIfoL_lGcb1_q8Syct3O81N9If67hOXHJiUq0XuMM2fcUoYWZvERdWG0uLfSBmUQsK-kKBsNqB899lRFIzsEKkQZucof6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=gSdAssoMO7UGFnGSfKDavmfZktHT0otVxgKid9DjaWlj-lH9X54fAcNsyzBuZWB_psDjcBqvlvqFF1Cx8bf_KitRGdZ794T_Ui_hbfg7H7oe_Zi6mlqloyML0_qNkZdth44UIgQjnmpikP4nQDqkFqil9Wv1ndus6IBhSOPCCOa3jNBdfwcjZz9NHhd-rqhQl6Q-TQL3I5qnSL4VvS-S0YVLNgSOBN_nZRmBE0liPYrL2douK8DMQrltIfoL_lGcb1_q8Syct3O81N9If67hOXHJiUq0XuMM2fcUoYWZvERdWG0uLfSBmUQsK-kKBsNqB899lRFIzsEKkQZucof6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcBcTX2q5Js0ShSVFHsu16FSFKfewAkxxDSVsLHxD8fa7LCRImufMlkQv4MfUJI3YKw5mx-PFRmpsJ7_6trw5x0nX698UQaaECgr7rofZMhspBapVvcn37TY0Se2UPeM9u-kRlDAusaKf08DSBXp16TIyFBrksQ5UhvqSGHL8WJzpStstkSn3NiKbPxo6W6SgahIiLIxjiA_nXlIKV3d7Eh0sbcHuy5IeDbQYAClX-K2fV-Ps754XPgJ7EXD6RBVw8x6j41wnosn54entzsMj1Cwnalp6AX7eOEW2HZOIW6ziz2HSEYzJ5rbsQYPhKga54osf4lCPad-38Hnv84RLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzx0vCllGmRZK0IPnCG2hqCXxOVBoLqL3yPQghysJVElCy0EbDyz6TVbEtup1hWHV90yf5uEsTDVcJg-pyt2tVLrHMQPnNiWMUfyzM6Z_6_YO7TZx0emj8-P5AzB1tNFLSZrhcxbptmsGXHPfTnqc7BXAux97WnrN18SuM5bGDixPgUXLarO-UzsG6t2XvSvy1bysYANy0DDjAtckT1oQNjtfOk2rxn_E94dG6SIqJufLlapYI2G4pDkISq8o8ewhhB7d9gpA2pu5k8JkIQJ3NhfxnCUJMukVQxGy8VB6eUzYR5WUTFpAUPl8HvNlhfsr3wWIuSHHhbE3fu29_VmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4Zt9uNgnY13kEVcFbE01K-szSqI47VldDn8MU4BE6Y6nPCGRbV6RiEIHAUpbytX9dTCQ-3vs6bfzMVjRaL37ZcHPaj73hW8mPDL3dNWC6NJlsW0U6_mmPXVsgS_k3VeabqXsSxXpeMAUQXMWIcMiYy1xXO7YCVHilYaN3q_EraiKtg5Y0J9WwVEWjOoXv71qDDTS0K7nO0foWIarwe_6KOdtSp95db9Ev7-I6TVpbLJL9mqLs-BeN1FtZ_ezCxC3xxWfUoe7Q3YmkgJIDKZaKLYEAMYpFKALy1_nY2hPrKMguwafkMD9utXXl4Q7pDCyFo1m89vx4l-4-JiViNHIw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=jZr0oTqbKy5Cy6x6OiRVeHb5gWuP7M7uqEEe9im741Hk6O0FXCR4VusuJ1k6sIomUQFqsWCvOBoTZFW9P-aFRLXev_gbZYoLiZSKFfyYswwuUASq_8xQyMAcuHg_C092A-VXRrc0LAm55-o7XtuU9GiCQn5DwOwGv0GNjVjpWN3gZtddDbzrw0NCWZ2gb21iMy5eHO7_1hSAmULwLErb8aQmVkHSaAyF9vfh9wELn45Iv1pTrEXO8NNfkRHam9u5O_ulMNkmDG01_5JSTBpkKqOzkbXyqw6EDzIup__EPoD1hYpx2AHrdgcZXkUmQupA2_oNRWbeEOVETgSqmCIlvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=jZr0oTqbKy5Cy6x6OiRVeHb5gWuP7M7uqEEe9im741Hk6O0FXCR4VusuJ1k6sIomUQFqsWCvOBoTZFW9P-aFRLXev_gbZYoLiZSKFfyYswwuUASq_8xQyMAcuHg_C092A-VXRrc0LAm55-o7XtuU9GiCQn5DwOwGv0GNjVjpWN3gZtddDbzrw0NCWZ2gb21iMy5eHO7_1hSAmULwLErb8aQmVkHSaAyF9vfh9wELn45Iv1pTrEXO8NNfkRHam9u5O_ulMNkmDG01_5JSTBpkKqOzkbXyqw6EDzIup__EPoD1hYpx2AHrdgcZXkUmQupA2_oNRWbeEOVETgSqmCIlvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TdfmiX9usBHHA51xenygAnaLM44MI8rCp7Nt1vS5JhZPPaF25SnIv88efflLmKxHMfRaeN41_eRaHA7LnZyRy8R78qZ_NZSKQIoCPOsRM8lCo98wNcOk0QjranCRqCWfkaiIqDE3OgHiKBHlIyrFuIJuc9669PwZdT-nMRaLNFYyKywh7ZxeB4oNNOr7U8XEefHy-IMPyUlQvz_MYRBa3NuHBcwRlaBLzHX9I8ZJiVZ9fr_OvA1HyuyS35HmiVEijZ9xKSFxbD0VGVyiqK_EOxLc2ZuoLGGCc2Qdx8Hhk5Z_2USEXw0dP1EvsZB-13n3g2-M2GCJXKqnazHbQzbaHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TdfmiX9usBHHA51xenygAnaLM44MI8rCp7Nt1vS5JhZPPaF25SnIv88efflLmKxHMfRaeN41_eRaHA7LnZyRy8R78qZ_NZSKQIoCPOsRM8lCo98wNcOk0QjranCRqCWfkaiIqDE3OgHiKBHlIyrFuIJuc9669PwZdT-nMRaLNFYyKywh7ZxeB4oNNOr7U8XEefHy-IMPyUlQvz_MYRBa3NuHBcwRlaBLzHX9I8ZJiVZ9fr_OvA1HyuyS35HmiVEijZ9xKSFxbD0VGVyiqK_EOxLc2ZuoLGGCc2Qdx8Hhk5Z_2USEXw0dP1EvsZB-13n3g2-M2GCJXKqnazHbQzbaHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=AlLoRU-nkpSNdd5y_B7SRdD4ZcCTWomOKiOWPP67unxTPVl3zCNalj2X5D7Y1wj0c6Gjy1HVMHU_x4HLh1ZpBVG4W2rCYQgszM8TVZ5gLlRtpalpmGgOrLHpTmLEHzrz_6D47K4Q-pkaS2u8dxmsGozDIvGNF-c0HtF0l1aMcahkmjs6JE362Azu9SsCj2ai-A8o6iNmoL8pImc2QphtzW0AK4H9e4_08P2KY4TxvhZ-5VEbpy4ABz-uUx5PpalwD5gnTINFMt_1HNgqGNh4Dais-d-drXcf33jCOvESRw4JA1Fcs7uMPAW3I0TblcS-7RcQrlWJw7gWVcEW8qIBSA034xtB3kUVN1XqFHRcD3EL_CiLumbCyzctpbZkSvPOU2xD-H2D-CcftuzD7RFDprloMv2pIlR25gbDDoeZPrRfHL4fNLsPGrhrdKLlrlevRlCiP1BzBSuDMRoFObpZe87xrzbcdBwN3Xto6lrjdD6s9OFgTL6j8ZRClsugvvdAEKajDk20DQJzapcPGJjjHtWAoUM3EE-O0opl7QApEJhPw_S0W0SAsbzg4h-D12mNVY2OaTwnnorCygA-ezFZut4renPM5dxKJTcIhQF84wtYgFUkW0UxZVjSRmDzkyRfcRcPuSB3dYmnV4wS-0MgfiXk2SE8OOTuSWgE-TS7GwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=AlLoRU-nkpSNdd5y_B7SRdD4ZcCTWomOKiOWPP67unxTPVl3zCNalj2X5D7Y1wj0c6Gjy1HVMHU_x4HLh1ZpBVG4W2rCYQgszM8TVZ5gLlRtpalpmGgOrLHpTmLEHzrz_6D47K4Q-pkaS2u8dxmsGozDIvGNF-c0HtF0l1aMcahkmjs6JE362Azu9SsCj2ai-A8o6iNmoL8pImc2QphtzW0AK4H9e4_08P2KY4TxvhZ-5VEbpy4ABz-uUx5PpalwD5gnTINFMt_1HNgqGNh4Dais-d-drXcf33jCOvESRw4JA1Fcs7uMPAW3I0TblcS-7RcQrlWJw7gWVcEW8qIBSA034xtB3kUVN1XqFHRcD3EL_CiLumbCyzctpbZkSvPOU2xD-H2D-CcftuzD7RFDprloMv2pIlR25gbDDoeZPrRfHL4fNLsPGrhrdKLlrlevRlCiP1BzBSuDMRoFObpZe87xrzbcdBwN3Xto6lrjdD6s9OFgTL6j8ZRClsugvvdAEKajDk20DQJzapcPGJjjHtWAoUM3EE-O0opl7QApEJhPw_S0W0SAsbzg4h-D12mNVY2OaTwnnorCygA-ezFZut4renPM5dxKJTcIhQF84wtYgFUkW0UxZVjSRmDzkyRfcRcPuSB3dYmnV4wS-0MgfiXk2SE8OOTuSWgE-TS7GwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=X5ZCYqUXk358sBA7-u5pP3PYVJWdpN_-buDI1-XOvrPlYx-xJdgxsgIvSa-8g6Bhmx8y91oa68grbAWjypRnFd3AOgI0NM9z1laBITioRNjhH7HM0iZq8-Vq2iXkkcatoYl8r1DBmepZIE3n16KTOx_WIaBTftD5t8tVvW5gkTv_4GsT4wz-y95Fy6Xhhp7XDpqAj-y-2ITYkSwyTtFIWSM9K9OvkUKK7u1Cx95Q5dncJ_1W43Da9Jl-PGTSYiUlGhfQoEfKEkwxvL9B2rROXpcaazcWMpjIM3aFCflCCVy2fzMo9wOnehRu8Cq7lZXXOguBsClnQDJpHBrwb7VdABBQqqrNVmxRPDLRmR3WAAiLLpMZTo7PXNQ3pbDxRbAs0pl5-c1zGHHGfHPNiCua8Iq0Fl6-IiSbRf3zN-WUAppfkCG5s1I0kR5j7mI-VDjAVV920u4YKDEMe7reNF5Kls4cZ4soT9BGXsVhZ11ux8fBtyJPROmWwJxPnQ1l_whvJECmvl63vC29clbFwTjuGJKerqMMGafDfw4Jl8tTv_77-5wJo6fqmluOTdta_ZVElDZCpYJwz3TsmyTtsu-IuDXt95k2R1rLMKy3f8ji_tDty714IKoO9Zc3_mBv2f1svcApFXwRP6lLtNOPaHJlhjF2K8J2xEgLQ58nWwIJgO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=X5ZCYqUXk358sBA7-u5pP3PYVJWdpN_-buDI1-XOvrPlYx-xJdgxsgIvSa-8g6Bhmx8y91oa68grbAWjypRnFd3AOgI0NM9z1laBITioRNjhH7HM0iZq8-Vq2iXkkcatoYl8r1DBmepZIE3n16KTOx_WIaBTftD5t8tVvW5gkTv_4GsT4wz-y95Fy6Xhhp7XDpqAj-y-2ITYkSwyTtFIWSM9K9OvkUKK7u1Cx95Q5dncJ_1W43Da9Jl-PGTSYiUlGhfQoEfKEkwxvL9B2rROXpcaazcWMpjIM3aFCflCCVy2fzMo9wOnehRu8Cq7lZXXOguBsClnQDJpHBrwb7VdABBQqqrNVmxRPDLRmR3WAAiLLpMZTo7PXNQ3pbDxRbAs0pl5-c1zGHHGfHPNiCua8Iq0Fl6-IiSbRf3zN-WUAppfkCG5s1I0kR5j7mI-VDjAVV920u4YKDEMe7reNF5Kls4cZ4soT9BGXsVhZ11ux8fBtyJPROmWwJxPnQ1l_whvJECmvl63vC29clbFwTjuGJKerqMMGafDfw4Jl8tTv_77-5wJo6fqmluOTdta_ZVElDZCpYJwz3TsmyTtsu-IuDXt95k2R1rLMKy3f8ji_tDty714IKoO9Zc3_mBv2f1svcApFXwRP6lLtNOPaHJlhjF2K8J2xEgLQ58nWwIJgO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ewmqnusXAyGEixd8_cadfH5-wd26J4H7Z8MdlrRc0GT_03oiawq3eP6Gyhu4ZkvrqLZPvzmQwM9_2Caw-k4XS8jFH_9ayvifg_YqTE9S7Mk3fTVcDSWk33R2x-6M5jWri689YE4bqQRG0QI-Yg_N7O8y-ZPm35jURm9vAWXujPicL9k8AAAJEBVm0dJGQEKu7yivwEser4EVKXME6wY1Rk4mZ_GBqxGLLhS3BHl-eB03yCdSBbaLMNi6TXcprdW3uZTwdxmRrUjj0_UpdRQ-g330aSUjWIbmnpc-veExOHbtBHTHVopqFnZPMtetUA-EaHy4IEa173B4faZg4pTX2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ewmqnusXAyGEixd8_cadfH5-wd26J4H7Z8MdlrRc0GT_03oiawq3eP6Gyhu4ZkvrqLZPvzmQwM9_2Caw-k4XS8jFH_9ayvifg_YqTE9S7Mk3fTVcDSWk33R2x-6M5jWri689YE4bqQRG0QI-Yg_N7O8y-ZPm35jURm9vAWXujPicL9k8AAAJEBVm0dJGQEKu7yivwEser4EVKXME6wY1Rk4mZ_GBqxGLLhS3BHl-eB03yCdSBbaLMNi6TXcprdW3uZTwdxmRrUjj0_UpdRQ-g330aSUjWIbmnpc-veExOHbtBHTHVopqFnZPMtetUA-EaHy4IEa173B4faZg4pTX2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scv6UcSRB205vSgm-2wbyNlx46_HUzOw32IxNr0roQTmkEACG8RR0Mbm34eqIWGRe_E_nknreIPXyt4zgaKXveAWqc__tyT2FaOreSlz5I32JN7i3dD2HFdiWya1tjg4yyaJ9VOp8O5bx5o62yB6PjwHAy8xG0Q3JNZp1CqNl79bBvzJYk55DEZ-htfZt-0mQu-IU7RLNJ1maajlpS_xD6YHCEwpPTG64WaNRQD9Q8oy3zJkD9k9PF3SIj28wS-gFGEoAZ6q-kDOs14uvd56zgWAaYuuYMSTG92puoumsyExSd6jZWyb5nigdhAzYYQeqnfiGsaMQkjWbley-qqfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=gqBHR7st81R92sFlx6Jt1qjpoHyeMl2uux9TNnCgZR86X5uCjFvHMZ_rJI00ck9p7G-9ULHUGys4Vx7NpezsXWhyMnus1q5OFzO3LdqMjFPdye73eR7yw091ay86OaFUvHRBTCoH39C656wCTWC0tsP-1yliyi2u0tT30fILwkZgxzYn9NVkMZEkwIwHZsIEFQHwnlp3BjM6_Hze8LQ-cvA40mUXoAYEzsI69ru1hQ5i6Hj4MquZIWbAarK_NlHQWDGvYPhTYqpuY5DJRrZGU2dlo4fcYNrp_kt82J6kFgDSxQTWtk0z3dO4diaU3mtjBTCEOSxEfpkXuIT2r2lhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=gqBHR7st81R92sFlx6Jt1qjpoHyeMl2uux9TNnCgZR86X5uCjFvHMZ_rJI00ck9p7G-9ULHUGys4Vx7NpezsXWhyMnus1q5OFzO3LdqMjFPdye73eR7yw091ay86OaFUvHRBTCoH39C656wCTWC0tsP-1yliyi2u0tT30fILwkZgxzYn9NVkMZEkwIwHZsIEFQHwnlp3BjM6_Hze8LQ-cvA40mUXoAYEzsI69ru1hQ5i6Hj4MquZIWbAarK_NlHQWDGvYPhTYqpuY5DJRrZGU2dlo4fcYNrp_kt82J6kFgDSxQTWtk0z3dO4diaU3mtjBTCEOSxEfpkXuIT2r2lhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=UnpMb_sq8nQ0r5g8Vsch06nTqGCd68bSj9hiOXw6oJHtulN294jIpsY-pyp79_tLy2EClG_mp940vCbp1zuYUheM2WYaqkYCecbR4UtsbTjQTXELbodkf7s5eUm6uYyRc_EjJIRwM85g8xwjaBnMT5dQruk0zBWtaqYfF5lOV0Z_75s4ZPDJCkBiwB6RqAS3Emo_sblD2pUvSzkXMibZGzAsZNBtzpy5jmSGPLBVg0Fza4UMngcGX3qbCJwAFj99WcClTWqV0NpN3I_cdXEqc24LCu9NX7qO8HIrgcHB_NbSNEEahdx2NcXqKSA-0rnzl3IFylu3tG49vLZU4Oyx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=UnpMb_sq8nQ0r5g8Vsch06nTqGCd68bSj9hiOXw6oJHtulN294jIpsY-pyp79_tLy2EClG_mp940vCbp1zuYUheM2WYaqkYCecbR4UtsbTjQTXELbodkf7s5eUm6uYyRc_EjJIRwM85g8xwjaBnMT5dQruk0zBWtaqYfF5lOV0Z_75s4ZPDJCkBiwB6RqAS3Emo_sblD2pUvSzkXMibZGzAsZNBtzpy5jmSGPLBVg0Fza4UMngcGX3qbCJwAFj99WcClTWqV0NpN3I_cdXEqc24LCu9NX7qO8HIrgcHB_NbSNEEahdx2NcXqKSA-0rnzl3IFylu3tG49vLZU4Oyx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLNayHit8b6xYUQ8nuyEr8_8t2Irk3bLpTAEh08ze5n0eG1rI1E271iY9dg9kuCCJIa4pwzsYhCnmYu_VL2seUDoHMQJH816evN9Y4fV4QdmYvGwS2hKVEW3D701V53vKAMlhj2vEIg5wwXMSYSDxyCO5yuYI6h70UkF92zruZt_KGCEYiaZKxEi0Z01HJSzAqVHnPopFIAuOL1wGggjJ2jhpODDQLLfmromdZwBQxxvJ5PtCfndA7IgXlyuK6KkhzoatJgT_L9biWuAyPuQj-9sHwjJGns7vtJm8OvlG3H2rFplQvPIKCUBMTI46WDVsG9sVBafhGh-BCDOXsBbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIsBtDwHqqAkpog4pqOkfqDt_5kFz2IxZnTxdvQfrS-ypy0RawSasJEkUxOKtjV2xsqgltkAV7NW8AHSx_Kqim92DP4ollhD_SoUBxMqYEOnP7U2lX6_Syf08ICaA99-DZcc3ctMmrYSNfyrv_ai5cZqLvVpO5rnsRg-iihNg3e8LLziJfKlaZfHAtcFk1nm9rvVorXiLxBvmpwmmi9IgmAdK8Nu-WIcVzGYIMqtMvoqB5grQvetww-oPFw6LgDc32y8WmKIKgRkMzleeIEpY7YnysEpV-Yup2G8XrP6VXP_WlFNyu_QXbcOosLvTlZdHc30Tzy73MIdjVmbrjmSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPFnHO16js1YdlTqqg_nOE2aTE4K_lPeYnJJZigrH0TRGhrXF5y1WviAwj8jTatnPCaRuO01YMSMTIWyLdCHuyw9pMeVVH0aU6xfpVc3zC1RTKZJmr0aoeVmDThSSbOmNeVj8mQnPXmKQYNjVHkJeD5UVTNVDMozMJjXgaYD_U0ibTzy2eNYN0IysH1WEadHBNOP05LI1q5hR1urszLvThix6fqLDuzx7XGs13LT602aEJug2p_LeYvmdu3ruZUjKmMKRR7bxRTSgVYbGYFd42PMltrVj3Eug3crPDZfU2mbn90gVAGGcSwXmNBY5x1RjoNRzMF6-dji3w43EHdBDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl9PIYdWFaMvJ69u-1NiIdQ8KgqN9OAohc7HWKa2fXKtik66FxN6eOiyIokyv8JNrTdij6ivmszhDMsPRkIg-I2xKrgYjwgYUDb0UKKGaZ36oiQ8vO1C698ILMpQxA13LX5OaOaPqPOUbHwjngzg6YLWdBabyNxa5Sh4o8dmGWUckTTVHcr6bN0sIuFiZucJ8PO7NM6yST5vgcYdPZF90wWarK9LgzPI43kJ7--3sfCCGtARUhAAWPfAR3QnyV2dlpb7hFIFnszm_UIueUExwkwiA5I_2sqEoxQjbfkKccn2VDBjGNgVHPzv8Z96lGKOLMTqFEf2A4NgEIBuTEI5uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS_khKukCzIPmQ-uO8dkhIwRhtfv3SILTTXW9uSTflx6n8G9gTjgDZSP3K6OTsyEGxR_5HIhpgbbnhJUatp3ja_mt6OSjVjWPoJW6sB22uBn4w8yDtXI3B4SyewzQI-SK7b50zR8rht-THJAU8_zRisS3N_OnAGZLd3PthoqNh2MNSO1BjqpNHICaFEz3m-tqCN7-kWIwbMdKdCerW4hTreQav2pBtxk67gZ90hFzHB00xz9aeSEc9TN9zZ-SN23MEOYGGvm_rnYZj-4ztuknVBu_WFBpFQ5Zm1inLAEEtR2B-ZQKFx5hSwZmYG1tojjrSNuJ648f0uMSPll-fMcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0VYg8nWNAtW2M0aUZrgIcV8c4hpMjtHfjtYoRBeh1yZP14m0JbChLQALQG3GhNJ6FHpCiT0_esa8uGb6svBRoGPeEKlA0wxtwXl4aSU9PUWs_aHV1PbID64ND0nxEdoO-QOC3Vdr0O-N7Dtv4zHMHE4DGn5UXk4BlRfgxk1lkj52yDLgCySyzjAmmhDWDUve8QERuLU2yQhImbmWMsoNG8VHVMjUcSbg1pOtbnS36FbYvOdfYj0WH7thz0KYuIWomBaeoEbAGa9ksbcXCh8GeAjqpGHexmSs5s0IfAKZsVbK8i9PAmowP-MvxN6tv1NgLi8gOSmSQnScsQK8_8ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlzAea6lD1wbh2Mz3he-VNtsNDUPuYsne280EONIZShfxlpaL6RuLGO27JZAxRh1wZGSOEbVloqfdvyMs_06iJija98W3EEyhibkd_2sxsc3eiEnSLSEnwXBX26ukeefzvwqnQBDaN6wkr0noM82F7hJl1PrFnZFchb91WIDGLF6iNi55T34ki0s-jKPjLJRhvMMwkivj4FWuEs3U9qJ9Xt-A31QW3l9jCJd5rccb5yM8cIIgmmoi9txRRrI6PgJFEo68JsRjbO24QYI9GFMwVfNTg4O_j2zxVGA9p_Y-oh64pJEWjcew8-L_ElRz_ozsXRD6U0qKYQQ1hqpJLxwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VEJAh1et5m-rD7cTuD9Me87fMDhVMWN4yNu0O6llPUoxTGKGgVqhFdTois08-5hSEmC6uLt7YZZRJmlgo3nHGe93CGOa4pLcn6Ozm1gIn4-UcidC6WDM4dNVWj9sGlGp17digmctFX9aepg7Nt-0uCvoB8cGZ9e8UOU2DZxBQNmuCZwTqKsN0gIEelj1MtvqNvaIwH1MsT33rDTtiJe3JILJXAf4RafzZyheUeXb1W6XiySxpbwBdx_ky__usVIupGJ8cPCHhOLJGP19AR7JqKVfRbGHJhgmFLpINXoG-tIREuHlAmPJYlBR6r4nXtClSRN2ihfGimkRw-FPSV6Mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipZnKCp1vXXHJNmjGCfkwDZLdjDyJdmJHNaX0loEs8xMSu0IprFpWtrJpYEw1oSQnP_frCUHsBHQ0PScSuF8oi0bnFiMainmB4tpzavvhPKVJpfd3G5Fb-iBV2zygxQdHg9OS8oyRIjuOMm3jMob4kiFKDMs94C7OhJtQH9NkIOnLRfNaGkPRHDbT1TUC-E1wSqmkTndKrsM9VzJMA8wniYSoP_-FsdA0_OCnYJ4ojZ2DQH5hC7A3Y-YN-kg9yay8-G5P8vUv3aVWDTt_mRXIwNwVCb-pjLvqqqvfkqjaTuMxwnVTUn_iO93pnysTenDjP8ErmgPvMrsbYCMooG8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvLes98mC3Hyt_qW0ieVG_Zrx0TwTDoVnvklAWtNPf9VHTVrE8ipqiqANIqoU1fs0tIF2DmYq4oaZjzIyKQIEnFhL3b0AvcoYJaZ2uvSSOuiZnk0BcSF7m3x4dRP1QGS5RdhsS_bH1wslodh4B843NpiX7LFbp39Xh1vW_MNVr_NjyJ6xwIT4_-Y2EF3GCx8UAjw-P3ZLppukb7k3jkQQb8CZ3N7WwS3eNuLlJxn3GxP7mDDLrNHq8I4-KoNU_s6yoQtkd9XtrcvpXOdh7YX_gAWbcD-VWD_Y-EMbPKzLcKayuzHgezwdZfGqH2AgJhSHvmAt7KQe4O-DrJ9UK5AKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=aTQQUzoih3cvIKH87FNDbJgKeSPE3V70sG5z9uz_dDAWjTsk8aCznoqa3HWpdJME82_zPJcLsnCZ0Gto0Rj0a05sYsJnRzTxqX10xZe4RawLUSAL2wGnivgMe9Cq-nHf9VCCPKZRQIWvzrcEWGU0fdenN5pz-ZvbDiraaZ2HXaH_YkYcXCcxPHIkhlKhZKp5y98dTYhjrpUO_gcJaEKf4HsOS9YDdOPowj5XrLr4KWS2F3Q5eQf3TtCq-QUh27e_56WASGJTpLPlfTRQ9rn-KRAkyZ0_4yc9m8qOIGDJMrNd-yrDMy85uyydARtIrwE2saahLTLFxU3tPJgURoXbHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=aTQQUzoih3cvIKH87FNDbJgKeSPE3V70sG5z9uz_dDAWjTsk8aCznoqa3HWpdJME82_zPJcLsnCZ0Gto0Rj0a05sYsJnRzTxqX10xZe4RawLUSAL2wGnivgMe9Cq-nHf9VCCPKZRQIWvzrcEWGU0fdenN5pz-ZvbDiraaZ2HXaH_YkYcXCcxPHIkhlKhZKp5y98dTYhjrpUO_gcJaEKf4HsOS9YDdOPowj5XrLr4KWS2F3Q5eQf3TtCq-QUh27e_56WASGJTpLPlfTRQ9rn-KRAkyZ0_4yc9m8qOIGDJMrNd-yrDMy85uyydARtIrwE2saahLTLFxU3tPJgURoXbHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsLu5ZAg9tc_GlwGURHk310hVuzUQAFT-7Blou8dPkFLYl8S_RImW7FtT9lOIsHd3PUPXWfTiGlXr4HzvUmY6Afo0IUIWk-xYmddUwFgByvuDifTsFzO3wmz9oh2gUqS5Sq3KiHJcf1Oc9dTduAckLc5aTKYomX12FIMhnSYox9hxu-IO3yi7GZJ0LLTUFIWPhJUMPZZEyvNrF3kDaYi3QfPqkyS6HD5l3PMZIw3lTS9nDVCYmRTkYyzI4PQE9rfPllXsSwfTHsjYIeE6iLXie_MLmnC28xnnCSqro9BlJt4gUmW2hvzUf3dSid69-emIinsgFkIqcLMBiwF-E3lLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmXrLORGDciot-ECjH10zk0Z3PlyNmJavVL6B-kSzE03Z7YqV7MdkM4vx2g3Ijil34GUoecnq6wwTFsHqVWNuOS4CxOpVPJ4OLNU1DuUxYzfnQzmHxkh0w7ISMe5ZA7cyMB6CkgVqLXf6SrGEb1VW9HfqTiCsVNdjJKmHD9_LX451UXNYmgoG8GRY1avPPlY8sWxPtWYdXsWDnOrvQtZYmlbna3CftPdMYJpoFnlUmtSb9WERZmO_P_VgVraH9jZ5sLhp5_KoZKbRmMLg2wvKqBs7hWVGd-TIsKKtHtuiP5YnuqyyZYwbHFPCjaz3s9MHU9NKN3ITy8YyXJs7rc5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HqRF-QWaqcBPkmSLTPEPfFZUdJrkE2jK4V-fxXu8S-hirqa6iO5p3mY1aLHAYEpcv5NamSiJx_PGEL3xok5TtNG9XBMJ6iWKpYPh-TlA0XDeF3bzqLcYfzYGTGnE_--hZMhVEyDb_G1cjZMQ-5cTYQp2PuGs1iPqXPmc1aTWU4XlsiRL3NCB1Vq8OROA3TGtdxm_cN2zHhawz1a52siRj9V1wqnp8BtNdeXjHFzN54E666YT6ZFcg8tN1yqDtAxo6jq8xBkgNJTLNwgpxGy8TvO_2xs1h-g6eIXe7qOY8INmTARIXUPsB81UlDXxAC8k6YUrGECypThKP1aPMwDQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HqRF-QWaqcBPkmSLTPEPfFZUdJrkE2jK4V-fxXu8S-hirqa6iO5p3mY1aLHAYEpcv5NamSiJx_PGEL3xok5TtNG9XBMJ6iWKpYPh-TlA0XDeF3bzqLcYfzYGTGnE_--hZMhVEyDb_G1cjZMQ-5cTYQp2PuGs1iPqXPmc1aTWU4XlsiRL3NCB1Vq8OROA3TGtdxm_cN2zHhawz1a52siRj9V1wqnp8BtNdeXjHFzN54E666YT6ZFcg8tN1yqDtAxo6jq8xBkgNJTLNwgpxGy8TvO_2xs1h-g6eIXe7qOY8INmTARIXUPsB81UlDXxAC8k6YUrGECypThKP1aPMwDQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=EUQ3hXX-zewm_BNtjpHFaJNiXKW6xjESzosGbURX_Iz8bLgshU97LYnB6Y0TpZBJN33wC7gS0L9KtiGPubZNOY82n6_GImmgOX35NkvD7Lwh31nH-J3ChgDs0D75gAPfrsN8iqFVwXZ8V__Q1p4sv08u7ogPBqxMcisgEd9iLACTtWNaMeJDh-bPdBM-gSz8bvlrCqm5pA20otCve741b15X9512zjz5QEAUa1L592PyupCN-LB5I6lDAMCfRpQ2qNvhrjYhZ3ysHl1b3uggmz6oei1VmoFK4HxYQFko_fGuYa4tbhu1XaV_CcI1yqbRcXWD0WdzizzLSDN65zENVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=EUQ3hXX-zewm_BNtjpHFaJNiXKW6xjESzosGbURX_Iz8bLgshU97LYnB6Y0TpZBJN33wC7gS0L9KtiGPubZNOY82n6_GImmgOX35NkvD7Lwh31nH-J3ChgDs0D75gAPfrsN8iqFVwXZ8V__Q1p4sv08u7ogPBqxMcisgEd9iLACTtWNaMeJDh-bPdBM-gSz8bvlrCqm5pA20otCve741b15X9512zjz5QEAUa1L592PyupCN-LB5I6lDAMCfRpQ2qNvhrjYhZ3ysHl1b3uggmz6oei1VmoFK4HxYQFko_fGuYa4tbhu1XaV_CcI1yqbRcXWD0WdzizzLSDN65zENVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6RXZ8K8n61-j_gAO04BaQ2XtEoJx1O252OrmGkcXK_Lo7K9HfqKFvbWw5Na81rYGmO6n3Drv0SOh6bgHxvVzaHx9H7KfZ2jXkPY7KviGA6_dlzgH2zAuY05czX-Qwv6v2tqlB0p5hR9Bzpct0Fkqepjt7Ygq-af_zcAJVa2dW1eZfoDO5EGHBCyaQYNrJqqxcy5aLg_U64vGBRhJGKL1T8EF06OuUtxhGkX2UMnxu4TXOFn8GQeaLPeLne28j0ZWwQ85YWLld3c7LRb-43CLvrGeDOeavK5jaHhO17MjFrjDdNyt1s-XL-Bq7HJ7A4pMQ3Y1UwiWBq1LXLuAo2fAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC_FFtuiZJdQumTt5kXAhJ-sqaodX8L_gzZaFzcUDg-slIZR1yADKgqhi7zEN8q9-pb6oAZ7dkOMAP3nvFqblbXfHjTuoj666YpbiUC-HGT0_nqi-sgKopxLHny23kN6lMzRu6IaG7DyQGdLYiTjWzJuHxBushFKtIpVIFzPi3xnTDoDSkJpCtYqZweYHBU49tS0TsvVpJbrmw1mkQdLgyUxACuVHJ4ykSF3EofEbtlKDVHx1dSTZanNDly4J4XwbC-KhxKMape4_pvwpU4knkCBKgXYqLgnWBKPIa95KJoPqCpdNqzEu984FXcZiPw9OjV7hS-BvEBiBjVBuMJZQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxFwrvAB1fazTcdEf8tckEGtmSQUKCsEdD7cD70JcifhKRH1ycSy5h4mbrzZNVSCy1p4xTMBMw5at-lJyquNq5nE2Aj7BWFA7exk0Jffm1AACaernNMz6R_qi7sbZWaVI9bIHFcBGUfiAvPa-is8xI30mLcA-vEBgJiW0jg4viTP809mH7vbxckgRb3U8TNdPyCW2DaRBl4Vu8JoqZKEcOMBDYyauaBNXjRShayfKsJTMxBrVcz6daPh9h1itZ_yDhX3CDtrZXm3XMrpjtlEIPqxxXXl02Q0PFVxNp8_SMuNfUbZZp8FcsNN9WcQtHnx0jUD1oBzX8zLx2I0Hwa2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCVL8dmzzMZnjbUGyx65GiUG540KwgSSTyrz4eYYxhaNrMGRB4WVWxfxntOeH-nhtkiy3yaCah59tC0aCYZ_JD-yPiVjnXFok0Y-38lMRHjKuzct9oNVx6yIaI_rUBh1obqYZ09kfzvErMeoNbijc1WdjOzS08Nu02dG-a-KAMbBXXT0g19VY4fdkjJGdNs_E1h8bQswpk2lEITa-fC6NtXQLWiEfr79nNzwUvZrOybx-k6-q7lS2xcSfHh8ocXqUWW_QdjGfQKz4xEu4td4tSiA-FNRptz6JLkM2wVOF8CqFJynQqwZ-nDO6dV7qqnBP9TQhoj8ICpUHIxu7tnX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLSMwS2-HSnD73_v_lD_D651UxL4WLyN4cVTD9YkiuGgA2DcVPHwnxxiAShJWUSlUhbRfERXVe-lOBrqA86jdSa_RtqFgSyUZmmNpRPjsUbiw7Q-_nxWRTB-IN6WcZ3ubrsSdjUGzCDaOwILsQ3Pi5YHC6Yc73inTH1BtBGzQ15S4GeyZcN-BacWEIY0GfNIViaUR7BZ0dI9kK0CZJ-NouFvZOS2coaQCe29lsxNFOEp85vJlCZ9yjdZikL1XGZf3_WU4PmN1WLcMGCyCCbzZaHivcp9ISohJcKZDzfaAmwb6ZojCe7_fHDuHkklOjUwGxBJfiUhDOfW_W22ltRxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YulBVJBITrT3-4_7bxtt-yWBSy2WUebOULXxDyzJPExDs4Qmff9igd83pAFkhmU7754s2Ku90SCrUbhG7Eoap3q8xDn2R1QC4akXgNMWfloiT5tbVUcjjrK_e3drurImwy1NvST7Vr2txr173o7rgmjRsiw83LtpQr0rbr4INSOkCGOnNnrxuzx0Nrszs5wJEUbFBslamgNMVRicDc4jPlrsj6JCayJ01c_WUUpQMHV94gUmGZR_WF7LGTC_aviN-d8emjEZUuLCBDTwW9lSTYGZ-ly0nWxq7Xjhzz1XM7id1CB-_zQ7JN_EvuNQUNnSNbPXPWaWfNAHgz9AzMseuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8dS9GpYJTBYW7ZJAghrpPxu7JqKY_bD5gp9uHPyWPQeaZsgkglV8_Go0A5-77eX-cbNC0jfu-_xk7wvst6mAOnZS6u1g0WIVImwCs33sALEBeqPUFg5fTi1m-9A0x3RJOgheT7295mfhgniyg2Pt_yPRm1BGonb2H04gDgN3wAIsqXM4OjLdPs4wWFSNHnHtDm6QsD1rlfEbinRQDvWaObE7feS6pSHr-XD5rDAUrHaK228FKYIo5SJT0BhHmpKnbWm9G3CfpU4SavZowD2Q5BnHGqSYRQK2gYuyPNfoH8JwZ20goptaQ3-3URTGzKEahoHkVSR6d80r8Gvjhv_yA.jpg" alt="photo" loading="lazy"/></div>
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
