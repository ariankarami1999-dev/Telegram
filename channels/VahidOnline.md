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
<img src="https://cdn1.telesco.pe/file/eVEaO564dMWqWLswQme7ToGTJ745mvUJgUyC_mLYfZb7IY1k0bOleiKae0kCFnVPlZJEmJtvlVI_QTWu_2TUl-DKq7Yr-x7-s9B7ZoH5KZmZKXhgrxGbnGGZdsgcyhvUnDdcf2DqcQt3cyfL8IQnkzpXfGol-rZYsbZlbwTrXcre3Tys3hRuhSjkXi1Z6An3pLUAsBEQFXnFdZ6VPGylnvTe0iy-0o0y5s3rdEX0m4TTuE4LoqhlXMzeTc6bcZ11pVOlGk57rYQPllzNvPsqnsiCMFc53D-V5BGWVsgfQV8ITT3eHoPR0cIaw6-U12ucHqLG8rGIRuOl7LaceySLJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVlPFgi1dUPNCOFa9Bhc7C_Vxc2YUr9-lRKSOdwAAmSdaMZNuohFnjpCYc4qohk6ff_7YuyvNc9XjMLBAxsOgSAG13rpasB2LCnqw6GD-u8kyTxJpopWByPxwLAZ2SM4lDlqn21ubdgW7VODDKmRr0JmPBlwRXXJURPRyl9SLK-fe-cm44apNXIjpDtFwkypvZhlpxmakn9VoDVEM58zJfhBp3VHquP6eh6S49NsNhKcEiqkWCrBxLIhGMWjY791msyf1B6S-tD3NGf4eSJLeZ44QnCna5SA8lZo49f3eFLncm7KzXJHSNnPvRf7fCgYR1hTZyG9sSKB1hkjk0YndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=rxfZ1d8eF5yjQ3UezkpeaUIRj44OqroGAoeZM5vXjhQmHXuZmhVpsqDJVH8oZnCNNXb1tKX2gBNtwgrU8ZC-wbGza8HdHvL8JCa-qM3_II_7nDKCpeJIf8qHIbxt3J9rkv-QOwJga2hMU8kExe-F3RcRpmv2hqkVqszD3s_5cKm-vP0xW_luQ4IAr6fWLNcGedSxUglL5O-dFdNAuatx_cewPAygRGtjeI_YbnnnV0GVbIAEL8nr4adZ21aKHvCeQ7HIgnhTXUH_0BStPI7na1lB5kijhXeUVFqD2Xe1e720oGOzUCsD20tPrdlcDomh_RL6oneLWGI2EtiU5ZK5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=rxfZ1d8eF5yjQ3UezkpeaUIRj44OqroGAoeZM5vXjhQmHXuZmhVpsqDJVH8oZnCNNXb1tKX2gBNtwgrU8ZC-wbGza8HdHvL8JCa-qM3_II_7nDKCpeJIf8qHIbxt3J9rkv-QOwJga2hMU8kExe-F3RcRpmv2hqkVqszD3s_5cKm-vP0xW_luQ4IAr6fWLNcGedSxUglL5O-dFdNAuatx_cewPAygRGtjeI_YbnnnV0GVbIAEL8nr4adZ21aKHvCeQ7HIgnhTXUH_0BStPI7na1lB5kijhXeUVFqD2Xe1e720oGOzUCsD20tPrdlcDomh_RL6oneLWGI2EtiU5ZK5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsMzyt8UXBgX0yTcgwZuQNNhxtvOuzfP7plO58RNaZ9sYVOqB9yEDS-5NgAHOgkOJIRU8WO6BMx-pMlA5t_u1nWxsPqCsKkC1mfYkI6aVnAks6Sboklkp1F4hjQTTr3nqotYiI9UUKOc4NvbcJ9r86QQuegznClZ39YELWXDiEibiZeR3sa1q-TZ4UiBSFbD1PEg5tBgZklwLgQMvADwd_fhNRzYAg0LW9neiUMJOSmYD850-nvvteIoDKUYTjIpSy8Nc9Hv6FxokS1PMHT8jZlsIVmLIpBqT-AnNDE2oysW-pZ23mLIOxYf9DA21r2ES0ZK-j-NlILTvkqWVP-oXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=A93U81RZbazE5B7sOqi1LPEy6xFB0ATVYVTfd5NCQvbijTdXxAQcZWFb3iuweu9dmL_r6ypOEVPjYO5iGl-u3rAVlhYEr5WLpp7wYa_bKh43KCdE6eWT-eZmRmZbqmtbJ7NlLJ3xGqTE5GRn7r2mKfkaXuJXqiJBDiisEvXWX94VDNME2V_pJw3e6pFXcR-ugBi8AvvOD0QD2exFZc1n6pACubNI7J3uB08d8my9XCdbxl1r0nV7iIaeyYrLTi-6mOk24sEJZefOfmuMfdg8uFSYPQnKn_8ApITeKXAc0bKU9wfMXGzpG_2IWGrYNasDAG21DUE-qo0OvwwLKOQSjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=A93U81RZbazE5B7sOqi1LPEy6xFB0ATVYVTfd5NCQvbijTdXxAQcZWFb3iuweu9dmL_r6ypOEVPjYO5iGl-u3rAVlhYEr5WLpp7wYa_bKh43KCdE6eWT-eZmRmZbqmtbJ7NlLJ3xGqTE5GRn7r2mKfkaXuJXqiJBDiisEvXWX94VDNME2V_pJw3e6pFXcR-ugBi8AvvOD0QD2exFZc1n6pACubNI7J3uB08d8my9XCdbxl1r0nV7iIaeyYrLTi-6mOk24sEJZefOfmuMfdg8uFSYPQnKn_8ApITeKXAc0bKU9wfMXGzpG_2IWGrYNasDAG21DUE-qo0OvwwLKOQSjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJJ4ZRcpOxMwDZC7euPelEoJizclgvnOGw7sIvL5WfmLHz3ASXZIcnzViwFgXuW8Mr1unPDFhJdw8ZFKo709PURz3WTseAuZe4Sdu5IzjHTL67oXNXdIcpNVQGQ7anMmZ6ZLqu01jJFpRWDoXFpygt24qIujGsOK3mg9i2p3k_XJuWOJQi_5VbDd_R0vUu1Ik7PokZq1RFK0tnIOguira2cJLmGB-raf7JsfDDT3KWe81n4ktik5Rs2mLxfxPePw0qUDsZMq0fDEgwcOw58hvAmuyeS7NoQGxIcbGWQ8-Rm3oItO3ZQqQ6VaUVJ4x89u4NaNxkhcM_82ncJZ4rqiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXFH9k1UoOChT8Lt8YFEnrZYagYN5Xkkf_9fPQygi12uF1rRpqrxwgu9wQFPKOS-DOQPtxci1_7jqhomRsjgrYSLpGeln6ouo_iZrgiDdnSrvVTO6FucXpqP01ZArYlz4-_KFZ3T-ZqvLd1ykgqAz1jWHyYi4fhTgb5iWuNS9B1QZ2JMaeivk0kTVTc75hgBkRUpFvZcInMFrDjDCVvCNPph-EAm1VLruDz2UNU2A2TWwQBkwyU73p-7oSypwpNvi_hMcorOmYGedBGFNZAz_NAPrcrSB5QQ8f703NE0si8Df20mPv97uRGytbqSkxPPAUChbW6xW0puQyJHPFEWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJA_iUsSMwAyS2U4aPVgDI4_4OGvHL2zfXGrhscR2qDfvan062xW8AItx_zMJ8oLhnI-nSQ2q5X9cBl4yTyjC9c5tqMuC1PHqZas7_cEwzK4WtmKuEAU94aAUdPnhlwTdjg2pFnsDHIV7A-UMEr8Fsbax6Zz7J9mBci-GFYxa6hWjdnCbYk-2S4OsGT9uFPgQcAciQja4hx2CRoFtVPKTgFXt1lanNwNj986MV7AoerLAf5zSwh1rVBYC_3nNOJhs8zqVscemmNKR3LVAgC7a5Bqmkw8xvJs-yrGQUg2_iXgSoLJ4hzLHc3lvRNvzyy84ECcTdsn0Vb5QgrOau0ScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرنوش پارسی‌پور، نویسنده، مترجم، تهیه‌کننده و فعال اجتماعی ایرانی، امروز در بیمارستانی در حومه سانفرانسیسکو درگذشت.
خانم پارسی‌پور که از دهه ۷۰ خورشیدی در شمال کالیفرنیا زندگی می‌کرد، از هفته گذشته به علت سکته قلبی در بیمارستان بستری شده بود.
او در سال ۱۳۲۴ در تهران به دنیا آمد و اوایل دهه ۵۰ خورشیدی از دانشکده علوم اجتماعی دانشگاه تهران فارغ‌التحصیل شد. نخستین داستان بلندش، «سگ و زمستان بلند»، را نیز در تهران منتشر کرد.
خانم پارسی‌پور در دهه ۵۰ برای مدتی در تلویزیون ملی ایران کار کرد و سپس برای ادامه تحصیل ایران را ترک کرد، اما در سال ۱۳۵۹ به ایران بازگشت.
او مدت کوتاهی پس از بازگشت به ایران بازداشت شد و چهار سال را در زندان گذراند. پس از آزادی به ترجمه و کتابفروشی پرداخت، اما فشارها ادامه یافت و سرانجام به آمریکا مهاجرت کرد.
خانم پارسی‌پور در سال‌های اقامت در آمریکا نیز چند داستان بلند و ترجمه منتشر کرد.
شناخته‌شده‌ترین آثار او در ایران «طوبا و معنای شب» و در خارج از ایران «زنان بدون مردان» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K_LMdNiEbmdAHT_1a-6WQ4anR0if3ztf3aEOPpH0WLCHEv49hyYwsRkMj011RX8IR6IdoSKVcZ3n7IOzBXZqCuX70Z5Xfup6dUAXzf-jD4NHFOFoEMe2iNQqNj6u9Gvx0Xiezp5H-wPEY-nAvlyTRpL_NwPe78qthMZYu4zCeZXFABpcXEOpELis3E4fDhXpxG4mal_Qua-TBU9rpcPuEXGqK65S3QrqKz0OOhZpjSU5Ur8dNipBSXGVOxfRfDMgw4L1q1spBpfVC2xmFxkCbsuNg6sGYY9Sc5ouHn-wSPestAOuTUBWFgEdIEo61wl8XFyj4q-_79tTJInphUVKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/spvxllDZfpMgFnMfP_1sR7B5m9rlRK1C0bnQ-uAsHdgSb11onc0vUceuE0VYH7Rj-JqK0_QNdw8iFghGMSC6-bYVdQEkwu7Eol07V0CcG6c8csyPSqUhHfnzEyvBSQ4CZWMisebdXSZoVjS_xJN73ewC_pVgjZHna0VYzt8AY-rQYAgVkpYxKHUJVPd4q2XEKq3mVrlugxqdeHdOMIGG235JrkDGUsq3-_LdoipmaljfV4ovMsuhF3fAmhruP1WOVW9oP0OCp6UofxNafkhVxbYvPlFY3vQgWhdRGMKuXHVf4P4l3SwpjgjpUvGl2JZEIKY7s5eqi0fUhJ3td5lUZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=UNmM4vGJ7-JPmY5UzvD7WeOD7KJlWevwPM8uhjAXSYmGI4zP47l7BVrTlbJd9Hm2gWzxPoYLdgKhMD7laErKNwx0MbwRmJDAwPQbHrPnEvQBA2zVUilA9f49_FoUtK5LsJXk7BVZEYwbzlPtkgRGeDhHlNgYsO2qnYbNmSzkeWHNjHmH22fV_Yt1E3eMa4jcEQAxWssACSumLHY2EJbtW_d9MEbnGs3zDwlxkM8qG1_75PZIRABXCabuP_HKt6wZYZHICNcmc5-Jg_157rlZfSl1MehWD2EqgSgVvT_IxW3aYHzLGU7ATU-_GrIPhqTLgwqqxLP13akjeySQFpqbqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=UNmM4vGJ7-JPmY5UzvD7WeOD7KJlWevwPM8uhjAXSYmGI4zP47l7BVrTlbJd9Hm2gWzxPoYLdgKhMD7laErKNwx0MbwRmJDAwPQbHrPnEvQBA2zVUilA9f49_FoUtK5LsJXk7BVZEYwbzlPtkgRGeDhHlNgYsO2qnYbNmSzkeWHNjHmH22fV_Yt1E3eMa4jcEQAxWssACSumLHY2EJbtW_d9MEbnGs3zDwlxkM8qG1_75PZIRABXCabuP_HKt6wZYZHICNcmc5-Jg_157rlZfSl1MehWD2EqgSgVvT_IxW3aYHzLGU7ATU-_GrIPhqTLgwqqxLP13akjeySQFpqbqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=LhrW7MV7mfHWfRysCgBKEh5jSjx7OFJFTPsOB6wGcyHA_Y44itSTdS8B3k3fpa9PIW64rPwmDXKJ6YhPpL0NF1WWK6LsgGA11Qd5ftHR7Co8dKdxKJ28OCKlFHNxiwrNLtVlyqmFtCGAu-wDKTY_Dop4uXw5V07g4V8gI5nR6Njn6PHGxMRxugC_2rxGniOY3UqEu_lJzF0s-3Eur6ylSUr3B7U2QzTlJCObaZMZB8i4LuZ7eoYiESuIkmRWAnD07gus0YdF1fbIlfHXv4yajHObkpewLFeSqTs0UZWVINr2g7q3Bx417UJ8AOM0FLvMlk8HUSSBiPaMe5Iuo5Q2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=LhrW7MV7mfHWfRysCgBKEh5jSjx7OFJFTPsOB6wGcyHA_Y44itSTdS8B3k3fpa9PIW64rPwmDXKJ6YhPpL0NF1WWK6LsgGA11Qd5ftHR7Co8dKdxKJ28OCKlFHNxiwrNLtVlyqmFtCGAu-wDKTY_Dop4uXw5V07g4V8gI5nR6Njn6PHGxMRxugC_2rxGniOY3UqEu_lJzF0s-3Eur6ylSUr3B7U2QzTlJCObaZMZB8i4LuZ7eoYiESuIkmRWAnD07gus0YdF1fbIlfHXv4yajHObkpewLFeSqTs0UZWVINr2g7q3Bx417UJ8AOM0FLvMlk8HUSSBiPaMe5Iuo5Q2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSvShkbDkcJAlxvlFhN75enyZ69vRtOCP4yKQjJPEThyYPYmHtVQo4-ALV1SOVjx4ncz7OLY9LV5H0dB0JrkuXPzrZbzYLKFl7Qt78yfijqJtIdahCsZg0jPeQfPgOmvmF6voN4b7zwt0c6jCJf_dyWCbWyf1PdR8WUloWHV_2oF2PI-uGOPjayREgMALxrJeKfSxKUyJ-dRnckzQWMMvWSczp4hfIf69Gm-XuVipGr0jQpkqzmyPJBAxBgVyRqkIVrvLOfFCMfgyI6t9E46_CKPojRNyskhjoqqhkFpSWpTWEWV4g6W0wu-TjYHh4N_0azTzRpN02trScy9IWWcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi7rcPThB814LXaWLBISpyCNIWXPI6VlZhc-Zm2YoJVv49EjESF36O-hIb3jVae6acMc4Bg7750pNgBtpSNFACRsfG49R4hKaH7BaUBfDAvITpvDgQt566hFbMxb1OmeBIt6pm0ARjJ0FWkgDvlG0rqSQ6bUBxX6bPtEAg-lSYotjNTPQiLShrQy33Cq6425XR5CMXbvlH-P31O3E-AgZ23mO76PINAzufMJpeDIdNc4N0BUtt3_dBM3x4POsze7pI8QGVU1u3tlXIxuhj8FBvvTdrZvz5WIuHv4TO8WFskbBYsgo34t9A7qTjrSNj3dgybbALXdgTU3_8vM-vEhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tX44j5UoNuUQfO743i0_GU70dIjTtw3-vRkixDffOQPqKf_Gj4XjrEz7bBkUs_1YXYXhwthSqeOMDez8UOb7bcOEBKPEG6sLjDhzGfc2Gt0OLNRkzrI-HpRXL5pDRKmCdoVX9kJDtJO47SqIoWsUNbcJQ0zI3DX8b3bx8FFjXW9RWQD7O_bBudFKJhJh_PLMc4qGplW-oN1SabUOcIiZRYIM6j3Udys_WmVsejBg9_itFJgk9bDGSwsNcP05wcDB7odZDH8Itka3XuQx1r7vO-AbKkO-dQhZPct6AXRbrLL4DQdnJZhCUiR7zvk2doW_ODPDLhzQZ8SJgCxOw7iqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/piFUP2gB9C9Puq1u_4P1xcwt8-ZtPl947wVbLhbwVtYo4A3J8ns4Tori1EQuvkbeN_W08ggM2qWlMV1uttJftZY_ycjlTswhV9gSKOoYGyxRzbpMw93d98hoB8nKQH6l_2ubHP4sjww-NVW2HFpv-MEoqAM_DcnHD71sjPMFpO3EDA5H9wXjZEG8zogjHh_DpaXH4uKjXL72KDZqFZ7cQHPCbJ8wJa6QP_ZVxtIIEsv4slAoNLyiPo8CaFqEKrlAxnYuTqHgRrI1JIZwWlDZxa7omwQNaFUaj4kFx743hOgZho5n0YWT4ulK31ltJ_3L3n6LHZ5y-8JX9r3zZSsBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_xSB1TbxGcbEtzH1fkuWqC4XZL4sEcXCmrt0_M7QlK0ggFMsPEHHBl__f47FvDQxx9N7P4-1l9JiekKfyNMafnP-igCpHcEDlYsiyghAZM4zMq8RS91K7ERfYVcDEuKdjPn-oJ87LWpIt0Pg_AuihNXaD29wEzyQMBKE3FQWbs_JUK2jDn6551c8UDk-1chTx__BY9GOby7W8S1rTosTg1mMzhqLp0yEXYkjKrTfAUBOfZwoGzVMVbLgSgW93fhiwmRFJqDMSgIeuZx_h7N_zeBhWdD0Lsd_kFZuncN-WtLZCap7zBW8HpLnll_eTAAzKfv_dzyEZR-ZKlJKH3mgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=I2B4Q1alqKYZnKEmlqwdfqCLBwfsFYnzPiW5vlnnDKMOPIMJF3y2axn8dMI3mt71S-l9qLZ9B4KRbGfbOOcpyPC-Ys8s0uvxX291VH-Wc77WB7-5wofse5x_NG4mhek-YfZeC5XUS27eNLcrVBdEjHTEznQYgwNaGR7Dk-Y7fwCx2uIo6lL2jPwUTNQ8W6R6cRjIk92CqfmkAImFD9qsRia6SU45CtZzzPggDo41OsL5CInXfz_1sqqTCsDCu1A2fXt1zyqlsfBS9_f5TUSPRgJyAqXeuiLLzhcfD8IemdFS_hiOUoMkynM2PnT_qORPe8sYup_lMnI4HjioSZ_kMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=I2B4Q1alqKYZnKEmlqwdfqCLBwfsFYnzPiW5vlnnDKMOPIMJF3y2axn8dMI3mt71S-l9qLZ9B4KRbGfbOOcpyPC-Ys8s0uvxX291VH-Wc77WB7-5wofse5x_NG4mhek-YfZeC5XUS27eNLcrVBdEjHTEznQYgwNaGR7Dk-Y7fwCx2uIo6lL2jPwUTNQ8W6R6cRjIk92CqfmkAImFD9qsRia6SU45CtZzzPggDo41OsL5CInXfz_1sqqTCsDCu1A2fXt1zyqlsfBS9_f5TUSPRgJyAqXeuiLLzhcfD8IemdFS_hiOUoMkynM2PnT_qORPe8sYup_lMnI4HjioSZ_kMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BJ-3tYBpv0tyECMqo4O4nfwYqgLio4wJYH9HLaeT2-CWFDwdzJJBo2Qyhsvrty3BOpxyL-LLReLR0VG5aa7ovlCvAhwOys6d9hy69CZTwKjo7WQybRn_xuLPonKZseW-EbxCvmP4b9_BhuvK5-3vybaMBCJVMC5btPHKK4UnEsbxw0UJcKDWVHI3O51i60fdaT5VdD15S4f3HNhmK-RUBqYBDSNIjWJmVQ1UVxuJMAWyX3wd9SsOJSdPNeBFjByGzoWWLlXcdFUIBw2LxZgJNyq3UrMRv2-5tMgEmI1Z4r_CBESo4_vn8QSWBhe-EoZ9HQ_mAMguyUdTlmA-IvMD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d3d8Ts9Ag6GwsP3uYZhHCrBl6_Sb5mfSGKykJCx_YJc9QuVVWvTuZAn1LEA8cy-58O-8WPU30dfOW-1WxEFbZY68tCzwfXZWhbZ_h21UBEl1I8mBZcBx86OvPy8WvMlZV8r0gQYfyb1WB31OGbYYjQhj67-10o6budwowY3L3jRSqigz8hK9XYSLIXiwO3SumE8zHWoO3_gY98nXTE-a4ebrQF3NZ5w0zGVrm5LzXWfYwrvvE7A12nc3XAMPEPungWJHCn9Rx0JyU5cpTg_H74db2rbW_dLaMTnG75xUf621CQtt-A_Xvz8XmhbU-H6YfYYdCePMDjDEYYBcw_uMfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLkz3GM86E8AyWMev1VqFGELFAxSHAUWuIjGDiql2Q_6MefOVOc5R1g9mtMDyJEn0WxuVd-z42wXxrjLzNeguSDRwCm2_lAlONhjWeKn8rAVMuEOtEn4MXURbKsvSXlDXwuW4czRMyeyjCetGFNTiZCDiOasXq9lZ0-HscHS0MRb4KNkJxFgBmoWMN3rcTSL5QYcsDGjnjQ-hYWMZmAz_ECd3hH0DAIj7LDutwBNJvzGFIpJVKREEymBcZYMFvWAtnckRdtfoPBlXDKe97Ozbhcgw7jaWDoGy3NMCYvbc0dunmVgYPFd-COVmuE63cqIFwIfqLlorocFcKasRvmRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=ce5oGVp2QC3LxljzeOTH_-tMf0jek--hX-fG53pQevnMevmVttQCpwaZhZ2_inHYCi4FyNbdUVmFVYiDCD27G9oswfBRy8hCh9eXmMOpZb_ucITRLQNmFuS6hgb9CLZHUwi1rdeewQDa91x-ny1BDa7e3bqZDC-sCs3oIOhv0vboaIVF281r7upU8I9omwmp7EBnV_JMS-b4qx1NkpgQ9fBJY63NOQv65VRwMg_0kAH4JnmPIZbSdqKD_g_GGfz7dqUBlOCb-M_zp7WMzDBuSqD7SlwjLx7QLSg1yNVrwwef6nN66ecxzmPDE6P9okfLGyBpeFXDqV5Tq6MJoT3_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=ce5oGVp2QC3LxljzeOTH_-tMf0jek--hX-fG53pQevnMevmVttQCpwaZhZ2_inHYCi4FyNbdUVmFVYiDCD27G9oswfBRy8hCh9eXmMOpZb_ucITRLQNmFuS6hgb9CLZHUwi1rdeewQDa91x-ny1BDa7e3bqZDC-sCs3oIOhv0vboaIVF281r7upU8I9omwmp7EBnV_JMS-b4qx1NkpgQ9fBJY63NOQv65VRwMg_0kAH4JnmPIZbSdqKD_g_GGfz7dqUBlOCb-M_zp7WMzDBuSqD7SlwjLx7QLSg1yNVrwwef6nN66ecxzmPDE6P9okfLGyBpeFXDqV5Tq6MJoT3_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rlw4uYdIhypPaSqVLf7EadI3VZJi1TQ0EEnEkfrCxCW3TGK7OP7G8R4r3c7GF-UqkRkXWcOGWWwTziV0K-QsXe3SA0k7rMIp3ofAGLIyFhLliKVeJY0h7Fc3WiXUf9jGhHixC202TVGQ417FsGLcWxc0IKLlG2SdGWlQlHLh15zKHsxuwphe9cAHZoJM1YCSRWickOaOUdrEnxKJ1Mij--ArN4bjFI4dUx4pWyglVIhctO6vZUd_0xYPapU-sOjSe3Q6su11bRa7Y7XwsPSF5G1yHinMogii-a4YzHw79dV4vV5yptsbtbYjK9uh7WpbaGZj5fH_W5ja8_HzPHSjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/frvH4-3OU3S34rAun8DW5N6Q_g-qO2mkNMmx7O1P0PNbCja7PYb42LmNv1--ziUiR4INaXdiEKdxnIhP_7wM7e2SaKnwbPoEJVvtcb9LsnjPixRzsX30ShTO-_v_uKbEQdTJGlNOKazX-HhJK2bXzHk12KcjbJJ6pVdA3jWJXMyGCDroTZp40ov6CJ-rlLD6GK-0qXZJw6UytyWJ9EFNez3mfdutzDNweGJ0Chw10Dik_QDtFwKp_dmTFwY32c3kqdVArs3rV2WxJ6MOD7kOMkyWbk-5ssSEZbkc1uLTk-NuWReWwt00Fkpyx7kSLfID682lrYJ30IYVh9oA6RyTcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lAmYdgt5_Ffl_oq6nFOZTYfz5HtEsiTm2_Mlu1LMoK5hw3pfB0okUCipeZUdi2siysxZYrwC8XBvAZUJN8F-zdDVWiIIW0A_8oO2CHwWNqwDe5YM7w7OLCRsX26OKfE6BZk4yJejBNfoLpki88Lj5402JFyAOKMZ7Hjy9wb_CKnM2WZhQcQ40rjJXNXNPPj9ts9kJSaFcERGzVbS8S2M7tWOWg9XC3fafdgCeUbQ_wsIMuQ4tM7SiOoUsAxYAGLJ3eScGpwb3frQ48n-uJNmyZTNtqgrsPPS07-CiqlJOmdFJ5MX0dfM7xU73-q5aXlwk1TAKE2KEqz7_h2yoSKq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NmOCYzMreT7I_i2QEXtqlP_STsJp8ptucOoBR5txTm-28883t5Kvvgu9MTaIJQlpRRjZVHObQruzYV-dSH4OOkvjf5FaUGaoJe_prYyWkBO2egl6AGkuqSqnEusep4QRoj_sV8cysGagBltTdwtWct7T-Pv5y9dhAiHnJX-LpUIC2nLhGtAFrFH-zkeiSN6FPk_r_Bp1JXp5E7zSK1RIClam2y-R3aqY3IIq35ozoLQt1Ei3hFWd86fq7c0R682SprQpOMrBWjGf_DI-CuFDDLd0KDoN8e66EvteRP10tw8qVnk1ictEvqlXpcc3Baw1t3Jr3BinOkQQBYScYERTgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXwKP3b1hMjRBUCdiqGF1WmNBNJC_JkfDMENfYLDWORR4sUQPacNo-wdakJWanyBtHN3PuU8btfKp05kJ7wFEX3gORa-PzFMK4c8n7laeTYOf6b153-_2NJ86fqQl4myOKBwLZFYR27QqpkzoO11I5nQGz63yIQujGFD_AV_Y3eWc3WSMIzUh4V5vnYxqSCgCxy3SQuA9apcttGJ_jxog100tu-jEVtKCPE8Gz_pWU25u8etVi-_RIiYvw1hODCGESwimTytHTetjFPo6U17HutlQ5GvJR4M0t6zFuLi-uXG-8o0-FEjTldCdb5t3xukCt8fmH-9cWDnvh-GG9jEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COb5xEPdYUHyvRUjj4zVEWw7fc2iVzpEJFYPGgIGMQRZVOiMNxH272yMXqQfhfUmIx-tFyYYIwKZHCJCUHSeas3fQe8UIoVXp_7uMmOvtXLpcRHL01FsZcsZDBYzxZzbH2L5fTRh-m5WJc8ie6KBzZkq7kiz8VRfSiGiu4xueEwEeMj4nr4tth1GOjNF8xt5QhrhWgZFsemlUjbyCDcyoPulxLKyWYiaPQDLn9c17AD074lkcBcpH6UplJDHHFO-VA4bQHTKjDe_uJ_Bp9mBtnoZrtOl9M1krqRn8AvMk0dZ8H_UyKlGYBf0yee2UC4Ohfcg617grI36NfAK4yoKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=gxbkity6u1KADkrESwNUJJ0HSlBAo6CqOdAhO2cv8civ_qbeTacuhuTrUcy8iC-sQGZYDTVXM8ItvGtMz2Cq1MmZwCE3BO5y2L4n-IeVJdI1zA33rtxlc7xv135-Q9vja2LNeQMz5YltdZG1hCIY2U35XSaxk-ygk8Vz6rmXO6l1M8B7AzrxkZpbmpRJ48uc-2-LhTGo7SreGq3MOWRwv0c1v5tgBE30OwzroprttJfhUXrDkHFYly5aFN3yUOQhqftMW8cpqxUyfCSafvAmDZ8kW3HfyBcwpoEpl57-oW6aQ8UDJvo-URaXm7WOlogaqNLcH1azce1L4GZt_MKcfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=gxbkity6u1KADkrESwNUJJ0HSlBAo6CqOdAhO2cv8civ_qbeTacuhuTrUcy8iC-sQGZYDTVXM8ItvGtMz2Cq1MmZwCE3BO5y2L4n-IeVJdI1zA33rtxlc7xv135-Q9vja2LNeQMz5YltdZG1hCIY2U35XSaxk-ygk8Vz6rmXO6l1M8B7AzrxkZpbmpRJ48uc-2-LhTGo7SreGq3MOWRwv0c1v5tgBE30OwzroprttJfhUXrDkHFYly5aFN3yUOQhqftMW8cpqxUyfCSafvAmDZ8kW3HfyBcwpoEpl57-oW6aQ8UDJvo-URaXm7WOlogaqNLcH1azce1L4GZt_MKcfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFLdyYeKmOvW96AgSMdpa4eZ7Qd2cqSMFrsFimJoHoE4ObW4_HAV5nnXyusSx0NsZOL_7vqWLV0Y731Ui0rgGIuKBhcXEnGlCw0Xv4VkWgbf3kKzuMqpmD9yZk0WTUWaYvzIqnDLsDGAPbBSqjngwHct5Ls5SIK98XGQ6oIlDqZ-cbximnzIRkcJl42ktDENbbzQya9CBIS0qOkZWTJ9Tz5mO3HTrrR82blmmkXXsC8OuAMqRiQtI8J9AEU1qNA0WQNnarY1pOpMnAySKEUFK9j0cy9qeKY4APOUuBOaCe4I62U_KVzs2-jaWXWGhxW3-o8gkDFDGRRb4Z7p79gPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhZTuTSXngwTkrbO-HLt2mScUa2YYWILDtl4Br0c3LHn3tqS2Es09MWO8kOytRFK4_6GeTc9fWlUaFmWt7uErNKvwGWhou8f5HAainaUmfe1io3pHxL7BRFcSLbss69gOrQtAS2e52eELS5RCCqot0VKpWRVYkD62Mv2V7PoZJayeT3zRg-LRh9CsAC0yjGQSu_BVnCxsYeg__N-M4RQEhGlVUKWxZCH3xzv1b-DDcf9ZlX2vzeiv4_JDtBuUS7DSe4bleoNik4xixqVdZJtHyQ5WFHpB7GmqLgnWiXdwwNn6FakihVHMils-Fs-4N3EUhsAcdPM9I2rCx3HapZW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_xvuZpqP1o-rlWSXOEnuGd3bKsRcQTloPirHkqN7EwxY4Ef8Hr9Z9sHBk-hCpatpE4WKMdPIOoZdi4wWRPkVNflw8d1OwVJxsdhio_k2BYzGBIA7u6wEYGmE1iGL4vYoxThAufMYVKAVwV2vFA323V6wH9LqfTsTWl4NoibPppvoWH5vdYEwXO0vi1rOoplqUb7IJrOA4B--zMhdk0KjeYhPaIvIqna6Vu9I3tVLN4fZKOr4HARfl6z6JLpm3ANAZxSXHPYDZROQ4x-lp9Rq1k0lgPkRwbwbuzncqbiAdJF-dF7vG2uiADypVsfPkP6WZH6VYCyTL6ORCFDIjzW3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KRmgb_ecnkcYkHzzYvr5e-TtAhudUXUZqmgeP8YtWihB12ZiTvvV6F7dpIO0qRXbvfhinAYZnt7SiU4-xN0gRHpzw4WlFk2ChxE9SGA0hUaHU1DvneD_XSVEUglfeMnqJHsl-v6bj3QXG29Ru0oWkxl3MvZFL1T8NdV9ElwdskZ1R1FOFNH29WnFoUV3zxCnaV_KIggiX9p-gI2Uufn5vneBbYCKMgGKN167oLtGJ5Bm6KlTCwO-DMSVbRc9-oEjYv4Kj4NR2vFjta0s1l5cg95OIJ1VKlfhWzLXUcc3vdkW6dUNFsQexQgrXlSabndCQFAxD8AdXdzTlA6mZMG1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EZ3j_UxpMXHnhwEDe1RI0_imjxZM50zep9xuTBZdZybhAdVDIkvGWC9sMcsCVkIlXc_gHRiSrKOqryAvMlf5BgQmWiWa1OLip_vSNqUDYpDvPWRJzW7uD19b1SDfGzeKQbliCuZVIaGjgBoD0e3MyaCHh_pzBS0WGyzZNXRrjr5waa1H_S5L7MAO5RJyyYA7BifZUKZxm3WpzM241W23alD1mJxfJI7oGvStvqWAOXc3oouwcW44Dss48Yo8DhnExmoAEKr6kM4VmzeSD6uoe2NS9tQ8vnHeqQ7elSOF6BXvpMZAdDWeXJE9yNt36J8WUnOIPA2TQ0KwCpwcTuPUeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T53EJF_87Dd5sFJbEcBtrTgSKmzpquqSlzRM-iru6rLzEB5iwDoI8aev_7gSfiGgyntVsdAt8j3qXOe51suCgZ-qIi8S1tGOe7oqYrq_PcgyZsulJaXg9Qx9iijsCZPl_-82GHwX8ge_5joNjA45C4lK8jdhTCfaDvmgWIvXJ9gdN77B91ZmclMDR0F4LLXWg3Ku8S6MdhrkZrI18XvMWQu_tzwWmrIxOx8tsa9_akOKVB48GO7uesynDtuaqwvmEO0ObvhBYnTK_QeG4F54hsekpzer5xZpnBE89X9-B-Dc6b3Bn1KrzVeC-1TjSJknLxO3fYZI_TdU2dXCOx74KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltQesmlWNIwhqT03dc5Jfxpc72zxkQKwD64ffpcNFTMuFZl5x0KHNjyw5jDLGnsgveDcmNpD5sIB4AOF0HetArKAO9UooKQhimpSUmiSj2HvuYOoHLSxpBHoFJKcJOqb5TxpHJ35ecjO91V28QUxNzl3Pmp7AeJCpW9vjMnMGCBCmH2Otiaqd1MurY9I0InSC79yPnUK-lLKYUKAPgWQ0IvNxqepak85fTZgekhVR-jArewyxURkiE7NGIX4Rd4-zbig-bSZ2u8YYtosPqGeE58DV78PbGopCLpMiv2siiQKJQF1-TD9qF1J6UF1CWxYSVfhSKr38fePruRdp9pqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVgBeScBJbc_Q-d3pznr1NGOdeensASFEyLzjsryLAbWzDmT6teRR5mWYCnW5kbpwzR-mn6ZbXSMC2PfRbHU8vaGuI4pMn3GhKhZwhQWRC7TqZWQayLqiqJc4OUQOiy69UOeID75lZ5e0rbrY61HQu2i7TMfzSidjbNY_ptFejXsb44Od6fW2DTiqlkTzVai4Kawxq-4Q_0uE0LMK9VgsoVHwtCpHsqdSVqUT3MObiumUe21J3YlCVPEl_K94hOiFEibzN843_EbeIPRFhNeVyur5qcY_fdXsN8GnROh5Mu-TJENe3-RUNgrNH9nmj7dFCFl_xf6TRWkyomwvcptZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CkSMibuzpTIV4J9NtrPW7aqiPMcI92-wCBrGI2wO3Jj58f7qZiTOoLV5UYcxWCL1AO6GkpVQTLHP05nJCcsPY7ULlXZ1zihNbm1YPY5jhBpMAcPub5CDDWmsuUvQst3LqUyJejwvYD_fcX1JR_kYt0R--mwtORkk9MsjlCBd5NP_h1OOSd_JCiHp1mKNJXdxbdhJguxnMdFoRuuNdc9OdoYXkyUSMmFJCd-xgawql2NSkcC-j811r_cfZWaoDGskPR33C9FBUXJqYCQUyO-TXk8EyK1FIf5YkJFf8dyn9XVYdbb_iH_2c9on1VF3P2n6VbAOJ7buwFAqyLv_9ugyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReHtw143zk5oSMrfggl16Iqzuy441THmWShDHdQkAFmrthMaRIW3ezWX4Ru69nSc5KcWhmAQh7KJq-W5DTnB-a5IyBLylTb25FGxeLLqfCmVXktqbANjXAMe-CEQqlfwcKHn8hbe0tAj9U0eKDDStjDV5xREpDu7DRtxWRUJLQEfjmYk66DCq9_yuTbyFDW_AcF2yUDNDDttNJ_Z_OJhCx7JyQE53YMTvw8rteJdl-24BL0PsKJ0uD9vqgEJJ3h4w2TnqDkwG3BpAVeYj5ZqPqWiogiHj0xkn6BLPuqA_7VvfyDiGnJxwQ9PCA3EKWQw4tRBLEtjf8u66zJfPyqS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9K6os58_4l1042gASh4x0kMaEBGjcuIySX2SsRwMdQHZARhwL8XTVEkH52pZpjG-xCIo3WfTwX-lupBwE4CBArKNAOuDnWAuUibnYndIdxIPLLACnyfjv94nHvvGjLZls0yPr4ROVhKoSWhQiW_SmA-LcPo4wn5e_Pn_PLQZlehK70-0Kts7Ml7KCZghHG_NYs8TA4ftY3tJBuNTWmtYYspM1J04Zv6_9IkaPgvf2ofUalwV-oaLN6TpqA3OawN660M3eq0lZVAs0N34H0xs9xoa866fv6g5_sjHCI73g1E-gl3Svxyhp74eyvJUIBehNdHPHfOb_YWn2Kaau8H3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IZ7BfkwjhnMFZGr7jC8ka4YXMJy7s40Q_PsN_W88QDUC1kWu4pBezmbocriYw9wHd2YYDUoJ_QlMhSKJH7iTsE9IhBjJ6tz8wt60s-t85l1jPikJsD_U5BK9DdTG3eqIjKKKYxSPGw2k9SNFElJXlSUt9v_LZkJ9nchUz7vEwIwsxBiR-AEOdmh26MSdhoIqTkb_aM4Vp-OudNYPsYugrSc5e2QXQij-MsIYdt11uFPRGkwibcYPLT9Ns0n4BnglFc0VwY82QzTCjWyKphYITMnBB70bkgYSxris_CVckDfOrDh2O5-OK_W6980zJ7A6EvPwbOWoKfyRh8zO93MlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRs1fe14GSkR42I4gum5ynXXIIXraVhKDJY8hVZo8sVxD-LhrM7_2z2hHHIeZRS4ahTkbDc5mf8fhFEuZgNUZLx5HJzmg0qVIxfClM_zVRfdUBRZfgks_7nL9mrgYGYTtmB3eD2VF_ApMst6tUP48EDza-9Ud7IOpIcTi9e6ITw5K7ZkqtYU7OsZYwfjVD_AZDVVam9YEGmLMAaM_GrCt4XdGnDmn5egvdlc0bTAidJqncV9uskRUpoXdZFFKXDHmRSu7__MtuuOOlk2t-0qC52-R8wFiPC90VMEsUaTiuoSVG0GjxGAlW30_-SwM_hO9WmJhzeAkAbw0Tw8UyK4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vulcVnRTDqsv61f9WE4TY1KQ99TJy5B48kRlcPEyymtTm_6czRS3Z7VK64MnDL999XfEtl6y2jK1bDOjQKFuRI2ib5Kwj13VvEP1GPD-n9CFyRXiGGgQ2-CZmQ4oBSeQHlaqT3pHfrpddEXMvJ0elM6f3CZDuigPdQv3zlYBMvV80zFV-wrtNHLhyqXrPe0GKZR2oa0BFWWvtT60dQo4wYQLn9sVSOcl6cllsH-T-Tx4tcXd97otFIvFVxKzbbr06SBfE0F6d0pnyeBP_FgpAuawyLdB_E5ZsOuf52qUz1TPHftLpG_vQULN5-xlfXGxuG9RXzC_mK36Cq-0zSKlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d7YCgLsYS5JdZ0-AUrL5zbmtgtQxqpRbsdj07VH70PjRFwQdpl5X3n7Iirx07cOUdB1aODCRKBcvFQoj1zx9FfMMvzssjeVHYY65vR73Kuhx1Y2ZI3VTWtzWX_Ym2l5_eAVZgG01Bw-Auziba1w4etzDtu9jHIW7KURcezAIP9Hmre6JzBwefayexb0ldP4mRZ5AIv3OfwrTpyEJBWK867aJpEQ8uAzKjAErCSE_rJClKVtR67Nb1pwCUfSi8v4wbGnQnFh-I5IOE-aJAGZD0osPJPXgBEozRsZATA699W0w7VZy9bGQXPWTkEA43cHgxlUqd3VV1CZ_FaRIzzCILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Id1lkAbDyQ372RUJGyJIVt4CiIGsxXJoNao2y_m2kzqX31y0_wrUuoCFNRpkuXZSrnbQ-69PguGT1U_2BiAKh-TjJlYYBGtQ0RPKUqoYY9qAGk1Mf3Esv0zQ6gT4qhw4Cv8p8Bfz9vI_Z2Qk-B65LFNU5OiwFI9dQeCudUGDhEQOxaQ0e4LvAM7sBdlR2EnPofs-BQV2oKQsCTK49Oa9uByciZ2AS1gVrQGAaAbzwdc0-09XxX6EBIogom4e0w0wyD6o7ST3ZwSCHGD3y5f_14JfG1X9wyPE-z7L_aXrX-vADMjcqlA2a89LDt-0A36TTgt4v9UWNlkEeBUvGf3hnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/spqgy5eoTVsiw09xPB8vOUg0vRehQKsmjAIcPmEr0j9GAK7FMdbosr-q5QI-7MtgMK4c72LMk8xJ98jVzFtUWAeaZ-6SOb1-eR89CIXWQfAwcyt1ObHfi2t0fPz3370cE9JRiYhYxCcNrJa_Az284hU6mE5pbUmCozCHy3KnhGH6JkJ-uJn8fkWHcFhlYloem1uYbhanw5XzIFVdpPACeDnpDcceboIXoDdt6-Ss146xqCF54CyY4eddgrYqzbGBCKxV8bFFauWkb6bQFJp233BHDkY0g9KKptIgtw6Q9z3qnLdmD8oHt4eSLVHMt3llmUI_mSLdkndQsmaNkfNV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhDc4LpFPLB9x139zJMehD-WS07rYNkrp1TiMB-oljsXmnCNxeHuPI2Znicf929UahONVkEfbMVZYSyi12E9o-P1l3BwAikjleJznMgt1QYSkwcwXjNTBR5LhoPlUhMuguAygOxYFAKOYdSZwa2nor3IsV3Fo0cU4o88v_7K9uJq4JY92mMCT_6qSj6wS5Ur39gznRneOcdeHrFq7pAt39AesGdg5jRKlljNjYNAHfK7vCxJZNOkaznDV_kHznKeQ6PYUjTmnIw9W8pJGrggC9C9tYrSYplAKUPHgc-2pq41-a5h5ylSW6kFgstk1g2AQgBO_pABQxt0hGatgTxvIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWviarroYIhXFLvE6pmIjJ6DWmTn8GxgiORQ6p63g6lGhFkR6OrKz_dCMFmN8rf-0ISqgbfGjwsbBAZgql4I847a6pso983Psn-v-PNwW5LGTnDMFYx9vwb0xQFqMdTIUhN6yGwQ9Gue8jGpKnPCzlPmVnJI67NHAzLTXMpAjHcgkUnpnExWBey2cldclvDan8L5ILxfhXEhxNoJS5fmmSTvGaBUvulpEI54lu6cxhwZBN2NVgbO_Tfz9-eI9PJ779lDxKI2-NYlg7SxV20DE-kntAKeaZB9hfXQmh86gzoIOUiei_DhVS4J54-PnMUtJ7OMYXC9Y8SPLFvWpHr6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okC83XeW23pqvMjlUEkOlYCjx0g5nvTtJgdpvu-aB6_Tsbiwg3Az_wghPZ4VciSJuQZK7TBznccGf8OKpfUhdN8bd0hUcD1etQoZ534fp-xE3MbHV2mnrL1c76cjCArcfJrIuLPZFeX3r-PKqpc8Sr_-gNOU3ge5170-OLHw6osCcMzZpWC2th1ohXHw39qPns4j2n3ugolUgkdDjuSUeWyFvQ2CGmPYl3jIdgSDzVfBFoZ9Z8O6ee17xrIAsjYC6bqAhFB7sKoAFhlbW5k5pHoCev4k8eaEW3OeAVvAq0UG_JTkqi15-bMTvxluDCpCdsJI0WXWzFGTlKSLLX8SCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXy7YoRk8JgF7hAf97HgRZ4Qw3aGYfnPsI98fxIXtPneWpSL2yebPBKNjbzB9FUxE5CvnOkLyGLxy3IPpBB5NejZDCf0On9Y2GShya8fgOxuffmslsxDzDAWhp0bU8d4jnmHHEM65RHzTj2mDv4JPoohXDei10aVCbntfkYaaA_Bjku-2ouoRJJc2ZmiEfYylfeFSMDDudZJhI6PqbsncAZOu-9qnIR9u_KVnl_Q35-JhJmoFWh8jPLFIws3imUBhV341U6C2KIxqxs3OrLNpdEFwXcJ5jKMI8i_Ymn-1p77SQIUk7HPUNiesOi8DS4S6hr_2hVWdgJh_e4E4FK5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iV32GLcNPV-CYz-uTGD0SIqYwfDp4rgl-R5alsK083bR2DllGol7GWXb0SKSCzvNLem7IGQGP549L-4je7XP97g_jPcIP7SX7WFnRfOnBjZZ8GST_ypHzqW-ZrW-XsZV5UE69Rqic9Fpqkkv78I7epKctTAVbLoHlH71Ml2qhuk3dxwLrdgoBESh2HxPHd-qb7UZn3Gkh-A1_4Bk-GG7Nc6ytwn1d1qqrBBJbVxR4oCwGc8FZWYWNUt2RTWT30AoX3aueqW43ICkgcndqXJa4-657Eb38WdsZI5vLlr_Qw8mEIrSTBkqcET-ouRl36O9FcgCDMJccqc80h4pjp5S6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=EHJ5qJqB1-P-t8ydo44qvp5E0Fa_WSv7mtzIcru1aJR8ILsAJ-S0ZqTP72Q3g1mQGmY6fOaHvPzaUHs4pkoFq10kwWps7PrFGrTlmuvf3PSuxQurXGyIWtydJHVxfM79nBxykNb-3kELA3UvyM7xBmPAWvyZTeg6hxHyWcMqbzB-MbxY1JRlpZi90gt49E6NhK5CD_jUKtrOw_qauj5HIZxzu7n7pIuV24ONKkWn6OSfwFceAWe-txmqi-YEahDyP2pNjuFlMpELbEmitVHXy5UiG0goQZ7zQ244x6mZfHzTTRtJ0s8T4B-eJE4OyT2-FhNqF6U9ZhY0iJ35YT6hF0Hf9hOjH0gspUTklzzkwCaPr5gCMxT-0y586gA-Uej5Qv0QGTpFTHIIAme-WAq22ZqPIvkRiQVzTJvvcksPhIpItQNF3Re4NfCOK5WQ487T-hRN8TLWfJAAQrEqv5o4UU5ryeNe_yQc5BcDmoSUKHlpTHlO_NvyjsKTXlcOpqOQhmRVwWVTirij2XLfbFVney4K4Oj61E1-EaRIoR8QwzBMBSH_1IL1be2kBtguXJ8zW2AHrDdO50C7gk8CoACx1KLEHJvTgzo6pL2hx2qTy8w9iZiFVm2nw1GXPVcK4V5HpMoQBbRFkXNxwEl1Sg3PWWS22KyYhXJcUQ1mdL6o8FE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=EHJ5qJqB1-P-t8ydo44qvp5E0Fa_WSv7mtzIcru1aJR8ILsAJ-S0ZqTP72Q3g1mQGmY6fOaHvPzaUHs4pkoFq10kwWps7PrFGrTlmuvf3PSuxQurXGyIWtydJHVxfM79nBxykNb-3kELA3UvyM7xBmPAWvyZTeg6hxHyWcMqbzB-MbxY1JRlpZi90gt49E6NhK5CD_jUKtrOw_qauj5HIZxzu7n7pIuV24ONKkWn6OSfwFceAWe-txmqi-YEahDyP2pNjuFlMpELbEmitVHXy5UiG0goQZ7zQ244x6mZfHzTTRtJ0s8T4B-eJE4OyT2-FhNqF6U9ZhY0iJ35YT6hF0Hf9hOjH0gspUTklzzkwCaPr5gCMxT-0y586gA-Uej5Qv0QGTpFTHIIAme-WAq22ZqPIvkRiQVzTJvvcksPhIpItQNF3Re4NfCOK5WQ487T-hRN8TLWfJAAQrEqv5o4UU5ryeNe_yQc5BcDmoSUKHlpTHlO_NvyjsKTXlcOpqOQhmRVwWVTirij2XLfbFVney4K4Oj61E1-EaRIoR8QwzBMBSH_1IL1be2kBtguXJ8zW2AHrDdO50C7gk8CoACx1KLEHJvTgzo6pL2hx2qTy8w9iZiFVm2nw1GXPVcK4V5HpMoQBbRFkXNxwEl1Sg3PWWS22KyYhXJcUQ1mdL6o8FE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=YDdy_gCsbR1JiQfpRU9_ieNC8YbXu19CExfcCJsSUUjnlRg0Vz0R5vaqP83Ax52FLmLfazGNckCUrl1Qf7SYNpRz2rtecJj-PUfWRcUMMFy6KpLrRbdC9D6sJ9j1fp9g00XrL25b23SckvltsRqGM_DMtnzm-Vbl0bezigewLcp7e9tDW7-gZi9_AtwaMYYGiyEAi9bZMsVv9D3POyNpFApbLQ6T_zhuKc8IXiZLQ-Dubm04_AXNv1kPow2OW3qanhUruJkkXQLWJ1sNeEKZvq9mnj7SUWKQ-AZVxqITaNbR7_W3UtW-gGf-R5eq9MXF-VWKrRKAAxLdk1TvLraWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=YDdy_gCsbR1JiQfpRU9_ieNC8YbXu19CExfcCJsSUUjnlRg0Vz0R5vaqP83Ax52FLmLfazGNckCUrl1Qf7SYNpRz2rtecJj-PUfWRcUMMFy6KpLrRbdC9D6sJ9j1fp9g00XrL25b23SckvltsRqGM_DMtnzm-Vbl0bezigewLcp7e9tDW7-gZi9_AtwaMYYGiyEAi9bZMsVv9D3POyNpFApbLQ6T_zhuKc8IXiZLQ-Dubm04_AXNv1kPow2OW3qanhUruJkkXQLWJ1sNeEKZvq9mnj7SUWKQ-AZVxqITaNbR7_W3UtW-gGf-R5eq9MXF-VWKrRKAAxLdk1TvLraWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLe40nnd7018pxaYJEQ4XUDCJicLy9mTE3GUDuetWvZyPtcmYnkRJh6pn3rqIxfxsORwbdIeBHjJtFKLld3BuR1EMj75a1mpsu3bEKXk0CsspGrWBE8h94U4yfunV5-bvk89UCw5ob6Y5F7YPX2B4oJiOphcoI2Z4ufiIJafVdYfO9rt2O01djB0Y8p-qQD4OEPzm1-g0K8ZmMALI4SIQm2Zfcu8ttYdk6d5VCP4ruvM0UuekyabxPQavsniQUmuzggm0r2xhIn3QbmeRmUhLO9tf-eYViop6poRF3KgmKMLlx_7vvsEcgJV0A7DjhkO4E7DeMgS86sMC1SH-G3jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wp0wNJbpMIYdz9v8U29jwe2a3bnqpg_VVsbX_dQCDj7HXuueSTv4Tha6M7q972U1Q2apq7R6G8wz6eYbUaEpWHIYPynkBka-QCeRkhjK95hri-nHF43Lm3Wxw11lhqUgVGO0YcgUKpuVXRs2TsS0u6a66Lvdu-QYNoZ_7vaYPJZJr2y7D9mrcfeP8ziTT2kLHjt5PBGbrC5BMMS4B6-6Xe--mlzafmO7oG1J9GLcOGWh90slbdrqCWgaHd6QW-cwcTPTE4Fu7MLtyEPRikje7Q-CVFKrvaXjQHCPAfX-hZu_Noj4UteP_0hUxt2I9GHcoNtO5L-0MAlrhIx1eK8UOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrvmPLtRy2UcpTYpIsTGXZA5hiDc1UlN1VcyvAFWbWw6BdjJrL6m1CScC5fGHctuzrh_BeFD5t41afjtDubxMK7Ixp6DmU6ONm_hIFFGVQOiZT8YSQuXK_JhOKK2yFu9zg1etdVqOpmZ-yfuRJjcUWLR5BGpmN5D-ET8qy34lA61hMMEgk7QW_EgpNlkIi6WGTWaEiS3_ZE9VYyDnsUv1ygmQeIg_pSbFOY-do8RtcnBeRqmqP5qu3W_38yXDhju4EnV4gZGv3e1IrIiaiTLstNqXNfkuiOSoQC_T8T8z7XONxz0sqdkgUt-C4bKquoP1x2m5D5c6BZlgKM1gjUoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yy-udV7fPDkDE_Hs1NNA_UCloNzJzOx2jtMsIKipCTbZikRUtfpX6TqsQKLOsQs2So20yoPmZ-lCWnzdoGOXM_PpuHZOSRE0JOdCbE8S9G-Rq1xdvMoMxjbuKE36oAgT5rCEDC2jjgwKHBryDRwECPRsFQU55fS-ETKlvufOpidQwrHlWTp-UyN14-44umT_3leglgv0-_LiWU6r8WjG1A_fUb3uyb8EDL4q852hYBF3wRvM-j4UVMrtl_Jkl9jJR4j-MkVHbiJS6xFVf4YjqeYERwXAStKmrHIKoQ-MyWacfRsaYvyogwThK7VCxGKcUL7wlJdrpvsSzqAA9HD2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0UFaiwQcdhN7GvxkRZoiFvwodVtHAHbAl_mspDf3Gx23KOhpX47WyhY1Ig65XpnJuyS2lmsgj_blqxlBFCL7XiSI3H7tbaz9PhiJIE37ewLFKsZ1sx8os8zx7vm8z7hYt2XmD-K9ECQuxCrYKaAmzQbhyZ4cHObFi4po-axKmSZ8W5XTFoFsXk871Q3OBCenNLI7B7ob1vEQAIzoPR_0mIBClOluohMQTpCRYqz1SEoo4rAdeMDyEE9J8t8kKjDFfQGZkPC8ADceGqb5S35ie_3rfzzRAMU7PuxGE5JKjJ1CM9IFl7dMX66HIi7dmU2Cl0-_lY9xqXJ3YygdB7GMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC9PSB8nlvcHRQB_lMWuHLukJq-PF4aFnsFs4wTKvX6F0t_puMZMlLAieNJN_umyE9UfnYG9wyfhNCB82BaIOd4NN65Q3LPAWRZ5bQ0cHYbouASaDyIfbL4LUH2D9gCUPaXpIFCrZdARxoiGwbomvKKbxIJo3zHFuQaF_MuAC3dMqCyhLEUXFlQIAsNHMcFCXQi-gKGUwh9mzifVgCcV3LttM90MsePqDA_XXgHqViUxN_xH1UDS-WQKcAKqiyqN6PEiqhxgbXLMdxZ_JoB2ZHzetP-cZPRwCE93gXrbdt2k8CEh2WYW8VCFnY_6kN2UkEQa6wcRHqPO9BKl3tY5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1a2f64tNZ21ZlbA2SnMnJQFWXxkjAwltTWu-l4feYLS2pUgdxMt5aa4rrC3-3QUe6Hb4hj0ahz4HJKKAjldvOFUFsYUbaZKn_P-oSvWfdHNIF41F86IV8OszzXWJNFFHxck0wAB10W-cTyDLmgfWG8564IJPk0i6UuI50c6_GgGPPYa3ehdYFplghIGeGctUs82Y9t9o7AO37tDnBDdnb9yZ6mT02Ti8nafqovapHa1a2pFFO94O91gbt7wMGD18f_7kuImpVEZxO5MTmF20wBb-Qhg8OlZLA9RredcarHRhBUJQxC867p_3NsVyuHxwqPdexxvGLrQElY6PwKhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=TgJDNcaCkP3VDqMFPYK5M4IPvhml5qYKQIoRHjwBQDj5o59n-8oEVO_hauVSAqSs195Ffgx4KyAuyXMIv4vfs6ooAsQgsQcho0EiO3SK-KaC1D-A4wha4uD0yKDkRBtBLwHtjXFNOuAcR7D5wJmKri2Dk_mRwnsODPaar8w2qu6pHsMEJCx1-x20MKRyCVWpT1fWJs6UieWAtSs6vBjtRhg8DqdALnM8TtqVzLvoxbLtQTUcOGRhJs6BDGwz6AYiyuZzeTKc6yIg0CxR9jBoHftgHKUH2srSbnXc80agAMifRo9SyH-hJ00rjteOv4XrV5SgOc1-5zngbhTSV2r2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=TgJDNcaCkP3VDqMFPYK5M4IPvhml5qYKQIoRHjwBQDj5o59n-8oEVO_hauVSAqSs195Ffgx4KyAuyXMIv4vfs6ooAsQgsQcho0EiO3SK-KaC1D-A4wha4uD0yKDkRBtBLwHtjXFNOuAcR7D5wJmKri2Dk_mRwnsODPaar8w2qu6pHsMEJCx1-x20MKRyCVWpT1fWJs6UieWAtSs6vBjtRhg8DqdALnM8TtqVzLvoxbLtQTUcOGRhJs6BDGwz6AYiyuZzeTKc6yIg0CxR9jBoHftgHKUH2srSbnXc80agAMifRo9SyH-hJ00rjteOv4XrV5SgOc1-5zngbhTSV2r2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beLj8PJWmcpeOggZc_I8llnrULOJ3rZUonIgK4BKghDAGtL8C5P5zAa7AxLuFxIaR6YggvYj0_IyhRBjltL_GG9PN6vpKmp6UfW8yMh_r_j4ZtNJiJjMDEmdYo9sfU8QNZ_ZCZnF9xFpNtLfqWEJoH6fVx4bCJzNVIkkecoNQJ-Fd6DqlNMMhzfJmzehY-R0w0sjsyw-kMyKGtjsu0aqIpt-qGMjSozC17QzA4LztksdOZopraUjhqDY2UEmn9C6oTtizpf17CQZwejYStkdNFw1ws8v0gRTVt83cKHmYSlbQxO_jhD_IeVNGcERkkJwRii6Gu3EDyAl0XNKi2Tenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arnM3jPPCHCoOJu2mAczFfz7Yx1sr8qs3G2YzG3iXDNuCtMxqrRWYHxZLLQMT8iEA08DsPI9QI5BQxS_lTGoCJB3RAwjG8kyYjWevt5A6pWXi6pEIb4A8_6_aIYdGGdMfa9lyivCvoywOyJcBUOJxSarxKI3x86IMRKAjzm9pAB5K1uIu0Ti5Eprl_6OJu6l51IqPXLHPeHl5XUR4SxAgLfdhGpiGWLyHVd4Hjk3IkJRUWw7W57cbvAtmmHlhQlXoemMNHUjx5VB0jzm2fU6m7yJgNjVoIv8JaVSDww4ke7GW6nkj4U_NatWVIzEuNsPY_s2eeyRUkKp5_jGcYNqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u068sVCkE_v7N7Z93u_16jpOtRG4dqdijSdHGmy__dJWj3nzibtH1tnwArwm5Zc_nq8s7Ff0c7nX5DXn3jiMu_lERMClODfcFSc-F4PTuQBW4kIoOnqV_LzT5BuW2EidwUggge1uR2cieK2tNjPE2_se_fe6jmNjY4seMupocm90p_km0RZ2X_KH-8KHMtSwC3KkytgtllsjRFcpgU7z6dWDChbqIzE0_obGEvjJk3sl52jaWX3hhvWIo38EXq94pmaDVSY2LjWfbuihswbobOr7SlkOBODSttSRHArZTx5od79qo6iPTkHGQthNNnHZbfnD9j7JzkSdxpBAEmwMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=VPwAf8z__k6CKHThDqnLS7jmF5uyvjoupH6002EXX7GS4kBXoX2PeASV49CY2EydUI76EgGLjFDXdg0LIbuEAgnCTrB5vgV_vv6qBFShqYo8Vlod-A0HAV_6HesaKc0Ek-nqooz4lYghiBH0jLXgg6gjumj4uKjaJhP3Z_xBDgmNtr5quuoEYmsBRwe2nqYSM1-am9AP4gjuo9xDqJgYB1SniTloa6HSLIv5Ym7HWNUOMWeODcO3vLFUV1UhxUIQXz04CDh2mAwQiD4JWJbvE-Sq3BPJGKdk5po8aqY5AqdcMGfbkk5u3k3rSawbejMkiqVZMxfwcuXECNr9L9H4nA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=VPwAf8z__k6CKHThDqnLS7jmF5uyvjoupH6002EXX7GS4kBXoX2PeASV49CY2EydUI76EgGLjFDXdg0LIbuEAgnCTrB5vgV_vv6qBFShqYo8Vlod-A0HAV_6HesaKc0Ek-nqooz4lYghiBH0jLXgg6gjumj4uKjaJhP3Z_xBDgmNtr5quuoEYmsBRwe2nqYSM1-am9AP4gjuo9xDqJgYB1SniTloa6HSLIv5Ym7HWNUOMWeODcO3vLFUV1UhxUIQXz04CDh2mAwQiD4JWJbvE-Sq3BPJGKdk5po8aqY5AqdcMGfbkk5u3k3rSawbejMkiqVZMxfwcuXECNr9L9H4nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JsC1W_tp82ioixU4g6OTtZ6Y1nVD_7VNB2dE5I3KX-nCXaLx5hsgwpgM2Yojqd5UBkQOy3xbOSL9jjMNHQGQC5DdmGviohvnambMs1fc8kDUAreLY5Stti_AQeA29kkU2J4gFqCMbAktMpiie031yXsjqW7HklaRCxd1HL-bXuXADcuoc9sIqXkSFzl51h4yo9L0a-8aIaKQUcNeGkHYtodit1Z-qgUEWGFpH6GFr7alxwEBIVzMPPRhPscpwN-kZzzIosyqdtXCobVn16Xqc6N9Lbg6HxoJ5BwXesZfej27t2Wg8T63n2VAkNwsqWr_ZZpuecu4naDSIgyQ7GBblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kBylxXOHTRm18XqVrswfJTFbtVwFXtaxtnML6bseKNLjnrKuwuOiA6b_iPS1xBd8IwoVfX4Xk_IC8C8KgFXd-Xri7stG4PFp9N1HpAteGf11bgYU2WLjULALUrrmXBye0hOGGYwAvlSM_UbEMOBs-vCiTQN2zG6uZvZs4AqPUs91Lz7ExOtTVN4DmV3hu8jYdZ6eHs25suePz8OoExCdZ-4ma-q44anbCsn4B3BnmxZVkd7m35HBkKtSQUb9QktKCwhPU0vr5V5NUAxlWIsWwRFH-bIG7CVDL1M5sScP1EMq6s_Yja8gcZPnAQhUQGTjoqymun397h2PD_Eo-k1BhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vH0pZqn3y2_ToTphvI50NHf70ghycH5BxIaPkYt-2PSTfui0XJX9NCdkEa0ZsnkihnMaoxXlWZLUAR3Xz3URLwtn2jfkx8-IR8JqF-ty2dBgpWYnc96jZfmbCkbq9o0Vz_qGj9oknJUrJhfzb5QCItBthoZeOpMJHVgAb9e7tsgCNwdGX1wGWfvnmdiAuymq7PEy6hOJtGoaAJzIATZMRQ5axhJeVmlE2J8NWoP66jL5tlWDcRxAsG7DIaiZoH3CyyJgUp9xuluR3XPWNshKk-ix-JaYlCUMOOwxMmONCukDVtQntvx9jGiYg5oKuCYLK_1laZV-zDXFksiMPQ23cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=JlgtwsaJah5HilsCX7pyrfTfHIGhoEYOPI_KmcaieJ3KIECMm_CCYU-9HrAu4s60BvIm_b8a-gdWPrb3V6OwC8PWnhNetIbzYTLKH1D6c_9zLOtUvTOKh4uDVDl-75-PUJ0kZKwRMr6MZlQYZfk7Pbaf6Q8fFetXCa04QZSxeRUghijakt_f4RD6mxvuP65had1bwG96-TdwuVBtRXhARWVJt5VRZHUewQCMaAdoTbRPLtxbCGJf-eu1hFgAzyCkvcdp4gZ54yOe0A6BivGCT7qvjgVJ3jqXehnJH7XKE2-bQnUOfapM72w5hZyLVT6gzoHYV6a0n8iE3xQ0E7uTSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=JlgtwsaJah5HilsCX7pyrfTfHIGhoEYOPI_KmcaieJ3KIECMm_CCYU-9HrAu4s60BvIm_b8a-gdWPrb3V6OwC8PWnhNetIbzYTLKH1D6c_9zLOtUvTOKh4uDVDl-75-PUJ0kZKwRMr6MZlQYZfk7Pbaf6Q8fFetXCa04QZSxeRUghijakt_f4RD6mxvuP65had1bwG96-TdwuVBtRXhARWVJt5VRZHUewQCMaAdoTbRPLtxbCGJf-eu1hFgAzyCkvcdp4gZ54yOe0A6BivGCT7qvjgVJ3jqXehnJH7XKE2-bQnUOfapM72w5hZyLVT6gzoHYV6a0n8iE3xQ0E7uTSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=H0_VpWerYWvpm35Y1uoLjRq9af_EEX5VFvHf5wUm4DX6p6TWLNBdT1btP5beb58aWR9Onygk775ZDLJHhT8_OWZPGPGccOEG9EmToa5mdVtvzRP4erzbmq1nahsjk4SFhojopV01XsMTn83_q6gxdCneD_Txwn0ZdWx7adKaWhiyioWdG9FbzMwcv_HsCQgHaAydmUlOFUX5hPR3AXXN5ztLrlFeZipJy5HIO_q2AwPgPlkPzjYYVZOmICIA0NAZmx_mCNxfiacVH5VLB5_5dCW4dgKoo8FD4VkYWY-8GfyeWicgZxOA-4XpRM2pV1Q7jduJWO2r66QsTJLvkM_gCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=H0_VpWerYWvpm35Y1uoLjRq9af_EEX5VFvHf5wUm4DX6p6TWLNBdT1btP5beb58aWR9Onygk775ZDLJHhT8_OWZPGPGccOEG9EmToa5mdVtvzRP4erzbmq1nahsjk4SFhojopV01XsMTn83_q6gxdCneD_Txwn0ZdWx7adKaWhiyioWdG9FbzMwcv_HsCQgHaAydmUlOFUX5hPR3AXXN5ztLrlFeZipJy5HIO_q2AwPgPlkPzjYYVZOmICIA0NAZmx_mCNxfiacVH5VLB5_5dCW4dgKoo8FD4VkYWY-8GfyeWicgZxOA-4XpRM2pV1Q7jduJWO2r66QsTJLvkM_gCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BRvaODBfBzpBWPe6iYA9cF92xGLjVXOIrdjpv1WAQCaZuSKPC_MG6wJ-hfq9a5oR87Cna1xN05aVbHPP2WI0p_j2yVFwieLHcWLPisLLJwd3TA5llr9CqhhN8P5k3xpVBjZaS9Oe-opHDN3MkCe6SI3ival_Z8ByF5KL4_D0cf0O4Zt73rV7ER4Cjw-GixHl5spFRW4E8QEtJcwSlCpf7TFYAahYZb-z6wJFd1T3-iEj6D25jYmvDeO5y31cG4Q0AK__MBzb_Q1Mwf9zsSqmBHKFGRJuytRKsF87Hioh7JSYpiq9XmO4fOQzt5hhK-FP97_ESe2VeczkF5gZ0Sp9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ETYyGXyXyeJej4-DJt0vHWD7P734sPIvYwTuynGxGCxklHtQQNrwD87wncG3liRRT96gxNxONOJ4I45nNupE1OpFwKhfBix1e5fF2kvetlfydim0ZoZ9DinZhUJpQ9XQXk-s5kWXl7MnCTR6COIsp7LMGqPfpToWz1gnO6XlH_xVusgNp3irbS8cqPvCgb31pchR8GHKJFaP34aTQLmwZgTTYio_jkdURwXA6LhOkyrdLFvfpB7DCCI2dIBAiMixIErseq1H6fVLc9YlMfjiNeFUKbhTP1_UhsfrY7mllTMamMcil4i2bCvruM6P_1h8cfrAuGZM7npidG-4mQN11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UdI3-f2NsYvCZ3kK831upG10UlLUwYivAyWhGelV1mEYxqURk2IW3eXLPenwGZCWRH83UH-WG3rnkNDWzGSJh-jeMc6iyybGvbI8z-0AyQZy0tKTKvFZFDapGb55WGoUTlFIU09krqyV30Rouqgany25PBRbQhcMdL3ZCiASQEkNPDE0dAh7iycmFGPwNhvq_zTK4KkQy4CZjaFXEdu8t7oLedPPqm4c1jm_kUnMJu2kAL30t1ZJePYhzHqjn7cJWgefuGUnf89z-_UjVbWJa8cvxCEAwgUUaZbeQIWfVuBDI2IU0PNyptTHLldfi7hXjIE_faKJ8E7xLSFFQlRN9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=pyzxbbqBl8ymxMXoeKxkgJCRDGcRMJb4xJgm7X5HAwDhASqfGoxggz7dayRvjR4IXICB3WSEytXQRTlfStaayRMdQrBnJHuYvDOOjoD7pVpjTPLlga2wCsBwvmMCV4W0pc_DAOt5U3D9AKolqQ86ZiX51NawfpVbhfiGh8uohJwTHj35XhxNKGkABPjl9hPP24LdCZ2e0ndBjRf_GnANyIRDeaJ14B2FtL0Q6FU6iCsDQ1BNHouZc1zzSaGwp5PMO9uf_g2DJGLHmmY3qbv7Mj1iZxfuVW2WPRfZ-7WhYCXbxtuhsmAa6-I787NSJolu6gjhMOam8_d5WlPRQIIxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=pyzxbbqBl8ymxMXoeKxkgJCRDGcRMJb4xJgm7X5HAwDhASqfGoxggz7dayRvjR4IXICB3WSEytXQRTlfStaayRMdQrBnJHuYvDOOjoD7pVpjTPLlga2wCsBwvmMCV4W0pc_DAOt5U3D9AKolqQ86ZiX51NawfpVbhfiGh8uohJwTHj35XhxNKGkABPjl9hPP24LdCZ2e0ndBjRf_GnANyIRDeaJ14B2FtL0Q6FU6iCsDQ1BNHouZc1zzSaGwp5PMO9uf_g2DJGLHmmY3qbv7Mj1iZxfuVW2WPRfZ-7WhYCXbxtuhsmAa6-I787NSJolu6gjhMOam8_d5WlPRQIIxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9JbT_qvO6MLCA-0W7H-OSD-ay5yIVo_T8SMKoko9421AOQMj6g144SmEHAS-koeBCiuUkEvC74o2XbJrM3xcd6qh4Cg9CkBXA-a7tXqlAYrH85gsPkz95SN2T-W8W-XnlHSr66gGvKtQ6z8z-0hOALw6qlR6yJqtNUxrhB5D3lJv86Rhna_rQ-zjj7ZHMg9UTD5i9lDF3J15ZYteNaD2ZVMN5F5TVl61DxByQOGU6THqa4Xu6KmUk2mAQhstrMTFFAW-ZwTmBGK-qRrvjDCsQD9sOPyrDqbXDoYNThoLF-dnH-foSy1Bpi9fiUN8X3AlaPEiAQhSeUUHXnduc29Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbjfFlQfZtVxY0zgvDNkM2X0YLjfTi1aGmXYUwNaVJyoRyrmCGOME7_Y_MDV0eo2YNhNePWNZo9bHStssquvYZ3li98-GdiWmTf8LpnJur_l_kQZKyXE9H7CxvPgfmr5fMOqUzSgh9sKra7X3Os_s3iiIeR1w8n99EWXI2KXu8Nc48rKa3QdCR4_0SoOz2JmROYhXlO4idDZegEnHBBWizK7NEpFVy1bOH4EbmSF-OKeT4k0ovQ81DDL4M0JJltwistBmAHaK19rjBwBJhyQRocwaimzXgdgZIlS4ax9bXkX_iXYh95dh7TPq541TXeeJm7-KqZ6RrHoO0BMuwaR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq1SYQm3GePUvoq8gHj6PPsVP9Lv52igbrMVVniz8ugv-g4QV0ZF4NCzbtJTL8_3saiJo2tZeyQAW-tWUfZNvMmY7f2oUw1psQhUP1jXLYYSjvNw0dtz5BWOuVCjl85xR1sIb0Zyq05DtsnBGGufTnh6hgQW1-1YUfhwZLVTWaL9l__KTgDQyJTA8z9Ov1mLHBJEsnHcp7hbPN1iNDANK6jpT_DSmOzF8DeITIyrzNB6GT23gz0eEY8PFvQFAgi7uz3uTDhIQIM56sB0obOjMTHwXvGNGJmDd1mbZ13hhf3fv_yKe9f9lFql6Nv5wDIp9FC9ScsPXgw6yTOIFHy5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EauTASVjSWSVV5eeVmWMtGRPtxWo-2pRrH8ahUvoNbyeTJ_D6KSPjDDCpSZvtt_YfOPd_4-drL6NTt1imms5SGgtFn0FudGlbKO7R_SrhxjKmk5Pf9_KQtCD2QmP60hQlMsCE6c2QIggtwsv8JPD20SaWc1MgeuRx93I1Ir68OAdyQ24UpxlGtn-ANuhVu_NYNI_A8lzATDX93os7ocyPIjiuHZWRFGMwQ0zbCy1gTosveeo2CcLlXCpeRuuVraGGaC9TKBKkjxqJrV0hkQsqo70DNdiG-q0N8mzWpsHO48MxIv7F_3avaTQlOdV7O72IfyY9KWs1-CNxlzBkWO0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LqE_HRsfln7FMjB6y8fZ8a9ZiilDjH-4EM-Ypq2Th44qxLYB3tkYQQrI2nmshUeen5N2IGPS9553j8fwaJyWGotaPptS95Ve1HM5HRi0s9UJPQkMluv-Uczh8_egZk4Ev4Jl5tbpNO_JtHFzj8Lrr8EWv2q0qui_9gmDPTUnPfUYh6gb1fBYb-BIWqISksCUrPpd8Xxhv6_oQJ-Ald0LyM6BA_-gTo9urMMkWwYaSK8PLfu5vsJXQC_6JtUrx8BSf8x_sz77GRH99-SfdXbG4lfJCOAUynFjE6ukXKZOabWGoBBCW3DYUBiwk9S1r0it6GGu1jmSBTJkZn45wXHDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A_3UnFuYDYiRE1wvvcSlcVmBEbSQb7Z93pxpvgYzZAiLTsqUebZdYSR14r0-eMuVp3BYgFS0gWFAxBA9kCMukDeQJo-iPcrzsTYNw6UNaDHjRZQ-JKaZWuC-2RpcSamyRxK96LOa-pEK_v87nLwps7Y9ouPqo47S9c8E7UsETgoCXMK8QkNIEst_Kl0PX0JS8_WXysSS0fTZT0X6jzH0Jvwo3tMG7nPJa2k5Mpp1LvhdeWG4ocq5MywK8khBSYTsAU8k0Q4e1u6K6TIGszKyfJEP7je6TMeQg7nVq0zBisrphN6FbXOoZ6LyP0xH-mAHoVCY23e2c1iqEsZLwnX0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jmVVMDTXJc4emi8Ej83Wa8L7v9SzTQ9uz5HD1vEqowxCrJtxL3-BuTlQoCgGXmlwbf0Gww8O4j0NDSQghPwQlO9g1OtOgeNkpukPuJrIGmF6T4z0_k56ywgQ1YdsLUeWQ2c84XxiqLHzAb-m3x7Tj2LAxbdmSG3EoKo7z8NQ0zrLNkk5lFfM6YeG5snqbqMUs7U2Erp0HpSzObihwf8s7JXO543qiPg7VhbPFgI_1Ks_HbpAlY6y_hXDDmiAuZSXGtm8Trk_TfNGLuPELi0bgzaeLXOtc2-1B5AQVkI48zNJAqUPc8IhYNDd0_yNa4ziiKyMeeBLGXa3csQ8JrtOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GWk2cxaThsWMOCw3AtgneXgrNiruX_Snjy0wT7SUD1UxF-vVBUJvlGlmnAK_JeK5MmxPkx466QhwTtlPEKVWN_0Ed7d1EIHe5qq5t_m5Vou6RUCPH3OGygI7ttRk6J1KZsRlWuPo-Tju4AXgHM31e5rU_nYz2Mv5oY7k7FrZx_csvKdlIhGHS2wWWrVCqGG-lxwIfpdMBfiR_kc1IzBNbwneYtd-ImWK2Ua0ojRS18Ee4FDFBdpl_FPIhI-4fzz1wBliuvJgryQW6YrJowsT_bPyWblavm1sciAobsD0viW27LlfzL59c6U56ML3T0y48pdm5oLkGBgIp07uo8IbvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=KN-DQGsBywcLU7iqDkRUlCQK-CeAGMVTJXhMkmu9GadcyFocYh3K58A0jTAlYLGNaJ6hPSeiuowqlTdfGOF1K5EeT64Y23d3MKgumkc73vRcso43bOr78PfmVyDvBl-s7_c3JrJXSjQe3eRZ3GsRqdg_UrMNcA-JRvK0yOC1syu8rTnCo0-ndVpSl1Gxz5WLbk3Tg0UnaCKS4KkJNgMZKMuA-8fePKCqp8W_TstJY5BK13-t-H0TzL5Tt0_U-Q1gMvVGbMHB7BVuvSj5847Bnmu07vJsV3iwt1RIrlR9YlVskRA6BG4glIC2AxyspKSYXMQaT5i1l1xwdMkR5Fjntg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=KN-DQGsBywcLU7iqDkRUlCQK-CeAGMVTJXhMkmu9GadcyFocYh3K58A0jTAlYLGNaJ6hPSeiuowqlTdfGOF1K5EeT64Y23d3MKgumkc73vRcso43bOr78PfmVyDvBl-s7_c3JrJXSjQe3eRZ3GsRqdg_UrMNcA-JRvK0yOC1syu8rTnCo0-ndVpSl1Gxz5WLbk3Tg0UnaCKS4KkJNgMZKMuA-8fePKCqp8W_TstJY5BK13-t-H0TzL5Tt0_U-Q1gMvVGbMHB7BVuvSj5847Bnmu07vJsV3iwt1RIrlR9YlVskRA6BG4glIC2AxyspKSYXMQaT5i1l1xwdMkR5Fjntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq8v5EbwcFhHbNwuuoaQB08uxYr6i1JlThORzwGhmtlqMX1gpVcV75B-OTpXKt3jAFXaAY5TRHN2JjCEJ_kabuynikM3BXkiMahSL4AHJ--U4GySZdNmZAJEHkKlKigCEKf9Nf4xDaiUtidVg7MJD1B9L_E_wz2bqThqTaQ-5yPEE4rSQ59gZxhpbv8v8FiH3fSBCvYDCrfA2FvwYZBhTjyf_kgqO_Rd6ISL3fIz6EuDoofyEHDkuIVUY9JRC6bGI-RVxxURzqfz-06HOIqef-C7jBxweRuFS8Xako3Ull8HNuiOXki6J0EIxT4I47OiAiMrBIlwK1KjsVc9TBalCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nIriThUy4JG64wvO6-NXMwSr8IendWf6I-LKp7PHyp2zhWbqgMdJx7kGC64WYOjpFiVxYEUSI6RyCBFffQLn9HYkR9rGvX0r8HlPwCRAMD9_rtnTJsUmxMbW6rkJaoVtiv5DC3pj29liHiUkeCGA-zI-s3aDY7oWgsZweciaOEObc-X89WjQaLI5KpgNJQPyahJ1izXSqIMAqaxadXmlwnhdRVQw3Ku1JRgV0ZQyT_7zvsPUXc69JWPYAbawpKkPulpKrEoNHDEKyCc1jtf_bRQ7y4kzWsPo45jTR3_zSp-TU3hvs8qPCodq7NDyfHj7lOrhEuTjpM_B4Lamt0XlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JsDBU15qFLJgPk_YG1N1Z83QHBconYCzvACYeqScDzXG5w6tBeSOIKQExMUMNogdfgPnkfG6pPMuVrDUsBRcrdfq92WNigYKm-6sEpqi_JHhLvVk4RKfraw4Dhfg0XxYzFhP2M17ghgtgIT7mT56YyNgm5UesmpofRQG9yIpDOCTOOJD4h55z8QtaTuzr1cWGPMp6X4oBzCvVjv2Q8IsESg2XaDI48IZSJ5vnTRweZ4AwL1dFaVeh-yY_y-ib-9tqZfY6R5WhITMa5tOWBDnyk4SN-EVtl0D0Ae8p4zbI6O_vIqDLREjha79Dz031vvUMiKnWgwBvJ4D9J00_lLf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdyLTWOAzf8on-ZyQu30K5rYyrljCRGnBefUcItvPeEea2OvuSf_t0Mv26tFb9ZPAEbp1wkRn9XzB6y-054sGLZhMt8dNWuIDzwMnFXYSf46qUpj6ZQTCGN2p5HneTkWCRla74IKvmLeodHLodE100C89Huy83jXBZGGn_ZoGKKqMILpKRrI2j82VGHNu6APGlnz4Uh1TfUfPfHN1kMYVyM2iS-_kV-Tw30DF7wEI2urb3EXAoXJvKTIbtT2POzvsPRwVU-Lp6hQi2Ixac4G1j9BoyVdsnRrwVJxJWO18tApAGgQW-XerKgEMLsSuflKHQpzoIOMLKSh7UxVIVEjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OAJeFAxUQWOd72riqW46iO9ah-P2o-bQaGGKpYYGN5LdpnfNi-f1a5EQDdhCj2d9NXdDkpgu-0yD4AWKfUEt2eftkQ3XjeyOEO5RyniMlNTczVy7gAhFc7oaGgiG1fy0IPLhBCquLMo2XSs2rFVGQhKlSRqe1uxyF18QHcPVL_UThY87eIYbWmejIFu87ddWSI6YjKLLWJRRNFBjDRe2jupc1AiSnW5qrmWFM6DFTB0LCTAnuCBsIci57V65TGwm7r0jiT2j9fBHJLfvPhxxDhnrTPoJDjaKHNB59vq9AiT9Od19oOYoyxsDiWo1epC6Gr363kHcgQ6rMXweU6Adygc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OAJeFAxUQWOd72riqW46iO9ah-P2o-bQaGGKpYYGN5LdpnfNi-f1a5EQDdhCj2d9NXdDkpgu-0yD4AWKfUEt2eftkQ3XjeyOEO5RyniMlNTczVy7gAhFc7oaGgiG1fy0IPLhBCquLMo2XSs2rFVGQhKlSRqe1uxyF18QHcPVL_UThY87eIYbWmejIFu87ddWSI6YjKLLWJRRNFBjDRe2jupc1AiSnW5qrmWFM6DFTB0LCTAnuCBsIci57V65TGwm7r0jiT2j9fBHJLfvPhxxDhnrTPoJDjaKHNB59vq9AiT9Od19oOYoyxsDiWo1epC6Gr363kHcgQ6rMXweU6Adygc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aPJkngRxvcBmCCe7x7C04zdS3y6oVJwdbJ1JtwaS3615FtVdP-ZpeIVfUgrK1x9VnSoHOnTnKYRPyQMPiTicskPqFG0H5D5cMycjmnkAn1bFHC-RD0LeZ5FWr7pdDYiZ-VlCi3d7QdtaB0ns8YCGFbIW9TBZzGRLHMSkA2R-xiiBiX-sneJPHlnEMCoZIHH-fmLO2gRH8JtAGiwV19WrkL63mA6dwzVX2_ReA5PvPeeDPiAaB8eMq4uSViY473-9rQRgG0x85KIicx1RL4KpP7Jh6VTy3LWFAzNOynm56pBTEnv046x7gBLn80jqTp2neNVlgxIIpL098H36cvivlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E9aOZcVusX0X2QLUT8n1SPUSXAsf8DEED38UMqEi-llybW418iNanl9ygTPVMc8hG5btZYv8AdYvKNOCSRZ4vXxS9hk3HLsLR7H9BkzbNJOOMRLznEvB7p_I1oHlSQcEfQInXaRLlzmF6tBtiLc5jlWInlBToNtvbukNx4-7y_wbNKWdklGlKzm6LTP5Gyu7Q3iZQ59Jz3yNeDwi7qoZjR8E8L35-UtlCTRu6Sc97nGHzk6adjTJvkT4l3dTqnRfC-ZDmwGPXP9TYqF0Eh39FFjM3uy7E_hB-aBeBFKGJc6hD4WgyJMDovgE5pbAHGj4iNX_UzilXwTqfc9VWguLfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=kW_IUTbXk-_NsNWLSNRL1DKQvGnaZIXzJPnXItZ7SXQvpbW5_4n2MyB-hrYEy8SYhcjkG2E4W6ovG38Pl33A6v50YOMBfPKVxA9lVGrxvVLNmimyLDqalUes9OeZ-pQ1rOAQfQrCvL-7p0g3uTCo754qlUVRSgpqV-vMhLsNaHeUsYHPsoqDUvD52WKhYEkjoR3l2S7THrrAQ-aAM6XfFvrH_KQCw7jgDyQIpdjY3uZwMyS5si4YCPOazgoS1KD1Ijnnms2R2BtAkdrNbGu4gAqdoldjISoJe3KR1ClTuxjnKWJ0_qMQrsH2UH5KVI_0x7iIy6TFThvwx83Acip4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=kW_IUTbXk-_NsNWLSNRL1DKQvGnaZIXzJPnXItZ7SXQvpbW5_4n2MyB-hrYEy8SYhcjkG2E4W6ovG38Pl33A6v50YOMBfPKVxA9lVGrxvVLNmimyLDqalUes9OeZ-pQ1rOAQfQrCvL-7p0g3uTCo754qlUVRSgpqV-vMhLsNaHeUsYHPsoqDUvD52WKhYEkjoR3l2S7THrrAQ-aAM6XfFvrH_KQCw7jgDyQIpdjY3uZwMyS5si4YCPOazgoS1KD1Ijnnms2R2BtAkdrNbGu4gAqdoldjISoJe3KR1ClTuxjnKWJ0_qMQrsH2UH5KVI_0x7iIy6TFThvwx83Acip4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=QYBpD6VP2YV7DkOuFkwcgEadZS3BlJvm1IJFSCnsJr92mXeRE6xGaJjtyVjMhxIvwCNRf50Eg50VVf6kOYFxdY9TkNPh0z_fQMbvNQeCrK2SWuXlQHnjUKbk95Dn_hWQ0d4tCPnIgEAELIeNdpuYDLHk6lYbYrhZskkpf4tKYcIvotfnnlQzSsP4qFbFWbVJ4RqlpPKRYuSaMjdX-Qg_9sMvqv3C2oJ-iBxEqHbdWKzOTJxTY6FDXjxJ3DMJSd4WEpAUsz3zaYjOgHrG6uDHN7yodEcxsXA7c1PZiQEKJworp_AuYAxI0m1uY2D0mUY6j8X0GVKuCAxFk4rzuznw3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=QYBpD6VP2YV7DkOuFkwcgEadZS3BlJvm1IJFSCnsJr92mXeRE6xGaJjtyVjMhxIvwCNRf50Eg50VVf6kOYFxdY9TkNPh0z_fQMbvNQeCrK2SWuXlQHnjUKbk95Dn_hWQ0d4tCPnIgEAELIeNdpuYDLHk6lYbYrhZskkpf4tKYcIvotfnnlQzSsP4qFbFWbVJ4RqlpPKRYuSaMjdX-Qg_9sMvqv3C2oJ-iBxEqHbdWKzOTJxTY6FDXjxJ3DMJSd4WEpAUsz3zaYjOgHrG6uDHN7yodEcxsXA7c1PZiQEKJworp_AuYAxI0m1uY2D0mUY6j8X0GVKuCAxFk4rzuznw3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=UPBlcQVny5nHZ7-e-2WdVnL3ZUo9ziWXh_fUSYmQMmmeBggBEehVOC750hs1S_Xxq_WQhav_qliqtH8cB2IsQR6zKj9B_QnAwGAjBb8cyx7nlN3IbSeB0FjGXzU06c-A9112ZzNbZGhgo8OhWy9jREg_XP7Y02Ledz3ttPiifqPQXqA4pd8N9xZYaW9ov8ofQ3MPZPdAYXo8v_JbehVeCkQKeGv0ZsVkcNUNsAGG1srggM-eVKpWRAqXY1McikXWEE85avDvPlZ-S37u0HfdY6QwbxXxwOEd5HD-S0ZXtxjpgBrh3y2svjDg8y0yUHSC-N3p9r1oyvRwEi1GLhLHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=UPBlcQVny5nHZ7-e-2WdVnL3ZUo9ziWXh_fUSYmQMmmeBggBEehVOC750hs1S_Xxq_WQhav_qliqtH8cB2IsQR6zKj9B_QnAwGAjBb8cyx7nlN3IbSeB0FjGXzU06c-A9112ZzNbZGhgo8OhWy9jREg_XP7Y02Ledz3ttPiifqPQXqA4pd8N9xZYaW9ov8ofQ3MPZPdAYXo8v_JbehVeCkQKeGv0ZsVkcNUNsAGG1srggM-eVKpWRAqXY1McikXWEE85avDvPlZ-S37u0HfdY6QwbxXxwOEd5HD-S0ZXtxjpgBrh3y2svjDg8y0yUHSC-N3p9r1oyvRwEi1GLhLHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivOwBPOzHjJX_qoIgrkjFhe1I7GX29ywBv3vCkknPC1tUc7WWRE_kyjCLaVjeRJLyeIPnlbKAob8hdwA6Qtl_TjvRYMwUIWjWWbMi6yUnlJYh8VO1F5tdvjT_Y53Pt1cM0RrWJOHPpMWiTHVPDNngkibOoNdn2UjahPaCRpEFOwP8lkJnqLCoYlG2I9Ul3U5iTs2FwmjYn_g0926_jJ2f3FUmDz3COdHQl4tGD4DaXbfiN67I-t9DMP1UTtgqMckCjd2-MJtLtAWUAPanT4pPVE5YbDlpGVnHmsk86nGn-_ztCXXqgyTNMOd535qrtXGLNVNjlpfxrFPdDNVWGyfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S-WxMGEgbRjviwdAEfOnlNyN3NOb_YiCbalnIlvIi9XfnFGSwtevK588tzsU-lrgECEOZT6sLrqHBOlqVGC5StXnvF8anceGUBvj95UeC--Bi6WVIGwBk8zQ2pkdED5vpGt6NW4UKQGqXyfRdMfIBhmiKIg4RIYB4PKRs2XWx8sbd8dZOZ3EF1qJcZDnNe4V_ojHBasncY-5be4M9GLDxA3V-5EC_9sAiy3bhTAAdD9tBSE42KniQ3JmR7TfavrbVhfVlYS3KTCNRCzkhxI3SkYmAxdAoVE6jJIqX-Vn2Xlvm8Tjjlhqq1r8JKDXedtGfe3bU1wENEpm5VoxW0sQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQz26ik6hiu8-vRpObCOvMiY5N-EfVNmqebJwF2PXuaI3cfpkh9jyANCaBjMTnTP1jUE6mxixFOwDofUvWAlCY5fs7ib7SRc75HQpq_92R0Ca5J9QQvkq8LacjYB_0F3TdYnfG9-2wxpcmcysHcJbbetln3deXcsgHISYX4KnVpevc-_C-or0pkJLjKK1a_CpHIYZjIjc25VrV4VWZrSEp0jZS6AOdYJnl4BAHQ0grut6wNJ4A71amR65y0Y2L_MARPTzD3tJ-JLuvWE_9u_AhumCgMwnjiKfp6UYbbPYSCJTYC4wadu6ZMHnruOWln-IumBbn_8CSg6VugbiQPM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RzyrBJ73bCcFDMk7QltuCTM891O9lUqfxabfqCiiaGQV_Bq85FGtaq54vtKhFfJIJ2forVvx8ftImm44LhDnV1jlTwKZj2mAHMkk9YT3L6guYb0hh0mkj2ZFQxuUir-V5aQ5a4StkWOurMLcJYy4YmJjUVjIuBpujul08Zv7Y7ooX-PUSrkGwUU4v7NfS7Xe5LiI719kfJVHs8jbj6wRAcTvbnFH7vjeIe5kNsD_mSxwqwgNLVcdm08rybqfIV8pwYqokw5gGBX5tzTT_1SdYaOB78Mwq4D_xgkqpdyS2jaRmnO7tABgM4FxrVsSmrhrvADVpf0YPiscpNA8e619aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OtQXUzqDjBkJgG_AMUT163Z1eXSPjgYj16jqDbL7Rmk29HFqx1fJMwQaequXMZSpnmDuAfB3sc7fECDEZIaeK5LVHaAzFMvulPRFCtBzTTGUtN_TZKWrtvKXj1RUaZ47k_1UOmdhYVRkvFCIs_jfcVtsFG9by9i7ylX0dwEiaefbIycuEhR86UvLK4VgmaRQNM-W4-MceMGH0N_VKFNCaABuVo6aOfrk_pnCEQOMhgmvgZNrZctDCdw3L86-LOUYPYExzSVRs1gKyyC3iXXXK3_-FZS4fxtsJLH6ZALCZ-m8HH5oUyUUHCgiVP4IMNgekVzRutwsTcIpyr6O6-T3QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gZZ5ORhB3oxXrjHnIfeZpNWFtXIm3cDz49PGN_46Qz_T2JRSI--DneNYa5bonvnFubyqo5M8PbQC706b_nTzH3mJvdhwzllHIU_kPgwjWpEDVSyXy660WnhLYrIXydbApzndRDnptkIwA8_iDc_rsoM5Vqb1hE4nspY9XJYsqJr5IXGR3AoL1y0bOpyjDTkMdrxvJU5vHvYcwyXFZMbpbBSlWfwTI5a9X9avb3k2Xu5uqey-VSqJ7ARWC5alrpOGpAWY4E0eo9yg484MPfGhir84nZUcNP3Gqbmjvcpjj6brxQB9x-tiluMu3qxFNAxOawDRpjmH8PE72t73Q1zDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c4eh0Yv2vDWX7hbxrUwxCwczDYA-K1fxN7fiQVdQr-fxfXlHm68HGXZ1npPe6tDooeorBnFDtVP6qXvNrUUxGCvMbURI5G3mhblmBd3lYUc456aA5ObM_TudkVI805A4OXjZYYhrynmbvm8pMFeRJyWltpGo5JnB1rUsUrQGoYiXGL6YS1c72RdZe0-098NVJSeZ-eCCxlTPzvZgvG35jNLw2Ai-haS3R02UIT-gAjFirPtfqMVEw9ZqtLmQcimesgOFyBHQUgQRogn84iVucTbhjibPB3v65Clt3ce0ZSe5GePZvIQaDocogaib-zeLPx51VGauYnbu39G261rG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZeJoSy9AhR7sBQ3dkT68kOClRGe0bx9o1KCkrNtAMu71csO9u5L2MU5aXhb1RwaRlncmSLpohTVkDzkLZLpkoLJpLcogEPH04uvADfCEUdrzfVFOs5gc2ZQnb2r0EXRFEyetB-76TAO1sB1g__MjRduhW3rWzwUZQUyboSMRT0umoHWbilh7SpQdn8WxKx3I8tTcP6J7vHt5JIKO6W9-tOwyYWMXWChSaKVPKDCqk0ll1UESJKOtNSKjGLA_lz9ZOQjQR0qiWgtQZyM2VtFW33YZBbjWVU_vbmhBPUop8r605TYHWpepJyCZPvTLSE-kRYKlC7Na_yk43QhyK5lPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OUDUGh7hNffNX4cB1To6_VkrpJjayiYvVqbMnVZrwgvWVybvuaclZG27N2NZszokLLlIdPRKMpAva5rrblmBRBBGlqUQqSCkS-1oW9YLrOQ4OIMQcW9dGmbxtefpVZDWG6pIakSRs4ZQDQTWyvjP6pOsznFdlYh-WFgiP09CGBMbQxcwQuSR3CcwD9YrZkXHCp0zHo1NdlriFTmIARdxxfjvKFgREGNZNL18gyOgVpXbS5LAaiW4csP5SZeffmA3kIBayAW5eDGZhblpeFiK7Sx6Q-LllBxH8NSYDnhHYmxd79g6yvrhJQS5TbbwlIRhh67W4MF-CaA8K9pIdRZQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nzw4aYaIivMkSP7i_vIS-rmHObkBVTRYSdIi4pE_X--QvqSBf0NKcDF4xI1QwUWNKX69zRjJC8djB2ilXTyIFqdl9uV5mO8ONShZcwhK6qN__I0D53qpGvlnYTzijaBhYvm36S8oZfkSzjJ-s28pFX6Dz7Qbs3O1TcU9LNgHovajj4wQ_xlrGz7mkZnXbnaoBD4D_2N0DGPsUl2nzQ3sLLIaoCktMLqFIDWayKyT3JiDWj74VTmp9oluBjcG3DoDjPNcYUeIKjM7cI_4vm6FLTB8nqtGtYHyTLoymFZ7YpCqWpR_zF9H4RD_XMERSQuQUj0k4MM7IohZHL8e9joYcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UU-9t8qKnX1pXZoGZ5Irizk-KLjJ30L3cbbKXQWWpF8i3l9BtDHs46M3E_-MJDkw7i1tt2gS_RENkZ6hM39sf6gt_qnIi5l1g5Zs5VtZnC0f06VG7nU6zIB4Q-dkRnqW9mATxbf6frwnzgdMr20yegs1e3CCNJS_iTcvu_Jlo-IDQB15VlVz2F8O6Eq8d6SToxYeC22qJ2YqNrvHUbi_eB34ducgNYIW_lcl0B_ei3Q8Jq7r8mh3T0jBsJ_ydtJ0JHZMnmNmYZNVi0YLmpy-_qJAmrRua1_tyvNFhhYTZJc5c8aborFMc_oD2lFvX2yTbB72GfyckQDjgeZGbVtnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WLiPL13a-Qx1W3rcmD9Q34DcvrLB5rYfOFWnBIdYOMO7wnNy9JgE_K7DmBUIVIjJJS77wKfo-ytOu1sJZeK4n_vK98rIrBqbVE01FQ02DKEnrekq0WITfFDZIc3F4ROJQJxzcgFgtOGF1Z-TFcVkzts34I8qelqOrc9Ft517AAdS4xZpRSh5ItiWqhvaGW7RgnyDmA73A-IVatym3kqDYp469PvhvcQgWkOGZCsBE4r_oNE6hqWDDhJrOmw8bgPbBmf0Ly4Y3TNN699DWQAdUqWP7OyGhZk6zqC_ggH2QeIvRSQ5N4pIqvOHi_q7hKHsePsd4wwyT6QV-GBXTUeRNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8Cy61LE2r4YVN53D7luBK8hX9pVKFYQ0boTJuYwzgrRxEsr-_RMsNH53Vk6mnCic3cFUaaekL4V1RncX4XxQQxbrYzWzK5MKXgkgGJbB0ITZuMzqm6tOXRemdgv1WTGws7F4qn0rJHiK6Ewc-mZ-HUBAGi59ymCRn3DQni6tWYbFnrUWrlGWIaIquslraaR5iCEV32iLVOIYjwJpT0C8TANbEGpNuRtSazu5lWDyNEIkT-8Jbs-WRNw3OpWqauCWKrc6sB7ApBg5OvuIKgpbRvGmxgvQGRMTvQ6tr8d62vuVotIzBTImYx2uaHJg_ELJye9LF4dt4HLETitRLfxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpWRsvnsy8PdkCbgaJhU8dLp3zSN9ajRX7RxAosMRXQPKmmNKkc9AD4Kxrxz3INE0ee9WbYGIteN-kR12_okJxAJOTGhm4FRn4OvmSdytErKjjIPdZntXhAopDxYc1MnEuEcbE4l4WCEH3EOj2dzLqpqiXLiR3Qu37gF0r9rGeYwFdYBlMQWW1IT97rucHyLoLXUACKre9w6nOZUjXrchpHfXuItgC5sPyKkL0sUndZ6ekFjuEoQXXRi0v4J1sC5pd7wxCZDBU-8EVsh-_4DiG-jSnKXRXN82Z6_vzcPPYqc5zlo7sZlxxwxZdXb9obcsdO0Nq889H-CVR70bLgjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=KgOu2JGHhrlGFxCetn0jyHNAhyMJ72WMi82fs93J3s_25cOYmhjHz7Yz9OYMivJIqgfrcxtlyJuYFmh-H0WfEnzmok2kBqYqdILlT8Fx9dW-PoBX4rNCaKg5pzwAYY1bIlDuoW8YCzhJtQii2eZUpw94c04wfftRcVGXs1hCi6BFGAGIKIL__cfnkIGV2cggk6v96KdCzvi9jkhGw5gcWM-xtzcGx3sDJzYCfEL-64BOhHdwKQXhxM9xZA_XFcruF0W1foDVjj1fhsaZT8jLpTEczyf-WpDyyXsvrLB5I8YYyUTbHHK7xqrjXyB681Sj1DP6RKAbTj6-PBaaqSrrVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=KgOu2JGHhrlGFxCetn0jyHNAhyMJ72WMi82fs93J3s_25cOYmhjHz7Yz9OYMivJIqgfrcxtlyJuYFmh-H0WfEnzmok2kBqYqdILlT8Fx9dW-PoBX4rNCaKg5pzwAYY1bIlDuoW8YCzhJtQii2eZUpw94c04wfftRcVGXs1hCi6BFGAGIKIL__cfnkIGV2cggk6v96KdCzvi9jkhGw5gcWM-xtzcGx3sDJzYCfEL-64BOhHdwKQXhxM9xZA_XFcruF0W1foDVjj1fhsaZT8jLpTEczyf-WpDyyXsvrLB5I8YYyUTbHHK7xqrjXyB681Sj1DP6RKAbTj6-PBaaqSrrVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sNvi-4ljLTmovLTeQuxFwEg5QEuQxNjgAqNZ8MvhT9zLhUvd-PQK0Lz_efRm3KSFpnD4PPUvvhFSq1P0Xb0VF7jLsEptZm_k7V2BmnbNLyjT_qCDmSAMkG25UKXMfOGLXYF7xA8pqe0TrN_szbGyXL0pbBjc4JYIE2dU1Th0_eQWY45QNQ_sT1jhYz8KrVAyYGn5t_ZB3ZHcQ2IdjSrORkMbBOoi24oX_Tv7SWkcwo2JZnLQ-5vZ6CF_H6oZfIHuMH2uh3XVMNyrb5j0c6uGV_pQcsdoJoaP00tIfRoQtHg2tKNXc708_YBw6CAfAyEMjRLnVnHah_nih4cDgUpuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J_wRHt63htbxdQKQpSL5ZBpq00FUUsEuQzSzxOPg2jOJS5TEa6nv3sK9BaMbVmn9n9Bpqt61ls1XL8MbxAbYnN7Oghj3zgCBT9kVGBGLUmCMvUq39W1OZdG9vTJKfV2DMTtpuJzxP2I3Op0BbgSKdDWPd6Xv47SarD-g1watvqmqex2WHUyvxFIIspztpF25R3A0mcfanD6Z_-lUkQg8JzXQD-Vc3AsZHHnsiNKEwlBpBExOzm9ELdHZbddtpq360i0xbmukFG-lh3j7-R0Osj_QukZK-B9Ianx1qyCrtd_LAhi5UVYON4bBVYvyqe6iQOADE0tSgros0HK9Bloxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T8obxKyvf3dm65D6Z3I8ZIFxC4TSWz1VueIcbmxvtcd1GvRG660VG2H6al7-tUrbLhOxbS9SzkOjxyTkuPWxDPRN2Y2zewpHcGx6JOE3jfpM4OUYKaOU21KdlXywBegOh0ntBMVivrnQtaXhOrY2Ks8NbHeVvOXxD4gM2sP4KRrag6IOOxeyUdysx7ehvvBAnqFAVo3lPVpGO2NSPORmLg2F8nl-tlKcdlaoUKHVi1LTK-NZDGU6P6aoadlG2VTvEjBSySB9esm1RW0WT7PF3tym6FQziwyAOJ_GHjPTG9RSFDbkpgejbvRlA3gyop1e5Pbugr96MUk3WOn2LCQVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ln0rfiDmijmKswxhIAewfQZXt5ND23WpD5daL8wpLyTfHrh5nNLNvzf0TgsSLhqfZOj373Mz6VqKboQeXwl7RozfzL0EMrDbs8jBJEzPa9go2nd40Kkwx4IFaq2smKAwcdCNwXY_OtqkGOs48Ka1jHgRJw0U61vhYIhDtyIqnxFuTCvGJFqpHC86dRQyp2NB-PpacAf0wMZuMM5_PGwdhrQgY9csCM7zRdtPHgEVH7hvZrpKo93K2rkZHPRDYF6yMo6AMYpswNjCJKAXAIVSyD7_JnTZoBpVkKRWECvh9obF_mctgEt5yUvVNSwz76MkR62ZlMGaw3VSCjzHVrXSqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o8EZYyGPnq5Qf3M7AcvZgEm6vobtzShTdr2pvrF6WcOZldsuNRlJOtiq6VgRMmaB8jv56ugd618IoobYY1YT_zE1-93Rls8yrbODV3nUHuTX-qhtyjlGB-decLHBduJmpxp5rpGGaDmzEoIFD93dsjDdAQukvfX3ixbngLxtABOUFizyv7ROKMAJ7ytIiWdtrPlTp9hC6xN6Zs1tvQEBgpKBiV95kSPftTrB0VXlOl7mApCX4gVf1uyHmitWGuBuYkPU7RIC0MIj0Fp3tD_3ya-GfCp1N6RBXWrqb72CN3fC3p1j0vnfQVWDPr1mH7rfEIsthsWKm-UIz0sW65RQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CUogwQ1_EzAgdZkRMgrrAAPtuKEr9oyWLG4fem6by_Wao_rk5YXFLhwJynGk898oU3j48NY6nR8c8AGiOZ_mMYQfy8HG5cB8YOkgPDFFQ-a-L1HU1Ks8l6lZL7_0YlF48v8HtDGuArDgBA1hhQ4oY1eL_ZycVQQcSI84j99qDssR9J_Iq5xz0ek2_Q9cPvAy5EoCa_nBl6zlLY25We3_oONRof4n1HmsS0o9qFtorJwQ6bbtbBEzRQanOEzpA2FhE-xEMo8cZho4YLWSGA3YGTA-iNVO8rD4ZKCo3sH_wO03ocrNQbRRFoObGoyv01GAk-FtWiwrnkUcxYP4a-XEpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=cySI-IcXhuVsBOlJz6V-EHRuIls5wjGcwqiFRr2YB_IGpCy7lKveVHaxC-9fnsl5yCPa7LV6EaxohpDNwti0bLVYelT9KkU4HdqdmTjf5UaD2MiBPAD4-oYPl-rHe7mFH3WFnBZEIU8qOOPTQldJ0YyencwBk8Rsf0FLIfKIRVtR_lM1Fn87nI5zJl8fom0G9CHrUQbzrGlQY7lm_bq2IYWJHaQmrhADu48FDUBygXUvScIJGBCYZ1iTOO_g9Dy3TLJUBdotTxVJp3T4z6gqvTQgWWTjTUuVIKUSJVYEj9Opt0KTsm86C2XgXMfqOc14IdDey-ZhdNQQ802JNo8ljw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=cySI-IcXhuVsBOlJz6V-EHRuIls5wjGcwqiFRr2YB_IGpCy7lKveVHaxC-9fnsl5yCPa7LV6EaxohpDNwti0bLVYelT9KkU4HdqdmTjf5UaD2MiBPAD4-oYPl-rHe7mFH3WFnBZEIU8qOOPTQldJ0YyencwBk8Rsf0FLIfKIRVtR_lM1Fn87nI5zJl8fom0G9CHrUQbzrGlQY7lm_bq2IYWJHaQmrhADu48FDUBygXUvScIJGBCYZ1iTOO_g9Dy3TLJUBdotTxVJp3T4z6gqvTQgWWTjTUuVIKUSJVYEj9Opt0KTsm86C2XgXMfqOc14IdDey-ZhdNQQ802JNo8ljw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjdZpmTN5bfR0weo-yo3spCGPPlMA9HmWnhVpapKya6hUDJa8oeAa5ouP2AZ101k-IJ9Wmrbs4sTMMg0FrK844-IhgaFz1Cw04HQ9h60VNk0aBobg_S6_jHb2lajipttYDrYQgYDh_iGnkfditrem3U_j__PFqdr3JJ5NM-ZVed4C9rx-LAdhpgPu51eUiW4trFLFORS0Rsa4rcFc6R-5j1FRH-sMX43hlm6rSh1r9l8HrHFyDRCQtfro-bCNUHGR2n8vCp-Q2gWXWN2hGx8je3Ul5Pw1M02wPnajh5D8TgeomYDUVnw-hUoxA_4mrxe2-HsKLJrqB0wPaPKqiu6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=MEPQCBrHEXsYOP4Wgag5PnYJXroa3nAPAMIJ2hN5IJSRuq84eU43CfOeOMcMH8YexH6ahMlm9bgPJvbV852Kokgr_4ZkIoBUk4i85-bxT9aw90rVaK2Xko1wwpTrAPdP9veO1T-cR_jDmJICTTYt5r1F7hTMb0QpAuJCre3oxH2mFgwlKYx4lrrIM8cHdu4ppIZOjMrvTVpRrtVFLHxx8cSCyfgpzlhJ-0-Gzr_FQvcznxtsFM1sffzERc-TW5KCzkoH-SqzkGVlSHXbX2SO2KGBunb_y9FNJynYYaowbGVCwEm3F0jNYfrq8K-8jpPvYkUnna7SJ0q32SYuNFKTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=MEPQCBrHEXsYOP4Wgag5PnYJXroa3nAPAMIJ2hN5IJSRuq84eU43CfOeOMcMH8YexH6ahMlm9bgPJvbV852Kokgr_4ZkIoBUk4i85-bxT9aw90rVaK2Xko1wwpTrAPdP9veO1T-cR_jDmJICTTYt5r1F7hTMb0QpAuJCre3oxH2mFgwlKYx4lrrIM8cHdu4ppIZOjMrvTVpRrtVFLHxx8cSCyfgpzlhJ-0-Gzr_FQvcznxtsFM1sffzERc-TW5KCzkoH-SqzkGVlSHXbX2SO2KGBunb_y9FNJynYYaowbGVCwEm3F0jNYfrq8K-8jpPvYkUnna7SJ0q32SYuNFKTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNeAELRHo9djFUw6zVKm5pIGO2OZN4B5Gh9pTMZ_L9fFNlI4UQkLgyxo7evzA1BV0sYMY5q6_m8tbfrz2RaEV7vMmlPgQDz3D290hGkyKEkpdve3HNg1nce_QQS-E56uEeVc31InF_QJEXDo1sphuW_t3Ymsy5Wcwf2yFZP5-KlqL6Yqrcp-1B1SleJ8KmfWJ9Y2x-dc_fvDKEw6SS_bVhMp5ExHcFjosPfCMbztb0S6q9Qq826hj7Z4ohhPR60ho26CpRHpQzba1YxXZUut3h5tDXmM78fB7eCrRT1cS1Tbj-xZP67xPZYTrwH4La45eK8CeHg8ue6Ti-gvQlu84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_c0T747Y4u_qLKQHgdDFHd3uwNEXaeEyOEQdxWaKvC2ANerWO9D74-1ucM7HgrwaahHoI6Yxv8NhoT2REYfRLtI9bD1e1YRNmZMlWZZKenbeAsKT_9oAggIsSo8l2ix3r8_0_ct6dBoYY8WeVQIIR9gvEjfwKhj1vXu7Uww5jzXMYwq87NYb_T1nlcK15PmWuVlW-4KNJpZ7qnSeyv19Cpfb0rxDbSmKunvzPJaW6CE8XiPttOq2Cif4uW6jS0aHEtkD1f891bMG9TMZeln-jAHL0RlNZflxucSAeiwdgmV54dVkx4TgVg3trIf8dEpy5l0_NMWD13HxktGXr461w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea6N5mBpjOrLqE_Sj6SwNecAQUmsyKdn7lnU9nIIbPjztHFpfc6JgYIc_4R-lxKceBhPzpGmJBgpTrcScZyvNrSzOweCV2kVnaoi2c7PkPUnPeinAuH04g-zBrg-KVmMM2VqPtWTylP2j3xg9B8fsxcEbCIOVbA4XbXYPjNggzFf_IMrNGREpdgzkbcbbdDoat7ksqw-uBu8nD5t0AwbViGpVHEge-1jJhXtXruvW3IQI1o2nFlgZEIhG-app-wVvutEIjg6vsHlr5GLck815EP2jW9OTf7eCkffpJwrLGjDY7iEsCHzIG8lF0Tltvz_tIkiCkpTYiUtFQOZZa_JuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHRdHQCjrGZRFAxWiMXFmBqYqUXvbAvM5IJaFmgjnLobU7JCs-2FYSuiBIMiIX9Np9Sc5cxUmcvZGOtHDHMWAK6lBnrScQzJMZEdsWXFRorQaas8yYsinMWHPFxiSTjgIfY0lE2GU1UUjKYlPzBfBumRc-VoJQ8CMco8UUnjoczaLNOTDOkGw5tjptdGFo0TsUP8qirs8-6vYZg_dSghLGKW7uA17JO5-nyIgd9p3iDtl5JfoSsBYeKnjFDaK6qH-_U_fH4oXxajTzztSgDirYvLS-5rPQN3D2LjvKtMXQ5OnfMljtRRBOgSguJKkMF5j6-54ENUPGRRCqJRlJWDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ndvs6CXdPRz1SaQZdTCPsT_SrpVvG_y3g_OQSIIfWWlsiebaKa6A8StNR_VLIfxjEBoKqDkTBbQQ20893d0ahikMKHDSz3-7mwmdWc0TC-vfLk09PiExVyDU_Q_04ospPAuoHq5giQN9kHX--D7syb02TqJpFVIzhUmQuwvt_6XPxgM6kCVnJyynC6xn780lDu73VhhI1IhxRnmV3r8-VHGcr0kn9zmTShG9hC2KpUeK11UrxfkD_NNK0Qs984CvAPixsT9UmkVGNEqDI2cvRptHrYxtlEprUVmepBP9q7L-Z1JjkFBp5JUp1_cWRa2KCyfdSwySvxjauAH9OYapqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=jXG4XQcyNzpcB2kNaLKHDt60pHLtIxF618ptze5-ad8krr6ibHHDzOkUra-I6h3YqemBTlDnpT5Lk1E4s7hxgULUP6GjUOOjy3TLDhujrop-irRSfALZJ_Vx1ACLeTYtX4YTwHoa8eYwwyFKoHd0lNx0EyWeYNL1-QGlA5aU13A_BJyKa_bEH2LEEzqGlqmjSZ6p5ntqBhidhM-ayVyn8eiApl9kxWAqfJlmvYRpa06hBYjy92SxpVasBdrCHdDEfkivMdbQav6Jg81g7L_Ok-QiVI2Hkr93cUj9RA0NE19jkGCltE7VHBY6ehOmPiYmnSQs5cDmlbC7ZyMfxeZXMSGlEi2s23empvtmT-cOsRQuUXoiWWpvTP8g9ktj6Ut_UNfy-CCzzrdJHggO1uqKsTaZRcsmPUPf8WJT2AIVHLVHcAVX-g3FU8fVRtRhj1jxebzauB2oBLNA6bqDm9fDHMvGVWIkgAFPw0_MT0V7eCjTUvzB4786R6_HuygwOTshD2zxlg_0XijtYB3rzjn38c73d-1iy8nGTw5GwFzpoHPpE93SRCGGwpIYGcbUJlhFKwhnd6x9xzHCwXK35-pWKuQBCryn3c1B7IWuU_4He1dApnznAxl6zG3OM5ceB_1V8pJDH9YyKoDCBDI06eGMiqgSyjPpri3LwB9T_QEqhdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=jXG4XQcyNzpcB2kNaLKHDt60pHLtIxF618ptze5-ad8krr6ibHHDzOkUra-I6h3YqemBTlDnpT5Lk1E4s7hxgULUP6GjUOOjy3TLDhujrop-irRSfALZJ_Vx1ACLeTYtX4YTwHoa8eYwwyFKoHd0lNx0EyWeYNL1-QGlA5aU13A_BJyKa_bEH2LEEzqGlqmjSZ6p5ntqBhidhM-ayVyn8eiApl9kxWAqfJlmvYRpa06hBYjy92SxpVasBdrCHdDEfkivMdbQav6Jg81g7L_Ok-QiVI2Hkr93cUj9RA0NE19jkGCltE7VHBY6ehOmPiYmnSQs5cDmlbC7ZyMfxeZXMSGlEi2s23empvtmT-cOsRQuUXoiWWpvTP8g9ktj6Ut_UNfy-CCzzrdJHggO1uqKsTaZRcsmPUPf8WJT2AIVHLVHcAVX-g3FU8fVRtRhj1jxebzauB2oBLNA6bqDm9fDHMvGVWIkgAFPw0_MT0V7eCjTUvzB4786R6_HuygwOTshD2zxlg_0XijtYB3rzjn38c73d-1iy8nGTw5GwFzpoHPpE93SRCGGwpIYGcbUJlhFKwhnd6x9xzHCwXK35-pWKuQBCryn3c1B7IWuU_4He1dApnznAxl6zG3OM5ceB_1V8pJDH9YyKoDCBDI06eGMiqgSyjPpri3LwB9T_QEqhdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFZwD5BqlBgKI9JfcK-ilVPOvb1mQLeYryQrqcsi61NJ4bajSH_DpkouzSQKOql3R5pk7OGw36NCFse3t77ONYKfs9jm05JFjCboCT5Q6-syVqqqCK9Egt14FlE7btbw0nm2q-vLUgiew9HJvHsivrGEwjHKqpe1qGWstTpydcbjFhkfiKcUyPV8D1ZAx5VEKOj-9zSTy_l4nfkOcumhxB2EzuCC7l9d2ZIiueYkqB2BIxHTYFE1dQHGbo9AnMCt3-PolHZy0LNP1rhn-fr-xHMGxRlkE-TqZGXGln1KK5LvGqpgwYQJe1t6l6tphqssUYF55SLRWwOpf5ehhVBFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
