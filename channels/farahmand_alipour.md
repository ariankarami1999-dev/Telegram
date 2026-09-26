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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elcHb6yiaUJwvLFRbeFQsgJbActSxfuHDrkteD3bxxT-6_oKthVH84d_6KVb-kTN-3ZIfHcE8EfxZy4RFVnWf5z3I4O0urswAFbBHUKgHj7JFA8G1VVFjbqOWlFTCGPVqFQMRrc7wMzf9emysD_RltengCGxm8PEMqUqas8shVXq319Spz_X05uadiLhPJbvj9FLf8GL2nc-q5_kEVMFpfhD6E7_k62QvPeeTatun4mstv5VRBkFKH3mzi6i-czpLjYjmjNHxj-Wgk5xQQISOY9jc8PIIQr0DrG8-dKNWxvPVh7xEiBlXhOZQsraLtCEPnRR8D-n5kaAW6DZsW7H-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCsCadPeFAnMKETF7kriyXUpwIqf4-mdtiBS78pdpgmNUc6sZ3pshQCHHtKQdtCkScLEs7ST-pG60GsQ6Zs4V5pYGBU3gN2D_646VBc3VYzmfCZ_7qbCegblh1zKr6hoVXuugU5Mal80oq-GrULrkf0Mje8vTDuzunt9AUzqtKs4VwSS9VGqd4LmbjOQNZyN4Ed71jWkbEks9P-H5J1FkGhV77ij8DGtTP2yFZyHwgusvhGejam6oSxxUCLxoLc0mdaPKavsNN2Xk35Z0krW6HlccFhdUaox7zTRY4Wq29yyTJKGRxiITLjQZ4H7pRr5ubCfBIi2CnuWbG4NoemnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id-dheHcdtYht02c-arrytuq_OCJi8VcLv85FGF4J4qcGzJcI1NOeOhwp3qfIhBv67sPZwYEG8qBWC4-zHMa25D4NdQg-SAZSJrVDXFWjIPgkXG_PrgurePMJayI5CJ36RaV3rP7p5O_26eItXLFS_aXRF6m5r5dykUvevjk_ZYBVTEb_An5fHJFKeUcdP_MB7NlSLL_f28lDJIlPIVDVGRAPFLEwCD1LbMT-vGdOwbX2R3Pj5HA5a7P8ftIFYK9I9ktJG9z-B4Tz2fwgmNOjcYlc6a8O74MugNZZHeO9WdjK-_nZ1FadL325HVBsfb8psEa0C4viFfjYg7UjOmskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcHxkj6C72wV43Bq20KAQFohBCWsH5WAQZo4JJWQY1uB330QcfOqa4ZeZ7YeSWrLZyvUJgUjY7Om89ydf3sRy4PQqtpTOkZWoirgFNBa5YqHQ5-JHyjouO0BIpoeIQ19mIJt9rGbMt5z7V49gonQr4iRjPGx8Cn-YFkMAmlYPN8-pvv-Ry5U5ZweR-bP7YgyBSX_Kcn0-qGwDusUSLjb2IAjyiMb47tIuG6K2ZfyfiLih6t8h9vo3GDoDdtfNW_IKBwkFsg2t1azgDJo4P-wROpHlbYTmc3HG1yhgEu1hnnN9VvoCtoDbWELS50kGt7OZWg2W4zABk0eXfnFXnXAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=oF3FAeaixmWo1T9qj5H5E8tmUSwoRqtClQpM8tfz8OsQBnMBQ_tTBYGfUywvj3voXsZxxoW_1DkKLn73jgKOvuWt_UOamh4Xt3zmDYXyHS2e4nnSzVl3j4535lBiyI-xxQFWBeEpwd27oRQqgNxRfS5tbo_OhsMH3mCt28ggU1QPPHmxG2m94sMW-IAUfr_8licUHx21eYbRxhFNIYDbFYtR_5rDUZA363fFctbcTiHL3qunUsUr4MSktBWq4mJ_48IuiR8Di3mfVnq-qVo1M3Z9kk9Rrs6x4SiMdGSWCFbR75GyVPogkGwsixpMmXnQ7gwNgaXl8CETFbvxnAvBE4XOmiXy7NHlh39vBNO0RbpDrrj0II_pUUURrpWspEMuY7j4LGlf6C5_jGU_elUVysbFR-sgCjA-SOV4xXN7L9GRKw1y4GFfpZY8tPicOp9Jwt1cPRJ8dRSEzcrhqL9Dy1MqarWO0HZCHd2mNrs5-pMvfACeBfXjY3VDa1H6KvzbTFOKsEyT-IN3n1O5eYsIWz1-KNVvJJMLYs4NyKPmPGX8A6XZ6mz9HcpYuw16y0HG_CtpbX20PieaVIY_mExTthuIt4vqIcEaMOKWjJiLk80UV3FVcfcT4jUWMuM7h4uKy3JOyp7tF93Q1EdhROSbeCelETmWnEpUSNZRi1Ogo7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=oF3FAeaixmWo1T9qj5H5E8tmUSwoRqtClQpM8tfz8OsQBnMBQ_tTBYGfUywvj3voXsZxxoW_1DkKLn73jgKOvuWt_UOamh4Xt3zmDYXyHS2e4nnSzVl3j4535lBiyI-xxQFWBeEpwd27oRQqgNxRfS5tbo_OhsMH3mCt28ggU1QPPHmxG2m94sMW-IAUfr_8licUHx21eYbRxhFNIYDbFYtR_5rDUZA363fFctbcTiHL3qunUsUr4MSktBWq4mJ_48IuiR8Di3mfVnq-qVo1M3Z9kk9Rrs6x4SiMdGSWCFbR75GyVPogkGwsixpMmXnQ7gwNgaXl8CETFbvxnAvBE4XOmiXy7NHlh39vBNO0RbpDrrj0II_pUUURrpWspEMuY7j4LGlf6C5_jGU_elUVysbFR-sgCjA-SOV4xXN7L9GRKw1y4GFfpZY8tPicOp9Jwt1cPRJ8dRSEzcrhqL9Dy1MqarWO0HZCHd2mNrs5-pMvfACeBfXjY3VDa1H6KvzbTFOKsEyT-IN3n1O5eYsIWz1-KNVvJJMLYs4NyKPmPGX8A6XZ6mz9HcpYuw16y0HG_CtpbX20PieaVIY_mExTthuIt4vqIcEaMOKWjJiLk80UV3FVcfcT4jUWMuM7h4uKy3JOyp7tF93Q1EdhROSbeCelETmWnEpUSNZRi1Ogo7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeTjFhD9bI-DEPvshrsgBvhiIkLwjpHkoaKvtMrvo9hHZrPMTPoSJMprYupZiMnCN_Qa2EUeTECnVsV-OdO37HHWjs3FpoatDk2nHSbZVs5VBzt6tTMIHvUMFZ-lVZ3nFPBknlJIIkPFTHaltDCOTiY6Un-FAZATkGRgL9wgcL_JPzVBB3hesoG6abW0PU9xMsZeznY9AgAvGkESqgugC4BVBHlhg44q8QMD8Cp_lrf-1y44Lx0KpLJAHk_T92EOlpM1DV_iWbqgmZNttDhiGC2YXE27x2D3q3K11R6mcNCCDAoslouPVML5XY2IJpy8fzA56tPk5F39qeo51ED3Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3tP3dvvT0utew6SBQD9dSB1I8-t1SmtiBL5z6TZ--U-kizoCFl_ivGGvAteiSjqk2ll9svTPpJr_junzInCPPjWHk3o-ubhNSnJ3NxtJ9e6aHXahW7ZJ9MDcDaKExdAeZM8xYhsKmOG8M8PoyvIGuUO2RfyTUr29pMFAdOL17wATaojZTgIbA0miUvMHRBDKRawfw_5HEkVKkFM9B_LUEhtAxdXvoP_FbsZHNfDhvAGU8xInJya88z6IINPNgC16sEMGSqv3XfywrGzokVTVz2C5mEOA4DrJu1KthX0NBDyUQY6qubsV2aLWZg-l1IQVDkD9ecM_9nnKumNylyttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bON-0eLMzSZnIy1VrOYNaIU6U_vujWgPJAYtUYEux_8KjnW2SuOvc88ms0yrKWlUfXPWXy_FIDIPWIH8K-K_FO0T132x-m45eTRi3DUggwJDvP3q1kMsWxLXYGGvHkLzRLLx9UIMV071u06vegxWmpFDHv4bev6SSob7SKb-jTOFcuBY08W1erbRUxeByDPunJdXO4CQfrQrj35Qr8aJ_dnz2-0NgTvtajgaZ5NP6borUY0prcTcsFI-2BbMeKlTg7JQu3K175dQpN8Cf97sPfpU5GEO4woajO1C-uzbAgZlpQqMHzhu5ngmHXKx7Dhl2mKnA_7eM8UXvEZ_vuK_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A31F_AH7WQ6h2epAfztP7UA8d0F7J7pc1Sb3BA_U-9wr0Y6d-ZigwJV0cO_hbNAz0vyN-DEoj5YhTXwa2LdAuqOLnHGZbweRHmrNf7QzSoLYGKZpIBdimKCq3hOkLnuXpSpWjD3CpzevcAisfGsQ9FhU9_L3JRuYph6RHF6q06GoPGXJptjBcOB8xZsglVBlAOP_6qA4fnVSVj9FDeGgy2t2gMe2dmrauqNFnfM8lyCsxpTrWyeO-iHbYz9Alf6K4JJRz2Uryk3ICF-utO8fckIexTCAH_dbFRB0mSo7vEHwBN-M1GFhDwHsYUtrx8eCXz7XR8EACrpGENSzrck2Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kzr3dd0gcDFQAyjvABGsMEWNeKSxuxUSjBU5qR4tTInxH_3kGH5tUb-F3uQ_bvRxqquf0_ViwS4OJW-KtwlZGwt7hk64J1n22F1E_d1pDXmPai5ZoPjA741XrBKaiOgwRoEwVduRwosKSzDBQlvZUAuDbTloxnKBklRUwVCTjUEUYx1KGAEkFMlEyCTyNuSin7FVPZATui95ZAvFhJMhVHOWyE8AcrA53LQF3m9mkUyXysmLG2eAcIeoCLhtsFz9Vrn0g2qIbRr3lAVhWqPevcBxP459CxLuSElB6Cu1FtEzbzYC1Y4t7pws-qkSRncCj261POIJxtSGd9LLxvdMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3n4UK1weZBxEcqN0f-rEQXS2_R6WwixYNIT_TeEBru7-uX90Rd0zObvroXS_q1ijMQlQcwVv2OD8032vkE5qC941rr6nAo8r48vh1R6_p29hnsbRktRn4nmLCTLFfb0V7ppE6oBxcIRu3Ht7gAWv18B-gSIWCCBjNc6E9uA_XWsURm-pRfpLA4_bJAAEjad15ZlSivrHCIz34Wmg7677E5QOkAeylXC0FeumqbXS-qmDtqXq4P30OnOMdwASlIE9g3MbJ2oCApCTwQSbBlyjth3Z9GY2HsTP4U1u9yxRAOwUWFSStofezguNWyhQNCVerrRM-QrntsA9ESL5xqVvk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3n4UK1weZBxEcqN0f-rEQXS2_R6WwixYNIT_TeEBru7-uX90Rd0zObvroXS_q1ijMQlQcwVv2OD8032vkE5qC941rr6nAo8r48vh1R6_p29hnsbRktRn4nmLCTLFfb0V7ppE6oBxcIRu3Ht7gAWv18B-gSIWCCBjNc6E9uA_XWsURm-pRfpLA4_bJAAEjad15ZlSivrHCIz34Wmg7677E5QOkAeylXC0FeumqbXS-qmDtqXq4P30OnOMdwASlIE9g3MbJ2oCApCTwQSbBlyjth3Z9GY2HsTP4U1u9yxRAOwUWFSStofezguNWyhQNCVerrRM-QrntsA9ESL5xqVvk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=RmG0qbsc754TZ4y4odXjWTIk4NWSp1YtsIQkVOEzX48zW3t0i4fbRy_kALToosMTh1ilpcpVaLwa5SDOK49AeNZsjSfS_bYTIyYMdENfx_uI24EfIBNBEuZPdUnRrDyBBQD1KejD7ZUiZe8Qo5M9G3xXiSyHsGbR3uwciNqynFRIGue5mFhzSoSmSf1h3gjr8hY9I161iA5V52BZcOhxIP3552n2CwLrZDlCv9In3lAnPJzvgLvnXuTTylevUFXjbYe4KOteWKasQmtcMUSP7e8yY_LZ3h0rDIYPC5bu7--MG7X7--fkzDEaSOLw28hA8AhHCnC_bqHQ0sIioxStUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=RmG0qbsc754TZ4y4odXjWTIk4NWSp1YtsIQkVOEzX48zW3t0i4fbRy_kALToosMTh1ilpcpVaLwa5SDOK49AeNZsjSfS_bYTIyYMdENfx_uI24EfIBNBEuZPdUnRrDyBBQD1KejD7ZUiZe8Qo5M9G3xXiSyHsGbR3uwciNqynFRIGue5mFhzSoSmSf1h3gjr8hY9I161iA5V52BZcOhxIP3552n2CwLrZDlCv9In3lAnPJzvgLvnXuTTylevUFXjbYe4KOteWKasQmtcMUSP7e8yY_LZ3h0rDIYPC5bu7--MG7X7--fkzDEaSOLw28hA8AhHCnC_bqHQ0sIioxStUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=D1vSJm2lSg1-ejVqJpGk-JEA2YreVNQPjM9YJtU6l-B_3bfB8PPSiuLpKcC6GMdaU2pl81avXNrL2LaiEUmipLLkiomF8MZttOJrCGFY6XA4IMjtDufL-AhUgt2nRjV-BkXG4D8h-cNh7hi2K4bfh0GhFZ3a53pqPVYB1UlG4kN2SZxGtBCng9jYepY4h0megeXwefMUxU8wPB5GMJ8TUKMGlSKWOvffEJ_BhgLrCrsj4lGiTqhWjDW-hjqOPwIg2ttphQanImF9RMPgBBJwBXVoMn9CztqsRIOhqx7YASJ5QQT0rUlYfQ1qTztBp7zyzVKVDGY7Cp_yO9f9x77uJGMMctD0oY10uubP02BE3mDOAT0HzTwvXFWWMC9TrbyUMioiBbqvE-ife7Vb8tjd0J1urJLjyW-ECXhCwku-grGS2CKXgvE02UjicYszOi2GbKSbJP_omu9t14oaTfUI33QzdX_fTVjdS8k4zzDIDK1scjUS4jsMY8ZdmDW0ZkSNmUsGKT_5v8rpgZbeFKTv91uyD2Kj8XuTzLe68-dTKR9qCvO13vmAd0arJq45k9xJckQ6vGnXa0tXRhYG3-AHQuQDGwYPIJw5ObcnzVx02ueZAya_zvHblbK7UzVvCkEUIobkB0jnsxHJyH1SvDSgQJmXaRLCuOOUtAcRz5aJJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=D1vSJm2lSg1-ejVqJpGk-JEA2YreVNQPjM9YJtU6l-B_3bfB8PPSiuLpKcC6GMdaU2pl81avXNrL2LaiEUmipLLkiomF8MZttOJrCGFY6XA4IMjtDufL-AhUgt2nRjV-BkXG4D8h-cNh7hi2K4bfh0GhFZ3a53pqPVYB1UlG4kN2SZxGtBCng9jYepY4h0megeXwefMUxU8wPB5GMJ8TUKMGlSKWOvffEJ_BhgLrCrsj4lGiTqhWjDW-hjqOPwIg2ttphQanImF9RMPgBBJwBXVoMn9CztqsRIOhqx7YASJ5QQT0rUlYfQ1qTztBp7zyzVKVDGY7Cp_yO9f9x77uJGMMctD0oY10uubP02BE3mDOAT0HzTwvXFWWMC9TrbyUMioiBbqvE-ife7Vb8tjd0J1urJLjyW-ECXhCwku-grGS2CKXgvE02UjicYszOi2GbKSbJP_omu9t14oaTfUI33QzdX_fTVjdS8k4zzDIDK1scjUS4jsMY8ZdmDW0ZkSNmUsGKT_5v8rpgZbeFKTv91uyD2Kj8XuTzLe68-dTKR9qCvO13vmAd0arJq45k9xJckQ6vGnXa0tXRhYG3-AHQuQDGwYPIJw5ObcnzVx02ueZAya_zvHblbK7UzVvCkEUIobkB0jnsxHJyH1SvDSgQJmXaRLCuOOUtAcRz5aJJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=tqwLOCK2Iw4KzU1LGDtMvbhf3oTJaoDRYnzVcy2ny8vn7XUCPSo7rzrD-BP60W9lXl0UclqxbR7qL3bMqhfMtSUInOw86XP2kc1_Ww0G-szNCMSTidRkOzuuuwR4D_81PR0JtT3fVm3prKt51hJjSZOklZeJe-HYwyz35uEbAY8dAyZj89SUlxQ3gXiElR_wXnVM0EBPVU7Aai5L7mfqdql6ODBcaV2JsF9EjgqnOELm_mHbDq5ms-VbhSpUhEaYUXHOXS0ubj83ChZjtQqmWi_rC8JM3Fl5lptSWGijSiLb48zqM-7cl0C7GW82hJ13pEcntWCJvagKB1GJzZpFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=tqwLOCK2Iw4KzU1LGDtMvbhf3oTJaoDRYnzVcy2ny8vn7XUCPSo7rzrD-BP60W9lXl0UclqxbR7qL3bMqhfMtSUInOw86XP2kc1_Ww0G-szNCMSTidRkOzuuuwR4D_81PR0JtT3fVm3prKt51hJjSZOklZeJe-HYwyz35uEbAY8dAyZj89SUlxQ3gXiElR_wXnVM0EBPVU7Aai5L7mfqdql6ODBcaV2JsF9EjgqnOELm_mHbDq5ms-VbhSpUhEaYUXHOXS0ubj83ChZjtQqmWi_rC8JM3Fl5lptSWGijSiLb48zqM-7cl0C7GW82hJ13pEcntWCJvagKB1GJzZpFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUb4OWjlbDGBg-1QgYUMtMVPw1JX1IX4xPxaC0NEij4BBQcmtzf2d0Zl_49q1XJDE7C0QysptFdHGYeRw4NHC1jN6NXyEjoL_qGq_itG7yKT92MPmzV-yInCPNrmUlfHSeVynUngj3aI6K-mJnVPxZuDXLKOaPUJhejALLoykRFf9P-MrfbvdMdKSOLqQ6nmNclsEnRrXq3-zkilGnyShiEeNQy7WhGIulDj5fz1DUJ0RJUMb9XrcI_gup5CD3oHTtgCXJIUvuzLnbo0rOrl3h4bvbd6t9Yfzl54HxyNWk_V0_YeLqcRGo4M9E0Hyi5XFaCfsDCRFfWBu82KpgyTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=DkGFu1nwOvg8bB8ODrUAjkJey3d9MvrFKBNk1UcUoIHhlxrRuyj_koUoOmFSu9LkIzb1VXux6wpgF6War9FE28xiP2LTvCBbk9ea-aFJ7yqu9LoyW4ziNMeqohRwFttuP31obgGc1mQCRw7m9hznqZeS2z_BL9IK2l823Of66YkVCZGZB6Xvn63gc0zltYZ9r_aiOWMeHRV8-Z0HYj_YgiQpMk7V8APmZ0hJdh9D7RKRZkWklIh4ZQ1Z888dY-R6-LLZ7kmQWXxZKFUdE3J7sac8-ZCZQrDBQHhvLXwSK8ZZIvmU4g8d9BiN-3i5YK0Xi62c3b5GuY0PCNXk5YrrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=DkGFu1nwOvg8bB8ODrUAjkJey3d9MvrFKBNk1UcUoIHhlxrRuyj_koUoOmFSu9LkIzb1VXux6wpgF6War9FE28xiP2LTvCBbk9ea-aFJ7yqu9LoyW4ziNMeqohRwFttuP31obgGc1mQCRw7m9hznqZeS2z_BL9IK2l823Of66YkVCZGZB6Xvn63gc0zltYZ9r_aiOWMeHRV8-Z0HYj_YgiQpMk7V8APmZ0hJdh9D7RKRZkWklIh4ZQ1Z888dY-R6-LLZ7kmQWXxZKFUdE3J7sac8-ZCZQrDBQHhvLXwSK8ZZIvmU4g8d9BiN-3i5YK0Xi62c3b5GuY0PCNXk5YrrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=dyMACpesbkfP3BH-tgeLUgiUMsuwgLHqtXXkR3LwFVnvKVmkWMGwZeR32TczTxM2uSI6NT4tnnhx1uIQu0oOVlMU42i8aajBi8Qodu4I5F_OsEzrteUF9-K9f4VasWe79PoFUvpKz0VdUCpHwxYyCFUZx3fyXbnkuzli2mjOvvUdyQVsPTJW0YSGZkhqDiOm3GpPJpSqoW7y7YOxNttF2-TKxjy0aBV8djWld237WgrURk99nvreI_2KLo_x0Zm30LW2o-DhJ5Q75zSejTU5ElejJzPuqj7UUEZdEvKDsqMLcKxOg3_X8clrQnXdoiLT1p2F-KSsSOLmLPyc2908LihYNgZWWwNX2wfLMRzX4VVauRK1vhoengFUjaFs0N-MyBg_wq8YuBByBVl9qOksA67SklFWUKXtNS8JAD2SfmChqvWqGpJsvGkmliio3ZA5pFHECcAzwCi7q3WqsrlEb-9ShbwvAxrYl2CHkY76_7duA3BVB4i4ttRSnZMX69NhVK_xuZxZuwPytZIT61j7fXEBqVmJV7ehdta3EuPT6FnhK-5SBXvgU8XJOeTvvU_rWHAboJfd-O4GCSv193nrzxM1Yx9eluNAiwQ9LM8MeuH_H6O6PJ00rx7oedfFZpzopItRFxA55zpSv4hbv1HYKPQXH0hMp0qdMVG-iY-GDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=dyMACpesbkfP3BH-tgeLUgiUMsuwgLHqtXXkR3LwFVnvKVmkWMGwZeR32TczTxM2uSI6NT4tnnhx1uIQu0oOVlMU42i8aajBi8Qodu4I5F_OsEzrteUF9-K9f4VasWe79PoFUvpKz0VdUCpHwxYyCFUZx3fyXbnkuzli2mjOvvUdyQVsPTJW0YSGZkhqDiOm3GpPJpSqoW7y7YOxNttF2-TKxjy0aBV8djWld237WgrURk99nvreI_2KLo_x0Zm30LW2o-DhJ5Q75zSejTU5ElejJzPuqj7UUEZdEvKDsqMLcKxOg3_X8clrQnXdoiLT1p2F-KSsSOLmLPyc2908LihYNgZWWwNX2wfLMRzX4VVauRK1vhoengFUjaFs0N-MyBg_wq8YuBByBVl9qOksA67SklFWUKXtNS8JAD2SfmChqvWqGpJsvGkmliio3ZA5pFHECcAzwCi7q3WqsrlEb-9ShbwvAxrYl2CHkY76_7duA3BVB4i4ttRSnZMX69NhVK_xuZxZuwPytZIT61j7fXEBqVmJV7ehdta3EuPT6FnhK-5SBXvgU8XJOeTvvU_rWHAboJfd-O4GCSv193nrzxM1Yx9eluNAiwQ9LM8MeuH_H6O6PJ00rx7oedfFZpzopItRFxA55zpSv4hbv1HYKPQXH0hMp0qdMVG-iY-GDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzFF2Vkh5voRvFAKNLFuzip7dddjTAvGaJe8WjXyRw9IPXJpwW3J4xOJ0MC4bJx5quIs5xXdeoppYFkVt6J68A1hTz55DUu_Vh6rk7ZvcX2IT2v46bvoDWRGYNBXct-yf2MpgK2rnclgnc9b8M5AN6kswlTRg1TilEptYougpVyyPFSZRwz4v9VHBooEwUFxPWwJOsFTGm9uYgf_ic8D-qA1iz56S2q6pSFO6kk514L2wSNX_cSTHYAV96J-0E13R2i3hyFxkc-HBjcOOs_UdrgYSj0OHOz8BYhYRMBPnUWLyChN4G4NA1UywpcDvoYqdXy_3QzNmj33ivv70-76Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=eVYXpwv8L7m-cTZtUgcXaDDGBaxKnTXre3BJLhNsKfvmouj2gU-TE79jHx1k46VCw0tpqnHDEvwB1qNy4pDfVMB_fB0RWv2QmLPLCjV3lyEoCCqWMUAFES4UPYdiZbn52fcm8u85I_WsTlE7PutDqnjPAdmhyZKsF0RD07KfT9RNBibSA1sMQvRjGqHU4HbtWnpvswbnOqAkWeTkP3BVbTQKMOMoYXmLgq8eZAueO47tvYEq0eVaOal_MbMxHu7uoFptZEBFM6d2YI_srRf5xlR3PsVb4S__2krJhJrZOORjCDRdn5lIhUaPui4c2mDLEhUwH4RjYew_A5Z1NspKxRXeoMCyTjrNk6Gsh_E3axEFqvBSL09OoyQCMpP6Hzg8pLTEJylrfZP7PyEucIvB6sD0gIAQfkzG0ZIVrsHQrAEKmEIFkwV1CbSw0ZLJG2diRpfRdWqEzSh2En_D8nqqQG4UPDooZk43K0gMBo2GVF9zF1bMMOj1l96THn66bSD5CbB5JlaWto4uiH14TQknD5JEOFH-OM62zdYWuFo28hd3hshXL2TVDZ19pzxgKC42diIeQMZoh_kxL04k9SRWIp_MRRr2JCMWhOghjYGP1xamC-s6hXs7y8mpfwc8v5zViw6qfWUdZbAhn4-o9QpEVin26s6FUGR7ob1gFx-Olng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=eVYXpwv8L7m-cTZtUgcXaDDGBaxKnTXre3BJLhNsKfvmouj2gU-TE79jHx1k46VCw0tpqnHDEvwB1qNy4pDfVMB_fB0RWv2QmLPLCjV3lyEoCCqWMUAFES4UPYdiZbn52fcm8u85I_WsTlE7PutDqnjPAdmhyZKsF0RD07KfT9RNBibSA1sMQvRjGqHU4HbtWnpvswbnOqAkWeTkP3BVbTQKMOMoYXmLgq8eZAueO47tvYEq0eVaOal_MbMxHu7uoFptZEBFM6d2YI_srRf5xlR3PsVb4S__2krJhJrZOORjCDRdn5lIhUaPui4c2mDLEhUwH4RjYew_A5Z1NspKxRXeoMCyTjrNk6Gsh_E3axEFqvBSL09OoyQCMpP6Hzg8pLTEJylrfZP7PyEucIvB6sD0gIAQfkzG0ZIVrsHQrAEKmEIFkwV1CbSw0ZLJG2diRpfRdWqEzSh2En_D8nqqQG4UPDooZk43K0gMBo2GVF9zF1bMMOj1l96THn66bSD5CbB5JlaWto4uiH14TQknD5JEOFH-OM62zdYWuFo28hd3hshXL2TVDZ19pzxgKC42diIeQMZoh_kxL04k9SRWIp_MRRr2JCMWhOghjYGP1xamC-s6hXs7y8mpfwc8v5zViw6qfWUdZbAhn4-o9QpEVin26s6FUGR7ob1gFx-Olng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=A_wsLQDiD9x9yAqjrodTU1EHw4r6tKmxZUagar6rpxK5BlK6_UJGJ8WZxejrUdpULmUb9xMQ6BGbETBjDaZkTS3KOUxMCsUWgvVVtFAYBw0iCa5iBCIkg-HTYNtYr2PS3V-cumKb4imTjzRFNKtGsYKwt5VczU-WSO1VORr9qSHsiBCxujA7wMWLPOFAuGK5V8MzaIzCrDUiEc2DKlXKi41UfZWzNUlruWeasir_v40qBuLTaG8F7h82F0zfKGXemX-okpoSK01s9NQGmWdyeDWTH6mIPZVF5TjZyo1ECRt0vu8Nnn0bBXBBgBrn-IZ-xg63LEAvQyeEpC8v-yE2kT2EDHPrZgtKTsvqijd-pJgqV-7ulhRnUYq5T4DlOPjuK6TaWo5oyqE2993SEOdfsFzTALzOrQwvj3frErpdAZ7ubmkREeXvvpE62Pg6hCRPsH1d6xk0vbpY3gZ6sdyqQ-MZ02NXV5lrPmZcPEZhhWvRqbdmq9_9Ypz7NYQDtj5jlYuH1U_xfmrKtxoHH5pDbfoXHML18CcQQduBtEVJXXD5xUqVsBNCoyKHGXp74TLDPol90zprE1hcKctYZSo0RxhHtRHWNwyK5LZvfBkgB4j5mqnPFGtyom6FjfegpbHCv3neRD5bhd0zOzHb7Jl-sW90wJA078ZOUx38MT7Wk80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=A_wsLQDiD9x9yAqjrodTU1EHw4r6tKmxZUagar6rpxK5BlK6_UJGJ8WZxejrUdpULmUb9xMQ6BGbETBjDaZkTS3KOUxMCsUWgvVVtFAYBw0iCa5iBCIkg-HTYNtYr2PS3V-cumKb4imTjzRFNKtGsYKwt5VczU-WSO1VORr9qSHsiBCxujA7wMWLPOFAuGK5V8MzaIzCrDUiEc2DKlXKi41UfZWzNUlruWeasir_v40qBuLTaG8F7h82F0zfKGXemX-okpoSK01s9NQGmWdyeDWTH6mIPZVF5TjZyo1ECRt0vu8Nnn0bBXBBgBrn-IZ-xg63LEAvQyeEpC8v-yE2kT2EDHPrZgtKTsvqijd-pJgqV-7ulhRnUYq5T4DlOPjuK6TaWo5oyqE2993SEOdfsFzTALzOrQwvj3frErpdAZ7ubmkREeXvvpE62Pg6hCRPsH1d6xk0vbpY3gZ6sdyqQ-MZ02NXV5lrPmZcPEZhhWvRqbdmq9_9Ypz7NYQDtj5jlYuH1U_xfmrKtxoHH5pDbfoXHML18CcQQduBtEVJXXD5xUqVsBNCoyKHGXp74TLDPol90zprE1hcKctYZSo0RxhHtRHWNwyK5LZvfBkgB4j5mqnPFGtyom6FjfegpbHCv3neRD5bhd0zOzHb7Jl-sW90wJA078ZOUx38MT7Wk80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=rorU07Bef6PTNPrt3siWuTvgK2R7XQDE-CYv0HcPnRe8jij-lUv1PfwUBqMvZn-gSXC_tPicUxCICK7wmtidCMjKtupCPuDc3LylnYKXGzbUk9E6zVIFjCHxYqFDjtNpx3Uji3cxRekK8tSmjvd9OkM4NQpOioQ1bN4BU9HpppL3IriCdB2aYRs3-uHmF10NUGZXsTfsRB_Beuin6OWIGZIHNOvokQOkd4ap1aomRl5KSft5Ma6w1wwT4Zy2d0LLdFO1ffJQLaySuQvXgGli1ghr9iUayERNVbieQ94gpbJTccsm5VnHmvNkC-L9UEfASfF0kqPo-dsEErAqMRvKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=rorU07Bef6PTNPrt3siWuTvgK2R7XQDE-CYv0HcPnRe8jij-lUv1PfwUBqMvZn-gSXC_tPicUxCICK7wmtidCMjKtupCPuDc3LylnYKXGzbUk9E6zVIFjCHxYqFDjtNpx3Uji3cxRekK8tSmjvd9OkM4NQpOioQ1bN4BU9HpppL3IriCdB2aYRs3-uHmF10NUGZXsTfsRB_Beuin6OWIGZIHNOvokQOkd4ap1aomRl5KSft5Ma6w1wwT4Zy2d0LLdFO1ffJQLaySuQvXgGli1ghr9iUayERNVbieQ94gpbJTccsm5VnHmvNkC-L9UEfASfF0kqPo-dsEErAqMRvKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=aTmPkay2id5ek8Mv6StreGgtBvkXY5og3wbNigc221DiKsmiCXwmPy9OZ-quHEmqIxha7tUq87dO5aq4WIPS6nHYal94klD88Yl_XYfNSILW-HMg48Fv97ZmffJ1sjon8kziROyk2lp1WWjmFvbj_9YfROBTaEt7ne5p-OEjGd5W1WG0IFGlyw-5nDBrj7ArWqwOYb-g4LCQRQtvL_AXYqw72zGgJNURsYBSNzn3y-90m8pwgvJTkWLE-4M1kETLdV5ranqPPqHA64bwBBG3dgPT52Zu3BfP8m7BNR6XGliZ1cR4X22wiNErJKO6gEDuaYV8Nfj5LCpSPdnjPiXPaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=aTmPkay2id5ek8Mv6StreGgtBvkXY5og3wbNigc221DiKsmiCXwmPy9OZ-quHEmqIxha7tUq87dO5aq4WIPS6nHYal94klD88Yl_XYfNSILW-HMg48Fv97ZmffJ1sjon8kziROyk2lp1WWjmFvbj_9YfROBTaEt7ne5p-OEjGd5W1WG0IFGlyw-5nDBrj7ArWqwOYb-g4LCQRQtvL_AXYqw72zGgJNURsYBSNzn3y-90m8pwgvJTkWLE-4M1kETLdV5ranqPPqHA64bwBBG3dgPT52Zu3BfP8m7BNR6XGliZ1cR4X22wiNErJKO6gEDuaYV8Nfj5LCpSPdnjPiXPaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=c8vJ3gEfHbv4twqZC6X57429KrtOIcA0KJDNnPy7mzLsfhKm7mhMwmo8utU9dwxjmxuxaamLrpuVmiYTP8VpMwxh0qE3G-omZyJT6WvvuufO2y6bfI09lG_p3zgHIsaTyCmG10vLj5FiC0Xv4rMpxYibJSYQ5W7Z0hqRGvBLWvOq4EnXu2XOR4360V2xic_TdVmmKi3BLVK9lw-71J9R-tzLlFwAy8SkOjG8deS6ge16hePLZdAVh1ok8fn1kQXBaXzR6htJHHKkGVV7Vdl8LoFT8KA7TojamO30lzvajLRreO-b7OKpVw9twU-_lKyJ3YXuXOL_k_i47yZS2msicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=c8vJ3gEfHbv4twqZC6X57429KrtOIcA0KJDNnPy7mzLsfhKm7mhMwmo8utU9dwxjmxuxaamLrpuVmiYTP8VpMwxh0qE3G-omZyJT6WvvuufO2y6bfI09lG_p3zgHIsaTyCmG10vLj5FiC0Xv4rMpxYibJSYQ5W7Z0hqRGvBLWvOq4EnXu2XOR4360V2xic_TdVmmKi3BLVK9lw-71J9R-tzLlFwAy8SkOjG8deS6ge16hePLZdAVh1ok8fn1kQXBaXzR6htJHHKkGVV7Vdl8LoFT8KA7TojamO30lzvajLRreO-b7OKpVw9twU-_lKyJ3YXuXOL_k_i47yZS2msicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=fTMt0pN2Y1McODc--tp2S4hkTNFRHsWSfC3Gb8URrlBdbbtva_IpUVjJH7IhMohuCrJGZzaLh0KmqDRuX2jA18ATO3xRX0L5yA0VM7kDvkGmrqAS105h1xH6HSwqI8QAS5x5I-ubvKQ8xFwKbSFZmcTP2YaCasj7PqWody2LcqF7IdpvEh7CCjG3dMqcRfIxZcOYNA40MwbMb9ClGenVMzyfH4jyLwwoKyzAmsVrYyZES2p61nebHAhWAezP7JTGMIuQ_nUj0f1RyPcuPGUZjQFUyOMLFXZQYm1A1KQruSKpMPfoe_9ZwkpmkEq0ONBERe2mBJUzrsQuW1EI_7kcJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=fTMt0pN2Y1McODc--tp2S4hkTNFRHsWSfC3Gb8URrlBdbbtva_IpUVjJH7IhMohuCrJGZzaLh0KmqDRuX2jA18ATO3xRX0L5yA0VM7kDvkGmrqAS105h1xH6HSwqI8QAS5x5I-ubvKQ8xFwKbSFZmcTP2YaCasj7PqWody2LcqF7IdpvEh7CCjG3dMqcRfIxZcOYNA40MwbMb9ClGenVMzyfH4jyLwwoKyzAmsVrYyZES2p61nebHAhWAezP7JTGMIuQ_nUj0f1RyPcuPGUZjQFUyOMLFXZQYm1A1KQruSKpMPfoe_9ZwkpmkEq0ONBERe2mBJUzrsQuW1EI_7kcJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=HAt41fvgpavr_D6l-iVnPCrlZtHAujPRY5eV1Izsb_iDtqtqgXwK32V5vz1l69JmzrhyjS5JHX66V6mBCZ34_uErzn7tVgvuk8mH9dAZ5LN0B3c1fdqa0dHDJg2hzi3NkZCSy0Fxun7p-fLdnCZJWhzZVSs1syOjGN7CMDuPRYwhqMvQJ3TCYR_wJFuAPh5rnHOc9GEVITjxiw2ntPjROowDTnbHRJExp1hxVJBeO5XSiXrBfsdjgymVgw1Ftrpk8ZxKSDoUWcC7Iw_D2CRnF9vkTftLuBkkT7FZ6AyySNssDoDPVY9zRlL8s4lWQKBxht5a0fp81gy-gYT2ndvp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=HAt41fvgpavr_D6l-iVnPCrlZtHAujPRY5eV1Izsb_iDtqtqgXwK32V5vz1l69JmzrhyjS5JHX66V6mBCZ34_uErzn7tVgvuk8mH9dAZ5LN0B3c1fdqa0dHDJg2hzi3NkZCSy0Fxun7p-fLdnCZJWhzZVSs1syOjGN7CMDuPRYwhqMvQJ3TCYR_wJFuAPh5rnHOc9GEVITjxiw2ntPjROowDTnbHRJExp1hxVJBeO5XSiXrBfsdjgymVgw1Ftrpk8ZxKSDoUWcC7Iw_D2CRnF9vkTftLuBkkT7FZ6AyySNssDoDPVY9zRlL8s4lWQKBxht5a0fp81gy-gYT2ndvp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=pYgqS1d1HLXaG5L6_awv20mNwdYEOrpUoDBCxoJmtjHdMNLdDsEG7clcDifgk1BmHWZmti8tjziwobBYX_g0-CT14_0D7ewjMlDgIy9QMcLnx6G8qqk6mwgM3tciMZXDS6zsjrOvOoWK-dY1pHtIf2iJEFFBDiPLOF3xW5jVR_KEOVO5c8Uqi1JO1n50yCK_YUYrXxW8NpxflAHkYsNW3IClD6KOfXf-Ht48XYwtklMeXw_G26U-ae50AVfk38Ux51ke6uaW6fSwfvkT7QYuUT5KydJRBRbKswxsVyg9d7quIXP8C6WTWD4VTVNuGN8luftTAN-xGOIfwDdxDR2V8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=pYgqS1d1HLXaG5L6_awv20mNwdYEOrpUoDBCxoJmtjHdMNLdDsEG7clcDifgk1BmHWZmti8tjziwobBYX_g0-CT14_0D7ewjMlDgIy9QMcLnx6G8qqk6mwgM3tciMZXDS6zsjrOvOoWK-dY1pHtIf2iJEFFBDiPLOF3xW5jVR_KEOVO5c8Uqi1JO1n50yCK_YUYrXxW8NpxflAHkYsNW3IClD6KOfXf-Ht48XYwtklMeXw_G26U-ae50AVfk38Ux51ke6uaW6fSwfvkT7QYuUT5KydJRBRbKswxsVyg9d7quIXP8C6WTWD4VTVNuGN8luftTAN-xGOIfwDdxDR2V8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=TAzPDqrmGLgh6KY4fTwUO_aaLJ075ZQjaKPTLv8o07tueEtXlwdka8AUPVuJhQovCgdRw_d709I1t23F_hy0GvNgGdO72WYLRASbeWjeC2GdKIVf09fyNQxV-cjJY0cHk5ZP22sYrdRvb3IWL4Zejt4QVnMVLK6U0fQkjN67HXlM_Jw8NVH_wTBFCWz7QJroS27OXfUDfumGahjWjc4jqqjC36AoMgejCT2US3u-yQS3dLXTjjIc_bed6R-rxU7y7LtYBOiZS8tn27HaE9E9wtBYq6OTdYs32xYqoO4Y3l9N_pSn20PpBIQZfYcTZWUfqN-KmPdKgaTOk8hkYQNsJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=TAzPDqrmGLgh6KY4fTwUO_aaLJ075ZQjaKPTLv8o07tueEtXlwdka8AUPVuJhQovCgdRw_d709I1t23F_hy0GvNgGdO72WYLRASbeWjeC2GdKIVf09fyNQxV-cjJY0cHk5ZP22sYrdRvb3IWL4Zejt4QVnMVLK6U0fQkjN67HXlM_Jw8NVH_wTBFCWz7QJroS27OXfUDfumGahjWjc4jqqjC36AoMgejCT2US3u-yQS3dLXTjjIc_bed6R-rxU7y7LtYBOiZS8tn27HaE9E9wtBYq6OTdYs32xYqoO4Y3l9N_pSn20PpBIQZfYcTZWUfqN-KmPdKgaTOk8hkYQNsJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwVyrMZzXys8KyCBbdEkb7R5XvYRp__8KWbheZne4wKe4f1t9zrHdffzLxkjuFaN0wJG7qCfgrsvFc2O2ZMs6wWVWoXs5azUtme6Je-mHKyVhK1LoCXa6nEzMZgnQUau1xdTOWDBuxudLtoJ-ZGBc-AS8ER53lnSot4hcAODbJu0ry3hKctHor4_zFdOKh2RqSxPtujLYw412dsdY-MpmuS0Y8b-PiWoMinsE86ql_9cpLbWyC-PIHUPgMfqmsHzwq0ghj9KGut8Cr5XQVwl6Jz-sJ5S5Toc1CUbPegY-ebr8OatEH3jfnOywr-VtE9lBxoMfPNboylqZggj5bupAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=HAmh1mJ4YxEypG3SORtTTeqNFYmI1E3ZZ0PHPwoaM8fyDY-DgrbHfx5oJCZQw-beVLdpR_rop7pONiBr2XsRenYrvFj8eAsSzf5nCNvWgOcSuE0xy2MSkjc9yodZKz3nT0RJLkf5zt0-QzgWcx7qZW-L40ITTeJdtPd93cREJHM9cOorAuTr-RRPPLpSa9Ld_NgXFpapLzdQSkpEMq53QA0oXESkZTtEXWBQJSuam2IkR6yszhSgETTEobNQ751pxPY_ub-27RayVRo3wHnRmohjgKVYhOBOOBlAbXy2P5qga2Y7iRdfWcZUwMJxvVugbxp8ptWNI-w08BUPW3M-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=HAmh1mJ4YxEypG3SORtTTeqNFYmI1E3ZZ0PHPwoaM8fyDY-DgrbHfx5oJCZQw-beVLdpR_rop7pONiBr2XsRenYrvFj8eAsSzf5nCNvWgOcSuE0xy2MSkjc9yodZKz3nT0RJLkf5zt0-QzgWcx7qZW-L40ITTeJdtPd93cREJHM9cOorAuTr-RRPPLpSa9Ld_NgXFpapLzdQSkpEMq53QA0oXESkZTtEXWBQJSuam2IkR6yszhSgETTEobNQ751pxPY_ub-27RayVRo3wHnRmohjgKVYhOBOOBlAbXy2P5qga2Y7iRdfWcZUwMJxvVugbxp8ptWNI-w08BUPW3M-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=nF7inh14kth75RoEGBgGAiK_w713MGkN4U_9v6jDEwo1RQsWEokzFRq7f3utxjFID9mKqnaMBex-G8MsToVCeMkZ6tWfBi_HcPqd7YztbJW6DZZCWa1ZrHQKhPIo1vy-C0QeZ9tOQd9C4c1-H6uCWiu745EOgrF2vLcnXPB63sjXB6EDDbLEAdZRXWjvw3T_vkXRsBlsAjd8m87qcuyJemGRIVk_y0_xu0SyorPYZpIqhwjApGqpjs_zuuDITvbw7cAnqQvSsQ56tZU3QjAG2VndP1QbcwXlFvVv44sTV3vfx-YCqW9__ScBcemIEf9wg-E6x4FcgB1-CO_0CP1BZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=nF7inh14kth75RoEGBgGAiK_w713MGkN4U_9v6jDEwo1RQsWEokzFRq7f3utxjFID9mKqnaMBex-G8MsToVCeMkZ6tWfBi_HcPqd7YztbJW6DZZCWa1ZrHQKhPIo1vy-C0QeZ9tOQd9C4c1-H6uCWiu745EOgrF2vLcnXPB63sjXB6EDDbLEAdZRXWjvw3T_vkXRsBlsAjd8m87qcuyJemGRIVk_y0_xu0SyorPYZpIqhwjApGqpjs_zuuDITvbw7cAnqQvSsQ56tZU3QjAG2VndP1QbcwXlFvVv44sTV3vfx-YCqW9__ScBcemIEf9wg-E6x4FcgB1-CO_0CP1BZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fAKiTyDT-ncn5Rvl8CWBtVMAeKT0pGIAkWma1Zj9fBI8v5aBcte_CxDLlXgzjB3nomFswTtBfHRI2-0o3XlsS0hcMGA5VCAmPdQsnbendE4KJ3oMKYfEbKrIJSzVqboUBiu3y-llkuEkDA1a6Izd8ixUWsVz9RVLkb0n5VTbMNH76ZJmHnM27tUpIa2XCHNrOkGFCHMUwEgigyFHDjTya203hE2ifLpLEZgQb81NWgsp3KwndBcx0ahIx_E1cCBm8YHDwzh-2eVTIlpOUOmLKwNp-82cH_zqam_un4PUpvNoyvpSWC2LF2xP56nK2zpNwaIfL7oieU8HJIhuaZgbpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fAKiTyDT-ncn5Rvl8CWBtVMAeKT0pGIAkWma1Zj9fBI8v5aBcte_CxDLlXgzjB3nomFswTtBfHRI2-0o3XlsS0hcMGA5VCAmPdQsnbendE4KJ3oMKYfEbKrIJSzVqboUBiu3y-llkuEkDA1a6Izd8ixUWsVz9RVLkb0n5VTbMNH76ZJmHnM27tUpIa2XCHNrOkGFCHMUwEgigyFHDjTya203hE2ifLpLEZgQb81NWgsp3KwndBcx0ahIx_E1cCBm8YHDwzh-2eVTIlpOUOmLKwNp-82cH_zqam_un4PUpvNoyvpSWC2LF2xP56nK2zpNwaIfL7oieU8HJIhuaZgbpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=i2fhZoqRJWAcQAQqr-c_OS-XTzdMnRuSS3yGws16ytMANMzAui8K_7rC0gYGumqS0u_x9ShJPHxgJrJVP3wRD4jG_ByXDqPGiO0v5xaZm1Yo0Vg31MPRhYCEENPKsCPA9FKJ2g4SzlBNcejb4enYBv5o2wTWA0kfzmRdI4xDPtOdbSgP-VvWBXB-QvByClHXxQ0rau4kfHGlcl_1Chg6CwYKObZxA6_BF6LUOLS5zrezFtG6CuWBnqLa3608f0vcuMCXkLTF1-9BfznmyVD7eSkAnkePFZGslJUWl0TSRh3t2OoE_o-4d0hR9Nd88qfUOyL-C-wpYKuHoTmoTPeehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=i2fhZoqRJWAcQAQqr-c_OS-XTzdMnRuSS3yGws16ytMANMzAui8K_7rC0gYGumqS0u_x9ShJPHxgJrJVP3wRD4jG_ByXDqPGiO0v5xaZm1Yo0Vg31MPRhYCEENPKsCPA9FKJ2g4SzlBNcejb4enYBv5o2wTWA0kfzmRdI4xDPtOdbSgP-VvWBXB-QvByClHXxQ0rau4kfHGlcl_1Chg6CwYKObZxA6_BF6LUOLS5zrezFtG6CuWBnqLa3608f0vcuMCXkLTF1-9BfznmyVD7eSkAnkePFZGslJUWl0TSRh3t2OoE_o-4d0hR9Nd88qfUOyL-C-wpYKuHoTmoTPeehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLUDUhtTvKj-ecco8SP2CNtws1DpqyvLf2IEyRJ5Lbv-mfzSIs4208Qmg49A3ovC41YN8jpTonixVBXnd7sgIsJl8akU5vlUElHJ8tHavqQEwKFRjr99Dk1CwnRZyVAGuI93DSuL_8BCmCK4fUsqkKD7eQPI0l4ZoUNcuSpBiuJPsJRwDfkNpT8yKbmxbl62dOivOQ5Yau_zjTwEWOkAFLfF2pxi925vosvJccOffQu4KzA88mndorfNXVCGhMlTkvcwPX1apRb2RdwjIssTO3lmgC5g-Hh-mMyI2kk_xHYMkde45m2sr3gnfgxSQWI7Mt-HRIOnevLx6IBfk2KNww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Dlf5OnxWY99an9NsvLOp7BfW65EQH8e4IWhrykvJZXvau6io_UvXv6nxxOseZI7yG3A2xNMmSBnmoEtTodtSwgg8BSCrk-ppdYXEUpe0RliOVdnn1aP2I-hhTn_RW-ArcT2t8fo5AuGq6sX_FPvRODglThDdqrSrpySE_7qqKEiS1owYs8iMHLvZMPmxeZaX8rznw1u5a3rfmhVPL4OcvB2LcM8rKY6ZR937yf8_N3k0SmWVelrtE2Lt92fDwhIWEDWwmdFsngOOGW1W1s8wQaji44NYO4Q3Ta3mQ2khD3w_PokP1wH3E1poc1VoJ6yRukn02zYxu6j5dMzgL1Ck-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Dlf5OnxWY99an9NsvLOp7BfW65EQH8e4IWhrykvJZXvau6io_UvXv6nxxOseZI7yG3A2xNMmSBnmoEtTodtSwgg8BSCrk-ppdYXEUpe0RliOVdnn1aP2I-hhTn_RW-ArcT2t8fo5AuGq6sX_FPvRODglThDdqrSrpySE_7qqKEiS1owYs8iMHLvZMPmxeZaX8rznw1u5a3rfmhVPL4OcvB2LcM8rKY6ZR937yf8_N3k0SmWVelrtE2Lt92fDwhIWEDWwmdFsngOOGW1W1s8wQaji44NYO4Q3Ta3mQ2khD3w_PokP1wH3E1poc1VoJ6yRukn02zYxu6j5dMzgL1Ck-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=W-TfgVFr7UcWFczrMIZ8tO4nN-gHDQS0dRpFd__QoZkv-UtOXti4GP2q0oZZB2lCailWHnYKIrGmpFTudshRADKAsEf-Q0yFidXNcOWpzhc3lojnUBxHUgyAAS7RJOJHF09jpzYNUslXspFR_qNjnQn8u5Ht3vDP3H4HDheEQiyBHJc2E_C4PAgaaqMi3jsfCfdLfdhsfc6YuDvGa_Uujuc7qRcXP4lKQivLjajRdUau3EffcSy_H5ttMzj2FIi3RUcSm_78X1DUoncbkC0JNVibu5oLanS0nPsVgOCtQWA2QCagOEZgqak45rhxdGzxJDABMwUkkNMEv82M_Hf-Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=W-TfgVFr7UcWFczrMIZ8tO4nN-gHDQS0dRpFd__QoZkv-UtOXti4GP2q0oZZB2lCailWHnYKIrGmpFTudshRADKAsEf-Q0yFidXNcOWpzhc3lojnUBxHUgyAAS7RJOJHF09jpzYNUslXspFR_qNjnQn8u5Ht3vDP3H4HDheEQiyBHJc2E_C4PAgaaqMi3jsfCfdLfdhsfc6YuDvGa_Uujuc7qRcXP4lKQivLjajRdUau3EffcSy_H5ttMzj2FIi3RUcSm_78X1DUoncbkC0JNVibu5oLanS0nPsVgOCtQWA2QCagOEZgqak45rhxdGzxJDABMwUkkNMEv82M_Hf-Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEpQ6f0oMH-7TsH0AAI83ZHBhF8-C9uf51E2BEVpuNgVYrOI75cQCXMay1qII2m1pkkv-RimpLEheRWfpH55ViSjjsy8rRK2b8Gcl3eetrHOC4qVohGtOPr37w0ALwQ7bdio2nPvtYx1n7hkle5GeoUyTUNT_dsrnFJDZhPSv3pzhBhFmH6aaFDrikNzn5F67DyQUUButd7bM5H1PWb4-8pBocC_pbglgHT6Y67faZScoiYimR1CWz9tUByt1q2FzU5GZ4yY5q7M3iD6-c8lvVH3fRxWywpjXkCXMHwxcFs3Ar56Fva6b_vl8uq9Ugnr8efuzzHUpwk8ik01KReb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIQVAjDT-6iaT1oSYORJz4oKXEftNPGrVaCs_VGLMehQRL0PMXK-RwAwB_Z7uZy0l-xqWavGdRaj6Z93OCdZwgdCX4AoKkebLni97vDp9jKKn1TooDOCR4bqPfh-gXODJ3LcSG3w9LLtCGku1cy8j0ywXhxLmNZpQ38IPxBzEGyLUzj3Urw6bEh56otOdS6MHDOH8ZpRd8YqlpbcFE2gxIPPoaHTlsYWm0v_dTvv-cO6nHq9DOF552qbOqoJdxFm-83vSvqjLe6Zz80eB-EXsLS9n7UMBvOpkqvalW71jbRxxdFFjVqhJwrVTPtFyz1Z_Nq1NX9xDe9r-oy_3jwjYA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DPLBKfMsG1_KbRoSuFOffCmrDcKPT3hhNSfPEyIgNU6UOsoZjfiDE4xu8dugIyziH0AKwmJdd3lpoGeJYDgTy6SxoQItQVa6ZkM1bASQXWDYoVJGC_71KqSZyoolznEp9YnPIjUQQfigqL1X4cSqKpXayVOcx7FeUlHkaAxJdp2YgnY3c2bM6HWA7yfOF-mgFTrKtQrCHzX00WRjSQ5sQDnsO6Ya16Vp1tGzpB9T9K8wKu4BubXVnoEcsGWT9pblsPFWWPyveQSMTmS7JfBO44GtXX-mGCcfYHAh5ST6T9D9OQMmkRQ10_MR_NtCwoOq3ZOltpA7-5UCpUZnpqakaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DPLBKfMsG1_KbRoSuFOffCmrDcKPT3hhNSfPEyIgNU6UOsoZjfiDE4xu8dugIyziH0AKwmJdd3lpoGeJYDgTy6SxoQItQVa6ZkM1bASQXWDYoVJGC_71KqSZyoolznEp9YnPIjUQQfigqL1X4cSqKpXayVOcx7FeUlHkaAxJdp2YgnY3c2bM6HWA7yfOF-mgFTrKtQrCHzX00WRjSQ5sQDnsO6Ya16Vp1tGzpB9T9K8wKu4BubXVnoEcsGWT9pblsPFWWPyveQSMTmS7JfBO44GtXX-mGCcfYHAh5ST6T9D9OQMmkRQ10_MR_NtCwoOq3ZOltpA7-5UCpUZnpqakaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duOkFbYTM1kpeokFXicVCXPXP4Qge42sAZw-G7ETat_p7X1d97XPGSS-zW4-nwWabpt-I9I64oyuFxgzyvUiZIVUAgXlt__gt7TYNVN6fVLCoSItUsoptomMczzS-C7wMNippAB3DnlNUJ6q_J35hYJr3QJxndFamXqESINeJY6k__Cm-pUUkcYhLFsSB26k7-V1NST3ie40jMTJ5d18qhQqRWPrEmtely3yj81xUqHtDTrzz8xpO0wZCjsHPY4nvVsziuFldhA2EAYdaIDygbYckbU35ONtKvpwAN2MBEYgLP67qOTyQsziefSBXZILV7taMh8oXv-A_eb6ghLj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzJWEcm1unH9umUlaNsmzcoyOXYM6z0qQHeuJikJiC9Gln4RVPRb_16o4lZo6RkT-rhTPxfUcFV40whHt5cua8siEKLJEdQxzLQsZE6P4r1FghCSGbMFyHQvm1BPJr_MjQT6uJimC013rSmAsJZ4Rtj2N29GtmJFHTEaPTfblyKJkoLAN8jYSa_tXCOlI_8dz15Wgkgdxpk8ocA1TzcSltbLUwyTbyX_6dFKo34hM1qHjYAjzdZF12bzM9aP4wRzePA5Kbn7RehA-QASF9QHBJe5sjR8E4MKD2gcxCOFsmfeaGO4fVtM32UXfnqnsCOK6B5W-DA-PVEbUH79pB16iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhAP5ABzoPKSNelNMnzSn09Ovzr2rPaRW8uNt8j0ZvzJLvyWTxxhiWAILou1dC7kddU8XL0vksPMg3VCNgyzkVRyy-SXYsQIpuGvpFCHc3kGrJ8Qd5gTS68yW8SV97Ew7tSxKg2pjfH49WIprYKBHnYlXEHo-EHLL3VsE9re3thdSFUIcVRFqvv8ml5hy2KHoQ_jrQ_SIMmNJZtDofsW1W-HvzpP4vjCf95izp6uC1YQJr7OSe_qYbtDt-rQJxb7YIwVAEtuv-of9lyMZqwN3thwusDzwBr2OAPCop21OpPNANFLuWrAiQ47rGvAgfVRv2SYwp_wkElu0U6NVvVFhQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=JYMb9Gr3UzTTm9CPMTQ8-a-g17vPn-G4jMFtL-ZfqDk9Ev2zq_WYAyTr_Nv1hmU0nx-RbAH8qGbwJTFYViVyCpH8GxlX8ae5lfbl3MDloGTVVpISBqbBbx1KZ_XShG_3TrVJ3x9i0s-GPSBtEFssEKWzahW9ys6ATiy0PFLIXT2Igl6Y8g-G5tmYprmxsNI2rtIcz59mzKcotUZIEBeh_t7lZWzD1AFipeGXi34ZzI7oy28tywhxXC_ypmmIzmiHnKkEUEIuK0jJcLa7pM0QN96jxar_Ik0JsAA80TPgAz2PM5lN6pa4szQpHipgXrdmIE3yrjFYhOLmkCLILUMcgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=JYMb9Gr3UzTTm9CPMTQ8-a-g17vPn-G4jMFtL-ZfqDk9Ev2zq_WYAyTr_Nv1hmU0nx-RbAH8qGbwJTFYViVyCpH8GxlX8ae5lfbl3MDloGTVVpISBqbBbx1KZ_XShG_3TrVJ3x9i0s-GPSBtEFssEKWzahW9ys6ATiy0PFLIXT2Igl6Y8g-G5tmYprmxsNI2rtIcz59mzKcotUZIEBeh_t7lZWzD1AFipeGXi34ZzI7oy28tywhxXC_ypmmIzmiHnKkEUEIuK0jJcLa7pM0QN96jxar_Ik0JsAA80TPgAz2PM5lN6pa4szQpHipgXrdmIE3yrjFYhOLmkCLILUMcgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FkasSaeT2_DlxxXEXEvxq9m94ctLhUW-zG6fAmA8MKAPyhU1Kf9tjlwsCg5fSrb3T2MP8bP165-Zr9kuzeKjZ5siznib3tlXxCV8a9LVuH5EOt73xpjhc_WRDEEp-eDn99f4iCTPSw0rvVmAkxNvkdNAW6jfUq9_xO8CifAyFHclR2DZP_goLf4dHvaI2pboi-ijPG7ccIXmnlJ8x0U73IkO_Fo-REo42HqLsoVoQt4U4FLIySBEP_jBUsfLJtSd67oUfmbsFNcrtQhhjMsI9RJm0414KUAZwqHV6pheRj2pBy_g7FncCDDd3M_FnXjF-_LBGntYKiMXo7K1ZYnsEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FkasSaeT2_DlxxXEXEvxq9m94ctLhUW-zG6fAmA8MKAPyhU1Kf9tjlwsCg5fSrb3T2MP8bP165-Zr9kuzeKjZ5siznib3tlXxCV8a9LVuH5EOt73xpjhc_WRDEEp-eDn99f4iCTPSw0rvVmAkxNvkdNAW6jfUq9_xO8CifAyFHclR2DZP_goLf4dHvaI2pboi-ijPG7ccIXmnlJ8x0U73IkO_Fo-REo42HqLsoVoQt4U4FLIySBEP_jBUsfLJtSd67oUfmbsFNcrtQhhjMsI9RJm0414KUAZwqHV6pheRj2pBy_g7FncCDDd3M_FnXjF-_LBGntYKiMXo7K1ZYnsEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=junCOPIgroGcjsRgRO-axvemCEuxTFQYoahBFVJoOOT0o8EZJZVOa1pvJjE4QjEKznQvlFaJ-HqzE2TBUA29Z0HTuX88sEmMakAnloSwcm_x6G4B5jI41OVIVzoeL2iNhNFcs62OkQQPlCpWGT8pCqLBNO-kVgDm2FdwFxMvTbEpmCOyYJNqwZvxy1yYkJIQyAOyRD0indnZ7sNQ6VIXNI02Ql3dDxhUpH5r70ohdY19AsuXfILDTDgzrutfbYXWF3Ugwdk2iNFqiROplcazKybyPhaDFsZlwyvrxHGlHr7r5p1E3nitUCtlBkZjCepO8_Y--zcBrzsEle8e-zWM4RakwXwed64xJ3OUbFWGy6jWaHNeWcy3HR-jaPEEvqsBiUlaOht5rZK1BP0s6N4vFWWQJht4JE2dWjtlSbw3ornpfn8bPdH9FEgWNpKRLBDLDXzTaEZk6FFhyA78ArVDwH9edgQnCakcIGLmp1572oLDeDDbxNQqC1H5_UmmsSKXh-wlDUELlVgVbDvFu8nJkI_D8YP6WNW4hAfzS_w8cJ7eY5czJttSoH18SYGuabMItrGxB34_ai_A7jHDLA1-x7FPyxDITuhYaiWX38HS05TlmjoX9vCIfeMpJodulUv47iSPq0escULQfs4tG6LZKDZ-MCvxyQ_IAOEQTo7OA0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=junCOPIgroGcjsRgRO-axvemCEuxTFQYoahBFVJoOOT0o8EZJZVOa1pvJjE4QjEKznQvlFaJ-HqzE2TBUA29Z0HTuX88sEmMakAnloSwcm_x6G4B5jI41OVIVzoeL2iNhNFcs62OkQQPlCpWGT8pCqLBNO-kVgDm2FdwFxMvTbEpmCOyYJNqwZvxy1yYkJIQyAOyRD0indnZ7sNQ6VIXNI02Ql3dDxhUpH5r70ohdY19AsuXfILDTDgzrutfbYXWF3Ugwdk2iNFqiROplcazKybyPhaDFsZlwyvrxHGlHr7r5p1E3nitUCtlBkZjCepO8_Y--zcBrzsEle8e-zWM4RakwXwed64xJ3OUbFWGy6jWaHNeWcy3HR-jaPEEvqsBiUlaOht5rZK1BP0s6N4vFWWQJht4JE2dWjtlSbw3ornpfn8bPdH9FEgWNpKRLBDLDXzTaEZk6FFhyA78ArVDwH9edgQnCakcIGLmp1572oLDeDDbxNQqC1H5_UmmsSKXh-wlDUELlVgVbDvFu8nJkI_D8YP6WNW4hAfzS_w8cJ7eY5czJttSoH18SYGuabMItrGxB34_ai_A7jHDLA1-x7FPyxDITuhYaiWX38HS05TlmjoX9vCIfeMpJodulUv47iSPq0escULQfs4tG6LZKDZ-MCvxyQ_IAOEQTo7OA0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=JyIjcXrzkEv7X8nyDBy2ZFu59Z9XEZ5awDpfYvZES1AOvs6_7q4G5TIGWheWxaKEOcdfgUDU7Uh4ZQ1wJKMWcNfm_aX79hV3QhgvbabweA2GJJn40PGq-JCpPdkvCIYc3c_RLRNqWMsOgY3MKIabdYwCp2aGYVV9FcHfRwVzxHygRnfi3dNuSYwdQLMyMtkecRtc3MpwLt05da7H_ABIxNIkPF_Uk1eMCCrJk3pD8zH5l87oJVqh6DcDVtWdN9crbgodSckBQFNevyLNU-fYdODzRODMs_mc3Ev6x6AMv8t5kmrMnP4y-wucxO0pCJ79PfGIPxOPgt6VrLB_zJrcQImXDYZX5d23k4s-vAA5qzIKHHgvSMvjWE5-7QIikQtHyyvEc2AnPgtD4e0b-7uitBaB2nsZ-nacuaVhZsBVMq4g6wNsWsXN6sEH3yWc69DbEwied4VmMAENhIGTeNTyIR96dW8m8X8c4QTvNC88BlF0ZXTeIA6PLutdkpp4Q3omgGcRLRjjrHSJf8Vz2MUjBTYWIJGMLz36vdxHI5wwd6wOklwwJcv8S55cOEfQt3sRRByvTNDls5taQHiAf5zyreI49vLURUubk4wchzUWp5QgjjeA1gu0BN0cJg0mWJdCVkzbVD3HoHIQt6KbLVPMX1O0w9mL-ERJ02vKx8JBtUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=JyIjcXrzkEv7X8nyDBy2ZFu59Z9XEZ5awDpfYvZES1AOvs6_7q4G5TIGWheWxaKEOcdfgUDU7Uh4ZQ1wJKMWcNfm_aX79hV3QhgvbabweA2GJJn40PGq-JCpPdkvCIYc3c_RLRNqWMsOgY3MKIabdYwCp2aGYVV9FcHfRwVzxHygRnfi3dNuSYwdQLMyMtkecRtc3MpwLt05da7H_ABIxNIkPF_Uk1eMCCrJk3pD8zH5l87oJVqh6DcDVtWdN9crbgodSckBQFNevyLNU-fYdODzRODMs_mc3Ev6x6AMv8t5kmrMnP4y-wucxO0pCJ79PfGIPxOPgt6VrLB_zJrcQImXDYZX5d23k4s-vAA5qzIKHHgvSMvjWE5-7QIikQtHyyvEc2AnPgtD4e0b-7uitBaB2nsZ-nacuaVhZsBVMq4g6wNsWsXN6sEH3yWc69DbEwied4VmMAENhIGTeNTyIR96dW8m8X8c4QTvNC88BlF0ZXTeIA6PLutdkpp4Q3omgGcRLRjjrHSJf8Vz2MUjBTYWIJGMLz36vdxHI5wwd6wOklwwJcv8S55cOEfQt3sRRByvTNDls5taQHiAf5zyreI49vLURUubk4wchzUWp5QgjjeA1gu0BN0cJg0mWJdCVkzbVD3HoHIQt6KbLVPMX1O0w9mL-ERJ02vKx8JBtUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FyswiFeFKFezNGDO6I4IrSbG0NLeWahFbofbAyyP8IDvqabExGGh3rDuAxLT8Ia8OeILA7I2yFXkMrPyUH4QqCIzH1PJFHw-qlCkSzPIz4K7so8RQ-2jFcLImJbKseIrN7wvqTB5SKVkIGPL3S-D48g7dYZ7U8yboto-WxBa3YChM5iS1P4lSvUKXCy1ugnAWLTR5cLsc1xJMuBX14ZSWBNvrRr5FoilqBfO10ahUAdMJ2L4w2ZBX6_GQACKcZaN_aMDzyTZm9zouIMYx3F_aEbpSvhmjIR-pvll2m3nKUwj79Iddg5u_g__hIPc8Evzt7j0Le-FBuYrLKb0KCM4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=FyswiFeFKFezNGDO6I4IrSbG0NLeWahFbofbAyyP8IDvqabExGGh3rDuAxLT8Ia8OeILA7I2yFXkMrPyUH4QqCIzH1PJFHw-qlCkSzPIz4K7so8RQ-2jFcLImJbKseIrN7wvqTB5SKVkIGPL3S-D48g7dYZ7U8yboto-WxBa3YChM5iS1P4lSvUKXCy1ugnAWLTR5cLsc1xJMuBX14ZSWBNvrRr5FoilqBfO10ahUAdMJ2L4w2ZBX6_GQACKcZaN_aMDzyTZm9zouIMYx3F_aEbpSvhmjIR-pvll2m3nKUwj79Iddg5u_g__hIPc8Evzt7j0Le-FBuYrLKb0KCM4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAY10x4oG5QvcH_GqmaQzKrwoBd6CX0GqzQDfWbOEn-CGv86U4of_vlwJnmcg9fI_LcrgDCqKm-fs2qsbBE-Nxa_Y_Ywss5IGzoFc3MdiHnP1vf_haWAao6J7n1aVdrQ6GGdifLukFfWGcb6NJ5pdBLeelKleDL3cOwcqaVvqCnaSBUm5DHRuHAZycMcXkLJOEFcJdszNyE_NuQxtAX210IsRkOCPjWQSSEsPzpFW17ZqtducseOOqyN1PiTGu63Rjv-hORTkkyT0URUZQXwuRMcou7lvdJwmxj7PmO0LyzNrbzuKZQRKFsFeFrpDoEKOyb1dkrPbYYwXr6objaKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=TqHUR2SjVFWXj34shVmc3zB_r157jwJzBbOhIXBOLbfuYSUQYK8VtNiQE94dNSmWjHEa0Is-oxyHvIljHTIx82-nUMfrAjrnPJMhl8aPitvWb3AvF5CU5212LTAJTicuWgbuc8y55xuhOkRjDzZPmjVLwI9z1F5A7sxWntwdj6j2nOoRulYZWh4ROpzJ4eZska-Xcxr79aL-e5uVRq7Fp_VKK9xWmoZVpqjdilZ5_jJMurlfocOBxY6pYWnBQMQiELe1kmQ87Z7Seb-l2M0jSlQ4mEoCwb_WR95cwujs6ae5piTXzaiaFgqa8R03_M821_IyWoXkIl0mkZUyOj2E5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=TqHUR2SjVFWXj34shVmc3zB_r157jwJzBbOhIXBOLbfuYSUQYK8VtNiQE94dNSmWjHEa0Is-oxyHvIljHTIx82-nUMfrAjrnPJMhl8aPitvWb3AvF5CU5212LTAJTicuWgbuc8y55xuhOkRjDzZPmjVLwI9z1F5A7sxWntwdj6j2nOoRulYZWh4ROpzJ4eZska-Xcxr79aL-e5uVRq7Fp_VKK9xWmoZVpqjdilZ5_jJMurlfocOBxY6pYWnBQMQiELe1kmQ87Z7Seb-l2M0jSlQ4mEoCwb_WR95cwujs6ae5piTXzaiaFgqa8R03_M821_IyWoXkIl0mkZUyOj2E5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=baelB6krYSOXDh9XHc5vuxDNOXOZ19ZekdWjbmIx5T4dum5TjmgvhMBz4uHUDWRwvJPTLuKFxzT4fCvVG4TDgL0fbaC25dC2OKp2XNnuj8Azs39KG_Fm2jpP3mC0Lnolww5k_qUkUvmGxhS5w31KLT1RCGEH_66QVbPIuFXzZYg_ExNGJ_ZYQCUNtA1-0SwbyoTc0mXu99dcmJ1xDqIngQXISa9t7TWpYuie0dhLumDm-pTEcF4ZbNfV6aAudY0lkp6RUV7RD5br7qWBREEbWFtuI30HI8DOybfdG1fvOzr3idR8WruotxzuykAPYJ3sbC-20SqKJ4lVjTZalrt_tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=baelB6krYSOXDh9XHc5vuxDNOXOZ19ZekdWjbmIx5T4dum5TjmgvhMBz4uHUDWRwvJPTLuKFxzT4fCvVG4TDgL0fbaC25dC2OKp2XNnuj8Azs39KG_Fm2jpP3mC0Lnolww5k_qUkUvmGxhS5w31KLT1RCGEH_66QVbPIuFXzZYg_ExNGJ_ZYQCUNtA1-0SwbyoTc0mXu99dcmJ1xDqIngQXISa9t7TWpYuie0dhLumDm-pTEcF4ZbNfV6aAudY0lkp6RUV7RD5br7qWBREEbWFtuI30HI8DOybfdG1fvOzr3idR8WruotxzuykAPYJ3sbC-20SqKJ4lVjTZalrt_tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwKN_AJlbm-VgnDxmjLVXrwZJZTs3K-fTfAcWexImFkXKPMtrYUVi-W5KN0CYa0AMgniw_W01vIfwtWU8LjRoyJv14_G2-Jq7U_njWvNpnWoPOad0UiINfxUFx1SUVL6fEspzVYTKgl5ojQxxyYZOMd5OyrE6ifs6ZMam2O2HkiVtbHq7pEwyJjvXL5bQ8kkJ1sfzbCMRjBm7yR-A3teTH7IpNc6RB9fefSLUL27rmIzQDczj5MC7w8iEQ0bRWr4DOXn91_AzdQDJximImOwAim_1gSMOfcrKvPycl2vN3YnuTgf4Wi3VvSq9qiF7ZsYtBXtz6fsVKJiGddheqkV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csq-N8bvVfF9RU-lToVE7guJCtsiOV7bDOxqBLDx7WS3OD5k75K6PV_ZRB1ss56AYtdCSWWGibWKeynH_X3SLIWR3UNFBd9ZWDHtTlp8-vyRtFmQagKsF95SbgTd4FAvr5BvX9yTtVJvETOWPo335EMIcmNwYB4t0WEJTKYOF7mIXJ1qXni5zeOKP8XBNzBsr2e87KltrNnSz6rvzOFXYQpR9K3zMWcgTsDUjWol3_5S1IuSZtrsHk5TGpxtomWYT6R9Ltm-diQ8WwB3OxA7vYirIAHUUheIzz6NY2HHeqEMx7eqbjazGIrCNNLKU4xXF59EyNJQIJ14ijKSFggq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE6s1s3debICgz7wkL6goBaKIu47G3FsBjkYHs14jMlQeTXL9enurDwFvS6AJe8M7JRmzvbwlWGIiao7DPDOsmjoB1DZdsC_9BoVJ383Jvgwn5DbRUfNxqnOi3oG2s2Gur2jtfhLUQG0NDX84jPpRGNRCwZU8voX1g6CsYXzjlVH_n6MiOJPWp45w5YHKqdjLULBGGY9wCDi7sty9W2Sqi1DShkDKpUcDZdm0YGCVF7nTf32zkkT9T6mI6zJ2kGIjctX36s-ZxA5cfahU2kW56Fr51lVzuz6B0_w-qYT6twgVFg0i708zbE3mmxi8P4au3I9-OzCW2mBpwDeqHMLog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnQ4L4Dk8WZT65lIx4h3ObUrnF6JGMzZK0TI6jGlH7An6XutX12foGmuc3xkQ_O_GMBFBw1oCK3QktXwbVwWNQMwGwbyQD3f5ya9mUKEfMghtvvZmx6h9aT1akTZFUfnCUJEn3TX95k658SioJfvrGhZD1By6LZZXI7G61Klf4DbCSy3HHeNEDaO8W1IkeIEdfarH2b7cDEjVyZiy4lAc9FldzeHHibd4XEOfAUh3FOZn9E5mkYRsLhNLpK4XgRDddO9RNMq3aOAXdb9ZiH3aoZeAyZbwzoEVTSE827aXGYqhpPHTGegvQ5-op_TBAWKUhtqBHATWriELrk07suwpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5VvVTa8_SICUy1snK9Ge6Bum_EHp2IJJMvMxfaWEzCTaiMNRy5gXpWquULOpNJUKlUduIfFsOYXUkJI_UN7jk6TjQD9xdXhfG4GtcPEzKFWFLIDrYI03VBFnsRxBVrrJOvQHBofJ_ZQTAYz7PPYTjB1B1XQTmp5eTMr5KKslYLt6X9ufAiagK4a_UtppeNXxwm7IqUeukP_G1xEGJnd_xYAQ21PB5kZIZD-fahFwoaL9oLnDYQiuhq5DCZHBut7u7rGJdRbmlRp6zXqbA7JBb_9XBzgbw5KlWx5dvTOlxDtEk-IaiSqiCbMGcEzg7sToNfC_CIXk9Tr4ZrifSOuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXvUQjacBs-ts4C20BpEqdL5uysV4iXYN9Nm9dcpG7Hfy5ysr9VfkIk8K0KuYt6mHX4ry39wsdZ44WakWgyTfVr_otLbt4WCC5jYdJW-gcSQu9ZiZx-Vn6xeqcV3CLRG1EiUEzcUXcoFAx9bVLDRmEeZIpvVoro3JLDRsK24qR8H7H93-7gIFvyeQd_eKFefo-oP_4JokATTZEPylm6VEV0sgLGvqO4rr0ZLa_RVRe9ToR4z_wUe4TvjeQ8vM29JrEL77ZgJtlbOK68O6GcF2DqtCm-EQnamSgn50YyecEzez4btjI-wb6ewIKqB9u8MdB1HGSBP_pUBEYO_6hSIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LigkJBgfRMke-DUW4aXh6lWRp1L7G2NGSAxQkUWPFbUWu1lFSKlCJIPLM0mlXwYJVEV8XAEBT7038IP1cKrGFu0BypQd4zToSBkhE1aPuile9JxrNYcoWuE6yMamRjOyqbAcLFsmD4MIHksG9dGOyZJc4h3wL5AlN5ByyWWP3IB680Sq5HT6B5qLGLLRcCM3Rt16VI1CUH-jGN94V3MEPGvbol9dk4EHjXBI7R3shZOKHtpefyym21WG_Hs5ag5J_Vg6246XcJpScismsHbjSRXxaYOUrG8Yd8Hqacjn4Uf0CUraTbtZ_9bhHSRoAV8PSNW4J1E5_s2jMGpnIQvFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcfUmO7gICMEkaDgXBLhqQPkHSzjHB-85Upga7pVm1BtKRurHqn1DjLo--_GXsBEsj8dwbnHLEM7riG2Ab_OMcZTGWGJk2Pfv8Dt4vspLkjbWIjpc93b0na5mSsX9TTlH_TN-ZuemgErx3ybZMKiWrepT6bu7ft3yiuzF8JFxjP903Qgd-5QhT9xZkCAd8z8JIi0HZLPbu4d5syUvXoEWuB-9lwJjl1Q6-2jlc-CSFUJ43Zcf4QCZTW1XaZf2fRkU06Qk0LNv63IFoNk7hqA10w5Tnsz5cy-a1LvDE4WucsgNKXFs7dSiMRL_JVUtyn5V65to2PzJh-6ZqSst0fhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRajMtYPUtU-QqPNb4AqCN9mcx3FAhrkHIA8vtkq-OwLCBMMjD7FJiLNonAM7M_CncSZ-8r8vaA5JKrz-JXdAQyYk9gVh_JRqktVUV274qW1A3xliLnTgWfzhkM1bdnKeYowdvKCCYhlEgZDhermjEthKckFxK108IpgWUAJzSj7SheXsbqZ9NP7tXoKyg4Mwi-hQUsVXhb8CDroRc8PnJ0ofNzLEjWQPIFrvci7XqfNZrlnk9TGiYwLytVVhISbYQEKL_4rZmRXxNL2iB5T19wMv8ZI8CNorufRUb1QH4l3va-PwdJZT_-eAAn7y6lHAJqrfe1eCr_NsjOAZPiWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXBL6fGRzgJRbRdUauO8YF14js1nI7FVoDzXoFU6ziNeeANFHN9wnIq4TzPhP3C7nkGXKPgnCtsCsKgU_pE9XSulR8tINt2Tazpiy37c86aNYP-uW_KTzkAE_nv9030598cc6-IxczxyWB75vGNCEkvQNrsjxWWExd3GZAOPCXGtuMdTr4bXXwSI4RSagvw2dFqVjkStZRXKIfyl7T60TBLfa_fFXDcYFn8IYN8LVHZzidsm3ZxDMAnvNBDw9otJcfIG0uCNEFZMIjB3tgDZRKfsXrp21jmYUCYx9D6ijMhEn_svUE-Rrl7qIJk3f1NwIumqIvZdgxYFWDmeiJhUFA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o3Y5PGfRmV96PlSf0wUH0F1kP9mvpO8BuwWJxvvjgq8RAj0GKGTLnGrOrMok3lngSgqlHLDx-iY7zi1J_Pc9W2SCAJqd_cyHCPA4fBBKCUDYsdTAX0BzWMuitbV9bJpyd7mCfi45LbjMakD0zfmRGl56a3CMijYisQOJc_gFeiPI38cdsXjdX1sz6zY2i0bgOouWMzLh37ONYBR7wPW0Xygz3RNeX_uGHuoiH9srMp_Y6iU-BZj55zOC8P1dun3i4lVFWWT8Pwd_lrgLNkH1X1LEnMosgApYfGEMEQcU3ogBrDbrId6utp6RMfxXuwQOt8gV0A5X1E4TBhvA8lVCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o3Y5PGfRmV96PlSf0wUH0F1kP9mvpO8BuwWJxvvjgq8RAj0GKGTLnGrOrMok3lngSgqlHLDx-iY7zi1J_Pc9W2SCAJqd_cyHCPA4fBBKCUDYsdTAX0BzWMuitbV9bJpyd7mCfi45LbjMakD0zfmRGl56a3CMijYisQOJc_gFeiPI38cdsXjdX1sz6zY2i0bgOouWMzLh37ONYBR7wPW0Xygz3RNeX_uGHuoiH9srMp_Y6iU-BZj55zOC8P1dun3i4lVFWWT8Pwd_lrgLNkH1X1LEnMosgApYfGEMEQcU3ogBrDbrId6utp6RMfxXuwQOt8gV0A5X1E4TBhvA8lVCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COVTokeQHdlOmF--nHAVpzT4hNkWsFdEr0To3oKlc1prQNJJOLgqyj0agNy2RgS27hp1VLDDSWIUjMlpAmRS4D2YTPxrKnXDhNlKj51Z6X15T2fhaYt7YtqwEeACGoSkOCOExmsyJ3ngUl4CGmLjOd0Td0oloGO7Y8Oqh4mEsCQI4sqzwT13jM3BnsCgIGYykE1uhb_dFwCr3yEv96uReT109zOSPrOy4AyTvDn64o7H2Gw4dTjIY2dISiMxXLYQ4SLh7EK1rdUIRSgEuT7CrQYUE_SXkobU1ToHtArxRovDZftCIj2sstxRnggJoqDNfE-4dWWhvWZ3E39tD1cB1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq3X2ev8sbKbn6hBftjJdwO15cV2tnJ7y3d4c4mdByzPoKfIpW_fMZTaJeZg7L_P3QD6pYIoREpTVYgKKHSloYlbq_17kgqNBye38R_ELRf_46XqJh5xA67q6DbMmMSjcJoYj9HcQrmBbl2QeXHPBkEDrWDideWYcMmKj3LL1sSNdOvjiSbutJ_Ub_vHO00tDSF5pru8lS76J8HDiPmYSK2O7WSpktDW_93wl3pP5M5hOXNkdv7ImLWkURFTePQ8iMM9HPQx_G7R4CXPZDFoR5iJz3NkQwVnPru8TIEU9dpeWEe48zPAJ8S3xDsXWiQSZBzTeE0Csctwri-kNTEgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
