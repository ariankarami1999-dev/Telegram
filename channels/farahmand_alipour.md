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
<img src="https://cdn4.telesco.pe/file/Xrpecfhh4mmjC7QpsJqzy92vUpklfRToNPS9WFpPAu5LFmxvA7CCLtbaB6w5MApazSfrghrSIYOcBsiklynbKJnqH7Y--eSt2D1YPu6iZJrA58YFcJYriQudrjSiml1wG2CBfRtI1ETnIX5tg2ogxaxUp6xqCVzUW_Arv404Bti_c-EOrtpc66gZImLKuYGD7lGdL8xZgHGPbrYYY9FgpwBES_dqPS4u63cu1DYEgK3HdxzQXazRS3WeQvtJSTT4FLm-GdbDb98xxZhiG8IbjK2rhA-BbD2IxWC9ydU3B3RGc2sB6ZfGDuNC2KjvkuY1StKHVdp4hmF_ckEsjQ0QQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkQFqqRcsKfbmtLiXb8yeuh1buDJXGpfYy6oU3T-cemFomf-K5owK8D0oC97TxIU0v2nhfKXehHTr8MtmnvXs31kTctCHUvftIvS-Ioeh7jGKyM0MS80YuEoLsoApESMdcJGmc8aioVg75OUmQZmJDyT0bKEtCttIqMhCybsPVAllKyt5UzDGrdzDox7Re80izfZ9cSYVTj2AzXzi6dOc9Tr3lyY_2v-IbyzfR2DVYNWMec7eUOgWeTuIgICeZsJNAzf0XQ8lkbIQ8T8tL7PueuCp3-NaCvmcjaMrwAuTrz9Rw1gf-bbhv32EKH78wZMCmKyOMX5F2xEqv4ERUpTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhz-5BnrPY5To2QcI4rTr42HJWyZdnFzkMR6L8tIk-ZlEFfvgp4MwjovRhsSqF4faseXwea5MvzjtXV2v3pcmpfw66Uax1JHoudZuSSJnwfyl_e68rXtZfK5F-ANyWoPPOOQoRF0tQK9MSkLThlVNDQYO0dLpNgk4TYyhjbZMmqdYv1WO09uJ16u5GwFm9zZFqEZPqNx_NuulItjKlVn-HD5x4oo1MqCNeuQItMCDVc17kcwmhQntQhHKUe1oZYOtkrs4T_KNtgDA27_9qab2c-L_xD3pm3GqL4xIGjRJrKLcZuBEtTTuJ9rkSPaMY_p3-Ws9OqfrscvfuDk9bG3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=tm2bcvQLJoQJHhw6g_5QtoqvPCjla7NVCSHoGI5PYUWOCRMsLFFi9hIuQqI4nbkvyLmoAivVnIXYqscKrbHFcdoxJmjRJBr1z0VoccZgLeHkkLJE5AScl8F-mR9e5SdLgxQj2K9Tnfz6uVS9fYSRoV4e3ZI86qOw0DOmzsJ1v0DWPXU94QYVk0_UVZ3x8JRPgGpJS0yvTtSqVffZg--GGjK_kzvURLcnTTuFHMLD1ixWsC49h19yCCT0yLVlirzH8xdGG7sk5Ae4QpU_nr_4ROQqWxQjLLUX9YMJ86zTMA5nNxGbi-vIG-mffTOdQRDbWuwJdbm_AeZmQjM8I3Gt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=tm2bcvQLJoQJHhw6g_5QtoqvPCjla7NVCSHoGI5PYUWOCRMsLFFi9hIuQqI4nbkvyLmoAivVnIXYqscKrbHFcdoxJmjRJBr1z0VoccZgLeHkkLJE5AScl8F-mR9e5SdLgxQj2K9Tnfz6uVS9fYSRoV4e3ZI86qOw0DOmzsJ1v0DWPXU94QYVk0_UVZ3x8JRPgGpJS0yvTtSqVffZg--GGjK_kzvURLcnTTuFHMLD1ixWsC49h19yCCT0yLVlirzH8xdGG7sk5Ae4QpU_nr_4ROQqWxQjLLUX9YMJ86zTMA5nNxGbi-vIG-mffTOdQRDbWuwJdbm_AeZmQjM8I3Gt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=n-oUFkiJedHevY4_dJ5tflgN_PR5Fy_gbk2_HFOzo8mM6Remd23YGMOcvssR9ugjD_g0FA_GlvuNHxMOxuQYK0ZSiDYsZ_mrTEIPCKlNfVM5CPGXDug8UptnQGpwDCD0rtrDm5aSebibvv_k3R5uA_wM9ydTJy4rk_NGLhvW0QpIZ8iiUBFIysT8dNt8YUdVD6j56CQXGBTD5C1jx6i1bjsm6shQeNyP9nY75XD1NfV9045bJF7qopghuOONYC-OiohC-OybkNrx2uaP1gMyle9aSR_dQ603PlP6XP8JPJQoc5oSlosdXew9l7y3BOjjQOkY29bYAM6UvNrLt4JCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=n-oUFkiJedHevY4_dJ5tflgN_PR5Fy_gbk2_HFOzo8mM6Remd23YGMOcvssR9ugjD_g0FA_GlvuNHxMOxuQYK0ZSiDYsZ_mrTEIPCKlNfVM5CPGXDug8UptnQGpwDCD0rtrDm5aSebibvv_k3R5uA_wM9ydTJy4rk_NGLhvW0QpIZ8iiUBFIysT8dNt8YUdVD6j56CQXGBTD5C1jx6i1bjsm6shQeNyP9nY75XD1NfV9045bJF7qopghuOONYC-OiohC-OybkNrx2uaP1gMyle9aSR_dQ603PlP6XP8JPJQoc5oSlosdXew9l7y3BOjjQOkY29bYAM6UvNrLt4JCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaGvTXofqPaoLKcvQmkFYw_6CLchvixpb2edDKbgFwNRIm9UgJEDolGwAXRSf13qk5Q6byGyTgMURooaTFiDl0G-Q4I_fZ_wuKZsCg1wgQurYkUxURKTRznZj5_w8jfKyvdsX7Ag0IDyjEIo3dv7VORxD9-fdFA1CHaw74bTxzkSY4EmK9XyGR1LXf_-koYzyejvOTJJLKaYxapUAYbC5sApHywFR4m-FgROqOd0AAjqQTSlfpjYXtSdGZnK6EfL_phSfx-mJvOZUoyulOg1ITSUu3CFuxSO9iJpJPCrpVUuwqIOwSy3TdOiUJwa_xR5QOP-5Ox7CozYzTSFCSmwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=CizU70p_xv31Lxo_VPUwQEnzfuPiSj8_XaJgqZyT89d0FQGy3qE7tsDcay3VmXFYuNav7Oh4xNxAcooiZMm6B3sGWtMIL6Psf_OD7R1XPPhhGaKrLb6RLLhD2fXXb0IroLmqb4RcGszwsrCGwpfo9a1ViYyTpuBPdAwAW6jscb3_Om8tIBtrT4wtynkiCImGUHofwWRLPdwyRHsHdGmWa1CZtdIqC8N0MMjWoAvpz4ToQiYGXvvwoH5USZrLtOBcx1SH-vyJdzDb1fbSf517D4oPTXx1YMhu935kOjDhr5eb4vjiXFeQF6y3xocBlWRQrBBLg4mMkjy7aXwtNbsPFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=CizU70p_xv31Lxo_VPUwQEnzfuPiSj8_XaJgqZyT89d0FQGy3qE7tsDcay3VmXFYuNav7Oh4xNxAcooiZMm6B3sGWtMIL6Psf_OD7R1XPPhhGaKrLb6RLLhD2fXXb0IroLmqb4RcGszwsrCGwpfo9a1ViYyTpuBPdAwAW6jscb3_Om8tIBtrT4wtynkiCImGUHofwWRLPdwyRHsHdGmWa1CZtdIqC8N0MMjWoAvpz4ToQiYGXvvwoH5USZrLtOBcx1SH-vyJdzDb1fbSf517D4oPTXx1YMhu935kOjDhr5eb4vjiXFeQF6y3xocBlWRQrBBLg4mMkjy7aXwtNbsPFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBhpjzM0O9ZGJfDuj5xn7ekdVcpCQaKrr7ZVymW8uYsTTkCrYDQnBniJiIdRedd9durnqQrFBjoYo_EDW6cEa8J2be3cUCGB1KxlV29u8aOfT1FNOkv4_0RHbtplVvsqplSWobfz-ug4ScUNR0Ad0xERozj3G0FI8S6PKE5OM-Z6rirtBO9nZmG5a_Li_76qa8elAb4_sYjZLbZZ2twv1rnNNvlGvx0hlmJEAMfmrPxMF4VBh1MIbYiouyH7B5K8KYQEGVS7-8Wh3DC31-xI4eGfMIJW4_Z6O3AL3mIX0z1SWZlVP_fOZjNY8VbmPjQWgQK_GPgv_lt8AlbX4rrQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNhMfBODREZBq10Dir9JjF2sj-exNZgGrKCBr4_axTL0lg6wkCBhnmeadTrgzmRq7D8UV2hTrg_seiPb4E_aN4HY90WPlCg4T3oRtEsYsDXhns-cRXfrQXvmtv6YRmf_S1xV2Kf9pQnDeCb93Wh0GOMm-6stzUgavW9x39tGjxKlRlaN6lvwObsqyKy436285nKmcLZMB3or8aCXmhTC7cViqpFNCDzvcOXvj-sB0E_C53JhlmaiDHzp-9ZPGj-rcJzW9QTCpmHM5lgCgeN5c0l-Nl1j7MUFuhcnq600ft1v3-5qidjw_YptuBHKy6MvgFfeCmxuLtJm0HvDxZQPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jedOQf2yrPmBSd-9D_w4tgigCXnnALCpu7664rzl4SvRq_lrfjOkPWe7Rdensh9BPcYq7vKZezuSCJIHgO-3ZbgwFVWj4BR3FD-ufQgXzss09r7D37MDBQr7ZMq8CNtiM3a22ipFVlrZjWu1IG2ryTOyBZaDCL59-T_WLO5dbh3iQebcK_jw50Gj3pftMNf8eggvvYl_85kQOgNJPneFK5rju8bLKaMMRJ4MaACWOy8YjhXYcjanJNmFfg2p8qh4NmOd5EacYOTpPrn82iyk7cVpbDdgRiaK6SiSk3cdJhYqwqr8_9jHB3cBINs-xrddoyUn01OgWb8gsuQaytwtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcjDD5JQyWvf5qaygOd26qKLtIp4HluUk8_qUvTUB4c_Mk9G8tPTwKtCvwqKoKO1y7xt_0V0VC8O1NxY2qjIHYSKQAwOUR1EoEjiEs-ldt6oNxp9ciMRj14FKcVNeVazoS375dX9GO5EK_eG0b8oM-NHCkhq_pxNpchVk0GPwGk6qfb1be7oXKWkSw56THruNj6mowcB8_9r_k_BETGEfT_WUZ2uJ5G05-ybp_dy0kn0BmOUNhskJqkP3pO_tMCMoZHyGqY4Li_9Bz7KOXe5bltGMrrIVe8EwQp_HZ0BsdNPk_DvwQwJtG7LDxM-NT6GfZsZJ19w-uiH8J-MkOGQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZp9kMiGMNDc0Y0kh3uuKEp3ePFdx442_jPZTDdhNj28bGBKMfTpA4UJOh20mTjlniTqtlvOq9SpR1o9PdSR48Bqeup1xn52KXJ3gmpsXUzjyu1XIP8vxBLLK1aR8VsarAbx0Y6KNq9sB_5PVLFgom-lmhbiN5EkbkmGShW7MTJoGH_zvr1lqBtl_6nlv7BXAQarRK3CWJq0GGkRanKjxnPGdwyqgYaQePVipXKpWH5sOF6Wgx_lOqQ9zU7GuY3fh0DWFqOsNLCr0xOJgQksM5iU6R0QjhAMqeBpR9bnYq8TVgdSHEw0veK1DM1OSPgkJTfFuubmkzxivyLSxWDZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnT4C_84aDp1woZtmDNKisFOgg5qha9GX1wN3ztexsrQWm3A5tYrtgGUYLiIXtBrWrKGty9GLrjrQhuVSFaRJioDYpDrBBqTOfwlHMu89M1nkFqiYUqJypM6TBMArJMOMDA_63M--6kqCCvaixvdOWldVUn1eW9_PDnT0kb3CGTj42oYkAQyWrrTRiYIe9e36TjMftATcrZwnZx7pFmYj8u9Suoe2dwOZysH_gaxj1L6kujB1kPa-AhWIzvhg02WQWUplxVyBJs088cvBuaOvq1Bx85tzSTFzEo2QsjcvwRBJMdZVacdxTsYuaW3zLrkfU-z_IRxO8T94aihJiwapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=ThxcmYzmhS59sW7Qpm4VjtroVedCsSbal4GAP5MxYUehx4JPhxJtDG2hkm7kJ1ztF8TleYZh_2qHPDF_zR-RhIdZCgHRfoY-Zs4MYbtiueYQh_cZ81HyI_9E3wbk_zN2UUWb8ScNkPJmutNtHL68F5DsADLoUKyjyRXmaboVGEmYYpd3irRT-irt9i6Zm5TG74KatK2cIsqS6_LaSIimF3Nd7MojexWjv6e-NwI2Kr9OcQLrydjUvQKlFvmrJrNJIhAGJ5XBz8QyKIymQlBJUkF8nv6FY0KABJJnXaIuXB7MASz7h6cqzXoO1FvDF0TJ3TBKlXze1_BdqqaiKq0xrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=ThxcmYzmhS59sW7Qpm4VjtroVedCsSbal4GAP5MxYUehx4JPhxJtDG2hkm7kJ1ztF8TleYZh_2qHPDF_zR-RhIdZCgHRfoY-Zs4MYbtiueYQh_cZ81HyI_9E3wbk_zN2UUWb8ScNkPJmutNtHL68F5DsADLoUKyjyRXmaboVGEmYYpd3irRT-irt9i6Zm5TG74KatK2cIsqS6_LaSIimF3Nd7MojexWjv6e-NwI2Kr9OcQLrydjUvQKlFvmrJrNJIhAGJ5XBz8QyKIymQlBJUkF8nv6FY0KABJJnXaIuXB7MASz7h6cqzXoO1FvDF0TJ3TBKlXze1_BdqqaiKq0xrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbGchlbIgvf_TtX3XKBD6Vtw4ahZMu9qlmfwswXlF5OR2XUGS8xkPChAzD-1amJwPYxQ_Y9sSsfewfCizScZTjqwBEdMYilUXAqO5oKYLYcpW9QrfK8ba6qFfFQL84XGGFHtUg2LEGv-oPAM0IcPHxMUlo6aylxXk_wpGMLUQJLOg1YnqA5lssrxWa_bD0VKg13PGv4voek0dT_RFVqAxHF7ePWUB649f38u_L-foGCfIscSdTcxuxuQHSKBc63YwtEwr70B1eTcGWwfgpjFMWVW1ASBBb3lUXUOczcPSYD-rlyV0c6RvzQnopyUX6eRJACuGbKPyrMaogEAS8eaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOPw526fTzdcl4ZjOc1ux12iiQ933ZdWVP1bHuLuY1FyvZ50k4_PsCkfjRGm1YIqWt-E7sT4Vl0JIgOdaIDjruTWjSiyEPNIzNGcEZ7Kol6vMpy0DDoqMO-YbA2QxlgvSHDmIBKKzyhMJLINYWESTOUmfXDAnW0ekdF34r8J-JV2X7TRD9CBga3sMqQhZ0cP4RGBq8RlN1iTG_rU0WMg2J4s5YxxShfHJW9yGIHgjdBdr5MLKolCrSVDs9huHQoHhNwMZjYfifdzOycQqGWVzJJC4lY4K1isrKM-tg5iXHLiT7nVxDIJOOqC9EMpSro-8boBNc9hSFmV2Fp37Sczng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccowhK36Q2WpIwihPfDm2mUN8B9H3_zgwN91Bsj3NsuRZH9rVzJw8BUcSz8ox6IMQgczIntxedk4r2915wL3rnpn7gi2f2uHWx_9pSd2h_RkCqXNxPGWK0XrYZfm6g8OdAx6ZpvyUNWlixHEnB7Zu7iP-oLX8ilX5CdTV7ScZIipnV3JrVkDlOFFpx9pSlna9jXkYlC9nb2FM8BQzW6-wJ2K3m6G9o1bNhY7fdae1anz9ijjQocEw8VzKrlI4b_4pnbAh6rUOK_lZZXOt1QFSZkX_0wIdWoGVcsn_ssAh-qPHAIqVY7XZKAhObZSKKm6J93mRS7d4J5pZsNfyb2w3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwekiWY9CwtUNyYZJKzdCEt2u5GyGtIuHpa2V6WXTk3JZhXu1wh2OKjiDsoqWqvrPyHZnE1NA9w4HF-rHAjPEwKy74nOPyHkCRFU_-tZF9rYCoE25cElmn9gxl_yJwJGypGB_2_LFLtjkJws9-wDZnEiDbk1b17RVcqNyvsPQRHUWrVyIMPHmGUO5Mto2XCjmIMM0o5br1wnykK3c_KsN0MU2R-w3en6faSM_Izyck-XJgqmyyPPHdcuc9iM0KuKMt2FtV1ZsSyyGbeK25p-E-AGu4-98NmrBY9WNH2nozEkYoxsVSGZu4BTmyMPypY7_G4OwDZ2REvdclFzvWJwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=kwwNgyJI8Aw2tK76lKb5KM9ggiDroLxsIXFuHI3MLKncEYzOwaFzKUa81D06mpqaK4KX4aZu6oE0IxQZRQlBslbw0eeP9zvCqTIBJXHfatIItd_Ytm6Sv6I9JIBRJ2asHhmXhhuKfzd5zIQxy1mxsEm31D9HZ9uRKO1mw2yvhq43LejqWoJUzlI4owSRGP5zmYruKeFY1KVHdFWg9kg45Onw4O3MUnl3cMnodWX9WSKwsZoPV_q63g1lcucZuvrp13f0N4ZaRqG81daY9MN02fquDxd-S0t3r0ul3fhV9NM_EtqIsVE3KSjc7rU8Ps6a8IZPMKPTCP-Kx-LZWKpW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=kwwNgyJI8Aw2tK76lKb5KM9ggiDroLxsIXFuHI3MLKncEYzOwaFzKUa81D06mpqaK4KX4aZu6oE0IxQZRQlBslbw0eeP9zvCqTIBJXHfatIItd_Ytm6Sv6I9JIBRJ2asHhmXhhuKfzd5zIQxy1mxsEm31D9HZ9uRKO1mw2yvhq43LejqWoJUzlI4owSRGP5zmYruKeFY1KVHdFWg9kg45Onw4O3MUnl3cMnodWX9WSKwsZoPV_q63g1lcucZuvrp13f0N4ZaRqG81daY9MN02fquDxd-S0t3r0ul3fhV9NM_EtqIsVE3KSjc7rU8Ps6a8IZPMKPTCP-Kx-LZWKpW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvhTRy0IKleKY9mzW8GagJT8R_aFNyQbTk6s9fINxR2Hk8dSScmT392tM0zkLQc2qQLQns6KB2nKaNjSSHqrBOxrjvp3O0i34KPNN_MVk4nspqCoWPf7ySQQ_iU-nfNnjN5fKyGswI9J63_am5eO19ZGPQMDaDdGR_iw3aD4qZlk__7VBqF-BfxyNs6PXibf_XxgsYg4t2FSunbiynXcGfm-jjT3CA2njuBfSOkP3C48tFUM7lYtGIegR47NIFNUwv9QSanPZyGN3ufEX0MNJ_xxxVu0ZzvYX5YB4XI4Du5pe-eVQkjI5HV94cse-59fqAFEbQtFr1-qK4HsRUBkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrtXemwnSSGkqKS8722iD_9ZZG9f4WKqcFFQLcefLxkGuqRxgAW7MTFIjl9emO2gcIPG-tLRhTqNF-3tA8GU3E_SdKNzpSePasWV2dvZv9AXrzLBxKjUcMT8do5_toIBGSOM3LjXxTcB1mbrdFTFwJhvoM5O45TxT2I5Av1Ohf3QIzeGvlUw_4_Js42iP4xNelHo0dd40nceaBthFKAw-M3GuuJn22DN3ZVm33LvgRgM3sayb3UKF8bPNybRttxdFkAKRX953B6U1Q1xYpXXFYKShKW6bc8VUt08zzxFc1QtHRfm98wgUwqYOm205Jr3jhez0Rv1LnOKVQ9twQfWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtLq0xsYssyNlTzW6-tgVaL1fEcCZZQFP4e_UOO12jimT95dLaDT2sCjYaXLTMtw6c3SAhdwEblmZRXs9dk33w-ASl8ARaCAMKlshRIu7Da244J43fB8ApaoSpR18N27924xvMrG3a8BonK2HNxFXzcjyWYZrVMxuUIwR69a799j8RO42r7Vd19FRyj6BCadMpZQsnPZs7rqNwmGZ1Yrq_2t6jDkPy-w3LHkLGTQ2EhCE2s_Dw6D1Dfg8EfWbOAckgrmE-8blpWYOD2vvDmWrSi3H4VK1xnukccre9oaQ5xBRsYaORgl4pA3_bhATlGjltfQvdIWJArx74DhHqZ9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih_oEfvSml6wNnfTXkESDT2p8QZUEaEjt74DXbJO0ynbUSnQsxjS0E9d1QAKnkzgzAQr0aelZVGpsDvNZuUZMLqpKQNKeSsvQrMAcppeB2L741evwndNOlhkS3A8fblf6os9UDBOAB-ePsCQiRx6C0fYji4zEIHrzt8V1jBELEORqtBHGY4C5cHLM6OIQnSB4kcW5NHDQSpoH5qA4TLUZv9g19W2RxgTO1DYrHVmm3BV72zHMAEk1pgygpRtGH3940hdiEaKaCbGmVMxfNdoya5iHnCuGg1Ake1r0dkvwePt1W5PapyrPcvPqKzsfvsZFUh8lWeuzlVvk1GyXp4q0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-wyozlKZNdsXpYka_pvoeHmFpNrld6tbR22nbfueApWKsoxoqCkqpPOC9kd2Tx1a1yIUppYM44iJo_tiRhsXnXAZZYXHiHzngXOU0NWxJ4QPHCv7QFAXQ6D8tAQNu7z6vE8dCAuDfjmJEGORHtavBZb4beDHpxbeb7n3Pux3OwQ1aGS59sCj1ahH-_Eq2fiaUjBeOhr4WSJZHwgzkMhZ6yFvdDMMIE-erO8W1q1Q5lDuIwhOZ6uVNnZRC7pgx2hY0HasGDRecGDEU1snabGVKPoASQmuaImO2o9scJdxPVZLFpLzzO62EvhDEcKUX8qfuteG2PGzSVhs2SH7zdjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otd0t7KHdtY6dLzV3Q7c4azx4v2_rx9ZxlpPRioJqqGgCVc_gAaEB7pIhwoHe_7rH8bvDqRIPcaa3euwTyt_XEyfPnTxwM986r-6yyGVxEGW7kKM-9WSR1gOMOYRDj3K9uaq0c0dC56Muagqf9aBaTE8PaxEwX2Khj__yUnV-53D3DwDuLXMh0kCXOFwz3Pb99Ch1Ht40qbBYRvjCKck7ULtqZJnDlxL2xoXgVjp2hCR4zmtfODts_vmSwFaAZhSCopWuL-7C9m17fPB1yxSv3f8v_MdJ0ILdlXMLluUJo4-fg4_oPaLgzqcB1G4mAvDuU5frvXUGvZcJPW6Iacvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQlpYHMzSrAOuxkY86zVhrVgvAweO-bMO5FqKcv2oxq7nUQmGSnR28Z5XplRuWgBoG0cpMvg6fYu63vKVW43MsNRnCpRolZjHPIlOu-Q4ryFTU-xH5xBauXZ8xxjKc3EgzfDAwqtxszVnJn1w1bjW9st5BOd2M76UBb7xi4SiCdesgLe95Q5aU0Xc2UMPipZVrNNb6BnCVhDPLgkQFU2u8x-wtcuBGsrDh7GJV3JDq9d_KZQgiW23BZj2yqJpHN5b8bFz8hPt9KN1coKG7j-5AFGVYNcqw_R5f1KIRKQt8Z1NugmVQwqQdAiu87Sriv23piWqFeJYS1EGyIRhdNK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8-PfneChIZBFTh5-l9h8slnnmv6adoawn_POJdu5IPlSqDjGbE7C48rFpN0Cqa0q3FiBiebWp8rmyZqO8JiYQhIDUG1FqpA04ZTw0YomBdXB7o1gHC4i7lHFoy9wwZQRUnAagnen8QIZl4dEYmt0rqosnu8nc_Kw1cmadZrvSGsSL9IvzwkgXF5iabmd_vEsVE6y6KGy6IlB4y7kcMco0R2gVs_xL3wu5EB4isBLYLI4hwj0r775cDEH0EZy-lyFFWWmdweVh-NEIhK8FymOHx-vCznqVIuCMCkfM2-9T9jvz-lU2JUAFwFZH4JvgA_DkGpE5o6YAlwm9hRWYIKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOR6964e1eKIzpayywT6Fh2cqFMazDBbuDBjooqz74_f45PpaKIfsVXHcLgLrblGQUeRyb4373zxMXcBZclxWmAPzmDyLtY3pjXrjVMgow8OOH7IgdJVjdrNFEKN40eIsbLy7sAOzB_1oRk3SRfp_17b1j7lIcf6B4pEIuSlbWqdDhVtGpWCcGFiUA4aU7fSYx44dJ31EDge-8OBjcCdiC9ntOMbh2wHUbKFdDPUxLGHuKCEIt6va2M6UNlM_R9VnUG-8sVF6Skw4pNhk5k9txx6Jafmy8a9uplZR9z7YlWl8aZhGaRAUyDkxKWUY9QMtPkNAZXxN5zeARL5WqKpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQnKzXwnEGcHPF9M66noPIUrO8IqKkg8aqM0HWNHWJr7shc04T-9AJTCB4mj1ExQXZETqmhtIrNDqP2gqV3UshlYr3uoCFq-YnNMnGvppbqAM66_ml0czQovBGfGU3VSvO65KORUc27jqYyBIqyeHodhh5ZCPTTUOp9BMArt3yfU6wuVYC9pcIV-n-_HmHb1k1wv36JaRZ5P1fXKZDGFkUXY6skGYrX9_Xxhh_T_CsNt1wEbJC3HhYnFFWCeYtURRijVBPnl8ZkZwEAOpeTz4JW82cAAts-rWhN9fSkgBG2ve1LV8QQCe7bPV3OZdllQnBNN3gnzoIUg92SSJTiZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=E0rLZ0dOYLgGCcY5x_K5mAxxr2wuEW2mHNvc11EcxP6LCZMChaPOb0zDGxiDEp0LUr1VhLcmfyChzs53vONgNidO6b3lkaxiJCBZkpDMIaZl50e4cmC_jAYq6L3qyw3_P89Ki6b2jFisc3lw7jcP0rzST6d-xBGubKILyIpyIKsDm3l9WQNGfNRGSy422V-10IuUlVL8HHJTIK7RD45_0m5cX0Ic-Y7F5cQeUcsdRAhMJZY_V0OgoNCGGSqYg2bmSJLEGP3YVY4Xabk47kpRLhBzeZyOe4N8TfSVpbXKLSmNUm99f2QrFk2oC15SIy_Hhyf6QqArqAgoIe198-0KIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=E0rLZ0dOYLgGCcY5x_K5mAxxr2wuEW2mHNvc11EcxP6LCZMChaPOb0zDGxiDEp0LUr1VhLcmfyChzs53vONgNidO6b3lkaxiJCBZkpDMIaZl50e4cmC_jAYq6L3qyw3_P89Ki6b2jFisc3lw7jcP0rzST6d-xBGubKILyIpyIKsDm3l9WQNGfNRGSy422V-10IuUlVL8HHJTIK7RD45_0m5cX0Ic-Y7F5cQeUcsdRAhMJZY_V0OgoNCGGSqYg2bmSJLEGP3YVY4Xabk47kpRLhBzeZyOe4N8TfSVpbXKLSmNUm99f2QrFk2oC15SIy_Hhyf6QqArqAgoIe198-0KIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwFsuKhaxEk6zbeRSFqHOOKVEVSc9ardeTgaGCOV2iSEoqyknYvVJXzzDL57QEvbeN5uke2c8Qjwl-uzLRYqFqeKyAE3e9GQOvrJT-kt1c1l9p9i8pDPOkUFRAasBQYvDYW-UvdLV7YW1OTiaQvr1BqMGSHJgkhPHkHpktsL0azu0AALac9T7s59XXvmGiA0CG9bRUmvy3AKWlBPnN5qi3s_NhgeEmGymTN3hwcmX2O9z9nM_tiTK_WNvtWkwCE-PrsqZweisrX_aHY5ZdMU6ir9jjR0Iz3NltHdJT_JPmNjwRWLuRvLALTRnGF00E2_ChnQDrss0ZdzDxJMoe-PGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M42OXph_zbgv33m7SL0D9-hnf7Sr8qXT20bmk8PY3eqSEz-kK0ecL82YEYzv-knOfZgRkCnxZoh55aorQMISMLC3ttZhBeSPOJmpxjszfZTWQE5bR5ebxkV8rashd8flnEgVxE_4q4XLVXzPwSVvUONtn9qyxzHp090EHS_S9_o-rJCddqoN4G-t9DHZyYJbtOcaZz-9eM8qSrHy0BrJy9oXFIrvE9jqeoHGrWM9JkmPq-JnAOtoIFH3McA2XuN1R2Aq5r7YjPdgJDKTyzdfm2SpCKt-eNglguwEHA73TsrF5G75oou63x-spoJuwyQTTkfHHJagn5z2VD5ztho2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=PVDXWrQC0q0OAEuAh52TpbRcTVTOcodViwACQF-frSnc_LGqtB-8zWTCDUoO9yJl6d5YOe9md2zWu6_MFywFKtCntZoQTLgpB63BivEeGzZln0dYLsb55EJx7yH1MT6lbSLjglbZya4P5p-A0g_1KOpCWkPnNAeL8s8_Q1zCd2PUeoOymC8tXTI5HE5gnLwECCIe0hVnBx1HBJIt98kCKshixOl22nsVD3rnMj9Hovt3ydSajzW3EXoHHRC91wZzdvRHPmOa7y-bfnIph04F5ord3QVZdepa0W94cUEdLyqQ2OMpFWniTkYaFJV5POlICuxIjFGGEmZnpon-D78UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=PVDXWrQC0q0OAEuAh52TpbRcTVTOcodViwACQF-frSnc_LGqtB-8zWTCDUoO9yJl6d5YOe9md2zWu6_MFywFKtCntZoQTLgpB63BivEeGzZln0dYLsb55EJx7yH1MT6lbSLjglbZya4P5p-A0g_1KOpCWkPnNAeL8s8_Q1zCd2PUeoOymC8tXTI5HE5gnLwECCIe0hVnBx1HBJIt98kCKshixOl22nsVD3rnMj9Hovt3ydSajzW3EXoHHRC91wZzdvRHPmOa7y-bfnIph04F5ord3QVZdepa0W94cUEdLyqQ2OMpFWniTkYaFJV5POlICuxIjFGGEmZnpon-D78UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0oP5RDKgpaywR84CetDBPU7mnT8R9eLQwpp3i_ixLxGCddnAIfFYzoEpcCKsXMnxiPk-jFo_RjcfvryIVM9Nc6ths7Lq_G9dX2LMhv7QMesyqQ7nPqqHD9UWHuH2naU4lj5cfEcFgUgQ4S0cVtaEjBwNR2lShXaHAoQYh-bBfmeIQBhwvITiVbR-A_KoX7oH4xY-Q7q5fL75nmDOwfJFvOmjXHVw5O7oe6O09c6kKQstosguA6IbE06pQNMXNTcai7FFr8j5WnaHmZRmwg43LU_xyul_pI7ePF4deWByW_F6J63pQ67pKG6by968o5fdsDJ01fMlCaAev9m37-dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcHtBWIxjgD-RqvCbriACRCY-qQBH6Q4E7mgoTHQBEl-QpZwXED8-kkUHP3dpxo8ZwYhApgqQODWww7Kty4OntHqZwUllYlYHZyAzqTgoTxXL25hE7HSF4vj6EM7U3vVQngvoe1Ae_ulguc_Gde05VL8-Vt8ZZZ1YDDNbGq-eVaRCIPvOi2aowf-IbLPRqw2xdZ6wjCoKQxQpKUZ7xOD0Z1yYjt_1p-YdHqql3nG-cRRUJ0BkgxJaO4dSc1SmmousDblRptjvj8iAJ16bkheUeeV8Yu-RblxzaEDixVMi93-L3FHTf-TRUzhUoWR91uAYStn0dHUvM-bMvV8FMRhYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iAbRkCcWoB3TAfqEDNVY2i2dH5pO08xg5eWLLHNZUIwqUSz6DdlseNqaoL8QjS4EGS9RWUtGUVkiKX7nER5Lqf92TTZ091S6chKKAvID2ckr67VM6hKzTGh02BF5kd9bAXZTOfREnf8ZqsX2iOm-DJTE4o5oZ9_U_qd3uBEZnktKI2h6mgJ4uKu4WWEoqdVCRKNPhj4F7U0rNFqQGU_lU_seLwxRsaKJq-sbE3w8xm6uTPBdimiVh16Wof6qSsFAXxfp63AcT4lgJm42dUzd6YMdvxZrNQ1RmBmGJMZ7lA9-68kCt3xqerCT7lbJfH0SvsGw1Hq3sLROf5GR8CccSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iAbRkCcWoB3TAfqEDNVY2i2dH5pO08xg5eWLLHNZUIwqUSz6DdlseNqaoL8QjS4EGS9RWUtGUVkiKX7nER5Lqf92TTZ091S6chKKAvID2ckr67VM6hKzTGh02BF5kd9bAXZTOfREnf8ZqsX2iOm-DJTE4o5oZ9_U_qd3uBEZnktKI2h6mgJ4uKu4WWEoqdVCRKNPhj4F7U0rNFqQGU_lU_seLwxRsaKJq-sbE3w8xm6uTPBdimiVh16Wof6qSsFAXxfp63AcT4lgJm42dUzd6YMdvxZrNQ1RmBmGJMZ7lA9-68kCt3xqerCT7lbJfH0SvsGw1Hq3sLROf5GR8CccSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcBHiUAOuf3ot0Vyw0w8HP6syoc03BmdmErnE3OY2-SnMdWfPQfVHl3VuU6W_7nB5QzEhfujfWbwKwhgb0FcFmUalRGoTNJFRQA3ra7DOTPRv5EizdXypGvBUuwsoYg7fN18-VITlPWsClCCxk1AQqV_WZAvsYV0xhblCmDV33QPffZ-IRpXDnAZtENewH3jOz69uH2jgJa3UL7PUmJDa_HYsUytAeQDxsZmt3kwmfI_JBrTbZfpsyTh5JSoU3DYhmuwjo1raoKq5wSSJTYfo7r0d72mTye23XqLCuGC7rp8MnOK5UPyJzWfvo9UNjNBRXQAgsjD5QQAJHD-j5_hJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4Ek4Dp7hcn9DLqUyFYhiW1VdCiRrABLhpYHVwe006OkP78-7_8y5QSXCo74-rmonz3C4THFbzG1sLOGxu2L1Jrk1gRhAvdG5fzFTvui6BxzbeyZFYFbhjk6Iq080kTiiy4gjtTAu7PQCpeLdwvmWVoGmFvT3UY3JqtsCNi1a8QZOoV23wb8Qa-zoRMer7d0RMPGmhEKX7kK1mKtHdpN95u4jizvwzJ9kr1UES-ZQzkk4CO0ZTjoFteO1TsIrzQr9uOKpkN80Y7KZd21DhPqyVNZZl-3FHDebsaHIyzY6rW3UI_birKttnC1qkbCLt8LA0hMhMGqnrnvabmVajXTvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=fbSk20nnZ0bRSMLBl_ewuHEHU9UxiUApAIVQ9ewROJGobsXc11ZVZUR7uHb3QInIqtsbcG1CX7qKHsr2xJV0TZ79JmPhVubEy6URfQoZHYCtWNK1kVtC-czoD4UXu0Jd9yGpyb1hSGhDqpC7_Ww9VJk7k5h3YIczXDfHBdWMpQ6YUjItmR7nvw0-Yp69Mpd_3q1qUL_HS9UpevEUnujIuxJcFtGXMiQRtArVLVa8OJ5xKuTGX2sMGAJtkChpEU4JglVHwZOcT4OESY4KWPpPFFAFwbu50ZuY3eeZyFwOIJ19lRrQpVmxecFt4gY57nDITpSShmAZvm9L03h1JveauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=fbSk20nnZ0bRSMLBl_ewuHEHU9UxiUApAIVQ9ewROJGobsXc11ZVZUR7uHb3QInIqtsbcG1CX7qKHsr2xJV0TZ79JmPhVubEy6URfQoZHYCtWNK1kVtC-czoD4UXu0Jd9yGpyb1hSGhDqpC7_Ww9VJk7k5h3YIczXDfHBdWMpQ6YUjItmR7nvw0-Yp69Mpd_3q1qUL_HS9UpevEUnujIuxJcFtGXMiQRtArVLVa8OJ5xKuTGX2sMGAJtkChpEU4JglVHwZOcT4OESY4KWPpPFFAFwbu50ZuY3eeZyFwOIJ19lRrQpVmxecFt4gY57nDITpSShmAZvm9L03h1JveauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK75txNJpZeZ1-bXTZNObM4dbhuDvawg6R-csdqk48PuJa_zG6sBYLAkKmWKwQKBPzXfuglcMjiXLQHuk0jUwps8d3aUMfqJEhOVoA0KdVXbTF5gjiAAme8tucSpIge8YKuxkYD4GsxPAOn6h1MemTFQ-UC4zrH0ojeTctrM7vZMqmtqvKIZF1lvWbbIXiEupEKYKdAfGJCqkQ1Dt3D8LhhfMr4HCbVFf0_UJnZjtOfMM8j2pAffi6JqYeIr8tvrAhDEXpvdtlaqyB_dx3amqxP6Nm6_Iu6Vp4cih5iYV9W7XiigAPjtiExg7yBzsirspFKcvEhjwRY3p9WkxfkuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOBNFOIc3fqxrsabdB4fJm6m35esMd_rlNglhUr7oQRmKakE-hjL8MxIT3reu3lvFk1ROe8dNY5q_mEDUAom0cIJFx998aZm_FPmUTPRN4f16dQauC7f_phDv4GMgc7E8yzhdAWUW3nZ18W7ngZkjefMTIPCtGWbos4qHWYM3pGuAed2RvnrIwTH3cznNGgQ8yHp7wJrt69lugt89-OhWSdkwKNABvbIigFN6TDoagki4VDbbU4cv2kD7lec7o26w3q3o1_plX_hlEjWRQylltmGFj3JgsO8R-mQSLVe7czGcVRBLdmyMCrYzbkPfibe1mMQU0-Yfm0aFcSXJ1O4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZCw-bD6FZkC7jXXO-rFY7y5IxKNqPmC4Xg0uax-KCP9w03ectKnehUPn2zqX_YgtGhuYGtCynAZARg0s0_1r1nFWgmZuD1NdKptdcQsGZCdc2ooWDCIVVXnnvp8BMWf1QSWbM-DtLn6pF_FoNGuUI09yc2jfDKQsviJScYzDo8kQMPQUd03OaHSm9KEMomDhUMFdbrKRW9169PPivc4qe7Uij-Pg8JM0MQ6toED0kmXM5wedelZx3Kpw8yGgr-XKioT9pIjwYv2jhTDzU1qJNGkFwoWVf8AeSF3yvsDCa2pYt-Z1EM2GpNfvGlUEUg5QIQP4TVnifj7GSbe7ubz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAV7tIFYaP-msErmgj1ttXPJU098VIZUFQ7GH50jcD5Vop8i_gSIdSaC6d2np8EwrIeCQSruEg1WuGG7uSt_bl81XIEDJsygteeRqNVSI4DMg-uUynd73XyhNQgNmddlanP3g6Os1T4uYecOTrfXXUsYan_Y5RMAMcgoOp6OJqqlzPgHqDrHqL96HEqHAdUSaD9wn7sLn8HWZvLPWKA0tQncGf1iV-z_2_840-iUSEVJLSNFHEcg5VzKWNFzxs-RYGaIU3o_3kE2J_-_VieUwDKblInopwMOxAHfO6BZxoDkVVAxGUU1qyTBwcGGP0W8UZpwZ3LsQz9Dy7AgTVlLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8VoWs83jGV23qUvC-irSEyJWuZYCZncmxNN_47o75rYe9OVQYOxtgXkPfO7AiCFeuHv9XXd2ShCMI01r6vaKmFIhdoI9sZNJaTQJbKUA9xvUfM_yY3qDz140qnzOPzAasEWDHK_-WTOt0IQCqQrEGNRjK3Frwd0soRkmtXSQ5eXZbRJG0Iu0DPBVfnYrq1EoZuPhemy34aBL_1UqnSvNpnvM8zTn9-2rRf5QTLjymXXUQzJyEoWuBZOYsN3LXnaL7L9XTHr9_gyk13SDQFGNELQasBFfLKhJ3iTYZ6aYW2p6cs-TbMpfkRp8KDYd0j5unrz0QD6QG1Kh2Sm2wQOWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDF9JABmUg4Wf_Y4zu77IXupDfVqWw9yBXvDVDSwohc86Wh2pDu3emlKNK8WSqPjkmWNf2ATysydP3hNKdlhyKV5pzjyaWgDAbiQ9FOYzh54fs_aiQFwOvXmjSugau8YEwh7QCV8AcKKbyvIDyEQ-p2G-MeDG2Vqm-MxE-adgNoxxu_FkU-RNNvxOCivJBQixS129rWs85vrYwlZBJjF5kxRDNlmc2xTJ89Oruf1HpEHQcEa3wZZ9utntool1r6RkEvPWovhH4xvMjFgkSWmj005nl6heJrbMTfovMaGEhmGihTIDipobulNRAYPT5yzlcAqQaD9Uv91DsjWYaG2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiCQB6Y7zxoSJ7L6VZ7op9ntF2moWwdxvdB6reoxNxeDgB33db8yez8XXFMSo45FnxeewUfWxauFsBtVl3BgFoKRHxiqYHocxnw4glgUzb4C4NeZAMHNicTv-aw7tnfVT0x6qXU8DzcU6InmAMs-CEHhV52JgnDEbLKwKdIqOc6UE4Tvk2C6nx4XnL6lazxXMG4krZAtAi7dCRR3kuy-T_pg_Q5K8Z0P3eIDjMvqdWcK46KxHoFv5QA8B4qX0v6l22Q9wGImunEiEOrkqK8clLgyGKuhg-ylQpjaAZUNHKsgN0pPTkY1tWZMb8uXL1-rMKw7Srjc7rHkCTGdTW4INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlVCRoLJn8wQyyEKh_DKGCqXhmeVi6miEfZq6QSEAeJTvtREDqJLEki5jJkQtD9fKADr-1qjb52-1O9UMQuX_I3WRc5hAUKbXQk6MGOME1PS8vxnS6PAdBWXJDPOzNbCI1_byg7KdvY8S2TgAsh1HqitqHVmWB6e1Zg8tP11JfuS6Wn5SoCP1SV_caN98BcC0lBCpOTQb_RR_SSXqzubLvf4iUBtqDKzj8HYYAj0zVLylVahkhx04SpETBWU28sV6QwjhUq4Q5Pe9khz-uiuYXT7jVs4uBu5RMKQDEB9OElKYOz38Un_l05qj36AK5JbuZejHPS1nPOAyCra0ZizdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=nG48PrbN4CJBnIkn65I0gxkslWfuj5IAMfNREbbkLprOkLw1qhahdaUQmYlZYNg7pb1HNOYErWTJyBG2iTw5JNFivtIQKgA1Vh8s9E80hEMhgpS4wNV0c-u9eu1zTkJXikrMN4Y93XL2-X37ncC1TI_J5XTqInNiVOu0I3zXdf3DWnHWjs5zWwlwUi7mtmqiTx0vu56DyrAog6QEjE2CLvCF1YM_2S8YUhI-ayrmMOTa4iPtxVY3EjbGx0mJax8lPsttoSF6ZWzFw3P4DWPCi7LSDIhc1GWRQdwxNMTBwA0ECwYDX80gS9zR59xU0ylfKfrDMxr_zNugrlSeV7HQOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=nG48PrbN4CJBnIkn65I0gxkslWfuj5IAMfNREbbkLprOkLw1qhahdaUQmYlZYNg7pb1HNOYErWTJyBG2iTw5JNFivtIQKgA1Vh8s9E80hEMhgpS4wNV0c-u9eu1zTkJXikrMN4Y93XL2-X37ncC1TI_J5XTqInNiVOu0I3zXdf3DWnHWjs5zWwlwUi7mtmqiTx0vu56DyrAog6QEjE2CLvCF1YM_2S8YUhI-ayrmMOTa4iPtxVY3EjbGx0mJax8lPsttoSF6ZWzFw3P4DWPCi7LSDIhc1GWRQdwxNMTBwA0ECwYDX80gS9zR59xU0ylfKfrDMxr_zNugrlSeV7HQOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDbOJ31h7a5S8IVZ5FaDgiqO49-iWkW7DNbvqeSaiZBSpApHg05UBDy3b0jojLpJSS_JVrCO6m8rpI4CSVUDL8Hf6mUTqiYMAC-mpOfsgvtHSGZB_gHJ7DQg5YziGyCVwhzanh2Y1mg9N-16IFsfd_EZCxlU1G24RmjNOqz5_zEjqLsZQmURdX_HR3kmkpG6BkmJ0DtZUyilTo8N03obLWMHcvNTtb4CsIcBe_uSeIdlup7lr-u67WsnDJerE2uqUu5MtPp4II8nM4s0fs0wt4YxPUkaOOqGuW8Hnp3YKymgQmq0zIWG-oX-uC7l2Ssbbqvyb3Bj5wvM6avZxisHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=tzYzOhVhUqXxwS7ag173nmAsS3f9b2G6VPM5GG4zRwp5dV60hfGsTnTvyp2HR38-sloY1ZloFJ63s3g0WRuL9s5_265OuboQjXotiJGSrSxlMyoN07rH6Wvek4tkuEdZAS57OSRnMciIr3gLmMUiPud2Q5nzUBvkJaaIKEAvI_6ThoPiQA4wsExII8fEdwSuUk6ID0esOeeVJ2mZ9HRHsJcAuiem8ae4-zDSkEPc2Qvp82IcL2l6s1y6xcSLxa49LE7NKdNS2oUuSL9A2nrfiNMSYUeNy2XXsrFv3mr9o2jJBXREW3gkTS32q2yoII_yO1VDkxnadRuBMA_qrRvUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=tzYzOhVhUqXxwS7ag173nmAsS3f9b2G6VPM5GG4zRwp5dV60hfGsTnTvyp2HR38-sloY1ZloFJ63s3g0WRuL9s5_265OuboQjXotiJGSrSxlMyoN07rH6Wvek4tkuEdZAS57OSRnMciIr3gLmMUiPud2Q5nzUBvkJaaIKEAvI_6ThoPiQA4wsExII8fEdwSuUk6ID0esOeeVJ2mZ9HRHsJcAuiem8ae4-zDSkEPc2Qvp82IcL2l6s1y6xcSLxa49LE7NKdNS2oUuSL9A2nrfiNMSYUeNy2XXsrFv3mr9o2jJBXREW3gkTS32q2yoII_yO1VDkxnadRuBMA_qrRvUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
