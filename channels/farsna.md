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
<img src="https://cdn4.telesco.pe/file/RT0Y9vEDMtXt0auRdWvIaSKaml12EhoownyGZce2DqM5mz336LwSiJuMv0L425Zd5r7PRyy71QxaSsNOFL0tXpFbxa_0HNQB3NyxJmufBZLjo6Q-MCCcNtPsHOaWydS4sRKWTv3Cs4pX24SA4pplzAoEVzulG0fka03fgo2likFgUzsIi6232vZ20Mry7w27YxjV8CKxOfSBOTYRItkdClZFcTZz06ppjJZaRiDUB34Qa_LKSmLxvBAPZxxUMa2Nv5tttUtxOhp_jywkklYRqi7RCPc7hvNqR-OLJhyzhhzVYvP2elKKNqrZKgqaytWEtg4oUDGZcOJpTCA_2iOh5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-436836">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a162fc100d.mp4?token=bf2sPjNxk5edQrZ1lb8c_0fw_uKSbdkMDQ1lfWjyoRc48aK-idnOQJy48GCP0xFPVuCOal-kQ8b_wt95gxfSEzEb4p5J3vCFS3V7GdMG1Khua_ntC4pvN-iLvqQz0-lxf4boQ--8Uj2rEl6OcDPcEhBqts8M54Cdz1xvHpOaUGMOiiudp4Vpp2MxqQ31yckPoR1eo01SmqXppiYJDpK030S4B47VZXUIKMBHOYCqyFCj5lS-IWGPHrcYtS4HHwuPpvFumvIHw5GQ1MAU0ipdQTSVKcj3J4_cbLF65uIQEsKH72cdLPJNul54y8rCwGRk5C1sgCOLA0htkt0aRI5rWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a162fc100d.mp4?token=bf2sPjNxk5edQrZ1lb8c_0fw_uKSbdkMDQ1lfWjyoRc48aK-idnOQJy48GCP0xFPVuCOal-kQ8b_wt95gxfSEzEb4p5J3vCFS3V7GdMG1Khua_ntC4pvN-iLvqQz0-lxf4boQ--8Uj2rEl6OcDPcEhBqts8M54Cdz1xvHpOaUGMOiiudp4Vpp2MxqQ31yckPoR1eo01SmqXppiYJDpK030S4B47VZXUIKMBHOYCqyFCj5lS-IWGPHrcYtS4HHwuPpvFumvIHw5GQ1MAU0ipdQTSVKcj3J4_cbLF65uIQEsKH72cdLPJNul54y8rCwGRk5C1sgCOLA0htkt0aRI5rWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: با روش‌های گذشته نمی‌توان بر همۀ مسائل امروز کشور غلبه کرد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید…</div>
<div class="tg-footer">👁️ 228 · <a href="https://t.me/farsna/436836" target="_blank">📅 14:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436835">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ساعت‌های سرنوشت‌ساز برای انحلال پارلمان اسرائیل
🔹
در بحبوحهٔ افزایش تنش‌ها در ائتلاف حاکم رژیم صهیونیستی به رهبری نتانیاهو و تشدید بحران قانون معافیت حریدی‌ها از خدمت نظامی، کنست امروز در بررسی مقدماتی، به طرح‌های قانونی با هدف انحلال آن رأی می‌دهد.
🔹
کانال…</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/farsna/436835" target="_blank">📅 14:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436834">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14687e4509.mp4?token=P0a9XJaH_4ZxtVXqKioZtnym7QRaCdC7Jnr93HuL8eJ_K0_vLWPkCyTXSnUvHsPmYofkwvEMOwSQQJZccmVmf44Vw6oshqZB83MG7Ub_xKAvkiAdbC-cMQ59iRUH2NmE1cAKkeLOKvykilZjma8nkUINBgCc4ERvhHSNSu6MMe3156euAMg-8qNDP6Qe9DD-ovkgSWRqx68Kg0MXvn3vw1eV1ILV-7lvcgOOi3L7Kww2lafrxDePCgYWLXWRk8229DGZgDEo3IAqCX4XythL9q7GIwEJzPpmbYn6h2bon4dAYIydGWqWum-JxSxQxx0W2WGFQwoq0c7jmI1q8Cm1TZDHdTJpindjvvz53_0VnDDi76AvlzBDlmvOgWQ3pTVXQOMaWn9AjVG0Zs_vcMPesVI-T9clR8PmWIyiEnWoBcUHWHxxjKDIiNKWijNR82nhrO1nhESg2hDeLoIWzfufgEiEn440BvuoEFW9Xi4J_LeBEZzlw5BgzcRQtXZ295cBNhZWRlem7z_muXJVvV4CcJuauL-LdDsAb706k8eFeoRrHWQdQeH4GQugBQgPmXDrxnrFXrDWfzSzdmOmecC-SyILNk0AhHtNyYYKEnQs4SP1n6YiVfibWOIpxqwPhzqU4lu5zhVj90ze4GVD2V_RRcOXGq27K3DH9HytiKC0-Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14687e4509.mp4?token=P0a9XJaH_4ZxtVXqKioZtnym7QRaCdC7Jnr93HuL8eJ_K0_vLWPkCyTXSnUvHsPmYofkwvEMOwSQQJZccmVmf44Vw6oshqZB83MG7Ub_xKAvkiAdbC-cMQ59iRUH2NmE1cAKkeLOKvykilZjma8nkUINBgCc4ERvhHSNSu6MMe3156euAMg-8qNDP6Qe9DD-ovkgSWRqx68Kg0MXvn3vw1eV1ILV-7lvcgOOi3L7Kww2lafrxDePCgYWLXWRk8229DGZgDEo3IAqCX4XythL9q7GIwEJzPpmbYn6h2bon4dAYIydGWqWum-JxSxQxx0W2WGFQwoq0c7jmI1q8Cm1TZDHdTJpindjvvz53_0VnDDi76AvlzBDlmvOgWQ3pTVXQOMaWn9AjVG0Zs_vcMPesVI-T9clR8PmWIyiEnWoBcUHWHxxjKDIiNKWijNR82nhrO1nhESg2hDeLoIWzfufgEiEn440BvuoEFW9Xi4J_LeBEZzlw5BgzcRQtXZ295cBNhZWRlem7z_muXJVvV4CcJuauL-LdDsAb706k8eFeoRrHWQdQeH4GQugBQgPmXDrxnrFXrDWfzSzdmOmecC-SyILNk0AhHtNyYYKEnQs4SP1n6YiVfibWOIpxqwPhzqU4lu5zhVj90ze4GVD2V_RRcOXGq27K3DH9HytiKC0-Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: قلب ما برای بچه‌های فوتبال است. دعا می‌کنم تیم ملی از گروهش صعود کند.
🔹
۹۵ درصد ایرانی‌های خارج از کشور بی‌نظیرند. نگاه به درپیت‌های اینترنشنال نکنید که می‌رقصند. آن‌ها برای ۲۰ دلار پشتک می‌زنند.
🔹
ایرانی‌های واقعی در آمریکا نگذارند کسی بیاید تیم ملی فوتبال را اذیت کند.
@Sportfars</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/436834" target="_blank">📅 14:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436833">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94271ae1b3.mp4?token=vOXFWF522DZdoPVt5v_BKUZp_BIocc0YePIeBBbEuaZCkVKEaL-ez2CgT-WlacAX1_IZzGvwtPr6Z6SuEPdSSvD7e7gA4KdSiILvJAHt1yQQCl3at694JRCdXYejvEoZrPFl0QxiNruBRSgveZ99gzK9v4lwI_QwBR6qZusguFZgm_XQiZEVdMWF0dffwA92kuusJRTSp4lRMPvfn09KlPwJ0yVzoypq6ZzkDlcSln7lmhjiv45KmIwDpS-AFiXLsuQCABlIYpWjnO3uh1M6D4owkDEs2lU5NlA_jOMLCA9Og6DJZL_7x3VzSae6ccP61KEbaG14Cbbc-0CVKkg8Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94271ae1b3.mp4?token=vOXFWF522DZdoPVt5v_BKUZp_BIocc0YePIeBBbEuaZCkVKEaL-ez2CgT-WlacAX1_IZzGvwtPr6Z6SuEPdSSvD7e7gA4KdSiILvJAHt1yQQCl3at694JRCdXYejvEoZrPFl0QxiNruBRSgveZ99gzK9v4lwI_QwBR6qZusguFZgm_XQiZEVdMWF0dffwA92kuusJRTSp4lRMPvfn09KlPwJ0yVzoypq6ZzkDlcSln7lmhjiv45KmIwDpS-AFiXLsuQCABlIYpWjnO3uh1M6D4owkDEs2lU5NlA_jOMLCA9Og6DJZL_7x3VzSae6ccP61KEbaG14Cbbc-0CVKkg8Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور شناورهای ملیت‌های مختلف به‌ویژه شرق آسیا از تنگۀ هرمز بیشتر شد
🔹
خبرنگار صداوسیما در تنگه هرمز: سفیدپوشان نیروی دریایی ارتش در عمق تا شمال اقیانوس هند آرایش و بازآرایی متناسب گرفتند و از این سو سبزپوشان نیروی دریایی سپاه در همۀ سواحل و جزایر برای دفاع در اوج آمادگی به‌سر می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/farsna/436833" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436832">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27322a441a.mp4?token=l8-mGeVpl1a_U7ZjFBVP7e8divUr8SvXxT7LHrg7mjshVv5lYwRPLgLHh5BlHr_cfKuToenuXA4VutNWyrRX59huH5SVmTBKiB7bV3uginxXO4l0Knmbq6YdgTdJ3Oie4BGZKYVVVEMFB_Jr7y-hYSqvwsntr7ngS6q0S8WaQcXhH6UHetYLizvKxu-B5wjsAVTvFOYdTY3qv70uQpwMXzilmfsNp4zejyLX4OcqtnBLSTFQy55_JLCAWZalKzewhKf-FG2AJH8loZyAZ8UlAS77E8bYEW2z9EP6eAjjVCXhLvHefBb6XUwcHWgxDCCEdMcuqK5znD4xPj4H8AHbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27322a441a.mp4?token=l8-mGeVpl1a_U7ZjFBVP7e8divUr8SvXxT7LHrg7mjshVv5lYwRPLgLHh5BlHr_cfKuToenuXA4VutNWyrRX59huH5SVmTBKiB7bV3uginxXO4l0Knmbq6YdgTdJ3Oie4BGZKYVVVEMFB_Jr7y-hYSqvwsntr7ngS6q0S8WaQcXhH6UHetYLizvKxu-B5wjsAVTvFOYdTY3qv70uQpwMXzilmfsNp4zejyLX4OcqtnBLSTFQy55_JLCAWZalKzewhKf-FG2AJH8loZyAZ8UlAS77E8bYEW2z9EP6eAjjVCXhLvHefBb6XUwcHWgxDCCEdMcuqK5znD4xPj4H8AHbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
🔹
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/436832" target="_blank">📅 14:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
🔹
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/436831" target="_blank">📅 14:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhnLQYgqwRlhA0od9xwcf9Lwg7YqNH5JNETIaMCVt8V8rnSJCng9YPc5Ih6iMrjJWto4Pn7VuNpjJYV2OLXZgjs5le1KE0DCOVTO49pawWo5rOF3ekw_hTyUP3HgLw-eHL8c5aQmKuaZruHgrSadXQrm2ZYFbl99IAABoKDjh6MyuFezfeYJNOlH890fuQL-62ZATZlQOuHTGDooMAB90URSAyDP8QS6TpTf1SknNfXNizWAJRHgNKsyhNZByQmAauiOhtj_mwyR5b14tHk3sw4KACQRJIdY4bRipBZsoxppnHmcl59vUZftrG390hj4lIUsWeifwxhZ1mea0jvlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تا ساعتی دیگر پیام رهبر انقلاب به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/436830" target="_blank">📅 14:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078eb7e4b1.mp4?token=cwikG9LSDzH_OpOvB_xMRPZ2UOo_Tuufa3V-I0cafk75R-rvgca6iGk0QxI3JRnomnJNRGdUljZGnSiu3Qmecjby8tuS4iCjFH2PVrIM_Ri7WKaF5IcrUtDCNcxvqCDqXWzVf-Cm3g8GUK989eHgYlTNzhe6Wkd0dDHYx2A4HWxW_iXyFe3NZhVTueHuTX6z9hDOY6llbmauixle08FX_J_1rmT4ACwC7Omk-Ybgb9IXcnRtgYCZ7KET9EtFTo00CIom5SSyZG921fCaKOl9QS6CEuhirX51Fqw1FuUNqKC8CLzNJ-FQVEYL3m1oXmnuI2Opr--aMSVClv1NwQXpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078eb7e4b1.mp4?token=cwikG9LSDzH_OpOvB_xMRPZ2UOo_Tuufa3V-I0cafk75R-rvgca6iGk0QxI3JRnomnJNRGdUljZGnSiu3Qmecjby8tuS4iCjFH2PVrIM_Ri7WKaF5IcrUtDCNcxvqCDqXWzVf-Cm3g8GUK989eHgYlTNzhe6Wkd0dDHYx2A4HWxW_iXyFe3NZhVTueHuTX6z9hDOY6llbmauixle08FX_J_1rmT4ACwC7Omk-Ybgb9IXcnRtgYCZ7KET9EtFTo00CIom5SSyZG921fCaKOl9QS6CEuhirX51Fqw1FuUNqKC8CLzNJ-FQVEYL3m1oXmnuI2Opr--aMSVClv1NwQXpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتکار ۱۴۰۰ تنی مرغ منجمد در شیراز
🔹
تعزیرات حکومتی فارس: در بازرسی از یک کشتارگاه در شیراز، ۱۴۰۰ تن مرغ کشف شد که از ابتدای جنگ تحمیلی در ۹ سردخانه احتکار شده بود.
🔸
یک محمولهٔ مرغ منجمد ۹۰۰ تنی دیگر نیز روز گذشته در شیراز کشف شده بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/436829" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436828">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJwFbjd6g8k9ia0LLOzh7lt0xZqKhajaHhfSL1xFTeo2a3Bjuq_MDa4UYkwzV1B69DB2o8CzsKNd_IGHA55YxOye4eJyKC2YObgQ6ZB-51gHEC-grQHs3UaDVeydAFrYcuVqQn_Qy1yfCeSBvzCS2npqK_EV7qZZDRso2efvuOFxsSPiOpED-F3rr_X2ZE5TjLQ2l0HY8vCfanDlc-1cO2HBkf_JmslYDWcmdCCZbblrYJ3fTtI3epgWEcNktIC3DlI6YuowWzAQ9KdEaZqOv8SNQ5aPCWKyomOUvNdLStaz7PkO09-caOqrfQzADdyMSbPVkqaKjZu2qDHyu3nTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس اولین روز بعداز جنگ را مثبت تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۲۵۰۰ واحدی به ۳ میلیون و ۷۱۶ هزار واحد رسید. @Farsna</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/farsna/436828" target="_blank">📅 13:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه: [رشید مظاهری] بازیکن سابق فوتبال هنگام خروج غیرقانونی از کشور بازداشت شده است
🔹
خبرگزاری قوه‌قضائیه نوشت: «در روزهای اخیر همسر بازیکن سابق فوتبال، در فضای مجازی ادعاهایی را در رابطه با همسر خود مطرح کرده است.
🔹
پیگیری‌ها نشان می‌دهد نامبرده قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از مرزهای غربی به صورت غیرقانونی از کشور خارج شود که در هنگام خروج‌‌ بازداشت شده است.
🔹
همچنین ادعای نگهداری متهم در سلول انفرادی نیز صحت ندارد و نامبرده در بند عمومی زندان حضور دارد تا به اتهامات او از جمله پرداخت رشوه به مامور دولت، فعالیت تبلیغی برخلاف امنیت ملی کشور در شرایط جنگی و اقدام به عبور غیرمجاز از مرز رسیدگی شود.»
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/436827" target="_blank">📅 13:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8f77da65.mp4?token=oFCpistVBZ-2VU5ICpUIo8zQC0-QuSHmhMAIb7GzP53WT_6OJfgiKGQ3_d6Zek-bOrkFuiB5WveAFQhL2SAmzYMDu6BUYOxAMLcYSXE_vYQpkxdOBnys6OOt3Xr87ZYA2vEn5zUZiRtQD1WGBcPQkPOXDSvyLqBjL5j8OE80cBfGd6heeuP2diIq9Pj8N29XJN-qsNayVe8162_Qnr4BxFqcq5BH5viIHJeKgLcdWxzaiQ4d6BLfbYkoIIooy9QZW3GigljQD-oU8cj6QlYUz7wuxo2EO6opRk7TSIDPjz4wwf57SHsYBsCS2GvXciAGG2Puqfta10NzwoQ3ppTpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8f77da65.mp4?token=oFCpistVBZ-2VU5ICpUIo8zQC0-QuSHmhMAIb7GzP53WT_6OJfgiKGQ3_d6Zek-bOrkFuiB5WveAFQhL2SAmzYMDu6BUYOxAMLcYSXE_vYQpkxdOBnys6OOt3Xr87ZYA2vEn5zUZiRtQD1WGBcPQkPOXDSvyLqBjL5j8OE80cBfGd6heeuP2diIq9Pj8N29XJN-qsNayVe8162_Qnr4BxFqcq5BH5viIHJeKgLcdWxzaiQ4d6BLfbYkoIIooy9QZW3GigljQD-oU8cj6QlYUz7wuxo2EO6opRk7TSIDPjz4wwf57SHsYBsCS2GvXciAGG2Puqfta10NzwoQ3ppTpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ویژۀ وزیر کشور: در صورت تعرض به ایران، باب‌المندب به معادلات جنگ وارد می‌شود
🔹
سرتیپ نامی: ۳ تنگۀ هرمز، مالاکا و باب‌المندب مهم‌ترین چک پوینت‌های استراتژی جهان هستند. تا الان بنا به‌دلایلی فقط از ظرفیت تنگۀ هرمز استفاده کردیم.
🔹
اگر زمانی مجبور شویم از تنگه باب‌المندب استفاده کنیم، قیمت نفت به بالای ۲۰۰ تا ۲۵۰ دلار می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/436826" target="_blank">📅 13:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmL62fDGFzOXJoJouvhXrmKPbPIRXdlVXTx0cyeXIATCRVP_h7oWQs8de__Pe7cm6pTZNHUhdVZO4IhO-0zTMtOvEXPxLmrp_IPZi9suqjUjhRCZDDQOLD5sYhFXWzKV-Naz6aolPvix8KjOh9BHMPNHY97oLYDjgBxVNsypGTp_LLh9idjXCLXFD13Tvey7_DsaGGVLE7KYbi-maJR1Vs1Ot-CPyNdaZVAmu0YVaxG1x9Cs3rjBmDi9vESTpsMnVb1azFKcVNRpaXgluj8-zgddf7Db5s1WATR8q0el-ShGw6dvmFMfitQzf6gXmWJbB31ZvKC3w3reD9p-DUbkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تا ساعتی دیگر پیام رهبر انقلاب به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436824" target="_blank">📅 13:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae425b97d.mp4?token=DIjCclr1PsknrZXXfIvmEWaGpyIRmPozhtEpHoB_O77Lw0Mx4YW5QL3zw91qA_0QgppIZz8Gh8vxzUlmgNWg053Gb5nA2Pdih56Buh86AVKnUm-Du1dXCKLogAJ8jJnfazLRffjgHZX85AjQlILIivNvrry8zGwnmyEnbJutHxBm-WYW1aHcnR3W5rmczXvUvdAiRlatfnWutv9_OPpJFyHnADwbHUv7wS111HzWkfnuOlPoPITBFK1Odmj-Yfui1MX2p6Inp5lwNrybvLzDGrpt6BnpcKxFjE9JzePIZhJWwhGhD04NoxXiukyVnDQuBJi2rhdjWonEvOhh_BV8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae425b97d.mp4?token=DIjCclr1PsknrZXXfIvmEWaGpyIRmPozhtEpHoB_O77Lw0Mx4YW5QL3zw91qA_0QgppIZz8Gh8vxzUlmgNWg053Gb5nA2Pdih56Buh86AVKnUm-Du1dXCKLogAJ8jJnfazLRffjgHZX85AjQlILIivNvrry8zGwnmyEnbJutHxBm-WYW1aHcnR3W5rmczXvUvdAiRlatfnWutv9_OPpJFyHnADwbHUv7wS111HzWkfnuOlPoPITBFK1Odmj-Yfui1MX2p6Inp5lwNrybvLzDGrpt6BnpcKxFjE9JzePIZhJWwhGhD04NoxXiukyVnDQuBJi2rhdjWonEvOhh_BV8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعجب زن اسرائیلی از حماقت سلطنت‌طلبان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/436823" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjDN2zP-mPdHC9l_ZlyCbBLyt2J0h0UUpLsQWCcb8k41vE5f8bRKpC-sVc9NEr9bI7ob73DXQySLT--EpNoDYFqqJdSMnnKVN754zppm0Ydh7BSwIIJM9MxB0a05-Mpq5Ps8PSSqyPDqm8rOGD7ZtM2yztjEhU0apS--Q5yyohZgmu8OMQXbX1Jg9UF_Y7o2HrWj6cNegTNdqdxyJuuKO8Ql7X4lthDP06tQrGopNupScyOLQzw3wwo1ZQhz-RDO6uF-EKWwkj2DF5D84hnU7gdH_k7mcby94uva5DKbhas7Iu8FZ052LVACgNvDdMNXorZAskH3zdjtYen5Etuabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علنی پرسپولیس سر سهیمه آسیایی
🔹
‼️
شایعات از احتمال لغو ادامه لیگ برتر و معرفی مستقیم نمایندگان ایران به آسیا حکایت دارد. باشگاه پرسپولیس با این اقدام مخالفت کرده و آن را غیرمنصفانه و غیرفوتبالی خوانده است.
🎙
یکی از مسئولان ارشد باشگاه پرسپولیس گفت:
🗣
ما…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/436822" target="_blank">📅 12:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1vqbOhE38yQq2PtEurDW_lGto9v8wvBCXgI9pc3ec4Gnr6LfSfbwc8IhcM24Pk6ES5kW9T92tmLe2FnhCr6KM4kMXEclv3rM80DWMpIqJuJiphirgdys1yRhGiMASOVSB8iwIThkRY03UBcnZOrobj3c7V_RxCEHVbV0quJE4Ctwv4NLmNGy-OGMFFFENLQ8apC6KA_5PCE2UyyOHmWW0rcCatzKmlHxiXV3PyfGLK9gtC8VjxsronSEuO4wShr5CXiaQ4N3-djXbBakrfSXV8yRJCN3KFqWRoGjee3iWorK7Y-0IesO0akod4iFt7gtHufVOI01J9VgppD_hVfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«درخشش روابط عمومی شرکت صنعت فولاد شادگان در جشنواره سلام خوزستان با کسب ۲ عنوان برگزیده»
🔹
روابط عمومی شرکت صنعت فولاد شادگان
در ششمین جشنواره «سلام خوزستان» با کسب ۲ عنوان برگزیده خوش درخشید.
🔹
این جشنواره با حضور ۷۰ روابط عمومی از ادارات، سازمان‌ها و شرکت‌های استان خوزستان برگزار شد و آثار ارسالی در ۱۲ بخش تخصصی مورد ارزیابی هیئت داوران قرار گرفت.
🔹
در این رویداد، روابط عمومی شرکت صنعت فولاد شادگان در بخش‌های «تولید موسیقی و ترانه‌های حماسی» و «هوش مصنوعی» موفق به کسب عنوان برگزیده شد.
🔹
آیین اختتامیه ششمین جشنواره «سلام خوزستان» روز سه‌شنبه ۲۹ اردیبهشت‌ماه ۱۴۰۵ در اهواز برگزار شد و در پایان از برگزیدگان این دوره با اهدای تندیس، لوح تقدیر و جوایز تجلیل به عمل آمد.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/436821" target="_blank">📅 12:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsrxsZvJZ-zRjc7jx8gq1yYRCbToIcFvLql5yA-U2h7NOYQqp5Mcjf3gKJZA2kf1spj6-H9ERNSg0jlRMnG6i9LgxAXWS7kER8iVuj6SBhNTiG1o4MQrzSXSUhXKn4sNAtiFSX4AV0FuLlf4oPeD_x45yyN6yTs3JQ3OjH6BSPcsYm_Bo3_6jp4KYRnGwmbA_atNqPsMYywI1s2fkHTwZTDSZ2fiDkuL50ky89AC0AFqLT-92Xk8OSRSm35sr2QEXcu77_WUhnnZJ7G0R-tfni_QXdaWXdItbomR0VH5FTabgbfz53n7YU5FTdD7GEbhtBKwMeXpG4028ADg1LPM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
سامانه فرارفاه بانک رفاه کارگران به‌روزرسانی شد*
🔹️
با هدف توسعه بانکداری الکترونیک و به منظور ارائه خدمات مطلوب و متمایز به مشتریان، سامانه "فرارفاه" (مبتنی بر سیستم‌عامل‌های Android و iOS) بانک رفاه کارگران به‌روزرسانی شد.
🔹️
"درخواست کارت رفاهی متصل به اوراق گام"، "خرید بسته اینترنت اعتباری یا دائمی"، "فعال‌سازی حساب کاربری" و... از جمله قابلیت‌های نگارش 1.5.6 سامانه فرارفاه مبتنی بر سیستم عامل Android و نگارش 1.17.0 مبتنی بر سیستم عامل iOS است.
🔹️
سامانه فرارفاه از طریق پورتال اطلاع‌رسانی بانک رفاه کارگران (
https://www.refah-bank.ir/fararefah
) در دسترس قرار دارد.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/436820" target="_blank">📅 12:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/436819" target="_blank">📅 12:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fe7d131d.mp4?token=u4shJ7VfCqCFk48-SBbpzr6Xjruo9cqiix5nAD2qwTsE93Ltwl1SvqYRwNDvffR8jO6DQbT0dJ-ojRp1OrHFXoqnvz1220DvIwZPfprgW5H7IuAaG6MYNm9qIzZkqxzhXPtli9DJCPHPZsa0S_sRWj6EI7zRxuw8u1q8yKlRAjMMX435rSu2j3hJYOguBkmonziC4wrCiJt2kkmDzMAq0abk0sNRDLDo4LEEZIC4oy7r-4qCVkLr_uLXkhXiqx4M3Tg_sgbd8_jKq5h-q3I1N0fZxtWIUWpWcLOWN5PBHF0Iw3wQlbCpoQf-DtEQoAk43F1AFmCZoMo4Qo9WUM4u3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fe7d131d.mp4?token=u4shJ7VfCqCFk48-SBbpzr6Xjruo9cqiix5nAD2qwTsE93Ltwl1SvqYRwNDvffR8jO6DQbT0dJ-ojRp1OrHFXoqnvz1220DvIwZPfprgW5H7IuAaG6MYNm9qIzZkqxzhXPtli9DJCPHPZsa0S_sRWj6EI7zRxuw8u1q8yKlRAjMMX435rSu2j3hJYOguBkmonziC4wrCiJt2kkmDzMAq0abk0sNRDLDo4LEEZIC4oy7r-4qCVkLr_uLXkhXiqx4M3Tg_sgbd8_jKq5h-q3I1N0fZxtWIUWpWcLOWN5PBHF0Iw3wQlbCpoQf-DtEQoAk43F1AFmCZoMo4Qo9WUM4u3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحلیل‌گر مسائل ژئوپلیتیک: بازگشایی نظامی تنگهٔ هرمز غیرممکن است
🔹
کمپف: نمی‌توان تنگه هرمز را با توسل به زور بازگشایی کرد؛ همه دیگر توهم تغییر رژیم، سرنگونی حکومت و امثال آن را کنار گذاشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/436818" target="_blank">📅 12:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa09da100.mp4?token=vyNfJjyUxS6j1rSmVBFv6U8EH4llmcmy8bSO7bFiJvigGmHprMn1TL4zAHbgSi1ttt9rbYBFtgJLox-70H1ZPmxNRUiomQch_UBsPldHvfIprr4JJQ7uaNACfQOO2-RqMmbY2PJP1RawGVRHA9xNKrtcEhw570xc_Wd7ToYanHGIILYHtnL8JieWQCSsB75eLnnftpm2tytH5zvfg8JKyZvPv4hbw4IidYUgrN6hH1GK-9pj06ULl1yOBilX9YTgcT-ilXjP8nFwS7hV7bWL53sG4wHcmsMIQeqIusbqufzCuqmbdBx6gNSwzNgNmz1vHxiGOEzcwkW0V-N6sXQpDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa09da100.mp4?token=vyNfJjyUxS6j1rSmVBFv6U8EH4llmcmy8bSO7bFiJvigGmHprMn1TL4zAHbgSi1ttt9rbYBFtgJLox-70H1ZPmxNRUiomQch_UBsPldHvfIprr4JJQ7uaNACfQOO2-RqMmbY2PJP1RawGVRHA9xNKrtcEhw570xc_Wd7ToYanHGIILYHtnL8JieWQCSsB75eLnnftpm2tytH5zvfg8JKyZvPv4hbw4IidYUgrN6hH1GK-9pj06ULl1yOBilX9YTgcT-ilXjP8nFwS7hV7bWL53sG4wHcmsMIQeqIusbqufzCuqmbdBx6gNSwzNgNmz1vHxiGOEzcwkW0V-N6sXQpDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار فرمانده سنتکام از پاسخگویی دربارهٔ جنایت مدرسهٔ میناب
🔹
خبرنگار شبکهٔ اسکای‎نیوز خطاب به فرمانده سنتکام: تا کی می‌خواهید پشت این ادعا که «تحقیقات ادامه دارد» پنهان شوید؟
🔹
تیمی از شبکهٔ اسکای‌نیوز همین الان در میناب هستند. آنچه آنجا رخ داد را دیده‌اند. هیچ مدرکی دال بر وجود پایگاه موشکی در آنجا وجود ندارد.
🔹
تا کی میخواهید پشت این ادعا که تحقیقات در جریان است قایم شوید؟ حداقل بگویید تحقیقات چه زمانی پایان خواهد یافت؟
🔹
فرمانده سنتکام به‌جای پاسخگویی مسیر حرکت خود را تغییر داد و تلاش کرد با کمک محافظانش از دست خبرنگار فرار کند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/436817" target="_blank">📅 12:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da05Mgi9PDMbg6QlgEh5RujgZ2Ges4n11dXmLhyJq-N4YFzN5KhWCF_K0H-H9BdOyZgiP5ophdClZRvBpnwWaDAN-AnHThLVGNq5qjxPBSeREgSn-B_0PdHuOgJHmxxRgYOUC4sOBIClnTe_rrc9XHbDcxQKWqOMhVD5H4UVOLjz1wyY2RV82IQarxjBelvvZh9i7WFOaRQBGc7QZCcZP6T556BaN23QQ_nziG7jt5q6xPTpBulKG9A9Nj7Iw4xor-oDuXoashUE7yhAWJrBMsMwx_xV9uSz4TfqHRcIW3E-iwOpDfTOkKRggcjkUweR1FjhdA16iCZYEn7GOOchNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/436816" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436815">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس نوجوان‌</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0486d5e9bd.mp4?token=scblDeOmmDFKYLaESSU8fh6HvGomkR4ZZyvv_7f8zJvJ_w5uTZ-B90mvK3tmv_D75vlgJariWBkdMvFzvh-EuBsV494bYFFm-bErJXCbqbl8DZZsAPZHoevZ4Gl3dfyzDhQ9WBlWMY0bNpFl1EcpkZi6N9L5q5tdQQ2Pnl_FDL-Y335JtelVHMkfimb-SrWPfgnp84a56jQ8273wLZ-vJAlpZjVxT8SiXu2FCdxNN1KlxVRJQdoDBgbFM5CwEwFke9sZKaIZIrgqhnqq2aGIr6jpQgGdNOvhakLbsw1GEiFtpkFI8i69zWgJsNhXxWPaC2p8OctV0GbaHBbtsb_nBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0486d5e9bd.mp4?token=scblDeOmmDFKYLaESSU8fh6HvGomkR4ZZyvv_7f8zJvJ_w5uTZ-B90mvK3tmv_D75vlgJariWBkdMvFzvh-EuBsV494bYFFm-bErJXCbqbl8DZZsAPZHoevZ4Gl3dfyzDhQ9WBlWMY0bNpFl1EcpkZi6N9L5q5tdQQ2Pnl_FDL-Y335JtelVHMkfimb-SrWPfgnp84a56jQ8273wLZ-vJAlpZjVxT8SiXu2FCdxNN1KlxVRJQdoDBgbFM5CwEwFke9sZKaIZIrgqhnqq2aGIr6jpQgGdNOvhakLbsw1GEiFtpkFI8i69zWgJsNhXxWPaC2p8OctV0GbaHBbtsb_nBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر دوستمون تو ایام جنگ احساس ناامیدی و شکست داشت وظیفه ما چیه؟
به نظر شما چرا بعضی ها نمی‌تونن واقعیت صحنه جنگ رو ببینند؟
جوابش رو اینجا بخونید
.
@Fars_Nojavan</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/436815" target="_blank">📅 11:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436814">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeQXVz1vwaWydDDZ3tf-HwVH7t13FF903OKbwEoZF0PDXR6KxumeOXy6yjCTtiJOuBDeaa2GSmfbvTrXVZ3I77f6yw2UfzpDLLL46IMhu45CLj-y12Xlk6Tf3z0EFSpJpBsfD0HE-PqVNfYoxKK19S5mYhco09xujRqk0a9cL7c35SV9sd3LkD0bDjijy8OFqbzF9L_I0Fk_hIaFQWLi7eREYjzC4xXj0VjFxPz-KOgY6BbsxwI0nQ04s_teU0OYSaJEXfOWKFC53xEGCXRRSZPkOVfWRPowxBlB9Wq9bKlhQJIynx2TAbG10WKzmZVs0lprf2FIXyUdaRiBj4vQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبهٔ جدید قیمت چای اعلام شد
🔹
براساس مصوبهٔ جدید کارگروه تنظیم بازار کالاهای کشاورزی، تشکل‌های مرتبط موظف شدند با هماهنگی سازمان حمایت، قیمت انواع چای را به‌صورت دوره‌ای تعیین و اعلام کنند؛ دولت همچنین بانک مرکزی و وزارتخانه‌های صمت و راه را مکلف به کنترل بازار چای کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/436814" target="_blank">📅 11:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436813">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiwIlKZqCCa6Ku0qdb8Q3ZcVKb98RLLEGa5834EhvtUIkc9hZUy4-J-Pgv7EjtUgFlsmpZGzEQyU8CPfOHt3slz-ybVEUOBNsQGZzRLNzlEwvLBTScGcgM1QC3fgWvMUcHgGQ-Zb6nnpAX09VoveSPlIIH4Ygh3qyeWGjqUsltoy4nhhYQqR4R2Sz3LIuknUz-_FppRiOExema1utTXTQuH5xmqrAItz0dS1O7-X-eiQHeeKZ_0RK_Ap8TO8YCBXkszfKcP92QNaVbzcbVMx_JpnHVfj1wcMmn6EX1umFbbmcL8zPIMGVeEt6-CyEzZUObLNP9P_vHgQEN_0PPa42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شی و پوتین حملات آمریکا و اسرائیل به ایران را محکوم کردند
🔹
رئیس‌جمهور روسیه ولادیمیر پوتین و همتای چینی شی جین‌پینگ امروز در بیانیه‌ای مشترک حملات نظامی آمریکا و اسرائیل به ایران را محکوم کردند.
🔹
در این بیانیه آمده است «طرفین اتفاق نظر دارند که حملات نظامی آمریکا و اسرائیل به ایران، ناقض حقوق بین‌الملل و اصول اساسی روابط بین‌الملل است و به‌طور جدی ثبات در خاورمیانه را تضعیف می‌کنند».
🔹
دو طرف در بیانیه مذکور، بر ضرورت بازگشت هرچه سریع‌تر طرف‌های درگیر به گفت‌وگو و مذاکرات با هدف جلوگیری از گسترش دامنه درگیری، تأکید کردند.
🔹
آنها همچنین از جامعه بین‌المللی خواستند موضعی عینی و بی‌طرفانه اتخاذ کند، به کاهش تنش‌ها در منطقه غرب آسیا کمک کند و به‌طور مشترک از اصول بنیادی روابط بین‌الملل حفاظت کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/436813" target="_blank">📅 11:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436812">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjLL6LocSXjjw8ujAxiQPEt0pBqQnOI1ZXTEJ2KihcPj-cHFVWbBDppJyxdRC0ThWtkT4krOjSxj9U_sNcidHxETXqLPEHcGrcPVK_0bS0a8XC3tEvbI9KtTgL4Q9kOzAOHGcACIBBk7L_Vmt2pAEXgDf1YT6tkDtG82gudr6g6QThcEhzEGl7cE_BAsT7ciqwkEXiqYm73yzL-8wk-VQyVMK-g5B7bwbEGNrRBvWq9jiepx9JF1aVQfIdilBY0JY1TAwzwL8WJ4OtYBrT6tWqXdxYq-pYtcKLWI0vUgrcB-fp77k5uHFF4A06ARij9aVAgijtS4oKBDoMYMChY8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشخاش به مزارع ایران برمی‌گردد؟
🔹
شهریاری، عضو کمیسیون امنیت‌ ملی مجلس از بازگشت دوبارۀ خشخاش به مزارع خبر داده و گفته «خشخاش ارزآوری خوبی دارد».
🔹
سالانه ۴۰۰ تن تریاک برای تولید دارو‌های ضروری نیاز است که به ارزش ۷۲ همت و عمدتا از کشور همسایه وارد می‌شود.…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/436812" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436811">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkrAxqZoym1ucVtrjzTb_knN6avyxAUkrMrOTEgHVoe5sDyvNChvJktKxNg54_bozjrQV9zb34bgKBUIVVYYrLjZ0G9MToGCtvPqRHlwPRMG2zcY7_IHx5JBQ_5x4zxSJl0o433qv0BxW6qLaSkmOtibBK4KFRRJEyH5ntP5U-cOzFeJvT0shlIdGxBwhSbQ6sI2Yc9Tm--cbySX2XnA0wsKg_dH818uQLe8X81Kq_-Hkpd_nDpnHbDhbN4NLrpOad0clC1UlI18yNxliPpE2KoS2Fcd6_J5_4xGhMlhL6LYcLCKTtlEb-slvFI6SiytITg2_Tu9F8nnszP47KMy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اپوزیسیون اسرائیل: روند انحلال کنست را آغاز می‌کنیم
🔹
یائیر لاپید در شبکه ایکس نوشت: «با همکاری سایر جناح‌های اپوزیسیون، اخیراً تمام لوایح پیشنهادی را از دستورکار کنست (پارلمان رژیم اشغالگر) خارج کرده‌ایم. در غیاب اکثریت، ائتلاف قادر به تصویب حتی قوانین…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/436811" target="_blank">📅 11:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436810">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoYSskMuQeo3G3AAwReidsjY8qrFX8MLrkeqAoiLN12eYY5WbFGNPzW-OkILLESm2_cKXAxS_bgifVUMmZW-td0qiBfb5le9g8ujM8NvLu89hu9SWjXg2ZYoZCIRof9Ux9TB8PNZ4mDnxSuFx3RgVMSV8xrQYGYjNe5Tedm3IGY1hmcYN8lzI1ZpIPzJFP5DEbiSsUbXrjFRMdwrmakdZtqOgT5djUG6DmKV1dPrZ79roAMvg95A31s78KlYqkfWRRgl2VZqlBaC0SM59Rx9UeqRqjqrLoVRjaQGtAmMN4jodUgkXRvMZBcufJB6VsGvVj3aFaOIAgAVa99v8GcB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا: شهید رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد
🔹
پیام سرلشکر خلبان علی عبداللهی به‌مناسبت سالروز شهادت آیت‌الله سید ابراهیم رئیسی: آنان دل در گرو مردم داشتند؛ ساده زیستند، بی‌ادعا کوشیدند…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/436810" target="_blank">📅 11:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436809">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
حزب‌الله: تجمع نظامیان و خودروهای رژیم صهیونیستی در شهرهای دبل و رشاف را با حملات موشکی هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/436809" target="_blank">📅 11:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436808">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTJcqX7o7EszH-4gkJRA-FV0-ZuCV59yjUldkGx125xzr4VqsnFlrV0BOZB3VzmyRWA5f2lz7lnxPBVIf43NabgxiOD7Yn-ctR7nr5_5haVe_wPfFz0hS7O8MtT-gqN7ZxjYk1Ce5i8aqiNcX5Wk5qW7QfLiFui1iOhHxNNbE9zgQgxY-KGaqyC9HdHyaue0wJTw3IwEOYC5gBwCHkVQ85H51Ejk-UkxoAd7P7ZTgQs8XX0iLHkGQkR1BL2wDpjLQ0PAEfx7SMZsOaunvWjzou-x_u19aV5HsPKTRwo0D34srcS4yvBKiDeW0kWXUW_cw5iYJhpoNsvXv7uF3yFdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
۱۱ بسته تخفیفی انتشارات فارس؛ فرصتی استثنایی برای خرید کتاب‌های رسانه‌ای
🎯
انتشارات خبرگزاری فارس در هفتمین نمایشگاه مجازی کتاب تهران، با
۱۱ بسته موضوع‌محور
و تخفیف ویژه مهمان شماست.
📖
این بسته‌ها شامل حوزه‌های تخصصی و عمومی:
✔️
آموزش رسانه | روایت‌گری | خبرنویسی
✔️
خانواده و رسانه | برنامه‌سازی | تدوین
✔️
دولت هوشمند
✔️
جریان‌سازی در آمریکا و ایران
✔️
صهیونیسم‌شناسی
✔️
علوم شناختی
✔️
تاریخ انقلاب
🎁
مناسب برای دانشجویان، اساتید، فعالان رسانه و همه علاقه‌مندان به کتاب
🛍
با قیمتی مقرون‌به‌صرفه، کتاب‌های موردنظرتان را راحت‌تر تهیه کنید.
🛒
نحوه خرید:
🔗
لینک خریدآنلاین از سایت رسمی نمایشگاه
https://book.icfi.ir
📌
روش‌های خریدکتاب از انتشارات فارس:
🔹
ارسال پیامک عنوان کتاب به شماره ۵۰۰۰۱۶۷۶
🔹
تماس با ۶۶۹۷۳۹۹۶ و ۶۶۹۷۳۹۷۴
🔹
مراجعه به سایت
انتشارات خبرگزاری فارس
🔹
حضوری: خیابان انقلاب، روبروی دانشگاه تهران
✅
انتشارات فارس مرکز جامع کتب رسانه
#انتشارات_فارس
#نمایشگاه_مجازی_کتاب
#بسته_تخفیفی
#کتاب_رسانه</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/436808" target="_blank">📅 11:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
🔹
بیانیه سپاه پاسداران: دشمن آمریکایی‌صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پرهزینه‌ترین ارتش‌های جهان هستند به ما حمله کردند اما ما همهٔ ظرفیت‌های انقلاب اسلامی را علیه آنان وارد عمل نکردیم.
🔹
اما اینک اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این‌بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبندهٔ ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.
🔹
ما مرد جنگیم و قدرت ما را در میدان نبرد خواهید دید و نه در بیانیه‌های توخالی و صفحات مجازی.
@Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/436806" target="_blank">📅 10:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">افزایش وام ازدواج و فرزندآوری در بودجۀ ۱۴۰۵
🔹
سخنگوی کمیسیون تلفیق بودجه از افزایش ۱۰۰ همتی سقف تسهیلات ازدواج و فرزندآوری خبر داد.
🔹
بر این اساس سقف این تسهیلات از ۲۷۰ همت به ۳۷۰ همت در سال ۱۴۰۵ می‌رسد.
🔹
هدف این افزایش، جمع‌آوری صف حدود یک میلیون متقاضی…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/436805" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8vGUTZOJdEdIPTiHlXHozvQ1C0OmKBrtQAeyMRk1mXZ2mo4FNUrIaKkeBQmjrPcq7xE8WcWk1Dd0bomrQ9dYra1FOwRzk6TGj850M0b9JuBc-uhWTVD2Ls2YzjWJCgUPfB-ZaEzLnBrjId424hmHy6HsfoixDuU9Q1rDX2D-ghXpXKrc7YEVqod1Dv5H5e6sWgVmwq2SUaa-_z2d_9I06FlnKkGlLTqdpkENc8IGvyYRXUhLefPy5qSVYNDplnDo4an0hw8D3m0Nls9502eK9spdcgfzrpXFbLzkf3tA5phYCwXv93jx52b0ubUwGwtgOhLLHH-LJcGlwgtee2lpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
همکاری همراه اول و پژوهشگاه زلزله برای توسعه هشدار سریع
🔹
همراه اول و پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با هدف تقویت زیرساخت‌های ارتباطی در شرایط بحران و توسعه سامانه هشدار سریع زلزله، تفاهم‌نامه همکاری امضا کردند.
🔹
در قالب این همکاری، از زیرساخت‌های ارتباطی همراه اول برای انتقال داده‌های شبکه‌های لرزه‌نگاری استفاده می‌شود و پژوهش‌های مشترکی نیز در حوزه هوش مصنوعی برای بهینه‌سازی زمان صدور هشدار انجام خواهد شد.
http://mci.ir/-F4RHS6
@mcinews</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/436804" target="_blank">📅 10:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#ببینید
منطقه آزاد ارس؛ تسهیل‌ گر تأمین کالاهای اساسی کشور
در شرایطی که سرعت، دقت و هماهنگی در زنجیره تأمین بیش از هر زمان دیگری اهمیت دارد، منطقه آزاد ارس با همکاری دستگاه‌ های اجرایی و فعالان اقتصادی، نقش مؤثری در تسهیل واردات و ترخیص کالاهای اساسی ایفا کرده است.
کاهش هزینه‌ ها، روان‌ سازی فرایندهای گمرکی و حمایت از واردکنندگان، گامی مؤثر در مسیر پایداری تأمین اقلام ضروری و تقویت امنیت اقتصادی کشور است.
#منطقه_آزاد_ارس
#کالاهای_اساسی
#تسهیل_واردات
#گمرک
#اقتصاد_ملی
#حمایت_از_تولید
#زنجیره_تأمین
#ارس</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/436803" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436802">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/436802" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436801">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085abd4b23.mp4?token=A9CoDG50RB4l1fVvz74xtm9Pf6H80hQ03V6YK_bxrzz8dIt49oNkU0MMo8joU5qWEVt89csTDZ6j-3LSgQX_5mQlHyZTo7e2rxevYjHUQwCpawjoP3osjb1P9IajweRL2NTcHIo8kGdbJVdVygMb5Z7Xxy2wbG7tk6-e4FoLBIcR_TqWu4W26ayufTpi1ivSsCUVFRSt3qS6S6MWvxISHSah8PsOUuybdiFSoYBYYpQPFAGpNCTbJqiWNebbp5VkXTwmBi07kn7Xw-wJZ4xj-a0tK_v_gNk27Ju3kVpGksdWCXhoyW-jb8YX5MULemMqc_9NdCEFGdtVac69Fz_dLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085abd4b23.mp4?token=A9CoDG50RB4l1fVvz74xtm9Pf6H80hQ03V6YK_bxrzz8dIt49oNkU0MMo8joU5qWEVt89csTDZ6j-3LSgQX_5mQlHyZTo7e2rxevYjHUQwCpawjoP3osjb1P9IajweRL2NTcHIo8kGdbJVdVygMb5Z7Xxy2wbG7tk6-e4FoLBIcR_TqWu4W26ayufTpi1ivSsCUVFRSt3qS6S6MWvxISHSah8PsOUuybdiFSoYBYYpQPFAGpNCTbJqiWNebbp5VkXTwmBi07kn7Xw-wJZ4xj-a0tK_v_gNk27Ju3kVpGksdWCXhoyW-jb8YX5MULemMqc_9NdCEFGdtVac69Fz_dLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود ۱۵ اتوبوس ۱۸ متری تازه‌نفس به خطوط تندروی تهران
🔹
مدیرعامل شرکت واحد اتوبوسرانی تهران: با پیوستن این ۱۵ دستگاه به ناوگان، مجموع اتوبوس‌های جدید وارد شده به ۵۰ دستگاه رسید.
🔹
از مجموع قرارداد اولیه، تاکنون ۱۰۰ دستگاه وارد کشور شده و مراحل عملیاتی شدن آن‌ها طی شده. همچنین ۵۱ دستگاه دیگر الان در گمرک بندرعباس مستقر هستند که به‌زودی به تهران منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/436801" target="_blank">📅 10:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">iran</div>
  <div class="tg-doc-extra">Hesam Seraj</div>
