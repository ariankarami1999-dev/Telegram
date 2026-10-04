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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5QgAvcDYfx1UGP6sHuJg8o2cJxYp-CYfBiNMJjC5c1mf-ch0r8DpHrY6BGnI7d4sExm6QU1RohLE33jTfDxEiOoNucN3wL4FWYP3Z7x4TYK-7bI4DgC1Dor9avoIGy2Iy5XM17IMMGZmIaPCa4QpoTf5dr-cDcGSJPQVY4EQeCxj-lFFf-e17HF54W3qfarytlrqWpJBVV_OlFJy5yt3jZ-pLxrfrUE3r02TfOc8BDeZJSJRpyVUW-i0fBmOanMUddzVGkEG6fKltd_eZfZTDhs98mvR7aNEmzaDfRxvKjdKl_1TuYX8RrT_8RFBcLIkQOPgg99Tyt4ALoZ9vXXPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-KBmnxR5MyyAzIBj914YdX4aYSWy081bwHMq2SLSyqiqXRVPr46lgqpgUEPjGpCWzUwh_4093s0RgFjmaN8nvu-VKfoSwX0DmHqmeLTRHQ4qN1tS-LlHW-P_yX-vQcsaoRarQn7_b1HpFQi1I2hzDlOBpfquJzKPxQ3LRhXE_4Dfved_AQxSCBScyFNPWDzEG7rO-6rUlIMMj2zlclzoGzACPxexkRf_Pa4oglG4SCWToRwO-Uc1opHLp6kuIcgqgQBlFH1tVGIv4M1gGaVQP5rZT20RBXTB_y7_7W8EiZNV2uSsslygz3IS09Sufa7mD03KgR8wDdyTYpYeKO26A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjHnfc98S87vH7vmgqeZXywvV4lGawltvK3SgCaIuAwiXoopqUHI1Tui29YyqfnXYCUrmWn70CMyx0nnNHizYueoXuyOC8AbwU87Ede_Tmp8czOOLIVVyA43LgAG4_jbBfYmsd6mQXPmW-ElPR-HWzjDvv3hZR2B8Eb1Pv8f3ZGs_4dpjHYdwLFXayorvFoYFgHzy4LgeRH-M8GiWR0ITARRPrIoKtsn8GtwOGWtfC9HERhacfYxeQbwZKp7xGaoZtNBwTxMkSacNmN1j-ptLAe8y4XLbYFDqmkC7RebFaCHi3oiJr7HtGcQnwp1lo3WYIvzyZ0X0uvfjXUf62MBxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gaydQtU5pwUvSJWjI32RAfZRXrMWmkTaaYuY1adwdW_oLhX1Ik8MjdA3gabjuZjfJnMySyKa-O03QuwiZ-IYNeXUbPlO23d6wIvGh0ECzze4rjUc8Wt7jJtwG_6qWtvbQnce_PyytuuGqGLSNJblwsDzoWT7fo0HM13fGJrY0M5CeFSr-5i0ETSv55choZCee_gKgck9wnBeFHxdjt3Bi5rrt5PmDmX1I-uggh9EMY6upGiVdxMk3CC5EhBTnK3SdlNKzPqNl3oauw7qlQsfYmnxRTtEx8pzFuioJIfDXLfHDrtLRKtMCmcwcNzNJwxPZUmRIfg4-8Rk7ERuQwHBcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFqzneMzPpzh28nMunquj0PfJ7ZWQMO39Y9fDxFKo-aLrFltptltiflk4v3Yir_TR04pzbTgJ_nAFlw9sdgTu7BcaJa12a--FHmmsnGp1CLwl80kJ_97eu6i66Fex1yw-CRSws_KdHF7mo2QipSHQKdc_Ro1HXLWjpDg0MAVaSysUmt4e-bw3EEUfzTCYPV89C43wywS2zkE_AX6oUg9FQZuKsZ7MZC6ZjInZpm1F_pYqdu1AJmffZ7wWuCNnRqOCNQvh4zyCfcH7YhjWEqKF98qjD5A10lq0vNPJUygS14tvY3vkNhqrQr7D57O0rk8zZpfF5Lz4o5FaXmCWuUnuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C74WHE1mtx883uHfFIGPABxi0SEq7Wy79nKQtfAzP00yGS-9QRqlGypWvikmWshPbgKwEGDnJmuSabqADcJd3R0LK-wTfyjJZ-ZlNh1ESMrIqiqQRAo71-5DvyuWqgu4SMiy8V8XcO1_tRF9WDi58nNQ-fPiFdaTxN9iu0go9ayqPRgFWbdiZjF_2ZZgR4YBAL9y2ma3lElPgiAlIrWfVeRwJq_nzAT5fkLvT0VO_c_D9hYds6lh3j_JfVOkdjRz3PBWrwmqE8un0155glhRzsYd87EXEhy8sURvrUa-AA2RLfazMAlljajVzATKVplTwDG3Aho2fD8jysMWFtPmVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxV9Yd5RKhUCwq9D9uOl8YzPBoqB3jyUjG-W7wywQI6bq9jE6CRksxlIZI0cNue2F5-L9i89XQbA1Xqou2Iz-fNTXQ6jjg440_LdtCBxO8ObQwMOI4orBFJGNePZj9OeGQEpaCXl_VsOC2KatCV87W2XW41u3_sr_rD6g8Lk2C4mAKAqaLQOCpBOoeKs-rWvm0VlxjtPouUFzaJSVeJix7f5GRPhEjGbzpjtPAob_qxmjw3T8UJgbWEdq2RmD6FLO7ONA3g_v7xa4WVcqiWoTl00coc96KwDJb00bt7tkEcjZsYvPnayHgpd4z66B_uB17ZHRnOL-JOJB2_ZHhzHAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cC64uz2uJXFEH5Fp3DBrBcdW8IUcTZS0BACGaL2dmNofCm3W-oFnQItxTdaM-NRsz177f4ypzfgka1m5VljSSMjYO-T3EhwwSFndy2aHng-iMWecBRgr4AAPD9zsoYqMy-wZdzHgqbXB04P8CGadcyPhEzsBnrAaVnA70ZIaTaE48MBtnbyC5f1mAgLxs0NurpwRZ-1riTm76L1TJRwIQ1yR-3AOn3DKKm7ZTPp8nOJR5ng4H86GF7KOSIbb_5FDf0_x1VUKpOtIOGGh-XwHGp4UCOSaankiozy7i21RYMc9NfE-VvHKRvhwDpgfYbvPW8s-yGZamOMlBLUCZuvqyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqpiI5gVhqFCIOeAX1oNOtMv9QjntvzjehgJHiBl-5BynNVJux1PHRP5jizQ0Totgwbe75EDa9lfQEzEHnZj1ap5ZKy0ypN0QEsiuz6F7swQg_gAaXVfIJ5ZkzmUpSWKbNslPhyDE5FCJuC07bgqq-bDsHjYzj5yAHl8LHfn85yQNHh5MulSoku6sjruKn8B25DvlO5ciS95iIFo-5MrwSZIXbE8mWpVoz74-14AOUh5NnnhfJRZfaVlBPRDgBS8rXKJsi_pQqMLdUrNnc1jDn28V7kw0_W-6hkSoHbWSNDqqP6RyvijcmeQKrqQWOajRIoD8f3uj_8Eem6wCIz1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_kTuhWp94BXsDVG9unPABdZeXC9RnrN1sJR-1-KJ644ah47yaslET5ykLRH3O5Vom-urrmZ8-hREIC-FZOxZJ_fsldBkcy9AjiVtRSEcKTm9LTnd8FBNLfUbQFTCVJW3uqHaVPdl0g0G1NVl7ifP_lxLMTkmYkzGC5xAVuvVXihNcMRh7AkF9K-XUDwI8m0ovuiwnczPL7V6C3PN1Quz60UwOyqdWKgmzlZWaRYEK3WRKmf5SBKdWAiMFPiKKdl9MO504LAxD7Za20cuQcNZ6pDJY5x8Y4JctpYX1HOua3bsuDmDgVJeONb_ZTh4ADK76Jos0CZefS-dFsDAnmKxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iQJbyuRPOTcEWmDUKpfLqFXb7fTRYjjBzyqhnAf11tNGE8ox3sE7C_bGrWvAGezXKG-J5y84Hp95jx7BYJMU8PjlYsjX8zKe0yrWTboJkYlRah_LtmJuYTGEF9Ch-uuQ7tMzc9u4WXD3ZLHkANkHQYP1c2AQtrsJjt5KmBLNS8TvRtt2UAECyGXFsdBSQ35H_82x3qql037pdPJRABZu2Fm5CLr3rWTJhVqL-j2H1JvQjxGjQkqm90GTrwcL_hx5KZAY8i6duAZL0jhShm3zSGMhecrV-pPtbyDKl1TRi-UjsneMSjx5OQ89CaV2AbyolDciBUX-nMc4sHDQZXTRGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ED2EnB2FcatWyczelrr0rOStgyn_2VTmpNwkpyi9Q-z_dgxq4CJ0V5fIhCvuk_vieBY16-ILfcQVlVKoW8dhphaZvZb9vT0o2Xg8lvZ1yY41Jvq_7v50Nki30yGMGYt7tBnTaETqd95E7WIhtiDD3bzdweJ_b_6Yh6mhS84ZIzn168WYq4oL9DIkak3leR-ix8PrUcV4B5A6g-oHTcZLl-Q2WQLMydqGzRl2mfauz7Ecro4Vt4P53_0mg7XIHqH7FiW6x0zsXfO3O1i9vCAi1Qj10BOc1g4oZQpa0tKz2wQYVGUSaPLvGYIFHaLCSnbN3_Z1wahMkXMkP5ZN6OQ_ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iiyJ_6vKV7k45IIhG3N3gv1kcr5qHFq1GofdY0SXU_ZDhG_gLSnAtglJG-wtsa_e3QfBnDaBxW40PqfGRhlw5IrDrFjmdP3Vvg4dH44NgStV9CyF58q3V3EL8kDRh_iJxIY3rQ5s2S3Efj3oMtJ-6UkZLXLL7HziQHxKGPFhhCPRkyoBLY_1zzokyhzs2dYQ6Ja2csWGZ070Bt-AQYs6ab37TVcLrTWZpnZyHiEj5ee3btaVGMukk-NIDY604OfgrpPHb99rFK28jUrX81Dv3z-S_clZFAWBSnta5oD7x46KDPpX_3jAXiKl94DLl0GSyTehWSt5tpuU2zL7r4hGdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfJ1hsG9JbKZl7akPyqM1UnU5qRWFBEOVhn-1Jae7nfFG7nqDOnMhLFeqWx6514xP82Bp3CDLmoAY3PTCTSDs1U_sggyKMnDjiMvvzPNIlO_tpn3y_sgPY9YzySM5-RmIGZ_GtNrOVm9hQkexnXJyaySLmtgN7kLN6FhrA2WaT7bchuQXOiDrXGg2oPz7Em8wSqaKhXYd6kDACjs5sDrsj3XVE8HLYCR5pBuYvbbfAoiYwIOhGxd_XuDWACj4R9d7hM1fEOIlWxM4djD6XAcpSdtBN77kPu8By7drUO5pbAsAUdb8Svx1AfEMmzaKTCj693JCB5W0-XvFDEye14NQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ct5tA6eAOX_Ad_W1ExS32jFCSn-PwrhgmXVrSOcJD098A4lJM7vGVLdGVQPyACZXJe3v20cGr8EtfHF05FiMfEISTXonk9eIHNFpHy-G3DEjNjKvye6sY-OIleDekkZ5sMhA2Hc7M1m1HjURHVCVukeA2RDij6ycG0SqORPvAQTdIxi1nLtcB1cl0DHNVa1EvepDkThO13FLXyuzUZQYNMyJQT6DQNUaw5nN1cWBIM_lsvjUhgYL1LjeWZFf-s6lLW3ultT1zS-HAOPMpEmdWEXFgIzCgtUHJu_YYvKLcMUYKnu3SIIqt_qua7jxrQjTES5Hibz9Vl5tJ6ai9bRXZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oV-nbsYRrAo6IoVtivNOnVZs1Qutu0fmCqsGv8GoCd50FJKrDID3Kv_ej0rtu1AbQy_QBns4Cqtp8shcmsaVCKxjP4srvEB4qRfcs_19ISeuOCkEa22SJAI-hn0ibdZUloDbFcdyHIp8sY3NLwJItUCl8hQvfUDAWjZSJTRlqs0X41MWtnRUv4f3wjn5-65W9i6lzVtv6oXog2dxPPqd3lTDt8fJ1_-WcExbxQgEjPWfDjYmwnDNQ1PAl5qYSEk9bBkLf5uK4VfTO3O1g7I6NxvaOJyPyo69eKknKVBFMW-4QNagmYpQU-9Co7iZmdq080rFmRsB9s3UUoTJVDoIqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OU7r_FooGz1eNLAlKaL6m89lRuj2L84_aA-NFBv7OuGoue_uesLMbsvNFdEtYpchJI6wcR3gKYK1C54j5G7zL5w0hdpZyKTJkf9VxKqkJw6nObwcSqhnbQezllVgzv5fuqxtb93aiM3aR9X-CNlzXvgCmoD1ocux4DPIwlgLBYiIryV-6wf_lv0ySWUvtKnoYfWU1Tuf-yQAMrmpkKhvF4gnTeJtZjLLp-D-LlYVjf9cv4lY2KDI6dciEuXSHjWGq4EkE4jAmsCw1cAZvPDt6BHbonhvckrQh38vpBUQtv7RHIE4_pQpBT1TrNu9zhrueqSwnaYl5MfRYIzgYWPOsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dX-zmr23UkbvejXbbwnUmuuSEAcEySRpJ17U5LAmMjoMmzARLMyyRiNxetUfX6XwW7vKBnnyLcgKAqGoqaqJpdCzkzDhg5w4-ZmghWyJSFeiSK-Qw6gRIjaqof8jjZVV6bid02F9CVqxV2xzBvNyW10zjapitgJ9bdn-nbE-jgZJaRB_PfubMXdSgdB0XGKOtQj9qmAYxoEK4KCzo-3z5Gwny5wTwZ4Hhne-LD42NUWbgw_yMSF4c2C80f8JBGZbOYg9VPrpvhFS39ASRCm3j6m4RbrAOWPzvZPegGXxoBdhvUfxry-BP3Ira5FNCjPMpPpnC8ljUO4kXuiC6WjI5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TVDp453zlMIngFeUeWscXmJqkg2JCWsoBYBMjl-YRoRWajQjrqnP5YgOVyf2ZIK1iMMmUK2tM73-9LDQYKLbDzWqbafXN8cUSbpAI6syTCKDE51El2FB3BcFC4ItUeMdXEANyYmYsH_iJtcra05WheQBGRnNz2RXz5gi_krfPbVSxuwHXyCXA8fN86tit7_FX7g1hwkd9s6A7iv5a_OOKMvyrY1lC73L_rLAcSoeDfQZwUQSafXIxiNMLxdIAZIRy1EGxuifgUb5QkETwjJt-qrkJ4TQgplbeb-4IpsY1SujHsfAD0LEcaSaisshc6RcRYhYAZlMmsjbDExLyn6vaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V4-v14XibkPu6ZLuyEp5atQK9Kh78IM6S6AI5JU628bN0Zh4LkfVqCR5qkPLsiW77yTAuD4zvDS4JI9HpEU2Czg1fP400tGzomJnsJJRyYVDXlhM2OWoCrzbAR2HaaMSPxBFeoHjxbTcT1wp32S1IXCufIK3MpKBArlbcf2-90YO6J6OqvssQrcUVJesonqqgvEQAlA-rfrtAyKKaZSrVMPrf5Wo1w6vIAaeCqwe6xman_4alu_coU3kjoSz4kRPJeC3LZ5kPWy-z2_RGgdcNwfGsHRDVdkRb_b8BCDK0JcIJuuLbOvaFbF5wddTmh_ZBnMZdR6-6rdWOF23RxW5Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kAal-aHTB0Res2xLAruN2LAdKsxdnXhSi-h87S5ZxqbAyQy7f6t1ajo2w88fNhGzPyI9co0-OXAHEKh6zeOdX8iq8nZHu9xuNOOBcMPO1OFgGlAksUNt78Pg7UGoGl64V51mBAd6q13jcrX6NbizId-VDmk7FI0mx_nN8JTbUvDlz8btODkFgwrrgXZ03HyBl0cCYECVy2pwMWMJSp_Bp3n9URvlRgoFiwUIpl32ez455RBTMLpZUWphHAyD1qSsCfuLQjN7ef9_MLUx-H6vQ5fuESXi_kLoBWISH2kAWmXL3XwG4qAC6qRLM1tP_YafIfGRDIK4WAMaO-6Nk7Kqmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSNTY-Chv6huj6TYT0n2uvmAGb56MbGTeBCUns8Vp4gVeeYsrkVDx_X_U5NRTkerhKHdCr0PJft6M7bxVhuATGdLb4ZVlu3dUM6AfJeoGpv9l4Fp9mQxCMjCyWDD-Ihp5micns2csrLPdceiNWwYtjmaeB-h5QAP8RVVeVSQl-r-Ar_loc4lY3Ou0-XMCLR7F-VXHqNUZcROH7ucSMFw5L7PlygWRY-RWNTBb3QXKUZ2EvW4aXyLsT7KKYL8oSyGfCbOp_YCnbZX2vmg_QKbFStb--M0kQK7Gulo1btCU0qzFcDgM_CSx7Q6DKz696WYf2gZcrA5oMPPCufAQuYx6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TWPFJ6Gn4Q1noVvXY91TSGZf3vyHtyJZgYfJrXmPwSIHxGVy7xfZa8Jnl1T4yUs8-Ekn_0MEhEftJLzdsrFPiw8qVWyV2J4CMXqj5m6UqHZIFzxkPkAY8BC8geenyrHu2-yuDLbw-ySNuzfnYSErUrqpBReEm0SQUWvf5SjXIF9ksG17LD8BwzqlkSJzAuWf5lfIyhOYKbfMGNnGjSKbcSLNTDCxDhyAkNHyiZEdytYGcMfrqrNV_8ICwMQjQPNa6m3HYKIfcBzyGiYPuoOt9NlB-miaRCaQUG4KgMPYNN2mDVNi0GQYTL2i__VeCTSQ0M6DFLOFLaEO1D_kOlS8dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VyFQDHDIHK-edlGxYvj6c-7bocP8vqNj03Rq4WslSg7SpliAGMD8BZI0_xgD-kEDS82LKnzK_Vs0QkaCFMMa5fr8lq7MPMI2CQBUvvvTkNg9xIEeRKj8Hjnx_e6LfS_0qiUvDVan6hJ7Saa996isYpHrICmQ52eNFMjBHXVduVQoA0MfrPKjAvBfszZ6tkP9vTGiESJydLWAIrhU1PrPzccjS6agvHaEmBAof33a4SWgLA2xdSlVMe7My_iTWlkLL7gTec4BlYXwXZfD5MqZm0UeN2aMclLUK6AnuMzQgIFmrhfcVqn_wiu7Eh-O25FOyYKB58Bow49BiiXpdzGmPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/duvyRRYrcF7F9wlgNuZ_1oqkxhODgsBKZXwOXNgdzEI4Zt6mYKJhlqVPHNCsrGuuovLgNXe9y_FrBiQa6iAzaDtoA_XwsW0PCPJp799Gs8Uf1QyflV7IqA04T70S3-PlWrLCWxduqCj9dh9wizHL6MzTeBdcSzpkOK6lNYUuB_l3T_FFuqGWLBOM5dld1xuQVi_iS4vkszpP9t9SDb4kiFQqwgiUxHCSTuePeKvTTDWT-Qa2UMCDnXYF8AH0Cq5Nwzms5QMdsj5yJvUhKR165SlaexrqOSV9wHewA8nyKIxwEtLemCjNFDcM_Pj_HMwdtbM-Dw_wmb81YzxVR5qgNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJ42rmqalEgmOYOAwSjcDj2FpDiPmLNnu0RymytSHrwX4skddqt-8KfYqYNAo2DbGf9z7Hq3EClFLa_HroYaoI04CWb2d4wf_NPeLYjX3aovtlAOoZ_2kJ78OaHB0wl4pyIe7yyli2D8w1lNVQ0Khdol69n8oqYo6EI9iPQuPJfAJlZ_fYzSiCQX6M-IArJ8IMTSZptipfeqrGZPlh5cFg4jWxZOtxn9AvKj9kFlQcNQaJleveWuP6bxe3S2adKOJ7Hx4zk9od6ObBTLkzljq53zrrDbUoTQrC5oH9IS4PEDs9qnlL2KyKBHs5UPglx3Al1gPM-wSgU86u9LEum2vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9rTnnr2rYiQ_e70SPXCKd49qz2lUaGxrGlWlXxqzbIpjIPl5dMGebEEwAkyUkTPmzix01GL6HzU_HH8fQ_NACBWGdx-rt02CNFtrjw4yeEq2WZQ-9ohqNFXHq2x5ePn6zy901DbmNtczIcsAGoNY9AYKJ02oY5Eh6qSc_qyb9f53txC9JJi73eNl8HSzUFq08dc7PkTSEvWlkkSfVn4CtAPOVYCGAhYZcIn1e-Z4OVHF3iXCU_mYi64HwMFUUo8_AM9WBr4BZKjbm0KKz_UEbiSIzSH0NsLySUrJJ88yUrbPRuTaqa2DT8u6_wPx9ECocAKaZCMZNlLn5EbIFDHXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W971GEpG9_YQEk7hLBpX42EGeaZFcsg4AC8HiGSw2clC0fppYrCAhLQpQlmebhJRFni31WmzwTwux3MwMY6Ofi6HpgbgECH2BypeNON9gWugHQHkMLc54BhBv0nW7j_XofETjcFaL5z98a09hZzGR-LqTMBMlOgNTNC0XEHbvtHRZJSVu-3F6L-UA-eofHgwi3sbU-wFlaO6ZlcUXN2UG5TuES1Jr7L9iskzL1vQOMl1UBsdsN9eMW-92Q95c1zaewTDApkTRcLvgJzD3Rd5D7OND8B2abZuRpEAAJnTbfSoSsRE7YH65touUNOyeUxAIg64qQrqCiuH_ccQLQuUlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CI6bkya6vfNocu3i2rZB1AFFqGcE6SHnuXgPuduA3Xf6n4bgfwrYHd0f73VYanBdHES6agyzO5qvBsOf1EWr3AwBoaWWigmSmAW4TICPturUgPR_dTw_bWmmNFI7HuvMt0sH_cVkRyt4XliRhCSfze3-rfskDD0rq3t1NmOE8IE12f609jWmktYfcm0GNq9GkeU9RX87hSVwJGkgiH3I_alwXEgAPhzof038X-fYr9KeWsFpWTRxWIR1yyj-vKvmkZ4q9hgkNkRvkAJcihhImpbUatLvSE38En-NFA6_mQL7yZzAG1dFwuubwek_zbrAeZxX4NZcZnbRei7BgltWrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YH-ps9amYEscaR52u0ZbUe_Eoc_ebYca78rFTaR61dcsV6nKYyftN57vueHVoa414bExrjJfmU2wPJ-UWRjI4TT3t4BJOdkO7_lFsqCsJelFmDWWeyfCL-sZ1Q5Cnn7q7LvdFRmFlrRQOjrBNtUzwzOY37U0qPaEGerNWvo8pKfXP9SK8Dmm__vAkFZfOFAV1xF0w4SR7szAZdO0oPY5ZMBT26IL8IFdrMxpr2Zy6MBU78tr_nBEkbEfqIjxy2g4QnAQb51I8Ye-2isoHbgxsaGLOi-gHnusQAf4k5LWHwCciPyST_8-ommXzwsLlAbx2fYhQdPKU7K03CuI4Q_dQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9oRX-OxOhhqH2iPl8HMrsJ_ukfSE6JUi275Qsox82VurO8l9kMsTqMlli5e25bsPWQSwgjs8T2U4WfXPvTx21llwdBuXuIKpqJoFY0bd-5KR6FnSfssIg77SnnLuMM0mi7cJArzwq2taOtkFHu9BsbVQz_K3un-dmj_ANJxkGQjvAYp5OMzgtWaIeXq_mZXwpI2t_GGq_LS9ji5LRwX0dk4eOM13AFp5sfxODQax-QJU2Vnc10yFxDxwjmyInKmFAVNgL9X6Hh3pzxgIYLwmbehFP1WDuwCk2rS5T2vGQSb-7y_6V_NHIL47vzDJUmK8sZ4QG4mRwWNrO_q1QIVNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L07_ishQZsG7GSt15T4NcpN_0E8srRdJZlpvR917-Fo7yiUDSIBuyLPgMV1JgKzHtpJndIGHdPCsFu1UxDc06OGWpHTi1zpA7Qv-lR6gUGgoy_vWR-jffzOgBipm3xDg559svkEuvNx1Q4IKdbCZPxEcq4vcCMcc8ULiTRuqvKv4rh17TedQVTtLDqyHxQSlKn5o6a3635h8PXUAppu0sxmsj2bcrzkAN9ISkjaYZlAfoOS1aojviw_AkaYUbW8qBRuJo6S4hCD_ryM4CvWdpY7LBWrILk1GftbYKiZApkvbCd-kHSSOq2iSfZ2nUhMJ42756CHCTNH4Fxg671voMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxQrU92Jo8hLVwLS9G1lqqo2jHM2G-SheBPpUUWAcjWsREB04ONy3BED8b3T88P-t9kcTWJk-K-_ABfL7TU9KwaxLIQ1vIlD8kjoMzIoHfOnrv8iUMXwZ_2A9_3g-O6RsuB2J-ISsnRNyvU_pBpK9-1y387cjXYt8AEIrhxvzRg_3BZTsxhSPKI956zdYPMg_VikzhyFdu3UT88WZs8hXv7MOstRORVJGrLjx1a8AxVi-HBRcuJ3KjUtYYqoygZY7opyINgfq8WedFRTnqExZKmnmIqhbBe5whZEq5nNxQ6Rs2UR1rXARNCFXe5Su7vE8PmHksQBN9sK8TDeMEOBFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VMab2kHmO_14EAjecSjSUPD5z9vD7ZaKEKz6nfd1tAAh-2UgqRKrSYbi5FxDH2JQGzspjPen8xdYV0MQb-dGlfpsH28FObaDPD5v8qK6pUmEKUzI5aDfOdexKgFP1XUyEpHDE5yAVU7kWnrJoCoY4xF6Z-Qe3spwS1Wra9-eaGWbVq49EnRV_0uIMCEZw-Jvzzk2hTfvOboYAfMWfxZ2nZ7znuvj4tohxS-yJhjI5dFfLWuSleDl99AbM3xBlRu7REhOrkHjF2Eios0BWpFZukzlgel8vwrD2jzLoKOFgmlhmCZ9AgtvQgz1OkTO7HjKgBBjvc9_zBcOM0RIgspgJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtZCjl3Mc7Q8pqm6MU7ys5cSYKpvFvBJk5vz51gEpznjThp91mVkM05yuf_x0zArZPplr-jnEDy0k5EhJNQrozzFY1PaF3nUkhHLlsBVkAPijp6CMbzY9ki1-AYXc2hCpbrDrR5jSHX5P4P_2a5Y-OtWgeQIgLVmt38PLqtnXOv28Z5jpbTjbNiwMyNjmXdZxYPHu_9FXXQPJFf9_lXExYmOGOUuhyEMNPj375p881KiAO51pwGgxTQXSWmCijg4YCqEphkJj7l1lv901CfSW827eHV7pIP5TtF8TwpcCec8P7VwXYgu8xkvi3Q12DJe2X8lJ1-I4PvhA-B5NscKtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QX0Yq9AiHCEJ8DltJjdUqPmcOPg7R8GxoBwvXGZvkkySQx8Falboxc1gp0kVHG1yOBJ1EzS48dFE5ek3Pq-OirCg-f7bw9UXSg6y2W4lquxTvSpuU3p-FvMzo1l4HDnz3o3Mkky45ouX1d9zYufncwn8NQLhDW4SOfmeZNFpTLVN5fMGryKZDjs7i3cBHZZJEv_ZBc9pFbNE5iurZ7KPrnpTEgMrTXbdJYgszIZosGQ7KwEvNWWWuhAQTEbru1ugzFkrtdoJH5tuHw5ZSnLpp5YZ3k7kDucgtXZHRt17ZMmoIpyrj_EzLasVUSkHcWO3P5-AoO3OuaE6mFwimhKv_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ByX35vWvIZog-Vri9G6bhp0dzUILVtUYz3D65v63XyZ71PUmIkNxP6yRRUmietwUzkifkpzr9Bvofj9W6A3Qq9jUjjuqAZFZDeZe9i3-8ZzxZLgCBFPpRzNXCl0lsTVDvN4E25B6VuSMx6Ae43FHSPqK4rCney2MsVDIdMoVCmGM4GQvEuUcsddg7HVF5s0R7neN8mlN2DYT-0kOLUfwTmWNaCigIuk7uQuenaojRUyT7hf-lEK0WqXjnb1iQa93hKTp1XYBjJSqITmkGN_ZByVoJAujWF22PDJUl9jb3NfpglP-2NAnyai3gB2fMSoIa7WHd8rmt6vpRYRlO0eP5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsb14ZW8wwcfuw1Vj7VqrrC90EcgbixAaNoghDJCKOMyJTKZPT5UBO6im9ddZ-fMmw33Wcy4ZQpe4d_ZYgxMYKT7VSe40wXSjxjzby-kT47TpC_H1NI2tNdKNi6WQC4S-Vf6mNJFPuY7CzK8ej55TlR8FHzjt1t4IjR_nMk6FkutsPXOUWSdbAASrYJadbVdoLCUkesyRzG81gA23uIbWkS2SrWcFbltkYl2in7SZFdnnYmOicFbVkMUkdh7EiHmVNbBuEmBm2gzmJRp0UR5UnygLLi8mlwMfhpF0t-dhL1z9g5wON4_XOYjLFnyDLg1mcZW16MNQ-JIccPmNuSxvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYVo6BCJ-orjlvVo_1flJPscS3lEteo8wSUI6ELwjH11Olvt-uBd_RNdWN02oor1rkO008nJTiyf3HF4Qsoz-swzzieoosMCyLwBV2gupIt0sv3j4xA_HTWLw3juHM12F2O5JHLn-5jfCBf1ncztpURgmOdpYDvyXhGWX56SAPheF7cEkcdTWuy8VK3x39kOEG6YNyrvCazFHHMa_82zSaDPSKZspGAsCuw8A_yaZMyxhspjSQsMZ4zQOUhm81MnBaVful9ZqC7dX9QHgIldfjbHf8NhkCE_VJXeSxQDiV_M5sc7onyb4926XYQwasBqz1uPVwE6rFoiWeZyws41oA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Jp1CrnyoyNhspUgxebppYeXJTyVG-37feYySaOSJwPu9hN5UmaLQf5EBYNBIMzToI1J0OhkPiQ7IhgmF2YnzfTi-DvvNZcHNqHXcB_sLK9yEjkbONtWbB6z0nF4m-weMDGPm_nW-_HZl6MXUP4ys90dptYUTUp-dvL6cP3edkctX9aFWY80Nto3KYZyZ84IQ-QCx54Q4p6WGErVkT4utQ8B3UyxOl3ZQh5Anf1pPjAtbVquBP9WkyIpDJY9_I_vk5rC_knVpNRFZM9Wh1gb7KSmXJcEqEJYUdocWJjFk7KbuRgBUkYQL1jQqpEmvuB1tO4wc0gyPVuX3UdJEkPrd3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Jp1CrnyoyNhspUgxebppYeXJTyVG-37feYySaOSJwPu9hN5UmaLQf5EBYNBIMzToI1J0OhkPiQ7IhgmF2YnzfTi-DvvNZcHNqHXcB_sLK9yEjkbONtWbB6z0nF4m-weMDGPm_nW-_HZl6MXUP4ys90dptYUTUp-dvL6cP3edkctX9aFWY80Nto3KYZyZ84IQ-QCx54Q4p6WGErVkT4utQ8B3UyxOl3ZQh5Anf1pPjAtbVquBP9WkyIpDJY9_I_vk5rC_knVpNRFZM9Wh1gb7KSmXJcEqEJYUdocWJjFk7KbuRgBUkYQL1jQqpEmvuB1tO4wc0gyPVuX3UdJEkPrd3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCbmF45edko086sak6wqHm3s7kWMdHmxG-cDksjW5cVc_tCtS4bgfB0HOriu3AE5Ji3I3bEZJjuw1Ztb4pQoko9WnvtPwxCIbKueAf9NXVeZQVjyUZbIIEAEhZunLymEZ26lTB7TMA-LkbR85Wd6lhuHTrmqkHk123meFZYx3EgLtrA0K2ePzaAtGIxZFdohpq_oxZUu8C6DL8rIa4ba_jjfQkvUNVN2PGGsUkV0UytfFrzQuUBl9aGDYqR5a-WNzf1GFRy71bgnNfg653m123JzMqaaRTVNJAvMadi0QV6SVk8DLMyrO7GRcVA_0bZhNNYlS99qWmRv1ha51PFo1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CGIs9pzB6vO5CFvLXkzFJQG-lNt-ulmynVeInEKbGf8-mWAL4lBSQEW57vPkTXNG-UR7_H34VyrOOF-cYeqUA0RxdBiRxEjuydhrJbMyy8_FUVUDdcP_TDwJZWi5v_ZYzrtWPRktJyivrrcRvNnxf_0CJUKZwbFMA33rVbPmyp4AdB2rfCsSbsRdO0K2XFiCKhkEhjSr6wzGIUXws3JfRjhjC16oNrFSlTTBd_Snia9bgNu1GPrPvftvDpuNgyA36K0NTilgnDZfy5XJOKzYX0JRX8Q0qQb608ruEHL7zsTvGOyb6RZAaIndJieNNMEHNZg9VzvZDbdL144gfBk3dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YmvmdLGx8rYBi-9vOJlWJfvtOw0SBO8l-JKchBF-vxxTy5hJS3fgfmTDUzUw6ApHh4ZA2jya1ES8vLCGczAGhgvarRd-P4vxKyPYxJTSnjdtXD3UYtzPsYueLnLCGkW6z6LyTfPed9VHMI_vIgdC1a4pYXOzHZqiHg9_uSvAsQ5ETyOlQRq_LorSu1Qnkd5Z5y-P-nfag_kENl3aBb9TyrRkXSjfSi3tkiBE3wlThurnso4kWtmgk-VraJsHd9kA1Xu4sNwaE_G28sOqkc6FHFVx4o7S5ND6v9YCjAMz3XfOEOhYtCD0GYNPL9rkR4ho2hwwGzbP_RwjdupVYONIuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MAHcGk01_7G5z6nN2x-UPPcGFdmU650vNf0dghY1qO6AUuxa4PQCuptMY9sERBjPHKSC1Y4JTOvx3ihXSlwFx1-4aYc7luV-t0QeZAWURvLFlpeFG34mEBP7R1Hx5vqXeWJ3tBwRPzTdRb4QJcA-sUmM1n1RLIZxM2WfMXvqCrBAAkShkKxdVSB0x0KzNCG6YWWIVsxzOusqxwfQIySMsKIPjxE_p9Wrji1HS6ZJt2qCJS9k2xMbXPEo4r3hfkiXegvpGry4JJKvIsNsnAw4y1twQZWyMYjchOy5zyZ9Zcm5MhEcBzOb4a6A1h6XiKlCQV6PhDyvoXL29OPqQV_sAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eF1XyBLmqVODjxl2-vnEJTTN7JCXTe11snCWhvYeDyt0w9uA0rRydM35sQT9n_pDIB4IYAGKzMwpSIdbGAxjjqIDvj98ajz_w_taGjPh0a7GktcQ0Lrciah-xNmb087wLsYd_kAKjbfxS0hJk9g2hcHBbBYlJXQ-5vW-cgrqsvNl1selYMabUKJ7ZlndjrLfvFMyL5_QdWRSSbqZ9g1onm4OK5lmWbF7rS96nwZtvy3usL5NlY6xhBLlcrB737PoTpYfAPggCLbgI9UE4Njw5FSPHPfr0h32TgHEwDLIBlHanaBgoglEtIlscW5wfLjQwAQsQhTPcCywXJiH4kDYeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q0THqBFfgGRFi2paASG5ANAEI7-7WcG0jo9evDMxM2HXXfaUc3Dbhrq3ZrsQNoT2BrdNO7OuOJ2UlQLc0WgJZ8P9vMiYtyZLQN70tWdMjT0CpDP8bEkmJtKl3GeaMvYZkSJXJLYsldMsm1dlnTwa7XQ-7-pxG7K8cYZLI-ja_My5D_7gXXNjpSLGUMTw3cu4ZVH9yoL0eXgOawFTdm2oc37TToGV2ODCKvR1E756aqowqFRUKfMWjp7Eu85G9giS8oivwpugcp_nhF6jyeX1VPNYDdxrAAOtF9jhGCW01q5XA56BYsOmP7YG8I0a0wmXIg-isUG4Gs6qilwzHYfFng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eGkp8hoJ5DOCRJVpt-KOkXc0vMwq4Zxs2YZ-hV7fucb4p4HxWO_F5Y5jGJiYzFBPy2kDQtuYIFqJYuQgcgH5_-TrAD-1RCuPbugTpwcAkv4J2XTGr35wW-UAK9jtFRvtUDpftnAp9VIfO7e765EN1QTid_2oEguB0C4AyODRYTAo9IUiolVvhDwp0zsQOkd8K0nr96AmP5yujHmoWYJr77_EhjaaisYN0-PzdKeVH8TzYrVKWW4JFq2sazMKN5e5qpmLoKW-BdI_P6ZoSdxlZFfb05VJ0wpPhHrCKOeO3tqJ5o_0hdZKpDg8VV1m4rzEJkNvQ2Yw90CvzC6Ye4TcOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D89qtChhq9oRAKXu4GghxBgq4qpYMf7Xg8lBZk1Qvky_8yJFP2ODvWpLGRhtc5SNrIUFbVrzHKdCCmbs5VcrgSmSE2OnDriBYUPVpk6RWO1h_Pkp0dAahcR2uxzY4GG1EppYan99JNp2xVqQI2tfltf1JXFjsZ9JLPnWCSczKQ-E5tZp7ORqYISObL4MBZCnt-4bdzOElibkaekTBa1ROdPaa2xEAUV6kZBqkYfMcMZO71w7eOVv9x8VpsdRytq2n4ijoM4bXn_tNLo4rdGPGktMOwPuUhL7IZRHG7jyaUSO2zCE_VAMRHknjZsOO1cjoc2pgi_uJe5wXDcedy3ySg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KOt5mp6b_v_hkGl2uoGjPH0hTG3LV7-lKXO1zTjCBAYBiR4HzUqG9STQuUWiyS-jVtzM2pAjIBb7DPY6uT8ifordmZ2w5QqqAsKc6r4XaaOu02cLUT8KgRC6FZ7fvLTtSOpegb_bjmAHpfP94y-h8MSYn32PXCWM-Nqcmazq2BX2zQeMmGQVPKWCQlc_wi4RNI-gdg13R3qTfQay1T0gzuYPegSree_f3XdlCXwUu9bt0Ciwfr4YUpV59TZM89inWe-J-7wr5UKVknuCp0JJicIoiLFny0jIMfispFIswSwWMJpiN-RmmkVjb6pHlIuZaJxe6HBh00yEiPQDMjLjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
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
