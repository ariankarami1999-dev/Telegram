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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 02:23:42</div>
<hr>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhz-5BnrPY5To2QcI4rTr42HJWyZdnFzkMR6L8tIk-ZlEFfvgp4MwjovRhsSqF4faseXwea5MvzjtXV2v3pcmpfw66Uax1JHoudZuSSJnwfyl_e68rXtZfK5F-ANyWoPPOOQoRF0tQK9MSkLThlVNDQYO0dLpNgk4TYyhjbZMmqdYv1WO09uJ16u5GwFm9zZFqEZPqNx_NuulItjKlVn-HD5x4oo1MqCNeuQItMCDVc17kcwmhQntQhHKUe1oZYOtkrs4T_KNtgDA27_9qab2c-L_xD3pm3GqL4xIGjRJrKLcZuBEtTTuJ9rkSPaMY_p3-Ws9OqfrscvfuDk9bG3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=XV7r8qNCBmYeidozXAHEnHJ4hr-9HoobO5ZsUyqP2yvMpaGLBCUpr9kjS_79HGVkqu50O_AuCo2O3YFLfjqel3-DQ0YIe7O8VVxfBro3zJFPTwHQ16pvkLJalaoSjdBgzz7Z6AzVXgzrtMud9ZZORWBAI3U70ZvJ-BrE3mqA-fe0MTs-0L3rANnjxtf484ZNBoUoZ1GIGIgr64t6d6SfxlC6nhySXNm6r3_7L2al1zrXKUP00HsVY07kwdCg64b_IH-oRBrQLaQJerAaonhzSUc_AkaFnPA6vzUvpX2BvJZbJAfRobBUr4AnOju4ZaUbCWdpsY5_axiL_Lt41Q_cUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=XV7r8qNCBmYeidozXAHEnHJ4hr-9HoobO5ZsUyqP2yvMpaGLBCUpr9kjS_79HGVkqu50O_AuCo2O3YFLfjqel3-DQ0YIe7O8VVxfBro3zJFPTwHQ16pvkLJalaoSjdBgzz7Z6AzVXgzrtMud9ZZORWBAI3U70ZvJ-BrE3mqA-fe0MTs-0L3rANnjxtf484ZNBoUoZ1GIGIgr64t6d6SfxlC6nhySXNm6r3_7L2al1zrXKUP00HsVY07kwdCg64b_IH-oRBrQLaQJerAaonhzSUc_AkaFnPA6vzUvpX2BvJZbJAfRobBUr4AnOju4ZaUbCWdpsY5_axiL_Lt41Q_cUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvvQfVZsV0WNMI1ku1VTntZsSe5KRrScVqpMCMsq2pV1j5Qlm2LNHYsoNGoeCPQCtoH-Ee3q-R4w8OWjmLLGONU-D1LCrk4NB2qlecJH7d9bDfBclXxQTithjezAGW71FG9aqssk3x_7KnyUXX6Otosmlhf-l73ZB6Wmo7bgOPQ3BneiQCuejkk2f2LSzQye77nsyc19V7_AGGih1FIfJqypFrGdn1hIAGiHzJ1M1037fq0nqQvhA5Z4nuj0fXzvdQFuYvWW6U3b_27LXAGyySoQ9gMZqKRWLbjf4nrc-rLy5fG3iMaKDlPAQeb1gaQWOQrHegq-KfuWBmZdE8QUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=tAvSu56HR_0a8Pn0pEbRWAs01Gejp8Vq7Nh_QQXcTXEjnHN8gwplItSdXBp4cN3XDH5uyQfoggJhKAwlZWJ-6r8oD_9qI823Q_y69SD9RszO8JcloED2XwsTdr-ZKLJVnP0gnem5yRvrZiJvTyj84IJ5KjJIg4oRAkjY1sM7yAAbXxS7RODjBK0k2c7YXl2nlK_toZRSpz-h3KuGgP0Z-NiEVVk_5EVjigpnwmhC1MY13cOVb4cDziu-TBrzjdQ0np00kGjvj9SyPCReUxnmjI-4xPdtUzW_HRw1fkDladuYZ5Tmh2ZUuw1_DT5O7z2Ub6eXfr2JwsD4LvBRdqeo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=tAvSu56HR_0a8Pn0pEbRWAs01Gejp8Vq7Nh_QQXcTXEjnHN8gwplItSdXBp4cN3XDH5uyQfoggJhKAwlZWJ-6r8oD_9qI823Q_y69SD9RszO8JcloED2XwsTdr-ZKLJVnP0gnem5yRvrZiJvTyj84IJ5KjJIg4oRAkjY1sM7yAAbXxS7RODjBK0k2c7YXl2nlK_toZRSpz-h3KuGgP0Z-NiEVVk_5EVjigpnwmhC1MY13cOVb4cDziu-TBrzjdQ0np00kGjvj9SyPCReUxnmjI-4xPdtUzW_HRw1fkDladuYZ5Tmh2ZUuw1_DT5O7z2Ub6eXfr2JwsD4LvBRdqeo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9N0IInBxHchava30mC8FOVBii_tlYjG8SpyCnd3_Lrhb8Lcw4yW1TrRUGhTjmpTCz3OORTK4tT-Bh9jtCbYux6H7MvuvXIonGoHk09EVWmPe4wo1uDQ76E7RrlfcEaI1gSkXm8yXG9BcFmuqzgb0WwEu1ZNqgUh8KAlFRNwuyaF9gczVJ_sPHUn6a59v9f-hWIRhUrO-JLAc4M2IKklOrETvjjNqDF3iZG3BRX4N2jJymEPhXoSb46XHtipbT2tQ-RZodXoexytmY1IlpV3dQrV41Y4AbDX5fe5oE1Xcy0ENW_QSIWPw8IP8UBydNmVwxdVT3Y7Xmz3XJOxVKqNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTGmoGYhcPl0eSnIR0EtKTjf02ngcd0FqWomLKSg6ww5Srb9zjImNymO_qFYmnA8h5wQHQhvlbCMwUIQbHT8_SQl2riJGHhen_vb9zZEM1-skcV-Sugs5Zba7sicXSzCBf4ZuZfHoL9wbA-vG9QLEZUvL5PcHRSQ_sc3iLAMyLPB966CY4wt06NMczT_D1WvdZnR7AUqZK-loU4ly2_jFeUylqiAu8ocCsxlhWapQZKK6CtSQehk0KfTtOqaHRcl1O0h8-pWGcCM39tHjkFpXaIk-rbWlLNaZtCMLRPNl2al9eS8pqEf27s5tTS4HxXgHKq2BvzZtHX_Pw5rHGngrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBch9mhCar0MzRecFRwpImUY21K53IpIzRpEBktH9jJsx_K15G3YU_jIgnWacn3MOX8VtvpSqOfzNaCDslxzqfp7tcWfdbvLChf-0sHJCuCsK27XFyCcigGJBrQkyq4HzZGcoAGw3n7re0XdbKqFIaxy7vEek1802FLxhsda1ftREdLSARtxPyxPBNOfIxGpo3bL5otRBQIxP9975q1uIdLw0kAQERhtitCnBtu68OrAc2EVwEXSaVL3d9kK3l8ZBopTpNhFbQ2XRY1z1OjxyfrXSVyjgQrhAjDBzJTNdOhWsOSw_WnRDT6yQANmrvt4bZEIStSQXdj7eyJwlkEtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev-6eumqEw01PUKV4yAHCPtvsGZnZHrS8zayGXakiNuDoGptxTLpbeUpdSJ3ES1vmWKIyt9dQ4xuTI8L5TCu-BZMoMp9MqrQS4ZCPfVxvZans-ZqUryU9_a3hjY81phpk7Hm3HI3vkFGu3oBCyh1Msi2dcuWgWa-5rG0zWhonMxojpKEyvXMGhMXpo6P1AygqkI0XzSlPvfhVYghUh7OEXoUp-tms4WiKzUdix61GyVfcfuCeo56nWpZJyl1ztdEmUQT6pg7pOZzMRbJtiwvEnvxyJqP-a9FcCGF5LsOKD5bd-h_vfETdn-_XIe0Jbw0zR93Da50m0sqAkkPWYoQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLC1X9k6oxA8TQ5RcHZHpxyCCZAHAvs4BzRHrtaqnNO1HPqbGGwyz5jOZgKt1ILLYMnrHBHwc_wbSyMUsk0hNu6N4rJyy0joVfd_Ite-F9DKTpgsBfo1Fp4oKqrz6qkIbwMfci-JCuikA8qIM_A-b9d0_l6LW4NVEOmuBAfyDrxuYy_Nc34rxOMr-1u0q-sQ7XFPHKUrKCksXO9MZ9CsXOUcyWIrF4n4ISrc5_rWcqoyYzdUhAOHgf3tLjpIQe8SkQL3X4toMV0RiuSNjf7rcjuroz5sbWqWaNIjV4kPlOjJXGioZiUUaaMv82WAVtpAcr9kMy4L_epWVKFdBIXJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpB2x5x-90aPjM3DPPhMj_Fq0_xu2gxKQC52t6fGHcyrxJx88j6g9lGJVv3wemVqpAKMNo2cCXSQHrrazNw0sCpZrtDX7xA0udaSQAIg8nb1EffH0JsJYj1TocqyTUaD2IJOcxHqi8gn1xD6fyNL3zpkaX3QvJre8Lq2SxrumwwWuk5qg_cHHlbzgxvA-FUNnjpD2bV6XcUgTYqcSkU5UfGqgu9fHrUA4wSvnZEUte8CJQRiB2ul_J2-fP4Cc6hIU0PAFgJyynsWomVUjIxUyKlRS0WhjZhK1Dovv2V-sgFU28GikpycUPND2oHRsvfBw-BtRa1NFNarfBvNELvhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PX7ezgKCzw8czYDU21kZojr3CRzO0DrSvRkTdlGcSjrq-GOgMXux3uULqLCpYKZYUv5rIhraGFJD0PoZqLZBXViBmNN2H6AwyHJRso24Ec7ZSCsHQbEfff9mAjUPgoWXmQe6cOzlZZVG7Z1Rz_wazzKqwV_Q2QAs1h02qy-3JhYs187qVqpgyAZxrZUfjnuG8fWJTZNXvl3EVNBSNEGsxW_ldQLRhM1vX_8aJWhYOXs0XR0T-HOH2cGi5r1TXlUEpeuTOIOpriotCF4Em6RGjeAbaWDkvZ46ZoFUiW8qlyMgLMilDkPcblz7ZDbtHsU1DSK9HZT6yEb7G7MxSB-zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PX7ezgKCzw8czYDU21kZojr3CRzO0DrSvRkTdlGcSjrq-GOgMXux3uULqLCpYKZYUv5rIhraGFJD0PoZqLZBXViBmNN2H6AwyHJRso24Ec7ZSCsHQbEfff9mAjUPgoWXmQe6cOzlZZVG7Z1Rz_wazzKqwV_Q2QAs1h02qy-3JhYs187qVqpgyAZxrZUfjnuG8fWJTZNXvl3EVNBSNEGsxW_ldQLRhM1vX_8aJWhYOXs0XR0T-HOH2cGi5r1TXlUEpeuTOIOpriotCF4Em6RGjeAbaWDkvZ46ZoFUiW8qlyMgLMilDkPcblz7ZDbtHsU1DSK9HZT6yEb7G7MxSB-zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra7W429i4Gq-9uPncrOLtLntnxhJiFvj7ZTzPsAB5HdTd7-SyAGnB8RS0ASjZIs8slRgPSMmsgXalyIE4Zz0F_eg6RXoO24IHW7DOuwkY-v6gaNOBD-fgxyZ9BOrzBc2RoMQbJB2t1lxdRlgB1PFYJuNYnZAFN56aLnmSt_9MeFof6qH-ttOW9nAF7Mpx6DN6frTC8nliwcTKfqalY2dn8YcRSTG41M3oQOWbmsY0kDbZ4vgynzDMR7LZYfJmuoY3xeUcRqKWxvTPmcjXul4OFOhRrp8kYJ5CTYESUbrZkRaPIXmnzq-vuyQW9OmlewPApignPkGxfDTj8UX4cHytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9CU2JQFDd9iDtqXdgRQftFNa6UQRco1rMCPR_3-jrAWtOumkuKK55RuZQBNWsctD_CHOq-ZjtZNEd_r0HBBAlGDxaF8UQmpU5UyOJsZDAuygt79cm8H0PtwieI8P00huk0DfDqKrZcXgXgPIckrUYwHbNFwnPykGloYjUR5YcDTHNQaEVqgpe9N9Q7O-w1AqjVswdB9x6nxjW__GS-eZq8xgUDafrgUcWzBK-LAOOzXLU2kOJ465QYJemG_pVt8d_Wu8T6ebJu03U7lJohtLGF3gBgAJlLnEMdAUcMVfLLyjHQ1N47X_vzrCC2BtDJi5O7SzlEGCWESFzgf_RaDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iem9RPdmLzgze5lFyLfJe0cgu5PmCFR2hKNuBNkMZsMZYmwK4E9KtVeGPSaPMDux1HKtZd-0gQW4uhATkIwMZwu53nBQe2-FaErJpFI47WIDZvizB9MLX_m5lQ-RZKljsl51EYIqON0t96lTK7w2OPFmdKtMSiuZgpMwkWCaeyha5j0Xy8M8UDi76Jf2dudHWf_deZU7rb5_qTZjIm1AF-GLdGCC19ERaCnAHGPAzZc1kqfxekLv-9aMkFrV_j-GRHUM5-qOHOduYTENbnGOHBdaWEEMJ-oP2gL5peyUiw6bBC-PpVI3498yevt4tiSxlMAd1ZeLG1xjM3Glq8Bxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6-GUUSc_tJWhP_hM_EhQM14c3cHneuVwk8GhDgry2J7EATfwK61G5dlW_lumfOXTraJ-idbpThEAhpDOEcJCP0JUvH47F7iJVUokDKtLQ8V6rB6OjbwVPW_si_COnFF_lR3Y9c6x0esw2DbGiNnY9CFoQLTWRvWAc2u77ztGn19NynLERbgxhhy08Rb_angWyzNEv-bDTMjQxZ6mrQS9NhO5YS59Tmvr_1OlaP7MZBF93iLXtmYeEvixJusL3qQsgOKxG8b8qIrhFUxEMyrxgEF3zJqRx3MZFNjKeo6LYJaNtfkz1Up71NELh-YwycHuiR559DdbufBLlD7k5JSHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=vCwR2YErik9kODzPnRxbB_4W7qZqYFpM6dhIgYQ3ZFGmVG2AWZXjwpFV3Dz0bPvM_tgqksSSr5vVelzuR1zJCsDbTQiIA5BM8L6178W-pocyO9v695VmPXv82_RpE10o4fy494-T_YbeSSAVLdiS2AQm6-o-ILGN5weMepVp-MA30_n_EQf8kUmL5-G-9l7FVHuIZq_-F4_hAq2RJ6HgWuCaH5CC2MCeVrBJNj5Qg17CrYHTKn-uJlKIFu7XkjkO0rUz5cOWzVbzm6Wiy2QYNSgODWS_M13j4Ly-8GZBWHlwaSjwghVK3NM6qvTRKrplUY2RIqe70itLxxChXXQUdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=vCwR2YErik9kODzPnRxbB_4W7qZqYFpM6dhIgYQ3ZFGmVG2AWZXjwpFV3Dz0bPvM_tgqksSSr5vVelzuR1zJCsDbTQiIA5BM8L6178W-pocyO9v695VmPXv82_RpE10o4fy494-T_YbeSSAVLdiS2AQm6-o-ILGN5weMepVp-MA30_n_EQf8kUmL5-G-9l7FVHuIZq_-F4_hAq2RJ6HgWuCaH5CC2MCeVrBJNj5Qg17CrYHTKn-uJlKIFu7XkjkO0rUz5cOWzVbzm6Wiy2QYNSgODWS_M13j4Ly-8GZBWHlwaSjwghVK3NM6qvTRKrplUY2RIqe70itLxxChXXQUdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQZ2dxfEF_DZ9naloSf2Y11_r583OAclNY6kKMeCColt0JUWV9ix4ybGTXvEfd90S0DIHMMg8GZuQD7RuuHECVDmfoAPKx3riknl0q0PyYAz3ygiVhJc0bz_voCtyDiIFWcQd_y2m0FF5wzD-ObMKCS222N7jOdjCi-vGXnfc8JKXZ9c5Fj56MvKtebpVM_tsb0XM51TGGb5gxW-aFhe2IsazBWuDqP-GZ15No6_AmVVRBSrWibGueoPC6PbLespGX2jrwB7D1fFLX_MthbcmdnbRzlnSDevgFLWo8PMVmV0wHxi_esAUZTPUhNLwICGEhp03_lM4x2f9bCjh53S3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJzHfJlQGxr8e6kTVpxRk2e-JdEFSvdWNg9XSVLNLFicUL_YhjdhKEosCJy1JOtWEAPeX11pLmJEXBu8VZxikQnlN58qmhjTaDJjIPx9rXz86-SSPsz6Rhmfg9-jKQDSX_4OrIWi2wssrFegg9MaYd5XLC_Gm50miIFz2p8NBtotWdvmodDDSdmnaqG6N9TB1wN4VUXl_PQr9BRwOiPTQquCEIWD3Qavw4_FGTME-mE-l6He1tgxA0OdS3YKoS_Nj6suK6lwYqxNBGRW1LRk3OS3GX3feu5Yq5vXl5CIWu6qdZvZBSbeJIXSJ7TZuB9oW-IgwpdiPji898y0btKVSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB0RNDcDCKaFJOfMHaV5pCLUMynkY6LUCHpc40PVB06zm6nCK-QICCgqq9I4hK2qgxeWyFyiJgwK5dPmC2Bq_kk7_VfXhGYNmcGXtIRnVSC2-L4hECbaNmhj-bTUGOwwkwrGbcnc3tsuns6IYVx68FKV2Mrsxqm4gqTV1hKamfsjIHuD0w_mgOjDc68UD2_cpAVOZycWeld_N_n1ZWyYDE_qpHXIEXFSad4N8HpZgHzsDIm2Hu7nTZJmyx7i4eTp-ZWrL0HnfMvdz8yNvb81QZtyGJiJ68lvYM6JeIrcIfzrXd3CqzArjqOWuY0fd3sZ_tZBsMBkg7YJXmMxSwfpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3nxe23d5ds1fnQ7Cc8JRIB8xgXYuO6oqrg81MlKp7PlRGI_tHJzQNj6LSLrUGDTrTvGp0AzZAdvW6ersB47oKpDk7nokho5aGMke2xTw299FaqXGcY56OWpRBSTkSvzjVtpx9SNzOCTKFXxMzUF3RObkKZBgx3BYCb7euy0-zyZbTWCEf6ubzS9E5pAWL387h4fCm9BXcco9M2roLaZhfL9UQcZAVF4NvC6nnTOCMmfoF228fp9tg2CjqtjAk36TsX3w43IU52KAXIAAj42AWUr0ORrWM6fJV0J4PwmA13N_u8WiZrFKo3RKQMRGTh1WTBC9G-PuC7Mkx5usnH1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAgp2TPAOkXAp-m6ejZDflvsFV13E2ICiTxHv686wQXdQWNFYILahIgybre0zVSpGgnDG1s1L6KYWKHOrEemVN56a-PNMjHtOPWTUzRvT2norIqy_udvGxJApTnNxn5dIJngqvCIu9cUXI-57dy-IOS1J3LTkFjPxS2VTQwf5f4jQd2HrYgwda8LXbciF88O4LPfxOiPTU-aXvl5HQWAJZLvnRse7388kqj4hoRNRpj4l39KDDBvKTKjSowX8YEA7QrEqQXYrbgOWYzdMEvMGPpQ2z6UkrJjmf7nXJKRL_QaNuZ89VSEyjFX0Kdm--tbIL63cbqNnwBx9BIwAVakoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgfLPP2Rk1XWq0Zk1RNjh8dIBj1HfRMWSTXZ6CJEpEYQExHgcGzVZhNJrYMdRwLEOy_rJ9qYU68bFIGCzVUs5W81oR5YbQhTm3K_CIHgfzP_UJUfUbZ-dgjkzMWj97WtmUQRGDenG2wF0fwb_MVwkq7mL0_19ZwO2Ydz55ONbM52uKgUivcVPTkWS-kD7wMjWCgY9RGPAgDrwl36lXEuuksACGzpttD4lSoyxC9aj9LQrU4AXPqHgN_GT-CVGAn00N3bOQJRu4V7Bh2x1l4QB4xLqg9sJrcw5JJpAfbCYwULAv0zZpaQqXiMIecV9ZqfvOg54sr_YeYTqFeLKakPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szqv8Tj444h43mFPVOa6PUOZh4aN0qb3GHHvulnxqBGNnGfyGceNFnzjvv8a_OuGyrEXaJ2bfQvcBNrZ15-khktIz5h1t5Oc8-FcXOxmFL8e2q5QmASH79LfiVpY7aYq4I4gz1q56UiUKb-WDPu51327hR7GO4sO2wZrNWMwj1ma-XyNLTXOy-vZu7qcZPPbT9XElK_Ms1ZUQyBHOcfYj9awhH3Oq4W1zfrsgw3vvF4L39aNNKKn8gYrnz9TcZu9e4D24Cc71pI4PD-3IIKt8C8bk6lISMYczFpfPV4nJKaJthN4-fpViUeLPqqniS32Pqo0jt6ppCX5gpPZpbXdAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsGpqtWHoPWr-W75tLZTyjVO65iJ2vyrEfCL6ZXikdMkGDi9VygDwUfN-ZGgHFIMieg7BG17VwOeTThnDTWu_5RvpWAFChzSCksh6k7AGOSIZkJ5zxpdP1qebj_GLdOtdjf8pV-umCwbWkfzIpkdjYd_2ylFFxPuNxZd15BXvpfWkKzItVWNfoNidGVp1TWehT-HHStDWxi_5b8n59pvFcM-HH_daklzH7iS5xl2mvu1djI9T8suUOPS41Ld2fOG-viwUSqLkwqSv4NHL8rxvNZHYFTEhZHFW8ys27UHJsAzwgV3KV7HFZU8Ra6gkVFRnQ46FQfY51T85oedrRBymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGO_1SAvCL1OEfcpHYArqxfea-tGHBskb6O5mryKfwnvubCy_O-5U8B_ZikH4bzjJg-VkjTQSUryOUa7NGvVLWxXjBHYiBqd5JAwVcW5NHD7bLqOQad_meqUF8Gl1j0a0CgQW8-OVBZulao9Hsm-T9Of6i5EGEMc3Ji6tSGIc8In5_PE4VAtDrMUR6zER-_JI7qCeR4i5XTkmm7AViltN7CQ72OQImzakCCVYO8KksnoCrTu0f4_qxckgxVNWDzglhKKpZ6_YOjHAGU2TyRrxFUZJ2EJH-TYrdblrlxA78E3nJx8Tn44WcevXZm9Mq76iRAz2yJUElW42OyPNE6Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJyvOzFt57AOb7XgU4uQxNm3Ak_W9TYpLiRgUkxS_cVlKjdKAuJLvfcbjUt7NWVc2n3Yf32cDWmQNLYEo19hMUe0m7FLptLBxiorS_oLFvMi96vltGCOOksfGHuTMqmnMqUjgZ9mzq-I5hE8ixVscyIU38RZuJiOFrj_awmWygyPwgig0H1J8qsyh6Lwx694ryEQBkZ0jfK1QOWWD-KIS5fo6uHP1qSCcdr6omSDywnB8r4Tzyg6M_XZMa_GrQvMQxTVgYjHpDfmE6JH-ROVmdTxPbH93xt-_MWTY0s1eaSgn4sRXtxB0ks7-YWu8iQHy0gFY9hVUOdIpbyfnh9Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=gwzImFy_SrYQ3j42gPkF1caOiq2tHanYBNVwxeXWdnEjbIEJw1tsnGAg2SV6Xxq6YK8TjeMdVLWx2y1rRnmOVJ-p_M6OpXMR8db3gcLa7sLHV76_rv_84RXZB_JIXwr3LHo0VYnSw6y57aNP4vYPn7D3HAz630wUwQnSw2qYefv2XJVWZ_mMS1kzIYsr3hUE-aWUENrKVNx6aW2iQ_h0NCsi2vjX5qc9D7-8RirKgzaxTXRYVKV6KoOpGnymUYzn4wElwoz-LZEl8guaXs3eSx75D1WIG5wwcTxRgasYFupARRlk3urgVQUB8iKvHPg_7tXuu8y6O60vOcHTw-weTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=gwzImFy_SrYQ3j42gPkF1caOiq2tHanYBNVwxeXWdnEjbIEJw1tsnGAg2SV6Xxq6YK8TjeMdVLWx2y1rRnmOVJ-p_M6OpXMR8db3gcLa7sLHV76_rv_84RXZB_JIXwr3LHo0VYnSw6y57aNP4vYPn7D3HAz630wUwQnSw2qYefv2XJVWZ_mMS1kzIYsr3hUE-aWUENrKVNx6aW2iQ_h0NCsi2vjX5qc9D7-8RirKgzaxTXRYVKV6KoOpGnymUYzn4wElwoz-LZEl8guaXs3eSx75D1WIG5wwcTxRgasYFupARRlk3urgVQUB8iKvHPg_7tXuu8y6O60vOcHTw-weTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drs34MRQXpY0MaooRpUpjBQ9xYkXIGfP7olOvpqklmSvvbpXmLQUK9ZNvuTNx4A3zVPW6kcGKH0eYfuX1Ri-3Etw7JuwI_LjNpP_G-qcmDKI08MuOIHwPjhZBZd6caONiOFMX-5pU0vyhGthxwPwqlhDzp7X0e57E3MM1XrpgAhC2eVNkFa0VFi2BGb3urZwz_Y_kiRKEI8BDrCYGBRnmdKanfFuIibm-ZCTCq3hA1ZalI3kcIEQuU8_wbkB_Jwe6PZFPBSpm_M-k06nzmjnbtmaIetwCGaR1j87aC-dKlSyd5813gePhV1495-fggCoE_e8saKEctUGR3jW5P753Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtgOeRhyiBXb9ljv7h4EiaSkhoCE72jF2-x6OW6PsqfPtelOct9ixcUboQ7w2Bp1FhkP0j4M_r8lb7D-NdH0DykzdljxW1Czegt5yRbFjVxPuEGx4EJH_OUw1y-xlpw-rDBuihdgN7KlA11ZrXOZJURFAQ0-akPUYmeOgb7tkbt2l67qqx-DMU9Z82YM5puZotOrwYgs2yy3DiDyCOlZaUyE6LfmC-I0E9g96RM8OOpA6TxbgP5ZlJFAkdCYCflRkePoAubPCjo3m6bQEjsQ6nWMhQvGr_Hm84ss1Kk1-6-BK2YDVrfdPCv2bwBhfPDtaGro_aPH8llB6RYQ3MTXXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Vuyu7RxrbHXZ7J9HFLKQq05NtrveymKOIXm-L2HMrP-AvI9duWWgU7CBcTcY9d_NKN_QCSHCvknpa10TlgIuKssfWPrfBDsee1qHf6Ie9ioaswT0-6icX2RxO9HS6HNqMM5ZrJsl37odc4Znfi-pNOwCftBCggT9j_z9VaUtRT-7jRo2kYHkN9UgA9G4bQNjZxb9lbYpBp8Sz7cPCKAQPlrJpXtLwbgBUZvmUFcgeaCbVF3RPKn-b3h7SDdVOXIhdwSy__f98V5CzBtoo9SwloZLyCsWuTSffj_g1paBotuzuHg-wUW6a1AUYd42i9hUIV_nvmtIdOa6E3ConWCpZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Vuyu7RxrbHXZ7J9HFLKQq05NtrveymKOIXm-L2HMrP-AvI9duWWgU7CBcTcY9d_NKN_QCSHCvknpa10TlgIuKssfWPrfBDsee1qHf6Ie9ioaswT0-6icX2RxO9HS6HNqMM5ZrJsl37odc4Znfi-pNOwCftBCggT9j_z9VaUtRT-7jRo2kYHkN9UgA9G4bQNjZxb9lbYpBp8Sz7cPCKAQPlrJpXtLwbgBUZvmUFcgeaCbVF3RPKn-b3h7SDdVOXIhdwSy__f98V5CzBtoo9SwloZLyCsWuTSffj_g1paBotuzuHg-wUW6a1AUYd42i9hUIV_nvmtIdOa6E3ConWCpZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ih7PXldbTNrvNTZySw5S4iwlKEEBxtUAxp5BWnei0YMsjsqxnhrNXjSZK7xqTubfXR2As5yOl6FFSvFgPNUdYvkUXNsA8Z0ls0i3wbvP7fhG5wr5_Gnj4kKuaAIGVno4kLcllkG9R-xaQWbn06ipxK7z2_7XKM_7XNmWeiRb7e4gpq84lbi132-SSmV4xUza5Pzyq4PRtKEwAJHzIIk49iO1IuDBz-_oJQieAGd9z2OjeLF_M2kBI3X0PEx8K9E2ZfKci0Fpdo4h_ZZHoJZv9OKaLf46t_Eh7IUjolOTH7RG_d4ALHEUfmXnXgkcZOnzuoiU6RU79bXRo45wQS5V4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dx3gl2vbe7WCV7qtNcsH8g-twUc3ayVJU6wKeO4GcCgU8imqwkqA6wK-31FLA53woam6azmyVNG_mD8P9VF05rUt-m5NpoFuz_VVkwpdwtU8lNQkyV7roeNIJzQWLX2qYsJIwm2a7Xi1GBhwBDcVUc1LkllczQz8xoLrltMrE-vIlp-ysLk3RFNlCYNCOnZcsiymzPoY9-W_cweWgHd5GlXJ5ityCDadwiFK4QnaGj_oZuYyCtsp-ne0IYQVqzfbE5uo1T7ZdKOGhu3ZFwRWIesnK7UWeNt0Ohmua1bqJaghIoySFyuWmgFWFAuLUV3NGx3f5gY5cAI-FfX_Cd3Mnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iNY0_LmG1AtG2A8-Zn23QCTh6toDUElfQ0N2NdeP3IAw7dp0SR494vvMjzx8-I86RtBok6z1KuEpYxNFMqbOdUzwSn8-tyOVACLARhkn92svi_17MawWaoSh8agORuNn3hvXE5gROrxFewbh95PddrYxO0HXBOiASll9iZ2jYPub71nQj8eq1OTontwv4PeXo6QZF_JxICpajErPWFLR3RRvNB_CQ8e59hFjxxQeBZtXEbfbhaxO_dN8EDcNjBuRkC0lTc9qNRe00bpMlF9YDNcTXnfwWDe-PE9mzJGHicTOQz-mSRrwHPjRcWpHmwNhclmNrEIEWaMXayijorxiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=iNY0_LmG1AtG2A8-Zn23QCTh6toDUElfQ0N2NdeP3IAw7dp0SR494vvMjzx8-I86RtBok6z1KuEpYxNFMqbOdUzwSn8-tyOVACLARhkn92svi_17MawWaoSh8agORuNn3hvXE5gROrxFewbh95PddrYxO0HXBOiASll9iZ2jYPub71nQj8eq1OTontwv4PeXo6QZF_JxICpajErPWFLR3RRvNB_CQ8e59hFjxxQeBZtXEbfbhaxO_dN8EDcNjBuRkC0lTc9qNRe00bpMlF9YDNcTXnfwWDe-PE9mzJGHicTOQz-mSRrwHPjRcWpHmwNhclmNrEIEWaMXayijorxiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEf32HHS7H3uIRuW3hpBbVuovqZwqpwWlNiDm-brS1Sdw-E_JIgtdnj4d8jXybr4pbyLUAM5snZaWzbrNBeE4XWfehG5KGePjirQPW4muI2mmA5iYaTcG2sFcdJJ5B4_hFwZDfovRoHKwi6SuAl2PipnujFW8HfyNBWefo_S4myJRAL2_YMCIY4NaJwJ8HEdlrNMdHRsw7tgwNlOsrMN4tmWWJmdwqkg93MBZFgjxLrZ2-nlz7xxJxXAwENxzWBnOkvu6oPb8eomwWelgd8JfeE55OKUre5iMOSThcl-Ldzxbp66hLBt7qfsTw7SZtLJGnBiIAWggmQfAN08UPobpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgtAw0p3divU1SPEi_wM969uNrABQJ--yvJPLg0RQubCpku-eg-ATDK8D6yoEYIAowCway9YAXOL_KbTpUgROgs6D-2YN-BCGCgutXb3NcJlMOe7pxMobZZlrA34TXQpJ_5zla47w0Tt4kmiCCRRhV_NhUR1Gr7TziG_wNCJSWwqnHG9OZpYKjGRQCaWd00ePw8haw89OhmhBJzOArLYIyav0DYlb4zsI4FRqy9Ci142t7fn-RNX37JsEAJ1uk_Cw-l-XpslcY7hU4O6fxP2PLOkaQLWNe2BOVG7IVunB8TY9mZNQhghoBjJRt_bMUKw3jFiOxoSM2NbjT4ZUK0jsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=OIeVrB_n8Za9AddatquABXIFskp-Nymsav9HP0INv1ssU9WFgKdSDH7RhSEG1qGpuvU2rsvA95mhJyRnO8OdI8pZtDGagkPYLOKJ46n4TF63AzPhQk1DIEgh7TiujX6TKO_ZGw4ceqz7lkqEI7GFfJIRPBnmxDTNQ9XrHgrtOzYjCU0NnVM62W9aMoNO18XKxuiLGP_Xgh7t6zU8pgfLhJvysIYr1hF4dXzgiLnMLMcl7z0Ct3b4MkMxSabkS_4fJG1UMIq3lPmPEa81oSIxV_BP704srt4px45qOT0QlbeFx0Tvm4CavDsZ8s78RC6vwMUJMYUE5a-xINFB6-Gelw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=OIeVrB_n8Za9AddatquABXIFskp-Nymsav9HP0INv1ssU9WFgKdSDH7RhSEG1qGpuvU2rsvA95mhJyRnO8OdI8pZtDGagkPYLOKJ46n4TF63AzPhQk1DIEgh7TiujX6TKO_ZGw4ceqz7lkqEI7GFfJIRPBnmxDTNQ9XrHgrtOzYjCU0NnVM62W9aMoNO18XKxuiLGP_Xgh7t6zU8pgfLhJvysIYr1hF4dXzgiLnMLMcl7z0Ct3b4MkMxSabkS_4fJG1UMIq3lPmPEa81oSIxV_BP704srt4px45qOT0QlbeFx0Tvm4CavDsZ8s78RC6vwMUJMYUE5a-xINFB6-Gelw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMEHJjiJic-BIF0epKi6YCFm-JjEc_deVp-ULXz6DUnCKDpJ8QkGAjPGY3zAvyvXH-etNxmwyRxWpnNzRlvvNG8LrkLtoifcOSw8rDRaqN1592pdYmePJwO1Bi0yNj3j93SEIVBS5fO2h1NASBJo7UcsPUfAtXXuLYPwZAISm0Xo6XGkdiQ0IHV_gFpo4D4X12T4e75SE9tp17kWJhxYHym7xevmLcD8ky4qbLXTncszJeXUnFBqpbNyaqZ6mLPvj3kcwCBbWYI7qmabNlbcEvdsEfUX5ml7cC6h8ELQFi0yW2wjG6MFkggeT2mDzG1Ki8kFT8fSsLQo3Tzq_zOgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZi0tSIIOhrKo6V5sFFqBNQrCIn24E1YDCkuoBhLjTbW0d9vpPUPWVxKjzv-qumoWMne_m8ARNbiK7iDW5tFbt0z2tH-BkHCGiGChp8ObbCeGI17VctayeX-nu10X2GUcig5dCvSPfewx2I7d2AKYP_YXQpoB2iDVvlNry_Ke1Z1GwUo2wgX2DIeEsk2lUHEF192BPejL7dSC9cUhgAOALYCgRwP1cxIJMbfCBM71ZOoRKiWGt836Cc8kkwm_i2Xe0hAq2AIpxvDbb5tq51pnvzCwoj738fQyZFmYjqr3-7FbSVU8uS7q4iXsVYIu2_fCJOKS1C1Dz6Ka7_IHuNjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt0hQGyn-mooxyO8JRlF6aZ2LM7cfGLriXb2Pdtynqy4LosN1QRO45gJDzQC9P0exv0sWopaKFOwoaIkqvJ5_wc0dKdIAvwT8FSQlZr2dAsIfjJVTDaHYRYHbPaA1hAwVwE6MOuXqm0MZZm7PSh1I35zn0tLdnfEqMHLHJN8_A8E3q24afR0oyNMYLdUHm4N0_9VMm9padp30SAThRWsrP3BBbiLks-RqLRv-kgAv7ZybU-E73qU7EMaR0GSEqFXeV6_KTP6DVaHxJgUZahfZnAOjoTQ-xRzfAlzAb1RzzIjMPq_H5QnA--4EJsbN6vHiQHrHC5S9wiX1P07I6766w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pa3Kacjzllgxb5XkjRPBCD7bUkatxOua72EJOg1y1P1NWY5ci--fXXg9XuoHOVucGvuPvrGpG6rW1mCKyH_qqUWqvFqqMaQCoFDuURur2xoDjPecJPCZjlaOT3SIEnmn8mC9ExuTTtmCg_Mx37zssIKVbwFmKE__yYEFQXt739gishILJiqTGppFZhOckrJGzHSy6XnqFxBVsVwSwLldtlZgNwg8LvONpO-Ak0o9x89lEcmtPwTccN_KcAN7K-mtUOj1MesFY_ToTm59R4tHuImXaokf7IJV7oT_SQj_q6-L8rIVG47lMdyR7seSXYR1a1dMCr0T2sK30nr97qiTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0aADaucgLPkSX_2nB_V3pnmPhCZEoEzeZ_bEL2ErW_u3D_OhDwiPJjR8FynfFbbam-bFM-CXs1mOghH2ewJCOmgEBffcG2ZcG_t9ge8aDV1szdkEhRkQSNlNFn8wrD1K9Mn28DgCBZlEEC0buItg4X4bx5aOP2JL9ifAmKRwxvBxfLOnvrBzodWQnhdavmJ6VS8tKuyfnNu4tADGhnMyfzlHtJxO8JUUDUBi-5gthYkeV-NIlfI3LtN2K0WnixxbQkmJXV5WHhSAHJg7wXUWGOj8rLdimz2F7ALkGASwKFWA4cAki0xtL51wTPo1cbEdmWIcmq77RA2YAPNAejPlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-Ef7-8UqgOUGyNBfCVsNjEAg_kYaDbNajDHrY-6HfKYfhmmQBGxnO-hfRAzBfNP937PsTWM8g6Z41ovaKcex_eVBM1ZOD_DzvdI3-6ajUPkQv5K1ArjAlfAaE4IBPaf12MCC8gHjWNnmXuenpm5R7eEFNeID3coGsBuOFUeL6Sxh4ovSLdly6ca25zo-FStamWazLnP8fwUacQ2ql9XK0TsF2wuwE2cRNwXIGsaPOQVI7NlJ5zVD_zCN2WxuEgmv5xIft4fBfB4jfYOLGmzV21udGwq0VBrptrOo4jNA_FyMi3ogAxujzcEzFRlWppXKYLNGC0arzPfevMPe2Ia7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caImqQrMSJjlkWOy7t76Cbgi3_sy8YTaJwQgu5TyfCcIQtFzIIiThADgeqIbiEFYPvRFdjek60OEjSSo1dU5MfF97e6350tRB3HDXykxLsw6ZCAf_tJIy9NdNd5NMQPhafsfS1lNb4ymbbvu2CdqGalGMplFV3_lb6P1w8iYfoNb4LA2lyKR0RMkutzCCuZf6oe8k1LBC5k9jsh1_Yfl9ztP68tvP8oqQgO0-pY_d1PUKsmpS84KOpJFBwZNeYhowtJZJrSydyna7vIHnxCuhdNiGavvvuqSEHqhcfZ2zzDw09QF9OsZhqMFeASQ6VR5FJoP5uUtm3r5HyPq7eFaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlMm8WCR_c8T2d53nybiuxtQE5GYn2ZImGG4M_eEWuc8wC0Xo-0U4aSrREWaaTOKumXCMb-0ocZ-AjtRGBg72Sb1bfFjHIRfpV45E8S_nRarsCMCN9NWGfhko0_7N36Daus39wMuH_YkxGD0SHz4CHaFx3Xc5gM9T4R37IRqC-myXIgh9Atn8Y5DbT6PMd96G8CThgEJRB7sWLbXIFE2Dn7GT-J7t25SlMuIA-YFbRKYv_7Nt8AbO913_uxtEApXSt6S0HuTDB1d9pZ4mn3_AjJQkVLiR5JHk-U2MhkYBJTSKsdu8uP3HQHS2KG439kTk1gxioxP_IIog5csQccs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=eBLoyZ5Glpx0NiVFUg0rrn-yLZ3xMEl1XJwhO0pQdJtWGH8jpUrI-JnP4XKZb-0cZnlvjnuscPdFskyn00OmBqDWSKq7uV_PZA2h1A3z6oiru3nEqLZSdc8-X9AGTn7EHuNSS_-UjUUuYybQESk_AZEtFY-Yk5eeGOJ_KedIIvmoS8rvGQiI-zt3Q0wUEbUOyk_K4W5w1lXpDFOz10Vm1AQufzTufen4bYQweKYaclJRveujLDNCyAYudxL3WUTrksTUf1KVnB8c4tT9Hg2FG1gIpXrvhvybPX4gdAWlm94RBehROOsQYzFNbr5aftpHuTL6gPZEPu7N7ZUaLEdpYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=eBLoyZ5Glpx0NiVFUg0rrn-yLZ3xMEl1XJwhO0pQdJtWGH8jpUrI-JnP4XKZb-0cZnlvjnuscPdFskyn00OmBqDWSKq7uV_PZA2h1A3z6oiru3nEqLZSdc8-X9AGTn7EHuNSS_-UjUUuYybQESk_AZEtFY-Yk5eeGOJ_KedIIvmoS8rvGQiI-zt3Q0wUEbUOyk_K4W5w1lXpDFOz10Vm1AQufzTufen4bYQweKYaclJRveujLDNCyAYudxL3WUTrksTUf1KVnB8c4tT9Hg2FG1gIpXrvhvybPX4gdAWlm94RBehROOsQYzFNbr5aftpHuTL6gPZEPu7N7ZUaLEdpYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNx0g65ryQxR3bZ6aN50Fx5qZ7G6v4Cx0OmEG5kQ4XOQ6zCst7ag1J0tFOXrSyAOmFQgOMlm4UKGu--YUF_LUV2P8PaZWAgR19n8U6ktuWOKHFK4sKgZbQOmTNBjmUzjyy25nv-ORxP522i8HLjmuE3U66A1-CKWBv2lUJzOdKk9K6tOpM3iYH7eUJDgXj8ZEpx0qwBqSQNZgVjRetxl0FH861iHfpT-fFJWVNYgvD7bEcHsXYtM7E3HNHshYtbaAzPZxeUFYWPpVK0KjqF7Ehdy2AkfDEaKGL5ehpS3TsOElN91wWBekzOwIIOl6Y9vo5tW0H-mh03TK854yc3UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BOKcps9egPV0g66tZ5z7l0P2NZyIfsCWrkfRop_lF8Tf7NNuKgEoClqWe8RLBqryZ8HkHaHGEPWYQIEP7SaTtcidqjN_1j9SR1uCUh4USFNRMCZfOlctTQq5DA_-gpj3RPXHvvqCq_RdCrkI330obzRo8FCLRR3q2zIM_55xX24k81ZOJ_DBFGhjQp1-A6ofpb2aCEdmS1QE2pyHBpiPreCMMj5SV96JIYIDyFL0z_X2RIZlqtSwIfj13EdkC4MsDYjLePHxBrV1qOTNeHwqStvwAGwI8RjA2VtYs_r1XB_D8VfsxCFK-eUglWmUTQa2BmXx2O35MbigGsrGTem75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BOKcps9egPV0g66tZ5z7l0P2NZyIfsCWrkfRop_lF8Tf7NNuKgEoClqWe8RLBqryZ8HkHaHGEPWYQIEP7SaTtcidqjN_1j9SR1uCUh4USFNRMCZfOlctTQq5DA_-gpj3RPXHvvqCq_RdCrkI330obzRo8FCLRR3q2zIM_55xX24k81ZOJ_DBFGhjQp1-A6ofpb2aCEdmS1QE2pyHBpiPreCMMj5SV96JIYIDyFL0z_X2RIZlqtSwIfj13EdkC4MsDYjLePHxBrV1qOTNeHwqStvwAGwI8RjA2VtYs_r1XB_D8VfsxCFK-eUglWmUTQa2BmXx2O35MbigGsrGTem75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=t3Aax6srzF5hlLRvjIBk2afh72wWwgWbEid-oMMU8nTJJaCmrhXR0N9W6EV4tKmDC4XfoXRQ0rigTcqjGE_phMt_-ugJL3yPxquJIZ08tQi3KjItp96EwS7K47D85tEYWADlS_djyXmeTjyO71VZHEXT3lfVPA-zBdPAilb0x0MMtoqvqkJ7aZWXIIc-iZnjaU_IdbHX4qULu60AsG_NolcV49NSq6KKpW-MjHN-wt1P5E-GJ3JW11_gdFjd5YlwusB3q9zIu4xo_Tqh5RLHPrSJgjkZXlTYkOT5zGOi27BBya2yYlkb4z-d35B4Un3bABggeyJ3QGB_xPyNrwVxKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=t3Aax6srzF5hlLRvjIBk2afh72wWwgWbEid-oMMU8nTJJaCmrhXR0N9W6EV4tKmDC4XfoXRQ0rigTcqjGE_phMt_-ugJL3yPxquJIZ08tQi3KjItp96EwS7K47D85tEYWADlS_djyXmeTjyO71VZHEXT3lfVPA-zBdPAilb0x0MMtoqvqkJ7aZWXIIc-iZnjaU_IdbHX4qULu60AsG_NolcV49NSq6KKpW-MjHN-wt1P5E-GJ3JW11_gdFjd5YlwusB3q9zIu4xo_Tqh5RLHPrSJgjkZXlTYkOT5zGOi27BBya2yYlkb4z-d35B4Un3bABggeyJ3QGB_xPyNrwVxKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
