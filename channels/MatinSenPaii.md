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
<img src="https://cdn1.telesco.pe/file/fCxzT1-3qnhk1rJabGE1KGwe_6CV2peJWRj4XBAQo2VCcnsGFytMQHzlJp--FWLLq1KJnBXwMoHNXCF8R6L75QjsHM7nkyGXebe4wr038vRsY1tjBCr-oNuFvwIhF52ZxxM0rNf7_Pcc9P8hHMm5JyONW7uQN3C0NcMYKs7OoOjtNh-pwJPHXYQeYXKb5YHfOLMqUliKVVnAJJGH_F9rldIEaTmo9UYt1WcOZv8VQEUdw_3nk1NnLO2nfONveNgbVaPBATcTQoPupkK3hP__3dsUlaM-AeqhfK-4ulfmkMFL2n4ha_6huQLGJ6pp0uDxtjgioqNDq_PfTUnk9oPJow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 121K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-3127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q44Ld-Z6r4KT9D_L0mZHRS2sWxxYDL6EQ076C7Qj7UaepCwyCkaBpKvAD6RiD6Wf9quoWGqYja6VpD_Cu3d0J_o-LHvfxGzCM-QjlZy16zTzjhhkBxBJ9RiM21tJ-Y5PwSiYkBF8p2h9udKMNtz0KFi6f4lkyEGVrIxAfdApbFm2u0RbBjc6yiE2Yh0SxjjTOpx73Y27_3-JdUvhHHX4mtKaREV3tl8qys9ZJ0BUizvweBZJ5SRrpQF6q1h3XAVrGU6WQrLwmS_gojfVbvr3M6Und6J9HIR9FlHRMzGo-SZvZnmMm2NOpdy_ZBj8HWBZEVwMFL7q-15XcqEmhYyGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان. مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.  هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/3127" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">با گوشی هم میتونید باز کنید دیگه اون Index رو
یکی توییتر پرسیده بودش</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/3126" target="_blank">📅 12:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه چیز جالب توجهی پیدا کردم که راجبش ویدئو بسازم. به درد خیلیا میخوره
ترکیب یه متد حال حاضر هست، با یه سایتی که اصلا هیچکس نمیشناسه. انقدر گشتم که پیدا کردم
برای VPN نیستش. برای دسترسی رایگان به محتوای یوتوبه
سر کار هستم الان، تموم که شدم واستون ویدئوش رو میگیرم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/3125" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OG_4DgMbgBfBE6sWyUuJ48_ndZdKG1-_ETS91fczE-3U5pMecu2N4gr4-PsnwRPtl_xJtsg9LlmahqeF1NCn59-qL54aC4gMX9Dngu4DBMafGiAr3ruJaQeWcgyUgqp9LBtnfr2_AAlMkhpLHniXYNLR3gZRWCgcdWxL7WTb5haYR6uz9hFPQGI0Vdwy7Kaz8k9DknpTCqcyC8LwCa4hciTSluYZLeHOZAlNvD571O0r0aXsDDSysY_RVywe_umLXBQBqV_YR8AFrknqqDloS_1lkAfjraVsIzE_ZRVd94GRf-Adk8p2fzZJ8qpsoMQsmPbZSWX4fhpMSv1xYoq4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LD_dtSodoSESRPctlBIDXWKYg87FPj0u78C3HNN_UgHWz8nB6VKBJb3uftsCjEXb3CMSYLXqU_2_DNrftTwuSIb_KmPKSRaoYjyXcU0yHb5fISXB9LrSE75ujh1ninegwp-scR6-5-gKOlKAobRBKcu-yJzOXAnLnbiu4jG8s2h2WmPI-oBFxvFHu2VgxxSbsnUk770sUSnVa5j5Z8Z2gjDwbRrJ2DB5OuY8OtNJl7FZ0LF9hMegxtZ1Pj3_vHyZ6WHTgf0ONlIBfAEXFMHvSQd22oEQCM--F46vPZ4g3rzcs3nVeyj99Xu_CjrmZmEFRJv5oVEe4AaVPNsetpngzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فایل رو روی سیستم Extract کنید و بعدش راست کلیک کنید روی index.html و Open with chrome رو بزنید</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/3123" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">cdn-ip-finder-main.zip</div>
  <div class="tg-doc-extra">723 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3122" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/3122" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fle2obtsP6JjOfJ-QZx4Htni99J49wOj1isKwVPPRDH26R6nckE3tHuGLpJezcrrojfjUSljTJopFLrf-OZa65g-MfTrdTZscKcrLvHHEmaKOAo5rX3Ae1czNBIWCQcscq_WRzgk2YZLTKlBm6liQMNoHGXYF-DPB7rFzT6umls9Pk6hqEIFuL9rdmjQDA0s405Ffz6Bg_3F02v5WIjuQc8FN3yiP9p2HdMR8H1_0A5McrttfRkpRb_NhspUiQe_bs_tj0EhLSvOQBzgz42ThD9T8-h9GmKH9rNg8e53k_-_s6bf3lKLHFt2HPewf5hIIK8zsWPBkHLZhNMgAKHjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر اسکنری که دیروز توی کانال قرار داده شده بود رو برداشته، و توسعه‌اش داده و تبدیلش کرده به یه اسکنر پر و پیمون تر. این هم پروژه‌اش هست:
