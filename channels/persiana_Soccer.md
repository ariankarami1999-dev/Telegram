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
<img src="https://cdn4.telesco.pe/file/UI0X5Yxl5g0V2r4tyAeZv0dMGyOQImQoX8cYT7UR194V0O2ZiUVKg7ixroeFif8M-Fp_01rGSADsqra9IP2Tnt9B06hnozvhDvSxWJx43dUbOp2ZEjbaJ-NQNbpIEVxv_FKGvHJcOWP01P5SPRSLfhiil8BxnadcGruic_JI-gnPXu9XaGG5jhfBLnO8PSc0Zw4A1_LqrHXemIV7AthWqDZn13XWn83yMLW0eoUhRoqrsVU1E0rrL9MYu5HRK4ZIY6ITb9QwekOyi5AVQNkyXdheehflvXBhWn6y0F4B4sCDGV7HjpgKMnGACP2f20FQzZVaD-j-5EIqZe2E5SIm1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 452K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUvZjPdou-NHY2M6mERuX7HKctX5PNSPQqCRbRutqTeG8Eaq0q0BtiWFDyJpMce9Oi7GVjCgRGRDoH3ZY5dz6UEzc86qNx4r_o4AXVyv_c2n1KMs3d4B8Olk_u36aahjJe8GOKbcInPoORJE_J8EJiB4VFcLaDTeatkFxgjEAJtuk-8Xn_p67bvCMPSEhBEVmyBj4r_HTClO_8_HWdARhDjnoOP0bjVFDHJIwwq749HwIKAMwkTQK5GA7Q9AHkkKCR7YY0aaRRLTLfuUVs4LWpN1oaAmWP6WANTZ2yxz9upGWhDTHt3TEyXASBTu2xQsVBfVbE7Tf4cVuj3gpVkggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVkXu_MDYaXN850sbnNZCW0ze8tb25A79STEQM8diplbZdKH9zaMACSzWJVWcZ9OqPEvK11b1y2O8pArsKStIsGOvJ-nwxdUaF0kUjZT7O8lBUOapkyvM_Rxf6Oh7_06rzU5vs815YeD2TLaB1vnkgdrVhSCkg5D-xvWTAbO0YivGmJgnHqcQ-zyFNqyxdyRoi9IMD-sGuyI-ZTRjsZ4-vyE2bU1drxfiZ5CEd6WUo-7FXsB3Xgcljwke4BycpjJxG2tVd75K1QNn1MUSx-BiR9MTzaN_HLIwM795Sk6basHEhPhjffPAnAWj7PI-TnKzN4B8z53qEqi4DdI1gxsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzIwGA_ULP_Vtrli3b4eYy2j-V2Bcw8AwAp7u27yDYzaVRDV9rfWZXH4_CuK4Iy1nqNLO3mkKJTI8zwQvL5zA5SE9c8X90HRpnmOxKbs5AK604OS7v1WHUPzBhN0z1M7XIdMK0fmvZtnwKb0OqTDgiKczUnaQAHnh8xS2nyDm_bj0iUVLfDB1XGQBuaYDDGugii7C-mqqSXczaN5tu4TcDLk-1pddVk4OMhX9GgJe5VuencFEEEmcIz8Kw1oic2S0ap4dF-HYD16Fme_OyBxu3jE-eK2Q8OvS3zPyvQXkXi0f94zYMu1gBJ2aaeauE4Sc-SItZgiM8KeeCKRkGyjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30977">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPwdEptZRWa9oGTgr8KyPMIB3xsZzJuGxiCASxfgTXwZ4sL1ITpvupCbtdqWjNuxfcbh3VeOH0kMtuDZN3gQXbs_rhaAZq30iOTW0kCTgR_x5vIR7cbZfokFx19NgHMxGljDQXwo6KSmk1rrbB1RbLKPU4maeUxUly-XmlymfBCD7uv1LZIj1S58Gp69dZ3zvbKkkk9OZpLRugrnH5ijT82IyQhYI1H6q8TPtnglKgWs8mMQDjaAOEduDwQEftWMF5Y4QU0rIKrk76uk2ibdMH3KGyE8Qjqua89BvHqTEUmAornNY-SWRFfvqOvbAlYezr-14Q-KlqX2ue2kylRpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/30977" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30976">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/30976" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30975">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emlbymOifkxGGwZsFkAYHT8v4lOv7uJGL3WN--92jCgovc0in0uURwMeNGLVvhA87ECDx5rVsmuKyzgtFn2APeFIZPUkaLsLeXfE-NvUXy82QeGjOMtpg9aSESzlUVvxvMYL3ANrsPyiDzAywI1W0dn3S5Lh5Sp1gTKe48MZayzTNzW87fDfp5TTHMhh4rIpDYeeJzIr0w4_HcMuuv6zlaj4ISC1K4bT6fUdCaNRcLJIbev7oFuq70TdkzqnrahGgXMQ9kQQX9HPfiMdueaOxhYKehXRkamRUhboOKAtcVbxEbPgpcI1uaVbF7z-x0XsGunVP04AHZTcO9GnNass0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی بازی‌های آسیایی 2026 ناگویا؛ چین با اقتدار در این مسابقات اول شد. ایران هم ششم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/30975" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30974">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoxELDH_VIk93iVeJ8evw4JRtCVOz-73cvbGDBPGOyp47TZ69G1DKFXoY-odzAdjagx33tXQSNWIoj-ZwfZ2A4DzFHJH3at5s08UQquH4ei2kByI8CjBzuBM0YParo-luHJezgh6r2Ck8Qb2GT1nl1pfNIrVCVwtDxT1wsSvGa5wgTPjLQEPCq5GwHV9mWNw0fFok5Vxq5QW8ZDuLd5zTsltEwalK_3IC1ndgPHJsD1FgDrXfw7tvA3zKCSG0OFH2M1PxGe08P-Q9orMQ7fQP42dwsjHnfXYjnmzJQFSFX5TXyUFm1eWzayD__TymzXv_0HtWQEfbc1kZW0UIlhYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/30974" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30973">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbLf_YLL6KOa6vl643QDunlRkmOq8VZ6vFyd-WXxVGCJIPdafNWl1Fzj1afJDYh1zCaLNvESRqzhPWhyaex8ZollA7Z9kJ-hbiQ6VI4WWRp2VgNxruSHTeVBEreGzJ5fxkPSoLHX4owZ7UneffMhKS52lX_y1Q0ubVyCiS5DfhQVgtv3FRG04Jxq23dxeIvCcsPu8ngaFQqCTDKhHJarUywhcGaTN0G2WHTQQ2ubkWxFerlYgyO1tf82ARelBAaOaAte0YJX4ZhIRMqUeRhYyrHQL4uLlU23c1SV-ZYs-DpqNaYCl93umwbc_BtLmPtB_-Ta90LN58O-MTi5xMhf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/30973" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30972">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/30972" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30971">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5TZfAfYyPaJoH310A90FsWoSEdAxGXZ9ICuLEY_byDjHZ7fv3DIz3T7h9GD3px4fR_W6Xy4vNfWAXK6-mU4HUcrnquYZMIBPE-1TX9JyRikKAU9LYv9M4BEYBc03xO7C0dwU9lExQqtQecw7hiaZLLMCHc9Vfnd0nvX-JTkZG0anY39rK8kXdhot8_JG1uKNBpCqzwdzMb_ngGi6L7Zb3vhvATNAfvd_vWQpwiecLbqnw9LMjw9scciJBauWQ43xPz8ZOU0irxM2e6WPP5sRGeZxbsCLxDmsLWGcTqx3RNFh6ojNNjPLweCdqHq83bRzAnLsvAkMKmZnOfZC966xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از شکست شب گذشته دهوک در لیگ عراق؛ مدیریت این باشگاه عراقی تصمیم نهایی خود را برای قطع همکاری با یحیی‌گلمحمدی گرفته اند و نهایتا یک بازی دیگر به او فرصت خواهند داد. یحیی رو بزودی در لیگ برتر و یک باشگاه بزرگ خواهیم دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30971" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30970">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCc8QQRLCrigZSVay1lXY4aCWUTsAIV29ereUaCkzSSQqJyW1_Pyjxdg61YWHd_6nievCUiUnCf81Q-BLknmZwBA5tuuZLypeIcTWKR8mTTdIfoe_fNquUNb3GzVvVssUyyjIeELA_ZGoqo9pgW4CP8HIpBJdB9dY3zP7jAS8o4kclAlug0HkO1uOX5G4ScYtgY07EfFUZdzVHh0gFvp1NBw4wjZjeZFI_DnEAchJth-hgIRg-mikjhDEWndUssnxlnewdl-MemIOfTynII4KGJNx9vPvgY9khMcmyyHElIElGe3yogNIZUHTBbL-MonbdgcVibSLq-weyL-fyHfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارتینلی ستاره الهلال در مراسمی که اخیرا برای پزشکان در عربستان گرفته شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/30970" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30969">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzjlcKsOH6YP_2DgMbo6Z4IIU5xfRuFnyPR817xMdnhnXk_-8HctycfM3eigMyQIXzZyCYt8svJd3yKZexbpDcFwbtzkaWCYB6mNbIyeblUITMiftQCPuRs-We77XI_mYb6I1MTKaf_XpGhBwKklf-vE8DViqGUksq1vy3ynXIK5E3cjPAWxjq_HAM4BjXIcAxTRIwxgtjgcYZqyg_WGhXShKSAZpMOf4taamnfY8vodjAjL-JHNcsxIuY5AP5T4fsVo0bw3QksfOJNazhFk_B58JLA1BxaYsg5OyrRRl-Zur_kWqfKSPE1evN1R4TPTAqZ0L9GkTARO6TbDDHixOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30969" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30968">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2-A3IqbP55_Dt6Mvqok_nGCf-1UWNA12qI3lVmQQLTioft8vhAVnsbLpttmj-1uyIpkWYts-HQABQl8RsDiguyF2dl-keRY2hV52Ih7emTAo45zZtKFEFJyIxHd6a2ji5XY-wdiierqTGdOQWxbDEXG6gMsTvdiIIbBsHQdBu2sPVS8g6EdP5zFFOS57NCQgIT9DlZ-uJzX3IGLon4xI9SOVz1-6pSw5Uwprppu5GcSdeO-lmgxTOtG71NzLq53v-Lm5GL--NJr_nDhfCd-bLMqhu4mPnuVVyHi81qMRGndzx2Hi53geL2vNNLzEwfv9x1yGW9COwO5fx3s3sxaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/30968" target="_blank">📅 16:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30967">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEc3JTNEYD_gFuIYOHUSiykplnl4etDNxzrXG4f1rFZqLqFm0Ta8FuVgWFOS_mL6s7jEALuwl92YD7r05jgn0Kc-CsMToNvk3nvU_RKjyamlWpbLqH3-QyZitgKdG5PUSzowB5LbPB5K8eX_ZOB9XjQpgxiIiiVEW3udeExrKX3nTmMxLknHqviQnHi1YvU84t6rFtug_Ikhk-QfrSMh6sSYdfee0CTlRumZqCaqtm62XngCUgoCIF0lZFPKR8xw_lFjbvsQUtX7VQis4Fx3bQpcXc1pA3641uScbnGU-1z1YDFqrcbaBdCveGIUI5FIaeVEJwTT8ydYgMYLPP4XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فدراسیون‌پرتغال‌میخواد این هفته یک جلسه با کریس رونالدو و خورخه ژسوس برگزار کنه و مانع‌خدافظی کریس رونالدو از تیم‌ملی بشه. البته خیلی بعیده رونالدو در جلسه حضور پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30967" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhvTiJloofmffmyFgzsRLrhSFia2QoOaSW3NLWeL2UvTaK57e56ic_VsKAxowcAOPsLrHNLxYbfw6QzoeLJie6xUjNu7weR6xnrJlBhYJPgP-TMTNBkX4cdqb9FYLXCNuAIHAmte5_GcT-P_ljglLkDOQqvB7cjOGBib3TWkV56yp0jvEYeFn0aVf0z9Xv08eFSBC6LIwrHw4qbFI0den7Brv_ooZbR2T6bLuGfeHlcLZzb4yLWGmn7lWqyQSOImJT_NoZLm_3s2OtGsl9F58LkGEIrdyezDRqsZu2yo9hFn2nPOieoxPRB50_l0miBvZcVZFWTrrAv8dBpMdxaTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od1EpY_KrzUNeIa7fGvSWiPh3De0CkkR-WxW_Z-VFOP_FV89fCPZXZQQIAO0Q1QHLQ46pys-G1f_uZ__46MJNeoW4nfC_DPhITkaqbcxnCSsqnfDrmUyPYFTb5hTyuzR3TrlZOvN-CGudaAJ4F_rNBZp0R2ZnThcsQzSKug-R_IRxTBLMh5u2njkDXHMG9vmeAhJRHN_z22ZQ7XqZgI8ix7TI0BNB8HIbzY4u4UXnSWDRWYXZAxSFQB5IXu0OdYx0Y0EEK-PFldmZdhljGd6-D-RlL-VChlz_PlcqBcegz8XB2kxyU11AEvCc2NTU1mMN-2s53f4gRifzYUdqgikWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd2YYELGlxakoqYjLrqZ5RJzjCuFVNXvTLtlCldhm4sEGXSP7dthg9NLIDn2CrnJIZua3bdzP8fzzRwtLkdHv818aYWH9DaVXYrE1sjYrYZ-zJwRM1U_kagRk1J3G4clHCj4cCu1KAT2tuVcAyq6OlvhKfKVjhaHnl3t6ginOoB4jnhCy9smrNsDZxCPEQe41xBBroGd6G5dhckhwbNIpdcmtODl7NCXS-dcb3PVdP44i5ipTvV9Oqdr6avCF0CJVsBc5rHNh41UWFaYiPjgFW-AdmuIDWuFvQ8C_Nw2ItL2dLBC03kzsLBha1ywSQNUD0UyZ2YMNFouwWcKYHyF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGvFDI2VYSXr5Q2CNNk6RnpDZBGpKO_Wwxk6JYCLsMefwk3C9kWkmWp1YN-zy1L6wT71-Jtole6SOx0P9j2TaWu65b3KfiQb019MfrFFh6WtpCI5iFu-FKChUyqpjx_JHKls6afwlAyOlFTTxYazvAW_2jHrJ2sy5cSd7w8_6778pzSR5O5oWZmZsiHTI3prCnpDr3dGMP6orHRSXQVb1LIXdvrxq8ybXzc5LD4a3HRDTjCpY-13opigqT5C9q7dpTXDykkM_m-DmZh7xxZwA-xX2S0Acd4phKXjiKKL7peIbWIwJRzVGc7eIAzK921Yr_jTb5yVK1_YE-3GcrUQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=b0Zu3oD-TmomycWgINOWqdTNfIEL_200OM-CUJniWNztyirR191i8BdlqiMuT974fYtP412bC4NSfrTHjuW4xPHuG1acddg-h76db-mzLCKZbXQQqR4IAwxkZ2jlHBJ4wjZXgtR2aQTPM-nVLiN1QGEDl45GR2Dp62tdw38epMdPSNmFTiEbrewXv8BKpjJrOmIThSOBYgn89N1mBvPRz30D1SIFmWNBBqBgFvv6ijo29_IVWmkbXZOZZpuQ3ZCnkR7-JYrhSx1CFJ3EC4UG11YKdcvQHR08mO1jfBqYn-3e_2pgBSgCwj1tA8AbSBUc5s-2EdII6smdSVRyhBs8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=b0Zu3oD-TmomycWgINOWqdTNfIEL_200OM-CUJniWNztyirR191i8BdlqiMuT974fYtP412bC4NSfrTHjuW4xPHuG1acddg-h76db-mzLCKZbXQQqR4IAwxkZ2jlHBJ4wjZXgtR2aQTPM-nVLiN1QGEDl45GR2Dp62tdw38epMdPSNmFTiEbrewXv8BKpjJrOmIThSOBYgn89N1mBvPRz30D1SIFmWNBBqBgFvv6ijo29_IVWmkbXZOZZpuQ3ZCnkR7-JYrhSx1CFJ3EC4UG11YKdcvQHR08mO1jfBqYn-3e_2pgBSgCwj1tA8AbSBUc5s-2EdII6smdSVRyhBs8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk2XE4QsVR1YhU5_2MJO2QtFcEHZSzJWvZIWvvdnwzzCIbg8rTyKRE6pHTZ0dv8mhlbaLWJIUNljzHs19Ml6ITmpluODY3g3s5-TmUzYVI5EX9nqkfDsXxdVpL9ViZ9ac_SzQjjnfDhedaTtuo1rPZqzrT8awbYthBXwQ5SHc9D-QbEvO1rqCFhsdEtOX6cAsgKjn8GjjlLVU5bbD9CzTQMMD8IQ-XmTjDmRRJuRd3iTI65OXosBJ5e0CScc74ufCyfZdxwZPJ_4x1vaTaixaVReJrYILNS4ZRtxM5h2-qG-POluE4gC72ljEbsdKGvQYLNj91KBqBp45pqOLfb4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H71YdjnxQ4Ng2CJEZE5vt6brg0BG8sCqamqhITYGs6sut1Bi8XTvCk_CAtUX8fEi_g7ZjOUPjddP1gTagsseMjG9JYThh0xqqJJfvQVJz4n0_CY6okKc20t4_qHiD6Tvjll8lh6pOdQKU6Ye1QHskBcrZe5w2odlTzTr0zUngCl1K-tp4PiqKPPJv2qg1SDDByOW1iial2p8F0M7WyuofkprbMJDAwKw8yHxXL0-fsaMeKhaDfMtn2VrgEB1wLJDDpN5sMobc2MzXb4d2Ghu4B_bCk38MO-aGmhuQji9zhiE4qIt6h9gkRqEMw4f_gNyKTMWH8CK4TXAZQjzLDhQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqBMiG-y1H07Io1NOETYFo-bMRaX1bq7S9HwrTcBr95zqJb7sadi6X11S12vk6cAZxhtFlO6RhAjHj87_cnUcBySG7mBtGaijYQdTOcQvMPvyI202oVcKyLe_XeGPIGz9QN7h_yZL_qh-exl9ZKbLAJPRb6mx7X28TWQWOWdhPlegkDEB5T25c__upAvFK3V-TtQsWjvnLprKHYtQqIKjSTNtW4C5YXRVK0arOAM8NIL1Xu99Cw9aQlpyjGl7TINghdZoaWnSSizbyNMaxQahS6mhj5gapw-y20hjlXBS_Js9xiK6UAkFZmZsSuZgB_45Syafudi7Ty3bxQiYFPTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30958" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=GeZqXVl6pE665L-WYV9iK6av4eTF5nVmxcN0t_WQkysB-bp154Amo8kiUcb4D74ZEqQyEw4gXlzZQF8GatLbPW4CegrjxcGY4JcYupxuabMtGmQuuif5Pg24zZ0hJsrrwijoBSaiZbSu0023eVVdvmGIFQxqmTiQi7m7-tXOpcCD8xySJgI4u-ADvcM6rDw9N2L6M23GlYzF6Z2utmqmH204ZufHY5CICPBf-3t4S92z-4sd-DmYQwDMcDis5h4mHvzly_Uzv6T_Wmd8Q6PctzM2jQQGJWT5JqSYyo1A0uI4c6vEdbnC4SwS1TvDoxFxJ6PGDvdXGGFiE_jGFsCv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=GeZqXVl6pE665L-WYV9iK6av4eTF5nVmxcN0t_WQkysB-bp154Amo8kiUcb4D74ZEqQyEw4gXlzZQF8GatLbPW4CegrjxcGY4JcYupxuabMtGmQuuif5Pg24zZ0hJsrrwijoBSaiZbSu0023eVVdvmGIFQxqmTiQi7m7-tXOpcCD8xySJgI4u-ADvcM6rDw9N2L6M23GlYzF6Z2utmqmH204ZufHY5CICPBf-3t4S92z-4sd-DmYQwDMcDis5h4mHvzly_Uzv6T_Wmd8Q6PctzM2jQQGJWT5JqSYyo1A0uI4c6vEdbnC4SwS1TvDoxFxJ6PGDvdXGGFiE_jGFsCv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
زیباجوی عزیزمون با این وضعیت بازی مقابل تیم‌قدرتمندهندهفتگی‌حدود180 میلیارد تومن درآمد داره. انگار وینیسیوس واقعی رو کشتن تموم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30957" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzuy1udhuRpTfmQ3vxs3Wh8MqMOOc8hHDRjzDc6goQjp2xuJBQr4QbRuwhrXqW24687GEicGgsJDA1bIotK_UFdK5LMCE8V8ysUX0Uu4V8QbyGzbizmH7oSwdVstzCCr8UkMZZRNo3oCrm5aZH4bgUIjby_cqXu4oAyHthD6HdyIi0VroOgQt36XXm9aybgdl1c2Q749fvluMnEh26OCoKUUEiHn_10SzeroPp2Vkz94TXuCVeqW9y8yWpi77wi-VqebUW0GCPkjC5qkRnkqT5g2AHVOQgaNH58FQWY1KVhYY_VFRYe70GJflusWcKxSLakxGw5Fp8j6BOSi6wKcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ در صورت موافقت امیر قلعه‌نویی تیم‌ ملی روز سه‌شنبه ۱۴ مهرماه در استادیوم یادگار تبریز به‌‌ مصاف تیم ملی گینه بیسائو میره و بدین‌ ترتیب مسابقه تراکتور و استقلال لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30956" target="_blank">📅 11:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwDPDCzdBhJWqJHKSgUBAb4gAW1TSSShdd33H5CHt4o1Ap1gLYNLzU4DfXqYp7xm0OmCbBL7lviepaWswoSRUq_P3D882cphasCJLLRgcpvB_4ptbKnVK90II-O7zNfVKYUgnsWmDmLmpZfhp6tCRyBJ460tqWBZKhJkbDWczOaGszBbffWUjNC5dhx1GDuhSUaVPMyPVjh-N5L_5yIKLjLbviycmxXo6mVWpiVO5sF91Lx42bzet0uELgvQhfO2Wj-5O4wlojGuTw-k6I_jvtBgaHJ82Gxc7oqsDqZsU2ND_aOZdkvf_yvyvzRNlvfO2Iqm781ZY9d8rdp_BgViCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30955" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30954">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56284423e.mp4?token=q8-EFLZ5FAZK0qCWuRbtvFWpkPLS0eG7n0g-nBXQxhBsFMvicYJ_7hycapQjJyI7LlU_x4J9lVO3Xz760IBA8ozSKJLIw2WPccStIH08I_n3Av9uwIG2KwRIAf_ebBNyFDEPU48jn7wQJaRjW8g5u9AChZEvmVK_7USDiHqhvrRikTTY1CzqXr-zpzfTRoGVyiDu_2sZZaW--rSRXrSmQ-WEZrUZ8ACG2Y2puuft1BAJ9PLxTfVfbRwtwQcz7OgAfLGhhoF3FE2TuMmk3TZatOTV35PCZM0-zACvGbi2CbIHg6_Ye9xZCmSBhnoYiN-A-Z6tfuyZN_bBBlF3znVXujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56284423e.mp4?token=q8-EFLZ5FAZK0qCWuRbtvFWpkPLS0eG7n0g-nBXQxhBsFMvicYJ_7hycapQjJyI7LlU_x4J9lVO3Xz760IBA8ozSKJLIw2WPccStIH08I_n3Av9uwIG2KwRIAf_ebBNyFDEPU48jn7wQJaRjW8g5u9AChZEvmVK_7USDiHqhvrRikTTY1CzqXr-zpzfTRoGVyiDu_2sZZaW--rSRXrSmQ-WEZrUZ8ACG2Y2puuft1BAJ9PLxTfVfbRwtwQcz7OgAfLGhhoF3FE2TuMmk3TZatOTV35PCZM0-zACvGbi2CbIHg6_Ye9xZCmSBhnoYiN-A-Z6tfuyZN_bBBlF3znVXujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از سوپرگل پشم ریزون ستاره‌های فوتبال درمستطیل سبز؛ گل‌هایی زده شد که هم‌تیمی هاشون هم برگاشون ریخت. عالی بود واقعا. از دستش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30954" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0ebH4-8WRTHrBLQqcvuzqfqP9JW2bPO1-zsG8ABWQgGTfcSqUQedWiTJ4xK7FSNfr20Cv6vx8VL3KhzBt2r40Z2hVquGWpxrk_w3DFQFL9O7TujA6MGLYDknRR2Ya7PwEVGvIs1WS0X9NvZLMTBbBbL44KraN82lDVLKhjlSXNOIEL7SzOOAj4Is7Ux9m7bXoK2caGYmuHuXfcEhtyfg1QV3VKgduJIx9qrMtA7ttDJKpEcE1xcpdpkl6TlV8UmwyST3vR-kOJ-JzxP6TWAqHDiIBrj_kJ_eboh3WF_SdwytL6nK35uRexR2PoXMf3J_yHg9b87L4lPyVpAlUSCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اگه دیشب داخل کانال بت ما بودی می‌فهمیدی چرا همه  دارن درباره‌ش حرف میزنن
😂
🔥
😃
تحلیل‌های جدید  امشب
سیف تر و آنالیز شده تر از دیشبه
😃
♨️
آرون تیپ=
وین
⚽️
✅
💵
😍
فقط یه کلیک فاصله با وین داری؛ بیا خودت ببین
👇
😃
JOIN
JOIN JOIN JOIN
😃
JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30953" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30952" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=YSyJwFi04IWn0hLxHriYlOpmOCYT3GChAlAr5k6ZNCGRoAZdxA3dUQtN7GQHQ22bwcb5L07PIcdfnZJuKEMsyQ8jH4EOYtEE8vbukmPwBB6DSqLNvLJtOH3neL3n4zvOdN-wnJlqatdQmbe4_KhLBHHLFfSdSy8bC80dn5CjCs_o_zw-MPmI_6E_MlbvhiaMC_cWnKJlVQ1ERkJU7KRciFomKElPs_pBdDlc1cpU_q_Qed2ND0Ly-0EKMdgXNzOtfsy2EDqrjwqne75eZQym1VS9MCyLXPka1gw8NyBrBj6bnB1zik1rAXXIJrgkOjW7c1joMbm-QqT2yDwg9FCpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=YSyJwFi04IWn0hLxHriYlOpmOCYT3GChAlAr5k6ZNCGRoAZdxA3dUQtN7GQHQ22bwcb5L07PIcdfnZJuKEMsyQ8jH4EOYtEE8vbukmPwBB6DSqLNvLJtOH3neL3n4zvOdN-wnJlqatdQmbe4_KhLBHHLFfSdSy8bC80dn5CjCs_o_zw-MPmI_6E_MlbvhiaMC_cWnKJlVQ1ERkJU7KRciFomKElPs_pBdDlc1cpU_q_Qed2ND0Ly-0EKMdgXNzOtfsy2EDqrjwqne75eZQym1VS9MCyLXPka1gw8NyBrBj6bnB1zik1rAXXIJrgkOjW7c1joMbm-QqT2yDwg9FCpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30951" target="_blank">📅 10:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WtElvNLSq67tFwwSKOhsRuhbo5drrAvhBr6-9Jnz6PD7iySADFPss37rxJAN02BaN61iidVOs34orri9_Bp_YFUU36OEAznIUYqdX0VqjgXI7BAvNgJBsbKAmkmdhWP_w7foSrj9VFxhBr09vzAIjetDsUhkO6VfCD0J6SpGCsBqCQTe8MsADhgDs9yg-R_G_A8eGKEAqdv1-r9GeF5_6RqRjQOZJH_P2Jvynykfb1cqa4xxm4LAHTlbu3wkEry9QaJLm7qYPR9k-sWAJDJDAdDH55yIlYtHV5ZYUBKrlL4CPBWkyRIxxAq7SCZoiqGIGu3YUbwI-kjLfh2hGUV9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WtElvNLSq67tFwwSKOhsRuhbo5drrAvhBr6-9Jnz6PD7iySADFPss37rxJAN02BaN61iidVOs34orri9_Bp_YFUU36OEAznIUYqdX0VqjgXI7BAvNgJBsbKAmkmdhWP_w7foSrj9VFxhBr09vzAIjetDsUhkO6VfCD0J6SpGCsBqCQTe8MsADhgDs9yg-R_G_A8eGKEAqdv1-r9GeF5_6RqRjQOZJH_P2Jvynykfb1cqa4xxm4LAHTlbu3wkEry9QaJLm7qYPR9k-sWAJDJDAdDH55yIlYtHV5ZYUBKrlL4CPBWkyRIxxAq7SCZoiqGIGu3YUbwI-kjLfh2hGUV9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون یارو مجری بیهوده یادتونه که چقدر راجب فیلم عروسی سعید کریمی بازیکن سابق ملوان گوه خوری میکرد؟! دم‌ از شرم و حیا میزد! حالا در نبرد دیروز تکواندو این الفاظ مثبت هیجده بکار برد!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30950" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx5APqBjiv-JUaz85K_tsprDrXwjZR4hxk3RD8TKVfDrPLN4rvo-mg0weTLa5DDRWAt3zVg_AfTzeUC--03-4eUUSKEnEeHrY78F7Igp0NgHZsc7zMXTCrl5Fi39Upr7PbHdd4zJ86iYMnwvBY_FUdSbey8NDhVUWZPPKjLTaqzl_kryRlmzX7UU616oYlMyprISI_xZbUcedh8Q9-6m6-hK_nWK5uaWFRS7rUTdYlUFSC5GsOxBmOjdNcazNBEldZlC7GT6nOxN8Ksvjbnrw9b8Hj7zPUNqia8iiagfqEPZD5oLSXhUyftL3oJRdrBbEzYcw2qPk68LCxInLVHoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای خبرنگار لیگ برتر: یه خانوم در کمیته اخلاق اعتراف کرده که با رابطه جنسی با چندین داور، برخی از نتایج فوتبال ایران رو تغییر داده!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30949" target="_blank">📅 09:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQlkr-gnZEvfn0bkO5vxum1ZmqJaiizrEc0MV5IVc91V5ZnnLrPnNCn5_8XLblUOQ3xwG9OMQa1FKhMIsjQxRoderw_Vo5yQTMVhhjNFLbIOnETptaQ49WNHkOLbtkq9LYQd_SEhz8beAmcod0fPaZIW0HwX0i1oFwc7k4GbbwCFiEzCibD98M0RUeq9sWHiW8mzFlFfiCVnSbgWIS_bNHT-nY3HCDsg0nEW46Vf2nqx5G_RJfZvB1ef_z1qUfFwlU9bUDAJb1niGWlcammghKBiICE2pQxBBLCMynCwIQCqYlXLa8Sa9DB0yaQykuV3mU5UjSbNP64xWOP0SOp6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30948" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30947">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htf2yc7rl3f__1bHhjM4jp7KUyqXak5fRC4KvqYUzU-ePYDlYcXsFar_7JS_aojD7pkFfAhAs6NMweXefF9XlMjJcX8cHlD8gIlVQI4Q0CdTKgeIZnpQaJ9d45E6d8vX0u9-BmNGqpPb5vOlIWBGMIoUuX6HU346GkxaNTY-MrFgUlOlnx1bzFH-tkF76RkiBDjLD3VlB0IzAj6R_tN3nrrElW2LMK-xxZDW6C1pkh5oeiY315MOe2SshfNbepMPHXEwTGhv9IwdOtOmCNtF_ESPfiutlT1YAOTCXx8__OcLhgUJXSQ99SfO1GDG6XQZ5G375Yyjzkgl-wmar9BeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه روز پانزدهم "پایانی" مسابقه تنها نماینده باقیمانده ایران در بازی‌های آسیایی 2026 ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30947" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdbSH_Livv1YaKqLu8kHetb9Ohx67Dapm3lsLYUN8i7KSyN2u6N7sNe6GLLnyD0251sqfwsyz277sGyXuLm8E6RHt8l3uI1yvERLMooSlSnztrAak-vbFqM3FD60vzIxHHD8DutvBQCOiRTDQN-qoPkMOEpgwUtZJaEJWZqBMixUJ_nYPs9693rFRE5_OJqnnuZgdFqWeOPMrCb7fIZTxdqI4SAQHSEfr7XyOdw14-0TZe29wcYB26Gp8VfPQc4TaqJsvswdk5wWy9NWGX5BGRRDOo41gtXUU09_36L3HzQwHcjZtTHVxlf8aM_bifVcIdzmENck9uCzsGKqoR0Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز
؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30945" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD8Z2f4Uouq0CI0Ki1YCsBiq9t4Rls9IksooxdGBZ5C7UXnimZgGF7VZZ7B7xaEUrtJwHMY_xkCswLjq5wJW3K0Bvo3J3YFPvi5fxKh8BzmpLtiY5327Qmh41FnJ14EuJb_xpvnAlOSfSvZq3y_Qu4xpsnOVm_O7lhcqu3CuX0UG8rzwixXF2F-P59d15x60Epd3GPK-UxWHKxG0WZLPQdAtQM553HSh4xV6qW3TzFSsQzq80EX3BRC4Kg4SwdRgJ6eN36T_BQm0vVHy1wNsdIEKt-sU2KFhRfA00Qo2sWkxBwzfCGOBkf5DYhXbeFsSlSswdjZkLZpvMxGaEoaIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
تحقیرکرواسی‌بدست یاران توخل و ادامه روند فوق‌العاده اسپانیا با دلافوئنته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30944" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=TWapO7IBtaLCTCz52MgDnwbChLRh5Y7b2ebryr3VVPF-QpYUiPYEJtuNiljtFqifG32Cnia0BvS-qwtx2-tFsZweSBkxaggmPP6ALfATT10xm-9zCvZO8mbEjY1Hpn_CxxL4TdwYF0rdB9dCz5QqhBNS5tBdRDh-X8DNCDtIE6dA9rcRWAI5QbV6AsZiY0hMBl0T57yh8rVZ7Z1Vooy9h9guVhUF5LtbVQxNaC53LRE4CiyouCCnnsw0BmmcGXkzaVITqsqAn1xZmTRR3U4Ctpo4kQyGDPbBMG56kfAN4wqy1gR1ft3PUs4PYoWJ6SAeO_p3DPvqsR7Y6LMlQRLpowlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=TWapO7IBtaLCTCz52MgDnwbChLRh5Y7b2ebryr3VVPF-QpYUiPYEJtuNiljtFqifG32Cnia0BvS-qwtx2-tFsZweSBkxaggmPP6ALfATT10xm-9zCvZO8mbEjY1Hpn_CxxL4TdwYF0rdB9dCz5QqhBNS5tBdRDh-X8DNCDtIE6dA9rcRWAI5QbV6AsZiY0hMBl0T57yh8rVZ7Z1Vooy9h9guVhUF5LtbVQxNaC53LRE4CiyouCCnnsw0BmmcGXkzaVITqsqAn1xZmTRR3U4Ctpo4kQyGDPbBMG56kfAN4wqy1gR1ft3PUs4PYoWJ6SAeO_p3DPvqsR7Y6LMlQRLpowlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG3r4EPMM_AwUoZ4mnkkKoxBB-p3c_en7jWZp9gYR2YgzcGQDsHPdX2ph9YbKa_Ss_93YQ7Dihpd-O0bRGGYLRsiBibEs2EfLuiW3ruVRjTdD0Zjp5oWgUYQH2vji-b506-sj7UanrIjTKT9wUJHFWYXJucyAYufrn-e15lb2XfqsPxAicKec3E4oDT22ylH3TVI-AsgXOtKyT5l_en0APavpSYg060J_UL4-o1mXGahn34L-3njxS2lTQcz-wa_YesQ-i2-ddJS-srq7qL6r1y-E3JpPM_WeI-2KEBX0db7qkzW_PGY4FkzTYK7F86_PmDXtDfTQTNUolVT64-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov5rhXuDa0L-HkqK5f6-j8YB1koBcEBd4SayhPQkywZnV6Np338Tx5n4Ob81fQQp5gmZzz0Wo5PQt93_8WSg-d21Ogjxd6qBW1jO4ILUF7rKsRotxBN1qfwMpHrpjw5G_zdSk7L_SItMhAZD9_9IjiQrdniYfaK6p9ohHx9ARgZCW0XI1IyB-SW2m5eWJet5ONEz-1sKoU9umVcHUEPXIrKTt4G-fMB2Waynh4YX2JdPxua7DuvO3z8ShvT_W2kaiV3BuBy7uZ9yVhMIFwjpomssh0IIGZPp3MQnvJFmEK6lFQ58MBkv_5FCrHPeWnvWIGGIOJ-vYrb9oqZ8uPApjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5SiukSwaM6EN8dAD9kWg_Oe7JFaUMqMGZLVc5qoS94sp-e4X8Qexsv9-RWZrT_Dhz4l7b8qYToUjxn8SK-eaQQ8QdMATVsWVYmiHUt6UevkwrudAEG3DxVSYuF9o0DG_dzOwrHMGFovnF-4jj7pBnaS11KnTU8mgVUXZ2kQMGKluGB41DHbSxRw1REzAU1MxwXbwayG7KtdNXUOV_Dq6gSbnCP_WciPPhAsdrZtipKS1j4xQCS17u-ynCFy2JBnnY1KAzdvHWRUAYaoShO7FVbsuKUoXEY5EvnEaibVeuJHJrg65-B73KCQtzp952g9csRt7Qf3QpL_bDAVVhR4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwzJIByrqqMInfxq6AbsbowRAI25uu4X5EmLE6ZYtMBXZ751bGuDpjOa1-fwi_LCBVlmpGgkRe-t7lPlpJdKAqo7L_4-YvFDkAGUBmWv0irb2sEs065hNCyE9ev9dHL-B96IBfwQzRBRLDOw7eMPOsQNwJRpmrj7TLygXiXTkrCV7I_Q3HnYQY-_M5n5hNxkNpFok4hiapHoY2OvxZLkCB6STLfxqufcC2dMHjeuTojMtKdaUil0thhm5lHeDn2cSCJJEQOhE3T3ylKD2fCYkap_0akwO2eNsvLknFKCiE2GRUnLgwUHJX84NPx4ujYuBIHVoJTIiF1Qr-XrXMrjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUvVrZidp3tvhXVagK-18LTMB7nE9yA1mZzIqhNFRE5Itg2KEZUqYMMy3_arA_IwZMrpTuxFh1h3xsUiHoQ8AC7C5FSZQd43ksTbWlsd0PCp-RU_TTbfATO0CRxznSV0A08DZju7W777gbKjNWewHQSAKgoA-hO-uGdzWD3_ZTT8ZS1qp36NItCg1BbXGy5kf8TAZm3Acfw1Ce680Onm0tRcVIfba1xfCKkskHIATdfkDWqFixWscElGN4lIigXHMRO4tTjkImUxPvca7LZ0K28gvMJmqvdFHFf3iTkzs1lGA0a1FabtfW65KiKnmfDKjbzkeilIhe01mty-1ZEzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=rSe7Puux9h-75C_RWfIbBdXdJv3mA830DjESe9hNnC-GrfkijfEGBuHyWsVXZWmhVSbvRwpjNiLSLyoTk0YaS30jdL3Jdh2tj__lufm7F2EMpBZcpmCgHVThWfzGTSxm5LWKEAEN4uOW1MUsh3HWvMm6xO5XWL5OxzVA8EZXbL9SMfwa7JrfOAVraMoesXPy04Q4OviS8Sp2U1AZOTXFvhNGMUz20XJTIsbZngJOz5SlmVj52WiGBkxXVAJlctq7HY_m45CFFS_0fhxCL2Ju7YKlY36M8QQTBzDbABhBqmmBj2pQuJTOltMiD_WhmwFTL9QmbSpL_ZAi2WUV41e9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=rSe7Puux9h-75C_RWfIbBdXdJv3mA830DjESe9hNnC-GrfkijfEGBuHyWsVXZWmhVSbvRwpjNiLSLyoTk0YaS30jdL3Jdh2tj__lufm7F2EMpBZcpmCgHVThWfzGTSxm5LWKEAEN4uOW1MUsh3HWvMm6xO5XWL5OxzVA8EZXbL9SMfwa7JrfOAVraMoesXPy04Q4OviS8Sp2U1AZOTXFvhNGMUz20XJTIsbZngJOz5SlmVj52WiGBkxXVAJlctq7HY_m45CFFS_0fhxCL2Ju7YKlY36M8QQTBzDbABhBqmmBj2pQuJTOltMiD_WhmwFTL9QmbSpL_ZAi2WUV41e9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=HKOV2I4QCxrNdgN2PTg5xMRLqWmT3nYL3QCbuXMnr3Ts1h4uIsBtewfVKUw8WpZO8tVI9U1ECCZ6eA9HtXXkEFXoNQR63whuW8NFKn3NIAh-qNC3ThftqZRAGoXX21rbfAUfdNPWV0l2tFwdVldsVMx4ZVYa-P2XJDrMLZbNe4Pk1YfqBKH2WRutzOMA2pZ1XOsbtNyse3nCEGz0xCPhyW9I8QIVXmCumQFtJ-Ff8dFYcn2352ZoQrj1geeCmVDm45JYFPgaTzhGOzDDYUkrQrBcKEWZjw3etlNu7iXIoTwHtkMwjPpC9Och63uMxu8oiyzsN6451sQokKYXa5ypIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=HKOV2I4QCxrNdgN2PTg5xMRLqWmT3nYL3QCbuXMnr3Ts1h4uIsBtewfVKUw8WpZO8tVI9U1ECCZ6eA9HtXXkEFXoNQR63whuW8NFKn3NIAh-qNC3ThftqZRAGoXX21rbfAUfdNPWV0l2tFwdVldsVMx4ZVYa-P2XJDrMLZbNe4Pk1YfqBKH2WRutzOMA2pZ1XOsbtNyse3nCEGz0xCPhyW9I8QIVXmCumQFtJ-Ff8dFYcn2352ZoQrj1geeCmVDm45JYFPgaTzhGOzDDYUkrQrBcKEWZjw3etlNu7iXIoTwHtkMwjPpC9Och63uMxu8oiyzsN6451sQokKYXa5ypIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXFwv6RdeQ159WUORaRBuFv7ObaGvIcaN4LC3pf8UCTosdGup-MZER9ffwFWXktorhd7KDfZxzaSL33e-ISF0Jeou9WZPqKUH6e_R2YPjwYFcPpUUG3RWPVH-Yq5nmN7fJiJ5WIchnQwE3-Gxh0637IRBpdFxj2JYEkIYOVT-YKyXP1781oZZqRh-uJf2ZHyhgov_OiI3_FfFBok25mtRW0Pja7ntaV_XEPnFNwuO9X2ckbGCQT3YZqNV-lWQ6oAUOgsEo0b0jwwzpmJ5mLDxDpFO2B69pvPhabt91jv6vVNkIvadbnL-4NlS85ZOAf6Ow418Rz7G7Wpus95ULK2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30932" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30931" target="_blank">📅 21:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9zsk3MrxYE5IwBBKtVzGnA1S7V4I1VMvGA6V1xHZI5jbHUrSHN6_JCExOwqaqRfh08JC6JKbH07NHuE5vuDZVTGn2RPK_K3dSm84g2ksC6fmIGNSKBVLYEgOFE3atya3kaz3PHBU-61h9WtzMRxHwCKlMV--xypj8BHoGOetAntK9cvu8Ad5g3ndZ7gMNGilLl3hWyHcbqTT6KNHzKfxxwtNxvLAzcKTdFMXHNl_6amABGewVlSGcp4gdz-A9nHXRYmRkBkZOFsQ9NGJyywWeSkM2KoRwfdbh7U9oopVMtJ1KIPPgcLyzf0hRjwV2djNHvrcOA5UBOc6n27GcV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UY9B9DmuFgQT6fxRIDR2KzVVaYoANaf8FMDbz2dRyECpN6GCo2FQhBLNHKUso72WFmv_JU_RVTvFacqwpI7U_pmu9h7QZhClNJPA8NIE_3xqnWo8dtWCwapHa8gr0xK8eIJP1FULppuH0h43z5RYscrj4qTbo4-VAm6aQvgshkDCrGO4Y8KGV6bxNwOI1aDL71vSiDLU3vAf75qNqrNK7oeKrkuyNx6ItkY2HuYybLvUbH01FyirO9ZjtLAkQVBJAHXrAIr99A98i1j8bHMWjRq2CYN0yIOSLLMfApYAO6U6x4f63QIEMAT9hh0lvPrX2ElywSs3zOOyO2_ncItixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvgSdNlMzdEFrplJ1unsOGQHwtSpfAkfLACvzsmhgHo24GN35MS38iFlyoqnoK2LTOIem6Nm-NnUJM4OB6waK9glpcDY2n_UA-LWo_nuNQxBKg-PJx4PvyIvk1StGauwtpNahfa2gPw774bjoJumK2Lbefy-0cr21A2ErO4vDZ_VXdmY923qEN-e2UvF2OhlQOz-TxcrQWp4EbCk9D2_WuOXNwjl7q-8RDD2nwTe_LTJn1ZuJC3mMsXg0gkLaqLh8eZFDGTag-lGwVGhv3FyczIplO_T8uAbgXbQBiDiX4kDM72-Kai6fZJP9jmXUKwl2p4ya0tFDGM_0vILeD1qyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=R6wM3SlqS3sFI8ed8y9gIxhKidDqSh_nOEgna_RX9Af5NNjGIHWF-flXgkYw1Jp1zm9KL1vs4zrnYekSku2bosWiOQSI1rRO0Npm1B1xVeHl52nA7G8kEyVGxIGrogYx9pDdmth6icBGz5vgFm6CEf1gnxj4_eTFFCJDum0cCbVKiyXR4mlRYmrjxyxlke4WpagnEoNiHW7CAcoxZyfxsFauyhS-R5e6ziOUJCOfxJ0f6qLGMVMUNRV3Wb9XvRXx8nlmAtHEdaOQbJBDY6brTkObR5rJ7Jzbi4h2upLyBt9ovT0I7pnHyANFIKWKnyFUPpfCfzBQNmrxJDxx9RP4_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=R6wM3SlqS3sFI8ed8y9gIxhKidDqSh_nOEgna_RX9Af5NNjGIHWF-flXgkYw1Jp1zm9KL1vs4zrnYekSku2bosWiOQSI1rRO0Npm1B1xVeHl52nA7G8kEyVGxIGrogYx9pDdmth6icBGz5vgFm6CEf1gnxj4_eTFFCJDum0cCbVKiyXR4mlRYmrjxyxlke4WpagnEoNiHW7CAcoxZyfxsFauyhS-R5e6ziOUJCOfxJ0f6qLGMVMUNRV3Wb9XvRXx8nlmAtHEdaOQbJBDY6brTkObR5rJ7Jzbi4h2upLyBt9ovT0I7pnHyANFIKWKnyFUPpfCfzBQNmrxJDxx9RP4_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=bQ8uAULqg3ARL_JXjHTx2LQ3vyeK7Ny3N4pOka7Jw1LyuP7NHcZs-iZLh7SYA7DKnnC3ht8MYLX3ZZ5P9lPGtqSjiK0SLzW_XSAOISOLS8PZf26W6-v3Fe-QYbBunLyGTo1A2GVImmsBKyLYHKOoPypdqO-mVemDn4n8hWvPPNg06I9CVAURQDwHomS8vIAXBjlPYayP_zwA0Hacp2BgW4DDXUDahY-C0WZqPUbOrPFilXu69LnSjfP87st4LlBYerCYcFvKnRXQnznsbYqyfcF2D-rCsjZke7Je9BL3ybbCaecWdnXhxMiKQ7nVJq3vQRB52FzGGvM4ESASgFnUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=bQ8uAULqg3ARL_JXjHTx2LQ3vyeK7Ny3N4pOka7Jw1LyuP7NHcZs-iZLh7SYA7DKnnC3ht8MYLX3ZZ5P9lPGtqSjiK0SLzW_XSAOISOLS8PZf26W6-v3Fe-QYbBunLyGTo1A2GVImmsBKyLYHKOoPypdqO-mVemDn4n8hWvPPNg06I9CVAURQDwHomS8vIAXBjlPYayP_zwA0Hacp2BgW4DDXUDahY-C0WZqPUbOrPFilXu69LnSjfP87st4LlBYerCYcFvKnRXQnznsbYqyfcF2D-rCsjZke7Je9BL3ybbCaecWdnXhxMiKQ7nVJq3vQRB52FzGGvM4ESASgFnUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حمایت جانانه و قاطعانه فیلیپه ملو ستاره سابق تیم‌ملی از رونالدو:
یه‌تفاوت خیلی فاحش بین رفتاربازیکنان با رونالدو و رفتار بازیکنای آرژانتینی با لیونل مسی وجود داره. من‌میبینم که وقتی بازیکنان حریف مقابل رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو پرتغال هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمی رسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ واقعا اصلاً راه نداره!"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVq5abzyJCavvumjReQloE_YoMVOk1iMkI8APuFSjrbFhWNNylxlo7HlPcJ4ITHmVu_gNHyFf15H2eLthHKLLEvyL1wbzCqXrDCrv-CdyXJutvw-5Bwmbs8TXKTA8jlQhhn3meOkzcN3vJDxsO30iwZI6JLdZd0H4NRh4smNEYMo9_ZvvkBRTegZStKT0ezkg9be4upaZRCtuFmzgPOabsCiIOvOVrxBil6lBXTPSOaz3v2VO0fyaFmqEVcJZaT1JHZ190X-D7mkLMKv5zEFXChQzet3UjhGHBt25Ky4V_LNkJ53x5UkXINPdc6OeMTl6wkm0Dm_bSWWLVZCledwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2e3a0sCkNLdk-ThxD-mF3DInQEptEaVp2Mcnldikto6a2icTyf2_EHT5mypb40V3NgrRWITiQXatc0zi2StuJmCPj8hnnkMdTv1Iq96YqY4x7KM88G91dWQdOTU_wpdCbmJ4M964a0SdvxThR4ThWBUNCQ3lg0Zlif7VHx2lvgSLUdG7XVpZ4350d0ed4zmiak-LLqTGpE2lnwcutqcsDX0XyGi28KaX1E4DbMjN9mZ6U1GLlGDpCvEep_uJZHbCmFMYeSf-w8EJae2kyu8ULTW52-M4CP9cVz1dL6sZgAhZR2QjxDPR5RUjf8i0phNzz2Utv0XqgSZzJfwfKc7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uitc87nanfUw4XIPCLqcCHqXLLNdbfI-jb2wy0oytzTd1TmVgC0vD8tsPCKFZsiPnmAi0XNftC0efLpMF4IBmsNrvHvf7_4-S9_jTLgFASG1wor9-Y5ONl4W72EZOdz9Zruh-KMVC_rY5hLGbPObckbV6D8oEDc9ecC3T-Z8sGh58bAc0WK1RuZ5wCX00swh3koYBIo0XR9eogQW2nmUHUMqNvfMRiJImAuvVb9SUlvme0NYLXyFcfhTF9uXsbt-FOtSh_We0On3zXAyhyKmoKCwsIqmhSDJSudoTtGaMGTAayFBdmIeV9SIMGT4-pZseExxWSGBso8UW4gGm042dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxF3D-MhD4-zux1m-enqCc6tKpnwU1IyzX0PJg8hvM5NcAxYh_0dJm8pFgM457eX2zYlzCDY1bhy8k93kTDa_Kax41Yg2WdTkBTFqrUq6GecQa1fuoyqOZvWFNx-6OMGofdp1kCWNM8jOZGzuCHKA01ozS-E4XyzaDmYzTQWj03jf-x_OMSODL4EQm8gFR-E0WYWUnabY0Y5k0dM-9BjGAIYhF3j5GBqEMdUoaGaqeOjOdm9bJFA8ZC1OkAs-t9QxkAmYvFGvEEPR5a2zzoWsZO51PjAaC09wRdNofHfKwatEcp8ZvehmIyYXs_N-2AHYaKr8draOWFD-IHjLKjUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KizNxuQwUfsxwLrGGhibnjPTAodoF5iMba2XbzzzoLk9wOji4k-4FHPPxYuTbELvtoeo4KJLlenNE_NigXbgFw45DHUspaZ1cSCoGH88MQ_XdTK-e0WG5tETQMty9dT-_Qv3emMxFlUlvU6S9kPDtOnHT_TDaMjf9rdqCHNYHawKLVreXLVkmCQOCS5yvlwJYmuB7EwjlQDy2yioGy6VRxsLw00TkuXPPHW-AEowI1aZrUz4w2lkuknGt86XGnCAhTgRApaYVJmode9H4g9WcJo66U64Zm-rlt_dN3ua9PgrB18m2LF22mLxxNXXlbfn6B-MHhYJVIgmQ48KtXHF7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewez2KT0VwjfYKuA9ti9uxw3CGPdg90aMvxoxX_YzxTLOnbds3xc99TU21d1JvBQ_Mg3PLQmlvzNlobOYJS9FS8462jfo9HEwWyOme5frI5zR2yX0i9rgOQ0Oyd1nDNO-WNNxsVcE9sdIiB0ijuhkP-DC8NLQWwQPAiQa61yNIJv8D7odTGM0z0E-u_Y3JRdpE6q9Wq4tYIkeJkYiNXIAtfeU26EgY_eytagBphRb6cDWCGOJKsWg7fUSiFXSDu2n29FGkk1NguLX_WouvT_R1_TCpkkEROMK5Yy2J4068ZFlJTG7kEopYR8ZoghIu9ZNK59hJPRksWgZza2OCHb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWeptM5kbePiHQgiO9muAckU-I4OBthGqsLestnidqureV49IGFBT3k83dmKjMaZlgX4bPytRHSjlNET62NYR-t2Zdi-bFQW0Hgz22rqHE05J_ODkUNfwZYYdOaVlLQlSqDBHjAZFTXfWA5DyzrCWTqdz4g2trj2vR9_OYgnnJ65kVKkVhj4wBD2BtXIbkU4kAWE9haIKccSFQAJaPBRJPcMSYAttSKb9i2Y2CAHM6CJb0P4z_brq4VzlfIZj8IBwqBNm8k_aVt4xMCV-YYUiL0do7Wwvr2W6x2FR7Aducg9QzdasMira_8NUm6twoxY_xhoSa2BKKHnXR9ZKoYlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8K3tfFMgq9UxUV5sIh6EX57KpK_hpmbJZfsTGaSxRVJ15EjHP5lFMgjAmtbICI0oLMvvRTSxSYUytyefT1UyOLmNYa0uJQXIq8nL5f4KP2eoNGUE6toLGJ0Bgg8YC0bMyaZh1VPjaBLrym12hPuNYR8DAIDCP5k-4yp2Sr8JZXs6jZLyPp6GSD-bWQTxqP_qqDIu7oMMHGW4U-NoQFu1TM0Dp5JlHC5jKWmrHnndCZiWgHPGPD0RC6vpXAHdLXkUeJJy_tfqRVRdvfBaFKMqkQaniPNnBSfiyY3Ksh7qrN9jG7gIuCKzecDb9J_SD_d2C04MRA6nlLg6hukZzQK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUDB3k9cl8_PwEL9ECVycwR7ZBoOJl3YxT9dfTgySeIWiBEqEyT5gcRzMB2DBBvjt5f-dyc5yGYEEGVGr03Xhd-6rWuqeWC2NC77M85e3uhEeSD4YvgB1FGqZeo8uKNAHMzItWaiUOc3F3V9od_JG_s7CnrMEJMp80DeIXhl8UhjwklwNW8ywsHSMEFobwKWPVtdFYNZERSLCXDlA_3-lvn1H7D5phBDZWCD2H41DRbnWKo8ep1ZMuE2LhjYA0FZUl9wyhvlJoKlYIEwSaGbaJC6UrQJ5KLe0XVLLvaYuk05oyvV338UmYXJ76f4QLNuNKVhQr5Zia1oNk3Au2audw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYilPj-_ZxWO3raHCVXoZwAunH0IQfGZExTEaqffdYhBg4ph1Ms_F3lH-7POqdy3gJMUPfkFl1q-NYkxLMX9fjHsATpUse90-r--EhtMxWzEvpnEeL2ayjviBDkEBaUlpWAYVWluIsNWG-a8oKbK1JlLOE3OLMn6tlb5pxJgMaTTIz41nj-dRtNQxsEF5KRj8j_sfJ9vlJjhrlrHVgm003JXnRnqna76_OlSQ9_5d-Cm3fQm2SW-AvGCvb0ISTnRHJAs1SwPyip0IJmnUkOAgiTsraHHo0QhZDIO1dYVJLKl-LD2L0d4ooq4qAZTnUztzbuuVTYuOndFn2yh9jVFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyML5wlmaaDfBIT-edOz6OLH16RQperiALlh6Zsde9l31ycrQGOx4UPmj8UtgwyyMzFhcq6QtcoSMZu1q_mOunJVLWIg5Hz1gZb2zIy9qQaSSQ_c2YrA0BmI5DdBd6ht_hLwSlhiWFD91vGbtx33xZZMg68Ay_rgoqi_s7oSCL3lWbV1sn0lsr_mTEdk9VoKgtnClfJX4X9xERxX_EHvxHjyWzI3F9P5aiags4LF8EC0Hmf3SBgiVMZscyqvbVQJ9VAvv9hl0qJG_zuF-zgDIeDcVg0_aW9sPEzxJHBwOeWuhLXRggIOygRDAnLi3MKSbjqyD6d8pU741TbVE2-9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu66qNpyi8STE06Hp-k1rdxEco8lEgdlnVQ_0_AdwmhHFPDhEPMXSa4codbni1US0Y0RWwsc_XOcgmLfIFHNErUC4V3sVsZv5M39JhRoPli4ERuDSxPzG4eF6FlnA4mOpM-vxbLqovktINt6yxVj7Jyee7G_0sTpLzhKoiplue1AySjDJnw9tZdiFu3sRBEGUAz4hzu1HS8_xb315wRDzm47N3freIhWsUoCK4xApaJsPiF611pw2XKxgMYSyU7IcVWdfaHIZQ_P3uSGPFlglkG2_nObTiKcDrDRTcEGeuK3X5M7jpLroQaKntUEpHeAXiCe3YxGqp0sk7lg8CGKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmFonIrCjxk07rEGMc8nP0K0YiITZrSTkTL-K4c7UaVLojyfze7dBO30lPVjCRKlqGjyfJPBIS7ND5sqp-bft0259JeRwlprmHTKjc06qL7iNNa6BJT4xoxJyZ1lKhzgQKzrljjPFkHEf3VnjjFwMij6vj52AJ1CyEYUxAxDFIGLjeOGxD0zyoWtyArapTIBLho6e_Vt3BsnDChjBz5qSrg_IOiTjr4vZhvuMxrhpQj2k2WztKMIRsc2jAwAB3arKy_44eLWK7mH4M-wuMt18SvicLj80xgyws6sEq52kjI1RDymvtjd9DvvwBmlP6n4yHRzKERDsKsUZRF-0hbUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=nUuCJU9V7uohbenwcy0JiQ-FdpNswUIiMJPgrzLB07kOXOPOHMqKX7iD3uvwiz5qojISuNd3zSJwPw25vKGIAWN8MJP4kvrpb_XbuPc7ALa7EabIktTOJ5YVeDz_taQMiuXzP-nNfU75SWiBQZt2DEHvif64uQiyWf4nvV3ZrJOpTTPeXs2JGz5c16MT9AzPLOE4R88EdLn1u-xoDU3vQf55IXm2uALwWU4FsXx49uNJ3KcYj257GG2oUrDTy4xXwfshSaWHk_VzDmrPMhUSrmxL0ylqBBqSsyN6ZxxvA0N4pGpekrhCMY-OA1fVjhP3__OZebqXRsKOaKKuvRx9d1cs6j3e_hRg9sEFGhOeU12CoRhtSS5MJ2MfaHDbLmQx0c3nj8QD-twpZkzEqFgEUH7PU13JAHh0UmS8yp_QQRcosDTzoLQ4VklffJUHfTktRejsb8TV8O01YT473cdaCW1Z76bflAvi6xHmejna90BnJWzz2zi5NMKWLfPwcWAFpG04AbyB-Som_RI0ypJmrTCV9hPyizP03HWO3JdrFQMSRWaSpfqTdoBviEd4LbdV5PKhaEk94-jU3S8kHhpvb-zfE93d1bYO7HmvLpakOEGNKxF7gLPO-gC5XfD6iaCpzlVGrMoLUux6FMAUpmmwdI0mHsn3-cT5RO2Dwr_4pus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=nUuCJU9V7uohbenwcy0JiQ-FdpNswUIiMJPgrzLB07kOXOPOHMqKX7iD3uvwiz5qojISuNd3zSJwPw25vKGIAWN8MJP4kvrpb_XbuPc7ALa7EabIktTOJ5YVeDz_taQMiuXzP-nNfU75SWiBQZt2DEHvif64uQiyWf4nvV3ZrJOpTTPeXs2JGz5c16MT9AzPLOE4R88EdLn1u-xoDU3vQf55IXm2uALwWU4FsXx49uNJ3KcYj257GG2oUrDTy4xXwfshSaWHk_VzDmrPMhUSrmxL0ylqBBqSsyN6ZxxvA0N4pGpekrhCMY-OA1fVjhP3__OZebqXRsKOaKKuvRx9d1cs6j3e_hRg9sEFGhOeU12CoRhtSS5MJ2MfaHDbLmQx0c3nj8QD-twpZkzEqFgEUH7PU13JAHh0UmS8yp_QQRcosDTzoLQ4VklffJUHfTktRejsb8TV8O01YT473cdaCW1Z76bflAvi6xHmejna90BnJWzz2zi5NMKWLfPwcWAFpG04AbyB-Som_RI0ypJmrTCV9hPyizP03HWO3JdrFQMSRWaSpfqTdoBviEd4LbdV5PKhaEk94-jU3S8kHhpvb-zfE93d1bYO7HmvLpakOEGNKxF7gLPO-gC5XfD6iaCpzlVGrMoLUux6FMAUpmmwdI0mHsn3-cT5RO2Dwr_4pus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=gJRo_G4992WhMcxYsScTh7X_YZB-ytUTFXHuJMkkVGE2SX_O3glE8GZ9KnYnIAKspPFMY6VdTvlpPQGU3eucsGuArB7HBhRurT3gf4Qk6N7r685Ok_CowDM-dWESQrea8vMJ7SsWvVHIoTzGPR_SjP3gcC_zq5EGi_7BJ7gFE6q_X3v0QU2L6Eg_x9IsiKvurSF87hH6gveqe2ZICxNLU_d5jEExdeGrOWJQSCMrXphsuIx6jxF8Qc515UDJuNLn1sA1jvicUXtWq97OUeeY0ZaJ7RFD4vW593dc0XJ5e7Kbt3oPzpR0674RLLHQcVbDkmT_2f83aFS_9GauKrm8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=gJRo_G4992WhMcxYsScTh7X_YZB-ytUTFXHuJMkkVGE2SX_O3glE8GZ9KnYnIAKspPFMY6VdTvlpPQGU3eucsGuArB7HBhRurT3gf4Qk6N7r685Ok_CowDM-dWESQrea8vMJ7SsWvVHIoTzGPR_SjP3gcC_zq5EGi_7BJ7gFE6q_X3v0QU2L6Eg_x9IsiKvurSF87hH6gveqe2ZICxNLU_d5jEExdeGrOWJQSCMrXphsuIx6jxF8Qc515UDJuNLn1sA1jvicUXtWq97OUeeY0ZaJ7RFD4vW593dc0XJ5e7Kbt3oPzpR0674RLLHQcVbDkmT_2f83aFS_9GauKrm8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTyQzHx2kyQB-bxaR_N1bH6GzHp0YgzpjlOnFwB29_GJZaBNT_0TUMNAb0fvJY69LABTWP46xcEXBNfF6ckoscfkFslXOR0BX__4cdlkSS-IJyveM225GloGctbV_jEwkQ2elPZVSMv-qvu6GDRNYqSC9xGRlGqo3_hps8vLN7ihpZ-9KzxN0IBvfaUh63Knde-tc5Wso679MwiLyPrFzPeqlrjjRGiZhbvI_3BxPwc81TFLw87ogVZjVlvb828PnH-x7rpattejgRqP8HCDMfcqbV66SRNdCc_DwpR0p0I7BAx5uBd3xgMAbquHisUhDhu5lUI1jjY07xVeknIEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwH72mYJQ-BFgls_vWhUpBGDYjnELJjF4-h1v3mclAITutfRCW_txBLx23_snKlNvnbLpoX0mYk53ksf8OV31vi5SeXA2eg0sEu4hVr0aZmY5Lomh_sg9nnv_5PE6yuzYEcSPCxQUlcapTU8uagG7r21xcVkFF125CiqV3R9SHwbWFmOhsjP5tSN7KGTNhHnibQidpvyDYGP705iS4ECkskUzuGUQOEgJSq616m2h8f03lbMzXNAlia_dVOuVPJcHNHqHkwchsmR-vX3BCGV_tNn9dNFxA97lWQQoqr7HS-sVMlTQlno5C_KInANdsxwagwcoMwtdoCWJN2OKVBq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJchV_SjwqDBBtv6f880ZKa4RX9vi0VGnns8qlcujAYpSmFDD3Sa8VIuX4oSwG_NgAnPByHyLzX9gIpxY8rDeHJFTZOnBucgFmvwqxq_PYwc3zP-Yd3QpONCnVJak5SPdtvnTf01iknGpOtcc8rJiTa6xZVbXsjcgp6x8OxXRZPUhkAsKl1wvTWSnPesr7b9Ej2d0wFKIK6-YWpC4nLz8M53cHGfgF6sSxKXFnjfP80_Zd08y6BApjPTbX_TWumF_kAhB0flh8txfy8hVVMNtKkC79dSRevKf_HjfPKwsy1R7lAztkiCzSjxEnlD_zL48qlbb68Fryv2peaoVrpkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=nhgUTalt4yQ9ZrEAWHcKCWLlF3EXn0ROc2auRdMDpyH92wRLYGfElqsM1OnH5kirqEDkXpe-q-y84wGYHAZPYrmN4VxLsiBk3GTaUsW1J9nOlrrcYIKNHIsxqasHGXUz2ya5f78YyPLQV_UbnhQ0tRnrpHj9IQajr8agwckypSwrxZim348rl1ChvNQnWGsQrxEbglR_eODXKXjpZrN_Ofk-8uY1ALxCAV8qfvzHW-vwDYfzKOg2DyMPfQASXvOCFOPDawgIhFMGAOWAUv8d5Tt9XxpKQuWIVFSHS4_XVGZumi-obH5Saz05wkdTVnte2GKRLrTcq65_RcNUzH-Q3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=nhgUTalt4yQ9ZrEAWHcKCWLlF3EXn0ROc2auRdMDpyH92wRLYGfElqsM1OnH5kirqEDkXpe-q-y84wGYHAZPYrmN4VxLsiBk3GTaUsW1J9nOlrrcYIKNHIsxqasHGXUz2ya5f78YyPLQV_UbnhQ0tRnrpHj9IQajr8agwckypSwrxZim348rl1ChvNQnWGsQrxEbglR_eODXKXjpZrN_Ofk-8uY1ALxCAV8qfvzHW-vwDYfzKOg2DyMPfQASXvOCFOPDawgIhFMGAOWAUv8d5Tt9XxpKQuWIVFSHS4_XVGZumi-obH5Saz05wkdTVnte2GKRLrTcq65_RcNUzH-Q3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTj2I7MQg4eEVZORJdmoLXLSirHz09PF0DFYDxW_6Z2YgkCQYKDCNBw9R08G32Pqlt6S2mm6cHiRntgT5vFr0fTZcvj8a2DjU0aKB99No9ue9_c1de0IhdcjyG23cLVNqP8lt_AFrrX5AD8ClCBWXFwVio8GQ6ytKr6HuZz3roFXtB60Di2yCtD_u-P1OcBfzh3hnk4i8Bz8J4vae_JsrXbuIgVQxA35_e26Tb-pFzd70OFXRqmHMOiFmIxs1rF8PbJNSkYI5B77HtFvzz4_hhgkEGSKoU12wcfoTxE-nuiN5RCUsTyTzahOOUKoHbzn2LrdJdFIT6tnO8mV_S6S8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjM3-qTZmLPvmzQHbh5bDOqsybc-crhILcPwD9lVhb1zyD-5qNoJG0Y5DZwAEjBxRKbxydNS9zr-mNb6Zxf92RsWXOTLUQuyJciqL5foHAtNPH1Kuquo-mIzov1QnsV8NLK6pVDLiBcXLw79UNNyVAGFzlUonSIHqRG0OVWKnAhi0uPq4ZGkdU4zCM_QXzVtYhD0eZXeaPdXWDkBy0ZouNSqOy9WebzO2ce-LNW8nDGQQrgaQscLjLD__ocb3qW-eccytcBshOYitQB094d7qDPgok76kO--yWZvyP1K3NWOHpFZtiOQdvSFkw-KtS7eD8Oqe9Ih2HDle56nJp2hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aujjll6MPvPFuIXmEnUm0N8whkv7eAvczwZrIfKJUxb6ExFc9ebSMaYIq6ghi9_Y-BLb9pUXb2ZSXtHvRcG3Jj51wN1tFv8j5ig9G5elvv3U7Y77QLRjWmCzo3bwddCdwW0U9xpFBnENN2inIC56XuD6kCYzub77TWJdvuUQ53vI3zzhReF-zCX8lWh4qpCnd0eLOW1w9dAgl9JZkCPIv1IlvSYrCMoHs13UIA1VXXA8iYMkKwbZ-UjJ6bQQMrMwqifdHDR7E8ivm4zA3OsuO96r9FPs0fiFbkplgPWay6RuBgD6_xlYE2zrJGNOpdJS1sbJ_pkNd9syGx73ZZdhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb4vTY4CDSwkaUnw-sSc_HXZXkfKYNP8ibf5sspBMiLnzHdlruMlHZYw65s3jB_vfrS9dJDaIgQCnM4Dilrzt20cpCjDG94986kCZ0MmVAeReUrs2Ud3mCccq46nqBnw2P6fqrFEWb26SZhRoBGcFgn7un7QayoUyPr1eyT_pDMiAVtZU-Pjg40Gw6dGJzKubVJjI084oP7C2yAmKjhJlXWKhW0xIxoJAceK2XCOBUOM999N5bSro6mmWU9TrRJH4Ghx2SU4CrZNg7so0InFzTrlVLgZ87h88rYthlGY__dh1ZiM_oyPTKPQ8NXkb_griFUV9Rf_gnOtCCzgYun2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9qLNWK_lqYZ_iTgexREZ2gunZVAS2xtyMfchmnACS4txFfHKZxdk5I5X7BIkICaEQAEsHjmjJHq-xWvY_Q1YEV3Yg8E43OetXW84TVcsW2BwsmbSANgxaALwKmF2u5cao0YsYu-bzUMijEG0a8mMie3Qq_yfu_gY20oN_HrvxNEEyTGfaytwBcnNkdhQ0mdmvWCR2mivdUI6fzDJdO_wCO1kP6HxXKKninYwF6ZRAm3MBfprso7ai80GXyrsMGenWLnZnmJ2PCY3pre0kXA10pTwHY7UzzmDly7ZkSVu4MGPsUWJPsmUK3Ygq_lVxiIpP006spc38mmIYEf8St9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBFS7JoXzzHo9-L4FN-XYH1hQm4ltJpEt_AmMApGcH4lSZBbSefcGTDArnsU98aCwl8Qk6-i3yC6LBs09rb2gsZ95kChAxwMATJTE68zmYuEMZdLjJKrf2KYA7Cuq_FIrp97twZGzjU8pJRqGvjEVxk7WNxu5FosWJGpZWxw4qMOyYiZ58n5R-nHCKBgClsBnIFvoMH9lSrlpdIeNSh4fGZHZvT64y78tc69dInLgASBFZgk0xONoOoeQ489WFJPWVUJADe5KQUQmeVwLoM1WqpoGRHRUIWf3cnsV2ED1GcZfk0deKTO8hSdPq8Pq6GpJPnieWTr9HbjiSdl5hDtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=olrpjVxFH38hhR_JDdOa97BJY4dnRQRzyAehUEJKqDYqmT-jtaMoDUq_tptU_we8sIsSkERD_qCzsfGSZc_vY1CugR1bWoLn-SKFXXZXbu1sOIFJFHG3OKZ2dSVwlpKO5q1TnPbdpJOuWy69KCCJVYvQWWfMW5LqSpD2obbl9VQUh_tB7ve_wo4lrc6FVUYASN_ZX36T072wZ-bmOZ3IGUQHbSUi50YS_5vFT5DHouWhN-371r2iy1UNcM2jx6yb-G3o_HzPeZzWH5buMmSMEWib4W0TNUf2bMkWJUX4WL-Bt-ijkW8bDcc0GmejuamXF1l0r3hZmekSj8u-LmEP3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=olrpjVxFH38hhR_JDdOa97BJY4dnRQRzyAehUEJKqDYqmT-jtaMoDUq_tptU_we8sIsSkERD_qCzsfGSZc_vY1CugR1bWoLn-SKFXXZXbu1sOIFJFHG3OKZ2dSVwlpKO5q1TnPbdpJOuWy69KCCJVYvQWWfMW5LqSpD2obbl9VQUh_tB7ve_wo4lrc6FVUYASN_ZX36T072wZ-bmOZ3IGUQHbSUi50YS_5vFT5DHouWhN-371r2iy1UNcM2jx6yb-G3o_HzPeZzWH5buMmSMEWib4W0TNUf2bMkWJUX4WL-Bt-ijkW8bDcc0GmejuamXF1l0r3hZmekSj8u-LmEP3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA--HQsPDCMhtzAaGlUHTxUpITg3KRTOyAmRv2lMEPam-EgI1AXsxZWhDJjdoFeOqViwa_x3VElqgh3Kt_Gv5AA0Ju1qq5y6lIRqHtG89N0cUlQA-mR39c018sbmvtbcVu1ZqcoHT42fi9Ku8iT4CRZzkuT8qNoH6pFkmifX-J5gCu8XhIov1eHYIhDghVGSqP_e4m5LOkB7XaijbEhpITEQ-EWlIJMHDDlZMcD7A2wFFSokrkYUyzrJ6sIYnUyabLDdGj58OjW70XrrLSMwGN-ti09doIbXLFfgn575OLvogbOAFHFiEbNb_WPa6174gedlsd1ZF7CPSEZco3X5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biN8cPW8HaEB8uVtNDEePqxw-9D1S4nyI1Ia7bz9UMWXcndZCTPXXyNCKx6dIP4nK9zcEAVmeq2aqt-LNJ3THn1PQsaNG3Rd3fpNPPoh6FVmaU_6_Vo4o9h60VxFeNE_Z-BCC7ZBg_X4AOVtb5oJUnNX0wumm8rFNFxWGYLP8lZC7GgEtyAUrrYF787hsULXPI13i5ENsIF_rZAHccqRvAfDczx3ZejQq1ubr-7SgKBACRy-4ZRged5hIVNqDut2SKE7lJkn5Zf-ETkMEXhwEbVqYozpMhLT3MyCRzvBT_c8FK_TODnsoXczpqNEtmZ4qqmyhKWoYV9jMl4JuUrErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJe_4Zulzv81C9plZY6EGLRtsSOQcR89jVh-H-2L2aQy4t2kh-ddW2kqEGmrLmDWjcbQkJy2sC9mOsKIznxjfOqor-7UtLqKOk0aE2MfMPf0SuWHQN9uqpOyC73sJA3jyFtHzNOBQdHDn0v9uXhPdAXiajV68TxvOi5yX3FY39ziYyaP6dF9-8oim5j33rvwsw8gU2vJ01cbzotyYSMKMaXlCMi_gmi78zWwsiG66hLQRo9tCNoxI6yhvlfGpzOnjO0lubD2UfneM90oJR_l8Ax3fhXpLO7vunqxpRK4tNdL0kEVVaVXWE04iV8yroIi6idVkuIkRfdzSTZt5DhV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuwmpSFTGNjaXiRT5s7FgKIeu-tk1YSCNrsX8wfdOIfPBDRDq4oc4lxmZ_rEouJdBabvXffVPcAPKQrtB3v0utCw1g-4tYwSLFcFvpq1wu6eh2D6_P2MtOhZA9QLIXMGqAEXIW7ujUekSmZyZP6WIxkuh9Enrz3lB4f6vpGeP2-yMoZ9BHKo_gxanCmwQKTUP14gdh4-Fh83wutAQpIU-RUBwbxT18mrS5c2zqA3gHR_eGLjIJm1i_8jYbO8dSWbjs1eepo2a8Z9JyNiQkzzpvj3pJdVhZzNxGg0ATThHbLZtWH9l3HiObO9ZLML08IscU8pbhAa1oNaZCBT8fuxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIVmGGD4mNQ7selsajd_cY_FCmW_wTy_E7f713tvMSnMe4mUDE4pEOFz-ozU6Vso4QVPvCC1aJ-96U90KYW9DH2yHI5YP-GBpckxiYwC4X-4izIvFTPVoZPuSebCkp97ZNftR47qJlW5UhjWDu6xiEM3W_6s0c-VJgH3Fmjk7l_7rAcC-nbkKXvvFdz7HDzLaUSDlPdy0Kn2eQK_5YVQ8g_qAI8xT7-444ifL02rUlVdNJJyw0ykqQvEUch2tUOIeDGRGXbIFE89jxVoJHSvbUrr0oVguQYrE2Sd3TvbVcdyS_kLfOGwYd9DlUxggK0rHgQ3s72gwk-LNjafuC8c0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=E1YTblpHEg5NeSLuMbzfdklKnymeIwpI3_1Jb_r7zUz_NoEx_1pCvLDOobK3r-tyGlUzGX4v7JBEcX-minb_ATJW5x167diWp9bgDBNhxmmQfSSt_lxStBulhbDM7W6afLGKHEj26KA2pa-91BL5O3ZG5djWWLQY4kXa73jWlNwEVuFj4XQxP5Pf3PzcygV0ZDvnCQNV0jE6bDWgqT_DPz6KsQNzVy9vNbgfr6loJxMnVepvI9BSucsqLe-02-qfCxZZggHlOVY9OCA2kUUlVqfo7nBbV0l9BXQAU43xT7aVgFCMnYq40m1toGmAeWAn07edHGWiJdk4ULVyFCLRRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=E1YTblpHEg5NeSLuMbzfdklKnymeIwpI3_1Jb_r7zUz_NoEx_1pCvLDOobK3r-tyGlUzGX4v7JBEcX-minb_ATJW5x167diWp9bgDBNhxmmQfSSt_lxStBulhbDM7W6afLGKHEj26KA2pa-91BL5O3ZG5djWWLQY4kXa73jWlNwEVuFj4XQxP5Pf3PzcygV0ZDvnCQNV0jE6bDWgqT_DPz6KsQNzVy9vNbgfr6loJxMnVepvI9BSucsqLe-02-qfCxZZggHlOVY9OCA2kUUlVqfo7nBbV0l9BXQAU43xT7aVgFCMnYq40m1toGmAeWAn07edHGWiJdk4ULVyFCLRRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is8TTO992iK4RmqO-cgntaCtXLFtERWMHtt6ONN-014SyG-ynCubrzqgF3znXpySunp6_CcoaUyRUf2l69PFiPyu7n9op9bB7OcPrG-NgraEu0Deq9gr4ozQ3zpeco5ubq6XGilFKmQ9xnpaqIAqmy8Jhx7Ed6Iw6uq-j_eiCn3PbSb0D--aG-gkI0lV3J5f_6LnDO0othFcz7-29oC9w_XiEeWYlRmhTL6bso2l1fkLWD6stn9UfudNY6h_e5MF0P5e8uzL1cQ_LEPJb4RZddvcw97ttQEEsVt0sVMgEeGlxfhi4vmLx-0Mr9OrhvX4w5Mx0EHhrsXjZF2lIc4yWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSXX1aL7hPD1g4SskzH6J8KC3uxJoKi8zA2vi8kUha71vSS860R7djQcH4unVtJeIty2Fe7buZoJPWsFjKFBzeHJoi1UNGaM7HahpmPPYyfdZ-DHUyiDkXnkkjB_OwyoBcPNBwiWZDvLktMRWYMOssXYYm94zwzj8n8-UgpyoBTOEMNgsVvDsdZW7iFUHAJzt2gSq4SLOOT_CdkcCAX8pnciWS2vdrMOE4r-i7SZxnsuGHbAa5Bm_4LKD0Y31ZiTbeg-X5iVYaxIZldl5HKjHGlPTTDSB-tdvEZ27zdhb-TZ9RhuFzlY0vfoaOCv_qH3C4oS9ZtF-ND7NIWMqQQXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA1OeYrzkCYYlroRvWQnFhbpR3n8yvcL6PloWVkm3Aaf1iizFlWbF25N0655mr77dxmmX_P5hjRnyXbkFmQob1z1l7z5WlEorv5-noRGbMjYSD7qPenId8kF7BVplqFsQCExwXWTSp1mRKHTcoJuyOG_lPDeGAOBIm5kb485DCDszjZE39V-dLK9tY_0mCTE9cfol2YdtLDQcT3PEjODt9fcuaQTHaoWeKflbVaB-9CvJ1gMdwMBr2IInODLrdl2Ao2zEGIdHaU979mzve2KlBCQPMgLhRRwkubI6FZSb2k5WBb15c5qan5pREHpYcVed-UmqGujFXoE13M9EiWGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP3L1lAHWHshuygK55xKZRq-8f3lRIgpZxG_OgyFUFtS-l_dpDvfqhy1ThFH8UEiRpAoIgtPmMRvxZ4qlS--r72QTM5XuggzOEmX9XV4D7DoTAt6KnfrQAT0cOPidgL2lJAcpZ9KqP0h8te1k7LtXP1WBWmgYOsC7EwFwV1nits_BEo61MRewjDr2ZsfQGJUH4S1sUjPjTMRnu8r26qB7O1Oxo9KTrXKlWKb0DSbbE-urDFzBth9c2Vcxs9GwtbYnOAJW6zTNJVw9W5yB_xohAUp5Iw2xCxtiAZhiDDkqBm8nOP6gwZ-ZMIhv8lWPaHQ6VaGThAj898hOKWkNfVc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzEbc83ER2jjNdv0WtnNZzCl6JKhAo8k0Og7QZ1CT2KbmxPO0tPm9D9NuaynAe37gjvLZ5ANxBgyyjOZF7SBxo5KcIVjsR1SG8XcFP1ESmNT0N7DqOVAZ2n3r0_FhNXjgLMVdXp030zNsQ8HGJFBN0zEJ7920uMM7UEdR6COt9sYjUczvgySzMcj5rSSIobOShcQ0uavKx9a-SacjlDPy6oX--Z9bwC7csxkS13UzOINLbNT1RgYWCp6_XBFH6PlGwoqgmJcpBuP2xh45PUFzJiDFnA82qjkWfpEq3kqc9GsKjzVt-K_Vzd4QVTpFuhC5jhvf-_f3KUjfV0HxdtupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bURXzBx10bjjU9mSdfMlukvowk1jwzPoMBcBXM3Oifk9nfh3QM_B0v0xMYwm29UIh7SwEYpIOCK3RsveJHbhRvzF-Z29nFqAqGH8NYSAWEnDYMesUpth6DdWzR6ufxlLlYz5slcJ82U_-mNKzqK6b9zrYJcT2eh7AqaQYhIMahqHf3rYX674SW1SSzftI0bEhZkGPu7fjErtiswhzZWGG3AG28dPRX5TKTEuubGOeyYF2NjaHKHpMEGuTUJViYg-xn73Il5MGx3PrSFZSLrXCQLYE0TRGoO2VcG5XXXGcmB5xj2v3UmUhPbQgfzmo2EDqJujrx3BzNxMdGHNJ715SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa8R8akzjUh-6mIrTUV9RqOO0FlHVZy5gNfcR--xdOVeIWVcQSD-PkRhpIapi4-b_cqjMY6y7KjO3g54zxdlB3VChTozafAk4poz9iyyD7cd5qkeh1qviGLxxB1d12btqrk5U5roYmC7mIJx1w8leIUi-goddsJ5Y1ivZZk5sQPoavbwdtCOPWA-2zppwQngJvuawP3PLDuRXhWuWWoO-AmVTph3PXnQcgmL9SXmitmMyXXLgYt7BevvpdP-wsRkL0C31PtAW_PH2UpVL5SbAMOVK7rcR_OA0al-Mjf6ND6w0tgchiqJdugLDXhh8hgMjijCPsJUUl2xAcf1UWF0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDCtuB_RvUjTduP1SrmmK2T4x8tkvM7Uu5ygeIshuwfncDbAiYKr3nNoxLN9Y4lt1I0DSPlnmwKuUkNgDe4x1M3WZmU2O7T-w8kB5BqordTVRdN9ydpWTglWC43o_9AYle1RuCGaueOb1FY_C8xyJYIYwGv5koENvGpOHmIY8g34H8sDh1KTGX5Vqs1hlqEkT2xZgTPMPOE7LN3SLpbCsbMupNgD3MODJAvHO5usV8CLtLE4xTuI1UwqVB-zihLI5uRiida9YTVcbU9X-6fceOyz8oFBIq7seKdAVbP7yUyUdbPX6_IeWiqrPXP6_ZEvYRuVDVYqJMeBf2EcisKJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkUpfdWMOam1epwP64hG-2qf4wRMhUclzL6JMaXMXd9N88ghEEcqDZ9unIvAy8VAgFF3_WBxtcFwC9W-oW5IwafNroQvNa1v-6m6kofNpvsuBFaNARZ7Ea7OEPbBypReYTMOCgL4tSthsvCy0g0p_mDYGutDY3ul23BBkACWUwgDrFnEv4sQfgVLwPEoWfTID0VbtzX7v2-oq98mTeq7yI_58iCE85XwOonaqlDgWTLqGuPPY71izFxWwIUgzI3SIGGvr_IC0ncTV1-XiH75TL2MVG0LvZ0QIa0_IbC39dZjb9r6jzzBuFu5MF_BLGVphUP6BwsaCdhTuEGHcYf8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK1mxQBRC25cP3FoZYPko6h8hLKz9QENP5zNjhYsVB0Qd-GiAz1sVWyCxkTxehikrxDJzGlX_5gh1wKRlourA6LAoKTguECzVuFyLBOCvab3GJ_zvLn-5eUY9jdiWyAHxYi8zxaJwED1hI3eODQ1e5hn5S2hnuHORvx2DpI324y6RAR0IVDUHe_tkmNt9Azi9c-GGI-wKERVLaY49DdLvQEjNrSeW48RpWyUMq5qkzmAQCFNNYFiTwT5Ka36i7sflU1F1VMg-N-gMT1li2Yk6AHraTfbPPq5wjvXydgPSmkmGY4wRH5JXoGgf7qRbhHFljmfPPBb_QZHU0r8IZoOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2SlnU0Kr78WGoT4bf3f-0sKfSACzcLLGTMrAwJos420vkCmXOkK41y1NeSTkRgF_hFadxXEpMXMyqswrF5huGCXoM3qGM1Rb0nv35_BloJODqxTQOZ5bMXlkeIZSdXO4e5KAwKd3QrIqQIOjHXX8mYf4KRhWycMEK-FOzKy43JzElr60AMh_EgA2-EmM9SdRz8umhVuAxfwT1lkjmjlQ9hVs99uL5wMzlq1eeEjtE-489fTeqn2itx4apB0HBVVFPyhEkBW8z2UbDizqtENBFN7qMQwEPPG-2-ToIf-xCJN2iteIfvnpLa6VsDZmp9HwPAIPbNjq5t7Bvccgxf0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwl4Ecy-AKEskgrbnYxemevbIVt3XjW49xG8xCafQVvCXfKC1UkxgrswxuA1qEUcVUT2XZXkx_pyf0aszFko4BUt-kreJjJOAhym-fgEUIddMzZDRdhY6hGbHu8R4T45hWPGpMUtaElWzQICq4QMEY23uKhTABsWwT33k0Khi5sgFsx_qFJiWGA1FfdHNqjAn-7zPwfq-XjPnH0PpGTGhlMA8w33fDPwHuQb495vsmh3A184oSj2di55Nk-1cqVhEOQVyI6YTdADsP8Q4LeAfBAsfCiGB0eHZmy_qEBPt1sdoCuryf8flN3WHzVWpU6QQ-IpYFlYZ94ru1mzGlXwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0W6p1yp5lOQppqQsSd-qKl0xJom4Q4QlNfQxa8RgbmA_OglSLNoofyEpTiiAB3ZBhOPHB3yGEN3SPGuB7fAJxaqghev4HfqYxf-NIgVsOxUt9brvkDXQ4kdoGYUomQgyoa5aloyneDIz9mlf6wPpyOQHjTR6nNHsbapv1hFOPUij9lMyl8v_nTuDnNwvjj7Sw0AeyJCKHdRybH8LtMPdfqCejIdErsgI7atJ0II6rnrtmvfApAYq4WnVfNwxlbjwRPH0nlrAZ_bjKRiVktFECgqrrRM2ET7qi787oiwLcERKluXfAwEGpDFdR5oiC0xYS_uW_Pv_aYRFv5k0BF0vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=q6st3xOROvP395O_HVLhO2W6X5N7c8yf64_Fzwbu9Pfza2kbc1tSekorzwwD07q4hUkwLw88NRktPl1eA50i4ONNScL1-Dn9HU1dP_M7dazRq8WSM3daSkm5rdjxkOMe45vDtoKbC-Fc4W7itWpRrbw8dXVWjjje1mGeCI6gLgZZKaSkf20Raeri81GyXe2adMmORL8qmvPXHf4FDDAigDo_4ZxglWhcqxA4wQySuBJzre-zSC9wQmkqCdS5118VbErgrjoBHAh5E-TU-U1Iqtsg3Ef0DE5ZnCKhuhCJ7TRjVLt9hq129fw-TfFTAJfFgT-DbzWfDl2EiBqgzgiR9xMmM568TRd-VyyPAovehKtHL0d4gv5sF4X96NTr6F61B2n5UaNW-pFoMrIjGZHqpEEEaBDoMCzGMKCST1P4v0jLNDa5EbkVuumtFagsLrwFavmFyVpwLFy-iQfzPYLrziPac2KVnQwP6vL5yctL3aK-r09zAMoDVrP7t1xLEP7FZf8NAsN9A_E9CJOQquBZAMoXRwNw15ccEgSVpEe9S6SlR41LFWxtqBGBg7UMB5kOIIC7kq_s6fPJoFSFl0qQjpO2wLJQYJBlXotDveD7JTR17nAQUfcy5Do94qz8LhrFfEc3h4sp8mfm8WVXyLsxSejOHgdidtmQz357acuSLyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=q6st3xOROvP395O_HVLhO2W6X5N7c8yf64_Fzwbu9Pfza2kbc1tSekorzwwD07q4hUkwLw88NRktPl1eA50i4ONNScL1-Dn9HU1dP_M7dazRq8WSM3daSkm5rdjxkOMe45vDtoKbC-Fc4W7itWpRrbw8dXVWjjje1mGeCI6gLgZZKaSkf20Raeri81GyXe2adMmORL8qmvPXHf4FDDAigDo_4ZxglWhcqxA4wQySuBJzre-zSC9wQmkqCdS5118VbErgrjoBHAh5E-TU-U1Iqtsg3Ef0DE5ZnCKhuhCJ7TRjVLt9hq129fw-TfFTAJfFgT-DbzWfDl2EiBqgzgiR9xMmM568TRd-VyyPAovehKtHL0d4gv5sF4X96NTr6F61B2n5UaNW-pFoMrIjGZHqpEEEaBDoMCzGMKCST1P4v0jLNDa5EbkVuumtFagsLrwFavmFyVpwLFy-iQfzPYLrziPac2KVnQwP6vL5yctL3aK-r09zAMoDVrP7t1xLEP7FZf8NAsN9A_E9CJOQquBZAMoXRwNw15ccEgSVpEe9S6SlR41LFWxtqBGBg7UMB5kOIIC7kq_s6fPJoFSFl0qQjpO2wLJQYJBlXotDveD7JTR17nAQUfcy5Do94qz8LhrFfEc3h4sp8mfm8WVXyLsxSejOHgdidtmQz357acuSLyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_mraH0NWqaxyonuvzg-GQyfi-MAGf1a7BsLWXWsXdCSusJix7rPKHJ8fK211pguCmvCm2EpO5sDITC45G4EzzyoUsVcngPfLKP2kNlz-Gfq_dcLBbdz0sxN4YtZNqx3fJWUnPP5BR-uS-qDzmCoBUq8UU4lv_gqZ1Za_gI7O8w1UW4cbiZNT1WfoQERYvqrrwxoM2i_0IubXyGKB_ks-9GxWtGIrrxlysxMwhIzkjLIcIDW40uUe7EaF2OlfZAhDIXIyXLCKjyLtwS0RqQDi9AaQTW4ynKoZGPidqytPweZ4cnclWP60GCDzO3_YCvYZn52bkfk6QjrMohT_j8raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjmiYXNv1mE4w3jIEfSdEQwVfTleCbQg8OFEdXspRarbS3yAUMkESJ5Wo66sOPreVQxITW8Uv4zzgTfqMZ3ooEFOz0xkm4_VuAoocYwTWiWxgk7QMWHfDLnU5R8m_eQARpHKPdPW0a_5zkNv7Ce3iaUqIX8yHnWB3J3_p0CHBFC9-U8YcchaqMf_gQ-KfTE69p4oamVfdyBEbdES9NaLy9yhDayOM-I44J7jlJoHapAQA9PiTRjs8uSmAAULGJmAurQZndQM7fxsWn24goY2afOeDzNE-y7dGBX5ij3SBcj-3_sqZBfPTMQRmj5umVLtLvkNVRZxkzaoJo1Z0piAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
