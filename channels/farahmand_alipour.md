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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=SPoBo8hg3l-YY22p1vXygXI_QxeEPfH9rp1iir-W9twoD-4StLDUzlbRWBUqhRA5zdif17SDqn5mmdDmykltX2Cm1PiY1oO5mCqLnqqZkXVAps-QvbGGa0uZ_UTQq0W9_-SyhZFKx2MSkTTUOhw5ba5QFazfgIyWk3sH9fw62ExV8RHtalc_8RH_hX_LDVKpgAZiFX17HauuhLCCUkI9SRJxssEzmqxoYJzd7Lj0NZZzN_td9Iv30TIiuz_vVcfdNoubwz0RedlXaq-eLh56QeZPs2p9GDLPsSIE1r1fzBjJPfE4L6HabM1Ba04t_tBrh1FcUvpl2dAKMshM7BFAaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=SPoBo8hg3l-YY22p1vXygXI_QxeEPfH9rp1iir-W9twoD-4StLDUzlbRWBUqhRA5zdif17SDqn5mmdDmykltX2Cm1PiY1oO5mCqLnqqZkXVAps-QvbGGa0uZ_UTQq0W9_-SyhZFKx2MSkTTUOhw5ba5QFazfgIyWk3sH9fw62ExV8RHtalc_8RH_hX_LDVKpgAZiFX17HauuhLCCUkI9SRJxssEzmqxoYJzd7Lj0NZZzN_td9Iv30TIiuz_vVcfdNoubwz0RedlXaq-eLh56QeZPs2p9GDLPsSIE1r1fzBjJPfE4L6HabM1Ba04t_tBrh1FcUvpl2dAKMshM7BFAaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elcHb6yiaUJwvLFRbeFQsgJbActSxfuHDrkteD3bxxT-6_oKthVH84d_6KVb-kTN-3ZIfHcE8EfxZy4RFVnWf5z3I4O0urswAFbBHUKgHj7JFA8G1VVFjbqOWlFTCGPVqFQMRrc7wMzf9emysD_RltengCGxm8PEMqUqas8shVXq319Spz_X05uadiLhPJbvj9FLf8GL2nc-q5_kEVMFpfhD6E7_k62QvPeeTatun4mstv5VRBkFKH3mzi6i-czpLjYjmjNHxj-Wgk5xQQISOY9jc8PIIQr0DrG8-dKNWxvPVh7xEiBlXhOZQsraLtCEPnRR8D-n5kaAW6DZsW7H-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCsCadPeFAnMKETF7kriyXUpwIqf4-mdtiBS78pdpgmNUc6sZ3pshQCHHtKQdtCkScLEs7ST-pG60GsQ6Zs4V5pYGBU3gN2D_646VBc3VYzmfCZ_7qbCegblh1zKr6hoVXuugU5Mal80oq-GrULrkf0Mje8vTDuzunt9AUzqtKs4VwSS9VGqd4LmbjOQNZyN4Ed71jWkbEks9P-H5J1FkGhV77ij8DGtTP2yFZyHwgusvhGejam6oSxxUCLxoLc0mdaPKavsNN2Xk35Z0krW6HlccFhdUaox7zTRY4Wq29yyTJKGRxiITLjQZ4H7pRr5ubCfBIi2CnuWbG4NoemnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id-dheHcdtYht02c-arrytuq_OCJi8VcLv85FGF4J4qcGzJcI1NOeOhwp3qfIhBv67sPZwYEG8qBWC4-zHMa25D4NdQg-SAZSJrVDXFWjIPgkXG_PrgurePMJayI5CJ36RaV3rP7p5O_26eItXLFS_aXRF6m5r5dykUvevjk_ZYBVTEb_An5fHJFKeUcdP_MB7NlSLL_f28lDJIlPIVDVGRAPFLEwCD1LbMT-vGdOwbX2R3Pj5HA5a7P8ftIFYK9I9ktJG9z-B4Tz2fwgmNOjcYlc6a8O74MugNZZHeO9WdjK-_nZ1FadL325HVBsfb8psEa0C4viFfjYg7UjOmskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnAhhrWX8t3FMbU_GfrXbxWhLylYb6yN7jmOLPbLk73_pn6MVBNi3FhhWYUhBO3Vrlf46VNBruH0Mf-S65Hi-SqbJX-aJ6vXK4fDcegyAd12RQjN3jV21XkRPpbP_oFGv0yGPDu3teQuEld4yeZZpv0Vtn4d2nhVVtZXfnQKK6W4AlTtOAyodgxnt9jQTB2u3YvUiNYfX1soCh2A11EI0SV4EiHFX7X49Lr3daPW5ejS5UIStUqiqRG77zas1I7WZF25iaZtJEY-Qpc8z5TaIKP41u2NeEHeNbhpZ6VG73eVuC5jKkDXQOomXlRFYQh5AF2huiA533WY0JQr7NV5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFgUigm0gZOkwOVvrgpR3ePHoGg3ZEbJ3lGzm_ZKtnW5nEVlX8IH87if9KaR2mFWKUnsxZCFKG-uvpU9JP7dzBExccJtuHRy2H3x0Zapa9TSRPa1ecJ_Pryk7fhoqpwjwtGRQzlAhw9NN0JYDz9oCunwuB7dAtERt0wu7uB4Eu41Su3VYDguzXdP3-ndAJLsrLPCDBLiJ93PzwZAcwOhpkpS3h9P1Giw0ToyFp__inmm0IEKYalsoARzYJXkKspix_Ieeg39SSbMw3YDFYiz06sRGbA-YLIDJnP3l44U90XCCLvXa9MpbTISpjXxaVPLDB59m4WUjADmyNsTxWU6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=vYJzvR6vVbx1S1Um98jrBdSk6o2A0Wi9VJVAWC-JDcZLv8t41KpIWpU135mxYxYXu3Mn78TdxPJyPUKBYGXIoln_xFupr1vj16wwZi0xjt51wCBBQg8kUvaH5Lpx02gIKs8u43agmh7HUBYr3SzqRfem3eCtCxRTGon118MzL1pWtvTK-wg11aIbZnPnHleXhSjIaaHQ4pJzdMj0mffkjpeK-3I-__DxVYAaFo5uKGA8HA8hiecvQRaDZWzupQOJbpgf8-fg9LLv08NqC6QDNHftKpqFcWSPMBc-twL20l0jMZPko9HC1HrUP5q7izrbTH37d3tZGRGt2CqETFrzHCaoR27b5tnpSXIM21eDN_NDQfAeh9xgn6YlSCforJc_6krdueG6sKlMPnoKSc3gulXVmZcIe_vtD6hXe5EY-AhBKnjRiq0s1-6uujFllunZzNgYD2rgi4qhVbuzit3CWgWPdRaPqYfySlFlJIcg-h8veZwNomfPtQG1twqyLRksjLudREYR6z72cpvdAnItWUWzW0LxnIYvTyq2rTR2tDJJlPSs6kcBPC8j_bzjsHGwiH-8un2gCXmsPAz9aUWp6zuCDR7Vmw0fkEAO9lswt4k3RY8yG_xaIRtZQ_RHcrnIvefoWaOZeMzD6MabW16Z9RkGiystj-txU66P74-YhUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=vYJzvR6vVbx1S1Um98jrBdSk6o2A0Wi9VJVAWC-JDcZLv8t41KpIWpU135mxYxYXu3Mn78TdxPJyPUKBYGXIoln_xFupr1vj16wwZi0xjt51wCBBQg8kUvaH5Lpx02gIKs8u43agmh7HUBYr3SzqRfem3eCtCxRTGon118MzL1pWtvTK-wg11aIbZnPnHleXhSjIaaHQ4pJzdMj0mffkjpeK-3I-__DxVYAaFo5uKGA8HA8hiecvQRaDZWzupQOJbpgf8-fg9LLv08NqC6QDNHftKpqFcWSPMBc-twL20l0jMZPko9HC1HrUP5q7izrbTH37d3tZGRGt2CqETFrzHCaoR27b5tnpSXIM21eDN_NDQfAeh9xgn6YlSCforJc_6krdueG6sKlMPnoKSc3gulXVmZcIe_vtD6hXe5EY-AhBKnjRiq0s1-6uujFllunZzNgYD2rgi4qhVbuzit3CWgWPdRaPqYfySlFlJIcg-h8veZwNomfPtQG1twqyLRksjLudREYR6z72cpvdAnItWUWzW0LxnIYvTyq2rTR2tDJJlPSs6kcBPC8j_bzjsHGwiH-8un2gCXmsPAz9aUWp6zuCDR7Vmw0fkEAO9lswt4k3RY8yG_xaIRtZQ_RHcrnIvefoWaOZeMzD6MabW16Z9RkGiystj-txU66P74-YhUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crB3DrlO3WyGFwQZ0jVWadvTTbBwQr6L0sVAk9LeecTdQPo6EEzAN98ufcvObbu6hxcjf_rfjQVCQlVVHpKpaGe0idj_KlDph93oDDBGu0QuH0YhmycZUhK_3i8u2Ofyo8ErfswmGWB9y-01sLHqSpg6iEN1_pXxRZeNy02TkvuglLY4P39g_MwN2mqEsn5CJjPhPEC1Q1eZkI2Xlyq-FKQK3n6fdu2aPClHJ_grSqLSKuucE4CuMc4ZponlQ3OBfIXEjrwMNVUuX-SgS-DxVY9R1bk_jKKAVTs4Io5xyv4LuBwa9MbwPQEDe_7_bzhp5bRB27TfHzFxO5yddqC6Cg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Ujr61Owe0p1TyhMIocwOglgdk8k-p2pERvuDcQNdhfo7Vd6JqE1TlDp_AOY33gyv6Ew9Nvh6Dyhe2be_0Z2uwmcuLUy9nXhFlpw9_jdvQ4uVUzE3C1Z1AxH4DPdQuJ0dUuzQelTdlu5Q4XkJDYULx3KfUqOs5pNGIR767I5WPzY0J0h1Q_k6iA8jp60QBb1U5BHWi3BOOvbBsRdkGaBEa2HXyKmEHmwgfYGkw3NYH61YHkgdeWtOn1N4zubymo_sYi8v3itHz707lccwby-ItWb5PF3CuqrvTEmDA1Ol2zG7dkOCC76pc0n-oD1Wj4advysdxq8PuypTqGVtFXXPZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Ujr61Owe0p1TyhMIocwOglgdk8k-p2pERvuDcQNdhfo7Vd6JqE1TlDp_AOY33gyv6Ew9Nvh6Dyhe2be_0Z2uwmcuLUy9nXhFlpw9_jdvQ4uVUzE3C1Z1AxH4DPdQuJ0dUuzQelTdlu5Q4XkJDYULx3KfUqOs5pNGIR767I5WPzY0J0h1Q_k6iA8jp60QBb1U5BHWi3BOOvbBsRdkGaBEa2HXyKmEHmwgfYGkw3NYH61YHkgdeWtOn1N4zubymo_sYi8v3itHz707lccwby-ItWb5PF3CuqrvTEmDA1Ol2zG7dkOCC76pc0n-oD1Wj4advysdxq8PuypTqGVtFXXPZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njj1y7PofLjrDn5a97vHpxJyQ40EZFAYWXpuPmlrvAE4YgvQcFNxBt2dV7pL18htQpMJRJKCYkrGrlZvUIDn_IU3sjZo8W986lzmQ0WciRa2eGsCm8sKlmLG2F9S0SRx4bdGU48d1Fc4m62kTIGyLleXA04wKdQDBHYW753p8iSAfvTWYQqWgtj_f2BL40ngEqiblPvX7wZ6PYuscE1regkGi4MqA7pXUDZlsYm3KyV2zIAsP3jD3plBkWJCU3eoc_wxX9fn4Wihfi8yLHqQ4AtA_rmwUUM3rOX4MlkGDHxqKBx9IkyvF8ePefAdAJWOCxleAU4AGIOEO1VOipRtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prj2RL0wSQkwvAdFNQPVXTRunJSW4HNAl-o9yCBSulySpruwoWmVNYjoeZkEUX4W7lEsWiqiuFFXG5OGlkudLKMdal6cWhnF7pn6tKtcyJllWcZGdGhCpHxYg2-8QxnxwEhE0Obr26brpxcDoVF4gGq0TJzkI7ahSZWzgahSWIgnR6TVQW7XwvPOxWXsnj8Hd9gRlZPgY41WHRZHSdC30eIQgtXw4vu2NjORhv3kanHtV6bCJpAX00lY22E4N-e-fU_qAoUpK3MKCrhMVnx1WtD0Neqp4trWh8poio7uAnxOxaM6XYkblsfWKUN8w68xMHzFGxwUd8WfZMJNRrH3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBYkxi7IKGucwnuynW-cN3q4-wdfuAioVzCtyRCahekTXEMqpMyFkY1kxm6sNbXOSsJWLAvkQbsdOyBwgZ_una5Thr-Kod5ORtrCtOBhNK-HXkHzswjvWWNmZtQ_TCBt4U_0qUF1r-zVp1bai8wvHxvbKlGv_YB579D8dJ5SDqtPHNoEeGlGsTR_ZNVFu6hlPUeWcLaK7BjkKefsvCsMzrlrR9rW_30CNHkJovJcvEa1Xl8rYgcAtiwrMhVuvbGEunmhytyzGbV6cPYHgjWk_Vw5K0n4fp82FjkedTzB0ep78bXAd_DXvYyw4H97alLPjmSb4lrSsmGCOGVPE313Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=bJjEvvrQB-UT32HRTJxduCxxJHYMl4OsP_HMLQwRXgv4LtBLRt704SvENb_c8yHoCHaAuA88U9R7Uevfb5HwiGGB8AUHtTysjM9O_dnlQ1vaURTf6KCyLgaOg4fQrp3QIpmb9L-Ry_-YZK7ATdvKt8wodaY-MA2BjQndDVtDUVZTZXW_BaH-3z40vZyhyT_vdLVuZro1jt4mS6xK43dR6hDIjk5M06iLQNV_x9MNqKIbsicpfQr8rqurEUVEGPO04Re4SXRzIWvkE-R_hJ1vhvpiXMhwD_HkEFub7nHLtPr7XLl080cg0oAs9JORnz-vZUman5W9EvU85ZKdw9pNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=bJjEvvrQB-UT32HRTJxduCxxJHYMl4OsP_HMLQwRXgv4LtBLRt704SvENb_c8yHoCHaAuA88U9R7Uevfb5HwiGGB8AUHtTysjM9O_dnlQ1vaURTf6KCyLgaOg4fQrp3QIpmb9L-Ry_-YZK7ATdvKt8wodaY-MA2BjQndDVtDUVZTZXW_BaH-3z40vZyhyT_vdLVuZro1jt4mS6xK43dR6hDIjk5M06iLQNV_x9MNqKIbsicpfQr8rqurEUVEGPO04Re4SXRzIWvkE-R_hJ1vhvpiXMhwD_HkEFub7nHLtPr7XLl080cg0oAs9JORnz-vZUman5W9EvU85ZKdw9pNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7SvyX9LJVWxmP8FGubFQgdRTmvvOXCFATlSS6_NV2n9OXOubf6xXt4RYl_d-2ujcmnvnkr6e4l3r_L9CdPyM7gazwuRdYWQxsAFEVSs02UWuy4oxNkHX5unICmd7iXpTH3pVhodZA3mRzYKRicoNqeeOVx3ENjC3ghQ0WYDsas8XnXpKI_JPlZilsAh67JSgpRLdRso5cRhYRIdl3EulmUNlCmzQQSvUqNMWTbkXMa8E2Pe4rERbs7BSaKNVTvmm2mEKnICUJ1l9CXqj8ZLwdBYZJf7Lt1KVwlFEBdy1LM59-MQltNQNrnCp_kMeq9JKe7pGvnZdqqwtM-IVEnFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7Y4lIRSiqVqLqtR0uwcL0Z4BqLvlWMz_v7j03cP9OME_c3xzSuYOSFK7qBQNHxtw6Ve2G__iN7I6slxQi4ay7JLgxvv66NGuRLlwbpsSzjcvWw84esA6rd4CCJj59hk6VsDD4kNWt5oMDU3270u_5_a77kzHrSECGo4wW8xuoVGFl2Ub89L3Na1cd8qKO_vbDLEhKp86ni0Uzdr2QgEbXzR_OIImUnWswp-TPRSNNh0onzJlOwdO_cD7YQG-6qt9LRHyYtloKfcZh9ZRScUb10JKkn6J4hVSh-LBQfbKOsW9h74lFs0LmgVrzBL0wEb9WcmzsrHj9DsGfTdgGtGfJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7Y4lIRSiqVqLqtR0uwcL0Z4BqLvlWMz_v7j03cP9OME_c3xzSuYOSFK7qBQNHxtw6Ve2G__iN7I6slxQi4ay7JLgxvv66NGuRLlwbpsSzjcvWw84esA6rd4CCJj59hk6VsDD4kNWt5oMDU3270u_5_a77kzHrSECGo4wW8xuoVGFl2Ub89L3Na1cd8qKO_vbDLEhKp86ni0Uzdr2QgEbXzR_OIImUnWswp-TPRSNNh0onzJlOwdO_cD7YQG-6qt9LRHyYtloKfcZh9ZRScUb10JKkn6J4hVSh-LBQfbKOsW9h74lFs0LmgVrzBL0wEb9WcmzsrHj9DsGfTdgGtGfJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=f7HxIUFvmEGJsjwnCQDw0RHDPXa8TYJCtsCMhjFmxxxgQ0gBJxTdVZjiqkWUwN1b4KedRY6WHBFqTt_WBFO9NZaWEIJ7Ygvi0W2BPFzON7klW1xUtOs-pRPTU5ruTdbVi0zFbi4eFRDRTJdliiCYH3HgT04q0ZOEM5ZazdgYXHuzqy0CwVP1dJBlL104UCZkmXqEL_5lOFSFrDLBz6jh73UgYMrNRV57YuByZvNw8SAN4DhMOxriVgg-HyQXyyZm1z0EDkSDg3Utiw5DSuTUOovVZ3rWXLxLPPtsW37XHPRsFplW7QbhEFuQSr5BsRrIOJVXDJKN_8NALxrJY90ZeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=f7HxIUFvmEGJsjwnCQDw0RHDPXa8TYJCtsCMhjFmxxxgQ0gBJxTdVZjiqkWUwN1b4KedRY6WHBFqTt_WBFO9NZaWEIJ7Ygvi0W2BPFzON7klW1xUtOs-pRPTU5ruTdbVi0zFbi4eFRDRTJdliiCYH3HgT04q0ZOEM5ZazdgYXHuzqy0CwVP1dJBlL104UCZkmXqEL_5lOFSFrDLBz6jh73UgYMrNRV57YuByZvNw8SAN4DhMOxriVgg-HyQXyyZm1z0EDkSDg3Utiw5DSuTUOovVZ3rWXLxLPPtsW37XHPRsFplW7QbhEFuQSr5BsRrIOJVXDJKN_8NALxrJY90ZeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=qXm4jaV1gIPPUJQ6WO5ulsd-J2l-chr83-cJ4TsWb4WXumKwzpY4hTX4MO1pI2WlZ1wrQx-x0cgKp_PoXCuoHCmmjDslDStZtsgw95ULXHKa0FZ1kQ45sgdCwLxAJwLwr5Hzq5y9QJzZC-yVP6S3ZmxLnJHWxEweFFzSVQIuGm2d4iPPyg61y1f0bZ7_7005X7WCzxZf-NgDOWu6hRnFSjABnxcDOK1bMrPtegSvA1_crKP7aIEzT_fcbrAFoIQsscJaF9mLyK5K1c5l11tWT7pkbWsUl3VpKXcADw6q3DutOgqUXE2G1Y1XlA2wjmUzOdrmM1ynNGGjA8B-UBiDtBYYUdRnAa4I57jZoNhp3Zr4LUK2c4BCYpwzKqTbCLaf7BXJ5sSxyQukgQlVeZhRssqMIa-YAW5q6TY5YAN6Gz1J_OcL4aSYhqlC0RjEHJMOkDkpbDjG4JaTiYxzfOpOfBJ3XgpHlwEns47fnwtV79pQdFi87YqVD0E6scOWp9dU68PG8CI20KG2DouN4Ou7b87RBKZ6sSgwjOdgdAIGPH49pQ2ofrXl7QEDZEM846mL1B_id5lEPu5DmAY7Uqn5vk-P_GTjg5fuYyYpF38m9DmQgqBkFYw9fK773ghc1tCzDPpjy1oH_fIBTMIXiRDqbr5bX4sARCBD87v6W-EkYDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=qXm4jaV1gIPPUJQ6WO5ulsd-J2l-chr83-cJ4TsWb4WXumKwzpY4hTX4MO1pI2WlZ1wrQx-x0cgKp_PoXCuoHCmmjDslDStZtsgw95ULXHKa0FZ1kQ45sgdCwLxAJwLwr5Hzq5y9QJzZC-yVP6S3ZmxLnJHWxEweFFzSVQIuGm2d4iPPyg61y1f0bZ7_7005X7WCzxZf-NgDOWu6hRnFSjABnxcDOK1bMrPtegSvA1_crKP7aIEzT_fcbrAFoIQsscJaF9mLyK5K1c5l11tWT7pkbWsUl3VpKXcADw6q3DutOgqUXE2G1Y1XlA2wjmUzOdrmM1ynNGGjA8B-UBiDtBYYUdRnAa4I57jZoNhp3Zr4LUK2c4BCYpwzKqTbCLaf7BXJ5sSxyQukgQlVeZhRssqMIa-YAW5q6TY5YAN6Gz1J_OcL4aSYhqlC0RjEHJMOkDkpbDjG4JaTiYxzfOpOfBJ3XgpHlwEns47fnwtV79pQdFi87YqVD0E6scOWp9dU68PG8CI20KG2DouN4Ou7b87RBKZ6sSgwjOdgdAIGPH49pQ2ofrXl7QEDZEM846mL1B_id5lEPu5DmAY7Uqn5vk-P_GTjg5fuYyYpF38m9DmQgqBkFYw9fK773ghc1tCzDPpjy1oH_fIBTMIXiRDqbr5bX4sARCBD87v6W-EkYDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JQ5EDrnJ9TnpXPaofJHV1dZfUTOd0h3QLKld6OQCsaX1D4mNGCMxvp_PQ3WQ_cI163p4oK7uzR3bhnOmKattfvrQqFLheTbg_arydSCxLeqIKSGTvOYv_jJXBnSNOF7fudY0c0Xlg8-Yv3mLysI4luZRuMgOz37KhicV91UM6WleKNGmnjqFVQeyVYE2zVi92jc0_rvvkkbdIr0h6-gxaVDDHAJvrfRrElIHCbpPKQ1UmaKO5Kg21ewhgmpEz0yMlUTYVQ1RyLbvWcblz51FXqC_V1ouAu2QOYDXbaCXQqOZFbG9Vvl73SDgdiAWSbOb1x08xT6NFdBxj_c-YJDIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JQ5EDrnJ9TnpXPaofJHV1dZfUTOd0h3QLKld6OQCsaX1D4mNGCMxvp_PQ3WQ_cI163p4oK7uzR3bhnOmKattfvrQqFLheTbg_arydSCxLeqIKSGTvOYv_jJXBnSNOF7fudY0c0Xlg8-Yv3mLysI4luZRuMgOz37KhicV91UM6WleKNGmnjqFVQeyVYE2zVi92jc0_rvvkkbdIr0h6-gxaVDDHAJvrfRrElIHCbpPKQ1UmaKO5Kg21ewhgmpEz0yMlUTYVQ1RyLbvWcblz51FXqC_V1ouAu2QOYDXbaCXQqOZFbG9Vvl73SDgdiAWSbOb1x08xT6NFdBxj_c-YJDIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSNu0rKNEfABi_YPpOmsGGbNAg_vtSHXCyU1ltSZ49dszbB7Qi0bU8yaJOnzeSqXPIadujsQormM5GWzJd8P_MK6Xu_895BkpqvNB_bg_wkhsV3S6lUbYpXtThTm5zFNlyHEQagrK_NuEhCBCq8NC6kBqm3I2-t9UYmQ9fKhjZeGA8yrkQaoazKL_KIY8HMar7ZPQS_TOZNFilOdquDQpHyMVyDmT--TT3ZVHzi_kO92EhJwn96ERJ3Tl7faUiy7NkX4_Z4z7NKeON6Q19x4DmhpRy-wdJE_8-hFLXxE5KL67_owlXyb-juWV7CfV-lXEYaQeE1CGgXGvPIjWAgWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=s84M4sbdHewWGSAFW3KVu13P159sDXbI08A7QpjWULIqwku6eD-FKeXjJEwfX4dwoJzvfyP4Lbo7rNjEaLqmxePUjeLr_g9ZAcovWG9-bZImPggavV0z5EYQibRCLpKsNe9fVrnbkTQJKBwe1bS_4FlcFdzmcKKk4beEA11VqJfG1r2corK8twvY_B9QessqrqB8-_cK7JPtECksm91IX5MxzTdxodDXPjeViOPu7q_K8vDJt6MLGD2JugAWFjddn9xFz3b1MurSZa10u8nekGncCEUXMkR6j6qDkH78JGKv_KD1k4SuizPbI4aqc-8IB16zNV7IWZjZ4abLNQUR1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=s84M4sbdHewWGSAFW3KVu13P159sDXbI08A7QpjWULIqwku6eD-FKeXjJEwfX4dwoJzvfyP4Lbo7rNjEaLqmxePUjeLr_g9ZAcovWG9-bZImPggavV0z5EYQibRCLpKsNe9fVrnbkTQJKBwe1bS_4FlcFdzmcKKk4beEA11VqJfG1r2corK8twvY_B9QessqrqB8-_cK7JPtECksm91IX5MxzTdxodDXPjeViOPu7q_K8vDJt6MLGD2JugAWFjddn9xFz3b1MurSZa10u8nekGncCEUXMkR6j6qDkH78JGKv_KD1k4SuizPbI4aqc-8IB16zNV7IWZjZ4abLNQUR1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=q_rTjXLR3MF-IkX5MVjY9DmlDcJ-oQEMxtKo_3tyzbQgSwfOgh5RsHojH4JohVizNxhqoUB4Jwzn_47LKklOwlzyx34SldYLU_LEed20aFiZLPep1r8n7d03Z1ys7-jrHSzFJdEA4lmI6d-s1N0MQx8zxF3S0K2jNvuUtdaIfJVjN3MW5JP8wSAqDe6qQLdzXrtIWorxpqNtULyZVjaroRehfyrWrhZY5CoYO3n2lUvROnnFBGQ6xtw074gXK4iM0lph4bNIUukgaTREcXOLGKzytHcJ0IDMqGzMIN5CiuhUjYRrCdvqWJ3OPcg31xGACjl8drgUnD97WSga1FrGv2MU5fxU6unSZu2qNR5iwFxWn5ZNRRnX9PKqPqnNw9JDWQy8mzN8eZxicFAmymoXUBsHqtxsi56vckzvv-V_D5NwHeoR3cJ89gWYe1FjHT_nGw38kWQhxbzIZfCdoKNJG2iVEGTRVY--FGT8223ZFMW65UPQnIMKMT7u3InWWsP4vYeKkx7trgKdIffjACfHgsDxmKTiqQLdS6k6axpgTvx3fMcLOAsdN2t2lD7AwgZYGEfjOBgRlZW9kZeZJwOPtSLKjOK2ljjroMNWoFJLHa4vo8BjYJBWYa5o-pinzNfQu4BL2iSCGBpTHKJbQW14TjJTAxAMkuLi-Pbb0pxz0JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=q_rTjXLR3MF-IkX5MVjY9DmlDcJ-oQEMxtKo_3tyzbQgSwfOgh5RsHojH4JohVizNxhqoUB4Jwzn_47LKklOwlzyx34SldYLU_LEed20aFiZLPep1r8n7d03Z1ys7-jrHSzFJdEA4lmI6d-s1N0MQx8zxF3S0K2jNvuUtdaIfJVjN3MW5JP8wSAqDe6qQLdzXrtIWorxpqNtULyZVjaroRehfyrWrhZY5CoYO3n2lUvROnnFBGQ6xtw074gXK4iM0lph4bNIUukgaTREcXOLGKzytHcJ0IDMqGzMIN5CiuhUjYRrCdvqWJ3OPcg31xGACjl8drgUnD97WSga1FrGv2MU5fxU6unSZu2qNR5iwFxWn5ZNRRnX9PKqPqnNw9JDWQy8mzN8eZxicFAmymoXUBsHqtxsi56vckzvv-V_D5NwHeoR3cJ89gWYe1FjHT_nGw38kWQhxbzIZfCdoKNJG2iVEGTRVY--FGT8223ZFMW65UPQnIMKMT7u3InWWsP4vYeKkx7trgKdIffjACfHgsDxmKTiqQLdS6k6axpgTvx3fMcLOAsdN2t2lD7AwgZYGEfjOBgRlZW9kZeZJwOPtSLKjOK2ljjroMNWoFJLHa4vo8BjYJBWYa5o-pinzNfQu4BL2iSCGBpTHKJbQW14TjJTAxAMkuLi-Pbb0pxz0JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR5SCcfikBU9LFArxTPbTtK8rBnowyQyrWz4jf4etO-uurW8pxpuGgs6prJ34rt37aBe51PzuAxfop_Iz7kMmG2GgtbMbY_h1AtKtjKI94JJG575FBCnC1fuj7y4HBzgQGydB76t7PnOaLy_EEMesKoa7TAivxWqtTwvZAN5cBrPslZiT2FbWCfJ2VJyXtBDvZqCjHM8U77tHK9oO52_IgH5AvUeJbsoGdqsvuHGOJnOAQqFGeSdH_7tDgLTcD5AShJ95ri7O2plZz0b_znBJIkaMBUytGpshsBL2aZqMfKTpfFn2v_eWoEPYaVITDrmvHcL_53yUMMI2nM5usgJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=e4NEV7R4-Z3-nA2nN21qMGLeTBMQbz0rRxly2iObLXV6osqGhYFRdjojtmHMAY8f-h8OvMnYeucsacC-MGeBtaEobwH3DayYhrsaLVYxUlw2v9vbQdV7vdVtk0tLfpZdjqsl7xii9Yy2jixVQFzriO9fRfKJFRhQkU33Jk8FKtxPA1cNq7oVQY25e_NiOndx6GT7YasAvY8t__DLSmNDVuylRGwgmAjJskMX4gni_5VmTsTa9gdgJPtZBOEEQdVwALfxffUhzV9KH-j5MkkpJ5Rbq9Xj3PUdaHXG4n-QxDmBTDDOl-_IMfgCLgMQKyRBGVJDnv4RxQksmbrKNKZhwjcLC37ubhTR6NtbdS5cVeBXbd7Wk4KxGLJR7ZvDxc8wqfh83jNPhoPyV734EHKvfzMWGasHm-YwM9APLmpb8m7BZUOKKd1erw5Oc0eab40poeuWsQI9J8UiageNjAJ0DVNOBB7rIdBB-7peM6swXY5KGqWJeMl-9rxLtf-m8cBv5LOIghlVMiUwXi0n1T_ZbmnGXIlv1bS2Qe91BpsiQkUCyaI5DUy5QKBLnTkXBs78WV8pcMBAdbCcMS9YSpniztZyWCsZUDuukYOWIbfJRgBB08NKv_mNl5-tIMkwc9TZ8nwepXCTnaq4INgPHXKO5VZq8im_aJlaX8aea5xlo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=e4NEV7R4-Z3-nA2nN21qMGLeTBMQbz0rRxly2iObLXV6osqGhYFRdjojtmHMAY8f-h8OvMnYeucsacC-MGeBtaEobwH3DayYhrsaLVYxUlw2v9vbQdV7vdVtk0tLfpZdjqsl7xii9Yy2jixVQFzriO9fRfKJFRhQkU33Jk8FKtxPA1cNq7oVQY25e_NiOndx6GT7YasAvY8t__DLSmNDVuylRGwgmAjJskMX4gni_5VmTsTa9gdgJPtZBOEEQdVwALfxffUhzV9KH-j5MkkpJ5Rbq9Xj3PUdaHXG4n-QxDmBTDDOl-_IMfgCLgMQKyRBGVJDnv4RxQksmbrKNKZhwjcLC37ubhTR6NtbdS5cVeBXbd7Wk4KxGLJR7ZvDxc8wqfh83jNPhoPyV734EHKvfzMWGasHm-YwM9APLmpb8m7BZUOKKd1erw5Oc0eab40poeuWsQI9J8UiageNjAJ0DVNOBB7rIdBB-7peM6swXY5KGqWJeMl-9rxLtf-m8cBv5LOIghlVMiUwXi0n1T_ZbmnGXIlv1bS2Qe91BpsiQkUCyaI5DUy5QKBLnTkXBs78WV8pcMBAdbCcMS9YSpniztZyWCsZUDuukYOWIbfJRgBB08NKv_mNl5-tIMkwc9TZ8nwepXCTnaq4INgPHXKO5VZq8im_aJlaX8aea5xlo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=LgklCKmBrm0xLpo-Yh2DFtg6bWBOvexjpuD3pjQHfCgcR2WdhSxB_3x_6qEi2JRAMz-GasUv_B_XETPUzbbkuXsMRV16LckoRyfJGuGyvS7cwx7l34DmrAkmoc4Xy9jhcymiS3r62r5oo97zleeCsH9fRDcxstgDnXIz4rO-4ZzqHatAuLB2wOW_hlGKfvzZW8hjq3ue_BdGf0rjIRuduvodbOQnyv2ptbUwQnb-_FiP4sQM5u49A-O0yU5EpEb_UGE93WCnHZ20S0NRbLAV_fsW8B-ctF_8pCzQRHgin4kdXztzQyZ4cuFGaBuZkrVxF4FIPVG7ji7tHdvEWJD3vzQIw_q-1uiH5hq1C1ZzxqS7bOdQkikY8nefYmTIPk6nkD9Us-G1NkWKUWu7w6HrCRVsJJxYPsR7XEQ_9Hf2JvzyLIaRpqJcnX14ZXBwIHF78L9bwBNoqQor0wJWzesohvjk1qMt3lqC-wk-ayDkosEy2nXlFSX5VX_6zuuIlgR4-0vaAzfsO2_kW55CK796egVNjyRp2eqvQ_NdP9WJwiV7O-pBriZIsEUsOB_nCKeyZhhZlkqWGeXt7wHZz-WIk5SC0WTvzfekcEQUmqiMn5GSnPHSDIF9-02NftraRwcudciw7KHxlTfl_iNDAcC6BdLZ90B1uqiKh9G1fLkVU-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=LgklCKmBrm0xLpo-Yh2DFtg6bWBOvexjpuD3pjQHfCgcR2WdhSxB_3x_6qEi2JRAMz-GasUv_B_XETPUzbbkuXsMRV16LckoRyfJGuGyvS7cwx7l34DmrAkmoc4Xy9jhcymiS3r62r5oo97zleeCsH9fRDcxstgDnXIz4rO-4ZzqHatAuLB2wOW_hlGKfvzZW8hjq3ue_BdGf0rjIRuduvodbOQnyv2ptbUwQnb-_FiP4sQM5u49A-O0yU5EpEb_UGE93WCnHZ20S0NRbLAV_fsW8B-ctF_8pCzQRHgin4kdXztzQyZ4cuFGaBuZkrVxF4FIPVG7ji7tHdvEWJD3vzQIw_q-1uiH5hq1C1ZzxqS7bOdQkikY8nefYmTIPk6nkD9Us-G1NkWKUWu7w6HrCRVsJJxYPsR7XEQ_9Hf2JvzyLIaRpqJcnX14ZXBwIHF78L9bwBNoqQor0wJWzesohvjk1qMt3lqC-wk-ayDkosEy2nXlFSX5VX_6zuuIlgR4-0vaAzfsO2_kW55CK796egVNjyRp2eqvQ_NdP9WJwiV7O-pBriZIsEUsOB_nCKeyZhhZlkqWGeXt7wHZz-WIk5SC0WTvzfekcEQUmqiMn5GSnPHSDIF9-02NftraRwcudciw7KHxlTfl_iNDAcC6BdLZ90B1uqiKh9G1fLkVU-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=OTyzlreOHKZ3UXnNS6hqnu2GeSkjoTylJ3Q0boxkCGWj6eoLbwdPoXera_SXVgwKRcYrDeVcvfHj56h5Kcv7lIxPqnFIhWYQDPjzcp8iCPrRomV-ESBiWweTEOXQx4EvCmOi3S2R6sZIimmyN7nlqXn6k4rz9KuCK8yHLU6p-I1BMRhrTO146p_WjQG7ENZO7zDi-oTcCLXXbda39WdaihExwmafFZ2vOXBllLltUbUJ-JgcAi8Z1qvTzmYi_xPhng3DxqpI1IuW6Nj-ZIChwx_gS1t0Z4m7wdNf7UYZ4E1tfKz8l6KZbuNxAj4W3WNHCYr5nKhEk-J8HuPGHFce2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=OTyzlreOHKZ3UXnNS6hqnu2GeSkjoTylJ3Q0boxkCGWj6eoLbwdPoXera_SXVgwKRcYrDeVcvfHj56h5Kcv7lIxPqnFIhWYQDPjzcp8iCPrRomV-ESBiWweTEOXQx4EvCmOi3S2R6sZIimmyN7nlqXn6k4rz9KuCK8yHLU6p-I1BMRhrTO146p_WjQG7ENZO7zDi-oTcCLXXbda39WdaihExwmafFZ2vOXBllLltUbUJ-JgcAi8Z1qvTzmYi_xPhng3DxqpI1IuW6Nj-ZIChwx_gS1t0Z4m7wdNf7UYZ4E1tfKz8l6KZbuNxAj4W3WNHCYr5nKhEk-J8HuPGHFce2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ifP4f_cpQkE7K0jRigIAMb-Ju0w0lqttejJ06J7Tfee_hZdDr-wA8wMS_27nma70rCxRCTRe_Sg2VqyVg48gG9hhIjMjPfRDe8NK3v__JK6GXjEHx1sF1nBSeNwSaK0xvl6lVbu0Dg1duN-CEh7Z2iEWdQgKlerS0VQykYX8dqlvVaz3PcO9dvLVpjJ3v226QjfCvZjzsxgdhhfffWcpVVo5pkhMQU0eafha-n68QYLiGJOrjtnu9qzezEPVCZTMIkV_igIa3A7K-Hb-Vt6o2DxxWNyJsNsWgYj9xUWlDG5I3ZBRuyQuMSF8VsiF5epI0VGItKXq4k5XvMGvZ2cwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ifP4f_cpQkE7K0jRigIAMb-Ju0w0lqttejJ06J7Tfee_hZdDr-wA8wMS_27nma70rCxRCTRe_Sg2VqyVg48gG9hhIjMjPfRDe8NK3v__JK6GXjEHx1sF1nBSeNwSaK0xvl6lVbu0Dg1duN-CEh7Z2iEWdQgKlerS0VQykYX8dqlvVaz3PcO9dvLVpjJ3v226QjfCvZjzsxgdhhfffWcpVVo5pkhMQU0eafha-n68QYLiGJOrjtnu9qzezEPVCZTMIkV_igIa3A7K-Hb-Vt6o2DxxWNyJsNsWgYj9xUWlDG5I3ZBRuyQuMSF8VsiF5epI0VGItKXq4k5XvMGvZ2cwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=aBT5K7pXqvR44f8rObfmRyGOk1u2V0Hc63agMRVPMYo2u0TElFzKK8QAB2xpU3NPH1OR1t_YXrn3C0rkPvbVC4qRk1P1Acs8yrvznacoY5wJenvQ8Svbq1uz4PdwSHLrojvsx9l-Zo4CJ_qCGdNG7GXFE1JSnkv1r3z2o7QdYQm9mM6jVcQFkePM7u1PRcE0iJ9FLi66aWZaV8Ld2zfPMOknZsC-aLhZ_SaIC4C-oVfs3sKuip8PSC46mn4o2kbZgNFdMyp1m0npWQrwBadOzBHpGg0DEiQcuFflEYXE42NBWz1vbxwfjM774q3eAOMeUNEqPIgN_U7q-EE2E0I6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=aBT5K7pXqvR44f8rObfmRyGOk1u2V0Hc63agMRVPMYo2u0TElFzKK8QAB2xpU3NPH1OR1t_YXrn3C0rkPvbVC4qRk1P1Acs8yrvznacoY5wJenvQ8Svbq1uz4PdwSHLrojvsx9l-Zo4CJ_qCGdNG7GXFE1JSnkv1r3z2o7QdYQm9mM6jVcQFkePM7u1PRcE0iJ9FLi66aWZaV8Ld2zfPMOknZsC-aLhZ_SaIC4C-oVfs3sKuip8PSC46mn4o2kbZgNFdMyp1m0npWQrwBadOzBHpGg0DEiQcuFflEYXE42NBWz1vbxwfjM774q3eAOMeUNEqPIgN_U7q-EE2E0I6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=bF58Ht-v_FEg3yeV5TxiT8uwnTEymg13FeuxWxnVfmpENcMlx5Cbm4ipieGCAWd1Tq6hOP5NkAe98y2FVhHTG-Wh0V8P97Mzr1YKt4zfPE9kunoO1IU0ArM-x7izUYN7ZI-BTRBewCs0rMKhm4uBFPFTUbYza80bhJdIDlDz1kysoh8HQBFJHWU4SoMgkxI6DyzptoV8FdHhX_JLZNed1q34rD_sgK_vzpM6V5jsp9xmnctdi0Hzhins_op1fd1gNaTsYXmGArYkgApsLej-xTnaaHSX4Zlp2wS_iMzOUiG2d8gAtYDOZp-qGBwGtqf1KJJ1-naAelZflMJD79NGdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=bF58Ht-v_FEg3yeV5TxiT8uwnTEymg13FeuxWxnVfmpENcMlx5Cbm4ipieGCAWd1Tq6hOP5NkAe98y2FVhHTG-Wh0V8P97Mzr1YKt4zfPE9kunoO1IU0ArM-x7izUYN7ZI-BTRBewCs0rMKhm4uBFPFTUbYza80bhJdIDlDz1kysoh8HQBFJHWU4SoMgkxI6DyzptoV8FdHhX_JLZNed1q34rD_sgK_vzpM6V5jsp9xmnctdi0Hzhins_op1fd1gNaTsYXmGArYkgApsLej-xTnaaHSX4Zlp2wS_iMzOUiG2d8gAtYDOZp-qGBwGtqf1KJJ1-naAelZflMJD79NGdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=PdmHEcy41waogZPK9XryCFwVFD5OOi2s6QlD2XaZ2hNA1V_bIM8oI6N1lxGJ9VyXUfTOsdbOqPC0jrbSRUcKY97gqhHl4UxGXLNzCvDfr_JkOVN0O-iCHgvaTHNn7m1u0bTE2o6-4FZYN1FA7VzMQlHYtbjIJsFGco3SptZO7N6VVkMXGyzPn7iQOnMq_zt6J5gemdB8iR0pe9AXPj7SP2-dgXzWHDBQytKtjrc2lmfj1tDog7CCAaYzO1tOIo-o02L7A1G1WkDzRdWyni_TAR0lBaf7L0UaY46GJj6Wq1s4tv7NaKmSWdY0ZPubC-fqS5RXj4-e9EKeIMnyqcO6mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=PdmHEcy41waogZPK9XryCFwVFD5OOi2s6QlD2XaZ2hNA1V_bIM8oI6N1lxGJ9VyXUfTOsdbOqPC0jrbSRUcKY97gqhHl4UxGXLNzCvDfr_JkOVN0O-iCHgvaTHNn7m1u0bTE2o6-4FZYN1FA7VzMQlHYtbjIJsFGco3SptZO7N6VVkMXGyzPn7iQOnMq_zt6J5gemdB8iR0pe9AXPj7SP2-dgXzWHDBQytKtjrc2lmfj1tDog7CCAaYzO1tOIo-o02L7A1G1WkDzRdWyni_TAR0lBaf7L0UaY46GJj6Wq1s4tv7NaKmSWdY0ZPubC-fqS5RXj4-e9EKeIMnyqcO6mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=FuWPT_h5QrVkMr4zLo_QlaJcHrPqPGhyLYO3vR9Rkz8U8yZhHURM1yJsocl2E3Bywn0-pmhtcnY0Oynt-ATv_F1h26bl2_ylgm8eV3RPqs6ovZNt3k0qc7U7aYDHip44zAmrwuGc8ta2ldztj3JJwwqmeBMBumwLNjIGAZYAXQai1wizigGRYDzgDRY12TdbONNWzx-6BIqocgJiqDudyWnEbVJTgzE5Rcz3SH8ehYgw7mm_MEV2MIZqmE5eJsbGcOGhVOnNlWxYhJCujZOEXsV05McUOcYQWwesk4Brp-jeD7UZMVrsRk9tYEZ5TeX6rBKcPN2iiElHHRF52TLEfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=FuWPT_h5QrVkMr4zLo_QlaJcHrPqPGhyLYO3vR9Rkz8U8yZhHURM1yJsocl2E3Bywn0-pmhtcnY0Oynt-ATv_F1h26bl2_ylgm8eV3RPqs6ovZNt3k0qc7U7aYDHip44zAmrwuGc8ta2ldztj3JJwwqmeBMBumwLNjIGAZYAXQai1wizigGRYDzgDRY12TdbONNWzx-6BIqocgJiqDudyWnEbVJTgzE5Rcz3SH8ehYgw7mm_MEV2MIZqmE5eJsbGcOGhVOnNlWxYhJCujZOEXsV05McUOcYQWwesk4Brp-jeD7UZMVrsRk9tYEZ5TeX6rBKcPN2iiElHHRF52TLEfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KcE0xonx2bkLVsWJ6a0qdo4QpLJyYIpYUyApOt2D83MceBwdP2qBOgNzrDXEPBokLnrroENkS8obeQgPtie8rpI_X4gqZlzmF6NgSRFi9XVB_dm76XLBjF0LCU_z2hsD9IkNjQRyUMXBzff-PyfUn_qRqv1V0syEZBziBMtUQgM89Hj7IkXXuFLBVVjIPXOMQobpT7CWQzl8w_-ePLq9v04-9M6FU7spgbCORvY4w3z2D1Wp2G1ue4okuBL35r2tlGytOUFsyaf27JxUiafqpgKtbrVbEMkH1gbFElJ52X0f5v8BcvcO263a7H9K5wg95QkIGnZYV_zclSdH5nBClQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KcE0xonx2bkLVsWJ6a0qdo4QpLJyYIpYUyApOt2D83MceBwdP2qBOgNzrDXEPBokLnrroENkS8obeQgPtie8rpI_X4gqZlzmF6NgSRFi9XVB_dm76XLBjF0LCU_z2hsD9IkNjQRyUMXBzff-PyfUn_qRqv1V0syEZBziBMtUQgM89Hj7IkXXuFLBVVjIPXOMQobpT7CWQzl8w_-ePLq9v04-9M6FU7spgbCORvY4w3z2D1Wp2G1ue4okuBL35r2tlGytOUFsyaf27JxUiafqpgKtbrVbEMkH1gbFElJ52X0f5v8BcvcO263a7H9K5wg95QkIGnZYV_zclSdH5nBClQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq7tKkUwlmyp9ffCLA370Bj1nI1xgjQv3aonr6sTciXTkBPdDSyXjoFDDa_FYdy2AQc09sbrQiL1lN-C1kvK0B9N1e4ydEn-niSgKRN-AckGn3hHvn4XabNKCuFhbUF8gmfQ8WwiFs93Xt9vrkElf83h0D-iyPF4YD5gG-60zPZNWoX9uB-xuI9QlyoSUdA_F-_VtM9Deis7IX1cEwLHJPUGV8sWD3Y2oxDNzW2dWYksurRdVnBh7zQHd3eoz50v7D8rD2MuQbX1Yn-hLMqevy8zKxeXUN_bGcDUU1duy-D549sdnsnjF-21DU92SIu04FMk8m3AHfAvuqqTn8EWqw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=cjAYlempY-j2XdKmJa-4yEhM7Hzd5FQBuPlsrC4gDqJWEegJqtACKPT8zs4XD3KzrZDStCBbgfEChWIfOXYXI-8EBfKNYPr5-2AGXzvWPuJuVxy1_Q79xlmezGVmtQzZUV_TwngMmEhgSjkw3973ZXK6vpfmph38tYKO7_wHAgxn93HyPMaOGZYrZym0tCC8K80RL9Jvmzjp2LpUKkGjC2VnotbcnJfGES49iTjNLaIPox2mUNhxIDx6dUa0Iva-55ekXwhbSuMUiF-OKr1QVomEOWhMaFKAP2NCe02Xg13YR0Bt_ZJuZpXAgnIGKw1GsBjDE2OMNFiF2AZeLaRtAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=cjAYlempY-j2XdKmJa-4yEhM7Hzd5FQBuPlsrC4gDqJWEegJqtACKPT8zs4XD3KzrZDStCBbgfEChWIfOXYXI-8EBfKNYPr5-2AGXzvWPuJuVxy1_Q79xlmezGVmtQzZUV_TwngMmEhgSjkw3973ZXK6vpfmph38tYKO7_wHAgxn93HyPMaOGZYrZym0tCC8K80RL9Jvmzjp2LpUKkGjC2VnotbcnJfGES49iTjNLaIPox2mUNhxIDx6dUa0Iva-55ekXwhbSuMUiF-OKr1QVomEOWhMaFKAP2NCe02Xg13YR0Bt_ZJuZpXAgnIGKw1GsBjDE2OMNFiF2AZeLaRtAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fxiNRjrhTnQdQ3tF1vETWMTf6SdKRezU9QZeiHbU0AUBI6tZuOPh-nGt5xGaMYTX-8BqBDHw1fcZg8k_SeUpIWCYj2LaikV_2Asrx1HfAgGKZBbx808l6eu2dpu9mjeNoUQOjxeMwHLkIfDg2YCPLrewYqshYNo8l_ZBP-QTGBSSRGyxPMLBY-NNsw8jINRWv34XmxXMDBC7G24QdM_R5B5LT_rB3qeiYPR8NPlLiuF_JIQHvzSPaXIyct65IjFhRLUvJnz1C_L1ZQZ_fbmZu3w8ekW83bw6N3_DwfSQqnzj3zzVrzDN5LLHQfHYIvOAfgQJBpJLTaPza8X0jzISDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fxiNRjrhTnQdQ3tF1vETWMTf6SdKRezU9QZeiHbU0AUBI6tZuOPh-nGt5xGaMYTX-8BqBDHw1fcZg8k_SeUpIWCYj2LaikV_2Asrx1HfAgGKZBbx808l6eu2dpu9mjeNoUQOjxeMwHLkIfDg2YCPLrewYqshYNo8l_ZBP-QTGBSSRGyxPMLBY-NNsw8jINRWv34XmxXMDBC7G24QdM_R5B5LT_rB3qeiYPR8NPlLiuF_JIQHvzSPaXIyct65IjFhRLUvJnz1C_L1ZQZ_fbmZu3w8ekW83bw6N3_DwfSQqnzj3zzVrzDN5LLHQfHYIvOAfgQJBpJLTaPza8X0jzISDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=v2acfOoqxwOdc4dNJkq4UdLB6m6nxJgXyImq2k3uJbYfWXnbrdLZyghPt5wtdzeriD84yy8DdIvIkmWdpwrojA6XoH-zEmi7a42wscosLXgVoGfrs36THKlrmZFGd34OnOSN_Ep21OY_YIcSVw8tT1q9S5NxcIc-9De5_o3Oh8n6RBamJ9webY-W9PhIbv0QLXh6vNyd2Nb-KU5B2Qd8cggM_tBqA3LLoXZBGzGs-TRaAA7RffCjU3N4NnzjzdgzBgQv2thKN2rSI9ogl65RHcHEePJW_RFXjE9iK8RRqXSK9NmqIkBOIbVlPpkjKuJqRKyRzIYlsG-z9rVVDs6guA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=v2acfOoqxwOdc4dNJkq4UdLB6m6nxJgXyImq2k3uJbYfWXnbrdLZyghPt5wtdzeriD84yy8DdIvIkmWdpwrojA6XoH-zEmi7a42wscosLXgVoGfrs36THKlrmZFGd34OnOSN_Ep21OY_YIcSVw8tT1q9S5NxcIc-9De5_o3Oh8n6RBamJ9webY-W9PhIbv0QLXh6vNyd2Nb-KU5B2Qd8cggM_tBqA3LLoXZBGzGs-TRaAA7RffCjU3N4NnzjzdgzBgQv2thKN2rSI9ogl65RHcHEePJW_RFXjE9iK8RRqXSK9NmqIkBOIbVlPpkjKuJqRKyRzIYlsG-z9rVVDs6guA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=G8CUil7nZUQ3hnU0lCLUMEe_k7BoCnUKkUZp98x1QntJwqrAZekZ5spjxijcC3dPgKpGpZ6LKYyTAm5R3GcoDVXWl4kwLtyObX7wfHuq8U5O3BGv8_NKilGYbW1nJhDu_S-L-5McVRJfIvhQ7ySG9WGA4IpWSQ_SZsUb87jpjIilBurTLNFmcW7s_7UjH51PXUYzF1Tm5x5Xm6aaLFiXREbXcKXp-I_PnXnrLweN6ZvAmcs3qSpAZYmQVpmlY-rDKbxWhEGkKF71oh7wsmRFqwt6wca2cXaf_dZcjNRxREnuh6EagjrVCwVUm0QK8CF8sYVo9stVpD40oPNAmciTFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=G8CUil7nZUQ3hnU0lCLUMEe_k7BoCnUKkUZp98x1QntJwqrAZekZ5spjxijcC3dPgKpGpZ6LKYyTAm5R3GcoDVXWl4kwLtyObX7wfHuq8U5O3BGv8_NKilGYbW1nJhDu_S-L-5McVRJfIvhQ7ySG9WGA4IpWSQ_SZsUb87jpjIilBurTLNFmcW7s_7UjH51PXUYzF1Tm5x5Xm6aaLFiXREbXcKXp-I_PnXnrLweN6ZvAmcs3qSpAZYmQVpmlY-rDKbxWhEGkKF71oh7wsmRFqwt6wca2cXaf_dZcjNRxREnuh6EagjrVCwVUm0QK8CF8sYVo9stVpD40oPNAmciTFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYO1qecuX527RIFGW9kNBKSSH0HwQNnMChHek2D4Ov8psskaPi-S6GSBbCHVk7DoD7MkLDB1CSOAT2rKG4VwhyL4jRwVukpkJPOO8C0PhiJOKTzsPTF7niFIhMeJtT1TGgdVrR-_D0InFu6m4r7oRzPOTOAptVZgn3TEheZvV3rEdyMCVf214SFqjJIKlowq_kW2-oVCOYQQSB1vnwvjgAEFcwI9_bkZJDyL74Bk8fuhwTMvrJVvBo9mAfmemWMwR-CvRzJKKEPVuSetp21-loInNeyx50Ty3Qves5sh-_jn5Ro8JFz-c8Ww3I2iD97G7QxPm9Izh20_Uo_wDD7fJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=gT4ofQxpDIu2zgVoJUG5OjxobHrE7rqlQ7bxc16xLtZRdLg1pcdwkX9y11hCaFAYSPSCJGGihH8mc3iXlBuUcUFLEzeeeGMsw1hbca4a6TpSKrJOgYRBeKzLSbGXu1SKzfDgLvad3rOeMQh2vZewDkrX-vPDzwulH1ubAWEg7UkVv1irgybG55jjUqeWBymM93ZOOWqU9swkDAiRfpXnjj4EL62qtG7wSmDBjp1yHN_cDSpWOA2dIXAX3FgHOkoNhzSmpnRZZFXyjko6y5RwnEQn0vlrcZakFED-ftYHxjR-IYXq6W9H6y5zdtCWS3DAJ-7DRTdZS_iGvuam4Aq6SDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=gT4ofQxpDIu2zgVoJUG5OjxobHrE7rqlQ7bxc16xLtZRdLg1pcdwkX9y11hCaFAYSPSCJGGihH8mc3iXlBuUcUFLEzeeeGMsw1hbca4a6TpSKrJOgYRBeKzLSbGXu1SKzfDgLvad3rOeMQh2vZewDkrX-vPDzwulH1ubAWEg7UkVv1irgybG55jjUqeWBymM93ZOOWqU9swkDAiRfpXnjj4EL62qtG7wSmDBjp1yHN_cDSpWOA2dIXAX3FgHOkoNhzSmpnRZZFXyjko6y5RwnEQn0vlrcZakFED-ftYHxjR-IYXq6W9H6y5zdtCWS3DAJ-7DRTdZS_iGvuam4Aq6SDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=kqDtsmwf90o1rIspD-0PG5cCosUvm8Id_ZCpFrrkbKgmOvlk0LNCxCvepsvsT1t54v3stioNuBBgU8imhScMq0FX82kcph9C0i5KgYlywbiN5LS-jVsxAiRo7WoNWLTDAp20QNTYMMjt2U72n2YiX_OtDUfCsEtp0HU8SiK6J9SoiCvgTyqX6vkgqGUED4HO2Ll7PZk0vDRG7o8_SiXVHZF-KQPQe6XW7OV7bkBEvg-PlgnXtS3ykcSL-lUOfeiykSzDXyuwLprJDezbsvkjr-wBp1LheOB5mADd8mKD_ZxyTNxxBqvY_h51dQGVDDr_sW-nghZ4wVTWJPNCV5Z7Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=kqDtsmwf90o1rIspD-0PG5cCosUvm8Id_ZCpFrrkbKgmOvlk0LNCxCvepsvsT1t54v3stioNuBBgU8imhScMq0FX82kcph9C0i5KgYlywbiN5LS-jVsxAiRo7WoNWLTDAp20QNTYMMjt2U72n2YiX_OtDUfCsEtp0HU8SiK6J9SoiCvgTyqX6vkgqGUED4HO2Ll7PZk0vDRG7o8_SiXVHZF-KQPQe6XW7OV7bkBEvg-PlgnXtS3ykcSL-lUOfeiykSzDXyuwLprJDezbsvkjr-wBp1LheOB5mADd8mKD_ZxyTNxxBqvY_h51dQGVDDr_sW-nghZ4wVTWJPNCV5Z7Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzAZdCaD2OHboMJjM-jRnKCXLiZTf1Actf7saMsR8FAUrY2fFEB_X-x5zjlM35f_MHtOAIc5b3kEk6Noq66AG8Yq4WwSfdsG7be-JjO1qFa2ja3MJuRWcM0S4d_w2DdNstoN_9bzhQIigwQqzRhfpjhL95hD2wBaIZ1j8UKUT97TrpWZDxJs5fjQg7k_Gz3Bu1iD5hd0vyHDUgDuGJNVeJmVXGnX6Ysv6BT33WJOU1V-qPS3sD2HgjmY3tGMZjlVk5yN_GJ7p5dwfvYkn-jzO1vvtgqbhIGQ_mM3EVI4qiFNOEIKijI0w825N77XXoHr6-zfvMlgcnegBiC_mL_IRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKhXgIlyOSm2_VRJVdWgvnsYA8JoZuZhNY-MGDNMisiUCJlq5IU1cw589w-ms8JZ_221R7wspvVM6oJoeC1BTcPPw2uKVhZkn066rgPJ5DPuLB4hEn1b_a6reUttKwbv4eezq79oadTF4WMUjR1gQbtsqraSnwvKsj9J-dUSJ3ArkBSfB1q_eM3rTRnhq031L8msAzytdZfeIN6qkMfh-AzWYw_LVDoXHic3tVQhKj0PdUSxJErk2UA7e8O1hYJlntvSq2yqddO-tb5AEb2IuBfAjJ0ClnanHqp8yqNhMBU_LgY99EbNumg72Xd5MT8DgEpRlxynd1TxBZ-aXiDiAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Nzd0BGFnw4K3tLCfx6e2Z0luOy1xZxGT715BCY-_2OQbQ-r4hhx4Ki4vjsShEMBb_jN8huy35pZYjewOAaZeBmskiEVhpZna0potfKi1IsRmENyy7yTiaibnSH3djpeam039DXwHCZQP1WMa0HqTDT-JHUaOpg4j3E_EtX3Gbip-eznDlcNhhRcSrRpoA3BFVIN-ViRw9Jr0cf2GTSnb4ZNefTsHC8-9DDXq1rKmk7-K8ECREftDQBZtn6UEAdZBs-soZ3FjOBMzQMVAYJvyBmzVN6kLOzIk05_Lslaxr_rCvBpZy6GiliMet3VKajJD_Wowbz9yY8XL7k6hMPqLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Nzd0BGFnw4K3tLCfx6e2Z0luOy1xZxGT715BCY-_2OQbQ-r4hhx4Ki4vjsShEMBb_jN8huy35pZYjewOAaZeBmskiEVhpZna0potfKi1IsRmENyy7yTiaibnSH3djpeam039DXwHCZQP1WMa0HqTDT-JHUaOpg4j3E_EtX3Gbip-eznDlcNhhRcSrRpoA3BFVIN-ViRw9Jr0cf2GTSnb4ZNefTsHC8-9DDXq1rKmk7-K8ECREftDQBZtn6UEAdZBs-soZ3FjOBMzQMVAYJvyBmzVN6kLOzIk05_Lslaxr_rCvBpZy6GiliMet3VKajJD_Wowbz9yY8XL7k6hMPqLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdFCJjprblFdDR-xygzuBRPaEaPHkKNiGCguFG-XPcUId69N4UeolgC6AkItZtSW05hZ2spa1V1olYwHhcKvmWxSPtQbJP89yZJvHVhGhGQL9I0MQU3Jb9wf78iaqQMW7EJNmzVS663aK_CvnvVDlaQbSfvzeaOoFsiE-EWP_2M_J1TcL4eC3BlLKS9zTNF7R8pcPuxJza_VSVSHa1CO4m9LFRx_Z5xSLElRq4TBtJeAzxhf7sKvd3j9EBVtn2WfGr_AgAM5L74qFgRWPqdoCfvUfICcdDuXjMWMKKvjS2YOQEcbMv4ZQ0qwTUb93jeSZLEWDGXDWGvbC_iAOUxpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQC7m1rraoQ29JPnDL0Y8Eb2wuqAMtLLcW237xhV-kyeQeMRQgMjlWr62xEketdKyZXrisMc4Md37pKcOf76gy3u3KhjCStfVBu7YA9pKdSGGTA6R0Q2-i0Ubwws47SaeAwSgmk3necqnChkbbYJFyKTh4o3FhUztiHbnR-IxHsiX3TqVYxywIgYkrtj8A9A-kUf1goK6gDb0TdnGMOFLRgxNmcd6Wj_S-wHQhRY0NE-c1Wyum1y6OZ-gwpdYtoYcqKph2DD4fZKSCjNmzdXrcoHZdS01oKRuaDG8wL6hnU5LwdtSxBYixzuhpIq5X3oBbsGN44CCtr_3pQ0hd52_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFbO4Fw4kZxPMjESJGEH4NYZgoRhRNxdo30OBY3bnDhtnc9uPsi0CfAcksLHbSWtBzR_ZPNherJzmdedL1EktfOGwMlEFO8nRJ8vVvvKw3FmmUndymrYnfoic98dLNtcLVbXMVpaLBgsNKJAQnSEJuJ8bZoM0gk6FSEGCYrPfM_v_NjS3QbRVDaodxfBaDPkO0FYdXfp9MVB23_Cs8qdKEDov1VKoSZMtBfoufE7hFi05ZhYwYj_y_GMPMShNsvnRYMFhE1UTBFuPKPTRBlR5yz5VqZ9PGg9AqcCQYq7BAJ-p10wS1LLtm20VgqwXoU19BuRCXa7mmYoGbCuxVtcQQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kdWi7-dFvEVLej4xMLLterNaJxXDzgnCH-r5h2YIdrG-kXJef02Ql7bJWWDxBZOCkqr9ghZcFTYx66noYLMCJXfhWnaukn8tX281RrnoBykUA62w5fu5eUxX-sPk7xmn481TWkEy2ecLjS6vQLxdgLwrFLYeaTUyVdM_PIDFA1jhOO_cEI2GKC_3tGvCh6lD51t8zwcylcOcx5ZZXARM9PELwWkmUnDI84Mj9JzLBaTV5yUZkGRzzcpXFf-HBBkfFp1pfDRbcU2miTeCF6erxfBS6O0izLbGRxnkpYIV00vk5HbQp0z9SULdcaVz_92iTXdprrxdnyxDTZ2tnOR8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=kdWi7-dFvEVLej4xMLLterNaJxXDzgnCH-r5h2YIdrG-kXJef02Ql7bJWWDxBZOCkqr9ghZcFTYx66noYLMCJXfhWnaukn8tX281RrnoBykUA62w5fu5eUxX-sPk7xmn481TWkEy2ecLjS6vQLxdgLwrFLYeaTUyVdM_PIDFA1jhOO_cEI2GKC_3tGvCh6lD51t8zwcylcOcx5ZZXARM9PELwWkmUnDI84Mj9JzLBaTV5yUZkGRzzcpXFf-HBBkfFp1pfDRbcU2miTeCF6erxfBS6O0izLbGRxnkpYIV00vk5HbQp0z9SULdcaVz_92iTXdprrxdnyxDTZ2tnOR8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=IZ2QkpJt3bXBH7yW1E1aKobYwEmx0mM2expdFPmF_ExsKlIOKaXR0zsfGYz1JCmk86zhKhe75EEDw1SXQNkkzRMnuvQsj8_WZAc08uMKQkgJi5KfTy6Q038ywKAXlUcMYvJq4LEV2tyvFgRePLSOVs2-kECjKZmRjtWVbp5np_0gTp8Y7KuBzbhNTGim547WWXfHizzJhJB_OV-A8xNzBB8J1C6mVsoO4QxgNOpamy4mjHOyhsIO4CURN0S47RatAUXVb-g1hGbjGgTMKoLR5zgSfA6ZNJeNuiGxlbNGfIM6X0wq1JOF04QmHsWhjgrXUKMM48CyvnTW-QCRp8KGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=IZ2QkpJt3bXBH7yW1E1aKobYwEmx0mM2expdFPmF_ExsKlIOKaXR0zsfGYz1JCmk86zhKhe75EEDw1SXQNkkzRMnuvQsj8_WZAc08uMKQkgJi5KfTy6Q038ywKAXlUcMYvJq4LEV2tyvFgRePLSOVs2-kECjKZmRjtWVbp5np_0gTp8Y7KuBzbhNTGim547WWXfHizzJhJB_OV-A8xNzBB8J1C6mVsoO4QxgNOpamy4mjHOyhsIO4CURN0S47RatAUXVb-g1hGbjGgTMKoLR5zgSfA6ZNJeNuiGxlbNGfIM6X0wq1JOF04QmHsWhjgrXUKMM48CyvnTW-QCRp8KGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cErGpHbtzpsrfWNIdjZPXtaOTJj7XTK8ZqVFFBEcmsG3nBW-fwA1BJ4zresLUQxJY6umY9NuHsWY9SNDpJFyRGszf9y32ZItJbgHrWYUAGEKT80-FX0ApMNMBaapB-bGKZzZARjb2rHHbpJqLQJPccCTBtZeLcBvA3PiEvbyV20PDXfKeqAJyq5kS6h6l__ZbD9uEjL3cp7YA6Xc9QwymDa_kbh285lqhWRyR5o2AeS31o2Of_EXEgbyn0n3fTQ-yzl04Gtcy1dRag6-Uy-jgSevSV2PBYUTr6D-ydw-TToe7ZLmyqXOiuz-8mslhHvzxEGPquW9KV4XxkfazHR3UVOm32-0XU8C4Gsrs70L5bu_ATGdyEnLHKbQxgh3VLZ-JxubTOzlNHNveB46-RPbqCjQx0VzPpTTcgzHzT68Yvab66LB5OFU5w37ocwl4oFVnVPfsyx7Gfg1N_rafj5tVLUc6fVcEnQxlp4F8QTUw_w9jARdD2cxlzQSoNZAPP-aQXzEC8DSMQOMSVsFFnoIWRY3OklBNljV8lUTGdZCroLXdRqzvtYrvEN8Ugr-zIMRkurITzN_-TRW-82bO5hnbf6WNV7gpoAWb14ya78k1WLIj_JlG5ymgOnJe1DrT17_Ef4CPwRUNQVPGGpJDhLp9H89UsxusERduT_0ARb81Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cErGpHbtzpsrfWNIdjZPXtaOTJj7XTK8ZqVFFBEcmsG3nBW-fwA1BJ4zresLUQxJY6umY9NuHsWY9SNDpJFyRGszf9y32ZItJbgHrWYUAGEKT80-FX0ApMNMBaapB-bGKZzZARjb2rHHbpJqLQJPccCTBtZeLcBvA3PiEvbyV20PDXfKeqAJyq5kS6h6l__ZbD9uEjL3cp7YA6Xc9QwymDa_kbh285lqhWRyR5o2AeS31o2Of_EXEgbyn0n3fTQ-yzl04Gtcy1dRag6-Uy-jgSevSV2PBYUTr6D-ydw-TToe7ZLmyqXOiuz-8mslhHvzxEGPquW9KV4XxkfazHR3UVOm32-0XU8C4Gsrs70L5bu_ATGdyEnLHKbQxgh3VLZ-JxubTOzlNHNveB46-RPbqCjQx0VzPpTTcgzHzT68Yvab66LB5OFU5w37ocwl4oFVnVPfsyx7Gfg1N_rafj5tVLUc6fVcEnQxlp4F8QTUw_w9jARdD2cxlzQSoNZAPP-aQXzEC8DSMQOMSVsFFnoIWRY3OklBNljV8lUTGdZCroLXdRqzvtYrvEN8Ugr-zIMRkurITzN_-TRW-82bO5hnbf6WNV7gpoAWb14ya78k1WLIj_JlG5ymgOnJe1DrT17_Ef4CPwRUNQVPGGpJDhLp9H89UsxusERduT_0ARb81Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=iyI1traNdNgLlJzWx8sAkTJ32g4zmMQYA8XpDuRSUYoKEc60k-0updl-gGDidYnS-nXo_YUdWLFPFWSlP7280mNFQKYpyJcjhIOFCHkSlwY1ka3VeV50hvZzWGZu8KYHnR25vllzjOt3LAw7QWJa462JQIl1T6j5wH2riE1UeYys4mgkN3toJN6T9INW_TFSf3zxWpM-N2Q7RfOHmYNirxiyWgxQNEV8S8M3aXpLyQufb8HuMyZg91hDQdqvHbT0iU5gf3MDxjgzM5DB3C4ssEjoPhF8ToW2GibZVLMsXCl5xOrJQHufIh4i_cXkBukTKI7LCLOuFua3Ny5qQUjX3rc5JBYLZtktQ-rgzpguaFECDe7FVlc-XQQstqbGqjGYe8DwiSGdlltMGU8s8zOkg1W_pSKlNoFqxjAT5Fktns9kGv2iugCZRZtAZIYMczjKu3Czr1LFpX3pfNPbJKo_CZxy8J-L-ZcpUCTHKPFO6hqrgjrGi0jkkDpeDb805i1fF8NDVHJM8Jn-SCbBGx3_u0eyAWQRwZqTN0zEYju0-Qz5nCpnpC0tT5DzWljRkKjDHlRpZeXxRbKQyLwp-lOooUqEIlh7y1s0i1GI1wFpyzAFVs_R-X7F1wbmonY0CFjBzm8CdTJviIo_RpW2KZsEusqtNckmwqxN3kHQM3S0Ip8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=iyI1traNdNgLlJzWx8sAkTJ32g4zmMQYA8XpDuRSUYoKEc60k-0updl-gGDidYnS-nXo_YUdWLFPFWSlP7280mNFQKYpyJcjhIOFCHkSlwY1ka3VeV50hvZzWGZu8KYHnR25vllzjOt3LAw7QWJa462JQIl1T6j5wH2riE1UeYys4mgkN3toJN6T9INW_TFSf3zxWpM-N2Q7RfOHmYNirxiyWgxQNEV8S8M3aXpLyQufb8HuMyZg91hDQdqvHbT0iU5gf3MDxjgzM5DB3C4ssEjoPhF8ToW2GibZVLMsXCl5xOrJQHufIh4i_cXkBukTKI7LCLOuFua3Ny5qQUjX3rc5JBYLZtktQ-rgzpguaFECDe7FVlc-XQQstqbGqjGYe8DwiSGdlltMGU8s8zOkg1W_pSKlNoFqxjAT5Fktns9kGv2iugCZRZtAZIYMczjKu3Czr1LFpX3pfNPbJKo_CZxy8J-L-ZcpUCTHKPFO6hqrgjrGi0jkkDpeDb805i1fF8NDVHJM8Jn-SCbBGx3_u0eyAWQRwZqTN0zEYju0-Qz5nCpnpC0tT5DzWljRkKjDHlRpZeXxRbKQyLwp-lOooUqEIlh7y1s0i1GI1wFpyzAFVs_R-X7F1wbmonY0CFjBzm8CdTJviIo_RpW2KZsEusqtNckmwqxN3kHQM3S0Ip8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=pfDYuRqiKsTAqmYRxqWSmEOUVlgP8JpAlB_YcDqnCTGLsuXT3VDcVbCKr_Q7fe5tqwK6recbrYdQHK4fEf6j5uaOicRZ4BtqerpyCTEgUMx1sEQTyNBYPxUbnQ-HWLKBo8idzKRh9DDZFi5o8WRI0ogjwT-Gaii1NENG-KOtrnq-xwh1AmNhC5-rs18o0TZBdHQd3WGlZI_UZ-L_5twr6VYCjKwev4EsGtG6bH1SF_10KcbHgRLh_0YTWBLFwTaWOJh03pgaPO15oL3BCU6uhBY5OrQ6c0EcMIVguEL83Ly-7mv0YOO7UbJcTWdIedfJmOD7JqmYvjnKOoOsC57ZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=pfDYuRqiKsTAqmYRxqWSmEOUVlgP8JpAlB_YcDqnCTGLsuXT3VDcVbCKr_Q7fe5tqwK6recbrYdQHK4fEf6j5uaOicRZ4BtqerpyCTEgUMx1sEQTyNBYPxUbnQ-HWLKBo8idzKRh9DDZFi5o8WRI0ogjwT-Gaii1NENG-KOtrnq-xwh1AmNhC5-rs18o0TZBdHQd3WGlZI_UZ-L_5twr6VYCjKwev4EsGtG6bH1SF_10KcbHgRLh_0YTWBLFwTaWOJh03pgaPO15oL3BCU6uhBY5OrQ6c0EcMIVguEL83Ly-7mv0YOO7UbJcTWdIedfJmOD7JqmYvjnKOoOsC57ZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5kZ3lb_nvVjaU2307mDeQAsDYUmwICfnh5GA9WVGWCnZ0LvdRHEijJxSFJIvb4sELso9y1r-2mJHm53F0tEFRJQ-UBgH3bdC94LhvbroqYEbb6TfudPG5vV0sEvneotbJm1zyeaRuwa3K1HDaZ1Jt-zIqkVlnEUFW4YnNlM_HH3o9d0yXcsGIhq9V5ckhmIrARv0sy9oE_89njkahLOD6_qQ9qh2BGFnAnzt2nGKIaa4NKYJ-bCJqxTjtln1QeotXD3oP64TV5aI24NScZWlJb_-XURnOITtnfRfYSmi3y1LGLH4rrvbWM_mxbYlFXPUwL2p7EUyQoIsoIqIMqvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fQbU2dxe6G5qHNTZoD7_4x_L8108v9Q0wLfeEeKBIpeKxmrEi7r4Sgj5nEp19izXh3JaZWBFh2WgEtja-etfxBu7nZytIh1zpvMBrgR52yenkQ_XcgPaDpM__PMMhU0budER_tQpeEHMP_glP481lme5Ub2cik347FxLfxNzfRlkts3GNvmDBkxvKNo6RTRm2TfmE2Kv9TfzPTdNK1fjSWGXLAbSLfeEuWzIz7ebBiRvVPs5207WMZEu6CJsj18T_Guqy1XVOWmKaZDMgFV-pXEacnQwOIUpCP-LprvWNovCNRxWAyL1s-d9qk8odyDb2913tBuY1mCGTFuMX1gUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fQbU2dxe6G5qHNTZoD7_4x_L8108v9Q0wLfeEeKBIpeKxmrEi7r4Sgj5nEp19izXh3JaZWBFh2WgEtja-etfxBu7nZytIh1zpvMBrgR52yenkQ_XcgPaDpM__PMMhU0budER_tQpeEHMP_glP481lme5Ub2cik347FxLfxNzfRlkts3GNvmDBkxvKNo6RTRm2TfmE2Kv9TfzPTdNK1fjSWGXLAbSLfeEuWzIz7ebBiRvVPs5207WMZEu6CJsj18T_Guqy1XVOWmKaZDMgFV-pXEacnQwOIUpCP-LprvWNovCNRxWAyL1s-d9qk8odyDb2913tBuY1mCGTFuMX1gUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=XNq1RNo261tCRLsqIFTiUI6s5vAdXJP_RBovG0c1XMQOokzPQaN0QlYPul5M0QsIzDwz1bLsmD9glDOkMusUBVr-i52PzhmCUyxgDCvmDo8DaMo-bMufwG2x7EGnO-DuqM-4bHB04KQrXVefuVEA8_MaLD0BYQJe4gqPB8HC_PcujSLP7FT5ye25wZOqRz12sh_PVXmo27HpL1wtb0KC2c4mkO97ozTOfVBjNC_DuNpHRTeNxObM3a7Kwj5eKUs-U9aLJwdEIC1jRlV_4GSsouCYexmYy36N63xpx9XqB3gbqk2uxJqTdndLvxY-y-T0KI2F-xdnkTNZBj4fp2yUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=XNq1RNo261tCRLsqIFTiUI6s5vAdXJP_RBovG0c1XMQOokzPQaN0QlYPul5M0QsIzDwz1bLsmD9glDOkMusUBVr-i52PzhmCUyxgDCvmDo8DaMo-bMufwG2x7EGnO-DuqM-4bHB04KQrXVefuVEA8_MaLD0BYQJe4gqPB8HC_PcujSLP7FT5ye25wZOqRz12sh_PVXmo27HpL1wtb0KC2c4mkO97ozTOfVBjNC_DuNpHRTeNxObM3a7Kwj5eKUs-U9aLJwdEIC1jRlV_4GSsouCYexmYy36N63xpx9XqB3gbqk2uxJqTdndLvxY-y-T0KI2F-xdnkTNZBj4fp2yUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKbhuDUzTvgpus54KjnnCZW_YXmCS6kv7DC8zqqEBZYFwLgY3ygdDHhUcmNxLRRDDw1nK6w4G_bd5a7_ZMsRBQXVspJx1Ubb5nPEcjMheExw0F5pqyTrKUZIKyvAQdCIiQzcjXY9-Rgu0gKRZxVowuyEf60k6Yc_oQBQfhkYSiBnU3snBWgt6_jLFofzJuLmE8OXb8NC6hQa392XRYZQASkvDaduaDmjtTE6l93ogKoQ6yGl4ucs0STzz7OIZKSLTU4NGJFMZnf7GNyG1_EHyLfqWeBUR-oPrRTphvrYK6tpECprIHE7s1pPgJpYnfm66CX1LwFO62OoBo7DwpZjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M99rzlLX4YgeBhFVf1KKhFhHHLPfFmY4Q0jAuba9-o9REJjiAmJAVUnLxWaVpO86OP3gz29BYiW-ven1C01Jm3dqbfPpNrAsrkU6kMpqgNOJjQoi30zfpcM_wQ9sPU1BYvidM85smdNCTcAac5uEK3vU7ZFR-wWRKndLGmhkzExRfSvJKGjWXxe0Fn1lTjvV5FMypbwcsqOXM3ZMo6UG_KJlmyry7tTsHN97BWIENSDhPGKZP4U8_58OT5pbpOb8Y8NXJJpIBRObUPcl7an3kAk9sBKH6JtRVtQnPYjLSsgiVL5I2g4Z4A6y8BY5l44Iztq5KVh4R4nC2GZ7jzltfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glu1vPaeED9Xx-DJtn--X1FXXo7RKz0gDWh3YR6GOe3_eXzWg3gHb0ikFrN46Br7uBLu2Cz1BrSZNAimIyMFI9uvKWEYU9pU_j1ZGUF8njWs7eBZFTIUKTZYoiZKuxKenkAQ59zS25nrqk4hr9oxVhLthwIEJ9IQ3WfDQPktSXwvkdX8YfdlSuhR-piaUkfI3Su3Biwx39aX6EQtaLY7q3eHhe1ffvZgffGRJ6LyErgJVwU5m3qcoKwxgIe5ahDVDHo3V0HVOe-NrAH8LybSkyw9qJy_xAPNjzm0FRPdWJJ7W8gG1zFJctSerGn-6008t4bjz0_4zehDoqFbYRnc_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogTHZks4NAB8i6PZFmVsC1-nqrC8t-uC0JIXtMCLxKDbUimqzOfne29h1n8uQ61GdsDSp-D2x6_iZIn7-o7zG1clod2Vz8ALs_xwt3Hw0VFqc5Q2jBeE6J-XZkYNP-G4dioZGQTzm-X1CyI4_qljWuZ5KHcgrZdeCnzxgPWbVIvYbQuPkBCUT_TxOEhe8g_U72y5bt2Pdq6ulX6TQrtEkEJJki0Y8swuTGv4AcEaB_aRNflu0wOToNDVo7cW2Lxwr3yB8ez6pp0VGkY_hd4ABz5rFFcwGpEueCFob_tY57or-FHalxP5MQrL_HrRgynBlJFY0M3LyHbe54CnLDH2-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOZ8tNTUlrLMlC3u3AoiK1ljyNkPq-C98tqgR--F-8eruHl1AavXndoefaZl2mPO7TjrbTU5Q_QUWFjbhRhmSVH_M7k-InuVy1SkucFiw4Z6tiF8N5IORbSFcLXz3PmVRRcdj3AzW30b_hmTNXUyWrLQa13UbKYxCTCuzUs9rC25pPy0TnRBEGHzFyHJ4QohXBFvw5RIOHqeS21MJQ-aNDZrUgnC_tlW_tPGHpYVAOVM2zhSgTIwCKRP0o8XeJ9Ovnx_L9L4v5-OjpgscBqeod-5INvlyTlkmKbFUKwJGUd5UdhLOwFPAjoLyPGdsm1SbeZOYWDAlrtqqjul5wkQbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-2qT2WflFN0NpdvaB-1mbZebcyvzrOFeZ0UdUcoV-kKizpmHN6jPaLNqYKcvzMHk-WvA2xwDlXt05DeJH0itMMy6HDd14s5P2-Lo4puZUIBw3ciuSP4AjiFqjnbEdxwMvITt7C6A9jtZB9bIzNwbD3wZ7tiGAOeBPZkSSUDBxSXF7tAFZ6EwO864NAvj33QsTMFIDm4jOrMLpGzkF6sJKoLbsq1LBBQOeqW7W-IOKYvqyZ_rVzBKBVS2Gb_yUO5cfHivDVNVrPrXDRp1-CgOHl_i4ocXRCjFAEcwVLqtWyvmRZxeYhAACmpIXECzRsvKguXzA8ppIVDtOTMU2HruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFWwBOClBxTE6LJIP4MGAVhpi2m0d4qWqXZuObIAg9MgHJX_LraBRDlF84LQBVNuVSeVCofo3XCOeF2qkREIhg36wby-2nF3m-6O6Lysn1fnKJbKb7CsOVFo0qzdWcTaj757Pfrm-p1-da9p46GKG1V1CdOKjNDIAYCIdZ-70Ar7hjeGnktQFSam8IdO0uv7xwVUx1ciTtVhLIKqBgAqeFnmI3MmXnjMB5qX6vTX7lAM7PxSd6yxP3PA1LD6Zg7OQDuNhi7c3GwEKNf_lsAUNnbQs_9KA0FsKhSDEwqHu-WoCa_lJzWhCdpV57jaUprk5HVSy5U56wId4WvB_4_iIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vA5K5YtNTXEyyfyYP6pC_Hq1xiddRQoJh3WY8Ryenc9LW8GQTjOkDtOfYS1PPiAT5vPZH6VIh2Pftdo7kX3wY4IcWyYUKjY1sD_n7sTXKGZjGzM1MD8xBwtC1rXUT6JwnA8VuyIVuB8FFrQarMeYOs2KzNKvOXC3yIcsJc0TxQ6bMKC_q3zor5kh6shddsQKsBhU8OXo0xy04b_E4LnTrr0zrdfEasW56ObLE9DQHWTQq4HVF3He0E4VxT6a38cy5y2L1mSet-086oq3PfW4596Kax5CpNLn7q0tbU5zqLgIdmHoxBJWmpvz7LHy6E9K088lB7J3SMXRo6idFaxxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlWvRf7Iznqta13bNN9cChRmc0T0qbZ4e-j4pVVmmJG195NoI9oz8hV65sna-7a60fHNJBhRD0DuF6NoCajg2JtSnnQAL4nMdOfNWfCtVR-uXg8-G7gYLWFiGi8MDDhYXvCskoN0OW1GUQ5MLWvVxCKB6Maj0lXG2dJLKSoMRT8Su_G54C3bZvmU1nofO_ihBzG6OdYH_Cp4fxYKIRnj7gCJ3Ivi4pJk-F5J3SPA4CrDS4_3WjWZG59Xajp0J-Wjxi9wl3t4nZCqDy91qXDHNtHqodtLq_EfIanHS6zOTSOxqoVlyo0_ZK-jNEyp1XG3His6kQA0YbzHwToM5NW2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXKnHpK4X0bJ4IylvpBWhR8Rl77v1S0wE50nV_1SZWSQkWL6s41EVxFcamzN2ke5VwRpdc3OrxVrtgMlreHAfFcXHzGUMhSR4ZH4jlks0zmV2fouFYYac6m8QFqha-deX7hpG5mYYptZf6UtpQbukNCabboTodZMa-byVwMx9aBKH9jHCCkLKEiw-zVZNfc-y9AhVMbza2D-Ie9uFcRwbrzX2JePkvZW7BR_raxsg0ktNS5388D9wBBmGH3SUw6SVgnPzo2X6Ow1Or2zdrAY8ip4Yo9G6OAMRZuJxcNLIToeu6ZEipLe9pw5m3hsBbXQdI1c1AST0ZihrooEEv-jMw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=A6yNsj_t5aAxZijpfi8hD07YfKGGEj-vPsShbaoOVwJN9zq1BkXX7NOHZMXB6NminylfotgW_73ARXdSp-4OFF5MVbiZgwXfX342HwQWm-SZMinklNfFp1naeVt4W29GWegwhuY-ANl5lZkai94bYXGBZIzWilE_wj1J9OuXZR-3Xu9OOd-2wKXsHAd4SamoDn32-7227LIwHaZqFT6DqElVmIRiPCRHqPDGrYw0i4Qh35YTwxqsGzGD_TYx3Nt_eu-o1wlx_7bNS764FLrEKIFCQdvrvykM3LUGYMHsu7vMk-NPQcmYRxMeYCL_kbkbEpEdMLtGnI7cW_Q8J-7njw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=A6yNsj_t5aAxZijpfi8hD07YfKGGEj-vPsShbaoOVwJN9zq1BkXX7NOHZMXB6NminylfotgW_73ARXdSp-4OFF5MVbiZgwXfX342HwQWm-SZMinklNfFp1naeVt4W29GWegwhuY-ANl5lZkai94bYXGBZIzWilE_wj1J9OuXZR-3Xu9OOd-2wKXsHAd4SamoDn32-7227LIwHaZqFT6DqElVmIRiPCRHqPDGrYw0i4Qh35YTwxqsGzGD_TYx3Nt_eu-o1wlx_7bNS764FLrEKIFCQdvrvykM3LUGYMHsu7vMk-NPQcmYRxMeYCL_kbkbEpEdMLtGnI7cW_Q8J-7njw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0o1yh-r4EqUmk2zPmzP-sEQpnkHSBsnGBh_lWa39Xrkq5ww4FOkvgV4uIVj6iL3OUKTx65AVishEIzEW6RAOCy_bA4aXW8pxllBRSDoW9exnYDckxdKIJXIid14-gmRNLk68mTFcPvIu7h-zPfnoR17FpmGbTw86Nd9zxZscoXVPOttVXcLtFQ9UaWTobIHR1NQLF_da_-UYZq74PsQ-jiBTJPA_Iuh0DnCydPn5Kr5wBtuw1DaqallLodnu7m46mUrsOkgIBAfVYQiuB22Lqgf0LI7JZtpDZF2fdCfhu_NZfunoxyIeZuWAEIImI5-_VGjooqvX0SdkK4WGANabA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVYAlYnaCPYVCDN-53AcyEe72OneI1lsvROPB7Alnw0jOwBnIdg_8XG28LkyEq1ngCTEnhLvolKZow-CJwxGZtFFvLiUMpdm9g699A2wOQFh3oCMSeSTsgdPjDcQjJYr6Shu0iHKBbyPNZNF1gY3je3ggoRU8eayx6Bgir8uyT3WnSiQHcdFNujNvnNIBdZ9rC0vIY3XnbcpVPWfcCf68lZ7gaGQxs5JdghosbB-SKlladxzry2ogJUDhokJFmqD9kHPhs2ni6cCVEN6Qvl3JMlCT6COoQ2ltfKH-YPfkyw31ElTxcjDVXlMVOGEGT9a3E-SevTLT-08atuRhhz5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