https://github.com/hossein8360/cdn-ip-finder</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/3121" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3120">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایرانسل:
95.100.69.108
104.83.5.203
92.122.166.146
104.66.70.133
104.121.0.17
104.83.5.65
92.122.166.168
104.83.5.82
92.123.104.67
104.110.191.57
92.123.104.7
104.109.250.232
96.16.122.74
23.40.63.69
23.73.2.161
138.201.54.122
144.76.1.88
94.130.33.41
95.216.69.37
185.137.25.214
94.130.70.160
94.130.50.12
37.255.133.30
104.81.104.13
92.122.73.138
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
92.122.166.141
104.83.5.216
172.237.127.6
104.81.108.10
23.73.2.148
81.91.145.2
65.109.34.234
81.12.72.218
185.143.232.122
96.16.122.66
88.221.168.138
92.122.166.175
96.16.122.82
96.17.207.149
96.17.207.151
23.220.113.51
5.160.13.85
142.54.178.211
63.141.252.203
96.17.207.135
2.23.168.144
2.23.168.254
2.23.168.250
2.23.168.96
2.21.239.29
184.86.103.210
23.36.162.202
95.101.29.30
2.23.170.80
185.200.232.16
2.16.245.188
95.101.23.82
185.200.232.34
184.28.230.87
2.16.19.136
2.23.168.174
50.7.5.83
2.23.168.47</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/3120" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3119">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/plQUwuPTBCLAuUhiySyMqxXjpGkEUPyL0DChPO_Vk6SlvQnproV3O5sQ_Oe8YW9kRI68k-t1Zb3daOPOol8J0fsa6xGN1V_k4BYa27r6O10cZHYUDc87mW3drdR5PCSwxWI-qEbJ5aHdIr7dsSMg5SCcWarvXpjSSyb7sgmScGn9NXE_vj1NPOHHSe2EpbPQPNeG4y2TmYtAqgvUpFhy5CgnG0LYFK4Ttqg72KsYr5j-fw8GAgMzWtyXDfALa_5vpjQJ3MiTPAawK7pjawUvczusH9uEp4BOmBcxCilCEbEHq41OFf0lukUKUvWoy1kQfe-P__hjxi07e6JjNdWgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینطور تغییر APN به
google.com
رو هم امتحان کنید. گویا روی ایرانسل بیشتر جوابگو بوده. من خودم روی همراه اول فقط با همون لیست آیپی‌هایی که دیروز گذاشتم وصلم به شیر و خورشید</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/3119" target="_blank">📅 10:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3118">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یکی از دوستان این نکته رو گفته بودش در مورد وارد کردن آیپی‌ها:
من چندین دفعه هم با سامسونگ هم شیائومی تو برنامه مهسا‌ان‌جی امتحان کردم
و یه چیزی فهمیدم که خیلی عجیب بود اما درست بود.
هنگامی که آی‌پی ها رو پس از اسکن، کپی می‌کنید که داخل برنامه وارد کنید حتما باید آی‌پی ها هرکدوم یک خط رو جداگونه داشته باشن
اینجوری مثلا
20.68.81.211
20.63.74.811
و اگه جداگونه نباشن و مثلا اینجوری کنار هم وارد بشن
23.96.52.41
86.52.17.76
و...
برای من متصل نمیشن و این رو امشب فهمیدم و با برنامه MahsaNG از سر کنجکاوی امتحانش کردم و در کمال ناباوری جواب داد و متصل شد الانم دارم آپدیتای گوشیمو انجام میدم.
و برای این که بدون زحمت خاصی جدا جدا هرکدوم یک خط رو در بر بگیرن، پس از اسکن کپی کردم، تو تلگرام ارسال کردم و از تلگرام کپی کردم و تو برنامه وارد کردم و درست شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/3118" target="_blank">📅 09:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3117">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3117" target="_blank">📅 00:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCIMkhKEWu2kTrgoL0KzV5n4-q05qxfBj4jQLvvDqqWHgwHmkh5cnvtyhTefhi3tdUtqWe5dha0rgtEn0n9MnSklBOE11HLxSW_j-tX9fJyjNlF933_417O-mmk4Z4BqVsWASjxSapzN-Kr8JnEKr8Y8GDG_LT9hRkxSOcwQBkKH9NdY-EB_UHlfqI2eVphQY6q0SKg_LvWWTPu37qYMtlnK5qhzStKd-nWcYyMFtIQBO0CqHK7GasDmxb-FccdWC27m9EmrBYnOMKXLQBE04qIEtQYReDNKH501WAMIv7ZBM_14SRJIvQqHMm61Ph5T5lIDuqWzgv6Z6CICd91rFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جدی جدی روز جهانی ارتباطات رو تبریک گفته
😐
تمام آدم‌هایی که شبا گرسنه خوابیدن و پول اجاره خونشونو نتونستن بدن و به فکر خودکشی بودن به خاطر اینکه کسب و کارشون نابود شد سر قطعی اینترنت از جلوی چشمام رد شدن</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3116" target="_blank">📅 23:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حس میکنم ضبط کردن ویدئوش ارزشی نداره زیاد.. خودتون اذیت میشین
اگه تا فردا دووم آورد می‌ذارم واستون</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3115" target="_blank">📅 23:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3114">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حدسم اینه تا صبح بیشتر نکشه که ببندنش متأسفانه. بله آخه دست خودشونه طبیعتا.
فیچر تماس تصویریش رو به راحتی میندازن سطل آشغال. یه ماه تمام کل دی ماه تمام اپلیکیشنای چت بسته بود اگر یادتون باشه</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3114" target="_blank">📅 23:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این ریپو رو هم چک کنید. متفاوته:
https://github.com/theermia/BaleTunnel</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3113" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3112" target="_blank">📅 23:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3111">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
این VPN بر بستر ویدیوکال بله‌ست :)) یعنی یک نفر بیرون از شبکه محدود یا روی VPS نقش Creator رو می‌گیره و تماسو می‌سازه، کاربر داخل ایران به‌عنوان Joiner وصل می‌شه، بعد اینترنتش از داخل همین تونل WebRTC/تماس ویدیویی رد می‌شه و از سمت Creator به اینترنت آزاد می‌رسه.
https://github.com/kookoo1sabzy/BaleVPN/tree/main
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3111" target="_blank">📅 23:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">thefeed-android-v0.18.10-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3110" target="_blank">📅 23:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3109" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه‌ی جدید نرم‌افزار TheFeed برای خواندن اخبار کانال‌های تلگرام در شرایط قطعی اینترنت(کل جنگ با ریزالورا وصل بود)
کانفیگ‌های این اپ:
@thefeedconfig
لینک پروژه بر روی گیتلب:
https://gitlab.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3109" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3108">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eEvIWg_hbLqkWGohtMNTyQlyYntOfPcwbFF7P7nfQ1Kk3cg1ck4UlXe5IbPUym-XSX6nkFcyt_XODAJ5X6iOS2CdJlOIqWRsPIpZRstsGl7FEBHAzi7nUHWF1mytntCGO3C4yFAG60q4VfgmKnxCf_1GogtN7lQdYY6g28wJoDbB-s7F5MmdZWjmG4zcBmFJkAc3Si9vFJxJoFsgPwsJW1v7U7rUEXw995HReIpSNqjomBIN7_O1dm2vWiLFz4lNZxUncwXzmysItyqCM3nX0sqpmXTzTJdZ2YWSaGBs9DYlPELId0AG-dacDWKvXHTue4A8YL2ymHlfxAZE2rD9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیزاین با ai
:)))
دیزاینرای حرفه‌ای هرچند قرار نیست بیکار بشن. مخصوصا UI-UXکارها
آیدی طراح(پرامپت‌نویس؟!)</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3108" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tUlG-WG6YKCYIn246u36FexESWRXxHRiYDEN7AgRFZSET9PhosotU9IdPdqcEeJP-taK2TFD_VOkcWAzuVDD0fPsHcRyhLxCCFRrcwBjHmBQyd_lRDWYcll2rp4mxCdrGOaufgGw7HbwwvRuHkdUt6vtifJXV-9S8FcLVLWhF5YrpC5Yw3C3Jj2tcoIBKhqXzZoolNyuu_AjWFV2lM64R1SHIeZ92agMMtMSOHKWVAgZ64AgBnW2Py8i2xDeNwSqT93HZJj9zFfQN0pp1BBSkC9Ru5-u7t0oypgsHlfvACh_bVH-1J_8BE1IifTDWc2OPhiF-CJOGqG6GoX3gabVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این اسکرین شات فیک هستش و ساخته‌ی دست یه سری از VPN فروش‌هاست. یه دور بخونید از روش میفهمید یارو خیلی هم عجله داشته
🤣
لذا خواهشمندیم زیرا</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3107" target="_blank">📅 18:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">CDN-IP-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3106" target="_blank">📅 16:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3105">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iXN5pmX8rmmTp3AAt7L6oDiNHXY_2qpmM5lX0Zn_Et2VGTbEVU1bxBasJFMvtPoEsm7Oi87yjSRKV8fLB7IvS5X8Z6_cxg4IJ7flSJ_M1s3wT80UAVxvOJScGBs7_5ZtXjI2Us6aStwrwX_VY9otbc8h32_ZQ5_fADuCtpYKoN97g1dpYr_yPk92U-HqEYruOnXfI17Yx4ckIFxRuPxJssP5eMgfpnrxIczu0NKgAa1OF35vF3iV-rmWNeCWd3CHzzAPHvrEzAFbQyfSf0nehTSL4hKQM9AwV8B11qSWpHk6jyW3dVkYRvP5aG6SibzmCos4hP25D5tPPMTElxi93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچین موردهایی رو زیاد واسم میفرستید دوستان.
مسئله‌ای نیست؛ من که چیزی رو اختراع نکردم که زده باشن به اسم خودشون
😁
صرفا زحمت جمع‌آوریش رو کشیدم. منبع هم نذاشته، نذاشته. مهم نیست که.
هدف، وصل شدن مردمه</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3105" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN-IP-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3104" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">هرچی آیپی CDN و ... از اول اومدن این متد توی توییتر و کانال‌های تلگرامی گذاشته شده بود رو جمع کردم، دادم AI تکراری‌هاش رو پاک کرد و واستون گذاشتم توی این فایل تکست. یه تست با اسکنر بکنید و بذارید متصل بشه.
صبور باشید
!</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3104" target="_blank">📅 14:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو. بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید): socks://Og==@192.168.1.147:46597#ShirOKhorshid…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3103" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MahsaNG_16_arm64-v8a.apk</div>
  <div class="tg-doc-extra">59.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش اتصال با آیپی‌های CDN از طریق نسخه‌ی جدید MahsaNG:
1- وارد نسخه‌ی 16 میشید(نیازی به هیچ کانفیگی نیست)
2- اون بالا روی حرف F میزنید
3- گزینه‌ی Psiphon Only رو روشن می‌کنید
4- روی Psiphon Setting کلیک می‌کنید
5- بخش Protocol رو می‌ذارید روی cdn_fronting
6- بخش Aggressive رو قرار میدید روی ON
7- توی بخش CDN Fronting Settings، آیپی‌هایی که من بالا واستون می‌ذارم برای هر اپراتور رو قرار میدید
8- روی Save Psiphon Setting میزنید
9- برمیگردید به منو اصلی برنامه، روی دکمه‌ی گرد پایین سمت راست(اتصال) میزنید
10- یه نوتیفیکیشن Psiphon tunnel connecting میاد بالا. اون وقتی تبدیل بشه به connected یعنی وصل شده
توضیحات:
1- نسخه arm64 برای اکثر گوشی‌های 2020 به جلوتر مناسبه
2- نسخه arembi برای گوشی‌های قبل 2020 عموما
3- نسخه‌ی universal روی هر گوشی‌ای نصب میشه فقط حجمش بالاتره چون تلفیق تمام نسخه‌هاست اما حجم نهایی نصب شده روی گوشی شما همون دوتا بالاییه
لینک‌های داخلی:
1- نسخه arm64 داخلی:
https://guardts.ir/f/ee1f60ae6d33
2- نسخه arembi داخلی:
https://guardts.ir/f/9d474d75a4fb
3- نسخه universal داخلی:
https://guardts.ir/f/7af85b518302
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3100" target="_blank">📅 12:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompng(Asal)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.html</div>
  <div class="tg-doc-extra">21.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3099" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
