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
<img src="https://cdn4.telesco.pe/file/Ra8fXhCG8Sx112UG1xK3ndbrPnrnlubteoA9kIX9bFCitPWBxuv9cu6DytwQy2z8m-m3WNpb5WZmMEU0HziPmwP1uAKW1IlDWeGRqcpfUjuSTqt07kZ4HjnXb-rRYQnn754XMSN1Y9qZjjExYrNsZLkn-t5Tx5yIaCvvwo7ZtkYS7KxumhecxLydi19D5uSFn7M6kw1sUXq5eAHju0OoRumG3wDNdLJKWZxMjMQ4MJNAhHkuW-gxh13zfArSfowCLSbfUq1ouZkcgSKoOOEDVEmVXd4U5ewhYLYRZugAJgSLNSQuV1sNLZaXKOmK4jeHzGbgxWXHh5EeAriwWhEYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 11:40:09</div>
<hr>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3mKooXnbv9QGxvWH4TEwZGDy-2LC4GV6hC_ypGAo_ABT932oKlz0rrdxv_fOqFIIdFfjYaLmWbVNWV4prjauXQpbyZhUIbjbZH8oXCtWSBCwyPO4Tds-qL9HU5f5h7vSw387i95c5j6HbIP5-kAAGcm1554GbBpYCrapQWQgpVvKLkc9_Pd7hsfE_T2kiA649wRYbefau3UTtfJBvbyfLvBdOfJbTz9li4oBUsHR20u39zGUUKGfB9kMM4KkaM0OPsrUz1Z65S-FNCByrrtHLSGmzaXQbAGdG9Ap3eoglGtM7jyuNEdmbkhkBTmjxteHFq1xVaJa6Sf-9YzMQAG-VfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pr14YxQu6ARRgyuXuQk5HGJXXUGi7aujlHEsHmu958hvFPfAFA4St2eNZUlqYrsQSH2T4YrFP-F40jI8-c226nCFA25Q4M1mSajsW4kym5JioDFHoF_-PS09CLvg-2lBkn9tfFioY0hGdf1_xTGb-u01WWNJtKDklBMq-0kk1CqTC4EfGAyiU1vRmF5D2uPgYOXsvetbYIUGaZAbK7FS2V05VRlHuENCIaryDaHGBHqs0JORzpdCujoBCkx76B03UJeLnAbBC3BWyjsFi6pumB-aAMAuNmXYrQ1Cp6hP0mDqlo7DqULg4bGgZlv_EVQXV66NysSZCeXAr-D-GZye8Bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pr14YxQu6ARRgyuXuQk5HGJXXUGi7aujlHEsHmu958hvFPfAFA4St2eNZUlqYrsQSH2T4YrFP-F40jI8-c226nCFA25Q4M1mSajsW4kym5JioDFHoF_-PS09CLvg-2lBkn9tfFioY0hGdf1_xTGb-u01WWNJtKDklBMq-0kk1CqTC4EfGAyiU1vRmF5D2uPgYOXsvetbYIUGaZAbK7FS2V05VRlHuENCIaryDaHGBHqs0JORzpdCujoBCkx76B03UJeLnAbBC3BWyjsFi6pumB-aAMAuNmXYrQ1Cp6hP0mDqlo7DqULg4bGgZlv_EVQXV66NysSZCeXAr-D-GZye8Bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H96Cylua4WSBm4lBT13xREJimfg3cRtT9ijJRN-QqJgwBgdrpXxKL6pFEYeYKlusU3G3j7TWGtOZS8IVHyxmjHSlU9IBEgTsAf7oxG-5syrClWWMLP8FLTXzeFoa47Q6c0EJGDJDUApE_XYa4MovOtRTh-DBwP8zExW83iTxg0rSNSz9Z4hYHcgPy-2o1yau1UL32N773jC-rKGxOWXcOcCalI-hR4lzfe0CLDYtfP2eTJvbtGGRGJgfQ-GJAueUUHltKP5kJqhIV69OrzA60BH0CTCiln-brGwAsxI-uOozp8Vh-bNkXaYnXbQ6ogJkfFTdIpRdJYpMvGjQNW1UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA5T_yyIkebjp6zSipKKrT8OrtsARS3Y5P5UQqsXqZQdiUYxeR5CtUu4thRTL4RJ-PpZUXPH3oi8t6WGaL-o__k5KAk239Sr0cRS6N_A67wz6CQ5QLuiAjyPYhVquaCpI0jScD77iIHFbv9B_f19iIke7L69Av_aIm146MFGdq52s_q_efk0ScjO2Zk2xwj3DNqbtKKta8irIdWWL6M4hCSOhQU-zAjFdJs3BBXbdqqxV9bEAQREoyv1L_ivy_3mXJnTz5pIuw1ToIt6VGyo9tb16ruMYyJGFeginwdJO4UumNet8L70YdScmwGYToczalz-bJBTIWKZtGIlXg1H7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgB70f83wMcZI9_4g03DAjtJM4pwxopGiKFYMpo9Lx5XNXYU-n0q1EwEUbA6gsF5x9JdJBEj9QJi3MaAD-Vl38VCIwH39i3Xn_RWGV8YG08HRhAo3Ak5umNP8323upahgOb_xBqB6ELR-VCIGHMDUKiIH_yLoz35LHDxoY2SWBqz8xqydf3_dswToD0O30FLcv2nXl5AteZoZYHV2Cn6u8Qydq4d1ApOhtNv-5x2-yAEANRvyna1wZFDtVPZd88gEPucg_5cJi9A-1bb0cl7kjCyL1PzILzOfnrcYlAMChKOR29fCCCf8RjiuVEBmAMT2jqI1q2yhwSQRWDykH97DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0hrpgP2qc8Q8eHJjcU_330zY8EX60djF4dKkKVeNXCAkJZsNyF-TXKDX6XDnXK-A1YPL5K-0o7tgCaX439K-RE1qyqcXOB3lUc-wmxfDWVh2EwzxdxJXihCJMh7BMAJeTUAUCBCAT7w2wFHoQkAqVNI6JFCjB0IWJYmriYYWs-yerkY9TifcFTI-S-5C3lm2zYgVuZ0Y7XsEgNFzhdd28Yvjn-Yvosc6VTGKR-vm_Mi1IZWNOaan8BmID21YG0MVFDxCMaD6kIT6aSz3O4CXmil_hD3zrLPU9-X_o_4yuvDd9gI5myIyzm31UeE3EhGi6K6pnQdFt_r39K7FJgXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfkR7RSLNXLpBCu_PEMuiSrVMGNseycrQsuY7NcDDS6-sSlnTZ-HcYkkN-3w7ofVFDp28NllMTGIWhYNhC-MMTb0MiAWc8Y1EiOjFJMGzcyN_tyzIDbs_4Ek46F51W79sstCerFdKbVAsmxiMl99h5ON3Q__3O-1kWiiE-oGv4k3oOXk7EDk4Xku3Z8LT95eB3NbSFALy6a3_il9bB1Poq_X7wge3bH7kOTQhYdHp9O3zRaL-SdoL8PxyG6j3iVuhV9k4pAoXlLe4FUqy0hdUuMQkYtPeXoF5peillTjf71shR2ZeVDpwjTuYrAeMASSKKSYWChj0du3eLQ1RqJ_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlnetxUD1HF4CBUqNcc301Ka4vbvGo1FZlR901nGeSGs1Y3d6fERTjVB5Au5Ds_27ZMMApbaIvKSqF9KKT4C_dD-tCA_o0Upd2bS5Evu4iATwUArV-38eEp6Vsn9V5cns13xdJt5xBMtXV7F0lw93O3rT2oCf7gMF_ZscyrSsttHnUQzkz6XVx44EYrvVhURpqYxRScachftcP4aU4JOqxmjaSzZeslzUWCB61v5I2nYpbofZXpviHNlgfmG1wAsGZN3RS9Q9mXOxoWF57PdhWFx5q8v14ynawqej6baz94WcAQaHv556NBOhV4QJST__hpNryDvse09z4VXiUNi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGiQSvE5pi4DRhVchs7NsxGtbRURO1fMOrBkDStj65BLqkGPeIA5jh_X3iT2jPdiSxeZ_pKUpYl9sS5s8VQEM9pw7fIfMuMJLcLTiiqL94PB_MCJuRIDLRMjEI7IGC8HxCLZJ_uWG9omMdt9TopTxuV-ND0nrzVsy9oT41_4RsqYYIC-jJlDqjPYIqRixez0wOvOM0IXoplUo-0kL2Kbzfnp3Ywf7zu1WRMKWLtDyaDt6o7N_jZmxrbyKvo3BD9csj_NmuwTfN5MbwAkxyE9h374hSBcc9VQ7N2_zUh2AP-cRl9F6ie6VavzoxETrvIad43sfI21dUflk6ZYwB8U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSH5U9RUBqYHO14OeSQlSPrH7OvDqMporRTz7gM7_3ySOjxOpOpBMFjrf-IfiMTGihe9KE2qS5fm0G8rxfzL6O0ENhqNEqaIdx0lOUIZFp_9_oqTmxsvlDpuSjeQc25fpfODa5ooniMPSHTGRhXpx195ZTt_40JGml1r1Jq160zPCnwiQ-iqp8pp0uakXnHavdh1nP0dfoDQfDtuezupvvFHKA_oIdporp4P04idu5H0YYMs6RczMl0LZFmVqrUEN0_6XQ-DsYqitS9rv5lyCUWa0eMPyLoMmCC5cB_JVcX_IgKnkmzxADzD7bbDvjHI-MkQXKK-M7nsrX1c64zDXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4ujB2C80sNDr6eVn2VLrVvgMA6SVENbFcSgHDeIVRIKs-Zh1fuBQ37w4SVpyAF8kXQe1YIVKSaiIJE6a3c070AIN9RwgyhIR2HNcTmMHT_FpUfoWs_8nPqrwJS1PeQ0mR9M0s6wZV4huXiJDahBmqxMfl4hrBWEkH4S13TDdaRfwvdV0nN8LnezrgaFcCRrZwAokKC15gdkkc4NxstmqK84ZJsaNuXwQZ0XSknK6GviE7MtkZmP34Wreei2MxFw2M-_OI4PKalv7vMDp9mIyJyhotIC713Kzuu3OhduTAavfHDCX4o733IPFVoTc6K3A6dgeTYhmmlQFkAMrEQV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dij4HPkFWz5yo2BzG3qMvHDsOye_Tl-7knidqbjMHFISFH3GXybjTzcNH_vaDYg9lawPZuF-1jnDUS1zYZzdLkzvEiwJz0-zQvhDWgc7D6A9d8ivTeyJBwfOswjIpFxxHeB20plTwdc1LKiHuYasJF3bz80MmkVUQE5FbuMTZVtl79L0qXtwlblw9XTZZsZ8mf8VcAwbeYhvhPOD_M1BN-wXrEtCk8YxryJXNaI9MacWaxxFOLfD5zPVOWEl7w6MJHAtx08uc2iUuzIry72l6icL7RQNYwfGdm7_IjZwmdRQ6SmPY0AAlLvL-1D9jvJaLeuSfFufHD8XnvuofGvZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3vFvjLnESzarGDiGKKd1HYyJSv-LPubxHeCjd83ldnYEbxEJBNTJL3En84Or3T5xh7IuN6fA-_V-TMd34bFAsGE9HSkACEBe8Wenv4Kwvzb0A5bhMGsSVwbrhktqZkRcaufJcaF9K0ACobeGkpQiEqH56zAP76coJDS5WSAn1NgOavkDoH-eF1c_le7I0xMJMbZKO69JicyI4GfSmu6ihnZlijLJ1QmMFBaEDPRL7ALR-E7ODPPIZOaKKVEbpc_IDbHOaZPqislOTcFFTIHW96tsPDiMq-Nv6Hzn8-6VqycAY3Dwb40zx9WhjL1fWYHWO-Wel-guSfdE_fYgg0XcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4laES2g-CYO9Wg-rbO8K-lKX1qavmsuUMmrzZT3HECfZC5iHO_IUqOaG3uvOzcJnmztFjwic1gw_r0--bSO788J_B7lANKUxoWNC1OhWtUyzYWdtMgvWkJDbw0LbSXRWAT33aJ9qbW2l7NsYn_LhUKIwUEx3MdBtJdDmxEGkAv15QD6Ak80Imf4E3IujOQeQ-i_5XYq3FNVFqS9IHgZ3lhe55S26zUKaVovuMcXtxwH5btKTIdLyWrd82w2LPvAepW4bD2-YT4fW-8dvtMpTZHuMVtYt08PMzB8N8OoFrRAl0VmpoieScxZBhCyyzYzT8fKP0KCF-DJ_ofyWcapyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYRda8U7WODjW8QmCZuA15PmK5NbYhShfHKzzX-p19Kgo3ZZ60SNj7k2hJWg8aA_G_mhMmU6Hl57DPrO7ycdWUvU-jGOmWPEsoSQGmrDVakbg2lnZclWVA6eIldcvzwu3B-V6axqZZtlMICD-3VmBLskox3IkGJ7rxQxHk6I-2a-E08XvmSGlyoQhFIqhaaDPstQQZX6Bofjvz-b-F5a45w5NVWDN1k69l_dk6WlLg279SLWuBw7uRYOXmo_LTArX0sRpddb4TRK2RZ5KkuLsL41RZk76zsm_HIwusivfibJEkvr9VxzcehVDrMIhOBpEFuU9LMjaaE5lBl4cUmjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=t3dTD-z1v11hdePAnVLONAWtS-BsU7O-CKi7-KINhx1Z1qIzO7m7qvPdCBo99PNQonUeV1DXKqjaXhbmCHngKEeh8xWPD-Ccn0axH55tCl9PG9hEqSlBijtYJKq9A7RQ7zI2n-SlhlqOoSIapUfvzP-hfSstvbb9atKFMSsa8tz6N2GTH_Y_ZD4cgJvFTLxzm3U9UNaTUoDBwN7JjIWgXANayjmZMRZbMrrSUbkYjdbcuwve7NAMHL_LJRc8Kx8dmBiAC-DdGaH5h3Bp59KfaKbcptbnmdg-EryvhtB5Q78CCvmE3i_MmwUD73YUaZ6tf9DXHXaQi6e98h3hR2hyrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=t3dTD-z1v11hdePAnVLONAWtS-BsU7O-CKi7-KINhx1Z1qIzO7m7qvPdCBo99PNQonUeV1DXKqjaXhbmCHngKEeh8xWPD-Ccn0axH55tCl9PG9hEqSlBijtYJKq9A7RQ7zI2n-SlhlqOoSIapUfvzP-hfSstvbb9atKFMSsa8tz6N2GTH_Y_ZD4cgJvFTLxzm3U9UNaTUoDBwN7JjIWgXANayjmZMRZbMrrSUbkYjdbcuwve7NAMHL_LJRc8Kx8dmBiAC-DdGaH5h3Bp59KfaKbcptbnmdg-EryvhtB5Q78CCvmE3i_MmwUD73YUaZ6tf9DXHXaQi6e98h3hR2hyrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTuOVQDgJ20zwxKwpClvJPMDv6XEloNtVCZuWCGdboOQnugU3wxloAvazR--rxOTTbedOfGFgOKpsICQ9hY2H3aamrG6YyT7Ho9JBSbfAFGEBJmBBUdCKaBZBGvaElGiZ4sjDFKTGkAHRcdDJNA3l13QOEiWe09CmJmvkUtH8tdBhayAuMrsHpmWcR9HcPuNDmXnTRgNS2yFtT3i0kRQ8mI8OC9pGFHKHwbvo9oP6KQOMcU6wx2LWh3MTayHKzW9tCkEvcxtDiKce0Nug11zfp_oAH-VIsbTyYdzdkfFmMT0BJ8BcaTGONDkNwJ7YpevD9h2nmjavduc9Gv53RVuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=dk-HJbv0-NYiAubjCfgNGlzWhxifCxOMYgYbE0DlayAU7hg6khvMbZ9-qeIgqefxOGR_hzPEOBD6A7QoonHHyWeaYIYtjNfHmq3xFByZcOJsn4mG_SSL7Ow67nrxrkusBhZt6D0O6cNLGDDx0G7fuOPPIGSe6D126uCRZDaEeJYKzNd38SDWZUzPNy1kSFBfjc2BaKAGEuyrgjdDBTDpxiOG_w9JkYTAbT5nyn8Rr9RTYzSE8Je_8NN93PjSybr4lP4A7A4aPGWZAwyv_RjjTeuaJ-LSnS3rc7rmNHR35LcPiLyW8Kzeu-x7U7Mfsgt8oM-LSo33hZ7XdaFYukiyHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=dk-HJbv0-NYiAubjCfgNGlzWhxifCxOMYgYbE0DlayAU7hg6khvMbZ9-qeIgqefxOGR_hzPEOBD6A7QoonHHyWeaYIYtjNfHmq3xFByZcOJsn4mG_SSL7Ow67nrxrkusBhZt6D0O6cNLGDDx0G7fuOPPIGSe6D126uCRZDaEeJYKzNd38SDWZUzPNy1kSFBfjc2BaKAGEuyrgjdDBTDpxiOG_w9JkYTAbT5nyn8Rr9RTYzSE8Je_8NN93PjSybr4lP4A7A4aPGWZAwyv_RjjTeuaJ-LSnS3rc7rmNHR35LcPiLyW8Kzeu-x7U7Mfsgt8oM-LSo33hZ7XdaFYukiyHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs5ufEoiABwwpquYAWCmyPGFNRRIraGIarZB4bH3WGo2q1hmemJAtiriehufwqYu2XxxmfBEwA_1Sj9YwLQ8lR2JdX5kcgGSh0uNb96BqTbu3PBitOjZZGcjnmWnRSbwd0P3HGu9l_61jj5d_UF6lNBF3CSxu6pyv_e5tTv8pvgsD7fUTz4MTCLR-DzhO2gnCsDiKnbfSHczOjf-uam1uWzvT5yfZwGGhEVv2WhwIIHZaTNn6q54tmOQP63ON7jRChQmt9jRL5jY731hrxqT3GNWsYjqcUBVImpQFym2Il3clhr566fvn2Jap064j4RkLCEfuQkOarKMAzb-Cgu6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCQiiUd5DJP4D6vQZosHSw2d9aADl0uIqHUPaAhw4LFbF_rxdmjyxCrkIYZOT1X53OhH1mE5YaUwZcMhDqphjrWt6tN0F9NkKDEw9dkzN0UC8ybGVlFD1QslaAN-k0BXTPQO_AMgCZ5n5t18n3MRt4VjyolrAJ0gd8xEukHJyCwts8UaltPFC_DJ5UVTkxWMB7G-Kzu8cpIVwJVynOxjgkVq7AEDBBl5wQIcItyjNay_EfGA9F-TvbcpRQlPPhXgCpeXeAUTdZFkLRYe8nKbthkV18coooLaVFvgKfNgrKqF_GXU85JAUbWjjDWhbd5YRSzG4Fy7OdSw80V5uViZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=AiARJXdNY4YmTgPjSyaR2sktgoNui-8s7gzTsOHrDu5MIoBW97DVhBayVAoSimylvSd3wZMIoryp7hpQsjjKixxftRs0HXLvgKYHeMcN4FoDXZeFxAtZeFLjb_vuj0gpnP-dlDYJm2zlBiwKlTFEyqS3n3orvNrF3boTBkF0QRKWqESPQVRVpzjbsaXF1xXboXDR58iZUFyVd2eqQ4WL6L6zBsmqqPWhySazhuImE5ikRQqBe92ztElo6jIZ6mGnNe-fsmNHzSJOVkDbTM3Usk3NwS8NDqejEsqzW3SHqOREpa3jlRCgAcrnfwa7rYbqaUzK-o8ePPvSXELqfMuNJxHnUhLc0bKjcvy8uf-vGlrNWvplKFCadIl8xud9gk_zgivxFpzOiLoYJBpW-8JGTGWvhTLcC-jV6P0pMBOFCl2LEDN1rE8FG8IpHl76pmSuwcUj1v6aIlkjDchMDRQTRZbZe1klXlZ-FrVLZ6kuk4hpxoZujlncMQcJfrZWK4HSeOnsKf7aHc22kxzpzziWEuHfJqIjVYToVjxuKVqTu1X3Ey1JjkkLScNQT34uF5Jcafq0IkYstFZ35AgjbaOTI6JehjdMO5rgRsc6tHLnGOCka6DapbZFQKLkPrvrDyBkdQNXG2uh0BIxpOtzEXkg0GKOgUOxGvpewSAVe1z9-4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=AiARJXdNY4YmTgPjSyaR2sktgoNui-8s7gzTsOHrDu5MIoBW97DVhBayVAoSimylvSd3wZMIoryp7hpQsjjKixxftRs0HXLvgKYHeMcN4FoDXZeFxAtZeFLjb_vuj0gpnP-dlDYJm2zlBiwKlTFEyqS3n3orvNrF3boTBkF0QRKWqESPQVRVpzjbsaXF1xXboXDR58iZUFyVd2eqQ4WL6L6zBsmqqPWhySazhuImE5ikRQqBe92ztElo6jIZ6mGnNe-fsmNHzSJOVkDbTM3Usk3NwS8NDqejEsqzW3SHqOREpa3jlRCgAcrnfwa7rYbqaUzK-o8ePPvSXELqfMuNJxHnUhLc0bKjcvy8uf-vGlrNWvplKFCadIl8xud9gk_zgivxFpzOiLoYJBpW-8JGTGWvhTLcC-jV6P0pMBOFCl2LEDN1rE8FG8IpHl76pmSuwcUj1v6aIlkjDchMDRQTRZbZe1klXlZ-FrVLZ6kuk4hpxoZujlncMQcJfrZWK4HSeOnsKf7aHc22kxzpzziWEuHfJqIjVYToVjxuKVqTu1X3Ey1JjkkLScNQT34uF5Jcafq0IkYstFZ35AgjbaOTI6JehjdMO5rgRsc6tHLnGOCka6DapbZFQKLkPrvrDyBkdQNXG2uh0BIxpOtzEXkg0GKOgUOxGvpewSAVe1z9-4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URCqKHQ3T6kIqGXY-SGz4vvxUr5RG0vZbWEJH43amAklYdiRYNhDgxVebt1P2E24XFFcxq-EDScgav9_Yoi5z0Tr6ZpD0bz2MEeeadC3BGlBFbFVR-KqSX3vY16vMz9uzti1C6YBm0k0wLcaKfYexS9xLRZhAi66Ua73rmqlrcX27XZbbDOBGgpIThexojzulwiw7m-6VeUJ82QX29biILJzRRdzD2_7noQtZaz7q7iUAGb0gWXeN-wAEU_2BaeIJahkQ9fr9vVnqo9izPbNLtfMXTWDqVA6SZqrIewEKkM94N6qq0RIKFSDuOgIGpCPo4LxjO2OljawC7PQLagvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVPPquRbmd1dxSG8rYiNUT0-Gj6PDkPd9VkgQ1uCb0wbGmTLEBLKNmqW4LOFZdSTLT7qCuBrL28fy8SqmfnaP0uhtAZzVmJ2xOxVV7mDu0Lait0Qir_lTbvjhNSKlIOoccT_eF4oVqbKr0Z8aiHSc28Q-SL4DI-z-JstpQixHiJHqp7b7rD6Ca6eeHabMUnJURqKTbCzYb08esNeFV-XWlaNV6Siv8H5tGT6aKOh3ZeRs-y4podMrxpxNrpf4Wu0jK9t5FAjdZkcfUJYJDDd4h_Q3UfrTphSxvi-jVad0IXjVaMCnUCQFNq1SsDhAqRQO6bhdUQVyYYJ34SZQs8jWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofI6FOV8jAhie5dfzAufdiS0NgRQ32G875u5M7zGviaEJVZGxEipubAH-KUZNGLTY91HyZRWhV-NGmsDKrM1wTE9bQ931xxnd38NtbE0Lof7Nmuv9wZJ4iixgQlZp6aQUlk9I8uX4RUBeduiWQ3Cr-xyf2PjOJBsjNBQtaFbmsAot8J-TzjWZtO1oyICiSk2eNzcQUJq7l-vqjHtfvkWy54Wqvd4a3u_29DCkXz-_cV5lTGgbLEIftTeXbgPxHUMSPiFEA78QMfN3-dLyUpgXJZiK4udth_1GyebX1J7YRJs7cjoJAkiVITho32ArK-EB8kK08-BL3do7DGAwmp_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=gh6vnO-0fGJjOuwEvtKl0vLgaZxZhA8efAnQRTszMKnsLhiG9jEIGldkOmRGVN3lxSE9fic9aGswWRzi-xbtuhaCYLQFN-NmkiFKhwwwLidZwuVQJ8huhIwIea8QV_S4eYAzrWBbiiihCbPx21P5bBebCOgyIcH4c7nS1b5WcNUdqVSNTW3gbwPqk4b-4Sg_-APYlk0Bvuzh-Eu6KcGV4LuUgqGGnyg1k5tT5QvmY0lyYiMuU78xNSc2pT5SUNyX2Dx85UNVWKTQJwoZcHYbCHWmH7PIqDir1R560jhvqJV7YGyaP49CmtS81TjVCJ7PRkqj7QvqiKkMraCmr9vVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=gh6vnO-0fGJjOuwEvtKl0vLgaZxZhA8efAnQRTszMKnsLhiG9jEIGldkOmRGVN3lxSE9fic9aGswWRzi-xbtuhaCYLQFN-NmkiFKhwwwLidZwuVQJ8huhIwIea8QV_S4eYAzrWBbiiihCbPx21P5bBebCOgyIcH4c7nS1b5WcNUdqVSNTW3gbwPqk4b-4Sg_-APYlk0Bvuzh-Eu6KcGV4LuUgqGGnyg1k5tT5QvmY0lyYiMuU78xNSc2pT5SUNyX2Dx85UNVWKTQJwoZcHYbCHWmH7PIqDir1R560jhvqJV7YGyaP49CmtS81TjVCJ7PRkqj7QvqiKkMraCmr9vVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTdzBF0vO5liI-IeOkxrMTDKIRefvEigzZp-UASZdKmC3vXzwC0KHxZF57d4cGvNqlsWOB_vrInEp4nlQtrG9WJ0dcWZY0uBiUdBfo5kvbudezzZxEq2F1sLL0b45RrVqfk31j_B4Ddc6b3DJBlwG9UNOSK_vcjzEoDnPXGx85Rk3D_pzE_zaPbcfMUgXqBwctTMMQ_wtYMwJYuV-0J-iYGgg06CE1ulQwBsBcy77zfyxIXDpTj_8evBDFwo2481P9hN6EhBilLVU0-_S1laWaUkx8kvjouriinxTJts10C02hwptyuuyPFgRrVXMJZBAJ9sDycCqKcNTiZNH7TxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU3-gYkGD464rcDNxoEBHEy3UaRH8oKd_YcVpR2sHCFhyZrphc0zgnEBkcZTevdQFsQpi25j87m9Hl4bjGiJdm8M26vCR2K2MxW-qTHl3c8SDqdRbOtwYENGhSL5pLNYSOm1GBxsAW7dSXaAA5PwYwYW8BhdU7RMSKPHR22b4j1MOLv95WCZJI6VcaOb6PaHibTVdqzkhh9seTZOpv6DVWtP6KD56oyu2P7h1L84hHwRpFpoG0HckbVY3Y4i19JlqqSWdiSH9BnLvZelyqEhU0s0SXeIYvPQFAjSzaPredcFFEZ2-g8xNZzUwxb_iDDC1kMtZdnnUa4lfS1wMq9WeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI8L8j3e6wDdDNsQrHgPirjA67IuySl5oGKbqkhsVuNFGZbVd5W1kHo1vF7BP5pR6_NQTMb36yV_kCPYWH8OnTHcF1tnASnFXPF3g-KOqV5YKEf8hq36otPBNPHoKk686ZgiptU1KdOPGPMsgpyhho6UooSbeaYdQJ079qNMhGTKzEPPJkSnA5O6ekhzScmKsuVXTpxy_y44VvQm2SHkd9FyVPTiejv-7lBMgQ-FU5uQnGSF3kDmC5wFnMGy1qQQHvkzC65j46eh9sfDL2dfysdHXPfenmj8kUxb3KGgR_OB1ScqUkiFSJ69qhuxIKQTuvnpUs_ydwXsBCYIMaiz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKuAvny8M6MR5ejzhkvklWAGgp5r3mcFCeT2pvF0ceTUPQJf035sYkwjwrifBpWJAyfwRR27FIoRsJoxaTaNPrxTt02T-Vo8hZUF2f48UR8TiaPRQU6CQda8cryMv6uE5ga5lx3e4coxhbqW9unrr7YI2gdrGwGXYIf5eWS7LtsHsZ0LWvdmB0wSm6AS-nsx_WoiTqbLuOOLZzXxOL5tkDHcsHKd59iSVRFsEEOsKFDLI2rxyBBW81VgRvNRpuW7lk60FFefNhm3_vQyLXlvhjWGVzgGjMVvucnJPP4uk6ZCgDaXEWEAbuymMG7R89B581Ods3mQbrzaOziZ2iq2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYiknPVKlKMxwY5epuTs85MDjWBikCd4hAbPDXqQsxwXtAXve6evEYQdPxNUBGwMB8H7iQItZrNiV3d2_pJRaCkEpAPmf-lfN0vOaYfIwoSWnOfTl-eRB7KLI2OAqV57LTJSKwJEnlSM8BcV8d5Yuy7t0l42Pti8g78AEjrYqHuvJqQoZ-thfzpbesNqTIp_72oZQ3mylPFyltMQlV8rgV_z3Pk1wA1bErLOXY0c7N1nAaZpEnyUZK6HUMMkbl2o52y-t4Sc9istu9ggUEhgA-fUaGvo2eoeqF9xYVL7nnFHadB0osrHaUuULYqr__H7YWVXhnVLL_FTvLHwGG84BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXgJGlcbUTDIUn0clCND1JfA88QWO0I9dpOOBhb5diVqiF-Qzw0waL_h-uioP-llJ5dYsGlRxTvsarGcUTBPFmujnEfebtU_dMr7jOrFyF7ghbrJNz21ie5FwM82WCVbf43oiZNfO7sYGJpyFsd9OKeu3Z8JjeSJZeYZPRrXqfj44PirECgaggvWRePE0UXAxspw26Mx05J-p4bFkG53G0oLlGOGIjI5vHJ21xPG2bfRi5UCD0eVN3Dbqi676ctAsOwI9aEWUhgy7qtMgCD1nfU-dDN1ufyqheJCrYoFt1iS5VRPPdJ6OBIZnDdnJE4H63STfUalTZLs0MdKij8j0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW7uOE_3yYImpLhK7_sS6WPoYP4dlnBXdMgDSnQQhRw-T5l_2KVhTAO8yEARgI6Y9DrUGuw7KjX4rFd45_f2UloLB3bTzhjACdziI7CKCrEEY6IKnyoX6D26l-5gASBhGTdwknyXeCZJo1ELLSMy05zrZ8Wq_0jkM_mBZ3vZCHKtGpXswG0lUKUecSTNfV24Xrt-kDxE3uRSCzXz73X9F-LyjCFXbmbqdwWRIcn870RheHWDxg-4zBUyZL7G4P-OtpLZoBbKLLv7aoGD5KJ49qdXSqsbHIIqcmh1LlJFti3uS76uhIaC467Krx1BxqxZYjmSigzQsz5LVwFXVaMfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWVgpqJnAL7P6qXIo7cnxR3lMowtCD2Yo_7710F5_uWxyvfo9FvVC9ARQgtJaxyVamD35E_DsGgemOB2OKclRw5MKrD2oBJ0Pa9jn1FFDfC6vbp1NOqc_syFsNV-lw_swnB15W-Ax928dqtbRfnGHqp0jyn0ROqNd42MlZqyCuXdKp7qvtB2hOLKql9WnNblSsxzCObuHMypmCcktaBvcnuiC3beU5h3t8KnIQGX4_CdzEWjUMdjHDnHtXcwQZN4Hu5IUCv97mXi_PmewfTw-bI0BTgGPBwI1feKi7PRGzijS9K2UJKRbHiwfWX4aTPTXVPbkpvJzdga-dJPVJ33lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEFm0h706FAU3xRg8_EJ1qLvr_d1MtjrraWZunDqgS0IOo_7hDrFAHvEafmIZJFg_NXseyljDnfzxzGXYvkn37T5_3M5R_IVuC1LckXzIMyCvRJnJVqChKs7ZrxotEBGjGHpI4zwnspCAsnjE_OvAqpzhIE_yu4E78-I-Uib2FxM4RWm4JrUfGi9iLXfJLw4Ou31Mhv19wR4w4Zy9Inr4XhCJPlPduj5CxA_gXRX6iSKWdfohgVDjq-uQn4izBy21bB5x16dvfByovxa-KXXf8kDI6G7j3VupGFeLBkpS6oqh0MA1EK9ubeVAqtnRc_dXLtVDLchjSEOx9NG20AGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amsX7yPku0gbxnd0TCTrmrNIy9bON6Ep2BGV2nhRuiu4mE-ayoNMQI1P98vf4cjb63Wi3m4o2m8xT6i2eStxKpXRv_6AqsrqUrEL-VMNsrfMvIidzRTIkj00KxRMOv21qwC5Mich5sqWcQwwD5D06kXqFJu_zDYFKM0rqurunehWvAy7iYo6m5eRq1-P234gGt_ZOZ9ptCzZb-7elrok8P3dZQ5xd0MYnG3Snm6zWTrNCU0jzVKji-uZ9GNw0nHRp7kjBIeHJm3y_zZGEHhy83NpGT3T42C6Hk-TReZ82isbf5QMwMX1uGK88ODSlbIE-GT1EAXHEe3nPc3wDIjjWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=OmN11xhuGWs6NiQzxTgecaQ3n8hrll1ga8zd56NpDTrM-7AzxXuobJhnc-TvyedeoLHrjl0elgY4K_NRHz7lx4FxnHNOMEF4wHUxPkAwIxI-gW2LB7vIwwORbf6TMK-oc3Mxd936bNFxgRMSAlsKQo-2S90x4WKOnotmkku193KP-afubwmyhFYnYxCwZisb51xiyME_1sob1W3qQi-TykMMIlvaj-dbNTn_cKIriqdByN8Zd5ZlYG5Oye4RXuH1RMLkh8_K1BehzFKSRwupD74GBtqXpjyxsHsSXNcq7Sik8Th7iD9TOgBMkBnOwV3lL609_Zkrp0Lmwgy7cd4sAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=OmN11xhuGWs6NiQzxTgecaQ3n8hrll1ga8zd56NpDTrM-7AzxXuobJhnc-TvyedeoLHrjl0elgY4K_NRHz7lx4FxnHNOMEF4wHUxPkAwIxI-gW2LB7vIwwORbf6TMK-oc3Mxd936bNFxgRMSAlsKQo-2S90x4WKOnotmkku193KP-afubwmyhFYnYxCwZisb51xiyME_1sob1W3qQi-TykMMIlvaj-dbNTn_cKIriqdByN8Zd5ZlYG5Oye4RXuH1RMLkh8_K1BehzFKSRwupD74GBtqXpjyxsHsSXNcq7Sik8Th7iD9TOgBMkBnOwV3lL609_Zkrp0Lmwgy7cd4sAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=tXbxYwkkdvuYlrvDgwG6iZx-cxHr6Q7r_6LS6CzmrEOENLztdz1b8hVO87-uOayP5jERG7FhaZGF2_1SCeKCmUuiKc4U5Bd9GRJ-wxBSmWuYMqgNYJywC-Kb067cc1SsiTW6WxOx14Q-cRw5p5eWjlvcB8c04BhNLLZSmiSWKN_4Q9QnsqjNLXHRqPsBiiz21cJLh8_THK1OIIPbIi2Nt_SpcF-2Ik9nF6Z3dTzXkhRR7c9gFQVHLQiopFiO_M1wc1hcVwaHDkfYeKNxtKL2f6THjmBDX9fd4tZdxes71kIG5WIiq6j6Ys5YpR84nU8Uf26px_xnJHqqZ9FRY2vm44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=tXbxYwkkdvuYlrvDgwG6iZx-cxHr6Q7r_6LS6CzmrEOENLztdz1b8hVO87-uOayP5jERG7FhaZGF2_1SCeKCmUuiKc4U5Bd9GRJ-wxBSmWuYMqgNYJywC-Kb067cc1SsiTW6WxOx14Q-cRw5p5eWjlvcB8c04BhNLLZSmiSWKN_4Q9QnsqjNLXHRqPsBiiz21cJLh8_THK1OIIPbIi2Nt_SpcF-2Ik9nF6Z3dTzXkhRR7c9gFQVHLQiopFiO_M1wc1hcVwaHDkfYeKNxtKL2f6THjmBDX9fd4tZdxes71kIG5WIiq6j6Ys5YpR84nU8Uf26px_xnJHqqZ9FRY2vm44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YScNlQ8BFbFwBXGFZhzw394j50ZABURBott-m83I-FClcTWWmEtjOSk-WxWUdy44T2qyfDLolG38Ukyl5ImQy9fxXvfi6klEd322_N20mACi48w52cehWyihLUn6iDgr49lrF3Gr1ARF8UXGBOc4Fu5JPwNnJxpSBeWLM3SqO3qaowc6YUcFP26TFFIbyGwFjISUp6FSarl2YfBbNRjI8wT8JM4DZjWOsdnHAmhQji6dcjTIVn9-Q_0DtXU_gbNC4KNYW9RAxZrQLGUm3imYSsLyqTsnmmfvDxyxQmF_vE1J29_I5_8o8I-9JWBZmDcemohL0BDx7EaZk1lD0pitGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTXnd_YyDzs2mVvogr5CSJK-7LoZ_gsAo9DasySC0IFyVKRt8f_bmGYsqAT_Dnu0xVZJ_oq38WotQ8SJdktgUNKkuA4gFPUEFMdISo9cyhydHulP6Dt6fGiyAlCQDVbW4p7EfuDQZWjUAhm7IWoZdKsGqcmjhN3iICQHaNZEeZ5wSe2JVe491E3-QCk35slUhaIUmeymrWwbpzINFZ3Gwt5U6G49jbzvw3F8IdKMcIQ7CnX68IS9v0eZAfutsutZHBM3mzF0BRXqAvaD-jjcleCs22L-BJ6wQYiNI2v78i5HPKMHUYAWQVaIpehfJqbA_WKFSptKjS1exmg9opYhQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCHSNe32AEE9XT6aEY7RiIanKx3tpOrOCvrGj_8OZ7JtaIm9eG2WvFQhvF4PZzwQ6YvxuDm7a-lDPPnmy43HBcIVdM7VK0gZ8A8oN7yjbFALeUcr5nEoTRXCBdfw5D0-YVzTjtW5Q4L5JVGRugCro1uwSNMZzS_DQE2ZBgovhGrXFEKCcjqySjUWUwtywNG_Lgzh_Wz2GgVNKyXUm_1KC4RntoCSzbQAYm7HD6wAerkaDTq7hTelGjQ6V8rW2Iy-7Po8HPx3DbqqL-768UEQIRMEMubKCQJZH4G17WdZhD9XxngFfqtXJapp3YkB7S4-fdEH2_chPj7lnDdqPtEp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhIUmtAVAEqP9WOpLOLW-pPSScSw59b4dqW0-iiApcnf0KJL_ZxyLqEjkxp6lbT8OFIT-X-Uw5kpV-NHsFh1O9Z4TtiYynPp6l_3jaTqT9tFhlODp4EW8qLoW1b1dIR6ME9c9Mg9T5ZfJ9clJ7i0mNceauaBW5MzSi1CBtAv2DuE9Js0TNtqPkN6KxXqfs6c1IXZmFWmQISJXT0j7Tf2D2kyOmjl2Ue75MkQgmbUbcVz2KHhAQ-1wPEJSMjGwQVaYI-GGy0XShZM5JBbXfALg_YshYQF0b54FaoQEY38vcfnaj6d9_tryNOv55ur_FiwbICAUpSaLmicMCwT4BRsNmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhIUmtAVAEqP9WOpLOLW-pPSScSw59b4dqW0-iiApcnf0KJL_ZxyLqEjkxp6lbT8OFIT-X-Uw5kpV-NHsFh1O9Z4TtiYynPp6l_3jaTqT9tFhlODp4EW8qLoW1b1dIR6ME9c9Mg9T5ZfJ9clJ7i0mNceauaBW5MzSi1CBtAv2DuE9Js0TNtqPkN6KxXqfs6c1IXZmFWmQISJXT0j7Tf2D2kyOmjl2Ue75MkQgmbUbcVz2KHhAQ-1wPEJSMjGwQVaYI-GGy0XShZM5JBbXfALg_YshYQF0b54FaoQEY38vcfnaj6d9_tryNOv55ur_FiwbICAUpSaLmicMCwT4BRsNmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=PidyJ5Z5-M3djM6nUFzpGLccAYLPhmNloK-WbDniN2uUy3IX3I3ZtLGH3eoklg0aObwD1VaXcOx7BkIvHEeHFg5gOr2yUrHa3g0YSW7ATWnl-a5KA7suvhiu08tWqf_pclRRmY3NloMsssSkPbBMFW3bnScmzqiJUZqoaNuZ3hIrTABbobQZQiCU2ZkeyES22kU_5wrefnoJGYzqUJLyHIxk9_NfPjpMbc7cG7jK10PpIlQfjQ2GuAos2wZ1oJcY31lYaPgeh-AIIJ4BVVknWLZ0bT3KAmHAYaTgCnAtSylCe0BcTdkPhZyurLAzq_O-RbD6inCZHu_QRTSkCPNwp5TX0YoICmyNQUP78f6I83fb9EwF6PGXIXosUE7u9Ao0LmM22Tl-MO_otPtJj0to_KKlOiaqv6mdusUZ9Dgf_3UkTXAmKNNMvy1hzuSMbKriQxys0xyLhiBeiuOqtqpZhmGhe4ilNH4BaRScym9iNDJbndjmWaxEHvaruuyM0zfJAvHFPPasnOw0BSUI0M6mW2r2Yji8QhXpYVaM7E1Eq9t0PvDuU0EWtHCw9im3PKCYMR-iUKGYOiLZbSvO3l90L54HfjMbGpa8_eJFMPpIHa0lGbiCq6wCohiWLL_Cwc1rfhygULM230Hi2eW4uHTAWQXhhhmUvcQvAFkmfqune84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=PidyJ5Z5-M3djM6nUFzpGLccAYLPhmNloK-WbDniN2uUy3IX3I3ZtLGH3eoklg0aObwD1VaXcOx7BkIvHEeHFg5gOr2yUrHa3g0YSW7ATWnl-a5KA7suvhiu08tWqf_pclRRmY3NloMsssSkPbBMFW3bnScmzqiJUZqoaNuZ3hIrTABbobQZQiCU2ZkeyES22kU_5wrefnoJGYzqUJLyHIxk9_NfPjpMbc7cG7jK10PpIlQfjQ2GuAos2wZ1oJcY31lYaPgeh-AIIJ4BVVknWLZ0bT3KAmHAYaTgCnAtSylCe0BcTdkPhZyurLAzq_O-RbD6inCZHu_QRTSkCPNwp5TX0YoICmyNQUP78f6I83fb9EwF6PGXIXosUE7u9Ao0LmM22Tl-MO_otPtJj0to_KKlOiaqv6mdusUZ9Dgf_3UkTXAmKNNMvy1hzuSMbKriQxys0xyLhiBeiuOqtqpZhmGhe4ilNH4BaRScym9iNDJbndjmWaxEHvaruuyM0zfJAvHFPPasnOw0BSUI0M6mW2r2Yji8QhXpYVaM7E1Eq9t0PvDuU0EWtHCw9im3PKCYMR-iUKGYOiLZbSvO3l90L54HfjMbGpa8_eJFMPpIHa0lGbiCq6wCohiWLL_Cwc1rfhygULM230Hi2eW4uHTAWQXhhhmUvcQvAFkmfqune84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs8olwk7vPuvqyTyI5BXx-8k-S9W5Fjc-04ebkn6WjW_3aD1ed0ZH1ALxXSAPyUQ2RRKg40z3Pbe02MedwVbFQvmbhaCmaXItUpjHiTULDoNmqFm6Go329tZFjXZUsNUmKzkpuV0aVrWlJPBoDwo_6DjdYhBd_lOx7y0QQT1CVeNE-P7FaJfXjNGoElR_mqw1pz5hGqbHTJrBHvAP-x9YNH5oqK1Wfe6QhrTCpQEWpf7tfj4SCu36m1ub1WHzzaab7NdzAIed_dLpyHAXzw7lCP_lbTfUYOJichyNYYL5uM96P6cSCDoodxO_PzNjUoZUDmlon_nT6VbWfEfxnBZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kcim3nZeYqDV47ZLE3-u1c539BXjKrgd-FMyJ5q-WtsP3xIebQ6kxLgsBGd7IeRbV7R5RT4VUZek2K9pmBCV8iOkn9nPpT3sAafsKH-zGxSAB_e8FuW4kIvxEZeKJIW8kUM288Z6djUKddnhZ5mxUeywYeBeeZRwZtuUxwnXM6WUeWs6CLN1s8pDZtTUsLqUSxQ8DElCsVKGPPydXcVJ4nAVRf6BaMAmuJW3irWVaxYlfUGegFi_NhrIvMYfmGTgWUdTILJrZ3i4BDhAaG8u6uV0FgOJ8jVgtm3Ef8Dx0ullNBtF0U0JZzT96IQXxALmivGFgPefL_q39-lNkycUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh1lmZEKxUFt6jG0-8rEQQt5585I67PY2Dgl4EPH9zrCX_KPpmoP6Y5xe_vgwTkzzQcj1VSWeYEcISDkZ7ArcV1OBAOFcvzvgZk5TN5uWJu8NldO_mZ5hvoLG-DTS1zPoLQZ4scJSsogQTsk60h4sHMIzMdT2KvsjNgaMg9uUKy3IbF7Pe-C_DKaUyosXumrH_P8raQsGXFO6xJuiSki85Yo6KJQL0Y4P-BN2K6deWMwJARSKGAww05-6QRzgu0l6pZhQ9qFZtGoFSRMVPAEmICgN8YpFC5S-9fGImd3xc8pYKEUuXYIGAUxik7cqEbOy9MfpcsCpqAfMR0K7ecOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=WGhsDy01EE8bZaEfcOPsioahFd5hgW4JOm6To0HQrbYsQLVgVG9ShC3-qgmyBT6kGkpLLIE07x21QNHwsBuLbL9ELPj4sPW2HCLS_mzl4XgJPKNHLn6hEC2YfmxVeBxnKGYMxxoJ4Ip14QLcGxwdSY7xogx4wOpM55x3U4k4SUodEshwF94zOLAJc_9ZanBifsA9YRGKT4cFIp2u73JrVBx0eI7S_1Ca2_zKaVTexh4ZycrdxACbY7E6IBVRewBxsDHVJUzq2gAiwRE8HxvtOr7DFDrXpHJwK0bDiN_i90SbPSm06GUFjSUp8uTD4TgYRV0VaKuyW2SleA6jfDdqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=WGhsDy01EE8bZaEfcOPsioahFd5hgW4JOm6To0HQrbYsQLVgVG9ShC3-qgmyBT6kGkpLLIE07x21QNHwsBuLbL9ELPj4sPW2HCLS_mzl4XgJPKNHLn6hEC2YfmxVeBxnKGYMxxoJ4Ip14QLcGxwdSY7xogx4wOpM55x3U4k4SUodEshwF94zOLAJc_9ZanBifsA9YRGKT4cFIp2u73JrVBx0eI7S_1Ca2_zKaVTexh4ZycrdxACbY7E6IBVRewBxsDHVJUzq2gAiwRE8HxvtOr7DFDrXpHJwK0bDiN_i90SbPSm06GUFjSUp8uTD4TgYRV0VaKuyW2SleA6jfDdqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMCCZsmgvKrGa90PxBoalRPkb9La7DYr2lr0xOf0XRE_cgdg_c68jb2js4Do6K3XiiQbPoZcgfwzx_q0TzIvo9grpxkGLhICJC7Pd-m7FfADb5QMH8iWe4f8y2O_F0SXjJrgZEMWJ-RQ1q08692iMblhcP-LAJ_hMBLxLSxqcmcFypiSj64DWQUksa4ZkPDD5tVE9ZOAXk-Rc95o6o5QPuegP5jSD5n3dfH5L9ZJgwZbfXO354ZpfD0ISDqdTO15UJv19X9LkZ7QDywT97GMqlfVTmhT4aonUxcP8A2mWV7vtv4d4n8VlXCL9xZSdNtn0Xmouvnv9fPiEL8ZHYMLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Tj1DZUNdYTLJ74PL909RJCHqY1BiXGBrJjYB85l4kUyYU5jDMNAiEoDdrO7sq-Q5YFQhI7GUk6HkUJ6gok1D56HGdGTQv-t-FTT-rZXUhF4oq1GXfgYVlcgSsSu4JIX_K43yBmDsT5BijcdqJBCpW2AZgyeB4YlJkghjed76LfbAu_UOMl7wIqsfwRVZJOwdoiKYyY-l67WLMlfYck5WRz7G2S_3RVuguF27Cq2psrlGFfoaEZFqGbl6GiQRjaROE6p5gXZtpai4hXWonyfUznjeQlwtG3VHc7U87c5bCL146ZI-v5Jx2ftgFlOKxqbkTbLY2k1nZPYL_mw3XvN9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Tj1DZUNdYTLJ74PL909RJCHqY1BiXGBrJjYB85l4kUyYU5jDMNAiEoDdrO7sq-Q5YFQhI7GUk6HkUJ6gok1D56HGdGTQv-t-FTT-rZXUhF4oq1GXfgYVlcgSsSu4JIX_K43yBmDsT5BijcdqJBCpW2AZgyeB4YlJkghjed76LfbAu_UOMl7wIqsfwRVZJOwdoiKYyY-l67WLMlfYck5WRz7G2S_3RVuguF27Cq2psrlGFfoaEZFqGbl6GiQRjaROE6p5gXZtpai4hXWonyfUznjeQlwtG3VHc7U87c5bCL146ZI-v5Jx2ftgFlOKxqbkTbLY2k1nZPYL_mw3XvN9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc1qywvit0LYgY2o2_h9NISsOtU0WXr0sNcOHs57p14WaiVFF5JYIjRWyzfobR5fcPkUmohcJ6Azn9nFUonANkC3EwDf2f13y3EJRlWZshIRTiX9Qxth4Emz23uUq-9jBfA2T0JxIR3XOee3yh8MajTGX0mMttdAFpuxLIxwlglvUlKvydNdnH0vQACmRiwn7KEwbJOIdZEcXJbNu_IC9mb7juEkgbrxKqVXtusznv_WdcBHK-xLaztK6sHmuq6BCYNiRz_E6dkGGOakD-wKik1HXDVkRQ6X3lPmCmzIceLWI-rTYsSb-c6CK5QbDf-pqrFlCWQobD95V59BSAUXJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ithi53ywq7tQAHiFOLjg2HA_mCs7dJHRG0GI3Ov687c8bOd1mhb67YJDdxC8oVgKVKbFhwtlbe_d_MhVtXV4sdlCuXcrjQau1t2FNPrFAkOFAz0tHQ1XOPu2oyGiYgmTXtQcW7dtqVGndqlR72ulFeWlHYAKGJiRRGXEq3woV7ujZzvgfJ0xnjQU2QeCL9QdzVnHJpstpjarkZ-HoDnBIJmcc1p_cR2YsgjWNkoqoq0PEL3Pp4R5IWNlBtZxGnKOL7OT1Lv2p7L7MAyOggLWgS68VPqvEJ6rWdbWmZCR5jRdKZ6yeS7Mf03t0OcVihvRGXtvcVNbxff6L2BqhDrNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=iuLMyHUYBmp2DX6YBAxBuqzdiRJx6TnEGXuHMXYnAC29JUwwqo7ybtW7HEbmMv7ZtVm2-C_i20Tu3LoPE8dXAkxnd51Y919Ch80adXh7GHczM2mI8w-BjQQeoEyc_y0hBTNshotPMbm_CKT9hGsZOoUKrL05n0-qCiwQQGc_NYZM9RvFYolaNIizR731U-pynDHGcPGJyjZAJpo4-eRTkuAAfIvaMDoFbUgvZoUUecnVpvY0g5Rh8GEpsYPTODLt22cGP7EnHlafzDjrLrMHR5BRau8DST0knIKZtXgKAx6JZo86qxkWc33Ryi6vpMd0YrRQw1sAlIAHDqPm_joKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=iuLMyHUYBmp2DX6YBAxBuqzdiRJx6TnEGXuHMXYnAC29JUwwqo7ybtW7HEbmMv7ZtVm2-C_i20Tu3LoPE8dXAkxnd51Y919Ch80adXh7GHczM2mI8w-BjQQeoEyc_y0hBTNshotPMbm_CKT9hGsZOoUKrL05n0-qCiwQQGc_NYZM9RvFYolaNIizR731U-pynDHGcPGJyjZAJpo4-eRTkuAAfIvaMDoFbUgvZoUUecnVpvY0g5Rh8GEpsYPTODLt22cGP7EnHlafzDjrLrMHR5BRau8DST0knIKZtXgKAx6JZo86qxkWc33Ryi6vpMd0YrRQw1sAlIAHDqPm_joKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ZlAVYgE8XGaFtoibUzJ9JEdJJc4ty4Cf16oR_YSOAaJfJsnYwCoprJa_iMFbyfHJXHOytrKFKlQ1rAcn0dPAiokvjC4ePG5lb6njkbtnDp-ba-RDHRTXUjoZ2CWFMu8ZnpvdSEPnD1ALesbBP3MjXKBDuFxqdVS90y97CKmuLq5mRDgZTPILS-ldUXrqmWeF-It1v_C3s1Ods8DktQpNxlaes1Jq7v81pwwgQ2DLfLl9cvW8_uuufa0f9RpjwkzhySu_a32RI2_eWrFoWxC8N3WSeU0XCM_nSDTls8Fm8DwXzN65iPMwfcyIXO6F366HlhETY2dKTcFafg-bPm2qlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ZlAVYgE8XGaFtoibUzJ9JEdJJc4ty4Cf16oR_YSOAaJfJsnYwCoprJa_iMFbyfHJXHOytrKFKlQ1rAcn0dPAiokvjC4ePG5lb6njkbtnDp-ba-RDHRTXUjoZ2CWFMu8ZnpvdSEPnD1ALesbBP3MjXKBDuFxqdVS90y97CKmuLq5mRDgZTPILS-ldUXrqmWeF-It1v_C3s1Ods8DktQpNxlaes1Jq7v81pwwgQ2DLfLl9cvW8_uuufa0f9RpjwkzhySu_a32RI2_eWrFoWxC8N3WSeU0XCM_nSDTls8Fm8DwXzN65iPMwfcyIXO6F366HlhETY2dKTcFafg-bPm2qlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=GRQrqE9Mi_1T3b36WgMd7A24dle7cgm3nm5fvbEyl94yMGbeWd7_VR_H4bxhBzMh2E8DSVcjjg83MpHwM0df5PWDHIIMEPNv4VTOM1MTmAUxl2ezoapcGbxowdfkXcLot-ZbMc9WUNaDeAxenNk9Ih82WTStlpMUOmPBtoNjLvShAwH8E_RuaArXpQX5QVg1Y99ElR19W6s5lYcrqg4h45RTwEDg1OjC71vytKmqgVX3LK8KY6HSiQtDadWKKtmyPYITbDg0OZW2xrX5V4M5YAPIXxjtMIh8STc91H45EFf3xLTcR2kW1p9RrIGmUn-xG68E5nNz-dMKvsw4pzPOwkpsFSfIlo-GcCB7wPUz1KgKT4Ne8e_e4ZVr3AYnFq22iehcCBpcsaI4lg-BZX3O98jWH1H3Pltg7ZFaXfQFL9JDyxMNoqJNh2Df_OpPVNkL6S2zTcig6z9FyV9T7bK-jVQCyGwLjMKD48R7GG0Rjhrg8V5z-el5XLPUnB8y6Sl19Bt3rgxgd-gTWDfqcANIyO0Ilnch_f_M6S1w5BjTr4RNM3J6meNLBqBzRPGscLYjdgBqfO-VqW0paQz29lify3ZlBL1_0-aQBms0MHauRGOV3vT-OpVdqVBdMXP574yuTw5sGMUptNfQyJqfeV8iwfno_IfIpt14q0mhz4v7Kwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=GRQrqE9Mi_1T3b36WgMd7A24dle7cgm3nm5fvbEyl94yMGbeWd7_VR_H4bxhBzMh2E8DSVcjjg83MpHwM0df5PWDHIIMEPNv4VTOM1MTmAUxl2ezoapcGbxowdfkXcLot-ZbMc9WUNaDeAxenNk9Ih82WTStlpMUOmPBtoNjLvShAwH8E_RuaArXpQX5QVg1Y99ElR19W6s5lYcrqg4h45RTwEDg1OjC71vytKmqgVX3LK8KY6HSiQtDadWKKtmyPYITbDg0OZW2xrX5V4M5YAPIXxjtMIh8STc91H45EFf3xLTcR2kW1p9RrIGmUn-xG68E5nNz-dMKvsw4pzPOwkpsFSfIlo-GcCB7wPUz1KgKT4Ne8e_e4ZVr3AYnFq22iehcCBpcsaI4lg-BZX3O98jWH1H3Pltg7ZFaXfQFL9JDyxMNoqJNh2Df_OpPVNkL6S2zTcig6z9FyV9T7bK-jVQCyGwLjMKD48R7GG0Rjhrg8V5z-el5XLPUnB8y6Sl19Bt3rgxgd-gTWDfqcANIyO0Ilnch_f_M6S1w5BjTr4RNM3J6meNLBqBzRPGscLYjdgBqfO-VqW0paQz29lify3ZlBL1_0-aQBms0MHauRGOV3vT-OpVdqVBdMXP574yuTw5sGMUptNfQyJqfeV8iwfno_IfIpt14q0mhz4v7Kwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzX_oLAfnx82kA-zLRrRdlw_iqOPfAFeKC3yMGGjoNe-bh_9GjJC89Lidv4s_2RlEYl6-JG3_dhRpfEML-JBAEgjl9lBV4qASnZAJ6Xxv5Ulqz-bS3XI_q3oeoTByIe_CmjjNAgbFwaBm0EvmY3EAhqrbf81dGGiGPHjUHBwURcFWwk-xRB2S6wOBIF-1rFaNqHg6zk2MsJaWk1Ry3FD4wr5X1wT3lP3t7-mYuBNRwLX4i_7Xh1W9ubHBtYuTP43UTPnusFXC9hBHyeRTj7EuFnQzn-7WznmXvRy58wTA2ZN63S82ryK9mOoyqvNt5aOTv38ELp6xvFNtb4prolW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXHfiBzOFyQCqPmhAVnNfAeby1UzJfacubzfX7J-P0bW6wAD7U22nzFpo1YaR23cqu3WlisTvB_65Nv9avhM-LS4uJw3URcmwLx8oNBLkVc9Bj4YCNYn5BZjvaNvtiNRl33qzSlKBZp4wQhfIEyWU8_JBvvbwDEve-GsV-2cG6Xnr7aDZZl4WI3GC_k5FIDbBmNU23pzlWP7QCqBQWuz3rkqjy2c9k_KLAdtY7SAhz7KbAadZDMTwT1BjbahEKcIG2HfwpUQ1_FBr6_DfhmFVgOyut8L904-LgQS95L7pdliGkeazmuOWO9YlJ-uaMHMRHzaZI6xMLOWqihd5QgifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QszBndis9Ke9YTtkt9BYA_vC4-cuY7v6keBiAyE8n6Jh4BjQ_7GRHGj80g_HKKvbbgDO0G5wZo7od61laL9vemjsPsksnVUqNCLgWkqraHxV52uZDV-vKrAlv8Z-vw1np-VVtH2vGnA32nnla8MWf2TMWkGyaFs_WK_zlwO_lWjHbcszY-_Chup3QGj9nP42t5GgpuzAZNoJ3PyDg5qeayNOeRIlEPRMI4-0tvNlYi_d8WWkj1pSKPhqDSy7D0yNk36I7grwVm7DycGpq79kXVcOTc6VjbIQRgV4QcqrAVvkxuKBAvesD_9977JhbQP5O54GPNyvyXScig_oEBqsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=q05nddnBY9YGFkubuiquuSJdU6ehzUuTqLW59QaAXZWJPH4qppbP9TutExauzn9-5AWTiBJcveEur2d8WHaDW18yl_Mqrfjt5ZE4s61e4AsZ7v8FY-lIkB_MIY_KGUjavhyqHOGtVJb_xbOX8ZidOylyS2FyV8dwCqQCtLmXy9GY25DjB2sRe9KZye1-mJ3UUyzsTHF79q6krwHmtt6SHHIA_aitUKMKrFxpIxKOHJzM0ak-YHHSXa9S3m20e4iEcDBdvphGoTWJrie1GEYYZ1FjRWDmaDQIX9HiIseoTjQS__v7fQgXDt62IfigrS-EyIR779BNGxw5rCnP4rK5UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=q05nddnBY9YGFkubuiquuSJdU6ehzUuTqLW59QaAXZWJPH4qppbP9TutExauzn9-5AWTiBJcveEur2d8WHaDW18yl_Mqrfjt5ZE4s61e4AsZ7v8FY-lIkB_MIY_KGUjavhyqHOGtVJb_xbOX8ZidOylyS2FyV8dwCqQCtLmXy9GY25DjB2sRe9KZye1-mJ3UUyzsTHF79q6krwHmtt6SHHIA_aitUKMKrFxpIxKOHJzM0ak-YHHSXa9S3m20e4iEcDBdvphGoTWJrie1GEYYZ1FjRWDmaDQIX9HiIseoTjQS__v7fQgXDt62IfigrS-EyIR779BNGxw5rCnP4rK5UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=EIQ2HQEYp0JgFSBkSMJVFmpP0h1bhTdFy1GdjHByPpK1gyDhqpgG7HQHV64UCwhlm8Per26O-N6YOcMAMid2cxSC1vUvKk8UPkhN2o7CX2ovWa4wuphM3-Dnhj60sZXbsJDOmjkkDCS8d8UvAYXxccPqg7-CXA5jdd2LqMl0kTR1UETB1GwsgAGrJkAvHqyXPJpEnV3-7KotMtPEKF8K2TbjWTZYH4ZRsYOb3W1m9k-7Rj_x3sZbTizZ5oCxebcpgabds_jh6ouSHTGwu9TZBUz0o7QFYYEqs26o4xm1VG_8f4S1u5KPnjS5AJXy829IEfA745DWZFhXv_QX6zh0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=EIQ2HQEYp0JgFSBkSMJVFmpP0h1bhTdFy1GdjHByPpK1gyDhqpgG7HQHV64UCwhlm8Per26O-N6YOcMAMid2cxSC1vUvKk8UPkhN2o7CX2ovWa4wuphM3-Dnhj60sZXbsJDOmjkkDCS8d8UvAYXxccPqg7-CXA5jdd2LqMl0kTR1UETB1GwsgAGrJkAvHqyXPJpEnV3-7KotMtPEKF8K2TbjWTZYH4ZRsYOb3W1m9k-7Rj_x3sZbTizZ5oCxebcpgabds_jh6ouSHTGwu9TZBUz0o7QFYYEqs26o4xm1VG_8f4S1u5KPnjS5AJXy829IEfA745DWZFhXv_QX6zh0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=gcKF3r6L7Fek_Qg8GvKvBbq3JXFg43IOqPkED-S1sOuhXn7h3bXTCiZHhnTzlVXd911G5TLFcJPuL-gPf1B9b9jIDiZR1mjTBnhjH0Sj9BLPKQF9ksa7nZNxRX0BboQvN4xAtzHh6x9B9yQfjpEB3--fzNygTCQG-u0PYzvF-HUWpHKXYgBys1W1NKqYjXn5gzqmyKnwPKhQSjYzi4-yE0IoiHoNYV-zOWEJXIdxk8Jng6qhO7SKucuHb2GuWYjoECiT7IxHF4Se13WUC_8kVIpNQUwA7zwRE_bodKmKylJPCC6eqe4nXn8KCOnS88WnEbbF2PxeSGFd7zAofrce9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=gcKF3r6L7Fek_Qg8GvKvBbq3JXFg43IOqPkED-S1sOuhXn7h3bXTCiZHhnTzlVXd911G5TLFcJPuL-gPf1B9b9jIDiZR1mjTBnhjH0Sj9BLPKQF9ksa7nZNxRX0BboQvN4xAtzHh6x9B9yQfjpEB3--fzNygTCQG-u0PYzvF-HUWpHKXYgBys1W1NKqYjXn5gzqmyKnwPKhQSjYzi4-yE0IoiHoNYV-zOWEJXIdxk8Jng6qhO7SKucuHb2GuWYjoECiT7IxHF4Se13WUC_8kVIpNQUwA7zwRE_bodKmKylJPCC6eqe4nXn8KCOnS88WnEbbF2PxeSGFd7zAofrce9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
