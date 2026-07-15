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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 466K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 18:12:16</div>
<hr>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPNvx9gVJO3LVXfox5jfRbkewAttMPRrwJiQ4igENm6psWdHGSiY62azOkP68F1BjEmV_mJ3YcjutVKRRI63-HmPQ5PUfarto5JoDpR94qmQ-l88wbufPo8qLN661lBM4C4ue1VsTXG9Soxqgz2bxUImlb9qhkT4C_jpcv78QEziBANMEC86Tv2V9Spq1Uc-MaGzUrgU_xTyt7109oXzqRpulPCG0pD5Nko2gPnzb-thadD4GcfNmGzxZw4f0uZTYetxFLSAAG-vmovsjbjyPNPx2Xjy1hRFDroc2rb6j6kWqFc_WEghuwcJAeKTbD2kaX9QB-qTB0_ewnFsLgEcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKBUpOAwpKVlD7Kh48djiBej53eeuXWe1u7NJk2wRpzM5bmu8jcvlpPvXAIIjRcEEQvnUaRz2se2eJgD26ir4JHnSGmmFf9Nyph8a-nPZgzzp2nUy_n_fqvCWyEXsDTw4hdktadctLA0ARXDgXtAU23CX98y8xLITYYuTq9otixhdqbhDnjmuhzfy0tgZtKFPPalsi3ix1576cCx3pn_w-BIpks_7c4NnSB9DyU2CPGC3_sfVIACAskhaS-tF5KEqE1ys44V_ASkePNPgkLJmNGGZzhmkWrKMeN2-AadYQY0W1pW3NNwKLq9DKl-YiGzonftTXmNTodmYYG0uDTqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHituhyojUGvGyemVKVHj1hfRzcbAC1PZpjivOJhOIlqaS33fKtsrSF4QIHrpMYQoAInvatTp7KkqiLJgzgh9F03pt_NqVcQz7xjury2D8RiIXQnALN9Q1vy8ZIg1WTZ-ha1masoizHOLbBVgL319gUA7ckEMhlJZlvwfI1SOQGXlVz1cDSRvqvIX5odSrCWZKmvJa4BfAHyh2kloHQ-hLQt12eAkCtOrh0XyMbs4BaYEwuqSLe4ybbKgvlr9bN0D4bejtpiJ-8j5MyiTGbmDy2N2ZkTuz7kNkrtGRrHKoMh0WgnhcOQSoa3JpBiR-I0kqmF_WYtIPf8gu2TQOKzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCsSlCGhBmocdWts3RmbQBCTZXzbYCfasq7o64kI1euJrhC0KSIbPFovI0vmPpN3mdCP8Zo2uITU6Qqibu9_3y1mqNKU6LQ_LA9YI6OKp4EZBGTRXKHwcEIA_CrIqSuz7Ytkh1iBnha63IUkiwXqJ9fOgVKCh73TZFDMjoMH8LDrpHC9QBHxCc6LnOOr6-BGcVCe0JONmv8Nf6FpH_iQcBYe_I3WdyfameUd2RChQcLcvovuIkHYxrN8Byl7ONHuV8PccStCI1JkyvRR0DWf0Uo-eTMvsFQIxwiT7aua7gSo-oO1HT1y8SO-LYqooEg4DnlHRjgOEForRDKnOU8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TArVDF089jWJpqXTMjCpL7y0EnCGqL6cs02Wk7LEDSNIr_quO-6eLzGTq4CvYFytQFsWfAt68ZHYadxynKFHT2uKu0LgViororyuyy2_O7uv1Rybv23nE11cxxJhI-fMsfBi2MkMoCeCPggb1fTfjx24QM9Vtne3auSZhiUN_2FpA0Igq7d68_EX8z_5K8xe2RvLmka2zOWod4J35ugly1vZl9e_oc_1QcTJ5PMB_3dZrMIPbqFuvZE-PYeep4tgI3UEsuCI_wGlz9VrzCE-P5PdnmVLAVgsDakdsuNoXqW1JCf5D92CgRR0NwTcZQuhBmya8kd823cD95Te2nXWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpX4iCHqNSUOxix6XXQNelmd0hoEKjsR6naRPHpDPzbsg9Rn1xyJSBGp55BlNl3rl2lCI48FQLIZU-AYf7w48jNzKxk6oz9Hsx6sf6oWHIV57S4YLUA4TOVXgXrW-osX4yGkEYXWIrl4FbR_gNQwcxNgPGPomya9a7Bm9viuZlHBntjrLKnAO2ROabyjJ5McCq3zd7Xds3J0-KibYqGQ9Kk6jCmU_fhc1E01FmBPUtnoz4IcQa3WfMyL20zFqIolsmv3beKUmkxanSlVvoUl9okURNm9Hu5SzQe9IDFE9sDoTblClysHzP4wPy0TnZH4nPjuY25-XjEQ3lPMBOVG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=LlIUEKYPXPKHZ7abKr5gOW79FwmxmQS62GyQ0VaKEJrJ72o-QYteqoe4DP0T3pnuWst1LbI8_XvIE4m-omm80S3jxfYKXYtXYwLO_EWm47tRNB_Z8c0K7BXXq0CDC36whOB6e0EGUXNm7rKD4lbck6WjjmM7upglcIQ4VWZI_qhRQh1hXxMEGHQhlkohPiKk98RXLy2iL7Bn6tm74960xfTdGrKO1GxrrnNSY66R9NF0cJuBecUOXV-Z_kE39P3KRQCBGKLT-3qBmSVHJmZl7f9w_lqQBtecpp9Mh1A3GlfYqIAa-I536DlvbMy1K1CJKMb9VPrNEK7dLbCSnn2vTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=LlIUEKYPXPKHZ7abKr5gOW79FwmxmQS62GyQ0VaKEJrJ72o-QYteqoe4DP0T3pnuWst1LbI8_XvIE4m-omm80S3jxfYKXYtXYwLO_EWm47tRNB_Z8c0K7BXXq0CDC36whOB6e0EGUXNm7rKD4lbck6WjjmM7upglcIQ4VWZI_qhRQh1hXxMEGHQhlkohPiKk98RXLy2iL7Bn6tm74960xfTdGrKO1GxrrnNSY66R9NF0cJuBecUOXV-Z_kE39P3KRQCBGKLT-3qBmSVHJmZl7f9w_lqQBtecpp9Mh1A3GlfYqIAa-I536DlvbMy1K1CJKMb9VPrNEK7dLbCSnn2vTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr-c7cKrdsUY7C3G3wLByU264hwpgUXB5uRiaPb_ADSK-13RVet6xZM7LgbYRAz5FWTFyQ5we6k7DjXjrus88uFeK0Z9AKnRNsG9tP_YUoMhvXHt44SU6LX27b23tGIYJDfE3YDHs45e6cakCsRltgNSenwZ-dbNXCjTijlwVxc9DA8fgr9u1W4J6BqJLdDHErIIfGGOmBoy0T2w3_nBKNBlI5-0oO5uGF77Ykmp2EHUFE_WiwZxsh-_1jOFVqNGe-vV5ALfLyowxNE6xfM76ovInvAPCocqVXlDyNb8ZLqYuILlbzjEdCYcagQ_J3Q07MKQiUwdeQ7LkDz_VWB8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSxiDmUU14fzexx7FJwsNap48J9S23ExhiDuC7JLephYrW827OLRalK6GHxVSp4REtiegJIaEDjgrfchVZWwhsrmTzEvZeMOl0nwXAVksJAwzrPON0N6rG5LxW3kGz3H_LQlVtdCPH3OeaIC5lsD8Ly6DFddpUirh0ChUYBtKgrTVgmRSHoy9bc0v-gqxPmustoZYsvGuS2BL8y_h5795z81jLSHh_laxsIb3CtJeZ-ENDCc4k7aQzeX-0wGbnedKd0iB881LHoUtejakRh9FIh-vYzOCTf0wBan18Rq5qSA6Tplr3L1wny7Zaiy0TX95i-wIQgPbsCE8G4ubQPwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZX430xGFZSQM1ClqUkJGiWafk8rF1Rh4msCIaApAmWIL8mPcd6YYcmwOX8j0Qjyu_6Oiv11Gf6BP0AosnV4c9U73Zze8HZY3IdEa95K2bwcWnzhItrB_uAiWNcb-fDhX19WpdrVBkF714_hfOUpsCKsVDKf8JUJWhKxeQpHCRsGFq1aCRqhRBrkFkEGY8IvnInvnpwQw2e8Uw7OHwwHd-_YI3XXTbgngR5qUSghHvsoF_EGhtokldio90qYdDqp-wGZ-FdJUtgvuM765vgAEnZLrI8NUHnobBQA00gkz5Crg8bagkuizcwP9PVqiGH91hUvT53m0_OLfCALqo-E9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=Hl6-juvjffctWNH7QyHCoEilvcEV4ej8OmSbVGcavZcgNSnRwf-wqqx7gS7F_aqdLdOGmyniLy9DkWDR2bACj3Z-EwUqB2tG3rBDRTzYj76rDMs2Mt9jAaLbODq3TN5APqqQIoIpQByETdtkiXDLzC7Q29VKPLYFf2qVQ7fSn-NdVAav3FJ3ix5h57zl_JBh_Tlbhl5b1bS-brzjAB7_M0AHKXCVSquzl6LcQjv0dCBmLKev37qIPoc5YE7ikrAXqiHuFzSfT4e2RXjfrVGEUXT6jNDHelvtbBB0QBOr_kebzrZGkoIPm4IM4gH1ZxEs1Kbo_RwzK2k9sdBp_H99mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHqCBlN9Ph6eH5GT-SSLesqecRC3UittkxMKQn_NN5XScE66zhfPzSm9wgknrVtA7uHVPspd-cnXfv-EeSRUQS3-lthjrjL47-QCivSQh_SUiloTQCWesU5Es3nCqOK41eA4pMBWv086MYCYMWm8zUP1o5qI4QEESrUETcUicEaGkKeP9q_IfjbjsZSoNoDawdt-_U6rqrJaBzGr6OH3Y8Vx3Ab4tMpK4UHYa6uTvI_5PuB6lEKz_p5jWoCFULoRGwTcxi7mG9sn0qkNyGoShp9a97YZSbk6b0NJDloToO0CNnHPGWUFM3RWC7YbseaghgBqBwjfZ1mVsrM0lDexOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOGMS-zZCvpBQu49hqVFchL9Uaww5gd-7lBmAINn1E1faM7XJDizyyEJ0EFcWFAez-SqKfiIhHQoAwvBuIU7KJV9M2sbsM2iC7CrLTxpWtMBw3STz5XwVu9bywOtfJ9WBfBtL6G_6U1YdrvnMNJdZsWTrdCIA3TIF_t4jH1b_yytwMcuIO0QaGcQ8Eu8HFbMN3lQcxnO4xF9TgOfDvN-TVX7nlYXmxbELHZSOcMn4rNxDcYRQnE_ZO6MqQd5aNIiZ71XgqAmCAX3uhLtH-CD0ZgrSo6fjw0qizwBc2L-gxfqY3KiJU14Cmj7fHEbUul6FlG430z4Yjqc7kmZ5qKWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec4JG9GNJ1s5-iXnjJfDioI0fANMJUPiaxEHDA-nmo2iUdFHhdOC6H7M64utl60olRcFu5Q6ggPfHtdvEriTwZ30cComM8Y1UVlTl4wfqj_SeuEwc0M2PsjsB_6BY2hg5-c4oxDxQdYDn8xe6hIfyjeJP6zddpottWhnhgecvfX0h3QzyIW2IIf85rCEmnhqARS74vPPoF4Sj8wCzSw_Det8z4lzjk8OUB4xIjH9oi9PEhkL0n3Q-z7OtVfIpgShbZwoNptMiUBc__08n2cPbcbLg_HxwyKiM70OdutQ3AvoW-_Bgl1f6vBH0l5zfev2lMIVrjiV0AzKQ3dhEzqakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKv05iRbg_w5qmDgUGZT-U9QsY1kIcHKl4V6bhbevT_rm0jOOOD-1IKAUt0khezXhVJMwBrRC-DAwBmvYnK8CDltc0Mee5uF3hMUgRe6jvvCFVKywIM6RYtdhHJVeMqNIfSsj5w0ILYnDTmT82QZH-2N80__8Ou3YCwtRCK0Tlxcx85CpIbrmgqFN61tykSd633LRtkLfLS0BgVg0mhLAASdn3uNhxGzoJgNx21lp9bU-Mg7BxZdNfjVTzth4EByGXLh2pPCtHq51WSmWkEScdyUxWQ-iNc5yw1eSA2jCucJgA1L3GiPEPxY2X94l6yhwOyuqvixkMmy6UpaBpwXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRP5ammiu8y8AcNi2fu15ogD9zUs8kT9t8DbieNsB7DphgoqkbL6jebcKhDn6CPEyV4zMraZk2Erg9LVygaMaOxcCYGrFDNkAtUiVV6oN7tb-hcabQIfsEBFQi7wLnhD11D_1gA0LwbvyvlVtZsY8fOZzXYPzUlcHmxQEV9L_rZXyP5tzd4RwCsglSEKl_vZAqcreUQQfNFDB1o7kqDpobefPj89vANRAP7hmr_EoXzzCCxLOb8awR9qwr0M6-9XWsOOkiUvqNjdqJmtsogOr-iLhF2ZDxxeNApBGqRlCG1y_xVyB9Pa30kYK3lSbJSixBS3YSFD_vMRp7V82T8fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWRl7JGFqhG07MHgWG-Oh-Zbm6R1qv07dVgmQyl7vEHG4sMrPCQxt-Rc-hMPH1AmbOyvLRFKqTkEztfevQvl23EHB1LnW9b68iER_mNV8ieDlOuyTs6ADnZl_UsBDAw-lO3be9k2yz6AuVoLDwcNBSHjtKuw-zOJeJPHewCB8mPGuk8QMK-PrClpa9xGyQe8o4FXXJkRHaUcn0CkrBatWX4ftoxzx3KfkL-kdVsE8R2WYdsOoiisoBOBfJPsaMXOZc5KR3fv6ZHw0TiyjOa2biR1PC1yYm2OqkLsvdIbWvawJMYEXV5810UrLA7BPVXSyQRe6kwFuoE3dp9f29BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwp-az-yU5-SQJe3gezLMywvBxvkqLEP-Zqcar38tP1tQiq5HDemCpC8YFearJw52Eku-4CbmRbU_aMa-vGoZeTMl8eXZ9gw6ivXB69Nwbv0Okik_hXUjRn8erFLcM641xWKX5NNdKBpgj1J9g2JwfLbctkRzPmWGYhYIjv7uQFmSgssXTJNuRJ7eq8Vf4n6ne10BCpekl61bAuP_P-aWKxcrD90l8tggVgq1uWQtOY2-F-Ub2I0GAZe2lOk64x0Afox9hdiDjzwCqBOTjcL7uMLRGPT9HghLZ0HS39T5dO2dPws8VTWEd-5MaqhhY8TGyrscPelH4W8Zgloll_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6J8Z8v22e68jgA8K_d2vFmKLN07YlB1w0VXSHUev8Aw2N3-ORX2j5_LcKSZmdeRs6WRCUKb-0Colq79JfmIsnqIUZlepDdZfJ5N0rryPxFYhfRXWgi1AM27giqMObJjOSUo1QrXnKtSOuSFYFbH3rZNBjwsm0lgxE_ZVaheI2BJ4e5LfjnpvM_4giBGITlljUWpJ79B-b5_RouC17xO2kqMrcpL8zcMVyiVQdKMdUFWejvzI8c7kNhVvwBrd3zPeL7Bod6KZXsfkttybr9Fe-Nc8qD5VuNrp9ighBhPgchnPj_kJXSTc7LZvJGRbUOjU0zQMfMDgFy6HVt5EoC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWOdb-g1lc07xnC2M2hSLsZdBb2P5_9Gbg0qAdWpYKr2rksaYYCGl7H5tBDjASi2SDNLt2-8gNXbZKvX_6sw52DE7oMwn1-xJ3lP9hd0jSoET4KC8HCA_IE5-UwLy5ri9dQGplXH-iL8fYTYzyPy8EeTqtEBOWoGoCXJmsge3io-3Jw7T1PjaFbP0zpg7ahtZS7U6Uq4eXSfJPX2MEQGrL1SducwqRbcOEE7Iac7-o-95d_wQhdpbzz1JRDiUkHu0pPO7hWaCPpv7jbC0xoMatInuqKosMjrre3RN6OJIkgtRULgZt2nX0Cl21KNbAgj7SesakTwCpPx1iT08XkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB3qC-glbsoN8z-7G8g5SYBZ5DDYk8pO28AmSyIxZDI9i0rRmtoMdHIhWO0B-I8bn27jlKMo2frw6U41ZW6b8XL0Jz7v6GG-ACQIL0vNiq_l3slKzJA9EVo3x-US-YUzJByhzBsM3i-SKTAhWicuqnr-xsPY_3__PcpTtkcVWlauFH48FsicbYAtyz06iSNrGqm0yXt8tBx0C1O8rdiGOfFeEujyS-2jeOLmNsDvAyz6NbFLm7CPAA7SCEeV_yKuj5hOXCVMXGet2CmsCfpZ854RoGSu_3jKknArk2wRikwHo8ldPQ1ptheiYgBj92_-0zFEBNrzYttD7NYZWRsSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCinNNqw6Xl9mcnBDbGAzM52aUEgeud78nNvWZVTspjBpcoN5ZlaTfn0Bo3VZaiY88V4NsLyzhNyszYVYCjc-n5p8YZesXoRZL0kW3NjfYHklusI8S0KhCF77hzFDx838kXsarlIU0KMSLu4F0ECKXCnossS-qx7tZblYNNIXFpP3NXuiKw-3a8j2CIAso0V_XQWQTDm1qsKBaO3K9GXQjV1EDyiBHRPGRDnl-lWhAOq6ia0QVqx9agEb2V03896UhxdFq1ESbsIv4grBt1BKh92fkdQoTRuGo2DGVTaYkguG0DUWF-clwQMnWHpNdSS-k0Jbeiclxr3ZToMgAjJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9jf91FSqqEDKf0JlRmn03-OUum6axSXHjRvPJutVNjDvK1ZLxNp68a6jOVLGiNmCzUiaIhM7YZeGl-VUHGAH67R9ADrbW1gvX1hmaCAPr-Kd19UxerSWC5uGusrEowyYG84KSHxvug4_ipPpjpRHxlkUBaKAz9IiAHElO0kj2-R521Bzy7uE3dNzhTz1fZXlr4ryepYIzg6w_IQNNCulyI1dOPSMuN3czo6X8GtmlS6wpn1PPp_wrmRli0EGZb5uAtW5M6Czcxf5rHb8WPjzDXQRU6N6eqY48phkmJw8VDTR46ON_87Jjt71wpCPFdxOXjtDjGvo9lEeRGsZGLyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNtf-VoGrLGz_c-JzFXk9BuBDtnZiDHmJlKz3x9lqXCr84JA6hCk6gAJoEWa1m1zX1_NnIkqw0sCowV8s0PC-9huwfo6DH0h-lhSm8145QNke8csWpDv9cekpQh0zxGqWOMc2dnjfFCUTALIH-dmJF9_epJheiQYKrBy-NkIIBh3wXCAklbJVO8Ksfi4yA34TO6E_kn7D_8zKGJMgqlvRxEJ0Dhf8fVQ7ZMWd1mdWOyg00avZh1c29xM8L9IPLqtXGxq6XEl27QXOuugXca_z2fu-lCLlF8MBmkL1iKNzW_N0CSUSlBRdXf0QubixxgXqqp-t5PbNuMv_13a4Irm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=JDHhmoGCwlpAsAqgtzleIzcgojsJTilhz_pyI2HiqM4n7L3Z4BuJh5zVCKr89B3VOS4LmRJg4DwN0jPjaZrrDDitViYA4S1BoQ64Ja_FCybe32Qf9e66c7JiaRrQAKOH3RnG1FalngZCbKSyT4yChfUZtYj_3GQC3t2mJbAJeq2RCzSyQzTgLXhV3RBpDSW1ty7JuYAWAA6d3NFl0lzT8n6hJYH0pPs4tgyVvN9afVwYLFPMWdTXQeE6Zw0tO_-RAISnd8MsQsiqPvJztNthniqxD-VSxf6vI54BN7q0woiJlvSDh1o8OuP4xiKlI_xZ0LtGqcZORVqz7WMKha2-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=JDHhmoGCwlpAsAqgtzleIzcgojsJTilhz_pyI2HiqM4n7L3Z4BuJh5zVCKr89B3VOS4LmRJg4DwN0jPjaZrrDDitViYA4S1BoQ64Ja_FCybe32Qf9e66c7JiaRrQAKOH3RnG1FalngZCbKSyT4yChfUZtYj_3GQC3t2mJbAJeq2RCzSyQzTgLXhV3RBpDSW1ty7JuYAWAA6d3NFl0lzT8n6hJYH0pPs4tgyVvN9afVwYLFPMWdTXQeE6Zw0tO_-RAISnd8MsQsiqPvJztNthniqxD-VSxf6vI54BN7q0woiJlvSDh1o8OuP4xiKlI_xZ0LtGqcZORVqz7WMKha2-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrzsifyyTMwTduBo5AwDx66KkUeIxrj5TmntEJqdm4A5dGD5Yj2JewEoiMFdMGxNHeTMHqWU_vzxhdFNjzns1kwPvbSX7vGVvihgqVr2TO1wLlNdPH5b_i2Zfl92JQBOQi63JGSo9sT4fgemFSahP7_Z_m3RQySPKn__ubkYUUwXWACMt6UBFLS8m8xf8yf8rh87Oc0guhse6385fO40Xqxn9G_8ZtdQbXvHuQV6b9Wv0hLhu43erJl65VT0RrL-t44hKE8XxXUqKxNRaUHXV795p059PCl38EvS03C5Rb9yE82MNnwQ0UdGaqi9wHOhxh30eTVukeQnW41LVFzk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsQq1ns9KsKe-_dY9UjBI6luH5ZYYjEicz-vuXmbCmECTGs6wV1CQ2lWYHMCxABIUEXcwWOVQCMBN4YB1D9S-C16japXVzSfHRc7tSQmxdhca3dWcrS5TnA83K4cRntARCA-fUUjsDe-S7c7C0JT8BKbq4fXKWwq6KZPET_a68_nk0snoIfHhhFyLXbaS6WdONmiSzofYjUkx5JRjELnHyK3v5X-d0l3T4CFGi-pIhI6T0d85oWhLQUkvzDMP-A6ZCI-TVjGu8ZTbJcFmBkphdMt7UrY8vrGNPJi-PPDJ4kgMTKFbs1L5-4HdbmyMIIbSeY4hEqhixRvSnJ83uwBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=Gbg_qEhTJJdBamgQ_Ewrf63v_-BDWDkdeCf6DqfggwQTLOjyAhOkAcsp5cwJMxh4nBgKUJ2H-tq49iZTvSKxJ3TV4zQ7p5ny7_1fBdBLvZq3KrqWoqrYv8sCDbhxjEchKA7V6orfWo_V5bLIocspBAHlMoB8-2cPbAxMpMjqdQqUx30sJbi5VKk_MpHJcPQn1tUADptr_ceph0GdcdQH6_yNvKZ-BUns3Kr6SbGtuLBLKc5EBP4R9vkJhDam9UTFJWOoTc2lRN4X8xrX7OaH-LTIG3QA1y1eOEr_8BoL2nPYvscbbKj6Ka181ulTkTSjr5rMCklUI9EZr4W65Iu4HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=Gbg_qEhTJJdBamgQ_Ewrf63v_-BDWDkdeCf6DqfggwQTLOjyAhOkAcsp5cwJMxh4nBgKUJ2H-tq49iZTvSKxJ3TV4zQ7p5ny7_1fBdBLvZq3KrqWoqrYv8sCDbhxjEchKA7V6orfWo_V5bLIocspBAHlMoB8-2cPbAxMpMjqdQqUx30sJbi5VKk_MpHJcPQn1tUADptr_ceph0GdcdQH6_yNvKZ-BUns3Kr6SbGtuLBLKc5EBP4R9vkJhDam9UTFJWOoTc2lRN4X8xrX7OaH-LTIG3QA1y1eOEr_8BoL2nPYvscbbKj6Ka181ulTkTSjr5rMCklUI9EZr4W65Iu4HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kPzAIRW4G_I84HIovivH82wbVehjwaoMa1u4yQF_gmIvlLqbAAy3U7SPTuxzWsQ2RhDCVJv23VntdOTErRGuzZVhH8X7otDnNNChKYJI-HtbV6Q7yDT5WuJs8QRtmY-GptI5BY_ejomPpouWhams2kk5JP4F4IyBxjGzntYcFwALFJwsETy4Hbc6HR4TRvuyA4qo8xnXMcNWEXkpv2JQCaD4JXZKxge6s5zwr116BzrO0fpzoC3cdHghLYDDKe0vWZsy0RmT15SYttA5DyblG8Ll1-HkQDDnACr0bAbj5K5e7aiz-z6M8FMmvOaMHQCjQ-cS_cg3jW4xd8uVK82paA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=kbeOVKVSQb03ULE9RCV2lIiP3JhW4OkD42Et_blSHyZXvbNxgbFOTCKghYeRAViuEmtdkX8JA5RbwEqvXuyf2l9hXOigbqFIyfeQt_PLVxflaCz7x8BLxeRqzX_QUDIw7hoD6hR80di7Hy9BsqmzAelpjCQVY86L98u0Pr_SbZcTbomM2VzJr1pNdrQUs5nz78UjyN2XcIeAY4BesQdGeDnbm6Elj-MTFJnaBPqNPkq_IHPiRLN3MA8qNJMb87fjfBYCuZbsGgX2xNinmoRf5vehp4LeiLk6lHNlIzG-VVhT5GHuUDPxf4RVBJY5LYwEDGORJI4ErdSUKXz0QrF6EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=kbeOVKVSQb03ULE9RCV2lIiP3JhW4OkD42Et_blSHyZXvbNxgbFOTCKghYeRAViuEmtdkX8JA5RbwEqvXuyf2l9hXOigbqFIyfeQt_PLVxflaCz7x8BLxeRqzX_QUDIw7hoD6hR80di7Hy9BsqmzAelpjCQVY86L98u0Pr_SbZcTbomM2VzJr1pNdrQUs5nz78UjyN2XcIeAY4BesQdGeDnbm6Elj-MTFJnaBPqNPkq_IHPiRLN3MA8qNJMb87fjfBYCuZbsGgX2xNinmoRf5vehp4LeiLk6lHNlIzG-VVhT5GHuUDPxf4RVBJY5LYwEDGORJI4ErdSUKXz0QrF6EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv4bXximr_iidTDGeRay6oj6vfQvqZuNhbC3oYfbMh-3hrKzTkrdxw64NtWN_iL6D_dzQtPJDy-CGFbIJOp-p9JwYGRfqT07L_qVw6lr381UA1yTGfCmyfnYGVY-Wu6mBERhSrfSh77_1HvhkhslNblKLgxIn0WytjChTSFMariQHP5q6iiYOFA_t4krobYVmgKD_AJ7VTWHpieBke9DK1Udupcw5FY0bRVex6tTF2dCWJT93WhDqGOpDcVnd00wsOrzUW1xq0fXEd2DRUqBmFaDW-mAtOzsGFVRuThttd2-k6yU-tg987u-EPI0MRMsZHqPrIGSjIkZjcvJkhnutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXVcC7ATLWoTAAcgKlfUpW1F9kUvVKOe6pAnGoqlqEDGShRBbqA1rlkRrdv0KJFTeEd9EwOKtwRLt7IgJJmTWAywTLU7VjAWfNE7Iwwsgf9XelH4ZPA5GBbpzRtaQ73msNMbTKgGxVGCxOhPPF4C8ibhZenPlIST_Sgh6zd1wkrxsd89KjowXAzV_YlPxamDndq_rO_OvqvBD1E__tp5dYKww5kE0lFmYrkYVXsZEFQvpu5dAATIzRDPmZapWKif-kMp_MwW_dzrDQCJjb3ikFihIovV-xdTg4LZ6VouVMvwJlfvGQZ5Y1DAaNR4jnZQcsmoWVPDcxCEW1nB4E7XaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=AUqsIz107HuWr4_chdCrpYBxumdJCZjWtmZno-MVSpFrIL5XxQ-VUMhj6bl88e7s1OjtYjh50kbA7UgopSoVv61arXmP7yETkkfrnh7pH8SOA2aIkmkoTaNLQnkLfFP-3Hj-JMGGbOq0FQDrlNrLkcpjShGTGRHxBKNkYx4HK8TcqowFtgEHUe9JffGy_wIb1Ai_H0htPeExgoaJNCiOw32uTYnb8OvDoPCPvkIZzlfYOiwtpD5uVtvkQ-kgH9r-glAcxaIxQInHJrN8q-MyHxfVdDyDtBV7Tx2Jq-ZqdYxDNavbi26deBirLQ3UL32DNBgv4N61DGETgs_-rTwQwgPZ0AFWr-AQZBqj0aQxoo4RQNnv_upRzDspvTbKzakPyWrACmAfgEGou16o6CvD__Y9MXh_juxmvsSicWQsvePO5vzACNmjcPTPWBZY8nN1R68O_6XRFjob0pSuhH5j36dpkwscld5TEM8DCo3C0V5dmIhS-GGo-rFD3bPuADZIAHQo1pukJ4lUrN67UxlEjZxqtDcNQJMqxvylhfVT4IQSPyypczeNV4NeIcHzbQGuRpN3IgW0MqziQTFuPBG4UOvLUOuJIPKEltRkf1EKa_t8LhUGY92hSfezOB3YyxRCCCufLeDl3L2UGXFDRHweBm60I7GZZDU4G-dINHvkZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=AUqsIz107HuWr4_chdCrpYBxumdJCZjWtmZno-MVSpFrIL5XxQ-VUMhj6bl88e7s1OjtYjh50kbA7UgopSoVv61arXmP7yETkkfrnh7pH8SOA2aIkmkoTaNLQnkLfFP-3Hj-JMGGbOq0FQDrlNrLkcpjShGTGRHxBKNkYx4HK8TcqowFtgEHUe9JffGy_wIb1Ai_H0htPeExgoaJNCiOw32uTYnb8OvDoPCPvkIZzlfYOiwtpD5uVtvkQ-kgH9r-glAcxaIxQInHJrN8q-MyHxfVdDyDtBV7Tx2Jq-ZqdYxDNavbi26deBirLQ3UL32DNBgv4N61DGETgs_-rTwQwgPZ0AFWr-AQZBqj0aQxoo4RQNnv_upRzDspvTbKzakPyWrACmAfgEGou16o6CvD__Y9MXh_juxmvsSicWQsvePO5vzACNmjcPTPWBZY8nN1R68O_6XRFjob0pSuhH5j36dpkwscld5TEM8DCo3C0V5dmIhS-GGo-rFD3bPuADZIAHQo1pukJ4lUrN67UxlEjZxqtDcNQJMqxvylhfVT4IQSPyypczeNV4NeIcHzbQGuRpN3IgW0MqziQTFuPBG4UOvLUOuJIPKEltRkf1EKa_t8LhUGY92hSfezOB3YyxRCCCufLeDl3L2UGXFDRHweBm60I7GZZDU4G-dINHvkZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nagFu65hY5USn8Dbq1fin3WZtGkJr35moOZqj9VvyhZEbdP5rrZH8t6nG3tYYIJ6YIncnf0bb2PR9PtjhVPC9xU_P5HLadTcljuTM4Rhbbdsb_tjqBLNghidMx2tJRIuIFp46xC2ekJGHMzsI2HXY17LKFj2Xu9Mf3yYySEA51sUf4PMwMkHfwEDNakrhBvrqgKd4S3lx1s_Ez0r-Xh9PPmwZHxK23iiv0we8KgTQq82WB-tU5IMT4hWBc8KSVn0yQ9wplVpW22oqSJKpMHVPfE5lKCvuVLMYNNIHiUQDxLaxJCBMg5Aa6BFAoW_B3uh2M99bRbW3msFh5ojvVBM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAI6TAD5HwjESNZhNE9OrgbDtsVo1-FfpjFDZAG8FIOSgfIszhfaKx1saD6EJM6FHfeQ12vhjkkWBpVwe3z7RlxpHKCKBQa-VmzdMECfdCT-S3Y94Rjg80yXmPwa3j7xHXSYJGNP6lFDuh0DFUwV4g6-cePwMyGb_ejwxirn_F0UjdJhJc7-3hRkbn1J5eBL-1e30TomifZyZhErwVwsGcGm8FbkYDcXtSst12cosprYYCB0-BD6vg5hJgfeB_Bj1J_BBuhmHMCp_DjrJ6o9KinbTBzfU3F2bNhLRoBcXm1pwHseuV4bPfhTdDY0uPaopCZQiN8_qhFoVhk5UgkzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y126wzKdFutMF1O0XXqpYKmnATgHH0J7eJP6iDgvyVkR0Arky9a9SQMRKX9wxAvCtmZMGcVXMqljFRWrhulKJ9hLZtFwg-V0cfK5MrtzS0eUzoH30GtOh7w24lnytookWdFH8qQDGazhPO8uRuD0-3wMgGrBHS8IZ3OqpA-VdGzqzVSkq6TLFCR1Q_fzKcMXlZL7JzlvWt8vP9BiAWR3LHVJJQWP3jTmU2myUhvN4M8d9F-RkJj79l5QU52lL2ZebH6D__GW1VlHKPB001VqGwGOuaK33aTTaKW5vRfoZ9PELatuZTaA2oYsgK65D1GF9C_ZC5EIu-3Oe5mSzYfzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcIUDJ1xFPHY7_utCd-P1d_geYIVjhBuQ4x6HtogrRE8KN9EcErT-XGMczGulbxHNElOigRMX0Py7BJg0b1V732UzmOzyQrZLZOSLoSS7qTBPeLmF_pae1ZpoPo7IbS8UKWQLpUrv1JzPmJ0MWr4kgm69EgHXS0YmSC6MJnjcVCs4eKE29y7H_Ci4g95ci3bERkWOb1g4_82LHOntGwyeYCKo4hyVqi3RK830qzMY3Afc9qTZ4moHxv_Va17LyacUmpH5iX2AUJ73DHhUd5HjzS-1b1TbhWn-ZqTMX-Fo25bi4-GruwWWSFgC5q9YnrOIjpjc7lbHhVRvqZDgp4_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Vf9k1sqW7OkZFSm04yoshws6YN-SvyDyM3NOv1DBlJqlf7sJ_c0Uz2inQ7Q5yIqX144c7o92Z_nGqtW2GYQcUr5bWKosfCVzEeGLR9Q3Gs-ToIKYMraC1yGZr8q5jJu_g1dvxD-dYLizYHd159NIwpt0Le08cJwK4enKPDVBxq2yZElmmumq9vRa_q19IOtVHM0ivStfkKq8cA8ZrcweO7uGHy0Fz0nIZEveN-stZRkc5vQehjG33XtprsQk0CrM8zGtO7Y2U--Ir5TD8YJlare9OOxz5Cqv3578Y1wLVtoe70WWdLCh6fDpWjAhKq3M2G9Zbjvd4sWEetZVbZxyrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=Vf9k1sqW7OkZFSm04yoshws6YN-SvyDyM3NOv1DBlJqlf7sJ_c0Uz2inQ7Q5yIqX144c7o92Z_nGqtW2GYQcUr5bWKosfCVzEeGLR9Q3Gs-ToIKYMraC1yGZr8q5jJu_g1dvxD-dYLizYHd159NIwpt0Le08cJwK4enKPDVBxq2yZElmmumq9vRa_q19IOtVHM0ivStfkKq8cA8ZrcweO7uGHy0Fz0nIZEveN-stZRkc5vQehjG33XtprsQk0CrM8zGtO7Y2U--Ir5TD8YJlare9OOxz5Cqv3578Y1wLVtoe70WWdLCh6fDpWjAhKq3M2G9Zbjvd4sWEetZVbZxyrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6MShhXRj3QdjIj6_ihfetb7ANHp68nTvJSH05Xt9z4avaoCCjXNrDmC_u4LUPimOnskHN9Zf6QgSUcLSo7TNJvHzBPlOhjNIsdRB4Rh8pBpGKbUC_5alNTCVETdcYoCd0Ber06cVFFH8DQuPeTbRU1IlSXDhLyQjpVO3ct23jTm43juurv5DfieWKXDL80508PnjCqoaSPHx32zUjA3PrPnNmSpuErWf9poXP-tgnt02DxKPkZAp-cFnAyl8S-7phH6zVgHj5DRDmu10bXWkIyLq66WuD_eEhijX4umMOtW4UbQjp8JbRFCa3_S8RSpIuL0_O5kWmayNZyiIPfJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvBf13qkYvjM3gmlv6rkw9N86PVRNzGvBC77kR4lHr4bu9eTV6SV-Y1rC74VNtrVykD-KSjUnpVkKQ6WF7f3IYmkRZaavPRLs3Q4W1auHZy63xS7iKh7WFwbg8VttHzwmtQOMTJL5XTAXOffonyrQwVlBhN7tMGHjmUQWhrO3iqfahqYZwLGn_TFeEIv7MQzDOIN_5aRMojrZWnjuCAnzTIljF2FlYRYFWVe5lirmzhbw99dkLpZN-jFc8Jjn-7M-hCmzMc05diYKYNDhuPBnWxo5SCEIQUqEa4E4r1nCAKNxe_qRyhKQzXMLiN8m3Lvktwwd5cDGhZ3EvTtcE7Kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_G2raid4iqIeXHEvpIdjx6JnJvrcY6ZNJfE5Li4T_FLpidW_aIcIXu5Z6q3I6vwvEbHYazuB9tlMCexazbT_qpkydkWrWadc5pbAe_8ragxXSpDbOo4pOprmnvVXb-Xzq2veNY_TEzU5cWBsolQdWDlIQYrLTDgZNET8IgGOIrUDe-UvtnKW6bC63YF60bzd93qcBKjNgdGZ5I4_LFNKlbk6AjL_2tERC1wu2Lu1svAj-9WUjLdKAPdxHPUkpuqNLgH47rWLwLdDM6gFEuM5E7cdikAfzIRJh6aioLgHyMXEJ2RCdYB3su8q_JTdWB9v8bN0nqa5AuMiS_3Z2jOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kri7vuIid8OxrSbGJIKwE_1hbTxK5iC_pnHyClweWyBL2NYLiTvf8JB5R4eiXLylh_N-3gjb3u9eycnl3tojjaeYV6AuTE_LoB_wHRKFdWz2JnzoYh4OsmxuLqCOnSM_KqrXi1c-69xq6w1l98wFbolqp1UMeMkjiig4tSTALaqhVpVesPORdKCpxbr-QLTRvQxMUYEQBmim_3xMiaVRYWtHX0KEQxiJfikijlZcVQrXljnWJi40JjF4M5x-22nR95UpJu-ZjWYCxU7Wl7eD-2pv295aZFZeE7Dg62CdAfhRgP5uDLle45lkNAW6M47ER0JsqIs7_DMSJ-OBNoJZgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML05r69nHjEHwYx6Hg88KsaNFudouhV-eOxRPmXxdEjIm14cWSTzMP8LkvSnhd4rex_4jiypUTWRMdCbGZthnUWnymXsmzS6tQWUx4FlblR-mEeleyf2UInS15zZXMA9gb135-r-KRr_7V8Rp_iHykhsMhvZpLlPYCF7xPHE2eRvHbU1HDjlCxO9naVzFtORl8ThMcu93DC9RpLCwqgxZqJN7-UPnnAqaGNIj9cLlCEfA--093AHK8yFuAtKklWBJC0bCPXTpxjYVhzvyUmrjvyw2Rkx71hHYddcpcxGS5FnylAT1XMJ_p3wBRkB69C77XlB7IV7nY3AilOdL7s0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSkhB5pbCZTaHD_66SzeRJ4I6Le-RaPmpa0evCQyHtANq27wwjCq4GjvqSEj8xrs4VcXe9qoGfmkJ0Jt0jp6na7nh_0orHSrJTwWA5nbgaWCV4cZB42a7w-mEH4aCtWmWLm84ChA3zWeVO8tLBuOqxXohsNIhH23cMKgmszuRFgBJxAubTSHl38B7n8nsn7bAqaQkeEIHV3T4cveYRYgrymPQHIvw0kTMhQsX6Baiq7UuDYy1C0uUVCkygiKQNM6v3ehorxvQbUxA9xl1d_pwW3w5OPF1LEMS8fRzz--3jWFmCgfL9AnaTU2JKz0g-S1y2HyIv_52nPMdh3IEPGeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFlayNCujQMDogFT1DjQYTIVsuE27rZ_4i8I_zmByWnsXCbrLbfCq6jOEigBCHczytp4bhueIDAHe1B8O86fEd_Sgg1CIV92bceAecx2RWJOcAvkcFYdFX8jVSQ7km64FcuQP1CQ5LFe5KDMQ0DXQme09bP4RuEB8t26x8DKh9_ScJ9GC3ctdHCFtFJQKFOiiGKjcK3MB2TC4ohOIXS2syhgFZ0qzqkLcMEoB4QFT3nxGlEWaHRTK6tYKlWr4zgsMmhK6tDurVMkhdDODCo_aZHQ6QUi9tTyet3Fq_mSgTs2SgcnkfRiDTv27H7_pU9eGi3gEgLi4kBLsH1628KJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P31-Vm6Q1E-J5l19Pd-cZJo2NZLZCyTjzr52gCydgr1WGaUeI0Wt4FFVcBQoe-pgXmpvONXLExQ3ov5lZeaALPm06hgqEzR9ZlIW6yeYT_8Q7ZupMKWkDDbNcw7jU2JXj3ME9KJ4Z8_o7o1NRRBrwW959t33ZlSEAvO-fZCQN4u3XiQxxB1MlIru-6HNL9cxek6wQwXHNTQr5TWhPdTQNlrGpBv7bur4X0foHrfYOvYOhBkS7VGeVuvc6irg3Py18SNIX2BwkmSwitxdjh4hTUs1n8SsE9sG9BwZpY9g1wbS2Cd_9m0h2MMErMUWq60nbO4tzisG3UXVkDkLR6FYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twh3cq2OS944qsYWhF7D57HluRu00qN9uIgjFsqtxpQ1BQNd7kzKNdjcTZS3QjRCGOCcVZECwy4xtX_RuLzUnATLApHuG9hZXxSy424dHSM9cgzImVZQ6t84huQ9fr4Kq9HXXOeYHoiBB2C9m6-NEU3TxD0bIuOUx-Vvrx07G3QPcALoLDhCwck0GX2quLPMlwLSgIVXaJPgWzIwJpvHh8Hj9CTfinCcRK8xQWS9PXXNYUKcTDO--e9sbbNfrD1DJYi1M-PDaYuyBo0MjtMMt-XsMDqx0pWX-Qarjktn41j9qymqVeqOKHvcZfIoQ_u2Rc5fMFdAjinrEQ_PcGlsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ6MXd9693YaeWQdbSDmMJz-LPIZEQl-fqWSM6LsjMND8BC3Q-T1eDjdv-SA2LDTPGLgkvKat8UX6C_AOXULEWfciEJFHWPaSHRS1gT46z8MfETgK02oNE8ynoPo7l8-9fYxrWUebOFTngDgSK_1iQnDFIcvR_RpaTwL7NclizGKNlb-YMj0MgFjt6Q5dt2aw_MACEqxazKaQGZnAy3oLzqCf5gSAT_R8o2lJYSWL02Is-nFcZaIsO6UT3K6I1xsI6k7CEgrbx4HHMZKAvylmiNdVaxm2meNFGsdZBkHssT8o6WyaHdW3AaE1BRMLSi6n39EDisOAMP3vX4uoVdWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4_zHcjTwo34OM7sKFPzzhlK3eZM8bU4uyGw6aBnlB4jGGCpcrot1NSBAO6IxxCBnsXBIfo8QuFBoZ7PDvsCwBrIG9NID6MOl6QAjVH5qqmRaZ1x_4r2plOXvp5_4IXV_BEOa5qzCMrXqnO2xJ4RP04OF5Ev1aQHSTflAt9mf5j413Zb74qwIuDr_og8pXtrSJkPOkkssI_2yCvT_8d2HDAo3KA3S9_RSP_evWiZla2CEzS2vg3Ce6nH-_bahuDRjZ_aKp1fR-J4z4mNokfZLbqFyDw6Uji9rZ2WQtMIIEFaEqvp2WVRx29m8zBY7Ov7-1V6WpjFvPAVYr0IjRAzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veue7PiDmn1BSJn3cemRu1ilfQp4dAKlwSy_Dke0eNTz3V5XKiqN6W41iYKimuMsVOxFa4TA9PHZoZ84ug18u3VzSByD2r3o0bsBxu6AdPFTWVLSZ_wRHDbD39Mc8X2zvHNsU9zPcAm8TMBSqP9Bg6CyOj9mRj0Q8dg8UpjCEm1RnIL7AaQHkSm-R1CTgYdFVw5jFv1CNslJWBgzpRydDtWe7cp8l8sMCz9A_wF1Lh_2ARYlosanXtl2cmmqMXIh2L45mUkxsdTVC6c7ybWV1vm5bmD9n_yfxMJUVHJDY8NpXRzkq6fCx0z_WLL_vXnzkirJSr67BSDthw1fWdKEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG75Q_Z_MTWeIXDp8o6i_OjgVkw4PTjeK4xCKEkA5xEQLpojfGg5P2LmoaztvbBVexx8y-uXYcOSgguXrLBshF1wxR1O-BhfTyxQKmJepaHajxelnW9luJuy3Q9o0DghRVwbW8zgpHD9632WXnOsgWNYAsQxk8QUcMdB7Gh-zppI95nnkA_SnKH6Q8FeZnSDcxdeyQhB63MWcsNKxXHQSfy9wlCVQnaHSZb-kFl7kFlaq1A4qqR-sL9dPDzGYj3WZvkxzgH430iXFsmKMWJF3sELzJyaZrEb5fcwpOIc3LhdwXSU4ifAB1Jf1gyPGHRxR97Duu2HlEmCvfT_7Jr1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H94ZXhLl8GbyaIYE5GWS11yOpHO1tKLYg2O49HfPMEA4_O25GF_cFR_IrvhrC3pSOET-BYOPxEDlXGxudJpDUZcvOTUUrFucZZHkme0dkUlZY1LGo3qllYgqYi7ASpec26kAJlU8sn0VYQVzW-lN7cHjgcLWhyQnwg8N0CwdqtS20i-B4TXx6KGjGYJs3BM3UdbTBQy3P7UnFBr8KzAl92I3EEL8OlDJ7HT6Ov-TYLJeQxC6D_2BrP2Fl1B5QSJkLIYt2BJLBBJug-lnGjTRDqDF_GjfWEKaX5H4IZAymk6aD6jubZX0q8M6JkrkfwrWZC_5fDLSCWttuY15jlb_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6TC06kASfQ2oJtr9rp3DZJ0v-Qiu0sKNmsR-ZQno_bxOq5AlHqAooVYt2ekP9oFpJFlvXEQUZnMnunCo3mJ-hzmP8biuE6UnK8O8kHSWDTDoVVS16lZ7rWdyBEC1J_vRH_Nwd6q7BdoAW_RMY7-rg6ajfrZA7xUwv0Ce9PPPq_CsA7XS1_RB8u82PMNWZXq66ocU7rRPxeZ8VsXuJNEtl5eRjk_oZDwwp194HgP3Xs0KOx7rTijynja938NnOQ_JS0G3GLIodyR77RdnZt3Bu5gq-Cl3VYQmTu5YqjaEWOayEc-QJBLlt8n8tbGMfojgQiCL64Skl7D2NqTYAOMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le0Pk-iQo1izrhWBnJJTa1ZVz6ZotBWXwiE8hcK2B8SYSQztt9ydGnuu7gp04EzqxFYqro4yyPdQwLUiIfMSkixUu6TkYPAAi0PnU0dW6rcdevuwnitjzhvVLYvSa17-ZtMtd2lRSQgIDYNb90OWvEi5Yk0FOnv5vibAjfpUZn1idMoau2UWK-hiWzNK0KvNbSmVYcz6PIAprvNXiB5_Wxq9jwP0g_foPd1r7XEhcLsANGVnB7je30ICcAblJhXBEQH8Yb3fJDDYz7UydsKPXKiKwyfzHZEcnjTyFsYsD_C_qIF81p-1tYmVdZ5D2RoklXLKTKhoXTipT9O9P_3txQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AHxu4-pS0tHJU--rsmDdO195m8boLTMzDEeUucJB6ZDccLl9Znd1NExTKGWEz4RBGzJD6Wt3TBd3HqP8CG1hJcMjzFKQMt7HmI7r8s7kUQ1Oe9ASD25nwCgcIetVFaGS8Fktn-HcmXpk3Ufw_D8WYAz-Tx0wuOzZvvscH2vPgken4U_gasStuUizKMiQz1yHB3QMYLzbcWA6YepkJ6KDx8Iv-keoHcMRBXJag0VOOUhOh5b8cOm5cLejnJuJfT2SNKd5KT5BbUzCy9TQbPBnYnt-NllZB1tZlG00PKkhixknMjnC5FT2-wBvp9_DXoz6uZ7btolMGn3aX8KkQLcFfiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AHxu4-pS0tHJU--rsmDdO195m8boLTMzDEeUucJB6ZDccLl9Znd1NExTKGWEz4RBGzJD6Wt3TBd3HqP8CG1hJcMjzFKQMt7HmI7r8s7kUQ1Oe9ASD25nwCgcIetVFaGS8Fktn-HcmXpk3Ufw_D8WYAz-Tx0wuOzZvvscH2vPgken4U_gasStuUizKMiQz1yHB3QMYLzbcWA6YepkJ6KDx8Iv-keoHcMRBXJag0VOOUhOh5b8cOm5cLejnJuJfT2SNKd5KT5BbUzCy9TQbPBnYnt-NllZB1tZlG00PKkhixknMjnC5FT2-wBvp9_DXoz6uZ7btolMGn3aX8KkQLcFfiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=Cipg1wVGeibbyI8KIsAw0cICzXt-erDJyrm8tEzKRA40t_iuYAbQPY0pMD1b7KTydaPwy_5jfi25GPbT7zyDGLUWrn_ozbfl-jb9A3G-Toxd-OqqvlRkpsmeViZpUnlNDwkBDcWpGTGvBviqT2XLkx4ry_JPi9Eod93cAhhs3BQ2y8WpOeDtRaYEi3HrJoEoXtaWgObLdEU9j2bxWz3slED06Qp9yE7khafQKLFJYi27H1r0r-Lh4KMWiFWomqWmjLjXSp_fQ5F3GGAFE6QtYRJ4wjW9qqEasCxPh0-PofiKO1_JAMVkr18mj8if0GlryLtECJmg7TwSerM0I21uiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=Cipg1wVGeibbyI8KIsAw0cICzXt-erDJyrm8tEzKRA40t_iuYAbQPY0pMD1b7KTydaPwy_5jfi25GPbT7zyDGLUWrn_ozbfl-jb9A3G-Toxd-OqqvlRkpsmeViZpUnlNDwkBDcWpGTGvBviqT2XLkx4ry_JPi9Eod93cAhhs3BQ2y8WpOeDtRaYEi3HrJoEoXtaWgObLdEU9j2bxWz3slED06Qp9yE7khafQKLFJYi27H1r0r-Lh4KMWiFWomqWmjLjXSp_fQ5F3GGAFE6QtYRJ4wjW9qqEasCxPh0-PofiKO1_JAMVkr18mj8if0GlryLtECJmg7TwSerM0I21uiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsOBkRnhXBmA8GPf5XJnQPIGie66H4PRb2YnBZSVGVMszlksas-nCpY_Ya4aEOXHtDhSyRnct9e5Ip7gBdE0erqZ7QaKrdue3tJ5thGpJs3z7QYyeeN2YDAANSvn0oJbB5NsiLdV9Moht-_-swCh6ol0etTWoKh7jLCbAA6611fwhmVldFfSL36bFJ_CkUYXAkmz0kyw-i4Ow5fImFlJHVoLINzsp-2MI2PwbqOyC093PyGt2_D22LKUYM-t7UXdoIUka-zWcwgMCmEDNjo-RnxS3rGdbVYI7zhwrWwhBOEYH_E-P406yRZ-AULGzEg-ag5fxcGmGokvdk5DUF7ndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib8RaKSHLZlrQRfwtNF8tJlwf9r1vDYEw6b24KoUeUFrpTVBdHl-eROK8X_nBiESRXqBkj1HXnRtGC0O0fJ8WpwTALBfBSsHKQ8PQ6dzcBTaO_jlOm59u6tzexvvFlL-z3_ShQawoIkxRcYFNNMFQeBgZSLUja1GEsfq4hZs_DrzFNdbQgtaUCT22NraUfSP2JinOSOtcp-3cACQuGtdvv67FnTEF5DJFzUG5HEKLiNxcnytkkoLYMniQA4EZoACSXopsaFSdAza-ugmne7ikDH3yj3e_usUcoHufwPwGWbI84eEu3q6mqMCDUMWpjaNZ83QEiiV0He1dczkcUzLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMSoM-XYt7symGzq1pP1vzmXIX-q7OznRM6LtBqBXZprt1ru_0NmkmpohUjvD4r-bxIEd7HCPrOgjVY_HT531ixmINiLv3UGYhw2AstS_iINH3zpvA712knWLDjt3JgKxtlCBsb4_HFJO-2sfYypaal_dytOch1954DtDdbC6l0sLCdquU6rQ6RfduhCoyYPCebun1PUqbIAPqoZzDOddqlE8KVxNRJm7o7F-EZmbobBcnB5Zl-EgAvxRMi23zkPQGQei-mcvwwoJRydmx3Lq3rPAa76xQ7C1AIw-tTH8n0SbY1nopnl1P-rOViHVyX6qWWKJCxHh1HGZO2bMXxxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxaGEodrjWDw6kqMe7snCcknRKYz1wO4m4J5guswQ7D_ZZhWfCu3b2LlylPPaDzz_kNYy9mhVl4Vvctv_muHl18PE-O6O1L3wTeJ7XdQAsIfgOPXajHbnfxK4UA7EB29g-yLulRjDup7BTJ11F6I38uMD16_qRxO8D7s3YwM_dqCcgLlT1eX9Omz2tUXoncLqskQPzupnW1joLCkArLkJO6h3qIQLrQdLAxrVJvElbVa-a1Q2eBNwVbdMlfZuWJrso3ryfxAHq54QmFDQ80Wy3HTcT94xi5ooPiotoBcnNYMiV_6iFb02RI7_wGXi-xe68BQYWkGLKVIYp2MXdMJHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIs1GDYZ0mWjvDQLTD9jYwT0umqByS5_ntU8fvHJsdk8KmW7lKpszWSnte8uGQQhcb8sgDFVvOasWZD4fcY7N6AETUQDjT3eLYXZ9Lsuurqgwwci9ugsVXyICRHp63JE8BAkoVdFdWMaYgdAbcIzDU-KdI-j0IAq29bAeHFv8HeW7sxIQx24GORmERIGDz-gH-iL5_fTi2LxE4W_FGFKC0Z6B_m0fcHWL1eLlCybMZhXDh154jyU0gUGZyJfOoAz21rTDCWUjhcK6Yl4hu0fC4Z3vtWpN3Bqvq8mnkkcdYZUtrWxE82DdkaZQHz4BqxWDjc3vXpMM1YKqwoxMJ0cIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-5kFL2pSDThyTlSgSCyfVcizwaaTg95_Q2ylWlSV6gpQhu6PAwdGAN-Pqf7JHBIUrcdmP28tn1ePpjpvmQcmhBNbLuwmuDK4xX3c8fQIrlfjyaN1APPUJPSmZDMCjLj99Qj5umIxKPh7XNWzGzQj0R8BmVWEgOd4vBV3--BsXWQlonieR-89-u4jVIzPlI2DfJLSHpW_NFDnlrvXx5Vss6UD8ljgl6NQjOF7wHANvoLuuHa54y9rWUkHwtaMXkIqWsE0s-pfQ80LQM_UenvkaEMJdblNa59_l4--5lKIxXnFvbKC8u96NEwdc3oOfbMP2PXv5wwcQwsP4kAh7jD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERIVPQ47Hz-Q2RRKWHQTGTuUCgTcS0WjTasmPN7Mp0-DPI0Z9lTUhUgsVlhfFJ1WGn4csgCzf_RHiTXQwunNKekZJvR1WIBnoy7iZCYOF1XrqloHK2_NFCWBj59u28ebagPpiRbXLHdZFdf5iHFLXgiV2xzjStkOpEBNf29nNmvFQUxprZVz4pUqXauCdZ4O4rgODuhLK4E6eFycMZYj_KpvIuR6ekq-LKrzx0npvgGeiQtPIwFBFdUhylwPAtmoM3hFnhVD3wiEawleJOQ8fW4Tg63m640Fvz2eJWzn7Puqe7MZF719A3T7yoGKRPqKOjwVVNODV35YeUWJ4oXbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhyfSxirHxFM6KxBNm5bnlIlQfdjQbf43iOeDhqMzQW8mZhM7r4vO4BDWFLH4bQk98qoiXdsSGdk65ykVrHF4NEZNOzYXLoMSErDjBUih9RYOb37CzFteqb5JAqX5tz6Csf81GYd1j1o10yy0D4zII1iPcQMjsLjpsUB3q0tV57kVaNb6fB-MWu_Ma7TRM4ObQyn3Pb4Yd-cVlRRWQ2ChTg9-CcensO-eHU4l5SSP6ljZDqrp8kMUMVU992fJwlbTwT1SxutPKhQSehrW2P602aFHxR-L4zYR21U07ujwBIpcBikSIkKLSfDmh4AoKLgdlwFBPPCY4k2IJsFiwd4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkAm93iTmM-ueXlyNjoqV9trfVzdMbBps9WsN4NluynMy1EoYUf_cX90vGMKT_3a2h1LVX92PKQlf0Tw7I6g5dQxh97X_w6u13Egd_3lf0-FeoKq-usSXZ1HgLUIgQNFp0hXu1Q5yI6wv98JVe71_SUSbifB-hShnWF9cagxqrFdjXQHZxo1pcMw4ZI51Iyk2oL7M2Nv3elFrAJwy4EFBtI0mN2aPKqbdrTUEYIjUpCj2qyXcrKbhGlPnNB7j3AwnYwUyNilZQUARyWxp5v9pM4scEi1XRZcHOHBE2IIjTwPy1jXa-W-l1j4ZxIlqdlJ7ACFzyooLx4BGlki7kklIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeSuE0coNrKcR42yGg333uqg8C-EqRGEmCs83TItxjY6wbSvSGFVvE-vu8GxDoy2UOXRmMkmXLu_9oIUY0uvqpS4Dvq8Zgofnm0o7MKZKZyzbcWDv0v5hfNbNexlRmLuGUVzpkbRDjokBvmffY_2dU7tl8E7pW-jM_NARoR1cJj8fz1qZBN4jgMaY7jej1gXz7DGiTL7leTn56DOnOzW3Y5Iwrk_KG176-BjXiyhhd5QGyX-eHLhfD-TDw4SVkUWyJkaxbnlwIG3_JXWnMTvbLC0VU_RtDjc2yT6mfWKvK1txFWzG9kijeIb6tOplryQN7oJW8JOc_ojIgPQTBksVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=M_Yz0be_0pW-K_GA1eqRq8zp_5btNSg0KK4iQdFMGE0H5EBZWJ2G38U-FkKx3tHxwYusFpKt9EMXHMs0N_MGkSdFwQjMhpDIoBnH7irFF0QOx_UfBY5xPB3N5pz6Tj0gd0MorH-kSsLVpv5RSfi5B7KOHtQZyz03f5xoi4P2Oi81g_2UVinf6hRaaHm5dX0fa-6xXgnpwm5p-YkxzYeA9WQnV-BgqcX7B_fd6gefk9mgSURIRDIprVG9d_JuCyBrErbVrJYXnAoWOjC_yYUBEgMLtKZKEPpcUQfq9gIkp29ulfcMijchxSYL4mGA_zEngfb-HA2mA9xS66P1KFlVJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=M_Yz0be_0pW-K_GA1eqRq8zp_5btNSg0KK4iQdFMGE0H5EBZWJ2G38U-FkKx3tHxwYusFpKt9EMXHMs0N_MGkSdFwQjMhpDIoBnH7irFF0QOx_UfBY5xPB3N5pz6Tj0gd0MorH-kSsLVpv5RSfi5B7KOHtQZyz03f5xoi4P2Oi81g_2UVinf6hRaaHm5dX0fa-6xXgnpwm5p-YkxzYeA9WQnV-BgqcX7B_fd6gefk9mgSURIRDIprVG9d_JuCyBrErbVrJYXnAoWOjC_yYUBEgMLtKZKEPpcUQfq9gIkp29ulfcMijchxSYL4mGA_zEngfb-HA2mA9xS66P1KFlVJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1_IJG_InTtUrREBPIDyQ1UhXBC1sbt1Jn2gG44IsxxowevoGoGPxB2oKhwPvF-aux_Jv3OIVamuky7vhxA3VT3f0_fLNmXDUqO_NxYomHLFnWW8oAuSTXK1gaiKBzQw4KP2uZ83eW5Fv3OPqQNNkHZj7y9qOrvGMIU9tHJhsvuM5ItSXfU4czcgUFpAQJfvHgKyITlCJQfCErDF9DPxQxk1mu3dFwH14kc9pe0ALf0KBS6yr08tXz9CLR_vg5sy28fuJlNPuebNdhAc7uQuXEV-7hFRCsrzh_wC523RN_3S_WAjaRzryb8GR0d2w8UfN1oyrglfTD4gBqeH0PvlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tE81jerZjpSX4gICdvIVfdKBegeTCCb59BS5KiO69tmAN09WG1oWJSffeb5_WyPRtfQSXsawhx54wk5AQIsTJOjdnbczrmMfGEEYupdWWycNgraIQP5FaXsfcAceSkpKiTBRo3j8F6a7fuuuf-I0CSRWlI8nzPtK0xYc5IhkjHX_fu8OswznmPitDuiyUrRzKC0Je31Q1HX4Q13cjvLv7CK0-BLAjdPa0G_s03S3fXqvPDeYOY4y6M5S7rWiex-eeymyvdRe1U8hQYunJ13Gg6s8Dnv_GdketXsf3Dl2FKvlPqU06RqEVY8gw1uCKBJbYPsEpG2XxO8EeitEBueQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5wKGMiGRPR2VAZ-1HGuhgjJldX1KSVTDH_o-kB7SxoEpq33HLkVtlwbIYUiISInurRNEZmsIHOeX36qcq8kMURvWmSpN3TNTROoys2EUAlLYlj-4SwUXLMprhpU01qamY4puGhQsPbg7ZE4k2Je6Z12Fqi48wlB2lXdxfaBZiiIcWqqgZN9jwYuTAcXYnHMKd3OuRXDy_dgvP5erIVGrr0CtgHu5P2C4wBycbzf7KsTyRhanmd3gLuYfu0tcgaQi3z5j9X2ibN-m9sv1YE3ShPt7Drunq9ReclaNZwUcTGaznlYD6l14yMvXqPdkJJvmxpWmfgNj7W9c0FWJz082g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgxeqdGzQpUoYnesW4vZoLBsujqFPY2UCVgHImTmFyjgBQezdVJclOdJKiecIcfxbCr1WY2olyddkhyHmeDt_VVYRXLBLwuFLcMAPLOvme0YNtDOUeF5UB35x5ASaAWFepR9z9TzAPpozMJ9uH9EleDBAG6JL1-_gWitptn5d2dBxQ60497njYHPvjxQqaPZNbqj0H778BRGF3EJsZORB47udILwGjOUJt__tFcdUu8-SwgiGVE0wqVDpqaMxN9KnKA2Wn0yGjIDE_Hx6fbG_rkCHKAuDMHBDCsco4niUR47qyrrKECGUCT7-df_0CtXqXE1GvcJIDpT7GWZSfG_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzMETPdTpnggIHHltggW73o6MGd8hROacgr9tZNXOLwdJ8oD56lUQIDxDIkrUtvd2b3uqP3WHHWsnbtJ2NshTwin0mvo3W08zKKSfZZCOAjbTA6jWME3HOwEnOwb9JsxU28XsxsN1H6B2Dzg-MVcvZWSWCDCQuKdlAZerKP6YuqywYsN5inCFc0Za35gG0NNJpoXb58OFOqZ3JmKLe0f6b4fzKEOFXKPAiamNIyVM7VGJhK9hTpvGDQu282gwmi79gwqheHKdvdeQrLukjf_gl7U5wMHnLnZqldswsCxA4hWJaP3sVCit7jq2IV-Zvo4XRiLxAqikL2EUm06wt6D7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4i4WuGYQpWzEBoZ88KmzMdIBQWuvhjmsyYBqErvjMAK-HqDu3t6Tbv3vgNMLOyPRZKXkwKmmviYtrtYHkO1NMooN20i2of6FbuUb33olWwMdsJtNxwXpy09gOBlliz7fPDMxL-TO2tcTm4cKUMFbL5tbwhctlowmTWESh1q-fGExvsgjI_X72eRpZpXIdQJZwZGurpSnNHzRejdlxNAU6Sr7l_IQ71WGOFHszXPJjOIyaTIT9bmNg13U2Pqp10xDRFu_x36OyRWEU7xTku3LLiBEhhuQzaRcW8OueDzvjK9inu4UlW75ntCeAA0um-0UKk33G0KdHQj1FApOhQFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM7wtnEQDYSQJH6p8P_rd8wTbl0JG6uq3hH6Fw3OGx6se9DARQKrYIxr_KUgvtiNl-23oP4vWfoRB_cVvpPI7PMAb-BbN_inx0ldoWnIppUO-tB2rKVyoZn_aonc9EJXL5lkDsu83B8ERjtH_WYvJjOpmsdCffDOEVb_zH4W3AlTiP39nVoxbO0H3lMORCjlgdHJa98q_-BvvVmhSx_WzhsysC2XuXa-4Fs81CO7__fD0zQiRVkYqMI32NEiomQGiDqGx0UBRKQCLsjMU4bpm3gHzau4tkEvB9qlPIS9X5ifKozmgXOv4TuD-WoNxrfKSl11vL1-9Pe5MEgknP_TGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBZ8D3EIz7KcWdLK__KU5Z8DGUlfHWX5O_JPBlvtJpji3E1F5ixzzZhEctcBau5IhdTNofgUlORdyAGZvj71dvUCjRmWt-M-6hIaZym1_YEVesraCTNu_grcwZqavdEmKNUwB3R3qZzdHHnzSZrd2WmAULRw7gaAM5dVABI8hYQBGZGzwDfcvgxXpSALD_P0ZWt1cpLbGnv9YOm4WbADEdnrA560azFqWIyf7Rn1R9NmEK5Y16WD_psbWhsJgo2vEUjMJ_Ik64_4ZZrRdDcJQWsxfOE9y6F84y5O1svwN7o4YC9umCv99DmzVeJt-1Kb8yy77qCwi2beF1v76dRcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhXo_0k6t48CAtcCxnAbybIfyOS0muN75odf2o83pHSu6-QB1UeT6KzrH4dYsL8uTTUSFP-dpvJD-10eERY9dw2ASfAJyYsfJ67uS9clH6FRnF2PQFhmkV1RAbHPo5H3raShKpMwNAkmiUHYBJMJr_cBMRupdVfejDUkH54dFG_MQJD8CB2PvjL9_lWzLUkL6nckee4czT0U6Cg5dUwXjHlpIC8HhKQ9sUDhwy8Pe3du4kn6w-AfzfTTSADu62PFycZk2863iS4lZsK8nqtX1qwRP6oawrjgXLHfcB2JQhA3S1CwtFfci6dCyO0Gsog6nDQgVW7ixTkN7AacO23lIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQwqg7iJ13zvJ1qsVcB-KDLxN5WpNOkAAcHsu5mEiXjkRueyHOMXgBm9o3SkDVS1ViYWFSLxNomKCKPprBle89S-fw_MAxDQTc-7HRXfI5QCxEYgTuse1JA0TfvO05TboIRfh5RKJyVLB7EiEKAzeZ4Ye_5CeLz_IIzVt2n7SwK8mkqIEtKuY3MHu-T6tEmPFTbExesbzq7rKkl6vuq24JjviQ1Mi4cL46Kg0IoH9a3Qb_oQiejiEpd56h3zNCXwUf_ysFt0Rdde7UfQLA04_CKDBolv4K66dpO2Nhs7nYEAjAYWYXPWp7qaJSLsPfWcwk05VeNSLPV9SbTkIV7y3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcmOadSRvS1AWwBwsZwTUF3aaTtZSJiARy04CXIvASCqFKnZQkFZdN__5YlffbadocAnjDMQoyWMCPN9wFXBBK-QIiU3qNEGxxf0geUw2Yd_whIz2744xteNC5pyzyKYL8FBjY5A0lHUDmtRJs07Pc6SyUMDhA8YmrudGkXHD096IOPO5XZifWCzifWxA4_ukZRIXWEpGRvTbs327Rf0GRvxeyooJDH7gK9eKf3Fh1Hb_1u9ih8Br7D3zag3ccKLNxIbevKw7fbR9xHBzA8FNS_5SF6tiYMQ6oTQ7Ge296C7_AGNUie8uZ46ZIfkf-FJCQX-Ta9VKaFW7Q6iAblc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY9x27oiXBQ2VmcHTc2TsF7umRjNP6xf8sxGZlbzkEfE-x7F_f71cj21czqGY1Y0as8uqARMBq4Q9Le7j_O3rNLtnweAvPWLfa-TDlQ9LJEKgg6aQQ8ACYvvtHeIpdidiSFWIO7miLAufcu-uGn6z1c2MsEAjXU4J8PWdpQDNdiN9afSYY1BuN7WwObC-R5c0I2fKxhBtGYOqfccWUZ2C4rwKz4rCipmaUmXdkHosmDOjZWwURhhcsoDxFrmUi2MckApzBxQeiw8SiL3Ahf1xSh2E-iF9UsHc1_NnFsA4n-MUhaF_-dP6sttblEkOihe4ABuPWzvC0vzaA_7slOLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKRS2N9V5ZqY_VckwXnkmrw-B5ksLsZNLPFF7g6G14fN8NvkLrcSOPKK7_cIxiSVLSuvDeJqNFD_H_femZKwN89oef55DEdDKq7joUSoCSj7fv0HVKauEI07W5HJMyeg7krzNrfzKVW4Kp-ikj8FYycaXTLjSMsx8PFbt1apUWCaEim4PEIxwtr4gZUYVLZJrnwbekgz54u2kQ8D-KhcoPCz4aglveSu2PQ63CtZaCjoKTMd0AaubhLyqPLJ--ZH5Nh3E41V7iW8AC3nu6CMtjC0Q-xOPFkDCgXGZvQrOW0Gtzdh5upcd0Am5QR6AbkCa-j1WlCaimVZAkl4etP49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhPdeuV6nNUfp1Iez3_snPjaXa5OlK-0R1DHYETPaegiw8PDYDaKhmxCC7ArQM14zX25JJQ_lZRi80z0cLCNiyWnr30aftNCBIoUqVfMrJCtFjeQUinVXXZTTmdmvkrie0lXbNOtwazJXcrDhnyIuOMpexrD_j_pTzbfzCucm2Mjjap1vsabn4802jJL1Mh5Ol-NfDLZ308LH1hHBGXCrn5binq17_3bhn74fczYRhZPVIomWumYuXvp3tloiHOk94JbHaEuxkoAAo2ka1zG2r6QBJTSE5suUVgApE68CwD-NzPWglvpUdA3MExj8T35OJKxS8jIXGGh-vQx2P6DCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqFHveSmyQnRoRmYUnmuHaycA8s71cgcC8Usgz07n0mSW1Jy62YuMohW8rGi1LJIJxk8t7WuoHr1AqxxWhIrbSJ94JpK_EUJyn3kQUexFYtxilEpOpLE--gudUBX5IDtqJlBdPMC5PyuIJ1S6cvsMcyQwfS-NJSyc2fEhOBDsbZmtfun-yORGXO3h_Zq3SSZ2-v-OmR0YM5Xs93E36ZG32XBtHtRcuYnRGHmf_kCCHYEKi-y5GG7xlazxFGe5V-8I5qddRf8vo3iwnsFTZCqHKRicanZVlUvQhlzwbpzi4wKaRQyJkuJMx4_fV8i_TMkz0l7EXkZFLalz-HH-HluVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me_rCg235NIlnNsYA0VochXo1lNRutxsUAzH8biFQnNaNA7LWYhFU_S5zLwsPLVIZGnnTtv6mrJO3eWeh2CZNTrtgcdeJ-YnQkkEi0xWn_vOjqP0JvQd6HzTEzoDnzzWRdCp2_6HZoVnhI1rNB9lkxejFs7zGPMt0qmCTmE28QnVCp4Gocflqz5QNkV6C-JhT2XgXzUJfbt-Plu9tyDfKyi3s0UO2VMYVxasDdvFMp7m3fmoTzOTCFe_qAJ3JtT8pdHi291JMVPnNjlwdPt_REjaaWBnmcEyD4TTuyl2Bkkzxm9n9vvwDSGBU8AstCE0c6IQdUeXo2z62cNpHHQ5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vlg5nHT92dvE1wi1P03zexAD1goDBZAklEAEBCigYvamk7709-acz1OUXoPwtxJsofjkvlHUKe55rV78RgLqGI10NP1zfy1r2jQKIGM4jrSTZhLRyEHWGGKskLxeggNAkwOXRBJVzd0Bx5oDtyQwnnULK03NZWg5u4KsbtZPv11T318Ki6ej4OdslpCLRRdBxgie87niSb6ns3NYSwmi6blYzsQfDPN8_R7sJ2DmRUfveKTRsoJyYuITNXkE6kjFJw9vNUQYczdYdsoEermCvYZOUn4YitOCgscIiZBJEROsjFMhdpLzWEjKERMuNIFm29bV1RUKldqKhAdKLazD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDt05TTwBdnBTOhQu0axbfjmzrdE4kxFx4dPMy-2danfkxUfUm3GMQTyZtagWjgOvhAjrw_c9CuBe00nJEra_uygG7SqfXvsp9JJuqqk3eaTxdbDhEOKY3fR3IigWkQKYRUEqNKzEsSOkP57vhlOKSmPnWKvgMzy30IKnIj-H_NCI-rTc-D1qPkeZZ2Ju8JLoBmHOnSWV_IBLNy1b_Y_1tjyW2640qlZHFVgg57binrS0u5DGi3jclrbmkaYn73iDX8Vg6hFE2v_sPv8rBPw48Ei-bBQX0PDSBF1tbaTf1hTJbWCVgxZAEdw3xKR-9Xq0gQukzbhG3NmlTmhRyOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSMWV-CTmeCaDG6RWUAnHyhrK8_FyuYDIc2fe2yQzhvPBKpkVE9uY-ajU1QFdV0jJvEPgk9ZCRr-QAFDY2iP2lZo3pfYIq15A-lQ6vTWiZ3N4okfimxn6LdhhGKx60E6xDBNJFTgK1zNpvDc5xn1ab9bPahqijpzTg5sg9_NzLnHIaiRLwfQzfTlqealF1XZjwoU2aINZ0JiZXVbEqnMx_pQv7Dhkz9fLpa-w8pGMyGMLuAj38DFSslGgk6429nWmisl1loxHGwi__TIPF72dWrx7kntZkoVQqNxUwfGCuctJHop4kxoO3qByJpR3Z9ZXOnuu4k-ZzWPv-hd-yLMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXjOcPrR5Xtz0crtYfXDtoZ4VdlFtOg2-OjJO3Z_nbKQ9nsT73CVikoRgdtXJ98AHFWfC8OB0O2IXJjVz7Og26niwgzccComJuVH_cskL2DdJ_86ses6BPWi9paxXwl_oS6EmjwkOZ_rjdRLRnUSZfJjd5VVAuFIyFQA1eJHwCpGgS43w_QzRZsZBeRsBSYoxEx5PjzoAo5FSo6t6wLx2vU9UsCIorpmGhCfsF1zq24gmqfmrrfMbBZdPqB06JOHnyD_rqw3gTPPDS0w76UJ-62DWMz7o5GVGnxsmILCkVGp5dWKYPgsVD6hKtCqgzTnGrkX9LHbXDYsuLBphiI-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Wl256gaAhD7OFbjzO_TnyRHWQQoM_zLM8ClxkforJk9UyXsZSuVWAaWg8L6iKSshuXvSWxZt0BXFy0fc8RAZN6403x0YJJgL9V3fyris6LJakflRzfYBgF54VyVvw382tcRyerXYvS5S7R0igVMNtzly6pMR8d6_JmWQieOLqQ8ZvBD7lcVOxjWEEMlLlLELKHw2NwcnY841nhN5CUsKNeiM_YEIafXgKWHbXRXzwnqOlwoKnV-oPIuQimzeUzAAfj5pvUQIs0dwg4JM7yZJYcKjPPACcgBuhLkkq2Jvu6lhulGEeCRDRS1cFSbA3DEpmaL5SUpVE8XDBnS_uiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R34459o3T3mx8OapJ7BQr0XJedGEfaaLeDN5YkyawiYeQHstyrGQU7wo2YFUlc5vCg4rMrJU9nAFyHEF3BVyq8o77GD8EqZpDNd75Pxc_npFTeXRIaZFE1VvmDYb0Z25JLZGbal-jYJUynuPz2EaBp-HP5xoh5uP65Sus0Y8bxxZ8J3ZJFuFmfmTKAkwdivV8K6NhGih7oz0XuiWTNTfxfVDc_hCaBBS5LgYVwS6e66behNUJ5WVGvcBSTRik5zL1Sva2SEB1phQskuGj7d2nvPPQfpVidMoTfGpCFFz24l77X4WyLIQk0TGDMR09DMcrBpcIqcUvuRhwySJ3XgjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Ud8O5KL4-1aWTzgJeOSbVgx8Ms4o75Rm9K0luZMwgPI1dW0UxvMkCPIrnN14jCaCZt-FobvO0JQUFHgQxaqbye2VA7wRqb1WayEmPd0k12FrhoEgwCeePJH683OQKf1aL-nRXpRhwiP9usoWLbVKqMgKiRNvH0yA9ZCerFxg3i5oPtwkWViAXExQO3H7LQVl6Xss--OygFHKiLhYmIo0z5ecC0EpiL-v1Q9czyJ6haCGigt16GPlxkPDpi5heCN04F6lZw-d9XYaXgt6R9hac-Wp6_jpfW5WEPnmLazXDwWcDt8tlzRcBGboCZnjASMgb-ehd3zGu-RABqOElZsQ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Ud8O5KL4-1aWTzgJeOSbVgx8Ms4o75Rm9K0luZMwgPI1dW0UxvMkCPIrnN14jCaCZt-FobvO0JQUFHgQxaqbye2VA7wRqb1WayEmPd0k12FrhoEgwCeePJH683OQKf1aL-nRXpRhwiP9usoWLbVKqMgKiRNvH0yA9ZCerFxg3i5oPtwkWViAXExQO3H7LQVl6Xss--OygFHKiLhYmIo0z5ecC0EpiL-v1Q9czyJ6haCGigt16GPlxkPDpi5heCN04F6lZw-d9XYaXgt6R9hac-Wp6_jpfW5WEPnmLazXDwWcDt8tlzRcBGboCZnjASMgb-ehd3zGu-RABqOElZsQ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baMROKY6cV0KX7DYJFBKccRqrpozwQJmPryy5wS1O7vKjj8S1Zj8AaDINJvUlA_Ny2C_IIwYVmiw2nBRPPHydek8_ZDRPKp5DsU_mfEHpOXiCshrsTAsmPTvNOGhSbQ1krPuGS3Otm15b7vLMiLDgJOMO6mqzfRZZ0KhRhtwme0fx80UnsL-VRyIAKk7Du3OG-91EyNtCpVFf5DwfqoxkmMYoVo-IjIx09CeD-2TWvvpYvPz5x3EM54TvX9Heh3uvF3fCXTfmskiVYm_FsURW_wxf_ff7GTC8SBABT4Nh09f97sEsZ_npzY-mKVrEsFoOoYIg9h1a1byPgJDx3EUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=cl7Kgomo5RN60599qcR1f6e8bareOAxqmPSEqoZ26FSmfYPoWyfZ6LmWNvGqEh5T-p4iNjJblfupLtqGpXkNGAkomyqo0wB9CXLhBI90ohRpJE26F2tY966Uy1xAzDWGVskcIhmAhKS3a1OEGnw47TFVmwukfw17HwIf3iuFMImlmnxz3vKPdFNLp-B49yxGq8_QzeyIt5-QmCZGVa3O6M8z5LyVifzT3PZ-plr3r6J1ZoYbgLegqwgZhl78vBDe4v6fo_lIrhz1zg15XYF-lnuhcZ4MGQNFBP_DuYbg5L1OrRvFrPs0_MEeSHK5Ly9G01MCL0QpPpnxF0V1DItU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=cl7Kgomo5RN60599qcR1f6e8bareOAxqmPSEqoZ26FSmfYPoWyfZ6LmWNvGqEh5T-p4iNjJblfupLtqGpXkNGAkomyqo0wB9CXLhBI90ohRpJE26F2tY966Uy1xAzDWGVskcIhmAhKS3a1OEGnw47TFVmwukfw17HwIf3iuFMImlmnxz3vKPdFNLp-B49yxGq8_QzeyIt5-QmCZGVa3O6M8z5LyVifzT3PZ-plr3r6J1ZoYbgLegqwgZhl78vBDe4v6fo_lIrhz1zg15XYF-lnuhcZ4MGQNFBP_DuYbg5L1OrRvFrPs0_MEeSHK5Ly9G01MCL0QpPpnxF0V1DItU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=hfmkW5672fpKuGmua2N5mVdBSzhYwBuXVcmQD6te7Hppc6CRX67g9FldXYVH7MOX03awFh08HBQI5-rmh_AAoiHjPrSwgQGuyl41pkFA2G3l3EwRQeahxo58gmDZNyxkxmgm_vtGdqgY_WyHaXlPEeMwQtZIZ4t1nqCFdVbdDTBZhm4fe5uydLm3NLFEIRALQypbOgy7QZG2tdRSAIrM513VsSMao-M1iHLm3OSQOgjDu8J1VXV8gRWjI2OeVj2MMQS58oVc9D982W2uw8kfi2yEx19EDtj_LvpfRDPvRjrPytbcO5FM_Tof99GXB9TQ-8PSOmV3sYy8HRNg8kv0dHBjXcgJZ3zMqJ6jRYR3l-xQvqmYmdYQv4U3IIQLzsLaiOkqZjfapmz5GiSrdqkaqsi2X_C_1z59wbyQklPg5fsqVNRZyb3HvIM0ROtMs2DuBIh47yCEqYnFD_9iCCxCjf6PcKgCMMELVxK48lk0w5gHpgVzEHJGMUzHbbc38LbgNLxHs3YH4Zz-eYjAhjXsFJlrnV9HYYGeptrqWYbWYRr0x7wa0BBLjBoUwextVvZYG0EX5lYiN4T1p0PmgyJsIrAeqPYxl8XkrDcKwrj3dvMf0Z9kAKMfSUF2riG7Pt44KH7MmWO3ZErZIKzWZ8PkTflYWMFAjVeshcQchRZXCaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=hfmkW5672fpKuGmua2N5mVdBSzhYwBuXVcmQD6te7Hppc6CRX67g9FldXYVH7MOX03awFh08HBQI5-rmh_AAoiHjPrSwgQGuyl41pkFA2G3l3EwRQeahxo58gmDZNyxkxmgm_vtGdqgY_WyHaXlPEeMwQtZIZ4t1nqCFdVbdDTBZhm4fe5uydLm3NLFEIRALQypbOgy7QZG2tdRSAIrM513VsSMao-M1iHLm3OSQOgjDu8J1VXV8gRWjI2OeVj2MMQS58oVc9D982W2uw8kfi2yEx19EDtj_LvpfRDPvRjrPytbcO5FM_Tof99GXB9TQ-8PSOmV3sYy8HRNg8kv0dHBjXcgJZ3zMqJ6jRYR3l-xQvqmYmdYQv4U3IIQLzsLaiOkqZjfapmz5GiSrdqkaqsi2X_C_1z59wbyQklPg5fsqVNRZyb3HvIM0ROtMs2DuBIh47yCEqYnFD_9iCCxCjf6PcKgCMMELVxK48lk0w5gHpgVzEHJGMUzHbbc38LbgNLxHs3YH4Zz-eYjAhjXsFJlrnV9HYYGeptrqWYbWYRr0x7wa0BBLjBoUwextVvZYG0EX5lYiN4T1p0PmgyJsIrAeqPYxl8XkrDcKwrj3dvMf0Z9kAKMfSUF2riG7Pt44KH7MmWO3ZErZIKzWZ8PkTflYWMFAjVeshcQchRZXCaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHZHrWAhWiadXTDsScEQdbS0bCV_eN3ihfyhKN9dcvtalhiTceEqUydSKkEIhk_YrwOaBrrVRpzf4xV5twQgeL5qxUs4w885gopZfV3NskCJEd0VXgae6zm52EidqiotPeeMJuhqzJRBb1QD-DUCEkF39I0E8YR_igKdphI3_JLC4WSsbJADszQvcL5b5uNBqE5CAmOeOti9DK8YBr9vLcmO0saDUbQY7BT84NndKdGOYl0jxh2lNu8xyd-kKmzECCnbWPVOVCtUo4YxnKwKMAv9b_g-Qx-GZQe0Jc5pHnYP258XKCSQ5jVcwPsOcJjvxYeVJGECEJtimPm9Em1S6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=N13JKsuWTjXskaEKOUBPZvvCXHW41ncSE2K1uD8ys246QDaJ-zJAlw8Z-9ZyaCVZ9hMA_xRXJArfhVDSXna2JxUBgRwSLDL851dcgPMa2hSCXny3n8jmJzOtM9EVMszIVrrPtK6r3TGCLV-kfSw3O31ebeG-l6Y0xe404H-MTSwMvetfoCrI6G5cDDRDsHVfvE2RBQfTsNSfaMUKte-F0RBnDpaAxW6sDgX_0N22opI51jJ0ezX7qMvrBRSk5nn-kLKnHSqvZntsK7Ae8fXIjjEg_K6_T8ONM7C4jYbP6bdC4i2UDXADjpgaIIsThv_iV8J7Gx1KNYs7_4lPj9B9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=N13JKsuWTjXskaEKOUBPZvvCXHW41ncSE2K1uD8ys246QDaJ-zJAlw8Z-9ZyaCVZ9hMA_xRXJArfhVDSXna2JxUBgRwSLDL851dcgPMa2hSCXny3n8jmJzOtM9EVMszIVrrPtK6r3TGCLV-kfSw3O31ebeG-l6Y0xe404H-MTSwMvetfoCrI6G5cDDRDsHVfvE2RBQfTsNSfaMUKte-F0RBnDpaAxW6sDgX_0N22opI51jJ0ezX7qMvrBRSk5nn-kLKnHSqvZntsK7Ae8fXIjjEg_K6_T8ONM7C4jYbP6bdC4i2UDXADjpgaIIsThv_iV8J7Gx1KNYs7_4lPj9B9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=FpRHhwB7OVj7HMalbpoc5IDTrhB_92H2gmGuN4scjCFA-p0VUOUvUi6Bvu2i8bL6qDsAsFpCBVvbVvetXXgQ_U1fKlOJbpFLe6GY2yCsQBTawy2Fk1CoNm4XtLnU9HKUE6uvch8woGWkG0mbvGu21KIa_cWbtKMzXLw_hYVzUmz4c7_g4u_-PW-BDs2bs3caoGZd6dja1AydB4YYoFPl_d5LBLBh2LAHPrW6pzOXQWSzXRA1_0HzErSxXEZaJ6TT2Zhj7zF2V8vv7ly3a5rLhmPA_qVvm7sUHzgZtN3AZs2_gdqCFU1vyv-Ly1mu4MI-Hh1ICVdeYCKtEuRK9JeJ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=FpRHhwB7OVj7HMalbpoc5IDTrhB_92H2gmGuN4scjCFA-p0VUOUvUi6Bvu2i8bL6qDsAsFpCBVvbVvetXXgQ_U1fKlOJbpFLe6GY2yCsQBTawy2Fk1CoNm4XtLnU9HKUE6uvch8woGWkG0mbvGu21KIa_cWbtKMzXLw_hYVzUmz4c7_g4u_-PW-BDs2bs3caoGZd6dja1AydB4YYoFPl_d5LBLBh2LAHPrW6pzOXQWSzXRA1_0HzErSxXEZaJ6TT2Zhj7zF2V8vv7ly3a5rLhmPA_qVvm7sUHzgZtN3AZs2_gdqCFU1vyv-Ly1mu4MI-Hh1ICVdeYCKtEuRK9JeJ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwqXvaubUmDIUFEor_wSp0YlcC_wvo_0qETBJ46dj0VNhqQjsiQ1SNCA56xofnTpHBvVFkfFI4PuAbsVS4U210HPC9Lq7Sr7AnclJgpS9cwodn_FBu_hceBYtvK_xU7_Ys7hvfr_9mUQ5ejRWrrE1wVNB7mlPDR6iYUISGci2ZKpQ_RPJNFtYWV1yHrqJgdid3d9qjNt-NUqLoNco1UiWh9Oy4gVEf9KubQu7JX0pFXygx-0Q2sgXWFWX2jAGwhx87uaH_7jORx7ty76fOQx20gmMVZnGxN6bJgUwQFDsQffm8vnFlFg2uJPUWanPea-mjBrRvBPO6jqRJ5sTZikqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=LjDUa4shJB5tBKFp9coFRlnt4QPWtB7em3ai0lPSBGl84WfPEobwuej1RqDfb9CPcHUKCPBwWNTPTSZ_TGqcacniVcF6Ry8NcE0ikGb1tkEru8phTrXfx1WrjciPbnjpO543gxGiM5JH0LRuvHfk-Fv_gAl7nCaO4KZIaMyNg-l5ncDIYldTL5PzchSM7S3RM38BJ4Jwopj8YRy4lRAAmvW56HnRI_qDbCQ02PNO2qFYgEpsI6xA-quglyXp_6k5p1sRGB0AfiyxsZFU3q_CuB9CRSQ6TQf67scvkmH-fRtGo4s75nK2jFzRrMOFCjHlGTR9BzfFeZht-YMxN3R96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=LjDUa4shJB5tBKFp9coFRlnt4QPWtB7em3ai0lPSBGl84WfPEobwuej1RqDfb9CPcHUKCPBwWNTPTSZ_TGqcacniVcF6Ry8NcE0ikGb1tkEru8phTrXfx1WrjciPbnjpO543gxGiM5JH0LRuvHfk-Fv_gAl7nCaO4KZIaMyNg-l5ncDIYldTL5PzchSM7S3RM38BJ4Jwopj8YRy4lRAAmvW56HnRI_qDbCQ02PNO2qFYgEpsI6xA-quglyXp_6k5p1sRGB0AfiyxsZFU3q_CuB9CRSQ6TQf67scvkmH-fRtGo4s75nK2jFzRrMOFCjHlGTR9BzfFeZht-YMxN3R96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTIg0zDJj-GBhqzLVij_oYVg_hd6DfZwwV6ooxHIvNOQ9HztKahO_FbTaCOOgFZAnkldu_-PhFUtESQegU-Srs8oSFlLXeTcVghDEwLE2dSsE87AJBrmJrxEWIQfk0HLVfKt5dDM3y90MpddtG5KL5UJaE9jY--F-1Pnc5dMDcJopX63gFcGoDl2H7gm__YWoyK-RQl7mbWLDsd4bUVA4K7_UbDbMAIppjc7JtheEKKgEqM_Vf_8yMNkj-eo-A62v_z0dQ6p_NL7JyMiLFI5MHYddQQ5HY0M1nK1s0z7j05-YJXW9mugxf4Qva4x9e5QjcxwDyOmZzR5GxdvUj5DjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=XJhChbNr5KnSYX4ds3O9JIgXqj8wmjv_66wUZX2eFkfdKJKHf6-TC_d1I-Q3-5FT2GKQFLugyiRFZowUdRyMy0WqqzjnUJh_Qlxz_nmVJgItpWDN8LQqZIdmfPPmsFiHf8K8V9yQo5zlGTFutFVKe0Own1BcGGkV6tQWHLJZxIYndVnIpuN86lUW0isuTzeEriFg4SrYh6EecVdy3mBGLwpsmGllk7WKYddbS7S5bBWxjSxtXpPT9ZxZ6LtHoaJs8eKmF_bNOylD2o7EV7C-5yTo1Sy4aV7OiiGe-TsilkXBZ2oHNQwqkWq8VcLWrr7B_p6W-wTnJOaPQ1Tk5cfpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=XJhChbNr5KnSYX4ds3O9JIgXqj8wmjv_66wUZX2eFkfdKJKHf6-TC_d1I-Q3-5FT2GKQFLugyiRFZowUdRyMy0WqqzjnUJh_Qlxz_nmVJgItpWDN8LQqZIdmfPPmsFiHf8K8V9yQo5zlGTFutFVKe0Own1BcGGkV6tQWHLJZxIYndVnIpuN86lUW0isuTzeEriFg4SrYh6EecVdy3mBGLwpsmGllk7WKYddbS7S5bBWxjSxtXpPT9ZxZ6LtHoaJs8eKmF_bNOylD2o7EV7C-5yTo1Sy4aV7OiiGe-TsilkXBZ2oHNQwqkWq8VcLWrr7B_p6W-wTnJOaPQ1Tk5cfpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4M7nZch9MX6Y80ZyjiByOg_qg3FNg_Wm7JEvFfKIhLgYJ8OUk5jCJv9btngSzww-cuFpQdIhWT64X2BaAzqwWx2EkjE_OCaupid3ycEDUvOqH2YGN0Io-FrdiVv7UJkYOI1dgJWkd14rV3gIhrqhLol25gtkwpmeK0VigeIIDbvzIFpxIfexkuDX7ht7PnnSasaxwMg4XzrhzlBcWzucsheCFIFg0ZKFI84ZocEwvAlZRG939EYy4cL4sTcxvtEmKMI_FoP1nMjY5SiTJ-7sRaiyIodLLPTjWMjZXXSTEQX18Mq7SZLKvjSsmGd6t23FCrwqhFaFpWJYCg2KCen5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFGR2CeaUZouZUUtsDtQgKoLVS31vnhs4GW5hnY9wcrpxsevsiCMSkUB9gGlO2tIufBU56Z-l904oTtx5_GUaWmhl_49e364bwG4biJzHEf27aByu0xrTe3h71Bq-kW6r97X243KPKjFlzN7cr6Raa0ydzSTDsPYVHPbABo28L9Vwoy2KEbnNgJ8xZQBrkgTzuJ_h_ZX-Fkd0Me5fbxIVgM75wzGtlxjR4KpR-xGVaCClowssV32u6GbuD1Kh6dZyrdEU1BaCeTiSUhpl5aBFl29Pu6Ko-qC3NCqb4r0nncoM3230dwf7Fhk2UqviX-skcsQc1tkvcd-u8ZBTykSBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
