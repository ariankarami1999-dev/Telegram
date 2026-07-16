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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-7JLKpHkTIKODdtZIfbZf-G4Zr5lfKvMhzQCx3kA9C5g9IdxEnJu7nLM6ZBIqeFmPLkn4JnD2oluQaEB4J6w8aOJMGazbMjoQTJi9r9jo1kwVprCB8D0Cpdc-7Xo8sx_fbJaHRStGUHOY9PdhevBiX4MoH7fKy57ajaRVMXl6-r-v8bHsaUw1dyevWJAi6R9kSQbND6nILx0SErWDV-4pplhym0KwLwdpXuPtOtDgoG-FT6gvQVwwEenNR510x5TPHAwH2g0ejdMvAcnokTM6D-zpMTkdHZG0EkqiWj2lbEXzj3vJIIO6ShVpPxgm4hcKTCsUmTM8bcDkgt_toO5NR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInibF3peiLlxkW8UF3xqJyasj6hZbHKQ5_zaIodU6-wu95PjUz-ARmzyErw6NSUfWQi-L4gSj8U-x4xR3DFD0O-inPbsvgzJNJ-Tk-cWUh6fFHVK6v_K6n0ZyoCLaeaugSindc8RGDAkIOqohSUzQwk1MMXwMC30t2rUAUnjcq5Xado7XHAU0cipNgjXQzEoCJZJ-hhsCWpy57tYR-g8YO1hrYNMQEnsGQFGsIuMpes7DcsSFsYHa1tSctbeagFAmKrPTyqsKLK3bFbkA1VqzUTrBcV4pzLpX3p1UlNuDbBbwQN-QsDwRmJY5vqcop-O6bcZqNb8QgNvnCva65LHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S67FAPbGcSIj2mIMHB3rweXRNd9SeixdnSv8uvrcwW8nnvOtbl0mhQ95jnqSUYbjvGfmho4R6Ei5xQ40o39fj6JfxvGefHFtdDyo6aRh04UmLkVAAsInsKYlzqmuJQs-18faNQ3hC2c7FxONqK1LlxGO-S1wt1buPHFkbTI0qzrEdES4bLTCIb1DLuPjKH07FY6wjWt8Eij3kbViicG7zHZ9WI0tf7C-ipY4FwP2EijBmkd7tORJMqhhusXvszV6kuPkLvoCs7cJuq5qjLeuY_2tMU-eNnXll7N5m2QAlPS0koNASticS7RQENihNJiJvW3sqJXqvNtUahktGgzXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAn2Rhw6MG6nUjkdmcJSlFMjL-HZVXD_LhnzWuhO6nAT7foyaLOQhDi7Fpk3aDpNU_YRpLkVFdOM2d2AQUnLueSAd28tre0PkbGARbX6AbalhclNxd9blwOmYQPwBfOE8eHEUtslFt_JkQuKPSxFKih_wrX-reObp9UPdFTCZxQBizFwDmJs1ZccE0-wh-ZItW4uMHGXMFV8VTxh00qbSs6y6G58R2DF51lOtxcxWXH7VNkJ-6BYxkMSbs_VWmyQ4CfdDkbXQlK-Qrch_3Pjc9ox2-uy9k8D7ht7_ySacrDYQvwv6aUddBJx7z8GXAHo7RPrvowI3N-LssBt5r__Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHNQVXkFYovC-DCNQasPnb2TPHUhp0ZxrmBmDnpcHs5JSINSmWaibVmT06FqNegEuKcmEOy3Ga2YNovIEh0Y7x3JOysD_QysMdFVyrm4k4TKlw-prk9o0i6E1z79I6MULKICe-gOm0DpwPgCg-98CuRtRgspvQKL7Y8UEI_iZBdWfXkV-b4FLyIhFDo6j5xSGI5hp3rQLMmM-ekF4fIcmbkJGqPPfXY15bBhRJ--gZly9Y31ziVdh2l-8OtgRyx2YM010Pq7TaQHjzCBtxJgjfnRZU4VrO9JfZQXCQk5rL2I1c4XsZjQmRxFenYkUvqnxHIbSZ6qKMC6WeX0zJWqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=BH5Y4hBVzbQS3Crm1s3RtTbbepAqZB-K98pGmju5PQ6RjLHvxSkQZE5ruzvTH835iOffhZAQku4W-k7h5geWJSRchG-sKpIC3NI7JKnRT9gT0QkOk-wDM62iR-AW_tyE0Soh7KmlC7Q5apYs6J4cAo0nP5zNMZ9OrTOZKe6Kln0bVZeN4ICito5vtqJgNOdJgD95v4A-cGezlYoXB6IDUu37yFloVDuob8TYiKW06Dtb0adoTE0rJZs0BlRJthztXsdnS5hGKPMAXNfXpCH_rakJe3GzBKlUiHLwr62Hz6Zyo-F8xh1x2B2188b9qdX9zsFmANukvz5w6MHGIAvGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=BH5Y4hBVzbQS3Crm1s3RtTbbepAqZB-K98pGmju5PQ6RjLHvxSkQZE5ruzvTH835iOffhZAQku4W-k7h5geWJSRchG-sKpIC3NI7JKnRT9gT0QkOk-wDM62iR-AW_tyE0Soh7KmlC7Q5apYs6J4cAo0nP5zNMZ9OrTOZKe6Kln0bVZeN4ICito5vtqJgNOdJgD95v4A-cGezlYoXB6IDUu37yFloVDuob8TYiKW06Dtb0adoTE0rJZs0BlRJthztXsdnS5hGKPMAXNfXpCH_rakJe3GzBKlUiHLwr62Hz6Zyo-F8xh1x2B2188b9qdX9zsFmANukvz5w6MHGIAvGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=g4Vyopzq2EGPi_r5zCY-0-RGOFItEkht5tsjUoq75FAoLDDnvCxYd0F3aG94J1yQNF0Z5BWMk8G-lz1ETEpva9AAq86Z04oj_wgf3v0mbuRdLgIrK1hWEBneXfsTpkKsCUBHqNbTb9iPxv4bEQX18v_JEwE_MpKQ0g7xu4z7mysyXbiaz_vLZt8St2KgeeZ8dtYl1EbLBmLyZ9KEYisx7EK8V-tI30KlEC_i786-ltJOiqWRmX1Lp13X1VgQRXDiHpYDdp_bEDlFDuowWsgvw4LDDmWvvc94azPuLAy1ws2ye83QF-B5kJQjugmPar5CGCT_oVQ0MFgBfltapSRDwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=g4Vyopzq2EGPi_r5zCY-0-RGOFItEkht5tsjUoq75FAoLDDnvCxYd0F3aG94J1yQNF0Z5BWMk8G-lz1ETEpva9AAq86Z04oj_wgf3v0mbuRdLgIrK1hWEBneXfsTpkKsCUBHqNbTb9iPxv4bEQX18v_JEwE_MpKQ0g7xu4z7mysyXbiaz_vLZt8St2KgeeZ8dtYl1EbLBmLyZ9KEYisx7EK8V-tI30KlEC_i786-ltJOiqWRmX1Lp13X1VgQRXDiHpYDdp_bEDlFDuowWsgvw4LDDmWvvc94azPuLAy1ws2ye83QF-B5kJQjugmPar5CGCT_oVQ0MFgBfltapSRDwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcjCA-sSW4inlSJCGkpSVSdyPCCBuELiVpH5ixSiIt44ze0sy-Ig2D8Al-3i1mvkwDwbj-9_9RCBqjzdBoYqf7lQJxYzosd7RHDe49jUWvpb4pHJDrCvrk7bCYagSMwb_IBLjMhsnJUYczi_K8DW5LEhCUNRXmjwqFYfuG5g5Jsv1XBkVWzURGiEsXyHUxuANHkXU7jiOW6gLxjzNf10QH2TtSnDGgl7HWvPpkpf3Zk-qvkISNwaV4kmSvzhd9cNhIVsb1-sujyGlOO0X-scw30NOZWCNdlb9OK4oGJeDULrqrws7CVAeCAk3GpPiU1-wWdI465cXyKSTRWqJQ8Jpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwVkMhFScPoBwvZM5Wpb9PBZ_9vh6pNmlK-sTHhI1xtJVPP9g3j8J_i9gq4gS0TOXcfE6eNidrx1KbQfMGPvFL118r-GAJR_t8WXCBEuQ7ehg-PLNwXJuHdKASfe1ivU6BsCACLSd4wjZbSjIzoqw8aNOVTwbmSDRtrfTplYpyv_IXM-jo11XLuMb5zbgSStyPRPH8kMVvU3n5QTa2nZZjYeOAUDAcTs1eYwDqVLUy_8sx6azGTmXG-7dxH32mSz_dqGQDGF12bqBAWSFzWuWHHjxyycpFgp4pfEsNrzVWgwuSlJT9K8g_59OdbStsnnyMMx1WFl7w2uECK1noYeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=oxbQAO9xB6kFfK32Bp20WT4KGkzB8xzP_ZRgj-AhX7x2LBuWnTKczNTq2hnRs4ijRNMeX5cecv89cZ1BMgBKnGDBdiUfKLiRklEpFktjPdKrqBMILfn69GVxn8XeqSapsxa5MaHitU0ZUtHS2dWDsF56PjbdeCTPmnUj2Gyid6snnYngtvREgZbme9vtYxkltLFdGdBwsLyZ27jYoeASnqqp0x997GyTezZgif1wmsD8Fy9H-7gbpCj6hvs8pRDk4dRucisSlnp8cAW582kypclEMN2LgJjkQY1qpMYGpFAkH2eilV6Ss6qa8CuNpaXNy-M1bMjrr8Z9dVAVd3k8SppRNeP4FKTahF_j0BMHi8jDS35yeweDF4c-wtrl6MPUh6vhFoHUDklUx8CXXQh-DUjES94axPHmkfoKcRNF_MTvQFL6Yt605G_8-iEbbS-xnPFItzVoTeghZKSaPJlNgVE4dmECggM1Kz4Dexj9Sj8bYn-i2WCWGEOKpzVvbJp0_rEz8GFXpeuXv5EaY-3flcqIt2PcqCQFC4El_f0A8R5ng1vUJZ5zHOfCvlbsi8t3Bk2eNkso8SqCFtnqCY302hHHmiUkyk5jJOfOAAifOt3l5nqFZTRyi5ttJq8q2MnuxO9zbsb2i8pjmFBpUyviz0cRCGj7bcJ6xW5JxNEZPw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=oxbQAO9xB6kFfK32Bp20WT4KGkzB8xzP_ZRgj-AhX7x2LBuWnTKczNTq2hnRs4ijRNMeX5cecv89cZ1BMgBKnGDBdiUfKLiRklEpFktjPdKrqBMILfn69GVxn8XeqSapsxa5MaHitU0ZUtHS2dWDsF56PjbdeCTPmnUj2Gyid6snnYngtvREgZbme9vtYxkltLFdGdBwsLyZ27jYoeASnqqp0x997GyTezZgif1wmsD8Fy9H-7gbpCj6hvs8pRDk4dRucisSlnp8cAW582kypclEMN2LgJjkQY1qpMYGpFAkH2eilV6Ss6qa8CuNpaXNy-M1bMjrr8Z9dVAVd3k8SppRNeP4FKTahF_j0BMHi8jDS35yeweDF4c-wtrl6MPUh6vhFoHUDklUx8CXXQh-DUjES94axPHmkfoKcRNF_MTvQFL6Yt605G_8-iEbbS-xnPFItzVoTeghZKSaPJlNgVE4dmECggM1Kz4Dexj9Sj8bYn-i2WCWGEOKpzVvbJp0_rEz8GFXpeuXv5EaY-3flcqIt2PcqCQFC4El_f0A8R5ng1vUJZ5zHOfCvlbsi8t3Bk2eNkso8SqCFtnqCY302hHHmiUkyk5jJOfOAAifOt3l5nqFZTRyi5ttJq8q2MnuxO9zbsb2i8pjmFBpUyviz0cRCGj7bcJ6xW5JxNEZPw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2ICh757a9MdeDbPtMw0UVJiu5K81YlCt0O3SEEU9Z6AvGMkXrMBPihcIwjFXJREWDgp5HgSUitTwGtNRBHxXSgxW4gd4MDcenA4ktBbaA0W8teeZg2SdCo6d8yG3Uh1L-MEh02xnLhOeEYM3vogJwam6_r0-MuMFm6-z59tRdDJF20VIX0_rT0gkcyjozVCxr1LYD2rcv1Ksei5TE1X-mR8EDAhGALKsPg9Al7UHryWP3x5-8tvpzdxmKE3D8yszdeQ5sxGYnXQojMZiEZSs5DNUGytQulCQ3KDtbwt1AsvA2bI4lvqrOzNnUH88yh6eceqks6H9pIAE2LktJo4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlbGLCH2SGhNua76Qrw5fZLEKcn0Smt870Pmje_Q1QBRHqUycBr4WVQbIToja4yEu1ZD1CDaxd1FqhSGR_ewh7yb-xyH6o5qlGjnMjJSCEiBEx7dHZkMXgYFr2JsJmn5MX8dSRSxzMyybpPZGs3TVQk8fuRzSl8r-3Q6pTwIxJWf9ifGVRpOd86AcGRzzZW2NMkAZlwts5jPS0En7MR9b6h6E8Fqqdlmo-hbj0SYZ19D7w-kwVwAh8IhstXNBfrwDnHYkG_bUv6sJtGI5ZrAOQ5cJ6NlMjfeaxNUtcvRJjkyiCHBKcih1iRT9aeSMT8FP1FIOMz7NTMtdINYKkXxvWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlbGLCH2SGhNua76Qrw5fZLEKcn0Smt870Pmje_Q1QBRHqUycBr4WVQbIToja4yEu1ZD1CDaxd1FqhSGR_ewh7yb-xyH6o5qlGjnMjJSCEiBEx7dHZkMXgYFr2JsJmn5MX8dSRSxzMyybpPZGs3TVQk8fuRzSl8r-3Q6pTwIxJWf9ifGVRpOd86AcGRzzZW2NMkAZlwts5jPS0En7MR9b6h6E8Fqqdlmo-hbj0SYZ19D7w-kwVwAh8IhstXNBfrwDnHYkG_bUv6sJtGI5ZrAOQ5cJ6NlMjfeaxNUtcvRJjkyiCHBKcih1iRT9aeSMT8FP1FIOMz7NTMtdINYKkXxvWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=D31L28cD0iUbk3lNoU7kDgOaY-yaBAA1l4uj7PZd-wYcD_3EmlCGsrVkLI9UAOL5b0WkPVqSOg5MBSiBzIaW1S5ck-_3DnaawPccMHVm7y5Y1vI1OcwHNkDHBkJ1Oa95uT_p1bYqD0zrU0gUtoG221aKP21-F9V__8ZEq6CGG-oPnoMBqQfpt2tIEolX7KlySmhbWderlQXG_AEDPKaVF0JkpFGG1YkpdDLkdQ57AamRaJJssyAsTUh5Xf0HRD0pPh_4ohPv9UYXJOuw37GoQ39ySMDdomEOTGflN3gLsFVFBoJaSqHyWUoZEFihv6K9MOmhIsh_swGPidRoKyZqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=D31L28cD0iUbk3lNoU7kDgOaY-yaBAA1l4uj7PZd-wYcD_3EmlCGsrVkLI9UAOL5b0WkPVqSOg5MBSiBzIaW1S5ck-_3DnaawPccMHVm7y5Y1vI1OcwHNkDHBkJ1Oa95uT_p1bYqD0zrU0gUtoG221aKP21-F9V__8ZEq6CGG-oPnoMBqQfpt2tIEolX7KlySmhbWderlQXG_AEDPKaVF0JkpFGG1YkpdDLkdQ57AamRaJJssyAsTUh5Xf0HRD0pPh_4ohPv9UYXJOuw37GoQ39ySMDdomEOTGflN3gLsFVFBoJaSqHyWUoZEFihv6K9MOmhIsh_swGPidRoKyZqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=gc9YCqg_wndh25oxUGhMmo72ZPqc1j5-JSKKGJmIA2MNki3UP_rmeJCkvSERwOVFlkLmJvfXd8BvLtYEJRDp-oPBG7HJ4l-chC38HTVOjR10QND2umrVToMXIhgERRd6-DI6ismQUrNx9nfexswi8QO2xhtcUkm9jipsQUoGgjKrMfY3Nxsf7wvZD72G059ZDVpVRvnmkzXYN2B5pn2A1H4WHLZ6GlceZuEw3Vh3GvAMZ_r2Zzro9CszqKz_suMyOW6slWiQ3bMQGpkK3lVRdL7Vm8wCKIWqVu3pqAotFuFAIyDAStTdcCNPOvtnzz27pi9mRFCJPJ_WjvqbwpRA_XXzHBwnvNRTdcPVXXr6J-0KLS3veb2ZKyR_sMhrA1g_hhDKOhISxQ7g_0NZCPeiMX6qBS89Rn3OUybktuNpGMIj4iJwL95Vh9H-gsrUDMLIVs6L-VUM8_tJ84lQCPqW2xblBozxlw3UYOO6UhBBiq5qHwUG9l8OFt8Wzto75m5fBT3KOfDRiclpJWHU89hc_orpwi2HuYBrmFycj_mPRyTHp9zcPFsA2nMFPhBEC9ZelD9Wa8Eyk0xaY0sAnEhvu9oCdEtczv0SCAC_EUCS3QpfeCuOl03CNMY-8MguR3LQn5za-VOCBPWRVquaFJsPJR0GstaYrigykdjoe7Y3ZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=gc9YCqg_wndh25oxUGhMmo72ZPqc1j5-JSKKGJmIA2MNki3UP_rmeJCkvSERwOVFlkLmJvfXd8BvLtYEJRDp-oPBG7HJ4l-chC38HTVOjR10QND2umrVToMXIhgERRd6-DI6ismQUrNx9nfexswi8QO2xhtcUkm9jipsQUoGgjKrMfY3Nxsf7wvZD72G059ZDVpVRvnmkzXYN2B5pn2A1H4WHLZ6GlceZuEw3Vh3GvAMZ_r2Zzro9CszqKz_suMyOW6slWiQ3bMQGpkK3lVRdL7Vm8wCKIWqVu3pqAotFuFAIyDAStTdcCNPOvtnzz27pi9mRFCJPJ_WjvqbwpRA_XXzHBwnvNRTdcPVXXr6J-0KLS3veb2ZKyR_sMhrA1g_hhDKOhISxQ7g_0NZCPeiMX6qBS89Rn3OUybktuNpGMIj4iJwL95Vh9H-gsrUDMLIVs6L-VUM8_tJ84lQCPqW2xblBozxlw3UYOO6UhBBiq5qHwUG9l8OFt8Wzto75m5fBT3KOfDRiclpJWHU89hc_orpwi2HuYBrmFycj_mPRyTHp9zcPFsA2nMFPhBEC9ZelD9Wa8Eyk0xaY0sAnEhvu9oCdEtczv0SCAC_EUCS3QpfeCuOl03CNMY-8MguR3LQn5za-VOCBPWRVquaFJsPJR0GstaYrigykdjoe7Y3ZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzp_55kzwp26Hp7Ai-qSWnDywnrxRqNyKLJpYAVOBGIzBbQVgzCwJhCxAzvKYJU_6iiaiDkqLOA0KGnNDlW-xJAN8HmMQcxXbgVDinocNnBP-NLpIS8fM3Gfce53jwPllSI4kRsPWcbZxDilXeCzWJbHE62awHWxuND-ZWJ0UNY-xhA6Egq7oWTy35E5qzput29iMqeatJJuh3irOVhVLXrLJrySkhSoRAKH9aRJELIvgAsu572QRSLNMVYxvi0ot0sokResML0-cAHkZp_5bD-2EQU11VupXdAvXE5ixnDCSSb0_vJnIW55VCAY6QrY79yZgARK23TBt_RaQbLRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXet08H24NABJDzwnwBgiSJkji4qAaNxKtJZzGFMCEDGUtT9iAZgjEEkBjB4pzLgSshHgiR-GkRxd8DYdi5gKr0273QuAVI_iqn7MoPyBv1PpQJHrFyT5Jla9fXmbxiyItNnqL4na2or7UgrSYakb6Qp_SOWKxUABULb1cnxfY2t74TShUwe7xAZYGwZ39qRfsHLrGvh8LoLAh_BLfd4fAswzOBgydAVGoTdcshxabqFYq2okJUbNd5Ejq5dNgCUMrTJgJIq_L6UYH_Of7vvcLZKVR4rYlJuL0UzdW6us9gamkxc-lAdlwfC-o0l8EplJBYHDxRo2d4iqQX2D9HdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nTiuIFerwOrrQX7slG5Ja-_S5UWgiDOZPSMVfYj0e6J-wDunQfEQKRZjHEZU8SR0XvtNkOGL9yVR2uN4XmZUnzNkS7jwI-9yOqhdg0ArySLnuVvB28EvaF3OCEvkaLdADedcgiC1omKkvjr0WD6lfbutdU7xEJRp1wFEbkSxCzY7OR4EVwKF9ggc-b8Kq3h3yVtLNLVcFOybV7k5XaA7jm3Wb1Q7HIjWM5kemAiV9adx05E85Fi9bo8nRGadhDxgsTUrhny9kAoJyZvKQkhE0cbSAhyMgQcTS8XVJIYQnQL-A5KAzAGtTGFRkK84Bw72bccyZr9syr0pUHSJr57SnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=nTiuIFerwOrrQX7slG5Ja-_S5UWgiDOZPSMVfYj0e6J-wDunQfEQKRZjHEZU8SR0XvtNkOGL9yVR2uN4XmZUnzNkS7jwI-9yOqhdg0ArySLnuVvB28EvaF3OCEvkaLdADedcgiC1omKkvjr0WD6lfbutdU7xEJRp1wFEbkSxCzY7OR4EVwKF9ggc-b8Kq3h3yVtLNLVcFOybV7k5XaA7jm3Wb1Q7HIjWM5kemAiV9adx05E85Fi9bo8nRGadhDxgsTUrhny9kAoJyZvKQkhE0cbSAhyMgQcTS8XVJIYQnQL-A5KAzAGtTGFRkK84Bw72bccyZr9syr0pUHSJr57SnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=b8nyAofK1GvTt3MhJOXQWW8aookDCHGNeLvXM94NiDK3U28T5blUnBGhbMluRbFr-inUKihKD64K7nVA2a3X66GWkFG6_772JyFOs6nCytFYgiG758mhLBek40KgXyBBLauFLn545uLYxvIYQE6pWoDVdR4Z5ylU7ZECNLZKdHJFxMKGFIbhWhj1sV8VINXTWHiIwqJdbZ1rn0ZX5lXOStQc8beGC8YeSFoFu1iRCGriPFPP9i_CLoY2s1S5qEygZON7xsPniH-V9_KWcsZd8f1Mcm6NNiPbjwt8XMu5UNuUhEmJAq55wMFV7vYHbmBNPRLO5Jas-iyVxgETvcBPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=b8nyAofK1GvTt3MhJOXQWW8aookDCHGNeLvXM94NiDK3U28T5blUnBGhbMluRbFr-inUKihKD64K7nVA2a3X66GWkFG6_772JyFOs6nCytFYgiG758mhLBek40KgXyBBLauFLn545uLYxvIYQE6pWoDVdR4Z5ylU7ZECNLZKdHJFxMKGFIbhWhj1sV8VINXTWHiIwqJdbZ1rn0ZX5lXOStQc8beGC8YeSFoFu1iRCGriPFPP9i_CLoY2s1S5qEygZON7xsPniH-V9_KWcsZd8f1Mcm6NNiPbjwt8XMu5UNuUhEmJAq55wMFV7vYHbmBNPRLO5Jas-iyVxgETvcBPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=nPa_H3Df1-aP5xThzOoAvH2SZHsA2y4yX2nqbTtGbCi2m0Xw1a1jgqXfyK_vjDuEtDo7wJ4ecHXopQM5c1PKzzsh-WY64C3dKygq5vSYcgMjbNknVY6GIvAStH7qp01OitCDa8MKUD7xw24L_RMLw8NJxNGHRch-WcDrGzxJBck7hArGhCDqnMVgO0JK_EaTtDXnStsx32nIOTuqP3qAzgUEzrDpsKde1FIf3DAzDFzQ55BCehnlFMWC62YcGM9-Ri5RJaBxP88UjLTXXNwW0iC_k17Krtp1FT8tfHZCZ35Qm8oq7FhrJeeEtf91M-WuiX4ANsKXg1Lgo7tc3IFW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=nPa_H3Df1-aP5xThzOoAvH2SZHsA2y4yX2nqbTtGbCi2m0Xw1a1jgqXfyK_vjDuEtDo7wJ4ecHXopQM5c1PKzzsh-WY64C3dKygq5vSYcgMjbNknVY6GIvAStH7qp01OitCDa8MKUD7xw24L_RMLw8NJxNGHRch-WcDrGzxJBck7hArGhCDqnMVgO0JK_EaTtDXnStsx32nIOTuqP3qAzgUEzrDpsKde1FIf3DAzDFzQ55BCehnlFMWC62YcGM9-Ri5RJaBxP88UjLTXXNwW0iC_k17Krtp1FT8tfHZCZ35Qm8oq7FhrJeeEtf91M-WuiX4ANsKXg1Lgo7tc3IFW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=kxmVCNsJ2zuKTdfawpypVrtaH6Nv4ui39_hiLWG8kPmnV-HiN8AsyuWrs6APArwXN4ckOeAhC7QHG9THqB9GBx7CR3cl5DVxV50ApPU2THgBvzgz3EeKHWdHouuJwgvdOCNrNcwq1yVgS_7NXQVmYjfs0FVMaomq7dCH9kLhxW-ZYBvqD44qPeus44wZnF5V7DtRpL24aM7YLKvN8U0r8xRDjbHZi7jOzw1GtNIh-pmil4ZM6grggoB5MAKWr_XbG5fIo8PH46kidwa4UPLWv3xqOe8Z5PPRSBeRPUFqjmIcr-ZyyHgJejf1sfBwmES-jp8hVDY2G96oAhElE2l0Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=kxmVCNsJ2zuKTdfawpypVrtaH6Nv4ui39_hiLWG8kPmnV-HiN8AsyuWrs6APArwXN4ckOeAhC7QHG9THqB9GBx7CR3cl5DVxV50ApPU2THgBvzgz3EeKHWdHouuJwgvdOCNrNcwq1yVgS_7NXQVmYjfs0FVMaomq7dCH9kLhxW-ZYBvqD44qPeus44wZnF5V7DtRpL24aM7YLKvN8U0r8xRDjbHZi7jOzw1GtNIh-pmil4ZM6grggoB5MAKWr_XbG5fIo8PH46kidwa4UPLWv3xqOe8Z5PPRSBeRPUFqjmIcr-ZyyHgJejf1sfBwmES-jp8hVDY2G96oAhElE2l0Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFlBfsx2irjQ_3im5B25bXErXnDq8KLNorCCF4O2a4tX-DaDZFW6PGmfthWCT02Jcdb7JJ6m15jwcutyM4wNUL4EFiOFOneK6x184wwiwa7iatdTSc0jKDCLm5GtdQ7tYn_vuRWRqCVvqkZ6f1NNiLLj3MsCuxqyv4Ct9bN8BhkcMtWM94CcZOtt1282zCD4ROI3sTuS_7MiUuOn6DGPpih6xOgKSU5ltWDMMdhujAY2pWU8BJ3LT3drQw23aCia4OTMLSsyGaPKtnk92mTMBQsmpgeFaXbxPqIy3OicMe6bx2xkkm8kEgLOfqWt2LTJwernY8u6yE168ROQU8dmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvmYsYsGthrjra8GzVTqUML2KH5dphpF13MhGpbTrM_ZpcahE3UDOoo5cz3ehKppuL8TxfVCGuPVtvseDCAF4BZo4oQWc23f6UteaGwAOYyxTyyJ-82C59TVKdBkChPxHGUOhA-tGE062wJRkT6S2AuaG_VtecDfs8_eo759FVNd30eciVgwkGXi6XClZldsmkUNufviBYu1TSiQK-RRxxkJ-CmcZoCAas9TRa0cMv0BslMWpdy3hEEF_H_hF-lmr9YvN0vONJQ2zUIqsI9hFKfh8AD-fYaw77Bm4-j87o_BD_5DOX-62SABy-mhunfF76KkolMfUedFNKX6R0-b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=SV_JYbWxW_QEJ2hjZpqhH0ByMS7N37MXp5HCqL5MPYRYzTxzOkzDMUeABe6_aT1CBllTwK4b9obyCNI4VTfi58ug1Nt8_HgxHkpD-ozpdeKiy-yfBPZrjEEOr_3i54TyR2nbcJAtsMun-3e2OwI9wzl_2OrQbWOb-_1amgVhyO6YQn8-yRDx6d2Eylo0O7h7iavBbMTBHTCyVQ3y1wViu-TXRZKpsBOMlAikchfgMxv8bkSYpafEBbeMgrLzasF_aDEUR6LeRQoMVfUaAVoP98k3feM_F8zNu_m0Gh4ah2PISqrg5o5kCEycUbpbu_SsdoPOunMVgS1RFWZVrory1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=SV_JYbWxW_QEJ2hjZpqhH0ByMS7N37MXp5HCqL5MPYRYzTxzOkzDMUeABe6_aT1CBllTwK4b9obyCNI4VTfi58ug1Nt8_HgxHkpD-ozpdeKiy-yfBPZrjEEOr_3i54TyR2nbcJAtsMun-3e2OwI9wzl_2OrQbWOb-_1amgVhyO6YQn8-yRDx6d2Eylo0O7h7iavBbMTBHTCyVQ3y1wViu-TXRZKpsBOMlAikchfgMxv8bkSYpafEBbeMgrLzasF_aDEUR6LeRQoMVfUaAVoP98k3feM_F8zNu_m0Gh4ah2PISqrg5o5kCEycUbpbu_SsdoPOunMVgS1RFWZVrory1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=YCNbtbXOGJGOkApCXi-9F6Kmu5MqTbuIUD2Kak6E2HIrDAOY5nSsMjzkcoLeAI_WYvKI__WYDm1dCHdW6nzhKtHB4krmPJKAC53jAKE0jgWhNbcKHYO2BWqT3RXB12moFZ_m30IxRRFqN53IuEeE8Ss1Xp8Qvem3egI9FUFB3shqLWnD5VGMMMhx9mvRHfHGmF1ou3YiGcffT4KDevHByddPejcUtD50MkzYacZcU7vyUlbX8BTQJSoB5QajatwQTPtbDLY2dsHUfdxLiYhT3QfCaHizKEcMvZTAOQ9x_CAGj1aI6GqSOL7r7DkBM15l8NYE8Y79wnO2w-nhNvVMJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=YCNbtbXOGJGOkApCXi-9F6Kmu5MqTbuIUD2Kak6E2HIrDAOY5nSsMjzkcoLeAI_WYvKI__WYDm1dCHdW6nzhKtHB4krmPJKAC53jAKE0jgWhNbcKHYO2BWqT3RXB12moFZ_m30IxRRFqN53IuEeE8Ss1Xp8Qvem3egI9FUFB3shqLWnD5VGMMMhx9mvRHfHGmF1ou3YiGcffT4KDevHByddPejcUtD50MkzYacZcU7vyUlbX8BTQJSoB5QajatwQTPtbDLY2dsHUfdxLiYhT3QfCaHizKEcMvZTAOQ9x_CAGj1aI6GqSOL7r7DkBM15l8NYE8Y79wnO2w-nhNvVMJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=O364O4bSeM_DDpfu4hJgJo1HAiWkBZ0nSY9F_bAGvrJ2eaZYSIRFGiyikWRG8h0J4xNuNk9TtAqsRnPEIdb8xuNHfb8g-ob2s1Oo8gFsyFWFADUqlEdH6NVtqXkofJqZtewZGl4tjoH_QJ8dC5KHCigr1PN49pyNukWX1P1ktTT-6U5905XjXqjOgh61_XT2dmuGfFvDP_FVPD6Hg3Gw4_TWvqwQLHAUFePt1sz3cWuNp6tyUsg9VyrgQSW3isLXzO8Q5b2SWXOyVb5CE7eOE_jzXdcd_993tn2f-EvMluPMS7eTB12RwcU1-w44CSEA5bvOECdLrb9aQGB4lHrXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=O364O4bSeM_DDpfu4hJgJo1HAiWkBZ0nSY9F_bAGvrJ2eaZYSIRFGiyikWRG8h0J4xNuNk9TtAqsRnPEIdb8xuNHfb8g-ob2s1Oo8gFsyFWFADUqlEdH6NVtqXkofJqZtewZGl4tjoH_QJ8dC5KHCigr1PN49pyNukWX1P1ktTT-6U5905XjXqjOgh61_XT2dmuGfFvDP_FVPD6Hg3Gw4_TWvqwQLHAUFePt1sz3cWuNp6tyUsg9VyrgQSW3isLXzO8Q5b2SWXOyVb5CE7eOE_jzXdcd_993tn2f-EvMluPMS7eTB12RwcU1-w44CSEA5bvOECdLrb9aQGB4lHrXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMEXieGgKKuidSB1aykJnuE9HcPsfqyKBhkEJuieGGJHP5HY7VwQyluDYMWBvgmCFTdJ6CYaoNMex-piKnNJCjd9EeAq7qWhkIGmh-UF3Hb3-mJIxuUGQV60EiPTf4oas-uQcwGfHlTQFx_jBLUWQdZOMxTZyPXRo6lu6YEl4eKWSg8xyl3pKpwQp0AqJ3zJeHzQotG-wXLLfayLJiUUQt9xhnQu-lo7wqUqCV75b5GwG092NH46VmPkVHTkLHQUDFhWpvoCPcz-YEBEfQJAMzgFF9HJK2wV65fA7C7GoTPhBnub3Pqf6_f4LuhkXpYDZ74k7KHLai0Rm6PRi1qieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb0w5amh5J1ZyibQqiwehEO-hUYfE9F0N82hTWTKob-gsy2-utnBPdvLe7WJ4G9Wop7gTBo_kXzpQ2SVKfUl3o2x4g2xmjU1vow4dss6Xxv8B9nNpbi9RDopcF4r28Zyc-IMQpCOseJF5Mp9lMc3OWZ7Keyt48apyTnxt0M9RCflzog8ZkaIV4ab2tWFs3cbECNBC__7shYV-_6UkHGYlkn6e4mv9Asn9AU48r7iIrh8gayHaqX6CmrJcWiVrStj49oiFhhAVM96wwa6vmCF-kEfmCtvXxVoSE9R-wTXzZ6qwlUL6VGNkuk2QPamoCIHllhYzHvLPQwyTrAb4UsgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=Np3PreMyxQxir0_rOdfiIB2USM8MNF2i6C5CePdgZSkNo1SG2us1HrtO3Vwa5F0g13PgrE62ZrpHpJLFvN-1C1iU-bZdR5SdrZd2fSecRbmpnqxAgYUtmH7bRBj6a9tcQxpazy-9vug2oMLEez7hzhwNg6Gxl9vqQNqRkqo9ujjfM4xe3RFtzkM4wsMCrNEgT1pFOiQsK1AFhLgJtq_C09eCMIZhe0SqOCiAEUuXjYssLL_zTNO7SVNBFR-RfzDGaLiEi3Txo4YQ-J6rZPtpWsQDaD7ujIm7ccyihhAaKFOpdk_FlaGwnn82v_ZeMvSMKE5q5Xvq551QDKhr58l7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=Np3PreMyxQxir0_rOdfiIB2USM8MNF2i6C5CePdgZSkNo1SG2us1HrtO3Vwa5F0g13PgrE62ZrpHpJLFvN-1C1iU-bZdR5SdrZd2fSecRbmpnqxAgYUtmH7bRBj6a9tcQxpazy-9vug2oMLEez7hzhwNg6Gxl9vqQNqRkqo9ujjfM4xe3RFtzkM4wsMCrNEgT1pFOiQsK1AFhLgJtq_C09eCMIZhe0SqOCiAEUuXjYssLL_zTNO7SVNBFR-RfzDGaLiEi3Txo4YQ-J6rZPtpWsQDaD7ujIm7ccyihhAaKFOpdk_FlaGwnn82v_ZeMvSMKE5q5Xvq551QDKhr58l7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKWNEtHnXdZHytRlXVwTL74PJZlsJ1HCONRuHf6mau08LCTGw5G9KYgzOStZ3-xYd-6oY9l0hAYsYjVLIh68gLwP_1GsBQyuTRcz-lKFU6QA8UluakRl9FwYkj9BIVsxuseVedrsyGJ5yfoJwYLlIEt0ZMPgtX6WzQ_Cv9R5uskdmH04CQK_6W0Rg2JyFZte4NVNtoN8p9Wou_BZzs-PYGPAF7g_ysoWb9BCOQyiCXtXX2z0XRwMh7w9cPn-_vddV99nUFbBv28-pTS9DZE6SH3QRz8PbXI7DqsP7Eo-I1XkDCnv-zyXi8i9f-wMzTHznyJJTVMpegyjsrFjI-tb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t75odwgnJJj2TJGOC9brhM_TFYwMQ6qRXwWfqnb-FgqLD73lCVeFK5yoT7RxsL0oIe8EAHSn85dGOQFMvs3EWjGH9U2Q_PFRL8E36IPbWBWjWcU5IN4GP8ZxinTKE4y7Vh-EJxhh8SxLIiNV_7mD-jBm5rEIEWuI3sx3JQ14EKZEZMiqo0mbCTK4vNDTLMfvBy-obJBmVBXm5Dqpxh5CFdmIsUGYz7mUxYr5XO4FasbfXU-NY9WfK9YyRgecbNYdfjoOhar4KfJGYMVRFebhi5fj3QBa5nQrOhuWP8uwtMNMn7liY57yUvZL9yoCBPrOhB7MLc8nXwW95Rn5I876TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=Fr5f5CwGBOzSXJyaKWd6vAafeh6R81bgXFmb-Ig0syBE-Qt3NTpI6NEt4INaiimJs0LBuli12Nl5KSktMTIpCR-nVn5hHqCgA6ySlxap0ouMv88jjF7Vr2cKSNt7xrkMQnIh3dZsdy2coo-9mX0fo3z_IFlwbhxT8f8f__x1U7nWSL9OWA9-L_lJonRBSam3yaQ16b3GMFFCsToZtpfpK0O5IT7WL4Yi2feL1QIt5TCJ--T5CMxeAzFTRGohqM8ZFg9gtRoFLcUkYA-mn9HTd2ka4Yg_P9pVL-8asXWrB6LtWyo6M8c3UOTwmRnKDQczYebovMHv8zd1v6uY9cf_bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=Fr5f5CwGBOzSXJyaKWd6vAafeh6R81bgXFmb-Ig0syBE-Qt3NTpI6NEt4INaiimJs0LBuli12Nl5KSktMTIpCR-nVn5hHqCgA6ySlxap0ouMv88jjF7Vr2cKSNt7xrkMQnIh3dZsdy2coo-9mX0fo3z_IFlwbhxT8f8f__x1U7nWSL9OWA9-L_lJonRBSam3yaQ16b3GMFFCsToZtpfpK0O5IT7WL4Yi2feL1QIt5TCJ--T5CMxeAzFTRGohqM8ZFg9gtRoFLcUkYA-mn9HTd2ka4Yg_P9pVL-8asXWrB6LtWyo6M8c3UOTwmRnKDQczYebovMHv8zd1v6uY9cf_bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z23DAFZMyzhdwYnya2wGfvAuqgPjzVSMzI7BoOLPPKjBFBFcPgkv9JB4nU-znRIG2sIs2-PHl9uPhBKm0R2JDw-Ldcev0I8HMsaKqUzp1neFLJcKHwcVaoZ_m3EM0mZLrhAJmysaXOURCSNDHIFB12zuNz278ZjzHtQcQ18thdAy87NLKuMGgTpkMEiUOTAkj8gY9h36yzC-DfkwXmPq6KbBvW3dfNOUdgxqzh8t6agl1Xh9I5Zu_2_ny5vWnw7AVpYa7Y74RpCXAZJleafwYH1hDCdF4rqOJRgRF8cdd4lZvjzWnGlYAAAhNal0zWuBCMIEEJ8q9FMdMnA9qGLy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMzcQknHWc0ujIOLWl_syfGUm2wn16k2VJqLd3B1xKsRqrv_PK-s9rCOKnjkiEAckih2_XEJD3L4AX_ebT0OEQ1qQhFenem7JTeGS07Z3HKNrqTt5lLZ1jTmy8S6455CH1B4-lXd5Iyvu1Yu6172hToTWc5VOoW97mCkbmmCJ2pgbmDYD4gz_ZytVv_aEt09bYraDLrG1leb82DDQnaBMe76rpmgpjyw2t6p9GeqX2W6wzdx5atmiDVIjAkWI0KvexNDOEYmgLa3r238rGrodvM1YzxE-ovACp8RozLfPwB95Du_fbrfS6RV9tva0Mvi-mctyy4ahnvDCRWdunalpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=udNG23duSj4fx8x-3xE3ToypkfrKznfTYgW3L4ZzG1kQ5W6tsr6SKbBASi9K-fAHVQBCDxyM9zTAy3hDaVQ3XcsDk_0zDBFG-eVhEiRks-iZ9UzYewUU1kKXd_7rBGVO4LtHLbz4yMhJWbBzJsck4QSFYm6haizbwVkJyLJWGaynXa0peQhiP42awuxeuvbZL2KV0QIcDXet7JqfXDrapPRZfEbszZ_MfGWb5ULcVoDiSSaW04-Jh8Cdtl_9uKOlH2oRkQhI6TRAf5q2drDI0cKDpu24vHBrhDGC_CQ9ge6ojLbvh1d-DrMRE7LH6wpubaSfIXyu7yM5NNDMx8rPGkRNohWcXMSa532aluNMnA6SS67MOP0sQGwMbHhrVSjI2QWjX7fN4nVm-q1mbniVpgyNfk4uMYORtDH65OhDqbD7BwE--mbTjPrv5KnltQbQC9dsTh-n61Il3xwOgx349sZpIlemL6c_Tz225kBiIywDZkZRIDH3EUByahHaIGIgTk-ut3wJnitcgt1VKD7pU25aZzLb7N9C8pY1I4F_Y35cTc2zbMnr0h58lvYASKb25ooXH3hk9gjyvaF_mAl0vbL1TwgcvopWbdZ1-ax8dlMZO7-Lk3T1uQaNSEWr4PQXKbW5J8q9sZxqptJ2AD8xOelriwm0EdN_pnI5cqYZkwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=udNG23duSj4fx8x-3xE3ToypkfrKznfTYgW3L4ZzG1kQ5W6tsr6SKbBASi9K-fAHVQBCDxyM9zTAy3hDaVQ3XcsDk_0zDBFG-eVhEiRks-iZ9UzYewUU1kKXd_7rBGVO4LtHLbz4yMhJWbBzJsck4QSFYm6haizbwVkJyLJWGaynXa0peQhiP42awuxeuvbZL2KV0QIcDXet7JqfXDrapPRZfEbszZ_MfGWb5ULcVoDiSSaW04-Jh8Cdtl_9uKOlH2oRkQhI6TRAf5q2drDI0cKDpu24vHBrhDGC_CQ9ge6ojLbvh1d-DrMRE7LH6wpubaSfIXyu7yM5NNDMx8rPGkRNohWcXMSa532aluNMnA6SS67MOP0sQGwMbHhrVSjI2QWjX7fN4nVm-q1mbniVpgyNfk4uMYORtDH65OhDqbD7BwE--mbTjPrv5KnltQbQC9dsTh-n61Il3xwOgx349sZpIlemL6c_Tz225kBiIywDZkZRIDH3EUByahHaIGIgTk-ut3wJnitcgt1VKD7pU25aZzLb7N9C8pY1I4F_Y35cTc2zbMnr0h58lvYASKb25ooXH3hk9gjyvaF_mAl0vbL1TwgcvopWbdZ1-ax8dlMZO7-Lk3T1uQaNSEWr4PQXKbW5J8q9sZxqptJ2AD8xOelriwm0EdN_pnI5cqYZkwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ-wI72P6cETa0QduHJKcuNxlPwoG-vMuC-cHn_C_PLNtM2jHi3uQ7HEMJHbMcNlYoNYx5Y2gIrqx2tcvRoTFSNse_34e9jU9RVmYU3qm9fIQ9iTyTPKV3jcoWiCvKXCgGQiKklp8HXuBkgDA5nCjwBJ0us1v40aCkMbPGrpV1a0Z24NEwfNjF5zBa0rEmjv4TKYZI00vtugMW-zHUIRWjLipFaYKDYTvllchqCSAbv2oiQroW7dq4g6B-BYqcvGkJDimFcVZLaqkAWPetw_k3KAvG0Ptvp9lG30IeqhRi-BKEy3YfnP1vxAHfzN0zQwNcTqUYLiZpaPcERCBUIk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EQsNAukRux3jYJe_LDe6EbuoxSmXyGqbVT2AZM6uQ1Wdguf1raIS_MDhH_XZiGZtUolkbzm0l-81U0hSVOw-hEVS4uVW7bvsUKNIm1-NK_dStxrYB3zKCErArI06_2ldGRVtpUyA3vF0Qp2M_DYJ5EJ9Q4N_SCt4yd9bbUrE2tTOEOCuomsv9sbQKykG0SqqBnk2PBy_dLPKHme6RkOlMr4Z6UwGNfQ12LgvjBvWhuV1j3Cgd3gvSYtcWivB_jsgpegrMcxB7cUBfT0gYOKQFRCKI2rUMobP6HgOFJQ3UpnOsj4Lfsxrj0W8ImK0vwVkhyG0lryg9imqcoBjjYVnQsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EQsNAukRux3jYJe_LDe6EbuoxSmXyGqbVT2AZM6uQ1Wdguf1raIS_MDhH_XZiGZtUolkbzm0l-81U0hSVOw-hEVS4uVW7bvsUKNIm1-NK_dStxrYB3zKCErArI06_2ldGRVtpUyA3vF0Qp2M_DYJ5EJ9Q4N_SCt4yd9bbUrE2tTOEOCuomsv9sbQKykG0SqqBnk2PBy_dLPKHme6RkOlMr4Z6UwGNfQ12LgvjBvWhuV1j3Cgd3gvSYtcWivB_jsgpegrMcxB7cUBfT0gYOKQFRCKI2rUMobP6HgOFJQ3UpnOsj4Lfsxrj0W8ImK0vwVkhyG0lryg9imqcoBjjYVnQsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=RO9vyJIIQntOyQ9url5MYJ6pXFaBxVziKZzi2WthjrjP8O5Bg9QP0voLKgRslf1v0eveAnypeXxbMcjkCkQhRTdUDfTfEVngUvs62ZBpi4XoaNFL0uuRJKmUBd4bq2bO0Y5ycJ5ANotxffwiJz_2UNjWHBW3DtHzt0qJuMT24DAxzUcUK9lo06p4fnQaRUe-W3xNkwdFE42DX3IKj1GLw6a7kxrzmmo03SGvXfq_XBDWFetX7uXitsXquzqq-lQBicgmGJQiNhSCwk-ixAHvu_YyTnx1m4-QmuLymyaznCxPlnH96BjL7cSsJVnVK9bbAbssLYCNSXdrQPaVHOM3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=RO9vyJIIQntOyQ9url5MYJ6pXFaBxVziKZzi2WthjrjP8O5Bg9QP0voLKgRslf1v0eveAnypeXxbMcjkCkQhRTdUDfTfEVngUvs62ZBpi4XoaNFL0uuRJKmUBd4bq2bO0Y5ycJ5ANotxffwiJz_2UNjWHBW3DtHzt0qJuMT24DAxzUcUK9lo06p4fnQaRUe-W3xNkwdFE42DX3IKj1GLw6a7kxrzmmo03SGvXfq_XBDWFetX7uXitsXquzqq-lQBicgmGJQiNhSCwk-ixAHvu_YyTnx1m4-QmuLymyaznCxPlnH96BjL7cSsJVnVK9bbAbssLYCNSXdrQPaVHOM3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQxG3p4MiQtmFcWznZIrLy03fRtKxOWwDnZ8g6xl5pg8ainRCi-fs3G1I6bPrRebTJBrqDBTVPVnlw1TUtnAhJ8fG0ecSVKw6wxYG-BLo_eWfEwxBIfPLRXxNUgM_TxfTxTnKmRcZNK51TkTfw18McG1GzAQxc7LvMWZSUD6io7YcvlvsQgQTipOjXFaIySFInYyl5O29r4XdGfAU_vUY4MmeBJ8P3IEGaRItGlVrqvHtMW3vPPLs7SBiRM5znrHhlXmrOwFZOGvjaUXUXcC8WIa_M-unFNm4dPWaPGQuDuhtXNLI1jyQBAaFR4mEk13jFhF1XwRBDzKSjkkxMiO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=qExcVtMVy2hckznGA5Pa95zFYjtzRXez4BZ6sHwyvk8ohK-07SMsQBFhNuR49aksw-0fX0Drc9HHWqtP7CoDC-xG_MTYZQZ_v3bIIWqE1-4uQ6KXle6jvTpJF5Vj48rnnR7ej2IZ7T-8gixpxBTgj4ESoXGMOBxywZ63BWqR3QlhKQf1XjQEuwaC1XswJ7PTD47V9EM4ccgsIl9l8AiGG-KUxNlazkHoxt3FP9rwvixBVMK8Yhp3r5GE7PG4OTV3uGy3lTKAMNPt2wKK2JAONpKOTs2sW2ZfQwNFi2GWA2rvvNUiQFnBDYfxPgKwVnPXGhI9BZ-jTW1OmSuT0iTbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=qExcVtMVy2hckznGA5Pa95zFYjtzRXez4BZ6sHwyvk8ohK-07SMsQBFhNuR49aksw-0fX0Drc9HHWqtP7CoDC-xG_MTYZQZ_v3bIIWqE1-4uQ6KXle6jvTpJF5Vj48rnnR7ej2IZ7T-8gixpxBTgj4ESoXGMOBxywZ63BWqR3QlhKQf1XjQEuwaC1XswJ7PTD47V9EM4ccgsIl9l8AiGG-KUxNlazkHoxt3FP9rwvixBVMK8Yhp3r5GE7PG4OTV3uGy3lTKAMNPt2wKK2JAONpKOTs2sW2ZfQwNFi2GWA2rvvNUiQFnBDYfxPgKwVnPXGhI9BZ-jTW1OmSuT0iTbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=bXUAyP4GVH5GHqc0AZ-83MqW5zRvEPUupP5dXccyaS-wGhv1LDABSUcdtLv58zGIOeuo-eRFGqSRJJy3Sft20VKWaBWXQIyDWpQsKr7j2BnN5ZshNDQ9LE6QfYzEZi3UCqVUaQwYpC6GMseRJnbeGu3B_6r1Yu9iPqYFJPv6cwvY2bcJ4lw_6WxUPzUFY31hdrcecLkwuEIYWSzqt4wJ441N9eaL3PvxCAP-dMo25LKFZqnEfJ3F0lD09MPXwnEBLpesTsQn20xBf3CJ1LVzl_I2XcKllWQvvw3iIDotlKUNzF0smEfpVJUQfU9iZFzVgVM1cYHxViKZZ7GPwhJne4rz6386OiJF4sMCdrvkS7EzBfjcITwpbVwNO9atU8_TvFFKz6bxSOmtwrdop1clR_Q7yNpWUHbrJFnjxVKudXtWrEKW1RNxI5AUJLs9FJAHIIztHhPMNV4pS0klDM6McoCVn0dWDl7UaClnL0fNJcjbbcCnQrHGAR5JdfJ1X5iBbEX62AnSBfsl-EfcS-aRabNTOMaBBXeKUdTlQS4O3FyjvW097PwBjxXkSzIUiCXPtVFVBeaIF81nb85pwxvGZO4ElVCwbCmds1y0aj4hc4VrjVKlaIU5RMvuSaKTuuxkSha2CyV-mNg6wHouEfxofIDhpNjZq9mcjt_zzHYfIm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=bXUAyP4GVH5GHqc0AZ-83MqW5zRvEPUupP5dXccyaS-wGhv1LDABSUcdtLv58zGIOeuo-eRFGqSRJJy3Sft20VKWaBWXQIyDWpQsKr7j2BnN5ZshNDQ9LE6QfYzEZi3UCqVUaQwYpC6GMseRJnbeGu3B_6r1Yu9iPqYFJPv6cwvY2bcJ4lw_6WxUPzUFY31hdrcecLkwuEIYWSzqt4wJ441N9eaL3PvxCAP-dMo25LKFZqnEfJ3F0lD09MPXwnEBLpesTsQn20xBf3CJ1LVzl_I2XcKllWQvvw3iIDotlKUNzF0smEfpVJUQfU9iZFzVgVM1cYHxViKZZ7GPwhJne4rz6386OiJF4sMCdrvkS7EzBfjcITwpbVwNO9atU8_TvFFKz6bxSOmtwrdop1clR_Q7yNpWUHbrJFnjxVKudXtWrEKW1RNxI5AUJLs9FJAHIIztHhPMNV4pS0klDM6McoCVn0dWDl7UaClnL0fNJcjbbcCnQrHGAR5JdfJ1X5iBbEX62AnSBfsl-EfcS-aRabNTOMaBBXeKUdTlQS4O3FyjvW097PwBjxXkSzIUiCXPtVFVBeaIF81nb85pwxvGZO4ElVCwbCmds1y0aj4hc4VrjVKlaIU5RMvuSaKTuuxkSha2CyV-mNg6wHouEfxofIDhpNjZq9mcjt_zzHYfIm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXoTGjrTUZG-OtC0nNEpZdB1uvv7FewlOwfp8XHNAlibValbrf3qoOlBBj0D43FOuFyRCbjpnhFq9cA2LyyqCFu5BNevIv54SabuEuyVNrQPmnV2v7HGzLvfGFSNXY--Ji2wry8a8ne5nlFpI0MUeDNndDI6iO-J2OWDdEUA4n6HJlADNKbwYvWVBJ-JSpW9J1k9pBguyqnreR1pGZNkPA5ihYBsiT0B8jR3rGztz7QdvZdB5-g7nwpqWRtGhOdrxl6r4DZHRcczqnJr26dcPLb_1tgF29cdpe6QPBFTzWjE64cbX6zAcFzsm8-CL8T5LZg-fnkWxVR-UI5SvYtvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhKPdjQJJqlTacw7jUhhYY3ZmrVqKKHQ0Wsi01vq_1eNJVTRclDYLu9ELrwVQTjPMxGcIzxB-hUUHykkIqWPOXVgOLW0Nz45Vek_JqLA6H0bd58o4mYZ6fGEjb_I3FC5xsFKVdx4kn2_ugEo_z9f5CSqDPxAp1xXiizAnPKnwjcq3bB8HIfY_FmRFEJMUTf4T9kT1uHzNK8m1LjamdWO8wBhm--JEpkz08UR-GCkVxje3pMrgpK7lpXHA7KFbeN3gc-TDeI3MLRj2aiI4rjllwoJSDebG-_Uc7ygx3nfN8Tect9X8w4RqitueGOmqs_s842DFcvv04CjSUVuGiGoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo2kGbRzaAtHEuvz1V3cwY_8ykV-FIO9WiGULJRAxMndRT0Z-eWmCGNfXyz_0Z3W5c3jLwe6cGsF2qB3OeghqJ3JgiDVYm6T0VuohOePU6XuQsG5hlWKIDrh_cgle_jdSk1lYbH9tQA2zIx4mdc4FYER0q6qM1SD1RB3d5ndD4Q0ATtZ6kEQZqhJbq83Salxjhq1EydAvEUugMLfL368ieFXmfXtDD1cElMxoOq790sYj9sJoKb_LYPsJaifwmZs0gbi510yPnflwCYpkTLXjXS7Ju2_l5rZWf9kKXjERvs5JUSi_3TZzIodhd1-knIk-m2fPonQwVEZyWeexMV66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQb-6Mqcb5GBr0fKxEXjt4Z9G-wtP25wcmzKLkddS2BdAB9SGkEp4Ipd_Z9DX-VZ0DhBE_b4T8iQQ7HKrt92eh1PDQhQmo02Cq8C8N03rbYbCOxceNG3zJPGks-ji82pQ8sVGEcS-1X0tItAMwNMDTGHAABko9WKLwvoRND2QzUIvgS3n9V-uChk0AcAzfVoDXIY7CELdDwX_4PjDR4Ec-eyJAZ16AgxShrLR7bwT2U51-nCy3mTKu5QHyceM942uE7BoWjhYH7-KUnAnfnJ6MU2BneFi5egfFOfBfDbpjEyGlTgmnfpaywt4Nnh9vzIFXR214ROASKbfpn0hTADdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3NfMF8xcmYfg056yrLPqI7wjheVPNE1D9FKVgYVcIsTFaywegQ54xIsdQqGtp7sNnzA_3EWa8E1Vy2sbwy2htXXiRjWsPuqJA1cIZ8_4lRtpZcWBkHipXbENW3bPjNyTiqbJKh56_YbPR7hVgxsYRGiO-iJVoX9yFgmsfHpwfv2pmSDs1yxUmh9s99GqxRqjBjs8JxqFVZmlf0aHru8z48l3sMEEIOqlFPvuXw-i4yGcHxUhwfEwC5iUWDKb4weyybWonDYLl6xDomOCS9dcbjSPirFwFa5nyaozKSbA3k0kb7nDJbmtBPguBYqmkuwqe0Zpr814U_R4XT5q9BFAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofK-rpzXIHvMNW5Xuwna0wodjGY36KvctPKECGYFFyiMdoLnq73FgL6UIsZZHFch-PHFyJgtp1Or_diqu0F1F-YtJpGBpcw-PPQ_LYF1Jthu0WIVa6C3Vn81OgaZ0_cHdDnKno_uQx_JTvhaqoJVix-76W8SnGQNkDIFcLkGwkhpAIO7ybYOxnAkBpIu_5B-IDgO6gJZHlu7LbH61jd_yZRMZnsnPsUxcMDuVu6I-cXBQQfxVfi6CIbigMCHlZIiHNZVEU41lpeZgy2K4zqDkxIoP77P_2-PTefzsrx1Vx0_RPf3u6LkpYrJps65pGD8L9LYYwCUvf5EMpan_-Z2yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qlpoUaxD6Cu_d4zCjGRAaIjIxNHS-Ej4OFtZYI2armiMeZuAeZjCB039H9YX3MAGL4Oo5KJVOf2X_K8OY0b5RL6RimaT9bfyDg12CpQ7PZ6uTaMik-tkYZqql9SYs7Rvhb_ewM0kga8yfdWUwhJIaqXR-pWyXpp8R9QfjzTPeJDmuP8qrDxn7i4ZPAES-4sJdoFpySvDvb5LDpkI6N8bQskxG8IP1k43QbKwB5PNyE0ucghwe4bxC-lHr9PmRsUP7MSLorGVQdxwxrfR9mMFEyMrpESWfnZ-Q-jcWauLaOujosPnOST5ATdsGaQOiXQpDNFoPANCwNizuNP0GpEWhWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qlpoUaxD6Cu_d4zCjGRAaIjIxNHS-Ej4OFtZYI2armiMeZuAeZjCB039H9YX3MAGL4Oo5KJVOf2X_K8OY0b5RL6RimaT9bfyDg12CpQ7PZ6uTaMik-tkYZqql9SYs7Rvhb_ewM0kga8yfdWUwhJIaqXR-pWyXpp8R9QfjzTPeJDmuP8qrDxn7i4ZPAES-4sJdoFpySvDvb5LDpkI6N8bQskxG8IP1k43QbKwB5PNyE0ucghwe4bxC-lHr9PmRsUP7MSLorGVQdxwxrfR9mMFEyMrpESWfnZ-Q-jcWauLaOujosPnOST5ATdsGaQOiXQpDNFoPANCwNizuNP0GpEWhWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56plaYxueoVMol2zwuXMabYpVHn4BTVLeg810DRru4CxxhCDeMasjCO9OIUWnHVXYMPVgHL0G7E151F8cUB5A0m-UEog5O5qVmKK8iLhB2Qj1GXKNNmf8B850u6D9LJLK1NBHM_mVZpxwl_-CYC9F5K26uOwsyItwsi-7_yakSPfaccZKU9vdkKt2baYGInMdcBn3MFcugrdu1X71m7iFIIDxjF3Of37hV2Fe-X1_rX4-NwG0Qy9OK-wMiaZ_WnbnT5ai5lWD5sgTKXqet9RhDm7DhiQXenJQVFlHV3bJsNnmW_DU4x91a-jeM3meo0D6T2w2TBhAa3Of9p5MxO4j33H4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56plaYxueoVMol2zwuXMabYpVHn4BTVLeg810DRru4CxxhCDeMasjCO9OIUWnHVXYMPVgHL0G7E151F8cUB5A0m-UEog5O5qVmKK8iLhB2Qj1GXKNNmf8B850u6D9LJLK1NBHM_mVZpxwl_-CYC9F5K26uOwsyItwsi-7_yakSPfaccZKU9vdkKt2baYGInMdcBn3MFcugrdu1X71m7iFIIDxjF3Of37hV2Fe-X1_rX4-NwG0Qy9OK-wMiaZ_WnbnT5ai5lWD5sgTKXqet9RhDm7DhiQXenJQVFlHV3bJsNnmW_DU4x91a-jeM3meo0D6T2w2TBhAa3Of9p5MxO4j33H4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=ASWDa5Wi0ubjsgWF7XsDV26EeIRAZNsLILpWULA5X8k7JN-ZY1qRX0ctYR3TA9broSnCREirGVBRtX4ERo53YUaTExH9Pk0Z4CcTZADqJGAXxWBVrBRLpu5dQfJGOfTx4pkp2wCD4lGxl5FqDGcrVXsyq-WvCSuj4yEhmYJ2gwRI0oul1VSRzQMFGK_HCGyVURhQWY83yXKl58pKS03RqrUQuqRFMqLpMNTeuiB_4pOWPWhN2HREY0FQMzEshGGxx8ltzXGFFw1g0zrV87HkIKuOzbZpH8-Rtz34B2dvpAvT4q0vKD8wn_uyUQKkomi89L4sCB61xQzHLMr4jm2BkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=ASWDa5Wi0ubjsgWF7XsDV26EeIRAZNsLILpWULA5X8k7JN-ZY1qRX0ctYR3TA9broSnCREirGVBRtX4ERo53YUaTExH9Pk0Z4CcTZADqJGAXxWBVrBRLpu5dQfJGOfTx4pkp2wCD4lGxl5FqDGcrVXsyq-WvCSuj4yEhmYJ2gwRI0oul1VSRzQMFGK_HCGyVURhQWY83yXKl58pKS03RqrUQuqRFMqLpMNTeuiB_4pOWPWhN2HREY0FQMzEshGGxx8ltzXGFFw1g0zrV87HkIKuOzbZpH8-Rtz34B2dvpAvT4q0vKD8wn_uyUQKkomi89L4sCB61xQzHLMr4jm2BkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=sm671xBtb9PRBNI0n_J2MsM2D7FDnySdvCzKQf_gTJhan9AXT--VLjf-sw2CFOF-OifPNHqJCyo4-26ZqQ9kVWtCGyfikMetvLKMqqx-NBC1vhiROgAuKvofENxpq9ir7DulrX7jbsIztIknMZB0A-7BHWaTSDfjxcssN3eW6JihUGGJgvCdZ8hX0Ldbn94LbQ_ZlosxLHaM_DqopSCFkEy1eJAOuyxhw0ezakiK0djJzHSaOC7oB8pyAhulGfmAMWGrNWe1tre-O--rWdrA3qq0F26x4cmqa9eZsxq1-v_6lSryCXlY8vmKF3lYen6QMaJ4avbNSxOHhE6pJvgXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=sm671xBtb9PRBNI0n_J2MsM2D7FDnySdvCzKQf_gTJhan9AXT--VLjf-sw2CFOF-OifPNHqJCyo4-26ZqQ9kVWtCGyfikMetvLKMqqx-NBC1vhiROgAuKvofENxpq9ir7DulrX7jbsIztIknMZB0A-7BHWaTSDfjxcssN3eW6JihUGGJgvCdZ8hX0Ldbn94LbQ_ZlosxLHaM_DqopSCFkEy1eJAOuyxhw0ezakiK0djJzHSaOC7oB8pyAhulGfmAMWGrNWe1tre-O--rWdrA3qq0F26x4cmqa9eZsxq1-v_6lSryCXlY8vmKF3lYen6QMaJ4avbNSxOHhE6pJvgXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