اسکنر سبک آیپی برای شیر و خورشید
-فایل بالا رو با مرورگر باز کنین
-رنج آماده آیپی رو انتخاب کنین(با میتونین دستی رنج‌های آیپی مد نظرتونو وارد کنین در بخش لیست بازه /ip)
-بدون وی پی ان اسکن کنین .
-لیست آیپی‌های سازگار با نتتون در انتهای صفحه در دسترستون قرار میگیره و میتونین وارد شیرو خورشید کنین.
@p1ctok</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/3099" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=KVNCHbalY40y05TLwdOcnRzv-FdeDm6hzeU2rsw8vVD9xnW12SNT1at0GvDbRl-Mq3J5wzJDpFDv4LAPOmmmGCr82YNhwJ0OQ11Y16AGg1U0quyVEZInPWqLnCUcR0zhCTeLJZ64Pq_ZAl54H9N4ZQOuFQrmzNYmsYs7dHeYJoakHd23I_xIu68esZKfjS7_FZYjOoBRlE9QN31qK5Ke0DUZTsiaMc1IqsiFCXS9hiNJB_PKElc1BH9hY_vPYuPCS30NLt4B0zLFCrUglCFDOyDnqYnPi96VYLfkpDyXPjwjjyPfBIBbgR-fGOM_cqsaIPGiBsIZwzO90dSlX9DwUovMYy7oNl4Z3Eba4XSJXfuBE3o4QDeqMdoB5ZS5w7oRiDAhncjbehZmL5eGl2peLqhtDrf7XfiVQB0mU1DXujXj14aaSneMzpGOV3gz7vYseShVgH5CbXalif9XAXf6GQufBGQ6IaoeeJ7tOFbxSZhqS9E-5y-vgOG1eLiamsYWMEXn1vgGFNNVAh7lGzOubaihHFeVitJwdvLwDma4byso-J32TVpjKdx8zGWuUwUPhbn4yKUTH3gZC9oRqR_VO61pB924PgEo2TZ7TJ9cpaqDm33ub6XDbBg-5eF-kbs_71-EZU1eLkcVffGQ9BJK_HRbGcIJOP-VknaeygUR9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef65e3054f.mp4?token=KVNCHbalY40y05TLwdOcnRzv-FdeDm6hzeU2rsw8vVD9xnW12SNT1at0GvDbRl-Mq3J5wzJDpFDv4LAPOmmmGCr82YNhwJ0OQ11Y16AGg1U0quyVEZInPWqLnCUcR0zhCTeLJZ64Pq_ZAl54H9N4ZQOuFQrmzNYmsYs7dHeYJoakHd23I_xIu68esZKfjS7_FZYjOoBRlE9QN31qK5Ke0DUZTsiaMc1IqsiFCXS9hiNJB_PKElc1BH9hY_vPYuPCS30NLt4B0zLFCrUglCFDOyDnqYnPi96VYLfkpDyXPjwjjyPfBIBbgR-fGOM_cqsaIPGiBsIZwzO90dSlX9DwUovMYy7oNl4Z3Eba4XSJXfuBE3o4QDeqMdoB5ZS5w7oRiDAhncjbehZmL5eGl2peLqhtDrf7XfiVQB0mU1DXujXj14aaSneMzpGOV3gz7vYseShVgH5CbXalif9XAXf6GQufBGQ6IaoeeJ7tOFbxSZhqS9E-5y-vgOG1eLiamsYWMEXn1vgGFNNVAh7lGzOubaihHFeVitJwdvLwDma4byso-J32TVpjKdx8zGWuUwUPhbn4yKUTH3gZC9oRqR_VO61pB924PgEo2TZ7TJ9cpaqDm33ub6XDbBg-5eF-kbs_71-EZU1eLkcVffGQ9BJK_HRbGcIJOP-VknaeygUR9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
آموزش کار با اسکنر آیپی برای اتصال از طریق CDN با هسته‌ی سایفون اپ MahsaNG ورژن 16
این آموزش رو فربد عزیز زحمت کشیدن ضبط کردن و برای من فرستادن
فایل‌های مربوطه رو هم در ادامه قرار میدم واستون، و دارم فایلهای MahsaNG نسخه 16 رو واستون روی لینک داخلی هم آپلود میکنم</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3098" target="_blank">📅 12:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
): 184.24.77.42 2.23.168.213 2.23.168.174 2.23.168.7 184.24.77.32 184.24.77.5 184.24.77.7 184.24.77.16 184.24.77.36 184.24.77.21 2.23.169.111…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3097" target="_blank">📅 10:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تمام آیپی‌هایی که روی همراه اول جواب میده و شیر و خورشید وصل میشه(حداقل 10 دقیقه صبر کنید، بعدش که وصل شد دیگه خاموش نکنید
😂
):
184.24.77.42
2.23.168.213
2.23.168.174
2.23.168.7
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
2.23.169.111
2.23.169.105
184.24.77.11
184.24.77.29
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
23.40.63.69
96.16.122.74
104.109.250.232
92.123.104.7
104.110.191.57
104.83.5.82
92.122.166.168
104.83.5.65
104.121.0.17
104.66.70.133
92.122.166.146
23.73.2.161
92.122.73.138
92.122.166.141
96.16.122.55
104.81.108.51
23.72.248.214
104.126.37.185
104.83.5.201
104.83.5.216
92.123.104.67
104.83.5.203
96.17.207.151
88.221.168.138
96.17.207.149
104.81.108.10
23.73.2.148
92.122.166.175
172.237.127.6
104.81.104.13
96.17.207.137
92.123.112.7
96.16.122.75
96.16.122.70
92.122.166.182
104.109.128.153
104.96.143.134
23.73.2.141
104.83.5.202
23.67.136.200
23.67.136.202
23.65.119.52
92.122.166.236
92.122.166.234
92.122.166.237
104.110.138.190
173.222.200.5
184.51.252.36
184.51.252.38
104.83.5.208
96.16.122.146
96.17.206.214
92.122.166.197
104.94.100.73
104.83.15.66
88.221.213.81
172.239.57.117
104.117.76.40
184.51.252.4
96.17.207.30
96.16.122.83
96.16.122.150
23.73.207.11
96.16.122.77
96.17.207.155
92.123.189.82
96.16.122.82
96.16.122.66
96.7.218.219
96.16.122.137
184.51.252.157
92.123.189.41
184.86.251.12
96.16.122.154
184.51.252.152
96.17.207.12
23.79.48.162
151.101.0.223
151.101.128.223
151.101.192.223
151.101.64.223
65.109.34.234
142.54.178.211
2.23.168.47
2.23.168.96
2.23.168.144
2.23.169.207
2.23.170.80</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3096" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یکی از
بچه‌های توییتر این
آیپی ها رو یک ساعت پیش منتشر کرده برای شیر و خورشید. همچنان متصل
🔥
184.86.103.210
96.16.248.183
92.122.16.5
96.16.249.60
96.16.249.9
23.12.156.115
23.216.77.16
23.62.61.53
23.39.148.245
23.210.73.133
23.44.201.136
23.205.46.167
184.30.150.142
23.220.161.217
184.28.165.4
23.46.230.133
88.221.168.204
104.96.158.174
184.51.252.4
172.234.199.15
104.85.26.14
172.237.145.27
92.123.103.24
172.234.159.58
185.200.232.43
2.17.100.200
2.19.205.42
2.19.205.50
2.19.252.134
2.20.169.70
2.20.170.91
95.101.111.144
2.16.245.188
2.18.69.150
2.16.106.4
23.58.222.107
184.25.28.31
23.47.124.134
23.50.131.147
23.46.190.18
23.58.222.147
23.56.162.186
23.44.203.68</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3095" target="_blank">📅 02:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دست از سرم بردار فیلترچی</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3094" target="_blank">📅 17:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3093">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گویا یک سری دوستان با تغییر LTE(4g) توی تنظیمات شبکه گوشی به 3g تونستن راحتتر کانکت بشن به شیر و خورشید.</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3093" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3092" target="_blank">📅 16:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEoJ4ra-QSp7jNFE55L3XJSDNF64yl1exQSS9Ty-oUhU9G-JrqIJ5z_6CHkQD-T3l2QHQdybWnCnqilf_Y8arz_OLoxueBywajqO53lDeEmi5SGp-JsUy3xZWlrI6LjR4qG717meBEhQLy9u4-kTSqidVNEPBRvyrH1MWwAvJ_E9kP85JOUtPWbVr1WMWtzosiWScOfg9oHMb4rq9lRmWKESTRI7nIqGgfh7PuhYZTEh-DUljTCCIz_Wunfy_wDUZXxOIdFICWuXVZktiT5U_88W_XcClKz-h4njj4ve4lZP999gARBud9ev9bk6inu_DHBkBsdbkEDSgTvpK3jOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره: 184.24.77.42, 184.24.77.32, 184.24.77.5, 184.24.77.7, 184.24.77.16…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3091" target="_blank">📅 13:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3090" target="_blank">📅 12:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این لیست رو یکی از بچه‌های توییتر واسم فرستاد و گفتش که از دیشب(و تا الان) روی ایرانسل با یه کلیک وصل میشه روی شیر و خورشید. اگر کانکت نشد، مجدد عرض میکنم که بذارید هواپیما و بردارید، آیپی جدید بگیره:
184.24.77.42
,
184.24.77.32
,
184.24.77.5
,
184.24.77.7
,
184.24.77.16
,
184.24.77.36
,
184.24.77.21
,
184.24.77.11
,
185.200.232.49
,
185.200.232.50
,
185.200.232.42
,
185.200.232.41
,
23.48.23.186
,
23.48.23.133
,
23.48.23.195
,
23.48.23.178
,
184.24.77.29
,
2.22.21.152
,
95.101.23.82
,
23.215.0.164
,
23.197.161.35
,
184.28.230.87
,
23.220.128.221
,
96.17.207.142
,
23.50.131.18
,
23.36.162.209
,
23.219.3.212
,
23.223.245.150
,
96.16.122.59
,
23.2.13.138
,
23.2.13.144
,
96.17.207.135
,
23.220.113.51
,
96.17.72.41
,
23.203.185.105
,
2.16.27.71
,
2.16.244.11
,
2.17.147.89
,
2.17.251.98
,
2.18.190.26
,
2.18.190.27
,
2.19.10.30
,
2.19.196.105
,
2.20.255.113
,
2.21.89.66
,
2.21.239.10
,
2.21.239.21
,
2.21.239.23
,
2.21.239.29
,
2.22.6.68
,
2.23.176.166
,</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/MatinSenPaii/3089" target="_blank">📅 12:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZOSMciVXrpFWTegJ2uWZxoTCKW7bsVTXVxnmJ0m96QZxhJynQeJg_rWvHRHK9NkLAbuZvmeLxRX0KHPIavrxlRX-oVaumaZUXF7t8nVTc2d2wcjJnVQ44eeIQ7PiOFNMVG_gXh6DSiRoVvR_yeUigJc9THEF7KYCg6LKqY6mEak7Z1LkfFqSaeWHvyN7VTs-bgHU1QprHRwb_TtoWSo_vruUhkHO71Ifgh1X8oVAqXMb3F9hD6yztWXUmB88wa9MSVztl3YxEg0sSzUOe46xIQmFa0-VYwZLm3zR9FHfkuZoT8Zg7IEEgiz8Rmj4tt37kO7NVb9hRsIBlP8dv5iYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر راس گلر
:
روی ایرانسل تست شدن، مناسب CDN شیروخورشید.
23.65.119.52
23.73.2.141
104.110.138.190
104.83.5.202
92.122.166.236
92.122.166.234
92.122.166.237
96.16.122.70
23.67.136.200
23.67.136.202
همینجوری paste کنید اوکیه نیازی به کاما(,) نیست</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3088" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nh02v3hRGLNcVYS-i92JyWX10sakvSng9dWE5oF7ruARgmQ5bAqpJjWAqdNDUWqACrON9Z9Rml0jyh9VXahGJuONLyH9MX3USU5gaIDhUKJjGrrDoSEo9YTnkdfITHdZETEqwFLLoflbKmEMifAar51yH8shFQj4rEi97-u_K8AO4S8TMRGavwGpcq5zrFbMqgwOV1Pt6qC25rTvFFgKKayPLXxWY34CPWHLot1NCfBeM4v_wC1UAOAQrsSewALr5nccCJvwDy6eLWX4Fv3kF2ZAq2GCLJS8Ce_WQNfRe15Bh-SGr29LD1ZGbATwD4vd7ikpLSjda8_lTYql3NrDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود اپلیکیشن‌های اندروید از گوگل پلی با اینترنت داخلی
از طریق این پروژه، میتونید ربات تلگرامی‌ای رو ران کنید که به راحتی لینک گوگل پلی شما رو تبدیل به لینک داخلی میکنه:
https://github.com/ZethRise/PlayDL
این هم نمونه ربات پیاده‌سازی شده:
https://t.me/APKNitoBot
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3087" target="_blank">📅 10:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3086" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینها رو یکی از بچه‌های توییتر جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم. آیپی برای شیر و خورشیده، بخش sni رو خالی بذارید. خیلیا تونسته بودن وصل بشن باهاشون: 2.16.27.71 2.16.244.11 2.17.147.89 2.17.251.98 2.18.190.26 2.18.190.27 2.19.10.30 2.19.196.105 2.20.255.113…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3085" target="_blank">📅 08:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینها رو
یکی از بچه‌های توییتر
جمع‌آوری کرده و منم واسه‌ی شما می‌ذارم.
آیپی برای شیر و خورشیده،
بخش sni رو خالی بذارید.
خیلیا تونسته بودن وصل بشن باهاشون:
2.16.27.71
2.16.244.11
2.17.147.89
2.17.251.98
2.18.190.26
2.18.190.27
2.19.10.30
2.19.196.105
2.20.255.113
2.21.89.66
2.21.239.10
2.21.239.21
2.21.239.23
2.21.239.29
2.22.6.68
2.22.21.152
2.23.176.166
23.2.13.138
23.2.13.144
185.200.232.50
23.2.13.152
23.2.13.153
23.2.13.186
23.2.13.201
23.2.13.227
23.33.126.163
23.36.162.196
23.36.162.198
23.36.162.202
23.36.162.208
23.36.162.209
23.36.162.215
23.37.197.128
23.37.206.186
23.38.49.97
23.39.249.249
23.40.63.69
23.41.37.129
23.44.10.10
23.58.222.147
23.59.235.208
23.60.69.118
23.65.119.52
23.67.136.200
23.67.136.202
23.72.248.214
23.73.2.141
23.73.2.148
23.73.2.161
23.73.207.11
23.73.207.16
23.79.20.249
23.79.48.162
23.192.46.51
23.192.237.208
23.192.237.209
23.192.237.222
23.197.161.35
23.200.143.71
80.67.82.179
88.221.92.177
88.221.132.162
88.221.168.5
88.221.168.138
88.221.213.81
92.122.73.138
92.122.166.141
92.122.166.146
92.122.166.175
92.122.166.182
92.122.166.197
92.122.166.234
92.122.166.236
92.122.166.237
92.123.102.104
92.123.104.7
92.123.104.67
92.123.112.7
92.123.189.41
92.123.189.82
95.100.69.108
95.100.156.147
95.101.23.25
95.101.23.27
95.101.23.82
95.101.23.168
95.101.23.170
95.101.29.12
95.101.29.30
95.101.29.54
95.101.35.73
95.101.35.83
95.101.181.125
95.101.200.63
96.7.218.219
96.16.122.48
96.16.122.55
96.16.122.59
104.83.5.65
104.83.5.82
104.83.5.201
104.83.5.202
104.83.5.203
104.83.5.208
104.83.5.216
104.83.15.66
104.94.100.73
104.96.143.134
104.103.64.7
104.103.90.156
104.109.128.153
104.109.250.232
104.110.138.190
104.110.191.57
104.111.202.158
104.117.76.26
104.117.76.40
184.24.77.32
184.24.77.36
184.24.77.42
184.25.52.200
184.28.230.87
184.51.252.4
184.51.252.36
184.51.252.38
184.51.252.135
184.51.252.152
184.51.252.157
184.86.251.12
184.86.251.27
185.200.232.41
185.200.232.42
185.200.232.49</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3084" target="_blank">📅 05:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نمیفهمم چرا هر متد جدیدی میاد و هر راه جدیدی باز میشه، یه لگد به گیتهابِ بدبخت می‌زنن
انگار فیلترچی می‌خواد ما رو تنبیه کنه
😂
داره میگه دفعه‌ی بعدی گوگل رو هم فیلتر میکنما، حواستون باشه این سری عصبانیم کردین</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/MatinSenPaii/3083" target="_blank">📅 04:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طرف بله و روبیکا نصب کرده بعد میاد توییت میزنه که اپ شیر و خورشید(که اوپن سورسه همه کدهاش وسط گیت‌هابه) بو داره نصب نکنید امنیتش پایینه🫩
امنیت؟
با من شوخی میکنی؟</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3082" target="_blank">📅 00:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6hiEt_4HbDp_bxYrw_mBj355J2InfMPFlCX1a8lPskoD4Cnyb3zAEc6r8drq3sX-5qozvC0hKu7DxylkaRw--RFZfWpyZmRFQ3WjNKn0DOeYnjBCdLC1QdrAxoFb8QMU0zyLR9eys_dz7QYCjbrlAlH072dmcW1D16w44i5RWGwi3gfY_4a4QA-lNVeeJ5Iyej3u3RI7_tpHgsUTNHIf1Bj5bmykeYUfU-EE9-pqjAc1_fnqokhyuKR1hH_QElf7fDcDMZfcLXh_BUuJOaLpmISAGL0oljNgcOYsK9Y8UahLpxb3iLTtnw9vEYU8wAbFcnELUAguemTyOx1vYxUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62c2815606.mp4?token=vO2JwYAFyL2GNR3ZWFM4lu5oLTRlZfeMaB2PK1l4_JpGip7XlwQGLpmcgSDx0tNJg0gob1tjyNONn3HgF3VS1ILwk0_DEVSw47J3qnCM6zzFWxrbpS9jQU-RIm8dnd_jSTyzmXgQ1cxFf2UMdYx7Oxhqn1c1IGE6PW-JeJEFKumYuZoLqc_yiaUJk7_HmHFDS_6s_kyVkB7qdfQMI0yUNyfl84KZvUUXiMlo35oCYQohIqVN_6a35lWAUpGC7Mlo31oHUm5b3QBUbhIIkswR2ps73CQ8fBaYgaCrj8GvzbPrUFzvbaaiV1KcfDsj12T-WnvVu6sTCvJsXjTKa-U4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62c2815606.mp4?token=vO2JwYAFyL2GNR3ZWFM4lu5oLTRlZfeMaB2PK1l4_JpGip7XlwQGLpmcgSDx0tNJg0gob1tjyNONn3HgF3VS1ILwk0_DEVSw47J3qnCM6zzFWxrbpS9jQU-RIm8dnd_jSTyzmXgQ1cxFf2UMdYx7Oxhqn1c1IGE6PW-JeJEFKumYuZoLqc_yiaUJk7_HmHFDS_6s_kyVkB7qdfQMI0yUNyfl84KZvUUXiMlo35oCYQohIqVN_6a35lWAUpGC7Mlo31oHUm5b3QBUbhIIkswR2ps73CQ8fBaYgaCrj8GvzbPrUFzvbaaiV1KcfDsj12T-WnvVu6sTCvJsXjTKa-U4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چیه درست کردین
😂
😂</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3080" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبر خوب:
نسخه‌ی اولیه‌ی WhiteDNS برای IOS منتشر شد:
https://testflight.apple.com/join/GfUqXrFz</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3079" target="_blank">📅 00:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش: https://t.me/MatinSenPaii/3070 کافیه که با کاما(,) پشت هم وارد کنین:  2.22.250.149 23.58.193.140 23.48.23.151 2.19.126.81 23.202.138.125 23.43.237.239 104.112.146.82 23.2.13.136…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3078" target="_blank">📅 00:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این آیپی‌ها رو موفق شدم از سرتاسر توییتر جمع‌آوری کنم برای شیر و خورشید، این بخش‌اش:
https://t.me/MatinSenPaii/3070
کافیه که با کاما(,) پشت هم وارد کنین:
2.22.250.149
23.58.193.140
23.48.23.151
2.19.126.81
23.202.138.125
23.43.237.239
104.112.146.82
23.2.13.136
72.246.28.37
2.18.63.49
2.16.53.11
2.16.53.50
2.16.19.136
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.8
185.200.232.43
185.200.232.40
185.143.232.122
185.200.232.9
185.200.232.11
185.200.232.16
185.200.232.17
185.200.232.19
185.200.232.24
185.200.232.25
185.200.232.26
185.200.232.34
185.200.232.40
185.200.232.42</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3077" target="_blank">📅 00:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3076" target="_blank">📅 23:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oqMQwOfuKK68Z4Y96QP3TxTKIJtMkU3x4XT1M2bv_6dkpTBLuaUOWaLCFwgTI5677zGv_fvaTcliSV64x2n_Xof4mhlujsQQMR4jJ1pxNgfYKLL81s7SytnRv4HBwsc_g0mkLLJcKRuzCBBNEh5Pj-EhkLUHRIvQUw8J0TyNmFoXeLo_lA6pAIuarUUbU2vNLhBcXkAB5jv7TA_5HyScxhhGv-JzJBRvp3umLwJ8YvHcFbzJBjKfNsehEoswhTXd1E8yRWneBalVMxp53Yc88wTi_n4TPVKTfKQdlkvBAXGII6zfZZ7ks_otzr4xyMw10DzEebZVwJSKyKpLeMQ6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I1QB_dbh0dqVAAQ6pFDimoSmKD2BlLFxa6lGlpU_KPhPLai7P9EiYoxToFzut7jz1LQkBFk93llJtQK2nHgrXYzS_oJs0wmeITysZafhWJNRJjdmOjoZDFJhRuBE3Mqk4oKLy1gKIDWDTbhHAnkUUREYeRXB2Ep_NGVaA7V08KjnFOerTX2f40nNEXsnnyE0yOucE_wcjMvMSTY7WnOsrTpH3U4bo8RdofWGDm7A1NKXzQG9gYKebxFAfkqmjhBbn-qlG-lfbENBqcLQnaw2SZu6brUn6TfT36tyavvvIVNUjTOxgrnz3Uo13-Xqh9d8nthXRTx6LHVLiGMOkpsePw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر با شیر و خورشید وصل می‌شید، گزینه‌ی Share proxy on network رو فعال کنید. سپس به یه WiFi وصل بشید و کانکت کنید VPN رو.
بعدش با هر دستگاه دیگه‌ای اگر این کانفیگ رو بزنید(با توجه به عدد و پورت خودتون تغییر بدید):
socks://Og==@192.168.1.147:46597#ShirOKhorshid-MatinSenPIi
و توی گوشی آیفون(با Streisand)، مک‌بوک(با V2Box)، و هر دستگاهی که کلاینت V2ray با پشتیبانی از Socks داره می‌تونید وصل بشید.
خلاصه‌اش:
ببینید، گوشی A رو داریم که اندرویدیه
گوشی B رو داریم که آیفونه
حالا دوتاش رو به یه مودم وصل میکنیم
روی گوشی A شیر و خورشید ران میکنیم
میریم توی V2box اون کانفیگی که دادم رو(با آیپی شخصی سایفونتون که توی صفحه اصلی وقتی این گزینه رو فعال میکنین نشون میده) وارد میکنین
و میتونین عملا به شیر و خورشید گوشی اندرویدیه با گوشی B که آیفونه، وصل بشین</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3074" target="_blank">📅 23:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v6mNE5cJNGWWg2KeIaHZqFj-Er5aFkZYfJP4fXdcDpWsLEWPIe9lZedWZBK-INgTtcuZbwfEXhXoKU6rBzyFIaF_DSbIMuV4c_VWOtGcSSVu-cb1wEhqsAgKJogsjV-ZPv-ZKk_wT0pEhOKdlf5dXZG1DGWjv9Z_VvuEeNnzIgdhmBxVyGXIns7y3CJliviQWfQw4qzb6MFYjacppN_XULWkHFTbNGL7DlpfpMRDBlM-RH3KYP_5_c0ApGMLEL3g86LnL95WTRywwBtNfRyAUmmPRc-FS-couPL9d_o5eS4ZRdVYQ-vKG-Jpd9Owqpfe2S6HSpD64excANrkqyismA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
‏این دوتا هنوز وایت لیست هستن، چک کنید ببینید میتونید باهاشون وصل بشید یا نه.
sophos . com >
185.200.232.27
,
185.200.232.16
> Akamai
www . mathworks . com >
2.23.169.12
> Akamai
برای mathworks حتما www بذارید.</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3071" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jw1dD7nWQVAElM7mOhcQX377Z6G5oVr0PDsLxxjPhtQlcDnOKYX-AP1Ck2RErrSiZ1yqKj4ieSgCkZnGXjb0lp6cxBM1j0TcXmXeBHAv7hD6nT19NkUhFAdrzzADOYcnPNHt_2vbmaD9GCyOkPepkqsM8vS72HlkDAWyc4vwv1i9NvgLy54d4_EObBg_Npul4BwFE7Pb4McZQNXkTUjConF2opNeKXJh2kDNHCRjFrOu-e36D1N9SA6SF05M5_HEMpmnCOhzsqm3wL73CSQiICrQSpOkqFaC-wlaIrBXHjiKgE8jVhZlYjK2owzCj9wItEHliarXc3j_Wv4nlxvX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر روی ایرانسل با این دوتا روی شیر و خورشید وصله کاملا اوکی:
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org
‎
توی همون قسمت More Options هستش</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3070" target="_blank">📅 17:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-MatinSenPai.npvt</div>
  <div class="tg-doc-extra">3.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3069" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3069" target="_blank">📅 17:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Umf_UA47U0ht2Y-FBK5LZM3kwhnsAQ82VEtUH-BcdzlEcOdvPTNvpc2oezDVod_C9FDdarhhTJwwpCxxmV4IwXTxqFRW_A62aCYAiIWVhGmPXOZggSa4ojqxHR0xA043vGhtre8PTLMsSDziqlVmR7RKtIJNC92CJoWR210o-jDdKMFvt_7N4ulw49ssJi1IjAGzzRnk3JwuqkGsfb3Lfd-jElFIgBCR9sBs9RZ5XIzR3GLJBtuf97aHv7_j8Q_qMCApKxFSMpugZDjciTc5AHUK8ewrKewsx1pMIr95zWyE3dlERgKvluFz4502qymjZMORcl98Xfa-Z6_8ry6Zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود راحت‌تر پکیج‌های Dart و Flutter
