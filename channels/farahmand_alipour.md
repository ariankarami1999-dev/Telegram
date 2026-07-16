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
<p>@farahmand_alipour • 👥 64.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 22:27:32</div>
<hr>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInibF3peiLlxkW8UF3xqJyasj6hZbHKQ5_zaIodU6-wu95PjUz-ARmzyErw6NSUfWQi-L4gSj8U-x4xR3DFD0O-inPbsvgzJNJ-Tk-cWUh6fFHVK6v_K6n0ZyoCLaeaugSindc8RGDAkIOqohSUzQwk1MMXwMC30t2rUAUnjcq5Xado7XHAU0cipNgjXQzEoCJZJ-hhsCWpy57tYR-g8YO1hrYNMQEnsGQFGsIuMpes7DcsSFsYHa1tSctbeagFAmKrPTyqsKLK3bFbkA1VqzUTrBcV4pzLpX3p1UlNuDbBbwQN-QsDwRmJY5vqcop-O6bcZqNb8QgNvnCva65LHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=q98kEx6iNp_WnGzLTkyYFLNUw4eGcMB9OPe_bW_hQEgqIAt4M1mSRhHRvzOOqLzY3wEOssewJDfFlMx3bAnuT0nhOAkBNu-NtfsP_COQK1b0UHINqRLj3ZpGFaRpjGxnsExOOoQBz25m1qZPie2W5V0xSx6zqPRA6SdmWu_cV3nienJ4wJanO-1V1kB1PjfBszENmvBm5p8tUwn3pKR7yAICXvWt2Wv0J7QocNXpS0qwSN5NTt8T-sxH_7GCr253pz66AiJyaV3vVvXfjYw-bjS3frD228oI8m4ArEDDJ4gSuH0QqLL1Ubj1fplS6YDI6VRqtTITOqkwyg_B8J2xkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=q98kEx6iNp_WnGzLTkyYFLNUw4eGcMB9OPe_bW_hQEgqIAt4M1mSRhHRvzOOqLzY3wEOssewJDfFlMx3bAnuT0nhOAkBNu-NtfsP_COQK1b0UHINqRLj3ZpGFaRpjGxnsExOOoQBz25m1qZPie2W5V0xSx6zqPRA6SdmWu_cV3nienJ4wJanO-1V1kB1PjfBszENmvBm5p8tUwn3pKR7yAICXvWt2Wv0J7QocNXpS0qwSN5NTt8T-sxH_7GCr253pz66AiJyaV3vVvXfjYw-bjS3frD228oI8m4ArEDDJ4gSuH0QqLL1Ubj1fplS6YDI6VRqtTITOqkwyg_B8J2xkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S67FAPbGcSIj2mIMHB3rweXRNd9SeixdnSv8uvrcwW8nnvOtbl0mhQ95jnqSUYbjvGfmho4R6Ei5xQ40o39fj6JfxvGefHFtdDyo6aRh04UmLkVAAsInsKYlzqmuJQs-18faNQ3hC2c7FxONqK1LlxGO-S1wt1buPHFkbTI0qzrEdES4bLTCIb1DLuPjKH07FY6wjWt8Eij3kbViicG7zHZ9WI0tf7C-ipY4FwP2EijBmkd7tORJMqhhusXvszV6kuPkLvoCs7cJuq5qjLeuY_2tMU-eNnXll7N5m2QAlPS0koNASticS7RQENihNJiJvW3sqJXqvNtUahktGgzXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDDEnZNKUBtyQxgZRWW_9YKOGGCiabfvzVAIsQY1J7M_ES-7AnY_u-TF9_AZs2AazR1lgdtwmghUEiMsfLrTeeRuAxgX0UqkvRLEBVv2bUd0JltHqBrqrLfm6fnFVeqW7bL8Egw5cMGk11lC1XmrtR5zurhUzrzaGV3MRY2K2O9Kr1MPFAJb84Tm_ukaawTVoNQuHyExuygEwlvJ1eAjmwQGkUdzrMgv-GGQy3fCLnz4ydLITfnXLsK8_iMDUE8nPnltec2uY6JCGHQoiG3kfzbgLiLILC0v4H9Xdq2OFEXf3Ho00vLvFPlA5IsvXi9Ah91focU_kAAQEBv4qOqEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUx4cTxYWFEKa9j5Yo7MAm0D3lKzb2dIJCk2G7YMwY9XNPWl-gNo4qos7kL2vTe0ncVljBLO1riPEgKeQvQqdkz1vAeSJXiXajCLC_wO9hxpsej-0NxOYZoEgfWIFNIONx6sILh_9UrUxKYOeuHfAhf6mbD-SvsHnzGLD5GQc9r9iT_Jfh3scFEL6R3Hz0Xf-4SmaVyB0AO4x0Aj6NREeoR8AJowqM_beCt0ERBSiuary_GvZzp3_qiXaM9TECmDCHcz91sod1l8VUs_AhAxIGvaAZ8h5K-kMk8WSB2TzB8b-2aLM9QL-Tb4h9xARBFbta01zYPRS_lt3UtAMnujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=pBJVoSUiQwuBirlbjoAYlvE2Lsd7DF0X00ey_oioNawhegMpwl0sNvVgxpxCFFxfotGx_Iu8OwrZYE1dH0KjQxFjCwX2SP5KV0lCiqBSzcjE3SeulirlaSyukHNu8UPw34L8guIv88CHDDFA3L-fcPyoIiYcbDLEVua30XeRj_tvP5GSeZpsqnt-zZYDlWUk7cTGjgNxXZXQb7_O9JfGw4k2NEVwxMtNtt2QaojU1fXTnt9lOhBrVHeM4mzC3rcnKkkcdZGLKx_ltqdeVtN57QgU25Sp8Jbb6wxq5212dDaJZF0II4UsQiDyOrXNnSBfO-V0YBDpy9T-6TvBnI6g8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=pBJVoSUiQwuBirlbjoAYlvE2Lsd7DF0X00ey_oioNawhegMpwl0sNvVgxpxCFFxfotGx_Iu8OwrZYE1dH0KjQxFjCwX2SP5KV0lCiqBSzcjE3SeulirlaSyukHNu8UPw34L8guIv88CHDDFA3L-fcPyoIiYcbDLEVua30XeRj_tvP5GSeZpsqnt-zZYDlWUk7cTGjgNxXZXQb7_O9JfGw4k2NEVwxMtNtt2QaojU1fXTnt9lOhBrVHeM4mzC3rcnKkkcdZGLKx_ltqdeVtN57QgU25Sp8Jbb6wxq5212dDaJZF0II4UsQiDyOrXNnSBfO-V0YBDpy9T-6TvBnI6g8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=g7WgfQJcdJ4AZUk6l6IBZmuEKdDp7MC_Tn0qA4SLrrAhJ_o0fErKjmwIbv3NYaJRcVjgPqZyH4CZ0CDwlM6bWxlMs-zqQcGYaGb23MQeFnZcnPfdIKi26FVaBfF9_JHyJ5r8_8ZbL2kXYHuGA_q9dlYH5KDsyrLfZLrERfr9Bxbh0eGWxuM9VFZxcf7UE1MrJl1JPdEWlm1KyeZq573EufCD8uovee3JBYbYOik6n5sRVGhdKH6ejvpH4hLNEKNPv3JvPCFmjPaDHbwPHA_Eciov6ro5F_cRAsHjl5IyEh5wQDe2OOQQlL7VglrjQbP89B9omhwfbB9cZ12AwVq7koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=g7WgfQJcdJ4AZUk6l6IBZmuEKdDp7MC_Tn0qA4SLrrAhJ_o0fErKjmwIbv3NYaJRcVjgPqZyH4CZ0CDwlM6bWxlMs-zqQcGYaGb23MQeFnZcnPfdIKi26FVaBfF9_JHyJ5r8_8ZbL2kXYHuGA_q9dlYH5KDsyrLfZLrERfr9Bxbh0eGWxuM9VFZxcf7UE1MrJl1JPdEWlm1KyeZq573EufCD8uovee3JBYbYOik6n5sRVGhdKH6ejvpH4hLNEKNPv3JvPCFmjPaDHbwPHA_Eciov6ro5F_cRAsHjl5IyEh5wQDe2OOQQlL7VglrjQbP89B9omhwfbB9cZ12AwVq7koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4gZ9vM9flhP5Xhj7nY04VOyVgt_ow5SU4Gk2Xzva5VX7WsmFn2DCjETPWOT-BO-6nssW1jQ6aaA28w0Bp3e3_wuNS-MDgCvrRbzDFiyZR5OrpHrBY2_Yc3m2WXwBPuz4jEoTx_VNsHGLepW48Cbrg1BISwqGZPyKyTh0DiThveaRunS-TNZ5ZvLq-CLXyBgIbUot-tr9Lr460erEqq6481t69X98Umln7Aqr-o0GaEIFV5vsszrUxC9FV5zRJVsCNRtjBMLvVZVH_mTmM5Pnanie5i9w740RdCHj1dtnZLvs_B7rBx_3r8U-cfyjkyLP7umiePnae9WFvGuJy3vOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig-3ipGZBMm03O8Pa6UIS882TidsIyMLfh9uyKnLrQ-Lo9fN9x3APMFcBiEsuLuup7lC-qCUZJlxoVrO70kps-1LCHEci9JFsU9FTcjJbxGcEaIP2nCrEEhxc-Eo0lZP_mUk64ORS4VhkvMGAre4iAPT6yGV0GActFn9MUreCZ3Gxqkdh3foCrEctJgsEOWzTwPnCc2J2Gz5BUfoMLJd1taAq6Qp36XWGIN6Td_G0kf9i-lEMG1VDxS3bDo0tbLnvEYZyFmC086mYSvHbD5LsSKzNkXB1bUPdyS-t5joC1IX5JxCVQxVGvcKmukYKzUaTddmCDUI4TduNCoDHw8qxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bVSZp5zTmjv3xLkjs90l8_sqp8cNUG3y87xa6UfOj8pEAE9TyravvDiJI5PkzYKioLMatmPQUKDnBRcsFn1ADuGmHkGb--2ZnPY2NHUl98kDP_rzVBW3tehHNGp4ewW7WMHb3nm6IKQnR8ZgKNICs2QdRC4SWir6by5BxnSZk8OgJWElKkF5L8DxdomGtPfHo-AXXTXf2XeiKLoypq8-87J9V4lJfFS4uGeV2U_RuPNgIWVzWBoYJL4CRQ4iirBseeElqNI9TIKFJLhtFIGxhP7mAaJxXOM1EF_kGd3-1cHfQsoGK4IIHYUORtif-yiWznMuaZ15VtkXjmsOHFqQlhvuxKiTQvfPLEoiHOL-2fmv38vjYrnGBC98Lsg7X83Jkq6lU064ZX4paH4H2e6MogJY3IzkQI7V9AnqwFMwhhG_9jLOPx2TNMlmsb-gXKgEMDZd1caH8PLoW_nNW0X3C9wcHmF9gjDNsHpdPEOoSElt-H74Dk0ytq946xcy3c1S4AMzNmFWh8tIb0Fts3F70wuRajned0lH4yGx2eORtiKVR2-Typp4WqZ8L-JwRZwXmdjvra0uR9juS86dUp8zeIvpoCNV6jgyqcNd-qY1IVEANUHkxkk8cWK-DZVwvRfF1vZx_fYkujP710ga0wu7CN2uvyzNXzHpOrEUllPvQsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bVSZp5zTmjv3xLkjs90l8_sqp8cNUG3y87xa6UfOj8pEAE9TyravvDiJI5PkzYKioLMatmPQUKDnBRcsFn1ADuGmHkGb--2ZnPY2NHUl98kDP_rzVBW3tehHNGp4ewW7WMHb3nm6IKQnR8ZgKNICs2QdRC4SWir6by5BxnSZk8OgJWElKkF5L8DxdomGtPfHo-AXXTXf2XeiKLoypq8-87J9V4lJfFS4uGeV2U_RuPNgIWVzWBoYJL4CRQ4iirBseeElqNI9TIKFJLhtFIGxhP7mAaJxXOM1EF_kGd3-1cHfQsoGK4IIHYUORtif-yiWznMuaZ15VtkXjmsOHFqQlhvuxKiTQvfPLEoiHOL-2fmv38vjYrnGBC98Lsg7X83Jkq6lU064ZX4paH4H2e6MogJY3IzkQI7V9AnqwFMwhhG_9jLOPx2TNMlmsb-gXKgEMDZd1caH8PLoW_nNW0X3C9wcHmF9gjDNsHpdPEOoSElt-H74Dk0ytq946xcy3c1S4AMzNmFWh8tIb0Fts3F70wuRajned0lH4yGx2eORtiKVR2-Typp4WqZ8L-JwRZwXmdjvra0uR9juS86dUp8zeIvpoCNV6jgyqcNd-qY1IVEANUHkxkk8cWK-DZVwvRfF1vZx_fYkujP710ga0wu7CN2uvyzNXzHpOrEUllPvQsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeJTqTPdmvHRUhy1hD0uSjIzzPZlUJgTTWTxOkDgxAJZB6hNhH_A52MKngfwNjJ0rLZeTCoM9uzXq_01b4j7hWjNIF2rhocmp0GpaVZ5r4yo8xq6P7ivXWa-HsVlldjCkRyH2zgWC7MkxdyuT-e99dVA25kVDR3N3HnQJHSIint7tVcu7Bjroyn7DAy4sOiL3DOmq2XpRbrw-Rm6_nzJVF_H6JsSRuhAC9FdiuVX0KKKE-sCUI8tmyMDf-3NnyYbIZwit9-mKT12Nh9YOG6TS0kblqC2xl33Jjx3LK8YCsEEkuBxbIpG_Zgpg0c6pWdUzvjkPfg8wHLv_dUPO5nH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlZ2SGYstrHckagih8xPJodWFeuke2GIZV_B_ODwj6RUEb1jqk40y4ldEa69O-Ofxo12Qek_qfGXYlpo0oMpWy8KbJ3hLhORXz90YIJEXTadX0CgSZsaw-1ctZfTjunNh-pc-dDvw6iK5mqf8H5wwcnmjk_zFsp2rXymYnatJvyzedP2UDBsZGCF396GRLZYgZMSmBETEZn0awyZXMMbjtPDaBWY4xIBos9nUkkZfglN6o7hcbniGTbbDm9NOkUlhGOKH3A2VVvHVKLmYrhiIju-Ig3ICf-sjon8C5wg_q2WhuSBcgnwDOrIGp75Q4qHj0IHekOvUgvOLMq0clwM8O_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlZ2SGYstrHckagih8xPJodWFeuke2GIZV_B_ODwj6RUEb1jqk40y4ldEa69O-Ofxo12Qek_qfGXYlpo0oMpWy8KbJ3hLhORXz90YIJEXTadX0CgSZsaw-1ctZfTjunNh-pc-dDvw6iK5mqf8H5wwcnmjk_zFsp2rXymYnatJvyzedP2UDBsZGCF396GRLZYgZMSmBETEZn0awyZXMMbjtPDaBWY4xIBos9nUkkZfglN6o7hcbniGTbbDm9NOkUlhGOKH3A2VVvHVKLmYrhiIju-Ig3ICf-sjon8C5wg_q2WhuSBcgnwDOrIGp75Q4qHj0IHekOvUgvOLMq0clwM8O_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=H-wFte8fJbGqmjBC6VmThvhbPbiHgme4LApUjIcx_Aj_wtEb8G4tcbk7fZ1OQYTKcDreEFTiYZyjusMK3loiY0rBvNb5tw2DyFLoSvSClaDwFVzfkNL7Zdh7G7GJWlu-Zk0b6opysamXO96fh0xnUNGX8_mvJUArHkuPOklpfonOY-5zSnA5r_F6yjBEne2q07qDPj7LQEtLvkiEprDHzoEL3G6CPv0DC3GVsy88KUFYsnDHhaYhwe52K9Mdbld6VaXXUCqJ74NAPdWRDv4Zb_FP0iWD0iIbhlnsrryUoN2LmzerZC_Fav36rZnL0XoAl2ykGPz-e_AVI19bY6TzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=H-wFte8fJbGqmjBC6VmThvhbPbiHgme4LApUjIcx_Aj_wtEb8G4tcbk7fZ1OQYTKcDreEFTiYZyjusMK3loiY0rBvNb5tw2DyFLoSvSClaDwFVzfkNL7Zdh7G7GJWlu-Zk0b6opysamXO96fh0xnUNGX8_mvJUArHkuPOklpfonOY-5zSnA5r_F6yjBEne2q07qDPj7LQEtLvkiEprDHzoEL3G6CPv0DC3GVsy88KUFYsnDHhaYhwe52K9Mdbld6VaXXUCqJ74NAPdWRDv4Zb_FP0iWD0iIbhlnsrryUoN2LmzerZC_Fav36rZnL0XoAl2ykGPz-e_AVI19bY6TzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=Si-cF6yHtBy-S5IDqUlBnDISuYSW-G5NyFWoyNaDZm6CLATmIjKwb2LkjhI3WpljcMWIoajsCM4jrvSoYo2cMrJtWjSapwiuA9vY8BOssjZuk_Pz8EiIZ2aGcAZPnnCf0z4hHLbXZLwkZjE10v4J4hwoShdhyzb_V97dVXEfrQwOheXHbjJO1G0Lefs43o_6ASRPahhX0HrvwhY5zbBYyXGqYQNwpalYC5C8BowTU3XgMeLFIXwzRNBNHd2WNeCmuOJX88gGlgoWp7FoHNODsMAzHznu3eZM_nPhosrXXen64CYs210tI7XOS0v7BWvOxchyDA-54nHOlJKxjRx8z5o8OWSy7SbpifBm3P9eoNPL57--1lXt_W4VKBK1OGH3F1AC_7sOlhv14H2uUFoE0DUlCcVp7LQr-gt7aQZ_uPbiQuan-bhZfTOEVY5TH3IhfFtmdKgVvC_A_C4hPLKwnVAiBYNbHUf8iq7LO4bGbhBpCq-wAEeEt8GUINHwdBqGxsUfENry1koNI8wW-HESENg06zkbKe_fsTqSa-TF6lwgSuWWeQC52zfPY6cCsFt8XcBNTjlfpZlbrtgBo0Vd2CxNlK4FMnnwz7uPnv00wiJNddgQMdxwnv_oeNSZQY_Y8qVNgY2IMYvvVFX8x1CrZoBmLjEOlM2hxYNZOnkuw8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=Si-cF6yHtBy-S5IDqUlBnDISuYSW-G5NyFWoyNaDZm6CLATmIjKwb2LkjhI3WpljcMWIoajsCM4jrvSoYo2cMrJtWjSapwiuA9vY8BOssjZuk_Pz8EiIZ2aGcAZPnnCf0z4hHLbXZLwkZjE10v4J4hwoShdhyzb_V97dVXEfrQwOheXHbjJO1G0Lefs43o_6ASRPahhX0HrvwhY5zbBYyXGqYQNwpalYC5C8BowTU3XgMeLFIXwzRNBNHd2WNeCmuOJX88gGlgoWp7FoHNODsMAzHznu3eZM_nPhosrXXen64CYs210tI7XOS0v7BWvOxchyDA-54nHOlJKxjRx8z5o8OWSy7SbpifBm3P9eoNPL57--1lXt_W4VKBK1OGH3F1AC_7sOlhv14H2uUFoE0DUlCcVp7LQr-gt7aQZ_uPbiQuan-bhZfTOEVY5TH3IhfFtmdKgVvC_A_C4hPLKwnVAiBYNbHUf8iq7LO4bGbhBpCq-wAEeEt8GUINHwdBqGxsUfENry1koNI8wW-HESENg06zkbKe_fsTqSa-TF6lwgSuWWeQC52zfPY6cCsFt8XcBNTjlfpZlbrtgBo0Vd2CxNlK4FMnnwz7uPnv00wiJNddgQMdxwnv_oeNSZQY_Y8qVNgY2IMYvvVFX8x1CrZoBmLjEOlM2hxYNZOnkuw8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtYL-4eId_2Uq6FllBlF-8Ksa1wSmRljxoZPTmXP_3-OcPbo4fLChtgTBGh5s_XG0ZVrcO63ojPa7hNMTFK1A3Nu3Xqb-OnlPMels8qGQ_YxA6IlrYejNUF7x5uESXW3OpynyzoQD02H67zPx_RYz0u1E6YJIc1JH7_NLrvAXEsYvqHhRXtSNU8zMO6mPkN8DUghdHMfTnOTZBKxm3K_ULEVhNxFiK8csyPuDyoo5V8mOOdTBOBL-YTd6LqO4TPGGMo1pp1yoMhX9qK3FjkQJjzanMLWR54u_on6LTNdyB29cS5r4Lrm-9UYZESO1Do9bNBkjV_GNadiUtFeGYYrqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB6nz4z0kprKPKISCcYpRvbwx7jV25BeWh4VM5J_Fg3mZV4E8WmR9mA535Xp91BfR0fZgfZZSTm5zb6cWrgmEpQ88OAAwT6BsBPxf9hwhVXiRFaQ9oBmAmYZ5fShN7US377263t_k4BfZ7vBcAFw69HpgPfvsoqKgDFQAulfh-ipllM4DSNXrpbetcSQUY1bRt037G1EnAinFqDE2GvfPvd3XHz6MopPffGyM8y3Kw-IR2AVhTjQSJEpaaJY6V42GwD5ZPx2rx-BYyyKe0r8XQZFj0QDF6R8Bx5W7f-nXNFKrQ7x5YZo0HH28Dj13hkcNPFI_AbNM9T7txs6k2T6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=ltUtYZapDAybxNdR7tAirBClLd7Q6YpVXMZWSqpKxf03CGObDZA7Fz265nBp4b0hGCuy_O6QHx8oUOI5fY0992XOqTg831fyoL8_hExtGXv6yzokHN3LtPeYfD9whjEd4aj5n89_wppPy7jDSUQFVrdAfXP8Ii8FX9DdDFeoSa3WHBwr0EPnt-cfVxPoPuNpa-6QrMxbD3-AEO7Zc_RIgmCH1PalCx3e96yrT2CaIHvXGLaBuvo4KfdfZVypWeo86U_F_MkWDrhgsLZ2aXgV-6yVRi3nTiIFWFIu-mhcXgqoLABVBzF0QRPro57ueQC35MFbK1QivnMUo8srSpBWIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=ltUtYZapDAybxNdR7tAirBClLd7Q6YpVXMZWSqpKxf03CGObDZA7Fz265nBp4b0hGCuy_O6QHx8oUOI5fY0992XOqTg831fyoL8_hExtGXv6yzokHN3LtPeYfD9whjEd4aj5n89_wppPy7jDSUQFVrdAfXP8Ii8FX9DdDFeoSa3WHBwr0EPnt-cfVxPoPuNpa-6QrMxbD3-AEO7Zc_RIgmCH1PalCx3e96yrT2CaIHvXGLaBuvo4KfdfZVypWeo86U_F_MkWDrhgsLZ2aXgV-6yVRi3nTiIFWFIu-mhcXgqoLABVBzF0QRPro57ueQC35MFbK1QivnMUo8srSpBWIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ZytCzs31nK0N4kL6H3WOsC5vc_wTf2kiY3pyWbwkG8vBsRazbCC8C_3Xa4InxcnRJaKJGOH71q5DCSeqFlP6IzMrBo_4zUaIupuS9oH6acBjD3oPNGzcZwlXv4C9CZHW_d8PREZVzmqjNmLj7JXDE7MRxCXusZ0OousF6WWva56DL1WUiEjm2Yy1EJm33iO6vtRU39WNbIbVHwuR0PjdXCHrioHmHqWrEszeTwdriUtUKF_48A19kdu0IkrlQTkGfD_Ct_xyg2wkDBu-uRJ8nC1ZerFZ1L5LolwLdLTNmo5gJSTYa0qW6i_ZpMURDKGrutfzDP9DdVplhyynaD_wKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=ZytCzs31nK0N4kL6H3WOsC5vc_wTf2kiY3pyWbwkG8vBsRazbCC8C_3Xa4InxcnRJaKJGOH71q5DCSeqFlP6IzMrBo_4zUaIupuS9oH6acBjD3oPNGzcZwlXv4C9CZHW_d8PREZVzmqjNmLj7JXDE7MRxCXusZ0OousF6WWva56DL1WUiEjm2Yy1EJm33iO6vtRU39WNbIbVHwuR0PjdXCHrioHmHqWrEszeTwdriUtUKF_48A19kdu0IkrlQTkGfD_Ct_xyg2wkDBu-uRJ8nC1ZerFZ1L5LolwLdLTNmo5gJSTYa0qW6i_ZpMURDKGrutfzDP9DdVplhyynaD_wKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=Ukqdfy2_VvoOnk5cRcWZ2fM1cqRbNzuahtsC2gLFitwqOw7MqecX5lOgvL5KQf73KoxEwpYWBfy8GRu_hgG9c1a2Wxpqyuu29WTf-5HXLmqwFMvnBLW9YH0a8EEdE4tW7K4UH7WF8G9nXCh7o7IF48NqeEof8C7ooEWjJhsMNY7fz_5wox9M__bjnfICUcP4_yg248i6imLbji4PQgBpi6EvTM0MEUf4N0fINB2fIMyiyadAnPUTKcQ_aJS2tYYuIoeiQRqLuQ5W7_DIiWiJEGgOdw1lTrkuICALhucCZ63ox7_S4fGJ0FMDvNJ3Snfg0kQ-plfgQRfdYODJUNGf2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=Ukqdfy2_VvoOnk5cRcWZ2fM1cqRbNzuahtsC2gLFitwqOw7MqecX5lOgvL5KQf73KoxEwpYWBfy8GRu_hgG9c1a2Wxpqyuu29WTf-5HXLmqwFMvnBLW9YH0a8EEdE4tW7K4UH7WF8G9nXCh7o7IF48NqeEof8C7ooEWjJhsMNY7fz_5wox9M__bjnfICUcP4_yg248i6imLbji4PQgBpi6EvTM0MEUf4N0fINB2fIMyiyadAnPUTKcQ_aJS2tYYuIoeiQRqLuQ5W7_DIiWiJEGgOdw1lTrkuICALhucCZ63ox7_S4fGJ0FMDvNJ3Snfg0kQ-plfgQRfdYODJUNGf2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=O31vpb_95z-FGhiMft8KPLdUyQ__o_i4dCm60aPfsFTShWUQDK2RpTTLtyOqJqyEz_iH5WPXs0rYVOSKq6wwxTmKTX3E5b07hkU5-syeHBF3DhFBTajQeIfvd_maSI7IYJAQafcvaEj8FgDRWG4oSoNr6It7QpmhU2xBftmlwWKpOvAhlcSOpUtyraFU9O20I-k79quBwF5pw39Wd-AohlPoAlfrKKH4jX4xwwJoF8el4CsUgiCCGH0o96u201shbCd-CPntwkMoha6LU6zGP3fJWpYU5v2Qgn-TFZTyqwZPNxMDbKAooIoljWu-a63xzF_CDd83ZWLADm1btSyTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=O31vpb_95z-FGhiMft8KPLdUyQ__o_i4dCm60aPfsFTShWUQDK2RpTTLtyOqJqyEz_iH5WPXs0rYVOSKq6wwxTmKTX3E5b07hkU5-syeHBF3DhFBTajQeIfvd_maSI7IYJAQafcvaEj8FgDRWG4oSoNr6It7QpmhU2xBftmlwWKpOvAhlcSOpUtyraFU9O20I-k79quBwF5pw39Wd-AohlPoAlfrKKH4jX4xwwJoF8el4CsUgiCCGH0o96u201shbCd-CPntwkMoha6LU6zGP3fJWpYU5v2Qgn-TFZTyqwZPNxMDbKAooIoljWu-a63xzF_CDd83ZWLADm1btSyTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGvxT7jHatN0-odZt9flFOAhTSBmKEgzsVI_gD3aDFYEgsKa1VTVn3FocQY8ad88luo500o3TgzUeC8dmRQ3IQfrBBYQATXbSq5Go095xGiZNloqWAtXqj9JFUxZTVRCllMGtWkaMJsu7w6vvzCF5BjzB3hbvOYJWkJlIqoMCwhd5cvUXkmZci72_aMcvv90JqvVnF1xFyygwucLtWlYi2zXQ93u6tF3AANvyBGqkcZXpERgvRgNjtBrPZzH27SCDG9zQfM5nNTpqi84SvLXwZIKFokaGjtoNj6NpHnndYlRAO7wE_8BEylUxz-W_RsRecTy_wjowZEM-p38Uu3Xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9SfjKfNk8olmFkGlkHPHYgv2cJw9PYvkufZWXohZqEyYXvTYW15RayDOWMe20_1vaUOGYGilXGwAJGKA_0ut1HY5OrqMCEMLfkM1LQKtivW0JOP8E-Vo4xIPOb_WVgx_4lE19Dpa3fv5HbmwqL3La7b-_2LQbzvbJjjXO7w72WLUBgplMweySfKxmJ01U5_UqG0iBeOCBGkx3pRMywMmobBNTI2Z7BUfTIChHjcCzBLFqHOqrjmTgv7RLANCcbAA9LCi_YNAjj0ozwvAVuD53Fff1ywVxLsWh1cIbNFyjO9epAWwDrjGKA0WpaoO56S-WOmYCnjXQ0EGjLnuDZIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=HWIjFApi_mPrmu_lvStHkWM6SPezcIan1h2nTGGwzFLCGNEABBj-sMXga-AB42nPiNjcOKwLImZv_IqPEkexVva9H9qHpl1RtYyesrCAyB3hlAy83F9nQxKVlR46fz5mmJb3y06ZyDsk5SZjIDvsnUXN6bSAVRUZQZefNEhB5pcjUHsClDIslzsFL-Ite0wBRLxC7c_7VkA3nNa_uL2tsV_G66Hg-5H7oUP_8LwK0DnxTErnlrex5IMdHw0Mpe9BgSucVMlBWOeJVZ9r6LCqqqnRNOsNTS5eUU2v-HjKAqWT3xUzvkkvW0x6MO5sK7Y1v3oNGDhe4TKVhxzN2kb75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=HWIjFApi_mPrmu_lvStHkWM6SPezcIan1h2nTGGwzFLCGNEABBj-sMXga-AB42nPiNjcOKwLImZv_IqPEkexVva9H9qHpl1RtYyesrCAyB3hlAy83F9nQxKVlR46fz5mmJb3y06ZyDsk5SZjIDvsnUXN6bSAVRUZQZefNEhB5pcjUHsClDIslzsFL-Ite0wBRLxC7c_7VkA3nNa_uL2tsV_G66Hg-5H7oUP_8LwK0DnxTErnlrex5IMdHw0Mpe9BgSucVMlBWOeJVZ9r6LCqqqnRNOsNTS5eUU2v-HjKAqWT3xUzvkkvW0x6MO5sK7Y1v3oNGDhe4TKVhxzN2kb75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=TF-Uc1xg2tH7ODE3OtCCErZpezGTR8hcSb3zHSvpQYgLTS_ht6o_LSY0OMht3YhdiL1-LVzDD4VS4SPm_N-c6RW73FktknaA2bj05UO-sYWg0H2CZtdj3yLqMmB0J0ELg1y5hNZoBNT7f4Qxt6Ej01IwM-GbksZvYLli3-fAL0Q-ExEmpFByYohLScclIV-BE8LbfyTHh0KVX1mA0sI666YM3z7PRl7aZPVtco8vYdp7oSBSwSSxv1S4joewhr19n9TPCbEQ8G7OUCO6O4skdtKuzO0XjhjBwoWOY5KSsWd9cOIZCTdNG9bdHldwDoJ6bP8D90GjD7FQVt9K2Ah9NYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=TF-Uc1xg2tH7ODE3OtCCErZpezGTR8hcSb3zHSvpQYgLTS_ht6o_LSY0OMht3YhdiL1-LVzDD4VS4SPm_N-c6RW73FktknaA2bj05UO-sYWg0H2CZtdj3yLqMmB0J0ELg1y5hNZoBNT7f4Qxt6Ej01IwM-GbksZvYLli3-fAL0Q-ExEmpFByYohLScclIV-BE8LbfyTHh0KVX1mA0sI666YM3z7PRl7aZPVtco8vYdp7oSBSwSSxv1S4joewhr19n9TPCbEQ8G7OUCO6O4skdtKuzO0XjhjBwoWOY5KSsWd9cOIZCTdNG9bdHldwDoJ6bP8D90GjD7FQVt9K2Ah9NYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=jc3La0FxW3QpNzdWp0SJmQfhLJWz19aMbwNNtZvwNEDgsU3EYP3pkiUKrkGQUPBap5Mtd6TpuCP4l-DnmDZ5_CXsAwv_RMHfMrahRcyzMiCnKLESH23w-0XG962-WxdNtMNn33oc_7kopfbQ_VJ-sGCuMedYbn5Rn74Xn_eu11wUZoNHY_OYqNWTC0sy63-fG-S0oCrV3mfswIkHIiJPwq1g5EBNrrm9FB1cLqxQV0y0_aFPyf5xbqbjN_Jtkw99_ew3B62u9cnJVtAtEs0B31AyG-zfYOJ1153bRkRG8looisOg_jUr_r6wK_umVMc-na-Rbfvz-YQlqsHlWhyV7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=jc3La0FxW3QpNzdWp0SJmQfhLJWz19aMbwNNtZvwNEDgsU3EYP3pkiUKrkGQUPBap5Mtd6TpuCP4l-DnmDZ5_CXsAwv_RMHfMrahRcyzMiCnKLESH23w-0XG962-WxdNtMNn33oc_7kopfbQ_VJ-sGCuMedYbn5Rn74Xn_eu11wUZoNHY_OYqNWTC0sy63-fG-S0oCrV3mfswIkHIiJPwq1g5EBNrrm9FB1cLqxQV0y0_aFPyf5xbqbjN_Jtkw99_ew3B62u9cnJVtAtEs0B31AyG-zfYOJ1153bRkRG8looisOg_jUr_r6wK_umVMc-na-Rbfvz-YQlqsHlWhyV7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaYZfsuWzmY6cPaT6-0__b9SN34IWPOH5v1DDHeLcapKGL3zObSQcnDv8_yYfxhEjR5SOOVOvVjDJvJamw4H3b6tw0YSOeyB5zwIOuNGOlszg7i4gugXG1Lk3y-OQKnSjTw9sn5euXYohAi45m5X1UV7pZlV0Z-IRRUOb1dh21T8J3bvJb4MOGKd61um0rpVq_a-fmEMpBVTO8QpN3jdXNi0Sy9DSc5niWJFJablAgiaQf7MReIyN3USAqH_C3-FU36hfzkvTUDXXEwqEycGsAYCxWoBpx-PZWwM9BbEtpImRfMlH2Cs6nBwzJQgY5y6M_eagzItoQ3dwLFobGcz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-OtGPQKIeEVIby8KgHEHCJpjg0ZS5znbSu88fEIvf40_AkZAVAO73ULmz-znlA158_KR5FlmILzhEXLR8dyVncIp2tMwYcC5GWmWO9feCk8JFCTCDqvUOxhKCMNVJsEz9c463gJ1T3Y1Q0u3rxevYNppNt4CC3hAWJOVsss5SEDeXMRXZaNbbZyWYY28tw_WhW6STTiUiCjbYpWlDT-L4EAI92cX128YQsAJhhE1PhbQK3TEntR2vBchQPVh6ci3EzGo1rmpoVqJtyt5HhU7HZ5Tv4IfuZmfUhVTXL165xSF1xLdOAXtjQ7CpsniSnzk93yI-Y8151mRhLLQ4dA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=MplKfswDYD6ktujv9CHLInlbKUb2d5VqPhMc2W7Vm26g3hOvZPm2VAxzqqu9MhTwxCxCtNZ76aJveAoQIZRW4uz7TMcbK_78YnLGmdFMq_ukN0qEYruob5ySuHOPdLDkiuj4OckAGAkSTc1vQNAFjNwij25F4LowuVc8XWVGmoIOVRr50y9iYRYP4bVkZ0NkSOIAqCwML01flhu0Zf5TUd7KpGkav_fjMb3ZYgUs-_cGTUnm6ganD3kKdyx_ghSizH57P92WKkszv34PuPSjyndHF5Ti1U94414jITAglhRxxwqDZz1phraEApCvsTrDSrwv44-N-KtuOpSiCBvPvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=MplKfswDYD6ktujv9CHLInlbKUb2d5VqPhMc2W7Vm26g3hOvZPm2VAxzqqu9MhTwxCxCtNZ76aJveAoQIZRW4uz7TMcbK_78YnLGmdFMq_ukN0qEYruob5ySuHOPdLDkiuj4OckAGAkSTc1vQNAFjNwij25F4LowuVc8XWVGmoIOVRr50y9iYRYP4bVkZ0NkSOIAqCwML01flhu0Zf5TUd7KpGkav_fjMb3ZYgUs-_cGTUnm6ganD3kKdyx_ghSizH57P92WKkszv34PuPSjyndHF5Ti1U94414jITAglhRxxwqDZz1phraEApCvsTrDSrwv44-N-KtuOpSiCBvPvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDMXAE0On6t9SwN2kq-RVQYJhEo7aFeaDrChIG1u5-rLpgs52uQI_3xrBO16GrNDMYaaQTCHkrww2O_fO5kbBf5WYt4rLCTkcCbEM4HJV2QidGnJimf0cFz4UDS3mKrdyYMK0GP7Fi1oLZ6zLV9tPAvFeFDMRIzShrU-_pUWay8D-ubcn1OiZjsIBTE2qpWwYwI_OF0oaFTR_Io3DZ5uUHXU9TrIZS7Ca32LsguXUHasDbnWBYMbxkkAumf80oZSRPObuPBe--wQtbeivP39R4bsVrfQNc5cGaESPcuap4IUHc-f5Xpk7Xl-_SzV9xdpu2gI0TMnI-awrTeQVwmJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMZv-XALoBR4bh0ICF6uU8iJzfdZ-gz61ne2TtSM0NXKrb0iCWeDCAWaM6RjNYdeZ2OHfMIr1gYUXPFYZwL8pLpUs_RmZD94EGV76Le0BGnvtVPbe5Kzm_WHjvrVvt7-yKZbHz-N-gPFtIJQq74dZNMuw2fgYeJwjmtPqMo2rcmFu0l-QfbNB-5DGt2E2QU6Sm0OEopqsYc_SCWniRXjmkPu8EguHdyjRKQN12VgRFNjZzDXeuVDU4RK7rFKWWq6Tf6O1NAkrhOgRdfAUzh_1b3CAawC_My3ku8vLAXU2b9NLBeS0pcUOZWmuswbUsJzGjRJhSOCITAnkWiEJ5P5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=WydcCyAVVcARjBFQxm3CI2v35Vm1z6TyzghWLxgn_xgIFesc6I7tdHz15ocDcSVVylVWhGwiMytBetJbrb0ulGo57bX4TT6HgO4GgFZoxT6ciCfB283p58bS-d35d5NxL7dcJDDfowSY3prLtyVCKbKzagIyNK7W1z5LCzjyGaHD3gyr623YW80ddirbqV96J0NyS4C7-COdVomRFRbKLttcb25yCl6awlkmw93nTGy606IdSGYvW6em3Wrik9hlN32sTgHo-R8HsUp85crk9mVYCqhI1rFclmgUoFlFUU5p2fuiamD4GVJX2zUviOUMO1vq6Ktn00Nr7Abcx2fj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=WydcCyAVVcARjBFQxm3CI2v35Vm1z6TyzghWLxgn_xgIFesc6I7tdHz15ocDcSVVylVWhGwiMytBetJbrb0ulGo57bX4TT6HgO4GgFZoxT6ciCfB283p58bS-d35d5NxL7dcJDDfowSY3prLtyVCKbKzagIyNK7W1z5LCzjyGaHD3gyr623YW80ddirbqV96J0NyS4C7-COdVomRFRbKLttcb25yCl6awlkmw93nTGy606IdSGYvW6em3Wrik9hlN32sTgHo-R8HsUp85crk9mVYCqhI1rFclmgUoFlFUU5p2fuiamD4GVJX2zUviOUMO1vq6Ktn00Nr7Abcx2fj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nndp1meo0fyMmE2m9rOjONajkHa0GUMiJEUqLRhhDmURSCXldPmShH0bG9esX5T7qG-zylI6770IgGI5Eql7ZLjAIGuV_wjep9CgaI5hH_4ZdLTUeWrcTC_Il-r6vhLevFbPHSBQjUrBa1oO23NrPbfTLayapsDCMe3X1itYEn5s-sAF0eptydX6sMj7UqfX9fCcpLBX3Np1aUedQGDc8k6oxQ8-lvIeTalrBuG6ezadTuBy8B3oH9QbQ-qdUNiDEeE4vlvCGpUB5LH2BqP4OFCnr3u9Cbx7GgR6YS3wSDS-Gy-RO9lkaEsKIT4SIyUzLP3tffx0gUjVgocYb2rgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj6UWKEdmeYvtNbXkAp0Mxv54YphDt-cZDapDhgogepxUhB6PtQH8vuipVhXZLp5U-Be6CPDvvSvhGEV7Jx2SaJQ25SHydwg53j0U5WB6x2HgWCo6zZqsziG0h7HfJrpXjPOeZw83Sgv2U29PAP5h1mjRxqRE2LVSRYaytdiw4oK95fk3ZwjBfzyh4k2wHqrYHJInavfDYTI6iUfjdY0Bdw94FeMw59_HoLDsoB42FUhqleC5dcuqkL7C-O3M1ssM-iX2xbCWKwDBjIVRinCCuLRKphn1Xfw-7F0hcOLhC5UYFELETCLpIely3ssyW3iuEPoE06OZZjNCuilPtw27g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=Ews0-QDhn4wZzxkiTMi7KrR07dawTFC36aLPMWU8hNsRI_WN68N2aJtKdbl-yXoY7I6ucCikoBjSmCt25jkEkntvDoKlvkcMZks5hakmKcKeUsgR1WJ-pJkRhRVSNLN3RTUb_vQ8NI39ZsO0AEcfcAmXRINrPHiCHaWbie5LAngNtYhX-deEMiRF0XGHCi4jv8u-t_Zo2mMWLF0Cn_vkEz9RDRUWak5AQ3W3hSTaFnchgQ3UFxP4Cb20LPUz1EdbQkcIOyNaoJrypJxbB6VPuvnwi6ruH42jBm_XfQin2LCWBKHxnY_D4zy6Cn-AtxIqFcv6uTnzGZBnYQ-PhURQTwZ2Q6FY5poVzY1y9NMnx_UUv8KMHeHTyWkW3bTRpk5WiwXqZYop7L9HabBG63hSQlPHl-_9PHsTpfRe9E23YrAZgd8FViQGUq9idEKx4DNFaa1s2DlSTxJu7mQz4GTLjetkXHgAKsXFFJDncu5nJ0I7rL0ArTwVD1yF9wvBnfvFm3DmUcU9haJ6LT95bmEiEasNtUiqHjOdmi2dDiXNX2ganPfp3ufN1t964e_07sj4I-cAI_N-3V1s2NTf_XT3yr4NvcRTI1gTkpkmQjr9x8CnOuggEOB1_ZQAW9td520sJdRlFKtdrVf-RT2lKmwkVXXVqFjIftlAP4E0HU3VByc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=Ews0-QDhn4wZzxkiTMi7KrR07dawTFC36aLPMWU8hNsRI_WN68N2aJtKdbl-yXoY7I6ucCikoBjSmCt25jkEkntvDoKlvkcMZks5hakmKcKeUsgR1WJ-pJkRhRVSNLN3RTUb_vQ8NI39ZsO0AEcfcAmXRINrPHiCHaWbie5LAngNtYhX-deEMiRF0XGHCi4jv8u-t_Zo2mMWLF0Cn_vkEz9RDRUWak5AQ3W3hSTaFnchgQ3UFxP4Cb20LPUz1EdbQkcIOyNaoJrypJxbB6VPuvnwi6ruH42jBm_XfQin2LCWBKHxnY_D4zy6Cn-AtxIqFcv6uTnzGZBnYQ-PhURQTwZ2Q6FY5poVzY1y9NMnx_UUv8KMHeHTyWkW3bTRpk5WiwXqZYop7L9HabBG63hSQlPHl-_9PHsTpfRe9E23YrAZgd8FViQGUq9idEKx4DNFaa1s2DlSTxJu7mQz4GTLjetkXHgAKsXFFJDncu5nJ0I7rL0ArTwVD1yF9wvBnfvFm3DmUcU9haJ6LT95bmEiEasNtUiqHjOdmi2dDiXNX2ganPfp3ufN1t964e_07sj4I-cAI_N-3V1s2NTf_XT3yr4NvcRTI1gTkpkmQjr9x8CnOuggEOB1_ZQAW9td520sJdRlFKtdrVf-RT2lKmwkVXXVqFjIftlAP4E0HU3VByc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdAamwJi5DHR4-8h5FZYJpxagaFQgXb63ulwJI0-4OXSrcKOOxt-1ZF2vf_iADMmINWwBjaYw0mCy3d4Uso5oL2Y6e7jf6ZpCWGPUDdXytjEjKvwXc9Lr4k0vgsKolfC4tZusfDOgn_Wc3q1-aaqkrzqsvXbMvAAF8SaKGWS6bMtyvF90j_0dY_2m6Wk3MQ0oxQ8ZsrTmal0nemUV6E6S13pNr3iy0kuTIINqs9Fi3dHL8vw6qFJyprRwQfsWIEJA6ELZfKnaK9aDiIU5YeemFU8TfFQ_nQnhxbUMlaSTL1dOpNUD36d0BvcpO15vMHOFhnRgG7TLePBLiRch4grug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EUlI33uswfm-cFia6KoYnSk_HeDM57zz-gOKHCjRbbFqC1msd-aZxfyDqWkK51LTV9if1oo-nodYSzzMT0BgErUzFS8Y-caRTGp0IEC7LpC1uPMdY42Bno6cbPImKErw8FzFYPdfTVH6Pso_zH2gDjIJ7z5fKHQ0x-VAvS21IZz6c8yMYrWh0Q2PsAiQuVZj6KPGuiUuJRBaqPHH10Yo3kSue8wLmM7K-_4ztGW0uamo7vsjkPJzDu7faKmARQcGsDnu0p0AcSquW1OHmdDvUUyxXHlVzsMbKQnpyg6qA_UGzdVvl84ScSMM7nc0Th1HlmH0AVn4c6Z0M__MjZLp1lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EUlI33uswfm-cFia6KoYnSk_HeDM57zz-gOKHCjRbbFqC1msd-aZxfyDqWkK51LTV9if1oo-nodYSzzMT0BgErUzFS8Y-caRTGp0IEC7LpC1uPMdY42Bno6cbPImKErw8FzFYPdfTVH6Pso_zH2gDjIJ7z5fKHQ0x-VAvS21IZz6c8yMYrWh0Q2PsAiQuVZj6KPGuiUuJRBaqPHH10Yo3kSue8wLmM7K-_4ztGW0uamo7vsjkPJzDu7faKmARQcGsDnu0p0AcSquW1OHmdDvUUyxXHlVzsMbKQnpyg6qA_UGzdVvl84ScSMM7nc0Th1HlmH0AVn4c6Z0M__MjZLp1lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=iFY70ykoi8XbqfGu5gjhJpomCVWxDVnQGUG8IFjn34Vm_Hm4fsZ42vdcGYjn9KmjPd1_kC5Xq2vSaLrZZcJY_BA35uStWhAfH60f5HNjMF0JmNQAach4wPJqWySjeF6qZoRTQQNHJYTmYPxoXS4TBL700gIxlqn-jsi9OR2GONtCaiJ2MUMQDkv5tXJ3w--s3ERuxkVG0saegf1DMI0O5VF4q_E25Qx_ivOmlavscbzZETt4zmwlOCqrpbyRi8QDEEhhsokMMcYwRbMjuScrjXGfcVCKYOLNhSvHFBiT7y6ed_ftamASPq4I6w8i-hTTw-rH8mo7U6aliyfMxov-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=iFY70ykoi8XbqfGu5gjhJpomCVWxDVnQGUG8IFjn34Vm_Hm4fsZ42vdcGYjn9KmjPd1_kC5Xq2vSaLrZZcJY_BA35uStWhAfH60f5HNjMF0JmNQAach4wPJqWySjeF6qZoRTQQNHJYTmYPxoXS4TBL700gIxlqn-jsi9OR2GONtCaiJ2MUMQDkv5tXJ3w--s3ERuxkVG0saegf1DMI0O5VF4q_E25Qx_ivOmlavscbzZETt4zmwlOCqrpbyRi8QDEEhhsokMMcYwRbMjuScrjXGfcVCKYOLNhSvHFBiT7y6ed_ftamASPq4I6w8i-hTTw-rH8mo7U6aliyfMxov-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSFAmMim-0m8Lr5lANeUKGCgi7obl4kxmb5rl7GUzwo7lhUjmPTD6Qgd02qMaj-qF5EmA2Zzs6iIXtj9b2UxR6Bg1xlKm39ZGYOx0wgwNLA_M_54YFLrDA7C5B_4VOztwBwwcCCJ_LNcx7KxAXuTsAjnqSV9LBzNLmhAUgDr2PDpC4Cwv_JojEYtTf5m_FhjPNHfu4PTxbgXtIacyk7GM0FRmZqapvtVotdjDpoAC8oYu1jc4oGwmgqo42P17EPqZaBgtnhR0fhcMX0j3-vMgTq1bU8xg00V2U6qJ_pNNl9qTjehyN8hfuEVirZvDwleWzYNOm8N4sKrwA0TsocWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=qOb56BauBBXAWD-fi6eh_mkuxH1ZHey-e7vjeQfJNR7r6I3XjxiKvrQ7av8fwVYA7egPCxnKi-Ol3t1p1IGWcYyVyg7ekkwLiqz9-XxzeI44Ee1pwjumf3M4WUcCUkK4vI-hCDT6Dy_zTK4pXX1jnkWki84SjNoilLCQoXDYRU0ZNVweWQGn3F3MglMYCEHoXahlUYEFVuYWpEWKJCMM2eLWlCnWP_TeEn1U88hfGMAd2AJ0kFECH96QtN3gK51ZsgkB4LILWmV_TlJFniU2EyC7O_3W1e6C9vpfTNshFi-bAyY1TJLKHX622HsDq8xu7Vna_hCxjNIfuGDR-riCuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=qOb56BauBBXAWD-fi6eh_mkuxH1ZHey-e7vjeQfJNR7r6I3XjxiKvrQ7av8fwVYA7egPCxnKi-Ol3t1p1IGWcYyVyg7ekkwLiqz9-XxzeI44Ee1pwjumf3M4WUcCUkK4vI-hCDT6Dy_zTK4pXX1jnkWki84SjNoilLCQoXDYRU0ZNVweWQGn3F3MglMYCEHoXahlUYEFVuYWpEWKJCMM2eLWlCnWP_TeEn1U88hfGMAd2AJ0kFECH96QtN3gK51ZsgkB4LILWmV_TlJFniU2EyC7O_3W1e6C9vpfTNshFi-bAyY1TJLKHX622HsDq8xu7Vna_hCxjNIfuGDR-riCuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=jnltGRxKdIlpE7CxPmkv_IdpA4E1quNbn1rM_ifWjV9uaiVA0C5ktGWh3l-F2zD09J2B6Fj23R1_1pCVZDiKmHo7DDUBM7GQiMl-mUzvbNVBrdPxORlMe2TknMcU14kYk6wCQHXGrJ15pxd5AlLRjg9Tvu-b98VX2jeD54KtZXUtYryrP3WHryatnX-2xbGLFeZ7yJNtOEYkJ1h6Y2LXx05I5tG_1y-F_TVclpqW5A5skLYYtyomp9qyxBOxSgYfeO5kNFVxW-KtHKdF8-L7XKJdAik_w3sky92nf4eWm0JjJCbpTCkKav06VaE2LkO8pwBy-mReufxFLvTFDaiTy5-vRB9eACEKpaQBWTaUp7sBJlIF1HFkBykXpfcFE-cCdMf4Osrcr45q7YlR-h5CTLIirneIihqMBQPF4dCVC3ttQeeK8Yoc8V50id89iaGcZ8D5r4Xrk91v1tO9_05PbkFoQDc_W5DhPURrvL98bwsw_lSJ_J_hEcE1PjtkGovK9Hae_JAQEGODQKrtkUhvEbpINpPgMIN3LOT6uBpkRFMELDkQ-4LXKNg4GN9ggwdrGVqwNp114c4Giv2CajXOyf5IIHpMLNTIk6TeffmUtCGnJOsvamr5H2bFUVc7DFP_1k2t-ReWNZBnkvQcbR9X8DnNkLvvdTLsUX5CNhcBJX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=jnltGRxKdIlpE7CxPmkv_IdpA4E1quNbn1rM_ifWjV9uaiVA0C5ktGWh3l-F2zD09J2B6Fj23R1_1pCVZDiKmHo7DDUBM7GQiMl-mUzvbNVBrdPxORlMe2TknMcU14kYk6wCQHXGrJ15pxd5AlLRjg9Tvu-b98VX2jeD54KtZXUtYryrP3WHryatnX-2xbGLFeZ7yJNtOEYkJ1h6Y2LXx05I5tG_1y-F_TVclpqW5A5skLYYtyomp9qyxBOxSgYfeO5kNFVxW-KtHKdF8-L7XKJdAik_w3sky92nf4eWm0JjJCbpTCkKav06VaE2LkO8pwBy-mReufxFLvTFDaiTy5-vRB9eACEKpaQBWTaUp7sBJlIF1HFkBykXpfcFE-cCdMf4Osrcr45q7YlR-h5CTLIirneIihqMBQPF4dCVC3ttQeeK8Yoc8V50id89iaGcZ8D5r4Xrk91v1tO9_05PbkFoQDc_W5DhPURrvL98bwsw_lSJ_J_hEcE1PjtkGovK9Hae_JAQEGODQKrtkUhvEbpINpPgMIN3LOT6uBpkRFMELDkQ-4LXKNg4GN9ggwdrGVqwNp114c4Giv2CajXOyf5IIHpMLNTIk6TeffmUtCGnJOsvamr5H2bFUVc7DFP_1k2t-ReWNZBnkvQcbR9X8DnNkLvvdTLsUX5CNhcBJX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHxPul8fL4uPHkAMEkUMntSarHEbHOxUUl12axx62VVcjFQeLewL_60kF7H0l8fadC6jZhQX8CrWfI_VvWa20cCcvkBuUc_H8sdyYv1sXI0UuAFJIhbgmcouvVEF3FH2iSBiS8mPCOlQc10PKpHoHCRf33WQriCeYAxZt2RyNwx4VHdyuayKq-qzrZet0UPmVyYBkrt9JQUqBct2sLAIEQYswpK-SyznCt63fxlW9uym1OgSVmwkzqXCUghHdP1R6zSBTZQAp4Ov1cqc7b-rdgsu1emCa0kq9BEYhOmaYKoQWv6jdpqdHrbDeTTu7riAu7OVhpuYej1MCU9Syr7m_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB-AqHcuwHWRoDZqdzfmcTUQTiwMsfOw7S1-5o8wlKbe2xVT49ZULS9Ik7SAXzxXbpkYhLs1uOGC6t7sKXoqNg6qw9ydzr5ctDP3Pn7-TP-k4U49C1SNyBNRnf_tRa3-4LRyxnPIRlyNWk1Di89jKjnnxIeaTA9U7i4pTcdBj_8dLodXGJQEzc-VL-gzsJJbXBnHNaoaqehTIT-2pI2DynkieyoX2iybp9zHDvB5ve4K8G-MonGytVsFwYj_ft7rWOHsZ9K3UL5UkZJd__YF-fMGngq5DoXgB2lkuls_OsrH_pDTYLIVLCjsws5G3GxJmVqSxrUiySVLdWC-EkZjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arQvZgprUjVlhCHWvCwsjWjFingEErNQER2aAxJNPJyiB0rlF8ckoAhpR0j-RBPWv3Za_Jm-PCB6sd_ICta7SCbmZcuB60mgFwY6-QuDe24TjZ-E24x2xPN-co6MpttA-XHz-2THYg6ComWzB9Qgh_AwjaJXKZF-Hqp4Ltw9UCDfQwMXHzeup4Sdv1lRYsqlXnBTZq4lWW709JF7SCTTUw4mM2WXgYC0ZxauDADK3l5h6nvZY10T2BHc0yVpXAXm4221ZPqiP6omEK2buAOmL3xGavUh1MMvDD4hW38vnXWRntjVteFarskzmSAzido8swuqRkPG2XCoyWVh3Gct_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAxFtn-kslf1S2uPbihIloPEKNyeX530Sg8-9wM0QWBLu30b_Z7dRDO9v5VgrjaxHLWAKSyuHiYk7FFSrRkWs3sjmzpNt6kWZltJ3aw5NJODmwo2S6hU1QMLQ9fyz6hQC-j-b6sjNLyr90tc3_OD8qVz2FWMC03r5Uk_1BYS66cMmPCrdgNsj-VBu8bT6mLtTbSQYPcXD6kmFP0B7Z9CVZ3Jkqy-wHlkFbvcHqqgojuaP7jqtTXq0CPdeoQCMR3sCt6SpuGurFNnJhRwFFTfT3iofWK9S57CAG9AjqTiCZYzU6gFs9Ie48bizq2yM86yAISJJ0EoHilM0zERRUiX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfj-o5ALJDtLXxx39jXvAxIJjMWwOmhbkbogE7aK6tmW4x4lB5rwUnn8-Q6Cym_iKw1ElQ4Jnj5KAKu6kXbAgbDw94Dcl7Wvw3hkSV2CRlqWRTu5VSoh8HImuc2wrF1yWTM-vL3DwnxBOTJst2aSPAByy8BJAoIv7oGH_LpTYUYcbi52f8p7PbV5QcZiTUe654qPzB5a0BuXElbxPgg9mErJgehq9AxogWJuiZTMbGkoeKRK13TBoEZB_ZmjEoHjz-2OX9mI7YPGNH8W7TgozW62TfyEya_paoS3jTdP20zNz7-pph02VbqyrrwlIlnOcfItLXjoMe6uddSTru0abQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIplefl0dSbi8BQvMLK1zyv0BBAcKgykeNim8vpgbFFZC3Zdm9ZmLv_b0DkFyCnkh1j64U99JsZmuKyIxgpiEYsg8Geo10vADmIIlMLpFVrF9FFE5qzJMGEE99h5n2tovk9ch_qUVeXnZWGuJvDGm6iGyu_CPhRI5ifU667DRcZ3vvmy6bpf-o0q02jbgFewLD3eLYbU8H58a5nSIiFyD7_nurKoJMNPM1JbhyulKNHK5yWe3rAs02e0rQu7dkh3i-76I8tEatDBxTv71gaPrvMAzY6kLT0_hbWxIwtN2kRzjrKD_hDfGA-RuhU7DIOBoaIWlq0_anjKaTwqzm95Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qmPppmn48QdBPLJR6uR6vPZa-_O70yQAcXk_KATp-O56x2u449eD5XVJVtAWPBKyGxjD8MkdsMTcOXRVHtWG1sn5-8Lym57I6zAuV-DoCjH-Ds03i_m72kt615O1WLPnzRiK4qWJ9sKH0RRYrxJR2ct-PF4rbOhOcvvOZmq-_rKzptIHDAnm3sH7Uq2t36q2qshgVyJBrgr7DaBOTIrQtvwuFbIlOHiEVkE0zGmk-kZDEG4rAo3tNw5KbYPrYKDJEJclv9BmObeoL84zl7U6KgFTMVRSnOX6PvyjbS3NCL0OcFfvQfo34wP2gWZ2olzZUeAGNwFw4nus4-nu3NOXwXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qmPppmn48QdBPLJR6uR6vPZa-_O70yQAcXk_KATp-O56x2u449eD5XVJVtAWPBKyGxjD8MkdsMTcOXRVHtWG1sn5-8Lym57I6zAuV-DoCjH-Ds03i_m72kt615O1WLPnzRiK4qWJ9sKH0RRYrxJR2ct-PF4rbOhOcvvOZmq-_rKzptIHDAnm3sH7Uq2t36q2qshgVyJBrgr7DaBOTIrQtvwuFbIlOHiEVkE0zGmk-kZDEG4rAo3tNw5KbYPrYKDJEJclv9BmObeoL84zl7U6KgFTMVRSnOX6PvyjbS3NCL0OcFfvQfo34wP2gWZ2olzZUeAGNwFw4nus4-nu3NOXwXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkFEFYCPyUth7IlmNIJbG3D5juiTi_XwkaU8hubMoHSH_e_EPzAV2w-DfxqECTAp_Kq4vMH_GrLUcNnIbF7b4iFymHGyQAJxNtVK6Eod5gmmXP2IKZ168tT6ecHiVukGJeg1CRCOuUn_NW8VqKd3zHVNPo-jg1FHvWTomY4UeyN_5gJF18rk5Q7ygB6C4u8c0h6M7kjK2n5PlXmmraUw73iNu70Cch_zKx6xYoHLcIuasZdG2DKPeeIT8mQ-h48pzL04bfe93VlCyMuq3K6cP0JvDagb3bhisOfLj7WBWzoDFd_zFi3HemDBU2DO22-bfq2eVWeeZp_B6rEu4LKkkdxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkFEFYCPyUth7IlmNIJbG3D5juiTi_XwkaU8hubMoHSH_e_EPzAV2w-DfxqECTAp_Kq4vMH_GrLUcNnIbF7b4iFymHGyQAJxNtVK6Eod5gmmXP2IKZ168tT6ecHiVukGJeg1CRCOuUn_NW8VqKd3zHVNPo-jg1FHvWTomY4UeyN_5gJF18rk5Q7ygB6C4u8c0h6M7kjK2n5PlXmmraUw73iNu70Cch_zKx6xYoHLcIuasZdG2DKPeeIT8mQ-h48pzL04bfe93VlCyMuq3K6cP0JvDagb3bhisOfLj7WBWzoDFd_zFi3HemDBU2DO22-bfq2eVWeeZp_B6rEu4LKkkdxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=sHQHjsmpY8MgmOXDE-y0yMKMLh-3xjnFzpFaoytpPX6msI64G7r9_oNuWOEYDHMjahh6p9UInxOzZfgx4Y5W0jmZWCpr6h095XirWcI2z-vvM7vdfFBG95UIEZmtg5mQf4WVD9y9lFokNlKk6LBFtyGwUNITFbCuS2V-ycDT5j7RbvgPYGlK6y_vtDK_3fU7YiKr42QbutBQEp3xPgEqkT_4OzprqBc50dELJOj1qJzYOmu11UEFX8psnUStxygoI6_mqjRUyy7R2Y9_qmTi3uJeDUsOi9b0L6vm83zZWGbjiL0ME466eMrJ6ar_BhdgmH9MG_OoZey5EhOdzlcRkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=sHQHjsmpY8MgmOXDE-y0yMKMLh-3xjnFzpFaoytpPX6msI64G7r9_oNuWOEYDHMjahh6p9UInxOzZfgx4Y5W0jmZWCpr6h095XirWcI2z-vvM7vdfFBG95UIEZmtg5mQf4WVD9y9lFokNlKk6LBFtyGwUNITFbCuS2V-ycDT5j7RbvgPYGlK6y_vtDK_3fU7YiKr42QbutBQEp3xPgEqkT_4OzprqBc50dELJOj1qJzYOmu11UEFX8psnUStxygoI6_mqjRUyy7R2Y9_qmTi3uJeDUsOi9b0L6vm83zZWGbjiL0ME466eMrJ6ar_BhdgmH9MG_OoZey5EhOdzlcRkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