</div>
<a href="https://t.me/farsna/436800" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔸
وطنم ایران پاینده مانی
🔸
به رهت بنهم سروتن، دل‌وجان، تا زنده مانی
🎙
حسام‌الدین سراج برای ایران خواند
@Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/436800" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktkk2V7CchRX7VTUYVkzyCW7h-1kFTR8RFy7aJSxh4g5-LZQGgaZX7tB_1gY4gSbVD5i8dnvjGmw-QuarCDHubdTk7WP3_UBUca2mCLjEJV_v7xgGuL_veY2NYQnj4kxnCzSNcwymigv8ucVxIHecdmHTUsZR3k343lV20wgku4mFJFhX2ijH-2HBI6mzh-QaimhSKyCC2oCAZTOVyRAbBAgstVMiE9KwQ4ItjwHTYrTa-ywdCn4kDAZ2483fk9hWSoSk5__xFQPrmX7W8Jt4QauCyPATpxZ6APqQrGeDFrQQjneEcBc2Q83_UYd_czaqee56X3VpyQdGlgNm50Axw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا: شهید رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد
🔹
پیام سرلشکر خلبان علی عبداللهی به‌مناسبت سالروز شهادت آیت‌الله سید ابراهیم رئیسی: آنان دل در گرو مردم داشتند؛ ساده زیستند، بی‌ادعا کوشیدند و در سخت‌ترین شرایط، امید را در جان جامعه زنده نگاه داشتند و   همچون مردانی بودند که مسئولیت را امانتی الهی می‌دانستند و خدمت را والاترین شأنِ مدیریت.
🔹
خادم الرضا شهید آیت‌الله رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد و منش مدیریتی او بر سه ستون استوار بود:"عدالت، کارآمدی و مردمی‌بودن"
🔹
شهید رئیسی عدالت را در توزیع فرصت‌ها و توجه به اقشار مختلف جامعه جست‌وجو می‌کرد؛ کارآمدی را در پیگیری مستمر امور و حضور میدانی معنا می‌بخشید؛ و مردمی‌بودن را نه در کلام، که در رفتار و سلوک روزانه خویش جلوه‌گر می‌ساخت.
🔹
شهید رئیسی نشان داد که می‌توان در بالاترین سطوح مسئولیت ایستاد و در عین حال، فروتن و پاسخ‌گو باقی ماند.
@Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/436799" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
روایت احیای واحدهای تولیدی و کارخانه‌ها توسط شهید رئیسی
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/436798" target="_blank">📅 10:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadf181797.mp4?token=fzMALwRcsemEGMNO3VC4GlPgm9S_q-ZWo_OPmP26fPn7W8-YyvBpGiDsu0ugngOJe8HEvASpVocjWxnYXkDVfVuFiIDBt5adom6Dwba5Ceyqg3Z1uyw8lvAxZv-5UNBtVOPoZNIagOXsQUpbpQPdv6GEPZXyULYwToJ2qIvkv_FWOZ9Bhv3WleeHwEYBM1NNIF5m3FoG4n10x9FDhtCo2KXDbLwquJ7u_vyNUh-kzK-paWY484E0Z6JY4oiKn56UJ5XIYqa0ThrZpt11Obr5WaT_zEeTQaEIwr1196V30dJJpgLvCsWK8PxKZkOwR83-jyuYfMdGwfSBON-woyxnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadf181797.mp4?token=fzMALwRcsemEGMNO3VC4GlPgm9S_q-ZWo_OPmP26fPn7W8-YyvBpGiDsu0ugngOJe8HEvASpVocjWxnYXkDVfVuFiIDBt5adom6Dwba5Ceyqg3Z1uyw8lvAxZv-5UNBtVOPoZNIagOXsQUpbpQPdv6GEPZXyULYwToJ2qIvkv_FWOZ9Bhv3WleeHwEYBM1NNIF5m3FoG4n10x9FDhtCo2KXDbLwquJ7u_vyNUh-kzK-paWY484E0Z6JY4oiKn56UJ5XIYqa0ThrZpt11Obr5WaT_zEeTQaEIwr1196V30dJJpgLvCsWK8PxKZkOwR83-jyuYfMdGwfSBON-woyxnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین: جنگ در خاورمیانه باید فوراً متوقف شود
🔹
شی در دیدار با پوتین: اوضاع در خاورمیانه در مرحله‌ای حساس قرار دارد و به گذار از جنگ به صلح نزدیک می‌شود. خصومت‌ها باید فوراً متوقف شود.
🔹
دستیابی سریع به آتش‌بس عاملی برای کاهش موانع پیش روی تأمین انرژی…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/436797" target="_blank">📅 10:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhbO5TtEEPZkkFgHT0tWzHF1cKhDo3qHHWFwQlN8cXA0mOu8KpjnxqKol9uJzF9TCOEtepQvKi294DL9mbBeTulO5JQzjZpmXhWuBkhIG9FHUmjcvM-vU9vH_VfmoSIA1HnZ_RQDxd-Gu81iObmfub37Y-zvLZj3m3i_edLrrX0LmSDVhMhs6I2qHxgrB-uIBArCQKoywRkBdpEYKV_p4MXGl89Bprg7Cc5CC_H60Vz883FQtOQPDLfYJOxvTkJZLnlo75VDXa5B-RDKnmxm3yLbliLIN-K_di3cnjLDbCyi8kdr0aFYsOTXBXVUO9rxY1X0aZDfODVHcvN9lVXumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور کیفرخواست پروندۀ قاچاق خودروهای تویوتا در گلستان
🔹
رئیس دادگستری گلستان: برای سه متهم پروندۀ باند قاچاق سازمان‌یافته خودروهای تویوتا کیفرخواست صادر شد. پرونده برای صدور رأی به دادگاه انقلاب گرگان ارسال شده.
🔹
متهمان خودروهای تویوتا لندکروز و تویوتا هایلوکس را عمدتاً از مناطق مرزی کشور به شکل قاچاق وارد می‌کردند و مشخصات و اسناد خودروهای فرسوده و قدیمی را روی خودروهای جدید ثبت و سپس آن‌ها را در بازار به فروش می‌رساندند.
🔹
در رابطه با قاچاق سازمان یافته خودروهای تویوتا، سه باند دستگیر شده بودند که پروندۀ مربوط به ۲ باند دیگر همچنان در دادسرا در حال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/436796" target="_blank">📅 10:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaWe5G1FwXHgsv24cRUmIhfsfFooMaDT5Hvt56qnWWPGKZ2prXk1UuNt1J_E9HCVwfb_kUk2R4KsykWf43J5p-ZO0cfG7FIDdN6wiWTzdoUa-nfTeroT17jjzd4ovN75DdWRTOgE3xGcT6JAithDLDn8eVDJlF4NtSYdi_kcANyXBoUcbckj8ZH5WeZQnRTIb0PXrHav67bNBYgiMqO6LRKosDm2M_VMqq__3nzygPEbdJODQAZ-Akea7JWW_ZSJTOIl77XaZN1rtAqMkVWO6_mrD-hwa2ak_vuIP28nPeQjsTTm8teijFyGfS4CoDxLkoAuK9uH0bxkC17uwlwtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ راهکار برای کشیدن افسار افزایش قیمت لبنیات
🔹
بازار لبنیات این روزها در تب‌وتاب افزایش قیمت‌هاست. برندهای بزرگ طی هفته‌های گذشته نرخ محصولات خود را بالا برده‌اند و برخی دیگر از تولیدکنندگان نیز در صف انتظار برای اعلام نرخ‌های جدید هستند.
🔹
در سوی دیگر، اتحادیۀ…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/436795" target="_blank">📅 09:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجار پهپاد حزب‌الله در ساختمان محل حضور نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری گزارش دادند، یک پهپاد انتحاری متعلق به حزب‌الله که با فناوری فیبر نوری عمل می‌کند، در داخل ساختمانی در جنوب لبنان که نیروهای ارتش اشغالگر اسرائیل در آن سنگر گرفته بودند، منفجر شد.
🔹
این انفجار منجر به زخمی شدن فرمانده لشکر ۴۰۱ و تعدادی از نظامیان شد که با هلیکوپتر به بیمارستان‌ها منتقل می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/436794" target="_blank">📅 09:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkrQKl5TC3MhR_TDGK7q-WS4a3C6TuHRxf9CMHCYb8z3bGFQBAcyKUCW-J5MIZrmbh04YqB85wPq1Ev_xap228lL-nT96BZJK6j1UWr_xXlsbiertxkxUTpM-rST3oYFM-QfE22veLFhJqH7fdbCSnomPxUwm6hwfdco4xa_PnKb1C0qx1R8iaIXRq0bHrRDXsJeqTR38QB2PMROEdwrYKwBIIEsLFKFle3zfosMYbT9PDaaHpTcWHXrFLaJklJbERZu9-jWZE2tgR95syxLANJad31K8gkOwItJxa8dXiGmx6kBMNLIlIqr3LXUScLi_-qJT5PDpQOtMqiWKN5ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6qGhEZFqKVuYiQ0wF68vJAhc-pVjlcIgRjYpE_hh8RxjMNZ2tYIU8Mbxvt2-ce3cvwPZkEArZES5jqi-D7abuVv6I8ntjp_9zMo6XA4Eu0LQdNVp8SEAdhLWrB5dsrxJK-8SgiAbJBAFbfhV3EeIBs37h-oAIPy8BHR4S8G9B4_iIC4e55T7PmgAwV3Ddz_ePcYVfR-KV22axf2A8vqKyRoed9kWY8wSU3x39MojeRp4OQ6E5GbgZ9EniXzVLyUJFF41vJPREGJUpelA1GN-8oiKH1g8T-cFDL1xDoXaC6UJbqHJeLQic7kACPvOfAtgJi5qDpDMX0QFJC7a9-Q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXWPiIs3UnVQ0RAQXIiU4KIguBZ7H_snrZ64BOnKJi2dsV4Qn19E3h2kT40MjUO0WVNHvV3FdaJHBxCySfRdySY8awE8Q2B4vSuo6-UNqmPJwL9t26JyCtzGBcjd1glSy3Y3OIlVisKDazkXL5gxhAm9lfpFE0Fof6YbHFas3eKVxKKo9HKFHUxDfgK9hY9Pl7AL5uHVoNwSrf7FzMbiC-2sSUu4yxQHiObZdAgimrl_iqA0jDVoKJxfFfl-pagF_aQmk5wabF9PIazAQJdOL3ApowvWdAbno1FIjMh5C-1woNuU0MuxX5XFxlbNv6liMCYI8W5sY02piRoeUTFlyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-nYIhOg8yyu3Gr0Be6sJy2Wpgz2sWZ_0-36gXPXdS7FF3Cn2lCITLhKbOpANmdMhZwepej0sITNz8b-mR85VShbIkNgthu6Y4CkXN_3g-RZlN-6zHobxaXuH8KJrTBIk8uyzxzqOXNBxBnYx4omkc_vCn8eP6Qm-XRJGEYDJX0ZstLxRANFal1QFXNKSk8JKiM77kXPQLyI_wYY3gj5ho5xMhv-REdmUGux-kHfNPposaLK1hdyUoUWSg8m2nlUyAi7jPt7zAa5soGnmXQF85P4BUC5lBHKWQjvPL6iM_uEzxAHYYnDvRAqiZO1yShf2_u15M0uT5nvG_gSAqHTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCYCTTRU2HOgp7lW3ByMDNINt07fDP3v04qn0z--2wuMWIu5tB4ufBisogI53shD1iKOxTiM0h24yzgDK1aBDQ48IdifChYbaWPZXAFqo6-tq9NOjdJcP_ACu_yIEprYJKTnNDHdNG0sLJLFfuN38g_JILFrWTeVM1T4uN-avqC9osowFt0rzDuwElnpQ7BOJW-7vPOhw1723QCjjLrWYBym2dz8FtjhoKPpII3SDc7QJCOXBpT7CfuhHTslEXxJeqgEvoCrrDIfScf0EWJWXXiyrZ_k_A1jDs_foOD6HAuApTmc6vlNfdJ35wkA-Kk0DwONmZANJaY7BKy_cS-qnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIjqefDxGIa5h__QdFBL7J7eYnfctNcJqGhpTQtHNGMFs7cxOSUUSQ24EeW2fOVHrzchK6dErWUjU-2cYpQOGItj80-rVEePVXUytIeyMzVaCXyj6mUJJ32guZQbZ4s4wttBYppwiGnZXGMKprn8XnNJkx8TqaAskZ2gRYyPl6I41rTL6cm8QPWkwh2zmv3_eiPsgyzWnrxMbkCGmq2StcHjwrZ7ECQsjlwsUwT_hsHENFDmUeNI-rLAtc2J-WpMOXQeLvVkgypa7vHtOYxHhh99wmQoH-V9PTIwbs_qlQ5eKuev-5uRImsVoOiLeFPAms1y1ssZXCoVwpTYibFyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHncBNJvAE4HNan7LFuebP8uQ7nex8tN7A3h25p03Cu6FvBfGkkfeZvi_rJMMsK3r3N_SZCWasTSC78QVGZaHlbFx7hVirs9DOo0ObCQtAzSYzm53zTv26tOvgiFSv0a8qZOQi5XW0YCCMsnsGIT6Y6xWu8rUlfVvF_lmKsy5s9q_A1HlGTPBW-fWr-_4xhA8_oO2jWWAy94YypNBLlSBB0OQNa-gAnJUppDsw7tutT6LiXQJKMK1buqWmtXP6cZ_qGkkCHUFWXaKUpBS42UtcFCuqpbZ9JsC5jSisN3mzPvLBaH0pUSJ443eqRoXvduTmz0ZqrJ2D7AHtfz4nVCiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور: با روش‌های گذشته نمی‌توان بر همۀ مسائل امروز کشور غلبه کرد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید و راهکارهای خلاقانه برای عبور از مشکلات طراحی شود.
🔹
یا راهی پیدا خواهیم کرد یا راهی تازه خواهیم ساخت؛ اما لازمه این مسیر، رها شدن از قالب‌های ذهنی محدودکننده و نگاه‌های محدود در تصمیم‌گیری است.
🔹
اگر روش‌های پیشین به‌تنهایی قادر به حل مسایل بود، بسیاری از مشکلات تاکنون برطرف شده بود.
🔹
اگر برای مدیریت مصرف آب، برق، گاز و بنزین برنامه‌ریزی دقیق نداشته باشیم، در ادامه با مشکلات مواجه خواهیم شد.
🔹
باید مردم را برای صرفه‌جویی و مدیریت مصرف به همکاری دعوت کنیم تا بتوانیم کشور را با عزت و اقتدار از شرایط فعلی عبور دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/436787" target="_blank">📅 09:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436786">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF7akLwf00GOuW4YmEJXUI7ferePREWMgibnlUprzkKlIhCo67VNMdDhp3SlU6ozOl1vXuWWo7gfJ5NcRA97Ru2DjI_TevmoVCpahfV8cHggjqaV67hzXjWRd6o3zG-HyA0brV2NEhOat8_KiX479winMcZJfp64j8uCAKERquO6UxPDq3s0V4h5IqOhxSBemCSj_mY8s54ieUrY9HT3DZB-iESN00Pz3R2nMlW8GqVhfjv7GzLsHWk4ua5Osz8aMTpl5icDGKy9To8HzykwXotNCMBNlxaugUt7Kb_hiMbOrw0ersPC1lePLhwDY2sokkPS8DVJ5f3zuyEQwiKBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گواردیولا: آرسنال شایستۀ قهرمانی بود
🔹
تبریک پپ گواردیولا به آرسنال پس از قهرمانی: به میکل آرتتا، کادر فنی‌اش، بازیکنان و هوادارانش برای قهرمانی در لیگ‌ برتر تبریک می‌گویم. آن‌ها قطعا شایسته‌اش هستند.
🔸
آرسنال پس از ۳ سال نایب‌قهرمانی پشت سر هم و پس از ۲۲ سال قهرمان لیگ برتر انگلیس شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/436786" target="_blank">📅 09:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436785">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660ce9d7be.mp4?token=FIcqKNs30HBAqf7OaN2yYncT35klWblOal0yXsVzEuxh1CJ317CA-7E0aE1jjD3NjEtBzQ_t_JUmmX74L4JiU1u6csqhnW2ztHCWdMKy4a7i_tJ4bKCfHrEo7IFWJBxooSTXY2EYlVgU6PGR5HHEqp-XDLw3OgrQqVmOnSw08uRMKPBZI_qcmPGn7lYOtPhd33pUOp9j9tYuTRS5Ffpfvph8ybLZvy-nbYANkDMdtJzvfEJn2e6PhaGulYYpTZcsPc3WgdgPMd4JHrCv8Wgj0B5OVwMx-wqtorW8ORzZAzZBDp1FXtGi4trsGp5uED2xxzQ2PNAXXzu5CvNYCMQnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660ce9d7be.mp4?token=FIcqKNs30HBAqf7OaN2yYncT35klWblOal0yXsVzEuxh1CJ317CA-7E0aE1jjD3NjEtBzQ_t_JUmmX74L4JiU1u6csqhnW2ztHCWdMKy4a7i_tJ4bKCfHrEo7IFWJBxooSTXY2EYlVgU6PGR5HHEqp-XDLw3OgrQqVmOnSw08uRMKPBZI_qcmPGn7lYOtPhd33pUOp9j9tYuTRS5Ffpfvph8ybLZvy-nbYANkDMdtJzvfEJn2e6PhaGulYYpTZcsPc3WgdgPMd4JHrCv8Wgj0B5OVwMx-wqtorW8ORzZAzZBDp1FXtGi4trsGp5uED2xxzQ2PNAXXzu5CvNYCMQnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: هشدار سطح نارنجی برای شرق مازندران، گلستان، خراسان‌شمالی، ارتفاعات شمال شرقی تهران و سمنان صادر شد
.
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/436785" target="_blank">📅 08:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436784">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hskQqzU62d5wOorfg4x8Yw3jiUyyY9-2JTbW8ooSVHLCbdg4fxDVPhj660pawCXJ1GN-0309SamrjNSYotUObEK0Dr3HqW-u11i2WRTQj-RqcBdi7945GVHX27LFjEurOCP8R1ZWdP9W56BtenINp0BPkx08nncHpmH5_ewj7zN6Ho7yNOmGJJOtzcP4oiHiFpUDmF-vFEWMF09n42Z-cjcw-9J9Hna11O2kf2PukbVjkRPsuWEIcDyi2KczxCIp05Wc0Bzm-B1gkoVLQspk9xmzJF8G6Kv1dUSiY1DnynTtDhOHzXnu0MxdVPQNYSKa2Qi1m3bFFtxefkB4BZ_chQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوم‌گردی بسازید؛ برای هر شغل ۴۰۰ میلیون وام بگیرید
🔹
مدت‌هاست فعالان حوزهٔ بومگردی خواستار افزایش وام برای ایجاد این واحدها هستند و حالا معاون گردشگری کشور از ۲ برابرشدن وام آن‌ها خبر می‌دهد.
🔹
محسنی بندپی، معاون گردشگری کشور، به فارس اعلام کرد: «در سال ۱۴۰۵ مقرر شده است به ازای هر شغلی که در قالب احداث اقامتگاه بوم‌گردی ایجاد شود، ۴۰۰ میلیون تومان وام به متقاضی پرداخت شود».
🔹
این رقم سال گذشته ۲۵۰ میلیون تومان به ازای هر نفر بود و فعالان بوم‌گردی بر افزایش آن تأکید داشتند. اهمیت بوم‌گردی‌ها به‌حدی است که در ایام جنگ رمضان بیش از ۴ میلیون نفر در آنها اسکان داده شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/436784" target="_blank">📅 08:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436783">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e2f3eeaa.mp4?token=IY1zMeX6v_p1k0zYsM0XoXP2xq3JwaNyLP4WODHwQxa5dOD4ERRPwixcsLS1m7U0d3-Q22AR74A4yItBF8gpnwZa93RqBGnwERtURXgzeALk87THM-iO9Wzuh02pn5SY7klv2IN_HRSuQ2SjS4eBUxBJETNk0Aqn1ZpTAsQYkyPlgBuONchfqkdroPuIPNI3e7KKHwW5QAvi0Efkomd4B68_MbuOUdJCxFnIas9dxdxAJ9nMB0wKUj5hhB8jNq7wzBS6VYjYEj2sfFlp14Rg3Ak9miqaMoQ0LngRXkypM3zT-aVr0RAJWppAHR1DTXgb8yPpBSgC7OuCksLqAchO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e2f3eeaa.mp4?token=IY1zMeX6v_p1k0zYsM0XoXP2xq3JwaNyLP4WODHwQxa5dOD4ERRPwixcsLS1m7U0d3-Q22AR74A4yItBF8gpnwZa93RqBGnwERtURXgzeALk87THM-iO9Wzuh02pn5SY7klv2IN_HRSuQ2SjS4eBUxBJETNk0Aqn1ZpTAsQYkyPlgBuONchfqkdroPuIPNI3e7KKHwW5QAvi0Efkomd4B68_MbuOUdJCxFnIas9dxdxAJ9nMB0wKUj5hhB8jNq7wzBS6VYjYEj2sfFlp14Rg3Ak9miqaMoQ0LngRXkypM3zT-aVr0RAJWppAHR1DTXgb8yPpBSgC7OuCksLqAchO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فسادستیزی شهید رئیسی از دستگاه قضا تا ریاست‌جمهوری
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/436783" target="_blank">📅 08:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436782">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2ZuoddDJ8Qv5d66_3YMuTSeD8w0p4FXBmh9cSAnYPpwvUA6TS_YkFbUmyANgPYeKzxMh7w_4W1TwqVt4Vh2w4gkpXD0EvfGKUwb7RL60Eb35J7NTCVzJLQ57q3QHMPa24WoYillgR8982SUnKq7qFDOKDGdS5sZ9dD_Z6-5Mcnq9IiBPUatYLHKHhz1ztXvOZL8CkltzaxFynRkxv7UTV83Sq_fqlUCOAc6lKzQNHXLjdxQeOi-W1mZSdTQVKK9XVMPtQpMOW0o--cBCeVc7pkJPshzBiwxnO6bSD8JuUDyhvFCwHnLzp5ysDN_nls887gRfogGXsPKODi_fNy9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از استقبال رسمی شی جین‌پینگ از پوتین و ورود به «تالار بزرگ خلق»   @FarsNewsInt</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/436782" target="_blank">📅 08:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436781">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کرمان امروز تعطیل شد
🔹
استانداری کرمان: به‌دلیل هجوم ریزگردها و آلودگی هوا، اداره‌ها و دستگاه‌های دولتی استان به استثنای مراکز امدای و خدماتی امروز تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/436781" target="_blank">📅 08:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436780">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl-7LaErpqkuCJJzEZN357K2rmPK1CVkfvieQps9bY2byJcU82Z_8370t7KC_4vFI2PB19fXG4-s-YZRSVaHqtbXBIjtlfjRlNCwqW5ZlC6mRAfKlchhsbm5PoJbxOeVJREPunPjjwp68v3ph8wpCvUHezSFgEKQJWqklsdmypvlXsjwoD21fabSz5iY0yqV51FVHSzCHdjHu687SjB8qafDrCei5JHTWqMAcfK4QU3cZ9CTVMef01cucE7F9jgC761TtU8HYQUZymFfLkjklCSavPmSY7lghh96vzOTlqMdyOBeoFxBWQAOyAso5573UI8vCmBOVOaUGjJ-rc6G7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی به منطقۀ غرب آسیا سفر می‌کند
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی: از سال گذشته، آژانس اتمی در حال جمع‌آوری اطلاعات، تجزیه و تحلیل و ارزیابی آمادگی و توانایی‌های واکنش در شرایط اضطراری بوده است. من به‌زودی برای ادامۀ این‌کار مشترک مهم به منطقۀ خلیج‌فارس سفر خواهم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436780" target="_blank">📅 08:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436772">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4930b0111.mp4?token=HXLDZgGZRuhfCDi7ksXhIuJ4DhaDmXbm5BM3Gw_EVh_VuYszB5nfLtq7lvRyguU-qgD6V-oOGjZE6z4wucqcybTJB7-sUbQaKo8PodqmwuCfLt2wfBhNqtwph5Xn-P8F98YXVPKMXRnSQtm-eiFAQp5RMX5l_3iz0yC41gsBHKSp3yPG-QZ6crGeqGnI87xbQqWZBFqirXPsVzxClpccV8MCgmLeA9FCct_Kj9CP3WvCLw7hEv3VNl9xxdgtCIhbIWRytgtx0DMtYdObC-uC0lQw5cVSGYBH_O3kSvpvPOP1QylTnYn1ZWqw18gZMBx0SboYSeIp4BT3K8Pw92_lWxnT4aqBMU2O5J3PWuK-SSblgqr5G7S45O9XC0YeJJRLCuEx6y7IpPbsmY0zzO0wAx4dBgzQcgrvSQcyDdg3jc2I45o3_xL6trwe2DF3YAWR0BAXI54WxKmIM-uIiya_T9fiRUHQ2GIzrJ0oMYcAgudwe1TDaG7YmhFTKcHiS9OtaZrTXljqvKUeJ5POQeHKzWJoMd_ZMLi7BrD_0u9O2VBF2Bd36neJ-R9qheHnNc1pA_bA1-c5QIAoDSIbF1Pf2UkkzrBWbPGbYsRGrGarqrzl9HcOeY-wTCMFXqrORVtJc6lLzJkp-bW2zHoFIUz_ydjG6SeA2ZlKy2ShJn_c90U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4930b0111.mp4?token=HXLDZgGZRuhfCDi7ksXhIuJ4DhaDmXbm5BM3Gw_EVh_VuYszB5nfLtq7lvRyguU-qgD6V-oOGjZE6z4wucqcybTJB7-sUbQaKo8PodqmwuCfLt2wfBhNqtwph5Xn-P8F98YXVPKMXRnSQtm-eiFAQp5RMX5l_3iz0yC41gsBHKSp3yPG-QZ6crGeqGnI87xbQqWZBFqirXPsVzxClpccV8MCgmLeA9FCct_Kj9CP3WvCLw7hEv3VNl9xxdgtCIhbIWRytgtx0DMtYdObC-uC0lQw5cVSGYBH_O3kSvpvPOP1QylTnYn1ZWqw18gZMBx0SboYSeIp4BT3K8Pw92_lWxnT4aqBMU2O5J3PWuK-SSblgqr5G7S45O9XC0YeJJRLCuEx6y7IpPbsmY0zzO0wAx4dBgzQcgrvSQcyDdg3jc2I45o3_xL6trwe2DF3YAWR0BAXI54WxKmIM-uIiya_T9fiRUHQ2GIzrJ0oMYcAgudwe1TDaG7YmhFTKcHiS9OtaZrTXljqvKUeJ5POQeHKzWJoMd_ZMLi7BrD_0u9O2VBF2Bd36neJ-R9qheHnNc1pA_bA1-c5QIAoDSIbF1Pf2UkkzrBWbPGbYsRGrGarqrzl9HcOeY-wTCMFXqrORVtJc6lLzJkp-bW2zHoFIUz_ydjG6SeA2ZlKy2ShJn_c90U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از استقبال رسمی شی جین‌پینگ از پوتین و ورود به «تالار بزرگ خلق»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/436772" target="_blank">📅 08:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436771">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiW4wH6ysjNA7kMqqCyIkIDEpWbFUJt50XA-FhFU958Itz9GScC5hjiz-J9Ft9aWAIOGbrZ_pkhl7rfwiuM_VanCWxj1LZE6xZPL4IkXtuIynRFTDv8TJgHrL1F63-MCd-mLeZ3LyXfYpMmdfg2QKo-oOXWikm2jyxY5SOQEctCa1IpwsX3zm_azy2xjiMjnd9-YOKSLFPdrS-LeNo-KmfCcrM_gnXGa6IYCblF-CVVWGs94HyDmQp7rwJVgs-tbPOhvRWLZnS5U5iBpRUnh8EeN_XgJ0bUMcuwGyjQcM6vGphRCDNVfp3wyA4DWoJbWD64dARlR3NZKLUFr8n9IyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل خط هوایی فرار جنایتکارانش را راه انداخت
🔹
اسرائیل که این روزها سربازانش در فرودگاه‌های جهان در معرض بازجویی و خطر دستگیری به اتهام جنایات جنگی در غزه هستند، حالا یک خط هوایی مستقیم به آرژانتین راه انداخته است. خطی که تحلیلگران آن را «پرواز فرار از دادگاه لاهه» می‌نامند.
🔹
یک تحلیلگر برزیلی می‌گوید هدف اصلی از این کار، فرار از بازجویی‌های امنیتی در فرودگاه‌های بین‌المللی است. سربازان اسرائیلی که در جنایات غزه نقش داشته‌اند، در بسیاری از کشورها ممکن است دستگیر شوند. پرواز مستقیم به آرژانتین این خطر را کاهش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436771" target="_blank">📅 07:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436766">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoxUIrwcsb0gdp2v0Ah61VlQ-VhkQxGvYPE5hYTz6wS-60pLkhIH7N_eS3wHHsPVi_BNUi7qcEN6CnLO24ldqKfYUmMzQFTwvnllUM48EHJLdIgHqvGSeCXZGic7i9lhvfrHjT4UNLrs7QT_20jwZ0kyIT2eLgW6cwQ1guN6qljvmsBMBbpvXGX7SWQEDwoOvZ1zaxL1cAcETymulxxYLpUnWzHP73enH310Y_B2uuQaIdOi2ZjtbV97K6euT4oVmuttPmz8QNul3k7DcD1m5lMtoTX3JdkgyYxFOti1hB6mpUSSBsRNyu_0SJMmGTU0kCH380go4bg45yCf5__kyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pr30wMM9V-ijAex-nokI7_CyUEGIT5mDgttXN1XcvuSQFblyAx4aUBbgvK3dO3ALvRQq0Rz7oONyTqLtvOMev289bJrHZk8QoW1khzFY12R7iReG0sXhDSU1HGx6ih58jt_t1GHFQmm0W9nN8ALim5lhzi1MYZD-D9UAd3_Nob5m-eeq7noADJexqPuryaJfzpSv0Lyr9hRgP-I-3js3KLrQ-Fxb3b4scs7sNmuAPDlC7ARch1HGinOidrPTVYiGeghxGZgkziaeo4wnQg7jVpBr-z_QIQ8yAwgIZ49DFXdsKyg4loeTGhg41JMgs_EQIDDMrCZmctOq6EaqWf0o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kl44EMq1Xtr-5J1ycLYwyut_q7fz6nmV9X8xeYKMtxCu-31hh1vusDkWJhqrBuc1RckLUpcciFca4a64uO-h_V7naPAOUtgN3oMzwSfxRP95aNs0UrE2YGOAHzOrhC-zBh8XWy01fWEaNvx0XehDjsWfJSB67njwU5w7fJ-siNGZ2F1vitX2AsnHUdCPK85xijOZeJafqiLbu2vz-vXscYhQKHYiHcTQOd78vUMorfUU9MmGNquo-i4iBlzjUmJhmXPstIh1K3nooGIfJvyXtRu94LG4TILLfSj0WfkvcB2uLPmZrj5H6I1TLMWCATF_obHhi4UGX4WMgjXFwvmRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUENccEy7BMpNGMfb7YqqtbC8F9gB6nZ2wxdD3a6YiVyIFXNyN-qh5_bRQdfEWskZsaisRWrH4Q2qfh9u5XVq_o4CKJxWvQVKD8ibsMGsFfcc3CSbSSx_5URqNZ8c_5g_cQg_7jkhOLDiZVNfdgmJuLFPFM0GbJRpQ9w5HFEMbEwNaurf1_deSH86LBhWtvUnBuCYIQwVv7TcSg327qnJ60B0fz9_zKO_zGnbsEiEpaIRNpY808QUJooF4X-aLOqGsfj23Jwtglq_vZFlxfkFmhJF_DIa7myk4jznLB7VAvu6Fh2izqvPaTQvoPiOduSyEsDW_eQf-SPIci8STo7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHsYXcxoDZfpgq3S1LImNiplzeAj2gVrCJRyw3hwGw08VNOqI-zR3_dDVejDTeTES2EALTSjzYlsobOv__jns4utwfcAYOqcebj8X-YAJRfu4AW8aUXJs0-D29hLueQViMQ99_5VPy4OxwawiaoyEG3RKfKaDV2p4Mfuwh1CCmUYCfH0SapmM5ps3ZcNZow__jF90PjNpPNWAyLqZVK5Q9A6UdWldFuj44OE-pIVr9t8M97PX7S3Y95MrMUKK0j_ztuEnlsgVwof75r3ZAcBC2oYOB_DT5eCPJzR_uVbNdK_x9xlqngWOw6g14pc6I_iAIYnwrUKorUaScZzspkq7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۳۰ اردیبهشت روز جهانی زنبورعسل
عکس:
مهدی لطفی
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/436766" target="_blank">📅 07:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436765">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3erD6V5ne4qL3ua5obzpGk_HMQtEivLK9plI7ryPPbmEatmveoW7-wJGyxFIMAuSAxZzmQBO4nT3v1EEOFvqopszYjbDPPxhI9dT1RAWjdZNbc7LmJfVJoHq8GOGJFoNKyf6hUTRwm8erp3WoH1xTTZed0Fu9dFmqQ69H9ydm3C81rT8kGXU2zwYbio4XwK-nrhqr9OEJ9WXtuM-J6vvPWhEqez4c6sRBGysmJa2CqtN0WVtQ6aMQCcNnpfbk9n7QJ5iZyxDngvOzXSaD4hvvkqTK_GV8V4y-SrRuqEd_YjU9QA1q1_UZTS4yH34MJMZsM-F-CdEUWC4yb0vmbdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم قصاص قاتل الهه حسین‌نژاد اجرا شد
🔹
با درخواست اولیای دم، پس از طی تمامی مراحل قانونی و تایید حکم در دیوان عالی کشور، حکم قصاص قاتل الهه حسین‌نژاد اجرا شد.
🔸
خردادماه سال گذشته، مرحومه الهه حسین‌نژاد برای بازگشت به منزل سوار یک دستگاه خودرو شده بود، اما راننده او را به قتل رسانده و پیکرش را در بیابان‌های اطراف تهران رها کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/436765" target="_blank">📅 06:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436764">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
حاج منصور ارضی هم از تنگۀهرمز خواند
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/436764" target="_blank">📅 05:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436763">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCkIYGRum-lgzQi3DHI1FFYYTmXUz5EEHV779KuSUtqQeZ7fXf2UzyU2zuLFdoTb7-Ggf0f0qfr715pfmnzAm-1eFsJxaIOdLRtXM7nCNYtYhG5AusLzmkhjU0RcStT_Vhp9XW4eJ6eC9858mgKfC99JvaLGTMngWNTPJYkZLZ2esCbWpl00vDDOf30UUSUJA9jla1KKtwWqvZqruIqKA1098m-8U_GY2--i1zqdIJmTyJec9-W-3IR2qVb9H7D_uRimRkNKRAZOhQlfIxWH5hopHoa-shD-fykImK9aac8c5qZBIFTzbj0nkSaBXZAJrlpCjA1AouiRE0Qcakf6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۰۰۰ کارمند متا اخراج می‌شوند
🔹
بلومبرگ: شرکت متا قصد دارد ۱۰ درصد از کارکنان خود یا تقریباً ۸۰۰۰ کارمند را تعدیل کند.
🔹
این شرکت در یک یادداشت داخلی به کارکنان خود اعلام کرده که این تعدیل‌ها از ۲۰ می (۳۰ اردیبهشت ماه) اجرایی خواهد شد.
🔹
متا همچنین اعلام کرده…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/436763" target="_blank">📅 05:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436762">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11174b560e.mp4?token=WZQ154isPI14GdTJFXekNaQWSJ3J_X7wrUkfJ7f4vT_0GJSOd_g4qEFlQH0P6BAP_OHVYj6voQYbsImK1e6lV2WNvM31NsfWWIEpdiBMkz_ML5PD-Nkn9iUfKfWl1W0JLR5tC7EQUv2ZJFr2-os3JUfGEE9zT_u62YPLLQ2b0QN6_5oycsiMzJCpdrtbwQYpSw57PZB2IRMN1IJeeoJ26N0FxPzTZe_JgkUBE9_aSDxGeNiGk-lOO9jSkc7-SdxWxg4w4wPXnyIjcnOSSChms8BW2sltuF8CCwr9mvpcXNiE-IeMMlfjUf3W_6nuOmyhjZCTQ-4zgKK3TN7uW6rqNUkAjKPIchLpEl-aJRCoFnjxpUz5dORuZL_JedtBRsmqzCtXT4xCWp7BmC3QXHYT2xvMmQ9WDL5R4mWr8dE1nK56ANezdKAP1lyz7y9_jwunhTV3-ami42l42uN7_vvOGVlIlpg_lvASmwWnCdHNh_67uyB_3DF9LGibhGS_5EnizbUyhSHkuezplXbD65635sJD3f8L--FTwyoHnaSfKOiiQbk8ufVmUaAo-f6Ame6-u1oD07y664zcEPb4pfWw_jr0XyWYnz74mrH0mv4HhDfbVS-hXmIVBBq0vDOnBTynypNKrw74VOUHLBv9UxgKXGcijFwNSaQX3vtMvid6wJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11174b560e.mp4?token=WZQ154isPI14GdTJFXekNaQWSJ3J_X7wrUkfJ7f4vT_0GJSOd_g4qEFlQH0P6BAP_OHVYj6voQYbsImK1e6lV2WNvM31NsfWWIEpdiBMkz_ML5PD-Nkn9iUfKfWl1W0JLR5tC7EQUv2ZJFr2-os3JUfGEE9zT_u62YPLLQ2b0QN6_5oycsiMzJCpdrtbwQYpSw57PZB2IRMN1IJeeoJ26N0FxPzTZe_JgkUBE9_aSDxGeNiGk-lOO9jSkc7-SdxWxg4w4wPXnyIjcnOSSChms8BW2sltuF8CCwr9mvpcXNiE-IeMMlfjUf3W_6nuOmyhjZCTQ-4zgKK3TN7uW6rqNUkAjKPIchLpEl-aJRCoFnjxpUz5dORuZL_JedtBRsmqzCtXT4xCWp7BmC3QXHYT2xvMmQ9WDL5R4mWr8dE1nK56ANezdKAP1lyz7y9_jwunhTV3-ami42l42uN7_vvOGVlIlpg_lvASmwWnCdHNh_67uyB_3DF9LGibhGS_5EnizbUyhSHkuezplXbD65635sJD3f8L--FTwyoHnaSfKOiiQbk8ufVmUaAo-f6Ame6-u1oD07y664zcEPb4pfWw_jr0XyWYnz74mrH0mv4HhDfbVS-hXmIVBBq0vDOnBTynypNKrw74VOUHLBv9UxgKXGcijFwNSaQX3vtMvid6wJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸۰ شب حضور لردگانی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/436762" target="_blank">📅 04:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436761">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXnygv4exQcVUGIsHCE9aGjKa8qsJlI716bFeGGYpio665j-gqF_NGqkkmghsTsKppygGqHRVJP48JxxSQ4QHOV8lI-gu9KUrxukA-66M5dA33W0EjnuBRJoA49680iSCLdM8ptg7x8MLJyrAEtA59UoOeISi0b4R2D-P3w2tIfnqQYHWpSd4zvKGoIQhJQStSHQIQLwxO8Qy_Ec2ot_kRIosXTmVeCNDDxDbIKI5XCX8RmWxeopgaG0vqGJVpfvuDaB2aha79PnhZJLnGKQ__1igSriYO64ePrEaVBxzNMnm_K-jR79Zia9gGJihqjDkGKsDVwrXNuRJlyxfwGzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام حماس: اسرائیل از ورود دارو به غزه جلوگیری می‌کند
🔹
مرداوی، عضو ارشد حماس: رژیم‌صهیونیستی به مفاد آتش‌بس در غزه پایبند نیست و اجازۀ بازسازی بیمارستان‌ها را نمی‌دهد.
🔹
بیشتر کسانی که توسط اشغالگران در غزه کشته شده‌اند، غیرنظامی هستند. اسرائیل به مفاد توافق پایبند نیست.
🔹
اشغالگران اجازۀ بازسازی بیمارستان‌ها یا ورود دارو و اسکان موقت به نوار غزه را نداده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/436761" target="_blank">📅 03:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436760">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زلزلۀ ۴.۷ ریشتری بخش‌هایی از استان هرمزگان را لرزاند
🔹
دقایقی قبل زمین‌‌لرزه در بخش‌هایی از قشم، هرمز و مناطق روستایی بندرعباس احساس شد.
🔹
بزرگی این زمین لرزه ۴.۷ دهم ریشتر و کانون آن حوالی بندر لافت، در عمق ۲۰ کیلومتری زمین گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/436760" target="_blank">📅 03:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436759">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e149b765.mp4?token=QO4EpPoBvnzBpaTMlp848GO3cVE6rd7wQCsE7jUA_05EdqzlODtnGpX3OSeNSnI1osBPgN80Lkt0jYe-xrTw4nVOL_luQba8OeWQ17FdNyQ7sOYsg3mo_gmGJQEX2bemwxcIoTCHSadZjoAtYBbuHK4RDEXwSxtI-GSdNfKRNDNsAGsuL0ABUPFCBSH2TB6ggyT6gmBX4e0gIMroFA7_ea8jfvtGfRgEjThym7AwoPonKBvddiOFYQ2KnLi-7jjnWnvgWR26EgwX3eDtgiw7qGzswq1sV26JHYZPYkUs-mJT-paBm_joHMJvqzSCGc5-aJ8-dna3nusgmFt1lNdTXb8tbCMU96uf--30_Q3ArycbQ3Qf8jwxPj2bG78irF7SHGoeqXud0CLFtXsLRltLV5zWgcavSVzxkGjJfggZ4Jip5QG0nw-meGmb3rwgbdK6r7Ik97ivtMaTaTsXf-psiIA9-aydYEtG48nenfUeYdQ-cTpYNHe-o1WukaGMukOixpmdpDoAWoYfuYGeDPtzLDuesChvDTrCQAIUa9VXWuZPttOZrfqgNS4IZPLbbSwOiBBMKlx0dzCQyk_mnmz1Pzc5VEj5EB2hH_fWJdYFgsIAEAeEe_-yvfJUUrPHZGA7cMVdsjIy4fDEoN3S-SWz1UZpweVk0GTp_ShIg5qWGbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e149b765.mp4?token=QO4EpPoBvnzBpaTMlp848GO3cVE6rd7wQCsE7jUA_05EdqzlODtnGpX3OSeNSnI1osBPgN80Lkt0jYe-xrTw4nVOL_luQba8OeWQ17FdNyQ7sOYsg3mo_gmGJQEX2bemwxcIoTCHSadZjoAtYBbuHK4RDEXwSxtI-GSdNfKRNDNsAGsuL0ABUPFCBSH2TB6ggyT6gmBX4e0gIMroFA7_ea8jfvtGfRgEjThym7AwoPonKBvddiOFYQ2KnLi-7jjnWnvgWR26EgwX3eDtgiw7qGzswq1sV26JHYZPYkUs-mJT-paBm_joHMJvqzSCGc5-aJ8-dna3nusgmFt1lNdTXb8tbCMU96uf--30_Q3ArycbQ3Qf8jwxPj2bG78irF7SHGoeqXud0CLFtXsLRltLV5zWgcavSVzxkGjJfggZ4Jip5QG0nw-meGmb3rwgbdK6r7Ik97ivtMaTaTsXf-psiIA9-aydYEtG48nenfUeYdQ-cTpYNHe-o1WukaGMukOixpmdpDoAWoYfuYGeDPtzLDuesChvDTrCQAIUa9VXWuZPttOZrfqgNS4IZPLbbSwOiBBMKlx0dzCQyk_mnmz1Pzc5VEj5EB2hH_fWJdYFgsIAEAeEe_-yvfJUUrPHZGA7cMVdsjIy4fDEoN3S-SWz1UZpweVk0GTp_ShIg5qWGbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا اصالت، زیر آوار هم زنده است
🔹
روایتی از پیرمردی که با سر خونی، رسم مهمان‌نوازی را تمام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/436759" target="_blank">📅 03:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436758">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVM85LzHi9TgKzaG6HKey3d7BGizh0VWhSAOxRBhMBoVCPkIdXrVlBUS4xitKci3j1asMWHZbqPdsevKQXJZCKYWTX5pjAqWjbPjjbpiGFrBzatClibFJeDgwgqritRAXUud5DkXAfMF0_gxI7ahwlskETy4J1cfECywQqr1sSZ5arMU6zlZudUnB0-23vqeI2V9miyJD9l3K4HKQ3Y42q0NmsbvRbzJRt_2LIcfw3qNOUdEaYiAujprCe53WvPJK79EUrX8BzUApdqyTFW4-p8zaheJYsxWiJOmg9U3PUT-MUN80eCYoE7pH8JjhomCzI9EhWN_hb3SDwxTmAtT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ تعویق حمله به درخواست سران عربی دروغ از آب ‌درآمد
🔹
وال‌استریت‌ژورنال: چند مقام از کشورهایی که ترامپ از درخواست آن‌ها برای تعویق حمله به ایران خبر داده ‌بود، گفتند که از طرح ادعایی او برای حملۀ قریب‌الوقوع به ایران اطلاعی نداشتند.
🔹
پیشتر…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/436758" target="_blank">📅 02:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
هشتادمین حماسۀ مردم شهرکرد با یاد شهید جمهور، آیت‌الله رئیسی رقم خورد
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/436757" target="_blank">📅 02:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیشرفت طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه با ۵۰ رأی موافق و ۴۷ رأی مخالف، با پیشرفت طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران موافقت کردند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/436756" target="_blank">📅 02:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uADSiX_tDO2nAJMzLTi3z-9o0FWqgfQvhXHZm8u7NXd5thXHJhb3rHUhAvyEcXPkRS6zH76n0zdap8XnW4HjvZSDkMbZEO-aUvYcx25UhqfchSRn455N0v0aETwKJKFvaouqswcn55_qTarrXtdniwhsnFISPq1LxqddDmxQrV9HDNNZoZLNlcPHor7PPCQInjktQpNdcQs38irDJmm9OHgzelYA0cHRqzTuetrS7KDJ5g5kRN0cwQ8ws5D-ru7nQmWX9S_GUwRoL7W-CQ1NMu509QyXV7km0gCj3j2IMfVfPd-_YDoIFyJxQkmERSeadv8HnjsxOfahsG4U1dEjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه با ۵۰ رأی موافق و ۴۷ رأی مخالف، با پیشرفت طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران موافقت کردند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/436755" target="_blank">📅 01:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436753">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec04452baa.mp4?token=VEd7soLd4CEjGw9DY5cMGPc5UgO8R-2WXl7tyKZuzWiLKJvwqc1yx6AQSqwhoHy_zrVUAjhLlu0-fmMNcwlcIUcqnKqHUYvzAIwypYE-PhNkV6t46685VufqfZok1vouaHbCT8leZxnjoy5xN6nMGfvebc4ziCkCJsyaM_fxt3VBol401nvc-SOwZPi3zEIz1DjDBJVU03LlTMy3F2gZd5-R3vm8ruuW5hVBN7xKSN89FKKg7eu9qJgioMspZkH6uZs2RSTBrw1YQxsPCpETronu0_7MCmJi-OwwONAYieUK6mnNBzOrVvvamM9F2sE9W665C2uPGW1cu95SANxU8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec04452baa.mp4?token=VEd7soLd4CEjGw9DY5cMGPc5UgO8R-2WXl7tyKZuzWiLKJvwqc1yx6AQSqwhoHy_zrVUAjhLlu0-fmMNcwlcIUcqnKqHUYvzAIwypYE-PhNkV6t46685VufqfZok1vouaHbCT8leZxnjoy5xN6nMGfvebc4ziCkCJsyaM_fxt3VBol401nvc-SOwZPi3zEIz1DjDBJVU03LlTMy3F2gZd5-R3vm8ruuW5hVBN7xKSN89FKKg7eu9qJgioMspZkH6uZs2RSTBrw1YQxsPCpETronu0_7MCmJi-OwwONAYieUK6mnNBzOrVvvamM9F2sE9W665C2uPGW1cu95SANxU8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای آبی و صورتی به میان مردم تهران در میدان آزادی آمدند
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/436753" target="_blank">📅 01:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436752">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3c43e84e.mp4?token=oN8h2xHGyWBCuMzoNQ7onE_8SZmKP02sJgaEZQX4HRjghGvDHQCrI4CXjqOJg17CV7HjMtIItCyjnlvW6f1PZmZct-MVGR3kR5iG4Q7QkGfm8c0DPMOqPLfIyrK2EL6tVibDS8eR9Ua0y6Do8OV7DwXdL603e1DAAbvEuNO3UJ8g6KFtL0bwVTTSb4Ywb-_jH0uH2ibwKJD6nJCItHF_8GiX1GG7HKA5fHhUK1WDNBnV2kMFS5oCPumZFuwW2iYREEIiseJhda5iZx9976C2o5hpnif0QrM2HidFKcFX4Mlh1y1KQFg0HE1KgqHCYsNVlhc3nfgm1ztwOPgpI9X3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3c43e84e.mp4?token=oN8h2xHGyWBCuMzoNQ7onE_8SZmKP02sJgaEZQX4HRjghGvDHQCrI4CXjqOJg17CV7HjMtIItCyjnlvW6f1PZmZct-MVGR3kR5iG4Q7QkGfm8c0DPMOqPLfIyrK2EL6tVibDS8eR9Ua0y6Do8OV7DwXdL603e1DAAbvEuNO3UJ8g6KFtL0bwVTTSb4Ywb-_jH0uH2ibwKJD6nJCItHF_8GiX1GG7HKA5fHhUK1WDNBnV2kMFS5oCPumZFuwW2iYREEIiseJhda5iZx9976C2o5hpnif0QrM2HidFKcFX4Mlh1y1KQFg0HE1KgqHCYsNVlhc3nfgm1ztwOPgpI9X3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال نماینده کنگره آمریکا از فرمانده سنتکام: گزارش‌های عمومی متعددی وجود دارد مبنی بر اینکه ایران بسیاری از سایت‌های موشکی بمباران‌شدهٔ خود را بازسازی و احیا کرده است. آیا این هم بخشی از برنامهٔ شما بود؟
🔹
فرمانده سنتکام: این گزارش‌ها دقیق نیستند.
🔸
مولتن:…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/436752" target="_blank">📅 01:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKATwcGQTG9c1Vx8ThIP-cLBMn6EsjxPC-2PHv5777nBoHZ_aIb0irFOWSz6EgriQNSXkAMCY7jKIST2U_oDRAZd5xMEoOvS-8tiAeAt7_4Kco9XfqWhWRQkU8D50Vv1CTM_us3H3HEwePHVxB03jR6fLo8unxLkCWUXr3B91gIL_cUQGA3jTYReKPNpC2u2qRYQr1foGKvAGsU4V0ACxx74gWUsYDMtHM90-HFhhIYTPvNqXcIJrEYqwPz_r9xiWaztk59i8DVI85doMYXxW1NQkMK4HF1o_mqbLp_hSEozmCNU4EDhR2q1bkfV15VD5i19nIGCY7-mV5JXTtdtuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان چگونه دسترسی به شبکه‌های اجتماعی را مدیریت می‌کند؟
🔹
در کشورهای مختلف جهان، دسترسی به شبکه‌های اجتماعی خارجی یکسان نیست و هر کشور با توجه به قوانین و شرایط داخلی خود، سطح متفاوتی از تنظیم‌گری را برای این پلتفرم‌ها در نظر گرفته است.
🔹
از استرالیا، فرانسه، دانمارک و اسپانیا که دسترسی به تیک‌تاک، یوتیوب، اینستاگرام و فیسبوک را برای نوجوانان ممنوع اعلام کرده‌اند، تا ژاپن که شبکه‌های اجتماعی را ملزم به ایجاد سیستم‌های شفاف برای حذف محتوای غیرقانونی نموده است.
🔗
ملاحظات امنیتی یا فرهنگی سایر کشورها در مدیریت شبکۀ اجتماعی چیست؟
اینجا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/436751" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL1yKoE3ji_T9UVOX2auc6yvXlKGzBiD_m5dTGw1MjykXfVlHBCIu6oYuiRDvErlMD9G6uofTkh7BaXaP1f6sg1uOC-rbQdXeEJ-F-5WZGoVywIqRfofZHVf7yT2fhRLfT-44eSFClhuVWulnGxuY-FKJlDaHQPCZm97lDWOS_iNBdiFaqGnFjiScu7bJPFsgoS1B_rdUVJIwfUPyLv67KqSzX1BP1DZ4YUN0OKZWXKy9u1dmXpa-DmU0MqU_sqBuyrIV8hqaodoYe7oNdcsQ0D2ejSGIVU255LFzSqb-UbwFPD28cPURGe0DMmBWD7-oKVV3hl9Nka62wCH818_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم یک نظامی صهیونیست خودکشی کرد
🔹
سازمان رادیو و تلویزیون اسرائیل گزارش داد که جسد یک نظامی ارتش این رژیم در سرویس‌بهداشتی موسسۀ امنیتی در منطقۀ کریا واقع در تل‌آویو پیدا شده است.
🔸
رادیو و تلویزیون اسرائیل تصریح کرد که گمانه‌زنی‌های اولیه حاکی از آن است که این نظامی صهیونیست اقدام به خودکشی کرده است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436750" target="_blank">📅 00:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KatHlJQeClFJPOvT7_136Kr-eb1ZnDkvJv_uUzt4KQTaLKyrCbHcN9FJyYmzmDhFSiPCBthqNqSHRD0EDF9xIvhrCWSQtmSFSpOIC-yxYYr-E5j27VGaDwxwrCtSgsY6ouDYijk-k-YNOR2tpAc2Apap1OF2Gd_Wg86byNC9-reiWIHIY75oN_F0XpkV19ugU4HQHAZW-XGZ4B_mbrc9MeLoJE0EMV6u1FPBMabv7W2l0uKYK8rb5EGHq9Jxq2S81F1mzFOvvlmRUQ_2kPEXV7kgpSvqfwctHqXxH7T2qipAEbv72M44hKfcCh71nArMapGu4Jk9Gb_ExsvUG3iTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: تقلای شرم‌آور آمریکا برای توجیه جنایت میناب، نمی‌تواند ماهیت این جنایت را مخفی کند
🔹
ادعای فرمانده سنتکام مبنی‌ بر اینکه مدرسۀ ابتدایی شجرۀ طیبۀ میناب در محدودۀ یک مرکز موشکی بوده است، کاملاً بی‌اساس و انحرافی است. این تحریف آشکار، تلاشی واضح برای پنهان‌کردن ماهیت واقعی حملات موشکی ۲۸ فوریه است که موجب قتل عام بیش از ۱۷۰ دانش‌آموز و معلمان‌شان شد.
🔹
هدف قراردادن یک مرکز آموزشی فعال در ساعات مدرسه، نقض فاحش حقوق بشر و مصداق بارز جنایت جنگی به شمار می‌رود.
🔹
ماهیت غیرنظامی این مکان را نمی‌توان با توجیهات فنی و بازی با کلمات پوشاند. فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حملۀ فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی پاسخ‌گو و محاکمه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436749" target="_blank">📅 00:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1addgFhifL9gbk4lTWS2H79w2YyQ6eQwhFB3V2_vXZpY9BQ14EuWM00hiX6Xlzsi9VAO_n0_nY3hw6tVS50xon1yR0ihHzAIc7Vm7MB1ll-2xzwK-d9ki7k269CXvHtJSGmzvJK2SNr2MUEuLcRFxOSZCyq53Cc5WL8Mvwz3GumrX615CrT1Ix0fFR7TP5EYGc-xdG_lOBLffbkW8N_Htoq_gGWyyrVVQsaK6NLKZrMqAiSwcN82lu_dl6cw_o7GILpMyNrfJVhrR2gak87bY8bFjW_nURnVBgjBkeFL8WBKABs1ksDyFe7T0kTrZMJ4ifnGgzM-T9AjhrfPUHe0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOySjoTBV6RHyhnczYXGfKJZb7hPZEYZr9GDpZUP3oZnCg2lfvW_JBD57TXh8kTefg1-8NjzHQlOjMhNB8e-ALJ5acsdIUs6vU5obe0cPJLJQ-AHTZoK84o7Ppb49d-KJoHODF2Z5uzf1RqvjfS7d_L8uOIXGtYP24NIepAYb7I7K2GsJM7Nfdr4a_joXazU-sKBLztiXGIj2WMv9uLQAPNqZe4fHWJPj97pTNNEq6sg5tOOmsqk8itf77DCmg86y6oLKHnNcKGwC_VxLhTwSIg3mov_H3JVocEY7-ekmavrsMC54mHxbRq-i5GfEWsgCyC9lmrSc8EwaaKz29s4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxPLivhp86SxO6itPDG5pLuVbwM0ffUGZo5Vj3kiga9Wvibxfrol0IzWlWM6wTTkDTS3HF1jDsZ-nm8zdqLa9fTRNItaDbD96KVAoLFsE3NcL8josKYkm_lCbpfE6AxXX4mSmgMu3VhA332ebo1wxjUOCGwB8v2hKt1o9R59FodJ8Bf4hqXpFpNrWtzPl_Jy4nROfww2W2HRfj3gnMUVDnGEtQD4N2y68zgIKsK3xiIbt9Cla3FxGZ2_UBteMCRTcMg0WfMThpI4vDVT6LzBAKran6TTlKZ6frozEyygwwQIsV7DkWNSmOxx3AqPlCOYsOm_OKAYZ1o_74PUoRyA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsJx-rhQRnoaH_NJraEfYEcJp0_czJ7JVpaGCOGj5NHpDDhoV7gqX_VNn770VXd-LNR4AuBALALIVs_Lr0Xm5hCHd3GrfaD6eHKYGTmJuyT-EAiKKJsZ3tEnPCUNnfiQ5DUJJy-azWOVD-C3AB9OJ8tAlcPjEHWE7bz_qdkVsxB_J_f8uIhGrCvkbC166TVeGsa_XpXvOnYmFBnfDohmXuaj7AD-XmWSFS6ehKk16_FXn7b3M24tuihh2Ew2tbEzgdv6qF52aGgOKVks2StbTcF_pe-82A8u2OAyL4j_u3YyhxnLHVEDSaOWBEMKqlsb_X7-F8UxjyUSaU8n0HMmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbV66PDLKtrrRnGwZ9yKgzxGBnBhuQSkp73xL8PTIumiCWSzDiqJveu293R5THLWR7mANdfU5lJosXw62lYtcW-X-4PH85nhg_Sybv5k9CNMVPL3Y6m0tniJRke5mtkg_3RU3ksWwIZp5fip2ZhWAsrrnUZoKtMoY43Gt7QQh7SRRFnET73C0zrx2_VRhiwAVhGNg9VsAEMjqVWgwbSl7wLkuk5AIz62hHcvh3yImk2hFzhf_LZ43IkVdGjvBbqZP037_JqNN2zHOy42-4LIsxy7d8O4uq9etJwHkvxTVczPgSsW74znDsghhxXoeyYIpqBop-6Px2iInQeBrrO5HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۳۰ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436744" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436734">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idhJGjXSHhepnABW0qK0yJHvJ-SJxyVaHBMeGlufbxOd_96OKNXWStX65vZSpX0Ugd0h_V5B6TvSsscf6csmpYTOhjR-LJvBDB_50MwzAV6HCpMF9y_io4-Msx_7dYiEboHxXjU1Bjg5RA-eykCeqFDqNYajvucV1YobMSyjI1u5RRKJayPhwJke_-Bj2OGmMEpyM1MTbdgpC_sUKEqiDPTac0wx376RWkHhcfBEkUD647cTqsD5QxtIbX7bQWz71eYtVfV9hyBouR-oe1cCXvNR65qauSGotQAh47yue_bmWup0BqofruSmBwDxIiRwdkJN4Mkz9D6UivzXHk2N9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSI9sYh0vmjYI2cRENUjl7M51xkttiEycH9mKBrdJ26tnqHMhJHPLp16BeBcQPbgmvPWOXRgn3QoJAfQJgGiYRl_Eb1PzbPrPH6C64HMdRFsISg543pacbdkA6COZlEXGbR6PaqxaFm2_sZPAnHd36KU1OIn5fks9_n7AUi_bdRQzpM0RqEPjBVt0UnrV2v4JR-TnsOR9RbogHt53vvo33dGJwj9euTqmLWv5W6W5g1rBLAjEqwL08u-ANbpH1Bakqu4lRZ3D6n5x0Od5vCzWdwrWiUtuqkOFWNPKYw912_EVRNFPqbrF0Q2Fyn9tnNOo3MYT3uEmflUtk6v9JaqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHuir0XwGvQ-uajH7W2fY-DB0NFSdwrGEebZhEMDKc0en9FbLQND-eItLyaTs25TQeHgqe9J36vZZeVtxt2XGLh7A3akwwcyAn-dN7pxQfN5JWDW-gJlwExuvGPnTmAKCjrE242YhgcuEPb2PgoGR3Iry3-poxal4zs0DzRgaiaV7XKXPYU9jIEHxrFJz1dHSprRr-CPY6GX-l97Qg6rUYqcsd7C9pR1Htww_cca0azaCHWF7ag3NVKu7dx6BEb95ry-Lkloy8fyU7pprFyk3AydqeK-a4Nvg0TcWqe57X5E-4pQy0mJYEx_6Gq2GsUBoIIT7sI1FzAp7pZdi6gDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sItLSxJOCB8AmO6cF6mb67hfWt88QmD7EsCN1caqjb-uRt-uqV_e_BSGCVZyard51Xyd-Yyv463VG_-v34ggOiy3PYflDQJSs6ev9PngfI3rT6ZGyZG_XQNSIq8WDt82MWDhRmjVKF1Ohim0jnvjtzMbeYpWWcDi5xL9bn3Pg0v0EkgUamMdJVI3ONnjgMRmdqRqEtzVfBRT60xVJakiBReadx51IxeKPIdSjHdxtEmzuZO_RhPqBsXzPp8KBGZlKCg_CKxJBTh-QhtLwesBuKwzNjUJRKTfxszre_z6_zk28npFAke4BQdPh1sCrhNWKZvIVPp3qqtpz8OA9IRvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alrJCZDmlBnw9C8yibqGbyGbA3DHDUNyiZBCS9fDZEvm3tHJVBerOaJgBz_KFUW1FRi3ueLqSYvRNZ5SbpGydm1DGoXF2y_T-l2Q3k_0_7UcW3d7jvWZwy9jVq95nIWbJv7lGWZsGPxhhIE_DhumlnjlwsGjnLxml7l2hzXyRBpjJL2tZEYYhgu9VRgZBabidN4zvXOWXhtU1caf59WAJt1fwUk3h7IjoKxoVRtJiz2obYZgwA_2eVaH9_9vnDgj4OgQib3MKtdUZFnSYkj_RmSiAnuWexNjYOzbP1VdcoH_ivTSku3WC8A7pk1Vb1cuq8wDf0_SwwgFAaWojw4f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm4T6xpn3Lj4KyiDQ1p_gPlUJuo8juhuaIuajQSPo2q6eoy64-inT7MerBjuXenx7OufR3jsiovw8wJAN4aDp5dDRpDf6VG5WEK8RHgi-y-XCxSV_p1lOLYp2vy2QO0sT_wSgb0v2T5gsUstrIZiteZ31FBER2OoLfVUyjRLixzLsYfK6F0bLeoYhsmW-BgYa_EzzPYuCqLksSYT46kOlLE73jdLariewpm3qhEBA8wK3_KRs1J_ABf3Id4LMPQ4k_LwH59MoHVPNbG6ac6hQ6JjzsIHtvFL5M2eBgJBHxC25PZwN7NN4qw2miaC6effQAzDnOgi_gtYt-FEAJHXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNYaLKbVA9Zx5ZtRxP-u_eEACeVegrCZNcODIyGnM1AcFTRZt0HWsZ_M-D5BYvpdaa1LRWX2ugCAHEZtApdc2o0V0B73TJZR84Kl78kwDUT_HTdwo3VdpctAAL63a54CrLdaYS_P1V-TpSqCnG9aCMEuwIcgJqhQ8njzq--P9tybxgUqDM_4MLGzXogaVp1nmy-4vyerXUOr0PumI2hqjJPHdREDuIlSWUgnbDKeDCd6NClNCbr26jFcxTuxWE236A9VSdiOXVbQcPaTIzDuQWylWCdbbBZoIwE5YUPoltfRVxSP5x6G8OUF2AlMSWvOWCQGpesNZJFM17dAvQ2X4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9mfMr7jKxt47WVzVbBi6N8-MU0B9DHZAdN7DUky_fdsR0oSmjai6bRMiCPcAdtgoriAgyhRfRxM6MrmiBjDhnE9dlIbFoOnhDzlWn1Loy72zNCP4uFhrcubCO54LxJYSuGFQq5-qUpMp6JMfEPWGwOaZjW9N3RWMAI2yv3On4XTdqWpBJKZ2rmSGvoHyyWonBbO-OFhnPMwgCSTp4-d26i9U3zBKTdHP6QTDt_LsjVoE8-_LhZqre2FHJEmuRuZBCXLpsd3gG8fPoiS9saSSr0gapBd2bG1Y-f2eP18AkQwY-kYXb52RjpR-giIMjU2EPt5Riibk1KiFc24ESiK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avLlhofhcd8C1cIHVG_-Lwi2m2VWI25nbr7K71yqU7m4F_EIzoEP5G56pjTKPIy4TpMa8uG-ity7WWXM-ajtDtNHlncz13LbkNR3JdUhyOG0lat9BpWo2xCZVoczntwZ0zZwyWtdl53K66nsrWfyux5uovqVIv_5PpAZqkbB07bhlrWEfBx8DtUBOAIKybdvEH8jYo4hnyocoSyp0-zW4cGMru6kE54I-ZcS0YWRQ21NQRog-3koMAmHfV4loalBVT2XdRgMgzOLY7SzIa5irWA5TomR5Ac9XKswhbpYds0JCIdP_TuHCm_z5jn6sbUF2wSnXJMg-rbpVl25z31pgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2hKt91MGT0QLtKw_OpOtDDoN0u77y_T9L5YFn0Q0tJTYxfd-EdAJgGBMbaGQIAHKZ8vSH2PaWgedzWuztNc1mv3o6xoFtQGcAgi4imbXMSGH09JVCGoYLqrtGXjTdJAiPVvtKUv757UHpQe_5LsHE55UtyDoScGiq6KR8uOB2sxJqiCZQ4XCSbSayKjoid3szOoo3I2OE6cN4-Y9PhINjWyQoteOGmtDLFQf0fyCOHKvmj6z7_H43wqgV9wRl14qEZPdMXtJ1n5V7fX9osqkvgTLM3GbRyXuAoQLDFIq4DFRIscytlI0FD-B524axYqwCu9rwF5Fxa3cfM2Ta55Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/436734" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2eFuQr2X1UJBbMXdlI0mjOCTMkBXQaFx1upQy3ZoCZ6cvbiMLMXqh2M2IW2lSWy_lIsoIrBVR1YY0Gd_5c6HJ2cCvnXQWBrikO_CeJduuuagV-iYYXYEVzfv0VdrARaxnr5--_FMV4-5t1ooIReb8S-r789eepncIMYShMfFEB1L19GZr-2p2hmq_20Ep4Bu7yskgPsWpJ1w1cdfWPZWs8rqLv4w9myV9dujREZ7sD-0cyHqeNmh5LKaCd3asP1AdzQdvAPrFJdYSJbSpVJA6WI7rC4MxDbw8xmBfYlYuwxp0Suyu95T3B_9pyLcJx-XMaz_qYhJ7wPEeXPnbDiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کنگره از هواگردهای اسقاط شده آمریکا در جنگ با ایران
🔹
بر اساس گزارش‌های خبری و اظهارات وزارت جنگ و فرماندهی مرکزی ایالات متحده (سنتکام)، ۴۲ فروند هواپیمای بال ثابت یا بال گردان (شامل هواپیماهای بدون سرنشین) که در عملیات «خشم حماسی» سرنگون، منهدم یا آسیب…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/436733" target="_blank">📅 00:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
جشن تکلیف دختران بروجردی در میدانِ خیابان
@Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/436732" target="_blank">📅 00:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53d3cd232.mp4?token=ikeqy4OWld5B6Zjixr8nWNRi0o4SagXq6KEgcbriZV5Hf5pEjUMlYvQ6A0jh1k9OoTeQnejFmGzHzBwe_Poj8vfdMbEqqiF_4tmL2S4WuHzIuX41TB2vGbZbKPI7n4C1h9_J7ylDgJQknV5yvUAkI04RPpccdB3D7wcpOfGNbPtFfCPrvD58SMJPaNUCsJvgviG3ESFMeRkiiQrREvW7o9YJlBGQsQp70WujDeihdW_gCo7rcJBPQN0kU33OWlQlSJ0qec2L7iCh35GOCB2i8oF2vCK63PSvLFDxWQkygKO-eGWdmf2NtZLqq8DlRY5QY-_KNOzSUN2d9aDVlYq-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53d3cd232.mp4?token=ikeqy4OWld5B6Zjixr8nWNRi0o4SagXq6KEgcbriZV5Hf5pEjUMlYvQ6A0jh1k9OoTeQnejFmGzHzBwe_Poj8vfdMbEqqiF_4tmL2S4WuHzIuX41TB2vGbZbKPI7n4C1h9_J7ylDgJQknV5yvUAkI04RPpccdB3D7wcpOfGNbPtFfCPrvD58SMJPaNUCsJvgviG3ESFMeRkiiQrREvW7o9YJlBGQsQp70WujDeihdW_gCo7rcJBPQN0kU33OWlQlSJ0qec2L7iCh35GOCB2i8oF2vCK63PSvLFDxWQkygKO-eGWdmf2NtZLqq8DlRY5QY-_KNOzSUN2d9aDVlYq-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مولتن، نماینده کنگرهٔ آمریکا خطاب به فرمانده سنتکام: مگر نمی‌گفتید که جنگ با ایران طبق برنامه پیش‌ می‌رود؟ بسته‌شدن تنگهٔ هرمز کجای برنامه بود؟
🔹
فرمانده سنتکام: با کمال میل حاضر به گفت‌گو دربارهٔ ابعاد عملیاتی مشخص هستم.
🔸
مولتن: پس یعنی شما اصلاً این مسئله…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/436730" target="_blank">📅 00:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ISQVjhJJYxqeb9k7eMVDjcWxDyl7eajLVXRJ8jORfzlPKsp6DrT9YoxsE5uf23XRD3q2A4ONs-2JwbdJ_MJAgq_o1w2TOasEz1C70z-_fUmJ9r_uMoS_XU7Z8SJiSK2lFKMMFNPpKEASS9lOP5VGt3RQrx9bmMSYahNViLmInrR1XqSsLFvyeLPXqp8Zrdi0-tvkYWAaR0Yho-peCOktaUpZeb_s-Ms383OUFayNjZyR7aAl7mXETpDs2xuZbFkY8djMg5W8Wm5SpZKrp98977qT-HbtbDdn65JS8WvmGNxRopB_YTjCi5wvp6tDxaWeZlbcuERUbiQkcHZ0GHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: سابقۀ دشمنی آمریکا در قبال ایران، بیش از ۷۳ سال است
🔹
سخنگوی وزارت خارجه در توییتی به‌مناسبت زادروز دکتر مصدق نوشت: مقامات آمریکایی بارها از ۴۷ سال تقابل با ایران سخن می‌گویند. این روایت، تحریف عمدی تاریخ است.
🔹
دشمنی آمریکا با ملت ایران از سال ۱۹۷۹ آغاز نشد، بلکه از سال ۱۹۵۳ شروع شد. مردم ایران طی بیش از ۷۳ سال با فهرستی طولانی از مداخله، تحریم، تهدید و تجاوز نظامی آمریکا روبرو بوده‌اند.
🔹
بازخوانی کودتای انگلیسی-آمریکایی سال ۱۹۵۳، درسی روشن و دائمی را یادآوری می‌کند: تنها راه مطمئن برای حفظ عزت ملی، حاکمیت و منافع ملی و توسعۀ پایدار، پافشاری بر حقوق حاکمیتی و استقلال سیاسی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436729" target="_blank">📅 00:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f035ee4734.mp4?token=tUhrv9YI58_4gYqssyf6khFZ0PM-JE87mHSJnBVBX1L_Tx6Q3AsJM5440wugQiebI-aRJ7bi80HdhJM_k9GNLiH11cZb0MgITNCFo_1bkFGzaxowY7X3otP_wAz4yIrc36SOw3eIC5MzAQfosHPPV6u45XwGnTNUAs9TpK77n6e-nMVgsSnDx_4gy7OBjvqY7WihqawaGmlzG6gVppNAked14zAVSFcLc7m86Q6r3h4n2DlVu4m8jcILtBFte6glSyvxdfbDlrSSV6TpJU9r20ROCQaCOsDz_XwsTEE8PlZg34WD0rKQRpiG9A0NbhaCsSAqpoEVsIX1m-zAmZBEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f035ee4734.mp4?token=tUhrv9YI58_4gYqssyf6khFZ0PM-JE87mHSJnBVBX1L_Tx6Q3AsJM5440wugQiebI-aRJ7bi80HdhJM_k9GNLiH11cZb0MgITNCFo_1bkFGzaxowY7X3otP_wAz4yIrc36SOw3eIC5MzAQfosHPPV6u45XwGnTNUAs9TpK77n6e-nMVgsSnDx_4gy7OBjvqY7WihqawaGmlzG6gVppNAked14zAVSFcLc7m86Q6r3h4n2DlVu4m8jcILtBFte6glSyvxdfbDlrSSV6TpJU9r20ROCQaCOsDz_XwsTEE8PlZg34WD0rKQRpiG9A0NbhaCsSAqpoEVsIX1m-zAmZBEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگره آمریکا فرمانده سنتکام را سوال‌پیچ کرد
🔸
ست مولتن: دریاسالار کوپر، شما در مورد ایران مدام از عبارت «به‌شدت تضعیف‌شده» استفاده می‌کنید؛ تابستان گذشته به ما گفته شد که برنامه تسلیحات هسته‌ای ایران «نابود و محو» شده است. آیا می‌توانید تفاوت میان…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/436728" target="_blank">📅 00:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc615f993.mp4?token=giyESIg_zX51QcCjmWTzLdXOKKz2rdGbxvsR3Ut7j1KpfGrcQzdnOuOkFV2V4Oa-4y-DGoItVjIaYab1ukNpX_s1x5gsYoPkQRqgxMBX8_ZPofFZVpyexskETY81DXa8MJ68eeATjE71KOEZAX-WZDlLJk3gdm4Mnbs6xv1dqvd67w-lcBOXGFSmw_ikWAUzAuP2T0tZgEHCzBaKS8NSUbB8AoS-IKPCjndANk4YE3PT1yE8fBm7X7FU49_PmrTfsJMbisYxEIEQBuUaRzhnbwIDg7qtl6hkGX_pywTE9xbJs6lORU2yOSB6tTvXAjNH7IxM3fX_P-XsfCBqtmuPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc615f993.mp4?token=giyESIg_zX51QcCjmWTzLdXOKKz2rdGbxvsR3Ut7j1KpfGrcQzdnOuOkFV2V4Oa-4y-DGoItVjIaYab1ukNpX_s1x5gsYoPkQRqgxMBX8_ZPofFZVpyexskETY81DXa8MJ68eeATjE71KOEZAX-WZDlLJk3gdm4Mnbs6xv1dqvd67w-lcBOXGFSmw_ikWAUzAuP2T0tZgEHCzBaKS8NSUbB8AoS-IKPCjndANk4YE3PT1yE8fBm7X7FU49_PmrTfsJMbisYxEIEQBuUaRzhnbwIDg7qtl6hkGX_pywTE9xbJs6lORU2yOSB6tTvXAjNH7IxM3fX_P-XsfCBqtmuPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر لُر: دشمن ما از وحوش است و ما عاشق شکار وحوشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436727" target="_blank">📅 00:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTv8KAwsweUKPvYOjhvHjcvWLbJdB3tgFD_SAPAnbi2rkv-MWg10fD4_GkhfjCdaPs4xEgCY7O6weQnXonD4CGzZrCszuvcFF0w96KcJ3L6fpjw2kQUhWSwn3CQo3SvQW92s93SM7u2fnSAkERCgY26RPWWz6LKK3hLVK8ja_xIC9FxUNX2IEjTecIoS_FceTwIY-xWHm9LkweRW9SbbGOg4d_2Q1xBE5jaz3nhpiOEoXmsLFpXIggLHGqwqZyAjVBDF-6XmTd0TW3KCREJ57B2B0rs2k5CiN8WiSAVbrQDAd-9-1wNv_cqiE-V8R7wNLGAV5ykZIvj02QyEHgWRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به هر قیمتی بالا نرو!
🔹
روزی بوقلمونی در مزرعه، در کنار گاوی ایستاده بود و با حسرت به شاخه‌های بلندِ درختی کهن نگریست. بوقلمون آهی کشید و گفت: «دریغ! بسیار آرزو دارم که بر فراز این درخت بنشینم و جهان را از آن بالا بنگرم اما افسوس که بال و پرم را نیروی پریدن نیست.»
🔹
گاو نگاهی به او انداخت و با خونسردی گفت: «چارهٔ کار تو در نزد من است! از فضولات من بخور؛ چراکه سرشار از موادِ مغذی و انرژی است و شاید تو را نیروی کافی ببخشد تا به آن بالا برسی.»
🔹
بوقلمون که تشنهٔ پرواز بود، اندکی از آن فضولات را خورد و با تلاشی بسیار، خود را به بالا رساند و بر بلندترین شاخهٔ درخت تکیه زد و با غرور به دشت‌های دوردست نگریست.
🔹
اما دیری نپایید که کشاورز، بوقلمون را بر فرازِ درخت دید. او بی‌درنگ تفنگش را برداشت، نشانه‌گیری کرد و با یک شلیک، بوقلمون را از آن اوج به زمین انداخت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436726" target="_blank">📅 00:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a54ba1cf.mp4?token=uqoNEa_YWMPR9YEq6z7GuyDoB7XGMJKwaK0LbLmDfXBh9bJOL3rVX5g1e5RoKJRdTA2Y6LUtcTi41_7l-igJl8I8aB9R36aLWBA65J1a9Rh_GgW47mo5HBBcxxJBXqOqDhC2rCJQADtmJyNzzbrM2L7oKcv5zPddQIXPHX8mPaCHmMqsVB6f8ERB_Vvkny3wUdQKD2d8vj6Tme7aP99J6ei64BxDs-0cXXmkx3-ZyDMdbcfGaggSh0WEarEw-RCO0Z_l9SpQWm_WR4Kjuel6a0SCoyEC8s9JGPKfOEFocXzBR6p-XGHAszExCjwYfHq6faTv24D6-wFpriRzru3zyzKgFzk6_pZ8qT15X835qVAU9hfwf7A2qL6Aeu-g6FwNL_qXGnIFkaeH-1FOZbxwGbtGClRZmpHEo8H_j2XUMPXVbR7CZat2VgnDl46Iu03UJvzlijn9x4UEizCLkZeaBCfJlnFnabar7M7edTcEiLcoq4CDEz75rfg0GcvXttW5gXKYvkTYl1J5TCXE3jKMKEC8Tg3JqoflOiaVKtrIrnlya4LY-NOVV0GGEaIpmVxxHUwqwFkxzTBYLwRNVwJw2qDKvYlnR-ggsRAMizSvbYngyvODG6jOTPT9HeIxy-LKjKhzqAoMBFc1CupxUFav4kStMQc4YVvNH03TVtydNFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a54ba1cf.mp4?token=uqoNEa_YWMPR9YEq6z7GuyDoB7XGMJKwaK0LbLmDfXBh9bJOL3rVX5g1e5RoKJRdTA2Y6LUtcTi41_7l-igJl8I8aB9R36aLWBA65J1a9Rh_GgW47mo5HBBcxxJBXqOqDhC2rCJQADtmJyNzzbrM2L7oKcv5zPddQIXPHX8mPaCHmMqsVB6f8ERB_Vvkny3wUdQKD2d8vj6Tme7aP99J6ei64BxDs-0cXXmkx3-ZyDMdbcfGaggSh0WEarEw-RCO0Z_l9SpQWm_WR4Kjuel6a0SCoyEC8s9JGPKfOEFocXzBR6p-XGHAszExCjwYfHq6faTv24D6-wFpriRzru3zyzKgFzk6_pZ8qT15X835qVAU9hfwf7A2qL6Aeu-g6FwNL_qXGnIFkaeH-1FOZbxwGbtGClRZmpHEo8H_j2XUMPXVbR7CZat2VgnDl46Iu03UJvzlijn9x4UEizCLkZeaBCfJlnFnabar7M7edTcEiLcoq4CDEz75rfg0GcvXttW5gXKYvkTYl1J5TCXE3jKMKEC8Tg3JqoflOiaVKtrIrnlya4LY-NOVV0GGEaIpmVxxHUwqwFkxzTBYLwRNVwJw2qDKvYlnR-ggsRAMizSvbYngyvODG6jOTPT9HeIxy-LKjKhzqAoMBFc1CupxUFav4kStMQc4YVvNH03TVtydNFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمندگان هوافضا با ۳ پهپاد شاهد مهمان تجمع اسلامشهری‌ها شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/436725" target="_blank">📅 23:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aud5vu86R8VT-f2D6DVrD7aVLZim1IDa1owrBr1obS5U5F3p1FRjlZ8oyIFPBVPS0QmiagNjZki4pGTOGmzuziFzhOWPBVL7gNkeaSGw4ln77iwP71pHRx4brGXkJ7gnN9MIIL87Xq8hXZYTvy30NRpWqyExc30dViRU1upBgzY2xJrp1z6G_y7XH7An2YSucLp89sPg1tswnllMkNCK6U16SZkvw4JmeP8r8m-sowbKUtOmk5AD_JcQ0I8s3SMY-UbvjSQX8mI0FpUXZx1XRoy0XhAjZJFr5rlioQdnls28euFzBZmruJDrBjoAGjTiYuPnmu6WeAtvsh3BRbp5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدافع تراکتور به پرسپولیس بازمی‌گردد؟
🔹
با داغ‌شدن بازار شایعات نقل‌وانتقالاتی، گفته می‌شود صادق محرمی تمایل دارد دوباره به پرسپولیس برگردد.
🔹
پیگیری‌ها از باشگاه سرخ‌پوشان تهرانی نشان می‌دهد که اوسمار ویرا هنوز هیچ فهرست برای نقل‌وانتقالات نداده است.
🔹
البته پرسپولیس حتما به دنبال جذب یک مدافع راست در نقل‌وانتقالات تابستانی خواهد بود چرا که ضعف در این پست، صدمات زیادی به این تیم زده اما این‌که این گزینه صادق محرمی باشد یا نه سوالی است که فقط ویرا قادر به پاسخ آن خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/436724" target="_blank">📅 23:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwHnmv9EckI45hQ2uHEST8Jl71ev0mX_TafVykAE2c5aWdCbMdyo15vomFu9LUSo50vqsZahE8FwoDiRYcxoCJ4fBZDhxoPK7ZPvbN0XxtCXOSPwJjGy-27LTBDvVtYuwHcVY6j-PP29ucsq59Uv1U3f3kUSTKlrJOgNLpJv3kqPJSZAOsFqe4ho3Ia2yE8TYycy9_uK22txaaJ7ErMJvhuwpi5CVBferY3qpnU3GX4Nse-o1nhsQmcxyOSvHTHi03ziaP1TN4YCPaznrdssdJgW4hpgA7FYgLRv82pBGl2um_E5R0MtbSQmKlI4AYxh36If7f6O4sZxnj1k6-RTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان‌: آمریکایی‌ها برای کمبود روغن‌موتور آماده می‌شوند
🔹
سی‌ان‌‌ان‌ نوشت: قیمت عمده‌فروشی روغن موتور در آمزیکا به سرعت درحال افزایش است و برخی از مدیران این صنعت درباره کمبود قریب‌الوقوع این محصول به دلیل جنگ با ایران هشدار می‌دهند.
🔹
آسیب‌دیدن تأسیسات کلیدی در غرب‌ آسیا و بسته‌شدن تنگهٔ هرمز دست‌به‌دست هم داده‌اند تا شرایط بحرانی شدیدی را در این بخش حیاتی از بازار نفت ایجاد کنند.
🔹
مدیرعامل انجمن تولیدکنندگان روان‌کنندهٔ آمریکا می‌گوید: شک ندارم که با کمبود مواجه خواهیم شد. اوضاع حسابی به‌هم ریخته است و این مشکل به‌سرعت حل نخواهد شد. شاید یک سال یا بیشتر طول بکشد تا وضعیت به حالت عادی برگردد.
🔹
در یک سال عادی، تولیدکنندگان روغن موتور قیمت‌ها را حدود ۷۰ تا ۸۰ سنت در هر گالن افزایش می‌دهند اما از زمان آغاز جنگ با ایران، تولیدکنندگان قیمت فروش عمده به توزیع‌کنندگان را ۵ دلار یا بیشتر در هر گالن بالا برده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436723" target="_blank">📅 23:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZJIdhQ8ATfPvnR0O0yh0SKP5NqVXgwuPkhFRTuIwonB40lliIYyqIuGZt7VUIiSucGFZ7jJQV8vpMdD84glJx6Eeu5Z41ClLgx5KdAaCGpVIQQyNHqzTICM3ytdBztBbLO_M0XbBcIfvv6ElWiNY34quF4ctEFSlhQXhF7A1ASqCv2Lwu2xslm1QaeAQHykdKpaOYQ7wiqqd6-3_PqwJxxu5SbykEo7DkiBmhqk-S-cCMxuKd4gPBNlmsC-CmLxxjEdJ9SadNYIW7gE4eIXg96oaiUW9J0ycjng-KLxk2VcqVyakAhmg-zhjVwHhBraP6gH226C6eJOOWtL2EIlMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0F_VgnU1O5vfulmVLNoe86xBB3n0yF7jadUQx-HAkGgfjecwdfFrpSjxsiig2U_ZZ4ZFP8Fr1YqBg2P5iWWGS6zcAFMK3LlCGD8MyUsZZtHswe0qb02Dm2UscoUsnmrvhslASVU_rnAWiOtj3a1QWAf3jPvFdu_PZKEl0fHQdU-6bRHkOYCxGvb_wnT1P4MxclQhnIbJEIjC7WEIx7uxfwpwFhQ2i_TBawCPZSI6MgGCL1-Lxt6eaFKzqOQSx9acuWTkwUoRGYZnhMn0f9Q9FMJq5vuo4kSqEzIgqroandL-FEls2aBS6fvj_2jZ2bUruNGCeu03H0i9iDinvPGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvBGNq_1lBkZk-9V9MWg1AZ2nmXdcZE1IILOcbHlwDqfbfif7yUbstG68Dljj9V5zoGZ_3qLd6i3tqhr7R04eoVpYuJ68XUZUvcw8eAT5OnYI_yRgamrEanIvZV3s_5_hCkMq-4sziTSoUxkkgd8rhvmS1ixIQalqCpA-LWTMdNS8s4VjVkrLgoeMNnTA7qUImfNFc8gHlk8dkUmcWEM2W7Q3grvSDC51eTsxX8kR3LYKHgOfYO5FF69eCaQaJSmq_AMwJvl1iPWrnXycsGRrVkybE8FsD70WVyO53ExFbRo1jZpLnRmtNbnZoUbAqaAPXg31h-RBbFxQFHi4UJHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLqBNCIv3doMM7grZDtKf8r9h_vImbpoqZH_5sJjzVDJ7AYHvJ7cegd2CR3nbRdBNvb8M2I7QCo3d7qu8r1Ys5CBCrzLSoPnK_Yd4tTxO5kwBVxk6I-gG1_fx3-mxY-5iAWxPMaynB5SN7CPJllLINZz0D0sKdzVdifGCFNYZlTk1yg1inna4YoCsAsLASsl8K4JyA7xtFw-gENWmwwJl-vhY4vn3SZo1pqSdNtBkMD_ELH_RHd16e3kRJhIgPrbueEnDdpqhg9z7SrXrt5mZT-RK0vWHTlmPYXS4NqmHBcG57tIRpEO-o77oJluAJjtquuexh5sVS8RuD2K6ZPhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9zn9DnnxW7FbBzn14Dqrt5b3INV678X2MMANy6m8o6pA6BSd_ezR_T2WU7nnXpyuAkcJQFxkexknjlwfaHlOlTy52fk3ovdAWxB24zh1c0vkEPjeQeaK4SQa39YDyJObjSN0CkOc3amxVbO4LbqI1lzRV12BOSQJPcTG_6jmIvlkcm8iGtLgjyj950eHc87x0u9jr5ldTwAj-LwooalHCqaO8b4PRZVHE9l_LEnalqsUaupKR2UVj3oz10WyFRB4XI9JZCHQDMd8NO28zoxm5Qbi42VPYkISi7onur2T5Ua9qD5NbZKa-gsOcvebTbuWu40tyLK9d0-lCS6gmrDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG0R2hT8OYxDPzbMwOATIkPwXcA8X0weejUJ_2myovQARip_uymXZZzFEWwrE13ecfF9C1I_1aOdbEHowjiNPztWFNFOt6PffbgJFZ_llGSHP2qIjVLq5vaaeu2Z0mAGZtZ3K2QjKuIoe4X6EGbMPyWI_ibZtv_jUJA9sELg1DQtSN8VO_VWFJLGLsbA9Nu35NoST8CvTM1RWZygRcnYbbKGm4uxPlVZ_wbt3y19E9CZDVjBVqspgCeDHk0iWMdyQfcRsrsn7KRDlWRd0CajuvkRY-ctkG0AM7XeS7KAhV6VMsV9hnIELOCZDgykIcHN9QDt_BFeaWSm7TYutUs4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kikDM3pDpUca3jH_ccL0hNcUlen2xCwov67ZWtPkC92SD7yaetlQZB8BCteqPNMbCUmGbtPiMbCXZvVc6e5Aw4wxvoFKhyPrCTy47jG-_fTg3-NPKsvSSre8YA5MAQm3IHEE19sG3-u_pJaCw43VLPi3R8xLDX5w0gyU7KE3fWhHpEThMiO8-aqad3OZHZ4xT0tCrNpORagGyBW55XDYrdNZd_9czOnT1Q06syF5OI0dMenKnyUpfuqJCl-VwoMTAUE-WdLf82dUVR_JTOfW45CK7S5A9URMWSiUbVqFnk22UoxK7Mr1sdS_xL5HMjS50J7O7NQ8fI8A7RoIfki5qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت دومین سالگرد شهید آیت‌الله رئیسی در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/436716" target="_blank">📅 23:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af779788b3.mp4?token=B_ZyjC5iD7f6HMdrIJXoPgF2f8PccHDxsr0o2dcN5-gencNBpL3JIq4OMr_AGzcdSuVgtrCTfAi80qJFN6DBCtptvqPHn-FmE02C4MmdFNsFusdWGKKqdqqTh-a8ZbpDf5-N9HJDM2VpxBjsdf5ceMXxL1Rbn4zaWGvpd-hZaxB5I3ctbq_zqmLadkg8xGkSROVATTh1tojIlR2KYymjti94yD8E9N2A5KVwQrnKCxuvfKIjjl2C4QwaMoSSbJ0PEHCPKqpiUUNwCom0OAvHciTsDeIGDG0mRCS-noqgiJzsgVaEnodLNwtaoKQ7SBS9eLg0P9uxDFyeeNOBb0I2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af779788b3.mp4?token=B_ZyjC5iD7f6HMdrIJXoPgF2f8PccHDxsr0o2dcN5-gencNBpL3JIq4OMr_AGzcdSuVgtrCTfAi80qJFN6DBCtptvqPHn-FmE02C4MmdFNsFusdWGKKqdqqTh-a8ZbpDf5-N9HJDM2VpxBjsdf5ceMXxL1Rbn4zaWGvpd-hZaxB5I3ctbq_zqmLadkg8xGkSROVATTh1tojIlR2KYymjti94yD8E9N2A5KVwQrnKCxuvfKIjjl2C4QwaMoSSbJ0PEHCPKqpiUUNwCom0OAvHciTsDeIGDG0mRCS-noqgiJzsgVaEnodLNwtaoKQ7SBS9eLg0P9uxDFyeeNOBb0I2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگره آمریکا فرمانده سنتکام را سوال‌پیچ کرد
🔸
ست مولتن: دریاسالار کوپر، شما در مورد ایران مدام از عبارت «به‌شدت تضعیف‌شده» استفاده می‌کنید؛ تابستان گذشته به ما گفته شد که برنامه تسلیحات هسته‌ای ایران «نابود و محو» شده است. آیا می‌توانید تفاوت میان «نابودشده» و «به شدت تضعیف‌شده» را شفاف‌سازی کنید؟
🔹
فرمانده سنتکام: جناب نماینده، هرچیزی که به برنامه هسته‌ای مربوط شود...
🔸
ست مولتن: نه، نه! من از شما نمی‌خواهم درباره برنامه هسته‌ای ایران صحبت کنید. من از شما می‌خواهم درباره زبان انگلیسی صحبت کنید! تفاوت میان «نابودشده» و «به‌شدت تضعیف‌شده» چیست؟ آیا این دو یکی هستند؟
🔸
ست مولتن: ۵ ماه پیش ترامپ در استراتژی امنیت ملی خود دقیقاً از همین عبارت «به‌شدت تضعیف‌شده» استفاده کرده بود. اگر این ادعا ۵ ماه پیش صحت داشت، پس چرا ما این جنگ را شروع کردیم؟ آیا او آن زمان به ما دروغ می‌گفت؟
🔹
فرمانده سنتکام هیچ پاسخی نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/436715" target="_blank">📅 23:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b57512bb9.mp4?token=Ag_j7crICvqKQZRQ1GPcnwCsWtvcC5eBT-GwXkB2jrnMwQh3czY6K3vZu9M8OxgEf77LxZROh2oJ6VJrGibJXqd9tcfqXZC1YNNQahUeUv_4sW63_7anbls4NsoXjvLk1hiiplDsjFnLKJwGl4KSGyAVVu5kdRYXaZjVeoEyKJGOcdtj2a1N7mz4M5GkB2Q3KuN2Rr2YwNMG0MhTMZfEySvRO_bsRTcS79pvlWXDcVjRbuj_MIVgggOCuZGbs7dkVak5fIxT1V4he6fiVulXq-buX9eHF_fkwL_CrZxJ1s6xI8WWuy63-zIkrBV70YA5I2unsm5TABiDpUyIgr1rFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b57512bb9.mp4?token=Ag_j7crICvqKQZRQ1GPcnwCsWtvcC5eBT-GwXkB2jrnMwQh3czY6K3vZu9M8OxgEf77LxZROh2oJ6VJrGibJXqd9tcfqXZC1YNNQahUeUv_4sW63_7anbls4NsoXjvLk1hiiplDsjFnLKJwGl4KSGyAVVu5kdRYXaZjVeoEyKJGOcdtj2a1N7mz4M5GkB2Q3KuN2Rr2YwNMG0MhTMZfEySvRO_bsRTcS79pvlWXDcVjRbuj_MIVgggOCuZGbs7dkVak5fIxT1V4he6fiVulXq-buX9eHF_fkwL_CrZxJ1s6xI8WWuy63-zIkrBV70YA5I2unsm5TABiDpUyIgr1rFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری فردی که خود را عزرائیل تبریز می‌نامید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436714" target="_blank">📅 23:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE2xVLb_bcjBFfE-SkxpRAIIz8-WVSDxExoDQVzwFt_oqQVYCSSSfm4aeI1cL1jpZkuv6TIzmi-de88y4SsJDp9QOud0GaSLRv96v_O8K3J27wAG7HwoY6nsJK0NkCBkAjLix1R_LSuUFBxWwtP-d4pGx8o085Pz1lLxlvCMrSAg5gaoW0W5hm835QZ3Zvi40v-QZTg1DJgAFMroJqOQcI2n2Ke8LOkR940oQotfKIcj7lSoUyJpYqW9z2QReOJV3zoMBiBLBH_L_fagbMuTyHiamG0k_33w_0s5v1kMiG6-edOA1fgCr7W6JCzeM32DlTvuWz-QkeRFRNynRR4cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: برخورد ۲ هواپیمای آمریکایی در عراق احتمالا ناشی از آتش گروه‌های مقاومت بود
🔹
در تاریخ ۲۱ اسفند ۲ فروند هواپیمای سوخت‌رسان آمریکا که درحال پرواز در آسمان عراق بودند به یک‌دیگر برخورد کردند؛ یکی از این ۲ هواپیما آسیب سختی دید اما توانست فرود بیاید اما دیگری سقوط کرد و ۶ نفر را به کام مرگ کشاند.
🔹
در همان روز، سنتکام اعلام کرد که این سقوط بر فراز «حریم هوایی دوستانه» رخ داده و ناشی از آتش دشمن نبوده است.
🔹
حالا اما نشریۀ آمریکایی آتلانتیک به نقل از ۲ مقام آمریکایی گزارش داده که اطلاعات محرمانه نشان می‌دهد این حادثه احتمالا بر اثر شلیک ضدهوایی گروه‌های مقاومت عراق بوده.
🔹
مقامات نظامی به آتلانتیک گفتند که انتظار می‌رود تحقیقات نیروی هوایی به این نتیجه برسد که این فاجعه یک «حادثه قابل اجتناب» توسط خلبانان بوده.
🔹
آتلانتیک در پایان نوشته اطلاعات محرمانه دربارۀ این حادثه نشان می‌دهد گروه‌های نزدیک به ایران در عراق همچنان قدرتمند باقی مانده‌اند و تهدیدی جدی برای آمریکا هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/436713" target="_blank">📅 23:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef754870b.mp4?token=rXdeSPdv7EnA_IRMBgvk77jHu4pvMotSBsUktZito5vXtP6w2kAzaM3yXwVTE9zGqB84M_rzIWSnez4YgfnQZQ2CeMtsazUs3fuGJyI0cuDX12o_0IYkJp49UltAFhtCo9ooMhMsnxemmH9MzCxp6zmKEnLkzJrWZEAkHlBneEHrZy1IPUuCfD1F7wFABsd1nIN4dex2KLztfmkyqZvhCkpt8wDki_GII6i0_oGifJI3PvqCS-ObZYyUzFm5jPASGTIl8qEtAjYWdY0LM_jctRlINfqHyJA2K8px_rzte4QwbJsH_lQTl9rFQaEoj17qtTynC52Eh4gNsE50j7qgnXGoDbFFDRuDSyOjregXWM2SvYlBk5HLS6gnaLjX7c8xcpD5rNNCiY_yPHF4ho0mSk5rqs6RjZbTX_a5qipJeos_YWqiAGgXNJIVf8nTvUVNOAskqXqm5a6Wfv-fzueyFvwNhJOnt8Wsp8WlAvsJuG5NaugqVvNUDTWZMhlP5jOjSx9eA02o4BJ6l98zlW1CtNeBr1hLeXS61uuNFbbU5iF7CMwtKULuYcLODlFiCMHEKWnVyhTamQ4N1xPEA_m7t_XqX3sFyy61I-BvkzRG7Gj62wNzzsLYOHNZ7aN9aD6vbUfc6x5raqQVu4iUoIasrsQXgkYdmgdesIUBYAl1g-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef754870b.mp4?token=rXdeSPdv7EnA_IRMBgvk77jHu4pvMotSBsUktZito5vXtP6w2kAzaM3yXwVTE9zGqB84M_rzIWSnez4YgfnQZQ2CeMtsazUs3fuGJyI0cuDX12o_0IYkJp49UltAFhtCo9ooMhMsnxemmH9MzCxp6zmKEnLkzJrWZEAkHlBneEHrZy1IPUuCfD1F7wFABsd1nIN4dex2KLztfmkyqZvhCkpt8wDki_GII6i0_oGifJI3PvqCS-ObZYyUzFm5jPASGTIl8qEtAjYWdY0LM_jctRlINfqHyJA2K8px_rzte4QwbJsH_lQTl9rFQaEoj17qtTynC52Eh4gNsE50j7qgnXGoDbFFDRuDSyOjregXWM2SvYlBk5HLS6gnaLjX7c8xcpD5rNNCiY_yPHF4ho0mSk5rqs6RjZbTX_a5qipJeos_YWqiAGgXNJIVf8nTvUVNOAskqXqm5a6Wfv-fzueyFvwNhJOnt8Wsp8WlAvsJuG5NaugqVvNUDTWZMhlP5jOjSx9eA02o4BJ6l98zlW1CtNeBr1hLeXS61uuNFbbU5iF7CMwtKULuYcLODlFiCMHEKWnVyhTamQ4N1xPEA_m7t_XqX3sFyy61I-BvkzRG7Gj62wNzzsLYOHNZ7aN9aD6vbUfc6x5raqQVu4iUoIasrsQXgkYdmgdesIUBYAl1g-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد به‌یاد شهید رئیسی در شب ۸۰ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/436712" target="_blank">📅 23:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_1cn4rCaFIrPTDeoEYBueIDooijN6QDo-f7peICCT6sI7PW7Ad81n9AoJxw7pJZmCZNxWmqmd1W0VxQKgLtcAabKRVrIsOShQLb-wFXACHrw_Pab5stO_ZXxZdaKa9zIU9KOKfbVAnudBZfFAF_DGPXaCEsVqrAtZl1a8U06mRrfth5Q2RyqF5F_z5NSBv0Ga7iHGRlHXgupP24fMmnaKvd0SUbVEJZbPvltBrRqOWMoE9a0L-f4fQrCb8gbo6dP2CntfyCcYv31AbFIKbboEnCIvcjmUDebT7YAA8queeMcKCHeD59tqz6R4a93nsLMyqLlo2uM3LKBfdsMsWrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکمیل دزدی دریایی صهیونیست‌ها علیه ناوگان جهانی صمود
🔹
نیروی دریایی رژیم صهیونیستی ساعاتی پیش به کشتی‌ها و قایق‌های باقی‌مانده ناوگان صمود که برای درهم شکستن محاصره به سوی نوار غزه در حال عزیمت بودند در آب‌های بین‌المللی حمله و آن را توقیف کرد.
🔸
نظامیان صهیونیست پیش از این نیز ده‌ها قایق دیگر را توقیف و صدها فعال شرکت‌کننده در این کارزار را دستگیر کرده بود.
🔹
علیرغم حملات نیروی دریایی اسرائیل از سپیده دم دوشنبه علیه شرکت‌کنندگان در این ناوگان، ده قایق ترکیه‌ای امروز سه‌شنبه به سفر خود به سمت ساحل غزه ادامه داده بودند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436711" target="_blank">📅 23:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c437f0788.mp4?token=WoxgwoLCJdb9bRNxvlhYmADbkfyVzub4TQGvrd66SO2aoAdKSSRqCvkcfn1olgSc-httIOPKl8EhYLd_R-XOZX-Xf6UYI0apNWMgfOFtNlAJ77gf2T1oAk3azM9UM-IXHyryH88o4KzjZsLnTIO9LMN3STV4DHLXIrs3YGvrzH_9VlsciaBeDh9AoHSZoLGY_0vVK7kWD2EBYRBIId3cgY8k2-3Y7TAw8x4ba5pCiYlP7A-zxHCPqs9HvAlv-oztLfHoHPndYjlZYCTh24X-9TJwiso6wPYga8gogTYG1x0fBdPUW05ypRyj0Ip8Qk2oqmMEzT7IbViV-374oJ1ISFKWv7LFNkxx5m1929Y8PJLZl1KejjlGNhMQ81LK8mWkf7rEfy2K4TtFATppg_ispHk6qgTbhp-cuYM_MsqbJjvCuzXwxgNQb-dfrm14p9JaoPkcwauzVMTUjFgIiC0rNJNg7x80GqDps95pKkwzJW0SSSbvQwsICtIVzIvvg91rJuQyZJXB3pbIy8rhbM8Brkk3PEeZlqgaeLXAO2eHSexRZkFVnCgPOsu1W5d8i_DZWHpSkoFLYfHctiIWsM0-nQzjNwOoD_oM1z2dRTzKiYtqdOp16MXqMOZA5tuzSnQ6c74Y11ot7F-2LPwvgs4L9LkzVL4KLdK3uiCkM1Lrbcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c437f0788.mp4?token=WoxgwoLCJdb9bRNxvlhYmADbkfyVzub4TQGvrd66SO2aoAdKSSRqCvkcfn1olgSc-httIOPKl8EhYLd_R-XOZX-Xf6UYI0apNWMgfOFtNlAJ77gf2T1oAk3azM9UM-IXHyryH88o4KzjZsLnTIO9LMN3STV4DHLXIrs3YGvrzH_9VlsciaBeDh9AoHSZoLGY_0vVK7kWD2EBYRBIId3cgY8k2-3Y7TAw8x4ba5pCiYlP7A-zxHCPqs9HvAlv-oztLfHoHPndYjlZYCTh24X-9TJwiso6wPYga8gogTYG1x0fBdPUW05ypRyj0Ip8Qk2oqmMEzT7IbViV-374oJ1ISFKWv7LFNkxx5m1929Y8PJLZl1KejjlGNhMQ81LK8mWkf7rEfy2K4TtFATppg_ispHk6qgTbhp-cuYM_MsqbJjvCuzXwxgNQb-dfrm14p9JaoPkcwauzVMTUjFgIiC0rNJNg7x80GqDps95pKkwzJW0SSSbvQwsICtIVzIvvg91rJuQyZJXB3pbIy8rhbM8Brkk3PEeZlqgaeLXAO2eHSexRZkFVnCgPOsu1W5d8i_DZWHpSkoFLYfHctiIWsM0-nQzjNwOoD_oM1z2dRTzKiYtqdOp16MXqMOZA5tuzSnQ6c74Y11ot7F-2LPwvgs4L9LkzVL4KLdK3uiCkM1Lrbcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش کار با شکارچی F18 به داوطلبان پویش جان‌فدا
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/436710" target="_blank">📅 22:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436707">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیویورک‌تایمز: در صورت ازسرگیری جنگ، ایرانی‌ها تاکتیک‌های جدیدی به‌کار می‌گیرند
🔹
نیویورک‌تایمز نوشت: «ایرانی‌ها خود را برای ازسرگیری احتمالی حملات آماده کرده‌اند و سیگنال‌هایی فرستاده‌اند دال بر اینکه در صورت حملهٔ دوبارهٔ آمریکا، درگرفتن انتقام و تحمیل هزینه‌ای سنگین بر منافع آمریکا در همسایگی‌شان و اقتصاد جهانی تردیدی به خود راه نخواهند داد.
🔹
در هرگونه دور جدید از درگیری‌ها، ایران ممکن است روزانه ده‌ها یا صدها موشک شلیک کند تا «به‌طور مؤثر با دشمن مقابله کند و محاسبات طرف مقابل را تغییر دهد.»
🔹
کشورهای عرب حوزهٔ خلیج فارس باید خود را برای حملات شدیدتر به زیرساخت‌های انرژی‌شان آماده کنند.
🔹
هدف‌قراردادن میادین نفتی، پالایشگاه‌ها و بنادر کشورهای خلیج فارس، یکی از کارآمدترین راه‌های ایران برای آسیب رساندن به اقتصاد جهانی و اعمال فشار بر ترامپ است.
🔹
اگر آمریکا به زیرساخت‌های اقتصادی ایران حمله کند، ایران با بستن تردد در باب‌المندب به آن پاسخ خواهد داد. یک‌دهم تجارت جهانی از تنگهٔ باب‌المندب می‌گذرد.»
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/436707" target="_blank">📅 22:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436706">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf02d7939.mp4?token=s6oIElwOm4JlLvqutSKPbwQlHaA9RKUIOHtpSl6QCnDAtlN85ZdGntM-p0juOtRiovqRaB6b5CbxaZrB_ncOueugzF0aWu9Nl6mWvxT_g768K9hpb5Wm1Vy_R6fxZaMexODXJNs9fiTRFfrfM-qMs23dAi7mpkKz3cnzL3SZR-ATSIk1fvkJFjqFSY5ayJ2g_H2iwCk-LHR-5OaXznDlv9trgsH4H0ol1P9ry_FJuUHsX9OzMmTWZU3YprT4VyHQVvSIM0qPvI6X0oRxirA3tTdAG7ZkEB5r3hqSIp0roWgxIJ6wSX7G8l2tUiN8HKe0BQdkxjkPu9yRULhQI7BGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf02d7939.mp4?token=s6oIElwOm4JlLvqutSKPbwQlHaA9RKUIOHtpSl6QCnDAtlN85ZdGntM-p0juOtRiovqRaB6b5CbxaZrB_ncOueugzF0aWu9Nl6mWvxT_g768K9hpb5Wm1Vy_R6fxZaMexODXJNs9fiTRFfrfM-qMs23dAi7mpkKz3cnzL3SZR-ATSIk1fvkJFjqFSY5ayJ2g_H2iwCk-LHR-5OaXznDlv9trgsH4H0ol1P9ry_FJuUHsX9OzMmTWZU3YprT4VyHQVvSIM0qPvI6X0oRxirA3tTdAG7ZkEB5r3hqSIp0roWgxIJ6wSX7G8l2tUiN8HKe0BQdkxjkPu9yRULhQI7BGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از ماکت مجسمهٔ «مشت‌ گره‌کردهٔ رهبر شهید انقلاب» رونمایی شد
🔹
این مجسمه قرار است در میدان انقلاب نصب شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/436706" target="_blank">📅 22:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436705">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7ClOM7FaS0CD_BtZW53HF_2_PG0J83-wT17Q3oxv4GaHegshykLBVoLJmF_sva9NDEnpF0mdfbbq2ntl9HPQ48nrdVGngoEVJu9XwpROOQYb_dN5d4GM5HBAbNjNytWkOA16fxHmZHIJbRYoqVPGm5jtIcSDFqEhGpWLrBKDP3GCTTmXo9gBCYpN04Ae8488x5Nt3HyAlQOzOUfxYTT8pmkpELm5lqdNzuIwh6BMnmgfuKBQnsWAS7MeAe-rSj7srlNHDh6RTLCuh6U3ZjMix6bjHY_Ugu_srW4yVbyM518N9Yf-K6sDEF6T7WdaYxkPnruJv49zHicB-0QVLsXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردوخاک در تهران با منشا نامشخص
🔹
مدیر حفاظت از محیط‌زیست تهران: باوجود افزایش غلظت ذرات معلق هوا برای امروز و فردا در تهران، هنوز شرایط اضطرار گردوغبار در پایتخت حاکم نشده است.
🔹
جمع‌بندی نهایی درباره داخلی یا خارجی بودن منشأ این پدیده هنوز انجام نشده و نیازمند تحلیل قوی‌‌تر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/436705" target="_blank">📅 21:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436704">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmBk-z_ideA4mUe4zzH3wDhLrG_dRIgqglzw5O10vex3VzU84CXa8dBZ1Hr-l0VZZL_bb1I7YwDPK6gng6R3lz1acwJTd1aUQOlQsNwb9DWkP3U4Fg5WLES9Hrs_pIWP4B0CyddHKzwCN4NvMNwN3owo4fgqU1BjeH5hapdCRARbs8GCMQH91BhWMMOHxkregpVb2GgxboZVaRf1r4VyyZP-TGr_Gdj0QjSaKtmoWgBcqPIQlqSMJVxF17ac1NNjC7wlLQZGsUFLexmlzrmtBmH5mdLoMJXG9TKwOoBQOLpK-e36pcJEmk3gxayDfXoooX3D1cRIymQ5ZIJRxlWW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کنگره از هواگردهای اسقاط شده آمریکا در جنگ با ایران
🔹
بر اساس گزارش‌های خبری و اظهارات وزارت جنگ و فرماندهی مرکزی ایالات متحده (سنتکام)، ۴۲ فروند هواپیمای بال ثابت یا بال گردان (شامل هواپیماهای بدون سرنشین) که در عملیات «خشم حماسی» سرنگون، منهدم یا آسیب دیده‌اند، فهرست شده‌اند که شامل: «تعداد هواپیماهای آسیب‌دیده یا نابودشده ممکن است به دلیل عواملی مانند محرمانه بودن، ادامه فعالیت‌های جنگی و انتساب مسئولیت، همچنان در معرض تجدیدنظر باشد.»
🔹
چهار فروند جنگنده F-15E استرایک ایگل
🔹
یک فروند جنگنده F-35A لایتنینگ ۲
🔹
یک فروند هواپیمای تهاجمی زمینی A-10 تاندربولت ۲
🔹
هفت فروند سوخت‌رسان KC-135 استراتوتانکر
🔹
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد)
🔹
دو فروند هواپیمای عملیات ویژه MC-130J Commando II
🔹
یک فروند بالگرد جستجو و نجات رزمیHH-60W Jolly Green II
🔹
۲۴
فروند پهپاد MQ-9 Reaper  (پایدار با ارتفاع متوسط و برد بلند)
🔹
پک پهپاد MQ-4C Triton (پایدار در ارتفاع بالا و برد بلند)
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/436704" target="_blank">📅 21:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436703">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb0707161.mp4?token=tsixSiie9O1d9bE4_2qE_fuRI8xxH0e773sC4WaKdkYnXmYfBJqouV9gvEYsGj1s5oz0oZ1xiIBpPgrwseCEZ54Lq14SwF1dPRfYpFw4Pnv4fUqUuPLfBKIOZySKn6V80zGgVxve8uSn0s_rVnI92jRJjNDvOB5jlvW-f_u0-26cjD8EgUHlYzX9Zi9GSi3mVMmx4wkOzo0rV06Wk3XOdE5NB0ut51_r2s1ZbDZDi-uCJNDX9Jgvy8dmjGoUhLiVDo5cQ0WsIZDlRkGbR0I_3LCV8vbaIkTu0cftyPK__6Y8VvlXp_nrrDdOzteXDV6y__iVOyomoyvmPfNhLujvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb0707161.mp4?token=tsixSiie9O1d9bE4_2qE_fuRI8xxH0e773sC4WaKdkYnXmYfBJqouV9gvEYsGj1s5oz0oZ1xiIBpPgrwseCEZ54Lq14SwF1dPRfYpFw4Pnv4fUqUuPLfBKIOZySKn6V80zGgVxve8uSn0s_rVnI92jRJjNDvOB5jlvW-f_u0-26cjD8EgUHlYzX9Zi9GSi3mVMmx4wkOzo0rV06Wk3XOdE5NB0ut51_r2s1ZbDZDi-uCJNDX9Jgvy8dmjGoUhLiVDo5cQ0WsIZDlRkGbR0I_3LCV8vbaIkTu0cftyPK__6Y8VvlXp_nrrDdOzteXDV6y__iVOyomoyvmPfNhLujvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتادمین شبِ ایستادگی و همدلی در گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/436703" target="_blank">📅 21:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک خودروی نظامی در شهرک القوزح در حوالی بنت جبیل و تجمع نظامیان رژیم صهیونیستی در شهرهای العدیسه، رامیان و بیت‌ لیف را هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/436702" target="_blank">📅 21:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436701">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
توزیع مرغ منجمد با قیمت کیلویی ۲۶۰ هزار تومان آغاز شد
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/436701" target="_blank">📅 21:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436700">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thmkBqwvzS4ciNG0teuqHoKdgl7u7GDbYTPzl_IObs6bGSyOBXtTpUPwe32bfYWxE55KyLeSjRZbtDdpGFu-i30qVPyxpn3tiSB0cZYpCH4EciEWVlnXd-bz98Z-Kt2DpuVwd_RPAEtWn5trXFIZp56fVlx2NLZGmPe4oAJlMb3Ga3cV6J4v0Wkf8gcv5suEeDU3Ihn_U-VJLHwlWpmozbKT4xvwDYwW6qmEBg3FB21wY9No4UqpO3hfHJHCdCxbykNoWoDDkxPFi4LfEPrp4oNGSF59vHE1LF5R1rOjbDN48GvZLtwxJtCZ9W-CpYdzepZk5siZNjAoImjJazgNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ۱۹۲ هزار نسخه کتاب تا نیمهٔ نمایشگاه مجازی
🔹
قائم‌مقام نمایشگاه بین‌المللی کتاب: تا چهارمین روز، فروش ۱۹۲ هزار نسخه اثر با ۸۵ هزار سفارش در نمایشگاه مجازی ثبت شده‌است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/436700" target="_blank">📅 21:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436699">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎥
سخنگوی شورای شهر تهران: از فردا مترو و بی‌آرتی در تهران رایگان نیست تا زمانی که تعیین‌تکلیف طرح پیشنهادشده به شورا مشخص شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/436699" target="_blank">📅 20:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgKFDGIIglEZ5bCZ3ew0CnpdUAHNws1uTHX6LswU00V6LhMgiMSvnDfGGAUIQtqUB8y09TDY4kDaJDdeG9YVsHkPNlTnNQOZ71Sdpcw3CUzenCDB05QxV8V5ijlUGX6cVQ8M8pnuo7Dacnly6HYiyVT7Ki8XUREj2wmfOSCxY2DkpKk1Bg2Z-Pfx6TXkJ7AMDN0UQeXf8L4PTBx0zUR58hixqVaYSX5jy7AppnVAvzApSNx6o9sOiEGTEVBC3Ew5eqBnlv_266tmtgmCcV53BZGtVhArcujkDBNaXJ_TIpw1Sl4AcxDXtKgEiGPLWCcayXyU1J9jDodJuPGkvQJUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح مشارکت در تولید سایپا با قیمت نامعلوم
🔹
شرکت سایپا با اعلام شرایط مشارکت در تولید محصولات خود، اعلام کرد متقاضیان می‌توانند از ساعت ۱۰ روز سوم خرداد برای ثبت‌نام اقدام کنند.
🔹
موعد تحویل خودروها در این طرح از مرداد تا آبان سال آینده در نظر گرفته شده.
🔹
در این طرح، خودروی شاهین GL با پیش‌پرداخت ۵۹۰ میلیون تومان و خودروی پارس‌نوا با پیش‌پرداخت ۶۶۰ میلیون تومان عرضه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/436698" target="_blank">📅 20:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از کشته‌شدن یک سرگرد از یگان ماگلان در نبردهای امروز جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/436697" target="_blank">📅 20:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdjgXFasIbyUTFsbT-LM-Hb4-GWW4MtNQx2JoD-4bvIkFJE8cBAk7SKowjW3i5hoEDLgHCfGw3nyKGTUPr3p8T79ffPzNUp-R7IVMTax2o2DnfDGeqvXRThNuId0raDpj56y1eaQLzjXEpFqhGDQm1C_vcn2a4WHGhfk4VVVLpdH87qAT8GgxzTdTNiSTT6YuBj7L34FbEoI5_85Sqk4qcOa_iwkBgAJYj4UjgOHfMy_yD4mTDXy4aNsDPnDoFdMJSxFCvjhmbcFzNRmAfFKk1pJ_MwwvZjlt90qZTrpdRkUb0-55hkeq5r8dHluPyzqTh37479KUTWtEiqkHSXBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای شهر تهران: در حال حاضر ۹۴ درصد هزینه بلیت مترو از طریق یارانه‌ها تأمین می‌شود
🔹
پیرهادی: اگر حذف همین مبلغ ناچیز باعث شود شهروندان بیشتر به استفاده از مترو و اتوبوس روی بیاورند، این نوعی سرمایه‌گذاری برای آیندهٔ شهر خواهد بود.
🔹
افزایش استفاده از…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/436696" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrLosvKXTIpOkl1sWyHKrHYpCWedumvJUR0m-ea4kd8eAPMXM85V7eNfhvmm5kxMpY498IH1-HFFHzwTml7JB0sARmNWrYjhyXOrrRz_n0bGGUFKjLZX83b2dez7JvROKIPr2F7FDOuUvIQ157n9tVvxWl-9DRMh4wb4pxcC1oPxug6NjUjGozsKF31oRrlaHxGLrzE6momiaV-66ylpac5gNSA8GA_HMLwlSPIeNy1RcSr6xFSoC9jgae8kIlH0IwQleLsmcEEQUN7px61I7v6GG1ni-PrZZe5mGcl8Js1zct6xjdDrgikc-_JDyti-pQ4LwiP9U-CqOTABFVjt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436695" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
