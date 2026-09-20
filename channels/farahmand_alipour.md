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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 04:00:47</div>
<hr>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgps8NOQAYsHqo-C7w1TlHrRd9XL8LwNsfFZmHkgNogJTpgWoWF3EGCUGOlkitEOewg3HIpjSC0Q4O-Ohsk9q6YVMzHAccYh8bf6N7j-1n5tFMgyvtqXzqaNRTpZxKDG-knsvFwk6nau8bJlULZHUQm9eBc57QjbFXMllC77zxM6GiBuhV8Eu8CzFzSLpsbLrosxRFuiOiYu_2FxhqOSAMimmpWNULGEr836M0F8WrpwGL-GO8jahtedlfbqk25W_LC7DbcUqDn-PtN63KMkbmZIQZYu4HQYvGuDbxyqSiwDkI-K37ApVVxSvRMJtsOohrW-WXwgAafkG4xKVdc8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxCZqM90KVWnX2sBR0aPmmOl2LJFzVU8ry9RNId1sWC2ngzYKE1D4tre_Cv46WDTORTqmEp8G6UYBJtEFlxA4XyhLHhZ3h5ZI9DDqbGUj3GHtR6YeV_tD631Wp5p2dJdMBFp6FlaIkt355Qw318eDSC4dvfrUGpvTcZmcUIEamoua50ELP3nlBZ6w3qTzH8OGpFBjndCwEAV9dnorMOtUUrD0U58t0dg7jcPLmcTtdqTyQDnNkckCsd-1wq__3yvqhdcsvkOBRfb1NTEQ2TsaeBPl8mZwT-ox1wqsRS1fYjUW4Gl0GS9Iy-GSq0d_uRJfwZx-yhm944LQtz__QTZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmi_K5Lt3QJA26TTMCHJ-nL5DV96LSjxrZ3QUDZTl67E6p4tEb_4PpHkCuex-eS0z4-De-DvgtdYUQpscYMrwX0ovHAmrjZ5y_MyhxGpURAS3PvprxafpO-iofkrnIMANF3_kjpErN7uDO86965dkDCwiN22nZYppOF-BbdS7-xqkGlW98ioVGZfmQ9KX_Hl0WSlAZ6eDo5YJXEb--O_uZ7VgcC7bqms5_CdkEG6K6k1qSXrvX_uBpJkXI4DGcYo80pKfPuQ-6ga5nYUV170l5fEBUI41X2iVFcKePpk9opMboNrsGnMNIIfr_7DrRIP-MKStRz0k1H8eGOwQCiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=eq4RDNvX1rwCQT1XOV9hvCXwgmDqkj_3xOq_K_31DgyejIPsj9aks0lO25alt2ozukgnINaiFHkrgafMzRXb2VrgUhakRcrjytUjqEjkHqP7Ik1mfY89l8T78T0abssKcYxzUldPsGSXMEL4A4UOSmjOUA1voNbnzre8k4duU2Ym0JtLgVhXqoMHyuby-KbykLGBzfz8LapTPPZozMug4gI9NaJ8Uk00SBcjPejnjCLUg7AnOXubi_CSI1G5xzqqw0Yvs9w6r_5SrcxVoFMDJo4YPOstfng7Ittom3zwAfeU9ag6j2XaDb7PLNL4hx5igSIxWoyjWOgrVt20KFukQqejkUs56mU88Li7jhDQOel-YlR6j80tNWr2hhJ7844AR0oOLgjDPNpjZClYHINtf2vLlylvPh5wJCZ-61TqZERMgnILwh_Ao9I3kzVMe_XqtciMno7l6fQRQdQ1UePfUYVkZ7l9_U7l2gtwv7NO046yYVLrNa-r87Pz6uWu4Ozb0C3EMBxCstaDBWmfExie73aL86NJPAW_Enf_LcDCZFujGoxU5LpVxAefU4b7SJNCawqhmGjWZZFlCo6UCq75FgHQEFTP8pS1gyP4Wwx_m-tKoaa4oOTbKfC0nnJDOZQ6VngMl--0DZCIWezdCRz8o4U0W_3v9M1cnpx0T8e2yqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=eq4RDNvX1rwCQT1XOV9hvCXwgmDqkj_3xOq_K_31DgyejIPsj9aks0lO25alt2ozukgnINaiFHkrgafMzRXb2VrgUhakRcrjytUjqEjkHqP7Ik1mfY89l8T78T0abssKcYxzUldPsGSXMEL4A4UOSmjOUA1voNbnzre8k4duU2Ym0JtLgVhXqoMHyuby-KbykLGBzfz8LapTPPZozMug4gI9NaJ8Uk00SBcjPejnjCLUg7AnOXubi_CSI1G5xzqqw0Yvs9w6r_5SrcxVoFMDJo4YPOstfng7Ittom3zwAfeU9ag6j2XaDb7PLNL4hx5igSIxWoyjWOgrVt20KFukQqejkUs56mU88Li7jhDQOel-YlR6j80tNWr2hhJ7844AR0oOLgjDPNpjZClYHINtf2vLlylvPh5wJCZ-61TqZERMgnILwh_Ao9I3kzVMe_XqtciMno7l6fQRQdQ1UePfUYVkZ7l9_U7l2gtwv7NO046yYVLrNa-r87Pz6uWu4Ozb0C3EMBxCstaDBWmfExie73aL86NJPAW_Enf_LcDCZFujGoxU5LpVxAefU4b7SJNCawqhmGjWZZFlCo6UCq75FgHQEFTP8pS1gyP4Wwx_m-tKoaa4oOTbKfC0nnJDOZQ6VngMl--0DZCIWezdCRz8o4U0W_3v9M1cnpx0T8e2yqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=i-gj_jEBKzh7xCyC8skWTS2pbkNQtX1OYUNIvfRk16eQw3rSpP5fTUF_0nqtiYZ3L0FlsvESorhUKE4f2SlTacRq71P5DzpcSOdJSiRygmRDAzPw-lPuYEG-C0yIdDwflMlp0BT_AaayJPCWUtx7RZIj5xUmogQfWel_z9IPa5c4GQke9guclsdphgZI0f2ZoHPafLFAIIVREuAtsX2YAk_mQZNTYft_N59OVne-sprc4hr4G4B_T5KI0SNjc0nck7hkbStNEgA_eYnJsPQepXurAHWed9v8AQiZUOWy8f-oIDxvOw0dMfgCqyRvjBNKK0XPqys54l98i3umvN8NtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=i-gj_jEBKzh7xCyC8skWTS2pbkNQtX1OYUNIvfRk16eQw3rSpP5fTUF_0nqtiYZ3L0FlsvESorhUKE4f2SlTacRq71P5DzpcSOdJSiRygmRDAzPw-lPuYEG-C0yIdDwflMlp0BT_AaayJPCWUtx7RZIj5xUmogQfWel_z9IPa5c4GQke9guclsdphgZI0f2ZoHPafLFAIIVREuAtsX2YAk_mQZNTYft_N59OVne-sprc4hr4G4B_T5KI0SNjc0nck7hkbStNEgA_eYnJsPQepXurAHWed9v8AQiZUOWy8f-oIDxvOw0dMfgCqyRvjBNKK0XPqys54l98i3umvN8NtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PW-E4GiORsZdfOV3f5Aw24DPAt_4eVWl-IytxQSSjdwROEJOLgHc9bJEMCvu2xBNBKWJ_1nItm4Jc18thXiJ1S03DwL19xXJ4Y_Ffsj-wVGftnznBGVGcuZ3L9sFJCtmwNqyAzykWfQalfu_w1oekLkgXpzr_e574HmPMiSReuTtWXLP9AyiYx0PMc5Fs14DLR1ukRajKLo9dGigLqBYE21GCO4dY_LALIFHI9jxZLOZkhfxPVmx8U7i66gYQgJw0NVwd_Zmh0lYxXTG-BDRO8Aalz1r8_PhoYjhHKXnNhGFrOA29CE0ne3g7gaPPUtVawe5sZg8RzPLcEB0vSRT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PW-E4GiORsZdfOV3f5Aw24DPAt_4eVWl-IytxQSSjdwROEJOLgHc9bJEMCvu2xBNBKWJ_1nItm4Jc18thXiJ1S03DwL19xXJ4Y_Ffsj-wVGftnznBGVGcuZ3L9sFJCtmwNqyAzykWfQalfu_w1oekLkgXpzr_e574HmPMiSReuTtWXLP9AyiYx0PMc5Fs14DLR1ukRajKLo9dGigLqBYE21GCO4dY_LALIFHI9jxZLOZkhfxPVmx8U7i66gYQgJw0NVwd_Zmh0lYxXTG-BDRO8Aalz1r8_PhoYjhHKXnNhGFrOA29CE0ne3g7gaPPUtVawe5sZg8RzPLcEB0vSRT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=e2gjOSrZxdZ-eahlOReycvuzVqa1qBxtiQ-JU-k01KNwIF2jtsKDAQUL0CDqLNRWqSXi0w38QIsCg5n_iGELmToWSI5r90JPqKgg4KXc-SN___HJplRD643_TR7STr8B1SHNpBZTvR2D7JaWTesCEjpY_OEDWc4qGG58ZXiIaE97JZs8j27ow9lucIYeQF4Hx07ainLpHnJL_LB5smnXLhf3NjbcH-Yk6PG2sB_1nc6m0KO4hChn9Sun9sDGazU4tVzg6NRBmNa6bpqojR8_ACe3JKMEVW3-rYhSwIfRa27cAK9VAl64UkFsPho6mReOC6X-_39NHk9zmj4bYS01gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=e2gjOSrZxdZ-eahlOReycvuzVqa1qBxtiQ-JU-k01KNwIF2jtsKDAQUL0CDqLNRWqSXi0w38QIsCg5n_iGELmToWSI5r90JPqKgg4KXc-SN___HJplRD643_TR7STr8B1SHNpBZTvR2D7JaWTesCEjpY_OEDWc4qGG58ZXiIaE97JZs8j27ow9lucIYeQF4Hx07ainLpHnJL_LB5smnXLhf3NjbcH-Yk6PG2sB_1nc6m0KO4hChn9Sun9sDGazU4tVzg6NRBmNa6bpqojR8_ACe3JKMEVW3-rYhSwIfRa27cAK9VAl64UkFsPho6mReOC6X-_39NHk9zmj4bYS01gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=WZbIrz5tOHps2FLXUvKPZ-IpfzWFvsXEswspHHh4ypR62ImPqqfgyoOoCHj0Oi-cUXto6qhpMG-knyVM3EkH3_7wu1CZfeAfjOOoiFoStaOFfTTKmOu3hODAdRmHRYH51-kXG2VS2jbAl8kB2GbPNLHVQpg4FoEOYwb5vcfneFC9NUnY_6AyNz-JwkxtdEWvhirb-nhyemYV-Vg72wERFlyGD_XPIl1M2bJ4yikh4NMr-R88OIxLoj3Bu1HvaSAmYIbbjKYl74SSnECoVFoUOLu9e2E7Q9VNKEsLAnxDWxfRoQrDNKBKBRv4QZvELddsSFvK9Cpr273F8johO1A1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=WZbIrz5tOHps2FLXUvKPZ-IpfzWFvsXEswspHHh4ypR62ImPqqfgyoOoCHj0Oi-cUXto6qhpMG-knyVM3EkH3_7wu1CZfeAfjOOoiFoStaOFfTTKmOu3hODAdRmHRYH51-kXG2VS2jbAl8kB2GbPNLHVQpg4FoEOYwb5vcfneFC9NUnY_6AyNz-JwkxtdEWvhirb-nhyemYV-Vg72wERFlyGD_XPIl1M2bJ4yikh4NMr-R88OIxLoj3Bu1HvaSAmYIbbjKYl74SSnECoVFoUOLu9e2E7Q9VNKEsLAnxDWxfRoQrDNKBKBRv4QZvELddsSFvK9Cpr273F8johO1A1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVTXYgg-p3hMkwybD-GxPMk9B-EqxDtZKEe_Jw3FuQf8lmmWKWwj7ZV0nRugYxidAwFlR7QSHtsomlyt05DTj25IacylOMmZijINBgh2MixwlA7fc4jhI3KRbp9pibY-tCxryuAv4dRW6kedv0FW0qb3gZj6HL6zJ3gEsqxGOlCdnp4qfWHECS8U-K1adSMetllR8fQhY_AIc5FuNkwTSaYLZPuQoUKn7qN5FvVklKKL-shAJmYZ7RTsOYcXg1WUEmVT106FKnEXX-ELVU9IsqoukGSsYFP_w0NkB-gvLphUfrWm9Vlh951U2rygXm0OpyToyVMccBZzfG_Ns-3klQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=dHzrpQEfairxWty3RxtP1zu_sZyybU_bHK9MT4XGmFIIo5-X8bDMA7psSKb28Z-ZNaf851KNdTFEONPbb3iMhQsd6rLa4-CP4ikm16FW9SOXU4eIteGGbhjMWZS8Mhx_E3fuqmjd_5tUTY0H4yl9N4updLh-EXgBvGlCMT-GWtSV-cyW1fJtpkAgjCSA0kf5QhF7VQ-oXW6QlHI0s3kVSHzp4r3o24ahM3E6Xwq8KbuCrbJ5VZ2c9Kj9_YVhHOrmBttAdZatclujgHA27dBmm_Zc84B2YpCsma4ylvudnZhPF2FU0-IFNdYSB4KyE0ZRr8ecXKX4WcrYM8PxcIVEhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=dHzrpQEfairxWty3RxtP1zu_sZyybU_bHK9MT4XGmFIIo5-X8bDMA7psSKb28Z-ZNaf851KNdTFEONPbb3iMhQsd6rLa4-CP4ikm16FW9SOXU4eIteGGbhjMWZS8Mhx_E3fuqmjd_5tUTY0H4yl9N4updLh-EXgBvGlCMT-GWtSV-cyW1fJtpkAgjCSA0kf5QhF7VQ-oXW6QlHI0s3kVSHzp4r3o24ahM3E6Xwq8KbuCrbJ5VZ2c9Kj9_YVhHOrmBttAdZatclujgHA27dBmm_Zc84B2YpCsma4ylvudnZhPF2FU0-IFNdYSB4KyE0ZRr8ecXKX4WcrYM8PxcIVEhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=nn0Bo8i6dUZR88A3ka33kN99GLEHQzo2dbWUaHsr_AcWd1xACHYApyhzTLzyCQZVsQ4bpJ8RJZe0Yg51qqOg67dopOUxtbJlr6AgB3KSSRolDOQPu4P9HsPHxGWdPnElBi-26dy3FXFAJFnI1F_wwM8PTjn32LePLe8IVoEZ2Hajs1a3bJxqTE1axfCCDmiZ7hBpBU4VwygGhkGvCl_zkjq1Z6NuPs0D6bWL317GzvA5Zg0ZEKA6oAhBSw0MupLXtt6iJ-mE-W_tw7e8xM9O-w2MbjqpMpn0f2uXbLcfMNeeJ-yMVk85cEgWzRotV9fxGWOGk9NBqfpj6L2_dewmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=nn0Bo8i6dUZR88A3ka33kN99GLEHQzo2dbWUaHsr_AcWd1xACHYApyhzTLzyCQZVsQ4bpJ8RJZe0Yg51qqOg67dopOUxtbJlr6AgB3KSSRolDOQPu4P9HsPHxGWdPnElBi-26dy3FXFAJFnI1F_wwM8PTjn32LePLe8IVoEZ2Hajs1a3bJxqTE1axfCCDmiZ7hBpBU4VwygGhkGvCl_zkjq1Z6NuPs0D6bWL317GzvA5Zg0ZEKA6oAhBSw0MupLXtt6iJ-mE-W_tw7e8xM9O-w2MbjqpMpn0f2uXbLcfMNeeJ-yMVk85cEgWzRotV9fxGWOGk9NBqfpj6L2_dewmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcHDk6TDinHL4zHUK_Kxxb-UEyYGIn1LWoxxXutHNCBlYeaCcoYj0ujtAq7vVSj4aSQjPmuXrFbntxviY3ggovaGPjOBl5GJANeD_fKr74Ak9UuQZOqHuYFcFbzpUN02qwZw9zoMQVMgVadWxnh2V8Bnt9tuWIQzfmy8CJLUsz29PkLT7Z8VFnmIggrVVJC3bB5dfgg-aCfU74HZUknZ1jiipjGAFq09xULGsUMrt6L62Pw2g3kJ0VyBfwkoBn8rIp3gwLBCkMrOfn-P_Ki8L4gy4GuvbaRHU_OYfgYBe3fosQ8MnvBN8hp_YvN54mSdxmxfOrYTMIf4CKyvCkjQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9-WCBl1Gb8QgxDP_9p_ehUFd949FffUOL0RWLsixIfiTygvRjSQGUwaqAmg4PmkMTjzis_vfAzNuZb0E5snBxbwH-mqAWvOiZOO4u-sztpuEEex-Z9idTGsfMC6455EkfTCDOOD77X-SyhkB9oiLXpuTIjr_UXw4dgYAaZ4NBMHEOlWqlQuYuA4qhVFlUW1uh_tQAcere9JCGV76DSSbJVkMp9gnv9kE45Ikgxtl6G528jeC4NcnojaDXdZ1NPlVxEq0N96T4Y_PKDMB-ug0yBU8DFfS2FCwurGkb4cC7a_R_uvRvPbiIMX1d3haksBYjIsVJ2A-V_49maeZb81Tg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=SFkgMcTjgXiKT1pMxlNmcDB4Xqn2lPLzxyfGSndx4f9-g83zZfnx7JKsBGUNd4A2HlixM2rcA3l7QCLX8yp4vDePDm6c9PY8sJoz2Pw5XwbQ14x-fR9UGoEiMgeLNfaz4t-bI8nP9uZHqW0nD4t3O3DzbJg92tdGaOloTXy2xXy5_pkRxVoFqb9fK20g_YSj0EqUFZ00slLozHVVvZu4OpF7xmKbdMMclmMuJYPjqd__5Op0bTRCJMI_BNNZwb5YlAuILUjft3WJ0nspCSZkZe5vdQ4-0Sw_UZv4nOJWqO_tROomEeR-nj17ooXGu-QVj3xCyP1iWlDnVxJcKG9gRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=SFkgMcTjgXiKT1pMxlNmcDB4Xqn2lPLzxyfGSndx4f9-g83zZfnx7JKsBGUNd4A2HlixM2rcA3l7QCLX8yp4vDePDm6c9PY8sJoz2Pw5XwbQ14x-fR9UGoEiMgeLNfaz4t-bI8nP9uZHqW0nD4t3O3DzbJg92tdGaOloTXy2xXy5_pkRxVoFqb9fK20g_YSj0EqUFZ00slLozHVVvZu4OpF7xmKbdMMclmMuJYPjqd__5Op0bTRCJMI_BNNZwb5YlAuILUjft3WJ0nspCSZkZe5vdQ4-0Sw_UZv4nOJWqO_tROomEeR-nj17ooXGu-QVj3xCyP1iWlDnVxJcKG9gRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKNdcXKOVGGsRKI6wp7N_dlLUyNxgeTtZwlo8lpqm8ah8UR9GTpQbWfTIX3VNG9tDFsW0xjmG_E-F__BK0wLmG8GJCpGRUYQlai3ybE7DGrjhMqBtMAEoqxhT7Htmv440GVU354-ocBusEtWCNP6Z6Ah4wltwDhZqCji2HJS56iuRbC6L3RXj9eAOU2oV8VBdZpoBeGHGGBTUr3ba_3WEN8SioKkiMhRseHIbsd8kc4w7-2MBPIPRClnwrS8FZXjSSf2T8nD222cSg0svKH70uLWC1xims2V2oggcNFtna6L9oOEUcaer_Au-pm0lzSduLxa30CiiwFVbaIg1SYhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi5_-Xny0GQeEB-Nh738KG5JvPb59PTWhpS8HZ7YW98tWKEYYnDvE6qCoJhrbGwhrhm9VfEnXxKfIfiORbl0hkR6aoNlHomxPvGHI_Yd4ChM2WdkPF8C-95PuFBZKa61OF-WJFwpGb09geKUHvUvLt_ZnXJsCDvcSJZGfBcrG_0FbLEC4edeOR9msq9o3QUmOi83ksZCUv6XKJz--Rc49nTH80cIVLKuM4LusidwhJ18eX9CbTMYxpkDYvJCSv2xpSNMTXtM-JoJGgiBq4RWjm20LFw7MXYzG-MnhKvAxjqMx-CtSf8XrmeHAWAwoOXRJzekLm2RGVS6y_BbGiCOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co6Xi-huXeivL3rXsjCnc73muwGipNecly2drFtpwk2IqxTcJKDM6hHVEUEaSAP8isOL8sRb5AxBeqdLtsKG6fALs9c_LzoGwfM0GSTIA1zzyE7d2j9bmPO2BS-inAKsNzC0mJOpegMN76enuVx37yt46GXctKLNoLoBbo8-I251DlxUMJcd90eqhGa1bRQo6mCdeFJGhJmsMFyX0TnDReLv1MWBZa4nVt3Oda5DXJ1SKo-eKyIf82KP1prz1hvLOk_2oa45TCDTFPv-6GpCx_VuETmVgAXC0RI-btqlqWDWUKo_6FXtghOuuljWvKcWSr1MR2rW34GYeTCKh24bnQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=X-NqPM61XHRQsSk2WFo6D-dRNGoGA9vDJA7J3tFHThhycSYQr2BG3JAsY8PpmSX8-omY2EkRWUUhAwGYrT812b73fpCFICI96LJau17wTmFTofU-DgUJOM8X0wncCQG1elI5UyxYbI7O9c1O-IzW5ijd7njEL_VzOKeOKFofIpVOXcKZ0yh82d9cO1AW9k9nvU94dia24E-0mHebitVxw3MZNdaQmLCi9f34WBHugkVsegIaJRwonZ7Xp3rEzm6hEcByDCvh5VR7WoEIeaS69PwD7bdOaFauqOaDGsXyAh9hZpttIGgpaZKdojL_h0d6bWox9kDi9AyXtAMktWobEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=X-NqPM61XHRQsSk2WFo6D-dRNGoGA9vDJA7J3tFHThhycSYQr2BG3JAsY8PpmSX8-omY2EkRWUUhAwGYrT812b73fpCFICI96LJau17wTmFTofU-DgUJOM8X0wncCQG1elI5UyxYbI7O9c1O-IzW5ijd7njEL_VzOKeOKFofIpVOXcKZ0yh82d9cO1AW9k9nvU94dia24E-0mHebitVxw3MZNdaQmLCi9f34WBHugkVsegIaJRwonZ7Xp3rEzm6hEcByDCvh5VR7WoEIeaS69PwD7bdOaFauqOaDGsXyAh9hZpttIGgpaZKdojL_h0d6bWox9kDi9AyXtAMktWobEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=uS5TQ1F1zbI8YUErYEeyg4BlqZJj3pIwdN_sdcUyOTbBtX8EacqVk3bbp4d30p_VpSIpM5i3k4AsmUI7Q-ZDRPryExbp2N1uiiCa6f9x9n9dswkW7rgQSmRkOS9qsTATBx2rulRTPw8-z7krWZDlSEuh_56kSyy-gWaGKZBfn6EiZRyZcHjr7GGOx_ZQt490CWkbdBboeXAJod4JJtQD_388aZ8v8gM8wYdOhk14V4uUEdhN6yvBHxe3jUWMtWGXlDtcMY9KSAYxwJVd9Xz3wklsP66-SdfxUHUQKSpuyfagrSI_6KkkW5r9hkoWp90E33DjQhWVeF1WLqEp8EnXeAgq71rg-AHTxsGIvz8T-HG213JrgM2UKRo1rQ1xb6aVMsz8VLcE37TzUMfJKZzSGTTWs-S-cA4fiqNos78_seoXUQEJvEeUS3yfIi2ZxMV9-gdignDniDa2EXovSLQmyjXSLcd1uBsZYGMpfrx1MEYxP1VWjn4ePrilKwNW2j3K2zlFd2cE-qpCiov2fZr4PkclWDfIv5Sc_CZoi7xDarryUtnWbuMosrjhfwvZs5ltGnjn6yl9Fkh8mqtjC_fEEMFs7fKaDmR8kupLkytpgTBcThUxCKoPcbSekj38rKK64X1Poq4jd0ocv3Q9mvrgDI9aM_BvbzmBAdE79ObGOZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=uS5TQ1F1zbI8YUErYEeyg4BlqZJj3pIwdN_sdcUyOTbBtX8EacqVk3bbp4d30p_VpSIpM5i3k4AsmUI7Q-ZDRPryExbp2N1uiiCa6f9x9n9dswkW7rgQSmRkOS9qsTATBx2rulRTPw8-z7krWZDlSEuh_56kSyy-gWaGKZBfn6EiZRyZcHjr7GGOx_ZQt490CWkbdBboeXAJod4JJtQD_388aZ8v8gM8wYdOhk14V4uUEdhN6yvBHxe3jUWMtWGXlDtcMY9KSAYxwJVd9Xz3wklsP66-SdfxUHUQKSpuyfagrSI_6KkkW5r9hkoWp90E33DjQhWVeF1WLqEp8EnXeAgq71rg-AHTxsGIvz8T-HG213JrgM2UKRo1rQ1xb6aVMsz8VLcE37TzUMfJKZzSGTTWs-S-cA4fiqNos78_seoXUQEJvEeUS3yfIi2ZxMV9-gdignDniDa2EXovSLQmyjXSLcd1uBsZYGMpfrx1MEYxP1VWjn4ePrilKwNW2j3K2zlFd2cE-qpCiov2fZr4PkclWDfIv5Sc_CZoi7xDarryUtnWbuMosrjhfwvZs5ltGnjn6yl9Fkh8mqtjC_fEEMFs7fKaDmR8kupLkytpgTBcThUxCKoPcbSekj38rKK64X1Poq4jd0ocv3Q9mvrgDI9aM_BvbzmBAdE79ObGOZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=RT2_eraoRxwHXDEvyvi-QF61z8SB9wgmOWyyyHvMvjg3lOdicNTgq4g3XTexPR4nxD2LYabz2K3Nn2yafivPbiDyLQuErraKm9GDLrhdRe-0GuiZG-TRAsVzpjwt7EkHu53OHQP911Q_cINvzyT6bQXf8_RIWTLqZSlYCbHFpK9wM6bSfvSpniDW-NxFrm2jcqz9hz4eGGwZY31js1C9w2d2087K983YC_4tS7AaN5yBvLIoPDhkHp-wb34VSmFZ1kofC5TXL23Root6RGofcX-SADsBpDDFmAKLEmkMK8QE7j-1Q2LrlKNHZsgbgXTdoRWmyhsZTQNmkFZPg-t0jK74nQXEZOPZAbYbxJ98ty9cDb5G4J193dMpu4nR2ihQfda_YW-8OJ6fm-Hj2DbHiFFhGPHsaiCarORRiRBhJqS94JMqmel7ojmA8gkP94kEnUHbGmRWpxA9MwIWOGT6klWIE0Q5PHwyvy0Ueo3Rl5S5yswA6HOeNpTS0rYrQqrxmffhPy7WphnhXrNBJn-hLUvGuaXzA8Oua1YTT_Hy1rmMWdjYd9Wd6siG2-g-oUXuYVunGzYEr-xNVsolXYJJVYFWjZHJ1d8MGDviKGrXjJj2nVcwYJCbnkY1mBQa6fO_eiMgaOY24Z-lV0Gvte6Xpv9XrC_yffibgXLiyJhqBIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=RT2_eraoRxwHXDEvyvi-QF61z8SB9wgmOWyyyHvMvjg3lOdicNTgq4g3XTexPR4nxD2LYabz2K3Nn2yafivPbiDyLQuErraKm9GDLrhdRe-0GuiZG-TRAsVzpjwt7EkHu53OHQP911Q_cINvzyT6bQXf8_RIWTLqZSlYCbHFpK9wM6bSfvSpniDW-NxFrm2jcqz9hz4eGGwZY31js1C9w2d2087K983YC_4tS7AaN5yBvLIoPDhkHp-wb34VSmFZ1kofC5TXL23Root6RGofcX-SADsBpDDFmAKLEmkMK8QE7j-1Q2LrlKNHZsgbgXTdoRWmyhsZTQNmkFZPg-t0jK74nQXEZOPZAbYbxJ98ty9cDb5G4J193dMpu4nR2ihQfda_YW-8OJ6fm-Hj2DbHiFFhGPHsaiCarORRiRBhJqS94JMqmel7ojmA8gkP94kEnUHbGmRWpxA9MwIWOGT6klWIE0Q5PHwyvy0Ueo3Rl5S5yswA6HOeNpTS0rYrQqrxmffhPy7WphnhXrNBJn-hLUvGuaXzA8Oua1YTT_Hy1rmMWdjYd9Wd6siG2-g-oUXuYVunGzYEr-xNVsolXYJJVYFWjZHJ1d8MGDviKGrXjJj2nVcwYJCbnkY1mBQa6fO_eiMgaOY24Z-lV0Gvte6Xpv9XrC_yffibgXLiyJhqBIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J34-oyrcX1R4_eCtnCqCM3K2J92KJMNEpcTCQtvXKHe7Xa60RR-mVhm2YzTXIzmTXkbWBqQK5Rhjn-r3E2vri0jn9HdmZjwa5jowkIx2Ju_0s_pGr8HEYS-InFlkf2q-wY7M5Mmqra1rK3QLCXPXrPSo_0P3qrYpCYYAR7FfbJrmW_fSp8aCspt6W7HPuoiXoEzsEDK83HGH0I7XGdNCa5gcdMEa10pMgKcWoADJpZmZblnJugqtTpxyoqMy0jawaH3K_0swpJf_7vNwhIa0GijyxX87oWfR1CI1mryBPigC33glJQi19vYIL9WFXXrGdJze18TpEQv9-sg_gQl9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=mlosYxl11bXy0y6dp2ADIHWAiIs6HZ4NE82ZslJm_fjfrb1W5UD-kxFtnILXdSjECQe9TJ98ZIQI2keKsva-WTMLXPFNYq6qGsLvQhXuv1pseP1ofMqHNdix0yQTS81BYrSBH-CRm8xcD-3W-4O2Kuq121F4ScVyUD3ldJsTeSFuLAWz-nK4RfzpUM9i8M9UBAy6Je6RtWzFtBi2NEp5zZURsvPrOrk3YQ1X5LOJerqI-wevQ6FxoTRUIacK_pLbJQVDOXhhH2M_oGN7A4SErVMYvg-gn-meksThIaz3u5Sc9dKJN7RsZ6nQiTlOUlkV9AOkJd-VdoSuUxikpoTpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=mlosYxl11bXy0y6dp2ADIHWAiIs6HZ4NE82ZslJm_fjfrb1W5UD-kxFtnILXdSjECQe9TJ98ZIQI2keKsva-WTMLXPFNYq6qGsLvQhXuv1pseP1ofMqHNdix0yQTS81BYrSBH-CRm8xcD-3W-4O2Kuq121F4ScVyUD3ldJsTeSFuLAWz-nK4RfzpUM9i8M9UBAy6Je6RtWzFtBi2NEp5zZURsvPrOrk3YQ1X5LOJerqI-wevQ6FxoTRUIacK_pLbJQVDOXhhH2M_oGN7A4SErVMYvg-gn-meksThIaz3u5Sc9dKJN7RsZ6nQiTlOUlkV9AOkJd-VdoSuUxikpoTpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=b7vh9jLY0Mn3YzdSaSpYbCn0Hk0jmEuudlCfGy2jnHDorGqZIlwyRgSj0WAfzDiOIdgEhmz54vlVFJ1IyNRdXUBDKpc4ADs8qU0dHtY_fpXdRNJm9Oy2T9m2L20F49ojswABKRzJKeylSIeiV2K7G0QP6grQRFuq1bLZzxQt1abPEiAO040Eg9tMoyMrYat90i-scvIqDdYnVDTOzxrtsWQM9TBmbgpVJcUOCjIu2T4Uw8KV6iWkyJiG5ewvRsqYRNc8-nmbzBb4gP-IvmnP2l6gT4eKvL5w-zE84Je8YpmgzxBZgsJlUXdiE2QO69S2B7T8JncdRvV81T3pT270uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=b7vh9jLY0Mn3YzdSaSpYbCn0Hk0jmEuudlCfGy2jnHDorGqZIlwyRgSj0WAfzDiOIdgEhmz54vlVFJ1IyNRdXUBDKpc4ADs8qU0dHtY_fpXdRNJm9Oy2T9m2L20F49ojswABKRzJKeylSIeiV2K7G0QP6grQRFuq1bLZzxQt1abPEiAO040Eg9tMoyMrYat90i-scvIqDdYnVDTOzxrtsWQM9TBmbgpVJcUOCjIu2T4Uw8KV6iWkyJiG5ewvRsqYRNc8-nmbzBb4gP-IvmnP2l6gT4eKvL5w-zE84Je8YpmgzxBZgsJlUXdiE2QO69S2B7T8JncdRvV81T3pT270uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP22OjfKJZE9B29vKFwyWygHcfY8WBrwgUkXTVKD9eSTZuPe1CnoSET9hEOo-gsdEeDLjSpsN9ESq-eYjRECFEjUkm0czgMByQxGeNcTgetzIMWIsGNjZV6UqB2miO5xhkRYd1wNWqkiwQXebC4wesADsi8gRkh6mso5SiU8OXxOnhaXKyAE09INzBmnlDvdkUsp11CRklSYkrmEFQNEW43AJMmNblijxpXw0j49kE2W_xQQILwUjfmp03VZ5V0d_BOFwrFMnw7X-IE_q8sLBSuoZHZKOSUs-kIohR9OYwmHcMBmJ_k1wQ9YfZ6-l1MD1klHRo7Wtz1DBfNooOh34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMNG4zG7doI2ht7kC3DbhthR43D0Ay0nCXgqIo3VwL9lND1QZ2lX_JToB4jqv9ejNSbWYUarPrS7i7AN_1laVxBmO0Z2EgQ6Se9NRSNYM4bSlJVc4XvS51YEj_fBzSV7MD5reer52AjsgPYIg4dNSuwopdZFyBBzJT9B4jOdWHWooznu5ZeqxOQStLOQn3lS9H95FK65K8nygw-3xjiMxa6R204FGukNQhHmbf5B1dEScW8Ol2K061XhB42c0wJzUYRCEh_hpCUE70j6axOtJUZiUbDnAFEgQiTkOaaj9CeStxDNkhIWBdINPeahaM2aluklGdBSrW7AboFoT3v1AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCFsFjgpFV3xfcf-Kxlr2cFVvbAIdSWcuSQv_Bo9zeI3mpEER9VfsjSUSdUnnSJLrIlJdH4tjgMdRzX6LgsdZG21ttYn6lxE6U1wfDbsIByeOScvdBvOYpp2xjgBM_Vq0Oh8It5ksoBcvFAvxp63BBbkIn9tmNGeVZBlGS3eVOg_e13xoLKpNRVGmePSl--yR8H4YoPIsOLD0ruoL9DN45sRaUBq2mM5ZzCM6lfC3XNFUxOYaE1xAAD-Yy2HBx1OJ9GIWcQoknDXpAdRU4XuOnn9G0OrrtYLlEVwFlGq3KE3wGK9OCTDxGd5Qycq100UP8cdu2HJP4qa6jfWjZc35A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yle3pd0BLwSeKHkV-8BT3h4CNROG-HGFt7QquSQGHxZVTv5Hz-mZJhrtJ_Eqab4_5yWNTcwqQ0xpILT5dknuGi9eArhLvFCYxfsCn7IbqsezAACt9szfc7_ETS6ADoVxqiGfgegTlWIkhrTpx4x9CYr2Z8M3AoqAMMXOdk5pcZfUoKrH4AQimiJABI5YQkcNPAEhakDfKvvtBgbAhkkTe2p0EeOGSE3v_PR_d7hJmJHJ7a2Rmbxlj0J4METB0CRezN9D1Desz8sI_WmyU8J0_-og5-3nuh0-vz7ftEkcp1saNyWxDpO558c-v19VWeHccWH2L9cB4Zlgc_u4F9uVyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5IVc4_o9n2BvpCOVtwdHOkZK-kfPiaCLx60Fs3QgPehEZoaAl0wYNn4O8ZArwTVzyfsUCYSJm3BVv2cOGjjm2n_ozV31Fwd7E37feKX6w-XtpA4kHXDTVUWxmMA1Tnd9blWUAzCY-lf_MWQvopWv48gi9JFy1wr-CB95fDormLiGcX0It-CZcLtNLtn54WwsVRc1p-nUYihuoEMfLtG3CKeLQCcdNbfeQXZKlEE5UdGcxKh2QuZYi7RmZLTqTaRO8xspOCWoHaZqznpPBaXqYGyxBXW9Zy9g5ZxoTWx4_Aslv-Qu17rK9TbE0F6IBszuj7CLBaIHCDYxGiLg2-FqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNVYzr13HgP-bwm-Xeg0arGNG5uQ8SYMaDCN9xXroL2iFwnyI5V3hCYQcWYxwbjmIaUGZmLyQt_HMMFBNbYSW54h6KpfzJjerF6-4bRFDDLj_TZfcyUB8kbdSBpv3gidOVQfEQ7z_o_yN13JY5YNMx671K4f0OCGbY5eJsex1XFyg__GfhGE08UL2CNXgfjRgFixTS8NvgGKDI77sQMWxJgcI0TtpY65QrNjPlgcuC22t3QY2hsoKfGpP_D-i7AieN4IBGWba-4tWa5_nG1Z4aFTv60HANzfiN6FUimuf-FIhs5qJRLNOpqrmaDCtNad9RS7B7dcmn3BWpH8c_fBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH4ki_Qqv_wP5vdIErTeDvW1jLYkF9PWhEEpfSFeMRYpZg0LonU1_GdvOvVEYKKx1wbkwLhHfBy4cpEnEnI8XttCaEtuc-vjKx7UbyNQm5hRG8Cw-pi-BZPf2iW2LmgELsKv6ZpcesA9HCP1Uol8RCD7Uir50yvogD5lp-z_TiklKXe0fuS84jFqkyceOwgdfxZXg6OSggbUWIjYKYqx8IpPNwFsDmiZIBZWYAf8T59aF4oMa67Ly_txV9lBE0BE--8LXgYefQ-MohKq50gUzUAraz9C3_guMiX4uiSKyV-kuH7w2pK4t8Xv31YIISFdNCBMfQdPwM6zLauan8hk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBKbNSUFuLrsFo6Ex2LDPZqH-W3KzR5NV5egcEh8-U49NLgRRgeW6OB3PB7igWBXw4o9h_BgXlWeFr-eO0Nr0iBflTDNpAkTLLGlbAyfYz997klec98Q1vJnHzlfkJeQFcfD1VmwqYXMchPnFSjzz5Ve-4McQ6EYUf4inmn24CPBaZJqfKTDekKCN6ExmiRJr1KC20WTujgtb-7eNM64OZTlDKq7_6_52TEA-sf8-uy4VJ5WnCxWtBYivWauRLH-09yaYWKOOy-Gj28mgQM1Ws9H8kZDs2CYcTKPFkSapVCPv2BEjXPYlrBKOMoC9QJjWGAU8c-JVO52rrbi_DdUqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S11YlSya8GmIbvEMUoDIWmTIXacrgPwMtzPNZTrYiC4HQmN25rHYdoLWnOfbumS5PiOABvxn_RjFF22ZyXH30D4WHFkKrdeTZ3JZppRvx6FNUBAct5Q5XZyUMANXb4frncLyZTDaCCratBKDCb2fRAA49j6Pm2nmwPWRsK1kse3D1JYA2lq5qhm_BT4pkYLeU_S1MVYpg7fHj-oeMCq9pghgKGXllQWmF8tNIHqSBaFDHWpNIf8i9PeKrTqQY8IEqKvdV-4g0netcuwdGb0rf5NAtNe0Nhyr3E81d6CT7M627riX4yxnJp-YDx0Tq005YOnCuV0CFKbSrzJkjlja8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlgclFagsi49pFAVfjN_jLxeTYUaQR180pHVLeteeAXY_pTQBk4XMs_tRCf12gEBV0HG5wusFuMlz7Y9esfxJY_okm1x4YOhV1Mjxq2266Dnf2MOrt7elikCziXX-K8zzQ6en_1acSzpH4gYgvMa2NO8cTPtYY3Gd9V14mH11FfAhgMk_5J_B5oQxGqbfjQxJsvrbwvykdEZEy9SRQ50a5xAojQ4TwOkdgCXlpefWUV7dY7MWrBrOo3alB0qd_uYR9p5fFB9ZWRcPs5MYGoG2hg3mm2PZulq1Zf5_2t4D0ZH8VX_GzO709sM0YkXWgCDzLEs3W9XKZWLAihcRtg9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=DDcro6DyVcAbQLnuRnAmeTQLLPhAMhihQ18Kv_1aLV38U8fFie1XtR5RdryijPG0ZVFhDBT9aVK1zQu8ngpZOcWo6pE4PLMfukH1JJFtTFbgisuiFvrEF526n9V5LlZF0a_6Wj08es_XYVpZitQ29eexPrdwKqy1Y7OIiwp2vo5fK6aVXlit9hMtnZIxypQWAuLSzPZeG8oK6oIfZXXISQrzOEnIk5DOqO_Qc9KmDrkCK7UjOnQp-ysdGoYBjLKeQSv0nLQfGcqcVEwKMa0k6mCMKxHpCWkVe29TvgoCxTB-nkR8NoOdes1IOYXMuaXVkq38qr803jTSEgoJ-HEU9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=DDcro6DyVcAbQLnuRnAmeTQLLPhAMhihQ18Kv_1aLV38U8fFie1XtR5RdryijPG0ZVFhDBT9aVK1zQu8ngpZOcWo6pE4PLMfukH1JJFtTFbgisuiFvrEF526n9V5LlZF0a_6Wj08es_XYVpZitQ29eexPrdwKqy1Y7OIiwp2vo5fK6aVXlit9hMtnZIxypQWAuLSzPZeG8oK6oIfZXXISQrzOEnIk5DOqO_Qc9KmDrkCK7UjOnQp-ysdGoYBjLKeQSv0nLQfGcqcVEwKMa0k6mCMKxHpCWkVe29TvgoCxTB-nkR8NoOdes1IOYXMuaXVkq38qr803jTSEgoJ-HEU9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=MUSRoH5WIC4_pu5tRoNPhbh9RDOMejWntXzoZUd_C1Boctqx9rbvwxAOQjWihR1IMpcLQcxLDk0DqN6JNVU_0V1edTGiHO_AJDE2PXB_QWKrJ9BYUDkwZeC91hxcfx5g5lRvLWI26FUT-5ygu8rC4-I7POUrdcn24oLgHuWxwEz63sOZtzwDjCRZUROYxSbEh6tE5PADEWc1a5ohhzyj4I9-yN03AW6XOQWAjwyXY87gnWjkE_vsj7qIZKRcSzHEa1H9Qv5w1ZgNb9882LTwm3EPN48bmE9J4BMCm_gzC4hmbLlCfwJXDqVu408jZnxkKsSFF7rEgdTfNJYgPhp60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=MUSRoH5WIC4_pu5tRoNPhbh9RDOMejWntXzoZUd_C1Boctqx9rbvwxAOQjWihR1IMpcLQcxLDk0DqN6JNVU_0V1edTGiHO_AJDE2PXB_QWKrJ9BYUDkwZeC91hxcfx5g5lRvLWI26FUT-5ygu8rC4-I7POUrdcn24oLgHuWxwEz63sOZtzwDjCRZUROYxSbEh6tE5PADEWc1a5ohhzyj4I9-yN03AW6XOQWAjwyXY87gnWjkE_vsj7qIZKRcSzHEa1H9Qv5w1ZgNb9882LTwm3EPN48bmE9J4BMCm_gzC4hmbLlCfwJXDqVu408jZnxkKsSFF7rEgdTfNJYgPhp60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWk4xORpaFKmgQgtiN--yzmlsiH-EhFfOe6ggFgc-rA2i5dLlsKHO-pPV9CC2SKZs8iaEiC2m6vmAKj4trAC4zLZTQNZed4EeQCWEbo6TPLbIhr8uPdb-UhutaglzXzKxCfX6ueMhVESBPJNyLqVhP0dq4f2gqhg-22D7lRsAbj9a-DiGXao_A02fJ5AUJpB-wHHGtBnjT1HPmNn2hElxptdY-VBO1ljLxNgttGJBom13DwxMmGONOfVsPFjkuB7fy4DlL9DsSfT-Sijc9Jh7otMMY3zOcVpe2hKlohIFABafZm2o-5TFXdGEIjmCg2abRQI-k3RYW0UKoIgJYR5-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIYTuG755m1js2xyTZXNSjXcD_QMLvnH4edpgQq2gkfzamjSQba1TXrdzo-xJOWjJ_t_auT70oqZFfwQ-kPkD0-lYtooTXNNx1heM8x7sjFUid9ct5Fc_6dmQTLa5b18lqmnZhFH2HN64JuVTjGFhJPtHXQ-AWEQrmiF0Pvkj4-EtKWXtDB0pU2KTGFsKdQhscMcUZpKojqXdWIxOE3zmFSbK1v_u3Ma_newqbzNAvN-DdfyMEzsRLLB1WI8kI6avREjvO-pURvr7XLHwcFQvIkNIfKlPmME435hdMQWvhiOpz5PxbA-zbE-9zUJIP_RiIln-pnutOsiKjHoyG0iow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsUgbejcAgtLRU5BIu5XY-g5ydZnSY8ymJLt-M_IOSPNPEJpqYfqxHTCPF1UTRwQQZuBp_qsBPTJr_vuy3l3P8OXMNYYvHHO1mwWVV5Oi4j4Ol03yinfOSxtjV8CJy7tn7gn3tI3K6tazv9QJrmm_8AJSFp3VTHn4iwug3LJScO3SZmYmkTOUJAUXxx7-KJyEW94PiZ3-mVA_umIu23ONOiMM0BFVeraLsk8YyJVD4FnMAyy1pq570E4wxWeZNLEpYmlayfxrXExfkq6zEnJ5njw1Gjr9_4KULWRhDYNsLCqtCBye5EESPQaKWJ-tIJ5xtNEg-2ZGfCSkrab9BUGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kASHpWJW_1RaKFVZVMrveDtpwo1M0xYner4d9d-5ZZswU_jHi3_91Jtfftm2OZnIFK8EXY21xNIUcG2j8Av2SqPkzDP0k1Epm_g1MqFE2BjQyWw9tnjFprLqt3Ukr4kxBHQqLQy0ioW33Wa5E5qDz5Q6hdYFu0UPoaMoNGbEVlwHqMO2L87v_9VNqvOt88C1te-2l-TOURbht6_qT6FpKZBR-lbw70_1EKq1BHLEX79QSfblRLezk61-Xg4mWXZY3Hb1C9PfsKIapCh78pDQO_vfujHB1RlpqpQtR3PrNihtGE8VNfUI5AwqmJ1M_FqVQPL99kqAm_z1HKwheeX-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b46WeIxrCV6xy-V9mYdBiUBr7G9frtmPDiDrxdnQeIn4Dov6CKmWExUGrZqRJ9scBj7EWRpCJQJatMeSKZNC6l2u6Bx40ech1yAZpVP3HS8U6sD6biORKP_Ee3otyFKOJrx4ccg3133CTqkpX_DofirR1vfy6RdUNqpwraiE56Rxh4yAIKRl8HsRtoFl3Sodnsr5tcFbsikrnMUB1E8Rfv-13pRx-UQnpUFsNqxxd_k_It0xSeNdUpxNfb3Krlg1E8-r4a77K7NCzaswfV_GHXzoFnCcepaqPCEyuW37mNYLbf5ra8leqNx4O031gxORU2TdqfqX-FgECeIPVAXbxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATAcOmJFRh6T1rAR1WlIg8YdP2fSG042uLeBzVmAKaLNzSDKIVwd11QJ9Gd8WYvhqzE0X0DnjLJ8YoJnNHJIiaUvHlQVK7d64wqyIUTXzHIZ2oWPa39X0cI5IYvTH2BlTTvodYGveXXaPf-JtqxrQWQITDTueSeSa8WU1WTDYavc6lWxk2YMXe-Bqt37g_M3P-OgR2e3nsAR073576Q8T9nuRWfw3dxGrLFC01GfHz5v9NtJCUQrZzQkR0u0swlRrjvofT8sPsuG5w0F6HGWcshTr5YjsAqq52z-Ipl1fQ2uHnC7sdKtX0StKPOcpn90esceYM2MDSaEQ_8ZToo0Tw.jpg" alt="photo" loading="lazy"/></div>
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
