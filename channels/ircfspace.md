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
<img src="https://cdn1.telesco.pe/file/RMgoA--2hf-N1YEYDA0RZY5vqAsKwsemiYEgEpWCqXkcRchZcWW-OMfjbqPzh4wuDumtc0i_cPEUIGRwkXAS6KpmHaju4F_wIuErOsxa5RDGzpvd3YeJzrP7ZwpksWOnSfHYXmro5jriJkvl9y0XplngneMP6cOQbR744yJUQn9dFOxluoCo6cAYL-clnTTprQMSuCprmQ2ado7trEAWPB9iOM-9QhzmUrt0yRqbYKRPcWsqmhxng48sRGuFbLXffzc1ypfBNsRisyAnSckF05zqiDNkCDG_TMdHRVymEWh3fBQoMFDYLbiRKHBGKfivxHqWRda2bmeRICcaxqJxcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQcx3spuCjvpy18gtd6z2IGU1N7RiIG2d3mkYyeysDNM0ilW8dw7VMeyDiQJ_yddGsC_AsQRB6HZzNeU7ehnOcggn3pmniK3jFBHCTUu9tSj9U4cEFPWmupNpUEsDaAEgYZOfoplZwq-9bZXeUE6VhSpbSGcPvffgjV7smeFeZyYPBEmOfXKanBgoqDPmbfkZx43Osxw15chUL2EWqR-Tzbr9-VN26k2etJAzJ5r-29_Z8XW_khG-ViRIr3R1Gd9DJ7c4_doqlRnfivjrWUfYKDW60ceYSKEIRVfTQOjpzqcuZ0o524VXIzcwuDufYdF6-ZlWA_X5WSlWNta6rfS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r31jLzJq4rEs1dhzvAgXEedg03j1OqODhN097HTCnVAOl-Rs732DayUFj2Bm-NrcWKp1CrRApM8XcAg8fRkke8skgUobTg0uZmG0VM0qNnOEhkKUmMo-YNSc4anyad4qwpekWNUMx3u_c6QKVAk8aE25vAxyMJPSIsAsqU9qBV4mhSgjBv0leTRlwiqH0V4C_r5K9Nor9nAdB6QhlzzulDfIH4_wK6AJy4yf1UwHoxPKCTtB2wqQxfc98pVQVGpDuuFhzZXuafuDZK9YFt9PAYz25y7KpQrFg_-GzEjNVQZIYayxeX5UQVxUKLzyf8LXk-wVsUqHJNW9c4vBxh60Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSB_ox3mLwiJGPOX80yp9sEe9wcrWpikNmKDaUzNXU2PHArY8MhEn8hMA2Zu_Y6XxLB3tZ_Ln4VQSVwTJdyI8McA2ldagItqx717WZwMx2nAjnytczPqMmOSBoBZOtaR8qQoAObRs3dXWM10UDo4i--20tVLq5Gqr6w_WlplC-ShvOxOZufSjdF1qUh18Qc9eMNGAQwaETUiAX7QYAN2ZtW9M2oAxmpW4tlzzWHpxB1CldhB87L9ENjryVZX4ndHqlrDrB-UpplziEK1Yi2pj80TZknD--kYhKUA-UgyP0mDnCplDECjm9q87yOrqPaeI43k8K9Vq-IoQx8nEcy7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H8R8_SY1rp7cXDuvp41xWAaz83WJ8wxxa1OJfsRVOPdl1Py42rlSUcXm7vlZw2fBl7C-EWvsSdGYIYj5JjVsAqrns4XukWeBhLp2b7cuZhCuhc_90D1SjkiGG82q_Pjx5CId_YS0dzWgHV-2fiEM2RfJCUVJXtCADv1uWqW61PmnNgZcRns_WhiAaAodnTIjsIOjO5Wxqvr2JPjDxmJME5Vk1fTkwNBim1GbSrPFRx8qmkfCO2cfJbJ-9fCk1ZS6H0w6nOEpBMHBKIlslhHXpxtM3ht3dU0aRlz6NRS4SGIzDnfzMTLMe0oAdDsE8cbFAqUeHEY3VE-3SNa55_BQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N3WjfGS-kAbo-zo3aA0lNcjaMgJIZ_RCEr86YW3CxIpICF-99meY5RS78DGm6OLyGQsLU4wiT4NvZ75R1QIHlbvg6ZqKz-e62pvDs7-7VnpESdBrHbXSshGQhtP99ADxNU3B0j0ONCZ616583_8dTDfrQYp3_3wDAE_X4LMrLfftg_xs8w0TVnKN_AxFSePoWxfD88P97cyHoGIFi8jung0OjUqU3Ed8j2FhAboOa8nclfPbPCPGPIZN5IfCd2_ek_Zg95CZZ6cfoeoYtAft3BuWcM4ul4fhBzTypbvPhbse04LyYbZbOy2EWKmn6QzcMEhkMlsRgR1VYkDi4QWEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BLrwIWBwJfI3BuXEH602rUITkwSqf4Kagkph5ca9COflo7JiGQBOKhXsaMyo7erFFi8Lbp1Y7huPv6LlBAuRT9Xfe8mWTuSs2EXOfFA8PTSe9kyYhVYdhH6UnzEGQZ2S-TbKP4fI7hdMcMZbsbbQyKSO4rJfk1Y2uxR9UC_vV4zLC1atUeZCHQy-1E2t552jwL1RJqFpAXxRxd6zyMGylPBmNRXVX5VglYBKXuZ4CjjXSQcBK9lHrSlU2xx98OhZDwMGXjAj2AC-9teY0r88yCe_S8Wa3jU1QMslSk3D7yssJnFywlVwQGBEOKxPDknV4Eg3XSB8gsEFNEOukC5XcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYfXLOdety3rpVCn8-GhtpE2zbT8NDOlnMU3VTsDn4fBoEonk7jGqui8XfbkvbUSDq9BIvibnotOP-PvJbJ8CwfzU-zuH4DtXB4Yy_oPdSiFI-t_a0FaE6aN9YudzF6u9pnbr7pwUkeZm0NvEkfKtLEVrrhjvTURkJ7aLP0kiuseBSSxPn-6eDSfJP9m_EhbrPQ67ZI4wdTjHk5EXS0LrxkL6DIL_KvGLpHhUuBFCguTfDfstlUH2hNM7LkBLyxYUci7Zs8n25yiCJMq3eUAIn7_X7MTw6XmiYy9XIVuJzB92GxPTm168-b9p_7QX4-kSHuCml4_Hfo6h9P7CRkcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBxQHWIUTNMTW4tfT50aUf7CAw9uq2aWvGi-sq027d8wmQG28DHUq5MhBz-LjnCORrflbUA0hBBGR2sOn4RxFQ0gAFCQdqE4TthpR6N9Ei6cRWZuuBeNxQjZm_4GVFL1Br67q1CnIBTskik3k2LN96-tUIS4XPzA5wn6RiasuBcRrIm-J9yNARlLKnTx4_OXl0JjqwJyP4n2uA8kqq3oQSyjlhgzCaTo6CtZ9ABRYlIpRzTnWohEdxVDihxuCNatfVHZZozClVeBLp796kjePuei2xLunKwy9MoZYWA8jzR2tJ1hxhdf6-aHu-6wkxvtE6PzJV3FOlEebpBjAlVRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XW5wiHQ1Qj5PLtNJrR2bN-8YUrqlUGYTvZTnQPQ_4f87IdNFbGw19D-qiIuQLIIKEsA0N3s5ZoJDHN0VIrOuQFPnlCCuk4q9cmg0Kb1zgBKl05KJBDjAkGR_dgTpIRwVyRz1iYUWP1XZ3Lm83FO7gJ9F2ds1rZE8tCH_f8DaDq_Q3uN8oEIj92NYuxKluTtV8UO5UoOAXfiLFHKYZRpEQEPPr1NE9Blku_ws3ka_LViwCFdPwoVHvGaD97g7jln36vx0prs5lE_LR-hVLEbXRXXmWgRJZfvRxK1PP7ZsD8BXdfVY9gMfdt4cXIznkwxG1iy2wtVzlf1x4hHRMnwlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfpMKAGSGoUkcN9KSxGzIYOAY74f_65U81TsUafIUjGpDXXNZif225EphAnskjL0e0Xf3trgdepiwzNraYl6s1vQN0uuNQQ-u7fvqGSrQVarpz2_Tp1ugAIEJRt4klXdO6RPI4k66jsPBG7TsXgewmJ_pfYTFXfrONZem33GzWGgekoHbFeLNk9Q9ZdGyghSRzSKA4kYAJdFdyB7r_i4qUQfjLtS5rLQNx6TpsM50aGsVAT3cfbBC8bF8F1PxlR92-R_aokLBkcR7tSTMZoqM3knNUwhcZymbpkyYB9f-3ZcdtSJIA2z9yk9d83_EuyDWSwuIkBi_YFWR6NYOEnZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HuM7lUJpb7i1Toj9tPBZoRQwX-LBgHQ1ehzYStPzaraQh08tzHq1JSeCQzxHy8rrLcqXzZpDYWm0457H-3IeWGq49JbXadrs6xonxmh3ag5ULAqx8N_xgMQ7bMikar8R6n3vwn8d7HlfNwXc_uFPOfziupM29VdhpzEzNDGtqsT0ykiWqphDL2KskdtHC-gfsa_Mf2SSciQKdGyk9tqQlMHwsP5cWFRkBtby0zaBtyn2OaSWBQOJ52Drf0H5Jl69aZoucyPYtWDaO4jhSoICyaVdFATuyfIPZR-UPV4aPKly1ySM7qdHSvpSsZPyavLqwBxabNkzc5_CO8kVzqo7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGjAANQKNWYQuaX6Tjvv-zNDOypW3cuoKHhRj1yB5A5OKN7XhqU65vWasmh7skEMwzcG8RyqB3Pp33tgtGj-tAtyBSCESsotilpyRuBfTpfCDQHac-zIbS_fnxYVQ_3q_8GoZCbMNOtP1AfmYF6KhfHMCsw898yh2PgPH9qLsg9TEnbdCmiY9fBJgtqgneqF4B2B6vaprF_EhHngazHrADn1NqMcAyQL6lT2YqVFxrGNipV8v9RUIv3B4TmCSzzIdHdwzVYqmHRu3U8b0ZND55vKVFVI4qzMzcUlJ0RfxJ8ggA0pBcLrMeeQSKtY8Abs4jRycRADyu119i3Obywpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a3WWWh8OscO51yU0xrpWunBc4l7JZv7tSADwJlNkDwLdpwPthV-kd5vIAv-MR4aA5OBg4CPYIjGrCBBk_s72tsrO6OyBSwjcvHU2JGnVHzx3gUILqTogKBEnudh3bdQ3HGW27sgqY7arn3oj6NPp0mYdVKRdwvH9W-3DjkyU3YKoRENvDzgfQLDJ-C2aBc8-QxO7bOAEu76GCHoWlXlWYx_KD6z9vmcxNoOM0CGFmcfIyOv0FjdBJtmfWJ5L0WWb7hfeV7CFZF-2A8K1Js1CxkaI_tDssHw0Fq9GqwR7E5xMHHJs829jiGAiKAAKZez2JfgNsUJMnTZfjQldmYj3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l6YWid-42uliLahqAuM1gfEwFjKjseB2HVNzqtP8UYED_K9vH8Ny2x-PxYfF1FJfHWUdeiOl5Qaxp3Zq2gVUk55z-CdT80q9_f4tNSlyS4dBcWRQ2Nim9gID3L4n1B43GkohxErtBDYKMU41648iwnx6JsB7Lzl0R8UpzFV0jq9oT1i1iIbvoqVO2MTCp7-vz2LdFuf3R7lcRn_xQlXt_HRJE6iOcFstdF2lH-8rmaE92aVjCZxuQFC55ji0J0HWWoKGfxt_wwu0bBw9rEUt3Is-8DDyOO1fA95lXbBgmNyxy9CltE7Di0FVXk6dNal1tc4-vaAVLdPFxHGW-drIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bly9yNe7SMsH2lfovknJz_g3dxeqpdsAmmrmWaCfffZuKYjy1hrGVe1dPnb_EfUTn7GrmbDUfeJ-Kd6NxcokxWUMXSVTz4dxcIxiKh68H8lV3SBd82x-23awei6KATpNSF5HyPbiff5a-fMK-iCQAws4G6dPSM-0HAqJ3Ns97rMo40StZl2vrnfpi3hZ4QCB_C8QcPvstSfSR1Ur-lHEtX87JJ0WzVELFEHHrup-zksUOLnnxYjDitsX35nxL6D9rxXW6YCttpZTHlOW3c7jwzi8bVPWEvL-UxyGxS9YuDjix_tbKVPqSlm1VT3kbr8zcIluoH0WYDzcTWTmwlv5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dUXUaXhH5GEmgJyREl_6oKICf0_O0qFGaDoMra2-iwZsZQb0_dWII2jczLe7DpQQXJO5BoyUE_a8Y4Aya3MdvfoOuSc27ErLQsYfjO242mD-xSTFKsQJS0IzxHUk2BaEBzKKGDjo5_QxDcZs3JVqERGy4b8v-oEGbX4Izj3b40MSZ-tmMXADnqMw1D4NjQdBJZKrCctFUTqK0aNA_sdSf6rbfs0qFal9OkhWIuCM9jFxRTveEAz8uPk1V0qPj-qhbLwdv_t9Uca-Dp8bY0GZlMGkT_xJMrGHgFWdEjr042GFhQk6BWGeZb7NUxgiQjwgelcS2h1a_QY17l8M9oanyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHzouvz5-bX6Aitny4biaRL7bKHGGV0cnW6SRFn3hd4-IyAsfi618vBoRPryQ90EFZ-YCF6t4CvE7c30O375OpQIMlsfLzg6dQf-fO184xHWzN627mGEyS51zHFuJ7A6qRRl8BdJQVRDyr4TftkJ9omHEVj8GZMrR-0Ipj7Fuxo-Rvq-EhbZJDIbhPlyeeoT5JKRtOanMVBty_qhNeoZj5KZSaA0ufOiQSALkU7gkbZaFXtkvgGZY1NZ9Q7l_aQxBJwPQRN1-vyEqqbTQTE_Wk2FuQU19lvPRUefBgebjNy4_1zcu6HVLwp5zVuyYqoaAGOITDPp07IV5Mz1gTIenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hghWc98Qh2lu8MUzm22-ce6ZZVdDKEI2QlCW91XfzGrzpOAgMF51Vrf5GJL4-4MVUPhvhsPaETTMPJP9qN_mZ-agjU3NzGZKBzhXqrXy5k1KRzGl5-BrepeNXrMxFLAgKHXs4En-mliiv6QDh8FrkcbL9gK8D6Y0OtVEiLfok0PoYOJ4mouIzjbnhg7lIpDsJj27MVEuPifbXwCcmYbJcvBgSQsXJuqy1BaSupq49aGDCquyzkqjRHJ5W4p_SEjcRQb-8VBEoa_40LH3wtBTQQ7I5-ZhbO9iuVjL8HAQyyk8pyv2U3ReA5xGqXg4qrLC6r0FU8vQ0Rg83NXFOdbINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhIRP5kvh9nx40i07DbOXbG5GKFKinZRNIrOtC-SU43dre5KIl2IjdWYvXlPl56-sA_x5_Ym8AOHWYlR1QB1OZTEVuL2mUF-toWw3WnecA5QxIQq--NBT9rWFqRmizQnD8BEftwSc-vyOk-9tTmf-li1Ecz9vkgVe8cVMdgbuB4He0Zap47a3DA4Td5EnpBFj5hctToo5e0U0AOn3m93CFyd4igtEiCpRqn245rGxo_hB2AcU5ZU3ez11SLgCj_jBBrLllCnXljIE6TxVa5JX-Fp_xojok07jMmx8zKaYQ3ksxTSWCwJbTuJ0NNt0gLgkl2Uixi03e4x3xYdEM0Riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4OvJnIjAUFoiu39Eanw_3GQXgTCkpNYIe47fS0zIVleRBtDuPl8xCuYYcZuFeYr-C9tbNNzFK5Fanpu5pcoX-erNWMs5b3oBqI8CBeokZxKyi1FA_F72m48tNOGGgiT2sN9r7eZGNIP18-3DekbL79WJ41DfFI9TNUeLS5BKhWnSVsVsJpFkLpMKr_eMXIKKIaDpR8PtUeAk8Fgse_77IImx0ixRQPJgM0BIcxL_EOVAhb4fTpHfYo7WRvt6aYTmLf80h8zdZoe-p12SmNSZith3IbDjQLzLA7nEpqwxZtYmi2h2csJszMKbhLe2SEoBem_RD0yV6VSK5bUlP7p2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vx96dd3eN7l0VVXgs8MdoI8Qjr0w4DuLNk0AvRthRP4n0F0Ibz_GN9FLzpeKsrVCT6BflcHLsFy62L5mvwHb33Fm_9Ahq8ucISNWS7iKD6plULYMS7VEhDWFa-qMcHIZpO1d5_1fd5qmVEjQo9DnPoSwCIDqQVYAhuaMWU4vvoQcYNr3oyeA9AlodDddFbq1QnoGRjpSkTm7eYE8crTMahHDTHeicxaAzh7b956pydnVabqMwp3zXtB8y45c8xIb2o9gUA3075qnZ4dPNDxQYLsvZcwWxiXKIMSdpIWY0R9BEERNvvshmTur47j3milSPP3sKgo7pQhCsC1kHGWNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPFzoMCYtsZo9oEvrFDHE2E4qZNK8iVhvgxd6dwXhsYqLdCbAMYCqIbp9IzXqxaiLjjSjUy1fYQA3N0vujLiPiJWn0UP9bbgR68DtH3vCkkWtdwCguaFq8W3VPZ5fi_LFg2rrULPqn-Nq_mJC2Vp3zvAG0JBN1X2KHRHiGPQXFxfN1HAYwok3W1uhmpOaYmt8Bi4-9Qq9l8MKFqFG-ejvjIpt0uaJ2smabKJmaj7E3woIwqxfTlD6IMoS-XoYKzNDTHkvhQCq7o9btY9mRxWmP3f0yZOuxRbiFxjaQdVgOpmKeVXDoQp6fvCV50tt9Gk5ae6ed2DS04OYGzr0Sq1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BlXBMDn4ak3IF5_C_WHnrdQmN8BCvVE20iQw91iynJ56SBRSqmQ3A7QsIvZujwLbRkuPM6tREofhuBpW6GGcWLbmak4W1XCW18xERYVGxI970HbqiLp6QMaGhotwIUyPpS8fgKJEvFzU-2lHcf_pkhX07rDoGYMe1u-nSZrJ7HRDyXxQDPCkZ5BKxc_xqQO8e985uhQEop9hLkh3WG_XWBn7u8iOA714sYsQxGy3XidML821aze0jNre0Zk31pz959bJpeDLZgRNvLG4l6PP8IeUdEYQeNghJ_stVZAT92wjALqxlb7Cc2EzSBUwI-XGW_kgRV6ZusiG6Ec74PDzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZEcM6KggTojYN-JrKH1izO6ioMetbUir07zS4Lbnut24OmFIR4J2K6P9_kVNjD9KtIFwGCaPA4L2EeYUoW6tF5y_Y-lHXdVVbEUyGofBmyFCrPu4oKidAwE1B-R1Ybh1my9diTZUJdeg25dgTmfGxzQ67DEgt_a1p0AUVyjwq3vcP-_Kpd1kwxAaaqzUCYgTd9hqpTuGuZTfxak9rxXH2OvZRZijCRT0CtvpswBZkCX-Zh3qUJtzKD8O9EAgN3aCw3pDLzv5PbUIHchmzbX7-tKtKaYT2GaFm8PH3_Y9XpLvqq0EXzrYnsoIViWhscE6YdBlrhFptR-hGWdRguqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e4JLkfgOCZPDPU11ZBWxwIJQ6VE8RLy1Z1qASCTKFi54rWmWles1k72zsRCa9Na8ZVyqWOcdGHR19RFiR0hoPwnpj_HAaVgCInFvvpvx8zH3S5V-FT13NRNb50DGCgJLm-1iMAnCSTCg7pTt4NBCMLOsIIFmVvsT1oggF573m04Mmradgs0jM31VBqdpraQj9GbQ-8iBzwsNnVTjBdbET9JrT-eUJit1tBnCpIN1R7rCEVbr9IfGIfZ1bQyaVUqdwLPj0Rb4pAWUcmH5gtPsNSIjyd3WsG4hUyKV05Uigb_6cZhF7zVvhXfGJxlyTiXNmjLTtLL1NNw4qZtxZUNXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=RElbuM9MfWbhFJZY-1yQ_mOCee3C3RWBFxQ6s_P3fVjfXpQS07Gn9cjoclSODgXNqh8pmYKsz0Jr-UQuQhMOYNctDnRc9nhqP4-biLuG3PfFg7Z1OEJ8v5aB8PANc_bdUWKU0rUyc0d87Wof7JvyTYumfu6QX86dciHtLCQ1-UuMCmhl9B2QSPvLoM3ZOjYycRlQq7A4Ymc6Zln-UsH-0hG-5AvwbT0YoG5RfRgxol0lmZh1uRpj8M0_DI3oS323AXRrxqrJv5w7YdOD1GKEnN-Q5FW55e9Os1mM9ggvT6jh2WXA2TcOxL1xKN_dswuA3tMIGnynnqlcvo7AMTxtpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=RElbuM9MfWbhFJZY-1yQ_mOCee3C3RWBFxQ6s_P3fVjfXpQS07Gn9cjoclSODgXNqh8pmYKsz0Jr-UQuQhMOYNctDnRc9nhqP4-biLuG3PfFg7Z1OEJ8v5aB8PANc_bdUWKU0rUyc0d87Wof7JvyTYumfu6QX86dciHtLCQ1-UuMCmhl9B2QSPvLoM3ZOjYycRlQq7A4Ymc6Zln-UsH-0hG-5AvwbT0YoG5RfRgxol0lmZh1uRpj8M0_DI3oS323AXRrxqrJv5w7YdOD1GKEnN-Q5FW55e9Os1mM9ggvT6jh2WXA2TcOxL1xKN_dswuA3tMIGnynnqlcvo7AMTxtpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r926z8_-YRBTvgdLnx7J90hgPzHESHLdVAGHTZgiUNkqB7R5dEb-fhUCtsErCqiU6K4lIZSuMFpvciPiYP_HRw9Q9FVdw0P3DTiqV6nZJP4VLKAGGyYZTum6EmC9dHcsCYYKKZKIc2zxr9mNNxyq4esITMC0Br5mXkrqNlD_aQCm4yr9PccG5wQM3ceSnKYRXEBHlg-XCTICnUJRDSdicC6dyvf_H-ALJKP-vZWBM9UKIdag6Bi_97VHsz66BSJAwF1cxGcLBP9iqlrvdQ1E822xBB0a1A9m-tMMorWCfL7RITNNir8KK0r0FpuUDdNq59ohYy9o0Ubl7Udo7JWuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWKzLSRYsP7kRmTPkVTMcGkLA3nuRzuvXd5Wa62MVWmsoJY0tSwKykuGkw_Bkf7syWztz6YMq6yoZk_no5tezqZHzWg3an9xqzQtjNq2njxHge5MNqiRW4ochlfCTef_UvSFO0Er67onC4v9pRr2Jhc7etNqqcnTpDrq-UT1lwaYHDam_9aEtT-I7zc97jRWSrLiP4Xuxdc7IJO49MmAQwYsVMxMxNnclg_ka8Ekjnsy2HINKA37frCdCa-sKFo25EHH1rMWxPJ6a-W-kRA04uAPlOiOrP9raElxL7xDFlEMp7dbpbENxZZLRNd9ItJbBAESABb-4C4QvJKT219M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BgfnIdrXGyveRbVPKgdTYAM2s3wSl0vkAZ9uWvjqAcZUXikoYL71aBasEslgpXmL53_8ih6gStovQrzWxcx_CEZb84P2WV7LEPFNSyXT83OE0Ho_W1ScoKvvSsnw15sURtMSarOVg-asAoF8bUVGp73uHpIdlaJimrOABBpyEE9MHL6BZRb5-Lrse5UpQwZDdNwYPnl-7P0ziy4DhFIgEPuLzSiTscAwcPL4KywHrHaALu9KumlaS564bJK40xd1WimI1u09UXZhbtxx8PlF3HQeGNelUX_OKWWpKy2WNwE5Wi0JQZ2pV64P-cqvho2f5erbXt6RZrC1a76pdu3hqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSaGF-YlZSlKMMlU-A4V3ojy1_p41vWNm7eR7ZTnb1PbIqOC3pAFR6oiEkJe6xbuC1L2uYFc9TcPQVqYeAiCIK8WrOcVOALN3YaY-to9VMk8lN2A1m1Xb3nKwOP3WcpFFkxRXuydaN83tWB1pfZmIFXm4VjwaiUggvigyLdJyGDJzEVcm8t5ZWxOgs-R_qbqxUvOT0fYG1dLkshOD8pgDeofhE22DQlwfAZDg4wylnwsDauXQcwXz8Tb_IthdEb9lkvQnfC1b8aABPlJHOdyCxfLqo-s5lhnYsFmsWVaxWy5VG_CNR28uuauwe1BQJZeAjhu3V4by74Tyke3eK9E5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sI1rjTTJmY0hQ6yVgtPEIbiUrac5B56HhCpgZ0SRQ7XwCPjOa-Caqkc3vLV054yp_4VstNP5EJav63AMtww_Uco3A2ND2K5GBW3iCxFffn7tETl2GDWC0ipsSY9zuuP-3K5-NDZQLtYAIX60A_qIItUs6CQJHWXG-PfYpSLDSflcwQ_3MMdqt1r_cpBqyF6-7wPj_fwV1v5tNvtjhx5pWhZOtvghJOdCY8m32KHgSnTH3AWmDv0501ZMKNvyc3EF6LBXXo7XPl2TSAJKDRHuGlRmTKEQ7Tp8kNjCLALOj5p8P5l1WaTaLI18dlAA0vHrHOVJz55NvD63w0PYbNStMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmHaEvz4IhN7E0yTRWEeu90augcFXU3FZubPVW1wKwGY69eW33g7UtbgD-MtNLVR1NVPW84Vx6IXLdC5G-3Rs5tWd5o50dp0khI8WU3FxlDDXQC-S7wRpSvd434_IF8eGQCv71q6nEhwhqy8mNVWGahffZfQaZCAMDtYdKcDj4UWQWo1c5LF7lBNCQj9ba56U7KKukxOmbErrnTRTDdtE0ZCOXO1fHgDUYca16872KQS414SmqZZx_gK0gxmQs7uHcRA_jhf3dhylwXK86f4_m12VRXLUuMaGKzWMJTtIXE7wfEKWW-TqRLYNrG7lQLq7Kmy_vfC4Ow02F-Y-KRINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CESlGgapac7bui-uWirD3vovr8fPFVittnpHafxlCv8R_wSSuivmShtp5bOTzqX0cv5rmnOjoPjev620SEQ_eiUgHOtyxDf19SjT7kH8LDN14kT6LsPESqlGVxNEIpDNdlG1QwkrqXyX8ssKTFy6p3FmjwyWrp6Pbd_jgVnNMR5CMvEnNCjMFPkpQJ2EVnV-eZs-4e5n1nn9YsDLivY0Htj6TqXYlIUUT10zIB2lgqtVGiwPfX-qhFC0gkVVG7X9AGct18bqKbS_8ke-R6-Yzk52jTDlYANzzyjQ1uDXuurzjl_EUcKsXB-5a5wHUZvdL2X9prT-L48F6-_AqY6AVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILAONWFA5ZW1TVd3tSGiHA6VEP5XBh_cyWkzd71GoKvk1EjwT9sos_dqGLYRXGoPelt0b0SO5xFlvXz3xmvoEL-8o9hwngDsxwGGYIoT3LVVDF5gcShFRnHQLCNramA1_gRtNBoDy90e5GqC-MZWhQLkvKgN7jJqeBrUoNok49KBX6qRPMhsz-2h6m5gioESDOhmAUPjGEgXtIsAUM8JlKgmEt36TKJ1j46XKBTC9LjnYbi3HfXUO0F9u4jwTw52BSojXIBUv6SVSVEHlpDzVW-fMZAFc2Lv6Zqgjo8MCdRwD_sHcQ8DFl8lIOyfzs5vO_r4zSLO_jR-xhHvdoU_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXuhRHa-GP9eObzuShG-2JtPnUdYRiG_XFp4zR-ZOvCJeGJiyjosJcVV4LUBmri-0Y0Qibtv5R2X4TfbLtLQeCCAs9Z2xbIbdocJlNNseLm-SqWU3iqycdaDGfWW1qLxUCRT_oQSFG5e43n_FIxfRpiZF8285qWZpXzof_5j4BlVocMNLV1bJkUkOPpXrQJJi3Relr3ZDab3bJOOSF0n9Mn4z61edoOBfNb4l_eQy-qTgqc-wdri0TL3ClfPmYudjGg-M1YRnx0ZN2U5dGklkwOdJfiWCKgHihpzYO1dA-ZQocvpmEoAS37wxp5-7J0fIHvfq_Vk4X-IxU-jtR6eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ngsmevAS5V5E1sdsJK6NdNLw4x4kA7hSO5E98SVyDgj2T4b5aqwCJnfzh2CZrIa0Ek7uPsTu6dNvtApr6NZhuFgkA_x8FrMwsBxJFdTxuHQawAlpWLUVgP5xoenVqaAgJnChHYlqkxriK_NDHLlsywkk-5mS1fSFi1Vq73Eo5hhfdMETL8NQJtMZGjI71MlU4RIW9X7Holv-B_kL7jjj2pXah3LYmg9QxYlO5oRUIjl_RcZR1lidpMWsgaqkUPkqES0O-WjirpVYRSBvAsqnCkU4SGUiSMQB-drHiNHCkWUskKDh2oSriiFxnabSS7ErB0MFy0l4FrhDN6CuQP-PmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAsjkwRvGrd4uGG9Ax6SXf_3vyyMncnh1y_xKHEJbBpWEQcAYaCSDZKreR66TK1buopRVrrI-LfJ1r1CGPKouX4w-kmL0GFYb81A4Vh09_RL8RCfPthwMwBqNJenrnH4jfZCCOBMcykL8fXHzMR4Dxw-vmFihZyvFfjeWf2EyKuowtmA8mtoxeaSwic1JlpdocH6_Ep9DG002AV1G7heFFoiM3kts_0PzB3nlfOQViW0tGSEsWtO13-fhNYF7kJpmlQmiqRo13S-ANDn0-biVcTbSSv4JeMDjMJe-5fmJ883y-y6zasenEIG81DzKQz8evCCNGJYjaY4FfWAyh6yqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOBd3WJ26GTjO4LOLN8DLvYcCQrixVUdwCtbYNZuMP2688yzix9iC34wsk0Dq8lE6zzsCIBTAHbq6mTVFHQv2UQz6NncmbdZd_cPhzh_JITdDgFmHVRsNX8pLO5IRM0Tf_7jmVWq6jlTeWT1kbaTbf97i2RiPtgPX-Cgvo_d2YzHoaHiOlVzrYjC33ivnOWG5jsq24NJF91oEDvsXYdn6YSbcvAEJ1akOCti8sV3d2IootBalxrFRTaAlBDaLb3w4SnFUb-xU_S0juXxlLfQ1fj2pSXCEVquf3KPrkIQLu28d55DyvtrgghrNfAPn_WGoG-LptGdbwsUEwnN_mPV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDPZpboWWOqtCXDZS2kJoOm5kJWUn6SOi65NCJdZjhFIboL4emmm8la_PgZLP1BsIy1Sm_cgP8H4-ylb82E1eLdbVxSs1EKHiIzhDV6v7humyVP8qV7-nDhZnMJ5ow6SnK1uwDYO7Tx7DA60mUuARirTDQ3zvuUEMIRkkMMzzUxoXfydZAGXdY1qVjb2FYCIz-NRWzrWgczwjptqHzTAAFMcmjKsnSzAKuuY6wab1qGaP002KdPkZxb3wqZ1kzcoF6rgnwKSYNu_2Vnf2r_QTtbUn1fQ14xsRO627auO7slzUM4y9OCzrPo-tn1keyND07cUixig09F44hKduwGItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VEBLZExAMNZShEoN0nXO99scnJqoelLnjdJeaMb4BP4MCVg4v33djMRgyb-mYSs8gUF0Tww1MYVsP6Mexb6pnIQR0iNsxXATUMKrklFlVzGOPb74BHmO1v7u3XPMPZIOqeEtaU4q9vGh4YzLcZx5DtOoGKtCoOZZnLKDhl5QkuZ0wkqh2EPr4lvr-O8ny5-F6L12wYRv45E9KSH--DMfSGav-t9fYl0ZXmEg0V5SaWhYusC8X0PqKxlZAbBv3A2qpg9mcpOPeCWXh6u-fELVI0gXls7coVPuRE5h5YeJCWR4I_Bre3ZRFNUjl6CEzbppH9YXOoXPbOMVnc4iwekO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_EJ281JqNZmpk_3Bw6FnjVs822fY-u3C_J1bqHFUM5ykbSDjpEEptczfAzJ3lW-YpZuq-0q-flgQLBeTH1PclFe5VxVjd2CRlMcBRbfY9Pz-U17CdAvIGsTBBOri2UHobZa7IS_LWsu1AaxH3FHrPOvpkGm6f2l4QpNYfOSr-xNT-JzNu9ps2XYu-OTWcdDwQTVu4b2T6Rx4efFLrvnUNjTRMwKhl6kOF-yCXIIcr9b0hvqeu__fx_4dK0_Xh3Eyta5tRE0H11gazHXeOe1krmuIHLQO0hQdO5rIMEz4AUPsGsrgr3TkUiKbg7iqgxKRt2bao1Z9aRxiErjyHPmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YPmab99iAy3hiqZ5hNQvudI0sNoAndEWOd8aDvRrvplFA--8HTIAt1HHYaMMp7480CriLKNvMV3cUwNwv3pi8EqPEftix5dyCRR7lznZY-UAoxhg9G8ypKNI61RiVpATsTDoio_v83Mqj_D6J5vk4GACxhhAZup-9BvD9jQpIAhp4iiZXdITy1OCTyQgukIOz9qi9FYVRWPBIBxXNg4XZqLc6aFcgmN5lsoYLtStepxWEmGVP-BofX2bfhtWRGOZBfCqopZjhrR-3b96yDOMNWfoRBP0cCsVoDim7cV9UsZEnIXhRGuhujl5cbxxbM8W-pQI7a26DgVlKosWadJwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVVuoDegqVaU5yqBkWdqfdXJAFrQFy9rIvmw2To4IH1AHGSdJu-A-nwH-tpKLab9SfFmGeh-24t2bqsR3f5nt-X6fGzaDmtIIanynGnA-gm4t9fn2Eq3TWXm6Y9n1NEUN5i--HBx87XvS50EDggCcNHGrOn2WBF9oArhlUlut7MQZpu0wVS9hvE5X_-j91Rn7R1EPlqoqc91mPatq6snPQmfyFPEIe066J4ikwwp4vPzemG8B-mkSnvv2NVTQB9QkPuuiK72VSNOVF7rWofprelupTbkrSWdyG2Is8zWrjmY3Dg_lyXHqCAGhbep7T-c8dnaNqhs-R7PUz01udSujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UCsbiaf3NgMc4VKT8JXsoBWUhO_82GtpFlGDiNAkjEwW1kZ8zSMZJ7Y-ntDbMu8V4jfGQw2pD8WTbzgjN4ko-jBpLpacRVy2fwzSxB16076JfsACls4QM6J1yevghvDM6hPhS4PaFpvGcjmnhf5ehewTpHeV3TDsZKu37ZRHnyGqznFs5-6Qqs3MBvZOVM-Kb8kuDO8OzRuhlEFo0uGMarVQYJO73RvF9DF-I9z3KCLFa7EHTmQUDij-5JbESg4DHcHfvZPIxCOvcCSL9qmp5oHVTXIrj2zi-HYwi-Ay230PXuCKEzStoX-bL7-CjFaVOVDJ-0Ek3idqkdwSSvQ-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YE5SS0ZHQ2PiSyFzrZZABhrCO1YIEhBnEBuV57jziNnhxffsmaHzPzmpvhPuGtDFY_zT38-tHEyZ2pFJbmPgpHmqU-RDGRJKkYNMaK1mHseCibvrOmjcO6pKEcPe9_VTTPYnMxicEZUB643NuDSmW42dli4Jkp6A_rAan5diw5P_mvzMahH42Mq_qlZn4PB3NHoLebA75K-_pdklK1ihaneJgENAtu1CtxBf6lcRhs7P_pL9lP_rVeG4vYmCEpWhcN6-BCYF5CRDjsb7o_RNx2MR9gv_BVHEtAd1favAkXZYdnSG8siHv7hjKUamnLIgyllGADSGxXbjthgr11gA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSi3GyC8CZBOGE_R3cclmAaEh51BOm8jMd_IjxWTJkTulb0XMz3xojMZ4n5dcmkpZNXjpKaIX77GuRNVFhWvIKIyEjnPfy0ZaHTwoma3SPELTjy3lmV0QlN_u21Qd68CN20A5zYOwgLOFo7luwJraWo7wnl8tMtadDix9ZU5br34Oi2JnHzx3VHMC6PGv7A0zIIhqakn4kEPfr6hWPZq334HDtqzlKolaCkCGrlaRs0AOzSv-H2-8t2gAz5Jnly6K2HfXZgIM3OfNHMILp9N8Hpjccu0M-9aWgLyRQESkS9JmBYtuBWJJY61xK5nJEHVBac4mdm10giXFB5DmaUX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jMxdUCjr5NA8ycbLVJHC5rHviYF9KY8F0HwH3NVvzJe5C2fbqPkqaJGke0DA1WNfc-dyxjSBkIeSg1ECRkNVVDL9sO1vOiNqRGPxKSDD-GfOjUQocDnuIW7P3XK9TW36yuzSx5-l1fGuTAQcYGclVCYzHy_LBpSzI47mmmMC1276k6fVOwgA_EXORKLEB6rt_y0BZfjikCkvdAhTXyYxkf74FDWGqHRO8mWbCy4vajFLWuVQVdL4G9VnD-lwV5V_q97kasDznvx4029mm-jzYD6wv18Rv-4PyZOzQo_vyPv7kl3CI3lEik83DH5vew0Vo515jbl5qMRv6xcIe9ceGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXd9fJCwcTynh7r7vjFMlLN3h6YvTFXbxZ2cFtlkKeJKflu0oi-rUH3FSIfEltcROLO_6zKWQ47_wZZbedWrbjyX-PsKoBHm9GjrSoexQWENEi5MH3HUKG9b06U_KXYeJwPOS2UWSka1smwXnH8qXflX656B7IoXfAcN9Kv-lAh-DNP1npkadUktlflVYeDe8ZL5rntEzzvgFmBHiIhlPEhqJmKzqlaA0DgRBPH0NxsUdf8Heu7E9BzDR2KgReHrpODSdLr3RCMuVXQ6kMMw0xkBQZgm7kkPCz-ToQEhR6_4TbUyx7LFxFsKKUD_Lg9PaSdHw0bH3i_65Je1smkq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GDz3km3CU5Do8QAZd5muS6guglXpIRlG237pWRzxD4UoP5aZHucI13roTKlL2g9xXnG7KQXF83K-D_PcYXxtkx7MufdrT56L-tofy-3qnIyYJ_GPzTStUWc9UcQVfDNzPgi-I63A1khBepplaBc_I2swqj2V2NCR0HQxaL_oiE80m9gqjnnInOj614FL45q5mDGp_7TCJ-nCAoCFGCjvQWvKupWDzgxHZdcZ3uP5z33lhXvYaHhifEb6NP5YI5fbNcxcUmhcuguDKORBEmFxQPO2DISjj6SoYonzg9PlfNof_WEHVLeP5DrU84kZxKw8slaSss0OkkocjaujAq9SDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGqatvERcDLWuoCXey_d8MrbJLNt8ceg1DTmAQ3K0FqLZXIxChnBIaoyqdH8VOMNQeVENY0eUgbe3C557WffmDK0e1h8SQy0TTqWuBtta1TdcmEhaIYBARcQabhHgmuoJNyquW1tr7ytxQrrir0cvtZaN_k-z1ymWOMMzLbEzrxIj1qLvhRQ7JN6gS8gCJcaeoRvw6OF9MXWAy2AoFGP5zHEEN3MX5DqmgfACocLZ--RDLZxCcT-J3M3r1tYMyXebpGieWswFWCLZ33RUoB-xc0849b56_fvkLgnFDzrN7Nd9VcDC-wKWy1Qd2BlPVSmK35f71KRGuUOT2DJULuHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWyrRnnPCX001C7l5F8Hc1OCjihMoQWHakpL94oYsmjC8qCz867VqxeCuqye_yefqcraSJIkRcp5rfXaFqvwC09yfu39vkA2nO645OBdgT7FyouXTyL-G0EaycnBxU3lEWrOLG4Ot-gPat3xxaSf9AbzAwdtwooXjbL6zTdCCBVjWTkBDOVgURqUeHFZaBB2myithMtVCJ2HPAYce330MoL0N_nlCYklKJalXS1aZM0JDJXJWXZZ1RJ_oNJkNjORrwYRRbay1BjLOMf3HIECatJbI_gnZ25e2tbXclh39lM3VRGY4Zi-jLvLoQSpiQpfCyDuNEkTG-FufesDAflpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6jXG3T_oKdXe_os6qurd82bbe9VOfyds_zqjC522gFCkkihNQPBqD5SiNGRYFoIDVBbAcmn4LVk1wR-GUOB8WFN1jy6zFt-u5AVyv6Cw5a63eBQuNH504jbCkNDBaMFUz1tuC4TsmPdokIccWhuUpzoZPx6npnHJJ6ffWJtCAXnap35ZAVyKJarcldFytdojF04djLSlklFU_dlAAYyhSb4tLM2SxPY5HAAIgf0F9j7WLyiyn6Rk9VYLj80e0nmYpqnbQFsSmHoG1M1TdQKZRD9KHAKYe-4-MuPd1OFd6LPwVF-k6DwZ8x9iJ8QE9eVZ4IZF0C7btdyxQkZsFeo8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUN4o0MiMA2dngI9uT8Xaxeqr1Lbac_SH1oC80b1RMP8RJ1KptJ6qsRn4eBRUDJmMVv2C6A9HU32W1FDxYxMnuqlinsF8KTGha9kVTN9in7_9QabiGsbPAzAACK7T7xMYHWS3tKG9iryXMoepVF6Y4JTDLskxd3drzlAkOcI_NdGO1jNZUZV99fKz_Cdln8wxpw_bf33lUCBxOJJA5t_--tA9IPagbqT8z2AfZ6it2swQCgekKMJEs-XtG2WmPLv5riyc0xgC2810U7ZzIVSKp-Lsx5xnEOV2WPP3T7gEgt_RIKdI45FX_X8jC2PziCtmL8lWB9RGYtuPQO2fvR0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J011WY86bj8GzfdLGLAcCq9gcz0JdJfibm8mi9TXKyKjLbZCU0VZZo8it_vKRSE2SMLoWUDxWxfoFodtuEO8uCOHgNAXRthcfUY3c00K1mK3txK6KC9BRCQ1Sz-pIlFQ341H5gQbxRonejHhCWsS0udnouvvvirKBL3sTHlEI2RkIYHf84vcBp5RxEA5SlPsXUmNlJ9dsjntOBzk-vsiyVYYBlE9uTVcS6rfRh6TQkSRJ2FKxbHIlefpaRsDQqOT-0CnbaEWvMGM-jqgzhEangn10HuFsoM6dREs3ymE9aE61Fji6BAi_VM3L-q-iGGaQVxlm-Lseht-xNsREzN96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lllwcFIgKl0r2rbP4cGBve7jjTYwJAuumQYdpqRuB_9OKFOngJVB7fxe7yordIOaHN9eS-V4aywiF7qBRaKSQfLX37o9glr5ZaAs0Pyb39x2rSz7BMKcZJyI3Zb_Ge8Y7brJ130zajmgX6CfLhQ2Zxbev3Ap4OM71PUv74CryxdS60F3X4_SejW-iyU6RXetk1Zjn7LvMAfjwrKTw7d8m7YNo6V-uE3CCTDdwAgCPD1ER60qKykeVCfWc-1Kqse4FHD4M_0wyQSvTJ48bJGdALIf2LuURvEqg1Cgz8QtS-CMI2DfZOp04u5OPYyH7bm5a2dizU0mRUIxmMQGCHs6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNbDkK-7-Jh1STRWevyCOpjwpf8pZEQLNeVvphExGSttWvFJidB-hzNtA6nX7S54x9EzYY0JsHJnKbYnSbMmMgH0iVjcKTYhdATRFnyaAZCHnoNB34fIUaMlJeYkiULyi9QCKrAvAnEQoA_n4wBLCLAITdt4BKtITpLgT2ovQB9PKg3CseAB8xk9TZy9juer5jIHiSsDy2gWtU-x2TaSsl3KSF4L4rGKrFZArgMbL12YyXv5olhW7nzV1zLFRbeqH4iQsfcEgfUQ1xnG2ek4YRz23_01a3l5EtFdkUQ4DlFosVuRYw-JSR1OLseYVLULjte3oNNPQ0k5u6vvfoXcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kU8q7EWz75XUvTgSSsoRu9F8QJSs7CSEBw3herSisKeTd4L652EvOUYbm6HaJnmqJ1VuphyiNwv-_V3zUrTbAIY-MXAXAbC6PIMz6pLJfUpncT-uzBkorhG3JNRaKzqNwDuwsyd9GrTWVSKucvDTV2lyZ3qjg_passcGROHxJET7xPQtXFGv7aN14ayrQekvpU2B2MvZhd5uGCkzIuXixfgWia2Eo8S4fQG-stLnxjYvqFPPuYVKWZGi8zEY0MoDj8nq3Bi_kTHn2ShWZTvpfaMcpqtx-xI7wKOgTz0NaQD8tmJ1X1kTlgwxrEhapWynFdzlbiZFymvM_YfvjsRa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JsBT4UQd8WuX_kIPsQBSZiWS8D8mpVAa7tsK7J5vymcklmXjxjnOqz-ihNynTVP6d0rjCmvxEwjgnK7dfuorbm3eWbKbEwkoupqErWASRUVD1ROUMdXyM_c-BQz5FyMzB1Y08NG8MzcSSWwQz2v2D237rLE8n-QpUKm1U8cyt278GFirBsyrM8xnYdhTHDTx9jHNyYlx61H9eG2Kh6lSZcDDZ6ytM0KV7W5sCcQ3JvHhFA_B3hHRLlPCscta8amke1hVzyG1t80eEhFcQqDTCBC4DORpc5nrVWuaeuV_6P2XY9lfUy_VJzkVAlJZmLhH5mTw-abVvHbLDlYZ8lS64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2EgR-waykJuYpmcL0TrZoIP6t1kCqcnQkpFHayXGhH8d42wmc6hCkcX2YsJXlsu7g_3bAEyUg6bNVBnFm0oBv-Y04hU7QtGRm0Yh3_9JPhysXmWfA3YQIMh1zE-tDIzJz2L4uNXtcK3PEuArYB79_E3NMLxMnwgvdLPgXwGEIcMt4aQ4_mO0YVL6sIXE8xSztSsgdUM6FXFlNsiN_sRcVrB_gLQfc2ygkM3l8KgrtYwQ27m2qL4o8YRBHvDtLsqhLpemNkvg70r1T7g4Xvsz23bUMUATyCTp8WlTCo5Bl2XFYykIzGxgOJJaeJiaEw8zHheGMPbq3ajbTRuiZlgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f0LUUuwuEaT5b597AbxwyaD8qQp6hllHQpmWMNhnDoYzcdrHL4qZid5tUQuWpYd2UROfnZq_tOpe-MoqeGoBZKrI1fP4a_L2p2Ak6z7XHmBT68z21TNpnDV5VoSLh4aTuwy-Vdu4vDUl9xAP8nzcD4N2VIai8BWOty0AEvWlLnbPxZ-0nYG53Co3grUn-jgfLS7XIJ1XR0E0jEQYxl3jEL0m8vWwSxe8xxa0U1IFKjWI3U6mYxh5zo_c6yLdI14Q1FUbklGJJULqhjT-sZt4VNs1PIqLb3Mb4hqdeOF3zrWNYDvo9UqARoNVp4vJH2yVYjHNxufqJtzFnYoMvOZ0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZzrCBg1jF5_HVIGK9Rr-EBZpbWCWM6gXmzmM7nwppuCEgFI_p-Hys-U-0KBA4ihmyXCbiUluejAU_5Peb_0lxlfU45fmPFOpPex2qm5I7hMYngmNmhNAs8YUYRBi9TI8kaABkZa5aN4gL-iUqKXd-2IUup-rljftbucGbKv-k3WH72k_qic4wnSvOl9rC_05xw_NOZMKzycXFqkt6gl5L6FIslJP3f6Z4h1slRuf-uYGALOBc5AxZMRxwMFZ56bpWbjUc6xO2WdqyxFuSjWcLj6yNj0E8kNz4q36hj5x9q-H6ScmowNh5YOhOh0c4lm6TLkFcTVADJFkQrSwKW0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wt1k-e9EUAonwV-KA47RlvxdPrf7xpx2KNitlp5754vrUk64L-7Vgnvoj9blk5375hKt1fGbo1At3gk0ekM1tmFIifvHA1_CYX2Qt2dPitb7oyIW4iql7F-d9iE4d-f-B4nJpiFly2oYWM8qvgs1lCDrry-RyUlND87aNF-vOBQwrOoE5obheEFcxGXvEbfQhA5zo1SqhNsiS1QPZ-T4X9G5UYAeSWjz3yu9XbP7mzeFlr1orBrAC2BVr_XdVLvtgJNQ79q7w60XyiCge5FEkK_K5Y4U_I6sIAlllVNwQ3kP72ZDvSO3ExP0L87ZfIy7gynwTNKMYRZzw2v2X3YzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ubXarQmCO57d_zxguG8bkpOB3roAaQ8nAkUgc1p_UtN0UNzx2QCMNtFKWOosh_7gGoXG5iemEG91DmZdtHpj43mfA9_nvwYqrD803LvI2ADxnx8d9NxY6sjIPK8OolXluOEXuSe17elF3c62h4WTwEJz1BAUDRExus5abIa4jETaI0AqwdcaHDWU9lSEdzpjZ-lGYPb0WZVPv6LC0W1mDoErar0qccNqip_6FDzLvqP3wP5VQ8RjG8c-hmzt1H7lh6N_mKOkdNVmyGzTfIQ6wtAqdtkixAVUoKwx7z6S96eV8aYeClpIYJSW7QlMmL2VUEpQzeUuSVPqojptblAZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Crsm6U9-iEsIPSJi5BrPWx7miC9TMD1YEFQQcMK8XREBfWaKcQyg0u1I0XTtlpsTnOknhVJIrzdNigMyVGmBRcx1lw_0p3k6iNOgqKnWWr0nmXim7FBuao2mNsPzO7F6HwDh5beYONHjbI1qjOqEB9q_H_sYfDUdfsmVVPbCkaGH2Aih-70xdmW2EyfmwdyFfQPG2SPR_IQ6geEh6uDGEJjujonDUlGE6XLL2YuKWL0VacttQrAU-FIiSoDccQs5AtpCZ2QYVPiZwcfHs0or4nzGMSn22BoTFQLHeBQoQysgr2HF_DTikJrhrkmlSQhxmL_d1a-93_KvO3nmIj6k6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rYQ2-VrgYGZHaGoOBxvGlOCL14gqsTbRdw6z_tjgc7Ge41RAoPCvvuCMoLqOccyz6rL1yuoWwRN5wlq09RJAajTK1IybyyZl2GSeyYMkeuz5izWDkQMUIzR40OtVxdKpBJLXhbZzJmDBWIvVvouQnXE3I3DKrVCVHeYTIRTdN5i2yJaYNmoZyJdbUwBC5u17qIRg3VvaiqQhMLP7hBKUupelZixa49nmrXuO2JfY7uO68Fas_2-5__EUJ3PayCH8oZwm9UynzqMTzx8bNZ1RlUIs19r0iZc0wVvqrYb7X8D9UhSl-Mwx3UxrzmE3MO6NmMXgZUqAipJRos9Ofumwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4VGKWkTpW796QE6pC9rCfl9PC-Bcnc3-IqS_-Xbz4S0dSWwl83HkDouTax_ueUJHu-avQ7PwrCFQg4t6UOuCfOFfstt5DJgMIBzo8FFTVZf_CjGUf9DBqMsAD-yhpt3dM9s2kfnrRoJ6ZzCA4FpqMLDRsE6h7LBu0A-rF3N5y5tq4daNFlQmzLTxjFKgqfqerr0pdDumpXukNlWtwxxBJ3oGaUjUVgN9JKOj6jlZYrTYX3YCMVHmeWxx5KcNKbsb4yphXQCResUZWjfZM3DwXwXGwiE8Mch3Oh_YnOsJuEN6BfJUGGg8CK_DR-JobeviKzl-HIV0xrv5Ld7gLvgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VCf1EE9iBY_512snwPPbzM6eXfPMjUF8eLjm6JyhuInMC0s0d4ERGZW9IsVCAVlpKv9t_wnM0YvBV2_nqs7Eiy-EVZVfGDmXd6p9zh1f1opgGc9u5GtlLeywA3VYTgzXXmyKxjxcLjgTKuJR5CuzilyGNDuj5bfkhg91MEE9eYTnL-kkglAKHpsxLmDRvkHflrnNkc3TON5GMcVklkMQDs-4WSQxhFVQxOTWHcqr6vINdwSpJL2nEbrhqccbtCwiiCqJzxeG8Wlwhi9pWfgwE6bP-vGOEmEiexNveM0t2m5asZYfFZbaUBcbn_ouLOzIrZWfdp5zO3emaa_5BQrSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iffIOJ1eVgHP610zk2zQxzg4MNxidMDNxJFlFzLcfHVXmja15aGe4-OBWdjLiIhQpLPgB9Mbc_CCrcdfRRTk0S4GpzQJzMdCrkGACYPspZlQGCqiNy5BjwWqpB7teGKVThbRO0k3ZEOf-tzmGNt7ZkJYUBYOGT91OJCSA-vrMdxiChkiYJr8QgYuOBQMIJhhfRFAs5m3yzsQY0A431ZokUWdcsi1AUxfiyt4c-EnZF38DuAe95fqN7mi_kehftUcSWa9yled_ybBuZyk97S6BBNvdnE9MSDizoMa5so1k2LbiKjA4YoCpnbpLKNQcLiHjwqPO3cu68l8jqOcEhWJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShEUBNCI3tHLatt5MjhKfKIrUPOIwNwOtcBS9xfvydcX2IxzrrZexXu8zbCAOPxlAdquAoJJKOdkLHR9rg2cvTbAenp66D7_CcrD9S4oGpypu9hl6qpRbrnGyh5leeayclZTQUb3WP9l11vJa5xL1nBA-pGrq_3PPhxIgph8lQuQxQw0A-E_dMR99WOdNLa2n0dGEqL-hrljBW7GgwqnRXtIvNnPRu7QwfseTXDrQ1YQaPi72YR_2rO_ELzJLs81RHKCCJjPLREHz8cIowBdOIEdgj2_xiesAZaFh24NZZNrt9qyjGoDj9fd1p_C9AbQHMp8he9g14vd1RPABm2mmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mHJ0_ECVE9KfZRweTZ4Bn8LCFqjrgzt2_Ey83tfg2TMQ1jYHDFhjo6A__4sKNtMyuPkwPzqhVjf-XzfcBmgyWFDvP2CNmAYxieV5_-_eKxXq9qE-BJjuM7QK6eaEVIyXqZqcjM6IOQF6bhjWVQRVmZKMVom5ags29Cw7tgYiiJzGdsVj2dySAMdo3DKnbZr4Dgu2MJ3HLN6AtK5mW_JT2e0VKICDmcbJJVXgBmVu0sOexFtT6gfMcoJFTl8VwMfQEsX9hK02f-ZKayLKKw7zepxtQT_4EuM41cTQQg5OZ0Sna71IqXTTLMcyoAR_b2FwI4N7sc3T7ll-WFKrLkMoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGHZakFJq-WRU6b0lBVxze97gMn5xXTbZK7Zr_FINxwSFuMuqzdiv4H7iZoI3zSpuPNrxhfKNl5z3hmgdm2cJBsSiUP-zllnMUjkUXAn7NylVv1ggPzchJk5paJR9EDKvWGjNt75InPXfM2CjLpPteJ8Qtja3LLHQnxwJRyXITgNZu5hzO42PDC5XxvrlFSLISXIr51WNDR4t8s00uzqFTiYFnWjOUzU-64au-ReL65YDzkbX0UBoKyi2JeJ-mGQzMcXMRvNTl6ym0ApAOqUeKvMMF3SOhlwZdU4BHyyP5_zkRCy2X_oMpMi_LYRcSUKtFucbEIvVXyWi8l2hcQGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwpqjoCITIyqng8TfcNJcaFnYi6C5XVPY1UxeMgao7tgO6Xi7an_hFcE5tcphwUmGdIn7gtNQc8e0UopNoQ12np0PXw47qJIuobmNrziQTtSy2mU2A1KcjgLGwq4JWY3pC1_9QjlXmyDBVgYtXQRh3_r7KISbE9VOzLxc0nMVdc6GQi0rUgGhRSulPs528hRaaKAvcpxrWmE_hk3E5-Y2DDFS-V6nSg2gOfQFG04vPdvS_ITlcqaVVkjCf2DbONGOEKNDqdT9IMB9OkLsAfZod4BxR2h1ad9zP84OFNGscWByi4s0l5OSHBdkoHi3LoX5KOParD0VPSGeeo7WtXjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZoFlsrM5Eqety1FRPmrtcf5wFBr33E1zZ0EkQ4SWRcva-gcSUYDW-7R640roV_juchWt-cJ5qL8LpU1rmBPgF8BsPf8pZg1zOpCY9lNut2fOoY-LqyzvvFhx6VViLs-TLcApr8tRXdVBWJ0L6MXuyj-_J-kzJdr1tZHLims5H9Me33NgDFd0rsN2Ko9_bMmQuJ_RqH39uYVNNNP4blIr493OkahiRNKgbZ05db-8jP-DjXZ2AJ2FCcChhRXfmYNkxFG6hbpum_HIvqFlzWMHshr7joObfoGN6KjtMvufI7e3Z1ZY6ift3pU6dZaGBwtdeYBuYZQVBBvu9_4g8w7qwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
