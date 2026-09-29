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
<img src="https://cdn4.telesco.pe/file/GbhyCUEIl50r62c_J1EKXN5Lbn0Kr3vE30Cn49nhrFtUDzDEzNTYaF7pVMiK8ApWhfoNGH5gfWWezkl69rkU9ZRrckNybN3feLsr_olTe46_d4fPFXdWftbWkho0qAVdYlKhS619eQdCMf16cKJdYgzK2Avd_r5_eOI07XsLWb3MZPbFUq8CVMKM6yxFxni0PHATt3kYJ53zwzGziz4jGxptFqex1OsuFTXLM17GqMCzqp7Z15pV-cc0yiODT8YS6xEEQx2qlJvn_ELazl7K56hEue2GVuOkbt2s_iTVTpvmSvnFZgXJKp9x3id6idQ6G35Ioc4dMUF6ggkgJoReLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i29PHiaKQRcPFXyQWVKKhZCSGWPr-wYLxnub18yLWF7wEVaRQ0jK_uTfD7rvMI0kn428BOoJ3ZJ_7s2mNft5WfbP-OJwFc8u2aTI4eALvxOQCaYHKq5YJZ0wbbKmuMsyx1U00UzSr-a9ewegY8h5bIpcSbwRmr0Ssvw2wisHATZKgcQxs5Q45pBIHfNXtTYxiSI2LpAAXXb-K5nTOSzRio00xPgoWMlddOmQyL-fRs31UEqYtPnL-IibAFIDuuQaUj3CO1YGpjcfXcf-wL8VnHfpc1PorvBcUUj9Sjjh7JxxYZVlRI1Z_s_5h3V42hw4e5QqScoRCI1OVjKb6YHwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایشش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
هسته پنل رو یه دور ریستارت کنید تا تست پینگ وارپ سبز بشه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 501 · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tj92ucQpxx3QC1S0BKQkNNqtdDJe9-3OgG1oRgtaJLZzGLjtpZn9Wu9O5QLaFuvvB73lW7b7bMV4X8fnF40-Jw89irR42bjXlEY7-760ZAEOkaS7Y7vKM_B0KY-Yt96ovCWHanh0u00P87cpgDPuJ4YOMvjOThoFxI0OjpO2UeKp7HYXRiE3sHfEltcNoNv0rbz7PeCJwKj5ZKMcUijem-5yZEliL-4aqGoiulQ1AXWqvb5-XESXbOqxnIbhnusoqMnBjASXG1l9LzZTDsvw6-I57CbohC-oMtja-7t0g2Dr2Se_uK1x7dV6lHgr0-L0e-ZSo27VFY8G5n64HDV2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hX38EOIkBiy3HEazpWc8MNWcegGlEv7ug9H_HtVbrNK1ujIcRS3t7Z0jkfGS9OVzQPA8vBq9OiKMB7d-0p4BSJayHJGq78LTB_RhdQvBy15FlKwSmV96-QeAJv98SncBiBcZHhMvHDcu06cL_FcCKo8erSDU_oZY7g8aclqwAUX7vrWpZVLNVt3NxoTTWIxuL4QzTFegVYWcTPgV_r9kzSGWNxjbWpIqKjKpzYIbDaKd4LInq9G8785cDsfehvI9Z-mzzFa3wx4GvMpc_cqhTY0yUIndwR7TJBUgTOEzaHgL351i6HSdXM-_RvgBXrllZwk08utWiqZrNqwIjOlPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fl7W0iyGXtUdfaZPFYRdvq9PdsOKaJPsda0GRuIIcOnZbiti0VlRYC7PVo80sLF0j0_Fzq2dkb4bCvqowTv4F5AyfohnxOaBbXy_xAvQop5heXP_GNvo7GoV8kMTguKDSXUEYiwdg5g9ec7LjcmeLvF0xQMrpeng2NUHXjSQ4F9r1lQlMcK_xAyC2puMcoQVcw4I1go0tO2AZUdlwrTpZTeFoSv25wZpeVi14Z8wExanaGXXy_-mexBcU4KDn5D72L_iiUHjxJT2gmSvAcw4n5IG5O4CbO7se89kE9ApxqMZseVXFjq5E1k5Ssuo-tsaOxVoPHUM6ZLAFV-0RktL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jP9w8obLMPQenuPCxlunaXT17bruupU-wL1TEzqLkaxNdmQfwfFJBhhfBG5KH_VhLzhlvCn5nBF-a5oewOUmO8qkFkuMdnRXv3e5nHrYQYtpCnVDl6lAxVz9d6c_yqh9sfFixqsFKQYksATVJLcRZ-ECX_BkVoJznOAABKwyzuWR6IwnbgaUIU6Dsm9Q3-OjML8mNK0oFwhKJ-uY7kgIP4gns-pVicGvbqx8SIz7nGfz9VwgQpoXByWzO_bmA0-RFGdqpiBpRD9F2H0_Hp9SGvPIpIQNSAteAcrUOdGuhJi6-nIg4WU060A3DsXefmc-EL5syZAs-jxO23fDEIGmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1CsBwos-3gs-G5NmrQF43uaK3GebjZDkwQIthotayHhmv84m0IpkdAax-uzy9uZRTjTg_91QFuXuyEISevIpSw9BAEg2zTGAtbjgRBbGofoJEAhP7P-880lKabs_Q5-jYb1MT9VRKTawtzpYDjy5LbQdHLNQndDzWbdgh5HU1uBv9GpDhABRKDlMxGxp9NibPQqF15rX8B_EfN4Xq8H4gmerCbGcEQuYCfJAD76Ha3WLg49LJ9bYj91aNVmJ-S4wcVtBatWDAFXjpzGhF4XLViRviyvk2VR_Ic-cdp8d8ZUqjmFrAhGD-65L7b2ZwLDq_EjmyuAsfxGx9HcjF47vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3PL_cZzahhvsTi-2pisvJzRCFkSrHfrV94OD83-M9lZCjj-1K0mk0CTZFHcvuz0g2ucZ4MzrP_-Op-jn2bf0-acuusxuAXSTNdDoNxYdMep9l8JyIg2_e-viC28pDckb4_181ziWza5uUpDD9Z4okg18bPsMZCD15YWC5RLHTx_TieB3NYKDW8V8r-MPRF2oZssnD89EkYIY_WHlhzpVIiB9aLJ4jjy-Y07tTB5T36G22W2xMhRukD9T_mnvnac9tKMM1xMdH_sdJGng3sKuceRU_JMyJ-zTihfWZOysOaZT1e3ozTflkEvwCCSOJV6-oR0464tJo0z4jZ3CeTDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEheQYzx11i3RaNSTMu_5OpxCaLtO9Dmp3D-RkPuuxHFjgg4JWVfcSW6jk0zbS5HduX2Vqep-xFpV8WKGcfV0hs3LocgK2S4eArZkQERNk3vW8zaBht1xb8DuG5EZL_5uSxMR2Q3A4PtilJrdIcnGY-28G1cKRDOSFuCRsfA428MoqZVeFgnoTrr8DGlNmkW-4DIm7nEJXpjVYAQq5xd_woWUjnUDFTFVNVE9DUrWSu5IF9qLKSmy6xg6sYLglsGtT0xvbM_aeQhuU1P-AfqvkvpCEtfy1xjaLCheW8RRc6o6ku5qtqsVfP_rBq2Xgc8qKUaSgJ5R6sDUSjd8GEYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNWb1SUnY_NjqQxXn2PeM6jNgung-71oWjOLSZ_gc-qcKS6Pns3SWAvFlu83cBsTpGOerceCNKNgD3taAKojLAVdQ1OaPC7tMo_KBRpGce3Raxsf_upGuXniy_jCyUMwXFjXwRCKQiGX3hVnp39ja-hlh1KHszMpmX32u_D3y90ZrSeRoo9LbA96B9CB2dwb-4kmlX2zQyOT8mww067Fc1wFpy_1_dhWU8KCcP5GJJlMDtSJ7_xujX7orEeMXB3wgAUBNIujvtMmQ9V9_RZ49dUMeX-ARF6kuS1a6fxgi33KGzsZIPXcHj6irVHy9PTk4xyeUCxbhOZSc7BywIxcQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUQCeWqVuQzkxrrisGE6TIZhP-BDimJ8HMsbKqcSoPYNMhLqvDEsbfVCtrn5QkNfSXHqI1dqiDpf0otjETh-BYGEhDCdtVvlxrO230ttIOksqP2wcDAyd8kUjjVaAW9gYP_DEnBMPolrAuwVlkEaoy8iaywpDL_WqHstn0Gwg_tymorQUl9d4ANGbgo1OelhVM7p3Q7R-MZ8AeyUw4vSN_gQZItKk9oPfSRiX_sXdeelYUZAKlxAQ72_YpJ8NkUbLpB2AzfbpXEEE_Vhx4XEkPEKtvPy9X20Ko5IICjwkXTE2f9Cj-QP6Q8E0LqbDoZFx_Oygpg33iyXr8F_QMOIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F11WH2XRtPdQM2XguGlmFJKtJ99ktogRT_XJ7DkgQEP0IB7cBThewrvwdiI2EHmYSfNX8uQTAFvHhp9uJ40euPnvJEicOjcrwBZrbB1vXt5HP-6DuUGkvbzuO_joly9Sg--_VitijFsZwMz8KFIJ8ujxrFww06ktHeAe3BqF32xSvJSDdukJrV6hbxp5EOOFtoKJrtSSgN59vR_XgSZPxtb3wEZoBwy40wADRmqc7jym-lRPXJKPa7PGfNjQpvUCeBljDwmDjIqaJGuStG-pZIkExqTZOmjhkkT2j1lmDEYqeVpPEcxsUJUjkIwW2ILgs_2TNi0tx7tHzg_X2DB03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMyU5AeYGgVKuhNQ9nHQbx8kKpxosjioPJCGMU9NH6p-13OiyMMJe4OJw9mYEwbn0Ko5nfCMLTTQCKRNftibcw13wSRWUILwmEq-kUkTYY1Uqk_H8ILStT2FhiBegRtu6yc2ww0b7XAfsdcxdP8FloHGju41k8pFy15q8HoOptxOIcq4P4weACagVaMjEqOBzIWIFOz8l_ElqResQBv8wBhzWrh_NdLbwCN05xNaJ7IOTi7Ah5DOieP04cFGhtIjtzJNhnvEs3qu2Idp9pQAWfelJ1nEngLxYtzjX4dmKVuMQtqyK5oj5X0AiuBhGJZVpDCxyNvYMxkbTa8x_iDWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu0xJq_fYs0AfrjenwGW4sW_FfIM_PxNJY8kAS2Y_c97Wa7b4UWU_jbxCPaPsAuUCdw4pqnxCaS3Ep4gyJKxx1JJJOKN8dxpa0PXBb0xxrIfH3-tMWa6ThJZt4QdmldHHd_HppVr7YPO6IyRgzlrNfZwSdL4AnDo3lvLG8TjPAEZH-F_e-q-yLZ39mzexV0dGVvHyvFQ_bz6ct6SE5l4emKI-koGUt9pmTc53O8pBB8rND-5IMkTtllMpkXKM1daEbH8XQvrwy5vfmqYpA0WSSseFmzw6h2DBnoCUXACn8a3ofGbEC3O1jKrDNvFk8u-hbwvdhjMxDxrfQlPYlUiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRHE0lu_Y5vkejTwWm0Six7cCGZzhJImTnQ-CCSKNUaOp6FPQ12ubIZfPdT7IiBatTvXSvp0QSKbPCWV9kSqd_B1if5hdlpuvhbM3Mkuu7GjreDWyHd1XsuizfML4UD1sjBILfFH0cKkN9xFumgfCdaeRg1IvixB90wqZqjy2nzymrgIsY7U7fkgHpm-7Iizc1tx5JMcMUYTDgpfEKLX5QPtrXnsUdLKr6mQjYNEyEZEOGUIvSSn3QPBp7Rj9EEelHlQYqhFTbA0UjDnNjdiEDV4gEyOUjHXDGUeYUhr320E2ysCba7f7Xj7AYGmUNaQA_2DNz3zhkhTExX0KqW0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO7J2MLRsZ9FCudqevoUTOtk7FKSfvfWHDW0OvMbJToIo_xfcUq6W6k3xDcp8_Oo644F59h2kT6kcac58esOK0NlNaIf7qJJeJqSA0JGOegi56yzJHF8gXqCx1V_PIcs7IGQ_IYyEbwb-iKx9se_HrfUqQQosADvenyj87_LTCx7kkdoFDEe_PZ6SSCVpsnaUXiPli6EMQcYk4htBfkSauPZ1G79ieexr3MhZl8fV9haCJMKlBndqiK95lhKxnwZy-MDZM5lkyXmSfacurAtzJ9PSv0pEeaPEzZ5qEvXqZ8wvepbPo1xydYuSvcd4W7fA064qWeHvf89WHHyoLWltQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn8yikBMy6frNGJ4PiiV8kdj-A60NUWCLgxJIv7nyeYWGOE6BppeN3DKVJhSFwpPxcvNiCeEfqvSFZxnYDD2gNIwAHXGtX_0e9NYtYsnn5N0-gPAEikoWMXD6_a4I-WCvUUh1DwTbJX4KkJdjZMhHm3BodrWjzUqErgrJs0frlbEbMbmIPZLPYPmZgGhx0TlXJWmnEM4hNcC2Za2fDyXTF_7S6R1rLG9hlzJngP9ZCI8HsBFjQG1rM5zyB3vTJPJnPhEjtCvxV2YJLFyg4w1ZAt_Fdaz-rqkLEAQGCfVb5qLe_cVA250nY6pEU5al1JFplIkwIOgc_8MavAXNHfR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKkjtALhz4cNw0KLcSf5wVjvLrCMf-_4WWTiianZL1JNUMvOzrc6TI-vEIgpMJLyoF2np-Koe66MLqQ4gWJSKD8ib6zGLipJd8EFRYNX3zOEe7qcXB6C8CeiVg58mqo3k4kJEZpIMmiuT-C82tlijtbEfcmybG2soVFhdh85dEDh8ltzVBU-4hjSRZEBpdJTRx8XLnFqmhe7st7Ksj9uOOuxFWhia19MxfJUUTAdIrS04qiL1CQNJwnEFD2VTOeuJK1Mc-JQDVD-WjikmhlMeP08t8yV6lA4kZs5Kd9mS_o8US_FiEgqbizdLiLORTVMGT2niKVNtxp7cRi1cURYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZLvOz1C0VgEuxJV9SPtjqsGh3rawY6wS-GU1M3jPesur_qopvXzXlwiS0M1gEOQN0R1qG7xF6AKGOHYDZR5-5jTvE0-VtiEKNZSKZs29vqM1H4DPGWGTwanyahVoPJUiGzLK80P5RXiTIkvEX_MlcZdEkzEJMhl6nz-s5QGriqaJqShn06_tD0RUoRiyPKDI2SRCQHTLzuW1i22sYHMU9hGeMNBzh-mphWnHjR_mj0lbyUSmHy_R2P3sbw6nCYdzDqU46bwa4-d7W9_vJW11QGVsCN91bddwn99FfeGtSbmIT1m3al2_dt2H8QwzOUcL1caKa35GbMPqlOjks_hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pma6c4OM071HFnMvRffPumAf22sZMI6TYBKEidgO5pnCSa1Gqnw8KRFN9xF2zPSB2D6EfHex2jaoEKkLqT8QWYRQW-K0Tmj9znBiXrkJyrQjL_ZpvIHsTOLct9dTZbg6-0mMV2KWhXSu-qWsrTiu6aJv3QypHlEeIIXNFWDgx4L8_Vd3ugXoFKOMbgSP97hsUfWeJCA6woGzKEYuZmutr6Z0jut6ShyIT0FMtvJ7IbE00zxgEYPEYBfIywpJE2QMPaubS3PvJD_c2PogUrzmwufhG7qWi9Y7SUMM586EzJkc3YHW1XWi75QmbfKeQ4uxpKOTh64P9paoD8HH0FDw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtD_7DIkoNay8pjvmO51XF8CSDllIkG_O1F1399O1z8Pw3SLGa64zpfrhgpOi2oDTIMNT6QgFxu2aqdbUUO53Zliq8EshgSk8-e2SlVu7hTj0V0-Lcuxjy9QGa9ZtSVRf7Ui-KhXnWXY1ucqlD8X1HVdV2ASw9cHRNGpPDv3dbBbdeVS5Y1uYwjUZ0xb8gg9BKlBpp98Bmm4pbLQEelkog59EwH2iDlLjJWBs6_pTP6EWCL_Ck4eAWhDXtZmQ4E_1vsvs9Z7TGfy4yDkz6BEpBrnW62YYWv2l2RU2-3ErDCL_zwfXzCQ_guyukY7KjhqiWN79eOVPtESQYyr6G5GDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtf4d8Ptp66iZGjNT4o9H-sD0vlQZA0oVxA2raRYmbDvUwWMfnk2c1OzVBeUGwOYnVkvtbVjA5Gsmy7kjgcTr8H4_84HubtKcWcqjdRBxi63PJlE5Eh43qOe5B8gNSGK_a1Z5CFgzyo8t8Evk0MhV5EIBQKhGvQQ5S9J6zHCEHAE2k9XWYYqHTtz0LZ3PLJwkBkXswvP4MkYROeYCSAf1qbLDu70PrrOKWggplcy39iQqa-CEZDiygM8zfEU0WA5Jy4JNoz0ccZUZB5L9la4tKbopworAipAkN2o4eS5nXk1FeDyybso6CdvZhiCFwnHNia6AOWHLUsszIhJuCuqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=fz_1n9LtqFArdv9mFrGaE1RZS2F3JSjwUNjYw-40FrcTnsgGGpnM5AkmCInfTzUKQbFMXhOWq7yLmytuH18jSLo-kg4W_JAh5UO3o5fZlV9K7LEn86eoa8MHj4Y_5LMkP6S6LcMFWZ8eh76R7snekMo0dOu5c93jr-kXG0PIRvQMBgqY1IFXk4RagB6jR8rgsWDDZnaTx0lGePKlauvFZUbufsRHMb7zIl3uS_6KRF99O5cAtO7MatloaQQ6yJhrHwg1rg8zVQ09SgJks2nKshr78eN9OGXiLj48lkJ1FOgJg3oJxoa3C4UdZtIFmVJcOfZYc4Nxno55cbL41bUABQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=fz_1n9LtqFArdv9mFrGaE1RZS2F3JSjwUNjYw-40FrcTnsgGGpnM5AkmCInfTzUKQbFMXhOWq7yLmytuH18jSLo-kg4W_JAh5UO3o5fZlV9K7LEn86eoa8MHj4Y_5LMkP6S6LcMFWZ8eh76R7snekMo0dOu5c93jr-kXG0PIRvQMBgqY1IFXk4RagB6jR8rgsWDDZnaTx0lGePKlauvFZUbufsRHMb7zIl3uS_6KRF99O5cAtO7MatloaQQ6yJhrHwg1rg8zVQ09SgJks2nKshr78eN9OGXiLj48lkJ1FOgJg3oJxoa3C4UdZtIFmVJcOfZYc4Nxno55cbL41bUABQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtygGHMKZFt-0vHUyog0MXkIgmnNJlfRdQiZsTzOlr4tglR2Uj7kTdTesgnTzW395nXmmkeb6tVXQVeexh9v2s_K-Q-mzd8qA8EFXAwFbD6Ur74ej_m7VpBX0wBy9cEDu68D5XqlSE3Gab7vUSQZKyOUO14b5uAgV7S5fFnWFMQ_wvL6KpPXQ1yLU7LboHSZexcxXl00C_U9vLPWfecEUCpAgKDIvaxnxRDnAuvWEr6tcfJkcFgHp3y1TXqY4njFvp1p4LegJP0s_9Stx5EOmdHPlYPo7uz-WLSQMkJvC_fTLhDPMq5_4xgIcZnqQLoG7ztlC3gnzlad2KB4NF7mfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9EhAsFXyhppo6XXpEHTIx5Hvelsfi1KhESWD15a2rE7X6tI-oBVeJCQsP7ElKPrZxG0B8Aj4X4LP0NMcWwm8ntGEoOXzvh3kXnqW8UY-0faUJCtP2kziVgK6Ngt5pq4o5BQJjE4HpKyv-nV19UM1f6yb6XmqlwYOE_K0dhzrwr-B7l4-DDK4OZTAVv1DH6B0UUHGVPGTAtJltr3wbXAuQYWSRcr11OIoYwkBd0GcS5Nn5DrGQ-ZKfRU5Zh-b0pcQmG7rbqSZEGq8ETq2VYC2Uyi0-qSckqnUbIzGlMpwieg6NUiTpgRAZIb98PRyoqYMbgqKEaZiMAvMZCKJe8pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs5WDWZ7QBRmRYkXQv7SDJG_QxUZypdqlNcoipvIYmVGMPQbr3Vv3Itf0YiFZB20Mc7tjbfwJscw_ebHTHrFiKr7zrRdw0iiH51RzO6E6XC4wfw5xh2KkuRckH5I8OsrmawcgiWwxLO-YaLWMRnrf2uKwltopy5NCsBFfpmeW52tvTKwz1US1mpJQqMDq1rxxNKt1uSUrVf_fUx6zRkmeZCh6d1SrQiRMf2B87aolJSyfkDXdnQaVGoNBENtB5ZV-vMWZrEArBzB8Zv8bUUpgxNEguTnM5IPfjxg1Oc7cXwek77d3qTgFuvMNBt55FOHOQKOXMhi8Ddve7iCWDiLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWXsimCCt_54MEv0ebZRVYskT3csyrFON2JGLi9tUPAEEmOxj-ESZFhclKYZJN4oY1lcVYX6qj6CDVieDB7isSwyQx3zpeVnOYze-Ba38l9T_eKZmuqrHuqX0ARCFnaDosQv9DgYyYPM3Em-YPJuALe9mGsZDb2j3b5HUehztuOiCE4MX1sd5eNhZf0pDRZp3e8SCJ4hdO6Qh-Dby0a1HgwPeWmRvxgbjrW-MbxKJjrftHg9dmNOel8PtvCDYE_bYpZZSXptvANPpUX8ujdFxNydJo6TsYbSOqv59vFxexdLWYGdEZFkKMsmKzHhnG4T0nUt0RIqbja6869cX3akgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX7UjhrhQ-9wmtgEc8W9fvTRM0LpOf7iYrTdd4HAfhknJieAIzTcWdLJj-Q6o5QXW_3_ij_hk_6Xvy_RIgyxNw5ul-d6Hk7DkPTY-x4jqu7-X297_XFVj41hA0h-05DIMq1sr8WFXVhhTntqoZn0jzop6eW_yQBONCyAmi8ajDvG2SHvQA07ZkcHQiPCtEfd5Dk0zLNs3yE-jQiy1VdASeqE0S6Np5kPufR4mtHAg1C7OZ5YoGtSG9TcQUqMHOAaco5firHHm-WcKWFpdpu7kdBkUG5L3GnPwIzNGP_8PshjlYKKQjhaJFpeKudVEsx9ZhMls0D-N0taEfmw_GhaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEuL4z7awKXUNO63y3MnrMvnLoadKqc7LUvQD9r9IatN-VLoeD-iMAb95dX2cNNgdy6Gy8RDUn-GjLDjtKzLlWQIeSMpTcq6Lm-64B8JUXm-5su9OJS4y9USV9IoFq467HdQZAc8v9XGf4RON_A75ri1XRVWq6Y3KRAvUNDA8k4nXEItOIkU38QEiyZ3hQz7iuo6dfFzxwxWRSIgt24Mnd-NC5xlMAw-4voutR1AUwDx8niMSiov8z82p9k5jauk-QTE-fiOPcxPNWDerHsCn5CQNeXHk1i5DTaPXIEpGQrA9eMYgMQSQ7iR9jS4YXZ6IlfB9P_GIrDuGTDfiNAwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH9slLb5wcsh5NN9LXw8YP4WiX9tysASiCvF3r_uJA49ApQJ3z7-J1EnGMANBbAXqAEx4VWUnfXWm-ZpG9TsqsZ2dkncB9u0XlpdgG_wwa-H-LjrM0nVeXUENNqHvVOYA3vCPF9Q69n3MhxCkUtwZe4_0LW_aFOmmCwFeRKsjUAi6Tf6aHMS9KpOyswjHbzYeXqWCpJ3ruVmSnqvR1uiaUWfMwmO_E7e4NfNM6YYTOLZejAR2xlGxAifYIb4y92cQNn6jor84SP4h5eKLG4LApT9LIPjhR6PNXE1eVfjO2OtXRLvaGqHR1ydwIOJrNMjlnQWJWPiDWJQ1DDwmYk1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBpRCNeJH6yjAi5lwwf5XXnluGhjNpZroShmSDeDjTw_U-AXNL6C6i-SJki7KhftAlIEi6oPBPGLzhA2OV_G_q1mPBR7XAQWox3CYi4zlHsWAZmR1U2m2vOkxHoyE5MIkK7xHwWxLGq9hSIFjUcyYAtv14A5brKdQ6cdXdu5gWm9sMj2BLUaOKSit2S5Q1lrpkFBOc2X0n3BphRpKXNiRD3GTtOvFQ1waHZJj1UmyqLjPC5PNv9wCmmqC7ldJZTnSiZ4NPINgp8nfS4y1UayJxwV8MYNOX7ecJK9ion_e3q137dUADdZZZ2Fh5uAdQU6VeZ2f_OwI5kjf__MkWc2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI1KLLv-Vd44gH1K6U3Dc0nWS9Y4C0q33hwVkTWMU1TJR7cJAPHMtgXzNlEMR_VuVwltHp0d_0BcUh_YUC1p9cvLsqLFTjqENoTDQWycV6pQVTCvQ07-9ov3rE3p_jLa3e_O5Z4Ib0loABDfUs-aaIgHq4fGuxzgekqnTwrm-4VqU0OIfUkY8URbECNye5IrfxJnMvZke7S8HGnYVXUyynnMOdopW6MnsYEIIPWtqeP_XZRbOVjdqG8BSAtXCY2ELiytDfn0AQFcDQJhDmW5H7VAdJvxlTvPrJdWC14iDehSk-tQ4PEw6dn-npjQc3T3t2vbMzsyYlTKNjH_acwjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN_2QmtCoxjQspFhr0ODIlsuJ1hPDSs7e_qccWsu8JDVbgvaZJ9-Pq6CtmgSOKVu9B4GuKlCBWD_aWuHn8Ghsm2ZoKK_7yHeGQElS8GQGTmPdVk-k3yVZ7GkDJGwugQjkGltdcD0FlzW1qQTDUOkISdnuOmN1kdpfcl1JrNGMv9Nfr6Sh2CqQ9Oqorg2xV-E3ocKHsxm3oVDiY03_oz6G4dm-og5P2jHMX1Q13v9BX0wFQOObQwvW1TC0yrTN1zOLGPIOvTP_2_NIjiKSQRSB3eScoKBd9vuF-VkwPsfZLrnVX2fxhDlcfYZjBFEMmRVsZiGwzZFLUyjnwcnROr7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr3eAVJ8z7ZMbuVuzqYCABWHfLnrccj5lA25K7sc7I9nkVQRO12gTokgmDWLmPV5vQ3jJx9rvyghLoxapD19C63Cq0ao2stB3sQwxArpIPzrFqdBvyNUQbW5b6ziioJfHtnbtUefhgrLM8A0vnjnVAliijVix6XvVieYRGaj70f1kFl1cfiwY1lfCJsgncHD-GfYaKDpN_1GeaAO9m-aZBGTn8Hl0SB4YVgTfR2L2SBxK64tMGSwriKJkXsOzmUjvRDdZohGlTk-J9ShMLswHe6ZHgN3AiWIhOGY0gFm5UMwozZLFeqs8N6KHfvZpo21a--ycv12eWcvEDAHkj2VXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKmFNWMnlUiH5VR1bncpFn9U-FuH9Vx4is9eGqiki719PGmUGlZLE4uXMA64l0xPpikR_t2yGzQlCFWkiE_Y4dQG8lMGSbMGMhSpAOHkMuAWmUm72rh_Qfv25jQpZSTByIFtei85AwWKHja-zmhVwayGZkJ3cAvYt6kUC2UufScWu4c0ozjXIIdNLWgB8VLvh4INCRIl9WxozN8dINx9efOgUYYAklLuXQXHrcI6V3R_1V941JbisGMCDEnaP-19SF2zBx7My18cJHhlIGXYFiLPv67dG-2UEXNRXY0iQ0MDmNPfKpF39ayAwy2nP5nbowjrqox6jY7dDR_mvVH7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDXQu7KGuODVECC9jHdGV4U20CdsnXBvIoF21jkj8kjCnY7RU8u3oH6eu63vxrUXkuKfWU4Fi0eo9tf4c0KG-6Bp7uNCTfHtVOaTmXLypD5e0en3uqZ4HlMG3Xz-iDVJ3xTpdT99te2e8ttORKMaTRirUiGep7ux3QEZQ8HNHhIYGYdaQ5rx9z8gsH0zL-QuXC8bOp9BlARC4hdmu0cHVimY03U9u9c8FokJVNe-ie8mS53E30vj9usdDsiltcqOVm4IdQSugV1ZOp2wjrgtY9ZK2DsAnqnvZbuf7nETrlRfwq15xzM0PTxT0D9x8eMwxKKpuRJjxhO5AoHGikCpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSS47vcQ1UePe34h_s7Cra_wT2UpjNLg5kQKFPsPKBJ7W1pRp0NTZU06RQUP43yhSnE-zNAEh2C03WyEyJ3fSPEx5QNkNZ63kBGCg-T_IVBQ6nxH0GO_c4XsoA3W11g4awv9Gpwb9H-gsO7A0P6ZY4GKBPkAGuoe4YIY4zEiI_wQY4Z5Gj6qgv1mlwmy8jcyMDOwNp1_KXKYgh4oo6d1wQNr_hubG9CYO0izfCBPkZYiGgGP35H40oV-prlm3AWX3g2jt1dLXhuP0GsdPeipYgbRTGrSvMLW3hV5nazq_lQ3wGKRrmTSU40qiEaOcqTzshgt1qy8hYwwtm93hLQsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGLY-tqkqjGUZw1Itcaxx7NCHGoreqHV7meRbdqXSzzz-IOh596vakfXeXFEl2RvxUtRo1sfYtoildi1BlB7UwFomHa95I0ZTJwVQ4UcqFRmHbi_nb510bp6xRHFiTjgo98mM4T-Ke870IvLtbt8AU6gyPHYibs63YWXAuIUHkUyy-4osZEQa2Ij2FQz1AcdkpmpC8H1_QEQrQX6gz1NpoNG7VB3lo7_bj5CqMsSTz7j9K2GIRN4vn3UX-8L4lpshpxB0dEjET0EyOZL13zs1W5TLfpXTb8b5VzV_-ZObhxhKRtvFjYMfNtJyeCFSgyn_J2V0ILe5rp6Hnbr1PDwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZZAbwuy11ei_lLYeOgT-CwpjWrzEwFoxrMFH7ZC-AJU2_nQqjx-4Spi6KzHCLFVYsoAysGMRcJXW8Wd9ER9bh2AKfvYCCa-eq7OPnFx3u6gKyV3fhuFOthvyM5fuLlZgXBt0P7TbgBdapmUYwnb9NJp-atIsHehg2AkfTblWftztHKve1GyqusQrywdO_ADJ6_j4ihiVN6Uycfn8FFAFHpdUOAHrVs5TQaNBcEIzQYrorI_ePQHwHvkLg8UlZlNWOX8fuprK8Pz0DVctx94Y59z1hZjuxXpT0YoXNxMeWrlWSlMK6advMqllLaXdjzXhlvEQgUcEwM0Vv7z5q7T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxhNReis0Be44bpE_DGNbzsUsxoCBrsgNnRymQ9eNzIw4BP8jd1khpxFyoveBn9KyvlqLtZAalHKJtUX470M_udeUtlxyXjI7SXYfQ8ZxEcxbGMhD7PP3y17CnYekXGYhVHBZxE1-o_Sq9LEL3vMhguy0Th3Dpm0Xhvjq0_T1H2iHSyLoenjq5S_uTs9PV7POOa2uZNt7Oj0-EJz0zFUrT-fuzkWSBAgQBah2HmOalCy5L-zHcvPOLGHnrb_APBboRTJ_FkSds8I90PaBIEx0Bht1y2Iuy1E-wIHPZwHGLS9tG4XVBmLKBAmABhtJuH84kDGPjZvKw_QGiykw8thMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJBgZHDNfODG-gLoSrrXYFDHYfo2tj9C-RIyMeUIvR49Zj3DC_vnDnytnq4p396PcDhJwe_TR2YIYdFS9wvTh-Fi3lx0Hk6tkMsDIp-JiCGbJymqYNwyE6STWeM96j98FaNP65qU7PR6-46-ZkcnP7w0sRqONSjp0dx9RugGDW3mBmc2pSe86d8hHBWfwOGHUpxcH32nB13KWg0wa5od1UOY3mpyzl0L3rZQRvSFW266ffDFNxXBEs-2sqqO0F9raqwHD4gFDn0lLQwpddo7cnOynSDNslwpUsyAEovQK-IfVfEhjnD_gyaOYkMWgWUabTTRr-wKZMydoGe3jqCgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmm_2ruJCMGmQv8lcVqCsOooowKrwUT35pcVQdmsUhP_Epvf4o44NYhlFe-3BBYUJG-SeHsdOwHjKpUkDHC17mFlEUD447FTlFzc7qDsHcrqURkiW511x8SEGXJ9dUES5IiKCECe50etysUPi-imvJjuD4kkpLKhjEuHCapJUSmnEJ_XZpcuA1OraALk9lnbWZBR0BOe2wPQtWjyScFeqXkDoEfdO8ZCdwpb2Tydixyn6mbG81NAggKiNWHOwkVymfo7oV5zxxq5S5zlr8wdUqPWgNCuLBtnvBOq2ikKse8nZL9Pg4P_brtHy2m8RCReFb_0UUE_0I4-IqNFXvzFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUx3skOvImMNcowERfUIMqY-Scbk8XqLnkN21QkIEUV0ovJQSaZ902hl6nnXJPvP6b0hqSLUcGrgcy9QJabYrUN6_aImSXWM_GJeng5OMnk6U3kuZGGCv9GuX0wNt9uuS9wgrHUXkojxGHUI0cHQ2are0wxkKpaPUf7BSFQczyXUHFb6lN37QsuM1ehC5UgMdPQ5En0kN9qBL9wjoYOQWGCLVILanl1zNr5ChsDkNSjfapepX_rxWPAXuag8lMw4eT2kL2c55pcGuwV53J8_EUfvUjt64JkplcJPoJtMKCy2UvqeX0Cb_j322UxBHglIDHpALWBrkAPvGDc5Tar8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBtsPvrXKc-rQ2gyp1NMMKpk7-Ml2RnHoLv2f0GEwJ7CkoQt_2dqEGoU9A83dmxrgILUKCxg7kxpcaRNC8r_fj2EOsT8ciakqqKUXVkVojoQOd0UX9htoMqXAOQxKk00z-OXZvpQsFj4NC7HiR3_3cCDhtrfw6XxVUPARhRZfE_8BseVs9BbIwzkqYC88CaXSnxQYX4uZjYNXVKEstFSv_ozhRtKP-B2-zDRgGjR60gl2D0etHZ7Sp8tuh38oNeXJDguVVhL1GwebT4r6A61gtG_k9IokZvyEzyzkarkmDA-OwNqE4niYpqEsEyGDdRfjh8NOITOcsbIoFtNLLrh6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=m3SeVM8wOW0DqsmdRfduX3kRTFsI4RHFcu5QoapbqJuvU37l02BUlHMyR4EmIeRf1wOH8feGfaDZt1kR9UZoE843y1AQnoa9zZUZcMN0n3zWV4iTJwmT8zy8zX6bHY70LIes_FpsJUdScB36BcwyroEBydueVq1x9DNW6qhkbYUcyP8LiyDOXErIpZCE5tkU1UgqtQhufVpknJ5LhoXGISTvRHaE5oGY1tVpLePtDHHKtUvLZMVescBMNqhAjD8vaskTVCO5DVg3OVMiDopoF24zMNMX7AbRIHDCV2dwbw0JcuRbR72rpKkpYg4w7cJJ3Gru5aJ-o166ZASUYDpf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=m3SeVM8wOW0DqsmdRfduX3kRTFsI4RHFcu5QoapbqJuvU37l02BUlHMyR4EmIeRf1wOH8feGfaDZt1kR9UZoE843y1AQnoa9zZUZcMN0n3zWV4iTJwmT8zy8zX6bHY70LIes_FpsJUdScB36BcwyroEBydueVq1x9DNW6qhkbYUcyP8LiyDOXErIpZCE5tkU1UgqtQhufVpknJ5LhoXGISTvRHaE5oGY1tVpLePtDHHKtUvLZMVescBMNqhAjD8vaskTVCO5DVg3OVMiDopoF24zMNMX7AbRIHDCV2dwbw0JcuRbR72rpKkpYg4w7cJJ3Gru5aJ-o166ZASUYDpf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edg__q7RdNa6JvFUTbNYmZYvpI_JT032j1P22sRlU6UOnqdj5pKTkIJCSRNQXYirL6VnZJQ3FPbGWNaA-lWXOxTU6r7M92AQn0srL2Z9DkB1zyiV_TIJnHEe8Z2ogSzTTo6xEnc0bVKNI45-d6uzBbjq2rcxK8_iGY-1nc7WrtA7RZTNdzbbSzjTcDk4ueQ0QNG36w5Esg7xAgtEJTzfK7RwwbxcooHdkjvx8TvaDzbFWcNPIDJPKvp90owZmvxN1jTT6u0mBOHTu1mOMbcST0wf4YTg5Jp1tcjy4aS0dXapB22hcY_Ne7iZ9nA5ykGpUMp6u6FdDAqylFb7ExNqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnWurpiZtyCL2tu77ZeJGikAGcLwF5XsqzANgxK-lcJ4D7ID84JFZvJ3R8sCJRoUkqVraT0nTCNRGU24Gt1dzrNKKAu86_udNXAK2yU6W8ixVqe5YCS8WDnFcY6_FsfplxF_XWoJAE6Jy3eT8Of1xAXQmjSRozJnC1-b9LynuatvanjXjZOIWTsaAdbud2MSZRtXbRaS7W23KD3trisp1AruizgvS0F9e7YpLHya9Xj66PngHTpMMvq_LCk7nii0_paMuxQtXmatdkSHsP2CrlE90IU5INyF0KaHBlBgg5groHWDDyuk4y_DO39XvnufeqD2N58gekpax9GC7H1MpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJD2iSIE7f7CwoOW99zjapMYWrOensByTyy03FdvIA2ZlAVLmkPhG2nq7TfN2YuGcvX4JoaGigtshx0GE6aWeQDXn2TCN6VFrwaPkz8kzqN95V20kL_d3_exfpPRxv5WMWtLjJ4BMqtJtvaimeUK8q5kaA_k4oYqIMJghWN24-332MYdrZF8ZujrNd1Ur1Fr_E5K3npeE24xUsxfCurXk1FpMR8n0nbAl8ZROQSsLvv6LRe_8oqVAAfJgzH6SKJmFCBQMzOTi0Ik6lkGOJD0Iav7sMIyrZVY-Z_FgCzaELjUnBcBD8ORdOUC2u4bAvkDSI_aV21Wk461vjClp4623A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=PTQbJCgzrpDS1QWJWSZf7t8-pX7jE0FYeln98nvFpQPcCCZhxp3NYiyOb-OEW7HxzvAOJ2ziqD8ijRWo7xj4Ojq2TvueUznT3EoeoCuBY89kcls1j-eZzWGy8pKTGzInDzeYa-EEv0sRnhydVoTY2j8UpagZ9npfjapXv0RErU_pR3aUirBa1x6CNzrZwsqkNuyQ8A9NSYrSj6dyfwdbA0DEaU79rEcIcfK2hw85v8SEIaNyKDreDztOzk63dwZC3o7Jc-AhHEfbuuNeaSCLvB0r9i-uAYac2DOxJKzianJLg3YvQYeJEZbVTdPLb358ML6iSDwwsd4e02VEs6gS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=PTQbJCgzrpDS1QWJWSZf7t8-pX7jE0FYeln98nvFpQPcCCZhxp3NYiyOb-OEW7HxzvAOJ2ziqD8ijRWo7xj4Ojq2TvueUznT3EoeoCuBY89kcls1j-eZzWGy8pKTGzInDzeYa-EEv0sRnhydVoTY2j8UpagZ9npfjapXv0RErU_pR3aUirBa1x6CNzrZwsqkNuyQ8A9NSYrSj6dyfwdbA0DEaU79rEcIcfK2hw85v8SEIaNyKDreDztOzk63dwZC3o7Jc-AhHEfbuuNeaSCLvB0r9i-uAYac2DOxJKzianJLg3YvQYeJEZbVTdPLb358ML6iSDwwsd4e02VEs6gS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpar4n6fRmhGMi5C6n34uLppNj3dJWD5CIqiJjiLoO2Bhj9Vjpoiu36vfnPlftxvS9qt4-DQ2Vc_YimrqLTOQFmcMvmDsA6wFBVAlUk9l80GTBCFulwiiqGEgu0kf7hcgLXUzJqoTPfvbAkRUYSlBXUtUfAK8Km-l3L7qmJOgo70AMmlTWMa0jolUgPG3Q3oVzTeqEcIGfyWTTJLwEo8KziSFzM3SLCcgxaM8yshWags58WI2vbtOP_hf3BPt7ba3uHu4BS3nAkno6AzrHpbZ09N8VUYzD6C6J1U4SRti-8uo-JrgLGrCkiSsvF2XZpzEDKazc9Hyx1pWqvCy_NGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgxaKSb6gwN0QfFT4YDor_5LlVxJeLpr9OSa-5mEDK2eTRU8R5FzF-qlNAlIsZvfetGDRwLRLfRXjRcldhpzNicPTN489a1JqdiEtj1FBvHLmApP0E1JBhwKaJ_NxZ7zyf57mz9-QWrxr1hvjPi-z64rHKDTkzKXeBGu7l_lZ79-LxwJisWmAMcF8dN8qo-NbxmfAyHkPliHPxfaFnDAa8--ks3MoJ1UJa54nQoXSkojT4ySFirsDYLejyF-jH-EjNs0OWa-UcDNKP2G8quhdURta3i7KzoJiTqiS3pbTNvImzSg1EMiVmwjBnH0CjYXaGy41jiK0qxr9lnDFWjP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDAvI-0cj6j-nVECwU2niaBrHuTRBSYrup9ZXD8CMYfhXmm1gik9qwwiFMIrlaUMZzK6JSSNQBJK7R__RD-aKERVuce-opwNBkYlaiXRUIrSlMLhiafHP3ubIRPUWkWjmjiPVlzY3JJJqsjUhGOSy6-cyB4_yQIzvuwpqtcvKjqfBYF0YPjIJ9tVsf0twkredP9-n0dfHcaF0V2LJHjkw4yOyVjIENy2Y_2QaN8hyWCvrfUl5ohI8F-ibwG462phYTXVNmc9Cd3TdHStrIMued_HYXRf1MGZCczHXsvw-oVhBNuQ7_WzWZOIDjytv94SMsrU6RISrX9WLlx-hbJ1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXJmSu-sP8W76J0644D6uVbkh1cLO_cLmQiijB68PyyrVAsPFyUDnTTaNJLQpssdwbamKNyLcv0tRsX9u4zp-ce7AQ0yw7Ok2xwBPxK3R_nH64yDdEcJDS7uEGpgidFZ-EkQcWpeyXOhH_07ObXO7y2faAFxK7ftlcFPxFLUI1dI6Zuj8h-ITxQhq2pWwcYQ0EkKziLJuWl1uhOYr6cTk6gQmdTSBrOviWbNZE22JgciYguUTdcXbJ5Ib3b5C-GDIaGlPBehhvs86xSOstbS5U7QPujrP5nhi5P0X72HPFd6s5yYTCoSuiotwlOCp9L2hxC4rLWddQes0ZfI3AGF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDsLOoAooyDPwAuH9qgcsVhBt8X-0ElpmbJ9HejTUFbu6LUwUkxZoI6o7CnWwNkXbmAx7mfXqKgOhlN-Lq5V5Ru9RBIhDTCdrbfKVF6lUHCl0CECxXsl35sNxDCp7bHbyIPWZ6g5qgFBbh7zAn7B7qGxdghH8P3qwbYY8rLji3QQR3D_PwloINwkqqFCk3TdCEsViPBv7gvkSerldw0B-IHgm-N1Lh4QMkwYm7x5NraK2MjmfHSlKbmfb_NARcOV7gWSQ8Ftz3dzenbDwYUR9Io_dvWvI1EvDaDp38X8MngWJek64iaVNxQFLFNQzBWT78tNK38nqtgWt8HGQRsKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BV0s1etJGsMy7s9v2v7d9pDpQIcahASrdJNb6LlzqpZmjMBYzy17j_pE9TJQO-39x2_LXwLzIyN1nFrhciSHO9AwTRfZANVW_Qcqiok27v4FAAWlYxRCp9qWxv5QI-Deb7w6pjP5eDMJkfA8SleKEp1fqqIcirqWdymA8iRQQobGg1E5SVGkSPkr48iJVzKE_9kaX27YlKMnqRB9DL9zPxnpxmfOjKI27FP8WYDADZ-1_D4gPPtEz8W7TN3vlOw-q5-PgJACjBjBulUWoMGh1vw_3H-lBddzGfWp1SR3Puri2D49r9_phL5t12kNYYjB88aSd9wCcYwKEmqAWjmp0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHjbBBAF7rJ_0PjD4_FMcoxGMSS_nny3kQe-6XTgAT2mhEuB5qwCnQjbgmL-DIV7zrQUg6VYuRIgBud-85LI0CwGbWX1Jfbe0HD4Tjh-0A89M7_QCBHebH3rA89yo4hP_j2F1keo8et6qATaj_CiFdQWRKttEIP5TvnsK4OhdgX_A96pR4nfA0D3YGn4BnefSH32gaWcEEYRtO9a68i8_StprY7-YmRj6JP-XvZ5tQmuHuz59P6I-K4cWKEvcyViQaXUZPM78-_REsVlRQBU_0ueJfBg-3LtDnCAVl48UZR9e8M9D324biHzWJ5lo2dRagx7fhb-c2ZToxudQ3X3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=O7E4I7lQxAi8BNd3HqKW5TmO2TbMrJMaAbJkd9Z9anH5vIQyjpwqVulLhFFYQRjqY4dHgJJ9EEDNDpgMoD50KlE6cY7BFdoHes-bAtFB4SmwZ8Aranb2emVzfM4My3DiWOqd30X4aDPRGl5piZ2ebqhZmQd4IK0leVgOnz90S4amKVBhaXFGf-bkNEMoV_0X7z6yMC32ub4z4jWwluqbuo7SgHqT7s03JvHMEb93carIrrt-GY1blj7gcTP1bacOnaNH8UFVujy9okU0RTyROvFVgnGIjPq9UkGM0P1XpxIzVd_6svtNlCH8dnQ9HeM2Q4qf55_sYJNK1uFsbOMyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=O7E4I7lQxAi8BNd3HqKW5TmO2TbMrJMaAbJkd9Z9anH5vIQyjpwqVulLhFFYQRjqY4dHgJJ9EEDNDpgMoD50KlE6cY7BFdoHes-bAtFB4SmwZ8Aranb2emVzfM4My3DiWOqd30X4aDPRGl5piZ2ebqhZmQd4IK0leVgOnz90S4amKVBhaXFGf-bkNEMoV_0X7z6yMC32ub4z4jWwluqbuo7SgHqT7s03JvHMEb93carIrrt-GY1blj7gcTP1bacOnaNH8UFVujy9okU0RTyROvFVgnGIjPq9UkGM0P1XpxIzVd_6svtNlCH8dnQ9HeM2Q4qf55_sYJNK1uFsbOMyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdH4S5vCPG_Mqd-kNh4MPufSVFDRMBtJfLPXpBGN9PWtUs3_3IT9LQLPEr7iZiESdYjuuKCYyVbZaxAlqo2TAzw-AIyNce_w8Ah-uj2tFs9hvH19ClRYStvdIzw9wnOek8Rz69AyFDxBf3p-WWF_s8Xh6FIEPi7fkulZyFxHkKaz7E5ekoTW8ouqXC3EfNqtYz5CmXqjcdT_andqIY-PKCJDjnFWZ97tnksjHUEDR2VPeittCQkCNLX8wlf2WBVLAW9AuaxoONTE2CrInR17htYFbvtASUvT6IuIo0iQ-RJgwVzii7Qf2KzS78qxMTs67oTbJExQwCS99Ty972wVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao_412hFt-ygNU79LiWBzpMH2pepgCynyt0wVHC-bjccTkDfIz5LRiR8iRi2s2uFMUN_hFQo-wcgFlPMGxdpkZRizqL8R9ukkU2Vuc1crLVdMm3QfWvonZsHL03oxV0Ge3VuLadLOYYpa1j9h9jPj1pS2PmuOSas3ePi8APblU0IS9MTdSZAcpfBULKgVdxSkTq2wg9Gd-41QmJsW_9NVjqtaWE_muJv0KAXa1sEoGhBmZLZ-__xL-rj1fgBUqQUFXbFqcmqRKjYC60qby5mBPgpsDYrkiDlcxQ4ZdynwjJXCgPl6gsY7JRe4Avm7mRzAaOqACR2rjW9BG5synMb5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPcwnfOvxNXgYWh2SR-9i8e9lACXd5Fz9dofSW8ZXrrYShIlG_7Zlf4b_If2EweDh7DIYzwmd56ngzxxz27mYJnAFXQPCv3chJ5u2b1PEzGcI0_T94BUao9h4Aku03OHF4aMdz8GRhMHiYDml46dVPRaTPn_6gWyzM2krhFp5XfO_22FGJ6ZPZ_ECLsXozljaDikDRNBKjmUDyPewcH4Dr4lYWWdDDcXw28Leij6HRsD_B_4-qV-ShhMAWf4peUSeJZlxH1vFg8-tbXCHU01i8G1p5rHp_bwVXk5QHEvhlW-ojbJdoFkj-zpG41NyDJ6tC5W96y_TULp7lcHHWlr3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJxE2NCqZQxLQlbnPVYhRN5qHdTWp5xEDSA2LtcHMbUYYUkh9vGcJwMoRS0Y8FIzqfVy2mWTAq91JE3dG1EPYIEnPNWoVvSakr_rt2tj4b1_6aT2Fv6FhvXXeDE91excb6uWvLXbgr6rNuonGNJP-sB0UVlAGy2xms6XwSv0he9GfLR158x5PMyJhqalALnHTKRZJrxpidN5Ng_X3WCxlVZNvBprAW6Tt0wrxV9v3WMG-_de_iR91ygLXgfxJk15Dzm9DNrkRWysZ4frcHmA5JQKhsn8R0gl2TjVQUmsFnOAtzEENYfLNX7o9nLOkpFA1-tz6PVxe-q3m_27nPeKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKcJFqLsrsYWRTh3sAQi08WHWNKUCD6Sq1o-GJBu0gv0INbWSIppRa8VN8yRzttzgi4nmSyec_KexaKpWiTURJ1PWIQ_WTf6WlHNIt-7kKJPphoLtRIntXkBrELqp8uXQpx1gm8owja8Q5VuskWW-I-0sR7eDvtZfRS1Fcnfmvg_Y2RICEb4HQxGPlfpMBY_RNDctZsHsj9JsD4qhmDQ0LXKbD0i5Ju6Z-2SRxx2KZihTsC_mHcRgFBtPK6S0jHLRnkygllc-613byfVO7dN9SgDc4U3-ugQUZShzuEfC1KgPR2QROJRAlahDgPQs06psnn1uTMStsu1yy1G2xcS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DM2vU-rweBcEdUYgjLZcwj17Xa2yDogor5nDFQd-D7JzfpykiN4DTVQ1VAl1buF155Q_HHrtfY_OTKdTDjw4lAAe8QN992VhZrK2A2MPs4c9yams8sOAOM1I9wk_0IbHBGJctQTlXdXIanEaudjkoSOJ3QEVdDKGkJQ-WYIb-xH2f6A2HbBQyZRM5yf2dRYGU4iRavmLqS810beWu5gKqTDQc1neU7D9sj1OiLuUqX2dl9U2ZLZfd6vHPkh6L9fr9a-HmA3WL7mkGfrf1_eB9K0n_4-JddtL5sqo2nv5TvoS_KhfdQdKJ13bh1Azto-FiTsPx5wkBc-prJmc4jojnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hX_luuhtfZWFHmBN-g0thkwfr6eBNGJgDGaB_Pc2V4F6jLbiwiQk_8VEzp5xR4j0lmSh9a8yCAQRiegC0n_tHAqZtUsw8S-Ly-7W8048nJM2Jr6kcPTzevoVQeo1k7Vu6EOk7BvRxkkv2B4lkfuA4uek6I0lM_WD9DEuaTgepVZTlMZfZ6Ls6oReIQH7HWbv3GYzw27vrwb9PBKUF_bk0sEvjqYqPLp9XBF3HBP7Uivsw43rczTTKy0cHpMJYd_v_tPO5FOZOxw8e1J3jcY9dLMVr2EcbwHq1WaswlmwxvyJj-R67QONYTez7YE9Y2da03mLn5gKA1KAmFqxxkAzIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptg1QiZpxIhZ-Py4iTotKSh1AZdlYUwP6sZG_SDvbJrItTD31fLWj672A4zz30lJIWLxBgULizWD0tBSMF1Dz6moRMEq4SlsRkoatdwgFi5-3oP0sdmOwjmnFkHt5MXlL3YUH_1_vg27sOfKR5Qh8jTQYIFUUqKlbjF_zBzbTIEq9GBtHoct2IBUdWVPVWeDii8dYZOQOeI0zg_rjh-JXejnwZZuqvT4IQvQV0hzB7OqzQeyFsEM53j3OCrb3s8le-BXQklVioB8MUS3R3Xms3RruTDKhRacw8Bi5YngIKkhmbKLX3HfaViv2FppE44Rs5NFv_u86WL0UdH1TJdUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daaLCO08ELjky6YcKGN7i4-aXqjEJv8hoSBpYxqYyndiH6s40ki0YH7qnAR6G9BKGVOX5uV6lLvfnzrC08Fl_uWdECu6rpLS2-AvQOVRdoZamwbZEWNdtTb8QJSbMQtZmHGW91P42cCxVOaUQuxHyvufPROrEU0SxfGa3OxuB6HR23kI0EiuBZ-dRgKr61v3HWgsABAneq6_rfzyI0K2tPUEGb0ae7t6l2ZbiWPiVjwBh8G5cxQeMNTkCgYSdG1ANEgDuQMPxl9DVablm37uE4KS8OzvClmATUlArxPmIKThebEnG8yEFoi-uvxIEEEJbWzHaHfgAgSBUmiWUTjJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=IpB2wNhokYzWO5Ze6I1ld-5R2h5ySY5vAcuJhiWnmuRDhRKXs-zmdwHNg-gIjBgEnr_WiVwF6D3kx1CpB1PhoyW7kRDmsvfs1tiVIE6WDC7QOjiWxO6xP5gLHwDiwG-tunpLTK3RjsgSoVm_nBjReOSk-QUxOMhZnABLlnMvsFBSR4ApZWODQXagCH9jz4f1iVX1-sMjmhjNA6QTZfK4IcdvwNG37XU6vAPRsqVleDiiisbcdoUt3FdoMBCl93uTVt_HDR0O9WmP_3jcl2DuQqa8DVWC2RZJSVi-dtssQuPZkkI4aKPg3WtGjvczhlrSj5s1UN1vULfOo6tADDiXyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=IpB2wNhokYzWO5Ze6I1ld-5R2h5ySY5vAcuJhiWnmuRDhRKXs-zmdwHNg-gIjBgEnr_WiVwF6D3kx1CpB1PhoyW7kRDmsvfs1tiVIE6WDC7QOjiWxO6xP5gLHwDiwG-tunpLTK3RjsgSoVm_nBjReOSk-QUxOMhZnABLlnMvsFBSR4ApZWODQXagCH9jz4f1iVX1-sMjmhjNA6QTZfK4IcdvwNG37XU6vAPRsqVleDiiisbcdoUt3FdoMBCl93uTVt_HDR0O9WmP_3jcl2DuQqa8DVWC2RZJSVi-dtssQuPZkkI4aKPg3WtGjvczhlrSj5s1UN1vULfOo6tADDiXyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAZqjpGqPwV6EcN9fDurK1sql7DUFFd4eJLPrt97E22farMeW_OLhOMiOnSWJ5GcJGtM0-1v3ck7gUzHTfTYNtUxtALNd-Cu4u7Vr7SVDZCo50-FRgDW_9Bxu9Ru2T6VWY6DP0fD7QqRJ4SOIg1RJ1zog5PNy7LQeThDGqB38IQqTsc2BGVD0N2M0R_8XBjyK--RYcblUGYtA1l0HoaMYC7D413ByIbKwHevBinRf3ncJCjcl0JtnIjIiX4XuSHWb4qKFQPQ1Ny2UEPOw2yGuQtjrZonUMYRbfefR62ExbUWV0JM4D3aD1we9OZW8IstTLAgYFkOVAfkUKEXXokqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0wTWH2gBWbTvGfSy4OsXl4wR-y_8kZvYjzSCWlYDkP76Dlq9zrTbqOd35tescfsnWK81F2088wY04zcFgYuq2w-DsnBr_eohV_JJHcRoqReg31eXGMb3h2l2YRETO5R__tGfyZRL3gx4dIlQfb8f6tumu1jHN2bbmw__PwUp1SVLD1AYkT2Wprl2Cy54cNp1uDV4FR1aQ_JYZGW5LKD2PKVPMQcOPVLIVVTuH6GPViS_pUQfKVX5tQiR5IwsvUdeHuSQithXcA5uGgRRTl1mJcjJ9y-OwqydHdNYCoWXpzL-9gPxQD7rjNZ3opcieGu-DmqRhqncYQtL6ZKmM-o8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf_Zgvfw7ehWJ8uaFl08-bR7n9k55K_mpeAXBk7UMlKpM_qU138QGHfp0yR3bSXhYxi9iSwtgWgOw0Bwv8ppDBEml3JFD0cE1ZxYw9Pf7Uw0pcHwUXDjLbje1p5pIfEAys7cSRAKuWnuzN9omLEsAGDBOgBt117n7Cf0zbzetKnLuKzs47Vw9R7nsNw0euKjQHVcHIHZiJQKEs06GA_dZlTfXDMbxJWUEQ7mbnamm2C050PGvEsDhLgN6zt8PCYreMUZg4GqmODmBqXPFsa55eR1YtcNfEeGJ2zZkgi8kjQ4nhKAG6tzY3uAgQXEBvZGNHA08XrD8Ecv4gdukxHrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مرورگر Sigma؛ ایجنت هوش مصنوعی داخل خود مرورگر
مرورگر Sigma روی Chromium ساخته شده و ایجنتی داره که به‌جای شما توی صفحه کلیک می‌کنه، فرم پر می‌کنه و کار رو تا آخر می‌بره. هدف رو توصیف می‌کنی، خودش مرحله‌ها رو جلو می‌بره.
🔒
مدل محلی Eclipse داخل مرورگر اجرا می‌شه؛ طبق ادعای سایت، پرامپت‌ها روی همون دستگاه پردازش می‌شن و آفلاین هم کار می‌کنه
🧪
حالت Deep Research برای جمع‌کردن منابع و خروجی ساختاریافته، به‌علاوهٔ چت با هر صفحه و ترجمهٔ سریع متن انتخابی
🗂
ادبلاک داخلی، تشخیص فیشینگ، رمزنگاری سرتاسری و پشتیبانی از افزونه‌های معمول
⚡
در بنچمارک Speedometer 3.0 روی مک‌بوک پرو M4، سازنده مدعیه ۱٫۱۳ برابر سریع‌تر از کروم و ۱٫۳۰ برابر سریع‌تر از سافاری بوده
💡
نکته:
نسخهٔ فعلی برای مک و ویندوز (149.0.7827.117) و همچنین iOS و اندروید موجوده؛ نسخهٔ لینوکس هنوز منتشر نشده. بنچمارک‌ها هم تست خود شرکته، نه مستقل.
📌
دانلود
🌐
سایت رسمی
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-AoXZ06aeRFY4cDsCUGj1zM9JlL0w1FK6k9L88v_L6ckRdVpR_vPGUPwX41ubbaPBto6IbAf0zAVSElilVM0MIOGiOGwqt9vvLTxJ99784J1cesA7q0yCZUh3Cvh-VGcXaf9bK5W_fyZfmruTXehrnfNlkbQ7l2iCar6oEt0dQWKR-VmPrQN8mDqG_34_ddqIRrjqglZbJxX4ivz8o3f6bxfTNg0VOoFLZQhkPNxWgkvrNProZjSMW1SQXT21RGWF9f9VO2gxaMibu_2UZPX1IE3_RUy1RARSy6q-3hytyWGcb7ufGLFuKz51SCRBUw6_8M5v8Hm3KNf-LXuZ01Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4iXvQqAV0L_hN4waupJ_XCU64CI8yHSXkKDr2Ya9YWk62X2peJQDTckwHfqO7Nuzg5bu2ClsNm0vIiYVAIH0fAVElNfi2BSyGb3UKlEszoQW9hIDTWpu8_jJTLK0pDrC9XjaXlCVIVV2Bjq8GUjfg9Wd0BrGpUKkwEAbrA0Bns142ctBhM7wfcxfGaNim3o1DHlBPso-DYnWqDdkAcsZR3KKd8a29dr6OAlX1n-D1OHdx1p29aT4brcURnZl_N9Ikw1_1c_GGk_JWyJpiNWg-KnwJGPaRzfLbUJvlqjNBnQ_DSOYIoGjRXFhCrgDsUMg_GJHEubUJfsjMw5THS0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSWRXuHnTQTbaszg5oRFGTyGhO9EOexgmYzLEZevDmJx3IKYg896ZB_srcX9D9HOx83OaJZnHjdnNyCKMGtxZ184doDF98T40UNHtqF4v898nVubwxZKgrsUnSq5O5XAqsMBzadKRqfB4Mh4c-05B7OBhZOOy4QJR5L3RHX2lh21Vk-YDMS_nLFD8bvjh9hOdfYzvDs4xBwEO7__xTgQm5bFSF8v6OSzWSnKcmh2jaV6EwzbFN7JfcXO-cQGEl-UXDhNvJLANRSLgr9E4ci189-WkTq50vw4ova_lb7JhFFjMvPuSv0zdaKGYpyM4svGieLf2oWeY-u0EpR44B91Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cloudflare Quick Tunnel
☁️
یک قابلیت کاربردی از
Cloudflare
برای ایجاد یک تونل موقت بین سرویس لوکال و اینترنت، بدون نیاز به باز کردن پورت یا تنظیم
DNS
✅
با استفاده از
cloudflared
می‌تونی سرویس لوکالت رو با یک آدرس
trycloudflare
در اینترنت در دسترس قرار بدی
🌐
🔺
بدون نیاز به دامنه
🔺
بدون Port Forwarding
🔺
مناسب برای تست API، Webhook و سرویس‌های لوکال
🔺
راه‌اندازی سریع و ساده
📌
این قابلیت بیشتر برای تست و توسعه طراحی شده و برای سرویس‌های دائمی مناسب نیست
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzVeoBD1JASBaehUnH2wJ9OcxW5MjOiD6snXd2shCABd9VTwUig7uwW7aV1G-bDvtfQw7r3RJwJlsGuwVqi1gb_l0VzjJf5CjrCzEx4przMsyQS2-26E91KDrSsyt5MMwGwZPzFudeOaBwHDwe6b6y-HJ-F-KtGM06DiiNrV10fPLax0_M5QthZSH6F0jTEVkpsx_R0z0tzX4A5z0x-oK_XW0SZi2f2DUdQ2TjYXjjt7w69O9Pww4Bts9A1dJwmJA6StaUGlAf2FSVR8Vw9zwDc-Pflg0aMmGsQzZpuJDYaf1XBHDGY0MKD_N7qgyqy1bVvw6uzQCEZui0EzoUFTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4XaRitD74zVKOhbTvNNx8XIANKugJC-VmbSVflMHZOVUZ7SFIeQg0q52ScirZWdgKoA4zyDNjEYDT8Us4w5cDPqOuc-fwAqN-Yzrk5us_cDIrC1F2S8M7IAWTD-jmPramY14kJusAErO18sZrvoHElPNpZ3RtYSPj050EaDo3_0FAwhB_JSdeSU410LOq7zcFnNWZiU-mMH5nx-ttSdgcaYWoXYL2h455WoghyDHZz9QhTIaH51qYknnnuo8eCD8E-PSUsgAqquJ_WPbEcpBPM0w3TGwVOvMEBY7mgVjC_PCHLJTWI6nGHpxakq_iMMXOSGx0eeJEtMwQgcOk08Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmp5HcL0Uo7nuchx39NnhRFqCx1rfxlpjuZ9bC9RB7ywRcXu1LForcYqT_mkTdxrWLKCsN3Qy1ovb1LEe8GuVmB7HnKO3Yv--mL5sx6oS2kkYfc3bWxV8eiUnfmfY_pB3UBCJGIV9s2ZSf2QmgcRJdW9YDYQYVOnF7cx7lqvwVRmDTNcvQZcro1GTrWztSqWVBDqJzPJas-H56HkMoJxcldKWZX0j7qrs4VdLOsl4ZSrC9Z0eQPchlNDhszgeYEOJLqXHatI61S57bSZhhfeIT-6Gg2os7GLSJBszVB2nPI6TF_3GytLhjZhHuCigreedPLs4WomAzaMr2IVzy_2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reBKEG9SWZA9FzPosZuyHjaw58vmFCJmxwRLL_aFHh-o5-TEiptazxVb0jD0y0XX9su0J_efqbLlg7_8LMPAZ0w-IlxJSA7eiLY1Fzv4kcq72qfcwGq-p87-hp7vlXohbzs3l6nsJKJuyvlWOBhBQiNmx2j7IvuK6i0bxEbqPae3v2CyvfsEyhGuEtO5R4IHdk0FWzwh-SQtljEipp88mOAo9aFIHETjddvNezmcDBP4w48GHIkkSoMEobBFP9Go8dgYVLNiBxugC_JDJYeS1vWlzW7nBBLu8pBqExKtxUAd0tPfqY2OtjFA-VAZAkCDIwC9H-ASOdZKZ-kzGB_M8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM3VEsi3bPgk55Ep6GvcOJPI_q2-qZ2tceIem3S5untm-vKbjx_rreMaaGDzp8alnMTo7aFsB-ltPbyptgUnXDc30wWSg_MDqlPvoX1jpce4groFcugyY_3nuF4H8-r41tRpWA5ROE2t9j7-HETrPufUQ87qcoOWFQpR5E407sxFseBF32Rn-n0gnvnUE3bVRP_M2UImMQbTR88PH0ygDNPpBvEXKpVUwgzJ9Rd2PVPRqFFz1q_LaZaFiLm2YcozdryQr81tcb4yaVFxf7yWuwCvFsJLdh_qve02CuJwMg6ONHePwNQ3A6Kr6jMYS67mC-ZYmbojplr5nPLQ9PjsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppjImgaKceQmanO0-Z3NyqonbaAvynS-upFSypeJ4eUKrrgejJ0AcSyRQ7FilylyJ3u1VVCB0GCMQFcA3XBUldeHjxClztzycJ8jg8pWFGMdSEVCGCdvzrirPsvEKt6r4rnseEa6Q6Zwrqr-YcSBvG8lsQ4tfdNizqZY_7iQ6Evz4DsJNWO72nD53MUdlNChGiF42oJZ0fkrbp78j5dfbqHV5eMVdpx0AC_XZRDzfyzH0uLl47MnwzndhoLb1EK-hQP6EXiqglfLVQEqVduS50yEck-ZTqCKQYls1q5682UnsSEDZMVKAH_EnTMIHDVvHmIWvdHQB6TAGKp7Y0uYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxjlmkLHoW6O3lTeyXBJrS9nuxy0dMnZv-IPxZuUiqPvELDATvnEl9bVJ03XFY-1Ce3UAZ1K5XflqM_FRrD1BYPnxK81_30XwswKXGhs20n7DUv1-rXfAN1_Wls-mM8pMI5APiXUbArG1p6UHcV4LnO2jLWjDOsZyCor06CBu4rdPA5-jwL-cqjcmELcYxp7X-ec32_7LrLlv7Z4DvbHUFehYKYcIM4VmnH5hkegobNphDtDohXf73376vcTKIM4PSnV1U32-BJDCOBx33xPm-tDR_9DHfjCsHLJFoHbfk9Bo0wiZbJ8-I2E_WHwYiFM5mPlGy-J5fJ2EW3OjR-9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2hCgnhuf-GruLysjAmAxlbnDr5ZhJYFikZbpsYYbQFFlOmpaTXeURfsvHvXJR6_4Q3wBic92GsCchiw39jkQAQw0eByogFtDiiij4OzuIBiuh5Atmc8G7HVLu8TKFfGJHYzcDuKMBAq7NCsp4tbK1Ca357eQ8zonZLmVmsel__Fk1hAjof8s2GKzQLNDsWfP7rer1_sB0ebatTaWQ6xVRX2aZkywiORZipxcsjD_fB9QkuyNz4xua-eRc2ABeQQxdbf0d5OJmP_ZqszJIDQsaP5YwNyZGWrNdfjrE4wnofa6k_hP2b9BsKvcqSBIXzGrSZzakOmEnx0PZtZVZ7T4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
چت + تولید تصاویر و ویدیو با Kleo
🔥
آموزش
مدل‌ها:
➡️
GPT-6-Astra
➡️
GPT-Image-2.5
➡️
Kling 3.0 Pro
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=nr08V-23mkZYf8_SXRAZM00AC74jP91sBgFBNSQIQ3s8t9hLnfV_slcgtWTh9-4ATSEmu2EikHl182zhZqZQvB6mkQBfCtRpXKyrnXc-hghwghbn-qFNDX08AHzFJ61rOFLEezyc7oNIkVZHc2cyinIqgXEDbavPSvd3RF1MqI6to_TKaoFeGCLm2_zZF0y_y9NMyUe_Y1n_pRUBfK_uMU6o58RW8wHezx_NRjmwGens2B5M5SQ32Lr0VqgG2To_VQtb090OMbmOBGGfUc-w85s97pTeDtiZ_BoAHxY4PK8tL2X0O-l3TsK6QBRINMShmwNYUUp9QmEPLbPxyDjxmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=nr08V-23mkZYf8_SXRAZM00AC74jP91sBgFBNSQIQ3s8t9hLnfV_slcgtWTh9-4ATSEmu2EikHl182zhZqZQvB6mkQBfCtRpXKyrnXc-hghwghbn-qFNDX08AHzFJ61rOFLEezyc7oNIkVZHc2cyinIqgXEDbavPSvd3RF1MqI6to_TKaoFeGCLm2_zZF0y_y9NMyUe_Y1n_pRUBfK_uMU6o58RW8wHezx_NRjmwGens2B5M5SQ32Lr0VqgG2To_VQtb090OMbmOBGGfUc-w85s97pTeDtiZ_BoAHxY4PK8tL2X0O-l3TsK6QBRINMShmwNYUUp9QmEPLbPxyDjxmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
مدل Kimi K3 به صورت رایگان در Cline Desktop در دسترس است!
🤔
شرکت Cline به تازگی مدل Kimi K3 را به خط تولید مدل‌های رایگان خود اضافه کرده است.
🤔
دسترسی رایگان برای مدت محدود.
🤔
از مدل Kimi K3 مستقیماً در داخل Cline Desktop استفاده کنید.
🤔
مناسب برای برنامه‌نویسی و گردش کار هوش مصنوعی.
✨
؛Cline Desktop همچنین از سایر مدل‌های رایگان نیز پشتیبانی می‌کند.
⌨️
برای شروع
اینجا
کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Fx0-cELLc_8UIjj2w9l_PJS96CXamKJ67-K_ZH0dTDILHuf_dA8RieSXG3oY2DtxO4fI_ZC8zbgj4yZ74ZCK_OpDfmYVI1tjUg5TDEINiuiE6AwAvXHt62xmkENEHePbh7KqcP7vKspnASDpQH6Ip2TKdFdGrh_S0sKybQL4HwSCTR503_1EJWKzmLC5roCTuMC0nUrXG0A5YY_GI9q0wUKRT5aJcW9DLFuvazAaMwuN2mJfyD7OjErXN0dsvjmfgMvE-eu6l8oxCse1alvKYvcfi9ED6Klf5VaDQH2CeDTS_5yopNkkUNtEghqTqOg-X2Ly8xFHwT5QCJXZHPLpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fE-ThjTNdVuHmfJRVnlyHpyQmr0Rdx6-dtoHuAgnMFduqhiFFu0_8Q7QV6KGFOYcVe4vfjSpa322sWfsivcx0P-VRQKJrqBQ1hlxfDzx5lJsXbbIPffbyiOwAFyXDv6pZiCvHBABSSkv-RdbXeNExxWd5rMBGbsMxhtcTNqVHtv9yfx3RKijNo4TPLWWtmMOyOHBfYlsJ_EFkwErgCJmhYgXugfKDhjNt_gFrjUpccQvhS63A8TuhyPPwCTINSauL3MiWZj9gkBY3mdiMfsLL-6hIKX_zdtXu8r3p0KmsOjVd8aCW4HYMK7bwWhxpxGv0_-1rDLiOnmGZefukBgF7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNhHBPpSbN1YOx-V3gv8Y4cRv6gAiS6p6LKqSmWIfgVfKiZoT3qn0flshSkYd0DDGI8QngD8Obw0djgLQQaX2lIRjfPAQ1hvrxnguZtZ4kVJ5mb5DDwVbuIkFhXW0S0guoDJ3LnbzUgpsXzTzsKCa5bSHilT3BLK9rrohscOJAUzMxhowFTNuQx0eOuByVvzOeg1IoHzdW1uORHxaugnEkpyCfCpdCALehIgkoPTDY785rxZYHToKAbvRwscgbjuKrRoTAeizRFgM9sBCuJCOUBZXNwQQi54BZuDFKbX7uMbm1ERq9TPSqPw6KzV5rPPp2wnSy2ihWCOtOUGExHDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Fable 5.1 به صورت رایگان در Freebuff CLI در حال حاضر در دسترس است.
👾
📢
؛Freebuff یک ابزار کدنویسی کاملاً رایگان است که در ترمینال شما اجرا می‌شود (مانند Claude Code / Cursor، اما با قیمت 0 دلار)
🆓
✍️
مدل‌های رایگان دیگر موجود:
🔍
🤔
GLM 5.3 Flash (پیش‌فرض، بدون محدودیت)
🤔
DeepSeek V4.1 Flash
🤔
MiMo 2.5
🤔
GPT-5.6 Luna
🤔
Solar Pro 4 (به مدت محدود)
🤔
Muse Spark 1.2
📌
نحوه شروع:
🤔
ترمینال خود را باز کنید.
🤔
؛Freebuff را نصب کنید:
npm i -g freebuff
🤔
به پوشه پروژه خود بروید:
cd your-project
🤔
دستور زیر را اجرا کنید:
freebuff
🤔
از لیست مدل‌ها، Claude Fable 5.1 را انتخاب کنید.
⚠️
نسخه آزمایشی محدود — فقط 500 جلسه در مجموع (1 جلسه برای هر کاربر)
🚀
از این فرصت استفاده کنید تا زمانی که باقی است!
⭐️
🔗
اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه موقع ورود به gemini یا سایر سایت های تحریم به ارور ۴۰۳ برخورد میکنید، میتونید از dns های زیر برای دور زدن تحریم استفاده کنید
👇
dns 1
111.88.96.50
dns2
111.88.96.51
dns1
45.155.204.190
dns2
37.230.192.51
dns1
83.220.169.155</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام بِرارون و خوارون عزیز
حال دلتون خووِه؟
🌟
فردا یه آموزش خفن داریم که حسابی به کارتون میاد!
🚀
مو فردا مِخام یَگ آموزش مَشتی راجب «تورنت» براتون بزارم که کِف کِنِن ینی قشنگ بِتُم مِگُم چطوری انواع و اقسام فایل‌هارِ، هم اوریجینال و هم مُفتِ مُجانی گیر بیارِن و حالِشِ ببرِن.
😎
🔥
بِراگَم، گیانِ دل! از بهترین کیفیت فیلم‌های خارجی بگیر تا همون فیلمای پرده‌ای که تازه لو رفته... اصلاً هرچی برنامه کرکی، موزیک، فیلم و کتاب نیاز داری رو یادت میدم چطوری سه‌سوته رو هوا بزنی!
🎬
🎵
📚
پس فردا حواستون به کانال باشه یاشاسین بچه‌های گل خودمون قشنگ هر فایلی که ایستیسَن رو بدون یه قرون پول دادن یادتون میدم دانلود کنین. منتظر باشین که قراره بدجوری بترکونیم، ساغ‌اولون!
💣</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
Ashna AI
قابلیت چت مستقیم و یا کلید API
🤖
مدل‌های موجود:
⚡️
gpt-6-astra
🧠
fable-5.1
✨
مدل‌های متنوع دیگه
روش فعال‌سازی:
1️⃣
وارد سایت بشید و ثبت‌نام کنید
2️⃣
اطلاعات حساب رو تکمیل کنید
3️⃣
از بخش Integrate وارد API Keys بشید
4️⃣
روی Create key بزنید
5️⃣
گزینه Dynamic model routing رو روی Off قرار بدید
( نیاز به تایید شماره نیست ولی اگر خواست از این
سایت
دریافت کنید )
base url :
https://api.ashna.ai/v1/api
🔗
app.ashna.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGbqKdC35q4ZzeWL1XujcPQuBhBilt2tw0luwMH_mp4tsu36SmBvFTww7Tb0D35qDijABtIogulajTWgBK5A_4x1imnnPUPHXtV60CkiTxva9rswCTfW0JLgmn-Y3phblNO-ZroUMs9fIpOWtqc92EwHu4c2dlw-dnK1MsBvEXt82vBOgLAN6Ad6-HmzGLHpExFHAre3SkA6B_mo5jlgnozmBtMiYgDvNjclBiyEpSWkNKXN5LUg9p2vppxJjvHZdeLQai1Vwafcdy0692wt0nkNgyJMxNFqd0oPGafolLp0vAaChIydNnzOjDASlyL-7SPjWPiqYjZNf0c11hXPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2ho58eKZ_pZvgohnWpcRjISTjE1qKXpn_QmTLRjuzwZXi3VFCT1z2TmzABSXvKGB_MD79bZcRIsQbU_VrgAR1KPm934BWqihMtms1yxiNjolUQ0sY6jqAr3ak6Pn398mFI-jZiHGFD8uHgHjDIYLB9KJyja-GrZkpqyDMJ8f8vZOtgskFuDq_kHBPoMk4hE0cyyyaFqxVGRHQhDVW7rfVCDuzdIVnJDLUv8uPAJ8GuZG2z9EdE5qK7QazXEPloLDnKbZ_ngNYv0VLtL8M-WTcNijJeI0zwoLC9Uc0pvX9tr50d4nx57jcm3vEyj33YFiTuVlr3Wq1kPeAVIn-YZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تبدیل ایجنت‌های هوش مصنوعی به کارشناس امنیت با ابزار Cloudflare!
بچه‌ها کلودفلر یه اسکیل امنیتی خفن
منتشر کرده که در واقع بیس اصلی سیستم کشف باگ و آسیب‌پذیری خودشونه و هوش مصنوعی رو به یه هکر کلاه‌سفید تبدیل می‌کنه.
✨
ویژگی‌های کلیدی:
🔺
ا
دیت ۶ مرحله‌ای:
ایجنت رو گام‌به‌گام از اسکن و تحلیل کد تا شناسایی عمیق آسیب‌پذیری‌ها جلو می‌بره.
🔺
گزارش‌دهی کامل:
در نهایت یه گزارش تحلیلی، تمیز و ساختاریافته از تمام باگ‌ها تحویلتون میده.
🔺
راه‌اندازی ساده:
کل ساختار در قالب یه پوشه از پرامپت‌ها و دستورالعمل‌هاست که راحت روی ایجنتتون سوار میشه.
💡
نکته/استفاده:
خوراک دولوپرها و تیم‌های DevSecOps که می‌خوان قبل از ریلیز، کدها رو با ایجنت‌های متنی ممیزی امنیتی کنن.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💎
دسترسی به مقالات و کتاب های
پولی خارجی به صورت کاملا غیر قانونی
https://libgen.im/
https://z-lib.id/
https://annas-archive.org/
https://sci-hub.se/
https://libgen.is/
دوتا اولی فوق العادن
😱
، علاوه بر مقاله، کتاب های پولی رو همشو داره. هر کتابی بخاین.
کاملا غیر قانونی
😂
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارسالی
http://64.23.188.133/v1
gpt-6-astra          ←
⭐️
تأیید هویت شده
gpt-5.6-sol
gpt-5.6-terra        ← سریع (۵.۳s) و باکیفیت
gpt-5.6-luna
gpt-5.5
codex-auto-review
gpt-image-1.5
gpt-image-2
API key خالی
سریع بزنین تا تموم نشده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7778">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU9SrM242W-PuMOQakp0lWmQKuNF0Xb_5mc3f7sLcTGxOIBm0v46OlB5jmebrXpLo_62Poe2Zuu8Xiq2Zxanbw38IEmiHMA57CzRU6XnM5YgNsOgiDH9-Skfv--9wa4JIgZSEl7suEqHjQo30rOzUyp3otVN_07YMuW9qzV5E6uJXP5KbMDYSp-XCvgZLMY-3ZXEkd8rT2SKoqlLB-fd77lW5rPiNaQvFb-21sgyTxNWzIeoN_8jtASVm2k-kR-Fy75aPODu3Yt0S-BEkLxJ_eEpg35vg-n8vHiKixeUMZFjCX8lYCIN6Cqumf85pccMwCdS8X4N8ELH51vO2k7hTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جنریت رایگان تصویر با مدل جدید GPT 2.5 SUNBURST!
بچه‌ها پلتفرم Weavy داره کردیت روزانه میده و می‌تونید جدیدترین مدل‌های تصویرساز مثل GPT 2.5 و حتی ابزارهای تاپی مثل Topaz و Magnific رو رایگان تست کنید.
✨
ویژگی‌های کلیدی:
🔺
کردیت رایگان روزانه:
فقط با اولین لاگین ۱۵۰ کردیت هدیه میده.
🔺
مصرف اقتصادی:
هر جنریت با GPT 2 فقط ۱ کردیت و با کیفیت بالای GPT 2.5 فقط ۳ کردیت کم می‌کنه.
🔺
محیط نود‌بیس:
دستتون برای تنظیمات دقیق پرامپت، رفرنس و تغییر کیفیت کاملاً بازه.
🔺
ابزارهای پیشرفته:
به ابزارهای محبوبی مثل Magnific و Topaz هم داخل محیط کار دسترسی دارید.
💡
نکته:
وارد سایت بشید، یک نود از مسیر image models -> edit image -> gpt 2.5 اضافه کنید، پرامپت یا عکس رفرنس رو بهش وصل کنید و ران بگیرید!
🔗
لینک ورود به پلتفرم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7778" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7777">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ajzi9zyLOjIUBJynJcgfgRDo7beYRLR2qcNIjXESPkvDod6eO-N-XsTqL-xxF6kpBUqDywP8Vld1_RovxDsrLsnVkPhdHFjuGo0bWhavpC-L_vxvSCKYuwNKva15TT4gqUvUpDutUFPG4JuH8RXlM3cFn9UzjxD_G5gxxkSmscOVs0smMZfEAw4W7AprXk7lAgniM3zji_FpNQmNAjbFvYlNpyIx9rh7EpP-MeJkD2EpjnFilImp1wPTpJjoB10jm9Pmmy8K5uNaAg-nwWUUr_ZQzrX12U4hxknScn5lNIPkZSJ4mVC0wlh4ym3-uAHk2v9MuhmIh1DHQNzV9iT4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
یک میلیون توکن رایگان GLM 5.3 Flash
برای دریافت
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7777" target="_blank">📅 17:06 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
