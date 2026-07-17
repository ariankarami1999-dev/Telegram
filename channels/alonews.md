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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-135072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رویترز: پاکستان در حال مذاکره با کویت برای یک توافق دفاعی گسترده در ازای همکاری در زمینه انرژی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/135072" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
صدر اعظم آلمان : خواستار آتش بس فوری و آغاز مذاکرات در خاورمیانه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/135071" target="_blank">📅 17:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه: مسکو با همه طرف‌های درگیر در بحران در خلیج فارس در ارتباط است و از آنها می‌خواهد در سریع‌ترین زمان ممکن آتش‌بس کنند. امنیت وضعیت در غرب آسیا همچنان شکننده است، زیرا تفاهمنامه میان آمریکا و ایران در آستانه فروپاشی قرار دارد.
🔴
رهبران اسرائیل علناً اعلام کرده‌اند که به مفاد این تفاهمنامه پایبند نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/135070" target="_blank">📅 17:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شش فروند اف‌۳۵ از گوام اومدن خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/135069" target="_blank">📅 17:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5b7c49ce.mp4?token=k-e_hzgp35lzX9ySlUctubVte5i278VGKzzocRLMqiLk-Eax4t_1t2hFlnuQhTmlwezCjV58hW9c0iHukj8JKe6Rfrs-80Vq6pfNp1M3xuzYjABxnqThnNZM2XLwXIov7TuoQHKDOfQlGon3AC-eWxCcyFBniJpryB02EvGBAsH3NDnRGVdVMHwYfsHmdJbVgY3KQnyYw2zaSV1JzJT049Hh9bsGeHkzgzzjCOCxLMdZx-1CaGMt0Ps3dBoqRa6xNH7cfXiaBg9xCq-EVNhyHU6AJTIcmoK2p3RTONFEXhIEZ7sIP4sUeldYfKMKXhJbz_9v0CNQO2cPBGvWKowyWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5b7c49ce.mp4?token=k-e_hzgp35lzX9ySlUctubVte5i278VGKzzocRLMqiLk-Eax4t_1t2hFlnuQhTmlwezCjV58hW9c0iHukj8JKe6Rfrs-80Vq6pfNp1M3xuzYjABxnqThnNZM2XLwXIov7TuoQHKDOfQlGon3AC-eWxCcyFBniJpryB02EvGBAsH3NDnRGVdVMHwYfsHmdJbVgY3KQnyYw2zaSV1JzJT049Hh9bsGeHkzgzzjCOCxLMdZx-1CaGMt0Ps3dBoqRa6xNH7cfXiaBg9xCq-EVNhyHU6AJTIcmoK2p3RTONFEXhIEZ7sIP4sUeldYfKMKXhJbz_9v0CNQO2cPBGvWKowyWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله اسراییل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135068" target="_blank">📅 17:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بخشایش اردستانی، عضو کمیسیون امنیت ملی: در صورت حمله زمینی آمریکا، احتمال حمله زمینی ایران به کویت و بحرین نیز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135067" target="_blank">📅 17:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135066">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6c614a1.mp4?token=uIqeqy7kpMJj-hBVCHV8rrjWLUDR1HUGM98vapWU_CZFKeQZ1pMrA4fhjkYbg5-DR4f1aBU8u_hDU5tfBkBiI3Fx5NbPeIp5GYkpoRcsHZ1xl7fBTDbIG27QfVy3XFYMwxmU3Gnzt6tb2GrhMwqe2nuyVlkKolQUKvF8a2Y3sRg5MxIKB3Db9rFNyrnyj5MSCcRfN34mv0theKeD2ewkWnxvBjVFRJNCVp6YxkpDB7hJLvi6BaFjV9kvaFkLvubagKmyUHN3IOte7ef90_AoPo0t-ukV0N151foP39jNiL8cf_8pht65PYwhTJdt3NLgg23MRwbrgduOrN4myjRjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6c614a1.mp4?token=uIqeqy7kpMJj-hBVCHV8rrjWLUDR1HUGM98vapWU_CZFKeQZ1pMrA4fhjkYbg5-DR4f1aBU8u_hDU5tfBkBiI3Fx5NbPeIp5GYkpoRcsHZ1xl7fBTDbIG27QfVy3XFYMwxmU3Gnzt6tb2GrhMwqe2nuyVlkKolQUKvF8a2Y3sRg5MxIKB3Db9rFNyrnyj5MSCcRfN34mv0theKeD2ewkWnxvBjVFRJNCVp6YxkpDB7hJLvi6BaFjV9kvaFkLvubagKmyUHN3IOte7ef90_AoPo0t-ukV0N151foP39jNiL8cf_8pht65PYwhTJdt3NLgg23MRwbrgduOrN4myjRjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد آمریکایی از نوع لوکاس روی آب‌های ایران شناور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/135066" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135065">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdmecwRzN65wEKaW5P4rrn7TOvzatYpAVGi_UBv3eHoxSp5fMlI7kslM23LF77tfXNps6aZBSYJS3M8tx8HVzOPkRonscg86C0yud0vEq-1RcuAZcNwlWdWat9lTYFwNCYRDImhVoteHZwTw1WuBzezqoT7vN9TL8uLT03h5YndfoSa9w-7p1gUYJG5X6JWw9ll337gGXfzA5O45zi4jZN8DFrJeSez3qhl9vMsxmTCPCZKpOlVNTi_wGvAdwMwM00ESI7GtmsEHA5hvfXknpzrPMAvA5VWpDR4KjKDYyxNKKGPCAIpLvRlgFTe0sIGzyBhDe-HhqPjbxzsff6EhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
نماینده‌های مجلس فقط لب و دهن هستن و الا میرفتن تو جنوب جلسه میزاشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135065" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135063">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKaxgPxsTsJZi5a7RMAkPb7LoL22NyO1U6j0HQUUBfQGzLLEeyeAhKSzG0l61wUrTKYwkwPL6puxe4SSWreewMyShXTmTF-VJAMgwnU8kERKxYeaVIx1bviVFFH5lYP7fycbjjbh7_3QUECCKoPTjj0XkK1IJjts8Fj-bTjUEh7WmJ9-fcJAOavinVHEPH23nCqtyDnEyuOjOYBeod1BbNQo-iEnMBlpUm7eUSLlsvtwHiIMPqnUz__8V5cKr4SdL4mkZiNYt4b_m6GhfnazdJinRe7qPT9iup_xRrA3CBLjuUhWsx9Y08qs3ql6lD72FLO8PiYn_Y1BMvl96_I7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788a242c29.mp4?token=VovmR-VcQrZB633WH8sq6nFjc0vi9euSDDa6yz4KWsGljqi_mS2CVDTbRA6dLEXFMzAdaFSADzXsALXJ0v4Ln8dr8Uv1WYSJ2ogpotqB0gaX-K-xT190HNFFzRdNd-IamxjMY1h2lg9PSEwhluABUPSe8or62y3TaXJSBaNFwSrjs8YapPXv7_SwqE4HyiK_0TA8qGxGJ5mN9rrQLYBHKWBFCLjpoSUI8kmof7kLsizh1JyT42L2KLceucGaGKUJ-8S3ew-YXZMQTOCUSuK0xtbwvkhwWBBmp-DptVV9nt-nUWKQAWCNfRktNIcn2i2HJPM8DgOGk9GAz2LMBHdg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788a242c29.mp4?token=VovmR-VcQrZB633WH8sq6nFjc0vi9euSDDa6yz4KWsGljqi_mS2CVDTbRA6dLEXFMzAdaFSADzXsALXJ0v4Ln8dr8Uv1WYSJ2ogpotqB0gaX-K-xT190HNFFzRdNd-IamxjMY1h2lg9PSEwhluABUPSe8or62y3TaXJSBaNFwSrjs8YapPXv7_SwqE4HyiK_0TA8qGxGJ5mN9rrQLYBHKWBFCLjpoSUI8kmof7kLsizh1JyT42L2KLceucGaGKUJ-8S3ew-YXZMQTOCUSuK0xtbwvkhwWBBmp-DptVV9nt-nUWKQAWCNfRktNIcn2i2HJPM8DgOGk9GAz2LMBHdg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که یک انبار لجستیک متعلق به شرکت خدمات نفتی آمریکایی هالیبرتون در منطقه صنعتی مینا عبدالله کویت، پس از حمله پهپادهای ایرانی در اوایل امروز، به طور کامل تخریب و آتش گرفته است
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135063" target="_blank">📅 16:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135062">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO7K22prbm3ehOhav7cDI1vf2-bXdL2WXHVL6ljuWdYLN4jQPC4NGP1U15pN1KCBpLpvfifQSzsqJ2W_414GZfwzRAiGOo8Ssgc_b56j7919DiyCJMZxkFWkEl6-Om1TtHsvhlO69oEWVt2m2tvADh0kmswxR1RD53AphBrbQXTWHwYTYjU8_6XoNIQTNzN186QnAVB8AjweDPG6rkZpTsKuhUVcumfwjpcYanEJuS6849I15vMmWWziy3PF1znp6npXaIqIt-R1xMyqFxbq-U9iMZggO3saruteqH2O9lFNA9Cpp371rLp9x_Iz5B5OOoS6S6nrqOQe3ZO2ASvdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا الان سه مربی تو این دوره از جام جهانی نباختن:
@AloSport</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135062" target="_blank">📅 16:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135061">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFLLnvQqkm5Mw0d7QTBbcZPsv7JbOHv8JLigG8FixkpsHq5nrSm0vnBLFupz4ZUOKAAjn0nnmCP9Qwx_FaG30XDGSwpfB8G2abuVURHJvLKGDgwdnk4WlFJbiy4TkWpTMEt9STfZxFOsXu5Zm95lA2LL75g6yk_30FPGjmyQWaczd7LVUBu89N5OkD83752rup01mIQJdRv0hZ6bEPuEv8sbbxhXt8U01dhnSI0BBqQvqvIgEWzxb6yxKEmDuCdVGzEOFKuEgWivpryRUNIGhEQEnFOZtmh9NA--CACvGOg0b7JafdOs4fWB3WA54XRNAEq0MivApLA-jgTenUNPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق اعلام برخی منابع پاکستانی، فیلد مارشال عاصم منیر قصد دارد به تهران و واشنگتن سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135061" target="_blank">📅 16:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135060">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
روزنامه الاخبار لبنان ادعا کرد؛ تحرکات جدی مصر و اعراب خلیج فارس برای بازگشت آمریکا و ایران به «یادداشت تفاهم» و ازسرگیری مذاکرات صورت گرفته است
🔴
قاهره به شدت در تلاش است تا درگیری‌ها به «نقطه بی‌بازگشت» نرسند
🔴
فشار سیاسی - دیپلماتیک اعراب به واشنگتن جهت جلوگیری از ورود تل‌آویو به جنگ بیشتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135060" target="_blank">📅 16:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135059">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or67Ip1rKItkElT3rA6TtXWKNF5I6RD8YCHndZHCXrrpQCQzCQT4i97eqHW88cuJsKoN6LUrJNWW9Tyg2aY06cyPaotXKH2B2S3Oj2MWxKCLvaVsSM4L2zFDFxThhw16aRwil9NLRC_DneGzi7d6YZbv2GjyxboRtB3Dqcvn9o_zydLvs3-fYBXy8_PlOvt7K7y58RgdQ5oeJfLXXAbjcriej9rlTQGb1ceACRsSTt7pgh3PGdhv_xM5IT25xjZDbLJJcrILC44IJTSO_JXI3-bcKZlWEycaHH-YMRT5P40NGqTY4hM4O5Fuc4gq-2d0dDqMFCQ8kNZDhKhJqg-8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقت کردید از این ۵نفر خبری نیست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135059" target="_blank">📅 16:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135058">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گزارش انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135058" target="_blank">📅 16:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135057">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=o_aK5o0MnYc_UoVuJX019wc7wHEcGXdZnli_ClojtEuqveCYxr3VjA4Pleeq0hUETTwDgFDEEbJZ-QdH2mFyW6pC6eQpeNn87_DEoK_FwFptXWNDSpwEYQaygVwm5wpc861n1fZpJWeG_mwYuIM2ftXDmgf88cU9QUMgsfwLdRLCUyE4pCYpyL3SQ1gydhEX-7jIB7WNpM8nxEctupQg6CZDQsM1SRrU9HGG1saCO4kzhFqpUNr_B6w4kpfMu07gTQAc98Bkjzy-wd9rqzj4msYCCcTjKshMO_pUrWucnGaiRsc_7ojiu7qtPCwrEVoMbc8fNV-WeAjl4wYK2-yzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=o_aK5o0MnYc_UoVuJX019wc7wHEcGXdZnli_ClojtEuqveCYxr3VjA4Pleeq0hUETTwDgFDEEbJZ-QdH2mFyW6pC6eQpeNn87_DEoK_FwFptXWNDSpwEYQaygVwm5wpc861n1fZpJWeG_mwYuIM2ftXDmgf88cU9QUMgsfwLdRLCUyE4pCYpyL3SQ1gydhEX-7jIB7WNpM8nxEctupQg6CZDQsM1SRrU9HGG1saCO4kzhFqpUNr_B6w4kpfMu07gTQAc98Bkjzy-wd9rqzj4msYCCcTjKshMO_pUrWucnGaiRsc_7ojiu7qtPCwrEVoMbc8fNV-WeAjl4wYK2-yzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135057" target="_blank">📅 16:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135056">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f17c95a2.mp4?token=uhq-oQaxGP50p9fKpiJTbKNicqcrGiEIeOI8iydz9l0KqiMTdS9S_CZjkoSkDLKTE0cPaFfyj6SNwYJVj_ZhtXn4NpC3iTi7QDxuWxiyVxCGcX4rJFU_1ZtVI1TfltjDpdy1_SnuNgNiv3vdfH14XCXU_ayKggS6kqze3e4RRpx2eH8jtQBoHYPJJy1e5iuWIdDWBmmTPOnbUM199aAIPapAid8iptlAqiGHUIbYBQeKNihCGQn6Ibyi2Sq8Cn0mVz4jHuwLrUwuPi8IvIgWnNNbiMyPgCO_rBHg3OKxutldhDtV0vnoiWCr-DLAn2puuCKoJUcnpEhD5jN7tZrbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f17c95a2.mp4?token=uhq-oQaxGP50p9fKpiJTbKNicqcrGiEIeOI8iydz9l0KqiMTdS9S_CZjkoSkDLKTE0cPaFfyj6SNwYJVj_ZhtXn4NpC3iTi7QDxuWxiyVxCGcX4rJFU_1ZtVI1TfltjDpdy1_SnuNgNiv3vdfH14XCXU_ayKggS6kqze3e4RRpx2eH8jtQBoHYPJJy1e5iuWIdDWBmmTPOnbUM199aAIPapAid8iptlAqiGHUIbYBQeKNihCGQn6Ibyi2Sq8Cn0mVz4jHuwLrUwuPi8IvIgWnNNbiMyPgCO_rBHg3OKxutldhDtV0vnoiWCr-DLAn2puuCKoJUcnpEhD5jN7tZrbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط یک کوهنورد، امروز در علم کوه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135056" target="_blank">📅 16:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135055">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Ux0mesDdiAf2--Gj_1mh-w4QbDUaf-5mD-Hzu_ebgd20eOKscOzaLqf3A9W9T_EGUYMB0AQUd7x9Jwi3y6QkGDgpQT-agS8b8paR--o7mGzsJumrmUBugfzpP6Vh8En90tCQSXueMehLDgMJfz5D2niU_U5bGiCDlvvPyWt56TqWT6iB84iNDfNLYcMcsTBhRMr-dFPWISSai2EkYm4YZiq-H4nvLtbvqgwf4JwPF-mWICDX0QmUp__W4uTuPWHnVoPjcyFeK4x_NuUC0CebDzdKZD-Kf5VNIsxwPXBtSFSAnKu66ZoSnBU8jnjgLgAzHIWkpTdHAuWL6j2R8j6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیامک مادر یکی از شهدای سرباز تیپ ۳۸۸ بمپور:
🔴
۵۰۰ زدم برات رفتی بیرون چیزی برای خودت بخور، به مناسبت تولدت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135055" target="_blank">📅 16:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135054">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ca36696d.mp4?token=XeNCz1CxXsfN-bQwT2Q_tbecYikRLc4GsQK7JsphT2QVk-0nre74A0MhdyOTJyhJgNA5_Sr9jADi0afXG8HmOc20FiSSMeWzls3zjXgqQ1vVZtYWpeEjjBv_pWVM1RX3m0ZTH5tEhT6sjY5DerWD0se2Hh8ZPFLQRvM1axSvjpG-Hb_4RJrDIwpO-rzD50PKHChR6CIDRP_8owP1S2GLyxjle4XsrKkKMjCBK3uE5Dj8DxokAO2X1vZI-eROnd6uBMEbiKcq5L6KaUCiZzfws5BNY2HbV5XmDmG66VxzdqY07IiWjIESSk8-SrF6YJ5ytuJy7F9dgF7g1OBubhQd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ca36696d.mp4?token=XeNCz1CxXsfN-bQwT2Q_tbecYikRLc4GsQK7JsphT2QVk-0nre74A0MhdyOTJyhJgNA5_Sr9jADi0afXG8HmOc20FiSSMeWzls3zjXgqQ1vVZtYWpeEjjBv_pWVM1RX3m0ZTH5tEhT6sjY5DerWD0se2Hh8ZPFLQRvM1axSvjpG-Hb_4RJrDIwpO-rzD50PKHChR6CIDRP_8owP1S2GLyxjle4XsrKkKMjCBK3uE5Dj8DxokAO2X1vZI-eROnd6uBMEbiKcq5L6KaUCiZzfws5BNY2HbV5XmDmG66VxzdqY07IiWjIESSk8-SrF6YJ5ytuJy7F9dgF7g1OBubhQd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
این صیغه ساعتی های حکومتی الان کدوم گوری قایم شدن؟
🤔
یکی از یکی حرام زاده تر</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135054" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135053">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آمریکا: حملات ایران به کشورهای حوزه خلیج فارس هیچ تاثیر عملیاتی بر نیروهای آمریکایی نداشته است
🔴
سخنگوی سرفرماندهی مرکزی ایالات متحده، سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/135053" target="_blank">📅 15:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135052">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIvR-PgRVYjHm9YRuI2q-6bz8lheAojZpStDlOoV5VBAkK6tOZG2h66j_mzjARs7iFOC7o5w693o43V7aX_AxwNE9koZv142qxOEXLwSj1hx0jtfHASthzhfYjIT7QIMRdciY59sQRmkjjb4aLZyOr3l0mO1UngF1jJ_wG53cURCV3Y9WQ8_xO4AAh1hFtmuB1CtGU3HOwQnpsq2DKaAiXAAt0aPWRxXizAQZnY0xrMauK34sWFoG334rqnHbkpzBXE2B4b8GQE3mcwbVKplQrtJRG-_Sn7pHDJLX87UMbSui46XORhhnWe1qUQyDsQ7ZsfUwT7kWWDn8l7UrounTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مداح پاکتی الان کجایی ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/135052" target="_blank">📅 15:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135051">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=Ql2zaOoLzKb1KH-Sl3c4pP_fkKepuND4cANbsA3ymdfW4t_2d-hq7rp2K8wFR2aWmLYEcLV2w1zXtTHEZ2LmnaoGr_yvypWe-A0dPJt-f4thhKq1jihUo3qBAgg2jj9XHCJuQ20yGU7prYKx0622Ao-BTeKg50F2amyFNp1wfz4PWkmmsG617M9i3b39T8q95K0VDmwELvQ3UIiz46pthEZPELrWr_djOH52ws9wqcxRjG2nZGIODA3Pz2aAohW3FRaX3EOZInJCK3jyp1mFMLC05l8r4RXXYLMx2lZOtHjxybb06XRljVQc6dJycamwyGR8SkpAxdVGgnwxy-CrZS-l-c-Ee5UAa1TEmCGtNPMl7S_JBSYxevRXa4qmizgqtHTwjzG9kQAPlTQ9rmRzr6AgtElnegp0agx3QXZVKkhbeB2j1b3dAutCN0vRi15wVqHjEBCjBSrTRaUn2Ywa5pvNvPLZCnj2FLNUWdIEYJvSiVwaXOXa6kqAyHZnvBkN91uIa0hpSAdKCvFv3Qz5Cl_TmLcUhn2eLt53dx7mO7P78Yj28enqcwNx4Qmmuul8zqBXj_JgKiW_-Iw48dbHLtc8gNWaMxQsP5vj78A5--fguj7baD_JF08qrYiQqmtMT3XVn9f00_HYahxeShYWjFZzg5jdfp7SEEx5Oa05mBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=Ql2zaOoLzKb1KH-Sl3c4pP_fkKepuND4cANbsA3ymdfW4t_2d-hq7rp2K8wFR2aWmLYEcLV2w1zXtTHEZ2LmnaoGr_yvypWe-A0dPJt-f4thhKq1jihUo3qBAgg2jj9XHCJuQ20yGU7prYKx0622Ao-BTeKg50F2amyFNp1wfz4PWkmmsG617M9i3b39T8q95K0VDmwELvQ3UIiz46pthEZPELrWr_djOH52ws9wqcxRjG2nZGIODA3Pz2aAohW3FRaX3EOZInJCK3jyp1mFMLC05l8r4RXXYLMx2lZOtHjxybb06XRljVQc6dJycamwyGR8SkpAxdVGgnwxy-CrZS-l-c-Ee5UAa1TEmCGtNPMl7S_JBSYxevRXa4qmizgqtHTwjzG9kQAPlTQ9rmRzr6AgtElnegp0agx3QXZVKkhbeB2j1b3dAutCN0vRi15wVqHjEBCjBSrTRaUn2Ywa5pvNvPLZCnj2FLNUWdIEYJvSiVwaXOXa6kqAyHZnvBkN91uIa0hpSAdKCvFv3Qz5Cl_TmLcUhn2eLt53dx7mO7P78Yj28enqcwNx4Qmmuul8zqBXj_JgKiW_-Iw48dbHLtc8gNWaMxQsP5vj78A5--fguj7baD_JF08qrYiQqmtMT3XVn9f00_HYahxeShYWjFZzg5jdfp7SEEx5Oa05mBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی مطهری: یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد/ پزشکیان می‌توانست فیلترینگ تلگرام را رفع کند ولی چون روی وفاق تاکید داشت این اقدام را انجام نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135051" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135050">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIttBMZO92UTcLO4cFetnY3sYLc8pvSRSZHkqYmb5cNcvoItIkUiQtIXZVTgAhU_c9LYm8CuuzEIEINQu23FVU6oappFjtVG7deQJIy4cpcRxYXYsXNfc2p9-MXbkixCODfr-IWrykL3JBNyjeoZAmSlWjn9w5ApHfYRBLiicSdi_eoOP04HjyUPv-PPgm-SHnHSfM_EqxZ_IzRO0vIPeQeIdwx0cKvV-c9ylyqQJghWmRi4-o2c3eMtZiXTa6JpfiRFrfZ1AG0QzL9PfVU5XtvG5nD1DKccm-v0aeREuhotdmZmkmZowCDX4ANSOyT0_S0TPgIUOcz4wpP0LdwOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی در سکوی پرتاب موشک‌های هیمارس، احتمالاً در پی حملات شب گذشته با استفاده از پهپادهای انتحاری در مرز کویت و عراق، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135050" target="_blank">📅 15:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135049">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135049" target="_blank">📅 15:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه قطار در ایران موردهدف قرار گرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135048" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD5LK6UvJWG-SaH8tL-f_pUd9Hkw613C5YgsPSq0KQ0Pq7CksxxNiOUhHh7T3pk4FfqJzM_xeCzk0O3BIlWp0pH44HWjWajqF18P-w0tZ7hXHuvSOoCyr3xeAiy3yNmZ8Djm3EvfD0okU1jzLvGq9xJFNILpv7f6uUMP8duEMtvCSEOYgLkmFJnKzj5dNKu_u9qZ5LfcKLWy9cEqURl60TGmel6fdfrxXwaO6tIKKoq0fdqkMoUu-AMt_coRTcf3snz9yS6iVZnlT3i7HWYQ0IZjvaTkfa0ZybzOaNOEaHmzzQlGdv-Vn1IueQISB5rqIRYxEkxyyNLGxZ0A_ig-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: باید بریم پایگاه آمریکا تو کویت رو تصرف کنیم بعد تجهیزاتشون رو به غنیمت بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135047" target="_blank">📅 15:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135046">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUEKJ7HYAVExQ2WPcCocqMWmsRn2-csfR3XdxGtU_J0yxoyLDlSQR5rCs430tpOWpUobg4EPfPWsRGcNQF0KNclVNbwmpJGeHN38Mg_YwZRMW_b8gPq31d-hy2RxnrrdJiA7OVbXcQpN9M89-7j4BKEC9cXx1jVYTpvpfx7G6HWIL0XYMPUmYKmvaKp5FM4KZELnBsOrJnNwQjcLw9-efPTibeatRpx4NUFcOaMhYBPv5scVxpJnCZwSMdi8CvvF2VA2nyN_BiSUkGQBaVEgPBm_m5iBVkM9QNsJTGZKoVHfdaptndEC0jtrfpyRoa7b_k-NVhA-WxBtAAU9h5fR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بندرعباس مردم قایق‌هایشان را جلوی در خانه پارک کردند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135046" target="_blank">📅 15:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صداوسیما: ارتش آمریکا برج مراقبت ترافیک دریایی را در سواحل مکران به کلی تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135045" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZd0wwJ43NPHVIAyPZRrbL4Q-iAnwHjFU9DoEeNoM4WYQrQQeyVOPWud1HEwXBT4htGQfdgY3qbmhRv6dVuGWijJ2H1hCvdqRnWXxgtRXmxxkWrQLf-2w5BnCjass68F1KFzimVu5RyozoaLNAgO8RbcH87-ZqK9T8sH6nqw0jxEEFHdfeSIrEB_fkfIK9UQIEQdyW_kBVcurPj4pLynqdoe82X3k9KspEYWcBLJLekvCNU0IVnc1RaB5UYbBEJLBYagTroyUOgMH6ZwFHb-UpAfEDCWu5qW4ksDsFMaMMmlcaoZS8duXe0WcbgxxHvehmOghHXzTgou5HrfeBLE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست‌های عجیب در پلتفرم ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135044" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دولت انگلیس:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا به آن کمک کند، ممکن است با ۱۴ سال زندان روبرو شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135043" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPlYNPyTYKdEzyhpygobV4n7oe85TzkjX7NqSIEDLywJ1eMdLnxb8oNC63fauEYQi_CILJguC9JYUB4ui21d8AA-T04vqMccxAXnC5xpA4TLtS6LCo-d_J--B-cg0vR7wAe5ElY4738_jEHrrrPR__5CKFnW9YaaVY79tHy-HSZdOUi_Yo-4c5Hzhayylzw2tflYzPxUVd7293p2UpiaERg7Pjx852NAcBRB2iP_eJayioLjO66YGj4nyVxHvfJ2sF273XS-VwNbZsIDulaXI0-T-2yRlDKNmybJ_YkO75OGM10hWPqyfXeaWNGjKsJifQHJ5ET5DpwC2y0aPF9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعک‌های شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135042" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9aa080b85.mp4?token=MB8bEogJ3lYMCdj7kyXzf3wpBL0uVyuAf-sPB4zdI01XcQFn1-mbLWiJB5WqqmITjjMxE4pqB272fmKlMRMlYM0wbiZfdYL2MhMmWQis8ZwaNody4OJIU8Ib7DVHb8hsxLVLhtLYiIQNDt3ZEO88il0kBNPx-hQqD4KLH2TW50yCO6hBZ-9MwvLa3kPNwM7P2vsd5ZjBXNe5zR9FP1UFNHm0wPXh5_E1P92cAZkdfX82qVDAwbzNuxmIboKUms7WVClSEMhCwMqx0FUoHLE46lriIx_pYlnaS4vsQTPGPkNZrUBccCc83WmVjV-ufnbG6hPBuUBOnd3uqww-NHm8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9aa080b85.mp4?token=MB8bEogJ3lYMCdj7kyXzf3wpBL0uVyuAf-sPB4zdI01XcQFn1-mbLWiJB5WqqmITjjMxE4pqB272fmKlMRMlYM0wbiZfdYL2MhMmWQis8ZwaNody4OJIU8Ib7DVHb8hsxLVLhtLYiIQNDt3ZEO88il0kBNPx-hQqD4KLH2TW50yCO6hBZ-9MwvLa3kPNwM7P2vsd5ZjBXNe5zR9FP1UFNHm0wPXh5_E1P92cAZkdfX82qVDAwbzNuxmIboKUms7WVClSEMhCwMqx0FUoHLE46lriIx_pYlnaS4vsQTPGPkNZrUBccCc83WmVjV-ufnbG6hPBuUBOnd3uqww-NHm8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تو تجمعات شبانه : جنوب لبنان و جنوب ایران اسوه ( الگو ) رزم همه‌ی دلیران
🔴
عملا دارن افتخار میکنن که ایران رو به غزه و لبنان تبدیل کردن!!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135041" target="_blank">📅 14:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZqb2jIEB61EpPdnjkmbsSV-Wl7_vGgLVjLL1gbKSX-Xd7MLEvP6pUqvBt0tQt6Gsr0JFB-G-aGexgfVllMCIJ1MGY9pXC4w3Z2_CdJyvcQFHamYyjcr3VdiG6r89vIKJ-ke_Fual-s5nI-0I6KGKbiGNJlJ1rpGuT2Z6-MH5lnqCxcW51o1arNcbwjhaKBrFlsH5TAkx_niW5VD8L9y5QASgMWOYLFVozc3Iv864G27xsNVF3ntAWMVi8J8AZo1-b07J10mUEHuTsYoQgg9s90K9RKszYemtcCMNOgTXIFj_998ZeTL2mrvrkTj_d6uuwGK59uwlSCxfhIYEi1UJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپ جام جهانی رسید نیویورک
@AloSport</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135040" target="_blank">📅 14:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkn5flYtEE8Smy4Ay5gLAm6CXzcDuh4wjILUHlXIeLBg-1uUGW2Tx7WW_AothoH5H8-d-cX5Spy3wR5vIuFbijwH_4zrb4GhtEU29NjE9zYksJjuviuQ6y43FaQKxGNmP5zR61Lh53N3XMOVm55cl7PIGy9Mnyftf2x77UKnszmbcSn5v6bsaAT7xMgsaOzXxll2rU6GhsrZKjZsygOatEbmqfjrooP8TizHPxkOZNVCxwYyfjn9qMp71rVugAlj0kdTK6aohIun9aWUv-Lr2MNZqR-M1_NqTR-sgBuUdxCf2OjUonL7lLKFzxW_afxDDK3mP19yjuR_c9rwYSKH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی از یک حادثه شامل یک کشتی تجاری و نیروهای نظامی در فاصله تقریبی ۱۰۰ مایل دریایی شرق دوقم، عمان، دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135039" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=Hztwv2p6-O4Je_EwTzpg6jhjiDNN8n5Qk_iDL04vqiYT44cEwslZvNkxLJSTFzT9VpgZHHauOOkWmiGwamP17v18eHzXAr-5q7H9G3kLPEB5Qj0erQYG-VFQxfthoCeqwlyivWpoSZT20elRcFsFdNB7b_-VwroOsfYeDGG7FxqwZj6q_Tijk7zrb4t2NiugazIIzolpbxtQ0yUmuipIvCMhH1Y9t6170dZOLPq3hIB2ZTznxjEmPYO4KiSImKX82OLcZKr7oil4dsaGXnzvnrhcrzOt6VwzQ5qJWfFMvXsItoeUgo4Ac3ifP4_B8gOUsWOTsjUVkFRD8h7a1iQ8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=Hztwv2p6-O4Je_EwTzpg6jhjiDNN8n5Qk_iDL04vqiYT44cEwslZvNkxLJSTFzT9VpgZHHauOOkWmiGwamP17v18eHzXAr-5q7H9G3kLPEB5Qj0erQYG-VFQxfthoCeqwlyivWpoSZT20elRcFsFdNB7b_-VwroOsfYeDGG7FxqwZj6q_Tijk7zrb4t2NiugazIIzolpbxtQ0yUmuipIvCMhH1Y9t6170dZOLPq3hIB2ZTznxjEmPYO4KiSImKX82OLcZKr7oil4dsaGXnzvnrhcrzOt6VwzQ5qJWfFMvXsItoeUgo4Ac3ifP4_B8gOUsWOTsjUVkFRD8h7a1iQ8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی جدید از پل کهورستان شهرستان خمیر که طی حملات دیشب منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135038" target="_blank">📅 14:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/135037" target="_blank">📅 14:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135035">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=f2E0GB_gS18AbZoLy_IBDtFcG_pfSavo6qUIqhdkuiCYHRz5q9BwAUpceGTMtjFzWdGiv348uDOd1w9aOYwnG3zmIs6TFUuF0tfwtYQO521Tl5_GvbfMx4tw8i6LE6joNyVjdwzopl8Oud9bsvRR_fSSAW1u7WpaeSSO5Xfc_4ce507VJnAYtWdCGeg89WAcT22O_g8mZpU3lMFzoFfbz2vTgRdvodbS8UGIAfB834YoHfYaI0B1Q8UT6FxmCPpH2w0ltC58EOLsRe9w16bOcEAkUzshFk2XmRGmb0I-LWUivturCh6ukJAks-w2JuC5RM7uXJ61Fh0v3GBYpw1QUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=f2E0GB_gS18AbZoLy_IBDtFcG_pfSavo6qUIqhdkuiCYHRz5q9BwAUpceGTMtjFzWdGiv348uDOd1w9aOYwnG3zmIs6TFUuF0tfwtYQO521Tl5_GvbfMx4tw8i6LE6joNyVjdwzopl8Oud9bsvRR_fSSAW1u7WpaeSSO5Xfc_4ce507VJnAYtWdCGeg89WAcT22O_g8mZpU3lMFzoFfbz2vTgRdvodbS8UGIAfB834YoHfYaI0B1Q8UT6FxmCPpH2w0ltC58EOLsRe9w16bOcEAkUzshFk2XmRGmb0I-LWUivturCh6ukJAks-w2JuC5RM7uXJ61Fh0v3GBYpw1QUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی، تحلیلگر اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن
🔴
الان هم اگه سپاه تو تنگه هرمز حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور مارو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135035" target="_blank">📅 14:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135034">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvwRkM-rawA0cJG59hLMFveyE9ftclITBpbWib4flgd_aGXq3jmwyXB3HmymOzCagWliAhokFTbQs2plmitZVpuQ4VxgcgS9xGoLYaiZHcd3kTkQQabUpXz9M9CsQeGW0TkgZJKgntM-QAAT6hHpqucF2lI-KLIUaHhJF4WJJiVWZp_7wjYepEzBd548pPUcS9sy8reqXISH_469Cjs6mNNj8hQOfJX-WhZrza1e2_fKxcssQ9r1gYPlgpwHgy8-KtZtxvbUuu-NaBEIEfVMdzjS6tLnXMQzJg10ZKFHCdsv-c-gAY0__1MuNo7yjDG4C_HsRXMCN5wGJZNRavYC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل هم در حال تخریب شدید زیرساخت‌های حزب‌الله تو جنوب لبنانه. (زوطر شرقی - غربی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135034" target="_blank">📅 14:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135033">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/135033" target="_blank">📅 14:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lja31KU_fr_egVxKyeuhwGOp0RjPPAv4hEsM2l97301tLQ9_A22n-MhDymTOLMJKbbtVNFrNg7T-2fJPyeX03ZKbZHkGUqYCytXC_RrcfWP1QvSpiumHtFS9ZhmMdfSjbAcge-NQGZ-rxyYQ0RMP-MsYZ7SkeTJWhlyexXI65JEuVgP9Pfzfix49z_OeruaLhyXGN-6uJyTumCK-i-_vnuRN0sL83ieeQGUwph9EClZjVN5EvFiOaU23fX5H41ES6u9f4amWLYUNI3LNQDves0wuFA0OkoAMM9gbHKyG00NrnfOakywfySE5k6qaQN9w-lxT8rFcAqU1RKVQav-3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+اونجا رو می‌بینی آقای رنگو؟
اونا می‌خواستن برن فلسطین رو آزاد کنن، اما حالا از ترس حمله آمریکا حتی وجودشو ندارن برن جنوب کشور خودشون
اونا خیلی حرام زاده ان آقای رنگو.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135032" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=FsVgheO6YRcUhtAYQw-SiHwUiC86ZqIM1M6i0cBi5xdk6msojzJ3XofNqIGu_LF-pmUJF70R3W1tHc6MYtaDMzSTgvis4BNXnP5qzQZfBQCJw5hSN6n-peSfSX8aALW0qDYMZkqr1UBLI6xF5F8cCtAtqs13YsDe2R1oJeoq1xoy1QFTcqdPzXbQtHHCGTP93fMepajqT2NJzQ_g2wxQPXoB3IJQfGMGg7_lUCHxGMeiL1kKKYCCo6YJWF5FZUyzNCjbOjvdxm5rb8kXj9awqEapNLJLUjA3naoQdglrmcjJ9eJDQYxuiXUkHegc7cYrAzBePIJGNEWAqxq3aWkA1TkCl8DC6wukl9HrXQ6EV-LIqZb1OGXFJz0IYzUoUXUCRTFLK3qUqLdZfbYb7CklexehRs3sRGicNn4fgBrnaois3RHaeVYSYgPo3Ql0MzGkSPKe_aWl0iYVftLOsWkGT-ZlnukFMPbPuMMuin6UcFvrpqQPun_6jzj_1XnDJqnEH9ch7L0YQsXTdsPfEJh43eHCtYfY4ER7MjUz-uh7Bji1ppSY3tVqAeOQKyFn7AojUhwkoH5OIdmZDlGBub6Uj1S1tQZR8H1WFG55LIluUuDSJ8tAIougsD_Qa1yr5ExZVfx4tqBOoqquPnkNgo1yhKDVOQOBB4maZBQUmIDV5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=FsVgheO6YRcUhtAYQw-SiHwUiC86ZqIM1M6i0cBi5xdk6msojzJ3XofNqIGu_LF-pmUJF70R3W1tHc6MYtaDMzSTgvis4BNXnP5qzQZfBQCJw5hSN6n-peSfSX8aALW0qDYMZkqr1UBLI6xF5F8cCtAtqs13YsDe2R1oJeoq1xoy1QFTcqdPzXbQtHHCGTP93fMepajqT2NJzQ_g2wxQPXoB3IJQfGMGg7_lUCHxGMeiL1kKKYCCo6YJWF5FZUyzNCjbOjvdxm5rb8kXj9awqEapNLJLUjA3naoQdglrmcjJ9eJDQYxuiXUkHegc7cYrAzBePIJGNEWAqxq3aWkA1TkCl8DC6wukl9HrXQ6EV-LIqZb1OGXFJz0IYzUoUXUCRTFLK3qUqLdZfbYb7CklexehRs3sRGicNn4fgBrnaois3RHaeVYSYgPo3Ql0MzGkSPKe_aWl0iYVftLOsWkGT-ZlnukFMPbPuMMuin6UcFvrpqQPun_6jzj_1XnDJqnEH9ch7L0YQsXTdsPfEJh43eHCtYfY4ER7MjUz-uh7Bji1ppSY3tVqAeOQKyFn7AojUhwkoH5OIdmZDlGBub6Uj1S1tQZR8H1WFG55LIluUuDSJ8tAIougsD_Qa1yr5ExZVfx4tqBOoqquPnkNgo1yhKDVOQOBB4maZBQUmIDV5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت پل‌ها و مسیرهای مواصلاتی هرمزگان پس از حملات آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135031" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135030">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
هم اکنون یک اسکادران بزرگ از جنگنده‌های F-16 آمریکایی با استفاده از چهار هواپیمای تانکر سوخت، در حال حرکت به سمت خاورمیانه می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135030" target="_blank">📅 14:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135029">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
فرماندار ایرانشهر: در حال حاضر، عملیات بازسازی خرابی‌های ناشی از حملات آمریکا در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135029" target="_blank">📅 14:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135028">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF-0gTEUbr5b5K1_EMsN3AsO8g0ABN-4JKTTCNUpwe0YJO9gv8E03RkvyLYY-GIBJ8v2K5fNnmMtg12WK1JeuuyM5VnWmL1sqlyPqNgcgHbAy8xrLWHZywW3MZYV209DtJ0WbeSVY4ql4Sb_O8A9MlFfwgaCLO-qhrHpYGnUakNKRPStHM6p_d3O1q6PT1BiP1rB4mbKkuKIUhhNa1mXNN8w9YYPYXzfneWDpUQTB62D_aRaM7sCdkp86ChZJzjvppoT_cr6QAf4F8amnLgvw3gl01QLVoY2MN191up6yvstPK9g5NmJNm6zmQ41uOTJFTli-1lVA0KOAci9YFfxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کامنت‌های پویش جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135028" target="_blank">📅 14:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135027">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سایت داده‌های کشتیرانی کپلر:
ترافیک کشتی‌ها از تنگه هرمز دیروز به تنها ۸ کشتی کاهش یافت که پایین‌ترین میزان در ۳ هفته اخیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135027" target="_blank">📅 14:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHYREC3ytBPPtBFyrLaeipdy_LGutk-5N12asJOJe0Ms6nbuHiJdiiiBjONaFer8rezvUEMvwd7EzaIGC3Ugpc2juQMU4-6YjC0Y_cLWaRLgTM6kAk4-SLqpJN_ziBj6TuqDdj2rJi3JCHNWReaMuj1tl-ucDxpQfCrQ1GHKkobDATFyKnZkvvgKFC1Ia7H5VOvmc1GmqIECjE5A8V-ALMMh5IXaEzzHX6G-XoBcYdt3xBl-0oWSI8Y3TGoxvzsyiau4TZ6YTDLYCCKjWUFCfZwXe3mwBNKqoolY5ycQe-6ktlTd1ASQku8bOQ-FQuWjjpiqLhObtYsTK_a1RuC50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135026" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135025">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدخشان از دست طالبان لغزید
🔴
گروه تازه‌ تاسیس مخالف طالبان موسوم به سپاهیان میهن صبح امروز موفق شد برای مدت کوتاهی کنترل شهرستان یفتل در استان بدخشان افغانستان را از دست طالبان خارج کند
🔴
این گروه همچنین مدعی شده پیش از آغاز ضدحمله طالبان، بخشی از تجهیزات نظامی مستقر در منطقه را به غنیمت گرفته است
🔴
اگرچه طالبان در ادامه با اجرای عملیات متقابل، کنترل منطقه را دوباره به دست آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135025" target="_blank">📅 14:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9pBK0O-nr2F8dwqlVl78DEdf9QStVD_I_rjf5mX3wn9NgWU9QjoeMdI1HC3FgJv2Kg8O1ZZ1SJFq5biV6MHbRbLH1C9MZ6jtGMUIal6rdpDZB0ET-rR2jWSYyY4q3sODLKhnUJYeEPEDWpKmSIVFqZMZJQvNlh4687UKCNXLryn2_W_H8tGMHHj8WiulP-r6bVRwnpTv-mzneujqW6LP3fYZwsCE4_7FavjzkAjSS_DoFvmcH2WPK5NzcmWeq3kvqhH7CS3Ti8gWX3fcyFIH1an4PS5wT90QcsHStl5ZVbZ1eYydKTzq4WI7l_LuMetfjNCr3Xo221JOmJbjSqkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر دوباره همه را غافلگیر کرد؛ بازار در تب‌وتاب افزایش قیمت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/135023" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRsrTGfQVNTLhI4zCrv8QkaN6PqcN8oa-1G_dJ0bTKRXKnIfsd1fzlyJVk64BEHJJwq2V2llLqbxnsBZBG-AVh10K-3qlYvAreHuQrxBRzlavqBKwUgz2BIA8uhh-PqNtttGlLWHxjRrwnpHXvyViKLaidtBFfTrREPsDkjaS1ewpM5PwmkLsdhOSS54J5nj2E8Zu_kPbEp704LFCBRlqGU4IeD7otmN3tJVx7aHymALAQIQm2El3aHd_dFYEpbll_mzeOceie04beWrwDK-ok4JkWtlAe6F-BJiQP0jjg6VHQmsJKcab84FPGSsDB_pnk_beUgY42-rqHWmajG7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۰ فروند ترابری نظامی C-17A به خاورمیانه اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135022" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
توانیر: همه روزی ۱ ساعت کولرو خاموش کنن تا به جنوب کمک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/135021" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135020">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135020" target="_blank">📅 13:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135019">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سفارت آمریکا در عراق سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135019" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135018">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در سخنرانی دیشب خود که در ساعات پربیننده انجام شد، به‌ندرت به درگیری با ایران اشاره کرد
🔴
رئیس‌جمهور دونالد ترامپ در شرایط جنگی به دنبال یک سخنرانی نادر در ساعات پربیننده بود تا مستقیماً با مردم آمریکا سخن بگوید، اما او از این فرصت استفاده نکرد تا به‌وضوح چشم‌انداز خود را برای مسیر پیش‌روی درگیری با ایران - که در روزهای اخیر تشدید شده - ترسیم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135018" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دلار هم اکنون 188,250
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135017" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFfjEPBx4jbrTSnn6ES6ptA7D_qfM_sgzh2Uvlx2VvTy_tQJqiPcFzqqJ44yUmy10nDiBZrBw-Td4LOoNI1SfNGYyTTiqlJcLRj-_lyWAosDW_eBgpkFKyrTIf_09wYH6sgZOhiMy01Z_ylIwf_IDUu6I90XJoyyzB3C_NaSQft680s_ojsPVH9pJSbfSvf1MVt4LXPv-yoYAdlkyEFjo6TCx09rcyKNFcepGhAPkEe-AKgqCCzSoGu3KXXYvH92tcXWC2kXsnaWVnusf5jfU9q1iIBvesjORtafxbUAP9rPDgWYN2abIFCFmt0Pjm2fArqip5jxBmQ5EAwk3uQLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در همین حال، ارتش اسرائیل به تضعیف زیرساخت‌های حزب‌الله ادامه می‌دهد و گزارش‌ها حاکی از تخریب گسترده در شهر زوطر الشرقیه در جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135016" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135015" target="_blank">📅 13:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع امنیتی دریایی گزارش داد: افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135014" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135013" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/135012" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آمریکا: حملات ایران به کشورهای حوزه خلیج فارس هیچ تاثیر عملیاتی بر نیروهای آمریکایی نداشته است
🔴
سخنگوی سرفرماندهی مرکزی ایالات متحده، سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135011" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لغو پرتاب استارشیپ؛ نقص فنی موتورها پرتاب اسپیس ایکس را متوقف کرد
🔴
شرکت اسپیس ایکس دومین پرتاب آزمایشی راکت ارتقایافته استارشیپ V3 را به دلیل روشن‌نشدن چهار موتور رپتور در فرایند احتراق به‌طور ناگهانی متوقف کرد. ایلان ماسک اعلام کرده است که سیستم خودکار لغو پرتاب به‌موقع عمل کرده و تیم فنی باید دو موتور را تعویض کند. پرتاب بعدی این موشک غول‌پیکر زودتر از هفته آینده انجام نخواهد شد.
🔴
این حادثه درست در زمانی رخ داد که اسپیس ایکس پس از بزرگ‌ترین عرضه اولیه تاریخ، فشار زیادی را در بازار بورس تحمل می‌کند. به دنبال این لغو پرتاب، ارزش سهام شرکت بیش از ۴ درصد افت کرد و به زیر قیمت عرضه اولیه (۱۳۵ دلار) رسید. این مأموریت قرار بود ماهواره‌های نسل جدید استارلینک را برای راه‌اندازی پروژه دیتاسنترهای مداری به فضا ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/135010" target="_blank">📅 12:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otUNFHIq-Czsj7HRzFllij3-Uuwq_A5Uh-BUKu_hBT6JbH-OwEJZ1yPikFnI4inuE_LXUZ-n7rTf8dzAAO2EMPwjH_y8Dt5UjHZ3JOS36eWjHeyKusjf5glV_jZ-5jPqJbhuPon43DHE2UnJ2iiAQj2uS5lRr_txQ8umi-rO4yaaOYA8GQ_sbEoHs5owi7b7ff5f21G2WhSCluKVs8wtBspJmrz0OXXujPv1ihLTB67iZW7y68D4hgjWoEKW4OulaUNzx0YHegJWRRpoVrhambaS-Gy4Jw4IXDSr_B8KUrg1Zn3KlOBPTdRUwvnMzAgXKuEQZvA5vAhP-OI7oxMA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد برای اولین بار در جام جهانی، علاوه بر جام؛ انگشتر قهرمانی هم به تیم قهرمان
تعلق میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/135009" target="_blank">📅 12:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/135008" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N11mXOvQQGXXOgvoqqmybRqUKOr6G1_0aeCgPM7Bxwdw7ufgOicUkYOiz24gQaVZjCHYlod7WtUBF1Pq0rlfS7S-9kXRND57eFIWRvNNen8boZFrQgsfQXRa5Q0Q9OQB4tTeh7io-Jr88nH5fzGqtXK8ueyPFreSjAyLZ0twQXumoLB9WFSJdJqOOUSWGnDkmy4ASSzRQrWaE_Lt4B414lD7ub1aNk1Jh-OvaFPQ5oMoKbZspFokECBC1EXEXi1-tdsyR49MAyFbdlQa2BklMhQtYp8oQGJCBWoO9z4zM7_n3oKEvjj2NafLpu0Yu6ZfDTE4wstNx737QhW5rtm02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست کم ده ترابری از پایگاه‌های آمریکا در آلمان، یک پرواز اطلاعاتی از خاک ایتالیا و یک سوخت‌رسان و یک ترابری از آمریکا به سمت خاورمیانه در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135005" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135004" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135001" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFTsyCF-4RjihZFp5G5ox4iJvq6lCZpGjtclfuEdHP2SjFZ1012QsofxjxRjEMajeBehXTGFygnOc8mnUGdUsWIcQogWdUSg_U03mbDIVeKB0fKlykQphWyf4U1ax6GsGf_QQCjaBQDu9F6KYr5_8o7KxBixIawvBIdmAyj0iucauFSuDimgnCB089BGoOVdqpf0vinYMbQdbOlfe9zSTH8OTmHIDJG5jCk0pgZVsUDXO6blaNEghnivf6KPS9AZI12xWwUsTSxtDn83Ub9I0iM1A5DVZwDqWEmKecQ6WKdVI3fQgwd2wKu1-wNCcCebrXZO-3s29pLEne5zLAlLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا صدور گواهی امنیتی SSL را برای خبرگزاری فارس مسدود کرد که این موضوع باعث میشه اخبار این خبرگزاری به مرور از گوگل پاک شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135000" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سپاه: چندین جنگنده و سوخت‌رسان آمریکا را با حملات خود منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134999" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شبکه‌های تلویزیونی که این سخنرانی من را پخش نمی‌کنند، باید مجوزهایشان باطل شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/134997" target="_blank">📅 11:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس پلیس راه مازندران: جاده هراز به صورت موقت برای اجرای چند عملیات عمرانی ‌۲۹ و ۳۰ تیرماه جاری مسدود می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/134996" target="_blank">📅 11:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
🔴
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134995" target="_blank">📅 11:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
اسرائیل در مورد نقشه ترور به ترامپ چه گفته بود؟
🔴
اکسیوس نوشت: در جریان سفر ترامپ به آنکارا، تل‌آویو به واشنگتن هشدار داد که یک مقام ایرانی درباره تلاش برای ترور رئیس‌جمهور آمریکا در زمانی که او در ترکیه حضور داشت، صحبت کرده است.
🔴
این اطلاعات باعث افزایش تدابیر امنیتی شد. از جمله این اقدامات، جابه‌جایی ترامپ را یک هواپیمای قدیمی‌تر «ایرفورس وان» (هواپیمای ریاست‌جمهوری آمریکا) بود.
🔴
با این حال، مقام‌های آمریکایی گفتند این اطلاعات بر اساس یک منبع واحد و تاییدنشده بوده و جنبه برنامه عملیاتی واقعی نداشته است.
🔴
بر اساس اطلاعات اسرائیل یک مقام ایرانی در گفت‌وگو با همکارانش گفته‌بود که ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🔴
نیروهای امنیتی ترکیه نیز این ادعا را بررسی و اعلام کردند هیچ طرح مشخصی برای ترور ترامپ در آنکارا پیدا نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/134994" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نظامیان اسرائیلی با ورود به روستاهای «معریه» و «عابدین» در درعا، مسیرهای مسدود را بازگشایی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/134993" target="_blank">📅 10:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/134992" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/134991" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی صبح امروز، برای سومین بار برج مراقبت دریایی چابهار را با سه موشک هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134990" target="_blank">📅 10:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134989" target="_blank">📅 10:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
آکسیوس: مقامات کاخ سفید از گزارش‌های اسرائیل مبنی بر اینکه ترامپ قرار است روز دوشنبه با نتانیاهو دیدار کند، متعجب شدند، زیرا در واقع هیچ جلسه‌ای برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134988" target="_blank">📅 10:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری یک موشک بالستیک توسط پدافند قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134987" target="_blank">📅 10:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAMpExEY4Kg7hG3PMwOI1LXOC4aXuo7D3DcpsqhAxkh419O1vDujqUDtt-DShIcM91DPw_w3WJAbMbGCzf9PFJT9nra6g2zACohj93gdlfXsmorTG3u2P9nu-AsSK6sGxI1Y8uukEFwWhZ7UZnriKqB2SNFkkSIY8LGV7_zUfavIVoMY12Qx79oAQVHHgLYglieGrQ4sJu4S4DZ_f8J8ghKewkb6_SmWuiN-y75DjuD48chtrlLmmmS2-JzvkS2LoXHx-qc1uS2VFblsZxgeyatKKxQF61d3HtuKn9g5g1EqxHTrLA68OpmXJWxmPJtCNwimxRgFKcNE_a0BkFnDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور:روزگارتان را سیاه می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134986" target="_blank">📅 10:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY12AjdKxrqXbpWM-qKC_tJooi0Glepan7Gje6JvDk5bL6PC5SuVxdPo65Oe2Z59Jfxqg0_RO-anq-4UH9aRbLwSVgJq2GWQmmwmzfB6w0J_nOzAfsoiN2BwusVJ3xtXzGJKS8e8NoF34jeRTIcV4dHqH9MNTFGxbLlispZKEKlFPNu3KJen6ni4RtHIEqmMIR1sgcy-1-o-XhGr2znO4CoJnpL9oaMFQx_q1pHdeg_TvREOeUHq_eR0J7yYsvteUEkPY189v-Ch4o6GlprnMsH0P9631c3H0-GRF6RpWHVS6ret55KIOchlaRe1tdnadCM1X2T6B7nrPg78SiBSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134985" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی: پالایشگاه‌های نفت در بحرین مورد حملۀ پهپادی قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134984" target="_blank">📅 10:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSiO6Tmwb4BIbmcTdMwsBhNflnK9dZiFSz1_8mOUWy6pvRUFm2fQQlJ-3h3NZnINNTqav5e_TT7WfOCfP5__qzQHax9ntJAhb4OSe8nUb8f52K4il0JqBll182ef7xTzQaZX6sQLPKk5d_Hd69TQKTfn6uy1UhK8GFEB8SMF8UX7Y9GIfFpwdl4TbBgHX1BxtjlTqM8t65lfITyjOa32-c6ts2uPCiCeX0ECXsAgwhUKzDjNnGjX30zfvcZJ-SxTf6DSMK8QXb82Xa1-jdTqnsYBwmVJL8Md6k2xwDgwgG0DU--VvrBDEVKXL63tThFkKj-SIulqgXS2yrOnrozNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: «تفنگداران دریایی ایالات متحده از واحد یازدهم اعزامی دریایی، در ۱۶ ژوئیه، در خلیج عمان، عملیات بازرسی و تأیید ورود به کشتی M/T Wen Yao را انجام می‌دهند.
🔴
تا به امروز، نیروهای آمریکایی ۳ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده‌اند، ۱ کشتی را که رعایت نکرده بود، غیرفعال کرده‌اند و ۱ کشتی را نیز برای اطمینان از رعایت کامل محاصره دریایی مداوم ایالات متحده علیه ایران، سوار کشتی کرده‌اند.
🔴
تنگه هرمز و آب‌های اطراف آن، به جز کشتی‌هایی که سعی در نقض محاصره دیوار فولادی آمریکا دارند، همچنان آزاد و باز هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134980" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کنست رأی به انحلال خود داد؛ اسرائیل به سمت انتخابات زودهنگام می‌رود
🔴
پارلمان اسرائیل با تصویب نهایی طرح انحلال خود، به فعالیت دوره کنونی پایان داد و مسیر برگزاری انتخابات زودهنگام را هموار کرد. انتظار می‌رود زمان انتخابات جدید در روزهای آینده مشخص شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134979" target="_blank">📅 09:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سنتکام: مسیر سه کشتی تجاری را که قصد حرکت به سوی ایران را داشتند، تغییر دادیم. یکی از کشتی‌ها که از دستورات نیروهای آمریکایی تبعیت نکرد از کار انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134978" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFD5yRMkvkAUcUaP9irlE8RcN6YwLv7cpfk9fgeyiGry0UiEttwig-OMBdbxiC_8mczLxeLlX8_ghUY1a4oXcU_9zavmRQ5RX6yT8yg7yEA-f1E02PKYJUGoQopywkhzV57UHLBlSUN-hKUiO4BtgFvsxHU-8MXtdFCsNXeclU6UPhT1ZLO-1-F_HjBK1d2_FFufof0DeTdBBFScfV_UaxYEIVS9OvBDlwlY70JXM1pxZk3WB5yVlSxrBt1Q7NzE6_HRmQspjdxPXI23vfW9UaB28zPOh7TA30z2LHeQbpZa9wN9ikR4Q78aB3frLzUePoGI9jT6Z9U3IRUwL9U5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که سه انبار در منطقه نظامی زاید در نزدیک ابوظبی امارات، در نتیجه حملات موشکی-پهپادی سپاه پاسداران در تاریخ 13 جولای (22 تیرماه)، نابود شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/134977" target="_blank">📅 09:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ1KQv98nzB2WwxRwFP67tDiYVmLfqOcJK18XJG1qdEqTw29DIdC86bUBaJYmhC8EHor5_SzPAGplJlRrSO7Q8eluZnRUnf63BJyT36AoPy6-I0htBb3k46dkWtHz-1Xi10AN4EWlY3gd9hW6ZRV1ojiNH4BzOnZgfYAxPrttBNeJXgLbi_ZR434SeJ2JEdzXwPz3dwJtyMcuetfFEOayIFwCBjw3E-pxa2p5rD8qZLFBI2N4QaLe442s2f5ts9hQx4mHtQgau4-1KoEZAtpnFUIBA0szLpoDKmfEboMpXxxejrSvc8xa8J2JJFPkuKlUmS--ffsyeulWwI9Bg3W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردن اعلام کرد سه موشک ایرانی شلیک‌شده به سوی این کشور را رهگیری و سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134976" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: قیمت نفت با تشدید حملات آمریکا و ایران افزایش یافت
🔴
قیمت معاملات آتی نفت برنت به میزان ۱٫۰۵ دلار یا حدود ۱٫۲۵ درصد افزایش یافت و به ۸۵٫۲۸ دلار در هر بشکه رسید و قیمت معاملات آتی نفت خام وست تگزاس اینترمیدیت (WTI) آمریکا نیز ۱٫۰۳ دلار یا ۱٫۳ درصد افزایش یافت و به ۷۹٫۹۸ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134975" target="_blank">📅 09:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات موشکی ایران به پایگاه‌های آمریکایی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134974" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPsRbdD5toprI5GrBP3uXL7ak4BAJkv3ZhyaGUMMo_Yd7ZXPCatvdC2f6dlrQRpW5tbLvNJHeBDbjPUg77w7WTAsfFPaJkf9GYw5a3NSyAglPMXDcJBBBCWGf513W5PqtisvFb9Y08Xmv1bpPAwuPidzzuOHd2mqBh_ePVoU5-OtHBGQU9X4NQNSVnA3vCiBDembTYQrOBJmfPN33u5_CVpfoqaZ38bIn4fF4PRLN3xmh1W21XIkw99gkVZvafQpUYvEGVHAs0ZBLNIAjNdXnSaJJlaSURa6_E--ogV7XoIMcDQ7J1NOB2od241mA95DMrkh0i1lsbJGYEdZgBbRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134973" target="_blank">📅 09:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سپاه: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134972" target="_blank">📅 09:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام بار دیگر افزایش یافت و قیمت نفت خام برنت به ۸۵ دلار به ازای هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134971" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پکن: چین و پاکستان خواستار آتش‌بس و از سرگیری مذاکرات بین آمریکا و ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134970" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/134969" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=s8u660rjdJBthM1xrVUcF7BZRGxvNxCfkPK2Caxaly6pzBRehYH0S3YJ56-L_GxvlNt2VfC6KnG2VHd4ruq8bsoRgk30jJ-ZlGtG1RtDAygZyy4ULMKjb2S1sr9ao3Uqq91mmnc9SY8BfapWHtA9yZlAhFkAhz9XsZQH2hH2exriT5ofuj4JMEM5rSHTl3OlvjCOpiPetyMg9TuPw-fBZ1KbO2j_a3EFG1jpY2c5F7OQ77du84aD6hawK1aqDeBmGFp3ydx-NQTS9BR-hfsFS1FXij4hBzVh1gmqgrYhR6J9ti0EcJc6p_95bOOU4QKLB4RxSloIq4F9PSgOsDeSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=s8u660rjdJBthM1xrVUcF7BZRGxvNxCfkPK2Caxaly6pzBRehYH0S3YJ56-L_GxvlNt2VfC6KnG2VHd4ruq8bsoRgk30jJ-ZlGtG1RtDAygZyy4ULMKjb2S1sr9ao3Uqq91mmnc9SY8BfapWHtA9yZlAhFkAhz9XsZQH2hH2exriT5ofuj4JMEM5rSHTl3OlvjCOpiPetyMg9TuPw-fBZ1KbO2j_a3EFG1jpY2c5F7OQ77du84aD6hawK1aqDeBmGFp3ydx-NQTS9BR-hfsFS1FXij4hBzVh1gmqgrYhR6J9ti0EcJc6p_95bOOU4QKLB4RxSloIq4F9PSgOsDeSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت پل کهورستان در محور بندرعباس شیراز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/134968" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIiRert8UMl28JHX2vUXy89EOf67cie6s97oeH3cgimVxV8_KtOU4JOvKbNos53DQ63eD8tciWYb4pecx9fI84rsbhkg4w8Tgqpe7yOx_QkAocNiUA5KtkR-6Ze1YeGbA_bSI3-HnZRewKoURl9cLa4ijhZ77JD4eDT8k7LRAu6sj38fCGgSFuY3EGUQUGOy6CSzwMOaHNe6NLZR-ZjEfItSTWd6HqqHGt-q-vO6LXxQ5RNRpFppob3nYPkmAbrKS6bf_6_BtSTy6mpcjYcnghfzXlFpaUTb5RsSNnfcM2hJDMaQD8yIDr9fkQjXXkTIDJitZXYRLq96-W2vLhR7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در
نزدیکی فرودگاه اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134967" target="_blank">📅 09:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913d736794.mp4?token=ghKMegSwhO2VwzU7vEEav7obvhFR6Gmyk7uCHF5RXPYk9UxpNPVZGnjCvI9vrOY5uRdCUGHpDw0DdTDFbk_SHoc6H3ohkICj78DqMVGhSnnZfY7DaMSMDhrnO1K5IQkfvqOvldVLa6-op2DzLTd_b8jrNvtiX8b3bKwwHVNI5SF4U80HYAM3NmgivM0krO6QPxXbuNDj06GGk5pRNNLU1YXVb0HRnEbkgnPrvSV3BQwsCNdJYYdreUfTph9R-VRuMDX5T1NHHgulTnK0KTDv42_FKcMLOu5JL9ISKVs90s0Im10K-i3yBWREbk57mM7oD4bvZ4QYWH6r1FJI7JpdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913d736794.mp4?token=ghKMegSwhO2VwzU7vEEav7obvhFR6Gmyk7uCHF5RXPYk9UxpNPVZGnjCvI9vrOY5uRdCUGHpDw0DdTDFbk_SHoc6H3ohkICj78DqMVGhSnnZfY7DaMSMDhrnO1K5IQkfvqOvldVLa6-op2DzLTd_b8jrNvtiX8b3bKwwHVNI5SF4U80HYAM3NmgivM0krO6QPxXbuNDj06GGk5pRNNLU1YXVb0HRnEbkgnPrvSV3BQwsCNdJYYdreUfTph9R-VRuMDX5T1NHHgulTnK0KTDv42_FKcMLOu5JL9ISKVs90s0Im10K-i3yBWREbk57mM7oD4bvZ4QYWH6r1FJI7JpdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ستون دود برخاسته از مقر گروه‌های تجزیه‌طلب در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134966" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فارس: آمریکا دیشب ۵ پل را هدف قرار داد!
🔴
پلگریوه؛  مسیر بندرعباس، خمیر، لار
🔴
پل بعد از روستای لاتیدان (کلمتلی)؛  مسیر برگشت بندرعباس، خمیر، لار
🔴
دو پل مسیر کهورستان، لار
🔴
پل نیمه‌کاره؛  مرکز بندر خمیر، کشار، بندرعباس
🔴
پل روستای مارو شهرستان خمیر
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/134965" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vaktg3MFHk5hlT2WQOqg1zynrvvQWmdpz3ZdJhGB7xClziJtQAxtYxMyT2nfeUQN5pRTsbNgg38IWMgw4IyM1wOobvNwyUGef-ZuPP8Svvk_Gi6kg483kYXRtqCaZ7QZyIgsQQx8zKBz8Jnhc5T5EqbMUqY-XP1LX0Bg71NsjvYWhbhb6iI0UoZOwKVryLCd9DNQaO9TVmZqP0Fn47LiTB2_CuA22GACw3u8YmhCBLK2DMVjBw-dpzvirLLHgeOQ4oFwHsT_9raAjjGhYrGla1_TP-fpLmqUImg7DUWBQYdgZsoRTCHjDtDgB3dAywAIOLuh-OpuVjS3rSriGcx0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهباد آمریکایی روی آسمان چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/134964" target="_blank">📅 05:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ در پایان سخنرانیش: ما قویترین ارتش جهان رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/134963" target="_blank">📅 04:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/134962" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
