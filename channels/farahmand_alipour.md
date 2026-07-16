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
<img src="https://cdn4.telesco.pe/file/Rp27jzV72hWWizsDsMax-MGd50NM72riWgCjv3Hue88xCXPacDhnMCocxbdHieFDN80f6--psAetYdvpm6r4APhJxAvjM030zflx3Vt4sT0ahLVcilkTmjccv7Q4o7rkUKNd46XKK_atiVKdIoq4gVoV3W07sZOhSWlBTG3uv-AUCWN1IJU0mRtLuuCvMw5kMA-euGZycbivY9TxzTulx0xQF0XSzGK5sU7icydYKTguJ75oBNCHV4ex0rFVs6ILiomZiXokepHVC1L8HTLCLRs9kkTjkVrlDD4ogW7q-D3WJUjiZ1ZOIBjg45pobii0Es-FX2PKH1qIq8juSjcEog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 00:59:52</div>
<hr>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocUvZInmXSgxOFR_PkkilUcR6lyDAdV74ZT8NWKgyv1oIgBPLnO_rDXZkuKDAxp4IFbybmmZj22RdK5ILR-kfn97u2bAGkbDZ1RcjdrjgVsMu4mb1eC9Y8_sctIdIhKeDUJdBiEV26gvb0eGq0E5VM1a8jE05TFg-zm4bhFH8F0VtD_fvtQVEZa0A6Fwx0KH8QkXtpbheu3-bZtskLP8O4SJnqgJfZH27xXhOFIDd9YtOCpNHfuEw8cE9J9c5qnFjpAF8S_Iu-HB7VRQoZPQ_0fV_Hx6PpXSTEhGZTnFMcWWRNWNizB18L5VMJ86wZqPPRfOlenrWrUI3w0mESdJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=NKK1Xe3lAdnamy8oGjt7Af4xYh-a2Oj9jDiXQbMSoM_4wMA6jhTxCqJhzeuDqdUq55-rQ4xAbb3-rNIGr6dzxvCIdxNuigjF30xv1d6h1oAp5lyAKefSHb2HHplAkbP7cA6IHpr6TEQdR7NNREw13KpjGWiJkdUDsqMmZ80mso7Y0n4SW6NNSTC0K3beVJWAkFIG_QyPJkhMn1VJiT0Nc_6YSM7cDTfchhFSPXyZYX4UtGtlj5r0_KnsSAOPRAR4rh_PaZU5CN9o-K0Ys1y-L_oR9YzOTKgBnjVZB4X5zlaHHAIHAuxd57L2ntv53JtdaGlCEpyS-HPG-V_FYrKpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=NKK1Xe3lAdnamy8oGjt7Af4xYh-a2Oj9jDiXQbMSoM_4wMA6jhTxCqJhzeuDqdUq55-rQ4xAbb3-rNIGr6dzxvCIdxNuigjF30xv1d6h1oAp5lyAKefSHb2HHplAkbP7cA6IHpr6TEQdR7NNREw13KpjGWiJkdUDsqMmZ80mso7Y0n4SW6NNSTC0K3beVJWAkFIG_QyPJkhMn1VJiT0Nc_6YSM7cDTfchhFSPXyZYX4UtGtlj5r0_KnsSAOPRAR4rh_PaZU5CN9o-K0Ys1y-L_oR9YzOTKgBnjVZB4X5zlaHHAIHAuxd57L2ntv53JtdaGlCEpyS-HPG-V_FYrKpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R65LOgLpyFV6vFlWmI0lL_yc5ZetsI_cxqJMCsa3t8KYZIS8nYIIwI2CYdn75MFgnmX53MZQr3PxqeKQOuzQjC1EID4WuQl9Qh0-XEtV-q093tmVC-ejSUJnE_Hrzy2Tl5rLyBtdDELpHyctMTNuI3eKkPT_rCy6Q56odLYDwKmTwy6Iy7AoXLsBGn4r7TtoUieKr5hhb-2uUegYb_TUeThZNLcmyh-RGXoobBQwer_9LYzEVtGukq7GoIyHlikackIeDFdX4KR0tD9NjN2FtbfKnekwTR6OChF3UCj5tUbT4dTin3CYEHbfAb94Xs8T62SC6R9Km5q6gZK47wPbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm8AJMCaok2jXM0UZoi0kXz6-CY-cagVF5WN74EWdJgARZVsORbmI7qoWgwDxYBN3iTnghMRdckxCTTrF-V9SHRsFPTfxbK8aTFhsKPQVM4cBp7MtWdCDEEp-nwmI0elpIVC1JiHHYh_nFprrYAbze1i8cLljPp0e3WEWHk-A3BDXVV8T9FaHDsaSa6ncy4VkdifjMfpBOSEoFcvXLUHf0WREnNpa3nVrwB_5cuFv75AAZr4zDYGHjgtyfYaFoU02pLpF_mFIhw1evfVj4cI5ZbxtR4LrApAJFx93BlQGfo9B6ZZyIW9HTd3EmgdAon9ramdpVENs6dkdyLUfmflag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXUkRFveijuExYDT-F44dpCj1c7iEALqZUHTxX_TB-kf8Wies39wNuYaosZS765di6SlOEoFboYntKdnF_bSi4bgopC8f-h9x4v5PhZe6HeFdAVxeJ5ZKJA1eCOF45pt_YpiDAIZRxPBnvEaTKCM2MFgh09HrELcJ4pgaTq-lHdNw56-U5JZsLb0c52Cj8400sGXsMLTjjMyg43iGwBbnZg29CmWymbYcJElQPgnqwe1VY0Ix11MXAh9CgkKLxcIBD20OTjkE6F6h_giBJW8cep2aRxO_3DvMF214NwIChcmNnHynhcrFnjL8oakMopoxMGWDc-bxbs7d1mZBFfQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIQn6KSSRRFJkOW-EpsOWM7j6G8B00NbE2B5B3gok0K-1X2QL_8AhGFUF4uEfWD4PfKJbk4tv4iXiqFFqxL6c3sinrSzodkYKPq4jv_G_KaMeVIW5KqNSpJCiiGoeBxoPjB4ajuK5vSz03XDZvij-UBLW5MuaiSZYCBvImEt78OiuuRptZwb16Jrets5w_hUO_LMFO6HE0t6t8XSn1HjU62tJso2krc2BKfKX6fkMp4FNXj19pDHIqHSIuJ-ICJ7iBtNPwabOr6ZWTtFK8mxqx4aJdXEakIXf53IdJliUCFJRpzM4eqc4Xy0BdHNYc9aQEwCZ9_eZ_CTjlByrrg6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=cdd4A_MSWPDa8rrDkx9yfRGO3wEecF-QppF8ZNUzE9tMb2qfaEZlLwKecQCFSLQqVtfR36wmI1sgY6GEZ8P-Vufi1z8dTjt40Pf-8wy5ll6woscO913FpjC5qhCMDNnEyfRg_ulScJ2_ylrszmrpLCzAuS8TTHbuxB_FaTHYf6gvle1Pzi5WHJ1QmJjBjp2zu1SB7aBvcXGwBWNbpb7h7uyea3-FQeZBLCaRNjlPTFVFvKF_QVLbcBgb7U5sLiNRfBV-nsLgleNHcyTdniz1ioLgjZpOp-B3tOQ1EqEA-GjghMYlVfExYsBOcNJfZAbYeAa7vX7kxVgbzvV0lGxyhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=cdd4A_MSWPDa8rrDkx9yfRGO3wEecF-QppF8ZNUzE9tMb2qfaEZlLwKecQCFSLQqVtfR36wmI1sgY6GEZ8P-Vufi1z8dTjt40Pf-8wy5ll6woscO913FpjC5qhCMDNnEyfRg_ulScJ2_ylrszmrpLCzAuS8TTHbuxB_FaTHYf6gvle1Pzi5WHJ1QmJjBjp2zu1SB7aBvcXGwBWNbpb7h7uyea3-FQeZBLCaRNjlPTFVFvKF_QVLbcBgb7U5sLiNRfBV-nsLgleNHcyTdniz1ioLgjZpOp-B3tOQ1EqEA-GjghMYlVfExYsBOcNJfZAbYeAa7vX7kxVgbzvV0lGxyhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=iZAcRGEXMeurgVK9kOUHSW1RqnLMbpLXxRReDW6nXsiChaxSXPZhRJ3NZhqLKydOAesLGvFWqbML1lE_GulXrotOszIbEd0XmkiTARb_pH9Yci3ulGnkW_nLtKwG0lTQTMJBxjLLT3umY8ic2Dlm4sieT6EnwiI02A8KWSymkwtG55Jy2FQnfoHNOIRqbtXYG3o5QP7iUCYxwuT34T8NJjRixqdD7TxtnOutPvNWNnWRFv-x8y2i0sTt5PcfaptKIzJnvrBfJGbxBvpIV0G6MvvJAdA3dg2TvqCXNhpZP_aCejLT3xDxRfTF_03vG0UjvwCHDrh8JlwZFdVqKBJwqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=iZAcRGEXMeurgVK9kOUHSW1RqnLMbpLXxRReDW6nXsiChaxSXPZhRJ3NZhqLKydOAesLGvFWqbML1lE_GulXrotOszIbEd0XmkiTARb_pH9Yci3ulGnkW_nLtKwG0lTQTMJBxjLLT3umY8ic2Dlm4sieT6EnwiI02A8KWSymkwtG55Jy2FQnfoHNOIRqbtXYG3o5QP7iUCYxwuT34T8NJjRixqdD7TxtnOutPvNWNnWRFv-x8y2i0sTt5PcfaptKIzJnvrBfJGbxBvpIV0G6MvvJAdA3dg2TvqCXNhpZP_aCejLT3xDxRfTF_03vG0UjvwCHDrh8JlwZFdVqKBJwqoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgmZvbxvR3tKv-CCm3S3q8GSTCHxAZC7qncux9acpKzXYpwl58epWZR9fDjtLsAgaBBgIegITRpjYiFeisZiK2vRtOgkpfTL2-z6_hFPmdkblwX_caIxXwxa9fi1Pw12OucM2nBHWWKiUvW075q57NDK-KmUmDg9EVak4Rud-Zi-Ak2PgVhEMqmjHLBgDH017SxQMdhcDgDZUm2j66wfyL8zIT9eR4_STiKDt5l6RV4Ga7ZiWq1kazUZLjrIQcnWLTltrD8T6QoNzb7zCl7s4lWlboDRbv2_4YEm4HmHpZoLKKGNoEQV_Q0wJJsHYtfNKRFOzZROBs3L-Q6KUQ1dPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lluidip6uvwQe4X7GnxlFdW9h_LZcd4mVowDze1RrpPG-rzDTHYeoIsmPjC7lpjZGhENQ6N0DHYl4Kv_NR-IMknlKhCuAMJonnovzqFVpnz4eheO8IXxVOiQyEgpnfJx0ZXsSHS3iW8KtGlJHOvbeVLV_BzwNXJfIiQIiPQ_3zYOfCqV-Yef7NYuKKfwbR5mgy0_R2r8V4NswtUaOl2j4GgqJkqoWRKDQK1fSsQOqd8zStfdCrp_v0831x-QxpQZqbzl115USL5sM8g4MByFdDen11pDYuu9cknIuVkwNVMBPjXvlWnFJUJrw7QDeoQXQHadbRo7DCIkdf_Lc5YQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=T5P0jQS7LwnCxFY_mHX6w1qEj3rWtoRIsJe90HA2Mvp4CF8mmPQzrnxbeyWud3dJK4kLYmkE1lNelvPXr72ivRbccumClttmzo6v43t9sUD07LGxLF_Y3IwntNWAv6Da1ZHd-Ox2TKPRZA3VsE26mR1ej5XSO5sDHFkSwVw7THeAwJAOTrr5UPPYiR-tHuFXociOuZrODCwkegO_XyswG4eLNTgB7IbItWdvdkGK1poCkJ1bS75zN-sZXrQPCTwr57Yw34IZ5HBsfgeJCR_Zqvb2Ygo-XUKydeUGoqv80E9PHI_cB0PSFBZS80sGipTeIXjJKMRQgE5KojrUye8OfKkZ0kCxscHm7zu1wQoa4F-MYF6kIijoNAjUYzewboUrpI2g58cFyCyMlGB3TM5zPECXZzK0-jBOnLRMfRtl6XmuBdG4df-xNHTX5We2dl_BsnZQMdI_kMnXksMi7BRPWjSpRk3dIUYk7H9AClfee71AsjJYyi6KdMMZZXJctS0Qew70U4oI__pwIWKkV0_1PeAE3L4xOXzqbMTJ36-22MtMT_VtO7SSWBIJZyO1DmLMR4qxcWRY7XvUtdf5VJnDBIgQgTQqLQqn7BTdBWKutxSGHUbi7U97kryYJqjNt8ZiQEWcrni0ZrSDHX2_bfb_1fqwn8kuNlmN7nKZvEHvgmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=T5P0jQS7LwnCxFY_mHX6w1qEj3rWtoRIsJe90HA2Mvp4CF8mmPQzrnxbeyWud3dJK4kLYmkE1lNelvPXr72ivRbccumClttmzo6v43t9sUD07LGxLF_Y3IwntNWAv6Da1ZHd-Ox2TKPRZA3VsE26mR1ej5XSO5sDHFkSwVw7THeAwJAOTrr5UPPYiR-tHuFXociOuZrODCwkegO_XyswG4eLNTgB7IbItWdvdkGK1poCkJ1bS75zN-sZXrQPCTwr57Yw34IZ5HBsfgeJCR_Zqvb2Ygo-XUKydeUGoqv80E9PHI_cB0PSFBZS80sGipTeIXjJKMRQgE5KojrUye8OfKkZ0kCxscHm7zu1wQoa4F-MYF6kIijoNAjUYzewboUrpI2g58cFyCyMlGB3TM5zPECXZzK0-jBOnLRMfRtl6XmuBdG4df-xNHTX5We2dl_BsnZQMdI_kMnXksMi7BRPWjSpRk3dIUYk7H9AClfee71AsjJYyi6KdMMZZXJctS0Qew70U4oI__pwIWKkV0_1PeAE3L4xOXzqbMTJ36-22MtMT_VtO7SSWBIJZyO1DmLMR4qxcWRY7XvUtdf5VJnDBIgQgTQqLQqn7BTdBWKutxSGHUbi7U97kryYJqjNt8ZiQEWcrni0ZrSDHX2_bfb_1fqwn8kuNlmN7nKZvEHvgmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e58WIXnmjxc5wxRKMZKl65KyMFBYslITT7and9PAJ9eE3aFi8V_WMxYVji2aSLtIjWNTtoxDTtnVv9L-ZCcuxzYXB2a25c-mFWwRpoHeIfcVXJP19a3eGK6cw3maLSPde7mABt6tCUe3QTDV7mVgFLHGvHX2RO2AdbPCjAU-tIz7rPPagwFuK5D7T3dGPkb-arWGDiVP4NdNCpP_wztwijWghXQ_0nD7nir2fI4EwqbrMcPxlydW7fWM8bnJdu5EpGUEXS04j847iIG5I-V5IqUJXdZCdjDQhxcNV9h7e3NEQkfLwlYeHzTWwlKn0Wc9gOxx3nBKfLV4f5q4p8o8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlSZnQNYQ9gbE6XBrr6zxSyHa3D_1xt0UlZIzkm3J-EKqm1k8HmiNdGsmtf8cm-Bsrh2WDIYLGSZfO7ugD1lKU6-pVm8moeiYwpcxheigqN5GJYNCibpRPlsgsC7EaNWqA0Jt2rfGsMkSxEOrE-LoLaUmspvhiwel5OugW__lDYKAn3GcmC0PjJRYUOPfZ5tet4lY7q7LG1599yp9mrbINyBDnkQPwT2FNWodNMAdfANZTwssC7Uhvqryd7sa-CXGRULpfHS24pLLMEUAI8HVOxqUvCKkHwlXV0Utx6zNePl-t3ogyOiqk_VBr2k6HOmjgwpn7IOdyVQjXqBYDrmJHDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlSZnQNYQ9gbE6XBrr6zxSyHa3D_1xt0UlZIzkm3J-EKqm1k8HmiNdGsmtf8cm-Bsrh2WDIYLGSZfO7ugD1lKU6-pVm8moeiYwpcxheigqN5GJYNCibpRPlsgsC7EaNWqA0Jt2rfGsMkSxEOrE-LoLaUmspvhiwel5OugW__lDYKAn3GcmC0PjJRYUOPfZ5tet4lY7q7LG1599yp9mrbINyBDnkQPwT2FNWodNMAdfANZTwssC7Uhvqryd7sa-CXGRULpfHS24pLLMEUAI8HVOxqUvCKkHwlXV0Utx6zNePl-t3ogyOiqk_VBr2k6HOmjgwpn7IOdyVQjXqBYDrmJHDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=Q1VwJa28kpqZje-EGXKPrtT3JiyszTM1Uz6fVIYkhmUxF-MuXHIwvqg_wjoMgicjovZ2SJK3e5skHemJK_GEvUD_Ah6bciPvdtGGpEULlJkMksD2U6Oyhxun-QXRkr3Z5A6411Vn-pezMa4Y50QrVooPEGM3XKpsH0VDn0s0NyPLBnAxMLmNlasrCdgXtmVshyKxeidim8Teyv8Qo9wuc3-W4sXNgPUWz7OW8W6Z6XAMuY7rpVDDJs9INcN_0_nnBBxoel6jQcMHm5Ls4RokgExmJjMy6yY_U05cZQN5fhqUDQXSXnofJ5fHG5R3pX8LS9OScsPhcpeFcFDHIv25vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=Q1VwJa28kpqZje-EGXKPrtT3JiyszTM1Uz6fVIYkhmUxF-MuXHIwvqg_wjoMgicjovZ2SJK3e5skHemJK_GEvUD_Ah6bciPvdtGGpEULlJkMksD2U6Oyhxun-QXRkr3Z5A6411Vn-pezMa4Y50QrVooPEGM3XKpsH0VDn0s0NyPLBnAxMLmNlasrCdgXtmVshyKxeidim8Teyv8Qo9wuc3-W4sXNgPUWz7OW8W6Z6XAMuY7rpVDDJs9INcN_0_nnBBxoel6jQcMHm5Ls4RokgExmJjMy6yY_U05cZQN5fhqUDQXSXnofJ5fHG5R3pX8LS9OScsPhcpeFcFDHIv25vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=HPpVIU_jMgumYweRunOKTnlUJ2_W4GvdutIq32rWGwXS6JC_SkkmRl9OqCBMDCfgemaF39dP5Cf9_16DiObNzJY071QwK-EVYXXLtN9kQPWMgBhClSKIdvENkHBlOv_0-oFmcIF9EXIH9FsklZ5zZElRcC0cQH8uh6atYR3RHXQnJXp-DIL5mUDg9KwdN5_onD1rUZERVty1jW4nm-aaN01MC2oZxJFP4KLRY62Qc7MjkuX3rfMjj__PLqaIAjno4IWUBMEwoJpsIhbQmMa9o4klj8lXui9cwWdJUWjB2hBYnXhblIL0Siavn0e_jMIrS7EjSsMGDWEgAg_w88wVmXy-sxHc33o7ojCNbz4sumU58igO8AYWXTKPUN0r7zOptzZ5Kr2YNaa2n9uHFe3_UT-2M5vfn37ndLqL1E1WzmbVkGJiJpBen_qoCpUtKjJ2hlpS8VDcKuVj5AoUeiYPoffmPDswA6anZ9llGa23GlN0jp0yyOvpBTStqumTwC-NEAfN86LoZ1MDInPsywy9VvgGncy1JahN0mWjZpa_Peft9zpgUfV3N-LYQPoROrj1h1uzDfzaGXlNHMj7W23djrfbKsj1jSRjNe7cTSG_cGclZ0LtaFdCOASSRyS3Q_ZOa9kFthtfE20JR49v2ZtxYQwC1Hy-s3k67u-8GYnsdm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=HPpVIU_jMgumYweRunOKTnlUJ2_W4GvdutIq32rWGwXS6JC_SkkmRl9OqCBMDCfgemaF39dP5Cf9_16DiObNzJY071QwK-EVYXXLtN9kQPWMgBhClSKIdvENkHBlOv_0-oFmcIF9EXIH9FsklZ5zZElRcC0cQH8uh6atYR3RHXQnJXp-DIL5mUDg9KwdN5_onD1rUZERVty1jW4nm-aaN01MC2oZxJFP4KLRY62Qc7MjkuX3rfMjj__PLqaIAjno4IWUBMEwoJpsIhbQmMa9o4klj8lXui9cwWdJUWjB2hBYnXhblIL0Siavn0e_jMIrS7EjSsMGDWEgAg_w88wVmXy-sxHc33o7ojCNbz4sumU58igO8AYWXTKPUN0r7zOptzZ5Kr2YNaa2n9uHFe3_UT-2M5vfn37ndLqL1E1WzmbVkGJiJpBen_qoCpUtKjJ2hlpS8VDcKuVj5AoUeiYPoffmPDswA6anZ9llGa23GlN0jp0yyOvpBTStqumTwC-NEAfN86LoZ1MDInPsywy9VvgGncy1JahN0mWjZpa_Peft9zpgUfV3N-LYQPoROrj1h1uzDfzaGXlNHMj7W23djrfbKsj1jSRjNe7cTSG_cGclZ0LtaFdCOASSRyS3Q_ZOa9kFthtfE20JR49v2ZtxYQwC1Hy-s3k67u-8GYnsdm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_vWzNZPnLTdFtzLmLmR--1Nl_ydt0gK6OrjF7qBC0Ar192qoqcws71hKnZZE2GriUmOs_uIGdOfKMTdlnE30V5SrUH0sH0fh9EGb8TFejBSQHJZ1KuYmFAmoYvClkpLZCaARIUEnI3KAe228nL-goScbkcVQtBSEMqbITP9KNlAwIgAOQeIPbIy190-IC3ClaJBURIq5vy6-IPvAnsHqj65SBP4hZP6BjCFzrIo542H6lSI9PBe2naKQIwg_ZWLk_wIDH9dt3qAJ8ItaOrnmYUckaBnaWYCDXibOUCCiBVr-PwAetirqMCwZbSfCgqwy5nX33vtxHQ_kt5xpIkCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRZqLFzRBMJz_1j_I5NXMEK47OXYF9PeTqrOcWopHoaESNOMqkexgauua-lH6MDt0xt2xYj5JKz3kDdSY667oReEHAB6gH6_zfz-B2ToK3C1w8dG4_EKaUdPYH1g_prgu1e3I2kzqYPJY39q7n67xFwijpgOZHN6jCYfP5nND_ImKXX6zI2hA-pgi9cLOi2uiJZr9KEixMo4dSUTgsXcFvRnr-duPyptIAV9dwRfbSQIYF0oceywVjo5_HG_hgvtFrpR7c4WT4xixUS5IiI8cJmTggzP2p08eDmUB8nK_UvlBNnCop7b1vucRIjInOnPulzFrkSqEKIVerbBwtzAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nZLNyR1ibn8CYdLZm1-EtJY1QrgOHXEXs88Owog8sM41K8lF66PGssAMQaP_o_I3stCAJBGttRnGHrVQRx51jLqciBFccABz-junnoK-3nVZCpx8_2HgZojvdn80fxPBdZIYVRhhznLCggzLOuksCPWIGndo6UKrbSHNVzcQV-zB5qZyLfNq7ZdQ9S16LQstKyzhAmh9PKdYLhAVU2fDLeMPYn3dvOGqC0evHCI1UDEo7CvG967n5c3JNDrcVlLP1bsweqAkSVUhQayWKA7oTa_aibezU8YuGcX4JSXyrt7M-s8c3JmVgjcLJoXe8RM54HFDnHBmruBY4qb_3bEQDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nZLNyR1ibn8CYdLZm1-EtJY1QrgOHXEXs88Owog8sM41K8lF66PGssAMQaP_o_I3stCAJBGttRnGHrVQRx51jLqciBFccABz-junnoK-3nVZCpx8_2HgZojvdn80fxPBdZIYVRhhznLCggzLOuksCPWIGndo6UKrbSHNVzcQV-zB5qZyLfNq7ZdQ9S16LQstKyzhAmh9PKdYLhAVU2fDLeMPYn3dvOGqC0evHCI1UDEo7CvG967n5c3JNDrcVlLP1bsweqAkSVUhQayWKA7oTa_aibezU8YuGcX4JSXyrt7M-s8c3JmVgjcLJoXe8RM54HFDnHBmruBY4qb_3bEQDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=GcitCSP3mUNIvKQzjUELfJlsFmH32aBSatp72Rb5YJ9f1zmqCaEpNWDxqf_4w1DALyJ0GrE9mHNUBwQ0892OyxuuT4k5NunVRr4raHPHs94RxCMf_tZVbxH2K0LfDs-xC_L0I0Qii0BwDWti5RpCt2oANo2FQF9uM_B7OBNJ3B4Wi22dBMP5GFeFH-oeJkq2GebkCdIaMpmB23eZ8V8j61o1CkgQs0RhWrUPqHlVzf9UUCc75LlqZAD9mp0Y28jME333Z3bB60OIOvRnY94Y0hKYpxSpZ6YiVBAyIGPRFNYfZpDaU-0xKAE5kjwlYXNvMFgw9zmG0qCqBgGE7Nr8Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=GcitCSP3mUNIvKQzjUELfJlsFmH32aBSatp72Rb5YJ9f1zmqCaEpNWDxqf_4w1DALyJ0GrE9mHNUBwQ0892OyxuuT4k5NunVRr4raHPHs94RxCMf_tZVbxH2K0LfDs-xC_L0I0Qii0BwDWti5RpCt2oANo2FQF9uM_B7OBNJ3B4Wi22dBMP5GFeFH-oeJkq2GebkCdIaMpmB23eZ8V8j61o1CkgQs0RhWrUPqHlVzf9UUCc75LlqZAD9mp0Y28jME333Z3bB60OIOvRnY94Y0hKYpxSpZ6YiVBAyIGPRFNYfZpDaU-0xKAE5kjwlYXNvMFgw9zmG0qCqBgGE7Nr8Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=ZbSy33uiZX1Ed_SOK5DfaqdLLoTfPDqGjsfTMqrwC0BEy5zwlha7c2-OH3mXZRZdUWWdenOt8VhVUqZDm3MN_4NOrrO_WVtaAM8wmfGoWZ93sw52m7Krf5KHm3MWqTZpPM4VY6hvrJwPXHQ4Atgud7Y-sR0XfbA47dJ1-z_YdTyLEKDMu-z9dRniiKyqsPm3WPCMN-5V54QRCpE4BGY8TzsCHva6_Py9TD-fAS9juJqe5sq3O5WEpGO6JN4aKPV3xQ9Hx6xDHLBS2GwqxbyR5xMOukeKA87RIQS1PBvCqY_gWpJl0xVEG8nlBiZxn9o6MdhuSVGrhHrYED_4admY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=ZbSy33uiZX1Ed_SOK5DfaqdLLoTfPDqGjsfTMqrwC0BEy5zwlha7c2-OH3mXZRZdUWWdenOt8VhVUqZDm3MN_4NOrrO_WVtaAM8wmfGoWZ93sw52m7Krf5KHm3MWqTZpPM4VY6hvrJwPXHQ4Atgud7Y-sR0XfbA47dJ1-z_YdTyLEKDMu-z9dRniiKyqsPm3WPCMN-5V54QRCpE4BGY8TzsCHva6_Py9TD-fAS9juJqe5sq3O5WEpGO6JN4aKPV3xQ9Hx6xDHLBS2GwqxbyR5xMOukeKA87RIQS1PBvCqY_gWpJl0xVEG8nlBiZxn9o6MdhuSVGrhHrYED_4admY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=bjrKZtpp2vfiWIY6yg9WigC0b3klBq5X5CYmeiQqgsK2A3oADh58SH8ZxYwTIbTqlSL6yu37f54cgTo-6kP5XdtXAGbHw8_ikIvvDY4Gk_cg5IaNKEcjzLw4L7sbs4NHmtXyuRKLHKW1nmTLMwaljSxn1XLe3GBcP4mjmgBZnWgmBJDJZaVB19buBR7P4goxSwer8LWewGVODos1a3Cvp8v660BX29SPEfnbaSmqw7XNEYv87zHIdt6NUocHLLANB271EZcrlCOl3ZJBtT5o_n_MRbMqOm6cGMdwyo4VipEoTEHwt_3Y4oTRlYGTiQ1VD_d92WkjAWJakI0NrV2qnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=bjrKZtpp2vfiWIY6yg9WigC0b3klBq5X5CYmeiQqgsK2A3oADh58SH8ZxYwTIbTqlSL6yu37f54cgTo-6kP5XdtXAGbHw8_ikIvvDY4Gk_cg5IaNKEcjzLw4L7sbs4NHmtXyuRKLHKW1nmTLMwaljSxn1XLe3GBcP4mjmgBZnWgmBJDJZaVB19buBR7P4goxSwer8LWewGVODos1a3Cvp8v660BX29SPEfnbaSmqw7XNEYv87zHIdt6NUocHLLANB271EZcrlCOl3ZJBtT5o_n_MRbMqOm6cGMdwyo4VipEoTEHwt_3Y4oTRlYGTiQ1VD_d92WkjAWJakI0NrV2qnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fot3Xy4SVRONgT6IoQ6cPzD0DTh_xAw_7O2rQVS80UHk-KLquoM04Noukt4lY0DmqBdIwBlIZXgvaUbF-lrXF6Q3L4weUKA5pPTCtM5Ckm-4OSe88q9nxanrxikBkvuNQHH8pq7UpQz3MvE3YqpQr0RlxWS5mPl66nyqtFALMa_NLQTAELEms1rLLP3G4Z0gnOW6jaBDZUGr8hnBtru25pNP7fNjM29Dr9aao3A0fqmwBeNgj1YOdqv3QL4fuZKsKnBKnQaNoyFK9hUFA_XnnJ94S1Ca33bwy6iUON00k3SETCmDZXWnzrEHtcDG27IlaMivfbx2vLXsv1H2Nr8-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWhJhnO-IuSFarNL50CCn24B5BDYd0ebF1FUSK0Wd6S5cLzpyKvsNnd43XIFEXAZfQOnjPNL6l4WKhzrR9hlgyAbcHxdtO2IN1BZgMdOIBsLW8hde3EkVIoojY5Zhv4HZv7itG1WYsuPyeEvQQEcXXAvSHZtA2U0jR7j6jXL9CXX0Eixw-Ugpp7HfQcgomseGAtBddczfvJjKEQIkKDRBp_0D-xf3yx30qVDHWrUMMfyyr1W4bL7T-RuXNYlLngk7YtspBh3mdag7LRTetE1dZRpZ6ZkZ7O4zycoAMeLPSPMdGeLDfyauHRNebd63WbXu7S_VqxfKc5LofjUBpL14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=JBDfQl9kVocXEJV7pD-BUvT7MGTFbY39upTNm9ac52ABCeEAxFgK0Bchtz8jJoT18c6tlx-o8ys86-VJOvyR76MxhppDLJO5zbc5tPTJrDzdUOrUjgHNWvCo7RkOHW9kMI6HFmPuDGPLMpj28K8BDAHg2XKG8ysN6AIPqcDOWNijre-hg0rZoPYVYlPyxsbfojPXqVSrorCN22UIS5W_YPTSZauxrfstCHznoNHd9-oJ8f5pIjqb4mqBi8en-OgV-svSG3bFrLGXbeNW0FMMGHX8TwSRo3V-2rmzmFbj8VvVC2o5hNedLoMrh2_zGEdYjEq_HJyVXbfKHSlghogrKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=JBDfQl9kVocXEJV7pD-BUvT7MGTFbY39upTNm9ac52ABCeEAxFgK0Bchtz8jJoT18c6tlx-o8ys86-VJOvyR76MxhppDLJO5zbc5tPTJrDzdUOrUjgHNWvCo7RkOHW9kMI6HFmPuDGPLMpj28K8BDAHg2XKG8ysN6AIPqcDOWNijre-hg0rZoPYVYlPyxsbfojPXqVSrorCN22UIS5W_YPTSZauxrfstCHznoNHd9-oJ8f5pIjqb4mqBi8en-OgV-svSG3bFrLGXbeNW0FMMGHX8TwSRo3V-2rmzmFbj8VvVC2o5hNedLoMrh2_zGEdYjEq_HJyVXbfKHSlghogrKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=dvu9DmV1RJ6I_AYg4SKQ7AOxM4b_7W45KUa5CDtutZHfcTathQL18cLoEH-qQLsNAnhuE6tDoL_Xuh0YYEmmn9rU91vzHBtx7yCH2pI5T08yrsWg7YLY1cnvItvLsvX7rc9LgluJnfK5NcrEpYMEUiHyNpIEHiunjlA_5WqjtUDkEEGu_q2ZNz77GCHevtwy1E9nhreY_VNttOn4aYhkvkmCfDHJKNRRMqNp8kN5UXYROvqCX2w2mn8Lgo1C3fcSwA1Bd9NPDdr1lazGEx4Wgh2QFdpdWHnmen3OilZ03a8nrtz0BewBfqPHHwccPOubg7jsV1QpdQmBEwfNSk6HVklgQ9S3S5WWFrrEHDxA_j_xglOPxBV0CuuwK6j7aztO1V_p-8T0lJBhJFGE_JydyZMEOqDonW_mFV-kWd4UuG2_3in5l4po8DVxXloWdeONiFKGZoCg8GYp0Mi-mQPA1Aw4BylOP8F6OoswATf2JVzkFve0zR0MS0_ZQAowPaWxz7pMqXHj4LfH4UN3Np8tLAhuFRSWP5PfCUQ2Lz2WZnOc_eBMPLfGE-LS212054VdMwM9_J-KMfeLGswoFxXGZgmGVzWICmpz3_XJtkB4CWQoDTyZAiWU6kBFHenRhCyHirT1bDOQGK58nJDPNz1e-JqPmSoqchr8FapXO3dcLIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=dvu9DmV1RJ6I_AYg4SKQ7AOxM4b_7W45KUa5CDtutZHfcTathQL18cLoEH-qQLsNAnhuE6tDoL_Xuh0YYEmmn9rU91vzHBtx7yCH2pI5T08yrsWg7YLY1cnvItvLsvX7rc9LgluJnfK5NcrEpYMEUiHyNpIEHiunjlA_5WqjtUDkEEGu_q2ZNz77GCHevtwy1E9nhreY_VNttOn4aYhkvkmCfDHJKNRRMqNp8kN5UXYROvqCX2w2mn8Lgo1C3fcSwA1Bd9NPDdr1lazGEx4Wgh2QFdpdWHnmen3OilZ03a8nrtz0BewBfqPHHwccPOubg7jsV1QpdQmBEwfNSk6HVklgQ9S3S5WWFrrEHDxA_j_xglOPxBV0CuuwK6j7aztO1V_p-8T0lJBhJFGE_JydyZMEOqDonW_mFV-kWd4UuG2_3in5l4po8DVxXloWdeONiFKGZoCg8GYp0Mi-mQPA1Aw4BylOP8F6OoswATf2JVzkFve0zR0MS0_ZQAowPaWxz7pMqXHj4LfH4UN3Np8tLAhuFRSWP5PfCUQ2Lz2WZnOc_eBMPLfGE-LS212054VdMwM9_J-KMfeLGswoFxXGZgmGVzWICmpz3_XJtkB4CWQoDTyZAiWU6kBFHenRhCyHirT1bDOQGK58nJDPNz1e-JqPmSoqchr8FapXO3dcLIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=gwV-08g97HLX3It6i0lunxjuWWXvBSJ0mjB84v4G7JILxalJjnakxJe9eKGz_jiJiu6vqbn6_RtzhtE5IYxPiMyDzK4BtCuJJIYN1GV4asoThbMCtxcbnM5a6kKgd-BO0F10UZlSPKsKAClygvq2PBM5ctfaciojSS6EIfrC780PHQ-PzONxvY5oucq4JRJz_m2Vk9TIa4khHFUbHtlqhqj76HyP5dwJfO6F23k_KEKSNfAbzbOc9ofxNZQOdk7zgnDbL6g_NiyVXTogIQhQEwvmiMcufdqitQ9FbmWPOVUUJInYPUkTYzS5u21CSIiglF7dtVSwW7Mwz-lREa6FGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=gwV-08g97HLX3It6i0lunxjuWWXvBSJ0mjB84v4G7JILxalJjnakxJe9eKGz_jiJiu6vqbn6_RtzhtE5IYxPiMyDzK4BtCuJJIYN1GV4asoThbMCtxcbnM5a6kKgd-BO0F10UZlSPKsKAClygvq2PBM5ctfaciojSS6EIfrC780PHQ-PzONxvY5oucq4JRJz_m2Vk9TIa4khHFUbHtlqhqj76HyP5dwJfO6F23k_KEKSNfAbzbOc9ofxNZQOdk7zgnDbL6g_NiyVXTogIQhQEwvmiMcufdqitQ9FbmWPOVUUJInYPUkTYzS5u21CSIiglF7dtVSwW7Mwz-lREa6FGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENvhD7vOcpKEMPyxSU_mheq3UnRGzMG6xpZ8l9rXkqoPBKG5tt22fP1xoJAcQUfNKF6H09pNaMC00nvdDTrMq2n5RJOuoXJFiznt6EcK9M627fYFrdk1H6qer8EygAIWxOtI_Wf8-hgOvBduwoXOEOdHuaQJRMp6qkf0kbE0Y8T4DHeb4ftNe-MlPf1omrI3K_y9AOCmtw_9ZpjJfMZFu2dOzRNxK-qmf4YIEqXUuREybxOGxJZfvZp-D1xUrFxZEDejGUoPwjzMzUkYODyl86f968dttnOYL-oaxxRvkbP7bl8u9hxZVIgR41bSBQuDDvmaodDBgql_D9uClIxkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6VZ3DVAY341pxu4I6hJ2V1H0NKKKgB4Q2kEqR7Lnuog5yGpKDvoX6Jz6oCOBh0z87KNKY7NZrgG3dhOufEvqzFAYLKGYI3KV7iZ7SEpOJxwiYmWyUvFKMNuRhwuyOR1h1G9bUZuEYmcYwnpMfrfn28dAMRvu7kT53ga0hRn24b4duCKhRNMWTBUQdWA_w1uPV5iIcHsxMgN2CwVC5HxAY6efSXQm-Y0oXsY1-a_e-A4yBJPnQCgdhAjzXfNGpKKe5zreVZwgr3Uk8pptCSp52GmIjQPYusGQeRXJphILCjePwSzZ0MKklt2H-w1nY17tsVEsdm92yB_mAEFtydUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=EnxoysBpsGyEh0RmHKcis5Aa8bjt0X6qONIFyedf0PWQKVTb85u1njYbPHFsi3D7yn0F4q9uAPR2TfWNAUyLELm91ZxqUg4zR2aQh2hknhSG2KdPML4twHn53oY1du0pfkuYO2siyejHDk6oHYjoFdr6zTjmwqN6T_R07HBEX-4atjMwg0PAXWdjBRZc0yeqtkGpGluEgnPWi1Pa_5zQig4fyoj1NpGkejQ7rCrOncINf_MxjlQl9pklWZHsOAv7ihvfqctOyJ4EJmUTBcAI3Px3-7d_TOg4cms6FOWeS3I6Wl62W2wwgI--9F6r5GrnTbeWRfC9a3n63etnsgbuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=EnxoysBpsGyEh0RmHKcis5Aa8bjt0X6qONIFyedf0PWQKVTb85u1njYbPHFsi3D7yn0F4q9uAPR2TfWNAUyLELm91ZxqUg4zR2aQh2hknhSG2KdPML4twHn53oY1du0pfkuYO2siyejHDk6oHYjoFdr6zTjmwqN6T_R07HBEX-4atjMwg0PAXWdjBRZc0yeqtkGpGluEgnPWi1Pa_5zQig4fyoj1NpGkejQ7rCrOncINf_MxjlQl9pklWZHsOAv7ihvfqctOyJ4EJmUTBcAI3Px3-7d_TOg4cms6FOWeS3I6Wl62W2wwgI--9F6r5GrnTbeWRfC9a3n63etnsgbuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4rKPMfsq04S2ZBNTB4OIbyoKjtM1i51rPudkimMKZBuRfVvLNb3BpL7Vq-b8PYt5Rok4GhSD2dUyK79up9kWtB_t9lxJTxUnN56I0mhUQRphjdlUOkuPy2b-yTWMLMiiC5ku7fdZYKn9qcXQRL7_modDrVboTPAiFCoAt9Q6iSMMbWpUUq3P-4YDttnYcJtafcKHlx3f9656N_DBnTJcC3_QGKO88v9aRgEszNwLs7YYXYt0lL6hT0g1Wpg8N3ByEzzEndaSgft_wk9TPuEsbcXILU8EZMdanf5r1OM_axky9n0uApr3JBMmVW6zkqI1dRpdqKRG7gXlgrjp2Rlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbhCQMbeQy8_avVkC_Dt5e-2LUmrWGZvGSH3bXpvVWUe206fnkJ5ypy9IZ9CBWJHoHFU_NaZJm0fzU0OQ9zKawO5Zfig_N_NVf2aLoZjrogR48Me8irDE0jGN4bPYDfnKuVFga9C6ovKKsKbnTraUe4xBoP_Ldu2hfbgXnJTnYHeKC7cM21jQS96s6ik-hepG936goI8RYEa0wlqOFQmXns-m-8PZUmUZOOZLrljoGDlSsD8MpcG5c5EMNvLL0R6mVHhXfZ494LupxLduFT60oIdrOmfkvsjWnZNE646zIte8K4Q9owuPRwr4S9SI6KaQxqheRY5aPWHaDaUn74ovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=T2p7buBbjdKPkJZzvAqMB41M3jIm3tMSVIA5GO4ubWIcECdhzPnMTtmYFypOleJtrxlJOaXdfIyg2k4jGDSZ9k30GhndpEjz_B0WliTEoPvCOByg-29B-G7G3gQsYQzHvCAz6I5FeTQM3A55v_KC8D8Y0j-b9rQh2UTPBlSKeQ0ACRioFGlxB8p1ZHmXnrDp1-D7Ki4oPDPRaHUs7vYSdPArESkONntJmGBIAowfCg3fY1SVI-ovcU6v7D90V15FQn4eYHnQ3bbhuFokWO35Ja64dWR6Wmru-WHhu6N1d8UzctNslhQyAglhyVAbmBlme0Bdfc_KYWyZZVOQNg_Zgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=T2p7buBbjdKPkJZzvAqMB41M3jIm3tMSVIA5GO4ubWIcECdhzPnMTtmYFypOleJtrxlJOaXdfIyg2k4jGDSZ9k30GhndpEjz_B0WliTEoPvCOByg-29B-G7G3gQsYQzHvCAz6I5FeTQM3A55v_KC8D8Y0j-b9rQh2UTPBlSKeQ0ACRioFGlxB8p1ZHmXnrDp1-D7Ki4oPDPRaHUs7vYSdPArESkONntJmGBIAowfCg3fY1SVI-ovcU6v7D90V15FQn4eYHnQ3bbhuFokWO35Ja64dWR6Wmru-WHhu6N1d8UzctNslhQyAglhyVAbmBlme0Bdfc_KYWyZZVOQNg_Zgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxdjjEnp50hgP0fS65PhRAVAn-dbAg6hU6V9fuUYNxGVsi8QzB3GXzXutaQWIgyHjUaTAJG2ykHID5NazoAy-E36-TDJPMkeqW4ig2P5FCCrwO3VYjHEP6WSyad4g-Yiu4FmELi0j06bcPB70w-4fye0YdY2S0mORd7qtA11hImgnu8wtAXtbOaG9geQZKtp189xQkCIH610NkicZsyGc9RuGEvsiC-t-QFJBC0rCHh9Qti3WMMPjcHPUmC1DR1ZwkK5X_1VNh1ORArXf46oK8bo8z-1Jl9WB7cBuzikadnKxJfhmu5B5i4VB6E788K0GoFJuxt627-w8mq4tP4j-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFVPUvQNxDliJXK9lVVeV9NpAYieEfeyBn_REOD0TeAN669D6RxGV1fqe5d6OL93r40iF68Rtb4Q4NTO99CUgiYq1CyrpYKy03HdRVYeXEjpbxAcwc2zN-8M_JNSyqiyd7F2YJM4aqImzE4XMIIELOMHeOlzRI0iv8CfUEEsD_reULf2-umIYu4FAFolXYfBwE19uva0f1ebeY4AOsXJT9Bbgp4dOjJfc7DwJZA3UCdqlrJ1I7Eg5QSECNMTGyEU5xVPYGEFqNXdvQwaOMfqNGWdgLHinmimwACHGoEWoimAtkWfTg3tP_FtNPTrX9T5RWMfHdu9WsRR6GoB2GoAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=FfN8_KyqBLLORBo-NzhYgeEEokM6Gq_9HsqI52UopB3zuxACaofFPAyPjCRaMPHsRm-3_QzKg-dpfoPo2lQjxzwp6EAUUlpH0C7ElSmlTHB5y444aE0LDoU3F02E-hS7zTONA8yrq-zQs-u_zFjpICbk_h1PKAq11FWbrkB4PQolf9AY2C-usQwGJYbDcsB1xFtoHk3cWrmRPl48K18vcVppULfMVWKNTmGmXz6cYoQDF7PGv_KU_q1UVppgwy033o_p8p7-2doIN5bvjth6VVE2m7mkgpYK7f5f-Iu_yeJ93JuWKJLUw60knrJ4a75q4mjjeF5OIl3Nf8PwIJ1JuIYk8I1V5phTulbcN09Je5e7lQ7nMgNpqttu85AfzbEutJFy5Vlx1L_6BEc65lnGL88PKP-fL8-j8GYU7dG2j98M5Rr1L_kay3wl31iHa0leuMRHK0PCgpbgyskXUOEvDQDg14dOOJ7ihQLaaWHQ0YGTaGT9F0udhnZLd14lbFAhNnUNQgPtTf9XU2APDJUuf8zJlfVgSj3YNEmLSr18ZBUTioQarNKehNhye26sPQBV2NC4g-GLFy5uArf7FnmO1QC0A4PKkMrpT5cJ9dy2jPVtScSjCel6os2QSzABYict-AkoBByQzeBBObtcN-E2khaNTa2iWTjPHAJXZTheR0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=FfN8_KyqBLLORBo-NzhYgeEEokM6Gq_9HsqI52UopB3zuxACaofFPAyPjCRaMPHsRm-3_QzKg-dpfoPo2lQjxzwp6EAUUlpH0C7ElSmlTHB5y444aE0LDoU3F02E-hS7zTONA8yrq-zQs-u_zFjpICbk_h1PKAq11FWbrkB4PQolf9AY2C-usQwGJYbDcsB1xFtoHk3cWrmRPl48K18vcVppULfMVWKNTmGmXz6cYoQDF7PGv_KU_q1UVppgwy033o_p8p7-2doIN5bvjth6VVE2m7mkgpYK7f5f-Iu_yeJ93JuWKJLUw60knrJ4a75q4mjjeF5OIl3Nf8PwIJ1JuIYk8I1V5phTulbcN09Je5e7lQ7nMgNpqttu85AfzbEutJFy5Vlx1L_6BEc65lnGL88PKP-fL8-j8GYU7dG2j98M5Rr1L_kay3wl31iHa0leuMRHK0PCgpbgyskXUOEvDQDg14dOOJ7ihQLaaWHQ0YGTaGT9F0udhnZLd14lbFAhNnUNQgPtTf9XU2APDJUuf8zJlfVgSj3YNEmLSr18ZBUTioQarNKehNhye26sPQBV2NC4g-GLFy5uArf7FnmO1QC0A4PKkMrpT5cJ9dy2jPVtScSjCel6os2QSzABYict-AkoBByQzeBBObtcN-E2khaNTa2iWTjPHAJXZTheR0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxtRzhPa4HDLv7NWN-JpIEeLNoVkhe2ogrr7T3JBl8Fs4EsVko9Hpf_LGjCKBongkwluqW27ct7F6LChhWyv5JOUPWxKf8iVBtFC8sXBQBmKAshUm0tSu0f_Yk9I40fuf7mND2Xxt0RJcQ97H0uN9vM6wCKOrTYHCAAumb5Ax2JsYkZQKq5TxlGrDEvyHTWFe1T-ngYd5VgmUvAfBW7nQ2NdkfBWmdOhU8Ir7889trz2Knqil1V3RfdLRmqUxBfMPlE4bFZFOUc6deDz8TfQpHD-KALFdWNOIR0aEguFpg7xFwHyi4MrmmZHmSH3_DCuTZ27gA8ewwqigB596O_dAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV6VTHLgqrjq1Kz7o8kKGOLBPL4uz2L-c-obDmFDbCIjl_GEE5miDibQC-8Rpz4O3QjM6fvKFOT-AcN9HHfXvCNpls-15N6Snp8ruU9Fg_1jtO-o56hL_rdq0U_oqTQZ898MLfleQVY77Th3jGHUDoEOLSAuOzIboq_CMOAcPCXVqHelyYeP11qASDbGBKyRDQl6uNYWU91Acla-hb--UTYWLIYqk66-zCZuM7pACr_6dkz8-rS40Y6YbCfOJB6vABjD3h8YCeZhhL_l1CpEg1NEJQdPLGbsmBmSIRfN4q_lJM7hiFmVCs3ro3bMnWQp1Pb-TZN51Va-rTtnC0DuUgF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV6VTHLgqrjq1Kz7o8kKGOLBPL4uz2L-c-obDmFDbCIjl_GEE5miDibQC-8Rpz4O3QjM6fvKFOT-AcN9HHfXvCNpls-15N6Snp8ruU9Fg_1jtO-o56hL_rdq0U_oqTQZ898MLfleQVY77Th3jGHUDoEOLSAuOzIboq_CMOAcPCXVqHelyYeP11qASDbGBKyRDQl6uNYWU91Acla-hb--UTYWLIYqk66-zCZuM7pACr_6dkz8-rS40Y6YbCfOJB6vABjD3h8YCeZhhL_l1CpEg1NEJQdPLGbsmBmSIRfN4q_lJM7hiFmVCs3ro3bMnWQp1Pb-TZN51Va-rTtnC0DuUgF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=ZOYkfUFT8Q6fiZ0S63jhS5dndxSCU8wNjnC7lFkZvN39cw6nND-ok-Rc1CyAR9HlhrUHmhbp3_BaoEtBcZ1LveW46c9oPBIFh6fkxFIGqeC77-1qqcmEO8PbiQg-cL37wgaMrfOzBt9LQiTiaagW7q5VfbkxbY8xQcZwIqBggm6ZdiOhB8UKzp7IfZIcuQhPCAs4gh-d55ucibjgoKz9qa8nnBsDNIGXhFPgqAJ0kPbVex7bLjG4T97Fd1DTCstIOf7HX1rMcGdwLDwgy8MwMFAZpaOWLLzGISx-dIM_1kXRAzij0GXLhD_nDnsCuDlo69UkvHWtHi5jqFrdF0xR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=ZOYkfUFT8Q6fiZ0S63jhS5dndxSCU8wNjnC7lFkZvN39cw6nND-ok-Rc1CyAR9HlhrUHmhbp3_BaoEtBcZ1LveW46c9oPBIFh6fkxFIGqeC77-1qqcmEO8PbiQg-cL37wgaMrfOzBt9LQiTiaagW7q5VfbkxbY8xQcZwIqBggm6ZdiOhB8UKzp7IfZIcuQhPCAs4gh-d55ucibjgoKz9qa8nnBsDNIGXhFPgqAJ0kPbVex7bLjG4T97Fd1DTCstIOf7HX1rMcGdwLDwgy8MwMFAZpaOWLLzGISx-dIM_1kXRAzij0GXLhD_nDnsCuDlo69UkvHWtHi5jqFrdF0xR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXa6rWAKDBxxtAiEXgSweHjEqqHVW737QI_ay3h22oYEjEfxswOpoOl9-GDfNhoMn04DopmIsh8dVFkRNUnTFjiJARzgTQPhpkICPTkMwZOeSBfMgs81sG4inK--o2LyY-hU2JjUzcY9kaoZN7FJE_rWLwAhJQlldLHp0owBupOGMhl-eDLdRq7T-x5XSrQb1hksrZnv7pwlGV_0VB8ksKjs6zQXfzjJOgRxmXqaulOEReNK-tjt9Ib_lxIeDhoQkuQe2Ooj7ULgLlrDx0AIjJ6K1CGSTu2lDvESOoqLAEvjCTFF9DtDWBXn2_4Cu-ZthTBKCJciFSuNLI1u-S4O_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=qr1wf3uGAmpdGRoWdAgcQ5NlrYq-LYAnnsN_P2CaS7FKXhYUqbj_9dA18trgqUBV8U0FbprKpnTzYf4XsrK5yo2vhVy_TycYQukt4lUYQNRP9ZL8YxZAVgMl-LOpcjLjbrXUASuHE89NR-8BhcnYNC8QU4DrD_fJyYanLK4lPNbi3lQX53EGG43t7crvkdpJ-aVQok1ipIK9MMF5pxN4PF9YxWtIx6JVR3LsxV7iYHF1zBvBudwj9NQdiFSEJupnbDyvH3IQ6PI0yY405tIr9YDtyRrdwro1gC9hTQVedqxCCVazEVp97ytdfC8R3I93Ixlq2Ko4Pa08uXDpInvrnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=qr1wf3uGAmpdGRoWdAgcQ5NlrYq-LYAnnsN_P2CaS7FKXhYUqbj_9dA18trgqUBV8U0FbprKpnTzYf4XsrK5yo2vhVy_TycYQukt4lUYQNRP9ZL8YxZAVgMl-LOpcjLjbrXUASuHE89NR-8BhcnYNC8QU4DrD_fJyYanLK4lPNbi3lQX53EGG43t7crvkdpJ-aVQok1ipIK9MMF5pxN4PF9YxWtIx6JVR3LsxV7iYHF1zBvBudwj9NQdiFSEJupnbDyvH3IQ6PI0yY405tIr9YDtyRrdwro1gC9hTQVedqxCCVazEVp97ytdfC8R3I93Ixlq2Ko4Pa08uXDpInvrnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=Fc4LflGcDou_mNls0hvrbokka344gJhFAa2ByxDU6Yf-dMBi3h4hmYgthTlm-e0yWUZH2GYTVC0a2Kjl_21Wy7WxI5R-fQHD0_7MAiqiqldpZA80t-pqoZDKC2QSEWiYTcpok55fxBQozoVEVeVl3eefvz1BVpPU3tFwtH3Jx_tqIt73W9kHY58jJwchtSEivRoln16kB-PnCAo2FQ5uDlcwaoWGRD06jXFOBpiErybLLxyXyILbVekQNcvVqIQsQpwvE6KKDfxMrqNq_v5ys5qRkmeh9X8B3KujKJjhLr7-1wvyliTJs96wb36FfEFreUrSmupAZjaNFTZWj3mS3WQEa3h2a99o26uO8XFXOfEqJGDaYrUz1sbgNMkAnMIZZYH9rYJeoYij1_Mmq1vqQfMQ6EObO6MXlblgPZUYbJRVhbcf2nTKaPFfEP6wJM2TIaA7dyPVQfOLm9sVPeW6m2D36PuIUeSTxQgz-UO92WFRYkoOoipBD3mtwjFXTT-WW5C3batdgY1rScn3rnhmRwbsiTzDe64WMowqtxdmrqll8Z0K4x78yrLrKj3czzcPG1hK-rVNmVWH8dXwVVk9IvP2cZnshMqqcxIWnM-tNkdyBeBYG2UtlbhEBuD3JOsIGHTkaPL6kik2qp9ERppB-PBwKPLXlxTgGfGUERHxwx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=Fc4LflGcDou_mNls0hvrbokka344gJhFAa2ByxDU6Yf-dMBi3h4hmYgthTlm-e0yWUZH2GYTVC0a2Kjl_21Wy7WxI5R-fQHD0_7MAiqiqldpZA80t-pqoZDKC2QSEWiYTcpok55fxBQozoVEVeVl3eefvz1BVpPU3tFwtH3Jx_tqIt73W9kHY58jJwchtSEivRoln16kB-PnCAo2FQ5uDlcwaoWGRD06jXFOBpiErybLLxyXyILbVekQNcvVqIQsQpwvE6KKDfxMrqNq_v5ys5qRkmeh9X8B3KujKJjhLr7-1wvyliTJs96wb36FfEFreUrSmupAZjaNFTZWj3mS3WQEa3h2a99o26uO8XFXOfEqJGDaYrUz1sbgNMkAnMIZZYH9rYJeoYij1_Mmq1vqQfMQ6EObO6MXlblgPZUYbJRVhbcf2nTKaPFfEP6wJM2TIaA7dyPVQfOLm9sVPeW6m2D36PuIUeSTxQgz-UO92WFRYkoOoipBD3mtwjFXTT-WW5C3batdgY1rScn3rnhmRwbsiTzDe64WMowqtxdmrqll8Z0K4x78yrLrKj3czzcPG1hK-rVNmVWH8dXwVVk9IvP2cZnshMqqcxIWnM-tNkdyBeBYG2UtlbhEBuD3JOsIGHTkaPL6kik2qp9ERppB-PBwKPLXlxTgGfGUERHxwx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3qVUrZf7REoZna2lZF6y0bgnXM0L_uWFHI5imT-_jRvi9utnYV2jYX1b6I2okfAJqsWoUjRNm9tedP3chwhhWMvwnK_W_UVsniMwlF573JkWbnGKTlJ65gSJrLl1XWXdQJpv7557OmLPvhUrYWRWjREfMXSxfdDVw-vE_E8oyDpGM3Lqnscn5-E_2OmFuhOfQDeeGJb4DOqtnhtAUsrf9lRVRX60UZ_wGm37nIlkjWYjXCYaM9BoI3gDVddo1wIdjTRe9rLuJK9kiWNL3caKuCtGr3rJYGpyh2j1Pg65E_Q-5V7-aCe97vjCX4DZ1EeZ9RX5O4D5SpgfQtF4-VMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqjeMPW5jwjuEbcqxSPb_e5abGjCU33Tv66o30506yueAhLVv9Cke-qKWK_wFsvKrMNrZuVDlSPiSF0F5sfydc4o8rKoQ6f3IO2_PGI0Z_GIwVBCm2RDSBKBXUz3Ujr2vFobwQj7TOyNZ51CYUhrkMc387_PEFHHcILgsOEByJmA5tLFe1ZzcrGN4muO_bOB51aZJVk6qKA7A-Co5JWmLO2TZygPLIVGSZ4x8YLBviHSWQVCgyff64aHO91uU0kiJjWCHDChvao4-N68ZZpzn3uCpfWBO0FAcOY0pTa5AWIcf-SdHO67_iV4PrHJKyAfUqlw0owRLlZsONMPZPJJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esvOsnuS9D1pK5QpqIzgMRLT96pEcHYdBifUCn9I89WrU62dHyVhYkXwUTbzQQWPkvMl0yRCTTxamoHExzUHE_bdrrcaT3T4ax5kYwKYJWUFt-eDyORFhLQoHouKJeg1tmLV6fVb8qJLU-Vuci16JgV8ApfNraJ-D2MT8id3towsfol5UnzWyAe5O1H_hhrPe0RoRxh7QasNoByxS02bGK9YFIGLiWZszGLaCaKAK9B7evPL_U_31e1ois82SZy7DjirOMBmFDE4EX9TJ26k1kKIqt66PpOBusT3z0H8WwdXsGHlOM_cJcxHNr3fqZ3dXTiIFbJPykhJK9jVe7UjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epmQ8H23GuN4oTToQ4075L8Sa0RKzKQhgb_e2pzO7iJ7VcMrLIsQVd9YxlLKmXMyBvn1eKa1s5aC1-2lVgg0TKHU1rF_9imfLVuXRGdpeq64GY1chYfGD64Iu2y-ecHgsGwqJJMdcK1Z_zxTkgtaMfyFSQmgsWWsu5dJ5jHs3VHNQKQsYS1Bv6qR5JkVaBinq7qzanxQkpkIWjwRNUR1JsRh447Be83pskEymNZMkkyEdpV9H1a9ZcToFFINYaW1XSC4BlX6vUhxlKFcr9iP7RRrj82eG1aSA3Uy1uhgfaEtnasHAPWXpWRIxgqX7XetzTSvWVKVB7x8R1r5b6MYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
