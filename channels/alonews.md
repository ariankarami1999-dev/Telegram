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
<img src="https://cdn4.telesco.pe/file/bwzWoeNmdeEjwCxKik2NSpr3oUcLFZ6tAhxG0mlJL0KVCPRIldBauPe2Rr-IsBg72NfzSCSRwc6HJHJjGEiBCDklW2-ImQeDk4NOSc8FyYJmhnypxrf7HiQm7QTscl8NKKTlhkboKyo0TjrJmLNYz29VXIenynyNz5E0OLJfY0A5Xv0dLdvNBnJdyqxoi149nrvf7H-qNGV2C5bRYyhKgZfIBJf8ccFwe8hIWxXV-XC_Kq6J9R1VHyo3nhla37uaEboG7qhX_Zssu1vryPBOXUoLagvqBvQxk6HuL7a2xFdkPEh6HMlvwrEs2F2wmuPtAg57UQ8NsVgL5eZFD2XfNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 00:25:33</div>
<hr>

<div class="tg-post" id="msg-143619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP7yjM9HjwyPazHCq2gVR4ALrnR_t3hqTfuaLXZhCph0rwHRkuQJwjPbf3k4W0FK572qV2e4-W5cJvL-dgJqbh48Grzx1KZ711mUTuwk5WiDuERBeKaHg3rJW-e2MySOvcuPZ2URBSlkmb-Kwaq3Q0aAvQ-rigcWpHcSJfNjixXQV5-s_UsNHBVlsbpwRsYIVWqGm7wHUoJlzN5-EDl9UpuB3qoAbQv0ijm1rqKgEwUrH0ztI7uWoAanzy__iVTd0V4rR6xvLoHllBy_3Mq5pOSFX9mhf3wbSN6vTxmIocmiNWahEOPMEe7xF7Isb_dvKpbjlXtMki5RemZyphfhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
میتونیم با موشک‌های دوربرد خودمون علیه آمریکا یه محاصره دریایی و هوایی انجام بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/143619" target="_blank">📅 00:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pxF0nX2OoJg2SOTmdOmDEylQ6Bqr2dHWIstBkg6a7UcFCJ-7o2YjB0IpX5k9qmI4_FEkmHA4rfEu8npJywI45VWaIVMQw_5-PQch8FqdbAm25fAN9hkC2USUneT9XodH3-3Q5J3G7gc8FnVy3Nh17QX6eEUV2hW8gWJp8Iqhe_GLZv9zP8D-BNljDsXUrgfhUeUpYcJMHEIBLNV3V3GjusvVWP6e6cqIJzc0zfPFI9cRNn-2jB7NcLFPYa_HY99Mg_gLuJCZIXy_3gRbJWAghtlFxjdIL_D3mydwulw2sFAAXjrjopidQ5nka7vnaOKrRR402yH2COC5cFe_AshfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست حق یک پیج مرتبط به پلیس یگان ویژه تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/143618" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtLdyENh4Qddzm70mL4AYk2LTnH0brSm1Tk3MKo_KhNtVnNq75t_5dvmC3DjJ00jGgkC8KFWhdYaPWt6nuOyzd15Wp-MolMSFMPsW8gAeTOVz0OdlWjMGnTA56Fj9BF9ITs53n0NiU-anSQH6JUl6WDYN84V7qDGvWHW_QgczzjfuLLRdkFa1FDS_ozKHQPLFGE5hSjVSKw7j4qK3lNSEz6-5hkfiYl_ZaWScXqB5v-oapPA6hEdO2nJ1NvK3wW--LHPWTROVN5uWH0SBVN--7lGxVHZD3X49Huo2S_umeaYThNt4vhYR3Y-47_vtxm71iSWjDn1z9uuBagXz_dDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی خطاب به بسنت: معلوم میشه کت تن کیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/143617" target="_blank">📅 00:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر اقتصاد: اقدامات اقتصادی آمریکا را پیش‌بینی میکردیم و برنامه داریم. خواهند دید موفق به قطع شریان‌ های مالی ایران نخواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/143616" target="_blank">📅 00:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1yZxwOgSt0-ONlLwOkyZGcBhKBx132le3BuPWgDS1D-tc2Iv20hWtz9Z3CkAJxE_UHPTq8mVCpn6o2Kz8a8bTCVvITxWf9ADPBK9apz8E5mCoq3dMBKw2eUBuO9gi8a23ZVNx6gPHQL9wDLyaY5lTIQRHJVWSBW-wxJ7Ab5I0RN83WRGQ1etcvXvLuTI2hCy1KTBARBXLvkrPOa2pegSRaNg5ZtIUROUUkObBjpC_QvBYaFkCafTGXasen0bjoidj1EbpkADq9TJxhWxtYAbvAQgIy0lWg4KUhYEwes9FAfVfP2Th5ThR09eVqicUzb7wIiuLdxE4qzlnmG-AaM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت هوایی فشرده نیروی هوایی ایالات متحده بر فراز تنگه هرمز برای پوشش عبور کشتی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/143615" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الجزیره: ذخایر نفت آمریکا ۳.۷ میلیون بشکه کاهش یافت
🔴
با این کاهش، ذخایر نفت راهبردی آمریکا به پایین‌ترین سطح خود از نوامبر ۱۹۸۲ رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/143614" target="_blank">📅 23:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUoWGY7lwxYkt-ByhwRYuep-MdDaNR3fR50cVxvGB2KC8YSHk0yFV0qj2uy2XBrgAi6ZkC-NhR21kQ5S2IltuxNP4-YcQC0MK_IVlF0qqkmPFTRysxYg6jyd4eyTefy6Zz4cEfid6mt2F7Qb06BACenfL-_ZjbxtZP0bI5jK8piCgCjgDHhbi4Xcxt4ExzYq0j_jByYk8dmh6Oy29Vw5Phpv6nqPDoKgLLCjMOdTCoG73g1k2WMcPAgKTNGRd0lRbhOE8EVZLBH0Zp3bayOZZsHvgX1mR8YZJQv4Jgfwo70goxzmMvfZR6EfJZ-WIekQYmpUGii_VTsbu6fI9yTmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با بدرقه اسکندر مومنی، عاصم منیر و وزیر کشور پاکستان تهران را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/143613" target="_blank">📅 23:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر اقتصاد: با کمک مردم در جنگ اقتصادی هم مثل جنگ نظامی دشمن را شکست می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/143612" target="_blank">📅 23:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=IwsSX7pPR4K2VwLuz1SV5ysRLH6IxnuJkDSvROI-D2rl507WBgmMWNWH6IkvcpKLshkO_yRC7fQvk2-RswErByTtO9gQcEjZetxp40X4m6CbsfGsDFIlFiCv-GWFCFR4j1WkNsFBf7HUISpAmntJ8peMjgtOs-G1EoGfKX-MsuSchQbW-6Dz5cZDd14hzAcFTAcepYPNmEffy8tQnmFr1uDhjOLfFZUsSMP3TRf_-AFNPI9WLKi3_KH3fo0yRlpD8oWl-AfRKDHa1_AWjhaq2vonUdqU7d4mS3SyFOYuY9J2HEpK6trcUUMpRRvfsh4JxjuyFtme2gSyIJks8UwlmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=IwsSX7pPR4K2VwLuz1SV5ysRLH6IxnuJkDSvROI-D2rl507WBgmMWNWH6IkvcpKLshkO_yRC7fQvk2-RswErByTtO9gQcEjZetxp40X4m6CbsfGsDFIlFiCv-GWFCFR4j1WkNsFBf7HUISpAmntJ8peMjgtOs-G1EoGfKX-MsuSchQbW-6Dz5cZDd14hzAcFTAcepYPNmEffy8tQnmFr1uDhjOLfFZUsSMP3TRf_-AFNPI9WLKi3_KH3fo0yRlpD8oWl-AfRKDHa1_AWjhaq2vonUdqU7d4mS3SyFOYuY9J2HEpK6trcUUMpRRvfsh4JxjuyFtme2gSyIJks8UwlmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما:
آمریکا از ایران زودتر دچار فروپاشی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/143611" target="_blank">📅 23:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7kgbcZT5Jum8VcgDtydLvrggsba0AEfVJFkhJs_NyNUdgWzXjOAKHUKlt8dT3tKy1ctUFTxgSl5XzQ5wQODZolldhtWBMcekziyzQkf2zPhCseYySdpBsb8thKybHYRNV2o9B5TouyJu4f3cZVawEAkVNJ_mefVEXkupgeKTvRZO4Ou316lyx9I94wjqbY64GmiFMmK5r6WQp2M7P8w6q9rlrfkp7KiQFUuoNGKwXi3PUaBATyjtgQt3tr7wyNBDnny8SOpt_bX5Pv89r2pd5NxFZ4NdHc6H4Ksv5wceItGZ-W4tqc1cvbaTIKvib4PCtkA6dNgYPdNFr9vUw5btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ظهوریان، نماینده مشهد به اظهارات سقاب اصفهانی، رئیس سازمان بهینه‌سازی انرژی: انتقام قاچاقچیان سوخت را نباید از مردم گرفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/143610" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b413f273b.mp4?token=jH8AfVIN8tOZfNEx6qhyUILLig9_q5hSHXsViF0xOX8XCaYxq-AWzAiP0PU436LRZtBrkzmpoku9iHAPZ4yAIuEN0Z17U8PiY1L96-duxi6cDJKZvIWjUwWoDU4aMja2rH1fMGo6QzGaeFaX_XIeEr9hqQkBbuUEc1gGnV2XeIXDjp40ADRwLwA_0abKeUnqkvnsO0Xa6pDL6w4dxIdiVjQlHWeQiDSVJwdZOWWVTGRgspFhBno288KjMYJ1QC4XDIIal8Nkg4bJ8ouXcr36h2gRqTcp9NE1EbZMRLEWQmbwgWfyu5c_u2j1yP3Chr-dpaSoBMLNpgD2d7nKjIjFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b413f273b.mp4?token=jH8AfVIN8tOZfNEx6qhyUILLig9_q5hSHXsViF0xOX8XCaYxq-AWzAiP0PU436LRZtBrkzmpoku9iHAPZ4yAIuEN0Z17U8PiY1L96-duxi6cDJKZvIWjUwWoDU4aMja2rH1fMGo6QzGaeFaX_XIeEr9hqQkBbuUEc1gGnV2XeIXDjp40ADRwLwA_0abKeUnqkvnsO0Xa6pDL6w4dxIdiVjQlHWeQiDSVJwdZOWWVTGRgspFhBno288KjMYJ1QC4XDIIal8Nkg4bJ8ouXcr36h2gRqTcp9NE1EbZMRLEWQmbwgWfyu5c_u2j1yP3Chr-dpaSoBMLNpgD2d7nKjIjFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت زندگی ایرانی‌ها
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/143609" target="_blank">📅 23:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182c788691.mp4?token=rYnBynIdi8SZluCa0YitdTufomdxqp7oe4kZb5XsCOZ0hQKy09jPJZ0wA8xsloTYT87fpwJ3DnyNLlGtahSrbix9jeO2BfkyTCaax2aVR8cJSzsSKFzNLg-l9zfSg4GxnvH87QvTceCkYlyEX6LSM4fDTHyCERUpXjT4oMLY5IfQiyxNVp1pD8FjU7TRnysjkIgBHzEPE01wH3VznQDbPgTh6uktYxHdZ7CY37Jo1JXpx60ns7xDqNm5TjV3ecfkU3udU5-FgL4dnzWdVgixijTk4GGoAmVwuek2RkCo7ZXZMwRnUJaJwpdu656szCFeVH_P_NWI0ijkKMOrqh2Giw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182c788691.mp4?token=rYnBynIdi8SZluCa0YitdTufomdxqp7oe4kZb5XsCOZ0hQKy09jPJZ0wA8xsloTYT87fpwJ3DnyNLlGtahSrbix9jeO2BfkyTCaax2aVR8cJSzsSKFzNLg-l9zfSg4GxnvH87QvTceCkYlyEX6LSM4fDTHyCERUpXjT4oMLY5IfQiyxNVp1pD8FjU7TRnysjkIgBHzEPE01wH3VznQDbPgTh6uktYxHdZ7CY37Jo1JXpx60ns7xDqNm5TjV3ecfkU3udU5-FgL4dnzWdVgixijTk4GGoAmVwuek2RkCo7ZXZMwRnUJaJwpdu656szCFeVH_P_NWI0ijkKMOrqh2Giw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: دیگر خبری از افراد ترنسجندر نیست، فقط آموزش
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/143608" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر جنگ آمریکا درباره ایران: گزینه استفاده از قوای نظامی در تنگه هرمز یا در هر مکان دیگری از ایران منتفی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143607" target="_blank">📅 23:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر اقتصاد: تلاش می‌کنیم وضعیت بازار ارز را به حالت عادی بازگردانیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/143606" target="_blank">📅 23:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbkNbg_sI4TtZWydlHje-IV6W2wM7xiqwdsblRUiGoHUzexuMXs6kSUOi2H51pjHEQep8QEP6r2OVNQbamDHkhHmslP987t4R1CUvDesHR4rhQxsD4cwl_0vPMeO8jLdIv26yDnht2GJYKPPUqqIhjDtKUC3cPHAFzRMiYp2_mB-I0khX9GTKo449Fvf3z7ugsyZnvM1_qoEFqfXSzzeT3U1fOY3zxir7v_bZsQu9yWkqSs67bKxDAX_x6sOVuOkbpyDBWrlx5TfrdaQW-rse5Wtm9CpfzZempYeGz8AFlwDAu9q5NB9waB74CP_F6CqKGmCnsqPigBWoK3B4jGssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: تبریک می‌گویم به ترامپ و بَسنت به خاطر تحریم‌های جدیدی که علیه رژیم ایران اعمال شده است.
🔴
شما به درستی بهای سنگینی را از آن دیکتاتوری بی‌رحم و از کسانی که به تداوم تجاوزات آن کمک می‌کنند، مطالبه می‌کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143604" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور: شما شاهد تغییرات بسیار بزرگی در میزان ابتلا به اوتیسم خواهید بود، که این مسئله شبیه یک همه‌گیری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143603" target="_blank">📅 22:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
محسن رضایی: نتانیاهو و ترامپ یک برنامه برای 6 ماه محاصره دریایی و اقتصادی علیه ایران را دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143602" target="_blank">📅 22:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa19e45d1b.mp4?token=GlK83FTX2b22H7oSbaM_B_a6nNk-9AlYyxYyBXk1g4JPugVmyLmv8gI6stLgV4-mII_PTwFZaUFOES0dDyPVhMdL0Y3lT_62meKzsNP-ceTv2p9DdkFbXCbWGSSW4g6AunZjMOhyB9IeCEyTxBINQc-e9zH_MYc1X_8yVdZuoDX_dakomaEE8xTHwz_CzL8wFf6kRBY0t3DdHnpGhotVpc3OGAjdHFLC0gJSFcPYn1hjVlunbqdHIzCEllFnSzs3OBHOubE5XhEaW6hlHa_0VsyBV-y74ds7iY0qs7pIR1F7yXyzrrrhv8VnkDqtsrCjXg_ISDeQnm62GUHb1PuLuWh2wyvs_i-lH_cIOabAWBOgGE4IZcukFqY5l4sBDLRgVDsX-VFqg1AIZ2N0fKdeEurYB8uv1R6OvtqqpWo4Ztw09DGWC4hz3QhGF6BPM5kQS2vtY-VliyfS2lganbr58XGhGa6ZfFNIhqhYBcC0hraOcdMP9AlboKLBGpubcvi_JDKyRoFOEYPRCFiuLiTzzxNMbYsONjv9n_s0c6Bm37Sg2a5CXVBBFlHXFGDF9GAtJpzmgTHVWYmzN7r9K4O2bg7A6-NXvA4JmQSXi1RNHqnY9K4n0tbyGC8k7aUhffMK2moPO12wlqL1j7w_f-ucn8Hd_XkIbOxHSB55EuBcgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa19e45d1b.mp4?token=GlK83FTX2b22H7oSbaM_B_a6nNk-9AlYyxYyBXk1g4JPugVmyLmv8gI6stLgV4-mII_PTwFZaUFOES0dDyPVhMdL0Y3lT_62meKzsNP-ceTv2p9DdkFbXCbWGSSW4g6AunZjMOhyB9IeCEyTxBINQc-e9zH_MYc1X_8yVdZuoDX_dakomaEE8xTHwz_CzL8wFf6kRBY0t3DdHnpGhotVpc3OGAjdHFLC0gJSFcPYn1hjVlunbqdHIzCEllFnSzs3OBHOubE5XhEaW6hlHa_0VsyBV-y74ds7iY0qs7pIR1F7yXyzrrrhv8VnkDqtsrCjXg_ISDeQnm62GUHb1PuLuWh2wyvs_i-lH_cIOabAWBOgGE4IZcukFqY5l4sBDLRgVDsX-VFqg1AIZ2N0fKdeEurYB8uv1R6OvtqqpWo4Ztw09DGWC4hz3QhGF6BPM5kQS2vtY-VliyfS2lganbr58XGhGa6ZfFNIhqhYBcC0hraOcdMP9AlboKLBGpubcvi_JDKyRoFOEYPRCFiuLiTzzxNMbYsONjv9n_s0c6Bm37Sg2a5CXVBBFlHXFGDF9GAtJpzmgTHVWYmzN7r9K4O2bg7A6-NXvA4JmQSXi1RNHqnY9K4n0tbyGC8k7aUhffMK2moPO12wlqL1j7w_f-ucn8Hd_XkIbOxHSB55EuBcgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کارولین لیویت:
او تصمیم گرفت که فرزندانش را بیشتر از دونالد ترامپ دوست داشته باشد. من از این موضوع بسیار ناراحت هستم.
🔴
او باید به خانه برگردد و وقت خود را با فرزندانش بگذراند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/143601" target="_blank">📅 22:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS6B6wE_7wpzBTO7zGbdxkC5ILeaY0tyZHsIZAffQCsPk3O6fflPshHL9se7aQuhGVtRZRwIabOsCobqA3mUytW9YZYkMz0SAzIyDaC4lZHLdtu7fqHdnXqJXrUishklwwO_mKYKsnXt973MqJxvCT2OqU1NVxYRaHAVX2shzS-zQHtSNS7xdDxwwBJMV2Maf0lE8zRcXH0PeoOLsbkWTFkTJcAR9x-9alzyxpqITkB-8h89yA8JbhYLDIWvdrGRseeQhB7epoSb_YVIOirRsJEFHh6_v5J_mY6pRfEhXrfj_R9rtqBf0aB1p4CYz1xUKPNrhnvuP9o64yxA2AVqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تکذیب خبر منتشر شده به نقل از پرس‌تی‌‌وی در خصوص موضع ایران نسبت به پیشنهاد صلح ترامپ
‏
🔴
اکانت پرس‌تی‌وی در شبکه ایکس خبر منتشر شده به نقل از این رسانه را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143600" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0EpTl8DPkOaoRESqd-YPc_0t9HnmmUEugeJ-8mQ3W07TWjJrfEfcE-K1hbZbFvSE0c5R22r7dAwxKmxyPxUfWEWgpGc7svDVZSmXM5yzKHV-cnCVn25LquVQhP10YTHyJYmcF__EHARxT-OSLw3Olz4hmZzoEO4Czbxi3KLTVzPFBOlgVsL1q7bC1KGq7_Z1rqGn7iPIsw74KZRcqTPZcFa0HbJiLADjI-nYKFIDWRhsfOzKZKjfGcXvRmlfxX2QAwcrZcJSjFyhnDkDNCV7DOu6p_OtUJxAGyMX-IjzRkmXzXDdBbCKytDzFQzy1QiBCsQyZon2XGHTHAOZzBC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عاصم منیر با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/143599" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/الحدث: وزارت خزانه‌داری آمریکا به دولت عراق اعلام کرده است که باید تمام گذرگاه های مرزی زمینی خود با ایران را ببندد و از فرود هواپیماهای ایرانی در فرودگاه های عراق جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143598" target="_blank">📅 22:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQI4tnEpe3f17SWaVWNc23IvEFSmzgJMvbyKz439vZdknPAOelDd9ejToJbhiKSiCmvw20AX8WGg6O3STtKX62y3wsNvVknFI7coYFm0-b-3JrfIt9RmhHhA_KhvyvClLW5Q45lCxa_S6zlL3vlrQM8BU-7alOOwuwk5f67W_7sqynEWhJyXGMrMiFRfdBdLkNmH2bKr7_094nQPKRv1FKqEeVZCn1ewjfxl00pPmbiAwDGwGTkdxdxYg4XGfTOue5K8fuvpprv0EB4vpimATb2DWxeEeGmMUgbGBCBciMxeOkLNPLJyALpRQ9OwapCEt5Jc8h-rXepndXnng3TyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «داگ فورد، نخست‌وزیر استان انتاریوی کانادا، خیلی لاف می‌زند؛ اما بیشتر به‌عنوان برادر کم‌جاذبه‌تر، کم‌هوش‌تر و در مجموع نه‌چندان تأثیرگذارِ راب فورد فقید شناخته می‌شود.
🔴
آمریکا دهه‌ها بار کانادا را به دوش کشیده، اما دیگر تمام شد! آمریکا همیشه بسیار بزرگ‌تر، ثروتمندتر و قدرتمندتر از کانادا خواهد بود. بدون ایالات متحده، کانادا نمی‌تواند دوام بیاورد.
🔴
به‌دلیل رهبری ضعیف کنونی کانادا، به‌ویژه کارنی و فورد، دیگر اجازه نخواهیم داد از آمریکا سوءاستفاده کنند.
🔴
بخش زیادی از برق، نفت و گاز کانادا از طریق آمریکا منتقل می‌شود. کسی باید این دلقک‌ها را سر جایشان بنشاند، وگرنه عواقب بسیار بدتری در انتظار کانادا خواهد بود.
🔴
نرخ بیکاری کانادا اکنون ۱۰ درصد است و به‌سرعت افزایش می‌یابد. شرکت‌هایشان نیز به‌دلیل سیاست‌های شکست‌خورده و رهبری ناکارآمدشان در حال مهاجرت به آمریکا هستند.
🔴
دوران سوءاستفاده از کشاورزان و کسب‌وکارهای آمریکایی تمام شده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143597" target="_blank">📅 21:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f867e6c8f.mp4?token=DXFNNOm4O68c2JTUVi1rAl3DnUZa49meVc_YQl3cWa-KFHGg0RB3HI0TWq7SNEUyPXaqzgE9Qh8V30SC-lCju0MHHBDyCNlvPorC9XVCOSG6A-86LWdQtrqVYGDFlur0Qhn-QCb7JCkEUe16EBDTcnwa4Hqy-h0aeTcu0QCG3aAvC-44f-QsTzrzWxTQwYHMg6b47RjYgSGG2MRP1kXwrSzrwJ9UwaAicVPJO5HUEAKHsD6sZ04AiDGsY3caXWcn-XlAUhSBHz1Ne410xlmtqba6cFRbvDPfuuopVBK2WAeveLHWXZBY4MMtn2EUlAXqadCRkprTQFqOXqU05iwL2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f867e6c8f.mp4?token=DXFNNOm4O68c2JTUVi1rAl3DnUZa49meVc_YQl3cWa-KFHGg0RB3HI0TWq7SNEUyPXaqzgE9Qh8V30SC-lCju0MHHBDyCNlvPorC9XVCOSG6A-86LWdQtrqVYGDFlur0Qhn-QCb7JCkEUe16EBDTcnwa4Hqy-h0aeTcu0QCG3aAvC-44f-QsTzrzWxTQwYHMg6b47RjYgSGG2MRP1kXwrSzrwJ9UwaAicVPJO5HUEAKHsD6sZ04AiDGsY3caXWcn-XlAUhSBHz1Ne410xlmtqba6cFRbvDPfuuopVBK2WAeveLHWXZBY4MMtn2EUlAXqadCRkprTQFqOXqU05iwL2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره کانادا: به نخست‌وزیر کانادا: از سوءاستفاده از آمریکا دست بردارید.
🔴
تمام شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143596" target="_blank">📅 21:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ایالات متحده، سوریه را از فهرست حامیان تروریسم حذف کرد
‏
🔴
سوریه از سال ۱۹۷۹ تحت تحریم‌های کشورهای حامی تروریسم آمریکا قرار داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143595" target="_blank">📅 21:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
تحریم‌ها می‌تواند راه را برای اقدام علیه ایران پس از انتخابات کنگره هموار کند، زمانی که بازگشت به اقدام نظامی ممکن است.
🔴
ایران در یافتن مسیرهای حمل و نقل زمینی یا دریایی جایگزین با مشکلاتی روبرو است که توانایی آن را در ارائه کالاها و خدمات ضروری تضعیف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143594" target="_blank">📅 21:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بیانیه مشترک عربستان و فرانسه: پاریس و ریاض از ایران خواستند همکاری کامل خود با آژانس بین‌المللی انرژی اتمی را از سر گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143593" target="_blank">📅 21:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پرس‌تی‌وی: ایران مستقیماً پیشنهاد توافق صلح مورد حمایت ترامپ که چند ساعت پیش از طریق پاکستان به ایران ارائه شد را رد کرد و همچنین از سرگیری مذاکرات با ایالات متحده را نیز نپذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143592" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29cc221a8b.mp4?token=VxHGVXpGPu3HkMGfxG72TcM9VHWuZWronIu_61xXn37R_myfoHrTcIhiS3pHSjH-GBskjXOZ19OfJaw_J5MrX_uLpD4LBorAiRIeyZ7r3O-DmpC_DsZnWmtDF26tX4gjeANTgluN4jmuAjDdVsUlgVFKggDhjj2mLizzCDLs3Slkrp9pru3MQ3tZ9QhLpLBB1AbsBcacVike_wRVLDJ0dQgd4qBUi8JhJqNb_hqqqM62E3321fb0yLCrNxcIcIr1VOzW7UOPrKcaSlyoIPO4gZXnVT2ua6YlPPb_dF3ZTkjIQo7gDNfOm0O3fBGJlKDzQcpkZYmeRg9VxPeYoHAMxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29cc221a8b.mp4?token=VxHGVXpGPu3HkMGfxG72TcM9VHWuZWronIu_61xXn37R_myfoHrTcIhiS3pHSjH-GBskjXOZ19OfJaw_J5MrX_uLpD4LBorAiRIeyZ7r3O-DmpC_DsZnWmtDF26tX4gjeANTgluN4jmuAjDdVsUlgVFKggDhjj2mLizzCDLs3Slkrp9pru3MQ3tZ9QhLpLBB1AbsBcacVike_wRVLDJ0dQgd4qBUi8JhJqNb_hqqqM62E3321fb0yLCrNxcIcIr1VOzW7UOPrKcaSlyoIPO4gZXnVT2ua6YlPPb_dF3ZTkjIQo7gDNfOm0O3fBGJlKDzQcpkZYmeRg9VxPeYoHAMxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه داری آمریکا:
«نمی‌خواهم ضرب‌الاجلی تعیین کنم، اما صبر ما هم بی‌نهایت نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/143591" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdae7b8af.mp4?token=pWUDPMBDdR6N0yahmuv4s7Gkg5z3PUjuZYSNaM65XQeOn_M7FajFkhjWS7NX2J_RhT56_IAkWOQGGAfnxglDnLZPq6pSoJFHQscAIwrC5HKiHeUkfBTdpdW1LPhbKB99x2pOxhzEb4HPmd639CzyUchxwKS4B2-KZAVnw0HSW2lHOp4evDJYtBbctf1_SnaKWYii3no2CLN5f3bgPg-oNAt8Rza9VCPvyhLGDNVhiTaJL2b_irhmHwbshwXsoCH2StANzbUu8cjrfjMRV-nsXQS1QT6b_lrH2sgpqv7TPm0RpTr8eYhqX1LtTqe2RpqqAnO5SNLDI8UF-S6bqv_XaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdae7b8af.mp4?token=pWUDPMBDdR6N0yahmuv4s7Gkg5z3PUjuZYSNaM65XQeOn_M7FajFkhjWS7NX2J_RhT56_IAkWOQGGAfnxglDnLZPq6pSoJFHQscAIwrC5HKiHeUkfBTdpdW1LPhbKB99x2pOxhzEb4HPmd639CzyUchxwKS4B2-KZAVnw0HSW2lHOp4evDJYtBbctf1_SnaKWYii3no2CLN5f3bgPg-oNAt8Rza9VCPvyhLGDNVhiTaJL2b_irhmHwbshwXsoCH2StANzbUu8cjrfjMRV-nsXQS1QT6b_lrH2sgpqv7TPm0RpTr8eYhqX1LtTqe2RpqqAnO5SNLDI8UF-S6bqv_XaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: «گفتید ترامپ با رهبران جهان تماس می‌گیرد. با چه کسانی تماس گرفته است؟»
🔴
بِسِنت
: «قرار نیست اسمی ببریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143590" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه داری آمریکا:
«کسانی که در کنار آمریکا بایستند، از مزایای شراکت با ما بهره‌مند خواهند شد.»
🔴
تمام شعب بانک ملی باید تعطیل شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143589" target="_blank">📅 21:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f1344631.mp4?token=Gp9yZTIUvOGdJahkdL58djQDnopGYO42agh9fEhECyei0LkUNOyHvHNK6yGYAcltAugV61MPBO5BI_FD3d34njZlHIcZP02h4QEohqdqWpmjmc5ZmoJ9SR-TbNb7IhYVhSy6KulyFsB7SrOxODRHnQ0Etcot45NbqYZ97JYQR9XBq4ytGx95mqZJYi2rx-UeOSi8oNVqKeBppDShFA0Mse44KrfC89WIN4micM1ru-e-SCzekfWRj387C8_KL7g1YY-XkzR2dp97-uL2KbmiJOWAP08ctF_4kBYyuX8cIiNU5wg7SACmbYqE2_H432ahfmaPMA7ojosEM4ssk4y2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f1344631.mp4?token=Gp9yZTIUvOGdJahkdL58djQDnopGYO42agh9fEhECyei0LkUNOyHvHNK6yGYAcltAugV61MPBO5BI_FD3d34njZlHIcZP02h4QEohqdqWpmjmc5ZmoJ9SR-TbNb7IhYVhSy6KulyFsB7SrOxODRHnQ0Etcot45NbqYZ97JYQR9XBq4ytGx95mqZJYi2rx-UeOSi8oNVqKeBppDShFA0Mse44KrfC89WIN4micM1ru-e-SCzekfWRj387C8_KL7g1YY-XkzR2dp97-uL2KbmiJOWAP08ctF_4kBYyuX8cIiNU5wg7SACmbYqE2_H432ahfmaPMA7ojosEM4ssk4y2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: «شما این اقدام را یک «روز دی اقتصادی» توصیف می‌کنید، اما روز دی صرفاً تهدید به حمله نبود و آمریکا هم به آلمان مهلت نداد. پس چرا همین امروز تحریم‌ها را اعمال نمی‌کنید؟»
🔴
بِسِنت
: «چرا باید بخواهم نظام مالی جهانی را منفجر کنم؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143588" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7974dc7e.mp4?token=J_lvwWCsDWJV2-zEp0xwq-GlYXMTYPoc4EWErQFW2XGt52899aN-eO6kMZcrx-dGnUqaxP-1aS0c8AbQlRySVc6fjt7VmPhI1vmPaP5VrY12oKuZpCA79VmvSsrklSBovUATAOGdM-V4wWH0w6wQSI5oJyAMz5XWYblcFXfZjp7bgNBZHk5Xq3GuH1_jwa39TrFmMBrMzfVHUgYJg_lWYDnjyfabdt4jvTtUdESQrxaK1iF5kwrfH7Z28_dTbVif3FfZ9k_tativ6JseZ1JLiXhin2hkSIF98JH3eOzYK5aGs6iq_2joyz_zL6zuj6qiae3NagZzxP4PF7c3hw_-bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7974dc7e.mp4?token=J_lvwWCsDWJV2-zEp0xwq-GlYXMTYPoc4EWErQFW2XGt52899aN-eO6kMZcrx-dGnUqaxP-1aS0c8AbQlRySVc6fjt7VmPhI1vmPaP5VrY12oKuZpCA79VmvSsrklSBovUATAOGdM-V4wWH0w6wQSI5oJyAMz5XWYblcFXfZjp7bgNBZHk5Xq3GuH1_jwa39TrFmMBrMzfVHUgYJg_lWYDnjyfabdt4jvTtUdESQrxaK1iF5kwrfH7Z28_dTbVif3FfZ9k_tativ6JseZ1JLiXhin2hkSIF98JH3eOzYK5aGs6iq_2joyz_zL6zuj6qiae3NagZzxP4PF7c3hw_-bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: «آیا آمریکا و ترامپ همچنان می‌خواهند کانادا به یکی از ایالت‌های آمریکا تبدیل شود؟»
🔴
بِسِنت
: «فکر می‌کنم ترامپ می‌خواهد کانادا پای میز مذاکره بیاید و با حسن نیت مذاکره کند... متأسفانه نخست‌وزیر کارنی با مواضعی ضدآمریکایی و ضدترامپ به قدرت رسید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143587" target="_blank">📅 21:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه داری آمریکا:
«از امروز، فشار را تشدید می‌کنیم و هر منبع درآمد احتمالی را که سپاه پاسداران و حکومت ایران را تأمین مالی می‌کند، مسدود خواهیم کرد.
🔴
ما سیاستی را اجرا می‌کنیم که هدف آن جلوگیری کامل از هرگونه دور زدن محدودیت‌ها و نشت درآمد به ایران است.»
ایران دو راه پیش رو دارد: انزوای کامل جهانی یا بازگشت به شرایط عادی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143586" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbcc283cc3.mp4?token=XtPRBaAjkxog6sQSswgLzTn-vD7M9v_cJzkEgr1B9wL6p5OAB3LkgJGOSpNH4PxaxKtmp8R4n31BVWXK_C0jjhEDXVKIxUrDvQFlA0YJfe975D5bZi8rrY4h-FPOCNOKO6WydtVED6mNRKBoxsC4OqcwR7wRAh1eRQ3iVsAoSRxEUxS2fArmwcYG_mHq71x_xllVy8OczNx0WyXezdPm40NHxuHqkmOFnGAwJRE7bCEVMVLyH5lfkQ1PvT3x6oXnZCWP9Am7XRVfY24Py-h64_Yqi4s4i6WARJ2ud4sVl1nGScjfYf44-G5mA6KxUGnAmvdDHpDtp07y4GLIZgEbrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbcc283cc3.mp4?token=XtPRBaAjkxog6sQSswgLzTn-vD7M9v_cJzkEgr1B9wL6p5OAB3LkgJGOSpNH4PxaxKtmp8R4n31BVWXK_C0jjhEDXVKIxUrDvQFlA0YJfe975D5bZi8rrY4h-FPOCNOKO6WydtVED6mNRKBoxsC4OqcwR7wRAh1eRQ3iVsAoSRxEUxS2fArmwcYG_mHq71x_xllVy8OczNx0WyXezdPm40NHxuHqkmOFnGAwJRE7bCEVMVLyH5lfkQ1PvT3x6oXnZCWP9Am7XRVfY24Py-h64_Yqi4s4i6WARJ2ud4sVl1nGScjfYf44-G5mA6KxUGnAmvdDHpDtp07y4GLIZgEbrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه داری آمریکا:
«می‌خواهیم امروز به‌روشنی اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست.
🔴
اگر کسی معاملات ایران را تسهیل کند و بخشی از شبکه‌ای باشد که نفت ایران را به پول و سپس ابزاری برای سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهد گرفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143585" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اسکات بسنت: هر سازمانی که به هر شکلی، فعالیت‌های پولشویی را از طرف ایران تسهیل کند، از سیستم دلاری ایالات متحده حذف خواهد شد.
🔴
در دوران ترامپ، آمریکا دیگر در حال مدیریت تهدید ناشی از ایران نیست؛ بلکه ما در حال پایان دادن به آن هستیم!
🔴
هدف ما این است که هرگونه ارتباط اقتصادی را که جمهوری اسلامی را حفظ می‌کند، قطع کنیم، تا زمانی که تهران به تنهایی بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143584" target="_blank">📅 20:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه داری آمریکا:
«انتظار دارم تا پایان این هفته، خبر مهمی درباره تحریم یک مؤسسه مالی اعلام شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143583" target="_blank">📅 20:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42d6444d6.mp4?token=kuIdQQ45CMiJNgQsf7s2OrSm3bm9SHwiSPMxvHDuqpTVGwsnIxUD9JLalYz1t5mMyjyXyDfsYJ2NI_ws5EjvuI6tHoxUXHwLIaOVlpaxlp8niW4X2Sn8lcBOm3Sffysw2TRqTP3QT-AplPlBKSvUA2N-l4EYCUHrScVl-8W17wo1fgt582eL4uW3V-Ps47Zo0sITVJFomVih4K_oZJw6Ky4rvJiIV_F0R5XbVoCezFFTsn0T0gDMkFBXqZWqiFgA7jnY8mcKPdmKjYxpIj5__yvUwQwaIlddHaAz2aoVZB8bjLqVAIMPKIrSLKyT2GsYUHikzsehTDF3grQ6TTVvKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42d6444d6.mp4?token=kuIdQQ45CMiJNgQsf7s2OrSm3bm9SHwiSPMxvHDuqpTVGwsnIxUD9JLalYz1t5mMyjyXyDfsYJ2NI_ws5EjvuI6tHoxUXHwLIaOVlpaxlp8niW4X2Sn8lcBOm3Sffysw2TRqTP3QT-AplPlBKSvUA2N-l4EYCUHrScVl-8W17wo1fgt582eL4uW3V-Ps47Zo0sITVJFomVih4K_oZJw6Ky4rvJiIV_F0R5XbVoCezFFTsn0T0gDMkFBXqZWqiFgA7jnY8mcKPdmKjYxpIj5__yvUwQwaIlddHaAz2aoVZB8bjLqVAIMPKIrSLKyT2GsYUHikzsehTDF3grQ6TTVvKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
«خطاب به سربازان عادی که از این حکومت حمایت می‌کنند:  وقتی پرداخت حقوق‌تان یکی پس از دیگری متوقف می‌شود یا به‌ظاهر فقط به تأخیر می‌افتد، از خود بپرسید آیا فرماندهان‌تان کشور را به سوی پیروزی می‌برند یا ویرانی.
🔴
به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به مردم خود شلیک نکنند.
🔴
و خطاب به کسانی که به تهران کمک کرده‌اند: هزینه آزمودن عزم واشنگتن را دست‌کم نگیرید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143582" target="_blank">📅 20:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه ۶۰ نهاد، فرد و کشتی مرتبط با ایران در زمینه‌های انرژی هسته‌ای، موشکی و نفتی اعمال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143581" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02be258f93.mp4?token=ujd0gquiiGw5puDJbptTJM-xjsxrmXlYGGEVHHJKRtOeco9ZAuCXPoN3wJpd9H8P1b_qAOM6r9SWjAn6slskNu2pP56cODxGbH1zEwu6gxkmgj0SzaH_P3drq6aHX8ixVk7vRF8zmNrTrZlc2s99U6F_Hy5FHgDQeANndEFJTjAgKjMI3TyuPrHA4o8AtYV-BnITiF6XGt8UHAxnh-GAKH9IWmPBrYJBIWBELtwJG0LZG8_HxAviiU0hlHV8juxpgH0xzEB5qCKlrB-vBtsOyYPzmQ5T9XPOXv6sLhvUc_KCG8DZhFtSKeKibFyPudKTo7436WUDZ_w_sVkjPOsbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02be258f93.mp4?token=ujd0gquiiGw5puDJbptTJM-xjsxrmXlYGGEVHHJKRtOeco9ZAuCXPoN3wJpd9H8P1b_qAOM6r9SWjAn6slskNu2pP56cODxGbH1zEwu6gxkmgj0SzaH_P3drq6aHX8ixVk7vRF8zmNrTrZlc2s99U6F_Hy5FHgDQeANndEFJTjAgKjMI3TyuPrHA4o8AtYV-BnITiF6XGt8UHAxnh-GAKH9IWmPBrYJBIWBELtwJG0LZG8_HxAviiU0hlHV8juxpgH0xzEB5qCKlrB-vBtsOyYPzmQ5T9XPOXv6sLhvUc_KCG8DZhFtSKeKibFyPudKTo7436WUDZ_w_sVkjPOsbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: اکنون زمان آن رسیده است که رهبران جهان تصمیمی بین آمریکا و ایران اتخاذ کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143580" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4476bb9a85.mp4?token=lh827OwOPrNvRizw_fLxUaIVYWse5WNU7n5TOrb5RnOTO1JXrL5whGNW0TidyM1K0iegNyZckmmtNET_-Ea-cHjYezJPbVhOUorHvo4HEco0wMGoPQy1Xyg3J7jFvWDx6xv_60JCNhelCXMC3NRAGOHtD2YklTI2K9Cd1Yyu49bchHhBfjWivfKcFVffvNhA3TGakQfW6BZiasvW9waTH6wP02HnC2ZFOLEY_vICPpbd0nMz7WcnqefZiwa2DW41fRhmwfofBjFc_qfp6AV994EGS5ky417CJaW_CjR8jtjxEYqjETA63H3p9zFtEwnDJz5ZaaifAiUohu_8u8ARKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4476bb9a85.mp4?token=lh827OwOPrNvRizw_fLxUaIVYWse5WNU7n5TOrb5RnOTO1JXrL5whGNW0TidyM1K0iegNyZckmmtNET_-Ea-cHjYezJPbVhOUorHvo4HEco0wMGoPQy1Xyg3J7jFvWDx6xv_60JCNhelCXMC3NRAGOHtD2YklTI2K9Cd1Yyu49bchHhBfjWivfKcFVffvNhA3TGakQfW6BZiasvW9waTH6wP02HnC2ZFOLEY_vICPpbd0nMz7WcnqefZiwa2DW41fRhmwfofBjFc_qfp6AV994EGS5ky417CJaW_CjR8jtjxEYqjETA63H3p9zFtEwnDJz5ZaaifAiUohu_8u8ARKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: دونالد ترامپ با سران کشورهای جهان تماس تلفنی برقرار می‌کند و از آن‌ها درخواست می‌کند تا از هرگونه تعامل با رژیم ایران خودداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143579" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727ac25eaa.mp4?token=VfXPQCRrB9O3JXUPfTnQehv3tuxpvHQEV2AasUEv_wcJNXiO2bR7sWaBzk1lCa8xuCsE1WnIsZaFWtxO9GEnVnl8qMiKUFjmCJTx2hICj2BcLvI328VfL4sBKPP1QXkoaV8YNcu88nyVheH4C_LHGKrDb9YjjMLDhVcLA1YLBj2OnJjkzphPkW3tPCmUJg31x_49Q97LrNekL4rnh3TIhIazSoEDGM9XDFbgV11EdCjkqD7Mdq2wSG90-w-BANo2YNCqDEw5OPMz9ZqOSH_e77vprou0iYNh0vXNVImkQv9ljBCCMinMKbBny32PRxS0lME1HdrTAY6uJiku82YOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727ac25eaa.mp4?token=VfXPQCRrB9O3JXUPfTnQehv3tuxpvHQEV2AasUEv_wcJNXiO2bR7sWaBzk1lCa8xuCsE1WnIsZaFWtxO9GEnVnl8qMiKUFjmCJTx2hICj2BcLvI328VfL4sBKPP1QXkoaV8YNcu88nyVheH4C_LHGKrDb9YjjMLDhVcLA1YLBj2OnJjkzphPkW3tPCmUJg31x_49Q97LrNekL4rnh3TIhIazSoEDGM9XDFbgV11EdCjkqD7Mdq2wSG90-w-BANo2YNCqDEw5OPMz9ZqOSH_e77vprou0iYNh0vXNVImkQv9ljBCCMinMKbBny32PRxS0lME1HdrTAY6uJiku82YOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسِنت وزیر خزانه داری آمریکا:
«امروز وزارت خزانه‌داری آمریکا عملیات «طرد اقتصادی» را آغاز کرده است؛ کارزاری بی‌سابقه علیه ایران.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143578" target="_blank">📅 20:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdKL9nR-p_s9ko44SXsRvcduxEqDOlME9RBqWQ7mJMr2NgWgAHqkfvBJHQNU8Dq8LeCygb05jZtMnFTAoD6UdFAkKHz_gKE5sBUv7Ng00gCv0XgxfXD8_2Xn776P92WT7wKPIAQZ5Ol_LRtTf7gVCff_54WAGtoqX-4tDyL6IbyqVPUITPqMBxf0u7Xb4Kb2fTJz6W0An_PS3E4YzXk-CER20eANga38k0WWFZaUuQWpvUyobhc78j95ocaFNDuSgdAhkKn5TFgZa70LK5SPoOua1-QNlNafEsec_k5CYHvU0b51QGcr-1VhlQLh11-vpdLpJ8xNkcZ9tvvbU1IzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف آمریکایی‌ها می‌دانند که کسی گُنده‌لافی‌های آنها را باور نمی‌کند؛ آمریکا از لحاظ اقتصادی در شرایطی نیست که بخواهد روابط خود با دیگر کشورها را محدودتر از این کند.
🔴
شرکای تجاری ایران هم در رسانه‌ها و هم با ارسال پیام‌ به ما اعلام کرده‌اند که این اظهارات را به هیچ جا حساب نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143577" target="_blank">📅 20:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOSoFB8WHdhwV6GwWe08D6AT1qCF2_9WvB1sFred40Kf1LAD0n3IjXtSa-85PrNB2WKoHvT5Tf6uarEABoq6NnmhgDgmbgdJyJzDzuqlNw7ad9RMsZlbllBGuFmdWIei8ZZC27SNOgml1-K7Tba29BxabcE6JqLWfnefmmiVHIW2AwVgCxnPwdkapTMZJSCzHvAEz9vWTARTVVNX-eyH5CpqTYATiJr-FA6B9eIAKPBEqVzoPKybaHxiEQTM_MHKzlkEeBeDyXF0A7tYmY-hCAIzslSXL4IT-apKKCk7pzTyxAA7Q7jyz8MCBUFRgv87HlZJYViFjEmKDKhK51cmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ارز ایران همچنان در حال سقوط است: امروز، نرخ ارز از مرز 2 میلیون ریال به ازای هر دلار آمریکا فراتر رفت.
🔴
در طول تعطیلات آخر هفته، عبدالناصر همتی، رئیس بانک مرکزی ایران، اظهار داشت که کاهش همزمان درآمدهای نفتی، درآمد مالیاتی و کمک‌های تامین اجتماعی ایران، بر تمام بخش‌های اقتصاد این کشور تاثیر گذاشته است.
🔴
به زودی به 3 میلیون خواهیم رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143576" target="_blank">📅 20:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کانادا تهدید کرده است که در صورت تشدید جنگ تجاری بین کانادا و ایالات متحده صادرات تمامی برق و مواد معدنی حیاتی خود از جمله نیکل با عیار بالا و اورانیوم به آمریکا را قطع خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143575" target="_blank">📅 20:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
خبرگزاری ای‌بی‌سی به نقل از یک منبع:
وزارت خزانه‌داری قصد دارد اطلاعاتی را به عنوان هشدار به کشورهایی که به ایران در دور زدن تحریم‌ها کمک می‌کنند، ارائه دهد.
🔴
وزارت خزانه‌داری آمریکا شبکه قاچاق نفت و دور زدن تحریم‌های ایران را شناسایی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143574" target="_blank">📅 20:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / نتانیاهو: ایران سعی کرد یکی از پسران من را ترور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143573" target="_blank">📅 20:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEOXo1DVOgLKAm2uP2cpOensthRs1Eh5XN83SY6J0cnzVudZrIlnj8ziGhMNvKGFs26j7l5mmzyiZm-8TozSQNni0HuaYUEOlY_yGdNdLiwthDb9yBR_hwj27YiTmNmhT0aj7sXT19hwpAR1VptKR-JpTMOIqwkXsm2iL96Wu0KWC2CMLx-Kk-YQpjI2BCCNjTaXCwaANRn42kw0QLYtNAkuQs9MuROkfvWMyLt1UFEIlKXUuDAy2pUg6kgiLLww4hYtQirZf2lf_-fEaV9pU3dffh9e5aKufWW5MJxL6mO0usT-dHnbvexppJLUxqp_eNEw4qPxkW4mar8WzVvbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: دموکرات‌های افراطی، با نظرسنجی‌های دروغین، به شدت در حال تحریک هستند. آن‌ها این نظرسنجی‌ها را در سطحی بی‌سابقه منتشر می‌کنند.
🔴
آن‌ها این کار را با عنوان "عملیات تضعیف روحیه" انجام می‌دهند، به این معنی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها از خانه خارج نشوند و رای ندهند. اما نظرسنجی‌های واقعی فوق‌العاده هستند و روحیه در کشور ما هرگز به این میزان بالا نبوده است.
🔴
ما در برابر همه، از جمله ایران، پیروز می‌شویم، کشوری که در یک بحران اقتصادی و نظامی عمیق فرو رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143572" target="_blank">📅 19:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
قالیباف: پیگیر اجرای شروط تفاهم هستیم و این آمریکاست که باید به تعهداتش پایبند باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/143571" target="_blank">📅 19:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA8d-0TiwmzFM59YZeiVA2amg2IeA291KxnDnqnqyiPrwxadDSa5DWRsuJ41QlWco2FrSQ7pvbcFCnRtY2PV_dNFgUsY7Z0GZ-ETe7Bpu5VchalFhsgwRT7_c0BD331axxzPsFMDOTqETl4qRexW7f3z8Z4XX6t2Ca1TMCLv9lbLy2K5Ycjz637Lj-NCWYNYsv039g6OYREwBRT45iFlRELS01MC23nO9QemxDcX5eMz3G9Nvu7P0yGYgIXz5A8OrH8sMBTlDIvWAegrvfYsMy2udGSysoIO3xfbnRj-_Zn44IWdOPBsNyz1Xgghg5z_daUKFJMehx-bIn3Dxq6Nhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس دیدار و گفتگو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143570" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
الجزیره، با استناد به یک منبع نظامی یمن، گزارش می‌دهد که انصارالله یک کاروان نظامی متعلق به نیروهای سپاه کشور در مناطق العبر و الوادیه را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143569" target="_blank">📅 19:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
معاون اول رئیس‌جمهور: آقای قالیباف قول داده طرح مقابله با نفوذ را از دستورکار مجلس خارج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143568" target="_blank">📅 19:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
الجزیره به نقل از منابع آگاه: ترامپ هفته گذشته با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، تماس تلفنی برقرار کرد.
🔴
ترامپ در گفت‌وگو با فیلد مارشال منیر درباره موضوع ایران رایزنی کرد و از او خواست از نفوذ پاکستان برای ازسرگیری مذاکرات استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143567" target="_blank">📅 19:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آذر منصوری، رئیس جبهه اصلاحات: آقای سقاب اصفهانی نگران خرد شدن شیشه‌هایتان‌ نباشید و عاملان قاچاق سوخت را معرفی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143566" target="_blank">📅 19:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0d58c62c.mp4?token=VRCeR2ruvs3l-68khBWC2cv-oBo0Yi944iei18-wx5h_3OT0GHV7_vgy35nlLV6VJDOQDtHOXovhruRdnK1-GkN_3owFHMtq_Vd9As0fgUWAVUtWSsqverQEMRfyYYpJOADGN5kgJ5IjF0y36r_L-o-yBi3qB0SieM4EFfeNk4ISJ0SJ26TIoXe_uttz7xUF8XfaNc9ySI-jD4U6b70ZZwrBFiz4dZJ6dNIr7c4VxWV4-NGCVlaY7tKqAT7wsGFhkf3dsx1n6B0TrOOAjSqTNypgxHVmeNQnZHY5nMaOy5hyHTxFUXNFcl_Cm0cAJvTvzFSqimFVkKZkHvxyDk-q5T5CD-sVD2fDZ-znS2_p9maXp6NeQD-VhYv7Cpiu-lf3ZoMvaI7f9p26ksRFls3nMpD6NK5-MUde0WhTf_c3E5ifmsCrPaEuelS526p-6IMe1Ma_u5yNOK8c4897-xNlQsuf69tNsSz0JeHeaoWmx4aexnJLChhufNpueF42mS03Pw7WsZwsVU3WDT-8w9KvdLRlg2YnbfDwtGRFjHUnCuLqp8OEwKhHFoTLD5wsgr7x2aJbBxW7ded2TtLDyr02GdtFsa74zLcz0_5PWpEGPr_R4CTPqsb4SFrk0I7uhlK4OBcrH1hc3ijSVsgoPH0ynTwHH9NQqLerFy_X0L5jsB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0d58c62c.mp4?token=VRCeR2ruvs3l-68khBWC2cv-oBo0Yi944iei18-wx5h_3OT0GHV7_vgy35nlLV6VJDOQDtHOXovhruRdnK1-GkN_3owFHMtq_Vd9As0fgUWAVUtWSsqverQEMRfyYYpJOADGN5kgJ5IjF0y36r_L-o-yBi3qB0SieM4EFfeNk4ISJ0SJ26TIoXe_uttz7xUF8XfaNc9ySI-jD4U6b70ZZwrBFiz4dZJ6dNIr7c4VxWV4-NGCVlaY7tKqAT7wsGFhkf3dsx1n6B0TrOOAjSqTNypgxHVmeNQnZHY5nMaOy5hyHTxFUXNFcl_Cm0cAJvTvzFSqimFVkKZkHvxyDk-q5T5CD-sVD2fDZ-znS2_p9maXp6NeQD-VhYv7Cpiu-lf3ZoMvaI7f9p26ksRFls3nMpD6NK5-MUde0WhTf_c3E5ifmsCrPaEuelS526p-6IMe1Ma_u5yNOK8c4897-xNlQsuf69tNsSz0JeHeaoWmx4aexnJLChhufNpueF42mS03Pw7WsZwsVU3WDT-8w9KvdLRlg2YnbfDwtGRFjHUnCuLqp8OEwKhHFoTLD5wsgr7x2aJbBxW7ded2TtLDyr02GdtFsa74zLcz0_5PWpEGPr_R4CTPqsb4SFrk0I7uhlK4OBcrH1hc3ijSVsgoPH0ynTwHH9NQqLerFy_X0L5jsB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد ... چشم:
محسن رضایی حریف ترامپ میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143565" target="_blank">📅 19:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به جنوب لبنان همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143564" target="_blank">📅 18:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اداره ملی استاندارد افغانستان مدعی شد ۱۳۹ تن کالای ایرانی شامل مصالح ساختمانی و دیگر اقلام، پس از بررسی‌های فنی به دلیل «عدم تطابق با استانداردهای داخلی» اجازه ورود به بازار افغانستان را پیدا نکرده و به کشور مبدأ بازگردانده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143563" target="_blank">📅 18:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwgyZLknMYPjDyPU_NQR9isI6zdDOovRm6q1ywWPnmck-nJ11n7cpbTN5zaldgI9otrTd52VsFjaUgUm4RFzYsdV68wEehgxh8e5Nf7ySB2BGXNXP_52oQLKhCCx4WHZdDJ9yaXaWMA4uatSmXIUzke1Sw1ccBbjDW5AnprmfdPj78b5tyBFHyT1yT-ydc2XwlhNpSwhyUNDRuRMUP0S_rCef6FYsGauteV-CKxKjyGZ9rqIlZYP5SJN6XXpaRZxNzGW_gkyrGCVLKFRrIwbvYVX7zfcJE7Uc4ottSvwpQbVPgW6AJuL8zJG4L0bItJtIyboeg-Wx7-CWgJ3LKPV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوگ فورد، وزیر اِنتاریوی کانادا، به خبرگزاری آسوشیتد پرس گفت که رونالد ریگان به‌خاطر سیاست‌های تجاری ترامپ «دارد استفراغ می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143562" target="_blank">📅 18:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی سپاه در واکنش به جنگ اقتصادی آمریکا: جای هیچ نگرانی نیست برای هر اقدام آمریکا سناریو داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143561" target="_blank">📅 18:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBZfzLCytRQ45xDjQ1hWJIX58lYIUX0GryFdmYUUiriIJhNDM4-eheryUS9J7IsNlVOLKIdrqqpTi_u_ScxgOHsp9U526sCjBgxwu4HO-Nv1jgQskQU3Ae3BT2c6L0Rl5k-1m70PLTlmjiSolGCh92dH6K0fvboskDMHI8Vd25oOtvD_MyEVjwcFU8MrMFzq4algJ7bU3Z4mmq29Mi1zJ5I1_WFRw1nhD7WaeQMFkX9NkuuVAEXKjeoYDVXuCg7HlzxQ5D2qBagxB2Qm-hvVHVw1dDvkxU7yD0yDHdpAoVGjvhdZT8wnmQlgR1_XXTNJCxPkRJfs3GqNcavjMqQQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون قانونی را امضا کرده است که استفاده از تلفن‌های همراه در دبیرستان‌ها را ممنوع می‌کند.
🔴
بر اساس گفته‌های او، این اقدام به «
بازگرداندن آرامش به فرآیند یادگیری
» کمک خواهد کرد. ممنوعیت استفاده از تلفن‌های همراه در مدارس متوسطه از سپتامبر ۲۰۲۵ در حال اجرا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143560" target="_blank">📅 18:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR-NdoVn-d2JWVXIuDISsXtQLVbg8qOnZxR4Ngr9P3OC9z2U_OFxnRgd4tTWOBM1le2kN-w1fC2FEUs4OIoEY38cqEfweJvcJXS2Wl_907Lf8qJ29IjuVUdrxWkn3u4rpEgoHCDtrt0CXHHhE6CHEBqhwdqt2GQHkgDR2-0fuH1UbRmlR3TD1FAxtITJmSTfUq08EVr5k9___U93LZvjypvddodJB8vEyM4upEByMX1qy2iVBJsmDp-KQNpRaHBhhKFv1u_K6RD5JAG3kHPu73L2MAQS-F27nHrREl0PQIMs4f-t5_NdkE-URLFm8qMthK16zHdkypApo0MRiZ6l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: «مدیران خودرو» بابت هر خودروی وارداتی، به طور میانگین ۴۷۰۰ دلار گران‌‌تر حساب کرده/ ارزی که «مدیران خودرو» طی ۵ سال از بانک مرکزی دریافت نموده، با ارزشِ کُل شرکتِ اصلی چینی (چری) برابری می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143559" target="_blank">📅 18:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی سپاه در واکنش به جنگ اقتصادی آمریکا: جای هیچ نگرانی نیست برای هر اقدام آمریکا سناریو داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143558" target="_blank">📅 18:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7c35d2e7.mp4?token=JvpzChnshqaH24miP5VdEhKI-QhP6UQaoFnsYsV5P7eF5tRUb2OF-RIkLnQMtnJznh-HuUIgqorHYoYNIIm4WE_RuTvI945SbY0aYaSC6jnKe4boKy3rpIx736DmxRwLlg2j-Njx73JQM9w1YZ0t_m5nKOJNX5GUsT_ZRhDDD36JJGi5BFvZyQPc7UZZVb-YrP06cZy2RjIliY5ryfCScrNR8HLuQLzu7rMR73evkNnjzetZulOOTIdw9yJYLJhEPKpIh7ScB-mqdD3t4_XyXFQhk1tYTSxPITpGmioF6kXk753LeDnt1hT8Nm0DEwVLY6PDhsiwZu6_j9AWnMDPCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7c35d2e7.mp4?token=JvpzChnshqaH24miP5VdEhKI-QhP6UQaoFnsYsV5P7eF5tRUb2OF-RIkLnQMtnJznh-HuUIgqorHYoYNIIm4WE_RuTvI945SbY0aYaSC6jnKe4boKy3rpIx736DmxRwLlg2j-Njx73JQM9w1YZ0t_m5nKOJNX5GUsT_ZRhDDD36JJGi5BFvZyQPc7UZZVb-YrP06cZy2RjIliY5ryfCScrNR8HLuQLzu7rMR73evkNnjzetZulOOTIdw9yJYLJhEPKpIh7ScB-mqdD3t4_XyXFQhk1tYTSxPITpGmioF6kXk753LeDnt1hT8Nm0DEwVLY6PDhsiwZu6_j9AWnMDPCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از حمله حوثی‌های یمن، انبار‌ سلاح ارتش عربستان و نیروهای وابسته در گذرگاه ودیعه در آتش می‌سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143557" target="_blank">📅 18:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یمن: یک کشتی سعودی را با بالستیک هدف قرار دادیم
🔴
نیروهای مسلح یمن: نفتکش امزان متعلق به دشمن سعودی را در نزدیکی بندر ینبع با موشک بالستیک هدف قرار گرفت که منجر به آتش‌سوزی در کشتی و فرار تعدادی از کشتی‌های دیگر حاضر در منطقه شد.
🔴
این عملیات در چارچوب تصمیم نیروهای مسلح مبنی بر ممنوعیت تردد دریایی برای دشمن سعودی و تثبیت معادله محاصره دربرابر محاصره انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143556" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر امور خارجه تأکید کرد که گفت‌وگو، دیپلماسی و اجرای تفاهم‌نامه، راه تحقق ثبات پایدار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143555" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
دلار به ۲۰۰ هزار تومان رسید؛
🔴
از ثبات ۷ تومانی و قدرت ریال در دوران پهلوی، تا سقوط بی‌سابقه و نابودی معیشت در قهقرای رژیم جمهوری اسلامی.
🤔
یک مشت حرام زاده دزد زندگی چند نسل رو از بین بردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143554" target="_blank">📅 18:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شرکت ملی حمل‌ونقل دریایی عربستان سعودی اعلام کرد که کشتی امزان، متعلق به این شرکت، در دریای سرخ هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143553" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرنگار الجزیره: جنگنده‌های اسرائیلی ۲ حملهٔ هوایی به شهرک المنصوری و مناطق اطراف آن در شهرستان صور، واقع در جنوب لبنان، انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143552" target="_blank">📅 18:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: ایران ۴۵ نفتکش را به‌دلیل نقض مقررات عبور از هرمز در فهرست سیاه قرار داد؛ این کشتی‌ها ممکن است جریمه یا توقیف شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143551" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع گزارش داد:
وزارت خزانه‌داری آمریکا قصد دارد دامنه تحریم‌های ثانویه علیه کشورها و نهادهایی را که با ایران تجارت می‌کنند، گسترش دهد و فعالیت در برخی بخش‌های اقتصاد ایران را هدف قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143550" target="_blank">📅 18:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmnGQOWC5YPQxyKOoR0phZT551j5Tg8UgQkqv_U_xHpAIdbGNRWHExQ3bvkFIByGktLmFBOm5AiuEfVjRfBEru0f0KVG0V4Bc5hCeUjWIZUQlE8zJqCJgk0DdfixSuCIqEc6nF3XO-z3o2y3cA52e0QSwtiIX6OpK2aaMcZh2YJPtvwfxwBg1eXQdsXOPJcWHdmgs1y7MqKDxYVTWCRyeDhNoHEiBWaOwwKxGyH_f6CqnDXxO7ddx04FIQdPyWcHhZFs5l8DpZUng6kSK-t8byVAocRgImjT24KJyY0lNuE_zOkSuaYoNdsb-7L23rtsbK83FUVOudWl6mu1MErpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1SvJKcqOJcAEMfP6TJuqi_93OstEXF3VY50DmV3MHwTYTbunNWRrS0aWV_AcO2UPOWQWcHfLgkDkfySxsjubpJQgQo0Cicxdqg8CjaoKBoa2GPwEjffqEtwWKPBqSMytHGu0EWK15_IAprVV49LXL44RZY8rE2k4-IN_KOMjdhGAmTNvtBG5RxTVLiW1wx_Cwc9of1uLFRN5yX_9Po061tey6hxe6xgFTGqRux_zSfTcY7xtzNaIPglmni8l3KXlnEJ3BCNYTvK6MhEWRFf6-vCWcikEShrI8gnDYMLlqHntdBk6vBqt_Pa-m9DYPwZLgTE2snxuv6RrOf949YzpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جهش قیمت‌ موبایل
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143548" target="_blank">📅 17:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otpffSDHGOO8vF8tAOgVK_BRkt3YPvmR5uf8gPNPMheJkEeKJPOy3P7OgmXnTUYKgi3nv1h9STuqPW4i7CSDJPI5xuvSzhZEM9YABORxxfrKiFdnb2LbPwRAVoZJJyxGwu9gcbr8TQxrJ8gmNpzae28KO2a4rIE7HOhrlDhsw_8JZvcRJqCqR5eeyrFB80yVs96ElQXafTjatHWxcTU5o7d013CfDxCXWJijb7FmGBkyx585c4zYXnekoWIPYxh97aU97xu6RRrx0V_cabX2wxmkSlICRxeFimJfqj8ntYFdbJzczEN2kTiW6c-AORN9ixGDT0B8_zoZZ0i-g7YwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی خطاب به بسنت: ایران نیابتی‌هایتان را نابود می‌کند و اقتصادتان را به زانو درمی‌آورد. شما و آن فرعون، به‌خاطر اینکه مردم آمریکا را گرفتار این همه رنج و بدبختی کرده‌اید، از سوی خود مردم آمریکا نفرین خواهید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143547" target="_blank">📅 17:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3dnEo89qDUF6inpzN_J-dEyVjQalAlFXAA9Qbc02YYAYlQ_LUhu6sL6H_QdF2Y8UlHrVZyMy6gPDFuy_5CgSfm6MrZCmg330Wy-lTI5u_8c0lEkv8dq8gkNkAaf5EXS55F5V1APkVZ-BodwtNcjCAyQ6U6571KnBUAYYuQlJZTU8RAUgEGdRQiB-Ldx1hSRWE3j_h94aLTM7azju1NUs5l1adCXt2qdOqKkorUWbuxgFq38nEe8rbxbp6iGKe__qd20VoeocnEBP376-mCKGa9O3oQEnO9GN-bZt-XAM7467HljttqrTKnCV9QcYb8W9cHWbj581ogzJrNEHtCzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لقب مجری شبکه سه برای محسن رضایی: «سرلشکر فیلدمارشال»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143546" target="_blank">📅 17:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=BDDgQCR4KBNFYaLAvYNrqlla9aZXo7IilCbw8OaJshscQU9qG5ybEvQ83w8N3MX1gX-8VywVtbATTjbjh8bDYkjKvUx5MyWYo1ip4BrfhKE2zf7dh2YH9ojVogqFtniGDHpbs6mHUuLQF6HGi1DxmisHVGZeEZY6uEN0j4AunBn_AlRosxlwhebLMTDLNlc3NrW97qfyq0SC6uH-iF4U-33HvQiI1yndKdXk7SEA85tEPP-miC9mZqQRxVetw6FC-Xi4IOOnlrBjFQSA8Q9YuLwSStvEnlVNGikOuamwnzXAWP_W37PEDBDjirdK8wW1Nx5dSyqI2d-Xf7_DPwsGmq3ryVN8amiRrnNVT_ebcVjCSRLZH7L2lDZI3VRkFPVH-3_mGZqPowDoQQ-CHdjFWQWvbTaDCSgbUOnnv3HVKdWv3Ct4LxeYoVVkMc43o2-umFLaKv7lam2p3CP5r-Je3HVrBDzVcA3_6VjxEm5vNfuwOwLQW8myq4VFkkSJGXVCjbWU4EpCgSi8Sc6IcogIcSd40tbENWgBXqm1ZvC3c69nw_2d6XDHLhDFm-hA5x7mZ_qvp6vx8QnmZWP1LYCSQi4PMQwlG6Aif-9eZA-GP4P3o9thq6lRRJ3sT1jDrMS1bCOATXYx-k9K4dFe_Rl6FLKGdSyUvTOnT41queF0uzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280cc51c55.mp4?token=BDDgQCR4KBNFYaLAvYNrqlla9aZXo7IilCbw8OaJshscQU9qG5ybEvQ83w8N3MX1gX-8VywVtbATTjbjh8bDYkjKvUx5MyWYo1ip4BrfhKE2zf7dh2YH9ojVogqFtniGDHpbs6mHUuLQF6HGi1DxmisHVGZeEZY6uEN0j4AunBn_AlRosxlwhebLMTDLNlc3NrW97qfyq0SC6uH-iF4U-33HvQiI1yndKdXk7SEA85tEPP-miC9mZqQRxVetw6FC-Xi4IOOnlrBjFQSA8Q9YuLwSStvEnlVNGikOuamwnzXAWP_W37PEDBDjirdK8wW1Nx5dSyqI2d-Xf7_DPwsGmq3ryVN8amiRrnNVT_ebcVjCSRLZH7L2lDZI3VRkFPVH-3_mGZqPowDoQQ-CHdjFWQWvbTaDCSgbUOnnv3HVKdWv3Ct4LxeYoVVkMc43o2-umFLaKv7lam2p3CP5r-Je3HVrBDzVcA3_6VjxEm5vNfuwOwLQW8myq4VFkkSJGXVCjbWU4EpCgSi8Sc6IcogIcSd40tbENWgBXqm1ZvC3c69nw_2d6XDHLhDFm-hA5x7mZ_qvp6vx8QnmZWP1LYCSQi4PMQwlG6Aif-9eZA-GP4P3o9thq6lRRJ3sT1jDrMS1bCOATXYx-k9K4dFe_Rl6FLKGdSyUvTOnT41queF0uzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لقب مجری شبکه سه برای محسن رضایی: «سرلشکر فیلدمارشال»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143545" target="_blank">📅 17:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad49a3037.mp4?token=CbEttH_FOHGM4Yta5VHiRwdErfdp6mK9nBJTk2RLdbCrRu4wramKR4PrQHE2HN6xXq_IQy6WmiwcXzkm4iBXvhQikrSf7VSaPZ9RfPBTosW92majf7vQ9KzlZe4phcCQAe3gCbIlM0OHu5ZpMt9FSsXx39h3TKKg_0rtLgqyPzguTOpzNLZEhTY-v88NDdtsq0U-ZVxwWa02Rq9qJv3vJSiAqyludUCE2ebMENWKVVqElsbNxTWKZfsfg43Agacs5eRSBnCB0ydDC2PfR_yrmIn9Ku8RcBU5IAgq5NpUSh1c5mC1wYdyzV3u0bLr3VIdSLKtROGcfwd8Qh0kxsSTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad49a3037.mp4?token=CbEttH_FOHGM4Yta5VHiRwdErfdp6mK9nBJTk2RLdbCrRu4wramKR4PrQHE2HN6xXq_IQy6WmiwcXzkm4iBXvhQikrSf7VSaPZ9RfPBTosW92majf7vQ9KzlZe4phcCQAe3gCbIlM0OHu5ZpMt9FSsXx39h3TKKg_0rtLgqyPzguTOpzNLZEhTY-v88NDdtsq0U-ZVxwWa02Rq9qJv3vJSiAqyludUCE2ebMENWKVVqElsbNxTWKZfsfg43Agacs5eRSBnCB0ydDC2PfR_yrmIn9Ku8RcBU5IAgq5NpUSh1c5mC1wYdyzV3u0bLr3VIdSLKtROGcfwd8Qh0kxsSTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوثکام (SOUTHCOM) اعلام کرد که نیروی مشترک مأموریت‌های نیمکره غربی آن، در روز یکشنبه به یک کشتی مشکوک به قاچاق مواد مخدر در اقیانوس آرام شرقی حمله کرد.
دو نفر از مظنونان «تروریست‌های مواد مخدر» کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143544" target="_blank">📅 17:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b8e92ec8.mp4?token=ErzWFHGce0Jf7ChPMJm6Dcl0rRwoofkTycxgsC3LR-OzJhgfIbJOQoBOIAQuU2MPb_ZTRuphPKqOeRq16B7MK15PbMXGgktAjfFAGb9MiL1ct3I33uts62Hmg_mdKrXjqSKTW-B0pvuWoz0yNfxOpMpHiyaJ837WSYHJzqxsWb37uNV-XRlODWCEsqdKb7tYECksWaGZgkW26wIdUbmQUbCD1I3IksmngZoRLlfJwoq2JsuqIZLHRrA89-PwcGYlQ0L5S2beU0BhLKoxOJFKn4Tpt_5B-xc7Qm5iGQnvVKtmSGJwC9vteOvdLFlgbci8-lZkMQYlgkXGRxc8lojPeX3pCD1S60ueIScAfbUjTEliXMLmeT88vpqUlcBXDT9yRu5u4Mw5ovpAPQH1U9nFS_iOIJvzdDZEYAp4xAAold4h2glYBC5jB-MeASWmkRlB6DvnfHbMD5yDdpbSMn1C5nyRIo58k2ijmEPbgBsj0F32xn88Vc_YjWGj7_NaTGII9uQv88MgqDwNzW93B3GMzgwD6Xo19lE3-72PGgxtem2Pl9XbfROjOPJC6GdyHcurGkA_Q7xwGPlOgbVUoGmmMaJlW8xt2o8xdci1FrTXdz1UzkfndiRUPia4ScmqjIkyBYJBJNdqdqcjfbFm4OmtYfQ-QuuB97LVy-lVnLdqETY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b8e92ec8.mp4?token=ErzWFHGce0Jf7ChPMJm6Dcl0rRwoofkTycxgsC3LR-OzJhgfIbJOQoBOIAQuU2MPb_ZTRuphPKqOeRq16B7MK15PbMXGgktAjfFAGb9MiL1ct3I33uts62Hmg_mdKrXjqSKTW-B0pvuWoz0yNfxOpMpHiyaJ837WSYHJzqxsWb37uNV-XRlODWCEsqdKb7tYECksWaGZgkW26wIdUbmQUbCD1I3IksmngZoRLlfJwoq2JsuqIZLHRrA89-PwcGYlQ0L5S2beU0BhLKoxOJFKn4Tpt_5B-xc7Qm5iGQnvVKtmSGJwC9vteOvdLFlgbci8-lZkMQYlgkXGRxc8lojPeX3pCD1S60ueIScAfbUjTEliXMLmeT88vpqUlcBXDT9yRu5u4Mw5ovpAPQH1U9nFS_iOIJvzdDZEYAp4xAAold4h2glYBC5jB-MeASWmkRlB6DvnfHbMD5yDdpbSMn1C5nyRIo58k2ijmEPbgBsj0F32xn88Vc_YjWGj7_NaTGII9uQv88MgqDwNzW93B3GMzgwD6Xo19lE3-72PGgxtem2Pl9XbfROjOPJC6GdyHcurGkA_Q7xwGPlOgbVUoGmmMaJlW8xt2o8xdci1FrTXdz1UzkfndiRUPia4ScmqjIkyBYJBJNdqdqcjfbFm4OmtYfQ-QuuB97LVy-lVnLdqETY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده‌ای امروز مقابل استانداری اصفهان تجمع کردن و گفتن با بی حجابی برخورد بشه
🔴
پ.ن: نظرتون راجع به اینا چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143543" target="_blank">📅 17:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سپاه:
از این پیج هم رد میشیم و به قله میرسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143542" target="_blank">📅 17:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22d38c95.mp4?token=v1-_sPDux1LUzuMJbZAsqkDVfwQXxwYulQcVUF9UC5XThdkdfViqPWmd9NLiPHTLCcuVUOxvjIX-_HF1fBQx3vfPZvzSUdvoG0Lx5v9O6zXE7jYRTwxE9Qyx4PR3wW85IpQfAov_VdCDExGnaeGJoG-EBEEBghSRL1Y6Qm5Cxx3uTC4idZBGsgYIqPK3kcBbX1CVYxs3nEAnqxhF5s5U8DzuolybHGYWyjzxKrKtJ9yg1oEKWPvRCpXC8HRruZOk58Rv2MnRPmIbvt5__KOsqZkvXbA9UcQiTSZWoENO205vxXT6luZpnFWH8iLG__j7GF5OpFkwS47y3RIcL9Wlakaw6ozY-PK7ilYy7Vp71S-zTFivUzVpuPVp_2Mii5Ef9cQSrXuFu7h5aQzP1yGv3T-vyKJl4bjUpcCyjDXmQ8dnwgOBcZ_2DtNl0uXpdBKPilK5Mz6k9CxkAQVxHXeGOPeleZMhFdHwNauot83_xwnDmretN5QITWf2sJOwJTzIhOjmXCUuU_U22p9ANr94j73vOuWWKz9GJbw6KVXcwlgfSbysYq3CPF2v0zNhqcPBZzDVNmtl2_qHJlYNbo_PpUEoOQvoZEfGzcKsAZx_dpSzIA_2mdddz3H9Toe6DQfxzN-2BVL3YNMT_Chj4O4qn9hmkjsSe3_9kc8QVcHxYlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22d38c95.mp4?token=v1-_sPDux1LUzuMJbZAsqkDVfwQXxwYulQcVUF9UC5XThdkdfViqPWmd9NLiPHTLCcuVUOxvjIX-_HF1fBQx3vfPZvzSUdvoG0Lx5v9O6zXE7jYRTwxE9Qyx4PR3wW85IpQfAov_VdCDExGnaeGJoG-EBEEBghSRL1Y6Qm5Cxx3uTC4idZBGsgYIqPK3kcBbX1CVYxs3nEAnqxhF5s5U8DzuolybHGYWyjzxKrKtJ9yg1oEKWPvRCpXC8HRruZOk58Rv2MnRPmIbvt5__KOsqZkvXbA9UcQiTSZWoENO205vxXT6luZpnFWH8iLG__j7GF5OpFkwS47y3RIcL9Wlakaw6ozY-PK7ilYy7Vp71S-zTFivUzVpuPVp_2Mii5Ef9cQSrXuFu7h5aQzP1yGv3T-vyKJl4bjUpcCyjDXmQ8dnwgOBcZ_2DtNl0uXpdBKPilK5Mz6k9CxkAQVxHXeGOPeleZMhFdHwNauot83_xwnDmretN5QITWf2sJOwJTzIhOjmXCUuU_U22p9ANr94j73vOuWWKz9GJbw6KVXcwlgfSbysYq3CPF2v0zNhqcPBZzDVNmtl2_qHJlYNbo_PpUEoOQvoZEfGzcKsAZx_dpSzIA_2mdddz3H9Toe6DQfxzN-2BVL3YNMT_Chj4O4qn9hmkjsSe3_9kc8QVcHxYlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوست پسر دختر رضا رشیدپور: مردم دلار ۱۹۰تومنی هم براشون مهم نیست اما دلار ۲۰۰میشه همه استوری میزارن
🔴
پ.ن: جوابتون به این
کصکش
چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143541" target="_blank">📅 16:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsMQcDW0NpXkry3GQCvzIuAzAI3ZiXLiHPejNgT71FrNYQ-HLvleZK0OQVI1dajbz8f3m_fDBdflhBwcOnko3VnXFsEpmBbIy6KAW32tYTXl_TjrVYiAynUVDs00sVeF9O0aUZeOB1QIp5GabLbJbmsN2fqhI07P2UFHRoh3-8ifGeWBg0GEZLKgnxVsTLjSy5c9Wanh5OtWcv0X6gOilkaVPxVO5Gqsa3ZC3PQBwA_8s_3ZeM7DZCX1NICe_G-Edsbr1kJgnJUocTlX34ZvoCTg_VaudtnBGMlRJ4VgFBSMyPZ64q0AX_dGGJNsNBxaKnjYPzveC0_NQxRLtZiigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مقصر گرونیا همتی هست
🔴
پ.ن: کصخول فرض کردی ملتو؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143540" target="_blank">📅 16:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpK2aTtxLQpGWZ9TsDgswxB9BfaC9hHqHQ2XV0ujVWAhkEfjyx85YgHecML-ANi854ENeubuUYHVAe_2VeArV28K2CvTxhnAdi1HULRhWddbRvJ4SSkuZFFV45xPYVKPE5gV8Hz-uSOWxlK1Ly7J0wuobSiPIH8V01HryPPG0rQW54Vj8xovMT6kF8-6eRRfL5iFrmIEOCv2OvMI0P1Y0iDaz-2UwzYiaAqvmsbxbiYYQIGx08eNk8zG94ZueNz7fqDnVSOnvhhhLYyEpr2nGAn12ZmG5J_1iT3WXWlcypdU7ggschvE-Ty9LQm9qyYIYg4_LLnSvZciJf_yMxjGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ممد سامتینگ(قالیباف) گفت ما گشنه‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143539" target="_blank">📅 16:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRBeHGygpBUZh3Qrw0iUXLIoLqYSehsPwmiEvLuPClijFfTIT6a_RdaVMlXft2UcCKHwgqkwuq2G4zLrjwJJfOirGX-9udIZbU-6LF4_YqEF5ENdxC8g6ek5QPfcqXtSpXNQa__-QmANDHR-lNcGIqY5ayCuEPVwc2W_7h4SFl7CsEgiK3GvnVIEIZAVM_edWBH0wn2YZFwWZmOaF7GfQwjASTeZMIUDflsAJE1cy307RhitkXiSPuRDJ_6Lw7qkZVjLxD-q9fjtoi7vBlml1yzxiELc1A4JceN4nVdZDOcQfJtJUMz-gYJJfkvdgLUz34d1f9_ub64Y8c6uWamQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
ایران به طور کامل در حال فروپاشی است!!!‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143538" target="_blank">📅 16:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=kCfyDikUCt_pc9B5ZUC9CoKluvnoNFgDh5BQw_NWPVTC6lQRgSMbZkq4dkUORih8OTlswwN9EWk64KMYK-Mcb0K61tPVhL1q_QOr37Fncx7vxxVw6yXpxuzDBp2j-hbO-1-PwsKAc2Zj152gIdtBomdgdshp4ifPrdOztEpQaIbTg8IfH_OR5OPdK_Bwdqh0-am3mmF0JDozcZJKTDLggPSE8FD7_7bQdbSFe7-7nOb1wQboyisa2JpQX8DzMdg9z3VdcHP3e0KKUZMmUC-1PI6w3SZnGGF1llS_9eS1VeAMummY-Nz5OAgT71lxIkUEzXNw6oFBuwVufXzV_roE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=kCfyDikUCt_pc9B5ZUC9CoKluvnoNFgDh5BQw_NWPVTC6lQRgSMbZkq4dkUORih8OTlswwN9EWk64KMYK-Mcb0K61tPVhL1q_QOr37Fncx7vxxVw6yXpxuzDBp2j-hbO-1-PwsKAc2Zj152gIdtBomdgdshp4ifPrdOztEpQaIbTg8IfH_OR5OPdK_Bwdqh0-am3mmF0JDozcZJKTDLggPSE8FD7_7bQdbSFe7-7nOb1wQboyisa2JpQX8DzMdg9z3VdcHP3e0KKUZMmUC-1PI6w3SZnGGF1llS_9eS1VeAMummY-Nz5OAgT71lxIkUEzXNw6oFBuwVufXzV_roE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 22,900,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143537" target="_blank">📅 16:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=X0K1GxoETofhCh7RcRRBM_gDPh3A58AwiiN-rX5lb5HdGZwVn-XjVlYfTirr3a_4RqXVJS22hX4ZVtKqz7-_Lj1DPUtKCvuiqFHzVURVuwfDC4zFDdkF29BaGdfktYZ-RD8pThs1yHdlRS4QhVaIWeRMLEhEOB5W9982y_KuR3NJLtpzLdk1mSUlv10Hstyor29JQbLNPihRnta8lfSnRC2P5zPEUbjpDJdO3MRT0xzMUD26bTSviYqd3lNfQDNK7bh9heL8uQG4DhvmaGshh4hu53Tz-YyF5kbKQXFLgcWK8PepjuXl2DVqXvyf7S5nLaYuEsVhx94prJ7HACGXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=X0K1GxoETofhCh7RcRRBM_gDPh3A58AwiiN-rX5lb5HdGZwVn-XjVlYfTirr3a_4RqXVJS22hX4ZVtKqz7-_Lj1DPUtKCvuiqFHzVURVuwfDC4zFDdkF29BaGdfktYZ-RD8pThs1yHdlRS4QhVaIWeRMLEhEOB5W9982y_KuR3NJLtpzLdk1mSUlv10Hstyor29JQbLNPihRnta8lfSnRC2P5zPEUbjpDJdO3MRT0xzMUD26bTSviYqd3lNfQDNK7bh9heL8uQG4DhvmaGshh4hu53Tz-YyF5kbKQXFLgcWK8PepjuXl2DVqXvyf7S5nLaYuEsVhx94prJ7HACGXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی بالاشهر تهران، یه رستوران ساختن مخصوص شوگر مامیا.
خانمای میانسال جا افتاده و پولدار اینجا جمع میشن و پسرای جوون و خوشتیپ هم میرن اینجا، تا برا خودشون شوگرمامی پیدا کنن.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143536" target="_blank">📅 16:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔥
🔥
⭕️
یک هفته پیش دلار 200  تومن رو پیشبینی کردیم و کسی باور نکرد!
و دلار امروز به 200 تومن رسید
.
ریزش مجدد تا 155 تومن را اطلاع دادیم باز توجه نکردید.
دیر نشـده هنوز،  بیا اینجا
👇
پیشبینی های ماه آینده رو اینجا میزارم.
👇
👇
👇
مجدد نوسانات چشمگیری از دلار داریم
😳
https://t.me/+eonSdwsppnIxMGE0
https://t.me/+eonSdwsppnIxMGE0
کاملا محرمانه(ارز
ودلار )همگی سریع واردشید
⭕️</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143535" target="_blank">📅 16:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIotExb1QuvWZ3RuJG6JhVOFfQWXNCN5kBI3fZezm6LcoGsEO5BUguTr7TYwOsbtxTrT7f61IRnIOD4YveFUhfOxzCI3rc4xEvIxQUBpzYOsphiJeRN8RswMRQgO48qdd3HbqFFA5qM8qByF32wvbj1L8HcdwXzy4zPfoO6Zy6YUYo6vlSdV4IWBLxf0w9H8uZAjyJ9DSbQUwfXieE-kXpet0e-fBq_wyba4Tr2Itit1ziVW0zDm2m1FkWU35X7PYwoXig5SGFnHrSZ0-JQndewgJ6un_B3HadKiwwvLpmb5j4NyMoMGq6LrOca_RubgU0jKeevL5BiB_H60xWzOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند نفتکش با مالکیت نامشخص در غرب بندر ینبع در فاصله بیش از ۱۰۰۰ کیلو متری از یمن هدف اصابت پرتابه انصار الله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143534" target="_blank">📅 15:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اختلال شدید GPS در تهران؛ مسیریاب‌ها دچار مشکل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143533" target="_blank">📅 15:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143531">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رانش زمین در محل دفن زباله در کوناکری، پایتخت گینه، باعث کشته شدن 31 نفر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143531" target="_blank">📅 15:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd5kFnI7JOQZJlQI3ifyYeNeuCaEadqfap_6pEsLfiSTK2Ts4QwT0eLhlZqgaNSceOXRFVTdbU4qGn3Hv-HFz46AUn53C-8tY9MO6pB6ObEHn9Z76mByX1rbhmhAGpLGe7hrD0BdeMU1lMFYr1Je36z7fbkyHcDnbcNUL2aOl38F2angFK_FP4AyIhRLMiB5Y3qwxXoPNy27LRqtX0EeFCs0EHHNrTa5TexxHvl3cGQXzk3h7awu6_Pb0MDwbjsjwzS2C4Yj1hiiBRbSx2Mb3eoc79nv8uoAcLkZ4ZJkIesiQ9ng_73m61_AGHkDjnZMaZ3xX_H1tfw64sVSDEvB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آصف شیبانی، وزیر خارجه سوریه:
دفاع از حقوق مردم ما و ادامه کار برای بازپس‌گیری کامل و بدون کاستی آن‌ها در تمامی عرصه‌ها، وظیفه‌ای مقدس است که با اولین فریاد آزادی آغاز شد و بازتاب آن هنوز محو نشده است و تا آنچه شایسته مردم سوریه و جایگاه تمدنی و تاریخی آن‌هاست، ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143530" target="_blank">📅 15:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiM1rWpyPMdzyDYkFLiFqGbhjl1q3PiaIkH0NMP5Y5fDcgdZfsGNfKRKD0iGQNlqovkBv0tm7Z9kFH7KFQ7fGYBuz_UwL-Dd3nArpETG-dn44Wa9BVi5dpb7FvLZTJP1O2zvHDig9YegTFF29QtXY3IykrmqH7JWRsb7OjRHdBoKzhKM7eKxvkCBRq7c_SURCMX-kcgvArT8EMj-eL5eq-DjXpUgQNRvYP_Y1es7A3nHOjkhY-djjP1tNm60e3tFnjUV_zFxRYkK6wukUT4V8XUn93PMlKbLOh7ZBZpzYr9uyPzhCUd95aLWNmRTcYCFw6D5hMCwHQj7nNOkOJht5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده های اسرائیل لحظاتی پیش دو حمله هوایی به المنصوری در جنوب لبنان انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143529" target="_blank">📅 15:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مرضیه دستجردی دبیر ستاد ملی جمعیت: حدود ۱۳ تا ۱۴ میلیون زن و مرد مجرد در سن باروری در کشور داریم که نیاز به حمایت جدی برای ازدواج دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143528" target="_blank">📅 15:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJo8E5NwoxohEe7Opx9QfBFdndTy0pYCzxYKThIdYzs8az4DzxlQkjOndxrTB7eSk4vsvAR2ZL-72bJ_FL0fk9rgjMNyPFBwSWvwEntH4_MS5XKQTVcL4DaTocjaXssE1rvrnQjthneReXIlfJhwp2U_e-VoDe3kCqxAznvSJ-KuafOZfkF_WILNgFrHyd7lk3-Ee4ktxjiLTsl-8qZiHvJDqUeOOdPpwZQbNZ-52HqCNnryK7lNA7S6VDUTS3sZTxYniknoJdw0y19BTaIs-BRn8c4DJSikwnnWgELmW20PuES73kDY4DljiiNcAO-0pB2jXo0ALg0tnzo6_v5h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطع برق کمیسیون انرژی مجلس هنگام بررسی علل خاموشی‌های اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143527" target="_blank">📅 15:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143526">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ارتش اسرائیل از ترور دو تن از نیروهای جنبش حماس در منطقه دیر البلح در مرکز نوار غزه خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143526" target="_blank">📅 15:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143525">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZIF-dEGMNuT3sW2tjL5guhB-7--4HuNHNlEE2bzbkGtS1F-PcxC0l3SvBFFAoApRwIr1sgGfCttZC6MlQM3EUhkeLZLCGQO5dkfOEMhLFqsOs4Nx7OfOkQNFAc7cxEO8Kt9JLkWhIV48F7yBc-bjRKe8jeBFq6xtbQMjxVW6HePS4lrGWimkeOFxTmwe6mcAcmdw1oAQ2iAIpHD92Nis1B8HRUSr49kVoNXpuFleogtfHPXBEaoQr9uxgquCf8yYgGd-V8Yq865JEXemKYtmU_cYZpNJMUwpGY3m82JVFMkiMKMFxa10naqksr5-HKXxmh_VFqTrmNsdtfoAtExrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکا را دوباره گرسنه کنید!
🔴
نمی‌توانید شکست‌ها را با ادعاهای دروغین پنهان کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143525" target="_blank">📅 15:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143524">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
همتی: قیمت دلار در روزهای آینده کاهش خواهد یافت
🔴
تهدید تحریم ۱۰۰ درصدی ایران رجزخوانی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143524" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مدیر اکتشاف شرکت ملی نفت : میدان گازی تازه‌کشف‌شده به‌تنهایی می‌تواند تا ۱۵ سال گاز کشور را تامین کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143523" target="_blank">📅 14:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143522">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دیده بان ایران: زنی که می‌ گوید همسرش دیپلمات ارشد وزارت خارجه بوده و در یکی از کشورهای اروپایی مستقر است، در حالی که او را ممنوع الخروج کرده، نه راه تمدید پاسپورت را باز می کند نه راه طلاق را به او می‌دهد
‏
🔴
این زن تهدید کرده در صورت ادامه این وضعیت، نام این دیپلمات را فاش می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143522" target="_blank">📅 14:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143521">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=ZaQziG0d37I-lWR_dtlf2zC4h4Cy2wXBiQEwFbXoKQk19bY1_NE6yerVgymdQRzvEpAMu8IJk0P6rMIYmzNZu5S96hdGj95a0wSGUqjcifyFj3gVTP3Tss-09_R_rKIMr8fNRPJivsVfiXKwlolwYIohUTHsxHFkVLl6lSv0hlmqyeMDp0D3WDBsfHz-T3X1DUKLDhKfJDwxAxQ8WzeezOccrnqk0kfs7nqSqcdWX19lP-E0d0VceUfBpWjLg3uJor9M_Bu2WskPWLgm_NE3cdfitmK_u8MxpjStp05WCu--drI920qhwxLa6d3GHmlbzJnq6rrWlbAhlkT85t5-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=ZaQziG0d37I-lWR_dtlf2zC4h4Cy2wXBiQEwFbXoKQk19bY1_NE6yerVgymdQRzvEpAMu8IJk0P6rMIYmzNZu5S96hdGj95a0wSGUqjcifyFj3gVTP3Tss-09_R_rKIMr8fNRPJivsVfiXKwlolwYIohUTHsxHFkVLl6lSv0hlmqyeMDp0D3WDBsfHz-T3X1DUKLDhKfJDwxAxQ8WzeezOccrnqk0kfs7nqSqcdWX19lP-E0d0VceUfBpWjLg3uJor9M_Bu2WskPWLgm_NE3cdfitmK_u8MxpjStp05WCu--drI920qhwxLa6d3GHmlbzJnq6rrWlbAhlkT85t5-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: وظیفۀ ما خدمت به مردم با هر گرایشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/143521" target="_blank">📅 14:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb7af662b.mp4?token=L8d473MvzfRK5xRdDcg7QvWljOAvOe-evTN_Q2GwhCG0MaFrEG-iO6j6ATNwDGANFauTXMVVzfuJwlKQpa94P_tSyZXpl_e0aK728s-HZ-bZCzlUEf_IZD3EHFfs0m_4TSD6jomvpdDnCBSK72paGXAXZ4VLm9wLo43PiXzoukGm9fmysrR2QNcoRjxDadGETn_Ry2Q69jQGoiDvRctk8hSpzapTVAv_ouZ0SAGWjr1y_vDiJmyZRtlsMVbfwJQzLiZIApWonbLjDx9lGOWcPtQmHwIAHBnL_TBLY0h9uuHO38WsC6gKg0VLkHcQz2AYKI0LlJ6wKd67SbZq3h7YNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb7af662b.mp4?token=L8d473MvzfRK5xRdDcg7QvWljOAvOe-evTN_Q2GwhCG0MaFrEG-iO6j6ATNwDGANFauTXMVVzfuJwlKQpa94P_tSyZXpl_e0aK728s-HZ-bZCzlUEf_IZD3EHFfs0m_4TSD6jomvpdDnCBSK72paGXAXZ4VLm9wLo43PiXzoukGm9fmysrR2QNcoRjxDadGETn_Ry2Q69jQGoiDvRctk8hSpzapTVAv_ouZ0SAGWjr1y_vDiJmyZRtlsMVbfwJQzLiZIApWonbLjDx9lGOWcPtQmHwIAHBnL_TBLY0h9uuHO38WsC6gKg0VLkHcQz2AYKI0LlJ6wKd67SbZq3h7YNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوباره حمله روسیه به فروشگاه ها در اودسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143519" target="_blank">📅 14:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
👈
زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/143518" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH1VLpA40sQhfBUVmvJgrBoqOVpsUsEsXuatCd8PnR_Ah7tGnPPWQeE6V7mRR0dIFxoCyfPKKTdopugvrfwce4zGKtiuFFM2EnysYIRWQDhgKo6iKLT-4ZXQEsTg9A1j8giVxjKU__3yjHXUtgRFYY7rueqbnVOPj8D3tsp7-TOE11F30a1ZIHeFnJbb6O6Uf6Zqq2nHDkmY4t9JkFcJG6bFNxGFwliZ76QB-HehMQ90LPATpqHSVFTcEEL_efmEpCgeP3_UZlSI8wSy-U3WorXs7A8NX6ZWuwTlfYBV3lYf3H2A5uURTD4Gf3J0DtK7Iif9_19NdGHH--cv-mZD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر قطعه قبر به ۱ میلیارد تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/143517" target="_blank">📅 14:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
👈
اژه‌ای: درباره اصلاح قیمت بنزین اختلاف‌نظر وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143516" target="_blank">📅 14:05 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
