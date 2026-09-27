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
<img src="https://cdn4.telesco.pe/file/No3xGFjt95j0VvoUnPTzrhFudo9OXI0J38ug1HlztX_9xATChG0VOlA43HVyMPDg_uR5Nl2J8u4DBbltoJtaE0VKjBRCtzAwSNq3I_i9XR4qzj-5qn3JPMrqZ26GHPfAVSkmWGfpWGX8BAgskelRAMC18R7d2E5k0G2OdXTv3Xb_qSRc3pVh5zxpKgOwKj_rCItROw0w1Z2ehe0PO8iq_4dnFvgXAAZ80BCo70LiepFyPZm19V_GX3VgburrGViDAfnv6zffRhurDBLKtJU2k0z8e6vxj61wXxQmoKQdjLxXrSSQiUmi38ywKaGUSN_HOXl_pNmircI01DcPDo0ROA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=adcpW5vlW1UBbJtcDF_Cmcgmm8ubmbcjKsx8gBlplmOHNjqqIOKBdp8VhSn3-I-J67ngWyBZwIr46hR7GBiW5I5WvTC_8B6kTiPaXZ6EFXUX3VZA0wEjUYD-_kQjObHM0R4_r_MSHcx9vCsamGddm72i8TUAEVYsTi93WMoF_gTwURqGYVomNr5gwa-6GAAvazOPNAD33lvBblmC8mkZv6DjD814FzTDmJWG4HsZzoIwAjth_57d4jVFLmJs8D79ad9QAeHK7Xx2Y5mJyyZnO0meybXDnuQSSxgcVxCF-wEACprI3TKrX1106itTEWYMShqUdSipy51rihfmD6lAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=adcpW5vlW1UBbJtcDF_Cmcgmm8ubmbcjKsx8gBlplmOHNjqqIOKBdp8VhSn3-I-J67ngWyBZwIr46hR7GBiW5I5WvTC_8B6kTiPaXZ6EFXUX3VZA0wEjUYD-_kQjObHM0R4_r_MSHcx9vCsamGddm72i8TUAEVYsTi93WMoF_gTwURqGYVomNr5gwa-6GAAvazOPNAD33lvBblmC8mkZv6DjD814FzTDmJWG4HsZzoIwAjth_57d4jVFLmJs8D79ad9QAeHK7Xx2Y5mJyyZnO0meybXDnuQSSxgcVxCF-wEACprI3TKrX1106itTEWYMShqUdSipy51rihfmD6lAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elcHb6yiaUJwvLFRbeFQsgJbActSxfuHDrkteD3bxxT-6_oKthVH84d_6KVb-kTN-3ZIfHcE8EfxZy4RFVnWf5z3I4O0urswAFbBHUKgHj7JFA8G1VVFjbqOWlFTCGPVqFQMRrc7wMzf9emysD_RltengCGxm8PEMqUqas8shVXq319Spz_X05uadiLhPJbvj9FLf8GL2nc-q5_kEVMFpfhD6E7_k62QvPeeTatun4mstv5VRBkFKH3mzi6i-czpLjYjmjNHxj-Wgk5xQQISOY9jc8PIIQr0DrG8-dKNWxvPVh7xEiBlXhOZQsraLtCEPnRR8D-n5kaAW6DZsW7H-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=gHmnYQHfanNNx9Elqv4dxDrCFG5l_RLaHD5CyM9KcBCkH7-3Fp2fMm5YUITzP-un6H4OukkA7wvJbvvwSxd3Wr2sDKNV7Wu5VmEuFN7f771_bWvkpM1J5zV30KKllRe2cfwO36MvMyrNRuoghFdBxWSwVkEhk5OtjSq4_GvBJM3d2ez18yg4GXDVCDvQpJBNZfutMgvtHbsSit8lrXcpu0jOFCRd9eygGQetfTEZ2WmxHvZ0v_zQ5IDc4nD-2z-p5BTkciBMq_MBuZnuqnlwLO0IrQK5IfS0AM4RvcnBESTGB4yERSA4ywvVmF6pivcv2EDuIZsJ62gLroE_rb9T6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=gHmnYQHfanNNx9Elqv4dxDrCFG5l_RLaHD5CyM9KcBCkH7-3Fp2fMm5YUITzP-un6H4OukkA7wvJbvvwSxd3Wr2sDKNV7Wu5VmEuFN7f771_bWvkpM1J5zV30KKllRe2cfwO36MvMyrNRuoghFdBxWSwVkEhk5OtjSq4_GvBJM3d2ez18yg4GXDVCDvQpJBNZfutMgvtHbsSit8lrXcpu0jOFCRd9eygGQetfTEZ2WmxHvZ0v_zQ5IDc4nD-2z-p5BTkciBMq_MBuZnuqnlwLO0IrQK5IfS0AM4RvcnBESTGB4yERSA4ywvVmF6pivcv2EDuIZsJ62gLroE_rb9T6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCsCadPeFAnMKETF7kriyXUpwIqf4-mdtiBS78pdpgmNUc6sZ3pshQCHHtKQdtCkScLEs7ST-pG60GsQ6Zs4V5pYGBU3gN2D_646VBc3VYzmfCZ_7qbCegblh1zKr6hoVXuugU5Mal80oq-GrULrkf0Mje8vTDuzunt9AUzqtKs4VwSS9VGqd4LmbjOQNZyN4Ed71jWkbEks9P-H5J1FkGhV77ij8DGtTP2yFZyHwgusvhGejam6oSxxUCLxoLc0mdaPKavsNN2Xk35Z0krW6HlccFhdUaox7zTRY4Wq29yyTJKGRxiITLjQZ4H7pRr5ubCfBIi2CnuWbG4NoemnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qumRAzwBVZTf2x6AvNxtMy3b6taNPqRQyv-7ykhe7l6BBu3_Gk4TgG4ky7Tf6YHl9IIWUbTxH1fsJXduWAAWa8Zns2TDBEeDN49J9GfypiAmJcAnhAUEAXDrIAxatYviIzwjz9tFH0gujJPlAkxVoqBhs4afWuabIkeKuLYF40sarZvB4fZxYFfNhDGRvRoU8kk3427lwF9ZeOvVGsdrb1i9-1UWxVfA4cMM4cOvN8iSO_L8ybXJLhhQT7riIcQ6CZrNn4qYjKmaEvJWJd2jRsdHn8JfN8cnYzIWBt5TaDnJHkth7K-OcTawgBQ7Iz1sU1B9i3hCxAr_UMG51VVmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=hAL7DAzBNrFPMnTpNdCBLKizLWiaeXM8YUgUPNO74_yWZxYEDVTazmHUJnnuW5eEu18FheROvaOMUYQlYm2OxevJhKyZXBJHz_GZe2ng_sbAe6zL8PtZ_BHKvdaNHVhaghEabK8ayuqZ96ThIqlNNhKYnE5_bZwe4FiIAKDMXaRbfw-CM_21vYKgZASdZUfU3EINCGoq2cVqTwiKbQB8PRXnAthqJ6XK8mnidDLp8OKaNw9pkpqqBAm7PLA0P_qZZXX6mCJGzMjJuG1363GU_mhrPqvo4kMslGYY7N4wjeNHqBUJfwA5DMRdlZz0yT7JMkhCCbpMPlnDxFwcqztYyQ0EvBXWLG4IuHTuu-4Ox5wXLy9YZXpHLk9CktoUAaA6wkOGhyey51pCF2cXxLE1GtQK3SihI823IPOaScdb7b_jjb2_sjkicbF418thCJjeWHP7S6-ZTXVh6zWRxfWA1EqAa-pRpGzYeY6Z4D8vrDH8WdPBsCUSykUji3csCyncI1sepHZV9cotp6eAjjn3IdxnuOPVRjNWetRMhSGyXrd9QjyDPSSQnp_rmW-HzSx50DyY9_6gbF_R1NEuvNlVHGaZB19fe4OuNYiwUPCrS1NhrEon-YEq9AclX-J8B55XzYMLWpzTRF9rJij-WnoNLfJ6ADEB4ZOB2MXTF2MoLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=hAL7DAzBNrFPMnTpNdCBLKizLWiaeXM8YUgUPNO74_yWZxYEDVTazmHUJnnuW5eEu18FheROvaOMUYQlYm2OxevJhKyZXBJHz_GZe2ng_sbAe6zL8PtZ_BHKvdaNHVhaghEabK8ayuqZ96ThIqlNNhKYnE5_bZwe4FiIAKDMXaRbfw-CM_21vYKgZASdZUfU3EINCGoq2cVqTwiKbQB8PRXnAthqJ6XK8mnidDLp8OKaNw9pkpqqBAm7PLA0P_qZZXX6mCJGzMjJuG1363GU_mhrPqvo4kMslGYY7N4wjeNHqBUJfwA5DMRdlZz0yT7JMkhCCbpMPlnDxFwcqztYyQ0EvBXWLG4IuHTuu-4Ox5wXLy9YZXpHLk9CktoUAaA6wkOGhyey51pCF2cXxLE1GtQK3SihI823IPOaScdb7b_jjb2_sjkicbF418thCJjeWHP7S6-ZTXVh6zWRxfWA1EqAa-pRpGzYeY6Z4D8vrDH8WdPBsCUSykUji3csCyncI1sepHZV9cotp6eAjjn3IdxnuOPVRjNWetRMhSGyXrd9QjyDPSSQnp_rmW-HzSx50DyY9_6gbF_R1NEuvNlVHGaZB19fe4OuNYiwUPCrS1NhrEon-YEq9AclX-J8B55XzYMLWpzTRF9rJij-WnoNLfJ6ADEB4ZOB2MXTF2MoLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq4v68gu8qZgxyv0x79koN9sXy2NfJgr4zlAPbJoX6sqmqELWbjEQTrbvomHOnxNkcWSuj4Y4tmBXh6xWHmv2-c4UUln_v5nqIwWQ5t-kLuK2HRLPJarh7TO-HWwseVqrFf8qRFH0MYhJ_eeOtKNMZaxnPlvXSWOICRGJG6AQlCxP3cYAWO8Vc2u-mCs_q2i0C51UfNBfmdQL1FBOAT1OCqHUNqj6RQI6wpzZcp-4LYvHpkr_iMaIICbQOuYB2MJ2qcoYHXnRekwaT5Xx9MPUIHzsrS5EMJhyJENDX7YT50y31aHd2LpgYoc6WVj3ft7HTw7hRHklbhC26RpRSIS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcHxkj6C72wV43Bq20KAQFohBCWsH5WAQZo4JJWQY1uB330QcfOqa4ZeZ7YeSWrLZyvUJgUjY7Om89ydf3sRy4PQqtpTOkZWoirgFNBa5YqHQ5-JHyjouO0BIpoeIQ19mIJt9rGbMt5z7V49gonQr4iRjPGx8Cn-YFkMAmlYPN8-pvv-Ry5U5ZweR-bP7YgyBSX_Kcn0-qGwDusUSLjb2IAjyiMb47tIuG6K2ZfyfiLih6t8h9vo3GDoDdtfNW_IKBwkFsg2t1azgDJo4P-wROpHlbYTmc3HG1yhgEu1hnnN9VvoCtoDbWELS50kGt7OZWg2W4zABk0eXfnFXnXAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=q-dQj1BEPF1dIhHw9P0x1QcYizBk3IP3-QjKTNrEFK9CltZURJuqZiB62BtTHY4BdSdwlecx_0VEjh13GbpW7GVvT5VMo8WoLUu2TzZEa53y4t-IvtiE6i_T1E_Ht7jaZLtCpAJ3NIvPY1oAmYCKUe-YAKiVY8peqlFzOzpAGTzHLLB9LlHQ4Mt8fS8GwKRfaVkmli6JFFSfNt3oGXIAu6yD0apJaHL66dfHtar2DT0fMRUvZs1lU1HJ1zx5RvFwAHKRO9DLXCwHSASTVIywfUkA8riz-RJhLZTkOw-Vf8T_hE0D8FVCGm6yx2PYvLN32ZQOrnDvP_iDLu5lEYpIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=q-dQj1BEPF1dIhHw9P0x1QcYizBk3IP3-QjKTNrEFK9CltZURJuqZiB62BtTHY4BdSdwlecx_0VEjh13GbpW7GVvT5VMo8WoLUu2TzZEa53y4t-IvtiE6i_T1E_Ht7jaZLtCpAJ3NIvPY1oAmYCKUe-YAKiVY8peqlFzOzpAGTzHLLB9LlHQ4Mt8fS8GwKRfaVkmli6JFFSfNt3oGXIAu6yD0apJaHL66dfHtar2DT0fMRUvZs1lU1HJ1zx5RvFwAHKRO9DLXCwHSASTVIywfUkA8riz-RJhLZTkOw-Vf8T_hE0D8FVCGm6yx2PYvLN32ZQOrnDvP_iDLu5lEYpIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=WBq14-x7GKIYlGhBkKj1kRRcGFwxMAWHPQSmfIxmrq2MNYpB_1ZC2yK_oTez_egyO1rrkwWfhZYiBTM2reqp3SUKCTYoG8k7lGQ2nrjz_MIf6AtLKIBqR30oeKBr3gQ3k3NO-4fyirmsAIidR5BXaXNWiNg3ugNei5_AnJO40dogd17z9n6jpvxveJhyHVcRz7HEqAn5X5qk9VPlTHprtnNTq6ihllLzIj5b8H5K3xE-O3YmIYjrtZzXRNY0p8J82z55UdEjwbGQkKYuVUSGMCqL1hZLe7sCnoaaI0ITQSbcEC3fwxG7HWFfb-RiXyf2Can3srhtec-LMHPBvETj8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=WBq14-x7GKIYlGhBkKj1kRRcGFwxMAWHPQSmfIxmrq2MNYpB_1ZC2yK_oTez_egyO1rrkwWfhZYiBTM2reqp3SUKCTYoG8k7lGQ2nrjz_MIf6AtLKIBqR30oeKBr3gQ3k3NO-4fyirmsAIidR5BXaXNWiNg3ugNei5_AnJO40dogd17z9n6jpvxveJhyHVcRz7HEqAn5X5qk9VPlTHprtnNTq6ihllLzIj5b8H5K3xE-O3YmIYjrtZzXRNY0p8J82z55UdEjwbGQkKYuVUSGMCqL1hZLe7sCnoaaI0ITQSbcEC3fwxG7HWFfb-RiXyf2Can3srhtec-LMHPBvETj8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=a6awzOtox3lSWSw5quQyHG2JaMub_JPXReqVK_Qm-SL0RAGQaNa2jhQJFc4sl4mmYc0zXRRATP8IfXSXYqenY6Km6SYJJR8GYrlkwcMheb0Z51dg1bspu1pJcfCPeNWSFQf7kaifq8Pz5Eo6XrzzQtcGpQiUT65DDSsEWDiD-PnxgR7uws8jOoyJoJ-KFXxMGGedPjelsmHtYFv7Q4niy0PLc5CvSo36Fc-0hRffQHj2lpOx6LESWVjkneUJYSvqoCyfbqF43M9FUrt6RaGzc5eVEn0H1QhXQc1yP_zzTcDbDT2iiHA09A1wBPExZ3ZEYOjTGTKc-vKmd8Ldso7NWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=a6awzOtox3lSWSw5quQyHG2JaMub_JPXReqVK_Qm-SL0RAGQaNa2jhQJFc4sl4mmYc0zXRRATP8IfXSXYqenY6Km6SYJJR8GYrlkwcMheb0Z51dg1bspu1pJcfCPeNWSFQf7kaifq8Pz5Eo6XrzzQtcGpQiUT65DDSsEWDiD-PnxgR7uws8jOoyJoJ-KFXxMGGedPjelsmHtYFv7Q4niy0PLc5CvSo36Fc-0hRffQHj2lpOx6LESWVjkneUJYSvqoCyfbqF43M9FUrt6RaGzc5eVEn0H1QhXQc1yP_zzTcDbDT2iiHA09A1wBPExZ3ZEYOjTGTKc-vKmd8Ldso7NWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFgUigm0gZOkwOVvrgpR3ePHoGg3ZEbJ3lGzm_ZKtnW5nEVlX8IH87if9KaR2mFWKUnsxZCFKG-uvpU9JP7dzBExccJtuHRy2H3x0Zapa9TSRPa1ecJ_Pryk7fhoqpwjwtGRQzlAhw9NN0JYDz9oCunwuB7dAtERt0wu7uB4Eu41Su3VYDguzXdP3-ndAJLsrLPCDBLiJ93PzwZAcwOhpkpS3h9P1Giw0ToyFp__inmm0IEKYalsoARzYJXkKspix_Ieeg39SSbMw3YDFYiz06sRGbA-YLIDJnP3l44U90XCCLvXa9MpbTISpjXxaVPLDB59m4WUjADmyNsTxWU6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FtplQR7vm8E8zsZ0-e9nUbBddaA87q8dD8N1BVNa4_0jmXL4YcPAsC5wFYolDjtP6FkKP3XF8y-hupnkJjWogn2mft2oDei5OWzfG2xNO7yM_BniovncO_LekDxTZVl_ZF6WbixTPeQ0tzEcji-k8LV5P2QId77WUEeQF6inWmuaAj9XPuFGiblIuyqpJIfyA5x391f3rXQeSUio8pGBPd_iuXQAek7frn0DZOzOh86NOVVtoGyQITV6XWHCqGX1cx5ZdqGGFyCodZnm80nXSi3LAyNxDFV4DUKOcs8CBnFiuRco0j04qrhmvVtbzDwuWQ6RFGQL10gWvRIb1NKkSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FtplQR7vm8E8zsZ0-e9nUbBddaA87q8dD8N1BVNa4_0jmXL4YcPAsC5wFYolDjtP6FkKP3XF8y-hupnkJjWogn2mft2oDei5OWzfG2xNO7yM_BniovncO_LekDxTZVl_ZF6WbixTPeQ0tzEcji-k8LV5P2QId77WUEeQF6inWmuaAj9XPuFGiblIuyqpJIfyA5x391f3rXQeSUio8pGBPd_iuXQAek7frn0DZOzOh86NOVVtoGyQITV6XWHCqGX1cx5ZdqGGFyCodZnm80nXSi3LAyNxDFV4DUKOcs8CBnFiuRco0j04qrhmvVtbzDwuWQ6RFGQL10gWvRIb1NKkSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=Zz9it2bJrMmsOl2o8vIFMuki26t9ShZAiuTBZL9VHq-j1kgT31dJGcm1md19R6giPFQevgo9RglTu394UDaVohs6t-i2ZGhz_jTpObdrddaoswVONlL1znOSildaTgtikMFezGgMnraOMjiG6iSjx8klk_WIaxEi2-ZKjMhkIjWgL9WUVceJNPsDEkOTVk63GkAi2qZ1OqbhkicVFbLf69hItXJg90Da_Y6KN1E_QeuvTsXaMfvi_TH9N5ABRnRg7QZQrK6isyvX0LJhG_GW3hh1ASDDRCswg6tNpBnkMVFSiMVt8CCoV1KiG5FNxVtcrOXTE4DUY02eViLbjjS-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=Zz9it2bJrMmsOl2o8vIFMuki26t9ShZAiuTBZL9VHq-j1kgT31dJGcm1md19R6giPFQevgo9RglTu394UDaVohs6t-i2ZGhz_jTpObdrddaoswVONlL1znOSildaTgtikMFezGgMnraOMjiG6iSjx8klk_WIaxEi2-ZKjMhkIjWgL9WUVceJNPsDEkOTVk63GkAi2qZ1OqbhkicVFbLf69hItXJg90Da_Y6KN1E_QeuvTsXaMfvi_TH9N5ABRnRg7QZQrK6isyvX0LJhG_GW3hh1ASDDRCswg6tNpBnkMVFSiMVt8CCoV1KiG5FNxVtcrOXTE4DUY02eViLbjjS-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b08o0RvRVmvtd4nbrq3mJE-fUUAmGPGdbZ4YLnSME0MouLZ050sKziTvcHGbpX-YmN3kOWHop6haT2RH9UVaLmblObeaibv0BQ2itTrJe9PogGpSIvkJos_fN8PUDUpJvl6zkmiu_tq6HGsk17QGIHaqLAiaQTJDc_tssR5MbfxGekU6zlvNo1ksaTUtVg5izw1KwXXAl9KLlVVU3P8vValgZ5Q-hNFZliUwTytgSyiLqKYdHi765Z0JGUcW9RLXtQovQiqONhUE2c_DgC5ECT-OOjPQXZBL5w1dnX0gke-80e1gtmZg_S_kmJPpaRXmnPUoHGQlXyVtVf1MlKgvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=qoevQEAx9h_qu8E1DtK3pyWfCtu6fsRKH4ejPKkSdJ8_2KjLZ2Vbeb0szsfNzM4XarmnSCSJu1GpdySO7dbcrzhr7j2LBgbU2eSsMfkXatxIWVIqGtI5B_w-kTk7jZrD46XqUhQtXL_fDFpXdW275spYwz2NLIOhB8YOMSQ9ruevIpnGam20LOtx6iIjZ_mXLoJ5Pha1HDIBekkJbxXRI9BQixaYbmYlzGs3B0juoy4KKhZG_g7zpYJnlOEEeX3gdH3MBLVW5XI4K6Hlc9fwk-SowgA1Y0IFFXOop4HT0SW0i_2hhQyH6M_cNccl4v2ShBObToyABigApgxAXs62GHA7NAI38mpGUmfJDwbES5ayyKr6HIwUJL7lqs0tV5KhAcuDCYERZMFK6ZbUUAgkNS7-s_RoTBKrqazwf_-P3bMF5Ijznq-d4B1tqorY6EV9LKHYeu5vj2FVMWWoTGktjWpUvImAfl4lRWvJ6sJgmmXcLp1xe8vSnbJHki4xHcbff0lKfbcMEPrupQPgtX4l_PX6l6Eeu8iSo0rjZh47uHsLNqs2ILHrwUhmw0Q_KlcLVW9WEgKmKVdZ4WQrmHaNlqpoKclVKKUSrXWIxM0yMgiTJHqqmwG4oO3kl5QamhdjMRTxItqIKIe0_3EjqLSZGNxvXxbkcKXRq9BW79nmS_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=qoevQEAx9h_qu8E1DtK3pyWfCtu6fsRKH4ejPKkSdJ8_2KjLZ2Vbeb0szsfNzM4XarmnSCSJu1GpdySO7dbcrzhr7j2LBgbU2eSsMfkXatxIWVIqGtI5B_w-kTk7jZrD46XqUhQtXL_fDFpXdW275spYwz2NLIOhB8YOMSQ9ruevIpnGam20LOtx6iIjZ_mXLoJ5Pha1HDIBekkJbxXRI9BQixaYbmYlzGs3B0juoy4KKhZG_g7zpYJnlOEEeX3gdH3MBLVW5XI4K6Hlc9fwk-SowgA1Y0IFFXOop4HT0SW0i_2hhQyH6M_cNccl4v2ShBObToyABigApgxAXs62GHA7NAI38mpGUmfJDwbES5ayyKr6HIwUJL7lqs0tV5KhAcuDCYERZMFK6ZbUUAgkNS7-s_RoTBKrqazwf_-P3bMF5Ijznq-d4B1tqorY6EV9LKHYeu5vj2FVMWWoTGktjWpUvImAfl4lRWvJ6sJgmmXcLp1xe8vSnbJHki4xHcbff0lKfbcMEPrupQPgtX4l_PX6l6Eeu8iSo0rjZh47uHsLNqs2ILHrwUhmw0Q_KlcLVW9WEgKmKVdZ4WQrmHaNlqpoKclVKKUSrXWIxM0yMgiTJHqqmwG4oO3kl5QamhdjMRTxItqIKIe0_3EjqLSZGNxvXxbkcKXRq9BW79nmS_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_lUsCSaapBxRqmePOMFKKFpdEWH4zx25VnoIQNBwaEdTTRMLk_6vw1mELPKYituHqF9qSWzGcM9Db9OSOJP-MwKuoGEZhJQCuRv3GfXEgBowCsqLK0bRIuIi7yecYWF2SaX82ltgvteGPoArfXGxH7-H_wpI3ENYMe1KkElxm2u9XrO5-Bk0j_pK8FYPoaZ5cFBZq4PIiYlz--YkElB9z4yA3EyTZFW9UsmPtFbaNPLQXmSeQhV98pwHDld5k6IbUYhhD1vEvbVwe8D0uyloa0pjq2XTBgLh-R8BB3KEG8F74R-M9K0xW80P3Jty1TdpicnNvJOyBPnO_2unDs06A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=QDJDqXfEApsA_luxrClT_M_pkWGYZ4J5YslmRFf5xQrybyEFwusxCkfHXAYzQKImJkFIWPcqM9MbxKFZMVXlWkzaMOAV19WR5SpmQ2G6fESvfurUpmqi-6Pxh3LAueIt_duZcATTtY2gem9QvMp2tB4DJnKe4oN7wIq8QOwAqp-f9TM0VQFHaqp6-H2REtdtbseLhFJEAlMcCTZ5nFND-nECA7BxarMHtUZ-7kPR3dZtTOiBOn5r5yDCeyymJIvgpF1EyEcgzZqY0F8coAW9N8DLxObVG-s8fua04bczuYCSJ-fQmaIHX55UU-cGTRwas5wVFDbACvYEZiVdheZsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=QDJDqXfEApsA_luxrClT_M_pkWGYZ4J5YslmRFf5xQrybyEFwusxCkfHXAYzQKImJkFIWPcqM9MbxKFZMVXlWkzaMOAV19WR5SpmQ2G6fESvfurUpmqi-6Pxh3LAueIt_duZcATTtY2gem9QvMp2tB4DJnKe4oN7wIq8QOwAqp-f9TM0VQFHaqp6-H2REtdtbseLhFJEAlMcCTZ5nFND-nECA7BxarMHtUZ-7kPR3dZtTOiBOn5r5yDCeyymJIvgpF1EyEcgzZqY0F8coAW9N8DLxObVG-s8fua04bczuYCSJ-fQmaIHX55UU-cGTRwas5wVFDbACvYEZiVdheZsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3MFYC2fMJna3Zvm0zDjdkn3FNMcqYZC17nP2ZHc9e7iL1-b1UgyzzjZLsTl9rraeqzkv9O6_P16_z8tWbVKvjgY3EX3hpzuz6INmHHRCbGyrzi_KYMKQFj_uiEpQMRsinW0DDNl0oJVyiaFDt6Q9Bsr4oRzMc3wIm9i_l3cvTYrMXBWvRNeWpRbaf2Etlw2m7zgsFQU0ewMIJhaHiE3y6P3qC3Jzb65b5deaKvd1ddGS4frbO3_S8VZnzdcrjBSNiFbHnW4A7ZoBxWqD2c5VtpLc_l7PsmPCkOLvgbk9nIdyPeEBcSAabTdchZ3sCwHwXrQnaJZ_LIfRnsE5kASmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cERbcflcC7q4U9h7lFWFc0skJgGOrUjlnzFpCZVhWWC0nALRl7vTbfobPj6E36vO8PEmuBP_ywTkLchcHUtaf2NWsctyVvTgiZNt1i633Cf6NN96xVmKrhebVF7Saah9jyAtep9Gk8wz1BxUwCY6dB9QHR3fXwgYBJMHrvV9kxYY9JCUrbj_fCoXV9z0PlIPXZxwrLEYWfT8yJtU5fpe3aoCECthJHdG0b2nADrCc_Cfgr4P6UKyvMD-JrYxFD917_Joiv-u7QNKuqugtUbwsiZih5oj5EY62Eqk1YQYZ5ZSSMdJUwC86okTzS52cGzkg4pI329o4GLsqFvppTyjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8CUk8UoqUe7onTM3hRgagcdAi2htSwDdL8ac7jV8LssxD9Nt3r6ZCeYIKf74bKh7I_Yg5CXU4vSwwgc3KGH_K2vfdfY0H7bszJ7loxTaJD6N86UGEppL2BNsRhA3AsYz7yojfbn9vZayF0SODE_4ad4YGfNALkCIyI1vfTFYSwEbKk3KMQp72Qw-g-fqyDSLCn9PvtSpAHmhce89xjgZM9ebE-dhbIuG9BXH2SgNmpo35u7IxiSpYR-3ac7EFjld0KM7Zr-UYCuqUUBBmLcQjPYq8jjF_By8_Ps6aLma3nyhvwc4RQrQS6INFE5kogh1lPrXYCcQp0YyMYowlt5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Cw0oVFgHJ5AXFz7jHTwz5c4c242k4ukMFuReqeaJ4uyaALuPo9wjhtgc5c2yuZVJa0kldRhz5sdVtjxa6MwAdP37YkjAuY4wfyoo8jHZCTqXHwS9lYxwZPyNzQ_OjY7YqUT6HykA0PUXJBqLbB1dJ4ebzA7ppHabHgKOtMzrPpgudUtBuhgQMOFuRw9u93Ib3jruarv9dzzZTaT0Ax5-DuaS81u6KrukOBY0wCi9bGKzJYcPUrVUSI6YakEvvTcVuAkn-QUfzAXGnpTIr6tIIoibQaJIgDagrxu-BcJt_zElD_knqLzwDwnv3V3QrCFS6yy0E-wE1XV-RgijTEhtLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Cw0oVFgHJ5AXFz7jHTwz5c4c242k4ukMFuReqeaJ4uyaALuPo9wjhtgc5c2yuZVJa0kldRhz5sdVtjxa6MwAdP37YkjAuY4wfyoo8jHZCTqXHwS9lYxwZPyNzQ_OjY7YqUT6HykA0PUXJBqLbB1dJ4ebzA7ppHabHgKOtMzrPpgudUtBuhgQMOFuRw9u93Ib3jruarv9dzzZTaT0Ax5-DuaS81u6KrukOBY0wCi9bGKzJYcPUrVUSI6YakEvvTcVuAkn-QUfzAXGnpTIr6tIIoibQaJIgDagrxu-BcJt_zElD_knqLzwDwnv3V3QrCFS6yy0E-wE1XV-RgijTEhtLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNDI8unQfjoDTK_saPGSEyvS9l2v3TjQJLxeACfg-rQ0TBY7k0WBJT2RCCHefh8M28Vg7CYMJJm6xy6wUNNNpAupEwGFYrS4ht-1ctCACF9mHApLK0KYXBmDKNrG_HbF3k6atUJhskNj8wu4W_ZquJE6FAopt56u4jNgDk_CPoBOr1Pat38KyTcDxXWW-QyxmogsxIMIFLqXK5VTLIbcs1DcbGN96PqLKRQ8FAkdgXL1qXGivfJbQuOYLvb1yWUpGa9NmYw3Vet76EnCXNwS6I1oMowhXwoLhIHqxOsMrJ8eYJMLd1Jv4F0nJnz9ib8Mj61pMv-OvvPaFN3238m1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuwKgFJKvJ_7cYc38oZF8E0_FsAG69TKvYkrgbUVZdM5rC3mk2DiA9_enYG1Ngqx7O6YHLDuvkZBc3D6wbyOPbDg739LkWXOGzpIs4C4fZ8zJWhUkI0_EqYp1W8fXBQmllNuwir3G3MYoFP2F50xRgFTdtV5RtL16VfgfwGVfyoKlgMoycbJMSMQwNKTa92li7kMzWPlOZ8O60-Xirp_dLvD8wRHaoxeyh_Jfh0NMcE3Sj69xpIOMdhEadOWF6AheB9ymDnDoKiAMDf8Dfd_3Wipt9eQDxCJ5PIZ2h7Tl0G4xm4zYUQAH0b5FzoWOBFbTUo-buQshHJ0M2KMLK05mumk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuwKgFJKvJ_7cYc38oZF8E0_FsAG69TKvYkrgbUVZdM5rC3mk2DiA9_enYG1Ngqx7O6YHLDuvkZBc3D6wbyOPbDg739LkWXOGzpIs4C4fZ8zJWhUkI0_EqYp1W8fXBQmllNuwir3G3MYoFP2F50xRgFTdtV5RtL16VfgfwGVfyoKlgMoycbJMSMQwNKTa92li7kMzWPlOZ8O60-Xirp_dLvD8wRHaoxeyh_Jfh0NMcE3Sj69xpIOMdhEadOWF6AheB9ymDnDoKiAMDf8Dfd_3Wipt9eQDxCJ5PIZ2h7Tl0G4xm4zYUQAH0b5FzoWOBFbTUo-buQshHJ0M2KMLK05mumk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=flTLx7SM5bSxh4CI-KHyi59tlusYL5n_dS-aTKNpsW02H5eF_xsQjAZ9D2SqKP9SKRIRXHpAVoz06f0EsTch7VG3lyJoVc4fku823d3Ig1_e60RKwPgW3p_tym6E38U3X_Kwo_dJKwcsg91m1EQgrIHJzOONi1XEHxRA3vD3eTWTkkZ7_p7AaJ9pj8hG3J-bsn5ZfQ65og5NW6yYAM1Sjv_xxUy7tEy2koSZuNrMfI_ALLEzcjM0GU-a75YB1YGXaozQGU7ztXI6-hzQEQUT7hW09ZOQ2zgOpQt0IlR1d6H23akTvDV_7ArC7v1iY9F_vV7-1McsBpy3-a_VjuPMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=flTLx7SM5bSxh4CI-KHyi59tlusYL5n_dS-aTKNpsW02H5eF_xsQjAZ9D2SqKP9SKRIRXHpAVoz06f0EsTch7VG3lyJoVc4fku823d3Ig1_e60RKwPgW3p_tym6E38U3X_Kwo_dJKwcsg91m1EQgrIHJzOONi1XEHxRA3vD3eTWTkkZ7_p7AaJ9pj8hG3J-bsn5ZfQ65og5NW6yYAM1Sjv_xxUy7tEy2koSZuNrMfI_ALLEzcjM0GU-a75YB1YGXaozQGU7ztXI6-hzQEQUT7hW09ZOQ2zgOpQt0IlR1d6H23akTvDV_7ArC7v1iY9F_vV7-1McsBpy3-a_VjuPMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=oG9LdPHK4ss7cFBceYIV5DdsWQjyRNGJmEDITxed4sCsOBnKq69p294b7TO9YuT8lN7riJy60_fsb1hU2UnJgIb0gZVYa5xC0vnbAxL7VcPnlfniQ4W1etJxovOyBz1YV990i7zPwqnuCHrmxdtf0AM-gO_2TUM8bPJNCvlzQmHaP-ozAL9DAxxfMTH9cnnJVGUairYbOfy_w2RCmSAXmOeZJIlTuCIvqu97VpY_GjV84iavKIoB2ZVVsWr9x0LtgEWWDtNlrdVGcBznD891dZKJf5ZL79BFC2nc3Zor8gljsZ5Y4Sjj786Z9bd_HvU-OR8tOODfO4b7tzAMEtIwWDgxX2tYC4nIFdCmMutDGrqdJuspVdz8tcFIzXyyWhpsRBThp9NKbQrfn0_LkSTrqBghm0x5bKxFoEQOAmBcQbJHYciwSIibB7lAS1yD5VKtSLUtx7dAsjV_QvzhKeCUCRUjpJOKF5rdROVxMvBpa8q71XXXisNQ4kq0jIKNmosorqtDg4gUMeE5M4Xr760Y-dLGNfftBop09qxogwVdnQo30GNKNSq35S9dqD--JPSJcjVEnXmOyU98nxuWaJb5AAhUHoJkJ4cYPtIEx7nTZNLEmME6LeOr9HihgmxfaFEcr3TJNxT1OMwdBB06TpryTSVATZwjUuhsFqB8-GxBR2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=oG9LdPHK4ss7cFBceYIV5DdsWQjyRNGJmEDITxed4sCsOBnKq69p294b7TO9YuT8lN7riJy60_fsb1hU2UnJgIb0gZVYa5xC0vnbAxL7VcPnlfniQ4W1etJxovOyBz1YV990i7zPwqnuCHrmxdtf0AM-gO_2TUM8bPJNCvlzQmHaP-ozAL9DAxxfMTH9cnnJVGUairYbOfy_w2RCmSAXmOeZJIlTuCIvqu97VpY_GjV84iavKIoB2ZVVsWr9x0LtgEWWDtNlrdVGcBznD891dZKJf5ZL79BFC2nc3Zor8gljsZ5Y4Sjj786Z9bd_HvU-OR8tOODfO4b7tzAMEtIwWDgxX2tYC4nIFdCmMutDGrqdJuspVdz8tcFIzXyyWhpsRBThp9NKbQrfn0_LkSTrqBghm0x5bKxFoEQOAmBcQbJHYciwSIibB7lAS1yD5VKtSLUtx7dAsjV_QvzhKeCUCRUjpJOKF5rdROVxMvBpa8q71XXXisNQ4kq0jIKNmosorqtDg4gUMeE5M4Xr760Y-dLGNfftBop09qxogwVdnQo30GNKNSq35S9dqD--JPSJcjVEnXmOyU98nxuWaJb5AAhUHoJkJ4cYPtIEx7nTZNLEmME6LeOr9HihgmxfaFEcr3TJNxT1OMwdBB06TpryTSVATZwjUuhsFqB8-GxBR2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ecnKc3PN9lqyWIZTJG6ti3VC05RwgW7FhbR4Lljhi3IQ4gQxQ5V_jLFUPqmeieoqF1xfuvTten-ekx6BHFSGrlFXGr1v9KRYXm9mUMB4zb39X7wrJYmjE8WUwu4U1_ETCmGX-WCI67dZoHJ4W5oxBGxDwchHt-4r3doimHU_DW1AnQ5Vd8tOotdN7BuMSxKG1teZ2sixaB-0eirb1qcOEDXJp_REcQeA8TtRGO-kRvtERRJjujvWxk6iVTLjuPjbIsRcRNnfEDcW_hkincVThDHGwe1ZU0ZkEdzs-GAfFIFnY7cLCiSdr8X9lyaSH0Xkw8NsLBJoJalrruNPX30kwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ecnKc3PN9lqyWIZTJG6ti3VC05RwgW7FhbR4Lljhi3IQ4gQxQ5V_jLFUPqmeieoqF1xfuvTten-ekx6BHFSGrlFXGr1v9KRYXm9mUMB4zb39X7wrJYmjE8WUwu4U1_ETCmGX-WCI67dZoHJ4W5oxBGxDwchHt-4r3doimHU_DW1AnQ5Vd8tOotdN7BuMSxKG1teZ2sixaB-0eirb1qcOEDXJp_REcQeA8TtRGO-kRvtERRJjujvWxk6iVTLjuPjbIsRcRNnfEDcW_hkincVThDHGwe1ZU0ZkEdzs-GAfFIFnY7cLCiSdr8X9lyaSH0Xkw8NsLBJoJalrruNPX30kwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKj6xLmzuvGs6fL6yJXoeDdQWMvg6GqTHXiUu9nOZ-GVErULQs3lsI7cKKItmugKX_uVioYNloPizKef5Rs3idjBctWvl21_afBlT4TjqUkGtUMuhmfnibKKQXU5awvxqrJCczQfRPent497uPMT1owrrD0YU4SazMR8sRiYHs80VBWq8JQDHtuSAszUsmgq60PoRk4mPdkwFvQy6ZLPOo023shkhUHH3qGi6_8p3bgjf3sXM5UXF3cXI6OgmEsTOSTPg1OanJbEbreJb39uydIb0xuTsWpBvlAqi09ZyxC6Kb_PJvIauQtG-nbHDMGK42S_XV1dhirWfpFD1e67bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ficB8__Z23_YapYO0w386AUV9VMATfxsw-rImDC_jq7gXOBjkc27LtThtOLHFbp7rlnH6_n3ZrjH1ME7fsGNtM71AbnKzNyjVDbpK-0VioWhhmBQgWUMnU3bPWCPk-ywRwIVEGwqSJ71fvOEEV2q8u2A99YQoGEAontMB0kfeCLep2vEZbpenFr8P1ZsOOu3dQeq3GftDsmmTA5FE8LNvUCr5VsMjtRaZ18YOmMNqxRabdzSTsFpNsvpG-wnHKMEA9Ta6BMxQie1IwcodgHkmH_cUvDqkAHjzZMycL0tC6hK2eIYuIse4dKMVcwKkRDLjBkcMEzpizfn1oHUbAqLqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ficB8__Z23_YapYO0w386AUV9VMATfxsw-rImDC_jq7gXOBjkc27LtThtOLHFbp7rlnH6_n3ZrjH1ME7fsGNtM71AbnKzNyjVDbpK-0VioWhhmBQgWUMnU3bPWCPk-ywRwIVEGwqSJ71fvOEEV2q8u2A99YQoGEAontMB0kfeCLep2vEZbpenFr8P1ZsOOu3dQeq3GftDsmmTA5FE8LNvUCr5VsMjtRaZ18YOmMNqxRabdzSTsFpNsvpG-wnHKMEA9Ta6BMxQie1IwcodgHkmH_cUvDqkAHjzZMycL0tC6hK2eIYuIse4dKMVcwKkRDLjBkcMEzpizfn1oHUbAqLqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=G0yC3hYCP1sHEtfsUYEg7a8eJhDmTNDzfwGbfLn6RvIe5TAxFos0-xLiA7ELmLERwFNwUZUJqR48stgqhTvLcyPrIKIbWVFQvuSVEGWw6mqcXZfkkjUajM9vGp0GSppRhYr0H_8WNYKZvWkZbgVHx4EjUbm3FF_oEsFqp_NDXFAPcjGq4artHK3TfMJZHEoyfANZ5fkaweuHfBT9G5pMiNHhXpSw7FJ50wlF7b-wiuLd7q0uRSblZpvg-7I7sj_U7sJa2DV3sMLesqZ6FqZWpIvfXotJIvxgA0iRdIFYNdGDpQC-mWxCs3Ye2hoQcyqzOg1MSCRxJZ_uclxGfSWUeRFQj1tRoqwPu-yU69KVI6gfu2E000zjJNph9vT7-oYrUmb0MyQgPR4R89FGa078mETrkOrhbmDxwKSQ6HP-juz5Jgzev01maw-eyTAHSNrvkwCPIx-k_7Wqevjf35P7EZSnt9jB5GZjs-Ghg3ZuBV5-Yh5c8ZSev4auR_Kb3NEqqLvNVKBlFG_XBZXRAG33RL5p_8gopka0GzgTotMEdON4VjFczmMuyHhZAGYWJVlObPjJsJvbRtyD9Sc-0lYZzdlJdAt-2txht0MhbCITqFyHD9EW9edVijb7GOR_85ekLSD8mF8JpdzK6a0EiQ1lled08mYoM80mNsCbfs4rzp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=G0yC3hYCP1sHEtfsUYEg7a8eJhDmTNDzfwGbfLn6RvIe5TAxFos0-xLiA7ELmLERwFNwUZUJqR48stgqhTvLcyPrIKIbWVFQvuSVEGWw6mqcXZfkkjUajM9vGp0GSppRhYr0H_8WNYKZvWkZbgVHx4EjUbm3FF_oEsFqp_NDXFAPcjGq4artHK3TfMJZHEoyfANZ5fkaweuHfBT9G5pMiNHhXpSw7FJ50wlF7b-wiuLd7q0uRSblZpvg-7I7sj_U7sJa2DV3sMLesqZ6FqZWpIvfXotJIvxgA0iRdIFYNdGDpQC-mWxCs3Ye2hoQcyqzOg1MSCRxJZ_uclxGfSWUeRFQj1tRoqwPu-yU69KVI6gfu2E000zjJNph9vT7-oYrUmb0MyQgPR4R89FGa078mETrkOrhbmDxwKSQ6HP-juz5Jgzev01maw-eyTAHSNrvkwCPIx-k_7Wqevjf35P7EZSnt9jB5GZjs-Ghg3ZuBV5-Yh5c8ZSev4auR_Kb3NEqqLvNVKBlFG_XBZXRAG33RL5p_8gopka0GzgTotMEdON4VjFczmMuyHhZAGYWJVlObPjJsJvbRtyD9Sc-0lYZzdlJdAt-2txht0MhbCITqFyHD9EW9edVijb7GOR_85ekLSD8mF8JpdzK6a0EiQ1lled08mYoM80mNsCbfs4rzp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHE5FGToFR1Tk4xgVHQt8n4gtLORYVX7LFlWHIio4t1lw1TWRQIRW89cpoyByFHgEW3IBN3ez5ncgmyNcKUmtPfbLuQOd9-ioaKX0fpE_krSLhgvIK1jBJV-G0gaO45jDqw0DMlxS3BloMpAKYM0Xyon2qZzavXRNad6rWAsIR0i7CgO8bX6V4U-wkmS_JoS7NqaVBtTkY9BKr7TJSx4JVPGCWdvxWxmX3fuiNm_lD9DFBbNKDnZ3NR5D_3BA8t1v2TtrqjF_tzQfT7FIvn2LHkqwLYyTNfu-d0NAIOzwzo3Syp_zGaeWSOIRCHM3osEmvfORfARdnJUitPkYnXrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XT4U3qick-E5KvuPe8Ir9vJzWVtCXV-eWyuVoyHEVZktsl6QJbwj6DShNuOqg2sVJQE_8nvlcJ0Y59QFBM13LachTlmtTyv-6x3xEadHTBwiZn5cxcTNNAlmO6wVX4yGmtVkUvVWOustfRHPBXR79ExEHqtIwBPVsQfPgmukfnwGapSKaLgUQ6FlNyW8BQ2MmnobMs8gk05hpwj73mrRJafVH0ghqDqxLNQuzu891fIfMOr8qgpIVZibNoaTDU9qqh7YHnlSCZPXXyS6yARMkjx2x71uoqboDFgOMnPCyVMCEq_xKR97eVzb740DKE5Y-9JVPOh18mjeiG57Q0o4RraWoD2Y-J_a2kI_y4AGKy14H2e6-2OYatjeYLOfJA2Tciv6V3Gg1_hR0QrS9Zg0AV0LgntXU_FV1RVtBbs14DmDSKLZoWihPRtdnsmMA1LXGDCtC_wtDO93OMIsiTMk3af7LhOQ1Oyj52PIjKW_f30IUDUl85dVxMrSQfbkvRoowS14x5peuXxtNVfQcabTG4oIz-hcSyFmt8woWk0m9zjeTkDi64sbbth3-ganmMYu97oGzYU5M4yqjzFryt96HcutAStyoRtpf_aMyFPszkxcZRXO2HmPQn1EPW_KdEac_ag6HE-juWORngtyc8QgV_wPXwrKKyGRaxaL157KqlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XT4U3qick-E5KvuPe8Ir9vJzWVtCXV-eWyuVoyHEVZktsl6QJbwj6DShNuOqg2sVJQE_8nvlcJ0Y59QFBM13LachTlmtTyv-6x3xEadHTBwiZn5cxcTNNAlmO6wVX4yGmtVkUvVWOustfRHPBXR79ExEHqtIwBPVsQfPgmukfnwGapSKaLgUQ6FlNyW8BQ2MmnobMs8gk05hpwj73mrRJafVH0ghqDqxLNQuzu891fIfMOr8qgpIVZibNoaTDU9qqh7YHnlSCZPXXyS6yARMkjx2x71uoqboDFgOMnPCyVMCEq_xKR97eVzb740DKE5Y-9JVPOh18mjeiG57Q0o4RraWoD2Y-J_a2kI_y4AGKy14H2e6-2OYatjeYLOfJA2Tciv6V3Gg1_hR0QrS9Zg0AV0LgntXU_FV1RVtBbs14DmDSKLZoWihPRtdnsmMA1LXGDCtC_wtDO93OMIsiTMk3af7LhOQ1Oyj52PIjKW_f30IUDUl85dVxMrSQfbkvRoowS14x5peuXxtNVfQcabTG4oIz-hcSyFmt8woWk0m9zjeTkDi64sbbth3-ganmMYu97oGzYU5M4yqjzFryt96HcutAStyoRtpf_aMyFPszkxcZRXO2HmPQn1EPW_KdEac_ag6HE-juWORngtyc8QgV_wPXwrKKyGRaxaL157KqlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=itvobN0Lit_UxLQMmJKqAgFAd3BxsAHUivZKSuGVnRUHYHBXD76TYgK_jXs4RhSuVMSeZxK0dshfQlbCowGo4yANy8cdYr5nY55H08_KCqGSsNsVyzE-IN-3Gjd5OTa5GYzMmFsmKKutpa0_Pzqr-ME_XHV6gtIA4bbINBsWMlRre2c8diDu8nNKDmbLxId8rP_6DA9d8crMP1If5GJtT9fRBEG4DbFIK4tDjqq5gKGgKiQGQFbEXMqWrZYiQq6NItAIlua0vIdZwB3k1sz1CCpJoX3t0ZZ3g9J0oF5j_JuWc60STcGFaLNQoh3Td-MKYIBrqhXjSeDRoZ5uKjjveIKLzam4sD9GIfCkgxrih0EfiW5S-clfxV7uze0FCv5PtApfHnLQO2yTapyI3SRNH36emXuKNvXfeRwo4jBcHT5HXFVKoy5cdH8AttFMzsWfOlHKPoEeLPzW3r-nkGSgqLhXNqGcV65e0Af7aluXhIGPvAS3DsmASI_ks1Ps5HNF3JK92jbz4dbvyHuQUR5uxyB-i2udVSEgKBwfqv9YMOu6gJ0ISi32BRfIzYto7MkvRzsXirIq1lOzA65cNXnyf0zkpSljh4DfOX3ItyEZmPhx5cnbBdXEN8HfNPwKepRP1UJqcGvjFUUTIk06uCcCWImqCgCzmjDmTW6KqZUxytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=itvobN0Lit_UxLQMmJKqAgFAd3BxsAHUivZKSuGVnRUHYHBXD76TYgK_jXs4RhSuVMSeZxK0dshfQlbCowGo4yANy8cdYr5nY55H08_KCqGSsNsVyzE-IN-3Gjd5OTa5GYzMmFsmKKutpa0_Pzqr-ME_XHV6gtIA4bbINBsWMlRre2c8diDu8nNKDmbLxId8rP_6DA9d8crMP1If5GJtT9fRBEG4DbFIK4tDjqq5gKGgKiQGQFbEXMqWrZYiQq6NItAIlua0vIdZwB3k1sz1CCpJoX3t0ZZ3g9J0oF5j_JuWc60STcGFaLNQoh3Td-MKYIBrqhXjSeDRoZ5uKjjveIKLzam4sD9GIfCkgxrih0EfiW5S-clfxV7uze0FCv5PtApfHnLQO2yTapyI3SRNH36emXuKNvXfeRwo4jBcHT5HXFVKoy5cdH8AttFMzsWfOlHKPoEeLPzW3r-nkGSgqLhXNqGcV65e0Af7aluXhIGPvAS3DsmASI_ks1Ps5HNF3JK92jbz4dbvyHuQUR5uxyB-i2udVSEgKBwfqv9YMOu6gJ0ISi32BRfIzYto7MkvRzsXirIq1lOzA65cNXnyf0zkpSljh4DfOX3ItyEZmPhx5cnbBdXEN8HfNPwKepRP1UJqcGvjFUUTIk06uCcCWImqCgCzmjDmTW6KqZUxytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=MCyt6Ul_VI5vltf_i1USx7uXOS4fatNnjnM6IBWWNjOc42aff6y8J8awEg7qCL1zJk9_b6aF3ho8xisPcXfWRlpz2xnj-fiq2vUGVwQJeX3x1FQ3Jww6mU2UPCz6Tv-dnpvMbrgwwLYdpyChHL9EyN5is_XOLa9mjKuLimDRVKRsc01zce7SVSH-c6pQEgzrpDPmZAF70gSRjahgSzGOQpdx9-3oi2e3f6vLh6bDXqfpsXQeyAr0aXW7weGCewxdW-o_4b3XPcPCfvcIsmKVWZfTpbXV08258jjo1cCTNja2MRU7Xt4nMvlcMqr6lm1OyjmPbDjxnGdhBIl2aCBOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=MCyt6Ul_VI5vltf_i1USx7uXOS4fatNnjnM6IBWWNjOc42aff6y8J8awEg7qCL1zJk9_b6aF3ho8xisPcXfWRlpz2xnj-fiq2vUGVwQJeX3x1FQ3Jww6mU2UPCz6Tv-dnpvMbrgwwLYdpyChHL9EyN5is_XOLa9mjKuLimDRVKRsc01zce7SVSH-c6pQEgzrpDPmZAF70gSRjahgSzGOQpdx9-3oi2e3f6vLh6bDXqfpsXQeyAr0aXW7weGCewxdW-o_4b3XPcPCfvcIsmKVWZfTpbXV08258jjo1cCTNja2MRU7Xt4nMvlcMqr6lm1OyjmPbDjxnGdhBIl2aCBOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=iSxm-Rs7jOwewPK-iT2ZGzLCcy4s5fviwUCu87VddOr10lIFX3A7pX3O7asjVNssmKjKOrZmrdk326RFG_WCw-qAUwiqtOLJroxw1TYgObHRj1wBAG2ninQVdwnxySq_zmVekgcUSPVnLDIMGW62sGoMzb6lkZIw7Y6ZYylxOCxrUozSAI68BC3ZYS4unm4btZopqOiZPxz_w28eqA1Hws6baV00rZAzSaZSxa-w7mHIXl2FxW_6u_uoc7FmPJOwNCW3KeaA9P-0b_c6I7LKj31sCY3YD9fImQNwDR-AME_bcTFDRKsWGpRcO2L6Q1inFc-BP9qPgRlVQWHiYpw6kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=iSxm-Rs7jOwewPK-iT2ZGzLCcy4s5fviwUCu87VddOr10lIFX3A7pX3O7asjVNssmKjKOrZmrdk326RFG_WCw-qAUwiqtOLJroxw1TYgObHRj1wBAG2ninQVdwnxySq_zmVekgcUSPVnLDIMGW62sGoMzb6lkZIw7Y6ZYylxOCxrUozSAI68BC3ZYS4unm4btZopqOiZPxz_w28eqA1Hws6baV00rZAzSaZSxa-w7mHIXl2FxW_6u_uoc7FmPJOwNCW3KeaA9P-0b_c6I7LKj31sCY3YD9fImQNwDR-AME_bcTFDRKsWGpRcO2L6Q1inFc-BP9qPgRlVQWHiYpw6kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=sEJgiKw0Tjetav4ImJwiazP9KJsmRoT2eTErZ82xNUCycYA0QeYDGrm0k3jE1uvcShpQj41uhzhCrkx7ksEND0CvrWuI6Z3hElyB51vQYurAvz7x-Exehgiu_UoID7ryQ7AzyAFzOviMctzdK6yTi_0lk9Jjjz6eAt8uvpoY4J-sasYy7mYkFq2y5UupRUoFBaDiTITzqye3rS7-MQPVsdNaujDrEW5heVaqY24FfUvXHzBxlJrQPTwinuIeZfWF1iG6C7JZalV1Dtt5Fyeop29xqj9HMGA4OvAlDZkPbleaYGy_S3OvQ4RuhpNK-FcZY3q162h31C5rha1yv9xGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=sEJgiKw0Tjetav4ImJwiazP9KJsmRoT2eTErZ82xNUCycYA0QeYDGrm0k3jE1uvcShpQj41uhzhCrkx7ksEND0CvrWuI6Z3hElyB51vQYurAvz7x-Exehgiu_UoID7ryQ7AzyAFzOviMctzdK6yTi_0lk9Jjjz6eAt8uvpoY4J-sasYy7mYkFq2y5UupRUoFBaDiTITzqye3rS7-MQPVsdNaujDrEW5heVaqY24FfUvXHzBxlJrQPTwinuIeZfWF1iG6C7JZalV1Dtt5Fyeop29xqj9HMGA4OvAlDZkPbleaYGy_S3OvQ4RuhpNK-FcZY3q162h31C5rha1yv9xGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=nCJc_5gqUGwJ7-nqk_ijYx-DYASMLy0ukeMKrXI1loNnAElodbV_oBFyXLet3ZYJG-Tbrs8BPf0MXJfeBSra_HgOTZBXSTXycEIrtufM7jDexnidhwTrON2XzJw3nbd7GV2lIxRL1fx8SvfSQ8ovmH8nZFdaNAe7erCtROyyqZjDmavJSKaYcVMU7HLJelIr_F2G0YoPT30LTwK9hfg2fqzQSPW3fGWx22kakKXGhIy7_MTdwFl-ia6s7QsbrVY1QJEYAPjg6tNztkO48nMzAGtkDbeV1MqFJk1c5yIE_rVP3wdeXKgaXsN8vAtpSr6sQ-vc9MaeqCSziTHIoko8-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=nCJc_5gqUGwJ7-nqk_ijYx-DYASMLy0ukeMKrXI1loNnAElodbV_oBFyXLet3ZYJG-Tbrs8BPf0MXJfeBSra_HgOTZBXSTXycEIrtufM7jDexnidhwTrON2XzJw3nbd7GV2lIxRL1fx8SvfSQ8ovmH8nZFdaNAe7erCtROyyqZjDmavJSKaYcVMU7HLJelIr_F2G0YoPT30LTwK9hfg2fqzQSPW3fGWx22kakKXGhIy7_MTdwFl-ia6s7QsbrVY1QJEYAPjg6tNztkO48nMzAGtkDbeV1MqFJk1c5yIE_rVP3wdeXKgaXsN8vAtpSr6sQ-vc9MaeqCSziTHIoko8-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=RdrxV3gBZNkdf1abZbJEGeR9qFV9G291WHnf-FoF8rBuPduPwOIz9nnAKK9EAoWL_kMHp0ioTsBB60Aazlxn8vcAjJHCoKYuMBo_2XA5sc8guaIOGmdsxpGWRN9hOJN7bsUTVRaCq3jcOYBRljwM5yIA5sxx6WNCX4S9JeDiSwsML58HX_tceM24xAqk2g1mLI-sv_dNuj9_tDb94sxWLzNNwN54XOGyEkBBZyzt5ks4rDle4vbJTR9klaKboOZMlL0i6xwfKRaVwmXb8px-b-ANv_mBfcAybh1OCFhr_-MLH6Q4-OPURhBFRf0Ca4GNJYuegBno8AbrD5k2SPJuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=RdrxV3gBZNkdf1abZbJEGeR9qFV9G291WHnf-FoF8rBuPduPwOIz9nnAKK9EAoWL_kMHp0ioTsBB60Aazlxn8vcAjJHCoKYuMBo_2XA5sc8guaIOGmdsxpGWRN9hOJN7bsUTVRaCq3jcOYBRljwM5yIA5sxx6WNCX4S9JeDiSwsML58HX_tceM24xAqk2g1mLI-sv_dNuj9_tDb94sxWLzNNwN54XOGyEkBBZyzt5ks4rDle4vbJTR9klaKboOZMlL0i6xwfKRaVwmXb8px-b-ANv_mBfcAybh1OCFhr_-MLH6Q4-OPURhBFRf0Ca4GNJYuegBno8AbrD5k2SPJuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=vwkU9VkkdgwqnYUJ9xeWOn0G5qIyg-1JKhojvAF3esCVIS_iIZrV1Nip3ENzwQnjAuNrBzidYEr1W8tCJ795MwWbacl8LUGJZE5jzWm9LsqWsBmVsymiVaKfjkZJUDdMHx8NTtNvh1O8AwuY6skN1NQEI989eTDjboTrlCGtkKQr-AbcMotYbH83MsBn_WMQcj3hh4TxGjaF6DsOiLsTVjbgRvSBiKX7PkeGEdm0WV_kPEhfNNgcxg1zZeUUcCflDHjxLboVJzNyFbMiyC1i8iRPrPn7QMxhinVsI2hsVn4nrBfT9WFc2NsiiClMpGfc16cArcgPXymURKrFblw8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=vwkU9VkkdgwqnYUJ9xeWOn0G5qIyg-1JKhojvAF3esCVIS_iIZrV1Nip3ENzwQnjAuNrBzidYEr1W8tCJ795MwWbacl8LUGJZE5jzWm9LsqWsBmVsymiVaKfjkZJUDdMHx8NTtNvh1O8AwuY6skN1NQEI989eTDjboTrlCGtkKQr-AbcMotYbH83MsBn_WMQcj3hh4TxGjaF6DsOiLsTVjbgRvSBiKX7PkeGEdm0WV_kPEhfNNgcxg1zZeUUcCflDHjxLboVJzNyFbMiyC1i8iRPrPn7QMxhinVsI2hsVn4nrBfT9WFc2NsiiClMpGfc16cArcgPXymURKrFblw8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=plvqrTNJ8b0yjgeRXTXTXjS19ZGaSjvlvJQD1Gt-okkiEe0oT6AMWJg9ZkZgcagu_-okYvQPS8i7x6lvInJEaJxRCeFF3xUgDxkkEiFKJYBTTe835X3H-3zWkJLOBMnALi5jnN4qdOsCabU5gcZ0dmBsCJWi4BxtpMKKZ_UI0w3CiqFzImRci_AMRWEYJ8qW1gswbqNYPsZ3NvE2OTuKswkGggzALMYCOYWOJHGxe7eNPEMN1Z--uwDLF-F54_lMT_zb5FqTeMGH4xFjXoD-L1goZVbgGbaO6UmfZF4eTIQ69xTGMnZtX4PRX3PmQXTvnhji3sEMh0rjA16jOyMNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=plvqrTNJ8b0yjgeRXTXTXjS19ZGaSjvlvJQD1Gt-okkiEe0oT6AMWJg9ZkZgcagu_-okYvQPS8i7x6lvInJEaJxRCeFF3xUgDxkkEiFKJYBTTe835X3H-3zWkJLOBMnALi5jnN4qdOsCabU5gcZ0dmBsCJWi4BxtpMKKZ_UI0w3CiqFzImRci_AMRWEYJ8qW1gswbqNYPsZ3NvE2OTuKswkGggzALMYCOYWOJHGxe7eNPEMN1Z--uwDLF-F54_lMT_zb5FqTeMGH4xFjXoD-L1goZVbgGbaO6UmfZF4eTIQ69xTGMnZtX4PRX3PmQXTvnhji3sEMh0rjA16jOyMNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biIpLHUR7JHYVEvZau4loHE-eR_dOjKRd0Sx9LY4YRP_IWywCO3dEspm5Y-aUNFr31TuMgL0hc3qqerDus-SIllsIYQY3CejAVGL_ettGBGHy8MKS7eH2X1ONvA3HY_yt7yNit-zN96_yK3fiMyVLsLkuF1hISE1gInRKaRXQ0i7PBKaAlePl76j7xOo5ynHs59J9OyvYafDjHxTAhNs4hrrW2Jv4MdAY7_KwnYuncZQcBhitdACR8q-Frg9tYlHXwREuPr5t6d9nTaKzCM-h3Sss_OlBuesT_xrBs7t5mRl5w-NB3lgPC_Yyzsk9h1DZbPwx3VMCrkl7nO9cp05vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=vy0_BYava08EvL73OgiAGjS8lmPexENjhNxbAQ5YhPb5qD9Vdo1g1aA6Id7qc4X3KpY62sSKhYkWG5OpGkqc-4ZS56BB2jxYlTxpjJ8IaFBVsFXTMuWapYJlq10zJXvtzHlBbNmKbr5lP6V9HxysoExLr7AvnoMkqT8EGqRqlIW7OLU9_JlJ-gBvTcCKDV79_TZpZgQ9_cs5oaxRuK_Z7WtV64qsSUNMB3INjwXncuw_UPR5u3tNHv5SYGX5C1jB8Gmt8pEAXKhXsYzgKeu8NjqMCzYrz9DBKUcEKniIZBXQZOsRxiz2MS0kZvU3_6JJq2Zti-DKeJsxU_jZkTV10Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=vy0_BYava08EvL73OgiAGjS8lmPexENjhNxbAQ5YhPb5qD9Vdo1g1aA6Id7qc4X3KpY62sSKhYkWG5OpGkqc-4ZS56BB2jxYlTxpjJ8IaFBVsFXTMuWapYJlq10zJXvtzHlBbNmKbr5lP6V9HxysoExLr7AvnoMkqT8EGqRqlIW7OLU9_JlJ-gBvTcCKDV79_TZpZgQ9_cs5oaxRuK_Z7WtV64qsSUNMB3INjwXncuw_UPR5u3tNHv5SYGX5C1jB8Gmt8pEAXKhXsYzgKeu8NjqMCzYrz9DBKUcEKniIZBXQZOsRxiz2MS0kZvU3_6JJq2Zti-DKeJsxU_jZkTV10Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=TZe9P5AU3-bvCRmGm2xJeQALH4LlmrRp5zDsCiOP04tyc_kk30pAaKEgIu1fc9HDdWQCWaH1VDW8yfHAGxHLWo5uFTQg0XLUQFs21jfgg2xRT2fE02hw7gzjLT3QR2-3zIwVToAgFRaQRN-UYZYI2yeiB1Cbx9x_3YYkJeMBCfa7qSxwtDt8mowWkUdl4-dHbDc8KKuX5vHib4g9AXrKMNNaZfvbf3WHgt3yQ-1hwM7sajSW7LV-deQjzZ1MV3embU5X-dlIqv0t7Nny0uvr-Y0nXmy-dPZ2DIfVizqDQuXYRWXKcQi3F0kzABQ9inD8whYiLNSVtYHea9dlK2jjPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=TZe9P5AU3-bvCRmGm2xJeQALH4LlmrRp5zDsCiOP04tyc_kk30pAaKEgIu1fc9HDdWQCWaH1VDW8yfHAGxHLWo5uFTQg0XLUQFs21jfgg2xRT2fE02hw7gzjLT3QR2-3zIwVToAgFRaQRN-UYZYI2yeiB1Cbx9x_3YYkJeMBCfa7qSxwtDt8mowWkUdl4-dHbDc8KKuX5vHib4g9AXrKMNNaZfvbf3WHgt3yQ-1hwM7sajSW7LV-deQjzZ1MV3embU5X-dlIqv0t7Nny0uvr-Y0nXmy-dPZ2DIfVizqDQuXYRWXKcQi3F0kzABQ9inD8whYiLNSVtYHea9dlK2jjPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=tzu7M-lRnrPSgks4RPm99pxcDEPgRUIpmkXbCe0XI5Ug-FFCBMWo0f2yL1u_7FUKk-IYifLRTU4-Kf_9d67QHCWYjxnOAHwiAJi0_68pMzqsb4yRLxareO9k5Mxg8vHWzXpXWWIvYfQBChVs7LsWeNNDFx1sfuf1O_UAo7gHBjA9cBOpM6Afa8FDdOkV1pmj1rd7zUvG7yydG06BCpd3VES-kEi3FYotKnoVVeK2J1vm1uxO3DLaGovcAGFeDjJlzaaCHa2K_xFVGMmkja-hMtj4WM1bF6z-ddOe19dCemne67VnWhxMc4xWWfShEZPQGeIxYmlSC6IukIoA__GITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=tzu7M-lRnrPSgks4RPm99pxcDEPgRUIpmkXbCe0XI5Ug-FFCBMWo0f2yL1u_7FUKk-IYifLRTU4-Kf_9d67QHCWYjxnOAHwiAJi0_68pMzqsb4yRLxareO9k5Mxg8vHWzXpXWWIvYfQBChVs7LsWeNNDFx1sfuf1O_UAo7gHBjA9cBOpM6Afa8FDdOkV1pmj1rd7zUvG7yydG06BCpd3VES-kEi3FYotKnoVVeK2J1vm1uxO3DLaGovcAGFeDjJlzaaCHa2K_xFVGMmkja-hMtj4WM1bF6z-ddOe19dCemne67VnWhxMc4xWWfShEZPQGeIxYmlSC6IukIoA__GITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=AZ2ML-Ri70dxeXcpmcMrkd2z7aA92zsnfQS5pcq8XM7a4onZ8zVvfj12mmhCW4dqP6wLFdyYY0bLTd4_W98Al4zeLKST6P9TZUmr8J83qm3l53pfa4clK-rOO5DzUha2b_E8cZ0x_T1m4qgmg1DT0B2ICIdWf_lRoXpBZY47dyndR6V54w6TShgC-iZ8eo6zyUZH4ngnaIpki3UYpxaKXL4cVSw5VwBn9qxeoHEm6Np574ioswPSaj1jXM9L1ROC120d-FMUBYoz1PJmJjaDmbs7vQK75DImJ4ctVNeiuqHPyTaolmOEcTYXm5Yf-OyQBd7w6p1ZCg4nzDVfMEt7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=AZ2ML-Ri70dxeXcpmcMrkd2z7aA92zsnfQS5pcq8XM7a4onZ8zVvfj12mmhCW4dqP6wLFdyYY0bLTd4_W98Al4zeLKST6P9TZUmr8J83qm3l53pfa4clK-rOO5DzUha2b_E8cZ0x_T1m4qgmg1DT0B2ICIdWf_lRoXpBZY47dyndR6V54w6TShgC-iZ8eo6zyUZH4ngnaIpki3UYpxaKXL4cVSw5VwBn9qxeoHEm6Np574ioswPSaj1jXM9L1ROC120d-FMUBYoz1PJmJjaDmbs7vQK75DImJ4ctVNeiuqHPyTaolmOEcTYXm5Yf-OyQBd7w6p1ZCg4nzDVfMEt7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-3egx_pZY11UOLbNYCKnfm13gi6jTxd1Fimg03tsJUOwtc-LTcW_ZKCaazeryWRCO66gWKan7SAoGJO4oozxJJCcVbcZU-Haj-xlXQnNoxh2LIFBW32UZTdER6-IJNS5iw9JVWfQ1atxf6kmBw4Hqj62zRg14tl6BTnmQa3XL_tCcLxqrhJDZK_UCDhd6C4Y9jvATlzgmfMdkzTAsm-TgKxv20tz0O9X12MmbHdI1AjVJLx6SeBoX73a57KMOMwJx7_RLznaNavCN02QgJP30_ubwcWYp_29U46gGQXN4GL3-aG1qmDRfOw22iyRq0_F_vzHJ5gZpVwKoZSJfIC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ETaxZ-3Tk9a6gyYGpWfZ1MPL2x0EJTaGFhpekgSQT-VtVMBSOiDN4L66wkEvZ1BsSPryIMRmO0fqOqTbye_wgKRyBTO5i4YdE4cmWhDXCaVv3NuX4aErVSK-rpt4AZJmeD4fJhBkCX79R8w5oItBU-aeHQYJWPmfpbQDkfU-sShDGBvChxTS2E0AWQRxE74UpwplmaKdZyLf02eyVAfLYb-PZhvqVXXQXFAWY_uez2jkAALn3_BNmlmlZfVuyR7PbrYYVjykm0sy4MUd-HW38r3R-wEXDdm58ndhnZxuSklWfYZ3lAL2-t1Uj1RYY4Tkk-sw-sLpvu1PiQVZin2HkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ETaxZ-3Tk9a6gyYGpWfZ1MPL2x0EJTaGFhpekgSQT-VtVMBSOiDN4L66wkEvZ1BsSPryIMRmO0fqOqTbye_wgKRyBTO5i4YdE4cmWhDXCaVv3NuX4aErVSK-rpt4AZJmeD4fJhBkCX79R8w5oItBU-aeHQYJWPmfpbQDkfU-sShDGBvChxTS2E0AWQRxE74UpwplmaKdZyLf02eyVAfLYb-PZhvqVXXQXFAWY_uez2jkAALn3_BNmlmlZfVuyR7PbrYYVjykm0sy4MUd-HW38r3R-wEXDdm58ndhnZxuSklWfYZ3lAL2-t1Uj1RYY4Tkk-sw-sLpvu1PiQVZin2HkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=poSqTMl4Y3H6OJJYoeUSEEzIOAwKa-yRC4FuNlj04IHf_GZONDsHwu6X0CvjR9h9c1VoFEtp4enqRdMZzHbvTwzztoT6-EVUPeBdQNDpckP5lgE02DXSVNYSXYqucSAsGRYBUncTeThXT_Nv2iqp9oyz0DgMF_fUxBlQx1IMUNSIRJX_qui3K6dR7VtNvPSiv_vOJAjtAW1ClxspwrZCUvDzWivwDm7eiEkI27Bz41ixgd1A4zXlpqiqEhCsGSHl2YOvAWvjsYGbK8MQdOcwubnF-Dqj35Vk4ZBo_yvtSxKuMzM1fqGNSzJV7zteujuvLxpJYQvI9rMSnyQA8JtoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=poSqTMl4Y3H6OJJYoeUSEEzIOAwKa-yRC4FuNlj04IHf_GZONDsHwu6X0CvjR9h9c1VoFEtp4enqRdMZzHbvTwzztoT6-EVUPeBdQNDpckP5lgE02DXSVNYSXYqucSAsGRYBUncTeThXT_Nv2iqp9oyz0DgMF_fUxBlQx1IMUNSIRJX_qui3K6dR7VtNvPSiv_vOJAjtAW1ClxspwrZCUvDzWivwDm7eiEkI27Bz41ixgd1A4zXlpqiqEhCsGSHl2YOvAWvjsYGbK8MQdOcwubnF-Dqj35Vk4ZBo_yvtSxKuMzM1fqGNSzJV7zteujuvLxpJYQvI9rMSnyQA8JtoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bs1Umbrg2bgEtwTnNcLGAF5vaQbAJiwYPZUvOi6rBeopwCIhVvr-K3s1S8r2h_WpulETaoWTHxq10foKch6Mvrh-dWAik72qX4IqyHJxz0c-E7iy7HimBguSBPT8c7dn5fBTGsMUv8ZDSRsl9tAjUW6DDovqnd0IX1EFAxaoyNd5dI2s2FJqvyLpDnJnnrNBeka4XWz-SD4LHu0i3Gcu_sFTbQp1Kq2JWU9LB37vmGNrbtpTgP8u2pcUg7Gh5S28Y0m27UShOiLlN5KjqcaQx4I4bajmNRNo6NHC4ykL_Wsj3_Mj_dX2NJJzlCi1dcDD80h5s7jQ-0VnOpZ-yt_Dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVn97wGuw_f44N-RYEGSiKgDmiorN8We0VxIMcmeAwYuq87t3kZldSmVBP1WwHJcUvfhwDYrIB6hv3mImdQ5t28G9VOudzHnvGdehr_46FCpY6Kyqhbi4VaqPn5qHj65wKYLKqYbsLt1ahOYF3LjFuNp_a-klLK8wO_t-4csiGUe9PiuWiNm-CGGoYbbmC4c4gUvk1iK5ieGwqmVrd4YRbsPgEXTIv9o38YjJxGTZveMuG9zuVT-vre6axexaHObTSz7FPE3tm4XWXgWMJBdMm2IpHyQ63jCHorKYzJvrDP1LNI88clN-IyvzgIQa_VHQp3yhVNSjUBnCFUwtC6pgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=sxfr2r8zzsZIV17-RT43HCnYQz6O7Ab8m7harL9NkPh6vBt0BW1Yd3r-diWCn7eUG_To1gPS3uXrBocCy2Kx82-Cv0c1IrlDZiSuhmuGt_rLrqvZ8kgmKANHFxj_Z8xk3Yd5htoXFltzBPXjezfwD64T8u2EjZfFnAlWoMSRgv9njUP_uT_KzrSWMzgCbmWpoc24BRkYb73mx0LD1ShcCmkFkPmyXcildJYV1QNhkuRKIjjR9HuCq3aOXv0hgUSwNNAA8Y_blmjDNGzDCVLEZPGQafWtWrunsUycss_SLGejfH3flP4COzDvbd0lfAVabRWaJPYOxuzTI-6AcgHwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=sxfr2r8zzsZIV17-RT43HCnYQz6O7Ab8m7harL9NkPh6vBt0BW1Yd3r-diWCn7eUG_To1gPS3uXrBocCy2Kx82-Cv0c1IrlDZiSuhmuGt_rLrqvZ8kgmKANHFxj_Z8xk3Yd5htoXFltzBPXjezfwD64T8u2EjZfFnAlWoMSRgv9njUP_uT_KzrSWMzgCbmWpoc24BRkYb73mx0LD1ShcCmkFkPmyXcildJYV1QNhkuRKIjjR9HuCq3aOXv0hgUSwNNAA8Y_blmjDNGzDCVLEZPGQafWtWrunsUycss_SLGejfH3flP4COzDvbd0lfAVabRWaJPYOxuzTI-6AcgHwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnPQXqswdfTwCICE1booEOBrxJ30-A58bsFXQxY4QBK2SewnGpdqtob9wfiW_a6-XdCaddXdeTEZfOOju-Cfo0wkrjZYoi4YapfbKStWvmTo2mBxPkzvaYKBzXtlOm8mf3i8OT2x7AE7Za7GNFcEa7twkQzN5BRU9AflvyBKHoFILrSj24kFxd4_fu5UHI6r2-w685_a1J_Z_eua2rEFx27PV7QJLnAvuUEfM4ko2Y6uAW3yD39tQn4M-lZzDWINY-x1jfLzgrOsMScfPxkExbrnCivmLn4nfrxcDOJgjk2mLjuwXq3LCF6U_GCWNcCUKNepbu6EduPOXSfs5gbxCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOiQBm8m1bzlN5w3PCPIB-AebxXnRRMb5MV9R_74Ha8tqNkxdxyo-vQ7wwSO_uAvPk0juVxp9rRk-UoUeeGzYmFa8_uWgvwmR8b-hnAVUTlXDb7nkJvTYYfWDsVNic6iJ-NUahCAMy5k0jEvnvy26dxV4PZcjD6nyBsJfPSrLF0c8P-gTTPtLmeFFTwmswfk-390olPYN9p1i68g2rv5NW0HnNeubfX10YuroAE8KxGKxFo2B0pVEbWgBPYsSEBnE04N3Tbg3A1uhTA4nEfdlwyjI8ogwyByCdjNvmylIDdQxEylYcec9zwJzddaYmV6KazScM37VfAAJqoBo304mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNrbbQZA-3H9jX9duerCV3y3QuXJmMGTkwnhFtnpbpU4T9F0TX8S6EQQXRQ90QTgYFoclB_T0wDmpEWQMwi6NP51vvVyhDHsSiA8RIdYw1aNGkJiaLrBOjKJfXGHVGTdEgFf43v7RuRuYU5c8A6z-khd_hq6Y7-iQKDAcRtC7nIJRQlIPcswXgCBa0Cmk5byjvH5SV0U5zBJr5nIA_PyvzVF1m67Fzqst0L0EyncIVMPgdf9nS-bnAuaKtBemTIGswkqOs6RgJWbWWOMkGpWjV5JPM3FJRW4Oj-KblyvzKXmp0ZULEa13EjbqPQCKC9uCy-JYbmM_PkjvxhUwNcc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=oO77xlwPtXAYvDDYx9lwsXnvdtxKMlAE7tDnWF23NawHx5ivqyn6aVbeOTwAltUrd49eLc6p-Ja6QgYHRJiHAUSKPvqy-7tJ1fz-Kivr3gFx9BxedWPqdp0tnZne891XKB1D__K_qOkPYeDZvbdjCAswehP3-KkyxmHk91epr38R20bSPGJzgoaTJD3fv5OSl4u8BOPkqOVEbDSpozdqDlkKHUjHUKcimnnDx_fItIFSe_LKemz8T1vWGwS-7eT9R90OOJu-bGPVckkS6tMz5NQ4Z5g2wsQ9VfUyx59n4szn3hNFgiK6xUm2zFS6o1ySWjhsbQcmiwCZ11vIs9DSDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=oO77xlwPtXAYvDDYx9lwsXnvdtxKMlAE7tDnWF23NawHx5ivqyn6aVbeOTwAltUrd49eLc6p-Ja6QgYHRJiHAUSKPvqy-7tJ1fz-Kivr3gFx9BxedWPqdp0tnZne891XKB1D__K_qOkPYeDZvbdjCAswehP3-KkyxmHk91epr38R20bSPGJzgoaTJD3fv5OSl4u8BOPkqOVEbDSpozdqDlkKHUjHUKcimnnDx_fItIFSe_LKemz8T1vWGwS-7eT9R90OOJu-bGPVckkS6tMz5NQ4Z5g2wsQ9VfUyx59n4szn3hNFgiK6xUm2zFS6o1ySWjhsbQcmiwCZ11vIs9DSDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=YUzUWr0T5vukYwl5flXKc5TYWzyQZOJ8yyH-wEppMRmjkOJP8S-j9rDyBMmIPo1-aXs0E4ih8vxzQBjX84inRG7nZAM5qC3RlLM2IfBcsVZ50JBA-hqRbS-LFYO31Zt5BQenEvRapPsD-JYaEIISCF28IYR3Kl-BYT6vF3wMS0de5mqc7-FddSpLzFeF3QVeNRmjCjNbtRQOL5pRH2hSL8emFl8EYpvpPjZiu-u-URMkydi03WAPWAMZDBEovaMcy8lT5vNh5Or2sWEHGfiblx5YbnFGitLNW-JUinri15614rQys7W0Myu6CanRgW-IK1GcvT9IPMUOiFqdGMIYIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=YUzUWr0T5vukYwl5flXKc5TYWzyQZOJ8yyH-wEppMRmjkOJP8S-j9rDyBMmIPo1-aXs0E4ih8vxzQBjX84inRG7nZAM5qC3RlLM2IfBcsVZ50JBA-hqRbS-LFYO31Zt5BQenEvRapPsD-JYaEIISCF28IYR3Kl-BYT6vF3wMS0de5mqc7-FddSpLzFeF3QVeNRmjCjNbtRQOL5pRH2hSL8emFl8EYpvpPjZiu-u-URMkydi03WAPWAMZDBEovaMcy8lT5vNh5Or2sWEHGfiblx5YbnFGitLNW-JUinri15614rQys7W0Myu6CanRgW-IK1GcvT9IPMUOiFqdGMIYIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=XFrWoiFnz2MxQqiHZEIo1sTl6fxk3sH9hbsyBhtkzO08XtCuweJWCi5-l8-X3p6CVkxb0OuHURHEvDCeiHHDTfiianDGZQNz6EkO0fb97i1EcGtRLPIGB7s7HA689ycC1_FoJIs2EqyMNKLuRE8uLi8JhHyDO7BVJzkkfALbZ8GiPIbf5jxwsnaKP7Q4a_V19Nqfcnwy8iZoGCFY0KxEBj3wa1llEreaox7FbWMU7eojTwenysS7oDPAIxDCSvdCd7FOFSfAN3f1ZOzY0Bep23rR5W-sUs2dnF2jAhHBJkcmZpNgh-YSAmsqWKmrrvLQMkOz9QnVLkoxQKks3a0xlG6b_5n_RdDBxC9bI-LHMgX3QWlr2VhJ-UdDiOIRUfXlKLTrZmBBCRbUPag0k7RhkcIyUtvS9f3Ah9XncvIolxTGDWoOp-Bf6IqQ-nbGJkxBoGguprHTCfeQXWejc_NCq343RnXW1sipubUnR4JnNoXAH26CPpNwOwH-z8VcChqB21c0GWWtqwsPjryhfN7HE5oc23QA5vSKBbO0J6hC8uk3Qm0nks-_wmjYxN912G_aWGjSJD5-2KZYXPp9QsrXW9psFYRw-8p7quTNEd8WWPpKIhAshb1pxPr81Pr43Lrq5nKNegp2lJyZntn6NSAJjiEV_ZuHSsXtAYGcQKHvZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=XFrWoiFnz2MxQqiHZEIo1sTl6fxk3sH9hbsyBhtkzO08XtCuweJWCi5-l8-X3p6CVkxb0OuHURHEvDCeiHHDTfiianDGZQNz6EkO0fb97i1EcGtRLPIGB7s7HA689ycC1_FoJIs2EqyMNKLuRE8uLi8JhHyDO7BVJzkkfALbZ8GiPIbf5jxwsnaKP7Q4a_V19Nqfcnwy8iZoGCFY0KxEBj3wa1llEreaox7FbWMU7eojTwenysS7oDPAIxDCSvdCd7FOFSfAN3f1ZOzY0Bep23rR5W-sUs2dnF2jAhHBJkcmZpNgh-YSAmsqWKmrrvLQMkOz9QnVLkoxQKks3a0xlG6b_5n_RdDBxC9bI-LHMgX3QWlr2VhJ-UdDiOIRUfXlKLTrZmBBCRbUPag0k7RhkcIyUtvS9f3Ah9XncvIolxTGDWoOp-Bf6IqQ-nbGJkxBoGguprHTCfeQXWejc_NCq343RnXW1sipubUnR4JnNoXAH26CPpNwOwH-z8VcChqB21c0GWWtqwsPjryhfN7HE5oc23QA5vSKBbO0J6hC8uk3Qm0nks-_wmjYxN912G_aWGjSJD5-2KZYXPp9QsrXW9psFYRw-8p7quTNEd8WWPpKIhAshb1pxPr81Pr43Lrq5nKNegp2lJyZntn6NSAJjiEV_ZuHSsXtAYGcQKHvZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=oqHd1gh5AjYdCTWr08uH6LgMI9rPtfZjKZZIggwSO-nlqWTwI6BrXFDmXnZg3oEgua7cZoSIzAd_xFDIlZ5Ak81yQrZhVJSqrr9os0ceIqwRPloBz7NQ41fNTMJcOCwwevGLBjzZMFfIn9LMwMv0HtOH_IBrg22MqXeIKCfhBUJmEZ47gVYNUoGuHMBTzrtVDQGMEv0Q1WYzCNClKihwF5lTqgREbJvTjNnuwwaqOl-nYLzu_gWIjk6Upv7QXRhFnjoBPQxwYN5p4m3w7kkDmR1OAxVlXs8OkrEupgm4oltsWqrL83dsemTUp7nY0Fnbm9DEQVUM-koe_jsfkVEHcCDdA0C4xlDtfSXseXARt5U3X9k-Xtz8pKut2wgpO8bSSNa_Mq1JSejDKN2bAveXfYeXVpo-1HSCGy5psO6Tw_Huf2WGtW1bPKmxvqi0ZM7gEOePJ5tCV0TiAmsCH72UA7HcLnnSXEiPfDGNThvh2bX9GWn9PX133LtTpdSIc8xDB66oQb8MBkhzEdIELUItAUDxClrZKoys9SiQaDFABO3fu-EP8Bq64adJlvJlfSvNkBq7ClvCQrbsepYh9k9smXL8ANu-_G5VG59ntRtZYoih5xlnsvjI29Cx0NkFqWAW8txEulYzaH_WcJ4BonxoHue7RCJKao_o4flkCuKt7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=oqHd1gh5AjYdCTWr08uH6LgMI9rPtfZjKZZIggwSO-nlqWTwI6BrXFDmXnZg3oEgua7cZoSIzAd_xFDIlZ5Ak81yQrZhVJSqrr9os0ceIqwRPloBz7NQ41fNTMJcOCwwevGLBjzZMFfIn9LMwMv0HtOH_IBrg22MqXeIKCfhBUJmEZ47gVYNUoGuHMBTzrtVDQGMEv0Q1WYzCNClKihwF5lTqgREbJvTjNnuwwaqOl-nYLzu_gWIjk6Upv7QXRhFnjoBPQxwYN5p4m3w7kkDmR1OAxVlXs8OkrEupgm4oltsWqrL83dsemTUp7nY0Fnbm9DEQVUM-koe_jsfkVEHcCDdA0C4xlDtfSXseXARt5U3X9k-Xtz8pKut2wgpO8bSSNa_Mq1JSejDKN2bAveXfYeXVpo-1HSCGy5psO6Tw_Huf2WGtW1bPKmxvqi0ZM7gEOePJ5tCV0TiAmsCH72UA7HcLnnSXEiPfDGNThvh2bX9GWn9PX133LtTpdSIc8xDB66oQb8MBkhzEdIELUItAUDxClrZKoys9SiQaDFABO3fu-EP8Bq64adJlvJlfSvNkBq7ClvCQrbsepYh9k9smXL8ANu-_G5VG59ntRtZYoih5xlnsvjI29Cx0NkFqWAW8txEulYzaH_WcJ4BonxoHue7RCJKao_o4flkCuKt7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=bGoo4Zls4QoeVIT1M7WP4N4BRB9hVw3NPRLqjFIDSkT2tcpDLfVfiFhPS4Rj_DAHkO6dQXWjrYZwTZbbFteGmth6_sqw8UPklgTZPCiau0NcKcVcekV290AOs1M92y99NAPnP5tMoJYFHu0rj5skGAcMpxrQIwki7EcqlVnZ0e7a7KSxQRJ5CHJIbE-bWJ3BU7lMim061D92NJVq5o_W-n005itDABOFzqzzsMXVVoO4EQgLtlscoijKyiY6hAb41yydDTK-fnuGIzS-XWYx26LHGkIpUNphV55ZojH5Ynl2KC9GyZe0Ft7q2v69q04NmIOo4daW51Rqu223mZiEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=bGoo4Zls4QoeVIT1M7WP4N4BRB9hVw3NPRLqjFIDSkT2tcpDLfVfiFhPS4Rj_DAHkO6dQXWjrYZwTZbbFteGmth6_sqw8UPklgTZPCiau0NcKcVcekV290AOs1M92y99NAPnP5tMoJYFHu0rj5skGAcMpxrQIwki7EcqlVnZ0e7a7KSxQRJ5CHJIbE-bWJ3BU7lMim061D92NJVq5o_W-n005itDABOFzqzzsMXVVoO4EQgLtlscoijKyiY6hAb41yydDTK-fnuGIzS-XWYx26LHGkIpUNphV55ZojH5Ynl2KC9GyZe0Ft7q2v69q04NmIOo4daW51Rqu223mZiEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYy41NY7UWPY9oWEKed-bUHNJcV1Q7gA7VIlUZW-VekKFszt6ZY7_NAP8tInWG2_0El55POF3L0qMQxOovMQiaoaXtTJFlkJB8vczAvb1WnuklarXKsxyJNe3ffFQ6jUGNigd_jJ5W9CsOwuobp8O5SWSvFNNjju6ZiyL-3Iwby4FUUtxIEJjE-acTp0YQXFJXA8DC5Rj-nIrDEOBh-inch-ex3uaCJp8BIK_CTELO0TrjGBVBwoFLF0VKaKnDD4vC7BLXZVfzau0PKuwqL7jBF_3BtgtNCgFfpRkw6vWyquGXWBN53pgjiFsxVUg4eYgvQTchfjQvpA4_mBuqJOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Mfud8HBbWYbvLSgMrknvjBZab6YiB4jogfRFlWDK249m4rYJqRfb4nySaYqJ-PfhiUjRuhkM3nLpvXC8EILzp2NCt_yuXH_couifJY40kd7HBTElm3AQ8B_GASMtKKM-kt7teOVSLISc9zVrDFjmM3WQZPXgDuhlJFzPNC2XzMKM2yQX-YH_4f4KUFUChxUsjZwNMSB4TZWHuFOUFqydLAXUzcwR0thFfzWVdXtJFJydvMKcd55ea9qK6aDAGQOtQyEQJ5WauUMBi-MORyN7Zw8jBwE4BHwR3a7Nuf9Ri7laDR6K5E6-XaBTmclQz_KgQ-SuZYDzf1l8f72F6-Vatg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Mfud8HBbWYbvLSgMrknvjBZab6YiB4jogfRFlWDK249m4rYJqRfb4nySaYqJ-PfhiUjRuhkM3nLpvXC8EILzp2NCt_yuXH_couifJY40kd7HBTElm3AQ8B_GASMtKKM-kt7teOVSLISc9zVrDFjmM3WQZPXgDuhlJFzPNC2XzMKM2yQX-YH_4f4KUFUChxUsjZwNMSB4TZWHuFOUFqydLAXUzcwR0thFfzWVdXtJFJydvMKcd55ea9qK6aDAGQOtQyEQJ5WauUMBi-MORyN7Zw8jBwE4BHwR3a7Nuf9Ri7laDR6K5E6-XaBTmclQz_KgQ-SuZYDzf1l8f72F6-Vatg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=U5iEhO6EZqlqFiZE9IUnnNM19Q-mLdXGX7tUcc_qrYm4zFwPLJ9yjJ10x40Q5ORpYQbfZZjSQOeeb0xXLTVkYwW25gbIn7vMvwztiCkNoUI2WUwwa2gbNydo-Y_kSlgKu1FX8drXkPzFV9RP8IpaPILvKPGpmt7sqOIWup-3ssMkz1Pq_P1MsAMt9cYbmUNsEYpXHKkPgJLrjDOYJai3VCjb6nYF-eZwTdBBql7t5DxV4JpaZVts-WqXCPH8TBnIeFppxyZOL_D0vFQXtArvaO82XujOIJDymEe4XWwzSKsZweCdS1pNDGovw45UqwqE5CsR6taj-WJai6UQ6rDsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=U5iEhO6EZqlqFiZE9IUnnNM19Q-mLdXGX7tUcc_qrYm4zFwPLJ9yjJ10x40Q5ORpYQbfZZjSQOeeb0xXLTVkYwW25gbIn7vMvwztiCkNoUI2WUwwa2gbNydo-Y_kSlgKu1FX8drXkPzFV9RP8IpaPILvKPGpmt7sqOIWup-3ssMkz1Pq_P1MsAMt9cYbmUNsEYpXHKkPgJLrjDOYJai3VCjb6nYF-eZwTdBBql7t5DxV4JpaZVts-WqXCPH8TBnIeFppxyZOL_D0vFQXtArvaO82XujOIJDymEe4XWwzSKsZweCdS1pNDGovw45UqwqE5CsR6taj-WJai6UQ6rDsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9TJReXWUSvIFMvl-Glyge4b8oCeVE-tmUD4BE05tocRHXfozIzVc07gzNrgT9KZ1e47IfesjVNtCY0b8E_FuD6NcQz0Juy_Ut1nGWCZOq3l_-2Vb-Biq7MyQNQr_Tnn8SnIhYCN4o4ssh5KwMfzH0atuY6fq6Cd7trIyMbfHzTbngG5pttm4fi05LeWv03dMlMb08t80Dnm5fTf0x7UPB42nIl5THqzCtZSFZ0A2JhxhMtjs90uTlAZCEb_LFqTlZn9HH6lqUz4uOanEASylr9NUTJWuJVfgt6hpYDMZfW-tAG49HRmyc7dOMsy6BavCeJvQr0Q4CZgY6KoeYPZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqUOnwihB5xk7Nwkf_8ScfCxr6rWo-kQgK2Z6fokICvfY1grx17RsddWb7rNEvDDbb0BQJvlbR27K-OxIVn8jBeKdOLtvxlY1MXj00cli9ydctuw1Pv_XP4kxDYVMF1V_9TfBariJSYc-9rtFTLGZgRIo-ECM5UEpK9lvIUIS8uqYnnUD2umLPSPwSg7a6U0JWIwhva_ohk8nAaPH4sdz3wLfPB2VlC2HjR7BCfzBfpsyR8jVM1GGTHxhHp29O7HzdBcuiFV0BauTcWX2FPR6IRHq3Do1zYwbmsCyihWmetPW4-Xq-OdKi0vio5xe8HGeZviW-oRpjNUsyOG9dPCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6CndpcskME3k9qICss5gKxVlWwXQEYShMM-eSbt0IddpKAgGTsCMcRQnNoIY2kLMOIz6pkOg1qXCFVVMaKHR7yXLY_DEkAZ7w84qTw0SDqYYcUjttDysnJ-7N3RxiXg627XabIAGxw7_abkorBXPOGTbV2nqHaZH1f2n2fz4QN6zstBPR6SIUnMzr_Q52HCTYGRCb9C_WscBjFDK8wWFcFwYq4022ZUfa2FUBh3r9R247FQH6uabQJJtFEMaoORBQYEKG3eSmZagMcwA2gIvwlejHmyUiKaTVG7SlOETmGBvw56u1npcIT6ZzaeoHIwlgUQaKunn0TVvEFSVWNDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-IAO4aWeDKX3y6RavTvpmVpsxDptgs0vYpqu5wJX5X8EHSpM0Va15L5NDCPMJjd6Yj0JM0jAfQAEYfMOKY_Ne--9kGWMnDl1LKvME1fJLN_ZNOwiAoHC5SQGYukik2gL2utBmfqC4KFwXs_d4lRq_Yx14ZVZm0vhtakWB00FUm5-iI_amLTsq83jR6m0B44FWcnyR5aw-gbCAWy2OUBeESJOeRwzwXOr9yVKb1onveMNLb2-3T8-pUgU3_HvzVq30QNEZfPMorUs6-5FX4WJQy8RprmmEoYy99ida-LD1723pPHVbbZQcOPcZrP1DjPtxbHsiqoNOigGLoclyWZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW5_tVs0wtNE3-sStXB1n9iUscVdfogqNBy-W6P8_OiqvgkSqw7l4PFNNsGfN6xjpc8iGnbqJGVPDcJ0YAzPH41_6o81UhhOMwOuDKjchD0LpFWi2W02i6u1LKvWVDEU8HALFbsXTzjzfAbEXi_4tlq_2iw-nX6tgnb-a9C3GNhbbav4g-ssVdzgwrswUikcSiYZ0jPuP9E3cDv9YAeWEM7mvnzn08N9tgVMxLW2xYeoYtUpmFbWY-ABFDd56D3iNusl7QQBbXHtSaUKx5DRRAj-Fe1HTGH-cOyl77d2hol57Idezk32TnOvResBMlN-y6h3y8y0e4BxCOKsHwYeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCq58qiUCvmWNBApx_puOyLZn4j2xQSjjXz7kxjoGZsdxZM4J3X5748BRaNvgYuNHGldy1tT1M6Y-QuexoLVYTg9TCiDkT2C9DlH6jFx92wNIXaxdb1xRkrxzQv_KdrZviErow0POu_NGomNldjI8W7uMGacH_u2aRv7HiElfkyeX5ztebKqjs5G2UZ-wrClgIkQ86TVc91hWZZHgTxYanHMnFbJsznYrX7qg_lFnOj1bvEACxMpXxGxLGkaGUl_472Txzrmqyw77Ox287b_reX6RWwPCrukog9edO5aWkJeXXWijnTJkns7mZDOsBOonV6fXCvKVwZHQAIU156xVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqv3LC9iFfrAI_fzLVs7mQkyZYWeGn8OM5-_m3bO4xU-9m8EiaplPO7PxKActyTd6Z0aLg580VdtX7-W-kqD3a5-CQ0R4XMnPFSmHpfYCKjuGmwLP6r33xnPC7TKoreAgfu36noFyKk6ub0n0wkfZWPmTOxanlZBrNOhwxtwJqPrnTk1yjcDp6EnLQmx5ZVkDMcRFJQnDZdwlitKGijyxFF7Ky_Evi8uoYXC2xNsZOUdioKlXENuJm0y4h0inTWh6s8y3IN-BvVOpBjdCLyijxg-JIWD1_L9Fv4hf9XT5DN7Yxw3Okhd4XPQVD3IdAzDEpBDMhAxlVJOs87Y1f-9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNt7eyhTMHQ1KUkdxQAYcB0RE3CngyAl0cENfyto21LbHGnkbe6j08y6rc3I-fZpWkQghvBHQSNQG31i3sVDVHkFXq9vVeH0tZV9y2J6Z00MAu2OUnHSpfegWJmILQarzjtsN2NPKlzBSZvaalelXm8RFw45kr7sHWvRW44QN8qvgb7ZWZ7lbP1pPvZ2s-tz7-bc1Np8Nr_uitAoydnBPm5h38y-5pQmjSr927YKPY0SgZlrlSZjB0AZOoCkC1Xbu1DXY1Z3pwvRPdMwXsFb7btlw4OiMRnY05vvfVuel9HT_H-V_KR13SkvAFEZywcdXTbAIQBugkV8-U4Ac2Bpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgtqtSYtjqqv27ZNmD1eoUAcTftFcajeaIlBrHiavilKHrk0kK7E0BgqmsKsT_HeRgSZdjNvNq_dzoN9wYHj03wlg-VM9kkxZ5WkZAjJdrA6dfr4bYQPkf6Q3PWGwM7FdBUPoKqMonaMD7v4HcX4RwyGhrkBTH5XrKVnnvUysKCOxo6RfCTHmtfCNWRqPcsOzzOQ1aZ8pwHY8ynlovXSVB6nfeX4HgqAQfqcTv6efoZ-iZdXREPZFJlqA2aYmRWjMbJjkF0_PMX49vt8PFjvm6M35e8kLOmTR6PGT-pEUNsKMOo1UDbFR7F4KZHDc_Rv4opkht-3YmMD6JQpPYi7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOKbzuT_znfq7Z3Q5m8WWMosO3FNERLpMg95LRRyiC3ORBHTeAdA6nD_VCJ1v0f27CAnh8B0vCUWlhJ9NDZQNU0bdlSKkT2SfdOUtVk17AsNaR2BY7hNVgjyPa-N-aK2lC9Z3pU4UCdCooaIcUKW0B1Mcu_N6dveBRccxbaO7g9HdR9Hi3zc2nUFoHdRFJeNxGxihPucXHaV2tazVdFz9uW32YZSPrfsMSiklQGOKanbzXVZUfpAsp-qI5zcJbMFdeOdaNntr-IYMjwuV2R7YTvSfj292-YbctgdeMjlX6ZSptB5aL5BFSNnWKVS_DQx8ul6kHAjzKK1660QA5t49w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=BO2BX-i46ruoO6m4KW30JBkOKiOMePbV-wQ6urWtcJpxVK_LZpstAa4WnavCyNKDwYKB8qI6qq-0o9ZLRNstZVy9NkknEjuHVJeCLkigF0SEp3fHFfLn_Qp6WtLuXc3Yzi-l7HgeGpwS8xbeV5sOB3N-r1N-HkF9P8ma5U5EbDQ53iVJPdALIx15OOUXQBTkuwPk6jgipTvYWoo8J9l9fY3KxhXUxGQtMRcitUhOYzuiMmOMQhDLGN2JA_0s06aNXmbQP1xCHvjSXxEuoVUJlq2_KmPCgnXQqAQT2XHhsoK1hXjvWtF2IhhPW6V9prr_SPBrglUN7DBxGXxnwh6vLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=BO2BX-i46ruoO6m4KW30JBkOKiOMePbV-wQ6urWtcJpxVK_LZpstAa4WnavCyNKDwYKB8qI6qq-0o9ZLRNstZVy9NkknEjuHVJeCLkigF0SEp3fHFfLn_Qp6WtLuXc3Yzi-l7HgeGpwS8xbeV5sOB3N-r1N-HkF9P8ma5U5EbDQ53iVJPdALIx15OOUXQBTkuwPk6jgipTvYWoo8J9l9fY3KxhXUxGQtMRcitUhOYzuiMmOMQhDLGN2JA_0s06aNXmbQP1xCHvjSXxEuoVUJlq2_KmPCgnXQqAQT2XHhsoK1hXjvWtF2IhhPW6V9prr_SPBrglUN7DBxGXxnwh6vLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbOGWPOQvUxJW0m2RS68xdEESmnw8xZsc-ucau6iyiEdRktdOinKxYYsSXkQ3DWQpEZ5-lXTJetWhjxuP1G67nMMuZjM1rtxx1lFuTlxl24FgijYbDFQynC4m10-E7jN7VN_1ED-ijf1Izpanpa8rqBArY5kWwO4BNxwz_52W6UxIZcSvHpm6jEu0WUWXQWVxuUAqGgP96naX5h6Z9cTq6clDTPUfYWNUocPBdsA_3q1YvGGWINV9JWYkN_Vj2Eev-FVPRy0q5RgZVPPi_GtX43YOxY2LBxh_Sh0sip9N0wQb7QDWUCX-4N82Soc74mp8vceG2FSwt4kdD5FcsqrMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUISVxNDSHaFSg8huAio_N23J1MRoiMzi8k3ll5xXumSZVmEFyB1zEkhfdj8mg_DEUW4A-V_hI-kFnGXcj2lkn8BBMMRYgBS6DvvnHsxuVuRyYiVAXTvBhrJxUJiR97wxtrq86IdmrVG4E5qFO88OKmAHMD3GAFEdkf2HsXfKbb60aJNVOSF7pgzGI30zqFeU8QjA0eK3QvUn_KLKcUgcdj6a-JQsrtquIaaIWuZ-jgPCzmD9OdPKaUNvfA48i6wS_iSpqClPOPgZIeFxXkgDOpvVCWqLVEMSKE1Je65c3HqDGHo8aabV9TQazUD5jvekZBTu309g6e5CdxMU1r6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
