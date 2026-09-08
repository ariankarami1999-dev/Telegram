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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
<hr>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LfmMHx2EAF9siixDEr9UkD0vSw-mgKUfOu1OIg4uW6NyIxqCMxkq1kVdpztiOyGf66M404zxvkkWUwqohzphNU8DPHMexwUNtBrpWg6-CUKatDRRMDw4Hnk7Vcl598se_tFziE8EOP3CPogS1AiJV5--yT3PlAXqVjpEphVM8A3BYcVPhaIvphtH3HaF8w67fGOwI6BRnuDM0NbLPS6tydAnqwn2CkAa_SJUKVnXh92uljItN5-zCN9-531ABuKwLKWedx1BKtFg-HM1JJEaZztP49cJzkgsVaWmfXiTRqrfo43H_843qQIMhD2-v0SKaTjyIq834x6R5o0-Tz8Q8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TtUHZADA0OlunlN5me8TyfsrOmAK0USLEGSNpQ5a9HcUGyTOZFs6GS5BIUPL4pxFkzQP3c2nv1AJFMWLN5p2EB7IadCjQk0X9-qHadXpze4kB3zhF35-PkRIHvvibacMHZUctd6Z1uv2ahGOxZrrIdGF3IQvPEtgxaK673TJg7J1J3TC50ktTz8wuJcJzAL4ZlY7cASzL0hDkzEGIKb74e73NCM6Bn5vEh84MplsZnD2uSSoUJsOaVAXgoAjhmJ4qBm5C1CYFn-StkcDR1jqvyKrhZ6A_MrPtUxqWEeu6GSvXkC5Jbq0TORV_d75ygJ0tqZDTzBZxDgbl4hClcFbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7T2KzymnwMqFQ2Bo-sTrn2SLp-gOL5qFifGrBD24cX_zwT-pUgq4aB6bVSoDHB1SnKXi9gYJwG6b2wKCZGqbtJKJSdWCx3Ra4EGGoaGqb1TCkZO3N0Rk_KImaTnRzuN6KriIAGBcIFypiABTVjsA4zXq4jWNDL3DIIL9-fJxRJfnR6DmuZf0FmTUew7apA1HTCNJDy1V46pUBXnswEeMZtl9yUhm-u-BYBULIsh6skUtft4WoK_ZPE3rOBOX3HsRt5oDbEDjGZjreY-eYXwbOw9rYzHdvNLAKTD9fJzAd3oIlldTMNzqw0LGeNt4RsDQ0lovil85kx7gBh9byvcYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RB0L9t4i-KqqLDaFcqyohRVpGupCtH-j6KIfCg71fWNl5c1lq5YzYpIk1xmaG2gjiDyNQFFm-RUC32iZBiquH5CRL0l1NOkDUSIvkJKnQeWnQ9QvehXLZS-N3KbzASCHyFJrv2L_ArGgY3V_isrBuLPrSANsJhxI6kMdbQT05VjaERGxz3rs_pdKeHiY2iXNY3T3MRKDE4INPZbs1xvaohjpM00y0yM0g1tYVqW6FWvYUsscQkdCjFgYtB02Ozp8bCSYBl6WlOTmijwwbOmaBNFrcJI19xQdyuPbmCc-wpxRz7iy9BIhXac2J9AJa2t4GyreNMsLfgEqdOBed2MFHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqIbwJRcWZszwRO3Db9AxEeix8wWcxZ_VnGZWsVzgsGJd4b-eK2BmbB4CSkDhxjsJZlhmzC9CHDG7g5hPU4jBuUfjlGtEF-4J67Ogh6wK3tnJzZfEXcxjKEebAKQ9fR40ihp1zh9fKXh8cFtFvvyt_4ZSFCwJXhlMQjE4A1ZK1xPye1E0CZvdyMZJgBFX4gL7K9QUr1PRwW2d3yCajNhi_c6gB3ERyiYP6Ixv-DjMInT7vuyPNxQH-OBekX_aZdTBAa09SlSUgevCMUxW8Kf83r-GadiPID4rwzXDccGsinbj5tBdgrcfvEIvSeTP6pkYJKCZpLLmOiKLroT2PkQvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oX6xyWiJMLaTs_8rocyC5HdjEyLySZv1opQvoe-BUZTuQOST1lBiFmh1xqGz3sYN43SccePJ61J2u4Kn2KOE3NMzBXNjj5NlXto0xBEfD_Bhvwsprs6I6A3y7yvH8pRMcXDk3ym2Qj6ToknM2Y24oRcSmJZX-NKUFmBWIr2tlcgKr4Cm4-f5tnmgaF9RFl3w6v9WmLm4WexCVtYSvdbCV50cyY2QlW-vsFdtAXk4SF_M-v8pXVo5vw4HzNQ4r-qUyQI1iOMqBAlSIj4l91sZRjIe4c7wMEwxEk_QElLloA8miblVXjTehQxXkIVOrvS60J6oGxqyLjRdK2yDeVTVVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MmJw9vg1OFkR6lxHH9ItN6RyJlUR2c0eQl5OhCg6LcMbMOFEclFWS6o150YahPEYOIm8JSLYTKXi7RutbjM6V9QQkGHwn7v5yfPgSWE5_LYgn-yZzFT4ut4PQ4JszdpfKE4iehhgSOh-RAjJTa_Fi1dGz6x-PnfYGxjZY0wzr7IBaVgji2jzHMnPJn1yRLq3upFm6_bdx_-Fp7BCoHK_cvXAykhBnWUCZ2mYLhNxywEuappBw-J3xE6f8-1rqGJ7QTQZubhGGWbMCgfna2f3ek871fy2akL42fOjOQWdf6oM0N0AIcjBNaP2V4T7i-dFcvkzEw_GHB4qx9R3GhWdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wCKVpuo-Ghf8PGzr-d80AWdJuASHbFF5T7NNo9Mv_Q9CT5X3USVycjpY6yTW3cXHV24RrVouOUTIS8qgnc7VhH04fbhUmN0oSC3hfVMxtGupGK3Cwk4mIhKNFcou4uRTRQiOPeYln36FwchfhqgbLLt7a3XkEabyOzkb3OMIPeBadDrPpuxiSUJ7MS1OMFv8m3kwKAjG6WRNb62urslWV7tEAUo_E6811CPg94F8wHHJTlAjOAEB3r41rGXX-XLYn693iU71Rm0T2xmCOwvmMywdf7qoXhoJ3whrYI_92d9YZ0nvFFuBbJ4MNsAft8lbXeFO75gi6ImMyh-wu9WBAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IEb-LX2n5lcUWN7nTgHQI5L_h5EkOjVIKprXzKEP6o2LZTIg6CEPo1JhaNE1bn8GfN5Pm50eMEPGUs_Zw6WsB7xFMhoLoPvZmjbb7w5jaVzMkZmh8CsktUwMKOdv1hBFnXyxSyeDBOWcvfGNGhsTifNUswOVea49b_oLfCrUO_tyeXBsbROETAajWPKBj6x_V-XdvwVAcHGWT5pCF_cX5auDSfYcs8h3B5hM8aoh7II2tSOzTKjYd61Zzt18wk9ZsEt1f7j0StFITnZ5lZr7LCRbpXEdjKbEtEQRVlmmwsbDF3xw9czSVDoNPcpUC3Rr6Qu5A3ol71RKAGC5UY80FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HdezeEOgSyNXdKfN2lqBkphh4j9eYImp3DT0uaTle-IqGxgCuySVDCS27iqAUA9Cr5lRVCRMImnBCyJ-UwjsNVBiLk1EV6FzScy9r0461SjS2JgOwenYyWPx2JaAeks9IYjYxeDy1F5IXm1_J-khxWnZ6SDdlWetFGaV8OhnN_r7qFBiduU2aMDaKqEguiZ2fWwoh1cnZtzOERmMXTg85cxTuU-uhKDlR7kzcDFQ5g_lxSgC0ITTWoYGp7jc-Skv2Zwz8Riw259aDYZlgABqmnBfubN348se4VhIEer0tV-Un2olQlYqebxCv1PNAeGu9Majlt99ShfKEu7zT8fCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kywQ1k4b08Oh1V6yBSVry8Se9wZhpFtcnSr388IxTLSPMxozPsD8GtiUdXhY622FUeTlg7KEcMFIjD4I9mqKzRgyZlt1akW726R2SCFPUZ306q4-Lr5UDLo6AtigUULPKq_YuaAceO55PCoWeDBGAG3E0wowd1qJA8zGsaqLCXRjatibTl8VpI4tFxMUoT_d9CE4pJHZXRQ_OM1-lkS7BHAyxQ4v4YgV2ZB3gOOMvRQaKxFU_TUqjmIsn--mqI9S-d__hTPQWReL0E5RcC-8lnXuN_45tmpCD7Af-gmtKxJIMbv116z5IDZ9Vz0hMX-5HAjv55oYlp-eEp4AAfTcLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dr3ZGiMd8aObZg5fhdE2boxCXknQcK7GybIu3IRjiAehph_UBUfkIh_AdYuHqRy0VCohXlkdIzsZAU_VST6G9QdsGrTNv9Uw_XYVuF8M6St5iZAMvrtCAJzbdNMV5SMSQkqlcwe_f7rPCrDPuXZVlUja-vvDwNaiCLHwIYbfwKods6dgkONS3rKBoaih9rjy7RTFvx23lLBtdxsiy-V2g0PDLv4nEf_-3qokR1bwdLcRGhqWLtZ76vMC0J5s5ZuUA-vS2bmvdu0f44r1UFqZlv9An4FbvGZcxmi0cDgXHan2Ic9-XllEOSgcaLLGzkhII7EtRE8msVsKCghKdblexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCZR_EGCPCKLR4ggra50DlCcYBlzBLlCH4OfItubzaXjgcXB2gKPU7BPfS4hdk1qGGLteqRkZq1dTnBGx4RGxA-ygPOPOFTiE_I_GDMvkxXsZC69_TP7WhgHr28D25PAQwEB7u83KMEGjrOKkE7B9owmPx0h5OcGEEVRDxzVN0VQHFtNzluDghNk-NR3eXHgaTx0k0DAbUk_0u8Ri9l1_Bv6O0J8dK0FTPAXewCmc6MyE3kHJuwmU_EW8vTqvEZ_oIgiyPWNrqZ8RyleR7w8EJkBGURMaFYEDFH46eeRMlABTEh0F2eTMeA3TaBnxASjph1RlEAPq0-c0wJWlymt1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJokzh2U1iXxmlGmVKNkykv97uh6pEdPAys3U8mb4kt9T_pNq2p2zbVeGSvRVX7ZnIvk73dyZVGxZg3fT1bTda6fzQlvSLl4pJV8hWImdBAyxEBe4ne2KGMXYdtyD-e1R4HQ6TnOgSL651Vu9ffMHiYQcDvoNwwZ-Taf7LI-I7QyCxujXF5mmJybpBLmWLUWeQqg4DJ1IQFqnn01cDN7nkMqF8bL6s7ghULXrCIadSdSq2AwfHUUOhT8QpKRSMEPbdm1vF398SG3ltW62lJ1V_J7V1V-4cBIZ6iXurc6sBWIqkY4riQ1BuHPtA1X7Eqmvi8qjg6EavE_xevrUcg78g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=LAbO5GdyXX5cFCIehEQ8mJPOTu8xNCA3ENKBcaNa7AUDg7Nf0miOylr2uLs8F8dj-h9Kp4TRCG-5oSL-2sR-6QP9G-4kl0GU7jz1x6k0t-m1TFjgtHfFTsx24TutCYXHxw9zwbAYLEN-57YGfbFKa_hxvo_XN6v4JsG-w8FtC5BQUD5Owv7zIpdo2R0WYMbnrRh0ebDfyHp3Op6-jztVGH8agB4EtyZdDSI01lQMks4KTnFuXN6her0achCMx_rx3RfxIFUikuMz7hfxtRaAuPQmN9aomQwszb2ygrA3YU0U5sfLf8jpT_L3y67wU804pI2AOV4IQ71vB_QNRm57lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=LAbO5GdyXX5cFCIehEQ8mJPOTu8xNCA3ENKBcaNa7AUDg7Nf0miOylr2uLs8F8dj-h9Kp4TRCG-5oSL-2sR-6QP9G-4kl0GU7jz1x6k0t-m1TFjgtHfFTsx24TutCYXHxw9zwbAYLEN-57YGfbFKa_hxvo_XN6v4JsG-w8FtC5BQUD5Owv7zIpdo2R0WYMbnrRh0ebDfyHp3Op6-jztVGH8agB4EtyZdDSI01lQMks4KTnFuXN6her0achCMx_rx3RfxIFUikuMz7hfxtRaAuPQmN9aomQwszb2ygrA3YU0U5sfLf8jpT_L3y67wU804pI2AOV4IQ71vB_QNRm57lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QAAo0KhNMEgAgfCBdGU-QWll7WFcDYGssiDKnZuIy1xKbZ3EIusciFGD_6v8dljwIbLpVldprkB-f0LBK6XckKGbt3oElrbprf6Xoztq3htSGOyvnv_zB8WSoh9EoeAj6M7VVqMiu8EO397gPuVSvdPRPfKZ6iYl580INIPFlFSZ-IKD4lhe_8kdITkSi0Xdz_ypx69ViIEOVlk-MU0MqVBBoJfYf4nKPeRDsk5QAcW-XIC9wqjQDSHrEYgIiwJsXGfq7NqBGJv5U8BOrGQa_eTZBjm22JS1Hyq_xe5MrdZxFHM-7kzAzZjJLxKaUXmsNKxEG44q2GfqOOAt1blxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PbC63pAcH5mYz6JMnU3w6Z3wJihg476W54IEEPymhQNjwDyBKjBQbJviteveVuefBp7Qq_jWoiMoGMl_iFxL6r08IfLJRxCQVRsBrjxQUbakdSdWiUl6ZYf_LuOLPJUovpmthZwkSdLIEk5xSXHIV-ibb_2Ighc1rW4BCM4UfFra8_TPhZjT9dn3ngh36I0RE3dWIOTurVwuYwrxekU3jBFwtL0nwEU0-aob_Xrhr0DB4pCRk_dtLAQvhF719ngMZoofl5SihIJ-Pa30Y1pEx9XPwdK8DSZ5lDfy95zL9zj_DKO6COMuBuBNS8YAaJjgcnajsXIOBM-oUvcMjUv9vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s86UUa4pk427D7CseYkISPBrQRv8cCxGRYHsXHlh70w4hmJ6H0oIr5G0e0FiSnidbdi6O787zyzSowB8d_cxHFrgcyfy-ARq5k3dJ0Q7cAwkHHTmuv0hojOOAUk3IciMBkZyDh55oITaGSGbYbdDY-pR94Nzi8duXRH9P5QEVNhDGJLh_fgLysMovOg9rgAgAutz7Ln0hCcY5S6fTTc6ktpdN3zUwjVb53xR7kNcDj9Zve89PXmM7pQe5K9VMFVbr_pRYpVxBnoK5PgUXKNrs1Qg-_p6aQnqq_ivMRs3-lA8IK_jspLEN-pfsUEQvXdNUhqXu-taXdM7cKQ3gRE3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZjs_ysRhvUAdH6MY2Kt_4vtKtQIgOXH1SYEQCkkskN7Jx7_gzznyBgR9nsbNyoWGywUwqm-u3brzWMqMVZixO9VRDPkyMgKp53n7E5X5jfQtXo5QGrdWKF7Vp3OWnlBzAX3-SiY1jOmjjLZxwcEe2uHQ9PnandnTznEbts36fRZWNSiaIhAnYfiFZgi6eDrKNLz4okRLlkhfjUg2ZyerhLJoUo_be37VpWZeyrd2rSo3xxjHLkuw1Ld-mOkaV3-4bcvLsRgN4cN6RX_8FAF9qVnRo8IObSTsYCWlyTYwhVfHJJIx_GECddzewwto5WAU-iVxpntkcothoXU_vmECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6RdxKj_-t1ljJnSzN9vK32v-8SLVeoPq-bN7FWbdiTtdEvaIbYHgdNXWVqYiqrbOMY7iQh6b_auJH1xCRpVEU39L44P4erOL4LuwUS8N7VfTGIEfV8tbW-eJ2QLCyiuR4ZEZEbSSfNZHXXECxKvInomy1Tu7QKSVDy4lVqoBpN7bPG_T1ALbxyPMIVedF3WGmBVCCT7RdOh6VXfWXbDWH8bz6wDivbqDAzzpetu0q09p6fqvLq-sQX1Y1N90Y8461fcUvU_WvJrRFl0hM9tyJePlVDCrWlYSJwvFfvVBIXKXYlcVZBL9hTJ-5pStIum1IHYD407DifXh07-dncZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/maHdVkLWd7EZJnIbEPI6J2HmoCNZEJY0z8cH5p3kWZ6MDPy5FoQQS4M47-oWajyUup-eipQiWgLLL2eS9MuJz2Ex4TO7dS0PdLVvBWlwICZRbe6x79WAw6wtd0KlKs4XRfaa5RJHWkuHvSXoIRNi2U9MW0A3NpBRTivc4a06S_xVuBMPK9fU-Z5kJNCOXH6cRwkT7YKNMYD_CX7AyWheXhflDiea2BIO3Tt_f3AwK-Mt4mJpGjb7a921Tyy-7cw_GQcC-iPNx1wNxdiTFXEqYADI01Qt6_8Z6zJTxVMMeOSs5SM8FGZHuknkCd5qc8zgdBcXRJA119hs0UOykRpsRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9PBRottREOyEEFRmQNKWiqSC8q-SGoTLKyiVIMk5hjuTMZuybrBu9oa2AK7BRHQkG30UYu44y5ozncsO54jTsm1vPl3_Gt_eQYsphfWIuD1v3ssyMYZXJaaWXlz4H3nHOyW4tIl9arSnfhV1uu8mIRXMy0KrDMQzY8uY-6H7cq7UPDWH6MOeW7FQX-Yr9mz4wvRpHY7CZxy2Xk2AGIS3Iqzt284x9DVI08yTl9jIbZOjmB-b2jTq6uHAfJl0lOADW2dqNn4vCV4uRyvc1lCYhNaqm5azewLxRu9Kv3txS0dhLoueuIklHTVyI6STWY4MM9X8lTRewspGya9wuV2SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t-5-MKIzA83WvgT40ONDZCUuI4knHXLsLjx_P4KW7B5ULozYbgwnlfvq558w8mTXABbBKGpMagynGTSuE7nUk-5lD40yaHycCE-Ib9b9Ki9f3XyPaoK5_9BPqEYQZh71JIo7yYfXZ04PUrBYYFL9WNJ0bPna9YytJdWxNr0veCNiFOutZt1kBBGywjgitSiD1XC8TiciMDDjc6L1h0YpfbRv4ran0GtQiLkxlVGJj3_6JsboNYk8-O6v4dPUbnH4noJEs_Zg9LF1aOqtP7jy1RbKhs6WP4_nOojT5CJT88M_weN5Zl6NCfS4ZhBOjD9HQESFjZMvNLNoSwjsG2PT6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQNv3VvwLa5LnOttPhue-fhSgcUUjzXRnNiwozb-fHhF48RSd9-M3vph9yyE_WAAGTLepi-yT3Fa6u_jdbBsWmxv1K9yfuJRT8KQvnsgNRpTuJTtUfQt2e1rAQB7P8YrPj92GmoKN6Asmruis-c3rXzPI9WDf1HSJsl8IO8_Yw3who6YWWbB9ZIXKRNQUpJq_gYBgTpgB-O52E9iMHaxBiK-8tGNI4fdHHWVpVrQOI2mP0wjg8bm0p0gcSG2W1CUSAcpsJ6DNi4z_UCIirb-kiymyPDULmgyGuj6ClEfQKVsZwQIFZOrLz-QZVwwzKDqZbDhXKxdztpig5rP_B5YbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fbL9c0hejkZQp4gUjzwXvqz41_HuU7ZG4-fCJtxKTdV603EH8ROwi2bQSEJkV-SFtWUXFYxHO4DX7BLLkbKSk14dnk5lsFgNva_BCKoFIF2g1lQA2_uY66U6bGOqEId-rxd7HpjuxquuJeFSs47lD48iCRkTYKTrdc1fEv_4XWAjf4KOt196Qy0izF2deOoAmq0AkvagnTUOqlKyfgBw4I3oqRGuVxCCA29qUQO6hQmnRrMNVlDiZgRCo3SGjy9Q7RnocNVTHL95e8dVB_B_U07dJBgsmEbDYNriHURSetOu8-oB_S5_aA_1ZR-U8XtueQaH_MAtep602f1ijE5dqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Io0iOMMMpZ52nj-rAzpK5LoEqfSI3ACpxKXoTZFZuownJObv75EzI1PfKE53ozLk-OWKAATdKAaiG7tEHRS5PUAifbaiwXdZIT374EE0HF-tnaxiaqnYwDVIC6VbAUgBPBbeDla9s9GtqxE_IV5BIdUIGhUy24uTUyMfp_2jg_3sY1GtLDMSq4lO3NTEtV4kmZMJISt7TnkZ9wAJmbbc5FiMgdIilkytVupTi1K7oDr2KZubC92p7odDgvByXymkAk--n_sC6bmkbjwdnhq_XvhEWCd6Xsr45rHxmKpEwJTA2aL_b207v2DU_EfrMKDsDXj8_s2pBUhJbahRV6RDKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DKa3Wf_wE1dg9Kc1uifhtYk0iFOk2CzbeQlMBR4yxIVhxn5EOm-J2_7Nxm-aLq8kj0uJtKesm7z8EnaQZSob6g34HrBJ6AqVuQwY3roWat8B_k11L0r5Z-mmfk2rUt2iYw31iGMuZufUj_xnFdVs3IgiYlc2crXY1q0mVEI_KrA4jgSwVG7hNOHWAuRBakjHKA2eyknGnYKFqxvZp8oyWKXKUrm59c7wVBEjLpru94A67yK4j4dTbdtWN-KDsRYiLhe_yNgumDDFGjcUqbFCWzVDy6eHZL9IUcNWP08hByGBaB1SVvc0_PXI_KpBGXgLKebJpPjW4aDyFh5bfW9vXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyNn8mMGFbPhUW9VmCeN0IUB-YCLP7wGz8BBclI6UF6oCy-6P9a9tQp-cFnBLFUO2sCJslEUhZKbdCQGwk440nZY5xN956PXWlAiFGNv7wyaSvUeX1foHN8RzTCKOx_BkbRf_KiStZKAXL-fnYZDqkxlMw8hEWBKD83Pd7NSZrYw8uNXVNGbjqliiP6ich9Mw0B8Lo9LQ4SV6-fPDvIciZEHbd0ShcGfKllSHkphLZ8LG7PwW7p0uzliyev3gc8LC7BU2rMxkWAJAr9hnAnNwUzxdPPy1g25FkN0OOmK2JlHg9e-jQxeB9Sfmj-IxGkeGiOC-wJPIg97x2cNv1lJWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D4R-83XzTw1Llxee8KZg8SJ-UDkrIAcAvaDDtPh1lerp5Lke_mvdGjVrLvRiajIv1kGET-DENclH3wdKBI8fmfuYJMbGhIqTPlAiWxm5RY3oGMr_vEYrmsjSN3z0Zl4nKktqWnUqnDVexdTcL62B5ybYg2Blc39EJ07iBMFFxg0ephXUFO1qldCQi9rV-3k7aj-nyoMXGi8nsRi_1Rg_UBbPThEtYqwJIViQJ3I1ktnjNrcqOy94_sDsGMIe3ajydyYs38_lQMS9R_2hdxltDgFsdrQI2MIiOhptr1Hrb4QHTs83K-iSAp0f4kLsfujFneU_fSp9D3mfE40N_pBOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKmB2a5yM6GeGzFH0Ygsyzgx2RoFx3DV-LVBpc-Szj24aiXTAHl1mfs-d2JAiqpJd2l_omU1TVLZIAINOrL6DwrPSACoswC96iS0v0_pxJ_q6C3pbQDdnU2jKQ3D4K2KfO8eHsoptHMHYxX4VT1g-B_swBeFsswU-SrfQvhTu0Jnw7UT9X73Pcw8LrbGKfgkIR3_SR1N2Qh98PIS-QKVLfIl7SvBd1qnoH09uuO9hOJbCjIOHntme3j3OQUG3BF2_qUtqU3uQy5EUcdU3f-EM5fwrNWL-2BrzPekJvB8rNoBVwxmjaGV66jqtDoSzHPBD1vg7aLfLNnb8utHLk5yIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_NTOZHkQ2wmdvRRrcb-xkLSjMYM_DHJetybwOeTGMd9WSh-cC5aMEh70TyX2iGgr6KKD6O9O6IQdtvh-xzUe2DIROBhDiMHAe3flji5ceLtgTHpyj8CaLwOuISxA1A_jmiEA8Y-oxR4EQ-eyQiXz0Qyv1TQcHefhjP6Nx5pfC_IEBIZMHvNyCU0J4AI7Idp0iyaZnARasmXsV-f6cNetuA91uJnPDGWFf6RaaahXBUx9BCVAQyADvDutdBD6dlrmGhYnyasgEnjv5XC2XmpkWV76tRfMzDnDXvE3MS_oYc7lglbukOGQHhWjbCAY1FbToJjknpCrK5of3eA81TU8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p35aG6YZxtE5QU3tjZRoZ1Snbu75MYh-YJkg6zRWVNoNw4KDu1BvGvfD-xWwgKxeIq3Efz1PwFaRBB9kZ3XvETxvSXiCjfGfSJiC5JI8IfarAm_QXV5LWILpD7_dMmBLW-qPwB9N_BT65tgqmDNczd-btqTTcaAHGPKiWLMrOjpDvD19nmq_fbLmrFuvru9620HQ3WIl6WQLdxn05263uJ60SITrL4f5Y7oiPhmLhGjpj1vZFPBxJ1mYXuN9phAI0lg1JbhTXaQnUR-CGX5bXDaTQAu9HRWCJs-XSApGPsWRLE65Wa-0x-z2zgbxZCplAE-3tCtu4XUlOP5p1t4eow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MzqXPVk6Twxj-MKIDdEVPbk_xe3AXxsZ7t7AExtFAHKglEZM2ZFX5UhQuDa5nyhtAl1SxIDnTueHTMTHEFUblI9Q9aDi92qGWrwG5p6fzoJFHJYdFdjKsLBMwd5boqI77EtX0DuaEvF0C4GQbJRywRQX7kSjIGh34oq3_RBPq2Ed0W_l6wwXGjrUyMzVN-DfYGg1tC3GV5RYc3B6-nDdWsxLaVnj92WR_yYCyTATZxgl8UavrgiWYThC22EPYLDHkbY0ruN_Oqmr0HdiO7ABiPYklDB1lCioqXB5kHl1pBy7ZYrov3iG4JuH40GJC724N5oS5T5iIgYAuhXbu501EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/isOwP-cb1h7nDqxzpj-bM4gS57bojBQYJWSJhw55txXmChmnn_1gQ5dTeixGKK9flZLcSu0ToFbLz8zwJXUYJc4S2AL2jNxY3N7xEYGMokk3JBiD2k1kPTP0RMdA4YChQNjTvwLQmYQMzpQnpqQAafswZugRbm7I7DjoY_fZeA-GtbWNQBg7YDEX3C0FzGPxWvWlYjAitaLAw_wBqfTchDNXjlOAYgdK9YNlml02A_kv8i3auHWaqFG7Vd6HUQPJRnEJL5_GXjyxWqHG4NmbCOo20xm3BxgNDf4aCs_BXzd2H8rowteQ5FEg8ZgKL4ywuKgEprpqwS3RmIELQKAtRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIH_Q67ShUecePrfwBtk34No59I5bm7wWwIZ17UsntOxCY6NTKnYlUUDvuDsPsFkF4xtEtufzro0KEyZiShEDprzD-CwrfRti0z9ZDiSBqIYeNJYL0qOGXgdd2DM-f_ig4aiKqIPCjmwdKu7zpjKhablfMgNiU73I1pF39ckTvfjUkFI1LFiz9BFwV487sO5pmfXJbMXj2Xs--i-gV2S-UZSfv8dWjxV1CDHSa5TnbhUe9tLCM8SLYLTwzP40j_Io1vZH6uGhPXLPDCkJJP6KwMRjb5wNFvUChULzuXist0g4oBOJ7r6m5mNCI9XnOjBi8s5yeV9qQETNOR1B_4fpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNbDkK-7-Jh1STRWevyCOpjwpf8pZEQLNeVvphExGSttWvFJidB-hzNtA6nX7S54x9EzYY0JsHJnKbYnSbMmMgH0iVjcKTYhdATRFnyaAZCHnoNB34fIUaMlJeYkiULyi9QCKrAvAnEQoA_n4wBLCLAITdt4BKtITpLgT2ovQB9PKg3CseAB8xk9TZy9juer5jIHiSsDy2gWtU-x2TaSsl3KSF4L4rGKrFZArgMbL12YyXv5olhW7nzV1zLFRbeqH4iQsfcEgfUQ1xnG2ek4YRz23_01a3l5EtFdkUQ4DlFosVuRYw-JSR1OLseYVLULjte3oNNPQ0k5u6vvfoXcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FcRShD0EWHND9VBMmOTrVdZrX_vo-MWKCUERyI8uuO_6iLPiYMppSwci2L8SaI7Sddz-jUMtuvfsG2dfonHi2mQ1R3jZsIHDOk-TkVGhGW7P70gqiIeDlskSgS6EoH8N99FHM81RmQgkawjLhObqqrOHzkd_vtTbdbJCjFQCRjmQjfyIP52hMLcHYBgPav7dcu18unh60ZjFD-UJlJEnU2LqSmug8vYvP2XPlW219Rjkqi9QNbt6OTbAGcg-uX0OBG81ZiScjdwLmO-Lb4xdZ9Ry1tkB1IWYW-luaQOoBrdf_Z099J4OihLPGZBGIydYRkCFV-_qJZ86Vq3_pAuKnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y35KaAl9Kw_Mzc6AgRTxhJmVbEEnieEI8ww8Avd5U758TzgR9UMq3v4-pW3dQ1wBolch5aSH1Gr1beVFeB9ext9oqCm8ofAGFZj9xsEMrsS7KdnGBHDwCj87X0YF0Rl6qu21hEK4VO2h4VYPG4qjIdBuJsOFo3lstohTWWs1M53ui1jmVbnTI55PPXBajr7R1S1FyxgvANpUT4k9VaIE4TANEiZvfwCo5SFhK_5CxB-8Zk8a39E57q5b-D3KEsY_oXI_8WSiILGToQj4Q9xU8_33SOsdOrUwcDV2fgcJYq_TKxNSusaeQ_HmakAJkzzvrF085ODfBXgneONSIIzqBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pjzwXasM-ANo3CEGh-8KKZFvmaveHzCWxY5U0FxRAbbZQdLhfzqZf8JBEymgOV-bacUyQJxyjLBMCTGRyDeoILOJd6kqYw7vB9NTr0mxE4GlOhUB4AqUYaXkdGT6bHXs62vih6xzs1vwEJ_F2s_ZcJvDmXUwJjyfH3yMVsoVXkEe1js-x50QFtUQ2XaJBZn140ACd4LY7deimSZWPaQAEhjWO2Cv6vtTFyo1RiMH4DQ1ULgJY-XXdYX9QQpn5Y-3-CMdy0nxTwMcFZwRP-AhmqSNQh0CiyiinMaTNRixqz3fhJtnT1_BySrKVr_PDny_to9uZIb-9IqbNBGdGXvM_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZDTiDNCd5YEV7RueLO5qQpRYmqvM8SQZnYUR2gBIhfQ3GnumlYibWy9q--ad64GFucUPY00YG8n1uwzWEL6ZqWGqvBCAm42IaDZ9R4Mpbrve9_AZmisN-kgSoh4hV1vEKwFn4C2m1GL6eZW-CW1ZGd7IUCqGRmNPdKg0TN_Chh_6V2-dApC_x1IacsvlwHWs6X926pwdYkrO4_TlOeQrhv3_FYnEW8x35rShneOR_pz7Y9Nw_UAYuJ6dF6nfWpbKIaFN0zeEMo1i__gpnRGzpm-Ws0PhMQtq5ejL7i71cWWT9C9KsIxS8evhFHeDXrbMRE66YsjFWQ5bwsGa83xpfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZgZ0c_bcgLr-nxdTfkEK8I4oWEZtTYWB-pSSERiwAfS-1uA-nAqWH0Od01GUr9SJSi4vxEYj8ocxr_2Bdj9M3Cs1mSfUZGpXaqOh8r9_yUEAFXbxBy8t-6ghklJqAZjOdKT4XzYTfQbyE6LJ2lSzsMH3tAWQX-tMvfaAmHItDSXd3VYIurcoDodHk74Yd3-GZidL20s-ZQd6Djc4ky36F2KZ4BS4qm8ndP-Xo3PuwzVZ-ntgCAn8EEd0lHrFB1ocXXh-1mL8leaepVlM8HYpJe3MKZFchS3kLFbeF6v7v05HO9-PL9-RaBIkkMiUalRoPvFh4vXUjSXQ-bBy-nKwpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YBICh_E_ounQwLWqaua26GOXhomUlpOIhlpu2BsdRK3SRY70cmttqoQpGAIvtx0PtsYnYt9NjFBMh54savq0Pjj8jZNmoLcC6krTsuAs3_7jTg1xQNM2UY5V5mCqMkf-iMDpdkaJAt5HZXZ2vY9jNWeolyUlNULfW7i0hKd2x9GlqF57bcQewHrl3mi_r8UaC148OWvhY-Zs_F0e6eYq8ZbaMm11fHdaLAAeeO55na6dukkwCfAv3KgQLBvc-sLDlk3gNU9cDbm9rL8ID2reBAQSMeub9bp8wV96GDqBQ4_j8F2ZcFAEv56ukPewr4IEiW3ecWUTsKVf88LhIN-i1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M8cNruQqVOn9NmoB7KhInT7DNIj_EpbEQMR-iWPtY-f2GVRkxXLtdGdhD5JC4pCKTv819YH18AZmRThln_FI35PwQAu7ZJfaD8bzE9uXKXwxnmL3GmWIFUABY5XvtJEZAZoz5HlD8UzOMJzLdPKi0u-cuArmF-6_BrevGXJwRD8FeGv0oA_pmWepIJOaA0wxSXuzBhLu6zfLARxiA9i8leEO72jKP14YH0LTdaoBBvPponm3JLeoaNQICR7TpjLvSUeMWoK3-AO4HlaMLknCbGuoeFH_omAZ5x4dZTt1wsgHY8kQm5nLqBYe_SUVlPNoJQv4b-T1S-xU_rd1Jye5SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8OrNGSny2DhaJ-iEMs6DrwSroyVx-Ya8Ths0-SK3PdZxbJHXlIn8xcI0bbT7jnAz87HHrl7F86wpPqWmsZYkoRa_jOpuzVBu2Tr5dzVb1XmaVesVnoZscq0ylid6Z5Yy7AIqRCEvMcuyG5HzDQ46kvqqHNVtSBK4v8JZMudgrjZ090c4cTK9GHtZoRBIG5yPnWWl85fZJp55Qabm7vy0_XfAajr5M-lzeyInugwwM67D9LoR6APGq3d71gNoW9WBG04-Heue-gTlYAQ6RlOZpTZhynEHksTDqT4qAtYK42OFcstUN4rCzaYbHQYCUdkZo8SO3b6w3xwsGkghlv1eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c1Mec4tFDKwwGykneZi4jYPSQBjqus6kN7jGRdeX1kM_zy7x0za1dc3pdCfdueBUoPu-r18UDXTnNyYmI7vI4ROyPjhldIwPT8JvHa389mAGDlU2urmSSAoGyeGW6ZgQ6c_bsTHbf0AwK_RhSIROnOf7AMZjxoJrW9tiZrnOxotsB21g402F_KYLKXlsZigyO2sgwGSY089Iciw4Eh4NNbjFtappzeQZswR7VoBhmJmrRz9NIl3IDF7qCf42XIi4ND8EwVPW0mN6YXN1v_1g8xi97c-BgLdTr7kP0cmUonVH6jnul8ZAPnFxsBMxXto5CF_mY5g2RUXovsS_CMtX9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_rJLRWBzcpvhFIKb3KGXVwtSaJTs7L6FK_w8xWH7RAuWWhXJbMYTdzTudgQLEPrwpm1OF7XiLzOcKvMceu9G-5kJwye7s6Piq4hnG6R5DMGl_m6lj0Brr2DXmwz-P5aMB-KuSsLDdvrWiV_dINt-aSKKHY6DbvBH56wUg2gLKvZskSox0R233YBDJnfrIyJ8gwKbvzWmH3CWzzVBdvAZOuEH1QRTLKqRWIFZnYQPNIiXWYIapZWgfvn4fWa6qnQF3u7yjra7OHaw4jHBAakGsw8eqBXfZljECsNfa7ImN7kFhQW5LIUBk-YFNzbVIHEHfqhBjhUFc6WV-whV4J_Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqaapb-yG_pivpR5kp-1IMzhuNkQLgIbC-xHTzRaV_HXqqJPe31NRsbdfp61BaL2DprK6tUYDRiCw3Fx5cS4XgKIi5zgf8_XgXLDPYNZc-aFMqQtcW7LXWGeKpYYKMmwnFYWGpl-hSWcF4tsRJWhJoXjPXLvoSO9X6mgf2acn8GrWeX7HOTlcZOYOqHZjN2356KK1TZVgszvzJocgNWf0oIqvHdMWq4DdHtEMaErKlBtIz5TF4G68qJ2KU6lF0qNwulICHuIOkvhbduWe3mCF1ilAS0dGiQPJwsvUl-9Jr7IGabMOwPY01rl5CUU2pPg4TcTYYQlMUXrXEWB-flgJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D-hk2Hvrddfn-tqZk0ZHVcn5oThKoOnoNBbtlY4aj1GPQ1EIYxHPuCbLkFKsbMKyaVzJnm2nI5M670U0w3aBYOzbNQi3-0cX0TPc3G8bmpt8SZ82Uaw4WlsIJSxiOWgOAcUIOe2l2uJdO9wwr-idHjCh4GDWnmta_mvaUDakPQQZo1xM0801l0rHpSEfrYGFEtXksUkKwtcTZ33Wu62ttHsSvbhRgfohnFC3t4J9ImahGfwmyTb1Nm_9hpGD8VFHQtzhpB2nGXTGxF_baxaV2r-F622L4epLbYVN-JjY3PrKXBrWwc737UDCtzFoo4QzB0qTaoLtw1XRE7NWbhk1yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
