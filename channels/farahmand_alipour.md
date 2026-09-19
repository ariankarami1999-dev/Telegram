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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgps8NOQAYsHqo-C7w1TlHrRd9XL8LwNsfFZmHkgNogJTpgWoWF3EGCUGOlkitEOewg3HIpjSC0Q4O-Ohsk9q6YVMzHAccYh8bf6N7j-1n5tFMgyvtqXzqaNRTpZxKDG-knsvFwk6nau8bJlULZHUQm9eBc57QjbFXMllC77zxM6GiBuhV8Eu8CzFzSLpsbLrosxRFuiOiYu_2FxhqOSAMimmpWNULGEr836M0F8WrpwGL-GO8jahtedlfbqk25W_LC7DbcUqDn-PtN63KMkbmZIQZYu4HQYvGuDbxyqSiwDkI-K37ApVVxSvRMJtsOohrW-WXwgAafkG4xKVdc8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gr1NdhZ9qoo2OW83qMM0qw63xhY2NVXYwGjGOcjIhuQxi3gwn5qhJzjbT08AfwafjGz8GT-slbpSLBWugnbxKqdwBldBDs2gkA7I5RRvbx_pynfIm1LHXnTh07mWUWTM5dFZEpAwIHxQyXcn1Cy1LIODYPiLedDj7Xb7hWJ8AJ4XeF_mnpj2z3DNYW9jd3srbXQDWeMh6CtsIIncnn2bYdOxC9_nwUqTWEyK1sDETp52gIqgKCZ813OHszMdoP5GI1AByiYkIIohuuLqRFxPzB90dIbBgRy2QnBr0OHHAW47GyOp-pJ9DxsZJEYQbXK9QJjU_lmTe9rksOe9W62-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gr1NdhZ9qoo2OW83qMM0qw63xhY2NVXYwGjGOcjIhuQxi3gwn5qhJzjbT08AfwafjGz8GT-slbpSLBWugnbxKqdwBldBDs2gkA7I5RRvbx_pynfIm1LHXnTh07mWUWTM5dFZEpAwIHxQyXcn1Cy1LIODYPiLedDj7Xb7hWJ8AJ4XeF_mnpj2z3DNYW9jd3srbXQDWeMh6CtsIIncnn2bYdOxC9_nwUqTWEyK1sDETp52gIqgKCZ813OHszMdoP5GI1AByiYkIIohuuLqRFxPzB90dIbBgRy2QnBr0OHHAW47GyOp-pJ9DxsZJEYQbXK9QJjU_lmTe9rksOe9W62-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxCZqM90KVWnX2sBR0aPmmOl2LJFzVU8ry9RNId1sWC2ngzYKE1D4tre_Cv46WDTORTqmEp8G6UYBJtEFlxA4XyhLHhZ3h5ZI9DDqbGUj3GHtR6YeV_tD631Wp5p2dJdMBFp6FlaIkt355Qw318eDSC4dvfrUGpvTcZmcUIEamoua50ELP3nlBZ6w3qTzH8OGpFBjndCwEAV9dnorMOtUUrD0U58t0dg7jcPLmcTtdqTyQDnNkckCsd-1wq__3yvqhdcsvkOBRfb1NTEQ2TsaeBPl8mZwT-ox1wqsRS1fYjUW4Gl0GS9Iy-GSq0d_uRJfwZx-yhm944LQtz__QTZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rY4fepG24-lCTO8ulPpH1z0D6Njz-dEVo_WUAjzmA0VXF5HC9FxpIjg4Cbq4qlI12X6zks_4NtCLxH0k3g2oVuGqa_hX6h3EH5KzK09mK0tM9aEg7DSIJJ_R5Y5-dNfJmHWIBssBbk5RqZOqd71volqbvaVgwzOYVeJ0fMIybI73SfQKMlNlXc3WdYR5Nx7D-EYoiVkBHqc2doVwq_QFYP67HATAQu8aIj5oMb9kgDALWLw-CC1MQvQA5sPtedp7oiJp58ccM12tOChQh7ybjCwkvKNmqa9Z9MwvXzOOlCeBuXWPBMSU3HyUCawfotkRyEQdN8ZTm5AXSN9SQWdmIGiGMvrTTAGRwU5yZ6zLJEb25bgE8jAyZoqfvov7t-tzqY7VFnSpEmKQPKVEBrb9qfj_H5FuZogH-WN12DKFuODILIFV5lJAAYisPpFgVot7TKHw3H-VGyFIKAM0hXBno0kHAJ5XF1HNf72aOURyigRw3_Kj7tIk3QokAPZHOYZQAMm_Z3Z1nXPzy_HrkEFSzR3Zk6nUftxv8rnYa8jHsqAa-o-VUteKvmDWRYok3WudwSnQoqRi0RhKtfhkMG78t5awA1TT__Vw2NFSziowMwrq-ouz60SVYxJjDQisRtYvUHI-mUJOGFaPV1SairONwVQkSqLJrzPLu36JrMOcoM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=rY4fepG24-lCTO8ulPpH1z0D6Njz-dEVo_WUAjzmA0VXF5HC9FxpIjg4Cbq4qlI12X6zks_4NtCLxH0k3g2oVuGqa_hX6h3EH5KzK09mK0tM9aEg7DSIJJ_R5Y5-dNfJmHWIBssBbk5RqZOqd71volqbvaVgwzOYVeJ0fMIybI73SfQKMlNlXc3WdYR5Nx7D-EYoiVkBHqc2doVwq_QFYP67HATAQu8aIj5oMb9kgDALWLw-CC1MQvQA5sPtedp7oiJp58ccM12tOChQh7ybjCwkvKNmqa9Z9MwvXzOOlCeBuXWPBMSU3HyUCawfotkRyEQdN8ZTm5AXSN9SQWdmIGiGMvrTTAGRwU5yZ6zLJEb25bgE8jAyZoqfvov7t-tzqY7VFnSpEmKQPKVEBrb9qfj_H5FuZogH-WN12DKFuODILIFV5lJAAYisPpFgVot7TKHw3H-VGyFIKAM0hXBno0kHAJ5XF1HNf72aOURyigRw3_Kj7tIk3QokAPZHOYZQAMm_Z3Z1nXPzy_HrkEFSzR3Zk6nUftxv8rnYa8jHsqAa-o-VUteKvmDWRYok3WudwSnQoqRi0RhKtfhkMG78t5awA1TT__Vw2NFSziowMwrq-ouz60SVYxJjDQisRtYvUHI-mUJOGFaPV1SairONwVQkSqLJrzPLu36JrMOcoM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=SpH1oxXQXQADHnvydWzCJAKkHIl9vT_vZVM4Df7YTgyV9HOfdBDRWh738wO2xN5zo147tQb_QKa3XO3ORyo_wz_1OFxM5VkChItyLMygAlnbIH379XV3YKhC8ES08bzqtbS5FxkaL387fWCxUenNVIR-locFVCuBydDq5Cu7oW0_ij53BgbOui3cFZd_EKUY3DGVmFBmFTOgsvZP_uKBTVOe8f0ic7zgQ1rwCPr6pcE74M2P9AvlnBQCp9yUq6FfycHp4MvRScdxymg7D_DWPP7sHEYL3ENWFvohwV4UExKVDakcwwOw00YsPxf9IEwgSKvvK5_OJzO1k_hWdeTcyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=SpH1oxXQXQADHnvydWzCJAKkHIl9vT_vZVM4Df7YTgyV9HOfdBDRWh738wO2xN5zo147tQb_QKa3XO3ORyo_wz_1OFxM5VkChItyLMygAlnbIH379XV3YKhC8ES08bzqtbS5FxkaL387fWCxUenNVIR-locFVCuBydDq5Cu7oW0_ij53BgbOui3cFZd_EKUY3DGVmFBmFTOgsvZP_uKBTVOe8f0ic7zgQ1rwCPr6pcE74M2P9AvlnBQCp9yUq6FfycHp4MvRScdxymg7D_DWPP7sHEYL3ENWFvohwV4UExKVDakcwwOw00YsPxf9IEwgSKvvK5_OJzO1k_hWdeTcyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cEyh-c8YVYFsOfkfDj9u1-I9RT181bb0OFdHohpS0w83bAKVCngZrgcJku4SZvzNJ5Yu_bXrjOQahC2Fj8W2-jO66TSZbmlXKAF8Ah-C3yCAtvU3nOAqJNScu614-bmn5eHl-rZwuUN2OHMC2alAdNgf6xOlFPNmMPVedFsioykcqKW9CVenfYqtydUtgOtWhfrCQIsdluJ2quagron3IIlhLAsckN9vZT0KpyKlsZ1UgCc3DVNU9gBQprEBoPQuK3kvaSM_rHyVmwfBKfZVPXuEURVb5HTk2OjpcYOPOlV8DuGYy0wdYYgvZELR8uLVcYkFV2AQH4DjwyBSOGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djqt7jeTchA0KXPM7lqatwKNrBdLhkqgZ_1hnp2CpInXaUlH89WnjTeQuI4AeuFqjyfOgKMbTYO4A9bsvsmHFpWJ2h7Mw18uFbHJN9E9h0s2OTWKKuWbiHH5x0_ndgmmZpwqAnDNLdjjjBK5jH6kere1u_cW5wbe12EywgaIf8VjuquPrVmZ5QoGxCcv-avOC4Hm2D_wd5hySonDHtD8BSK51WPdioq_5gTJtzp3IUfV9zvRKlMNXKpd2ufeSj0BKUFQsYItOTz5w1Ufnk8-MQWw3ZvFbw7QQYAPhpMeWPjW5iVklAldgMuDRJYNhdDtX0sYwVW1yfYjZqVfVFv4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmi_K5Lt3QJA26TTMCHJ-nL5DV96LSjxrZ3QUDZTl67E6p4tEb_4PpHkCuex-eS0z4-De-DvgtdYUQpscYMrwX0ovHAmrjZ5y_MyhxGpURAS3PvprxafpO-iofkrnIMANF3_kjpErN7uDO86965dkDCwiN22nZYppOF-BbdS7-xqkGlW98ioVGZfmQ9KX_Hl0WSlAZ6eDo5YJXEb--O_uZ7VgcC7bqms5_CdkEG6K6k1qSXrvX_uBpJkXI4DGcYo80pKfPuQ-6ga5nYUV170l5fEBUI41X2iVFcKePpk9opMboNrsGnMNIIfr_7DrRIP-MKStRz0k1H8eGOwQCiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdCZkXWmAK-z-SCDarSmag5q-GnQW0tlVyecvNhue25Q0HCfaDbvpJD32j8xnP1m2Vv_PBgt0kqfcRbStoPwSOLMhmXAiSIRHGIhVTAaB10IYl7YmAIWjywrAweASsEYfwJjMb7jarYyS95GCSXafLfiHY9bNAmNH18aHUqlg1xmDGOWWHmvdwfxDv1ZkmS9VgC94F5n3vPme0BXiMnJjntyc7eKmM5hPqyHOGkUrAT3G_0WQH2c4K8vq7rAF6TUuROi03iL413UgXO9PxXQTku4HVogGQNIyTeh9BaJHY3X3-Bqw8roN0Z7rFKO3VtkelViTJPfUET0v9rsg8zxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4HmQcSZ_AdPWPW-W9NjJmuNISye5s-u9xVtQH2BV3q20MmzuEOmGghWO6YVunGEMuMe4t9wUdr1CY54XmI2ZdaLjZTJmHMeaPYYPiHtz4CDe5esuJUmrhKJu31ldPxzxtl3NtTj3Kd1yAMJUAR69DnP7BpwQFmegqGA_NiRxl_VWoMr3KxRBBjeyv9IUafuB5pkMzFpEri31i80wkCLwUp7so8y8rnEBAVqGePg2Pw2MGdow9g9B7q5t6avRnwvkiGk-Obc6CPSFNN3tD8MIN8vloESZA5J8azJijKDaR0oRaDjqdqjZ1BkhlUePsLEHnAwyAiuVgZMuzMMcgxxvvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4HmQcSZ_AdPWPW-W9NjJmuNISye5s-u9xVtQH2BV3q20MmzuEOmGghWO6YVunGEMuMe4t9wUdr1CY54XmI2ZdaLjZTJmHMeaPYYPiHtz4CDe5esuJUmrhKJu31ldPxzxtl3NtTj3Kd1yAMJUAR69DnP7BpwQFmegqGA_NiRxl_VWoMr3KxRBBjeyv9IUafuB5pkMzFpEri31i80wkCLwUp7so8y8rnEBAVqGePg2Pw2MGdow9g9B7q5t6avRnwvkiGk-Obc6CPSFNN3tD8MIN8vloESZA5J8azJijKDaR0oRaDjqdqjZ1BkhlUePsLEHnAwyAiuVgZMuzMMcgxxvvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CSoEXXFPLg9wcUQ_nb7CV6nn6PVPpopqWSqMN0TwQ6Mq3NK59s6AkYLHbsuzDHqlznZsmIU2nHeMSMHgG__Kje5_eaOQj_4Xe7KMuQvMwCUy7bnlUChyRB8xk7IJzUUKtPGLyzp5FumpNTtKPkJQ9gStDeE8CQgdYfbniZxiObskP9bYuN_m5vadcbN-wucoOV3jjORYhemO85I42gdDqfWYeoqTd2AVvS6E1FuIiK-suM22HRSLjkl0X--RWbdP2XTS_5Lec6wnow4KXlyq1BqapF4-wdsjXwWG06nc0XSXBAj0JJhfK0-E_rBzByVUIZhvZxrf5eYUjF4jX6zLAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CSoEXXFPLg9wcUQ_nb7CV6nn6PVPpopqWSqMN0TwQ6Mq3NK59s6AkYLHbsuzDHqlznZsmIU2nHeMSMHgG__Kje5_eaOQj_4Xe7KMuQvMwCUy7bnlUChyRB8xk7IJzUUKtPGLyzp5FumpNTtKPkJQ9gStDeE8CQgdYfbniZxiObskP9bYuN_m5vadcbN-wucoOV3jjORYhemO85I42gdDqfWYeoqTd2AVvS6E1FuIiK-suM22HRSLjkl0X--RWbdP2XTS_5Lec6wnow4KXlyq1BqapF4-wdsjXwWG06nc0XSXBAj0JJhfK0-E_rBzByVUIZhvZxrf5eYUjF4jX6zLAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=gz66sPnXjYc3iqW8vC8ob8d_H9G7YyDpw9SsxAK4v6kXWbwfdYwIHrKuT0m3sWlc787kiW4MdKeWHhUEyk-1OBn9Kzn1uDgmKU_O8zti4MWuPaUxuqVmXlTCT76OvRanz3EG0biO9LQwW8_CPO1rudH30HzhtI1KofNKE045I78co3vpJbtloKTz5ETSUwaPVTMa9ga-BjqAOoC74TTD51_9672ydRg2d1YI2GDL-ShEs80Jl3MoiK8EXtyu3nqapDL5d3LIEotvkPPgINwAPIvEtZmyB60Y-xr8EBJ5Qw0BnaIaD4okVeov-ILHAd39NlnYvAxcZ7eu-0H92m5B7krrL5-5tpH-D04-U2JKvndEywlswbnT8Kv9cZya1VXMfZiue9fZ7UAUdBDAnwNbh-6GRxMN99qcmSGzzEIyU-etTHHYjpWbyis2c-7nyCIVKgi_pSP00sAqnuY0oXNmqlj0YJwUgjh6AjZOO98pDK7aYWg71AbDH9PSEGxMkQZkDUgC3VmdIBTqvQ3argA93tjQDglw8hUeqtAUcasQjme5mF-5PF4YJn25j366oWuhXRCrH5mHrnFtxYxC_-Zmg6qMvIubWi9QmeR-SN_CfvaYf-XCO_TIQkWvNIbb6tbFvMg3QYx5CSfDNagP0blNUVuvDks8QpDreZ4KWOtgzq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=gz66sPnXjYc3iqW8vC8ob8d_H9G7YyDpw9SsxAK4v6kXWbwfdYwIHrKuT0m3sWlc787kiW4MdKeWHhUEyk-1OBn9Kzn1uDgmKU_O8zti4MWuPaUxuqVmXlTCT76OvRanz3EG0biO9LQwW8_CPO1rudH30HzhtI1KofNKE045I78co3vpJbtloKTz5ETSUwaPVTMa9ga-BjqAOoC74TTD51_9672ydRg2d1YI2GDL-ShEs80Jl3MoiK8EXtyu3nqapDL5d3LIEotvkPPgINwAPIvEtZmyB60Y-xr8EBJ5Qw0BnaIaD4okVeov-ILHAd39NlnYvAxcZ7eu-0H92m5B7krrL5-5tpH-D04-U2JKvndEywlswbnT8Kv9cZya1VXMfZiue9fZ7UAUdBDAnwNbh-6GRxMN99qcmSGzzEIyU-etTHHYjpWbyis2c-7nyCIVKgi_pSP00sAqnuY0oXNmqlj0YJwUgjh6AjZOO98pDK7aYWg71AbDH9PSEGxMkQZkDUgC3VmdIBTqvQ3argA93tjQDglw8hUeqtAUcasQjme5mF-5PF4YJn25j366oWuhXRCrH5mHrnFtxYxC_-Zmg6qMvIubWi9QmeR-SN_CfvaYf-XCO_TIQkWvNIbb6tbFvMg3QYx5CSfDNagP0blNUVuvDks8QpDreZ4KWOtgzq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=i-naGJWBc-fmO2-4GXfyqu8TZbnVsyGXnwZmtYeDd3zgR03pARoyPr1g2-4IgItkizZARbwv5TFDrQTdZoKPJHPS1taHY175WbFPyeaS3TmFcQpGOjKCd3RG2UOwc3FRLoYr4aYDK2C9llu_ArQ91Hm-sUo9Aub3VENjBpo8Y32G5CAd_3n-uNIZ05fYdZXYkfld0hpPJzEtI-XyYJbWiXwMN7rO_d0z9GrDXA1dpcL3JP84vbICHBkIBD8P2wK2vo0IYAlJwcx_B8AqpD5C1Bf1cFTJy9Zh9iuMStOWv0OVCn0CiKC2uG08voN8t6bYWwNlQWsWGvH4WY-35YHvnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=i-naGJWBc-fmO2-4GXfyqu8TZbnVsyGXnwZmtYeDd3zgR03pARoyPr1g2-4IgItkizZARbwv5TFDrQTdZoKPJHPS1taHY175WbFPyeaS3TmFcQpGOjKCd3RG2UOwc3FRLoYr4aYDK2C9llu_ArQ91Hm-sUo9Aub3VENjBpo8Y32G5CAd_3n-uNIZ05fYdZXYkfld0hpPJzEtI-XyYJbWiXwMN7rO_d0z9GrDXA1dpcL3JP84vbICHBkIBD8P2wK2vo0IYAlJwcx_B8AqpD5C1Bf1cFTJy9Zh9iuMStOWv0OVCn0CiKC2uG08voN8t6bYWwNlQWsWGvH4WY-35YHvnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNvJJtnqrYmnGNhbDOqN_fWq342poq9juwyrhessflz5G1bFJctVALlIqC7w64xM0VENWNtXe2qqAJasVO1zz9GvlZXQ_NwSQrdykkd66Xpk3TZ6-rApeQ0bn2dqTPW2o58r2Xw6rRV7ieYqcr6GRaLOeLdikj1VMxPzoS09Ls0mJI75C9unez8Zye1AVGkIOpXQ6Z5ybGNfbCaOdANprzMCFRguqQZEfuNtmNsZbSYkTDm23VOyXIG2sNX7_kNwM_Y3l61Q6lbsAE9q54aUpoae--ofcONXk2DqZDmoWvraAVsPYDvQqogc4KYTfZs3NpzOoiXfXPVRVSRpX1nC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqnqhC2kFRz13RUjyBAMfcTz7UseSwuyfQDq_E5iF51uQLN4hZ3mgtl9Hu-0PlEgzBLrJamMWCBF6IvJzBT0xo16y17brw-62xl-2wOylo-dllrfP0Js844Kr6cvIuZRKaf859bv_fSrGezYzSxrPFhY-hYGf7Impy6hWcT5XU59SbkSatVASxOx7BSr6Qhf7qYZkjZJBcdEeNkiPMNpWtpxkztXKpTNcAJ9jeF-OOM_nEGhbOiRY-odB3K0t6zp9KhEyG-Wjm-Ihcir1lTO4G17isFDTV14YWKFrXd5yAi173usCYaIuPj8La_X4ffw7wM_5ALTOfrrRjQ5g_KYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sEjjbKGtEy5GNgJKnFfFOAPP_kPZ-mbe0WofShRSIUR-lyiqJy6qLFhA8NOeAvum2auWguiixVNoUzaMN7R9Db-drMueZRYnb95gIabVwyGMjh9zASuiUifwbgfVJ8IJ8HKmRfRGy8ca-IKqHa1WmZe2NZlN2Cj8keMtLmdUFvzoKOqlci_Gb8YATEY9uY4saYnaRuOZNYUX5l4Zlpcnjp40FdT6J4DIoL2T6qPW8DXl9VyMpJ13nU3YEARBfWRQrvXEK9uwrfCc7LMe8eTz2qWMCoMNKuFIPe3_7JpA8gleZ_8GIamBgvD7T4dAAejnIYXxjYliNmAKrcbePiuvhRwasWEDY2Twa0of7e3Mg6Oxku6fpLBKcDdiluiiBzLZ9acaONpEpbZTfYdcaCents_lSbl6EhO8-IBW720rpR2KYvr_v6EjJIIduD1N4wTrcgc0yzB_mAsbIDovZJ9jyW5Kq2sQHNJaf_z2Bhg4YYnivuq-ArLsxqvn45mmiY03YrPQjxavB8pvxx1LqH5OtDlTtoMpmDUEqvgbRvjTLdMFkyC3PH3dI_jBGgfvH6OJKQ_g6GHfMVM5BlHV3KKrXqg7K6CyJTRGu5tiSHBsmdKdns1fmqa_C7bui_r8FP7_-ZgOqg3t01eHKTlVVIfL9yW5RtGS6B1AAHVfzmIwels" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sEjjbKGtEy5GNgJKnFfFOAPP_kPZ-mbe0WofShRSIUR-lyiqJy6qLFhA8NOeAvum2auWguiixVNoUzaMN7R9Db-drMueZRYnb95gIabVwyGMjh9zASuiUifwbgfVJ8IJ8HKmRfRGy8ca-IKqHa1WmZe2NZlN2Cj8keMtLmdUFvzoKOqlci_Gb8YATEY9uY4saYnaRuOZNYUX5l4Zlpcnjp40FdT6J4DIoL2T6qPW8DXl9VyMpJ13nU3YEARBfWRQrvXEK9uwrfCc7LMe8eTz2qWMCoMNKuFIPe3_7JpA8gleZ_8GIamBgvD7T4dAAejnIYXxjYliNmAKrcbePiuvhRwasWEDY2Twa0of7e3Mg6Oxku6fpLBKcDdiluiiBzLZ9acaONpEpbZTfYdcaCents_lSbl6EhO8-IBW720rpR2KYvr_v6EjJIIduD1N4wTrcgc0yzB_mAsbIDovZJ9jyW5Kq2sQHNJaf_z2Bhg4YYnivuq-ArLsxqvn45mmiY03YrPQjxavB8pvxx1LqH5OtDlTtoMpmDUEqvgbRvjTLdMFkyC3PH3dI_jBGgfvH6OJKQ_g6GHfMVM5BlHV3KKrXqg7K6CyJTRGu5tiSHBsmdKdns1fmqa_C7bui_r8FP7_-ZgOqg3t01eHKTlVVIfL9yW5RtGS6B1AAHVfzmIwels" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OZeRUnXYK_jgHNdkhg4ICqsH76TFZ2qUhRh_8pI2NBQ4aPvzJ4wUNHtNB09Gq6GMSEEtbsMiu4NTFxXDKRN9eWLn1nyxyq1nXyHfUs7b8HUmK2GIeIibNFbKJq_OBxeOhDhnAT_qNBEAx2n1p3sJbt-lnZ2TCuybxx5x_E0LA2m0xHmZGiaim_6UrM6J7KIIYXJU5CeQeofEpLos8WnTJ6oHVaG_IhkwqbmTRU4OdYFkJ7ty6m6Rrwtc3Zteszkcu1FlZLwgfKZkmfiq-7qbuKLbeH1vDJdTxKpjLa9fbpVMcydEKEB3e2eZJaE3r8WRZeO0vYc5OcQZauOA7LCzlT8GPet8nKYWqb1vB91_oZBvpJv16db7C8j8f5wdNm01bUPKm1-PV4ryntWGlSNzo9G88n_GZMRZhbn7qMZj8RLvllSUxwJ1ps3ghi1kcLelC1LJnrTUTq5X88kCe8LZdGfygvfj68Z3mJDkWB3VXern1klcebKmNc4KcV90VfUTgYFon-G6Y3KxaFyf4-vyrXhekYcHtOJI2SKrMzPib0Pt1YQqqsKrjRLoW1HlEfJSrGBmaBvpMIKi4C5aTfBH7xddDCUcxgyLD2vRuhbUSyuoXfVdGVehxwo2ljQiLMhrNCz5_UrDHvlzCV5aKnMk640WZZrTCZR3vEDjvY7DtBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OZeRUnXYK_jgHNdkhg4ICqsH76TFZ2qUhRh_8pI2NBQ4aPvzJ4wUNHtNB09Gq6GMSEEtbsMiu4NTFxXDKRN9eWLn1nyxyq1nXyHfUs7b8HUmK2GIeIibNFbKJq_OBxeOhDhnAT_qNBEAx2n1p3sJbt-lnZ2TCuybxx5x_E0LA2m0xHmZGiaim_6UrM6J7KIIYXJU5CeQeofEpLos8WnTJ6oHVaG_IhkwqbmTRU4OdYFkJ7ty6m6Rrwtc3Zteszkcu1FlZLwgfKZkmfiq-7qbuKLbeH1vDJdTxKpjLa9fbpVMcydEKEB3e2eZJaE3r8WRZeO0vYc5OcQZauOA7LCzlT8GPet8nKYWqb1vB91_oZBvpJv16db7C8j8f5wdNm01bUPKm1-PV4ryntWGlSNzo9G88n_GZMRZhbn7qMZj8RLvllSUxwJ1ps3ghi1kcLelC1LJnrTUTq5X88kCe8LZdGfygvfj68Z3mJDkWB3VXern1klcebKmNc4KcV90VfUTgYFon-G6Y3KxaFyf4-vyrXhekYcHtOJI2SKrMzPib0Pt1YQqqsKrjRLoW1HlEfJSrGBmaBvpMIKi4C5aTfBH7xddDCUcxgyLD2vRuhbUSyuoXfVdGVehxwo2ljQiLMhrNCz5_UrDHvlzCV5aKnMk640WZZrTCZR3vEDjvY7DtBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=J-n_9UEsPeL8AYYQoGRo00JuVsGXZxgqOo5FjuCAZAljTy0MBTPI9ICmfGiqjj2JVJIz093FLYtuUcl5ACMbVtpw8DMgzF5zpZIKXBj5GJ6G69axHVDI93pepXup_VdIqKBa28KIgtrkYx5U41XULvGkjsd5S5FD5C2X6bczkHIWcTmn4jRH6s_jgew-vkYprEmZ5vm_rLuj-Cw-3i2Yww5qu2y62MpADbB2bJZcRYcXLXovLYLyawV1EimlmMunclWI1qEXM3oqAjg0HHpDSsmMqLkBrfn282HnKyGp3fIyX95tuLGhqg9gtNjzdrZauZefLSxGqribZHBq12TcOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=J-n_9UEsPeL8AYYQoGRo00JuVsGXZxgqOo5FjuCAZAljTy0MBTPI9ICmfGiqjj2JVJIz093FLYtuUcl5ACMbVtpw8DMgzF5zpZIKXBj5GJ6G69axHVDI93pepXup_VdIqKBa28KIgtrkYx5U41XULvGkjsd5S5FD5C2X6bczkHIWcTmn4jRH6s_jgew-vkYprEmZ5vm_rLuj-Cw-3i2Yww5qu2y62MpADbB2bJZcRYcXLXovLYLyawV1EimlmMunclWI1qEXM3oqAjg0HHpDSsmMqLkBrfn282HnKyGp3fIyX95tuLGhqg9gtNjzdrZauZefLSxGqribZHBq12TcOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GWRStDFQhWwLEWRmsNJqbj5Ke0eKsujKOYv0wmGNE2rVDmOI_K3ugOtmDdhX5W3TGq7rjoPtSENj-l4WLC2u_cQfSJ9NcxT6VA4pUQE0wY14GHqlzywkF5GRjMYbmIn3I0lsh_RcnkDxLf7kc9g-pJ3D7z0rPCKePixZ9tmersYP1LdtQZDnZV3AIphIMn0L5MfWBGwSnGuOtzbi-mNPueY1NDbx7GM9M0whvUZ9Gr6G3ShiO9YsZP_f0wRN9O-KyZqJnCtcvRpkhrN7xK77eQ1vP5odL2sDcSWnXjF7l87o1qHdYLjC28TuIq7FzlR9I_3Sl6pmMHExkrteYVoU0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GWRStDFQhWwLEWRmsNJqbj5Ke0eKsujKOYv0wmGNE2rVDmOI_K3ugOtmDdhX5W3TGq7rjoPtSENj-l4WLC2u_cQfSJ9NcxT6VA4pUQE0wY14GHqlzywkF5GRjMYbmIn3I0lsh_RcnkDxLf7kc9g-pJ3D7z0rPCKePixZ9tmersYP1LdtQZDnZV3AIphIMn0L5MfWBGwSnGuOtzbi-mNPueY1NDbx7GM9M0whvUZ9Gr6G3ShiO9YsZP_f0wRN9O-KyZqJnCtcvRpkhrN7xK77eQ1vP5odL2sDcSWnXjF7l87o1qHdYLjC28TuIq7FzlR9I_3Sl6pmMHExkrteYVoU0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IMKI4m5BRWf6_LUn9OxDoIK31RJCN9larz7SZhmnZ2-6ldJBZUnQ_rOtdWUlsoRV9EEOi8egwdQuXYPhdDKHWooJWUg-2m5OO8R_d3a86UOvhdsoq1cQ1XzUPIpLAeKBhugQJ_sOTM6pwVJP_TGZvzdmPvQTHjEpLgnpltRDcxVPNAVE-RdUENe0XpBIPpDKnDfuCYVmudhgInJU2nz8aO3IYJE3FS-IpkctByN0qAG8Zhr13KLcKggOJu4lfXRJ7SKXcT9iaaBJ63gih7txqTdONT4IuSl-jP9_W5BePNiMfuKY6f-gzkBWxoIiJ6WvLr3fChGZMQvcwDZUooGvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IMKI4m5BRWf6_LUn9OxDoIK31RJCN9larz7SZhmnZ2-6ldJBZUnQ_rOtdWUlsoRV9EEOi8egwdQuXYPhdDKHWooJWUg-2m5OO8R_d3a86UOvhdsoq1cQ1XzUPIpLAeKBhugQJ_sOTM6pwVJP_TGZvzdmPvQTHjEpLgnpltRDcxVPNAVE-RdUENe0XpBIPpDKnDfuCYVmudhgInJU2nz8aO3IYJE3FS-IpkctByN0qAG8Zhr13KLcKggOJu4lfXRJ7SKXcT9iaaBJ63gih7txqTdONT4IuSl-jP9_W5BePNiMfuKY6f-gzkBWxoIiJ6WvLr3fChGZMQvcwDZUooGvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=e8nswf4U2IP1LcVUYOltu9DugbWW6yQgXug8KJWLfmT3RRNJPUz4lnCk3QtBKkf4ROz3TsP7eu_teZiCiz7MuN_LUoSEyVlcBucbReH8Hpj1sst4c8UXklhk84auJMT9ngnryOfYOYolGdNar8_ipUoNB8rCud3PMq-5QZvvN_qY9CzB8rj1puryOh2NT9FmOnhTKqwDkvlmsamrUAmvjJvUgIeFmfaE1v6wsDbYoD81DJkrG-fZBH9Utos-QNYgxW9SwMrBTtTz9id8gpsUAjrZ_oOmmIZXThWIT1DBnMq578hGmFQqMn84AvAYlADAi86r7nBu3Cb7gSibp4cJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=e8nswf4U2IP1LcVUYOltu9DugbWW6yQgXug8KJWLfmT3RRNJPUz4lnCk3QtBKkf4ROz3TsP7eu_teZiCiz7MuN_LUoSEyVlcBucbReH8Hpj1sst4c8UXklhk84auJMT9ngnryOfYOYolGdNar8_ipUoNB8rCud3PMq-5QZvvN_qY9CzB8rj1puryOh2NT9FmOnhTKqwDkvlmsamrUAmvjJvUgIeFmfaE1v6wsDbYoD81DJkrG-fZBH9Utos-QNYgxW9SwMrBTtTz9id8gpsUAjrZ_oOmmIZXThWIT1DBnMq578hGmFQqMn84AvAYlADAi86r7nBu3Cb7gSibp4cJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=uEgelkgEA1IUlJc-kBPfkSCxtolTMVJtfXh-yMcmZnsyw5psWdYbG_X04n0HB_OJuwZiQBgSUztVgNsuKDp-mJ9tf1ELS5UkwgyLaHXDVV49Ujd7xGgNY0HET2wnopBjJUYmM5yKZ-pJ2Wcyx_hAzkBU3NgX5FLG83-sSk-zOBVLzHKYfwmEedVNEqLZnwvQKVqbpVQqipP9u4yiOaXb28PzDuhoT_Kcsa4WTpwnrw4zXGjFXY5Cn2mWNAu3sZa0X3V9DyQzjCH1qvJlurb_pR4HiBaSoSQuOTGLhuUoa338WaHuOMtCkIiLRFi1l1Xg-aunuo2DP8oI_MKWu1xiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=uEgelkgEA1IUlJc-kBPfkSCxtolTMVJtfXh-yMcmZnsyw5psWdYbG_X04n0HB_OJuwZiQBgSUztVgNsuKDp-mJ9tf1ELS5UkwgyLaHXDVV49Ujd7xGgNY0HET2wnopBjJUYmM5yKZ-pJ2Wcyx_hAzkBU3NgX5FLG83-sSk-zOBVLzHKYfwmEedVNEqLZnwvQKVqbpVQqipP9u4yiOaXb28PzDuhoT_Kcsa4WTpwnrw4zXGjFXY5Cn2mWNAu3sZa0X3V9DyQzjCH1qvJlurb_pR4HiBaSoSQuOTGLhuUoa338WaHuOMtCkIiLRFi1l1Xg-aunuo2DP8oI_MKWu1xiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=JNDTWrMspI0f7cGXpdpqT6KzOJVJd7k4RmNTcncyS7srVWVGTsl2V216pHq-ouYz4KAOtSi9xnWprpeWhMCBhetuYT9AcVw6quA--_wVFRmR4cUyrrSE9BzU2wWbBxWGegRg05OCk2L6nBPASW7l9yMk_zM7ndL-NCXGC2WbdgFnfYmL0cFrdHnsgXAG9cxVZkm3BLDpKWjXlL9vvBFZcaRQFLT_bWAP9xdy6xd234LqaxWMsVS6CtMX6tnBATLcR4h-Jhhb84X0U1Gn85KgJ1VBwKliZmybVV6jd90CR2mh18t2mKKo183vc3mcCVJjNkGY3fZXxeiv-uECb0eakA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=JNDTWrMspI0f7cGXpdpqT6KzOJVJd7k4RmNTcncyS7srVWVGTsl2V216pHq-ouYz4KAOtSi9xnWprpeWhMCBhetuYT9AcVw6quA--_wVFRmR4cUyrrSE9BzU2wWbBxWGegRg05OCk2L6nBPASW7l9yMk_zM7ndL-NCXGC2WbdgFnfYmL0cFrdHnsgXAG9cxVZkm3BLDpKWjXlL9vvBFZcaRQFLT_bWAP9xdy6xd234LqaxWMsVS6CtMX6tnBATLcR4h-Jhhb84X0U1Gn85KgJ1VBwKliZmybVV6jd90CR2mh18t2mKKo183vc3mcCVJjNkGY3fZXxeiv-uECb0eakA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJtSYYXBURU1tkhNWFruisNz9qeyKrtZjTBe4cb44mzeOyQXolQWJTe4As5tCKnVQyeCOiaj76kMd2sUUGM5wIyETzN5ApjPHOzbRr-UwvQ3lBXMYmFWP7RUUVDGi_w4bNwfBH6PMHgmfTWzHMTedJjWCSSEDF62-hYiJWn6MRuAUGToT7GHxpj_JIsowhaOoHBEzvZ1NbjBiauc-59Tr4rbWkeoEU6ShkcQOaFh7yiQqzhv5X4n68FP8D4uEYWalsDq6XXEz9t8JCqPfTFkVEHJRvLrug-ECs5KdZWa053l-sdFadLyitBm4vmkiRkvqUSuRQedysvDcLjR2BTMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=T-kz2-OotwwtVhT-BZ29BelS3G7EKjGkn-qpyr44ynZEG3iRhauJ4325oP2keLIpRarf8Ez_ZUplgzEpu8h4zX6Rau-p6I4T4SBnJ3HOh_8p07I2MXQOR0Q6y5hiPHWOycK2tjepH-4a4VUAwbtYfvM-4ag43tA7UMj5od7sMppMpR6fWrabxBptAKMn6OEsf2fCzDCf2GCEotBslltctQOB40qXDsT2uWgtwbIVhJHST6VQrG8rtb6GuWqDP8BNOIOKZuedPunvCfCYG7DPEE0m3Tsw3kLc4-4C-40Kv5uOHyGQb6iF4JZ0VgOI5_yk7WPajtEWzdCn3w6eAdR0Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=T-kz2-OotwwtVhT-BZ29BelS3G7EKjGkn-qpyr44ynZEG3iRhauJ4325oP2keLIpRarf8Ez_ZUplgzEpu8h4zX6Rau-p6I4T4SBnJ3HOh_8p07I2MXQOR0Q6y5hiPHWOycK2tjepH-4a4VUAwbtYfvM-4ag43tA7UMj5od7sMppMpR6fWrabxBptAKMn6OEsf2fCzDCf2GCEotBslltctQOB40qXDsT2uWgtwbIVhJHST6VQrG8rtb6GuWqDP8BNOIOKZuedPunvCfCYG7DPEE0m3Tsw3kLc4-4C-40Kv5uOHyGQb6iF4JZ0VgOI5_yk7WPajtEWzdCn3w6eAdR0Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=rDAbiM_51qaLMw-wDu2z4OKGTwFhjixjwRYWkaSUyWxltVLJFFiAFqJSbYr8Gx8IAQ6dXfiDbMJ2SynShuywjUfA70gDiRANTuho3hBE5f0yz0u2h0S4bqMOvYB42GXXhyl2hfGlf07G93HEi95aPCfHv4kgqwMvbWes3wD0sVITJZVtrmzJ4-q6zOQEuiQx8E7Mwx8YVXYwOwk_lyPwnmSzgaBhJ8Q81GeJGjRvIFuS9jtV1NAc4PSD1edCqoq99rGP6IWdwfJxIgecg_OwrxCDj5PtYWXdWjC34azL93umkCPekUmmHIkK-Y8RRh4Bjf2i0tDkFCisUwLfZophKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=rDAbiM_51qaLMw-wDu2z4OKGTwFhjixjwRYWkaSUyWxltVLJFFiAFqJSbYr8Gx8IAQ6dXfiDbMJ2SynShuywjUfA70gDiRANTuho3hBE5f0yz0u2h0S4bqMOvYB42GXXhyl2hfGlf07G93HEi95aPCfHv4kgqwMvbWes3wD0sVITJZVtrmzJ4-q6zOQEuiQx8E7Mwx8YVXYwOwk_lyPwnmSzgaBhJ8Q81GeJGjRvIFuS9jtV1NAc4PSD1edCqoq99rGP6IWdwfJxIgecg_OwrxCDj5PtYWXdWjC34azL93umkCPekUmmHIkK-Y8RRh4Bjf2i0tDkFCisUwLfZophKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=k5KRnRTFhg_BSOslSdHIimoM5ZtpSWgosxhDUDDGYj0_Y-AJxZuf5Db1KK7FYOE_o10S5jPpMkNoUkfOP0WXJE_9zoqwNhGbrZEITunL7beFsHyoXzbjkwdkGxBEx9IMHNvUXkfgI39NyA7rrMRc-V8an3rIPkknwkoJx5XeLH2SSLP3rd7QTEJvcmkokcixk8vm1Rr58Wpw8GLbIf4MyOpbVP3vaufpSLlbEpjfqdKdpjhf6XRjRnED5NnAlef1Gnn3YHO2mMUtxlor3HAqWO8dtIh-vVnBt7uv2b3dx7LuBF0flEqmuPvIhU_NaMJAjUOhve1a86qDWqCRfCUGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=k5KRnRTFhg_BSOslSdHIimoM5ZtpSWgosxhDUDDGYj0_Y-AJxZuf5Db1KK7FYOE_o10S5jPpMkNoUkfOP0WXJE_9zoqwNhGbrZEITunL7beFsHyoXzbjkwdkGxBEx9IMHNvUXkfgI39NyA7rrMRc-V8an3rIPkknwkoJx5XeLH2SSLP3rd7QTEJvcmkokcixk8vm1Rr58Wpw8GLbIf4MyOpbVP3vaufpSLlbEpjfqdKdpjhf6XRjRnED5NnAlef1Gnn3YHO2mMUtxlor3HAqWO8dtIh-vVnBt7uv2b3dx7LuBF0flEqmuPvIhU_NaMJAjUOhve1a86qDWqCRfCUGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Dj6Nf4X1PIWuHLITWB4DzW3ZOupd5ShQBSfQuw0GLbToBLCxa_N495sjWLiLt9O40lNZV1uRDElKWYK6zzRfY1L30ZDNfD-TFerLxJuNg2TvVccZZysBJwBlMAHb1IrcQAZ6nCooyES9qbsOJWSQQ1UZQH7ONv20Sa1NvbgcmUJYp9sC6xGywOiatfqZS5D_cFKCYDLYJnqrtCjj6th0GQnYV_e0mUzwxlmX7afHRNu0C9vBdlXr7FSYOtopD5UAN98gcLZRc_K3EEavjWH_cCvEzTRzN8VWMmlKGvV83tCiAbazQCN7NTdfkf6-poDT0Ch3xyD_vFTH5z9KhIrL0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Dj6Nf4X1PIWuHLITWB4DzW3ZOupd5ShQBSfQuw0GLbToBLCxa_N495sjWLiLt9O40lNZV1uRDElKWYK6zzRfY1L30ZDNfD-TFerLxJuNg2TvVccZZysBJwBlMAHb1IrcQAZ6nCooyES9qbsOJWSQQ1UZQH7ONv20Sa1NvbgcmUJYp9sC6xGywOiatfqZS5D_cFKCYDLYJnqrtCjj6th0GQnYV_e0mUzwxlmX7afHRNu0C9vBdlXr7FSYOtopD5UAN98gcLZRc_K3EEavjWH_cCvEzTRzN8VWMmlKGvV83tCiAbazQCN7NTdfkf6-poDT0Ch3xyD_vFTH5z9KhIrL0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn0CZuFiB6P7lEtK-zPjdej07iYDlev5Lzy49AwTLegOHwI5WoWrTTcHdUqEySlVN5du6GPnQ1Un1m-2IHzzEEwxO_rlbYnm4cuyolZzw7_2wrz3ytzmh799tXRmnnnA-GeVOZnqWvo9R-m5WpfPB5XvuBGgk0Tvo7mMnL7JxWeBLO438c_j1-w3Y5zzBjEemAHOjeuOpBUShGkKwiB_IQqGw8TiDHPgy6qMk00PjFLJ7WWOehHqD6ihF1oc7h-HWVs5HGBn37knlNj18VAkm9qdPyVR3XSiaxiXk-sABVGelfUOmX_1KZRddFJCj404I9LtX6Umi0CzCeaij9NtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=WwpsaxT_xRa2X8pfvuXUtWQbZgjW_qbchYyUXN7kkvjvnWb-nNM_-C7So_xViPfmQnnMBD1jOQQAK-aXSRf4JBGv0JY_fIZaq7kxyg9YhwqE_i_tmvCczhbbeiBC2xdMqM-IeQCOpwGAIc6-F7TLKNepTXQ5AL8Bi5ubzuGUedSwpMAGyiDqC-kyzxDRWUjnN4z_p2oxd0afrgZO6f_6X4PGKG7ZvtA89Tve3RiVUq7dVm63rSa2OkNzRq_nzaxB6yoUtwO2LOiBL_KgqqkL3o4FG8xtZNsgQAwAomHhe37yvtz3tVAxkr6shaIsfwdMFaUfY6t5sNkunsdtgEXzcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=WwpsaxT_xRa2X8pfvuXUtWQbZgjW_qbchYyUXN7kkvjvnWb-nNM_-C7So_xViPfmQnnMBD1jOQQAK-aXSRf4JBGv0JY_fIZaq7kxyg9YhwqE_i_tmvCczhbbeiBC2xdMqM-IeQCOpwGAIc6-F7TLKNepTXQ5AL8Bi5ubzuGUedSwpMAGyiDqC-kyzxDRWUjnN4z_p2oxd0afrgZO6f_6X4PGKG7ZvtA89Tve3RiVUq7dVm63rSa2OkNzRq_nzaxB6yoUtwO2LOiBL_KgqqkL3o4FG8xtZNsgQAwAomHhe37yvtz3tVAxkr6shaIsfwdMFaUfY6t5sNkunsdtgEXzcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=bI0TxGN5JJiJmmljjq-5uqtL2zC2odzocryCM4RVsziD8YE2HQcJwGQE49EJ0Rrm__wRhHJU88x3s3h7URVewLQR1ySoDzsyzAjK8wy-_H294EraFJ3CHFqpLwp3G88pOXP33a6NVKPf7_shoXiVNIPpcgzfNR622pVAV1QrF7CFfXP6eZtfe6zlDy8lylx34AiUQsSLk4omHWPlAIZwbzUjH7et1_uk2gSsmYXnK3720wjET0cPbZm4EE_GLA0-VlFdkZgdUUb788tfaarEmmCPC58slG91pgRROtUL3TSthKJT8zQzp0ASg7ZHZV9Kn2jpnDKwwVNHcZrPLekuKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=bI0TxGN5JJiJmmljjq-5uqtL2zC2odzocryCM4RVsziD8YE2HQcJwGQE49EJ0Rrm__wRhHJU88x3s3h7URVewLQR1ySoDzsyzAjK8wy-_H294EraFJ3CHFqpLwp3G88pOXP33a6NVKPf7_shoXiVNIPpcgzfNR622pVAV1QrF7CFfXP6eZtfe6zlDy8lylx34AiUQsSLk4omHWPlAIZwbzUjH7et1_uk2gSsmYXnK3720wjET0cPbZm4EE_GLA0-VlFdkZgdUUb788tfaarEmmCPC58slG91pgRROtUL3TSthKJT8zQzp0ASg7ZHZV9Kn2jpnDKwwVNHcZrPLekuKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7xFX6990dy0n_pOorrXJbEQLcF8HuMEgHZPZAx61Kx0nBdnqklPsI0nQcTOeuk2QYFlddEgqpUcDeNJ3oJGPd4KUKtp0_CjuCVTJec34EIiwQ5Zbofx_S4kwaPp5tE6aSvo1uLGv_dTw1lsxDcN-D9eiywcMkbMGFkPs4zvW8UiKYf_Laz8cwHWPzfzZmTkHUTTtpGJwhlicEncsNi2Y79xahQXqCV3TXfXvF-gwVnSmokyuO0efK9OS1NalVYbI0YbdLdJimyayazmpDFL77dIB4Iy0cHdp-9eoLwZbkmbx2vHklUx9NGiPkhATm1HCPPdiKFMI4hfGxwULeopIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhB3OsG6flJDaKTnVAPy4O7fAbBHPCpFK1bUQnCDbzEgH4FpsoA0oqde9BjxQkCZBXawkdLuTpM2xHd25xoNrudYW-gHUwWUaLk8ZzaB9p0_5z-ih1SuzvkLeRuORZq6UQrRdVBGbCF7sYHq13RRtPU7cmEcofIH4S12OGXDvrUipZWa_XlRy_lpzPBlJRxyKP5RfFTerHKHDPIKj1KNHqh9vakWwkkmjvE6DnjdvZOL12H5QmT8TeLA7q7F0wue9teFmiwLykI-AeDy7OKRktzfjSOvOCnzZvqvIqf4xKS2Wbxz2_tbs63mLGr4gNAWNekfI6nOOE2Xe1gkumjmXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=pPQFwh8Gx4Smj_CtvG_-SEVNm8hMul7f78dYYY1wnk235dsLwj03vq-7MPxroKuRxZ1v2w45aGXWLgb2kgi6a9ZCzUhExysC8xkm1bkukjVf3xhkcxTy-X4USx0RWN8iywCFx0NqjgkKnvHMOBlZ4ZG5QbbqWD0trRx5ztqz0OK-N4_qFWe_bSCdmkfwbvtXcP9g3k8iwSOT_WpYEDCDAQ4ato2hqG0ZntTOPZnMsaN8ybPETzS0b3MdumusAtiO_4vQ0K4dH2P9pZOdChqaM02naXBb0_81cTrfgxuirEhwv2RYTRddCRN0OxoqjaK4B6YiutgD35ofEmsYbC9AxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=pPQFwh8Gx4Smj_CtvG_-SEVNm8hMul7f78dYYY1wnk235dsLwj03vq-7MPxroKuRxZ1v2w45aGXWLgb2kgi6a9ZCzUhExysC8xkm1bkukjVf3xhkcxTy-X4USx0RWN8iywCFx0NqjgkKnvHMOBlZ4ZG5QbbqWD0trRx5ztqz0OK-N4_qFWe_bSCdmkfwbvtXcP9g3k8iwSOT_WpYEDCDAQ4ato2hqG0ZntTOPZnMsaN8ybPETzS0b3MdumusAtiO_4vQ0K4dH2P9pZOdChqaM02naXBb0_81cTrfgxuirEhwv2RYTRddCRN0OxoqjaK4B6YiutgD35ofEmsYbC9AxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCGFA_o2Mtv6a0cgeFWai-S-4YVKA8P41HaQw3t1DjN4rxp_-c38wRolU2hFO5l4lXK4at1SG-hGjfAJUHpnlRg_mO2zZzvffpSEThC0GCft3KJGX96MksCo-zuw3TC9AxKf_IJhGGfEjvX7ipO6WvXIZYcYEP-CTunJa6jzk92fkMOXv5KbMEMQmQvH4KZcEUrZozhUBUTw0tWQQBpbB--3wrUISLGGIhubvaHv_m2Vv3CW0TTLDWAu8jJcd2E_NL7h71K9nNpY0MP429ZTw2Dx0675GQE5-wRNbGHZROaD93nwDH5zj1iKrAMzAkUsrXt-2mNWTW1bJUiaGqWCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAEJl09xDkwiRLS-HgglXGCVWLJZMOpRgY6n7aT8xQw323vBA7WdyMTOCrEmoL5SQ_-Lzfq-PhFY-MB4QDTdcfy-aUCrJJ4LEluhtOdyaadaFQQvxfNeBP2DT5zBJ8tXdpym0acrjfEKEJP1xK9CDpUfB-24DsJ5eStEGhOU9d-PmR6nng-vdoFQ-Z1_WV9XAWYk-MZZ3WZVF2SGlHo-pDsZNorQkbbSaMwzKjOZGsjU5g6RGXhwLT_F49dRdS_ToRGFY9sOt-GRxBERJKg6AnFKdg82kEUp-n6sMqXvdIttczhWcpDToXME0UkfP_A1aflsd-qHuoi3nMM6sz3-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atPmPbF69zUj_z2ZpBq1mT2ldNnA5RJDK56cgkpDeXtYW2UpsytD3AyugD6zG58QA_Hs53lyVx-d8ANBWzik-88qdCO3nhFguZoZ9xd98ECK_hrU_UgvVAikDKAuU2_3opTsyaZP0RnC-DX5zdKTIoR98Tk90Bty0KX_84nJ8K1nHb5lL2J8wE7oMUxjU2UwTfy01AO3Vupucd7pFbh2xXqLpjrVTC2MEzjIJTgc8dcLUotqXgG2KRm0lPXh_POrKAxzLwZVsqk4PTSiR4V59lm1dYifTU37JJb_qCK7z2hGeThcbo4H0uCSv1AuT3XSxSN8yQCpqCJMY8oPN1kY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=hSGtAyi6N8r_aGFJMoSzaB72EryYsisl3WteXbusRaxkQe_x0hisHBA9eOqPCy3594K7k3zFKoEhAe5GLdb1iSYzdEprCHhYIdULixw6qTsoJFLU2mW4fiIFKgWQwBl9cQGdNuvPy883tn7rwGOzj0Ygs-WzMl4mdxqWN1GqgaIlXp7slJvA9WFRaTFOky7u6J-h7FWsfxxHt68FMFSjjcDyjUNOf-3Ve5hSazFT9m6ZtCg5bgyNUOsUTrQQuBxQpDPm8XYB6AY6PSlpUD93z6hjxFhfQVjPI9hdvvQYW369cD5IS0wiSLlR0HfE2cDnU861fVrCwaxOzcQxFwyAzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=hSGtAyi6N8r_aGFJMoSzaB72EryYsisl3WteXbusRaxkQe_x0hisHBA9eOqPCy3594K7k3zFKoEhAe5GLdb1iSYzdEprCHhYIdULixw6qTsoJFLU2mW4fiIFKgWQwBl9cQGdNuvPy883tn7rwGOzj0Ygs-WzMl4mdxqWN1GqgaIlXp7slJvA9WFRaTFOky7u6J-h7FWsfxxHt68FMFSjjcDyjUNOf-3Ve5hSazFT9m6ZtCg5bgyNUOsUTrQQuBxQpDPm8XYB6AY6PSlpUD93z6hjxFhfQVjPI9hdvvQYW369cD5IS0wiSLlR0HfE2cDnU861fVrCwaxOzcQxFwyAzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=i1lugXm8IxxVyZnynfhd63j_K4x-WsJZGlcCaNFTjUx-gSm9cQpNIvx5amP7QZ928IvTlCz7UiG9l9Om9sDalFtWVgTRSUOQP3cdpZZa6glQk3MIIpsB4mKAgjK4v-Pb6hM4zkWlG5r68AQUTZ3qUfeLWTcaoG7GwPj_ebYMq04ADbpUNE6C0H2vP8DxxOSSK0eZqyYT8O6VDLoRlkeqojAuPwxQhlUhH1XJbLTdPkJXpKOumObsMPyNRUTKBMirXgjTuk1HBDNbwiMavfmMO44uT7GPEOgqkDIqulAQB0lBwGPHXa9y_Si_sxKCkPaMWh0ebffAVAR_RVX5F8Y7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=i1lugXm8IxxVyZnynfhd63j_K4x-WsJZGlcCaNFTjUx-gSm9cQpNIvx5amP7QZ928IvTlCz7UiG9l9Om9sDalFtWVgTRSUOQP3cdpZZa6glQk3MIIpsB4mKAgjK4v-Pb6hM4zkWlG5r68AQUTZ3qUfeLWTcaoG7GwPj_ebYMq04ADbpUNE6C0H2vP8DxxOSSK0eZqyYT8O6VDLoRlkeqojAuPwxQhlUhH1XJbLTdPkJXpKOumObsMPyNRUTKBMirXgjTuk1HBDNbwiMavfmMO44uT7GPEOgqkDIqulAQB0lBwGPHXa9y_Si_sxKCkPaMWh0ebffAVAR_RVX5F8Y7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=LebX4OWDOcnal34v-FFftaqdU7okFgHG85IoZqjXwGmrkC6vYWtdKd3XElu88DshVU98Vq6htB5FwLX0e9aiIwxfSlFZxEu8qX1MUjmu-vXjN1WDCh97itk0SNn1KCEs1r8q41hgMyNMkT187xBOT7g5sBCXyhm176hi3GbQIPpvAr9gL_vyKT8hgvAEUL9PvIJ94NR1je1IdurQsaepP071bgJESnJGQc1MZFjtOWgNY3lxIAFEQ3orzuAlwhkzC3Qwfuq4lfQna20r0iYaP-d_Y2DMexO6tBoULudxja5EXzP33zmNpNM3il-lj-1fCDQqCLK6Iuf62_PgT-rjpaEm9pVj7osNUECeHJaeg2ujFVmFj5g25lKcljoiZe8SWvpdUN6vvRegV4YIQQMqaWnVPNHyEVmsPfJQdiVvIvuTfFzy4yRG4vpY3HYg7p7gP3kHsHA9FsVkS9VV2TcLNnWAcUOs4xVz5ifx5QsGEVTgkMAOURlmMttGacI-LJ4S1Mz8lS7vwneRaDLLAwB6s8GYBTFswj9cBeVWa6O2ivq7xICud_7sQkLaGgVZZWf9o0ZB5gRHYYhwz33Oejyq2zyO_sbUIEGDyZRUd1UfQ1XsL1B6MsY3l_KNufZd_U-7rJtvSOafLCxzjsjTwPhFxsT2FpLs82gG81Y4JfhdmJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=LebX4OWDOcnal34v-FFftaqdU7okFgHG85IoZqjXwGmrkC6vYWtdKd3XElu88DshVU98Vq6htB5FwLX0e9aiIwxfSlFZxEu8qX1MUjmu-vXjN1WDCh97itk0SNn1KCEs1r8q41hgMyNMkT187xBOT7g5sBCXyhm176hi3GbQIPpvAr9gL_vyKT8hgvAEUL9PvIJ94NR1je1IdurQsaepP071bgJESnJGQc1MZFjtOWgNY3lxIAFEQ3orzuAlwhkzC3Qwfuq4lfQna20r0iYaP-d_Y2DMexO6tBoULudxja5EXzP33zmNpNM3il-lj-1fCDQqCLK6Iuf62_PgT-rjpaEm9pVj7osNUECeHJaeg2ujFVmFj5g25lKcljoiZe8SWvpdUN6vvRegV4YIQQMqaWnVPNHyEVmsPfJQdiVvIvuTfFzy4yRG4vpY3HYg7p7gP3kHsHA9FsVkS9VV2TcLNnWAcUOs4xVz5ifx5QsGEVTgkMAOURlmMttGacI-LJ4S1Mz8lS7vwneRaDLLAwB6s8GYBTFswj9cBeVWa6O2ivq7xICud_7sQkLaGgVZZWf9o0ZB5gRHYYhwz33Oejyq2zyO_sbUIEGDyZRUd1UfQ1XsL1B6MsY3l_KNufZd_U-7rJtvSOafLCxzjsjTwPhFxsT2FpLs82gG81Y4JfhdmJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=HoouVYQ8sEQLX5GsyIiD0T5TL18RijIBU3Zk5VZC9DKtgRZdrS3bCUCFMZfbVyPV0K_8gdtw4k9w12Q-RXOCpIYa_OkyQ-INGubmI9PN0KyzTVltoEl9pyU8-w27WuXSgmRkVxfd1MOb3yGmRI5NqB9EhMzXSVzkjAWwW3HkhN-0no58ruP9-2Y8311tnj4oi1vHKXGeH0KyDlTUZ2-UqGJLt7-KWA-to2ASaINCj90suQ6iCKPD0_GyxOcQ2sHo2t49JJYJQVvcrssbZ6i9zTPgNhM7NSXW0lCefteOQOmudgXR1-JGnQ1vmHHt1PF5efVU0-XF1LzWI9yF_p15fZToxdZEIIh_d0YrKEQ3XAwl_nC2_DJdngQOY6CjdidqIbP93Xcz3PNRgjdiEJGZ-bK9sQT7FXvj8zWdiqO-6lhXYsRou6HuHzq70yXHyTruUXZkijA0qIHdmF6AxZc67PcDLMs-C2gn4E3WmGvNIjY434nODUOgec9wewOY0kdE7irLztle4Br1HWwoZvdu-S8Sh4QbPK4GW0fc-r809fSKi1waib_XPmb1oOCSusDdoQWLQrRBseuCbaYk7aiUdKLkaGA8SieybIxdz_HI_945sxOicifRlnhIzZ2pVNWWcNdtFnYbQzDnD2CMhwSo7_HlnHMGqbZz676LPlrVK8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=HoouVYQ8sEQLX5GsyIiD0T5TL18RijIBU3Zk5VZC9DKtgRZdrS3bCUCFMZfbVyPV0K_8gdtw4k9w12Q-RXOCpIYa_OkyQ-INGubmI9PN0KyzTVltoEl9pyU8-w27WuXSgmRkVxfd1MOb3yGmRI5NqB9EhMzXSVzkjAWwW3HkhN-0no58ruP9-2Y8311tnj4oi1vHKXGeH0KyDlTUZ2-UqGJLt7-KWA-to2ASaINCj90suQ6iCKPD0_GyxOcQ2sHo2t49JJYJQVvcrssbZ6i9zTPgNhM7NSXW0lCefteOQOmudgXR1-JGnQ1vmHHt1PF5efVU0-XF1LzWI9yF_p15fZToxdZEIIh_d0YrKEQ3XAwl_nC2_DJdngQOY6CjdidqIbP93Xcz3PNRgjdiEJGZ-bK9sQT7FXvj8zWdiqO-6lhXYsRou6HuHzq70yXHyTruUXZkijA0qIHdmF6AxZc67PcDLMs-C2gn4E3WmGvNIjY434nODUOgec9wewOY0kdE7irLztle4Br1HWwoZvdu-S8Sh4QbPK4GW0fc-r809fSKi1waib_XPmb1oOCSusDdoQWLQrRBseuCbaYk7aiUdKLkaGA8SieybIxdz_HI_945sxOicifRlnhIzZ2pVNWWcNdtFnYbQzDnD2CMhwSo7_HlnHMGqbZz676LPlrVK8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aAFjq0INSIxc1rHXv7gEv-bmuOUusA_7mt56IJwdDCC5T6nhkrrpia2CNRfTIilXMS5tgA_V3eHgwerel1ujgfbLyP3v-imz8xU0SbVsnBohjCUymcCRJo2Ry47donA_no1cLzzfzXpRdOKVJ-ukeS-OfvOBzh0wjcnXQQgJpPnT3KBZTia8Zv8mhyinxkC6BBxsrf97vcOVlX9lrYMdC_0Q4slbwIV7thP7wRKKUBYhoPGFrq-yYPszt_nC1MEvDn8eVgR5owyKPKdnFTZmsXGvXczpBVxrl4e3NqVihcWbzbb_-CvlcYmQstFHxbr44_znSzrYtwEgNQVA9rpyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aAFjq0INSIxc1rHXv7gEv-bmuOUusA_7mt56IJwdDCC5T6nhkrrpia2CNRfTIilXMS5tgA_V3eHgwerel1ujgfbLyP3v-imz8xU0SbVsnBohjCUymcCRJo2Ry47donA_no1cLzzfzXpRdOKVJ-ukeS-OfvOBzh0wjcnXQQgJpPnT3KBZTia8Zv8mhyinxkC6BBxsrf97vcOVlX9lrYMdC_0Q4slbwIV7thP7wRKKUBYhoPGFrq-yYPszt_nC1MEvDn8eVgR5owyKPKdnFTZmsXGvXczpBVxrl4e3NqVihcWbzbb_-CvlcYmQstFHxbr44_znSzrYtwEgNQVA9rpyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsBPoEqHEacu7k78HcQKRt-evgd_dtKnAiPz8h8cXd_pg7D9C1FcuhWFjQEzuEqGhT2u8v9dQ2XHLWU4MTVFliva_inueyn8dYYmV7I-5X8h9mu7moduqY_Im-wfRAI2XRvBtVjFXUqqKi-fMiq8l2awYxpIceBDrv7e2IQP2zMiEqPJxvD_SV9mHeSkmxPK_BRuVRm1VzOOxtRExhoxHQIpBGo9cu7nc4uCsv8iGbwfTbusghsXXX3eayifkewPPi_tXS9RsvfrholDlyNJKh8ifu-Ypr2JgJYi8PkR6HJdZndz71Y9aXcYQseirqpXnBY_MekjreaYFh3ORzfKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=mtp-ry4UvbkJ1ttwZkhPxkLRGDauYKHVmwt5Y2wQqcHq4i5uaen7n8ebYRg30hiYGohXcKGcIsUCOmKzM14cp-v5uOJEYFKefc3q5OtZ1GkVLCtSook8-3lJMOIdUDEVsvHYjMr2ovbI5lL0wNKlXFR7FRrEYZXFrvhJGedBwBDmezVZN6001Tsz53_uE8XVj6EsGK5uLifd6-Wfw-5UmDiRUp_Yz5JNeZXlZEAdFpIlE3g4wBS6VV2lfgBgu4aPra-50zHXVieBsHHBFrmA3HEToEpnMA4JSUBTlxkcF7Vi8Wt0tWvDgaiDftDOHiDB6d1rdsWOC1s3UHhpLekrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=mtp-ry4UvbkJ1ttwZkhPxkLRGDauYKHVmwt5Y2wQqcHq4i5uaen7n8ebYRg30hiYGohXcKGcIsUCOmKzM14cp-v5uOJEYFKefc3q5OtZ1GkVLCtSook8-3lJMOIdUDEVsvHYjMr2ovbI5lL0wNKlXFR7FRrEYZXFrvhJGedBwBDmezVZN6001Tsz53_uE8XVj6EsGK5uLifd6-Wfw-5UmDiRUp_Yz5JNeZXlZEAdFpIlE3g4wBS6VV2lfgBgu4aPra-50zHXVieBsHHBFrmA3HEToEpnMA4JSUBTlxkcF7Vi8Wt0tWvDgaiDftDOHiDB6d1rdsWOC1s3UHhpLekrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=XRxbvU2-Zch4MGTrYc7ipcWGdMv-1LLMY_YLG2qnkXX7LnF778iaYU1G3usS4TJXP5TWgJp_HCXqqvlacHkS80GMkIznnSheyVNWtoAbZB_PRsBPAGemQ2Jz6bO2QbZI_2cWcx9NVrJjUqE_rStVljqSo2Zfrg9AcfnCC2i9vwMOu3EamwVGhfvwgA-3e_SNHFi3_CsFyZ4lPs69MIioKojju8lxxoF94FdS0nb-Ea29HL2y4tKBTLEzoPZXwH2QCeOgfO1I4DUD4UJ8rBFsX4RMxFPuVQZvRKNzGBGTcJcNc2Se4ra2s5EFNvWGazNI8cKXJEEcwAwn63u_zKSgJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=XRxbvU2-Zch4MGTrYc7ipcWGdMv-1LLMY_YLG2qnkXX7LnF778iaYU1G3usS4TJXP5TWgJp_HCXqqvlacHkS80GMkIznnSheyVNWtoAbZB_PRsBPAGemQ2Jz6bO2QbZI_2cWcx9NVrJjUqE_rStVljqSo2Zfrg9AcfnCC2i9vwMOu3EamwVGhfvwgA-3e_SNHFi3_CsFyZ4lPs69MIioKojju8lxxoF94FdS0nb-Ea29HL2y4tKBTLEzoPZXwH2QCeOgfO1I4DUD4UJ8rBFsX4RMxFPuVQZvRKNzGBGTcJcNc2Se4ra2s5EFNvWGazNI8cKXJEEcwAwn63u_zKSgJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogjfIDON_F8zcAAkdRvSroa4_xY-ww77uL3sVPmba0JRccPPDoDy0SZLlAN0GXsyuLsxn8CgoeTVqmR2pObOOKJv0dMc36GdBzLfJVp1kJCob0sENRYwLrK604j_hhY92wSOj1vB9zbxPDOGhpmhiVkL8KIM1ST_JgbPrmwihP2MuXTva4zZyatk_VWOanMYzIUaohyzSWJBAYyeeP3J8LQqSQ4RTSYfbrpV4Lsl7Y6YomDRjgweh2TtX7cxt_XMAHVSECWrY3GDczWJgXqLi5xyLBtQKxT1dc5BhDnyPzfvDzJ23ZwsUBR1HwVJIQYYu9ffBfoAMfmPABhioooe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdK34Qit57Jdqe3IsdE03EGIwul-90o1m9TH_FHArHyjZ1aNljei6-awmE7VRXCcNriJpdh_4oWE0TkJzYLr34SYBqd7QOvjNuwn1MFmVcm3Pt5TeuNZ8Yhb_TUxJX8zlGI_IDKZysDYDrtTb5wKV7frHqV9nyJ4s2hA2KtUtsKAifwBeibNG4KB4oSJ2LNSbspN0dHyicjr9ITE2qA75XIEzMCPluq5BgaZ3uPsPIh2Maykw6vir06XSlR-dJQx9qBbsQg4LnVuRnWwd69JcVKanxC8jK-pSzkFiAsMMOKaInGFNooRexOFd6h65VlakeehFOx7yCM88gTxv5nGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPzjy9ojVv73D-MnasRAXKyE9gOuFrRvHOvsOXzFwG8VtM-CQckPd7LPrTzb_JMweAXuivv2yon8RYMvz9f5tXDzJlxkXnBm768xvTlw44P50BmSxxZLSq1nW4EZqYJTi8cPiwnRTSaa4YtLVAlv4O3uGmTt1rfGBXVyiTh-2Mjh59PbGMEGpYCcXr12l-zg-ZZ2oVne1aCK3wiCDFWllfGjls_592P0yWU1gfGwFlqai4GnBq40kyugKhuLSrfH3xNMroyi5Xues7qh6hey6ulasMHqo5T3_ErcJ65eqoWbtK8Ja_8CrDcJ6QDZ0CdPdUqDYNLTkpqpIQCFB5vAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFGmyOZytynVTqdwC5xivq_5NVmDtOdInwJWKqPhHXu12SFO3fsfMxL7cRrFpXjban9vWdigEPEYpL9jHIe-VDhU7OmMfuNgB8WNKI2KvyPsqCFf83umKl3LlxxyMss0kg81gIf6micN_q4Gre7TS5O2rhlew-cDhbVdHiR1e1RSTplowKkZs2nHW9qG7C_MBgCmb_sjZqUyrDfN0SFY3toZ_GACVDtpgxEx6BP8keHPCdBd_MFSjFSEwC6rTWkjSIQkJdisp81FolO8znDr3ILoBfkdxwzgKNovhLWws_58ExiJQdTk3Q-Qn4ijUUivzPD4J0ovR0FiTKwxIO6Fgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxOKAw8_-zxFvbSfr19KyDmKaGkBNR5l2dNYZwDc9l511vqfvXz9fsVF5o9-hpBhFEsTr3_zMCx_8kB3zLiL5p0xD04gpnVk90oDuG6VmFJ5IIg6pjmew_T0TyKWbg_uRZWT-ElcmDpjxYlhSuUszS70UZVJVTMer6wHyHxuk1bPvRJ84fxftGhJ6spuf1N7an8B84eJSzZRpvnD94uYJVz9TqOqacD5WW7FT318H8Nh80raCdH07zjX4vb_BniVV5mu1Vhfd7tXBzinmgQdxL1apvDXN6oL7y0rfUAnTJr79_6AsK_s6fBBImV3ku_dPeAy4MagZLDMDPI8yXfXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIjZw6LqBYDeXXGqDr-bGXQfaxFkjcRuyrVU6lY_X5o9FYjLObL2lUq6CTjucL3IrGXhm89fsBidAjCe3mMgYihms-TY-l-H5fqylF68rZeZhd_whb5ebMLpPxsz-4R9fVk0kEa7jnxmzHZYUO9Vn3L84nXsD_rO7XhQPZJcAE1juAY5udod5gPJ6QOAB_TjXk7-c3Z2CkwVT26LKMzftTxQoxzE7u5EnvfkIagRX1tJLY72G1F4G_4TrXWgTKxtIbvww0nLQyMGcNt6KA5CcovV4N8iRU5XRBpAYlQa-LCty85INQq7pE2Rji3FHUFOb0RzPKFUHQBD8zBK4UsoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz89y2FUM--6tYARgf5nImK2MoTrwps2CaPnRMeV7bskwWfXd8CItSD6a1OCz_MIVWf2kgIFtxWvMzTANQ1e7W8vhsTaEwT5fV0E57Wr_aD0Zwuvnr5tzd--qYcMy_DYNiQXR1RIlF8Ca-ePrTnTGxOsGblq6ZMQzC3sss-vuCjJE5wEeGdCtiQz3iqPkx86zWvmHVYq6ZnDpydmntOWUqM7nvZfdh5HJus22aDjHEPp96DfvaiemcTXTsNSxx434YUAGLbtXtHTU2ehvBo4hFQbj3BFJoj9rwKAb3uVZfxaAQpd0cvfKhe9WHGDHzo9AskseDIg2s0HYNcyqV4YzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWc3kWzMsQ_IF7y7k_01RU1Aiwl35lXFhJF_uWHIir8b4NrrnHUl7FxB3Uy5Ky_nzXtyJadQte-scm99nF0Q-Rz2IW654PcZG2wEeA4xxJbTLtbUEwOEe_CbM2U2in7jP5SCs8TugiJ88O0zGnJddIHRJg_XzGkk8cR-trdnzwtVmN1lJistKIUbtDglbH6dyZMmPNPscYr6TA4bgPW77aCEFt180kBfzc9BDFgeVggIedLal-K-ID6zrbmiwe8302kH8SPfgUjYRvULBhAvbrEd7I5ht9e4h8tt3sTljUGp3o8L43tUJe_AXz24R5ZdvhmVF3BuVOOtt34pQRdI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzEqmd-PO6ozr1lnfRD8979M939QIw7GhPwN3vzjp389A9OZIhucYC_9Zoj9fv-H_Iyt2eif9RZUonvo8sP20IdhibSPtlY_5XBV5dJkIxmXMAY09osusNYzeEUY51oy42cMSQ2wr_tYEwpX6UBWyXj0ktePNIOohcMm5oI_XdGA-ynWBjEDgJhmtcPZ9d5AFusWnwAezExHnyELAfcN7Yt-qGlJonye4dkIEZkyXVna9W7o_NK-7bkJDUTw8yxAK2plZ2YJ7ecWfDQEWJGbubwLBZe2JN-VQKiNH_h4uSpDrQw1vD_52bzodmaD58eSDNkJ-LnQM_BtGnkphNx-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq1C360-_otuZODfN4vO6ql3ERC3LOIiK7yy9OXdtGWhrl7mhDlz8kjed_LCtzsBtHrzM1AYIVeNDLVV9uYfZPYrSHpjvRTK0RMwxTw9HQE-pNRgp_aIwlXT9Y8QFZuvjen066vjiExSt5MCABYzxcKFd-ZJ2X3M23nKmBer-eDRSsfghxmyCm-bMC1dpaMNiNvX3AXPKN-wCv3CLSy9jf5wNg0Th2njM64AVtwQrpXWpMguedrpLDj-X5MswE5X_Vbx7ZYW-CUcjJqLvp5FDcBb2XxKA5lzQbDgKdSt6fNfHpgHNKDfGu1SpLLRrTBo73DoNfAvsjjuA3lojX1lLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=DNoIwhJCSSObN20hUshs3hljK7sDkEAtgw4rlS5idEFjJnC8C9A1zBdJGKcVLfJP-4w0ENPqdToPpnT9RfyAiTs6zdAiDZ0VtYNttc4aqufMJtqJ6css56uYjJX8xh2DT7I7kH2gy3wUFLwriHCgJ-WQzBVldMcanKmx2hB1pjYkz_tJW9D2nbjyuk6u_wJx7--Yp-yb8N2kOm0I7sjlufKwOgG8olSLirGT9pjV9Ao1yNenbHtKyk-LmEb3MjKenI-VqtUQiWEm-p84Lw3V-QbV3Dczlhr4w0S6zx5hKQc52YVqYrtghdHNNxAPeghPRrIG2iaUyoaIsWr499mn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=DNoIwhJCSSObN20hUshs3hljK7sDkEAtgw4rlS5idEFjJnC8C9A1zBdJGKcVLfJP-4w0ENPqdToPpnT9RfyAiTs6zdAiDZ0VtYNttc4aqufMJtqJ6css56uYjJX8xh2DT7I7kH2gy3wUFLwriHCgJ-WQzBVldMcanKmx2hB1pjYkz_tJW9D2nbjyuk6u_wJx7--Yp-yb8N2kOm0I7sjlufKwOgG8olSLirGT9pjV9Ao1yNenbHtKyk-LmEb3MjKenI-VqtUQiWEm-p84Lw3V-QbV3Dczlhr4w0S6zx5hKQc52YVqYrtghdHNNxAPeghPRrIG2iaUyoaIsWr499mn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSwvwejE4-UtiuU-E1KFMQC_6xiujigMLssgbO-vzKCUnNCm9DqDpXLZimrrW5hDdLZnzTk_rv7yropKcQFPKF3062OLSdXi5tS-Z8yWi6TLwu6CJqgPziFcbuIELPjxdpo8DNdivjQiP5G0csYUFme8S7BOL9NfZqADvSPG8IbW4hdcFcpVJx3mzZe4dyFABcRorJtdZTTHgJmHkCmN_Vlfk0gFRliKJt3Qe40_uvdZfvtiSWSKK0VUoUgBXNz1fppthNK99H9vnbDbX0cxw5PlDtO1QdRa8muORgqi3Ied-0kU8n9FwCqQ44GXE3XfHTQ1TJG0YEpBXfpz89rv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKoX24zFjDK4CGmWje-jqP7bMODrmG3XnIdiGl659TIPUbFjMuA828GKFSytsOSQfVbqkU5Ww07NrjOruLr-6L3gKW77PeBj8qN0sdcr4Pv3_nzoRcQJltaWZIEyYSZpoGyY4rnbPjJE2o_mjD6Mn_3oi5vEFsKrWQreGq_HI6F02vG14vvxPbmyWhUwdtC_1ShFSyMuErR-W0uz8rmTQPi_SHksnqcfqfOUmC97ljMbtYqJhXJ16QJpvnzto_Ti9pgw15f9Y8oL0-v4iXeBS_RMRS-iqZQivD5a8TQc5AUu1bAYmm2LSgq1spB4jGVyf_SYUIxFSFc0e5QEUuaSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=tDU3_XSXtLMYGEi-lrfBOXeteittKAWOLDe1-WESVusKE39f-fotdi--0urLvPzyVc0ZsP-UVTFriAFA-mb7aV9Sqn2tmSEyflkxq4KKJXUm5yBDZs6pZDfKr72syjU-YD-zUTkmKNNkklb9SwUXgU9Myn-79OK7mTxRPDKI0AwgFKTC3Kl2fwhASZ2MRWmcb6oGf5QwSi_3lJlc7wpbXfhUWh7dEQcS5mnfLUv_JjMJUOOo_u9fjx2NP9141uBwtQ-jEyPkZj7JqJE3BSiY5xS_qGB7-F3nOKRvtKSgwT9oScw6XoIKv9FN_SBRdqRumHQuWuxVXP5fTXvIZzagqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=tDU3_XSXtLMYGEi-lrfBOXeteittKAWOLDe1-WESVusKE39f-fotdi--0urLvPzyVc0ZsP-UVTFriAFA-mb7aV9Sqn2tmSEyflkxq4KKJXUm5yBDZs6pZDfKr72syjU-YD-zUTkmKNNkklb9SwUXgU9Myn-79OK7mTxRPDKI0AwgFKTC3Kl2fwhASZ2MRWmcb6oGf5QwSi_3lJlc7wpbXfhUWh7dEQcS5mnfLUv_JjMJUOOo_u9fjx2NP9141uBwtQ-jEyPkZj7JqJE3BSiY5xS_qGB7-F3nOKRvtKSgwT9oScw6XoIKv9FN_SBRdqRumHQuWuxVXP5fTXvIZzagqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XV17kWeT0ZW6_AWKPBPUfjQbnmU3c9lYLYN8IsL1zptcrHKdrZ3JkbNexcgEmOFJwOoOYZeLzhvMO7WFHIVrEmjFeoOgqelfU9yOFeTm2Abpa7e9EN4uKQrYQuQxiD-50Kqe2geIGS1uXSm3R1_zT4Oit58tf9FF_mZUJsTizHN_BlGkD2fJyJJ5mrxC8g7as_M6emVTeSVLtYCI4Zg30GL7Q4Yc-QK0bX0vdT_As2oRJEgxi3X4v-8_Z4pbg3w7EBykCMCYWFlkIPf782NEovuf0g8mY4u6_8JghYIo8S35XAUvMTTvdfaYUryDVbuNj873YLBjS7f2ytX1JW8qCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=XV17kWeT0ZW6_AWKPBPUfjQbnmU3c9lYLYN8IsL1zptcrHKdrZ3JkbNexcgEmOFJwOoOYZeLzhvMO7WFHIVrEmjFeoOgqelfU9yOFeTm2Abpa7e9EN4uKQrYQuQxiD-50Kqe2geIGS1uXSm3R1_zT4Oit58tf9FF_mZUJsTizHN_BlGkD2fJyJJ5mrxC8g7as_M6emVTeSVLtYCI4Zg30GL7Q4Yc-QK0bX0vdT_As2oRJEgxi3X4v-8_Z4pbg3w7EBykCMCYWFlkIPf782NEovuf0g8mY4u6_8JghYIo8S35XAUvMTTvdfaYUryDVbuNj873YLBjS7f2ytX1JW8qCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaOovsZ2g8XoMG45fONjsyYWXOHXjD_9esM3vzwh8I3rKePT3MB5IoBt9KPffW75kaZ0v9_zazSkaxcx1c9XfLfOnZKYxXG64cradQ1PRohSEhLELqnWROUXfMPYzKpBZAQO9N8Q0Fn7_nWKZp4lFKcHqtHJ9grfRPqHLpZ57mzOCvywPJKR5mlbqKAQlR4ZZRrVOJiRbXOIoprMe2Pk74ITpM_xBhruDrmqidkXrBMHBkJYLaHBBJ3c6vJHc3KX07CZplOjGHLAIQFJjzX2EewIuZVsgqo4XsRv1Lt-jhysAZ_cPCb0-ptpfIB9H3pecrjjrX-zkX42M4zJwbsfZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiEr2v56QduHW99hbR4e0OWHNUkdFKCkAEmgCg4ghOa3QhRRfGzWpQ4c_lpXyeAVMaO6drbuWwHPxCEOJKrAFQypNKcP4nXxzWOyZTVN5ViMO9S4rZnWfApIy0z0lRLFDE2rjWPmUerM2bebow23hGzdepgQBrgWd5z2R8iv6CGOrwaz6HFBITin05BoOlqIHlqD4Acb4cG3Jyj4vZuKV2QPnWCaR_pKVZyz_WGgDDKZMw1vacIymRxJllmLDiM20dwTzULtTIflAPxx7wcwNMEt7JyFxhIK8DACMq1X-KmJwGhiS7vU378o5CbjeFBiticPCP4hA1_O57LdvX6bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDDfj4aLLugWXAcxlPxYdD-pMCHMBSJRfnS6ao-5QuEbybbYaiBj0hMQMvwHqsF8IIT5ElST2ccA2ItH-W_dKGrXwXkVsOyywHmxpecRcSzBTqNqqv5TEriQS2Pri7D7KPBVQzSepge_5t5bjZIOAbIFK90_Cg0Muhib3V2l9LQFjT93NDNPbvV13JOLpzZPBb9dCMUiKqNYED07L3gDJqwSbRzjd-ZnB1b56okh7QsNE0HiAiLXHrUVUbRB8DErfp-n1U-wfniJYYZM8ysyZ_rFER-wIcUrgAgdyNpCOE4-HcPFN17fnSghpZSBJ9vEutcx9IX-qsbOAxbs3TZJpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9GX9HNqzQKyXdy6ttrmBX7SRVsFKVjLRVHmk5x_XxwSo0JLzVJcxVdu2HJZjatu9Hls7kWNlHz6NZXTzfHVo-e2REcfLQTgL6RH5Y3Qv0smXTNVe7wF-EcTGc-Fh2IZeexf-pWG8tSHRiwXZ-EK92rZmMkBY1fviqDft4XlpVL0GGDT2bNdlkBKksYd5YFvG8_0HfT8UtWqn-RJBUMDIKKoeinHFs51YwvzeWGjKfZ6yjGxXG7Xgy37zYeYDIbHdrG_L2GK-NUttqUGX-FR2IVETOx0CLITIm2ThlgE-0C5nrDz5aIsV--YyMuyPtoXMUqY_Vx-fIsQAR5ycDcLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awtXg65I64CeeRNCVLni44MPL1MuSbsHeSFANLu7ZMPzvYuFH7vU3VoygDfHUZx8ttVmliQt2nk9GbueHFy2SJ6_Rm2FvXYBpZ_nqDxk95aZC6e2Q3-CGaFh9hrv6US5BxUVPbUPXJEsx_jiJJOLcpszBrx3zk4Xw59b0b5SUs1FFpJ5l27YiDAawF5U93wArYdCb-T_dwh6GFIva3o57IT_idOHcwz-nsQ-ti3qozzCQRSyCe6wsuabFwBBJ3ZTUBSlIGfxmc6NR40iJmmsgYp1QF9FEgeqhtCOQ0Sn02pR_rJtp4LPMhhe2DtXpj9ik_ks52WSeMad5yNsp_xnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFDBRXra7XDdFwZpoEh4A8DSllGT5Bx6B4emORUzHb72dAEPJBeODcgdPnHhIma7F4RPpiA18iNxQv1ZBB3DQgfNt0VIVGPpR-sMT5SItmgIAv7CzmgN71MAr9I-O3RvVR9vIMdnuWaX5uCFQDWrodJAxjw8reiOnbQ-RvNRsB4TZx_y1ACk_FGUBtDUawca3ypxo4UgVc6-VekFSBciCpAdSsLKjtyf9qzM0w67ljaiD1kICrTJzRd81Z35myPHjAMHasryfADmRYO6yoZOA5feJ_QnelP8l9pycoYUigvOLYqVBmFZ-wn6thqLH6M3jUQyXhfqvtBoef56zUM7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOGn-h9l3dzh_w0cGr3jaUSR7V052T6JzcCbGMJL_DT2cXIEq_BK7NnnDxYvNY-y9QE-zzOm5JVHhpW5fYzAwZ4wjRs4LViZF4y9cHsDuXNqbjY_YOIQ0EtNKFAjtQkgSebg9a2V3iJAnBEK_DVJOnTD_N1mo9C4gtH4W15RRegVyuQZZHxJyMAnrQXZ9WFI8INs_8FEtfg325MwOGq7b5OGKy29tS7abyexKqJ9telWk4t4FqRTgDblXijJ2mEUcNcc5hSsY6AU6lgB6fFoesXLrdrXxWzkcfRy0zEwroPovE5jyBwaa-dQmfuY38ppaTxaYRRODBFgta4RZTmQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=dxWmMFqGFhSXVIslPNFUz9yPGBIRwbmfBsQnbdrXv9JgxMChBKTgL2DRzf4U0_ofO1-kkOIJP-jPZP-8Wi-z-AO_bddCzk9nVvOSwjI-p6FBLSKcLMhyB39OKG79WOfWV7tuHLyvDGiN7IFwMyxWTwmAtxzOsloGrljGT75MYe6hStRBxfRMCXuFgcck6n5HbYMYLT87-NfCBppHMOBzuZnn9Mu528XQd6KZOXZmkUW_DtKdBIun-DEAkCl6Jg4Lpei-iotUEczytL16DhUzXcqsiBtr55c3wf_SV4I4yc8YL9qYWw1WcZ1aPI1MAqWdd3ZyBzPdh9Tnkdx3LZhreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=dxWmMFqGFhSXVIslPNFUz9yPGBIRwbmfBsQnbdrXv9JgxMChBKTgL2DRzf4U0_ofO1-kkOIJP-jPZP-8Wi-z-AO_bddCzk9nVvOSwjI-p6FBLSKcLMhyB39OKG79WOfWV7tuHLyvDGiN7IFwMyxWTwmAtxzOsloGrljGT75MYe6hStRBxfRMCXuFgcck6n5HbYMYLT87-NfCBppHMOBzuZnn9Mu528XQd6KZOXZmkUW_DtKdBIun-DEAkCl6Jg4Lpei-iotUEczytL16DhUzXcqsiBtr55c3wf_SV4I4yc8YL9qYWw1WcZ1aPI1MAqWdd3ZyBzPdh9Tnkdx3LZhreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZs1HUa4lU-T1UtZmfNcf57KX2m5W7Oz26hWWjD3i6cr6W2XZ7SjjlXeGlFlVWpop4aAmsTtFxuzVrSQCL3SviIP8Zt8bRzXoJo480aXmwDRrafELLLopEvMDli_So9JTlO9vSByL7w3mUcSQKsYOyStJgK7y2QcH05kVLCniPZNqANRG_D394YqHmFxyK76uH0ss_6QXm7ZzswU6w70Rq9oXXa7p1KcsueNDu5LnbdBFyg8X1JSBNpgZ3VZk05kzNrj7A8ndYhkYNX9bNTvN7PYPSbnCg-nDyX-41RcpS81JI6W7ZRR1wFO2rGtiHk-sScnvzBhEG1mCfVgHvir8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