وقتی "
pub.dev
" کند یا ناپایدار می‌شه، PubYar کمک می‌کنه پکیج‌ها سریع‌تر و مطمئن‌تر دانلود بشن.
پاب‌یار فقط یک mirror ساده نیست،
مسیرها و DNSهای مختلف رو بررسی می‌کنه و بهترین راه دانلود رو برای "flutter pub get" انتخاب می‌کنه.
مناسب توسعه‌دهنده‌های Flutter و Dart
PubYar.ir</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3068" target="_blank">📅 15:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گوگل من روی همراه اول یه بیست دقیقه‌ای بسته بود.
نمیدونم دارن چه گندی می‌زنن باز</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3067" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vpRY-MfJZW4LTbN7rE0PqyU2yi6ldQNsGyIiyZYLquxXTY0VDFVdl9Kd1BTN-4NK5wtFyL3G_S6gAgA8JcL-75JQcPbb-WyoEukKq_-cbpBrkheDAbRLFbIL59A9hrWye6grqrPuPSdFisF5pl7PARePmn52pCEqB_XjZ2PRtCgXsYaLcD3Hddg3Aoi23p5rN1LaCfmPH3d6hONnNYiv7CfmkHvFvd10bULlb54WErbt-RUsaQXwlj64vVboPRZi4tS-fD3RY3_lzx_YrsHg2lq4SxzQRLqsQQ02EOPYofogXUzCqcopM8lGxQdEVa1hZvth8kGN2biOwFDDAUvEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k7uL-KQz_xR2TvIHxP9D0fr0h7pfLmHFr9jrb8Sb_HskBIh2e-MRg-HMCbxioo2OfJMWEjtsxB6XXqd3gwW6-sGeyZf8F7Hpv31VWqC1FCJ2Q0xLPmBRlUNyqSKO1VXbAI6aEvWGM2f7HvWNUb9gqd6F0Z52ZY24b0SkbKBu4cArI1j5o5SVte6RP-unw-7EDCUgmw8kHdM5JnkzN-GuBs8Bh5YjOpcMkXj8SAmmngN1Ge-U8bXkkklryJA5qfKru0g2GbzlJeVZ4eiZRKLVsuAn_WK78a6RFvBR0nW1fyRppN8SdxwJ7Qb6jzk28qm3ecSk61mArWUnUl0LGZ_FzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور رایگان</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3065" target="_blank">📅 08:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3064">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ورژن جدید White DNS با یه سرعتی ریزالور اسکن می‌کنه که آدم باورش نمیشه</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3064" target="_blank">📅 07:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3063" target="_blank">📅 06:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">masscan.rar</div>
  <div class="tg-doc-extra">1002.7 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3062" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم نسخه gui مس اسکن خیلی کار کردن باهاش راحت تره
