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
<img src="https://cdn4.telesco.pe/file/a6mL2sy2jo6wlKXsUQ5nOIQaG0FskIDaWqd2KBJueFiif-h4Y5Lp1HPG3XRURX1edTFUPPmOZDEGcdzkSEqY1K8xYK7Iijvyjhh2tRhmVfwGjYTSOHwBcu_pQ9Ofz_a6IRzvdfXzfcggaYEXAmG0VwvZoheOVpv9qMTRGktlPjHbWD0u0cqejhRm4_h8iVaanCXLAorsGAIDPvTTzqKtkpLe1cTd0DonRMrp_6ABCktyqqm6lBMmrEoqzN1VpjAYnNt1ogYMIYXu1OZPYFFsjKcS9wCqrQ3awRHztK3lNg98a5C54jV5w2Sd4icgZPxdQzBPcHBtdeDIbjhhtqL_ZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 02:32:07</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elcHb6yiaUJwvLFRbeFQsgJbActSxfuHDrkteD3bxxT-6_oKthVH84d_6KVb-kTN-3ZIfHcE8EfxZy4RFVnWf5z3I4O0urswAFbBHUKgHj7JFA8G1VVFjbqOWlFTCGPVqFQMRrc7wMzf9emysD_RltengCGxm8PEMqUqas8shVXq319Spz_X05uadiLhPJbvj9FLf8GL2nc-q5_kEVMFpfhD6E7_k62QvPeeTatun4mstv5VRBkFKH3mzi6i-czpLjYjmjNHxj-Wgk5xQQISOY9jc8PIIQr0DrG8-dKNWxvPVh7xEiBlXhOZQsraLtCEPnRR8D-n5kaAW6DZsW7H-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCsCadPeFAnMKETF7kriyXUpwIqf4-mdtiBS78pdpgmNUc6sZ3pshQCHHtKQdtCkScLEs7ST-pG60GsQ6Zs4V5pYGBU3gN2D_646VBc3VYzmfCZ_7qbCegblh1zKr6hoVXuugU5Mal80oq-GrULrkf0Mje8vTDuzunt9AUzqtKs4VwSS9VGqd4LmbjOQNZyN4Ed71jWkbEks9P-H5J1FkGhV77ij8DGtTP2yFZyHwgusvhGejam6oSxxUCLxoLc0mdaPKavsNN2Xk35Z0krW6HlccFhdUaox7zTRY4Wq29yyTJKGRxiITLjQZ4H7pRr5ubCfBIi2CnuWbG4NoemnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq4v68gu8qZgxyv0x79koN9sXy2NfJgr4zlAPbJoX6sqmqELWbjEQTrbvomHOnxNkcWSuj4Y4tmBXh6xWHmv2-c4UUln_v5nqIwWQ5t-kLuK2HRLPJarh7TO-HWwseVqrFf8qRFH0MYhJ_eeOtKNMZaxnPlvXSWOICRGJG6AQlCxP3cYAWO8Vc2u-mCs_q2i0C51UfNBfmdQL1FBOAT1OCqHUNqj6RQI6wpzZcp-4LYvHpkr_iMaIICbQOuYB2MJ2qcoYHXnRekwaT5Xx9MPUIHzsrS5EMJhyJENDX7YT50y31aHd2LpgYoc6WVj3ft7HTw7hRHklbhC26RpRSIS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcHxkj6C72wV43Bq20KAQFohBCWsH5WAQZo4JJWQY1uB330QcfOqa4ZeZ7YeSWrLZyvUJgUjY7Om89ydf3sRy4PQqtpTOkZWoirgFNBa5YqHQ5-JHyjouO0BIpoeIQ19mIJt9rGbMt5z7V49gonQr4iRjPGx8Cn-YFkMAmlYPN8-pvv-Ry5U5ZweR-bP7YgyBSX_Kcn0-qGwDusUSLjb2IAjyiMb47tIuG6K2ZfyfiLih6t8h9vo3GDoDdtfNW_IKBwkFsg2t1azgDJo4P-wROpHlbYTmc3HG1yhgEu1hnnN9VvoCtoDbWELS50kGt7OZWg2W4zABk0eXfnFXnXAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFgUigm0gZOkwOVvrgpR3ePHoGg3ZEbJ3lGzm_ZKtnW5nEVlX8IH87if9KaR2mFWKUnsxZCFKG-uvpU9JP7dzBExccJtuHRy2H3x0Zapa9TSRPa1ecJ_Pryk7fhoqpwjwtGRQzlAhw9NN0JYDz9oCunwuB7dAtERt0wu7uB4Eu41Su3VYDguzXdP3-ndAJLsrLPCDBLiJ93PzwZAcwOhpkpS3h9P1Giw0ToyFp__inmm0IEKYalsoARzYJXkKspix_Ieeg39SSbMw3YDFYiz06sRGbA-YLIDJnP3l44U90XCCLvXa9MpbTISpjXxaVPLDB59m4WUjADmyNsTxWU6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IVM-Tz_nPZY0CRX2B0mUZqNc_f6KIzaqanysqO-sS9iKmbWeZ4F7OXnNVM5H5A3-0uMazZ-18IuTkOR7qMtu8w2QkkNnkoDZUhlCj4ORUFaZfm2OqpWUd-6xtO4aYlwYlXblisC_gyz9jPEhPUhdrNNxITm1TWVTibBadxN7yCRpOLWl3beMBU05tSyjhJVTIYGH9hWjMJwbKis8k_NHkqCvhoJ0WLbw5PxDcFjDjEWxPncCAZQlOpzSJ5FsU0FGLfUH6Gf50MmxCqlNEhA_r4xVGU69OAAd5pECW7B9KI-5Jmy2AB3jJenvb6arxynTkWGkpARQj3MPZ_6sHMcLtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IVM-Tz_nPZY0CRX2B0mUZqNc_f6KIzaqanysqO-sS9iKmbWeZ4F7OXnNVM5H5A3-0uMazZ-18IuTkOR7qMtu8w2QkkNnkoDZUhlCj4ORUFaZfm2OqpWUd-6xtO4aYlwYlXblisC_gyz9jPEhPUhdrNNxITm1TWVTibBadxN7yCRpOLWl3beMBU05tSyjhJVTIYGH9hWjMJwbKis8k_NHkqCvhoJ0WLbw5PxDcFjDjEWxPncCAZQlOpzSJ5FsU0FGLfUH6Gf50MmxCqlNEhA_r4xVGU69OAAd5pECW7B9KI-5Jmy2AB3jJenvb6arxynTkWGkpARQj3MPZ_6sHMcLtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSw__rW-AWNMFjqVgUq-XYjHyQoChaYZ65kOqKk4l_0Ips6AePgFZemNONSHDCiaXRawg-LoTG2zekcwZUtxQBDd0kL_dgGX6friKzdDlVoRzqCRboSXZcNOzzIrw1lzXVHVtBpXDBiw4a7KD95rPinzS9kHthgg7X_KMV3QqC1rT3cLENE7YKwEQpYlrwODdFMwCQR0hA2C3QlJaJd6Xx95DB9Wg33djRxC2Orh_HC9x1IilgAJvQniHaJwnFOGPS5uf7gizkI5Tsh2oRV-vPIJSvWn3gZj0OsHG7utu7OZ2KiOeBq0fat_h5vBohIuJvQzdKXEFNvFlYOSkY0Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=b6gS3m2HiI7Te5QteMLDl0Dgqh9yALtCojQPrA-IVkpqFwe27tJlYihEMVb25AfH0_-x4DkxpyN5H9JsUGC72L1LRcYj_l9nWBURZ-Xz5HAs8Smu5ixPGCUgfHmWWikV7itCqfb9TemUvvuaSFU6TZKTDAgZfk8-HvAefF1IXSUBkSBuiG-OSKZUr_qCn6opBwLuLS7P0KoHScoL24fxGAdpzl41u5g9MHeozuBegqzppZX2xXfNcbJhCHjtWhTIis4Pd2sk3y6gdzAXGtuq9_3lnU4t8XKgQjYNnkZHxrCSVQXrVAM-7wgAlTxVmqLdPZfBGjTON19NUhWYfMxC0j8nuVRyaxbjCas4M-c_As9ZFVL7R1CUJ9aHS7wcHT2X1Y5bfe3ZcEJg20lU9mA2fGjH-bWzgzcIjWHhnShn440Gg_dZNqmCcpFatexAfyRAEeeka3zN8EdEWQVBEdgwCVZiPlxAkwziNlhOSPJB_0iRn2Povyb-yZhUE54yJ6hZRuBtJ96HGw2SWgw9ivP1vaajOnu9w9BNNhKSWU0MfduQDW8Ny72dNX4k5xfjMvBOpdssRNlYz3xBOF2PlzsoNul_z8zOVA89JduS6jEajqXtCjyhiC4-6Gy-geVZMFXGmlbGzrh9vQm79gui2kCfQkgBtMTxcHgA7J1dyxd3mgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=b6gS3m2HiI7Te5QteMLDl0Dgqh9yALtCojQPrA-IVkpqFwe27tJlYihEMVb25AfH0_-x4DkxpyN5H9JsUGC72L1LRcYj_l9nWBURZ-Xz5HAs8Smu5ixPGCUgfHmWWikV7itCqfb9TemUvvuaSFU6TZKTDAgZfk8-HvAefF1IXSUBkSBuiG-OSKZUr_qCn6opBwLuLS7P0KoHScoL24fxGAdpzl41u5g9MHeozuBegqzppZX2xXfNcbJhCHjtWhTIis4Pd2sk3y6gdzAXGtuq9_3lnU4t8XKgQjYNnkZHxrCSVQXrVAM-7wgAlTxVmqLdPZfBGjTON19NUhWYfMxC0j8nuVRyaxbjCas4M-c_As9ZFVL7R1CUJ9aHS7wcHT2X1Y5bfe3ZcEJg20lU9mA2fGjH-bWzgzcIjWHhnShn440Gg_dZNqmCcpFatexAfyRAEeeka3zN8EdEWQVBEdgwCVZiPlxAkwziNlhOSPJB_0iRn2Povyb-yZhUE54yJ6hZRuBtJ96HGw2SWgw9ivP1vaajOnu9w9BNNhKSWU0MfduQDW8Ny72dNX4k5xfjMvBOpdssRNlYz3xBOF2PlzsoNul_z8zOVA89JduS6jEajqXtCjyhiC4-6Gy-geVZMFXGmlbGzrh9vQm79gui2kCfQkgBtMTxcHgA7J1dyxd3mgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf8PXZi_Qe9V9tEVdOh6JyqiNNJX1d9Y3GOSeQ5XJt55OcehGgeESdnh7gx8ndc_iN4coi8s1oAMlBBQ2o4A4HHu5UDCtWuBQuQhUC8nn7TRFZS6Vl71ObUVzzXGGLROTaxm8wse_JVIDeFk4EohhX_Tl62rdAR_lVLpsRQxeTgofiGZUVTdXn09YkQ5DQn6dbjCgbvZ0ks00681uYXhHGQ_E2VOJp7JKGxYyDqPA-dTs7GJeDYEF64zRmXKEXjDoiZKWSfTpfzonXzB6mlgJFGyFNdcNuL9vxObNu4uFfFhez0trR0gC9S69VMrezv4ULye08mAwMU4LNkX4KP9zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIiVYVx2jgB8B2u0P8Sx9N3PaToE6O8Xx8ojRP5VU3i-k4mmjhV4Dj7FiQ9sjuYR0pelriEp_M231DgUA4iI0oKoQDL3M6YVJl2H9KBYrNnPpQ6E7lkop8JRai9_TEn3Vu9zdgIDQTFqL8xwHmn2YEyFfGJmzk0wH7bmb9YVekCHzSsJQCBaB5ejkSimSDrA5cmc7lcvyo_8mCfwceYuGvJZjeVmIl5ZtvsaQLMiOcsosm5CNvMkHgUYfGRyJtLMk2RfSJUrfeBP0p9h5ctp-5H5m-eL-b3clPNYhBhas1YbqybsqRYOssEamCVq77kiEzKFp7zVQJ1BcuC6FLYjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1muZeM6IFbM7amLYe3EtecVjjE-6k-Xy2po6cqx0HlIHhxeBFmYwY9uytnW3i7y_FsbgdCLhIhCLa6wLxkcpx-zTJLVM51QvQkXZF30LCB0NO65wm0CAD35IG7GmOwdfkV_Bv2E0KR6dbTlIO4FCL4hyezXwkksVRa71xj6uXjS2-Ti33QRqn43m3KQxcY1nH5XpykbIg3_dLcS8AB4rcLpO_y_FhErXSZdLthpqU0E6W7GdB5jwE_Plj8WaWZm9GvKWspPIvrPwTOqISZ4vX5Dkkd0pO_akGdjnLeqb5-pFVYX822Bp0SqCVS7vCi91M21jhCDjC2-gyenybpBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRBuPt7od-oLrJDkR9quQpOlaGACQ5wTvmPss7Q3sXCFdzsr2tmfkOUEhVIMkcxR8cog1BFUCkYvzFXnWjNJIWzDtS-jNtqi_rCZC_Nf-7H41a3lFVwc2Vl2PYOknwklWGKvmJ1Ak6uLfhDiZAheNYZh3u-TSQ78mAoDNC7F35-hBRxdA9zIuUYmzKO0L5LytOOlCnSwBFzUwJCrVjS1TFOtBssWC_kM38xKycnv4HpQnfZdHOM4Z8DrysloX1wDWcK99JFStLKRwzeBKPSxoctQ68ot0GE-cmQ_vH-ixbb-QRQkIpAwviikBeEpOhmlgIFLI6oVxoTQdI9DGuAFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy9SMr_HmgtNgx-Uo3u5DSUAO3bmpgI3a48ntFG1EvmyBn6LzRHwTMuMy_iHHsoLLttgDKodE89IAjmTEwa-B3xydYQj22aUqNMF8es_nPEbKoDt6wOd15NQvywTpkMsZs6-tivXTb4f_G9d-Bbh8-379H6Yo3xTKqt1ASZIr3cTs6yGkK46ipxywAom9ruPUywL74J_chACjsk6jOnogXwIQ2p0-utfwNzkFOwj8-IPb-9-iDuMKQoLKruSuu84J5-OhT1GtiuEZORxt4t5hpH9QWP9u3v7LvQ4Zwg5U6hKnIKtdc1AD-ZV6I_uKFw9zzmlPmlnxN70okzhZTNNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0qtxlx1gXzz28sWL8TBOiEbWMBvNixeNklfxH3Zsw04KpQrx6fscLPtCOAxN_eiTcIcSv3Fdj8ZJkvHt5mXghs3ZCJYDJscnrMaEUe3_E4PwlWp8UXub9cbPzFwg5VBzNzLpJf7k-GPsd8jMm7LFcf8Cw7m-FVT1AE1MuwkhQ5vQGMmP6ykx0ZEMjKg5hLWPB30_gzvKPS6iL_BM9dyVv-_e1VxzpVZTZZwC1UBLfxFBczJ5S2uKAdkDC4OUkmYbIomQAF8w6gcav4pFNEYg832teOhP2boRrGH_U4Kr1n2pTl9guutIT3_o5Z6n16AkEXp2-R1WaTftp8jbGoSd2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0qtxlx1gXzz28sWL8TBOiEbWMBvNixeNklfxH3Zsw04KpQrx6fscLPtCOAxN_eiTcIcSv3Fdj8ZJkvHt5mXghs3ZCJYDJscnrMaEUe3_E4PwlWp8UXub9cbPzFwg5VBzNzLpJf7k-GPsd8jMm7LFcf8Cw7m-FVT1AE1MuwkhQ5vQGMmP6ykx0ZEMjKg5hLWPB30_gzvKPS6iL_BM9dyVv-_e1VxzpVZTZZwC1UBLfxFBczJ5S2uKAdkDC4OUkmYbIomQAF8w6gcav4pFNEYg832teOhP2boRrGH_U4Kr1n2pTl9guutIT3_o5Z6n16AkEXp2-R1WaTftp8jbGoSd2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=bQzXNTEQV6Kytkw__2IYLA0_BwIvGvXfKong8bpGZ-LAi_-mHR6fe0Qg8DtQfKSXJcYs4Su0Ux0BHO-Tbxo33H_Gy7qu5KUlQWh9J_ItUwERNOXgGmD0eRVHjPWsxz33yhdLvnJxqFyTw3zJ5V7s20WPeYSkPH0oKQYlAnkyDkMQ0p32rQDtvqTqZ6S8xzFWv3vmm_doJWKjF2SrIRmxYONQa9cXFxmqEbREeyB-5IGyQwYrCWv8gmFtujWuc0NL-b_1AX7v5L8SUnzqXqPh1kbpWPIQbuxq8rvp0Npynu37m9OavqIAWk6Kh1j77v8tbGNH7bP0LUn_q3v25eJZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=bQzXNTEQV6Kytkw__2IYLA0_BwIvGvXfKong8bpGZ-LAi_-mHR6fe0Qg8DtQfKSXJcYs4Su0Ux0BHO-Tbxo33H_Gy7qu5KUlQWh9J_ItUwERNOXgGmD0eRVHjPWsxz33yhdLvnJxqFyTw3zJ5V7s20WPeYSkPH0oKQYlAnkyDkMQ0p32rQDtvqTqZ6S8xzFWv3vmm_doJWKjF2SrIRmxYONQa9cXFxmqEbREeyB-5IGyQwYrCWv8gmFtujWuc0NL-b_1AX7v5L8SUnzqXqPh1kbpWPIQbuxq8rvp0Npynu37m9OavqIAWk6Kh1j77v8tbGNH7bP0LUn_q3v25eJZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=UucEPCUjYp6l2p3QoEgniCgH0HWLbtL1Y3EFsp2Q3J-PFyEnmnYJnZpuIIse55DIAA87z0vv4HagKynMA8SZXss7HcKlq9poQGxOCuF8EaO6QTrCrkswYqTUD_E0vBRiRI9_SgB1XveStd56kBFTFqlT4jqbJZlu8A0mILQwPtXFHvrhZ5zrJmRUf1T5gbO2w-2x5yXJLlUpo8cwdDvet2QZbn_GcqtP_cafTRM6Unt8jIG1-DCaGlIQvkcyeMJSOlgtT0g0AUZ_ZsR-xqXAGNjUT0e7EMfQ14aae6ZBXwLBRAGkK2fbwqmrI_VDTA0a3tfl5dpJpcr2JUyt0SHYgnnEax1SsyNI6FWvoK2_Po0G-papqXuAlqTraEUL2S5KZxcJtcHkIPweLmZJ4R-5GZzchxnzHv_pEcQiAaZjp3ycUavqa510hqCYHVCbB-_AhdKg5mxtwubEw2wKxmpRFWwGr-aoE5jpUo6jdRfLrPIOffedX1eHduiXs1FCsxlh4onQGg_qBtfhWCONCAZ4rfY-33Q8oplmcR9gwAwqFq399yJJFul2xfhIJNBuYdIFRR_B00JLQj9CXTBDUSgAnhs_q5Jco_tFxvQY7951_1IIH_NPpKa2IU2dkJZTMANT-anOppL67Q2gemZ-c8dFhej6AbguD0kIH2144S4vTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=UucEPCUjYp6l2p3QoEgniCgH0HWLbtL1Y3EFsp2Q3J-PFyEnmnYJnZpuIIse55DIAA87z0vv4HagKynMA8SZXss7HcKlq9poQGxOCuF8EaO6QTrCrkswYqTUD_E0vBRiRI9_SgB1XveStd56kBFTFqlT4jqbJZlu8A0mILQwPtXFHvrhZ5zrJmRUf1T5gbO2w-2x5yXJLlUpo8cwdDvet2QZbn_GcqtP_cafTRM6Unt8jIG1-DCaGlIQvkcyeMJSOlgtT0g0AUZ_ZsR-xqXAGNjUT0e7EMfQ14aae6ZBXwLBRAGkK2fbwqmrI_VDTA0a3tfl5dpJpcr2JUyt0SHYgnnEax1SsyNI6FWvoK2_Po0G-papqXuAlqTraEUL2S5KZxcJtcHkIPweLmZJ4R-5GZzchxnzHv_pEcQiAaZjp3ycUavqa510hqCYHVCbB-_AhdKg5mxtwubEw2wKxmpRFWwGr-aoE5jpUo6jdRfLrPIOffedX1eHduiXs1FCsxlh4onQGg_qBtfhWCONCAZ4rfY-33Q8oplmcR9gwAwqFq399yJJFul2xfhIJNBuYdIFRR_B00JLQj9CXTBDUSgAnhs_q5Jco_tFxvQY7951_1IIH_NPpKa2IU2dkJZTMANT-anOppL67Q2gemZ-c8dFhej6AbguD0kIH2144S4vTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=d3qX9CxD-onj-J49lNeKQFo0TKu8Ha1DAH4S0N0P8NDsdMvWAM8QbVl_IcaYZMSpc2mX4uylBhcX63yPhgSXqNYScwWuw_U2-Vd0bdbvKeRgvUvlHAec3Z9OOM2R5EkUlsf-8Mu1XJBYlwZJnwA2sLxxaAWE6EoZiQ2KW0Vse2DUaC3APXnnqAicDMYSYTdSE197JskcItmAwiZkFpaLFL2dmhrfIwIZq55wTZ1_tJFSB1qZnZAKOaMFEvXDgxl7OWVc5jxRWpQt6lpRo-DyGzUWti7kj5T3f7c5t61OIPRRFjE-YR_TrIcdD5JcGGaTAIpgAoHle1PESQR2avpEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=d3qX9CxD-onj-J49lNeKQFo0TKu8Ha1DAH4S0N0P8NDsdMvWAM8QbVl_IcaYZMSpc2mX4uylBhcX63yPhgSXqNYScwWuw_U2-Vd0bdbvKeRgvUvlHAec3Z9OOM2R5EkUlsf-8Mu1XJBYlwZJnwA2sLxxaAWE6EoZiQ2KW0Vse2DUaC3APXnnqAicDMYSYTdSE197JskcItmAwiZkFpaLFL2dmhrfIwIZq55wTZ1_tJFSB1qZnZAKOaMFEvXDgxl7OWVc5jxRWpQt6lpRo-DyGzUWti7kj5T3f7c5t61OIPRRFjE-YR_TrIcdD5JcGGaTAIpgAoHle1PESQR2avpEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV6kmtQdh_2fKVgLpvCInqSq9XlzUCogHwrMwlLp5Eooqe2KuPIfpB2flMGGeIbnnJvcZntdh49WKv0Qyf0RG9BXrlj_UAKX_6Xf4ZR9daD4zgUXyYoL3z-3XDB25ml29zkhuH-VBHniRUHL4ND8gNyUPAe2KndVpiV3L8B4c3YRCH7zZ10zhPvdpXz6yisGYNY4dndLxCBGMbEIAsX3US5snonrYfaD3uoq9-Gy4K_WFJSf00eIqE-gLhMddX0x1pdiv8IoSCofU_E50UR2A7w6HUID2bCdwZ3rA3X6WSCbce-HWP4WwTSVnfiG_9GXQUaIMcWQEKm2PDX_5BCgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=o-PTYaDmVOOWeT2FXWLxTmKsvBfl03jw7kf9QgOPK3sLqLxD698bsDGsEItkdecR0ZB0qxPvRsittOIobaub4e0hiN_0LNwJuJUmIgtUyRaTdi3WOHoEVByEuUm3_b_L4wPIXUQ_FD9zE5F8rGFI9-Soa7GV1tWT89GRwKNqEzp05zdsF9SnhkvskUrNdVf5S0geyVjSGGalLVX-53J1NH4Sjhu3KZkZ6raLlvXdZnSXuppwISofxYVFwdv_bVLmBMbvbW4e5A2TszTHu44cKhOaTJS5JOshBUnQmVRZSyX78sla0L-bfb7QzWfwI99Aieh_y-FwA8tWzJ9Gfo3Cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=o-PTYaDmVOOWeT2FXWLxTmKsvBfl03jw7kf9QgOPK3sLqLxD698bsDGsEItkdecR0ZB0qxPvRsittOIobaub4e0hiN_0LNwJuJUmIgtUyRaTdi3WOHoEVByEuUm3_b_L4wPIXUQ_FD9zE5F8rGFI9-Soa7GV1tWT89GRwKNqEzp05zdsF9SnhkvskUrNdVf5S0geyVjSGGalLVX-53J1NH4Sjhu3KZkZ6raLlvXdZnSXuppwISofxYVFwdv_bVLmBMbvbW4e5A2TszTHu44cKhOaTJS5JOshBUnQmVRZSyX78sla0L-bfb7QzWfwI99Aieh_y-FwA8tWzJ9Gfo3Cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=GBPhSzxQUii0uHj_bj9sZzrJOIC2PK-nRZMNGbAVdOkrVvU4PIALw2SIbyDPffa0xg_X06zu7jGyXIJTb3s7EhCeUCQDQjAhP9EVHCHgdp1IShoYYNOllY9EUrjcnnRPCRyoLT8OhKCXRKTuY3fLzmUos7AIBgDtT6oOWc2BLapRalStdynTdt0Kb-ggVcf6BSxlDeRHLaK7WSKTrO481uJwkTJaylyrvrRwXGO4U8kghH2P7wOfCM5V-CCwmNk6gu8Ybmpdv3qMwF55h6bkdKcEly5OBNEDUt7sjhbKwWFeKmbFsYdydzyJpSNFqYkK8rDVeSEFxwtRyMpUHQkHqnO-ihs3fW6tb-TZgQPLam-GzO7dzqpDciLjTaDq5RjIig2z9J4xk1scGPTuVmR9cTBw97GeJMqgkEuNQc-p2COXH5GgMhPIbdsCr6GQCojVXpSDYZdO4xwrcqCE6CIQJ38ttzoS8GwznS6bEfhzYys2OZipXTA-DkPva3F4u54vDiVhekL5Rydxm4FaKcB_b_X7Z5p9wa6ekXij_m1FnhmMWHlpI5vWuAavPZ1Z5NrS0rqVpwX-xzujogtTUggxMt5bsmS-3oYkEDI-7r8b4hwoojJhHUEIL7y9LtGj3NFH86j35M_YMvv0iAAi_Ccvn_PyXP2P5ee_GpfTs8w_vL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=GBPhSzxQUii0uHj_bj9sZzrJOIC2PK-nRZMNGbAVdOkrVvU4PIALw2SIbyDPffa0xg_X06zu7jGyXIJTb3s7EhCeUCQDQjAhP9EVHCHgdp1IShoYYNOllY9EUrjcnnRPCRyoLT8OhKCXRKTuY3fLzmUos7AIBgDtT6oOWc2BLapRalStdynTdt0Kb-ggVcf6BSxlDeRHLaK7WSKTrO481uJwkTJaylyrvrRwXGO4U8kghH2P7wOfCM5V-CCwmNk6gu8Ybmpdv3qMwF55h6bkdKcEly5OBNEDUt7sjhbKwWFeKmbFsYdydzyJpSNFqYkK8rDVeSEFxwtRyMpUHQkHqnO-ihs3fW6tb-TZgQPLam-GzO7dzqpDciLjTaDq5RjIig2z9J4xk1scGPTuVmR9cTBw97GeJMqgkEuNQc-p2COXH5GgMhPIbdsCr6GQCojVXpSDYZdO4xwrcqCE6CIQJ38ttzoS8GwznS6bEfhzYys2OZipXTA-DkPva3F4u54vDiVhekL5Rydxm4FaKcB_b_X7Z5p9wa6ekXij_m1FnhmMWHlpI5vWuAavPZ1Z5NrS0rqVpwX-xzujogtTUggxMt5bsmS-3oYkEDI-7r8b4hwoojJhHUEIL7y9LtGj3NFH86j35M_YMvv0iAAi_Ccvn_PyXP2P5ee_GpfTs8w_vL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=DjpgwMUJQp4oj32FDoI9uLykTjOsufUIvGA7aV7wim8V0vlsahd6-Cl2GhOgYRL4RnPmFnKjGZKHOTAhC4dFILnitCSr-LeCJJIiiz-l5FTT7YGJA-zfH1up4jiAsIjMhAfLfdEtff7mV2qDM64BC6jvKyEmup0rhBmd6frfta0WgpIvjKS4hIZQoUNB1b74fuKtbj8JLPcx_bWaCN4P8-t_BHb14VkK6qz_y-eygOLyShH3jmWk5VBHOeWBUzApcb66wxcNMVr-3SPNdAPXaYfjRHm3sQfKfVuQ4RMM5zIhbeCCUwacIHn6lAZmXiu8x_fy8qleddsOpDmL4cN5s1m1pmklNPQHejyYMG6GEKFR9b46tR6n8CHYegREmyYxkwigfK61NudysxqY0tvniTY8PT2Wn1c_q15Kxvkot4pOlke09nFGlvLACIuZgLoPp2z0SIbjFwKhFuOg6nrJijeK2qepNQzFheazqgC3QPH8enzDgvuityMvgnOGfIRB3pIXuiqeSJ0yi2M6CT5EHpJJNfU55AjGBpgaX5-VtGXXhhjfUPkpOMjoOkkBJm9UGVUsWyip5kMwUdj6BjWMRtTRORbtkRqr98FAb6FBdxrADxzmCNubaNs23NFBWeLIWJIDZLSgvIz7ugK2L8KUuPsobRqlYmAA2cPdMdKq_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=DjpgwMUJQp4oj32FDoI9uLykTjOsufUIvGA7aV7wim8V0vlsahd6-Cl2GhOgYRL4RnPmFnKjGZKHOTAhC4dFILnitCSr-LeCJJIiiz-l5FTT7YGJA-zfH1up4jiAsIjMhAfLfdEtff7mV2qDM64BC6jvKyEmup0rhBmd6frfta0WgpIvjKS4hIZQoUNB1b74fuKtbj8JLPcx_bWaCN4P8-t_BHb14VkK6qz_y-eygOLyShH3jmWk5VBHOeWBUzApcb66wxcNMVr-3SPNdAPXaYfjRHm3sQfKfVuQ4RMM5zIhbeCCUwacIHn6lAZmXiu8x_fy8qleddsOpDmL4cN5s1m1pmklNPQHejyYMG6GEKFR9b46tR6n8CHYegREmyYxkwigfK61NudysxqY0tvniTY8PT2Wn1c_q15Kxvkot4pOlke09nFGlvLACIuZgLoPp2z0SIbjFwKhFuOg6nrJijeK2qepNQzFheazqgC3QPH8enzDgvuityMvgnOGfIRB3pIXuiqeSJ0yi2M6CT5EHpJJNfU55AjGBpgaX5-VtGXXhhjfUPkpOMjoOkkBJm9UGVUsWyip5kMwUdj6BjWMRtTRORbtkRqr98FAb6FBdxrADxzmCNubaNs23NFBWeLIWJIDZLSgvIz7ugK2L8KUuPsobRqlYmAA2cPdMdKq_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=QNzmPGpHyneZL-td5grpfoQtP542WE1fNRLbvN0ujegBrzUSxHA3q7OSWOv3OnNdsdR3Bzb0cRPbF0f_AuPnezsOE_tHnJb6xuHS2kmg2RYZupZHn-ZwO3Cc_sLQbwzK7EO6Tvib4REXw5LwM1ZiTjCh2tltFragVaAH_-ekZ_BNRE_o1l2dh7Gm7vamWjV7I0mdff4j_91fGyLRMxGNVPtOgJW-M4I-hbWQGqty-5s638mCxjGhUhLxc-gI2aclgw3zwX5OMlkyJL4ag26wybJUPQ9piR8wNGynHRTRo6FZW24msAFKBl72OctT5oBBPbwv_2UgqrS5WkldtKyTLkynGnrzsQ78filf7LAXyIV_yTqB5lM_hVBWVjRvjXbgEjezMcKzAL8kbz7bQyrG0oXaJggTYj_XT1GXY4EcGY6w324YewxfdYazCsWriFwbelkqqBaU0t90aGcMjIzK8ltIGsTE1Izg0q2sPX_UtHlY-ZueqYftSyAUdH54IksYY-x5SWiC4AzEFl03e03rqbEpqpmiSF9r3PAdIkLyjhKgrY3nmeG64S_IBTDy1vBnt7cskhe8hBxoDXuIxlAhwZFb20XlTTzb4dWDaVD6DqZxN6wg8kbRBZvu3Yr1sV6cuuJ8RglnUAMQAb9yBUgTmTw38QieRMKIxmAahXAsFZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=QNzmPGpHyneZL-td5grpfoQtP542WE1fNRLbvN0ujegBrzUSxHA3q7OSWOv3OnNdsdR3Bzb0cRPbF0f_AuPnezsOE_tHnJb6xuHS2kmg2RYZupZHn-ZwO3Cc_sLQbwzK7EO6Tvib4REXw5LwM1ZiTjCh2tltFragVaAH_-ekZ_BNRE_o1l2dh7Gm7vamWjV7I0mdff4j_91fGyLRMxGNVPtOgJW-M4I-hbWQGqty-5s638mCxjGhUhLxc-gI2aclgw3zwX5OMlkyJL4ag26wybJUPQ9piR8wNGynHRTRo6FZW24msAFKBl72OctT5oBBPbwv_2UgqrS5WkldtKyTLkynGnrzsQ78filf7LAXyIV_yTqB5lM_hVBWVjRvjXbgEjezMcKzAL8kbz7bQyrG0oXaJggTYj_XT1GXY4EcGY6w324YewxfdYazCsWriFwbelkqqBaU0t90aGcMjIzK8ltIGsTE1Izg0q2sPX_UtHlY-ZueqYftSyAUdH54IksYY-x5SWiC4AzEFl03e03rqbEpqpmiSF9r3PAdIkLyjhKgrY3nmeG64S_IBTDy1vBnt7cskhe8hBxoDXuIxlAhwZFb20XlTTzb4dWDaVD6DqZxN6wg8kbRBZvu3Yr1sV6cuuJ8RglnUAMQAb9yBUgTmTw38QieRMKIxmAahXAsFZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=PR5K3gyBOOqKGPqCufg8Jg1RVa-MdiSJw7CIeeolPuzhTMJ7eJ7xjsm4vxz6gsW_snRDe9R1yvfk9ffpHUz6QKKJOgaZE2RX2utauk1AUvX5Hbva9ZaJ6QUtLDtmP3IHKLJvhEYUlWLvR-bVpUYei9Z6JZv0pFWnt24Sx4kiS6t9PeN14pj-nQd5RvDPjPaUcUPlBW2BwbIotoCJSHstSLLnO9vWqVWlKI1PCYl-zupBA-VUwYap_EXvoWCI69EUt9jPjor9NH9EGoUxfNzA0N1oyVARUzVjWR84oyYCsI0jw4W4wm8nvvGio5Ifhmjk_rCctbF_FbQ1jC78zAoPXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=PR5K3gyBOOqKGPqCufg8Jg1RVa-MdiSJw7CIeeolPuzhTMJ7eJ7xjsm4vxz6gsW_snRDe9R1yvfk9ffpHUz6QKKJOgaZE2RX2utauk1AUvX5Hbva9ZaJ6QUtLDtmP3IHKLJvhEYUlWLvR-bVpUYei9Z6JZv0pFWnt24Sx4kiS6t9PeN14pj-nQd5RvDPjPaUcUPlBW2BwbIotoCJSHstSLLnO9vWqVWlKI1PCYl-zupBA-VUwYap_EXvoWCI69EUt9jPjor9NH9EGoUxfNzA0N1oyVARUzVjWR84oyYCsI0jw4W4wm8nvvGio5Ifhmjk_rCctbF_FbQ1jC78zAoPXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=fjFnfcAmKsoWPG_lDvo7IENjc8fEeFKvnv9RgcBI9tpxT4zlKtGm-1oFc45bcycZ-1qsCZGjbXhsUAcbIRf7ZzjL0Z1b0PaP_UKI8aDcCkdt6iIPRFyu0j_znFhW9zhVdK5qNoi4aKluOZVBa4Nn4I164L3vXcAB6x8AnHt2XepUrSX3psBRUaK2kFOS8utRIRh15eklFp8rXLTzwMO3PCbqmyzaCPLTtHYujd-ta2o35BggfcjTDacojHvxPYsXVD62JyFv2NKDoIAFEuliWAaxw0VIuZ_DdHnROxZXXkJrLyzZTIy2d1bWm-s4pdOY0wxkWEb-WNFeaaWWF6-JYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=fjFnfcAmKsoWPG_lDvo7IENjc8fEeFKvnv9RgcBI9tpxT4zlKtGm-1oFc45bcycZ-1qsCZGjbXhsUAcbIRf7ZzjL0Z1b0PaP_UKI8aDcCkdt6iIPRFyu0j_znFhW9zhVdK5qNoi4aKluOZVBa4Nn4I164L3vXcAB6x8AnHt2XepUrSX3psBRUaK2kFOS8utRIRh15eklFp8rXLTzwMO3PCbqmyzaCPLTtHYujd-ta2o35BggfcjTDacojHvxPYsXVD62JyFv2NKDoIAFEuliWAaxw0VIuZ_DdHnROxZXXkJrLyzZTIy2d1bWm-s4pdOY0wxkWEb-WNFeaaWWF6-JYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=vYn7xsVJW9Cp5GwJ4MW-FqSR9oHcGpteHtem32hdQ5hQjXzrW9ZUaYjDIpmcXgR0lg5bXZvatUZc2crWFyyQPaYBoGDcUrBvu6q4P2JYqH9hq9bpoD_4tJDV3QQjZTaFwz_MUUTWTXHI_XRwjVxRNa04BJay4NeBCooddSwmJGyv55dWLsCcZBVYW9T5BCnK0jNCemR9zpHbJ4-oKivfv_2wRQxFDvyEUJfOnJ8L13LqIfq1P2p9_1lRYylH-IFIQ2TkgPAcsuITyeCWjc_Dj_qUsZRuS4WObUbipwZ_tmdVfHuxu5SwMZy6ZLuv47PJ6t2XjyVzp4z_lPpOv2hjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=vYn7xsVJW9Cp5GwJ4MW-FqSR9oHcGpteHtem32hdQ5hQjXzrW9ZUaYjDIpmcXgR0lg5bXZvatUZc2crWFyyQPaYBoGDcUrBvu6q4P2JYqH9hq9bpoD_4tJDV3QQjZTaFwz_MUUTWTXHI_XRwjVxRNa04BJay4NeBCooddSwmJGyv55dWLsCcZBVYW9T5BCnK0jNCemR9zpHbJ4-oKivfv_2wRQxFDvyEUJfOnJ8L13LqIfq1P2p9_1lRYylH-IFIQ2TkgPAcsuITyeCWjc_Dj_qUsZRuS4WObUbipwZ_tmdVfHuxu5SwMZy6ZLuv47PJ6t2XjyVzp4z_lPpOv2hjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NWrFieKk1yBKFU5btHu0n19pcBCxSy7NpPQNslKpt9Uiej583p0YqcTir7x1wcrKVKfXPF3cOgwWsFlx2N9swRJApaGpa29iLgiLIJbjNViAmKOTP1aYattXBPkOLt3hT_126FMH36vJvEGRyIEDuAi6LHUc3XxVdwyS4vKzCk7zQT3kkATfvF3Aoq9FDXaEuXVHaP5hL3Y6wNX70X8_4lStiy5dnQHU6kr_-GYBw9HfXTM6ATNAb01RNUipeP4klp5Qr8nIvwluUr-_tkrsjSKXbgEnL6NBsnUTDkgrGSSLUehpXciFQIaz1ZMRvVTOt6vAwWGxn35wBXEtiBUzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NWrFieKk1yBKFU5btHu0n19pcBCxSy7NpPQNslKpt9Uiej583p0YqcTir7x1wcrKVKfXPF3cOgwWsFlx2N9swRJApaGpa29iLgiLIJbjNViAmKOTP1aYattXBPkOLt3hT_126FMH36vJvEGRyIEDuAi6LHUc3XxVdwyS4vKzCk7zQT3kkATfvF3Aoq9FDXaEuXVHaP5hL3Y6wNX70X8_4lStiy5dnQHU6kr_-GYBw9HfXTM6ATNAb01RNUipeP4klp5Qr8nIvwluUr-_tkrsjSKXbgEnL6NBsnUTDkgrGSSLUehpXciFQIaz1ZMRvVTOt6vAwWGxn35wBXEtiBUzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=M4dW7g2R3q1bVrh4_NHh4t8mxWNroxzkW-S649uRZC8UJGkiwazyALd4HMGeVnZwIUkoI4Nj0XSU7UPLpkm_T7hdP4X06S5briI71HZFWDXfDMoC6dKOjhtqY5dgQwsQD_y6UmK-2dr2TCdqbCsXUEvrGydI9vV1wwFAlnHZEtWWpGwnK1xdBKrpfTnRAwZfUCHng6jOQjlY61Yts6QxX3LqeyZa1P1RMnsqogX1cEjvXWLakgfhcgrlu0W0wA0CvZnwjVYM5IJlvOG_TeCgHnNEEpgY5mnMfq0nygRkL9qrhh1QJIi6jFZtNwmeJc9loz3d-yxpOc088-QdxnqoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=M4dW7g2R3q1bVrh4_NHh4t8mxWNroxzkW-S649uRZC8UJGkiwazyALd4HMGeVnZwIUkoI4Nj0XSU7UPLpkm_T7hdP4X06S5briI71HZFWDXfDMoC6dKOjhtqY5dgQwsQD_y6UmK-2dr2TCdqbCsXUEvrGydI9vV1wwFAlnHZEtWWpGwnK1xdBKrpfTnRAwZfUCHng6jOQjlY61Yts6QxX3LqeyZa1P1RMnsqogX1cEjvXWLakgfhcgrlu0W0wA0CvZnwjVYM5IJlvOG_TeCgHnNEEpgY5mnMfq0nygRkL9qrhh1QJIi6jFZtNwmeJc9loz3d-yxpOc088-QdxnqoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=KgVXLAzHsz7LuT_dh2cRxPZvyXKbqrpP0sIVdH8J7jx-LEj-t21XyGPzanPNSVami67BFAJtg6GcU_JOnodUHH3vHVy6SN7-S568zUfI4BSCix5LTwQxUyisn9aQQyOFeajl0nA8C0xkct8pXjlFFjYmeN9MxsPAN6Y9ZK_RGv71ea3fudIk2aRUgvk2LBFgha6cttr-9veiV-SR0j5T4ETuCb7oaat6bi2mq1AyZFU99n8AWQsuEFfcfvOk-McPiRFUkIGWvvwDTMPMTHCIowO-qx5EpMtr-BWTk83lwoJRTM5o7YmgspgO-UmoADL2B7HwIpjvxBPRUEyPBOtW0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=KgVXLAzHsz7LuT_dh2cRxPZvyXKbqrpP0sIVdH8J7jx-LEj-t21XyGPzanPNSVami67BFAJtg6GcU_JOnodUHH3vHVy6SN7-S568zUfI4BSCix5LTwQxUyisn9aQQyOFeajl0nA8C0xkct8pXjlFFjYmeN9MxsPAN6Y9ZK_RGv71ea3fudIk2aRUgvk2LBFgha6cttr-9veiV-SR0j5T4ETuCb7oaat6bi2mq1AyZFU99n8AWQsuEFfcfvOk-McPiRFUkIGWvvwDTMPMTHCIowO-qx5EpMtr-BWTk83lwoJRTM5o7YmgspgO-UmoADL2B7HwIpjvxBPRUEyPBOtW0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=pvO7wqHM9fmsCLOdHX1gKfyerBVWPwFimkQ95DAa9vHljMk2mEAnUNiQ6bofbMNhMdcwPeQ5ylPks6TQhS9rlyJViPbUS3nIBczFxDuDmDauIQO-egXQAi9ra3_NiNXVcl7pQHYgTsrQitFGKfXivLLn3jP5vvFM1o4prrbTT6XzyAHE9SNdF6wkmFnesKZpHg2xLzp-OogvG8I2fnaVNXGt7pVxTExFhdo98kW1ztCQxdymNvSJ1rMz7YZBOsDNeAhiDNkKhPKEseJziiosB48v04onpMXygpsholekmbO6ThodV4oBdANvKjbkE35DEbHVqn7YAt2XacOSvqyuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=pvO7wqHM9fmsCLOdHX1gKfyerBVWPwFimkQ95DAa9vHljMk2mEAnUNiQ6bofbMNhMdcwPeQ5ylPks6TQhS9rlyJViPbUS3nIBczFxDuDmDauIQO-egXQAi9ra3_NiNXVcl7pQHYgTsrQitFGKfXivLLn3jP5vvFM1o4prrbTT6XzyAHE9SNdF6wkmFnesKZpHg2xLzp-OogvG8I2fnaVNXGt7pVxTExFhdo98kW1ztCQxdymNvSJ1rMz7YZBOsDNeAhiDNkKhPKEseJziiosB48v04onpMXygpsholekmbO6ThodV4oBdANvKjbkE35DEbHVqn7YAt2XacOSvqyuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=cNSDUcQ-DbLJ_bJwZ9QQJhJLVQbKM1sM8hXGLBcgMApCJKhyJnvln6LMw86qRl-8A9aOfDVsqCAxOIouJYBwBELMQE44OWs1g_PFOU1wMxnuqLypgXPLfy3TpoRcfvaqZHx2FFNUcSYo0emzYypqUUGtAbF706NBJKgPt8u2BRhqwWjnAc-yDft0FpfLIfuQSTNcx_U8LKJ-7Hz9PCMB9WaFibEw7pUzkGn7B-xatIu1-1ON3qRHOVBAVQyija5dz43XLQAjn_ck9c57Ie8dNDEKquZptr85dHhqDU8qtP-RGAEtr7RA47U9LdhG91PwpCD1841kHIgYonFIAJWxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=cNSDUcQ-DbLJ_bJwZ9QQJhJLVQbKM1sM8hXGLBcgMApCJKhyJnvln6LMw86qRl-8A9aOfDVsqCAxOIouJYBwBELMQE44OWs1g_PFOU1wMxnuqLypgXPLfy3TpoRcfvaqZHx2FFNUcSYo0emzYypqUUGtAbF706NBJKgPt8u2BRhqwWjnAc-yDft0FpfLIfuQSTNcx_U8LKJ-7Hz9PCMB9WaFibEw7pUzkGn7B-xatIu1-1ON3qRHOVBAVQyija5dz43XLQAjn_ck9c57Ie8dNDEKquZptr85dHhqDU8qtP-RGAEtr7RA47U9LdhG91PwpCD1841kHIgYonFIAJWxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=DBYqId_eWkh5-MUChgXZv6UqvpDKDOpcwOESW-iHEGi0JHhI5W-rIK5_twyxK56X1ptwrr3uQFztcArh8jnM3gnAZxX57XkRFKrYQ_bQkjQWxknEvIeXNSbhuKo29ndiFF1QS_rRjJhxei_PMbfKZIIebyAtOyGC5bOm6H2euENxOnoTnnPXdVx7_e1m5JS4tqe0v5VLCPW_t_SZGh7-rWruBJrqvSrRohpNE5IJdNyrLjVjIV1KaBMkHbISVPUE16Qmo8ZXY5mj83oMe5jLbKRktGC52OQqii56hFEcVB5-pX_whniNiy6hs4lf77DYTOMieYWUE3N-kOsGD63SdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=DBYqId_eWkh5-MUChgXZv6UqvpDKDOpcwOESW-iHEGi0JHhI5W-rIK5_twyxK56X1ptwrr3uQFztcArh8jnM3gnAZxX57XkRFKrYQ_bQkjQWxknEvIeXNSbhuKo29ndiFF1QS_rRjJhxei_PMbfKZIIebyAtOyGC5bOm6H2euENxOnoTnnPXdVx7_e1m5JS4tqe0v5VLCPW_t_SZGh7-rWruBJrqvSrRohpNE5IJdNyrLjVjIV1KaBMkHbISVPUE16Qmo8ZXY5mj83oMe5jLbKRktGC52OQqii56hFEcVB5-pX_whniNiy6hs4lf77DYTOMieYWUE3N-kOsGD63SdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=SaN12zhglUxieX0a7TROXWJ7znIL8ME80PvoqJ1CmhN5gaoHe4EyM1FDpmp9o6uH_vWmySyepsYu89ovfk1HYKR-BFdHmDlNtwpSL2UXe2RqzeCEwbvJZwL1pRGzdjThUPYk9dbBQLBZFI7XaWMXBgDA2GTwBVOmfCEIfvljOro-y8AnFCYTWnWvctRNrP-GguSIogYNrrcKh1HkgIzmFCOjdIczGWO3UINwdYvZSoSu01G4qI3HtmmMIG0JNIeMaN5HLYx4sCpQwPj0lKVNiM2luZiY6CeDY_yEegYGvHeX2WKfWbyeCKg_Ix4W30owXwkkE4ZkeK2E7XPFzIevBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=SaN12zhglUxieX0a7TROXWJ7znIL8ME80PvoqJ1CmhN5gaoHe4EyM1FDpmp9o6uH_vWmySyepsYu89ovfk1HYKR-BFdHmDlNtwpSL2UXe2RqzeCEwbvJZwL1pRGzdjThUPYk9dbBQLBZFI7XaWMXBgDA2GTwBVOmfCEIfvljOro-y8AnFCYTWnWvctRNrP-GguSIogYNrrcKh1HkgIzmFCOjdIczGWO3UINwdYvZSoSu01G4qI3HtmmMIG0JNIeMaN5HLYx4sCpQwPj0lKVNiM2luZiY6CeDY_yEegYGvHeX2WKfWbyeCKg_Ix4W30owXwkkE4ZkeK2E7XPFzIevBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=dyigUlSZsd9QCi_hEwEEISOzCVk2h9tqEEGZjb3Lq-ru5ZBTX1oSM6xHUqbVvPpXRF1zUwhvaNH-8QyeeaXDiA_jLAXjpLMuHcJ2U3dw0He_ZO0-qjV91kxGubaSvCjKaT0ElwCzz_Fe0Uv9r5aeGCmfoxeAwVvTnazA8fN-KjLCfnkS2zxA9LA75tjObxHZb4i8MJyKF1fjTGxH-eDtNzrqUTwB1u4DijbjEoffTmiGOYyzgvXGYQ5O5outF0slBDXnxfPNoeRs3GBJfFogUuSpEgYqnv8d8bQ7Nj4wcJ2QN9C-CIV00weI3CQqrjZ9fymxLZaCbwFGm2-SB8zJJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=dyigUlSZsd9QCi_hEwEEISOzCVk2h9tqEEGZjb3Lq-ru5ZBTX1oSM6xHUqbVvPpXRF1zUwhvaNH-8QyeeaXDiA_jLAXjpLMuHcJ2U3dw0He_ZO0-qjV91kxGubaSvCjKaT0ElwCzz_Fe0Uv9r5aeGCmfoxeAwVvTnazA8fN-KjLCfnkS2zxA9LA75tjObxHZb4i8MJyKF1fjTGxH-eDtNzrqUTwB1u4DijbjEoffTmiGOYyzgvXGYQ5O5outF0slBDXnxfPNoeRs3GBJfFogUuSpEgYqnv8d8bQ7Nj4wcJ2QN9C-CIV00weI3CQqrjZ9fymxLZaCbwFGm2-SB8zJJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4umjW3xR9UoutSUPK2NWkMNndDORaehRPJtMWWoputG3uUIZnhV7eY8Od3F4B2W5M7S3qedXAqeA4tyxE9su7ZwKM35U94iQi6_q4Zp6va5oOCVAnumCh3f1aQEd2iKvijOGQen6BB7KSsPiZ22grkSshl9s3cnHzfHo6haWOE_z52NU1x_FBj0a4wDUzAzzRnQK8sirUnGeCffxYYtPFO6v232P72zwkD7xFnu38K3odoEkH4ipg5uIA-ezZWM5iT7MVRd-R22evCEdmHViNyEcu-ocwdNv23l-5up7_9ehW5G342STO1psdzrA-hPCBNbgHXDP5-3rOcJarvSSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=GD4-qOnKWFeyRoCdrS4is8eiGjduyYnryEsyCSMD3omelpYDEUHSSGl1qtyT0G8voWMZ1lYJqpCLJlyf1LXQdXTURZkuUIjugBmMtQjzs-3BNJG-HkRyrd4cqEXYcsT07vd5guWsXWKSPGJ5Ip2rw3XlYuxQxG0xwgq91D3OBROwGwX2PIyVT_N57pA0EA6HnTLvMBLNaQge-zx7wdPWAzsOamAOy3aPVsZB4UjHmCP4PdwhBbX30GUMSi1rpmmN9moChHbaK7Hxwbii1dY1senlOFN8Mb0voZJY85gODYKmVm4QmV7X_86pF1_XJ51ZbkD2FHcvCj7BhjeOtFscJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=GD4-qOnKWFeyRoCdrS4is8eiGjduyYnryEsyCSMD3omelpYDEUHSSGl1qtyT0G8voWMZ1lYJqpCLJlyf1LXQdXTURZkuUIjugBmMtQjzs-3BNJG-HkRyrd4cqEXYcsT07vd5guWsXWKSPGJ5Ip2rw3XlYuxQxG0xwgq91D3OBROwGwX2PIyVT_N57pA0EA6HnTLvMBLNaQge-zx7wdPWAzsOamAOy3aPVsZB4UjHmCP4PdwhBbX30GUMSi1rpmmN9moChHbaK7Hxwbii1dY1senlOFN8Mb0voZJY85gODYKmVm4QmV7X_86pF1_XJ51ZbkD2FHcvCj7BhjeOtFscJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=rYY_D9zjjdKxwNIqifNpg_i6Z11-CTU-ZN7k8oho7Vsh1M1aUWROelityxbo6qMGjGSAQj8yiCXSLgAWAMXy5YQkARmgn8-XwRuCJWyd8k3kTwC_X4QRbqM5wrtf6nr7dq-52Ia13fVgcrB_K1LRDGbE82M_LC4RW1Cu3kXsLfg5SdBcFS5aFnW-p9AotopclXauOLe8iCw1PWfxjqevYfMVKRStiVyK-26rUZeLn8JnIrg7rFzm18ucs2HY_Ba8ZbqvmzY7BZ9AM7iXE3IbR1-Srz1C2kx64M2yXuEkYVo9PEClKFgqkvJ62j4RqIvfam2j8vQi-RtzY7Ztj5Nm5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=rYY_D9zjjdKxwNIqifNpg_i6Z11-CTU-ZN7k8oho7Vsh1M1aUWROelityxbo6qMGjGSAQj8yiCXSLgAWAMXy5YQkARmgn8-XwRuCJWyd8k3kTwC_X4QRbqM5wrtf6nr7dq-52Ia13fVgcrB_K1LRDGbE82M_LC4RW1Cu3kXsLfg5SdBcFS5aFnW-p9AotopclXauOLe8iCw1PWfxjqevYfMVKRStiVyK-26rUZeLn8JnIrg7rFzm18ucs2HY_Ba8ZbqvmzY7BZ9AM7iXE3IbR1-Srz1C2kx64M2yXuEkYVo9PEClKFgqkvJ62j4RqIvfam2j8vQi-RtzY7Ztj5Nm5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yc1qbISVi_lqUyYg0fRKtWQbNTMxpmILIy2gl43OjFYaUovd9jCT5XydAZbeOa1pA4ivfKw_ZvSnPT7iw1dYdQGILhVDLxKbulgXr9N04prwfJHDCVmCevJR5o3k7ovxBMnGsr9PIjukX-NOyzDBjVn_C9mnXR268iY6YYqXLaT_I-YkDyG8Ph4ZdvOE-LT6fEJsuTHA2JSr0o7LfhfPaB2WUu872Xos-kzbmCDbISIAA4Xp3EIzstLwmN5BpSxUBKDRmPGIC93ApcGjwouYBDKnlpY0SJHaehdt8Xp1M0m3P5_5m2o_l0nIdwctU6DDDBcnoa8Rl8NhHOP9ZgCNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzpWb1UgR9wMx62fKT-qWUP4k9dATJTgB5jzOCwW1mxUVltEzBFVED-qn_hGX0vfEGHiybVvldJI-h3qQCdRrlryumck4jUuGTD_cQ05pmpmaiG33i5uMTSoSBeoCik5d6MTqW6HcjoJAk4ZAVxHnX64BqOtOIQCD75Jp0owa1-QUXd_p6sS8hGJsuWg_LjSZgoNkaWMMClzV1OS6GTZtx3fiUjfWww30SdN4O56BanvS_3nmvVISYI-Jd4dQCvs2qM4JONWuGNNDYwDm5FJsf1t0ocTQymIZUtLgsDJl4VKTFcMfutETcnB0imHE5p7Sd3Ujd0e1CH4FuepOVQ-MA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qOmGVf3yRQeXIA_B3vKuLYijn3coZVtvFr3M3Q9Bke9SsC_k2QXergmOqRwYSkfeI_Cgs46VLnTSXcH5cF7BQYki_Gb16m7StA7oKHPmBNO0BRXWuHRnt8mTq_Ffu0wCQEE5PiZGP5MJ2Cyu3mEgAMydk6OHvAHFidKrAv3548WPI6U8CT4TSUfPqdOCJfn2QOz3czF1GH1R1mqpwpg_NK0peU4JIrDKzJiPYBLlMDsSQznM2YT4yNFpkPLQ0RPqODnPvXPAEhOE-enywAQj-8cUcVFQDbzQPU_k3blflIEUGe6oYnLnOVWRv3tMZ_Dh8w3b7lYAl7dr9WVlmY0D0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qOmGVf3yRQeXIA_B3vKuLYijn3coZVtvFr3M3Q9Bke9SsC_k2QXergmOqRwYSkfeI_Cgs46VLnTSXcH5cF7BQYki_Gb16m7StA7oKHPmBNO0BRXWuHRnt8mTq_Ffu0wCQEE5PiZGP5MJ2Cyu3mEgAMydk6OHvAHFidKrAv3548WPI6U8CT4TSUfPqdOCJfn2QOz3czF1GH1R1mqpwpg_NK0peU4JIrDKzJiPYBLlMDsSQznM2YT4yNFpkPLQ0RPqODnPvXPAEhOE-enywAQj-8cUcVFQDbzQPU_k3blflIEUGe6oYnLnOVWRv3tMZ_Dh8w3b7lYAl7dr9WVlmY0D0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvRkN-pWeb45wX8k3_rwEbayGJ7HP0PyVnKXe7ZMILEhA5mlMrcCD82Pkq6XrMG89saZtUMSHBuhyJ1um-xJ1WcD8BAfBtQtfq2uaIWjCCzUnLbqpA_C9Wke2Fg5VkVDhdaZK8TeZ_Kc44ZeDzWjQfYBj5FSonLAxo-I1vQOjr-ODoa_G1pxW28RCqsqiedFLRoNIEe_H1Shl9mHSw22vyX4JTBNYZ-dJoyGdJNnoWvy43UyFTGj1C7P_U22i8siV9NSrVgDJHEAO7crIqMT_M0LOERp4PY5SdE6NoY-DtSwPOfZIFPBLSwNtIRd9T0TcURHY0M9qpOzXNqZhHfPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRkdXUoP9aRu77dfRmmUAytH2HJCMtVgeN-D4NX8axiMagydga6JRjglo4RH5iUjuBdYZ0zJyevOLltrf6k8ED0Uoyp077MAn9NXBS5--vWjMX-pNo9l5B7ZvK-jeDrqojPdQ4UjPNzBNsfJDuxrX7-eWa8BxEtXv0agpQaH48ECkTnvLlc53sqZFXrSX4YSA3aTqEOghSrSjqgBbeWYoT6F1gyg2Ygfq0k8gL0UUZE5HCvWGOdSdC3HHnItIdWnVDkjJJSK2PG2k1jcAIQMucWLV85Kjt7RdjsYLDiAxwoZa8UAVgT0Wk0ssMvlaw8VGw5lPzR3LIV1mc5MQWT90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px8Ot0vJwBEIrhoHe2Z_D_PLTdy3Xlb8Kp14Ie1hnAovo0tptG_ndBjuk3IKCwCJlLWDoZghxzMOYX4g0csaxsmWY45Uf9FPjepFQs7wZGl73YPd-e6RgfID_Zo6m5mnjdDSWSHMMz7IADIeedXeed2V6ys-XpnPMxnewqn1zrMZV1FGYVi_M98LUFI652oVWFVlqaGqj2MAoIduiz70V1qsDS2PCRv6oy4u_CHjI05UBSIB-GuwfHiP-PaWvjLSFgcSqJMSb_rYJVX2sIpnTmdg7IWVt5JTvgp-dZ9vIZneHiooUCaIw5kKy3vUM8lqZG1qzM7INofZgXaxrFZUsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DxgxQv68rRR5VFKchJ12ii_QBWYDrVijxlNryeiMOoa0RM2QbAme3_Jwu4baPFS9yatGImJkCzj-YOi_qjVKT6KY9rN_CZ6B4P31e5x409sI07oc3IxvqPKKttbH9wxRaSdquNHrkSq_hmK9wX2rfBRdrlARksruWlj80REg0Mjje8aBlepH_9q3_H5h0nmywoSEXsFOfmK8pmXnNKXXpZ1yp42rvFyvlbsbnUNU_qPW2-ZapQA2uD7YCHVSikMVXWAMa2iqbkrMegs1fdegmnnHkeZ-YDI8dgDmZgxxHPh7QM_qrFyvOT0D0fHYzeCSMD51qvAxzWsFPfPpG8b3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DxgxQv68rRR5VFKchJ12ii_QBWYDrVijxlNryeiMOoa0RM2QbAme3_Jwu4baPFS9yatGImJkCzj-YOi_qjVKT6KY9rN_CZ6B4P31e5x409sI07oc3IxvqPKKttbH9wxRaSdquNHrkSq_hmK9wX2rfBRdrlARksruWlj80REg0Mjje8aBlepH_9q3_H5h0nmywoSEXsFOfmK8pmXnNKXXpZ1yp42rvFyvlbsbnUNU_qPW2-ZapQA2uD7YCHVSikMVXWAMa2iqbkrMegs1fdegmnnHkeZ-YDI8dgDmZgxxHPh7QM_qrFyvOT0D0fHYzeCSMD51qvAxzWsFPfPpG8b3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QdhY7aWQi2CGhfXv9Ngilga8KqEcpWxhtmffqK8ko1NrcdRtx194pS2hXIdURluIf93LrApl61LpBsOVQqKsdomZux92Y4VukFCraOvuA75upmCv38jwOYcg6z3T5G2wnRaXf4AjPbYXe_W3aw9r6h0SXFTjUDxlcE5ChQIE6C1yOYCavkjy6uWkS2PqcdypLhDE46NlAv5iw2wABg8-Hc4A_KjH_WCz2rCHCJa7TQBfa-Tf__IeyOqfe6s3IFmhUDagUo75KuXJ_SwmzlFuNqEwsmPn7c5ery_edVCZM5zjnotz85WT17hPjcoR2EX8daQgvlVW97ye-H9lDVxfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=QdhY7aWQi2CGhfXv9Ngilga8KqEcpWxhtmffqK8ko1NrcdRtx194pS2hXIdURluIf93LrApl61LpBsOVQqKsdomZux92Y4VukFCraOvuA75upmCv38jwOYcg6z3T5G2wnRaXf4AjPbYXe_W3aw9r6h0SXFTjUDxlcE5ChQIE6C1yOYCavkjy6uWkS2PqcdypLhDE46NlAv5iw2wABg8-Hc4A_KjH_WCz2rCHCJa7TQBfa-Tf__IeyOqfe6s3IFmhUDagUo75KuXJ_SwmzlFuNqEwsmPn7c5ery_edVCZM5zjnotz85WT17hPjcoR2EX8daQgvlVW97ye-H9lDVxfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cewZAPiQJdlFBDyChO9tsKPfQJGIbSWjzt_eVUPreuhqosemWhGnhr3vOO7HDMfphRgIfxP6SFL8IK-3gGUjadFEa6LB5XW3PmSeM6CZTP9jS2ljl0pX-Jnr5nqLzRqZdBaTE6VoFmg06oLQ4Yuk9cY72FJ1T8smaSOTs0pLLSGwp6u3mmNR_TnmgRmUnSoFn5yoI5AAL9NFwRGJVlfrbrOxIv8xgdN7h6RoYtSoDkj8B63Jaz3yTAlP72_cK4BIX7E_f2_paAHmzpw_Ttqk3XbmKcZFX2TqDQLn1Foxs3AlKcGJQBE6r26VVSJkgE7wV2KH6N9hgkb_Y_OdAbjcpr8AISVEzGFkbcx82Ir8G0vs7LxqkdRaq6QvI4fJf4nq_CLB0AWmzAPny-LXGcCuTTrZsc609lmNjewG8MsCfAG0X32ctCjDnUwMNa3vc0dyj-gmATbA10swz5-WJWFx0Hbl-Sm1n-ZwIHz1ka52HivQY4ukXZVyH7PS7F04J73WK7aNwRTgPdeNNgiuClgLdY-NqS6qXprYHgNXRaULhjgz266eA60LvRdrZOU0PFmEO_AJ0EUCwwjtGChsXDW-_TsbxcEbVaGtpX4a5MIU6nIFnLrKFlAmn2MBFJPRi40SZwO-f-uY9NFZH__Z8379vao-dp-AUgfofTQ9xRfKl5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cewZAPiQJdlFBDyChO9tsKPfQJGIbSWjzt_eVUPreuhqosemWhGnhr3vOO7HDMfphRgIfxP6SFL8IK-3gGUjadFEa6LB5XW3PmSeM6CZTP9jS2ljl0pX-Jnr5nqLzRqZdBaTE6VoFmg06oLQ4Yuk9cY72FJ1T8smaSOTs0pLLSGwp6u3mmNR_TnmgRmUnSoFn5yoI5AAL9NFwRGJVlfrbrOxIv8xgdN7h6RoYtSoDkj8B63Jaz3yTAlP72_cK4BIX7E_f2_paAHmzpw_Ttqk3XbmKcZFX2TqDQLn1Foxs3AlKcGJQBE6r26VVSJkgE7wV2KH6N9hgkb_Y_OdAbjcpr8AISVEzGFkbcx82Ir8G0vs7LxqkdRaq6QvI4fJf4nq_CLB0AWmzAPny-LXGcCuTTrZsc609lmNjewG8MsCfAG0X32ctCjDnUwMNa3vc0dyj-gmATbA10swz5-WJWFx0Hbl-Sm1n-ZwIHz1ka52HivQY4ukXZVyH7PS7F04J73WK7aNwRTgPdeNNgiuClgLdY-NqS6qXprYHgNXRaULhjgz266eA60LvRdrZOU0PFmEO_AJ0EUCwwjtGChsXDW-_TsbxcEbVaGtpX4a5MIU6nIFnLrKFlAmn2MBFJPRi40SZwO-f-uY9NFZH__Z8379vao-dp-AUgfofTQ9xRfKl5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=A-5pI22k2YQZO13GjXUyr5SVaLyZRy2f6A1UgX4k93CyZy-chBtsb9nltWPKMDhWbvDt04E5CcKUjbALsSg2RcB5H1kR5hWUdSCgNi5duKI6gEl51ziDgYGn4fteybG2VlzYzWO__zG6_ws8Gh7jxHq3PcqLwhnulU_C-nb8b4xJzyG3m7HJ6pTf1KZPpvd47Znj__FzeRHPrSxKTgtjq9zovy9qM_pZqxc9XLvDGijTmtqAWWahnh4dhugg-8g5oAlMRVpPIXzQBe2uNB-vNpmtdqG0sQ57MXwBkbPGcQ_UVqXSjDhvKigQgVKt0XsIYaecrrrlTUIHhbgNbRVivXmdqaJigMTKQsucVm1c1sgtu_QxBCJp4iBoUlGvMn3QxyeF0NWmHvOeRubSrdqR_4Q7p8KxCHFlPvchyiEpCe3cWUWejZr90ITFRPhbY5qniYo7ToYYiGYEN3vEP6oqgFpaj4X3WToFiIQ4X7hWw2X4PJ--P7-FeRe87xWe4kmForhyIW0KCsGOxmieHM-j2pfpquUqy2Rl0HE4axhB_vVU6uVwfInUVABqsQ_XXqUg9FlOAcj2qFuUYzOlb_8f3WsF6dUz-ZBTHif0j8Ncd_HZgLwo_uahL-Nu4bhB-fUJGcKuT8e5H5k2xt1ul5Qr3KvoiT1nKRc4ancilEPWpD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=A-5pI22k2YQZO13GjXUyr5SVaLyZRy2f6A1UgX4k93CyZy-chBtsb9nltWPKMDhWbvDt04E5CcKUjbALsSg2RcB5H1kR5hWUdSCgNi5duKI6gEl51ziDgYGn4fteybG2VlzYzWO__zG6_ws8Gh7jxHq3PcqLwhnulU_C-nb8b4xJzyG3m7HJ6pTf1KZPpvd47Znj__FzeRHPrSxKTgtjq9zovy9qM_pZqxc9XLvDGijTmtqAWWahnh4dhugg-8g5oAlMRVpPIXzQBe2uNB-vNpmtdqG0sQ57MXwBkbPGcQ_UVqXSjDhvKigQgVKt0XsIYaecrrrlTUIHhbgNbRVivXmdqaJigMTKQsucVm1c1sgtu_QxBCJp4iBoUlGvMn3QxyeF0NWmHvOeRubSrdqR_4Q7p8KxCHFlPvchyiEpCe3cWUWejZr90ITFRPhbY5qniYo7ToYYiGYEN3vEP6oqgFpaj4X3WToFiIQ4X7hWw2X4PJ--P7-FeRe87xWe4kmForhyIW0KCsGOxmieHM-j2pfpquUqy2Rl0HE4axhB_vVU6uVwfInUVABqsQ_XXqUg9FlOAcj2qFuUYzOlb_8f3WsF6dUz-ZBTHif0j8Ncd_HZgLwo_uahL-Nu4bhB-fUJGcKuT8e5H5k2xt1ul5Qr3KvoiT1nKRc4ancilEPWpD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=acoV2uHNexkccIs3Feavpjwnpe0qns-uaK3cv_JI4BUWMfPzBZmK9CKbakjKe5kQttE9zPxiZ8NQPXQvZP31PuAjmxfUlZ7amagmnQuCEGBr_D-klw_A-7yCz6rhPdKK3HLjjqb1G65kN1qAQEdBvXfj_sHSAwYz60hI1_bjR7ehutyID0oL1I1wskX3DkRGS1w70fVwGAEOT5PNdhz7RWEafAB28Il8oF9M_8G0u1-uIbIw8m1tsXWrfkjJ5zCfLCY9CrgyfF3Xqy5oIsm60XSzgjzG1tNta9hRYKXAgR8U0RatbZsUE_5gh5yTcIm692ijvXRCZXEEdtzaA9sBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=acoV2uHNexkccIs3Feavpjwnpe0qns-uaK3cv_JI4BUWMfPzBZmK9CKbakjKe5kQttE9zPxiZ8NQPXQvZP31PuAjmxfUlZ7amagmnQuCEGBr_D-klw_A-7yCz6rhPdKK3HLjjqb1G65kN1qAQEdBvXfj_sHSAwYz60hI1_bjR7ehutyID0oL1I1wskX3DkRGS1w70fVwGAEOT5PNdhz7RWEafAB28Il8oF9M_8G0u1-uIbIw8m1tsXWrfkjJ5zCfLCY9CrgyfF3Xqy5oIsm60XSzgjzG1tNta9hRYKXAgR8U0RatbZsUE_5gh5yTcIm692ijvXRCZXEEdtzaA9sBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1NZWVZ2l63rdaXyA9MI_KW-KtA2Hd9OQOCS8PprengmuLA_MKqClFAenF0haoSB8pgJz_yN_VvBUjiNsmr9SkBuhyjL9zoqNYg2MII1epDPE5rnj1DEbxBJn7iSCTRseqz2xZUnVhPI-uiwn6sFAZGR7vuQo2ZIXKa6A4BMuFXaEzlMkDCo8aaLXqWMRcXIjPAX9EqrMk7BQDDW7e7e8VdhEnboUXZ58ptuYlk8Y4Q72Y0rIhqorPhGV_Cj9fKqf6W1ssrMiCw7FqAvknv9u-X24hdgCVVs1OUly87Y6q_J-zCzSzic_iQE2Npbm_W3mzMyQxlaeJODEznvGaPuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Bo5xA8_ntF9u1WxK0jjm2N3vJK-CDUAg22K5Y4BuM6NDWAoGoj60sjLo2X4pACEwY5xgnwhEYQfQd7y52m2a4Azmfd_1E446eEjGDNqxrVSiMgsX8J3n30iPRCjyYpkbo6-1XrRYIQo0cBPKpD41Q_uyCkEXAOMZx1s3qRJBu-1WIgYMnK3neRgtSnw2Tjpl-p0CJb44JR3Rsj_edXBVuEvAvMyIptUZslYHxtlok3uHi1Tyy0Il4yS4laP9yUURy3dmH5U9BPNWkes9xBC0KNqF1hi4BLvcvxpkePEHsMHXgbvwRHUKk43r6lkk0h8TTJVsOnc_HauJ4xrNCgyzmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Bo5xA8_ntF9u1WxK0jjm2N3vJK-CDUAg22K5Y4BuM6NDWAoGoj60sjLo2X4pACEwY5xgnwhEYQfQd7y52m2a4Azmfd_1E446eEjGDNqxrVSiMgsX8J3n30iPRCjyYpkbo6-1XrRYIQo0cBPKpD41Q_uyCkEXAOMZx1s3qRJBu-1WIgYMnK3neRgtSnw2Tjpl-p0CJb44JR3Rsj_edXBVuEvAvMyIptUZslYHxtlok3uHi1Tyy0Il4yS4laP9yUURy3dmH5U9BPNWkes9xBC0KNqF1hi4BLvcvxpkePEHsMHXgbvwRHUKk43r6lkk0h8TTJVsOnc_HauJ4xrNCgyzmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Fw1cE8VFViwBlLp5R6prugfS40uv_YuB3pLGiE1OhSp3p0IUjug0SGuj21w8L81G56iu6cAFx4fbwH6qohLHPg7ft36Panb9i7URtaqiaYl8u2xDoV43g_jV8JcgM5LWygmn67CUSLrrFyqfp652Rkj9HH8yvO3lsFe8s2g6LI_zvEsMZNXpJ38imEELcMDNAWejEesuFTNg-AQ8lJSqfy3uhk-iJJPb2nKU2mew2sS6NYYrvu2eOX5R7Rfrz2uUDNgO8ouud6buhc9QV4OBGHXu9L83-66bKg7MXjTpNYz-e4ljFWiCEcyoCS_iV1o9tvSPkYdhdewIYaHZLgG2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Fw1cE8VFViwBlLp5R6prugfS40uv_YuB3pLGiE1OhSp3p0IUjug0SGuj21w8L81G56iu6cAFx4fbwH6qohLHPg7ft36Panb9i7URtaqiaYl8u2xDoV43g_jV8JcgM5LWygmn67CUSLrrFyqfp652Rkj9HH8yvO3lsFe8s2g6LI_zvEsMZNXpJ38imEELcMDNAWejEesuFTNg-AQ8lJSqfy3uhk-iJJPb2nKU2mew2sS6NYYrvu2eOX5R7Rfrz2uUDNgO8ouud6buhc9QV4OBGHXu9L83-66bKg7MXjTpNYz-e4ljFWiCEcyoCS_iV1o9tvSPkYdhdewIYaHZLgG2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzLDd9QThkRgEabDfRdTEY2Qikg2g1Pw4pHs1gRxYchs_ylg3EAh2JWUyFSBKMsjS40rYznwU-7xXZebk1htLVPPEfPDLgwFpvJPJdHMdCzYDCw7q-nDcGcaV5-o6fXZwriaJsWMFVzbm6NWSqVOi0sacK9i-GbD3ebpL5DE5x2c3EKDRXFqIcgPneEuZoofPEXhBiKhEJ8jS2iInLM-FvW-rNyTVkUPPCJvK4Tc4PHnEGFKsb1zDbnZj5QTPFUZK6kRS9N7L0VxNFO32JFy5W31IwVk3afTgQEWVtOhL8RToHGN1Ap-L6w2-F59CUUO1vZuScUv8BjynXGXdjpj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJETnNZgK0qr7kPcyOwPIorKAeBE6XNek5QlEP7MZUEKzBmRg4JGhEvVjsaUJIx-CEywQ55iNYZb5-5qaXR7EwtpQH1tFPUOLP___MoF0IV2w4hiBHSx6srWrtF5r4aPgzd9nUwSNM127pBQOxKg6A8R2B4iP75D4rVb6pPqJCBSmXJ3yZqcJ7ETHv-YNH3HD-aVkcNNy3HLB8D9c-_huNihyvWMNxYA-KCyLz1i3T4PUal6uv4SF6EeGkAe1yYZ93DBCSkyd5YGttrEzjnHlARqouwhc8Ey0xPNUrHupTPf4-fn2wBdkZFSzzeY6kmX9dln-mNkWB45pY4NSZM0OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3h4nAtIpKSosuGWKKZhifgagK1yh8NubgvOK2m8G8E4fh_d7hYX7HCerG_Ly1P5kqpgo2mqZ9yc-tPlU6egh3hqiKIrb8zgu8vtDppZ3sk8cAg4Prmhv3iPf9VPgCeACHh6b0dtRbtTrO-XQBWv8w9BL2ev51nluJ_xCZXWgVfjoN6RysLxuAdRmLAW_GCJnU2klf8zuuLa-MaWGaZpXV-Eo5n-NIm_VWnPv9rbqLJbevgPrXV_-qfKxIpbiYeHUBwCPQnrCJ_ZV7onh7QyfGyT5MrZZDmDzIlIV4IyWdCE1VO5cF8wdpMKaOO3foz8BW3rqZs4A99IsEZYOwcEuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4UsNgiM3XqTZbsTiqv9XlepieLSFbndBpGsd0sYLPAF1xTFUgBhJaUA6X8DCacC4jmrNTAo3Z4twSHNMh3nB77MQcFGKgcUOD8A-uaX0-RKgjUllNJUYzU7SANfsQksFucg3G2Nzb1xcgpHYRvQv4R7n86nvxSPqKj3N1UFKI-5NnJFLHcHaLc4kYr6e-SmFFpANUbhU94OTTQfibEQQ37oculsOOgRK6rz-e-R2fCc7vXT_jvM5dMkXcvyyXb9BBSKV1k7Vn7-ddn4FsB8wSzBIUBT3CtA4s_xNjwGCCEypIql_Ak6Roc1lF34pPYHLyBjG9_RUDUUEbkg5GP3DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScNa4ROG2IbifbIQ8zTspqYdPe0b5o6gyNR_VSLRHXOcBaz9lRvKfzDMbtSLawBDNOQW8r8joekMddtZgHeVDxRa-PGya_8yprHQh0GOOgEEb8yXOu1T-h2GHQZqEWrJQRxeo04xqiVAVjGznis_eMn-NWcwGRHvHWGf6E6xHttCxUvdhhnIYXDWNBq8-M3KmGdDyeh7MiaAfF5tkXqEfHNO_5jJJJ7pVnLceGKR4lRvAwtq3y4D1qmhIwpbQkeFnMund90rfPMbERSCCtnBCPaPTDalXid0E6mEqPxnG3XbJHXljOrna7Fycx3nzxCAxiX_eggpkFW0O71tYKK3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvXWAZBMP1YNI62kDjJdOAfnNCLOV0VNv8FWQzkXWITBFXyN_N0tIpqzaFCITxc3PYjhquUE7CDWRtiiB7JXAVdP8tjsL7sUy2WtqKwJODKDVE4KiQB6Oju1tJYwjUPQQZqyW4cgOUs1RmA9X-uX8tQncz_7I2andAEH_AaKXskWfjHA1k-d0Kh_g1iGcmdr_YSfzfwjEWJDqWHWdJwhj0OXDxvUE9Z8lRo0UwF9mCzMgJnBaXlkYkL8JOABOV5MOovXS2Gte7saUKWwgX1di_S6HEfd4i62_KgyIHWnG_Y2BacWQjOsXYpfmau30KNL2HaP0bu21CHALBGLx3ILHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYIZcIuw36I24cmB63Y_0pvLj8qY-CVZZYG3a5bsdjqGk_5vZ9T6GATD5dpL57cnwvdi4PbvuEw9tGZra_ppQ1IfgRO-drSz2X-I7S2KCc3gTwYM7Wp-5mG7DVGct9ay09c7JnzCKzeKX33Tdgbt4p6vDWV3ESDPJs_hRGyjLWpwvuUwN_ZVsxvsxuFL-WiWksxnmpKxKRMNyAPYC295WPHmbIQkNBe8LUmKD00R1pEEQqcDhpHncuoBXOGyeG71gQHHzapBMeQhylSTfnCsY3DLyQLtkgLAzW6dY2yd5YMMgULtLBqylTRdsmgM0zbEZg4Ppqxn5AADPMMbsyIkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6MddOwNoGIVQABwhwDm3Al10NXKzy2t69DomW5R8r_TyZ7t2WxXnZYKTMNeZkOaapia_sisnSPinwkgEiT3CSHMLakUNmFUwGu2Of8Bd5z8oPMbDH3JIFfKbjDk1r7v5aVQ3M7l5r5nORenjj90Yy1ZYbiqpmz_zLZH6eCgAQ4cKJM4t4KxkI5-ig7JmkBDmMJe1OUV-Pxem9nIIWyu3Yv1aKRRqHL2x28yVUE2V6MTe0aWQfjzAaCFRGMGJSxMNOj81w454BaJu4SMh6aybpgVgMtguWiVNVk7qhm9DewEMuPOpfD8rT7c6rfMGlGZqIR6SAuMwYrh7wx1UGkmHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3BMDd_3bVcLY9DofdyhQV9H8TXpk71ELYZj10_ZMKZrQaG52IiBSiKmK1xXAkkBIkr1-6iZcYSqpOsZ0-KlT-owpoMtv3opW_E1y6jLjKmuSUfXk4J0nrsr4xfNjBrAkXsrcqr3aA1nsK0kA7WcTBp3y-SGPC95eAKCwaL8UWvLFeWwn6Vh1yU5G3awWR9_UwfKsU4dCSBF3b5wA1F6_F7e0HTiiAeY2Wg78mav4dn3KzeGSPOvePxD9hCCLyBP7hbNieZWYUBvxd8fa0tZpObIS0SuoIQpDVVEo5B94dUxJaIuZ0oO_y6pyuszvRJz081y6x_BEXV6ywqYH0jedA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVUuyZcUiKRfF7sv4q7FsIEuLLiaOKlgGVtBzfz8qBkl8_1qyzpa9djGmtHnfyz0c0JBQapjn-N1rqYrYzt_e7nP_7Wnptf6zFh32Sw2A3tnqTWH1iMHGPsEcRr35nde3hVIQtaeaGEICNUk68UVQwMn0vzenw1_4-aWPNYQ3wPfWMVLcFB4Un4WmLRG7HxEJFW_-FK3J_YHgcK5Ox9wvct_ZkmEkXxVCANHd-C07SK-LV_kdKsSrkTNKb2U2FFMkbwkWR-WhHA4bboo_Mw1nYkmZga4bBMzoUesOCQv7bPweGgIIEzAoH71s9ughOh6jJIvb8ZZt5jeOgnZXTeZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
