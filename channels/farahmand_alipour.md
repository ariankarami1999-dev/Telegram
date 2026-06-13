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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhz-5BnrPY5To2QcI4rTr42HJWyZdnFzkMR6L8tIk-ZlEFfvgp4MwjovRhsSqF4faseXwea5MvzjtXV2v3pcmpfw66Uax1JHoudZuSSJnwfyl_e68rXtZfK5F-ANyWoPPOOQoRF0tQK9MSkLThlVNDQYO0dLpNgk4TYyhjbZMmqdYv1WO09uJ16u5GwFm9zZFqEZPqNx_NuulItjKlVn-HD5x4oo1MqCNeuQItMCDVc17kcwmhQntQhHKUe1oZYOtkrs4T_KNtgDA27_9qab2c-L_xD3pm3GqL4xIGjRJrKLcZuBEtTTuJ9rkSPaMY_p3-Ws9OqfrscvfuDk9bG3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=n-oUFkiJedHevY4_dJ5tflgN_PR5Fy_gbk2_HFOzo8mM6Remd23YGMOcvssR9ugjD_g0FA_GlvuNHxMOxuQYK0ZSiDYsZ_mrTEIPCKlNfVM5CPGXDug8UptnQGpwDCD0rtrDm5aSebibvv_k3R5uA_wM9ydTJy4rk_NGLhvW0QpIZ8iiUBFIysT8dNt8YUdVD6j56CQXGBTD5C1jx6i1bjsm6shQeNyP9nY75XD1NfV9045bJF7qopghuOONYC-OiohC-OybkNrx2uaP1gMyle9aSR_dQ603PlP6XP8JPJQoc5oSlosdXew9l7y3BOjjQOkY29bYAM6UvNrLt4JCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=n-oUFkiJedHevY4_dJ5tflgN_PR5Fy_gbk2_HFOzo8mM6Remd23YGMOcvssR9ugjD_g0FA_GlvuNHxMOxuQYK0ZSiDYsZ_mrTEIPCKlNfVM5CPGXDug8UptnQGpwDCD0rtrDm5aSebibvv_k3R5uA_wM9ydTJy4rk_NGLhvW0QpIZ8iiUBFIysT8dNt8YUdVD6j56CQXGBTD5C1jx6i1bjsm6shQeNyP9nY75XD1NfV9045bJF7qopghuOONYC-OiohC-OybkNrx2uaP1gMyle9aSR_dQ603PlP6XP8JPJQoc5oSlosdXew9l7y3BOjjQOkY29bYAM6UvNrLt4JCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9j4GZtrM3SKgiPHg5T0S67z7_Bse1KbBfpcHT_FDIO0aLzG8NZqpeHZIp-R8dZayEfPc9kxJiJDvWhSCVrVYUtb7y7EpYtDjBdQkBc4E1OKVTobDJyOHm18fmUqf8303Zp6BveXSQKMUwscx9M30raN6WzbxPLI8qFQziPuc2pHEPVMKGDaYJa-P9gJupVtrmyurXkQjF1QKLmPNOvdFfXaV89hAh2cNe2H05ySTtDpB5hEOUidh8zBBnHhyklGaOLHuM_vigkeOyQH5HzPiukQOwnj48axiIl_k17hVs9rzRQc9UxGjZ1-xr7w1SLMNY6Mcuwhvo1gZVG_sgC5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=a07myhSKJgEY4FWCQkcDUoflOkTjvz2TI-o3lpgB9s6JqfWij2rgb7pnhF4bOk8lfaiK-JeJXsR04tByHBJ1vTUzrObdLyiGqgyaxq4tfbJUL1-CA6NNXnGJJXGbNUCk-qiQ6GCohvTpZwCjW287X0Lx9bp_jjsZhFBn3G65JA-2kpEPeL_GDleT_OOsyYQCMcGTNLUbOfX5V6xqhb0LxIYavPC7ksmplftnNELnmckphFHGj7TFu5ObeNnPq0Hdz8oo9GDkRj-yWLSwqyt1xokxK355_K__XEJAodHevjPOCc8ctdqsn7H4dERua3aaB4r3q7VC69UijXFII0IwDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=a07myhSKJgEY4FWCQkcDUoflOkTjvz2TI-o3lpgB9s6JqfWij2rgb7pnhF4bOk8lfaiK-JeJXsR04tByHBJ1vTUzrObdLyiGqgyaxq4tfbJUL1-CA6NNXnGJJXGbNUCk-qiQ6GCohvTpZwCjW287X0Lx9bp_jjsZhFBn3G65JA-2kpEPeL_GDleT_OOsyYQCMcGTNLUbOfX5V6xqhb0LxIYavPC7ksmplftnNELnmckphFHGj7TFu5ObeNnPq0Hdz8oo9GDkRj-yWLSwqyt1xokxK355_K__XEJAodHevjPOCc8ctdqsn7H4dERua3aaB4r3q7VC69UijXFII0IwDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjnzDvRaoN797OrjaK51I_p8O5oTqirYCfQJmw5nksDhY_SxR33FzymPq5KCEe_W0D4tE6sbbAPs-DtOybZuCFhGJuevby3ppmNLdAmqRmJ-BHyI3gS5_1xjRmOUWpxJuluPQwIR6G866CnVmeIt1jRUzydwNeLzmyI8pTWVXCrEtmFZI7i-02NxxoyslXrHK4hD1qPVNFb2jzuQp-oUHd4717E8GrAsA1JYluj6MRis-ZzXN5_t5H3ESnm5osqe9nEVS0SpZZrtSh0BbUYqcXxfi6zvyjQxotqfhYGjKQDI7_vQPsY7_bhMvCWTCnREA1VgAaW3x2x7F7OoPKMnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5LY59Nhu-teKzVkWCWsWryNCn6nbR_8nCI5wVJvs-cWjPrrVvKhaY7NzAlruZ1T1I8w63XsVbMYfnyruSy1KJO5Rs_RV7EH0Yk7--4z7vRVtf1QeQclfUxVoywzSaPIbSW_FVjr7tFL0HJS-l5HJWDE5utPNXgDBwfK5CpbsS2E00YwBC_AXuCd-M7CzDvOGN8YGnHcJq84wTdadZcSYAlIzHIQiQS-2mMUG8GabIGP3BiUmbtBK3wDN3iTaQC0IBpv5LfjGDb7wF-iI3eW1Q3ZRmpQ3Kqc5Z9sdBjseFu5L0Ux9y5q5ymCXoJcXPhc3Lqw9aKfsqVlyKruF_T0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyGhntUx6osOKH0vhclVBhkLQ4FsrzHnlqfSfE2AjyragXBHrMRDjJ4g7yIHQS40CRmpuhqmEhWpWAHPf3mGt0Fq7rbEEq2dg4fG39S4YO61Td8Djw7sODYTyMznnryJda3IzrTEG_k57_RcOQsge36eQiEJJVaS03iTjGny4qiXlYCuPrAmDZWfpLwiHcfA9n5AHc80GBxaRkpQBqvgpFYMH3wJHQDsU-XfDgG_fvvXVFd71A0QvnnQ9HQugFV0zjFA9Muj9DeiHgaSHPs2bG_gNub73Flup25oZW9fAolxJLPVLG05Lb9he4jBvu0LWWgl1bCjlehntr48mDZckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZZSHeFLBHYXzlAyW32LvKL9Tf_IkQ9QailhAsxFnwJoRws2JSB-StW1I1FSTNfxYGitbjWs_9I6czVhdyEvexw_XPXN1oQZSHMGOBGJwtb3a8GqnVjpjL8MzAK47b4VW7gVYej00zuQ33ddmZJqfWmSbL0l2oFq0llCALOI-JPCFxN_Dz_oPFT0doC0SDZW_vgFVNLX1-ZL58PslD8QptU_wFLWvOXdmq_2XogAUHdTAf69wBHBRuHAEyb2MbOcSRnv4PQ6MSS3SF5o8DGimFxycWqAhDOH3-7r2Iyq3dVYOE8gcHcFpYwvpFiYfKgSZJgzKKlao5CZ5uXAcQ7Fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4kbp8uBPFTq6ExPeBWzmkc4eWcU9FrlzWRfXmwfQmvzDJ97kosqj1WBzZGnkOor7hWhqxV1-ubV-dbi_6MO3S-8HvhGohj3xj-4X71O2jm74rENO9-tv3yPCfDvMF0kzEYMbsweQ01V8k8-dkuxtR0lAqMzzVSfCT7quSGM-N3ue1IbF3bHdJLMsq6jy-vxOyQylrr1hPT3zFK20Ww7WreYhSzozuVMHVH5jSrXiMTjoshZZJA2ru2sqmV-tzFsZYvqsrOCnA-M2DZbcPCY6uW_hVxgfUeFSght-1QxK_JKhWYvwd9BoA-jELVNITPcEJcJQVQbRgv7_a4nUJZkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii1x922b7vMWxGQBCqSKepX_3W4jXrWlx9yA5ALCrCXMYNldkaMQ1GI2LLPi1XweCpIyF7zTVEClJTNG0XGjnXpUlWGtIT_ZLaR3B06upQCR4WvEdjZcA31xk1KCOP44sbuRAZJn7XBRHh-fa-vSXGG5jguzp-0act7CCL8p2Mof0TOtrMn5OU91qYPldsxpFCiqHcX228oOP9AISBv-uiqTyfE7mjj7bKE_XbK9-RncDfbXOxUxlOSoBkuCFz0c18x0rqXynhFgbbu8xFwjynQi2ydCSbF8gFc8Iubz17TcVDgraJYza9Yvi1WAiWHkUuBVrcUBmS9o2NekcIFR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=mbz4BKqEY46SeCc2K7RWAGXNUY5LsYYxAmm_7aOwXU70LfN_OaD6fK9f4DolOXwwQYS8qYegZdWYrMXhwDItd2ZhceBtG_FdhEqdmywm7fvzmPy12pDjHUoTNbZjVC_zqMjpIrkR-ZU9F3vY_UalNQMtk4mP7UrS1V9iUL4KWzxly1ue-NwMDkJtbR624YYqrZCW8W8DrNdphwsV2lT5CIBQ5x5e2X4_qaA24qa-jnHMxjsGJmLaqU-e2xcai4kyVaduCv7mvQ2lvc_AfwffSUj5w7BRgwLvd9oNE8vfoKlBbCkdey28l4qnYUfoClVSVqsM5aSH4SQ_2HBHvg4v8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=mbz4BKqEY46SeCc2K7RWAGXNUY5LsYYxAmm_7aOwXU70LfN_OaD6fK9f4DolOXwwQYS8qYegZdWYrMXhwDItd2ZhceBtG_FdhEqdmywm7fvzmPy12pDjHUoTNbZjVC_zqMjpIrkR-ZU9F3vY_UalNQMtk4mP7UrS1V9iUL4KWzxly1ue-NwMDkJtbR624YYqrZCW8W8DrNdphwsV2lT5CIBQ5x5e2X4_qaA24qa-jnHMxjsGJmLaqU-e2xcai4kyVaduCv7mvQ2lvc_AfwffSUj5w7BRgwLvd9oNE8vfoKlBbCkdey28l4qnYUfoClVSVqsM5aSH4SQ_2HBHvg4v8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghCEO-Tb3xnHAndavBf56O3nXgfOYuzIim-7zOnF_VDTM9CfJAbquJhngZo67zp2idZFLL24xiqeZjx4mKdRTdjkAD6GI5d_eef2STK6LfMk-v_Jh8QCcq18HsomXI8TjAn4dYgbe1pH6JwVb5wYIfckumISm1tYbUbwEOM7CYKZgQLQpxRgw2vCinvcz2cCviGVwyNVvDobbbQy8m49clCLgo5fbFUZd9dKLOFZaYUZY5ekRn8wOCKZhvAhpI2-AQxRTWkais_vgkAYnajlFBknwT5CweWBS_KM2Bw9-WZEvvfVVoEbr3cDpSXhgms6XMvgm25a7yTDBUYT09utvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3Nw94AHAF8h6pXCgrd0Uf2k3XafkEYEIV-_NMA3RbfuwDhmVspjS7xAEXzKQieG0hk8t8ZRhpbfBkDvSWQBt2dG_WgGAcEyIE8XIyNcNGbg9TvZThtX3gE1HxQSwmuW0eSbBAwxPlBfQrUxZ1zfGKWpwHZtugmp-JXsS89ff1ogryURXS6rPsSbMBQLu0pcgsmfwZR-7DdFCTFpiBur1IthiTnerGFTl0gR05EbDV6LBO7f5ADIryyY6hf6a-vQy9TZs3B2GOohk4MrTvcUvbsd0o_f4Fq7qf2qxZddn6p-35tyjwVuvhD3CrUoaCLKEY5JJrtrgdTEpWHc2dh41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDPVNzzoxJHlxKkz_mMQQtYk-ojKqma8FBrmStroVlER69ZKHFkWy-9kKD1XskNY8sHfIKw6itBiLfGX9d7___FhPjqjdKMKZmZL_eZDY4oRuXf9HAdKl8P1raM3JfO50HWeRfD6dztT1U-AY3eQnZES1W9XdrL8T_CLll57A7DMkaXvHiaO0CU7K9MY3BRJm7CFTxz7yQVTnrM5XVJXrm8PhixHHdexZsEmdGeqw6o2zkKAxXbxYJYjUSrVsErz6zseGXAVlfc8nVcV9xjSkidYScCK1Qx_p_yxFoRBfLBmVk9VOkOQh5xnVbbHxVVJIXqixbNo80Om4TQPBdFvDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7YoPhwBegbUYXPt9mkp2XdIZX7WC7W4v3JWAYQXyE3iFAQomw0ukewkolOopx-qaVK6ZLGc4ACmonTD79J11qZUX8Ejihq0IX71kcOJ7SCoByXkWb5Cfp3MyU-dphHfw1duyYUCR9NN1MB3qf1JtKXNTGxPxFyxH2RfCXbemA_IVINsbemblexe35lJmewAw6SsiJJspzN6HfP1P-x655t1m8kZm14pQdbT9DvYCyFArp9ck-YauBhRizep5LkB2ptV400ZtRKd499mOm9u8qEJgJtSGkiLa4ZEcflSiMjmpEzLrzk86ZJ5ginUa3kzWICSZuznnELfJGzxxsMsnQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=vNJqIvyoDB3wHcSs5qHqV3wuQCIiOc5Fy3jtkyOHKwNrW1D-l1HYzAm_KJ0p344CI0q4_Pnoi7ELfVUsQGPzNqT1bInNPVDDLHw9mYqPJRllNFn5kl8Kjr-4Nr18ahd3FOEahCsQXtv_oWCwK7LJLdxjS2L4ynD1ppoihNVEni6kMwE8q9uOe6nbkEW4CeaiLJyk8LhL1x4TiAL1QQltoy95hbfOFhLQFsUJQ8zn1Je7dx6SnKH9j8eN5O6zambu_Zo6qudS_0_q0ZFhSPbIsweIob1ECYDNqmnKnHVwsm54c50AC7XGcyCB16XdLNZJRG2k3hHWeVT1Jchsicdv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=vNJqIvyoDB3wHcSs5qHqV3wuQCIiOc5Fy3jtkyOHKwNrW1D-l1HYzAm_KJ0p344CI0q4_Pnoi7ELfVUsQGPzNqT1bInNPVDDLHw9mYqPJRllNFn5kl8Kjr-4Nr18ahd3FOEahCsQXtv_oWCwK7LJLdxjS2L4ynD1ppoihNVEni6kMwE8q9uOe6nbkEW4CeaiLJyk8LhL1x4TiAL1QQltoy95hbfOFhLQFsUJQ8zn1Je7dx6SnKH9j8eN5O6zambu_Zo6qudS_0_q0ZFhSPbIsweIob1ECYDNqmnKnHVwsm54c50AC7XGcyCB16XdLNZJRG2k3hHWeVT1Jchsicdv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ4xEs8zsbX7icme7SU0RMy7P3wwqSWQKh6BxeYocDrA3qX0O9iXeQRkSW3f6N_GsMOsA3TkePFL0bp5Of7Y5rRxvCQDKZ1JUQvNwpOBDHinVtjw9gNR_X68zbKymae-v8U11cJGZRLts_mwLogP2ef4AgCWqbC52Dhl3Bl1xnuTEEEgEZq55D9w_nHA1h0s9U2JtqMXIzjWzWtn9_B3wlYESxiM2S3Gw1eLTui5egXii7YQN9j5FbtmacrBlKXiWC35IBprYt-6PPDpq8JNz3HZgjDWKLIZkQXOfn1Wrd9Z2Ti7p3pPLq94SxeaBwJNd21ppFJJw9cX6-pVF1w_Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP0QuxN7srpGYRvX19J_01XVelG4V5UTX4aC2QPRly_czh94MtBoweeBxNQYJxIxI5C6-gNG31sRVrwt1WrosWsh6IK5in7ftMhALdSTTaoGZTJ07Z9MTlhK80Zz3eBUEuS1EYA563YNlw_gAvLfO1GthfFmtSIN1K4eZwoGyKRnOw979oHnwEdXPznULyMUyRMkjhN0K45ftFEy8o1FJtglmVy4TvTZUTvrxslGbNqUkJjlcsY7O2WCZnQ-_wlqJ-_y0sIaXyjJkoiofJGn-DsnoDPDbgsvUU2bzD_VWCLl4r_tWkXVBc9TQ-9guaiWXWv0_6I4ADay_rrMi6tmeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_-iTM5rQSeB0lsTjatXHXQkc9fgg1gAU-_png1qmQOjEt1weSNkagArRpfySjfYngWCawD6vjB82dKxGDyDi_kiDabXmoAYojKmCc-GYyI7_bTv90-MYu_oQXlqDZfXg29bemVV43LYySNuGaYfQapAwraHjsAftBGOt9bbRIcAl0-o2k71Ny42s_3QgYgMpPyWTI_EJqfXJux1sa-fAM94656Ojj7d5xIBErzIBJ0kSD1fhnfr-ElBzYavEtQrusqwqdI45mO60FN80VhHvnmbJ5Z297mkVfP0GZt4StwxQAMF9wzJxtLnqiTt0qYlPbnt2yX8rTAkdVa40xIQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQUt5Yd6W-t8esc9Ox4tiKn664OaCMrwMiMOwcs-ictoHtrZuSrR9fJQeA-zMn0FqEeQmLcBtYW1ARiOaHu3z_bA77qdMLcU2kIyH77jxYqBATgG-7pZBJtoE8O8YbqGQc1byVOAPjlQ-XqEFJl2I01ZWpNCdSq05qRYRn0ZpFLfj4yxNElCQbTosKJZyV9ihgM_P95KpKxYqNNrJfM0aJRo8CcQYXqVG1aC3L5fpgj0jf91fzmNQ_JR5ZlbK9wJv2cWyuSLzX-gIGK0ZK57LaBE5wi8X7T24ycnsWRlniEdB32tt3CnNPJiNjI7f9TxawQWBU0GSqz1AvpjLfEsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osd1dlpK8dJ7o9zDLNXZZJ2ftCmKC9hByFG0Yj5xAgmq89Yk2eZZnNd_ikZ3Si_eZ9mtnsr922qfkRksImhmnAYo1HyLpdyk34lBg0V_aahda6wC5pSiCJNlF_7rmwWz3cf9hJvpc0_zXnPTrDUj87ptVNEc7_H46Xy91VpYXxdSskwrdbUT-Y21elIC9IzABg8sXbQ3emEGsJZqjj8zMCpWBaGkGaMBDYgfHdJvhbAIpzzEsKMjW_OlSMlZQ71u91OXD473EFXpFXR8Knthx2Sb3CZ7mMOarJYcQyIcRUg0DDxfRD_eZ77vN5tXH-eA_JYNIsAm9FxAPKM-xeqr2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlMQB92-SWQpDIscwGhEHC9det50sx3nrJKZeKHkiqSofB8R8fvgEOLspOC45FG5MwwnWwrFedWlrM0YOeKP-YMcliU247J1Wf_NVQ89qc7YSjNQWwFPfIKSMtd5XEZzdjDfOaYGyqsxk_jarVxjTP2nlwAHK_mIBz3KMONeM7P2cL4Ism7mwKLJTCngtLK8EaHdIPEpdtdbg15UQuGNafpeAaUAWfvNl3XY3z7nSYdI1aP1DdREBqotZouexxQLV-4Om7seqX4MqEJn_WXJcqD2-cRM5DL2hYAaj9qmpCPdCkYNh1KFqqMPw03tD_-2VxO7hy-lf7fMPwomy1ynzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRpFrvcabmSarLzDCzO5cxLNMXZ9j27ci5SQzU82odafixF7XEQa7w8QTk62qM_GcgzjIUmvt6PPo4AxY2SVArOQXbzRon6UwMXCV1JjGj_ot0wuiAlSWV5maI3X2LYT3CwwgS2fmAzfJWuF5h5BjQ9X_5klLxx4eakan9ZHGmly5kKpDGAeaIw-aoRZCpMIOOslURKMBfV84VN4gk4iHiDqIgwQzeA5K4tu2Z_L-72J_jqfDhOxwEjreigr1jt4qfqUatRgkZ-0hMSTKUFy-0X13_HhYURygifwAYuDS9XjNZCNG-TFVpgs4n9xlVzn0e-q8Sl8C5tUVTDNtqdsXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLYw0Bzx9tNBGtq16PXU5S7xd6ZH_IHEZLDBl2c8O_F1OBndT9e1in_PCpincMODY8a1dyrdR_zb63Kvy0TFpum55VNdPnwJiXFiyEcukMWjx6okdqXusqDjNIiUZ8aZfRrrC1JlEl8MZSpeusHrP6zy8tb7fyTN03n_deDY8ZyGv6ff0VtvuRtGyjRYsPjiS5IRd-oPEVOg-PQs59IneW2wbrNbKSmBmmTIKgEwT8kPKrYIsRrrthznbM5xQxvppXHRxtP8Jgxbc7vpTAgXnpo61zOXXb6iHGO1DQcwjzsGdvWUl8QTFqGejejvQcmk44TESUhpRypNwxUGdSAuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXC59vul1p0B9ZVXoclp6GSpjS4JqrQbHmO_yHRjmEt4dDO-n-59mvzGW5tOOlsn2_cwh5DKPNy0tqPczlKYVOPOrEicyUEkR7YkN93_x_KgCJMC0xH1wGLTj_WN22qkbXODCT-_PAntNJViFLGVYG2IcIInhmslQ9AcqL9U21qDAiIWAnibXYcUIMANeTA4_3cX8YsEvMIzVN0NM5uUPbesngYy-BhLLJztWWfBw_-I6KTtgiq8mY3MyT6dlDsQK0y5zbMrLz1OiqBm-siTxMn9D5BQUraWoi-l9rRTd7Jmb7tvTObl1h44tuEFr86ftBTd3-4VUzLjEOV-GuXlUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=RE2QTVW5hEMBVfiEdGfUiqA25tM4CyEBnGzBMt3FP1rFUAgHU5013TcJAN9qTjV2n2R3S2RKJb5_ICGUPHXBvHNEwhzwWxqz_274nSAxRwQz4J_8WUiE3em6XYUv7crIlApLm1UGlEcr7aAcPuxLz3F5hjrBGEMzUxVukI_-WD2KVzG1YB2iHZV_ROtzZvQF6nCZxGLBUfQwdj-RCQ0duL9uW2IBNknDlcCFLxEG_QpEYyLzOmvG1bkfboSpwlmVD7rqjo44GhcLyZqSgGC_jIS4G8Du8It1SEctZ6RmR4FQXsPPMLnoPpXgmvefn7GNttbbxxFE82UZRli247z_UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=RE2QTVW5hEMBVfiEdGfUiqA25tM4CyEBnGzBMt3FP1rFUAgHU5013TcJAN9qTjV2n2R3S2RKJb5_ICGUPHXBvHNEwhzwWxqz_274nSAxRwQz4J_8WUiE3em6XYUv7crIlApLm1UGlEcr7aAcPuxLz3F5hjrBGEMzUxVukI_-WD2KVzG1YB2iHZV_ROtzZvQF6nCZxGLBUfQwdj-RCQ0duL9uW2IBNknDlcCFLxEG_QpEYyLzOmvG1bkfboSpwlmVD7rqjo44GhcLyZqSgGC_jIS4G8Du8It1SEctZ6RmR4FQXsPPMLnoPpXgmvefn7GNttbbxxFE82UZRli247z_UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp4OYKDmkqOCyJnW4Lu35VpSkeWzMjsbbw1z5v78EjNAgEf7lZjjhnlpQ5LAaqX6sQUTSzjpSHhO4L9KU-p-7sAcjJ5jZWF52jLHMLfnGs1schVRSscW5JMCU0zsZylHKBN3vuz40_ZVif-A6VfxaBNg9Z71dOJeWgV-AiTMhs4HNZI2FI7PpthQlt-QAVB5HUg_2ySFuDe4mpTmyXGoZ_Xl47oUPzv598t_5PxDsWt4YGr5iO2zM7dEnnuVH1etqsxyhAcR3ZSOuO8IS-d6jFZhgv6YDQP0n0Vdt5AEBK1Is8glKBHrxacU5ApJnCmMxQtehhelCBcTBUpLGsg1OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R83uPcZqgkxzjlCfXTls2jZpYzb2zA8g0aEfo2WYKgqL36jKoKlPLJ24UDN60h1mVWPdplIh19DSvOgYuA5P5tiPwHCcTVOhDxYgpI1mhPnK73mseBPmdRuQPvghcD8Ya3bCLADLEk11dwK8iKuQz2_RTlue42HlRlCJLz_2ejEEeEn8NN6Umcm7bgOHWMWRn5Lr0OxHdpi9kr1iqbkmtUSQ1Dw9lIO4w53-nD9RP_ZQb1oc6c1-XRwxBrTB5qbiHkM7iRmq_WgojsAeuMh_-k7Freb4jy3pxyi4mD6TnRDEVi5vq6UH33Zoa6Ox-Fg68iAbmT4SuNcLcvoOT-t3Iw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=jMmUzbEQdY31EIAS_xdwgYWEnIwr1t3iKrM8iFkRt5Ne5MYBV-DfyhTA3ayxxwizYTZUWK5-hIrn6jY6WVcw6ZUM0-06Oq6l5PdsVpEo5qpCXfWgqG3sV9R735IMHdRX9HYmfdxS0ImZYsQjPT98_vxpYqY_pxNPyFEfZiESXXOBL6DIJU2xw5SyqdgcPZtORW7fT1xnh8Z07PIfhv4Zx2-b4oWmaFwdFUFaBwUlMWBSh8Ajg55imugcEN4mI2gd-2TQUaBU44sd5BHsB6VqLaWTEHSsc-5U51e5mTa6lXZLXOwDvC5oM4ZQhzawgyxHUJfcrpolF8V6ePUb7IFMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=jMmUzbEQdY31EIAS_xdwgYWEnIwr1t3iKrM8iFkRt5Ne5MYBV-DfyhTA3ayxxwizYTZUWK5-hIrn6jY6WVcw6ZUM0-06Oq6l5PdsVpEo5qpCXfWgqG3sV9R735IMHdRX9HYmfdxS0ImZYsQjPT98_vxpYqY_pxNPyFEfZiESXXOBL6DIJU2xw5SyqdgcPZtORW7fT1xnh8Z07PIfhv4Zx2-b4oWmaFwdFUFaBwUlMWBSh8Ajg55imugcEN4mI2gd-2TQUaBU44sd5BHsB6VqLaWTEHSsc-5U51e5mTa6lXZLXOwDvC5oM4ZQhzawgyxHUJfcrpolF8V6ePUb7IFMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFIW9t1nZTTjp0QVz4L4MsUE-rp01ojXILglda5Twv7ghFuB-yCEIPlOcXaIy6Ry_3oFUd4sKKmUmtXf6FrTG-sKJT0-jjcxkcFhBuykCqTEPj4JbO6B1_PDh_oioJzxDyuzg0RmN8KZLNubQEAu_OGfHizzrVH8cBKkZk0E84Gs-MF-yaKz5Lu-TKTaKWjnQYE8rpcpYAL8k4D44x_vOXMJyM9ARX_mlBxbAJTforRzX_zoRNrP0WGid0FRBo-DX3SbtAzoZKwvWK-qeAoT-wmyqDMPU-AWyqkgE_JR6tPsdlFxjFj60sSM_i2mkbRW3mP_xS6WiJ82gyWeeHIfYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7CcyD25JSWgvNFUQWa-9Rf8bCbKEFxWtHQo5MjKVbZqGZpdsxtY1h1wfF5kl_msZej3Ck_wqo1QwnPCfe_pj8OnUV7TmJmTNjpanyTHj3JM2F5_ntDUXx2HGxWXjSPecizBb4Ic71m3-fQLcJLJzFJJKqUN2TIyXjiguIsrTgv3kGbpH4NKUn5ID4WMca9pF9vN01TT6uXDD363JllPri9zvOFpgihPrDLef5nlZhgw2DId0GkXsem1Hn5P6XHXZ7GEt0JVgtBBthjNwSuVcLd9ozZu7DEMEXF3GpGYq6b3HBhLY424c09UF0q0PV75TaXaD4OvsCAjZiNMPOf5AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=nB-zJk0oDSbg2Xo5TrHUnKGO3a5Qj6chx2vC5mhLPH-u0ezWGfZZm6gKXSuk-5BuEpbTIY8m1ZD6nLtTCMFGHJSOMm8yfwkyzuzuM2xi2VvCM150s_zI6pu9o9zRU4is-p4xQftTWY6JZTBqkf_rZnnA6OfOayNwcBQlcVHjffmwk0V513n_9HWdI7OcdFLAjz1o294tG5osDr3Rh9nnRi7rIrj9veQ9u7OYINt8NPSs1WxGk6dTsuKG6dtHO2IdzzkJ8RH3KvfOO532KaUcBwaQJyKvgLGj9dOkSV4jnxjblAhp01amOXmlnKWvsCQHPrLRFf1N3fnTY_w0xzJEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=nB-zJk0oDSbg2Xo5TrHUnKGO3a5Qj6chx2vC5mhLPH-u0ezWGfZZm6gKXSuk-5BuEpbTIY8m1ZD6nLtTCMFGHJSOMm8yfwkyzuzuM2xi2VvCM150s_zI6pu9o9zRU4is-p4xQftTWY6JZTBqkf_rZnnA6OfOayNwcBQlcVHjffmwk0V513n_9HWdI7OcdFLAjz1o294tG5osDr3Rh9nnRi7rIrj9veQ9u7OYINt8NPSs1WxGk6dTsuKG6dtHO2IdzzkJ8RH3KvfOO532KaUcBwaQJyKvgLGj9dOkSV4jnxjblAhp01amOXmlnKWvsCQHPrLRFf1N3fnTY_w0xzJEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWn5YHf_OpEdaPcExTm5d8WYSHiX-EXeucC_4j0AOW1vwV6IiaqMSN088goZjHt7i6E-mEqS8CnGsZTX8tz2TbP5kUMOiAeaU1FB1Yd4FldXIYxH7LtrcGIZlgu6_dGc36-wce3KSv5tCbsGWauDE1Uhiz9csKGUqPQQRuXCTlnSR6ExhyhNrHV7MXWRWAbRTHHXlPjhKKJcM2Ttsr4-woUeI6MdGtB6eUpXOXolAunCaDsxqmG6ncoqmhLblcSdG4j6DMFQ8OJffRtgDINidXmNwedS_QQOwN232hC_wlieI2jhQWvKoFAtzytwK98z3FTWhe7vHMcuWC3TmQpi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLjRY9lDRa8GuZmLrOLXEJ65gFTCK00xZYW7P54ZoNttvz94RjYnSXqJ2bYeSjrQ9Yq3yLjDSkc46MOrbo73QhZJ1lM3vsxJJnnausaO6YZrohUgiLW6WxBlZwjcMu_5bNb2T61jW5Utk5IaIyKMsW6sgOQhNZTUP7gfw2GLMTvuWwVJaSGflAVcuiqypzAyco37wX35iYEkTjBfkjcxMtwG3ynwUcFmE07HccHoIwbu0IPJ_ZJfOJvP7k5w81tFFzyoZMMBU_F41oibd43jFeGTwumvEz0rIbj32stMaix3hCJ-dBQB2z8ARIg0CeylmFyQ8-fjtQWmsQkm_OG8wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=RDuOeji8Gcqs-FtpPoYmvHblxpwQ3sb8BmKpnP6xQW4CeHDFHTDWKvM_QvvU7eS-HTpJ1pCaMo_UhUDrLz4YmljOcYxDHomy5Smsc9iTImA4Egq4Plj_lnIUcJ0WVfMDoL5RKmGUEm0N8ArUDQtkZl8tUr7QnnT93RUNpzIWbViFTCp-4YDztCcCId2kqGUXo13_RnvV4m7toB38DyHhcjWT62RBbvVe8Kqq4Bau_XT_GrXrix7jo_MkkXpQM8vnxVXbG4SUmF9yGUOktAgvduQSId6QjRbtdOVyjNsXun-XwGyQ5WzmiQVwOIXtZSauc8VguwSMLMaqj5EIFyj5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=RDuOeji8Gcqs-FtpPoYmvHblxpwQ3sb8BmKpnP6xQW4CeHDFHTDWKvM_QvvU7eS-HTpJ1pCaMo_UhUDrLz4YmljOcYxDHomy5Smsc9iTImA4Egq4Plj_lnIUcJ0WVfMDoL5RKmGUEm0N8ArUDQtkZl8tUr7QnnT93RUNpzIWbViFTCp-4YDztCcCId2kqGUXo13_RnvV4m7toB38DyHhcjWT62RBbvVe8Kqq4Bau_XT_GrXrix7jo_MkkXpQM8vnxVXbG4SUmF9yGUOktAgvduQSId6QjRbtdOVyjNsXun-XwGyQ5WzmiQVwOIXtZSauc8VguwSMLMaqj5EIFyj5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnXlhUJWnzNlBrJPb21QDEMWvoCdg5BluaKEXGq7GTnMmEQxEe7iWROJCuf7r8nmbzgG029TTTcJcZJ9v3cq3neHrE1mqCesrc59g-X4vdZFQIP58vzqjacoKpvHfQpTUSTO57EXskVieHSybWu_sRE-JysVQMUWwGotZzD-c0Lxdn7aUqjm7quByIOU44Cj4_VU9nHp2OC0Z4v6XeCWSvyMLo49_CbdqflwUS-p85MLWgMcVr6UTV-2448MWE_me4L2NxKbH4D1tJADfwxZ53HkQg_iglsjHfHK7896fz1mKsWzkW9sHlGX53mFnlWfrozPJVQEKUufPeo75_Hq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsaicTcNbQGuTNPTBGOhXSwX5BSEPdB0ymzlZIJxN4h3sCymFKdKWPbr1L_tUpzdW8eInhZg2-HZaLxC4SjrzXfFMQv1KSMvytu97aEdMf1q-CN56MBevzblpXZL7Urz6pHNqm0gLGwSUGdLAiCnYrzt2qXojo8_ZzOAnbBmPfTqyv0BjJ9OyenXACnhJ5dvJIS37btX-HLoN15qrwMEO_3o45faWUpHl0cflCdwOwqB6Dq0n8Imljcc2lxJymoieW84trnPRoDBjeArP9Rkd7Fc459l1880sq1rcLIgtTEkakOS91U6KAhiomurPxb6bJdlLMSY41gFYSGoD50oPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXL4itSobVe6vQ7CZT40DKpVR4G7Gt090-YbqLIXcqVF90EnSv9l3AclhXv0YkjYRvGq9Q46ZiGzY_FHGss1W7t7YAfU_Q03pIU5v9etjd7hfi0HU4aIuBuAgEmMvuFQgf675EmrjANL66Zm3fRvwqeidzHoSpF6eXRfuAPfjtVsTRhja6w4opIpluWUkEj5BxTLOUHCFEmYMnLfxOVIQZlCKoJkca-lL1pNCYnYaUa9zNWAkOyCd8_9WIlpKg8h-gp5jgTjH9HS5H5ApyZf3OmOWup5chjbQisMxZXqkPj1p1gM01s1WqN8vWNLm-os391ocDq-yXTYsv8rRtedCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqI0nC_E8J4W0dGyWOB05V3ruJ6DHN09U-klwDrAx_x45O9Nr1MM_oawUp33mtR2Cwc5xuIjqFkrZ_pMmN3cep2j6fnm9YdtSkeG5Gwr2BP8UZxY0YbGxEV7gbS4h1sbAKXW_aZ_cF-Qw6XI5kNHsIdHbkfnbwn3UdX_7lHX7ZJG4cK8EUCpnwpimS-Cpc7dEkl195Wfvm7VwX_FwKX2RXGVUpygTfuTiEzNKpZKb4IWmXCDGUy32pvsLIKGiYfSfDiyorcus_uU4DPfs_lD6PSXtGUOx3UbPJ0rohHP5Szy9NzufbyIjdvVnECXJY14DkOmE8gCfXoc3P9-TnybPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMEcmzME-BT8_JAZ-kZvHAxGhQXiwC3ZnlpFcPfPc5_x9kyvt9vvDbhyav0ZPf6sM_ir3Er6zHPrG6jHyfNc7HSmghUp8qaaSO6sbhBCkuQ3tQc-l2FBflznu73sA5pvEKiLsfYYCCJ4f6lLA5fHfHjzm9wNMou8plCl9YY7sYhg_m7n9-1DghxavNpIcs23qEOH5wgL-C7ek8DBbwcDmRH3xy2RmqxawAO3sVF1EKPxTOL_CuT9HKwKxH1N_RPQfN3l44F8fLV3nIeANb8-Y6gFmbI5GChFIpj4OF9YkJB9SPCdVf5N5olQOr6U8r9FqmOwyhL4x-r-GyHqcEj7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqv2fe2OveX8I9D6pSlVktsfqN80K5I2VjLqPH921w93jNQlN5UsmGnKywA6xOVZbxQcxzthWtQX1V9AWf4-yux1Vb_D__cpl9iC177yoNX23Tstia833pG-tJekHk95RukYweiLZU-usxs8Loas5KT4EAzx05h5Y0CaeiiEb2ejaJ2sE7KfrB5j42LBR7tg0xcOpaSs2et9LpI42ymoVOw-6XGMUF8A2pXnM7IUz0Y9iScMEuUs4QtsrPXawWuki4hBUOE1c3ljO-q-F3JG5wG5a2Y5JGLDSdm_-3yLYRCh7aNGx4Dpp0zlyzMOPuwWy0SpqTGj7KxtRfAAg70_6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcYgdfnKYZzrQiA3pKO8sOHO-s2f9cpdR_yKtipk_0U1l0Be_jYfAhy8PqghXIe41wbqNYq8Hhh-ctfRMJMxNWK_Ue8G3kQ7YXup6PKPKKroKnvhrix_fSKrawhTY6rPV2X3Eb4TkhrzuIgIvTRzU1iMuuG1cWgRo9VARU12auzlsN7A03ZkGzqgZAHD-XwYK2km4YTgrvh7goxKAXXXBq6DW6WXofg-GgcNbbP6MfeIwMe364cD4itLiygHIP0U7zDm-JDIphK26ivmJkUyqRS3AvP9rIteFDIA-p3nshHAhxnadAtcwEaFecSElLqvYRH6Q1mMiWOWOPcX9Az6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=TaDwYSY4vWuRTdvRd1KAr6gjZnH35UJ1MTT3XhQNR8NDQYqIL7wLTRmNzY0vOjzRb0pooNY9OiPsA1H-cdbiVhJESa72mBNN1mStFHqsKiH9ilEy2tl6KV7E71WjvwkVTb03u9BuRVM9Lltz4avpk5xLyX5V7xuhtfFf_NHbn-1EVHScG-KyKZXb4H10R3BU24NNzgowU6VxvxD1uCwyl8u9TXTMZw60r4hhnzvmtivxrtx4IeN0qGJZL6Th6P46PFuilMDr5WlJ5Aic4xAQGovSHQk1noUN4J3rkMSBR2pI7zea3wU4NyH2CtG8fNSeHVXFxFalHkoT2ADU3uzGmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=TaDwYSY4vWuRTdvRd1KAr6gjZnH35UJ1MTT3XhQNR8NDQYqIL7wLTRmNzY0vOjzRb0pooNY9OiPsA1H-cdbiVhJESa72mBNN1mStFHqsKiH9ilEy2tl6KV7E71WjvwkVTb03u9BuRVM9Lltz4avpk5xLyX5V7xuhtfFf_NHbn-1EVHScG-KyKZXb4H10R3BU24NNzgowU6VxvxD1uCwyl8u9TXTMZw60r4hhnzvmtivxrtx4IeN0qGJZL6Th6P46PFuilMDr5WlJ5Aic4xAQGovSHQk1noUN4J3rkMSBR2pI7zea3wU4NyH2CtG8fNSeHVXFxFalHkoT2ADU3uzGmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3amkVd4RJyBnswzkKcEBFpZZ0kwrXEHx753rQGPZCJR0p11Y1WYS7WPQabgY7fE81lfOk51WlC9mZuRYh6Cc_39-BnWXbLhsQ885t37G8zrUVO9-MwAbVdM4LAg57M10VNhA4yMjWRienSIOTEDkdkdmNllb95eAq8PsBSNzqyIN7LnQ7v7N7KpmHcbz_TtBNy3_ycXDj8pZ8Wm6pDfIepoCtUIuwG1PUlL5yv2tVVbI-EmjZHbFryrAt1p1g1GrvpZ9z82NmUtsAlND2-3ITu3C1sKETkyzQJH6UN68SYSur9T6cS9tjG4s0PhAbmZK0Sfh7nXKucasR4HbCdr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=JPPFrS6WvxTkJpFs968u74YpNkq6vALnK2Ug4REl0lACK3j64iBS_g616YEMRNw-FSF5m-nqK8Pvh0qM7A6VJAfIo_iy0pQ3Fvd9_GGksqjLFTOqIYQIZxo8DZe0fI_fzwtN4AX-WCNBq6oxno_KdVVRNfb1wjO2JMpnawnt9L-MGHmMifjFq8Limwyb5UyWawztdm0z1yFUQr-Q_G4aiLKrghDZPG2B-GnbrTE6KJESylDfEdjDDF7QVbVJDgew5AA5ti3bKHamf_E_Wy-N_OimAzU2LiJNfsk8ojE96hHbLyeaebJVwJEU_oH1J7aYZ85iNytzg8tfJe2Fmqkecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=JPPFrS6WvxTkJpFs968u74YpNkq6vALnK2Ug4REl0lACK3j64iBS_g616YEMRNw-FSF5m-nqK8Pvh0qM7A6VJAfIo_iy0pQ3Fvd9_GGksqjLFTOqIYQIZxo8DZe0fI_fzwtN4AX-WCNBq6oxno_KdVVRNfb1wjO2JMpnawnt9L-MGHmMifjFq8Limwyb5UyWawztdm0z1yFUQr-Q_G4aiLKrghDZPG2B-GnbrTE6KJESylDfEdjDDF7QVbVJDgew5AA5ti3bKHamf_E_Wy-N_OimAzU2LiJNfsk8ojE96hHbLyeaebJVwJEU_oH1J7aYZ85iNytzg8tfJe2Fmqkecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=bEXbL0U32mfnOpoQqdpKF2WDUlmgO31q8E7yE5YqBjmQaNJwJtebWONPW8tnX0JkkTWz24_km6Tg3dgd0L0K9TQf33ohNuiLgYmUKq5humYEEzc5GyqA3hjbOSXt_rSJHFm7kKmS2kByiBmDDGwFjXZ4wYZ8hMSkkmomzEp3RwmCCfMSvuVtWW9dJugDjql_MO-24FXZetpKWNTaAKjiiC580tCSMpASre-JqHNKgcTd7X8BajMmtp95Vx2JwieSZ1WF1Sr8sT4ot8TS9F3YZixgN00ZSFnUB8nlrHJU666yxqV-ej87Hes3s_FGe5cSw1fxzMBw12QykZGDlmwjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=bEXbL0U32mfnOpoQqdpKF2WDUlmgO31q8E7yE5YqBjmQaNJwJtebWONPW8tnX0JkkTWz24_km6Tg3dgd0L0K9TQf33ohNuiLgYmUKq5humYEEzc5GyqA3hjbOSXt_rSJHFm7kKmS2kByiBmDDGwFjXZ4wYZ8hMSkkmomzEp3RwmCCfMSvuVtWW9dJugDjql_MO-24FXZetpKWNTaAKjiiC580tCSMpASre-JqHNKgcTd7X8BajMmtp95Vx2JwieSZ1WF1Sr8sT4ot8TS9F3YZixgN00ZSFnUB8nlrHJU666yxqV-ej87Hes3s_FGe5cSw1fxzMBw12QykZGDlmwjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