قبل شروع اسکن باید winpcap-4.13.exe نصب بشه روی سیستم(سرچ و دانلود کنید از گوگل)</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3062" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3061">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai.txt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3061" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر بسیار پرسرعت Masscan برای اسکن آیپی‌های Akamai:
یکی از دوستان این رو نوشته و خواست بدون انتشار اسمش منتشر کنم این رو:
متین اسکنر سم و پینگ خیلی کندن
از masscan استفاده کنن چند هزارتا در ثانیه اسکن میکنه، من راحت تو ۵ ۶ دقه ۹۰ تا آیپی پیدا کردم
دراپ ریتش ولی رو نرخای بالا زیاد میشه.
کپی از چتای خودم:
چجوری اسکن کنیم؟‌ اگر masscan داشته باشید خیلی کار راحته صرفا این دستور رو بزنید:
sudo masscan
2.16.0.0/13
-p443 --rate=500 -Ss -Pn
جای اون رنج هر کدوم از رنجای زیر (رنجای آکامای هستن) رو میتونید استفاده کنید:
104.64.0.0/10
23.32.0.0/11
23.192.0.0/11
23.0.0.0/12
172.224.0.0/12
2.16.0.0/13
23.72.0.0/13
172.232.0.0/13
184.24.0.0/13
23.64.0.0/14
ریت هم می‌تونید زیاد کنید
https://github.com/robertdavidgraham/masscan
این خود پروژه
ویندوز هم داره
کل رنجای آکامای هم اتچ کردم با فلگ
-iL
میتونی بدی بهش
همشون رو هم ۵ ۶ ساعت بیشتر طول نمیکشن (خیلی زیادن)</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3061" target="_blank">📅 01:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-fastly-1.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3056" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چند کانفیگ سایفون‌هلپر متصل.
تمام اینها صرفا با تغییر ip یا sni در کانفیگهای
force-fastly, force-akamai
که در
https://t.me/projectXhttp/354790
قرار داده شده بدست آمده.</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/MatinSenPaii/3056" target="_blank">📅 00:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">برای اسکنر آیپی که خیلی‌هاتون پرسیده بودید دایرکت، ساده‌ترین راه اینه توی ترمینال(چه cmd ویندوز چه ترمینال termux) بنویسید
ping
20.20.20.20
(آیپی مورد نظر)
حالا اگر اسکنر هوشمند بخواید، میتونید از پروژه سم استفاده کنید که اصلش برای کلودفلره، اما میتونید کلا لیست آیپی بدید اسکن کنه:
https://github.com/SamNet-dev/cfray</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3055" target="_blank">📅 00:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یکی از بچه‌ها(abol) گفته بودش که:
از وقتی سرتیفیکیتو نصب کردم رو سیستم
دیگه نت سیستم به کل قطع شده
هر چی میگردم راهی برای حذف سرتیفیکیت پیدا نمیکنم
و این شکلی مشکلش رو حل کرد:
ریست شبکه در ویندوز گاهی همه فایل‌ها رو پاکسازی نمی‌کنه. این دستورات رو در حالت ادمین امتحان کن:
توی منوی استارت تایپ کن cmd و روش راست‌کلیک کن و Run as Administrator رو بزن.
این دستورات رو یکی‌یکی وارد کن و بعد از هر کدوم اینتر بزن:
netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
در نهایت سیستم رو Restart کن.</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3054" target="_blank">📅 20:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/3053" target="_blank">📅 20:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان من، خیلی ممنونم بابت حرف‌های پر از مهرتون
🥰
خیلی خیلی زیاد خوشحال شدم از دیدن اینهمه پیام‌ زیبا
🌱</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3052" target="_blank">📅 20:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم. تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/3051" target="_blank">📅 19:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب گویا آی‌پی دیفالتی که پشت جیسون بودش رو زدن. مجددا موش و گربه بازی سر آیپی و sni تمیز.
Pypi رو زدن،
خود
python.org
بذارید باید اوکی بشه. همینطور از آیپی های این پست استفاده کنید:
https://t.me/MatinSenPaii/3040?single</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/MatinSenPaii/3050" target="_blank">📅 18:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگر حمایت‌های پارتنرم نبود، مدتها پیش سلامت روانم رو از دست داده بودم حقیقتا. و اصلا بعد از دی‌ماه نمیتونستم هیچ کدوم از آموزش‌ها رو استارت بزنم و شاید از مبارزه ناامید شده بودم.
تشکر ویژه از شما، بانو
❤️</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/MatinSenPaii/3049" target="_blank">📅 17:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zhn-nSIIECSQxUafYZWtOxU19jaPi9RQODXek9kBXq1ALxTwdRI4Ar7O6PqTnlhYzTiALDmNhyQIzQRrRsDGPoTnHhLSr5FwhS02Qd6AdTG1S8s_x1VKm-4oMQVqjSv_AuXqxPkVlPf9MK1nopdkXBGhaI0u3pXW9lqkZEcrFDlh4kzka1IwUVQ1JEr_JtlCmb9F32DgntWaSJgisX588sTc8owRj6HFyr8yfnlfeYvp6XtLQU3BCwTy4KufmQ1UKObg9Dn9H-9ssCpjbUvYUV1n2Fx1yanPcQ-ZyjgOZr-v7KpLrjyNZJv9bWp7XrxclUNHAYEJQWM4s7Ino5xa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Kharabam
:
وقتی رو سایفون ویندوز upstream proxy ست میکنید دیگه اجازه انتخاب لوکیشن نمیده برای دور زدن این محدودیت ریجستری ادیتور رو باز کنید برید به این آدرس
Computer\\HKEY_CURRENT_USER\\Software\\Psiphon3
و EgressRegion رو ادیت کنید و Value data کد هر کشوری که میخواید بهش وصل بشید بذارید</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/MatinSenPaii/3048" target="_blank">📅 17:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگر به ارور Upstream proxy میخورید، یعنی پورت رو دقیقا اونی که توی ویدئو گفتم ست نکردید. یا توی بخش مناسبی نزدید. باید مو به مو چیزایی که گفتم انجام بشه دوستان</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/MatinSenPaii/3047" target="_blank">📅 17:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روی ویندوز از این آموزش استفاده کنید:
https://t.me/MatinSenPaii/3035
روی اندروید مستقیم وصل میشید با این اپ:
https://t.me/MatinSenPaii/3038</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/MatinSenPaii/3046" target="_blank">📅 16:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Matin SenPai
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3045" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsNccet5BP-F4fzEeB-LoG5RAAmOShAhjnu-kentWGzOwc72lGIKA9IxPm5XL5tR7u32zIeAF0oWb8SY2E-BWI22GuxG0J0AWIAVOn2F4MAIL99P2sEnBjBgI0iGZGCDUnhXKKJRNXReuvbPwapDh2b7OZHQaMqj1-DIFMbQFHO16vNBP0ghNcA6EUhifm6xGm20ZI-Fz51v_0QtEm7dADHgntJPkDoZJaYxkSwLYnYgXYQNFazfO0ruSFr1ARQKhagfXq-heLj3TUBbh6ZGUwGy96zcjWqFiLFboIrJIj9Jjup7cMLGkHdAB4JVS4fpAGhpobTiCtiFtkxwd82HNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/MatinSenPaii/3044" target="_blank">📅 16:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3043" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hB_4GK3YMRzuShiIkucAe52Cmg_6uoeiuQwm7toEmgCv9x5b2T6DVhi53NCtAgFozNz747YPfHJ0kOiXhsGyrd4iP1X7pq5QHye6Lflphgc6R_UwWf6lA7_TNH76Ko4MI7AWQhoKDBtvUwqKDdm3LgRnQRPBdCYvPoCcxTKAZYfweERwkwiC9mi__VYHIm19rUcicQb6AkVpTWyF1P4zXt8M9y9v17LkRb0n_wEuL0LKS-aeMHJ6548hhCuWlVpDfWg66xwnh5OpIZY1t7iOGxITccSAvkzZjVEBQfJhFzYqezWyGbyb5mjSc2E7xRLRWbe84oZ0A01m9c7eC1ZWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب ویدئو رو پاک کرد به علت محتوای خطرناک و آسیب زا به منم استرایک زد
😐</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3042" target="_blank">📅 15:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3041" target="_blank">📅 15:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PnDs0ZMmwtbr-lDk7rPryvRCPgsaxCbuLBD2W31NZVmEOTyspa-EqNe9cx_HOBTJrzPndnPauvNsANsfVCk0AH5vLMMNE7z4SJF_3a376jqHP0kBMm5AREZCW63RjnTivhsIB57fmCeQdp93Gs-slImSY3nnSi-Xk1eDuegELFj0OBbzPUDmLcvlHaJYDfRtkMjQbdlDZicNFdP9eM7yvmZZ5EYpzx1rOEvDK1bl2EdQbxsWuXSslrcNy8A31W9J3fyz6kFRutQIyTySinAOSFSIUTrIh35Kecj6Swocfja8xzyFu2D5nZ4alL9Zpv0WhVd2__25OEd2dcLtzDOyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MBF9fWZDd4owvCN96uosx69dPqT3YECbgVcqpVKYsjqA51qXdIFtjisWgA4S2LymxLja8IaTEFAHEULecUGrr-PLf7hLqR7I5u6LhQD-WB3E2fhptgRURUVy4_jYmHVBd1RjgVWeJr-J8ASywemnxFz38I65-9KabXc8VsYWNa5zDHTaYcMK1a19IF8hqK-CK2VjACZR0Vtp1RxrmczrCEQEDS2kpxdtG7M0-llXafT1jjjyGTP8Nrj79BGJxSsGKScuWDmMvZZAKdIh-bHa8ORGr_CSjBZ05uV9XizBtLeWPDVxIQ6QxnQYGH9NhCrcDosHhqBNG1Fopp41z5hBIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShirOKhorshid-2026.05.14.apk</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/MatinSenPaii/3039" target="_blank">📅 15:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/MatinSenPaii/3038" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حالا دیدین متد ترکیبی سایفون افسانه نبود و واقعا وصل میشد؟
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/MatinSenPaii/3037" target="_blank">📅 15:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان عزیز، خواهش میکنم به DNS بها بدید. معلوم نیست کی مجددا متدهای حال حاضر رو می‌بندن. از نرم‌افزار و آموزش‌های
@WhiteDNS
استفاده کنید و الان که اینترنتتون شاید اوکی تر باشه، نصب و ستاپ کنید</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/MatinSenPaii/3036" target="_blank">📅 15:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/MatinSenPaii/3035" target="_blank">📅 15:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چه حالی میده رایگان وصل بودن
📚
از زمان SNI Spoof اینو تجربه نکردم خدایی</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3034" target="_blank">📅 11:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بی‌زحمت لینک سایت‌های داخلی برای آپلود(هرسایتی که میشناسید اوکیه) واسم بفرستید، تا زمانی که ویدئو حاضر شد واستون همزمان به همراه کلاینت شیر و خورشید و فایل جیسون و ... روی چندین جا آپلود کنم:
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3033" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3032" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قطع و وصلی داره ها، اما هر 5 دقیقه، 10 ثانیه قطعه مثلا
برای گیم شاید عالی نباشه، اما وبگردی، اینستاگرام، تلگرام، توییتر و هوش مصنوعی‌ها همه اوکین</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3031" target="_blank">📅 11:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgAzkjl0FAe_yaF29Svzn1Nj8pVaqLCFpwR1a5wiOCBU8LpEci4IYuRJBRMNhAroaCR8Bs-fjaXJ9whVJDL-rCvlpkQRXu43ppoz31ssKTmByUMbSB0JzoRAf1X7wTrdMw2F6I5FF1JlaY7YbujfK4kOwX5c3XqXsFgHku1_xGkWpH5jwo0UI1-fQE9UUBuuxSpvw2dxqXTmirgf3Fi7yfG32PiGQLIDk3-JhvpBvW6LdA2L6SHMICXW1wXZJZy9fLkSGy3nU0I2Sv77kO0XQZcDQ12OmUE_vdPcNT30QYcTKsEwmScaSDIRvFObyNV7gdMn4geq1iIFs4HDncZR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم روی گوشی(تمام باگ‌ها و مشکلاتی که توی گروه‌ها گفته شده بود رو در آوردم و دسته‌بندی کردم و خودم امتحان کردم)
این پست هم با همین متد داره فرستاده میشه
🕶️</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3030" target="_blank">📅 11:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3029">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ftODVqQ8nuKJbsLs6tGrwY3E6R0JI8jXxRZB-pZBSHSjQAaKlwlEwf2k3IuQipOPLWBjd_OzJCfV6iAafQ3U0EEzniTTMwUKJq-vm2RzBj7o4tVs_kI8z-puwKhLjRhWD2AoJOvu_g5z1oWWp-WsGs_19dgkXI43nZD0OcVjn3_UEu8CVwP7yb5fyu1oXsQwUdjgaVRYwMNY1NynmB137dSduACMPk2vqkifZeUINeI5lp1IHsP1lFEs4KNPlYALP55jF7XR65-E6nlcrtuOe_PehaCk8C_M_gsCgGjnAjTaiOvupUGkVYT37EIg5bgQzYCP4w8yUWsAj6pK80IjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای یه روش کاملا رایگان، بدون نیاز به سرور، بدون نیاز به اکانت گوگل، بدون نیاز به شماره حساب خارجی و هیچی، سرعتش عالیه. آموزشش رو می‌ذارم واستون. خیلی ساده‌ست
با تشکر از
@patterniha</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3029" target="_blank">📅 10:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان عزیز که با اپ میتونن وصل بشن اما چیزی براشون لود نمیشه.</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3028" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh4grkxmqqCoxo-VS5JIFW4_upPAb8HYMWXfALscJRBS8i6oiv-3zyTBq1d6p6EbMxfiApPNbckerwqrnyw6FGl5tg56owcpX9FwBNYPYivuNTF3YFcBD7aiyL7cBbphRo4aagPi5vcvFWSvnQMzwoq1qKfhJ4zb0qOb20WGFZMp7CXxOkbJ4jdRGUqdCYhcqIUoeBFfrvPU8KVSIIMoBLe9ejSfdI_oDnHgJizTEXPRG7B3aI9teBbd-TAk6sgx10tgBB6UyRMWsEzApPp9ij_312G_7hAY5yuA8dIMZYhl3yXfNK30UvN5Wc4z-7wIt3jz_e_XiI__RVv1JwOkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3027" target="_blank">📅 06:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3022">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3022" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3021" target="_blank">📅 21:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره.
اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم صرفا این محتوا رو دوست داشتن، نه اینکه شخصِ من رو دوست داشته باشن.»
و اینجاست که مغز ما رو به بی‌راهه میکشه.
متأسفانه عموماً از اون لحظه، شخص دیگه حرف‌هاش رو برای بیان نمیگه، بلکه برای حفظ اون حس میگه. و همونجاست که گم میشه و مسیر رو کلا گم میکنه.
به خاطر همین هم هستش خیلی از افرادی که این روزها وایرال میشن، بعدش چیزهایی میگن که ممکنه ازشون بدتون بیاد. توی فرهنگ عامیانه، می‌گن طرف جنبه‌ی شهرت نداشت؛ ولی واقعیت علمیش چیزی بود که خدمتتون گفتم.
اگر وایرال شدید، خواه ناخواه دوپامین کار خودشو میکنه و حس خوبی دریافت می‌کنید اما مدام حواستون به این نکته باشه(همونطور که منِ متین حواسم هست) که این صرفا یک عدده و من تغییری نکردم.
پیروز باشید
✍️
Amir Mokhtari
با کمی تغییر از سمت من</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3020" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2jSTr383eG1pxrOfS0bdGzRVutWKU1SQKdTI53YW0gIftC_8m6FH_e3LffFBM_xgHEuk6wcVV4u9hR23xB12rZ-oaIce8cNWXKlBj-sDjsEuPsNyQN3Q3eYkgxcDuYjExqnMHUUrpNGGEDNevEdQqqUYN8bWSAmMCcEwMK4tjdBTGn14U5LK187V7CFBGzUJH5vFJw7b_dMDgZuExrCyIUDTpQ9GyVMIOWHn_8D1hi8g2PdlgI3RcVHQK5BCCDT-LBfJ-DRXy07l2Yu4i0wVlKpVtkFekMR-C9PyoxRRsLy7xW85QRSiOY4-_83TpvPBCFMu6ROQnY9CIIFgnHjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IRCF | اینترنت آزاد برای همه (Twitter/X)
🍷
اپ متن‌باز و
#رایگان
TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
لینک پروژه:
⚡️
http://github.com/MaxiFan/TunnelX/releases/latest
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3019" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_zb9LFm_m9lK1aS4H4JjCnrrncllUahY3xjOa9Bwb0KTwnp7eBq0kwO03YeFstMm8ZpPQ_9SbAwIbEo6yMaQInq4S77dYYzj00P6WXNScAfcyzF_utXii9gJG-FBuh-yyUbHuRPG8I6n4DrHEzxHYl0JfRUDUZjat2PgPAaqGRivtnOgo8A9S9Wx17yUl7_NgtXxiMndd3EJSQzoZb429M-sgTTKaoNjKy8H3BbDhFv0hkTb0Qmet8kwCJN8JbVClf298xssAcpvpKe3mjQ47qeBnVEtgl659394Kl0NGI95elkR_xgwjQZNAjIrnL4TlPe59Q3twaQXSckLHH2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3018" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3013" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3013" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kDVKR0nS55xHYWm45OpyLalJGsQBBAI6fdmmAwGp_HTAGGkVqqJRJvZ4Azgaq3plt2ChzhBMBomTQQUZl_c7QQGCj338mRMixWOF0VpY-xmXo4zndRgooRIDPtNLIjY4WsGi47zBODeU_Oe0nRQYFyE5s4keO2hNbklq5iImmHobw6gaNAiYcnORAt-hegqUpGAX-oGTk53L4nuzEimrwRP1xP3bq5MsMqqsMxShuJPobdC1CZyr40Hqdpb_OneHpxKwyiCEDj_0oW5Q9XSwhxTlZPqHgnSnGRuANtrEaXVpkzuh38kZA1P5a9St8Ukgu64T0XdpV0PIs1QFSTSj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dMopeRtRTeb_1e6IYoJxBuJ1i0rFyPU49nY8Hej8DsO-gnRziiAREaCcbyg1Q6vpO5p5e-Im1CCs7jRZJC_bwJtpbwV3BXuyomRk3v6_ln7XtqIqQUk8b2Vd8hfMzfNJ83xyr8GG7wApL28wkEBdcVc2SG-higJsDbyWsoElaYhuIXb9JQuPFyfA8lupZcrAfj9lUkGUxMl7KuhaW_8PtM4bJX0s6tjRNvKhU3ihGBzACRfn7op5fR8FHF1wLb8hoMVG2f5FhPHO0LvDcdGD8xM3GCJOW4RlvLTO1pC0cCwkOJWX26guvvSumn304sKa63QdXDA8BZqKL7OgUVgWSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی یه آموزش بر پایه‌ی DNS داریم. یک دونه رایگان بدون سرور، یکی با سرور.
به همراه آموزش پیدا کردن ریزالور
با تشکر از بچه‌های تیممون، WhiteDNS
(توی این عکس با سرور رایگان وصلم)</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3011" target="_blank">📅 23:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من تازه دیدم که یک نفر امروز صبح 500 دلار دونیت کرده به wallet های روی پروفایل توییترم. و هر کس که بوده، واقعا ازش ممنونم
❤️
کمک بسیار بزرگی به ادامه‌ی فعالیت و همینطور دلگرمی هست برای من توی شرایطی که درآمد یوتوب قابل برداشت نیست و شرایط اقتصادی داغونه. اگر…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3010" target="_blank">📅 23:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پول پارو کردنی در کار نیست. این پول‌هایی که دارن می‌گیرن بیشتر واسه جبران ضرر و damage control هست که بتونن یه مدت بیشتر قطع نگه دارن.</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3007" target="_blank">📅 09:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فیبر نوری مخابرات کلادفلر وایت لیست شده ظاهرا.. امیدوارم بازش کنن ناموسا بریم دنبال زندگیمون</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3006" target="_blank">📅 09:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3005">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromfarzad</strong></div>
<div class="tg-text">متأسفانه همه راهها رو معنای واقعی کلمه بستن (غیر از mhr که اونم نصف و نیمه و داغونه) وشما به هر نحوی بخوای به نت بیرون دسترسی داشته باشی باید هزینه زیاد بکنی ، یا بری نت پرو گیگی ۴۰ هزار تومنی بخری یا وی پی ان گیگی ۱۵۰ تومنی مثلا یا بری سرور بگیری cdn بخری وdns بخری و .... بازم هزینه گیگی بالا میوفته ته همشونم پولش تو جیب خود دولت و سپاهه همه ی اینا</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3005" target="_blank">📅 09:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آقا من نمیدونم این چه وضعیتی هست که درست شده توی این کشور !
هر چی میاد میگن پاپلیک نشه ! شما متوجه هستین مردم بیشتر از 60 روزه با این قطعی نت مشکل توی زندگی ش پیش اومده ؟!</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3004" target="_blank">📅 08:38 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
