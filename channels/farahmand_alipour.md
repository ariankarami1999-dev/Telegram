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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInibF3peiLlxkW8UF3xqJyasj6hZbHKQ5_zaIodU6-wu95PjUz-ARmzyErw6NSUfWQi-L4gSj8U-x4xR3DFD0O-inPbsvgzJNJ-Tk-cWUh6fFHVK6v_K6n0ZyoCLaeaugSindc8RGDAkIOqohSUzQwk1MMXwMC30t2rUAUnjcq5Xado7XHAU0cipNgjXQzEoCJZJ-hhsCWpy57tYR-g8YO1hrYNMQEnsGQFGsIuMpes7DcsSFsYHa1tSctbeagFAmKrPTyqsKLK3bFbkA1VqzUTrBcV4pzLpX3p1UlNuDbBbwQN-QsDwRmJY5vqcop-O6bcZqNb8QgNvnCva65LHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgPqcFaWZZG89IicQbt_w335ZKF3gi72yFokgiLZCyQkFWXknif3plxktRDLsZtWy2ZA6C2dY7TutGpKBS1N-xtNYBrqil2_R1MZzCJBa4V93G88X-I86QHLXSJfCItLP7HdyjNhR3C_KtS_Fr1cQFGs0Kg-5tB-ECzsfCT3WDrsWngUvVeRdzGanO-lM8T5pBIEMoW-S-pH6nbxm-Z-T1KIcm4G052FwoZw0tRk-EhzoYimYMKoveh3ZeUAQRyxr1uqffDMdDMQIkCoCmuYjKW9LABd6ka9L0r1AWExxAu15WXK24Lv50MtXWnRF711N3y6TfovxSUqBrbpb0JclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIzGQOKwzR3wq2EVjTp5Ptz1LSPIs7wWFyxfNes2xMQ-0LyS-G6cb3iidoDT3-mBahCVR9G2lyu8u9lwGIxWtlJdmr7wy4FaoaFJG1bO-TV48HIiHMcAoyhFvUhXc94tZZHSl-TubN045feZz-7TTBf3xPBeLsOjdvaAd3gLJN1aEjRgll3CLzlkT01f-e-qj1mqkJbdyqEHoCN-Wkca4nFBSL1vznTaewkzFf66Se4pHJ4oGE1IcQZoezEMdA3titnwcRyIJSV-ShMY_CkVseokS59C4bXfRB9D4EVaqKJflR5jHrlEeHgoM5I670ns4aL9uv-OZb_1ZMGSEb2FJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsM4azRY54yj7jY1nhMJxrecosS8Z6Gnox1VDii6EefVvPzFlRxCAH9jueX6wWZhsQpyrowIzZzJ2Uk7LjTJDmM4jbFvzhX0Uh_hNiXz65WAa_EZWQsYrNIzJ-7WEA3okFxrbWCddi1xjWMk3AGO1nsMA7-dx3DUsjQ8AKJFIgro75fSNcFrqbkUlVbGAKoOd6Zh2WIQGNyZHAdQnei5DdQvrzkVlkFfhUo-84YCglQaxORWqnJ9L5XJKyXq-0etXwS7tnb4DC-9jG82tYfFcy3Ps7P2DtdbMvK7Evt2fPXQ5IDkLjGcdUgJzHq-dqfMlK2j-HHIygNfvS95nWRYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=qRyF6pPEjGfMKd2kQ7GX_wXuemfAyXyvEoE8YJA8SElL5hYyPMvwH0WNTR1YtzBUEHM-3XGC_baSNO6xuoGJOazAu4T_4O7yJT0j7X-KHetEzRHAEIYmTk7dAmMiIssBexS5nkcsswHTJu81W-bzC34nUMUpIyULibV9m-Z_g-F8YTan3yEVJtd3BftjDW65wZjn1_-bOfEy8BKBPKEykunXQ7dqSVhZavPqHTCD_Q4luyuiWjN5JcDDXSOAWU_UUg5oZ4OGgC2VAPP8hRIdZE7Mlrn3amLIc_te2J-cPUsO7koHEHqih3RgQrs6VW3KCWc9g6cQgdtBdKr_ISDbEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=qRyF6pPEjGfMKd2kQ7GX_wXuemfAyXyvEoE8YJA8SElL5hYyPMvwH0WNTR1YtzBUEHM-3XGC_baSNO6xuoGJOazAu4T_4O7yJT0j7X-KHetEzRHAEIYmTk7dAmMiIssBexS5nkcsswHTJu81W-bzC34nUMUpIyULibV9m-Z_g-F8YTan3yEVJtd3BftjDW65wZjn1_-bOfEy8BKBPKEykunXQ7dqSVhZavPqHTCD_Q4luyuiWjN5JcDDXSOAWU_UUg5oZ4OGgC2VAPP8hRIdZE7Mlrn3amLIc_te2J-cPUsO7koHEHqih3RgQrs6VW3KCWc9g6cQgdtBdKr_ISDbEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=i5-bdZvUp57-PNQGV1uKWjLivC0m72bLWYrAex_xKpma1O9NutDUNnnzEcaVVTLEbm5jk9CwQMq45yLMSAWVNB4sVvsW8URICp1O5-RDEYmRmMCoa5PcT7GhE0R0CkLZATteBchmUSi70Dqb4k6xY8t5qnQHAnTwSULB2zRuYCZaCNeDW2ROfbrbjFkOktypjr_Ql_LH3OWAUllMuN7nICQz1SKzNyXRH5EWxMDDVvIiuIrrn4OCs_wQQHfx7Q9ZYf3oY_7MdKyeNe9XwajZOwh4mvDdKQ_QzPxaOukiybHT0gXVWLMeAHXirwN601G4cyFLZza0Y12keoA_eYUM0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=i5-bdZvUp57-PNQGV1uKWjLivC0m72bLWYrAex_xKpma1O9NutDUNnnzEcaVVTLEbm5jk9CwQMq45yLMSAWVNB4sVvsW8URICp1O5-RDEYmRmMCoa5PcT7GhE0R0CkLZATteBchmUSi70Dqb4k6xY8t5qnQHAnTwSULB2zRuYCZaCNeDW2ROfbrbjFkOktypjr_Ql_LH3OWAUllMuN7nICQz1SKzNyXRH5EWxMDDVvIiuIrrn4OCs_wQQHfx7Q9ZYf3oY_7MdKyeNe9XwajZOwh4mvDdKQ_QzPxaOukiybHT0gXVWLMeAHXirwN601G4cyFLZza0Y12keoA_eYUM0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIMULuE4s5dR2__9Jy6Eh_b9ou8rsVTWMCIzqP7G-o5OCbIxT3ZnIkDZoVfzTE3nawAaQxGJLRq3gBdJKvgaZV7JmgtqufCy2xTsUDt_kygWvw8q7EnpjqubGUau8OMr-3fwrr0IMs-aIjyDAEy4_EbiMJxCePZZdVQ1eee58YVUDqVRdVzv3GcEzcrHfMGAWf1yFD2aRiKlY2bcBxPMVjFjY6G_74a4Hk59DMIfXsz_qgm1kzIHnz81tF4Rb0DBI3qYTjIzQv5fVQfT6kyLpJ8XGHcOFCvB1ySGFzlTJtZStbkR6wJc5A-IFvGMrI5l5nVJDlH2FGU9kr3gq4oCeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsZnqQBKU_z4lWAKhWHfF0N0cRCxaR1NhqsyjYw3Q40lTZQtETaOxTUAeHKKdNQbtZInGrSJLVGOL4-YsiIzVMJrqLWRn9-8Qp9qzamoZHFwcD5311UXZMJ8IOeCALFpUHGblAEOjXKF7ZrX3MfLhI0KP4nSB4_B456peaJWnem-PDUf6vOP3bY-JHRIOurYWv9UmKfIOyQJgFOe4cwajEU1t_buzwAiRz0pnZ2Datft-WQzhCKOvXE_4xIQb0tyh1y2Gyes3ZWYoNT5IartOLpVDhxEVaImpZR-g5G4Z_iwRv7VkFAvp8JtBLBv_AD2j-L72Zzk3HD_V8gkFNrlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=RRTxjPzkauYXAVCttAcxX9FlopNkze_yYi1dYm1aCye8OPP7XHKkoYpcDyO-nM4iZa6fXhAm6p6unpi9srTkDF5fQsKsBetZCMmSWgDEZVDOr7pmnL0IwxYRYJRMAqS03PTEzHk56YnaSGXtJ6ldMeAzMvd7d-ctRUUAfAYntV5TuHmHnwAUfRskf1FvxmbXXUhQUdeM_8E7CbjUtE9d970KBC4B_o_s3q3oe4GpDDgo1-aPFqvQq5H68SVqGKbvZa4p1P0XDDz98kbcNWFbTX6qQdj1TdxVSRZ5x9DrEFZ7R_lB4s1SxF3ypAk45MbS2gxxLLCS1i_n579NQmpI9zeckxIqC_bQ7AWQKZPp_Em105dUzSYCtt0gmAWkeifRk1yt42hrbUF2ktoBWfQCfbiQ3VdxXmVY1gLCbGxQOY0uZvhI2l6RrMy42j26z_nRYzvBpQWooHNZ2Mzh9dFxYAtgg_7-7rZj99msLVr2iLpe17BXCkLCmv62map7SPhbiE8tBh0HexwuK0Y4-mHSA8XQbYF32FcEcnfBK-ttGcMWG39SjOnOlHPwbtEYH41Z_3jI0ZtlzV01IA95H-in0BIkEbQHHtjSprcPby0xG261jVt5PzS9tw0EjYDWil9dFLkEJqU1xfKEn4B7AQXbzRV6UrzclOW2TDcDrZJ39R4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=RRTxjPzkauYXAVCttAcxX9FlopNkze_yYi1dYm1aCye8OPP7XHKkoYpcDyO-nM4iZa6fXhAm6p6unpi9srTkDF5fQsKsBetZCMmSWgDEZVDOr7pmnL0IwxYRYJRMAqS03PTEzHk56YnaSGXtJ6ldMeAzMvd7d-ctRUUAfAYntV5TuHmHnwAUfRskf1FvxmbXXUhQUdeM_8E7CbjUtE9d970KBC4B_o_s3q3oe4GpDDgo1-aPFqvQq5H68SVqGKbvZa4p1P0XDDz98kbcNWFbTX6qQdj1TdxVSRZ5x9DrEFZ7R_lB4s1SxF3ypAk45MbS2gxxLLCS1i_n579NQmpI9zeckxIqC_bQ7AWQKZPp_Em105dUzSYCtt0gmAWkeifRk1yt42hrbUF2ktoBWfQCfbiQ3VdxXmVY1gLCbGxQOY0uZvhI2l6RrMy42j26z_nRYzvBpQWooHNZ2Mzh9dFxYAtgg_7-7rZj99msLVr2iLpe17BXCkLCmv62map7SPhbiE8tBh0HexwuK0Y4-mHSA8XQbYF32FcEcnfBK-ttGcMWG39SjOnOlHPwbtEYH41Z_3jI0ZtlzV01IA95H-in0BIkEbQHHtjSprcPby0xG261jVt5PzS9tw0EjYDWil9dFLkEJqU1xfKEn4B7AQXbzRV6UrzclOW2TDcDrZJ39R4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irBqiTwbiRNHf8IIREWX0I9YwPhIbxKCSQvHGHQFqPA-TEV7K9GDPdBt52icrh-YmeKTkW5w6_eyeIvmxZIXNTUJkSjYjoXrJxSQLKfBC_9xmAVLzo6nhMVnfS1Ve9fUO7ha4RMRox6hkLlbiPjnpznJueArssgTabFPNcWV3AtodsCPcpsUdH26TavPG7x_DEmII6tllJuA4_HTvWWLvZvXLxmXdzkBXnfshR4P-Nq7K99QL5EGuJvUSWeeD1Y1KRsaHNc0fbT9E7qF1-o9nlcgyTBgq8Zvg7yDINXXyvScOxvt1pNdHBQ8eQEj-lVrewe3IFK9r_Ti7Co9XcDErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcLv906OyTxYr1es9cW3_2FacEYnkCwanNE9Rbso4foDwaFLxcGC5tXzLlehJoMVdU0wiLniDCn0BRMMjhgnX_qK4g5uJ_bKTpklviljVSDERZY_ImGiBrn18xvO8ABcRfjEy8np97ABZ80iqbbE3kqB2INcW97b_nw1GDevCFOKWxORwoGNoznbw8TN0EiUj3V9RcPVpCcMVCVHRTHHY9UDxKpRakqnmh6Py5uDqSajgKebU2vThL6jIWRYqxYJWfuaVQ8nykTJFDs1X193yHgEjtWkBno5R73vDvX6pUYcIeqKoRSK4GNPCkH1Et-U8QaeSiQo5AWolF_Q8POn210o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcLv906OyTxYr1es9cW3_2FacEYnkCwanNE9Rbso4foDwaFLxcGC5tXzLlehJoMVdU0wiLniDCn0BRMMjhgnX_qK4g5uJ_bKTpklviljVSDERZY_ImGiBrn18xvO8ABcRfjEy8np97ABZ80iqbbE3kqB2INcW97b_nw1GDevCFOKWxORwoGNoznbw8TN0EiUj3V9RcPVpCcMVCVHRTHHY9UDxKpRakqnmh6Py5uDqSajgKebU2vThL6jIWRYqxYJWfuaVQ8nykTJFDs1X193yHgEjtWkBno5R73vDvX6pUYcIeqKoRSK4GNPCkH1Et-U8QaeSiQo5AWolF_Q8POn210o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=b21nvMmORCN3zf2WacWzC-ZnmA3YbbTE1IeXPGHIM-a6L9Wle0sBUZjgkCmktjzd9jogDeajLrbpzW5of7djtSAHmHc1ORoUatSZE3-FH7ekd20ta4qqM1oG5ptYJdQ3nTdWvApS_7Hjw6Vhp3Ng8SAInF25tVc4kWatXZsHuTNADtvO8NLiDQB7UZLjEC7zWQMz26ntmPxPJyAIG4NfOz_xrheLzfaElFyvpML4ewMD6m7_cKVhMg1cVtiHK6E6CY2sGjegtjzGnIYpu0mkxcZCjI9V0-6zJJ0kABTrwpCNA8yLiBsWMoxcqYHfRqQrm7Zrd8MgS9qQrj9zAqPTBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=b21nvMmORCN3zf2WacWzC-ZnmA3YbbTE1IeXPGHIM-a6L9Wle0sBUZjgkCmktjzd9jogDeajLrbpzW5of7djtSAHmHc1ORoUatSZE3-FH7ekd20ta4qqM1oG5ptYJdQ3nTdWvApS_7Hjw6Vhp3Ng8SAInF25tVc4kWatXZsHuTNADtvO8NLiDQB7UZLjEC7zWQMz26ntmPxPJyAIG4NfOz_xrheLzfaElFyvpML4ewMD6m7_cKVhMg1cVtiHK6E6CY2sGjegtjzGnIYpu0mkxcZCjI9V0-6zJJ0kABTrwpCNA8yLiBsWMoxcqYHfRqQrm7Zrd8MgS9qQrj9zAqPTBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=LhmmVkHFigtXNuFNXDU10YiQ1rqw_ktDyEFpvmyXSGPHngHRq8ryLybmV1YCpXw1gMQvM4LN8XI1E-6Lw5sdNy8s0VGFjaSBORyjcZFJk_XaswPDXP9nuCQ34c5UQonPWmXWK-6kTcwHoIrjHqHsGzGEV7s7lgsYq73djmmPjrUy5wFJdeR9ubZXMoFCuPCLkABiZV_qqIQPc9vSQYd7TJdIWmPOrbc-tWKZ0crwOatlsOdfYjoaN8-WxVRalAHbMo4Ndrv50L3t69v6VoxXIcfATBdeN-_DOJsCag9WURv6DYjM6JSkkIFNgAhzrEXdJZlVQiCGEWUzwGr9P3gfAGXC55GcU3LYZTMljNaIrSKjnt_0AAYmRGJLoBZfPoclKcXaCY2v1bM5LllKuTG1bEXsortStYEFfZ1VCo9JQRed-WUJ2RNJXB0w4_JaV6SVYg8QUMD8RMFAsJo7KE565YrzsWXhhRS1zga2D4ZyxUfRCGWAPEwGUh_NjCTwKytH9rPiEt6n2UQco2C9ffEPvRojER08S-WSG79OOcwoNSQp2rz3iiWUJZGvA4t0SbYkMsKpfe5AapyeKqBXoC_aXWoqZZ095CGaFbzT54n3aR750DbMIYFdss_cO-25OvscfOQuSXiDKz1y8OYUwhByT2wPg9WLcMT5IKRvTrTC4RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=LhmmVkHFigtXNuFNXDU10YiQ1rqw_ktDyEFpvmyXSGPHngHRq8ryLybmV1YCpXw1gMQvM4LN8XI1E-6Lw5sdNy8s0VGFjaSBORyjcZFJk_XaswPDXP9nuCQ34c5UQonPWmXWK-6kTcwHoIrjHqHsGzGEV7s7lgsYq73djmmPjrUy5wFJdeR9ubZXMoFCuPCLkABiZV_qqIQPc9vSQYd7TJdIWmPOrbc-tWKZ0crwOatlsOdfYjoaN8-WxVRalAHbMo4Ndrv50L3t69v6VoxXIcfATBdeN-_DOJsCag9WURv6DYjM6JSkkIFNgAhzrEXdJZlVQiCGEWUzwGr9P3gfAGXC55GcU3LYZTMljNaIrSKjnt_0AAYmRGJLoBZfPoclKcXaCY2v1bM5LllKuTG1bEXsortStYEFfZ1VCo9JQRed-WUJ2RNJXB0w4_JaV6SVYg8QUMD8RMFAsJo7KE565YrzsWXhhRS1zga2D4ZyxUfRCGWAPEwGUh_NjCTwKytH9rPiEt6n2UQco2C9ffEPvRojER08S-WSG79OOcwoNSQp2rz3iiWUJZGvA4t0SbYkMsKpfe5AapyeKqBXoC_aXWoqZZ095CGaFbzT54n3aR750DbMIYFdss_cO-25OvscfOQuSXiDKz1y8OYUwhByT2wPg9WLcMT5IKRvTrTC4RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E449VDZ9yGkJr2yi6zK4oznCzpnWaln4UGXYC1FAgT6jGEd3tjoIOfB1np4AaU16F2J7lWQvxjgU3EdIWBYizLR7N9ZMOzmYkqIjUEsPVnurPxYyWTjnInNKzaDzmMH-1CipLVllgsn5AMsOL0Lbm4L37WG6zkgbdJU8OqnvbS3ZhTIdpNqoKfr-hjV7j8pLbzWI3yFH2SzQJw2uNfl3HJPM6geTGrm_CwwtguHppq_wkv5WyCiifW3u4Js_vCeXh2iZQPwEotlVi3_3E9wL_cf2tVOjt_VIpsz7PcX_pQs4kMF4yyOQU_s8XrktxgeXt8mBXB-dqfCuG5wtzVmXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anMuPL0Acf5WNLDt_qXAK8ICtW_sqtyAb_gb4i8wo9DEzRtAAwW_Va5qvF_374sw5G99yqeeSZe5EwMd0O65yvVOYa_Bm6Mn7r-wrR_vXSU2XVd4umBqZKu_Lm8wfQ2cGJZXPYXTfNu3A-bpFvccZ4go9gJV9F_Xs4AI8gk2nQL6yGpW4jc6_ptjkvH0qtyIui-mVXr83pUMpKXIy0CvS4nbQmH1Rrc4-uiM8DM1kWmqxSccoYB_Wnctx3A0w2wB2rgl0Ll_ev5DM_jt8U7t9KIK5jHLHV_dhlaQaNj4TCOSxYAg8xyUOkJhZ1quZrsAjyYFm5zWhH5VTQWPT3_52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=I8io9x_NfJJMHIdWibcWn5JvpuWVNgifhLQf35r5nIhvfooF6ozItRJhWLT4bITI00qaUq8WikVe9WTb7uqWbbazV7zex1BnNmgknmibOzt6mzlMuJitwOdJp156Ux6ioIifJHJLQoDO_DQPMGjNLa11GGxx2Dcp8S4DK9w6ZjRJOyKJOXalxPxRnn2Yc20AueYlxzkihVN0hPRG9IRGVIfu6Yu_7qOngyCqfrru6cypVPxkYiZtKUU8ytGHaCpVBO2kxdTTGkilB0nkX_LIDmBQzL_oV7Qx20Dv9XYRwmayhYkmzWVhmTjgpesjjiCyShTNVaI-9kw7EjAnGauY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=I8io9x_NfJJMHIdWibcWn5JvpuWVNgifhLQf35r5nIhvfooF6ozItRJhWLT4bITI00qaUq8WikVe9WTb7uqWbbazV7zex1BnNmgknmibOzt6mzlMuJitwOdJp156Ux6ioIifJHJLQoDO_DQPMGjNLa11GGxx2Dcp8S4DK9w6ZjRJOyKJOXalxPxRnn2Yc20AueYlxzkihVN0hPRG9IRGVIfu6Yu_7qOngyCqfrru6cypVPxkYiZtKUU8ytGHaCpVBO2kxdTTGkilB0nkX_LIDmBQzL_oV7Qx20Dv9XYRwmayhYkmzWVhmTjgpesjjiCyShTNVaI-9kw7EjAnGauY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=Dg4ngNHRJiw0l7PkMnIFaG6iMFKBSOZQbybXro56Rtn7VIKeqfHMdUeGh-0SlAbDD4S1p3siAhKJnK7sVTlgPUTprdQZtdGIp5QSs6xpmGsOteyfyUX3sAdnTgycG4kDf5XhEcQvlCxkQRoiyJo_gPIbHzLhWp65aYq7FR974Aa7MADt3VyMu1qDjs5Qtw4AgD9K7nZJZMQyNDX6m-dCeLkFVSEfgJSLOUYh34WfEhQGS--LuV9tJQTDTCj4dbaf5Vi-ggmeHow1TxIsG3u8-wmvzthE_BMP81lz0XkgyfVFwZm5UP8jnsDj7AhFqHL8LABXK4MnJz186w34hq18Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=Dg4ngNHRJiw0l7PkMnIFaG6iMFKBSOZQbybXro56Rtn7VIKeqfHMdUeGh-0SlAbDD4S1p3siAhKJnK7sVTlgPUTprdQZtdGIp5QSs6xpmGsOteyfyUX3sAdnTgycG4kDf5XhEcQvlCxkQRoiyJo_gPIbHzLhWp65aYq7FR974Aa7MADt3VyMu1qDjs5Qtw4AgD9K7nZJZMQyNDX6m-dCeLkFVSEfgJSLOUYh34WfEhQGS--LuV9tJQTDTCj4dbaf5Vi-ggmeHow1TxIsG3u8-wmvzthE_BMP81lz0XkgyfVFwZm5UP8jnsDj7AhFqHL8LABXK4MnJz186w34hq18Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=eU44-bW1By-2UvsX0Uz8zSy02ayyTSyNIl_2EVvOUS9PFG4x4bu8FwUYp6pBawZWsB4nfpQMKLCltXz0PrcWtea7lTlXw18mokHesTKk6ZeH3TXl18H5SkwRfAnDb6l6ZKGnYejVFwG4Vaw9MM9FP2cqgoNNXm9y0aVh5yBp0QcfqedESbSvhCfTyi3xWeUvAdfWqKDKM-7skuvjPw9MnX_Dz7jak-ynTQqCTaMYa27Rske1OCquXMj2mK1EyOKeetnA80y2XXBNx4V-R_y3p4kk2_lM9RBkxx_wONACEpnTXrMH2SGMNPe3BIHyZ29uVU4vITmYx_gHbYxz45Pomw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=eU44-bW1By-2UvsX0Uz8zSy02ayyTSyNIl_2EVvOUS9PFG4x4bu8FwUYp6pBawZWsB4nfpQMKLCltXz0PrcWtea7lTlXw18mokHesTKk6ZeH3TXl18H5SkwRfAnDb6l6ZKGnYejVFwG4Vaw9MM9FP2cqgoNNXm9y0aVh5yBp0QcfqedESbSvhCfTyi3xWeUvAdfWqKDKM-7skuvjPw9MnX_Dz7jak-ynTQqCTaMYa27Rske1OCquXMj2mK1EyOKeetnA80y2XXBNx4V-R_y3p4kk2_lM9RBkxx_wONACEpnTXrMH2SGMNPe3BIHyZ29uVU4vITmYx_gHbYxz45Pomw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=u8MeXtVnUkToJEpDkqx3EGZxjo_l0p-O03sekl_w2MMrv8IV1R5RtIRPFdVPDU0sBRwN0DfCwmJk1VASbmeFwm3ZPDpYPZpNQucVdqA0QVpkY0FgT-8QEW7XIbqMO5_KXM3cly8dUSoGsKR6ftet8E7yjqC6_cgBweYf7Fq143gS7sE_cHgz2exYodTiu2QA2GwDRfAq-hrB-cH77errprMuJvcxTchDH-6QS2QhIBndWtoRTGiOVNHKCUaT5Gxm4oWTTqs8u4ZKi0f2v93X6pBjKga6S_7VbMdCncWLCJfbJNqRPuQp8QTjMtAV_Tq_hPNLjFygmr4y7pFSiPKlxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=u8MeXtVnUkToJEpDkqx3EGZxjo_l0p-O03sekl_w2MMrv8IV1R5RtIRPFdVPDU0sBRwN0DfCwmJk1VASbmeFwm3ZPDpYPZpNQucVdqA0QVpkY0FgT-8QEW7XIbqMO5_KXM3cly8dUSoGsKR6ftet8E7yjqC6_cgBweYf7Fq143gS7sE_cHgz2exYodTiu2QA2GwDRfAq-hrB-cH77errprMuJvcxTchDH-6QS2QhIBndWtoRTGiOVNHKCUaT5Gxm4oWTTqs8u4ZKi0f2v93X6pBjKga6S_7VbMdCncWLCJfbJNqRPuQp8QTjMtAV_Tq_hPNLjFygmr4y7pFSiPKlxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8EPRoiNfdUeoSDQAqvu0Cxkna7oMq-O9kczYK2OcooV9lQ6-jcgOMOldDK3RQ50uPQ_c_3ZTMLDqU2IyXFk4lmSoutF63HFiFw_wpJVbJPKZHf2_aEctfRiHWqotY7vpwwPCF86jaroO1K1BMlYqjZZa9SQsETuMXl3VaSbtXashRQZxbKUcQva-qjr0WMkqJLPpgu_wtngaZgLTqwMaf7ojUPb0ABCriGuOp7DUVlUkZOEdUoVGkH3I0QmhUJDPTfQocl59qi0XEalDmnwuiWLgIEJcTXG-OclEv0YaWYXToXnEb-LKnKXVDgWXyBAQCb9QTIVFHP_qQwEXipnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no-hjmbGeODZzx9AX3Eihdw-8csqin0O571ay9Cm085vZe8Hu1EiHSU9OLUn_ShfEsrvbbm8aY-KJDcfTfCmQTRgGcyZP0o-7LVkFFwEsuVqSMpgzHLYKXNgirgzn33_HQbGiIHQPLUEqzJBmp4iWauQsQwi1QZ1MeYiwRrX7d43ICj7pJ_meBIT5pdVpjR9y4sVtcTkMHZkosCoa1gk2NLg9wOxlBj9xJu_7oZQH1LE2RwLrk4DrCCv4TDxFyLAvNwWM73v-Ze3w8UHgEaKMZek39YesHcsbgXg3SEeTHTnu66xi2063K1Y6rmhq5-QzrAH5B6v34fEUKEFMDsWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=D2auo47rb_EgA745WMbidHLiHUxj7A9IbjRqePFyzXYNsK1hLzwsaaxiA-89nUqf0iJ4nlI2ICnECNQfz6GEz_CBVmT1d3UJLUDSHxsPnLBagK-nBgLBFY0FRZQPSMEO5kPt-O_YFagRxGUJ2pauMMRyHoHm4zkRQkRyWJ3oVyHlUrz_7lrNbIEL1Q8E5SPlFec4ErcYtnMsd7LaGcEPGPDk18IIK7w6W7qB4FxHB2GRgFcFKMC78XvuMOhyLitl_8d5URk_EL_A4zwEmWPb_9pJBu0VYU2axI04St0ogyKNh6CDCo_eNsq_z41vI-QArxZAAc394nJe77AFrsBAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=D2auo47rb_EgA745WMbidHLiHUxj7A9IbjRqePFyzXYNsK1hLzwsaaxiA-89nUqf0iJ4nlI2ICnECNQfz6GEz_CBVmT1d3UJLUDSHxsPnLBagK-nBgLBFY0FRZQPSMEO5kPt-O_YFagRxGUJ2pauMMRyHoHm4zkRQkRyWJ3oVyHlUrz_7lrNbIEL1Q8E5SPlFec4ErcYtnMsd7LaGcEPGPDk18IIK7w6W7qB4FxHB2GRgFcFKMC78XvuMOhyLitl_8d5URk_EL_A4zwEmWPb_9pJBu0VYU2axI04St0ogyKNh6CDCo_eNsq_z41vI-QArxZAAc394nJe77AFrsBAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=f7nzvVO14Nj5AlwJ-p4Boo7KxXE4PRo7OD2lnSdd7BW3r2RZ313UY9llI2-xEVEjvUEY88ZqkY3xsm4iB8RslcjhGpcEMa57IEE38QSil7MjaSY9rKRTzpn5MMfB1ikU-L-zsngvjZ5Fd7PTxbWRqgQWztV9Ax7vhQPjcv71M1W-k_4KOMOBsf7dtSp6rJZSgvM9gJIif0WTc4VCzIKcK8nikaz7d-dXE9_PWoI4UMKkN0Ip9b_CWwi1mJakwnH5DBnbKCQbMXILESVfE3kGiInf4pY-yXzEGYiHAMZNYc9ew39X8LUsWxn4dEtDNGVkpi3sL9JFGSZvOc7R6G27jCBx0kUeBV97t8BUnsOxO2QcJFYvIfpmMa9sOpEjHcsIr8N-aQ00o_CES7kWcFqK7dkwhwO0OAFxx54_Ma0EpB0pyUXDtRKHO9i6PPVnscxPWEeNJ_NyawAW6p_zq82cu3O7nD727qOYIWn6qASMcxyj5yeWagbvFEH1mzQD5xqbiowCdWRLhTVUPSl-Ir5PIdjwKLRuwwL4b7ZrMycBG5hn6iTYI_KekhWLHhPeymwPxhB0S6HnsG8apUozmjLJEXleYG7FGs9sr6FjvSQkk5_hNM7ga8fgwK4TR7MOSHbekaGCb4QR0Z6h8rEy84LGZ8e6l6X2wQRXUf-x8_SSJ1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=f7nzvVO14Nj5AlwJ-p4Boo7KxXE4PRo7OD2lnSdd7BW3r2RZ313UY9llI2-xEVEjvUEY88ZqkY3xsm4iB8RslcjhGpcEMa57IEE38QSil7MjaSY9rKRTzpn5MMfB1ikU-L-zsngvjZ5Fd7PTxbWRqgQWztV9Ax7vhQPjcv71M1W-k_4KOMOBsf7dtSp6rJZSgvM9gJIif0WTc4VCzIKcK8nikaz7d-dXE9_PWoI4UMKkN0Ip9b_CWwi1mJakwnH5DBnbKCQbMXILESVfE3kGiInf4pY-yXzEGYiHAMZNYc9ew39X8LUsWxn4dEtDNGVkpi3sL9JFGSZvOc7R6G27jCBx0kUeBV97t8BUnsOxO2QcJFYvIfpmMa9sOpEjHcsIr8N-aQ00o_CES7kWcFqK7dkwhwO0OAFxx54_Ma0EpB0pyUXDtRKHO9i6PPVnscxPWEeNJ_NyawAW6p_zq82cu3O7nD727qOYIWn6qASMcxyj5yeWagbvFEH1mzQD5xqbiowCdWRLhTVUPSl-Ir5PIdjwKLRuwwL4b7ZrMycBG5hn6iTYI_KekhWLHhPeymwPxhB0S6HnsG8apUozmjLJEXleYG7FGs9sr6FjvSQkk5_hNM7ga8fgwK4TR7MOSHbekaGCb4QR0Z6h8rEy84LGZ8e6l6X2wQRXUf-x8_SSJ1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=pdCLUhOS9P7TfmWzvwvRRnTKLYCDC3ehRbryyqYkiGsWrU0kDUqLQuVQ4zXl0oBHvh8P3AqiagfDzfCfyfhWlbEhbOqNxhHeXFiDbhGRczFySwTWtF0H9ba5eJbi113w8n-Pd4y63IYjxiQ4EzzIrhUyYcB4FVX_n7SKCM_9H2JMIJ_VcGnmOt9pPbm_Ck9Iss1KidoV7UC0A923ReqM6FE0E_u5kCs71bdivenYa4sTcI7dhxqlB9xOhecD9jcFEJgt9IQy3EP1xScbD8apiW-Xbxw_rQwJwDJgRQH-S5p-Ey8PxZjLGqaq6EAePxMlMTUsoOwv5uMxvCLEcGIgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=pdCLUhOS9P7TfmWzvwvRRnTKLYCDC3ehRbryyqYkiGsWrU0kDUqLQuVQ4zXl0oBHvh8P3AqiagfDzfCfyfhWlbEhbOqNxhHeXFiDbhGRczFySwTWtF0H9ba5eJbi113w8n-Pd4y63IYjxiQ4EzzIrhUyYcB4FVX_n7SKCM_9H2JMIJ_VcGnmOt9pPbm_Ck9Iss1KidoV7UC0A923ReqM6FE0E_u5kCs71bdivenYa4sTcI7dhxqlB9xOhecD9jcFEJgt9IQy3EP1xScbD8apiW-Xbxw_rQwJwDJgRQH-S5p-Ey8PxZjLGqaq6EAePxMlMTUsoOwv5uMxvCLEcGIgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hvlp-Kt4SgykL_MMpu8ZXCxEkyWznWYQ1W95n88RhqnnHaNTKymAfI8WW26fLdbQ3um2nUUBDFFJIXLK3IkB87-m1lH5HUhfdd7IB6pmI18s2lAFyXbK-GTtATxXM5MuJ8ucAqaTi2aSo8dW7ZXEsI4B-zklukWHEVtrgRhcNK1NMdvKqMGOFKlLe_BJjezZkf8glX_Fk0j5cYA7_Zv9VvDqOqPcuXqrKO0iKVGcgrgei9N1e21hel1pSHqJE5FMJDAl5eT-_wsVyp8ravA2JstHkQVVN2FNbzrvrWdST2bKkwfrLupaDemd4zO6PCEOXTLbCWqYrnqK13hgjM9BTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Bwfoe_9lXwglHBo9RepeSHKBHvPG6s7eiA-gTLL3BmGMrUitp6eIUNVaD0rEK1bgoGyAa4aP9qeFPyS2Ad0G7OIlkjCcMD_lYd38LXX86iRPuWeFZ2BSaf8uAb6h2FUx1_nV-CVYdyEjbtx3gMSfDubxs34fo8bq3a-sk3PqVfh5eRxW1ON2M8_EF4U40LRsRzznJHL453gRGuaan0xJvuMFpTzCotBF6gBlyUxuwe5PHOHJQJ8-k-lZwBb6jZbyjIgzXZtNSijMLLk5BdRw8C_ZoZNoCNT0VInFeZQeMFl5NZiiSPQUJZeCJ7Vmsrk8CWQ4Ue0cNtVMmfK9IZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=mu6JoWxotMhZC8xGJpohHLU_L96aTpgroO2bJKc4SjLXLIcPxIf2P0hwmDh9AyQLb4rrwvp2JmEzvjXEj9Uk2OrhpfXznFeGy_CeVoj5FfJupGOrfMH5YVJ-gKI8fKZE05pJChE33FrvnK3UmC6nAPsG0xGLV75OBh2ah_FDB-U_d4yat8gyNJaYLptCY9QroyYXXJeyAztKsi7i2qV3i_CMiguCtmmzZTQhpdHO5_3Rwk7jBDV3uOobGKETYVMhskSbYQ2eT4z1KpdAw-fA81D4jCzRLAYUuaAxNIOx_KzqpNdnoeQ24kw1NBSw5k3yCKZIQmDIsSwzwHK5YUoB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=mu6JoWxotMhZC8xGJpohHLU_L96aTpgroO2bJKc4SjLXLIcPxIf2P0hwmDh9AyQLb4rrwvp2JmEzvjXEj9Uk2OrhpfXznFeGy_CeVoj5FfJupGOrfMH5YVJ-gKI8fKZE05pJChE33FrvnK3UmC6nAPsG0xGLV75OBh2ah_FDB-U_d4yat8gyNJaYLptCY9QroyYXXJeyAztKsi7i2qV3i_CMiguCtmmzZTQhpdHO5_3Rwk7jBDV3uOobGKETYVMhskSbYQ2eT4z1KpdAw-fA81D4jCzRLAYUuaAxNIOx_KzqpNdnoeQ24kw1NBSw5k3yCKZIQmDIsSwzwHK5YUoB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeDUrkHgT_m4OYJ422h3G5bjE_7lBkaz_51fBiRpUrZcxgcdRWPaGoq-b8eZ5b1De2A_O131HTSMkU0BXJbtScOrIyHte6p_nhikupOMtCnTcYt0uJXQVk6BLWXsCDqlLiFQ5CmPsUdyV_dqDcnreC6_KNUtjT2OR2Sf17Po0XtQOchmgsMHniKrYG4pIh3nd19jBaR0pfjLjr-b8cZ59T0uO0Wo9tDUDGcF7KZpFhsuDEsR0xp16z4W7a6Zr8gnELGjwXUXQZ5gqu2C8QlS0q0zjGTrJfXPhhht5gp_pwH11VVJtRikEV_0VXpuLwiGl9p980rXgRih1YXUwAHgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWn9BW-FasmacPCL3wSIIashkvvLN028oh9QIk3kR85Vr68JElzNkinKhlWHhNmLWS5uxcfzO-aOA1WsY-yx14LaFCpZ1eR0pCGvPwjG4fGm_vBCtn02XloPbvv2HTdLEI8f_or7I-OLL_JvrxLprp88Wm9QB2XciIBiOqWP6T6gZ3BHMWeX7gujKw7n4IY0Xe9TmN_Q0RSnKWZa4yxXjeIIXZzYUb3ZTfmj0QXu55m0o0ijEkIyGShYSUavZtX-azdv-MMh_jB41Zb8dUPo77A5BPHNOLUyjJBZVtHDYgIHJYk7KWfDs8ncUGFUsqZZXZu3lXEa1SNtuTUESQmXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=OZVkhrwBXr-HQPlb_NrBfSX77nQiyV7CX5nurUwDJGwGyPZicnWzCfQbxYCMNvSvHBm4tzcvbYURbtybCtRxhSJbqhqframXC85ELvjQt_r7WHCA9uTgiYVmXbd-7jfHj1RTbtIKIs8M8BJETrzWAMhvfgz6JtE8cf21sL06gnizmJINr1qgCw2IX2M5_VKenwc8_gfSnc4mMjA2s0N2lCdPXvgGWXKN2RTmqqqKYUkV2_4lHVr9W2pLMSXmUaiKuZnNAOMZVDPW5IMHPSeLhTLi9av7AsLCDWPd1T6IgzbMWLhOqtLLhcNNhbCwmV9N8egOXwPl6L8QtK5Ukw7Q4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=OZVkhrwBXr-HQPlb_NrBfSX77nQiyV7CX5nurUwDJGwGyPZicnWzCfQbxYCMNvSvHBm4tzcvbYURbtybCtRxhSJbqhqframXC85ELvjQt_r7WHCA9uTgiYVmXbd-7jfHj1RTbtIKIs8M8BJETrzWAMhvfgz6JtE8cf21sL06gnizmJINr1qgCw2IX2M5_VKenwc8_gfSnc4mMjA2s0N2lCdPXvgGWXKN2RTmqqqKYUkV2_4lHVr9W2pLMSXmUaiKuZnNAOMZVDPW5IMHPSeLhTLi9av7AsLCDWPd1T6IgzbMWLhOqtLLhcNNhbCwmV9N8egOXwPl6L8QtK5Ukw7Q4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4kY3ADIBnQuM6FKAY3fNPv47oJpdJAnG3ictQTm5gER8O7ewOAkFWQm0-SyyOUyd2uZfFq98vZtJ3qOmuURY8T0lIOrvyyiNZ-l2thLWmlXBKIV_M_xUp9CH5sGuw-NQaRdg-5wU69FVH7StlKGMH0dBOxDsTbtIZG7gFFtTNGa4G8V4juMaZsWuXX79xkFjEZKZBRhQ-VoMgGDovelmpC8d1E7iNyhNrN4nEwApKMFM70OC42V9a_XDdzNZkmiWi0vPIztdkahMUC2SQYOJizEuE3j0ZjnITPqzUfGOGy0uBMsu4N2xQ-EfLYqNU0RM9eLExuVjoV1pojha2S6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0zAg4BvqR03w2oaxI0QnaqVB4cPvLVM4_W0jBzF1RQzu28erFsmoPiafJjt8M0r6FzUWWs3Qs0SngAuHt4iUHE3E5G-VbrsD6nJkhCQw6gCMkZ9Q9zh5sb-jMPOwlzW21WcEPlloMGVOPzPpSa37Rh3f9YPpekWz6k5tdAiYLtHQau_0wRbigEaJ7hjfqU0JhcI8z4f_3j7_Yr9y7I8zFvrl3zD4ppkc-U2Ob9cE9II2F8OophBgaSZHjSxOttr4N6CAfPPJS1fsHzwf7DxjEPx02zQMd8LDEVuGtE1t3dQQmNUA6N-_cBNBrLfiE4NtRLktMDPUVglnHBTW4kUMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=dutAHbKnRGlIv5pcZKXNpPinTf0Nn7cW5Ph1KHfCKpPs5CMmyHLpb2F6jhm1ICQ4UjO6x_scoFrJuXG-QYyTlwkUABYv_4S-J-sojWPGKtfO9xuyZLWlKfHHiYXqW0UjPXsZ6VJhz5pDL-lTBkzZxrjvGuCsyrR0LREDqFXrReO4AnBeuRk5xzHlUUIBhHyDWNBxkqg9pnbAv5xJkPp3ULDyE5EFt1HCji49F2e9Qr0Xx7cUnOp-28lIhe_SZxXOIk75F0D0tJdjkyox-VCckUcuS8wT2yHA2cxERMnd-1BiF2QnlIKUl3bBiJSimk3VlrZ6z2LBVybFUrlbs5RNwnIGUPg_Tvzobj9_lyYEeAbzPsZRsG2fdQAO7e2GGGQIFqFj0wyVoQPHzkoKBFSlr9jtFYJumAYHFE_3_r4WcEc7M_MpYHY1NZpSbupDxzRDo2Hh7F4FQGp3jelXk3WrukeilcAtKM_NYo40_t76U-4ZhobqYaDfRof8bsYSk7soF3jVXpdjQ2krsYOfeESI-K4wgj8YHgIQ4umizcHGSlERche3B7YSUM5f4KPXYsB6zKqd8dXPdc00xYmvJBCTqoLBSA7wEX-griHEN0_jj1ghz8QXzXT08dvIpqn7Tn_q0ttHwvRFz0AB5Z5A8bLROeK3R0iwhd9OYigZK_G6UyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=dutAHbKnRGlIv5pcZKXNpPinTf0Nn7cW5Ph1KHfCKpPs5CMmyHLpb2F6jhm1ICQ4UjO6x_scoFrJuXG-QYyTlwkUABYv_4S-J-sojWPGKtfO9xuyZLWlKfHHiYXqW0UjPXsZ6VJhz5pDL-lTBkzZxrjvGuCsyrR0LREDqFXrReO4AnBeuRk5xzHlUUIBhHyDWNBxkqg9pnbAv5xJkPp3ULDyE5EFt1HCji49F2e9Qr0Xx7cUnOp-28lIhe_SZxXOIk75F0D0tJdjkyox-VCckUcuS8wT2yHA2cxERMnd-1BiF2QnlIKUl3bBiJSimk3VlrZ6z2LBVybFUrlbs5RNwnIGUPg_Tvzobj9_lyYEeAbzPsZRsG2fdQAO7e2GGGQIFqFj0wyVoQPHzkoKBFSlr9jtFYJumAYHFE_3_r4WcEc7M_MpYHY1NZpSbupDxzRDo2Hh7F4FQGp3jelXk3WrukeilcAtKM_NYo40_t76U-4ZhobqYaDfRof8bsYSk7soF3jVXpdjQ2krsYOfeESI-K4wgj8YHgIQ4umizcHGSlERche3B7YSUM5f4KPXYsB6zKqd8dXPdc00xYmvJBCTqoLBSA7wEX-griHEN0_jj1ghz8QXzXT08dvIpqn7Tn_q0ttHwvRFz0AB5Z5A8bLROeK3R0iwhd9OYigZK_G6UyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ0Othl6BRD1qyq4hAyDOev-qPirwa8dqawtKFcGfMsnYkzRi5oXMKOMLEVwf8HkvOCkLKSZdFVcCYHt_HGZxjFIQBDuu0dpwOSZiOOGT97sOzDPWVmgldSkG2hqai-rQTi17R_Mh4Pk4tCOmSZjMc8lErJLmJzUqKYrdY8TLOg3y31fQ_DB3d4jNZUUi6dVauL4W48zHHPRS5Q_GtIQqeUW3qIDNuFeu6e6gFT-dlUgeLsi0XxNsPaQ9drNwiDYr1wMby1TrCvbyWC6x549DW8X9TtnpPnLPzcUJrBQL6dCljlMFQT7WrulD4c7ic_Hd7DHyRLJMbnGk5oKRzMTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV1k0_GYYZARXX-KpHLAhgwo7RXN0Li_FUkucuo558jMwt-VDIgN-C0dNqjTP2WHfeO2ram9763-r2tJWtp2hm4yWRaMNnvv4NCimZBN-oLPczdHYWl1MMqDhPWhCDPnYcbpw709yu4lmvBgoX4-DH-Bz6QT5d6FRZqB8P261jmUe0_Q39jvaIMdr3TprUa9AfS4Mv1eXw-u8QfBWYXJ3kmkxmAvXrhZP5nemWkgBt2Fzqr680HjWrJ4rT2yof6nsmYy9r7vfeWwpMBywNN2XvxCSsnmGmHSqMAVZDOaIFB_PAHvzLTDQbCIPl3hu89AkhvL79N3Kel2MHWvsrFtrITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV1k0_GYYZARXX-KpHLAhgwo7RXN0Li_FUkucuo558jMwt-VDIgN-C0dNqjTP2WHfeO2ram9763-r2tJWtp2hm4yWRaMNnvv4NCimZBN-oLPczdHYWl1MMqDhPWhCDPnYcbpw709yu4lmvBgoX4-DH-Bz6QT5d6FRZqB8P261jmUe0_Q39jvaIMdr3TprUa9AfS4Mv1eXw-u8QfBWYXJ3kmkxmAvXrhZP5nemWkgBt2Fzqr680HjWrJ4rT2yof6nsmYy9r7vfeWwpMBywNN2XvxCSsnmGmHSqMAVZDOaIFB_PAHvzLTDQbCIPl3hu89AkhvL79N3Kel2MHWvsrFtrITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=Tiso_BwZ72JVp_ZAyKON-s1dqOQM15SY_Ni9GoXqG_LznrN5-VVCRO5PTvXLcTNCzSgbpyDYURzNJNK69MPpP9Ro3Wf25UFgafBup9k9IT0H5dyWvM2DrGcarRm_Ai8SnU1IaYB6zQCJHvTOzkLLEqYuQAW0cwATFNXCo6eTmjNbq7fooGM9HCVuSWgcHoFSXo7u44otCnt8X9rFpnlKK4sX3oUruv2fwuotOSYhad7DjYNM57MUCkdG29sVNN7QMr7o-73OaokO3m79cx82mLDEC1Z42rPwutmZ1Z2Ze9piwY53wyNLLHywqVMhS64KOEUQqIVpx2JZNv7SzYG4Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=Tiso_BwZ72JVp_ZAyKON-s1dqOQM15SY_Ni9GoXqG_LznrN5-VVCRO5PTvXLcTNCzSgbpyDYURzNJNK69MPpP9Ro3Wf25UFgafBup9k9IT0H5dyWvM2DrGcarRm_Ai8SnU1IaYB6zQCJHvTOzkLLEqYuQAW0cwATFNXCo6eTmjNbq7fooGM9HCVuSWgcHoFSXo7u44otCnt8X9rFpnlKK4sX3oUruv2fwuotOSYhad7DjYNM57MUCkdG29sVNN7QMr7o-73OaokO3m79cx82mLDEC1Z42rPwutmZ1Z2Ze9piwY53wyNLLHywqVMhS64KOEUQqIVpx2JZNv7SzYG4Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivO2NU5sxBL8NiLmtMX0B52ImPBoqRtiR5HqQpCidbKNUJ5uOWXJ0-xsnAUQy2_U61z6nK0L1mx2uE41PL8pPCzJTgli8NSNjBWGJOEjKLDjbi6ZaDbbTahTzJIAtCm6jpGG9r5O3UezUsLzGBFczVILuyfrQdt61_q4Wkq0TAZBpfQFGk4xbSET7WRKiFqE8OQbeVOp26SzTRpClv5mnWg2fftIjlwJMS_cDVLQbvz8E_p5t4w6ucU_w2ebFZmhdB9oJ4697O3gf6OZbJ2E1lU2z3jGIVTp87a0C5mNcsrP1tRq8iaibz4S5hFFPm3-_rLzR551lmcA1DS8ekMiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=ip9MCOBozUBVTTEJlbbRfiUDyXByNO8sZw_9qNW-U0spihLSMrbY4AAqohR5VTYmfWCXFc8BdCeZga_KlNWszKnArxf7Uw9X4WunCc3a4mETH43evTVG1BDN13f-o1s3GmJRdOKdjPbGxiX93qDMdZxdkm_z5-wjm-QQ-aA0BVBWedDw3AYgIwKWoaIPiSJU_Ylw3Ou16NryiA_D9TUZhar7pZ5RjlwF-Vf6KKJut40lxjk8cKkBcj0BgHewN9TUeYiih5rSJC2UmECzhC-ymsEhcKcSmw494VD-AWXnYZxCcT_cyssdzjQxv25MPweKd7ir8qWh6pgq2gJYmDmZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=ip9MCOBozUBVTTEJlbbRfiUDyXByNO8sZw_9qNW-U0spihLSMrbY4AAqohR5VTYmfWCXFc8BdCeZga_KlNWszKnArxf7Uw9X4WunCc3a4mETH43evTVG1BDN13f-o1s3GmJRdOKdjPbGxiX93qDMdZxdkm_z5-wjm-QQ-aA0BVBWedDw3AYgIwKWoaIPiSJU_Ylw3Ou16NryiA_D9TUZhar7pZ5RjlwF-Vf6KKJut40lxjk8cKkBcj0BgHewN9TUeYiih5rSJC2UmECzhC-ymsEhcKcSmw494VD-AWXnYZxCcT_cyssdzjQxv25MPweKd7ir8qWh6pgq2gJYmDmZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=KOHig7MruZe5z1hhyrGU1sTxHjaDDYsWR-aaDRaXCh1C3wbsbqi0efgPbA8a73iZtWCfhsH6NcC9VlmSH3Cl9Ee9B4bGFfJZ_1Lbugivs7ICBKHH3JvYFosAUUxcL-4BdJ9Pc7Njp-hgdqrrtSnQ6IQTPod72btdn9UAv73i_0-G2UsLglCw6V1-4ZiCuJsnky-FbuL4NW1cthDqEzsBthzP4i8cjI-gt8fp0RSDFXvd2CNCgP9zM85AOnPu0DEgdACP4yrYARIQrJcmBf73HeOOZTMciULlJ0jWQoQcMs9vjo61Fx081jyQL99-jQrCrgAK8IIrORuNgiXOf6S0jTB04jAzCys6pO5K5T7_2qOXlwgnraHZ4c-YvSWdVTBbqOd6J42h39Jd6KPlli3_qBWiZIvKKMukITnhAdbSLY_UW_lSzFNbaDeq6RJ1wCYdnTS-Inr6O2MeXuofosavYwb9LN74bSWXJvLPJF---2JrRLXswtpxMU6pgK-6SV-n3cPPWhm_vq1GXCpCG7-R_fOFmqVwkPHCEcTOlUQKOZiFOw4xSHK-HD8gTgIn7kmqYvmzKWfDsxKLxieWjnMMU-YOieyozPYmICid2exJh2B8R2eyFtILsF9E8jAPMhXRnhGjEiwC4TuSB6duX99SbHLr4kdp36PDRSk7SpSOu64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=KOHig7MruZe5z1hhyrGU1sTxHjaDDYsWR-aaDRaXCh1C3wbsbqi0efgPbA8a73iZtWCfhsH6NcC9VlmSH3Cl9Ee9B4bGFfJZ_1Lbugivs7ICBKHH3JvYFosAUUxcL-4BdJ9Pc7Njp-hgdqrrtSnQ6IQTPod72btdn9UAv73i_0-G2UsLglCw6V1-4ZiCuJsnky-FbuL4NW1cthDqEzsBthzP4i8cjI-gt8fp0RSDFXvd2CNCgP9zM85AOnPu0DEgdACP4yrYARIQrJcmBf73HeOOZTMciULlJ0jWQoQcMs9vjo61Fx081jyQL99-jQrCrgAK8IIrORuNgiXOf6S0jTB04jAzCys6pO5K5T7_2qOXlwgnraHZ4c-YvSWdVTBbqOd6J42h39Jd6KPlli3_qBWiZIvKKMukITnhAdbSLY_UW_lSzFNbaDeq6RJ1wCYdnTS-Inr6O2MeXuofosavYwb9LN74bSWXJvLPJF---2JrRLXswtpxMU6pgK-6SV-n3cPPWhm_vq1GXCpCG7-R_fOFmqVwkPHCEcTOlUQKOZiFOw4xSHK-HD8gTgIn7kmqYvmzKWfDsxKLxieWjnMMU-YOieyozPYmICid2exJh2B8R2eyFtILsF9E8jAPMhXRnhGjEiwC4TuSB6duX99SbHLr4kdp36PDRSk7SpSOu64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdAZ7achDPMzVpy0VOlZXWZ2IaE04ARsJ0ya9g97wNFXgSb8P4cNfrVGqvKRXrngNICxpkooEGa_DnBkou3q6Y2n-yCzk7EdmdwaVGIMDBrh8IgRxY0jzc5O9_uEHv7Cp8vS_mrWkwndfJD9s04FEeriMwbLpkyBqFJvzefx42gfZI5OFNq5tWbejAJVdZikgdvj93ZaGYNzRyorF8QrNGPc3ggDyFf29Gs92KTyvQRfJaMYKlArpJwVrH6Tb-j5Zd7pAUX4MHngoPm5q5Hk548iTNGcE6yR8omcKiiAZtrY9hbULXoNjkBjfWoqkmU248n9Y96ZDSekVKOd1__nrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFYtS4D-QxEuUraI8xg63MShrpiEas12vcQ8zj5cXhX_yUleJkfHtM4GlUNGfpp51NC6g228o3KmZ5CmAGaZ132eLGZgE2DrPObP9JRQ2oGQRseVpOtAeUZTGYF6pVd1ek2BIKKQxPUFXgH5hTdQuGpGVrSXLDkJoRE1Ap-bqrNt_rw5w6o1A9lN1XxhDOeoYFHzjt9wyfJGEm4n1KR1_YnMy0Wb9X6_e4lQzSZJUyPPKXQKwMzOtO_Jk2fF2Yxxl4zd7tQ89jVNhDloCl114uMXkgNju4l4fXXl-rHhVb4rEIzZ72hoV6BijZdXnrPFNMFY1ivoaRtoGEuOkhKrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhSMsYdqf-ux7jcEK7NO-26TiEyGHmkPB9xtFejW4UvPhO1p_-5Q4k-waZzvuOwY0IE78NBVtPheOycs2SdX9UvYzyMOmQ--_BWS7pzOoj7bR9nBGXVM3yOoO_A2JqRzy1SW5yh2YSAaEJX9YjpCCR94uGaVQvrZh-ZgLnVyVtkB0ekja8hQvQL25BGMAvJL_9B_wA_fCmR7xPr75N0MktZTt3NILIsi92Fa9KOWnYJkhaA_-I1oczRkEgzpiZkJ4QGPoErtmc3T6uXj7zjHou6RHBE1m_lJjPOk0fnddqsjZW4d2iAx-5vNmV6XPpCPlgtneVGtxzyTR64apMxeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWw_thNO28KjrJfmt7mBZoIoyf-6p4YKQXDh9pLcqIp9i_FuwiqrHpP7rqym5eA4BX2Bpf5UHvOeMjUr82bT7ec6kEAiRt22yERrly6oqFdOAPUfvJAHOzb8oHs4eyrqlOf5XFuQcCtaGBofxfk72oYKQDYRwYH_rVPDdVMQTwfA3c99AjRXbnsw8fqtsRP5-m1sk7HuJEy0EpwNgOBh8MHsCKwX2kAQ0rtXcBmi0aFNCgrjOjY9CDeO-tXBE7xvpZ0Ov0skMIOgNigUBRDW--Robra7-bBskBPnDJZHpiqEqh3AgIekJgQPvhhscBwiwW0fSP-OrqAhA06maiBURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWF2sR0WV6XEbhmwbD77iNaYP3qUFOEXMZvrSnAcxqhgvzUY2pILKR6Mw1QHdquwv-q4Whpo5mHlb_94mkVqjjRdEWfaaVOLvYq4ruqcf02i4HPGUpEzXUHH0vkGguK-cB5SJMTTW4V1RB3D2bggdvuQAp30pFBnUjPeVtLaFivV_IpzvZnDeNwTyWd10KsXjESJ5Ew7NOov53dZix7UQmf2hpLLp6WMbEmbICjGdBJld4Uz8CGOXaFsl60a-zuHYm3dXKNT-rJiEFf9wc3thKdqcUEdb2VNP0BvqdaO4uH2sfxyCpOoTqC6aYzc2g9IJWS5ky6Zo5eZhBVlW8oyMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL4Fw4v47gq3iJsCAZ4ckskdRS6R8bw5sypuJkF6MNG4rVlhXXzYPc4rZnX7WrCjq7jSc7jkyRSkMIAo-2ySbKqkptDRtMeSfI4wiCiktgMac0MMLQwBIusVCcSY3TlyWOqPV9C71YejdMVwrMqfOswS9QNbFJPejZwKj9h2U5DYi2g2O5H2Q_lF2vHfHc8V72iGnGJg74wyT15W6OZLjDzlXiDYiiQEeLSdb6gs8JU1p_0_GHNzpz7tXv5AF12qNOKSvPT7cxkhDEknKStLnSPIFqT1I7xcoFXiFz5N4aIRxSvioKKhyr630Y7Z3lyYopuolf8TZJcgJDXTWZ_eKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3qzMy2Jr6pZJNvblFaGq-EeHNl-jz4iJhxn9fLMIUX7VMdjqsIpRTtIu1ULIuFGeU6RT289s8sxnfkNQ9mqjGk4ZBlMHQ8tcPnaiyaodBUBQYvdRNFuuGChes8-W3O5QSJ_tNLn_q6b3ZGVHxGG5JvRi-0VqiflB6gbwW6zB3J9Ymf7O32suCaanT5JVGMqCTrnwEWqpdZxJXByT_6eXRcZN2etyEOL2op5o99YAq6yh7-At90ASDV34A46ls0bOx_7sPPLKESYh_GEn-mRqoUg85nL4Tx4r5E_XZjgcMYOjqpuc4BFOxy6D5VsnPz6oksFY6rLq6wKblW4EdaHT5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3qzMy2Jr6pZJNvblFaGq-EeHNl-jz4iJhxn9fLMIUX7VMdjqsIpRTtIu1ULIuFGeU6RT289s8sxnfkNQ9mqjGk4ZBlMHQ8tcPnaiyaodBUBQYvdRNFuuGChes8-W3O5QSJ_tNLn_q6b3ZGVHxGG5JvRi-0VqiflB6gbwW6zB3J9Ymf7O32suCaanT5JVGMqCTrnwEWqpdZxJXByT_6eXRcZN2etyEOL2op5o99YAq6yh7-At90ASDV34A46ls0bOx_7sPPLKESYh_GEn-mRqoUg85nL4Tx4r5E_XZjgcMYOjqpuc4BFOxy6D5VsnPz6oksFY6rLq6wKblW4EdaHT5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pqn4uZKDjLFDl1FJlZ5dibWELA1msAC32tyJICTJQzvlb3831YIErtSz18H3f3anrOA2lmeS1RXXwuWfYA_Kv10VHrEbMDlvsGLq9dQgs1fJuEn-uZzpqm9bdngAfPePFAUkkugsGaXNac450g0ZOEb7Hiej_658OumjQUFpULlEujqHu7eeom_Mi1UIRzMoNL8j88CaGV2UnfNs24rq5txAakB8zxm1VPXP91AthBpRHDH66-KSjq2Eq3M5bNfgVew31NvP0YDfKE1iWnZvuJ-RSvHg3PnycNQuVZky46xV9OeeQd-PeSurRzKEvgbx6JQJtJrLPBR7Gkw2p0yq9d8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pqn4uZKDjLFDl1FJlZ5dibWELA1msAC32tyJICTJQzvlb3831YIErtSz18H3f3anrOA2lmeS1RXXwuWfYA_Kv10VHrEbMDlvsGLq9dQgs1fJuEn-uZzpqm9bdngAfPePFAUkkugsGaXNac450g0ZOEb7Hiej_658OumjQUFpULlEujqHu7eeom_Mi1UIRzMoNL8j88CaGV2UnfNs24rq5txAakB8zxm1VPXP91AthBpRHDH66-KSjq2Eq3M5bNfgVew31NvP0YDfKE1iWnZvuJ-RSvHg3PnycNQuVZky46xV9OeeQd-PeSurRzKEvgbx6JQJtJrLPBR7Gkw2p0yq9d8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=mpVFRlP7LppuSgm_K3zCiIBowwWN5jQX3i1V-6pPZZkSEKLmD85rmaCxfbce3UxNPoW1cmeSvQIJvW-s1Qp8KRxjUPfDn2Sl0jplAwsqd8fWtq4PGDbUSjgBN7XA5JC7g6HQiOouB8hYdohpM_-t05DWGF-DjDlxD9Atan1hcVBInTlNDJisGWUIO6Axwy5b2ur0ChrEG2PG80e70mjSWFbtk465C1nRQ6Zs8-uOVbrRCxrPHKjPP03Et8-tCenzxcR26HdacbGgGj1yPGKFW5XHS_pBDMGFbf8x2J02M_5X9wcd2kc2lltorwA74G7NHEZvdXz0NWKK6ECXnfq4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=mpVFRlP7LppuSgm_K3zCiIBowwWN5jQX3i1V-6pPZZkSEKLmD85rmaCxfbce3UxNPoW1cmeSvQIJvW-s1Qp8KRxjUPfDn2Sl0jplAwsqd8fWtq4PGDbUSjgBN7XA5JC7g6HQiOouB8hYdohpM_-t05DWGF-DjDlxD9Atan1hcVBInTlNDJisGWUIO6Axwy5b2ur0ChrEG2PG80e70mjSWFbtk465C1nRQ6Zs8-uOVbrRCxrPHKjPP03Et8-tCenzxcR26HdacbGgGj1yPGKFW5XHS_pBDMGFbf8x2J02M_5X9wcd2kc2lltorwA74G7NHEZvdXz0NWKK6ECXnfq4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
