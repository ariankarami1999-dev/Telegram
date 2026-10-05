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
<img src="https://cdn1.telesco.pe/file/LYtSTWkTkC9sRkIxmGlfcZvh3CtBKE36B7k_Fb7MGWjZP2r-645sp1UPQ5t_oPNTp0nZ2a95Ypo_W_t3EG1Zbe38bgogov9i_ZLbdTDhq2nPk_-qJtWBv3rTF5io3XQNBNQTHhgDznb6RsO5j4ZTcv6koL3WxvmAeoHwByfrl6Ruw808q9TMTuz5sWlMyNMBxun_B6ygwGeFlSG_i7zb4e9ZaUF7j9ldiv6D7KiTUdu2tAfXHrXPPzMfObf4EP8spOOstTrWgfMO6HYynoami6-QmfEMWeaeDyRVlCGX6myg3VmfdmZkiPTmMUiYw5jv8frftAQExXcLerwdP1mA1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRNMis6MwNjJOeIwf_n6XfeErJecTC_kI3-p-1IMCk1Ce18QItaxbg2ijTLkHPFOl-6sqUrl91y9YqsjbLRMujWD8IkqXSSWdZ-fHwNtYwN1mMPLLr7uY8vENk_II2Z9EKln9R10wtVQklT5-vp3CLhXcp2S37AbA3oA0s11ckIgu_2GJ70HdCeS0ll9Y1u84rEWjFUHXhIBknISNMwZWEWj2xYCclYjwQ7fLOsp8Wmo2UZWXC_K7qehFfmWle6eTI-qm3TZdIfedieM5S2N-FLWZDqmycX-rG-lp34TumhpLKWfW2UUmY3oMcNPXZzWlmIU3akIvpNCrWMzPpzJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/liMxvMn2OO-3Le5_zs_H0chLRPRbhzBeqBL_EcR7dPgsR0g7xz6JAx4NW5mFjdntI_Hr-G6rzERNfV6C0F2MRF3Qg2wARCbRuZSlHaD-SPupl27T2bhcksNlMYebTvHxro5S73gHTfmnH8WtdBgvPzIa6Q_dnREcpvjQmrQjqag-WyMSui_yrCzgCfu6SDioJ00gT8wUEJNtp-y7YcUgl0TcsH5TWcP3phbiuhw881X4MVUhXepWdTmpG-0t4F_LE8w7hEE8HRj6xP_9uxJKQvpdo37PFHhUON3PlRmzLqFtVJslb6sT9XVsJ8icgPgB0cFwnusAiTO7Eoq7f4HQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U4FW7cVK4Si8dNvIZYomQYbZWHuXbJxN5JBMECnw5XHm-Ayq_bGPKH9zODdmtMD7_L43Dj67ab3SIXzVvmHocFeKs8Zgyko_vJboLbbQrzFWR9orsHWYulYCvw_0qjtwyAPWYm1G6bSc7igHFmyrv2dhJJFpqG4kDuaLyquVHMEZ2U6CbIfFlM1m72kgb4zR353N7uV7yCoMh059BE_W5BrrZozMav7OLUYONfoIMbTj6vHcV43kxtyEOv0D0p3UfD0wDs3mSS9cLqhUVPp_oliqfHdX1lG5aZ_ynj_JdWFwnjNRQWGf1ogTk22zmOzZ2elg2k3TVXJXux_py441Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a6nuZUnKr6RjQ0bzcH1kn6K-KH4UgcxU-DC9cwE7pAivr91QZZ-p09guGNYjq14WnC2vFv3ZUjeKNhrAGMDBMIQBdhNKGRQwYvxUJn4AN_mD-CDsJQnNxPt2_NFNXE3NDUrGH5ZATha8gEtykR85nx0KAP4zaBBgeaiCxefd_o4vgt15XxROSUh6z5bq4CCn6pnVJvGyMQIzuZ_t-a9jGSnqL2elgaIy58n9CmSRH1fZFAw0IIsHSQes_okaO-zHrVjbqpWnZPJ1qAyipynUfHjiLUoe5E7mfvJP8SPhV1yuPtdcCx2TeM0LRUzkWoX7vHe5ILMU-lGTnrCNE45AcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXPZn5p0yDoM9OYzfZn9zKPMz9FLlpE1FQGyTWFki6hqI1O1BaFDNLdJvVCLNm02zUWGH-jHFWjmIIpy3SWDga31qUKOH5Oz5dybCSssrl4WIo_8Trui9YawAJvSSKbKHmDTygPThtZ9dEw1W1_uog_35u7-cC6LNun0evDo2R9GhcNYmHhpDn00WYwmIysjNwLM_a0MycypFu09oqsPbP47wanunuiAFK_WJOW2Xoggq9X4RcbZVZ0cXyPjvEojqFgpT9A5HH9MzWkC497qrNHw4oILNJRCyY_vzZXdiALp-NxJEPwZZppsR4f41QDTexubgt_VoxavkK2uN95KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSRb6dVnpuEGMLGfQipzU8DYj50MZbG1xV15lIx7cnl-wHotexLujGS-Olf6KsnZe9sqYujg8LSHBSALT5B6Bcbj1b4kXAv01IrlOZ6_6vLaYMst5pEJF1pRwN1JKttYfBWUlDWGV6X3wJHRM3DArI_OTI9NbYqwV2INJspmJoOrthsP-vseQ9TzK-v-Nq6Oku_ySWyc5_FYKS3fTm_fTS4D_B0s0p8S02fIB04WOtGFt8owcTANNGxwBP6rZkEe3_JZ1E7hH64gwGDUZUo6qCmhXq1pa9RgSqHzHfhL1o7gFFK4nAWqE1JbmA6f02n954j_gasAAb5cpCgsG3j0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lukexd0sukJDvHCr5Xp_YIMhxAK4xmmGdtBKElD5EqZnxkW0j5yUFQL7XnblT3lBhwrI4cqw_3zPBodE7smW_Y4CInHFV1YclufTXJ0LCsXN2jTYeW-jCYXGhH9zWkEJ1L7fNBU4xcO9A2gziK0PV0-0VUqgK9K0bnIGkmRfaO10bOFah0OUQ3b-byo23ikyVxaVw75IcGB91r5O607qqGBoKw1jzDnOivtE4uUQ5phJFpJyhp4COY7WebkqF69Kv2IjN7A5fmojR10t9RNaLN7xVW2Mqg_SfLRx_eNL7n26iq1DCPixwMeMGXkUhFsREW6yZWGx3lg1OLLwAwKQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2yo6xRdNeFof0-j-4QDdiC5EBZfiQrMQZiVqfcybx8FCVYDPQK89zXfSAtJuDeU8SydoPl-lkV0tWXtQR_b6dPIfavpdBOYTMpbuTqkQGP8zktC6FtvvRVnhaMcUSG6z43Ah8L5slvgZmJkbuhuVB5JW_URYfxt0gv77rpZFNncFV2IwDOKCkG8ddVI1UkGs8DcGna6YwJEKPQhJZ50hsyCVMRQblJ01O8roXv-Ng0hSFA2IsXWJbkBOh9JJUE_gSo4M3NY1XgtSpT2T1WNrGwPjPpNQTzEilUzGB6cM4VwnnWGdTwucM0oyQCkcWi_XnHBt28rhk6pMYhJ0pm2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ot34baO7aWkkq97pmfyUYLFPds6Ks8lIVb8ZiT11wYgUcO_0cWperrSjsSzpq8U2fpkFswHtm0mYkaxZqzTPGk0IdScr6cOEhQp0TEmxW8Os3BFdEh6xob0UzeTfm6rKD4bNCRCXDw-E-B4aTsU4ote3FX_ow2NDjySMNHAaKHOsGTgc-8oItNbsziTZ2rH9NBVbNqMce9LNqY3B43fb6-Uog4UGCF5_eIPMZARLtuGaYPMiIIFvu4jNaTQ9BylAP1Myuuy8OogKKE5YBqjc41uCm2k-TpeDYXG3r8DoTQlheHu6HpoX5JoKA4so9zCiJJ11UjcrdrFi1HKUD8yS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GEhvAfBdV4UDJKgZNhC8j5PXRntYupVnHutDhJApv6oHd3mEjtePgggmGCcBqSnV7HnFyF11mUFhaIod6e9hX88JtA_rr2KxTf3aUqrt2-DYUYtq7d42hvMbuFNQqawMD6Om5699FAE2-oRD-lKS7MM58nCxl4zU76C-hmdzL2bSxNOmhMATRNmI18SFHogqetWPriCRcqG5n283-_UxEoGR-1vYXgIIfqXiyG19sQNIgaU8YmkR7b2FrzOc81CqYq6_rUofngpWMd5dEB1GzBTvAaH32qHOgK1abhtG_bhWByT40v5zFzs6aCIZpNONuMsvVQFTF_mZ0IfT3EQW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hlkvECoevpqYBQAzTkH8IHyMw50gNpmrVZdfsYoL99zHFB2zuu7y1QnaACg5myC5ES7Zrqh8XGVq3nJ_-prweS6iOF1_nj-MXlUeilLotJ-ZXz9iqkKCxB9CLVcH0dnffK86PFW7_vHsYBTpWcBii7J02Fxj-XCR160ETKfmTTOfSC5qyFUQiv1GsCqokghOtmd-pXiaxXwZEaV5E5rwvdkezB-I_Ql3NGwxM4H92e2S57Peo-D86ikagwxnZIWTCRU5A74IqIUbQlBmGTZ_2fiFrUqWgImCefJahUEMJg_OoX7J8ez_KntuC-WqNMZyU2X4y7rLY1KIag7EQwzZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ci6lszwcYm16m68LEc422oGRklEu2n4SMqF4asnjjAEYWyrAFCb7E7nKAHjug4YmoDhdDiGCzBeDETh1sLKtuJD1uG8Q7ZycQQ0H1EwUAGh_5zBRVl7uvLtfBGaIKZ_HmtTcu8IdqAR2WQD-Sa70TTREw6e-ASixdN-H4Dnr5YeOJHfIwwgs4VQCDM3XhzWyUOzodeZ1fQlWz8QrjUbQU42X01lnWJmaBiI5C5RIouL7I7yYUmgTvWqgFeH0en7XOlrbzzwcz1ZktIcTCo3ulF-zEkT0Rb913LEZlqIb-NOwL7isDcQjcsx_oUPYagsqSrC1CZ8emeJhBWZ0LudHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHTEJb6qbIfLYXh2iDNWFKVWbuCvnKioHV_JKKQR6YZqFa3TFnuYwh_i0NdC5IoB_axmByhTJCYhFfNSEjbjFKCFeCqcrUc1LpppID__N29z_kbdhkIimCX9suHBFVLalG5jOZXyEP6TsqGxm-_8EHA6d9J_BYEBphmy7ZnzQxlDRfJh2AHAGJThgV7J1boLDVA0c7zlESjU3T_eZ7UPb6_4rF60d4rSZhwl0OmL8yihZnFJW7ORAA4vxgDbN_ViYy-zApkxlmxW_oQHCKehrGXYvv8AqEQB9MQIXgEGqgT_aBrMDmp5FTZgM6IZYCu-lg5etV9bb4daYg-hGyn7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fz8pDP7EoW3PMSRYGSrsydfXheLIh1OouahlpMhGftILjeaol7yeLIRQiLEn3_BOXDVDWJcaahrgkC-iGFk5dwHpjhNO5OP6MD111aNZAJaz6_sPjxvKjSWE7ydvDZrjvb7h2qO8EwaVt24PH8x0Sfe3Yj10DJ9AGFFC7dWLF7ckbG76WgoqRWXzW0HEBg1FeDolblbBAaBwdHtjEIqXNcUhP8jXs-z5lK5Izdxz_aWpGvWBPYEWf7CGZUz4yjFAZu0yxzzyNCd2_tensxXh_eZWylSjSWONaQAiGHapIUG194tbWRfi8VEmtveCtVWO9D3bvpns1Jwbo7O8mQuvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z8uPC0V8jLVkrvjDwrlH3vxcvOTvVslrVWJvLPFSNddzSksINXIKOzlDzkPSmU0x6rzwuXvDpP62Tcq6W8Pn_17i40wn-PGBpqURaTFGRtYutzfwcjSGxhZuTD1wU3NNRRaJjItd0uLNo-5CJjyYBpdTa5JdPqmAKUH0OEIbZHHPoByegm_RETlp9LoA9RTBOFkDaMb_JYgMuNbSf2VNn8vURIE-b7oPR81c50fUhHej0SnWVxsFr6DOkJfCdBqoEWJjlKZ52L0VQoDmI0NntHxN6AIIv-p9qU2NVIsjQr9yjr3agnATaCpg08TpklVuLdXnAWp-ZxZ1w9fLNy4Qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EM2UDGbeQhQv3KtSFLpkxQxN9ca-fkhqzBcIYzfe6hP8tyWYPG5-4gzOilEUCgPuZ8KBmpgER_cwD5ldcURM5fzqC-o6WxlAvZCrI1TxhlkOmlcvE70fJUr0klURFMW9SYxhhSrBCmGfc-EgjYnuXfzF1-1iITFXjoIP4MlBfN5CTNcnYdHdWEh6QvuiBlL584uOEaQ4xLQpjp1Ief0KS7dJCRYzbFm3xZLSi6QDuzJJS0j7ai--LEiuSfBdDbz_Jj3_WxTLkH3Vm-wHsCP8w9hDwQN6A0p7_lC-o6-qyxCY06ydZ5n2HUu0LzAEOTQJrnxYHd1FtLCM9rbNj70Rrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DPnOPe24kTha_tOQT_cR93D0w-MDC84bJlqionfQtMmWdwuHNCtqxWTJPJ-42iuU642_t36pspZAL94B2nEL6zTRVbBWNM848LrGIYGbiNIpZ-ri8aW-tx0OnyGQeiqXV2fGqI5iMvFhtAwxzJMGj5xKlKvq89U4pERElGIIjnJ0xnX8j4WjaNLpAIloYrfqu0rcq97tjR28gu8K4YG-8Q73d8TJxLh0NZiT9AOHjnUtDeahLcnszY7Eblmgz3Wr_ZeffNWSdFMS8OMxlStQyGDdla01PrWIga7178tm183MP5-l69apxro8_TUvGGsEh_c8XhSusLJPgcGixz5DXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jS2Qj5rOMk6umO4R0cZetC_QNcgOrQjZsQGYwdxi38ZyRzrcjgBrxJicgbYacmlW9_Fjg-S8mgm-OqcajYSxQ7LHkVdGm-0-EXokiHcAjyo_smvgzYxyrSzCu5Xl7wqkeyhRTgsT-zbG2RC0gvHpy3NtIDY-Dgt5QpBICYOtJ0mzEvImaLi5VZbpLhgOxRSS2Lqhp5ENFQ11jAa0obFTyMQceUWsQ_rW4O8OzJy4DKi-eiqVjrhg7M1xoJ9DH3L2dJARV5PJHoxZ6QGiRs_Qr-CR56W00klwUnwKdimdQMpQDwBSZAI4hslzeT75xV2M-C0ow_hcSWICSw-SE3arGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjZ-P1Id-VXk9g-izl68K4-uAPWHeFho0-RRwbDeGeKg8yqOXhMrvtIj9ztP-JHuG6y1xNMxatakUqc3GiMYVqnnoeB8ih-Q8G_kdA3SqZau6O_jeTdmxz7Anx4bZVnsu9rBFpWRSMz2N4DeKjI69loJU4J0aVznMoKAExlfNcTS4NBRhLW7UHsPM83hwPYk-56tfWFWDN1X3p2ap1COOEvrUzU3XEf3CVUaAmj_oZ9qTNXwGLQLoMIfyRoXWTF7zcFazR19Xm6NBHj8UY-bZLwt4UL85dFF1TvBbGRVS8OlmUfoaLX1nDIaZRFCCinck180FeLGZrVk5vmcNZ-GTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqdVjKI4yce5j13aWOu2x4qyPw7CuvqbHuSgJaauZF5ymMB7A0lEugglwnoUwiTEA-yDH-_-277OATFi6NnpmbZCaFGTstMJ6JvJ0NZmintXQyLWK3pSwZC6nQb_cgwNK4e-HzVwQeVclqI4u5CU70BB3oatjF_FJC7Jw3Y0UY0bNuDiP0wwUT6NC_igOQ6cQY2jIHCPJGWPwKxMK3NxUM8QT-WHyPMDk_okS5X6sklKEAhXzsbDmx_Dt2_TrdPvrEr9oWlXBYmFj6Y4EJWWsMg4YedvTAMPCWSYdio293D968FPKbtlQbbmW4gJ1mnNXJtIm3_-nx0L9uXGJTu6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xo0XUtlpQ-Qlq0Vhzm67efm9z936FCSJmGu3BstKx0FDbr98qL-QUgUqlwxYR-LKlYlVKHAFasqThBlFu8lCZSiIK-u3OuMtyEhDyVHFKt9bplGzxiqVkMawb7useMHlhpS15rbHdB89bxiJh9rRcEGlGS1OxumJIsxrZHCieLceVSTAElllQZlblFyPNkm-zOQx_lIU1yRxaABNqqyJi7ZlnfeTFxxvcHIIOtqaecIeH5tJ1bwXpdDePRVwOXgqq6vmbFgU0Ops0r9LoLnC-G987fx-EKteex4XsJL17l9GFcJ_D3HM28DbRqok1ULrCfMgr2KuxAm0qMtHwnmJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s2NcM5yLKXsDnjBllkygy09efxnDgk_84bJ4kBnMuwlvNOfw4aIBARAs7EXiGuGuNMF3NuKHPl6lJYW7dpQQslFRDCVxENyn9ntOF4z6QGvd1qPC4ISaP32M8kMFUQ7xfkO2GVGRoNb11xsibIWeq-qs64dnsnSTU7-s5eCJLQSbPJSqSKpx2fIW5EmFmAL7NB36w4lkhMhkOcSztdD_houYV99kS2KgRiwf_fCmVbIJKxOfxgXfxECLR-jP6tLuFLnAFaNr4wZf6IZW4Dp4XFBw-6iByjNv5uX3FKGeTpMa41aAAW-ELXAIZABmThOj0ARyemJRZSM720EfJNjK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lH4Q7D0kFY-rMyNvIXBD7ZGr98rD2UTrByoAMWFK7uRpVAMeUlnke3t1a7ulvpGpndSFK2SLFA53XSpZxPL442o3_5Gl_aGFT71MGf0vP7WhY24nOZLYvThAi2HPVjtzWkfMVF0GYkfMVroWAsIbXktctqr8P5ayGQ6U_YHXvpMKazlKe6mkzcTksIXpXpnZOPr3sLfzrn81JwLQUosAGGAA3oFtoVtLGiOJeixmg7yt1W5rbOCDQx-ICaF_sHFXKxyREvj2Sf6x-rdRbjMq3OaPKaLTvzpsmisjyZMueWQqQILxueHk4H4tB1rggLiFlvfpaJP5Z4NGUYXaM6cYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXNRCm6Ff_xfBrePsM-XhotyDcbcrSQYKePjib5YVgHpwFps9kMczOSnAaCbep8fRQEO2b2lZQpYbk2h7FsqNLH2JFKs9rUsLiKMZnMXrXRNSjSulZN1r3Gey5vF73ovsAbw8ZY0ptkIgawgacyDE-gAZqQ5-Gse334r93Bk0cLWOeYSKy4onE_Y7jbMGsHEIwAi1ke3TR-0yC3qcGYNaoSf3ZNjyaofqxWyYucLdUY4rvXVOSm198HSigYR4vMX30MN_8hnopJwpxoq710uO2BbLUPKor_h6n1QD6y-mQeyEGMgHDTLqD4X_cUbtuJvWAckaAZmvTfdLTK0v2hNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fG3GHvQG-NibbkMx8gorzK6k9p6GWU_-fpQVAy067zvnWOgiwmigCjjkChncE9BuoYGHQfG2vbv7O-7WOXU5FHRBWeAF3KdBTDJWp3z_7vsSC_PUIMrMXlVnk1PWywfeyNMy-4W1PpDJgitowaCBtDIL9XjkW_44mQ0__6pxIqDoUXwUM09p0LfHgkhdAkuXv1zOt5aC-58XY1dt-rkHYfJGSC4c6YrYeW-_Lyn_7xGG2oAsJg26MIT53mF9aAOAZQ2ovaSiiIG9z0IEDKi4_ze8umzj_QRuTCwyjZeWSlHVoHTzrqK0PgmTBa4I3iXw3g9VLWmCfGH0BmNlA10-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jj8O-eouxlwB2AiQWNXiVqgQoQqC1T7RNS4ibqn_e7UNgNGWM5tVysf4qDTwvlJ9n1YBNMwlXS-vkLlOuSfgRVZfTP6sdu8LNWweDP-SxSJykDQoG6HA5NN46iDC_RlLVnWHpWeuIghqemf7V-Kk6doeTxLxEUrpX0UWUaN0QGnR_brJBu_6ou1THkBMUqirg8T8dSHqhb8BH6012uh4YRFhoD1CER4RoW9XZNIF6GxQtNoyG8lBHezIjo_hara6Qvb7fpCTavBpOGgbctTUZETqpMdB7XxZnTSB2KI68rcorgypocG6ce4mnn3aIYtuF2Bih7fUP1KVFZHz-TJKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UiYX4L9U7EkjhxRS6bp8ML7uDcGx1fark1-eM4TAInx5z2f2_Bj2yrU5ZezdOh_XqzvFp7F4ldKgDukmon4Ap9v30pEwGoWr5DCMDMhGI2QZ0CIOsuSVB-bYMUbblPtimlUYB9x6kyHu_gDHl1C-h6Er7dFzccyp-3RO8y-PT1tD1G2jbPdmLFMO7RtuOeIXMinWA7AS88G3hlJZfoNCuyMKa3h8OznC_DmIcEOLI3nQBbnwj-yZxcDSfoP0LOapReCRT3Rhb_UMynhwNSsMh_U_--WWkoeuLl7rRpNUHzaoP8Ti4vDxI3e8RFFeGGyz32ZEreeA_w374x4LYNVDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lLdyKXrDw1J5DqCwXutALoUsu6VAIGkU7mWPdc852hpHWG96L9RsFWnr-JDgb_YSGZY2wHQ0oqMAmynZtftsBzVVLfPgwbcVYAwWVLRzf6jTeqmVLrWvntOlje6aB6r4mZNo2izz_NNUFK59UGuM5mYuPAU3mZNe4P9cWslTUJg39z9kG_foEBaVYX45HcW4ES-R-TRg7xTxAwmezjFt1FOYGVIUtdEH8KErTvWnLuBcdb9gWxbXtMFw-zewETRmZGySVL3D30znh7q5b6yDRv7AS-tHiDDsaPaApQnDnGUyvLm_jfSNX8seC9XyNS4Qk48Do9tfEiHwGM90-KVSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXU4U4WOZMwdWWjcIO0zEnUYNFdVBwfjup9sgoltgOnYP_4UPpSiNtsMRiOS4LMIytkEGoPlVNMbRcF95-yCXtFp0QpE9WN5JAmFahN_P9gpDGvhAo-SzsJxgosvHiAfD_AHCg45oSa166F4j-a9-X8TX98V9zn1IXhxssgrgi5sxoTDdfQXFdbmXYUBlN6-TAyp6ESucb1pC9Knu7xicY2ywRHrggJJQF_4i3eniGP1cati_9-A2FO5qWAef2Hbu7Bd5utp9BSuYSEiSEsksItBeUuCCwAQY9gzybDFrxdw8VEeNF6hDhiJAUWAX45GL_WuoRd-ORTppPCQTyxhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejBAeqEW3vdnkVG-9riDSukuQk38RwewnR8ZtqLE-rEaDjakBMajYNEq5G5dIfNKYcPqZ4Bi2beQA0X3C2tU0FHLsnZTBFD1qOgJcTtM4vk3aaMblM9J4t6OtvMHazcYycVqGspoWU8bqxc99n5FBuTE1GpnIX8VrOjyACJFUbrI_Az6XcDTXA0y02eD62ViwK4c2I5Xxsp-yUfsGls1zS-QdRtcgIUSAUs9YmGRPbkc9kT8X_2GN11KQr4At92TxXGrTLoWL6xtTPaWKF1UgbexklA-hiL3yFV4iS05sG0mLXkZjwQP9xnoGXdnC8PHOdMzfZS1-EeDa94XpL_--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WNg9ICM9eQ-MJy80DXPDjdUNyT_11BK1pSRurHfGs_cxdXpp9kASxoPPuMvqOAqPlXRdOlIEfWLEbhgcuSI0NIRyH39eqynaYnVbuAq2tG30Nv_KpilW7_jDRb7PfGYUdfDQAK2VQp2Q9AAOFSvT1CM3R7tVbIB8yGI2U22YE5c9HTASUvVl-m3XLPLd5s4MCSKAaTJgPoVBnvv4sOTqqkMdPrCzsKt3TQGJElBJEnJRjktmmQgAZ0rrM4eO5ZwUs9alwXqkdQXBOmS_lc1-EvDYwzjOrsXp8jfFXU2H0nfpe_N1nq-ro6HBXKJ6-e-5Kf-j1EgYEoJZ0rQ0uF2rVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tNwpcPlIzbzBRNNLSLBs1VSqJ_UWiTX-lgUWywOb7wICWWN65VDPbNR9SiF2rVt0L_5LgpDx2i5rP9Gi4Pgdzi7Ao5_7xzlzIY0t5lbXJA4jw5w6MUBFLYXICnbdHi-sc-uz8NuNfA-1Fqd7YUh9V5BTTiGwqPjnrGhQz9_GMooGIMoXSVRcbMksZ4DyAdtibrA-2dYKo1qW4SAANGHHsUJI88zDniyZy51f9Pnvl9shZXNbW6iy1y2w80Ds5DRhmxu_fLUTX6RV81jtueqz4QKQLTsSwQ3rAAWXZFdaWh6G2nl1EaxO3BJsIIEVA5wHgIReKEyW04co57dIK2rrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5yLZ1GWeOwojlcjmWd2vyO0XG_OcjTsKgAL8q3_v8i60SSNwMXrL4lQlPeZ5DZWYRPvQhG_lc7LD0VsHAs9z_rtB7rhfAxxAmwnU2MvVRgQPxM6Lh3AyPqIb2TK2b0vtltftPwoiU_Nc8HvxbWCXS1dpGWxDK1w2aNHH4kViA_oJzFVCXDWCYDNFNnzSFNydM9_w5MK7Y8IShXzoiXcjlAxABXXFMSmXfGSquIxS_kmt8ds0N5k7NcziDlHtYWPeeri2sNLMB5cYctvA0Z7Z5nnnm39tgoYMXEZMnvY5cJMbg8MirGgnRsmXAnoOiu1GzdEKwwuat5Qj9OR4x0koA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RlGF5A3RKnLm9D2krwOaxSMvANuiloKlelggnwi_04zE4T68M0Bg_EHztL5s-aoUQZSxHIZtE8h4bPtVZbKJc21LwLkuEadZJv0R7PITQ_NjvO39EfyP5VGCzyX65hZgLM8LHuahCNhh9zotvvDUolLRbcaZmJDWBcA5Fgf5b8bvJjzKZOMjQS9KlQ85cc7eyzJO8PKzNUy8PRWEGSFjKZJyTXz_EIwWBdX8VJf1ZJT7iAl4xLWOt3EqYhHMhWfY9mQ4mWGLvofh1PWyfc5zYiULv-VGiwudQth6lEhNSJbi2tqiaQIWmMRstzsAxwvV6DW1S06lCTLKBNNRTk1WZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfIrpCXevet9xTtjTfM5b5nz4Tv-q0-s9Sczg4n05N34xbXONhRA2yP6G3ISPWzFcYzcUvsBfpJ9sG04tGRv1yP3mJvpE9ZUsaEBrHjEUDA8QuSt7yTqaNlEADVRRaSA9lJ5Y0aadk2VFJUtdW_OCtiFq-OzDHJgMhgPVhpTMFwCLG3UaTVnYlTQ7RGEf2TOWa7kYv3c99vROPeDupQclPGsTopBSqTM6WK8VgyKgLXITRNF0lgDwg3XNP_w_hPYJs90wXX9vKkZwWCr2umLgPuYjDR_qdzVWIoHZauu13Liab4t0FTWOjidYr5JxdIbn1G5B8ThaTFRuQJFZ8dWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNtioufWv4HvxOM_bET8p9JkTkG37QfVt8PSKK5jR82fPIH01Wn26ZEF6ncND9WNwzBN06SWbe-lqt-qvC2rnxEGlrKpVwwwf5fYNILNhfLYSHbDygmo5pm3C7imUu9lpXXZKGCRe9UwiRbzKm2tEfxFNvTO1lvkQ47WILIBZAkaKF1U69QBw315l9kzEaUu1t-G5Hk0TWbjGYO-4NmEtn0GSAgdpuS4KfNkfOLAgpiWVw5eovVy2s7BMUYGrQ54t4TXco80dtAn_yuSMqpmYRFOgmX8nsPgAX09HKktbcisNDx4frRgsQ-OQRKHEYmrZj4h-QLjrGf2WnTC1yN0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmgesHquYWv0PteojfjuR-ZM_sY3ZsYhj9uHveVs4eKkt6MVoYJRMPb-Y77nQZvwzaxQPxfnUZTwEozxweAGMbn9FK1I-iu3Qp1ZrR652AhkH7tzPany96x_AbR2Ngu1DcogXkvP29oXZJenIPC8MQiACzHqv_6ZqpU2zUID3XuqRj3hxCenwrHsy-7LrIA96OQJdFr_JTGuFgzHW5qJ5c_EEMDtdcm9B8rYyFPKoTqteJdJpeAcM2bT2Ru01ZBdN1O2TNU3ZUM9FFT9hMr_A7qmiUY9n4NEBWKg-iIExXUbIxdbxJfEH8rNUK2IIKi2rZadcvKtog-H17MHGYWTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpp7fmbAxBGELp9WRtzA-eDpULB8t6roXf7VFEu3Gqa0ofjJ9-DLdEWUyTET-fJS98-eBrxyFnk-6Rg1-twi_X-EWnwoS-uMGHHwNwTiPxdOI8gEBv4uhUCtAWowmdwSmCDNZgBFitRjvJoAs2PYGP2qlcCq0tUvm5ZzcZT5YI7yyAimr-P9p7BconHcvdUEZcv2OOImPMwhOGN4ON_6x-GQsEQGzhI_2sSjCob8l6jg-wP1FkxKeDmYwGxPM8_Jywta4ip6bxI5zgzlyz7yi6SLQ574skAuiN7Y-OkbtgVZ9_UYKxsOI3bX38oaSriqUg_bDZ-eKvX4F7YBgl_Svw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMXVh8dl9Piz2BI66HeM70lb588zJAW0jSlnh4tEC_-JkxeblV9Ymgdf5tLM3IWBMyaOn4q3c1OD-GcOfvLeD9bFbxOEmmFbtU8iE45XKQ1ACTVhz3XV7KAqBMREHke5DalCBzSVDhS66Up6YBy1_nYnBH1XwamGjw_4vuFCMTO-UGqgYPPFiKrCF-nnZK_-vpXk_b3jNMH5ktyuYj1mDmuPeuHVg-rz5MyzTVJNQ1OfP3bAi_mogs3qWqlJWuRLgiAxeOka_XOa9Jjl85cdqQUbqgHk15erbANsblKoDMJvKyZmrxVDnlN3xVnfZLX-6tYq-nFEx3WQ91SkIRltng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K7n_t9ylXJ0UMsl8JC0FydM2_SaeAXwNMgAAMcRia8LQmIaeyebqX6yTw3gkhwbszjeQ89k7rwCIndCrUU0es1whLKCgF9dNR1vuYfeQqWMYFQxCZkaFYIpmy1aYkerwDqvSrY45hq0DInH4qaUIkD8AjOSGdQGMiQsZ3oBpZziltni0n0Tx6lqac-SldosqVZukwHQ-Z9yK7ISTuqk3WOa5DFI6Q5b0E99WZcY_aHvVIjRa4Cw8VUqfXD1S4XEBAffLpnZ6hC7ZMv86tuyv_b4p6Pcx1EcyDdKsJ4WhaVvqMjzrhJGE3BWz_b6XCVxd2ZxBenCQ7u0atpgf9N0kDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bhisOSgPzb9rFMtSQFxSLyKKo5BeeyPSEzyhjphJ721izf0r5duRcysH1RmYe_7yB21_sxk3WF7i43I9qk9JFof99pSBWI3XcCH4eodJXcW76MoWkpWMd95tTmUXPtuNEqTfmHvyIcNqn--LF21tYwVRTR0_dGfNMxpDa6ebMzoHuMrHb9MnALEZh9IwHhLE6jkGhA3rY-Ol7TuTmMO44Z3Lo3o5X62T8mfrZ4L-XNezji-DZnwuuF6GBT6kO91AhnhNb3YPjVYRGJD3QBz2WXc9EXuZJ3Jg6PwLPu0dAxpx-7pqWsgwb8N3CNIn1EMgK9nyIdt_U2cv1DGbSxHO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j2tY5gZ4zh0h6W1adPhC2Co7i0qloOLOUQPEe4KWg8BmNKVQ7IB7dLT4OH8PZIYc0vkFsGhJyjeLOk2OU3Vb4Q8R-5V_jx2g8KR11ov9IKjLY-yHJM9-aLQ0-xynmjmgdfFqTX53XibTSuUGBPU7VQ9l37WGCwd5vw8g_K7-HOqY79-JQht3sbewcgq4ZD4aK76fZnE6CyIRBj9OFh_MeJIYI8Lx1mur4TkmxmvE046cKELUyXj3NgFIsUz8rPGf7xif9WqKCiQ1lVAgRpU2zQNlR4tpD82l32j-43Q_DgBe9iefSpYwkhFz7nX-tJZsfZZpgUoTMKCcCBnYd8bwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZVEmnzaYDkZwP3HEcYR_25IUMZk-W3YHj8bgflxXpwD9qsGzikSWw5Rdg3F5mApKj02dXppwWudpm_dqXcsdS41H1rzn1ZawGUMlJvFAc3bOdRBlz4vJUEnJJF3xoL9D2ChCAddVxjQPwP3KNPkRbX2I9M8ptFh8QTrYqElPg53fYST-QUJGbxlyvBKjM6FpgzrUKKqDozWaTmcoI2pyEHwj154SvYCTcsWJalCMAaV3fHDIGs4nbrH0iKOdyWLV0gn30b_88bE6YKXRDI3tzEG6mOOtesbDRCZ3aorYgYut1VlPok3yxYZ8RF00NDO_8XmM_y5BtXQl5vGQ_kjLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I34nsUacSULqRzgSqO3wGN-Rwo1bdN1zioYTjSRf4gaE4v2zwPfpYir5QPQXOKE8nwGEldS-ks35zrDovnOwLJEpZ5g0hM923L-Z9ZRuVzXUJQ7lmTT0eGEwMFKvCogyVj70ZFKtBJ1O775WMeGwr0zIdGrRfMC7xzzFzfpuUPXqBSMO-N1fOCLgNeAP7Nd_OUUSGLm8-eTRyLaj5gtcPpBy-IcUdn5T8nrRgzEy0CbHAY9clYgGVYQXYyNlwPc6k99XAG_g74WJKejqpsDwGQxyBZ2MBfButyY4lYtr1hUa45VirPFx2vlGpjnweHAcvsxo4uB_gYXQ6NuAv2mWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THOFy41EJmMSVbJNGgSbnchrdAePzieJwwnU-2FKJJ5HStM1jty1IY9FBiK53QrKSiURGWgqav_iJx9-w-XHY2OxpIgneaAjxvz8zh4SMbVJq1QHXCQ-_xZNshORpDnQYKi36uVYrKw0rZUzXXKDIH0p9hGDJkfwD04nTDEG4DQrCla76XCPzenM1TnJvGwGy60E1T3UGavAm8XBQXlGxgGNXJl6t4CD_yQRANUkeHa6a6sI3evbrZIh1Oi6nz_QfhmnAAbHv1T8sgwAg7GLFQB9xd3R9UcEn3nOKBPhHwfDD3nUoOeZzxjun-YBHMRRP7JIR9R-9M01PkXAAOVgCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxLqGlf8a6IRh_swAf-5n_vP82fvMZutWZguQtZRXqk5RcAqJ7RnizH31gyt-7MxvqjJOBsnXKlTLSbgwWWRjPp9OwbybVp2hOou5xEe1j4boQQGLCEOdyEdCV1jVTt8g6fCvciBwS7Zj6eC_1Y-XOH3XBKRoMPJS9dif4C4omDfZdETV1VxeblxEBdsNRYRa_whTJtEywgrRGvAxlM54Yq_cZ92dTyZTOp9fpHSzxbWwptvQc4BFfwGbZs3Pr8b1yn6rkNk4KA0kAf2ZOjx_100dRizDE3QVZ3e4ssteueWbjPZWziTT8ROT4u_EtFib8cZWUWGozw9KxZeTxL-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fo_PEoBBSux1ZcaUZienUehRSRO9eUeKYAhiLPQbW37dNfrEeufP2JvuwFt0gUQyvfFy7iCpy59YVC9j917-XTnZYmx3P4UKgrgOomk7MWOXIc_hhA2u4byS7DdV6eu-Ps4DNRWjSzSDYGrXTozvtP6YSTZiMyUB-vPetrVr9kxWmTiNxC26NrY7TsHCw_IHJ20MRb4qhPL0DcBmd9xdhnmjUhR_EdTkPuUBfED7djzjORt7-_MK-P24r0gu8lm7Y7uRj7j4lgpwUiNIce4YfrSL_JoxgPruELCvHRE_sm1pgZHc0nycf0ya_Uawv05YcMFmXWIO3dViWUKq68VE9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gMxF9vWzY3CyY9ESnG6UrfMfHuqKRD_b9wOmdiw1in0eqVVSIp7IqYooPGBELeev0JMsGb2Hps37MBqSB3BBao8WqgPFmRDqOm1njzWOJmW5JWWx6MiK4EOqjPsOWj7alPLVeqO4chkhAWBguhqigH5U3NNnmyerU1mgCw5CfIm180AsWVs886JK19YoFVeBeNb0tmuX1TrlTo40AB0vfOLnTEFB0KDkDsBHHuBSsYL2YnNBP4O0eXoj997fVSiIf-dYBvb05e09sqamFZCIo_2We88C_-kqKJOdF9QN0r4wHiZoTQxuC6v569SVeYFZJM3wkE-rSQ4kGvXWg2M9NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAmwyx5cqt2P2iehHJax9kBmGochGYsfoIHx2nb3ul8uQDRvIYbrxjLyFSl5ZZ5ZmBK2m3pe0-BgDWO7-oQGyKt7duVvCYJy0ErvxPqo-URvTIg6wQn3vA4RzYxOCO-ls8H6WuFakqdveOhLFYv2pwP7BCTluSnJf0k7Zlp_t-9Yd88Y0hgzMxJs7KCfrnlJKh9pBs_JR1R9II2MZ-jKTdI7Xx-qmmhgTBXhm_il_AXyO2tde1S4-GNfYwGxACfzSOBE9Kcw8IyWUZyqxIW_3zykAKoHPDZlwr1gJrDr9UGrZ_TEUFpT_rx_s_hbJS_QFLLQd6wJnGGBK89CoXr5Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nZcm5XI1n7uwvuNgMmV_KZBgGF-UWz2WC7Rx2GxtNCVFxMEORmqvtxtAavUpuG0oyGwA9usjzoZI2rTBs3LjuicroFEUgvHYfOPkUMEBMKLBOwaTbs3x_Zwrjf8OFNPHZr7BGfUbZVZ4fPdEnstPAcDtj1ZlrjOhuUJl4PJIJp36AGBMKbGf0gFZBarX0hps505lqYgOPf8Gz2JKw2pJKQwltry6iB3l81-LnrNijFQsim8t6O-PygR6jlFi_wNGbkPFUu1aSy-wAzXi12osqSqzJpcWKYvnTpwkU-FK7ezBwNPl5xqWD19lKqpFwgLwfblNeal7CURKuKgcp2pxcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RKzGVaWOx1IJQmbQCkukMExkOHWoj7iQ4p28zFwqszk3JXbLa73m9e-SR_JQpoTJi2UDdFCQtZ4QMtoUZ0qHHH-nGQ4JRaFMq8r8wtL4SYxQWZ4RWaAX7QI04zAvST5pJ6grsLPWNUueyqzD9893uqV3JpPZt-m-qftIs1gF2tj8lPqby4AbA4Qm-ladUwqLAfHtOhDg4byVDa3r4s2TMkBg8Kiao0U-UXZcl0WmIX4UXQcHN09uq-ZocQZviEKoG5ONzC1a0Tsne5NZbunHMb_gisHls9huzNZDw3nCAT_OKf9hzoBsbrclkPdDw9EITag0ATYmgO9yP0DqQHvLKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWFX_G--1mPLYie_-8Xu8nxp3WpK8f6w120pYExEusyy6RMq9IecicDmTC12w5TIetwB3duRW1MYlqtHN6UW2uKhZInAe4g2bLPOSmUef8Y2DZzMKDlAw1QO41XwQKPJGVJgrmxKI9QcM6Plpaqhr192hAWaBtAIfsGOh9TqhjLp1z9nPVuXpVgX1gDqDkXv8DbLsIc89uPL36vTjcKYO2kqxH35oJymKc4s2MREZQcjSwFSGkOBtpsyoDP6WZYqhXGzBGaCeBawBTfNGmPoLRFjEfPgPyfj6gyvyEOoice10Yi3FosL6jyfvRxC-QUEm4Iu72kC3-e5Ljpuh6OF4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DcHvc8Pda3_pleLZ755lzH5qF7W7Kd-hQZDYaVsxHPPr_F58qSZu-r_jQjJHXTldT6tl6ICCMMFlX-aTtqUawjSCL_DASZNauUK7Ea0G65NyPd9pXKnCd-9bXfgQyylfoXxOPLfJRSrlsjmA18RgciA570ykKeTKbT2uHThPXYbNLCyYKZILXZ1_F8_wV7tQVpWNPqj9M_b9rCwHbEmI-8hOUhDIYDmjR-Uy685V5Cqoou9z00K_1QMkbjl5AnzymIcvLrTwMc514Uq1Jj8qDH1JHn5Uj9da2nbtXWO2KxW5Mkcimny0Zj-A2itVRRasoZb5VYBcNK2ZyI4Be8ZnUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaGVP-RpdOmldGtB_T10aB1XnIWJDXGcW2byUIPducEfcoBxEAyIjoR7kCfJdPeD5CEDev68icimMzg5Fjh_j49jcKvAmFjbJmZaeCGAEh5YEXbPbiazH7k--X3i2kfDJZIK4E3bvKZrVozISRjXUzF3DhP4V2qMl_QBQOz4i4hyeGnPFIPzUTBIOFZD3kJ51LctvTvlHH63y1QnfRQu0Ig6yBbWQ4owscldhsDUH35yiUiL_qZXECVE4-Ik67keG5yc8lkQbxW6SqelWSDm7RGLmDJqAhX5OQih2LI99Q8FPI_ptMDzSDExidB_nNmXVjDnkPt8PYJP5bPOeYkmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hw2dhAlZpa-zIWT-MKDQ3h29YwYRsn4LkwEgth5mA0lJpxZ4rSl6ngusSPwj5BJSjpz07KPR9onR56OtnH6GI_0Qm_XnsO_WNq6WNaSJK-6bkZAiIDkgcmU-aV9wTz3sX3IQD-XVwvNjCwnIAUWuKsR-aeADe2m3T7Dc12Hk24wxuKXcrs6u0DKK1cUEWhwHa8AaG5woKagsGIdQPkMkq-v4qevntODlF9LPNAdZRzS4q6UCUB68OEiQ5Vy2rPqam98Uj75STHzlSIAU8UIIp1MhBzFrhFe3VfyGelbpI1W2fgHaKPPbxsMDwtM4iHD8bDtSgv-QF_borgML6RTDAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cUClDeIrhXp_nB5DVvD0m2jd3SlTL9aLK8XEyV7PKCc5iO8Qf5nlkYW8osRTJU8bkE6vzgtKnix7PBx71lvnNn9Su8cXm-Z3rUUBhTADWqjqPpTqg0pUX-g9qmTNnBKUxlOu6WoFVQzcDUQ9cagKB4chatPtF7W2p3aqLVEvPKWEXvr3R1rDM0gebuzYfMkBzk6XSJkOCa8k-tdUsRO8ZEBUeZVldnnrsWPn6fN_a_siYnuWk-YftcewyqFB1IoHzKVcPpZ7pekrGGwAQ-9q6GSu91QOp_PFHTk1am7z9ERLrLe09T80Lq8f1eMYfb19uRyBMFAT4v50V1oi-GAGcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mr_Lzpd4uauU8hxd7SfdijwtYwsYc3XQWo_B4XvvNyiDYZ_KmmFrM8Qqp6PcucCokds9Fk_voE4C_URBEKtazKyYyxq6L6BIL5QAnTb3X90KlZzjec-dX_pSPoR_D17MdYtOmWehAUmm_z0rc5MzJVlXCxTN30yqfJkQ35Pt8PpDCYhdSw5Zr0uLh8kc1NyFnC98VOl-6deEUlwuiveSuYXHJjTSBdegAzoUeJm9UgQd6mC__V-FFBoAad9QHsuHGGdg0LCc48eKYZ40emB6SFCmuGyQwD7ZAW0FcH7Gc_b3Sa52-IAvobDGzE8zaq22JliAbno4M4ltrtSAY3EpHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nYNh5N-IaP817CJaCpEVTdpq0vGiYjh9pnwGR5FPjVfjSB6qc6FqXR87bhOZ1K7_ZZ-Y14f5LFIU5krtdHJRTNr7iuogxPvzY-hZW7xfUnmOofBZBMM4a8UO4E-bw5dF64LPZF3-mdfRLaE2Ptab08fp0wuGYMvTZ_GhVDVUafSeJZPZFLWaRcGx20GZDa2xLzxrHmV2BCRdyj6pN8CcFK4FIvGGk7bfreUFw0AtdlI76zkSwdzK_nPJPFovW2yApdCcYca5etMTWQ_Nxb5uie-Co9I1ZFI8W1AeqXtHSuSt2pqCx272uTP93ax-69n3tW0N1g7GdMyojdfRQcSkKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fvd8Z-Jz7QariwjUjAGoXBHDS5JLMajk8aILVvMOIF5JKG9zIYVZxUHkmmj9Au2hmxjUc-o3u3xZ2kcaXtz7t0Mrq5fz4llxzkeDCLq50-zNjmA7CAJPJHcL506-qVU7-vt8tfd3WBgTJ5JwSWYSJFwpBUgFc6jb3WLhaRk_BjrOag5KmBfTA9Q9-w0pbOPJ6FBb14ZKsWWN1PK_VtZVTt7097Iri2lYvY-NgI-yt4H1FeOtu0sAisW9bLjt_CkOnu4R4PoDy-C4W9YOP6sFkPvzCNn0OKHpJuQBBCXhbfKqfxU51HCROuV_C_kH1nKUo6pxtkeNGN8XE0KmAIX8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ed5M0rq0J4F-IM_9Al-DSzHfopTMfPHHoj4kCKVhUZJPKyZyGXpQxIvl7ZU1nHbVTuHKwnv5dBPQ7wS1Zw_EysypPiluyHXjvSaRMUTT649ANLkqRUcEmkXiXQ5hvio24AR2f1sDQE0oMPMG9eOpcu9JUdwJblgEH6PrfNzs0pREYqmDNV_njyGp3i8EMRZAmq3MDu6nYkw0Dmu-R0LXopmZa4ACaiablR1N7pjiQanIR1yQhkLTw2hobbI8mpulptAWtgIAYGOSzrTxeJ7Vw1aD6LsTqxfQaLFGd9orai61u5aId667nPatyu-_6YZQHCcpG9EGEJdAPrUpWHHhgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHnQBybIhDCkI7SpKE2r78ZzT9GqyPe12x-EOvN5WfXEW_n8q8mNP3or4AeZFr58rsVKglgqstyF4cS8CKHBfhSEt3_zxDOIXZpY5XUi3vAMMGKhy_ElLpduhj612XLpeAXiCFAlMpuhumqTYqI1NfD5ClG3CZTZmQLmFvqvtN5B_0kSVaKErOcTKWsV3lTA-diQro17De3P_h6qVjH9XJQX42Bm34E9_HLWx_x5srqgl9tFQFdtJYvy9dJgUKOrYFWvyjX5NHv4FQ_EacDqB-0078B9iwSGCO1tkscyhikrUOlxQxQrJ3WdUk0vjWayfWHePWlGFgw3tJtDcGNrAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DKQTSHLlBeLr3gDS4HZkKvW0n-ZuWx90i9MOdWYRew4iBtBjnheFR1h5noJHIhQAlylxb2wqZ2JE4CjwT06EdffztrWA1VtA-q1xB2yFgQ_6-WoXz2MvqFhV_kWv4qFx7PsOeqoyDMkhKgFl8if7zXjZsnfBevDlSyE7Y0h4xkYz5dtbFZpApAG2p67MjOE6GGVpcsDZgF-qFFa1vd6wm-GxifDivC6Ve7zvZeKPCg37ehF1HSGBmfz8nTI9nbAPpW6UQmH2s3jjo0q6kNdNsARJuSXzYxuoh2SQdztJ1ppWGFw2w8ra6Wc8a3ZTHICl9NZODV5076nLn69ZFGU23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vmy4QMJgEIHBpJ2BWK50GAANw5s_d_gUzZeXomV-cnmd3XKSfDTUzfhwmRmyVUb5kH-B4M_NWbmL5YvHTF68E2LOmEZdwNhum6c68c_OGF5hxUSXWg4IXOd0bJIqbZMIzpQcvyHJTh3s-Q3vFj4mAFcCpc1ATL4or1o7AG7LOIvQc81QlqqOTAIvRTqNNGzABpqJeO5hZ0czVBtJgeGGc3_kn_HNR6tj4HimNELJUSueKQ_IjyNMueeoRTSXPcqVWAF6LLLIuIjIg6SVtGdg8y4uKxJ5IlvIlR438SrIGnT7GTke2pAmXDWxjrkcRpktuYZNTLyj60pbpwVr1M0gMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LbCK0V4TOwazWqtxcABFd6ptoSBFXpPT6LaN8PGZywn2KiUugGuZOG81G8DWRV1YWDteMfA57CwI9paBaD_GqqZAI_HLM4j2aA7jKPC55LbpBCnfADhUxFUbzY_umuVdeyHG0XjjT3OL7yDHMUA8Jp_ELJPTqzqCsPjcB2pEA2xKXbTHigEvGKW7KIqLxXC3LFlksCVOB0Xko7JddygIqQDOxHbHVwb5fnqDrZT-B0gXs12Az-Ic6STUN7JCoI4TIDWo2mOHGXp9nZQBvQUy51kfuESBlfTV8KtH2nv8ji5L4jTY7xWX9iKx6zJfzKYeluD8J8J09tTBGETwdNia-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ddDUVYfJUmZA-YN9zPzcpdNy_xWmx1cKpJB-Dk6TYlBVq7CvAAJosNPbNtTxNg8JmMz9KxpP2-HsvWlNaolLnw1JfnIoaRdbl3s77GRQe2Oo-ovf2BKIPbqcT2OFesfsEA-wtvnWl9uBOO3HInDWqbQDWD4v74xZfW4uYSlrZP0wKJ1cHe4vRPYvSJ8BdOlgxrNlFAbdG1Ie5sz_0iJ9PGU_y6iIbzTkt0lpDWrmt14otCXl43PmY8-YijcoWP_qP7PXuoxJMRRNyzpBG6TtORoYbmYx9VsuVoAPcg2P1nGtosnAj4lKRxgIhYJsNYo8IZG8DbidnVJ9bPUUaEWEcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sfib5XgY6TiS-O4LNAJfwvRpmQKCv09rSo9qSP8tTgTPJD-nnTfrNIH2-z_3lVKXRJMRn7FWVka3x3XSJhade-HRP0O0tXEffHRI7scqeoE7q9ZOLmJNWc0qVTY6_ETtw19wzK3XXfRb0qyAIi4em7R6tTqALdhdOrOgUMB-oortO21q7WR5XsGYsCifR6SxW37gSuOKkFXWH4IZucXX9CSVCnhK0IF16H1kfShjJKMDYow6ZUkry2OgHCRDKFcdxIedJmE06BonsI8N6dS2SVoesJ5KV4oFPurUFzLoUjTAemCL8_J5y81TuITUESf5nULFMQHukizthW02bxJ7mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tj8tiyLo0t0DZ11iga-A36sTXlA0TiNSOTKJe9qwXq04prZfHAFHAZ5WU09ho2MEyiZV6qLUJxfXTzEvfGxlGw-SoHAXJ1zTypdvzRsgaKLLq2fX-HuJp0jOGeJtrkM6ngdka9V3RvMzMR513vwwuEmk2wqKKFhflUxcJ5j1jpS7Kaq107ADXu4Rw5qAYpxQCoop25aJFYpArWlb9Absv0N2Xybee7LpKC6Iln4qa9r4IHnr3rEuYQIUfHVUyjG_EUjYw-6aEx0t4VwAfJwy1Cg92zepym5w_o2QOypzYsuplHl5LY9MW4gEcxLKy2yJt4ym9vxYtajrymaiThq6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obv3PxNuv_AUrb0NqWt4kZXLFThs8SU0KCs0rO-OkgiSpggvlvpmFYC1tKE9ViGctUG8OhYka57jQV_4HF_zNwXb33LfCiBtjQD_0vqaB1hOdJcp83pVv6hgMGxiZZXOlLs3VyK_IrejOgVJv7N-kUkMYngHS84Rqmg3Ye_i3WhKGnVdQnmqFFXWtiWw1_u14kpXDSDRVuOHtL4vx_vYUkx2oEUwPCKaXDzz1UBZn0fD7xfWv7WTof9Vy4uKqAHScIoaXvKUsD0gYSZK4aZWTnjFHuHGAD2SciWSekTN-_nIhvqvp8BWJbgc646tInry1dojPoWhFz3czrXQrgoPFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCsfq3MIUZakFDYYPaa55x0NZzlkAMQkWFl3dt66WJw1Bn1qcIjuFV60Xh-Xl_Uz_FLrKunMCDsPW00aWniXm1-eMXlg9BXPSMxfjX-OkDJALvnkf5A2alYZSgZGgsxTuSfoTZxscABzmNb_nskWBQyiJ37NqkRjHyBqy9_XFNQTpsKTTkEAjaNat7z1ngTifQudc0AJV5tAyPgLuIMcE2Mft2crS4eNXdrva5DlP3C5dzGV3Ej6q--unUXVLhQvj8sA1tGj-o-w0AYLqgzZ7MjqFNcDzTZJiLDPvL257ODkd5bQvbkoYX7NcQYozYap3XmXbLfQtedhttX3D-LrOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=gfxd4THOJu55vxh2rGW4SepA6xviwPWG54zmGbA0oApxk1XiVTe9nRq6gTr8Q1oGH1Met2ML7lilEEHdFZLibbTGDqGESUbqvODtaI73ZuK63uScv18Kvp2zTAkcLbLjacmbXjNOA41yj3sbwj0o76Ca0jW_Zzyv5_rF1uXj8EqdPHw_PlQzZOS7olOFvo9LlOLVO8pq2LC7jxDAjSy5d0Lo6CiConhJUysfdIm6pvbHEgbHPMRIQeXq06ZfNNllS_jUr6FhUHRxgN4wZ_Eij0Opoa6UmTOiY3y8oLB7LVymGQuzQg8zzv6SCqCJSPZMjAN-Tup-qJIirkTq--RWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=gfxd4THOJu55vxh2rGW4SepA6xviwPWG54zmGbA0oApxk1XiVTe9nRq6gTr8Q1oGH1Met2ML7lilEEHdFZLibbTGDqGESUbqvODtaI73ZuK63uScv18Kvp2zTAkcLbLjacmbXjNOA41yj3sbwj0o76Ca0jW_Zzyv5_rF1uXj8EqdPHw_PlQzZOS7olOFvo9LlOLVO8pq2LC7jxDAjSy5d0Lo6CiConhJUysfdIm6pvbHEgbHPMRIQeXq06ZfNNllS_jUr6FhUHRxgN4wZ_Eij0Opoa6UmTOiY3y8oLB7LVymGQuzQg8zzv6SCqCJSPZMjAN-Tup-qJIirkTq--RWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KE9xj2YfH9HIHNxElV93YX029ArIX-1giVEWpF1TXEaw965qhy1w8-lO_HvjBBi25raC8E5JH41YPeF3i_gGckaYlkdBNBJOGHBQ3XUW4Adsfw0nbWh5hQpF9TjmfBw6i9ZQXtvKX6Wc-fGPugj4uqNfYAMbSUY1YjzWmiEmM_OWIEj7YVZGXM0NcQc9so-OcNgtEWwmE-73LwVVTPB7JDdPAIIYfg_Zb79rrE8SXYWkvnAr2JORaN2XPd25px0wCKstUiXyVyXhbob675rLfMskmQQuby44eVJYxmhT0Nw3xHOcOJ3jnfe1ZaHTFe0IYWuAXmYqi4VaIkbJVzZkfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eh8B54IljjABKNJ3-blGnBaA_DcxA31-xkKUcea33pTpHnDgpfPciNtD4B16R8_5yxx2XSVtSydAgyzxdmTxtPTppGEJ1puSvf81udijyKDsbmaW8NovxC7-VZIlitCdP0F0M2GIpf4ZK1sqSycSx0F8WqGsxc2wqk5600vK7xDXnyWqKN1tfgD-zB7nQ5-wkiFeguJJjLDSh6TwCt1s7ScC-G3NSAd09flK_jVfsLGz2GSVQvI-TDEiFYYQmoOoEQLVAyIWSQux2iwb_Sztxb4_85yHMaOXIxzntGCA4anYKmYzpsQ-f6vD-jpGsgPve860uOIv1Q1AgA7mEpSBVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q7PRRPIofeqTlN0rwWy9x0s407CrRPx7ok4YYeawhuGdbd19lpoe3E4z6RP3aeEU7WkiqvLFsYvkuuCykTgT3d5fUFJwQZBm60XUlqS4LrwMYAfxM9AX06jOv-4YgkY6d07HsmEVDNqqwu2gH1EjHARy43ndz24Y35nGeXznxv8jrjXGAUiALW0NXVZ9aO_qykoYyH93vCB2i9EeKobie9zCX-UdP3CxaKvWgId9aaV-oc45v8zug21-LiY7cskAuIq-bKUE1yDFckzWeOSL17-aiXXFxK2PE58ujiir90g-wnPBipJC37PW4xnGUp4Tl0tGloUwsN-OG0TKhWAbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f7lvm4mTKQJtEMUGbE0mh5xjqUo6CRq9G4V9ztYGa4y11wtEAimyASZEMmCUUAjPk25ns1qYeBZ5e_g626B48LZco3XPbgBAxfTt_bfMcl9ZReOwM1Mqwzm72XxI7LR2KBHkfWNgR_TIei6yy5wfRUmgdPWs8DZluQlWjj6AYV9WVl1JGtXM4H-5BI4PVZ3Sbg1xMPLoeWsSBKAFZsgyL7L3LqPOHnnXHz5AuHe_zQodMyBrGYMt4tiOUq6SWij6BD6wchc17GEbFw7eZA08THsRhNhSg0koGvwEfCqFwV-_lCKwGXIq1x1tgFG41zAs5crkcrNhsodNojlZn6VMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7Fsef_rk5Hzn-6lFdeUGS5YMBMcan-5j-mqRg5XBAugwOyDdr2DUfhxcG8ONTdTL8DBTsjfSJlwLQd5stiL5joHQCQrIFUz4Lqig9rNFIwgvvBAuOmixfWUBoDONQmfdacu0bzFLRjLq2KJED4FTq6av72G8rJ9KoMISTInMJTSM8rk73O09b0JoHnXiTB6-8dNMDnCB37grFOetvbQXl_ACtX4svASYfmre5Aj8ngk60UYvevBhxdYtUOXOyIUVevv6Tu6NUT7dP9mxznMNzvTTQQ1xeF2me4ugpI7D5ch3lazGzsxcHwUeyxeYCeZWL-1GjtUAFT0t14tqltu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jiGBMZiChGCxlUhCY9HkMxzPioujzJa13LWllUZJpT6PHERoQmEKsE-N9PTYPCrZXa3eHXmatRBOp0pdEh9ugOULbbFI5omkOdSUwvtN2fUHS-MHMNFh77GuQ7lrDq3cIPV4CV4ctvVDC4T_jmdz_gMnW074hHhoEGOZahL72ucxqcQkHeOKoVRA56-UycYFXp5-dvTBFnQfZmK32Gs57cllkLaDVFuIhkqf9qSBsWMswY0SGmn2Z_yI34gWogF6MiL1hdNWObdBjz4XEodnzOSRUzF72FfRQcg4jbOQS6fImqUhUrYR5Zb9xUmGCq1EerqNCovHNsgnhqLuVkwDDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d6XUHF482go1IGf-DJyqISud8y_o1MEigY0aT0zTdcyQ7tLPgXYBOgLyhE33hEjc6KZbIkWovOpauIB1-LImPKPKZkwxl1of8kpnavkqyWrGKVurMV1MEQVrrx04gW8ioD957dSfZGe4V7hy8uPx3HXlQmTtbJWBC-TNfPw-R10T2jgu7O6LvSVx9f8tB6fsg0Vz4ObFReinGRRbvQgzlivaqruIrZp5E9qQ14zCpnPATR0uQIsTqPUyrnDJ2X-x1-3KyPf1KzUOWS17lrgANU_EjzHIXIXRFgFOlps1hGqT_u6F1DhT7yXWsqxsaakBLV5Z-1kBCtlGNv5V6ECAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p9iaqzjJrbpf6Ra6mJ0InNvg9fYbns4XqCW2d5nZnENd8mK5Sj47vs3Me_cj-DCkBUpEhBsRepdAeMExXYDR93DgESS7ontFpxa_FijX3axJCm1nm1kKvRoFGHpnGroRH1Wb6if1S5JQ6ETC8z1lBCYPU-1_nGC_McQq50QXUQjenuLN9O5jtjSAi3HMw9P7NHNz6n9JqIppu9VE2T5j0GAxYma269Xs9eeEaCNO8fWOrqe-GLz4PsVky3sD8UKL9PXYVSAAQik3LbI7wX0CC41qbZAfyETFNjbJi1lpprzaXPLblayaKov6_aTC8HhhsIGE4eBpLNO7LeqWY7nAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 64K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfuskYP3AaNjBWWPYyIZOFIAJMSSnQOJCbCWx6NjLApN7Uoie5n7ZEQNMKnoEDmXUAEW39qyNp84Gna-_sN-LpBS7MQMYNfc6DAusmkLwuwH1vg1mZnXM98CVZ93sj8SUd26dyxT9rhoPW08eB4HI2hVKTbcrxqSVxsv2YvG61uWm7H-Mt_qXc-VBkG2528I7IM8XsM31e_Zb4bEKyo7Rv-SFlwAdADhSvLdO6jdHFRCRfkB0N4aPwaZjg1fDj4g8u1_hxPmhQgsmAOsz9EjSjqLYGt39_vD4mTNUbmlPHLGIL66WOk1kkAvjZwcmt4BTm55iOD7JxdA8AUTtjM7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
