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
<img src="https://cdn5.telesco.pe/file/p09ZcVKJ54wcBdcdjdy5EHZB7InAEhfXjfZKI79CDC6IJOHbgXXlTvsGm3A0kyOtsjQzqe5lqChTUcYsH2-E8HHvMDsjSNrC55whY0FrBwq6yGAF5BQUYawkT_qg3VulTp8ARXjJ79Enqxh4xvgUYCxFtuKs9777rhLa7koEpVPrz45H8mrpCceesz-i2a_XmP1K-L8vySf656HrjIBKw6a38_HJkBYCVZZ1oSqyQMuBsfzvHNV-_8d3RjPZ-KFs-DaJXrcEhdUd_CF7U_vSdShFKhU1_2gs2gQw8rzyqz-rqtMhTDe_SkNYWc1GMPylMIgBzS508hFsCP5v7cCWkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 446K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 17:00:34</div>
<hr>

<div class="tg-post" id="msg-104563">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52484f1b05.mp4?token=OujQhx9T2vgA7vxTPXfdxN1q1q4DUV7KqmMFcnmVO1puTj3UB7wlL61dtUcld7w2iB26JH2i12hEz1XUKZUQ0GgMK_z_5ktZxJEm_MGN2RE2i8WX0xZDlA1JhOJikxIMKkawOlpL4R4sAE6j3Yf3lCkRHhoGhRPUJ9fV6nhpWmzhJKT_ZYYixk937XWCb985PTMBtMP1bq8xpiXZWYunm94MztWvGbRIV5Ttk-FqzUTUF130YQVwGxtvBPChratYXeKcp8SS--IWi8FDg2EMKMZNPlh0yoOkB6YRuKSX9KTG-PrkdoIv4tew84awb3EgtV_dpA86cpo-1veAeYnZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52484f1b05.mp4?token=OujQhx9T2vgA7vxTPXfdxN1q1q4DUV7KqmMFcnmVO1puTj3UB7wlL61dtUcld7w2iB26JH2i12hEz1XUKZUQ0GgMK_z_5ktZxJEm_MGN2RE2i8WX0xZDlA1JhOJikxIMKkawOlpL4R4sAE6j3Yf3lCkRHhoGhRPUJ9fV6nhpWmzhJKT_ZYYixk937XWCb985PTMBtMP1bq8xpiXZWYunm94MztWvGbRIV5Ttk-FqzUTUF130YQVwGxtvBPChratYXeKcp8SS--IWi8FDg2EMKMZNPlh0yoOkB6YRuKSX9KTG-PrkdoIv4tew84awb3EgtV_dpA86cpo-1veAeYnZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب گواردیولا و زلاتان به مدل موی جدید هالند
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/Futball180TV/104563" target="_blank">📅 16:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104562">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00fe39bb.mp4?token=IsX4h9gH1XT_E2FWDyDB48k3wd5YMikJPYkPtJKwjDYKKYyLucGjYqqBTHk0SardW9tDFYUTJGRHhGKd-URtKxXAb294_OhqRYwmw6tg8Nrx4a3o9osTLo9oiqhZYexE4gEXcErYIOpBxBydd7bTgsbNntdq6v_B3ruURMMUcomqdwL-haQIh3hIev81U7Cogy93NfKhSgkVwZTwU2rKxn5Ry0QX8HnKdxZ-lS63rADkPh-PHP36qdm9qsYnxU8jw4K7a89urHJSn-o5Qq8SfPAlAD_HMHtdFdVHsrGRONAqJBB4Dhszr4bKBNkQ6exlnxTLhisZe4KTu3Xz2ygkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00fe39bb.mp4?token=IsX4h9gH1XT_E2FWDyDB48k3wd5YMikJPYkPtJKwjDYKKYyLucGjYqqBTHk0SardW9tDFYUTJGRHhGKd-URtKxXAb294_OhqRYwmw6tg8Nrx4a3o9osTLo9oiqhZYexE4gEXcErYIOpBxBydd7bTgsbNntdq6v_B3ruURMMUcomqdwL-haQIh3hIev81U7Cogy93NfKhSgkVwZTwU2rKxn5Ry0QX8HnKdxZ-lS63rADkPh-PHP36qdm9qsYnxU8jw4K7a89urHJSn-o5Qq8SfPAlAD_HMHtdFdVHsrGRONAqJBB4Dhszr4bKBNkQ6exlnxTLhisZe4KTu3Xz2ygkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فصل جدید اروپا، سیس جدید بازیکنان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/104562" target="_blank">📅 16:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104561">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb95f2a544.mp4?token=LJLxDr9pd77vcJlVgQ4nCisd-UCDSlOqpKHXvnpqFDydvRA-WZnWmOl3LceioKOpOUNlP9-zVPdBJhbDYxFhM9ay8jFgpsBtqemachfDga7RQN9OoWS3iFVIlW_Q1ZM15gJVjUV-3_DNgiOuILaSf7CvyJmouiloCB5LUS_-TLG8C1g2D_lpyZoNasUkoUCVFBaYhq8LPlWlixFJlb7nzeHWbXUM0RiJMjAgviYJX5SdDnUVbcTs0ghAyLLzDjzet19hbDiF4C1ldLK8Mmlq_bQKYRKrOybhB4xIcjP8vgvQFvobIACbRw-52Pqkwe2OTWF_PHWOxLlxEyRQ5LA2kZczJfU9XVn1bRtlPUOrJfOAdaEeMhNX0eD1K99P92aUJQvoAF4FtxKiJce7uMj95jvlYOG64iqGfri0--o8qH90lhOxWSTSp3QwU_aFMQ8v71QW4Lgd_RC5cCpukw6Jo2n4baSYf8gDru1Z5DpStw9NKoatk6lHIWUFR70ZCQYEUaRwlFHOHth2y2MSW3acMHCgPcG7TQ5WhJJLgTR1JHnlwcy7i8ClXQLRq_9pk5ykcz8o5S12a_66pVRBUHye_U3Cf2G70Iaagr7YsOSQo7zK9m5b2l6tDzPf68NMKFB8hKq1nUb7tDslE2xPozneQ7vp4_xQ0GFhURDTdJM7Ays" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb95f2a544.mp4?token=LJLxDr9pd77vcJlVgQ4nCisd-UCDSlOqpKHXvnpqFDydvRA-WZnWmOl3LceioKOpOUNlP9-zVPdBJhbDYxFhM9ay8jFgpsBtqemachfDga7RQN9OoWS3iFVIlW_Q1ZM15gJVjUV-3_DNgiOuILaSf7CvyJmouiloCB5LUS_-TLG8C1g2D_lpyZoNasUkoUCVFBaYhq8LPlWlixFJlb7nzeHWbXUM0RiJMjAgviYJX5SdDnUVbcTs0ghAyLLzDjzet19hbDiF4C1ldLK8Mmlq_bQKYRKrOybhB4xIcjP8vgvQFvobIACbRw-52Pqkwe2OTWF_PHWOxLlxEyRQ5LA2kZczJfU9XVn1bRtlPUOrJfOAdaEeMhNX0eD1K99P92aUJQvoAF4FtxKiJce7uMj95jvlYOG64iqGfri0--o8qH90lhOxWSTSp3QwU_aFMQ8v71QW4Lgd_RC5cCpukw6Jo2n4baSYf8gDru1Z5DpStw9NKoatk6lHIWUFR70ZCQYEUaRwlFHOHth2y2MSW3acMHCgPcG7TQ5WhJJLgTR1JHnlwcy7i8ClXQLRq_9pk5ykcz8o5S12a_66pVRBUHye_U3Cf2G70Iaagr7YsOSQo7zK9m5b2l6tDzPf68NMKFB8hKq1nUb7tDslE2xPozneQ7vp4_xQ0GFhURDTdJM7Ays" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری پشم‌ریزون از پیشنهادهای سایت شرط‌‌بندی به حنیف قبل از دربی؛ ۲میلیون دلار در ازای اخراج در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/104561" target="_blank">📅 16:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104560">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b661cf3a6.mp4?token=io5RSoZ2KtrqD9lx4aY7cV-x3jW7Ih7QbE6u3Eb65_24vy9NIoGv4hBIDf0651V2468PsLmmkZWwuZtSY5bsRPA-FuD21f0LasDqNYCEIWuhTMcnNnKurBq_yw3S8hVlh3pm4BPtZSEahME_CCT8mWRPHW_G2bbRGLPnc78c1Jwfsk7YRgV6Nmzd7rHqkrFAOKNAxhEJcfzcvADcM3_e-LkjkuOA8Z9L_SJhs8IaNHyZ3UgIe3jbILg77PiiT51Ofg1fvlKGwlzQOAaEcGgy4UVsG58ZxAhAriZPK6S-XkztCaQ5t7xMPD_OsUY5LYrhSpUrxJW5bUFEwq3ehqrU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b661cf3a6.mp4?token=io5RSoZ2KtrqD9lx4aY7cV-x3jW7Ih7QbE6u3Eb65_24vy9NIoGv4hBIDf0651V2468PsLmmkZWwuZtSY5bsRPA-FuD21f0LasDqNYCEIWuhTMcnNnKurBq_yw3S8hVlh3pm4BPtZSEahME_CCT8mWRPHW_G2bbRGLPnc78c1Jwfsk7YRgV6Nmzd7rHqkrFAOKNAxhEJcfzcvADcM3_e-LkjkuOA8Z9L_SJhs8IaNHyZ3UgIe3jbILg77PiiT51Ofg1fvlKGwlzQOAaEcGgy4UVsG58ZxAhAriZPK6S-XkztCaQ5t7xMPD_OsUY5LYrhSpUrxJW5bUFEwq3ehqrU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحبت‌های مارسکا پس از بازی دیروز که نشون میده به دنبال جذب یه رودری جدید میگرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/104560" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104559">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ES5PHTEMaQ43aXAPPyXOA4RMC6yYXt0LRADCIBeuFwsSC1bcShfbmGttP98TgffoDV8U40G9kIPfjXAVf6oxOGnKVZ51RfDUtHrV_2q8PMdUGPyZovR2A9q-mO6WvAcAZDwPBq8VRBsEwpWvkB0cYPQLBZVh1LYoYEChe50yZiBIk3gnIaE7Eq_bHto0WneHpuHmdaqVkCMnUnMNxIaszlC_bdkGZkFayZY_Shb1Mk2MNthB0cmN4Jk1IwEKQotC1ZvT1o_FB-uwEsbZFp5GQoXjFgrLG5fatFHNqClhohmt5Lu9M2N-l3KgpZGeiYk9Jg9AuIynHrDIKIbt3_i1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
ریدمان‌های اخیر اینترمیامی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/104559" target="_blank">📅 15:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104558">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33aa33566a.mp4?token=kwD0881kVe1eScmrcoK6X9WuTbDLwmYfVwkkti6WbnS4K87YFTh6mlt1Z6fJdntvwZXtCYWqhz4I3kz0aHJbUHQHBkdvT7o6Q7uPgc0BBlS0TmfOpjdmaCcC_7xgzDHtAv7lj_Fm3ymsADcOUf_XuKiVZhNAsMkN-1_zZYW8xl58jXDH3-Sz0u2IdFsPSYuDJcQA2hhrK-x0zM5fpvHqmA1YNbiGvGGav3Ee49EgNB4im3pIgg3h7XfjI1AtUeKbBGVR7jf6MhZMtrKg3NN9b6Fr8xVo9HmZMDczYPj6cg0ZcFaEYG5U4oSgzJbZ_JqEDg36eZitw1s2SFLP110aOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33aa33566a.mp4?token=kwD0881kVe1eScmrcoK6X9WuTbDLwmYfVwkkti6WbnS4K87YFTh6mlt1Z6fJdntvwZXtCYWqhz4I3kz0aHJbUHQHBkdvT7o6Q7uPgc0BBlS0TmfOpjdmaCcC_7xgzDHtAv7lj_Fm3ymsADcOUf_XuKiVZhNAsMkN-1_zZYW8xl58jXDH3-Sz0u2IdFsPSYuDJcQA2hhrK-x0zM5fpvHqmA1YNbiGvGGav3Ee49EgNB4im3pIgg3h7XfjI1AtUeKbBGVR7jf6MhZMtrKg3NN9b6Fr8xVo9HmZMDczYPj6cg0ZcFaEYG5U4oSgzJbZ_JqEDg36eZitw1s2SFLP110aOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال مادرید خوسلوی جدیدش رو پیدا کرد.
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/104558" target="_blank">📅 15:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104557">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f93ddeaf.mp4?token=Vcv8j8HZaZ_JMAEms1lgIF9our4Imf3Tn237al0NfOA8Glxnf6uzv6jQvRHVqMvQP-q-U7kq0ZTQka57qj3QM2m31Ibiq3e5XHOe6ZUsVwDVrT-UDdJzBqYLw1LzZDNYhZ1urQpErA-WZi-s1ibmymJI5LLYKZjXa4QRVFU2w-B3TWmPCgAdO_to4esPxHsepeeDsoV5HnhtmQ4iNpaJ3F3AzxAZ6kykVV_D_6JHEFglVapWs02W06NTGt1YZUbxZXsl8arXTCgJWA1km8XX4cwo92Y938jaHEfoeTxXseJ03jiN22JK69wQRdgbv8TiKSojLZLB5Ody5iQvq_iyxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f93ddeaf.mp4?token=Vcv8j8HZaZ_JMAEms1lgIF9our4Imf3Tn237al0NfOA8Glxnf6uzv6jQvRHVqMvQP-q-U7kq0ZTQka57qj3QM2m31Ibiq3e5XHOe6ZUsVwDVrT-UDdJzBqYLw1LzZDNYhZ1urQpErA-WZi-s1ibmymJI5LLYKZjXa4QRVFU2w-B3TWmPCgAdO_to4esPxHsepeeDsoV5HnhtmQ4iNpaJ3F3AzxAZ6kykVV_D_6JHEFglVapWs02W06NTGt1YZUbxZXsl8arXTCgJWA1km8XX4cwo92Y938jaHEfoeTxXseJ03jiN22JK69wQRdgbv8TiKSojLZLB5Ody5iQvq_iyxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
عملکرد فوق ریدمان لامین‌یامال مقابل الچه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/104557" target="_blank">📅 14:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104556">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c68f89986.mp4?token=bKwQCCuLfh1O6jyWZ1MiWPPGIMPWZsTZ-ReM6Bpb8Oj7y8UJGSrlU0GS-B0MHNjm1tjV1Cgy6DpoYVhx-IClEXtisncOmZMHg2Cn-u4odWCe5_2ZUBI9-tGlxlIgBTwBorA-M24h1Ae6sIBmr5eBOcyba4-n_YeYNyYnH4t39qOBl-q-mPLoZk7G33HJBph7iJG7AbajgblFk5GM-agOsXwzwAXdA6YVNh4nTQnTavvTE-XhbHL5j3id9khkRXYpdFSRIeVycn2YVaW53MGDZCj5iDHWYnPaZESmX_tLLz9Q2CAfT7bglZzpU8wHRZAftnW2eFom1hkTZ9teZV2OEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c68f89986.mp4?token=bKwQCCuLfh1O6jyWZ1MiWPPGIMPWZsTZ-ReM6Bpb8Oj7y8UJGSrlU0GS-B0MHNjm1tjV1Cgy6DpoYVhx-IClEXtisncOmZMHg2Cn-u4odWCe5_2ZUBI9-tGlxlIgBTwBorA-M24h1Ae6sIBmr5eBOcyba4-n_YeYNyYnH4t39qOBl-q-mPLoZk7G33HJBph7iJG7AbajgblFk5GM-agOsXwzwAXdA6YVNh4nTQnTavvTE-XhbHL5j3id9khkRXYpdFSRIeVycn2YVaW53MGDZCj5iDHWYnPaZESmX_tLLz9Q2CAfT7bglZzpU8wHRZAftnW2eFom1hkTZ9teZV2OEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تفاوت اعتراض رئال مادرید و بارسلونا از نگاه خاویر تباس رئیس لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104556" target="_blank">📅 14:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104555">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLhUEjlEQ1rcz1Vw1Qqi-59bfHXDrir-b-K4ug-2EZIpoej3rnv3ASfvkRza6Zf8eCUFLYhC2fCDU9h42vf5GSSs05uE7c-TKHKdgzOak0YCml0_lyMb6J9LB1hIz3xxEGVzNPQIN54Li2CwGQeVgxPxNGgpP65MA6wBN4FLrEMipUtDWvVqeFhHe1DbSxiwrojdUFuabAHEIOowKwXvNF2fAsanX2JkpfxZX_S8GnYIzPZtf7cQy-QGnZUPDun2AxS33JMkK2kWbvoYjUedTkWJ3qINeRY2WQvxiQSku2ZNaBmFVJfoMTR-952gV7qktNCbFX251CtnB2e7RO10Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سانسور ستاره لوگو باشگاه پرسپولیس در پوستر اعلامی باشگاه استقلال برای سه‌بازی آینده آبی‌پوشان پایتخت در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104555" target="_blank">📅 14:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104554">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8db78c81.mp4?token=RcL9QEAOysCZYJ-StV3n0VC128wigFVJajQUWEG6UpD2rt5P5LcfEJuaWpEVpDkBaFuI4_dq5eOOHE-5U80xlF-ZBHUWHwlb7IF3J2NFcV4WcFe1vKNt7n2609n476FTmB2fkhz0R9JqZOrx_FMPSatsi3g6qn2OaRn5SzDL0uJEyuezEtejg-6EIagmxi2WvzDQkeosKqbz6a9NXlp3iVcZcoFV0fHy12U2GEmEoT0VU1s3ZoIWwjeMMCgBj9h9R9XxHiCo0sTJ1o1SJtibmF-OQ6OYY3w8NWUyQy9Q6ikZPCv4pLm1wVbdKIRv_a3nqdIe2S8OImoQjubAzdF0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8db78c81.mp4?token=RcL9QEAOysCZYJ-StV3n0VC128wigFVJajQUWEG6UpD2rt5P5LcfEJuaWpEVpDkBaFuI4_dq5eOOHE-5U80xlF-ZBHUWHwlb7IF3J2NFcV4WcFe1vKNt7n2609n476FTmB2fkhz0R9JqZOrx_FMPSatsi3g6qn2OaRn5SzDL0uJEyuezEtejg-6EIagmxi2WvzDQkeosKqbz6a9NXlp3iVcZcoFV0fHy12U2GEmEoT0VU1s3ZoIWwjeMMCgBj9h9R9XxHiCo0sTJ1o1SJtibmF-OQ6OYY3w8NWUyQy9Q6ikZPCv4pLm1wVbdKIRv_a3nqdIe2S8OImoQjubAzdF0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هوادار ایرانی رئال‌مادرید بعد اولین بردشون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104554" target="_blank">📅 14:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104553">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7eelrN8mRfzjn01nCLQapAdMi-SuxrQulQASd9ZIJVBImC9z15wrROZF8XGd1ZKwI5-0o9AiDgN-KTiw1c6Y6wUAAh7axUcNSgzHJ4_qZG7Uo9NEdW9ahyJu6qc6gINRR54xKH-2K5ShsePZZ3mjlPr9kmyWUnuBoWzqWiA72LsiQD3HXxdxEXvU6hjGUgmBRnUikGSqjJYF4aX4P7MnBYfG4aeTBgElHMKXEsmBVh__IosF55dryQueeullhpU--mdVvja4Z7bBBNiFgORdGURXxj6fDOSqgkBwXyhOJcK5eaVMR5WsdC0A-VrYHI0IGkvIbDBimxPQZtjnbhzMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔻
بیلدآلمان: باشگاه بارسلونا پرونده جذب احتمالی سرهو گیراسی مهاجم دورتمند را بدلیل دستمزد بالای این بازیکن منتفی می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104553" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104552">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=ca4iS1_YLX6VQkYRdLv1Tt0V7WfTUfgenjxSrV4xOq5s1DwQiYR6EQgabtq5dXOIqHXAZ9cAYOj_TXbpgV3TZjqQrIS7usIX4HjyfJHO4RTWdC_YXLJHx3cT28hbhpiKC6RyPNznwDAL3J38BLYAIMwahVqCmSj_cd1hfRcNpm-58ActdtnItFr2yrbyDb38KilNgb7govrL28tO002aIrkEashVvyoe-uKEPNM70K2GoHszQdqlkF9IuWyDvohBprjM1L4d-7rv-viiRemyCtTnOzKvTbbOaW1EYvDVWw-0puANA3A00jMHw48IDSTQnYxot8lrK8QVdfL6uwNSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=ca4iS1_YLX6VQkYRdLv1Tt0V7WfTUfgenjxSrV4xOq5s1DwQiYR6EQgabtq5dXOIqHXAZ9cAYOj_TXbpgV3TZjqQrIS7usIX4HjyfJHO4RTWdC_YXLJHx3cT28hbhpiKC6RyPNznwDAL3J38BLYAIMwahVqCmSj_cd1hfRcNpm-58ActdtnItFr2yrbyDb38KilNgb7govrL28tO002aIrkEashVvyoe-uKEPNM70K2GoHszQdqlkF9IuWyDvohBprjM1L4d-7rv-viiRemyCtTnOzKvTbbOaW1EYvDVWw-0puANA3A00jMHw48IDSTQnYxot8lrK8QVdfL6uwNSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
‼️
🇺🇸
پرچم تکان دادن عجیب و غریب ترامپ برای استارت یک مسابقه در واشنگتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104552" target="_blank">📅 13:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104551">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a81219a5.mp4?token=nSbbll0vA3OjiDmKA-cM5hApP7M55l2YeyPIhGxsAxMIoZ-PfNjBQeCKI5iR0unUGqheX5L-mA1VRSVZl11ff0Iq_c3SSt9bhBhVYawZOIsafgiaTLBKofDvYS7A0bUUyjzCzBBIfnQ4dNqHdlc4tGtNNj9OmIOPoZ8V-IjEpSmui0p7wKM8eMxqBxP6Nr-bw0eCasloDxJjGDAnwJ88kqsBiVklvnGBQuwfC3PJlddwPbtKqOI3NQMMxRKobSEVvWBjmdGpLEjInhX4DkYlwiBYwQp_9u24wYGShQGtHdXc2mPetO3FgWgiwUhX_q840aXKLQpHsfzkxF7ImxI_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a81219a5.mp4?token=nSbbll0vA3OjiDmKA-cM5hApP7M55l2YeyPIhGxsAxMIoZ-PfNjBQeCKI5iR0unUGqheX5L-mA1VRSVZl11ff0Iq_c3SSt9bhBhVYawZOIsafgiaTLBKofDvYS7A0bUUyjzCzBBIfnQ4dNqHdlc4tGtNNj9OmIOPoZ8V-IjEpSmui0p7wKM8eMxqBxP6Nr-bw0eCasloDxJjGDAnwJ88kqsBiVklvnGBQuwfC3PJlddwPbtKqOI3NQMMxRKobSEVvWBjmdGpLEjInhX4DkYlwiBYwQp_9u24wYGShQGtHdXc2mPetO3FgWgiwUhX_q840aXKLQpHsfzkxF7ImxI_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
زمانی که رائفی‌پور (آذرماه ۱۳۹۸) این صحبت‌های مضحک را بیان کرد، قیمت دلار حدود ۱۳ هزار تومان بود و حالا ۲ شهریور ۱۴۰۵ قیمت دلار از ۲۰۰ هزار تومان نیز عبور کرده است! یعنی بیش از ۱۵ برابر شده ..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104551" target="_blank">📅 13:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104550">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3040879b.mp4?token=UIfk5xyMiE2ry5cgMOqEWjURhZtfqSPC4mICrlHCHDvJcQsalM0EnPkyKKU6CX5UiRHoxW7HK--Aw8gwnR6lL1Vw54KI5KwGI2o-hv4n6UjUh9C1J1lzuhYuCjxAVsgak4so0GGt4Zi1iSKvNiwyvW6NtSQaH4wcZe7Zp1s2b4BvpI5KZ11LlGRYpM0hajmQ83q1zLB4gpKnoF4RkIrMWU4qBCJQOzHfDSK_PZWfO6sz7TQdVqmMhs_xsIwH_s5eH8SORH-d9_VnnZLvW_y0PGP4SGXQAf9uxwTmwIzigVROhmPCC0lB-o4zeT-WM5B5cw2dg0gzWYnRRs1_YJYO8yAyVlKfAbbH61DVrLuS3NaMeRQR3emsJ95eRmveLWYRN_r1i_FVv4GEzwj-4tsfhcOWZ5Y7JwvfQLFNhIwxJE8Nz3DU5p0yLCDxUgOwR-Wlpl1nOV4hQbLgRCZ8f_n_fiOpEqSp_2xeHn-E6N7ted-pNfb-040hJWEaF0hEvS-pu-ZbIy-Ju5n6B1w_2uHSULhcxB7bCRQG0UkHbR7Kl1BFMyT8hmasP4DJvVPM44tSrbB21uK8ZY5tDhfpXVLuW21WaQNheJDsyVL3DAMuKHROlMiQuRgsHyPG55qOpRWZ9fRmG4RKR-GBYGt8SDsQ3KiX0-o36Na-NMDyYm6mzB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3040879b.mp4?token=UIfk5xyMiE2ry5cgMOqEWjURhZtfqSPC4mICrlHCHDvJcQsalM0EnPkyKKU6CX5UiRHoxW7HK--Aw8gwnR6lL1Vw54KI5KwGI2o-hv4n6UjUh9C1J1lzuhYuCjxAVsgak4so0GGt4Zi1iSKvNiwyvW6NtSQaH4wcZe7Zp1s2b4BvpI5KZ11LlGRYpM0hajmQ83q1zLB4gpKnoF4RkIrMWU4qBCJQOzHfDSK_PZWfO6sz7TQdVqmMhs_xsIwH_s5eH8SORH-d9_VnnZLvW_y0PGP4SGXQAf9uxwTmwIzigVROhmPCC0lB-o4zeT-WM5B5cw2dg0gzWYnRRs1_YJYO8yAyVlKfAbbH61DVrLuS3NaMeRQR3emsJ95eRmveLWYRN_r1i_FVv4GEzwj-4tsfhcOWZ5Y7JwvfQLFNhIwxJE8Nz3DU5p0yLCDxUgOwR-Wlpl1nOV4hQbLgRCZ8f_n_fiOpEqSp_2xeHn-E6N7ted-pNfb-040hJWEaF0hEvS-pu-ZbIy-Ju5n6B1w_2uHSULhcxB7bCRQG0UkHbR7Kl1BFMyT8hmasP4DJvVPM44tSrbB21uK8ZY5tDhfpXVLuW21WaQNheJDsyVL3DAMuKHROlMiQuRgsHyPG55qOpRWZ9fRmG4RKR-GBYGt8SDsQ3KiX0-o36Na-NMDyYm6mzB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
🔥
سوپرگل پشم‌ریزون نامزد پوشکاش در بازی بامداد امروز در لیگ MLS
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104550" target="_blank">📅 13:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104549">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fdf775f7.mp4?token=QO-kKd8fjRXWTkO3ERmoBvxCRDsDNr0Yu-mnn74BW7BDAH_fzJ4nTzDIgW297TX9njq-UUmrcX3BjgsdtxlqgW2ro6flm7kkL6QLWCWcTaJeZ7Aa6KPkMlSnBSuGdYMqqv3HfYb4EZV46pJJnIsHORqy559d3pJUV8RbiM7C3P1HcAY5pYqB_tx3YGH3y6oHngeOoSwaelkDGMe9YlHbSBeS5MxJ18G4v6hfBu0a7uflHRCIM1sDJ-cshX8dvrRFoELMNWed3FNjwvqMC_kU_CpMLZyh2npTRb7lh2ug14GPJoOp5M5Iw_N6r0pb-7MDBGlC4y-H9ce8mrp5Mt0sGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fdf775f7.mp4?token=QO-kKd8fjRXWTkO3ERmoBvxCRDsDNr0Yu-mnn74BW7BDAH_fzJ4nTzDIgW297TX9njq-UUmrcX3BjgsdtxlqgW2ro6flm7kkL6QLWCWcTaJeZ7Aa6KPkMlSnBSuGdYMqqv3HfYb4EZV46pJJnIsHORqy559d3pJUV8RbiM7C3P1HcAY5pYqB_tx3YGH3y6oHngeOoSwaelkDGMe9YlHbSBeS5MxJ18G4v6hfBu0a7uflHRCIM1sDJ-cshX8dvrRFoELMNWed3FNjwvqMC_kU_CpMLZyh2npTRb7lh2ug14GPJoOp5M5Iw_N6r0pb-7MDBGlC4y-H9ce8mrp5Mt0sGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دومینیک سوبوسلای درباره بازی دیروز:
«صدای سوت داور را اصلاً نشنیدم؛ مجبور شدم کاملاً به او نگاه کنم تا ببینم اجازه حرکت دارم یا نه. در تمرینات پیش‌فصل روی پنالتی زدن تمرینات خیلی زیادی داشتم.
وقتی ۵۰ هزار نفر هوادار حریف علیه تو سوت میزنند، حتی صدای خودت را هم نمی‌شنوی! اما دقیقاً به خاطر همین چیزهاست که ما عاشق فوتبال هستیم؛ به خاطر همین است که من عاشق فوتبالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104549" target="_blank">📅 13:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104548">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
❌
🇮🇷
رستم‌آشورماتوف که در پایان بازی با لنگیدن از ورزشگاه خارج شد، مشکلی برای بازی بعدی استقلال مقابل فولاد خوزستان ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104548" target="_blank">📅 13:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104547">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
صحبت‌های جالب و شنیدنی نوید استاد‌رحیمی درباره فوتبال این‌روزهای پرسپولیس تارتار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104547" target="_blank">📅 12:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104546">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37beb95f52.mp4?token=cB2J7eRQ22Q1RSCXW7GsDuGCe37FtMiFWHr9ddJLn6XtMAi5NonuCFKkiNaAc4yd-WVMCfTzczSNOFv43DW49TI3aS9OWOvTQ8gBGsalzojV1rg6MMLlCDETGgvd7PQcUzUxKa9isyl2cgbeDeNBlUN2IzPZKLSgg6m6QoYUb9Q9Il07ra70FvaGsfSIeSLYpkywish7Q7dtAV7HtKNfkaywyZ7yoLy4MR6BFl4od_Tf8D_4LhbsKen-jkpFtGuo8xokmfsXe2Ih0pdRibqHH2SFybZp-cvIdjhco7w31-TixGZkHrnn8zTT6-VuLx9LYYzeP-hpDQDU2DPXGEOs-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37beb95f52.mp4?token=cB2J7eRQ22Q1RSCXW7GsDuGCe37FtMiFWHr9ddJLn6XtMAi5NonuCFKkiNaAc4yd-WVMCfTzczSNOFv43DW49TI3aS9OWOvTQ8gBGsalzojV1rg6MMLlCDETGgvd7PQcUzUxKa9isyl2cgbeDeNBlUN2IzPZKLSgg6m6QoYUb9Q9Il07ra70FvaGsfSIeSLYpkywish7Q7dtAV7HtKNfkaywyZ7yoLy4MR6BFl4od_Tf8D_4LhbsKen-jkpFtGuo8xokmfsXe2Ih0pdRibqHH2SFybZp-cvIdjhco7w31-TixGZkHrnn8zTT6-VuLx9LYYzeP-hpDQDU2DPXGEOs-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقابت فوق‌سمی و جالب فوتبال در مسابقات جهانی ربات‌های انسان نما در چین
😂
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104546" target="_blank">📅 12:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104545">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900aee1af2.mp4?token=pznOqPl7UydBCGPBSdvhDN9AWTu7lc2iBqPw5_aIoVhtick972pCAfv6yd1LiSiLq8GdWqzccdWg7nWQVjX8LrN2OTs3DAPKgBSfK9Z8fgMxenvuGANd3pQgWc7reD935WAb8nQS02CwUVh86Igx4cS8YDoE6aRO3xpZ2GaF_dAVuD_3TkNLwXcPX0GmdGogoIp3h18K9OlMzxw6CXsaPZ8od_6MkzLdWiDb9S8liE9gyanuZrnHhXOkkPKEeS2oEJMUrITuMf1KqbrtqmMpixCGUPENNL0oXrdlATrp1fEx5-MBy74r06hQJQVULelmWaTPmFrb6TMFQLWYn3dINw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900aee1af2.mp4?token=pznOqPl7UydBCGPBSdvhDN9AWTu7lc2iBqPw5_aIoVhtick972pCAfv6yd1LiSiLq8GdWqzccdWg7nWQVjX8LrN2OTs3DAPKgBSfK9Z8fgMxenvuGANd3pQgWc7reD935WAb8nQS02CwUVh86Igx4cS8YDoE6aRO3xpZ2GaF_dAVuD_3TkNLwXcPX0GmdGogoIp3h18K9OlMzxw6CXsaPZ8od_6MkzLdWiDb9S8liE9gyanuZrnHhXOkkPKEeS2oEJMUrITuMf1KqbrtqmMpixCGUPENNL0oXrdlATrp1fEx5-MBy74r06hQJQVULelmWaTPmFrb6TMFQLWYn3dINw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
نگاه خشمگین امیر عرب براقی، داور بازی حساس امروز به شعار یک هوادار در فرودگاه تبریز که او را داور پرسپولیسی خطاب میکند!⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104545" target="_blank">📅 11:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104544">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1r1Z7odJBT65KJmXcVUyyoQdqc2h2d_chhfx-Kdz6lTBbX1-BgU7MudhS_vj4TSELboZPcXBwI_qDSg7orztgKCBxwNZWmhmhaGstdKet7lXGZnj9Pd3KK308d5pQXH3SwO8JwAisK2P71ZucHOfQHp-bhtnqcfKtD9NT05jy8Sa-OHVBIIPtxOzPK1EH82mGBMRceagcd9cuq_VqlAQrvd3OUryG-lQd6qOrkaYcuYIzaM7hod4ZX9Td84HshJyrnMwpwWu12UAOoEHY4SNd1FM5LepFEaVVbO403JNNL3IWX0MamoMi5BUD3V_2fWTqxiZhXPxULYaDFvSbniEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
آخرین قیمت طلا و دلار و سکه در بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104544" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104543">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pos1S3OeVDeSA_XL_74Sp6sBuy889fh9Ado5FBI81gBEDd_BRB4iCcBlfJVVFqtwICqTHjioLib735TCEJ4iFnMGbgMYz83raKKihH_XBB3xeVibBQTHWixmxvemxEFkfVnXSvdoxHeXrVOyMow_Bjwm7XkHPuktIo5tB-bqCkxs8GLTsy5bMe7gBTcpcfmbmPFEskRBS5TRXKYh4vqqIWhKn-nbEmTJoQc04d_S0vowgggYvIWrM_vlKclfi4XgBPEJj9QOqlQJQh--_97bl3-EXDGZXQWmmISWDiPkzy496gzE2fY41X3NfiuNOkgGyVT7olyRe-2nB9TksRNS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
#فوووووری
از The Athletic:
⚠️
یک منبع نزدیک به مدیریت اتلتیکو به ما گفته اتلتیکو فقط در صورت پیشنهاد ۱۵۰ میلیون یورویی از آرسنال حاضر است آلوارز را بفروشد. خود بازیکن علاقه‌ای به آرسنال ندارد و فقط می‌خواهد به بارسلونا برود.
‼️
در اتلتیکو اتفاقات دیروز در واندا متروپولیتانو را «یک مسخره‌بازی» توصیف می‌کنند و امیدوارند بازار نقل‌وانتقالات هرچه زودتر تمام شود. منابع بارسلونا می‌گویند همچنان شرایط خولیان را زیر نظر دارند و آماده‌اند تا آخرین لحظه پنجره نقل‌وانتقالات منتظر بمانند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104543" target="_blank">📅 11:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104542">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m90J2h2yg9zsfOg_9rwcLCgyMxQFb7hYYp3rjmXZInc6nXqiwKNJgp7lTk_4JcNqeX1PT_A9P5rwh9V5MxjOHxR1PVyziByYIy5m1-lxSKIbzRfKrfdm-og9eEPfvPlHwDEYA9GT627p2QgFTGjGqAG9SwSUXoMA9N6pOmgnfrbohE2bd4l4lJxCMdZQO7TW3M-YAS9A_Wgx8KZv_XvMgl_lbhWajLx16SWSPVUGu3nRCy4JkNLzUERKwFVxyIeO221Ga0qK5-DLldTLklku8Z8zEWamsMfUU4Y6Ds8FhTt7KmUSnOS0OEfdcFC7a5cMvY248xxK_PaINAt-kCFBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سانسور ستاره لوگو باشگاه پرسپولیس در پوستر اعلامی باشگاه استقلال برای سه‌بازی آینده آبی‌پوشان پایتخت در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104542" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104541">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmudH6m4ZAz1WEjQCViJd24Q3lPe2AP3eog2cxcvW1mZrH3z_FFUinl4MjcGCTSqegoP-lvv8HHzCvVl8Z0RSjxLnFnGDaLljAEZuki_jOqC-orPyMrrhBZoNwazjvuME1KKRpGaVGOZsDQJqHSu-AHcfzFaaupH6GYebrkKWamMDHsXAN98jokpezURq1D4O9VoSjOzhcu3cgF0n3JiJD5TKrDkzjwmuZ6xQ8SzH6fTgkcJZK4yikrU9C6I3fZkEjVFmlMCidsi6XCqIH9VZBu07eKsenBSaMEdxNhCL-Qca_TrIxBHKUSQLkjWHHbH_jBETACwynjTRaDems1AHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104541" target="_blank">📅 11:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky9EolC0Mj86GZdB5wKOr6h9sb5kUSJx50Ipf38GkviV8ysZ5iZlZOp1_808wg9IJuigYi13W715CYljRlOhcEMq8zkmeEOO8dUMkDWhj3cZpX4fVLvEdM1NHr4SSbxPA0eocfIBC7Y-KsazdYehvbGWhJQnfq7Pc5TxvYKPdkdpx-3b_OMQQo2jC-Gvp3SCyQwuECu7tMfqkXFfCbOY8MYftJk0dexdrmq17VVgIpqXbsGBqCpcFmu_FgBnEjXfwflTRl7qAuZEZfY5JiOVEzG8ZDnftQKUebVGiu7iZtqw3gCLedigauXb0fTzo0tmUviajifRKFAtuiH0176QhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه پرسپولیس برای بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104540" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104539" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104539" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpEHFnFwyNXHnmFj6Yqz23RW8Zy8QplwdElIsi0T9pJRxqvLUXE5OpiiTSsZbeRNCxSULlLcNfrUJLBGUPi6XQGhRsWbEtXVSyZw9G6Z16heMaj7hxlwFYh1PFJZ3zhEqiOJH1nyqE2xMH9vqp_s79huzuKRMo8MZ9JHrGhJCOvFYvRF5scN6kdHPcnqQKSOq53N-7an50CUpb5OWxdVn0qxR3n54eNF_8-5De_zlj5mZmedpaAgTGWgPl46941C_p8FJhvroS0H3YKac_ptnDyz9TnJ2tQLc8nhbJJmeX-9X2Yyud-TT4W68ns5jGCh5KHDIZVAy1Z9RCeIM-uQSw.jpg" alt="photo" loading="lazy"/></div>
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
r2
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104538" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc944da41.mp4?token=bfZZntFYA1TwUIf1EHeTFRfc7GYtcmsKVyFPuJFDrOX-UH17vvAWIupHX8uiLpovO6qasqMeI2IP-3AjemWZlmBGdfhh4R1NJnK7VPidbPpwWIk1w34rJU4Bq4AyhCI2OzKEU_d_tt6JimWcLN19vvHnkkAoawtQMBUt4nkfV9LTmtJQ6qGZPBTq928pwbovuCclMxs4HBoxbKtigSj3mI2-dmzJ1GQjRALhlT8JudROI8ZBX2F0CidpnWnNS8UzDP9y-eBpWrBFdtj34xOeHWHrLOcBcUnu7cykDVh-Lm4vfxxGQ1MTA9_whUUADHpK42QruDqt9kB2_CWac_sDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc944da41.mp4?token=bfZZntFYA1TwUIf1EHeTFRfc7GYtcmsKVyFPuJFDrOX-UH17vvAWIupHX8uiLpovO6qasqMeI2IP-3AjemWZlmBGdfhh4R1NJnK7VPidbPpwWIk1w34rJU4Bq4AyhCI2OzKEU_d_tt6JimWcLN19vvHnkkAoawtQMBUt4nkfV9LTmtJQ6qGZPBTq928pwbovuCclMxs4HBoxbKtigSj3mI2-dmzJ1GQjRALhlT8JudROI8ZBX2F0CidpnWnNS8UzDP9y-eBpWrBFdtj34xOeHWHrLOcBcUnu7cykDVh-Lm4vfxxGQ1MTA9_whUUADHpK42QruDqt9kB2_CWac_sDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دوباره بیرانوند - پرسپولیس به هم رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104537" target="_blank">📅 11:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00277ae5ab.mp4?token=lcbFkS-axGhC0JmxeSDalzjyhZDhnXxZONtnC5ePaQrI6xKnxqQIIEUPrVwULybqQXZpXRuwAtSJAmOTkEDN25zqmSUYFt4-nqNi2AYHirQwdRls_O0-luty93YHZYrlIzB_4q50qEv0fetjlyFl3tK4w668c4Y7B3IRvf9CXuCYrU4CxJnBO7rW4CxzQmgOG65v96t3fyUOiZb3hCzOIcfZfSXAskHXxkup8pnZtU8oU4lM6FbtYJuMHDo_d8l2TzweQrN7Uf1WgTxJ_BdUqOrKNaqTx3xsqV423yGrYcXt2VtUU_Vu6agFdPGiPZEBDLKatF4sHwiME0xyQy40Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00277ae5ab.mp4?token=lcbFkS-axGhC0JmxeSDalzjyhZDhnXxZONtnC5ePaQrI6xKnxqQIIEUPrVwULybqQXZpXRuwAtSJAmOTkEDN25zqmSUYFt4-nqNi2AYHirQwdRls_O0-luty93YHZYrlIzB_4q50qEv0fetjlyFl3tK4w668c4Y7B3IRvf9CXuCYrU4CxJnBO7rW4CxzQmgOG65v96t3fyUOiZb3hCzOIcfZfSXAskHXxkup8pnZtU8oU4lM6FbtYJuMHDo_d8l2TzweQrN7Uf1WgTxJ_BdUqOrKNaqTx3xsqV423yGrYcXt2VtUU_Vu6agFdPGiPZEBDLKatF4sHwiME0xyQy40Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
ویدیو وایرال‌شده از تفاوت صحبت‌های تارتار و وحید هاشمیان در مطالبه‌گری از مدیریت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104536" target="_blank">📅 10:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104535">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e82f680d5.mp4?token=AtT9Rm48JOBllPrOKP__iUVwk7Gk9eldAsj0Oj6aHWg0TsMFi_N67FMJO7Ud_At4m9dmX2wyr7fR1j3JekzrGUnZ2nxgKnuBV3pzN8q9bR9bNShSeuLhnm-xTo_k9kvDd6cAEAJ6gbZlLvlCP9fN6TgXIo6P8sYJuUFeMiFcSF9TMnAue-I3t_IaxYqgC-kWRyWAh_MxoEBP91BSqymaJq8P5j7thVTbqpkVTrqZSOsrcpyUeZIUs9KAHsAvbrn34BUE3jsYQWhOX_Rzp0kQviY-SrOTFEemB6evhurk1IpCIE03qBWR36r5Awwk1rmoKJPL1zqAXkkAnp7OOg7jB7aqw3AIVsKfjtQQMPeqGgUJq3cA1Y888j2JsGhBn_aj03feVwkk-wx_DDSwG1KOQ-vZnU7EtcQ5z5uO9nN3I8JswSLMJJyYghh4B1wujlx4MBEtXVbeELDDfZH-0xiqAUxNPjtp93iL3caAVYmwPDYfTa8BkiNTZRT3-n2NycjKyt3zg0C2tUhqb646LrauiBB4a3fVqdKCPOTvoacmnc1Rfu0lQyHh4B8dvahXyOQyuTSV9UcFIcN5XMx6xB_RhFJcVhi21kXfBs9VXpWRM3dbWWedKRVlPy5kpcMseRNFWPiMtm7Bpn77CEmjlnwWlxfM_LocZzM8SkpBGL-HDUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e82f680d5.mp4?token=AtT9Rm48JOBllPrOKP__iUVwk7Gk9eldAsj0Oj6aHWg0TsMFi_N67FMJO7Ud_At4m9dmX2wyr7fR1j3JekzrGUnZ2nxgKnuBV3pzN8q9bR9bNShSeuLhnm-xTo_k9kvDd6cAEAJ6gbZlLvlCP9fN6TgXIo6P8sYJuUFeMiFcSF9TMnAue-I3t_IaxYqgC-kWRyWAh_MxoEBP91BSqymaJq8P5j7thVTbqpkVTrqZSOsrcpyUeZIUs9KAHsAvbrn34BUE3jsYQWhOX_Rzp0kQviY-SrOTFEemB6evhurk1IpCIE03qBWR36r5Awwk1rmoKJPL1zqAXkkAnp7OOg7jB7aqw3AIVsKfjtQQMPeqGgUJq3cA1Y888j2JsGhBn_aj03feVwkk-wx_DDSwG1KOQ-vZnU7EtcQ5z5uO9nN3I8JswSLMJJyYghh4B1wujlx4MBEtXVbeELDDfZH-0xiqAUxNPjtp93iL3caAVYmwPDYfTa8BkiNTZRT3-n2NycjKyt3zg0C2tUhqb646LrauiBB4a3fVqdKCPOTvoacmnc1Rfu0lQyHh4B8dvahXyOQyuTSV9UcFIcN5XMx6xB_RhFJcVhi21kXfBs9VXpWRM3dbWWedKRVlPy5kpcMseRNFWPiMtm7Bpn77CEmjlnwWlxfM_LocZzM8SkpBGL-HDUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
عملکرد درخشان یاسر‌آسانی در بازی‌دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104535" target="_blank">📅 10:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104534">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f1d85674.mp4?token=Itc7B4V--TR8QqqGs8QP5a41X8SwX3HwdPixghAkNIfvhdA1fQKHwnWh4-1eYlvEVP47Fg0ebkmd8pYMk5gBA_iOeRdj4ZogxgdX0S5Dw42Cq4YnJQQtJ0xwDdDWnsVYnaBS5VxoJQP8PEdIdzmaq6pTd-lgbW7XtGlYqtUdGMIC2Viu5wmC-qev9MC5O5f52HhFk1vOnZFi17uEV02Y7-1mYw8xk7_WDAaS07rh3tUdcrhJNWF7_vLMld-AeRpU37lh8BA7UX4rGEO_JZzDBbjPiUMr5VEY8SQodxkuCrtN_JcFRVqeL4VzmIOK4xveJ2cutn9nLuw6kyHzcXJbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f1d85674.mp4?token=Itc7B4V--TR8QqqGs8QP5a41X8SwX3HwdPixghAkNIfvhdA1fQKHwnWh4-1eYlvEVP47Fg0ebkmd8pYMk5gBA_iOeRdj4ZogxgdX0S5Dw42Cq4YnJQQtJ0xwDdDWnsVYnaBS5VxoJQP8PEdIdzmaq6pTd-lgbW7XtGlYqtUdGMIC2Viu5wmC-qev9MC5O5f52HhFk1vOnZFi17uEV02Y7-1mYw8xk7_WDAaS07rh3tUdcrhJNWF7_vLMld-AeRpU37lh8BA7UX4rGEO_JZzDBbjPiUMr5VEY8SQodxkuCrtN_JcFRVqeL4VzmIOK4xveJ2cutn9nLuw6kyHzcXJbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلمون واقعا تنگ شد آقای ابوطالب
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104534" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104533">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13a3a57ef.mp4?token=Y7txw2esSLicSovpcb6QTGU9MRbARQhlxUMZHukPrrcZD7jbUOpE4CrwxofSwarKUmObm9Ba_T2rv13vtkKHT-H97ks5-jbLXiQe3QrN6dnBTQ4LR12LF3_dLaG5RAgPhbPz9NsAPRjOFxGF6JH9EljVMh-6QGM06PGqFnaoicnLBUguaAb_RSimeTumTq9k93pgvT8OGlHSyVHWeAkNUdbdHtOuqcfkz1YGn7stBXeQb90m2fGQKUyOm3QNFmmsE41lghIjkMOn-SDabulqDMPBbnfDacyBbhh7OT_b9XfGhzT9PpgM9OMPkbkFIDnegSnmM9Nt1HSze3ib-y238A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13a3a57ef.mp4?token=Y7txw2esSLicSovpcb6QTGU9MRbARQhlxUMZHukPrrcZD7jbUOpE4CrwxofSwarKUmObm9Ba_T2rv13vtkKHT-H97ks5-jbLXiQe3QrN6dnBTQ4LR12LF3_dLaG5RAgPhbPz9NsAPRjOFxGF6JH9EljVMh-6QGM06PGqFnaoicnLBUguaAb_RSimeTumTq9k93pgvT8OGlHSyVHWeAkNUdbdHtOuqcfkz1YGn7stBXeQb90m2fGQKUyOm3QNFmmsE41lghIjkMOn-SDabulqDMPBbnfDacyBbhh7OT_b9XfGhzT9PpgM9OMPkbkFIDnegSnmM9Nt1HSze3ib-y238A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چه فصل سختی در انتظارته آقای مورینیو.
👀
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104533" target="_blank">📅 09:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104532">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d382f7b092.mp4?token=ixiDyX53-5SYZGFiVJCQocunrh1fxcEOUJJY9U8UncIzzFXnvuSiTQE8QFkcFNhwYdzU--MaZ_z9RW_wVAE6vDZVAIRix7t6RUz6RvlnfAcXQZxtzv9N1fc-IkI1FYlDlwXUSsIt-cVitGn8hIGqrLUo5NeF87iHC0vPinzJh9L1SG6ehN5aBR3zMvMsU14DRcGd42WZjdL_nU0ccZGqVsUfarscdJ1BT_nI7GMpSbS0ZR7Z0t8pjcAZd7f-x8tmzG0HjRF0IYGQPMIx2U3X-KpykmoMK0RZiLBPRCM1-LjFWHNYMdIrCNOubRTguZb7e0D2zd-cAzohiIHNofRVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d382f7b092.mp4?token=ixiDyX53-5SYZGFiVJCQocunrh1fxcEOUJJY9U8UncIzzFXnvuSiTQE8QFkcFNhwYdzU--MaZ_z9RW_wVAE6vDZVAIRix7t6RUz6RvlnfAcXQZxtzv9N1fc-IkI1FYlDlwXUSsIt-cVitGn8hIGqrLUo5NeF87iHC0vPinzJh9L1SG6ehN5aBR3zMvMsU14DRcGd42WZjdL_nU0ccZGqVsUfarscdJ1BT_nI7GMpSbS0ZR7Z0t8pjcAZd7f-x8tmzG0HjRF0IYGQPMIx2U3X-KpykmoMK0RZiLBPRCM1-LjFWHNYMdIrCNOubRTguZb7e0D2zd-cAzohiIHNofRVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104532" target="_blank">📅 09:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=uBtV_A1LGjlVPnaqDsdUhLWeNko_9QBVer8avZXXiqJIfM3JWo8Fdp-OhjZJg19NEzPVj7jq10OK33Sn--c_vU9wvtBRlifL4TFkR51PKwA2U67PxJlq5ILoJ7A2X7frpjQaM6Q2nq-1uqeB_9xRf1b2Zg9C7_HYPomVV6lBbk9epkVmUksnfS9aqP6ootp33q8NWmDgErClN8Fid4xuid4juhnJsxyUyF8EswWp6torRjSoQuXZHKLiQM3rKeQshrkuqdyeWA_xl0yas2an4JYJ_IHd9IfKV74-RDFudeEza16wyWdk66mgbRkPj5f66JlhOjIPYV1Xm3lI1ftdZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=uBtV_A1LGjlVPnaqDsdUhLWeNko_9QBVer8avZXXiqJIfM3JWo8Fdp-OhjZJg19NEzPVj7jq10OK33Sn--c_vU9wvtBRlifL4TFkR51PKwA2U67PxJlq5ILoJ7A2X7frpjQaM6Q2nq-1uqeB_9xRf1b2Zg9C7_HYPomVV6lBbk9epkVmUksnfS9aqP6ootp33q8NWmDgErClN8Fid4xuid4juhnJsxyUyF8EswWp6torRjSoQuXZHKLiQM3rKeQshrkuqdyeWA_xl0yas2an4JYJ_IHd9IfKV74-RDFudeEza16wyWdk66mgbRkPj5f66JlhOjIPYV1Xm3lI1ftdZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
درگیری فوق‌العاده خشن‌ بازیکنان شمس‌آذر و‌آلومینیوم اراک پس از پایان بازی امشب؛ چه فوشای ناموسی و عجیبی میدن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104531" target="_blank">📅 02:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104530">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOn6rkNBObEC4byRqkmYEM_9rQ9kdjbPbY-xR-M05oNEn_-sDB5XyJq_UtyFiakkbYVtaE-6UMisHN3epNC0TlX-6UflrRMp4RXu8ArQ89S2OHTsFFaOxiQVCt2n5a7LSAzCcKjddNIW0YayyYYOl34F4tDMfBX4qJD4StqmlNI-116FvEKgKM9nD2hefwDtD8wGJiolHpEJ6gyjxm-cysOdOxcjcMj648jndHRfLXR0yOL-vcAyL70q1efNj1BYBXlvzYULRi3AYd1KM_JSunPHFsui-I3C8Q-rzT-EThd7ifKBdolderfk1k6xa_M-CJF1Km3YIbQEDDYtlv7jjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇪🇸
خایه‌کن اروپا؛ خط حمله بارسا بدون مهاجم‌ نوک و بدون لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104530" target="_blank">📅 01:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104529">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLKgnhnq12HRp95qjLyH0c0oTNnjHsp_UuobjmdwYHNhSlneUt0_dkLMb8Vef6SG0y_9Ri8dDd6_vbmKWsDYK5uVSUkOU0T5VCqxfcud34I9wI5XSCQ14INJGe6BSKhtjqr1f4OKICryOb2_xghAshNbiydNrJjEpDrtHPWEF9-bjoOCPHP32fTCILlk3M4Z66z_dz6L3HYmv7QtiOjq6YcuaOvGyfHxaGluhWHmOIoxJHFeFUO9bPtHLvvYK0VBfRxAdOn93mi4wGgUcxpcfQca6aKZTOjFEpMpAZOG1vQf8ckiWpUSk2Mcj7bUgjlvO0wnBUVy7GYf0NGPnhakIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری از نیکولا‌شیرا: بارسلونا در ۷ روز پایانی نقل‌وانتقالات تلاش فراوانی برای جذب خولیان آلوارز انجام خواهد داد. این بازیکن با بارسلونا تا سال ۲۰۳۱ به توافق نهایی دست یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104529" target="_blank">📅 01:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104528">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nc9v3ylnFfXI5T0taRAdUrnJsnseeh_b9JZQBQsFkutThMmgyZGTCWVjQU3cnVl9gbGFjM_-idJWayt7e9p-FRXETsWW6Ar3KIj4HfdT_K6CM3MI4P9gnWNpudT4ut6G6-PiM3ZRF_5DC4b7gQ_m4c9MUxUYuSd9dZx6A3fsem6m9nvD8xUPIfUu2dJxQrfJ6yw6FES31yqI1ux0lgfhp9y_VIwzPAPTLwcHLZrDB7eHDrXRqRtk9qKkLCPdWxalpH-CIgO3GLqjTeHzosxGH71l2XKUo0th9UvVW0dza4LqmaNXIlPmp2maKWzMkQzsvodGpYPfKNPLP85nXBNFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از نیکولا‌شیرا: بارسلونا در ۷ روز پایانی نقل‌وانتقالات تلاش فراوانی برای جذب خولیان آلوارز انجام خواهد داد. این بازیکن با بارسلونا تا سال ۲۰۳۱ به توافق نهایی دست یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104528" target="_blank">📅 01:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104527">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXg-1zcuYQXdMDNdZpMJsbQmKFzJQGYc_dZuWwiWyYgwH_u1XGdryeuZMTFI1XL6JJKsVYYqJZPX40q0DfYhNIIWbRRUSAczlHAgKRz1iklZAEZzcTlISZFpa8h16_e0VcXLhI-s6hwrw5E8eIrSEx-Hug38hL7zZ3KYJagHBree_mLp_-2LVXvaSkNfF8OqiYV0gs6zNjTroNKJQTwh_X3XOiXMLW5p4GdUPE9mncRh_nBpkVlLr9oKiplGz_Qjzj3TMr1UVHt7ObF_0Yx5bM_eIJOzEOi2uHOZdaDWVkpFx7_Qful3L8-u8WYb5Bf5CFPImzsBM1bS15DUAqj4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚑
🇪🇸
براساس گزارش‌های غیررسمی منابع اسپانیایی، گاوی بدلیل مصدومیت در بازی امشب بارسلونا بین ۴ تا ۶ هفته غایبه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104527" target="_blank">📅 01:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104526">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUAmrDnzo25jKvT_kkFGiVaEPoaJBIraoBxlAwn62us1tZfFYiWj5RmTtyASHk1MwN14najYMDOCXkXGJ4zmLGH1b-eoXNl3B9I9KtL58gg7kijU4qytHg7ojJl0Gk7ELgUEKEsTtt7LzbH-BD-YHgGQZg2VmbpDk0Ru2TRuITS4lGRI5N924YKpny5MomcrdZmBVQmFNMJePoY14UAxQmrerdD7kGhbsLMPVvNrhUsUbLHmcvZTHU9vRjcxeqCj9-KuCiXT7AMxXrK_yp4-LwFxGAFlrR_00Uyu89sy8qdZQD4KJnU0K_XBXjONzZ9t6ocnnLBi58QPEJs6J7aMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
امار درخشان رافینیا مقابل الچه:
۲ گل
۱ پاس گل
۳ پاس کلیدی
۲ ایجاد موقعیت بزرگ گلزنی
۱ پنالتی کسب کرده
۱ موقعیت بزرگ از دس رفته
۲ دفع توپ
۲ باز پس گیری توپ
نمره ۹.۸
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104526" target="_blank">📅 01:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104525">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ1jSInZONqL-rglCpP3oNmgiwe3lBis6R-nXCUc-LwpuYLe-jkn__NHPzPGkX0dDzf62fTy4B60lUOX1C-hI00FXlLPArYiwo1yKasmfDELsAnCuoAhJLnv8Cc5oer23_TcJMYemg_9DBGQk64leDvGwWI3Igh-5jP-ys0I2GPx55BhkWw0Z3K2wpsumpOmBh1-AY_JW2EmTDeHwfarIezvo0n1SkVz4PDAronjUAkLrTMzR3ovD4EV9Qr1xDiRghftkGkaqoOzr-WfRsQbfC5Wdfiv-wnu4K09UjTOUFCR8FhkqT6cYdSqM3R4GO0bID7MMHnH8Kw8njN-aSe6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فکر می‌کنی هوش مصنوعی فقط برای ساخت عکس و ویدئوعه؟ سخت در اشتباهی!
🤯
تو این کانال یادت میدیم چطوری ازش پول در بیاری
❗️
⏳
کاملا رایگان بدون نیاز به تخصص
🔴
اینده منتظرت نمیمونه
فرصت ها رو از دست نده...
https://t.me/+BO755zQm6VM1NDE8</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104525" target="_blank">📅 01:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104524">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZsIVVpOfVzWeu89nQLwjrcteyHJg9nRDEfniyP3MGL5HHWuSD-guFZ4EfgEzuwR8bgCR5HgQWgBmNYzOLESskW8CRH6nOdtYcD0kngstfy7yfpCdT0h0AL9G45ApKyPkP66io6hChQ5jZhh-2hEn5PaC8FYlzaOPZTEGvlkbcmHzf9dTDzO0BL-hFVlI_kMbkYg4JDi64yVkJ2IoP_ULLxqJfdUJAfuUUpoM95_QHMzMCw2cmLXwLtuzyU2mVU_kt2OhmQdCz4MnUdownaoLOB8ptUN2IdCopHJ5fOVnAcnruFdU46YeuBvmapFj9HQ45FZnWYJj-9Br2WFJchgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌دوم‌
لالیگا؛ بارسلونا با گلباران الچه برای رقبا خط‌و‌نشان کشید
الچه صفر - بارسلونا پنج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104524" target="_blank">📅 01:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1623eb570a.mp4?token=RJZG_wG71Gq3mc75R3jBsIjk3XDUi5H6JZTmex7hzixVHAD1TTJVu7uFn_YkRkSNwiJzXBkFAtmwETcJz__9zODAOVBN1Wp9ot5kluGwfzr7jidbfXYU11AcczUEYJs_Tk3Vv56AoIDd3c_kgy9cM-UADiMhoqBAp3Lpb37tEbLKNWZ4GcY_AAeveh7IiIeVpRrh-YCXcGjeKZWSGH0GDwBd4FiDWtVzCkWv-ueZwNdIEBrfdltwlpvBLCGKg2IUb3Rq8dmFYJ5ZzjPxM7uABGWct40F4grQ_LMhMQm8h7rPWtLXf4V8dbTj7Nh9wwatTwT6NX-g853EUxOv5bgkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1623eb570a.mp4?token=RJZG_wG71Gq3mc75R3jBsIjk3XDUi5H6JZTmex7hzixVHAD1TTJVu7uFn_YkRkSNwiJzXBkFAtmwETcJz__9zODAOVBN1Wp9ot5kluGwfzr7jidbfXYU11AcczUEYJs_Tk3Vv56AoIDd3c_kgy9cM-UADiMhoqBAp3Lpb37tEbLKNWZ4GcY_AAeveh7IiIeVpRrh-YCXcGjeKZWSGH0GDwBd4FiDWtVzCkWv-ueZwNdIEBrfdltwlpvBLCGKg2IUb3Rq8dmFYJ5ZzjPxM7uABGWct40F4grQ_LMhMQm8h7rPWtLXf4V8dbTj7Nh9wwatTwT6NX-g853EUxOv5bgkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل پنجم بارسلونا مقابل الچه توسط فرمیییییین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104523" target="_blank">📅 00:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این الچه بنظر خیلییییییییییی بیش از حد تصور کیری میاد. دفاع کردن بلد نیستن اصن
😐
😐</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104522" target="_blank">📅 00:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلگلگلگلگل پنجم بارسلونا فرمین لوپز</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104521" target="_blank">📅 00:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff874a3d34.mp4?token=CebpsPAzb-WuTSOzyuwazsJmLthYUeLb5M3moeycjsqZ3aFH5kWhR18kaEGXEQqsJHsFT2TTUP-3Rv6vyFGqChEw3go5NAepmu5FER7PuNTsorTiAt_dkVp5fe4NkXXj42Bu5KEDo32te0WB16LPa8NZFh-_Q0kd_-39TvZ1bOMjgNNKOrXaO1aEBNMFIR6bmYjokmACKCSLyEOkATLale4ePlV7mqntEnW91xwnB4TnT8tM0fP6Pume9XWNbf32djyKipx7UAi-zfj8SuMnP-pXTSVrIIj5hElG9W5VFMqibQ8bkK5qkF3NPwuNf7xv2Zxz3L0OShp242PusEE9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff874a3d34.mp4?token=CebpsPAzb-WuTSOzyuwazsJmLthYUeLb5M3moeycjsqZ3aFH5kWhR18kaEGXEQqsJHsFT2TTUP-3Rv6vyFGqChEw3go5NAepmu5FER7PuNTsorTiAt_dkVp5fe4NkXXj42Bu5KEDo32te0WB16LPa8NZFh-_Q0kd_-39TvZ1bOMjgNNKOrXaO1aEBNMFIR6bmYjokmACKCSLyEOkATLale4ePlV7mqntEnW91xwnB4TnT8tM0fP6Pume9XWNbf32djyKipx7UAi-zfj8SuMnP-pXTSVrIIj5hElG9W5VFMqibQ8bkK5qkF3NPwuNf7xv2Zxz3L0OShp242PusEE9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم بارسلونا مقابل الچه توسط فرمین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104520" target="_blank">📅 00:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلگلگلگلگلگل چهارممممم بارسلونااااا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104519" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگلگلگل چهارممممم بارسلونااااا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104518" target="_blank">📅 00:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ac58b5d2d.mp4?token=Yw8v1qQReg9VCpSBo4egIVUt8pt-r1ZZhYFoNvVLr3_6jhldPJgKnoyQqNJj5-PCmswKXV0lc0oiFpc_Ll9pTECVe6kmmyeB9sL6LzV6YVgkIJhJQYGah-7RaNDJOxLAfCW530VWXvMc065o75KlyhHXKnM28IjktPqCBQYknzuV9VME-xJvi3198ZJFjYSW-QWzl_zHkxGYAloJpoojVsM99xYz1IBCuvFYN2a-wt-9zsPEFGj8_bY8DHBlQgDMhAAIR3xS0ef-jrQin5b44JSh1cW7kZr_C3tIB7-zt6qfjuabCxjfatG9G8ygps-mI-xBNv2nvkiiWkPMzCAZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ac58b5d2d.mp4?token=Yw8v1qQReg9VCpSBo4egIVUt8pt-r1ZZhYFoNvVLr3_6jhldPJgKnoyQqNJj5-PCmswKXV0lc0oiFpc_Ll9pTECVe6kmmyeB9sL6LzV6YVgkIJhJQYGah-7RaNDJOxLAfCW530VWXvMc065o75KlyhHXKnM28IjktPqCBQYknzuV9VME-xJvi3198ZJFjYSW-QWzl_zHkxGYAloJpoojVsM99xYz1IBCuvFYN2a-wt-9zsPEFGj8_bY8DHBlQgDMhAAIR3xS0ef-jrQin5b44JSh1cW7kZr_C3tIB7-zt6qfjuabCxjfatG9G8ygps-mI-xBNv2nvkiiWkPMzCAZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم بارسلونا مقابل الچه توسط رافینیااااا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104517" target="_blank">📅 00:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104516">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d25fa697.mp4?token=V_wDaiaY7lc4jGHONTK0f-UfflpFBv6wJpvMTpgoEcIm-7xIGMEVSQuU1LhS8q2c5bG3D2SgKFqu55dMnyowUGZjcpV__mvFfoCPruI9NDYw2zlZFdZ8-b6lkLQTJ0r2elRIZvOFUkpugjZN-Z5PoSRYkcNs35P5LtU9ZNBLy_TLyJU0N3KOjfDoCI3hA-_DejBt3KHSIVFL4jn0FFx5-SeJChtAcLVCJsA2Sj6WTT3Mu37uSGE31Kibmk1F5GN9jOaDO2dcRSVjs5bz4MfGZAknFjCKnV6lZjqu1ZT0pMMbNvY2QQtR3pDTcqJOarbsLMxBn9LP69mRRe5Uv9NMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d25fa697.mp4?token=V_wDaiaY7lc4jGHONTK0f-UfflpFBv6wJpvMTpgoEcIm-7xIGMEVSQuU1LhS8q2c5bG3D2SgKFqu55dMnyowUGZjcpV__mvFfoCPruI9NDYw2zlZFdZ8-b6lkLQTJ0r2elRIZvOFUkpugjZN-Z5PoSRYkcNs35P5LtU9ZNBLy_TLyJU0N3KOjfDoCI3hA-_DejBt3KHSIVFL4jn0FFx5-SeJChtAcLVCJsA2Sj6WTT3Mu37uSGE31Kibmk1F5GN9jOaDO2dcRSVjs5bz4MfGZAknFjCKnV6lZjqu1ZT0pMMbNvY2QQtR3pDTcqJOarbsLMxBn9LP69mRRe5Uv9NMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
تمسخر گویش کنعانی‌زادگان توسط هوادار تراکتور: تونستید بایسا و یئال رو ببرید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104516" target="_blank">📅 00:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104515">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d106b59a1d.mp4?token=hyPCozUjrdF_ca1egKxYxk_jZwKSkV0cPpdr6vLOjtEj5Hjq2cMPklcCuQrmbH7kPu90meEyxl_QrupQkDwcu-chXndcePNrdAv5yINid_zqHveTOqmXSeuQ4Jp0OzF1zDTtLCr7RPFrYeeiYa3-RVV6xcjZL3nzPbM-770FybirsVg02EtFutK3F9mlUhVidK1Mx-AYoTOaPkye9QZOydbZ5owOQfz24pRELBXA-Fc9KPwXimFRok9Yb50t9vCOr07li020ZB7NO9xEJ7rTE_T-iSHip-v6yS0vJXZc5jxtM9-Blau9Fuj85BjyN5VNpqeA-vNyjAF37rG7OkrqC3B4-DFVskcE-sBn_9I8KnJ2cLYdVZehDw-wzc3zZHvWjUHmlim6gz4DozK9OSt1PWHn7xlm6fBV2YyXW7sN2wCBQs1PCpJ7tssHYTpD9lj-xg_TnlNBWm02TZUsbAsZXZrraY4kz-H3haMPUO6P-ll6oZKrzWwbcNfygW2ZC7ES11JTIcQ9UXnDY_nHzutJvuTVNN2nQW1ulukqjKbM9StLo4VGY_c0XYfZlMnMb3JAvIXYGL3b7NuDAEWIHIm8vloMbBkNQrWA0Tu9Nj1QgSL01ot1lUupLhHtxaiRUzkxPqVUQTkinzqlwX08cl4XtbQ5EDPo02GnJ_vzOib2Dxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d106b59a1d.mp4?token=hyPCozUjrdF_ca1egKxYxk_jZwKSkV0cPpdr6vLOjtEj5Hjq2cMPklcCuQrmbH7kPu90meEyxl_QrupQkDwcu-chXndcePNrdAv5yINid_zqHveTOqmXSeuQ4Jp0OzF1zDTtLCr7RPFrYeeiYa3-RVV6xcjZL3nzPbM-770FybirsVg02EtFutK3F9mlUhVidK1Mx-AYoTOaPkye9QZOydbZ5owOQfz24pRELBXA-Fc9KPwXimFRok9Yb50t9vCOr07li020ZB7NO9xEJ7rTE_T-iSHip-v6yS0vJXZc5jxtM9-Blau9Fuj85BjyN5VNpqeA-vNyjAF37rG7OkrqC3B4-DFVskcE-sBn_9I8KnJ2cLYdVZehDw-wzc3zZHvWjUHmlim6gz4DozK9OSt1PWHn7xlm6fBV2YyXW7sN2wCBQs1PCpJ7tssHYTpD9lj-xg_TnlNBWm02TZUsbAsZXZrraY4kz-H3haMPUO6P-ll6oZKrzWwbcNfygW2ZC7ES11JTIcQ9UXnDY_nHzutJvuTVNN2nQW1ulukqjKbM9StLo4VGY_c0XYfZlMnMb3JAvIXYGL3b7NuDAEWIHIm8vloMbBkNQrWA0Tu9Nj1QgSL01ot1lUupLhHtxaiRUzkxPqVUQTkinzqlwX08cl4XtbQ5EDPo02GnJ_vzOib2Dxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به الچه توسط کریم‌آدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104515" target="_blank">📅 00:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104514">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb0b5f685e.mp4?token=UG0v5dHDHA1uoaLjMwZQmsDROYgrDR7_k_lpOxUn2HAL63RJyO-4u4Wh7RCyo9KwE0J9j7AVu4Z4pmJfudO0pR71vGIJaPGmRxXV7X_qN_Q79iqtAar2DX6wsHCx90ICit2nNEhfspm975zmaNVN95Mc4qEUdUd8iFBGZ_KBIPICcaZDfLGTGsmG3hXmjy64DUO2MCn4eUpGMK7xwIzoZlvDITpUSstGrJBxTFNW7x3HE1wBKNzEvga1XxRT34sGn4XzTNT-MCwRbspsvMx1LG5I7EjWijdejxPUQBYeFebNzhkXE4t5Ysrd2sv3a6Hysp0fLKUdzKNHpKwgpkyhU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb0b5f685e.mp4?token=UG0v5dHDHA1uoaLjMwZQmsDROYgrDR7_k_lpOxUn2HAL63RJyO-4u4Wh7RCyo9KwE0J9j7AVu4Z4pmJfudO0pR71vGIJaPGmRxXV7X_qN_Q79iqtAar2DX6wsHCx90ICit2nNEhfspm975zmaNVN95Mc4qEUdUd8iFBGZ_KBIPICcaZDfLGTGsmG3hXmjy64DUO2MCn4eUpGMK7xwIzoZlvDITpUSstGrJBxTFNW7x3HE1wBKNzEvga1XxRT34sGn4XzTNT-MCwRbspsvMx1LG5I7EjWijdejxPUQBYeFebNzhkXE4t5Ysrd2sv3a6Hysp0fLKUdzKNHpKwgpkyhU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گلزنی فران‌تورس در بازی امشب پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104514" target="_blank">📅 23:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104513">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50615b177d.mp4?token=SHRZQ9l_wTx9irEOQAnXhREeAKRSmEEn2eR1BLzGdrrdSPEZZYAua9SKLkcDLTdZBcE0gTkBAKJL_hmYVloXG6FpB7S0O3erQhZaUgmRlIWtl2scatyLoy8FhZpCPk8Ud4SjGfo6X6c1SBoNPA4k34GAiXrVFqOmSl_o_o2Yp_iJiXP9C5Kvbk94KxpSN-hFGXxqcYkoSPtRd4ilCw19qSPW4x9R5gc2qEJbwg79rzCdcTC9KdVJLvISKDYgHyVABgkxgCEfAmJMd6LhqVFshrLC8-a2BIY1UxjROsbub-MCqixryHr5cyn78TlTt7oyIRvBg6GJqs9g6EbmAwKp51EBQVNHA2b7xoAt6zYMM54nJenAiKtBDT3AZBTLgIL43npDPTzNWWrNx1yv2JgJoyi9vRradqi8ZZbLruc3GUeggFuEstXbTan2vmHa_t42lAqaYXEFOqRgnnwHeTV39m1nWsdQxUBwG9fR0KgT4yWYG0KR8ymXuMKzWu5BNq1hapKG36nJ_PLggXbYHPNkhNZXpENN6DsGUVF-60hUTWyy1iiG7G7rNQxVVupOvpNNIDYLCZ5bZlee6IEQOyZjBdVWmH0Q0O8qyvFz3OqTMQHaDGXvwrYlq8x7XT4FPwgV1Usr6KN2xV4g38aAMboud45qRLbv70YHTTwk7ig6ZZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50615b177d.mp4?token=SHRZQ9l_wTx9irEOQAnXhREeAKRSmEEn2eR1BLzGdrrdSPEZZYAua9SKLkcDLTdZBcE0gTkBAKJL_hmYVloXG6FpB7S0O3erQhZaUgmRlIWtl2scatyLoy8FhZpCPk8Ud4SjGfo6X6c1SBoNPA4k34GAiXrVFqOmSl_o_o2Yp_iJiXP9C5Kvbk94KxpSN-hFGXxqcYkoSPtRd4ilCw19qSPW4x9R5gc2qEJbwg79rzCdcTC9KdVJLvISKDYgHyVABgkxgCEfAmJMd6LhqVFshrLC8-a2BIY1UxjROsbub-MCqixryHr5cyn78TlTt7oyIRvBg6GJqs9g6EbmAwKp51EBQVNHA2b7xoAt6zYMM54nJenAiKtBDT3AZBTLgIL43npDPTzNWWrNx1yv2JgJoyi9vRradqi8ZZbLruc3GUeggFuEstXbTan2vmHa_t42lAqaYXEFOqRgnnwHeTV39m1nWsdQxUBwG9fR0KgT4yWYG0KR8ymXuMKzWu5BNq1hapKG36nJ_PLggXbYHPNkhNZXpENN6DsGUVF-60hUTWyy1iiG7G7rNQxVVupOvpNNIDYLCZ5bZlee6IEQOyZjBdVWmH0Q0O8qyvFz3OqTMQHaDGXvwrYlq8x7XT4FPwgV1Usr6KN2xV4g38aAMboud45qRLbv70YHTTwk7ig6ZZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حضور هواداران مقابل هتل پرسپولیس!
🔴
تعدادی از هواداران تیم تراکتور مقابل هتل محل اقامت پرسپولیس تجمع کرده و شعارهایی سر دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104513" target="_blank">📅 23:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104512">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66baa2f686.mp4?token=IeUnIoYg48n4GkpX4qsfxCWvocwgaPBwdj9lVVNRKxFMd3kqnOPUF8X3eT4fEtshLGyd7otnnXTm9y1j-edxKYGEY6O5rbdDuzgZaTMleqALU1OlMqiH53MemUr5qix8LAhH8mivB0Igyg3s-mCfCkFgzRdYWREwCouqNPCH0-ZGljyQaOgqfkrAzUTy_BzSx27wvJVFPMLYHlFbqiEcI35FFURbMQQZYYjjUJj5FD15Lwlhzp_Uinl59tz8sJzP2AfCPXz2zK5W3YvCaI5-oZKGl19TVgfKUoeiZZUuGEdYnhthjuMvuERH3WMSm1KrjE2zqqyAFBKaB0tF_I8U9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66baa2f686.mp4?token=IeUnIoYg48n4GkpX4qsfxCWvocwgaPBwdj9lVVNRKxFMd3kqnOPUF8X3eT4fEtshLGyd7otnnXTm9y1j-edxKYGEY6O5rbdDuzgZaTMleqALU1OlMqiH53MemUr5qix8LAhH8mivB0Igyg3s-mCfCkFgzRdYWREwCouqNPCH0-ZGljyQaOgqfkrAzUTy_BzSx27wvJVFPMLYHlFbqiEcI35FFURbMQQZYYjjUJj5FD15Lwlhzp_Uinl59tz8sJzP2AfCPXz2zK5W3YvCaI5-oZKGl19TVgfKUoeiZZUuGEdYnhthjuMvuERH3WMSm1KrjE2zqqyAFBKaB0tF_I8U9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به الچه توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104512" target="_blank">📅 23:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104511">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8a179a36.mp4?token=o-hl9ThgImiokJoRoez8ToM1BoRgXxUaTTlfp8zRVrZxdX4IN0PWVOMcVRYHUqlgFkKNgs8_nKU1f2WvCoPp93MuJixgUTLASEBnhK5p1IJ9mN95rBLYjzhe5lmd8WdiXZX00IzfuXNQzzL42u3oBdrx81NeM5zSySiE1rBP24xDEHldN5kwJzlNKhMe5fNM_exyZZFJc1Y5rr7woYBjAQ990NWS9m7lLsDxmU9i53G2yM3QSXDeddX7VLZFaIaC-XUx2ppfAuSf0Gb3u9-oLnagCoHktV582iVxeag0A2BSzr7VE4peHJLVY6RNWSu4YbqsZkq_e5nmNT-wU1S3H5AYYvq9MApZAM8kdRSqeLxYhOkd1o8rSPFQbFr3lqwlLe-4jPPE7YA5--DDWkpyg2SFNGhxfaw4ZJ68llzLo6CPEpjs5vo4kouj5xeagDz-dVMq-aYSmOfP3QBuOo5Bu8Dn7DRpp8E3lOuz4c3oI7ZQSDtDJKcDJZRi0q7t-qoNdI8sx3tIgBcFqGXlr13fkchhhLBmlNbMTesCus82TOn1Ffjr3Gj7vsAjcAYqStKjdxBMOge4QVonvVCntoL1WLWVzCN_gIBumZV_pw-t542sP5HuTvntqrL_aedImLzkBPnyNJ2ZL0o7ApB1lTn7eFbC1ifzjF73F6Jc3vvTNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8a179a36.mp4?token=o-hl9ThgImiokJoRoez8ToM1BoRgXxUaTTlfp8zRVrZxdX4IN0PWVOMcVRYHUqlgFkKNgs8_nKU1f2WvCoPp93MuJixgUTLASEBnhK5p1IJ9mN95rBLYjzhe5lmd8WdiXZX00IzfuXNQzzL42u3oBdrx81NeM5zSySiE1rBP24xDEHldN5kwJzlNKhMe5fNM_exyZZFJc1Y5rr7woYBjAQ990NWS9m7lLsDxmU9i53G2yM3QSXDeddX7VLZFaIaC-XUx2ppfAuSf0Gb3u9-oLnagCoHktV582iVxeag0A2BSzr7VE4peHJLVY6RNWSu4YbqsZkq_e5nmNT-wU1S3H5AYYvq9MApZAM8kdRSqeLxYhOkd1o8rSPFQbFr3lqwlLe-4jPPE7YA5--DDWkpyg2SFNGhxfaw4ZJ68llzLo6CPEpjs5vo4kouj5xeagDz-dVMq-aYSmOfP3QBuOo5Bu8Dn7DRpp8E3lOuz4c3oI7ZQSDtDJKcDJZRi0q7t-qoNdI8sx3tIgBcFqGXlr13fkchhhLBmlNbMTesCus82TOn1Ffjr3Gj7vsAjcAYqStKjdxBMOge4QVonvVCntoL1WLWVzCN_gIBumZV_pw-t542sP5HuTvntqrL_aedImLzkBPnyNJ2ZL0o7ApB1lTn7eFbC1ifzjF73F6Jc3vvTNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نویدکیا: از اینجور تیم‌ها حالم بد می‌شود
. امروز نمایش هفته پیش را شست، برد. هیچ بازیکن باکیفیتی امروز نداشتم! امروز هیچکس را نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104511" target="_blank">📅 22:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104510">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7icfMK2fCciLDKi4QoA4OJqcD5aqJGdNApr7_4j6sDcNi149HLY_-xRp-rKfl5Z9tGawQVW6jFrMsY_Bjo_tsRvLG46Hs7MKrXn3wLU0QPYZxIUaesItfnFprvshSm3hczZ19bP4qSMYVj8JnEHl0sBZVv5gBIc7hTIJSjg3d3L6Idm1zMIkVzoBjq1dwHosomtHvSNmNd9c64WCgViROOlGnhru96L045h1Hy9RsHsKlENCNB5lD5-V0GSSxnWiOBoaq7LvYHV0FV84a7jLoOTZSCqqU1Yz1suIu5qf__74JZPTmJAvfBzthXXC_lj3DzOpBnm0BveY_7E4SEa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
#فوووووری
؛ باشگاه سپاهان از استقلال بابت استقلال از یاسر‌آسانی شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104510" target="_blank">📅 22:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104509">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
🎙
بختیاری‌زاده سرمربی استقلال
:
🔵
من هرگز صحبتی از پنجره بسته نکرده‌ام چون اول فصل گفتم که بازیکنانم را باور دارم و تجربه نشان داده تیم‌هایی بوده‌اند که با نفرات کم، نتایج بزرگی گرفته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104509" target="_blank">📅 22:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104508">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a46aea259.mp4?token=CBtBWmrVpfmTme1ITUgjw4NLhC1SazBU0-xQQU_sXI0FRkKQUNIM3gHNn4fOGuCldgcqvAwrUFEdQmUpjYVPuhN78h0tqE3_R0q2neHey0La1Ep-tNZwNJ3Q9dW3ZaKaa4GhBok9rPsEf18pK50WgOpxZkTpUUMJyK2FghKPidGOGFHKt5bIzA20rHPN97kU9qLj3h8rW6kG050j8BIM8U1iIfL5qx5JyOQX8ZP9gep0hz5I7_ad5sqNI5zNYSfYrfL_S2d9BUn-IXJrVcdODuR9xsqOfZOZ2S2dXjc-dB0xNF_QGDlyKkhk1EdGuLUjP3xpr6VzmYws1XWkIcmGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a46aea259.mp4?token=CBtBWmrVpfmTme1ITUgjw4NLhC1SazBU0-xQQU_sXI0FRkKQUNIM3gHNn4fOGuCldgcqvAwrUFEdQmUpjYVPuhN78h0tqE3_R0q2neHey0La1Ep-tNZwNJ3Q9dW3ZaKaa4GhBok9rPsEf18pK50WgOpxZkTpUUMJyK2FghKPidGOGFHKt5bIzA20rHPN97kU9qLj3h8rW6kG050j8BIM8U1iIfL5qx5JyOQX8ZP9gep0hz5I7_ad5sqNI5zNYSfYrfL_S2d9BUn-IXJrVcdODuR9xsqOfZOZ2S2dXjc-dB0xNF_QGDlyKkhk1EdGuLUjP3xpr6VzmYws1XWkIcmGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
آسانی : مهم فقط 3 امتیاز بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104508" target="_blank">📅 22:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104507">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f173b09f.mp4?token=Xr8U453H3xELGpPkMXd304eP4zcQDry7Usp0qCLl5hiX5-UAO_VKA35V5KY8YyiZefm-ENHFOJqA7hKe9fdomw6FO5sB7tWGpvWh1sOh84L5TZyTs2aWBX3bMA6bM1kjeRHiAA4uv1VgWcj4n5uQjBg9nWr7uC74c_15_vb-y7Z-V-BlV7DCPl9kXwk4yvctvbNIuntTkteCwPtREj-d1TogjrB24Hqb7zZj8FRIIzVOCGXJanm6EWTdDeiXj0V6AzVlE7iXw7KRxUApShYa3dEFpwkYYaFqkh6i4tztVXZW0-t3_g9Certk9UpH8hfH6OAoEW3B1aJAbchqxErDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f173b09f.mp4?token=Xr8U453H3xELGpPkMXd304eP4zcQDry7Usp0qCLl5hiX5-UAO_VKA35V5KY8YyiZefm-ENHFOJqA7hKe9fdomw6FO5sB7tWGpvWh1sOh84L5TZyTs2aWBX3bMA6bM1kjeRHiAA4uv1VgWcj4n5uQjBg9nWr7uC74c_15_vb-y7Z-V-BlV7DCPl9kXwk4yvctvbNIuntTkteCwPtREj-d1TogjrB24Hqb7zZj8FRIIzVOCGXJanm6EWTdDeiXj0V6AzVlE7iXw7KRxUApShYa3dEFpwkYYaFqkh6i4tztVXZW0-t3_g9Certk9UpH8hfH6OAoEW3B1aJAbchqxErDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
رستم‌آشورماتوف که در پایان بازی با لنگیدن از ورزشگاه خارج شد، مشکلی برای بازی بعدی استقلال مقابل فولاد خوزستان ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104507" target="_blank">📅 22:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4773567450.mp4?token=sGea9d5NwG2_b4vA6KP2TPMevheiyCUN0wRXFN7qKOBCkj1NLwyDBt2hFKo_RMy8emM5aFMrb_qAQoCY62az_0EiM2nlUOw_yiKVNTNHjg_72-bs7SHuw-MHvWNpDWICLBVOvm0BqB-1odbzjxdsdWkLfnJToTGyKpdqTqs0lZd-k-tec6iq6f3pGMOY2W4mU9eKHmeCUgpnmGUPz-N3iH1Nuep82NnxGk0F_WujnCglfLU3uzkcHRGPL-c4ORoJq7Voi8XUGVpfz9bqtIBdowqyl_LrTLMkAxv7TcHNRpVgQM0nCBpPVVSKXzVDKp6blNKm5uYdte4T3f-nQc1uzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4773567450.mp4?token=sGea9d5NwG2_b4vA6KP2TPMevheiyCUN0wRXFN7qKOBCkj1NLwyDBt2hFKo_RMy8emM5aFMrb_qAQoCY62az_0EiM2nlUOw_yiKVNTNHjg_72-bs7SHuw-MHvWNpDWICLBVOvm0BqB-1odbzjxdsdWkLfnJToTGyKpdqTqs0lZd-k-tec6iq6f3pGMOY2W4mU9eKHmeCUgpnmGUPz-N3iH1Nuep82NnxGk0F_WujnCglfLU3uzkcHRGPL-c4ORoJq7Voi8XUGVpfz9bqtIBdowqyl_LrTLMkAxv7TcHNRpVgQM0nCBpPVVSKXzVDKp6blNKm5uYdte4T3f-nQc1uzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇹
🇮🇹
یوونتوس در هفته‌اول سری‌آ با تک‌گل برمر مقابل فروزینونه برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104506" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d5a7c170.mp4?token=voVH5PWizndORMonj1dWKsENRDWnPuCgzKzqPRLQKHdCL55DLtuVVEIpInqJ58SixPwlJNR_3i5OClBUSThqPtO_a_JMxySgwqEO3bfqDxYThPMJIJKB0MZyZmgbjocxPtJPDcHBVBiRFMZ2YOXhixQLv31UVH6ZtlnN9xRQx0k3aNk3EtwFuWWyRF2WM302d_LvDuFtuzIB_rBiKWZVEvc8QY-YBPeWq0CS8Kftdb1D2aOCIaW4dVxSFWQ4K500ibOq42DkGjlS45BcyfxuOHYpPqr2q5uilIN779AVfElyuLujG6-xt5OaSWjkWdOx-D9QTdJDqQow1OmrrnO6W0JygkbZFGa3E3a2T8OH8SBq0GXy7OdlkyabSZnwnbdqsgpYssMoPvxOVElPsOFx367kxha92jydyK2nBeFpJVUiX92XQ4GathJgepf9MNtu7oSkq8WeKCQVsGpj9SdHePcPNKRhPK6tdmoS0IJhQzY49xjr2sXXm9ilpUOx-i4OKBdv9cb89xn_-6l9mtOBfVuKz4OSDfsaR_8h1cuIrWJVO62_0kC9nqyn4eT_Sx4_2ht5OQL658AFuPiqiyQh70MV5lzu6thN5d9TkjHqDiF0p5m8H50k3o6JUYlwVMigCGGu6bqAn4LHSNyuBCfcvRLKTsjZpImisxJnMN67ebE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d5a7c170.mp4?token=voVH5PWizndORMonj1dWKsENRDWnPuCgzKzqPRLQKHdCL55DLtuVVEIpInqJ58SixPwlJNR_3i5OClBUSThqPtO_a_JMxySgwqEO3bfqDxYThPMJIJKB0MZyZmgbjocxPtJPDcHBVBiRFMZ2YOXhixQLv31UVH6ZtlnN9xRQx0k3aNk3EtwFuWWyRF2WM302d_LvDuFtuzIB_rBiKWZVEvc8QY-YBPeWq0CS8Kftdb1D2aOCIaW4dVxSFWQ4K500ibOq42DkGjlS45BcyfxuOHYpPqr2q5uilIN779AVfElyuLujG6-xt5OaSWjkWdOx-D9QTdJDqQow1OmrrnO6W0JygkbZFGa3E3a2T8OH8SBq0GXy7OdlkyabSZnwnbdqsgpYssMoPvxOVElPsOFx367kxha92jydyK2nBeFpJVUiX92XQ4GathJgepf9MNtu7oSkq8WeKCQVsGpj9SdHePcPNKRhPK6tdmoS0IJhQzY49xjr2sXXm9ilpUOx-i4OKBdv9cb89xn_-6l9mtOBfVuKz4OSDfsaR_8h1cuIrWJVO62_0kC9nqyn4eT_Sx4_2ht5OQL658AFuPiqiyQh70MV5lzu6thN5d9TkjHqDiF0p5m8H50k3o6JUYlwVMigCGGu6bqAn4LHSNyuBCfcvRLKTsjZpImisxJnMN67ebE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📊
عملکرد سید‌حسین‌حسینی مقابل سرخابی‌ها:
🟥
پرسپولیس: ۱۵ بازی، ۶ باخت، ۹ تساوی، ۲۱ گل خورده و فقط ۲ کلین‌شیت!
🟦
استقلال: ۵ بازی، ۲ باخت، ۳ تساوی، ۱۰ گل خورده و بدون کلین‌شیت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104505" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7ToHGZWsrSrPyufo_FmdzdtV4NhI8fC2TLPoN7-lT2WiLDS3c89KUCcsUdYE1PUaSYG_3LR60IP4EuFSdgdeAh4Wh59KDiqIjS1kpJXuQJw1RrWVjGW-50JToJb1xrQT3Vx3Z9b-Q3h1GoF4dD3e83ky21CxrunJef8pmsmJ1AGdf0ndihIaWYFv_rGK_tmIUFwjgDoMsKXK9lurx6ggMtLO5x-9IesgBvn6CInhYiz1cYbZNA44zdSIr0wBadgEv3sR3rGkHfXRhXU_J6gV7mWeZg0_wC9IhVcKFke8P3PUlWct5ZUImLzP51lP9OmMkEZPhuA9aleM0FWal-J1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
از کیت‌دوم باشگاه پرسپولیس رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104504" target="_blank">📅 21:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk_oXfnl1LHxucNHG9ZPg0KAHS-5j5eMP7X1zMVsCbxRDIobVeJXdXfk82My2ZHp7YHGVdXZqRVFcqmNVC6JrLum0JYyE2NrS4z1tbLxi6R4qTyuOpojueUA-m34G1Ke9xWdEgGntl5t29XjlKnz1aE2xIfgvGa4W9lHiI3j_7RwZQ4mbQcgXmHQXp_3223szeFL5uVnXF0E9TNX_BH5VdOf4ScolaWotyIZ7SK5CjJY7u1ANRhYfKzZo5TxkJLwmTte3XzMnELd1_9e3DZ7WYSkFNyFgXSIOCEczxdLgvbczNtZBaLcOfjmelUvwmZtozCa-WiiryhlCCuYra0c1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
ترکیبببب بارسلونا مقابل الچه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104503" target="_blank">📅 21:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNhCjL6S9Giti8vpzSjWsjDHJeerB-5MPuHOcJWtBRTeagtqiPf7bR6aW_8pfNUhMfUZ3GEfa1m1BrBTUEG5jYvzIbZw8ASqm_BosaQLB_CVA_vpPa9kipTubffAL6ulMRgvhfdkfzqkP1f9HoUFSDpuhJAzZJwI9tWVNcQ8epaXGs_1ZHRq443zxR8ORCCwCXi0RTR0fT_U_a2HuzumFbSHkpe0nuwLVLEQ4u5-E4yNNbW4qt8wP8Vi8scsWsQxEBNaYfvsosITSzgus12-5ErRnT7KYoNo9wxv1aXQQyxLtrBsjBliyXTF0cic8Du48aLs1sJB9IueDagJ_3OWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
ترکیبببب بارسلونا مقابل الچه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104502" target="_blank">📅 21:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5de5rjNQ3urKanOTMseMDLwj8lf-E-nWQTA4L3EWeuR2wTQa5jDPzc-TGe9cBTUW_vyLS6pEXTXxD5i-TPX9jPc_V_Qeh6MvH8iYhii7BkLX8lq8L01K-J4eC6qOhDjv2QVjdVIoXkmZtvo_ZQrvy6OuISet9rSPGreyD_52CORyuknNU8A75qi8ddQLC0klaBQ7jd4epw500unuQLpvHApXm5QOP7hoQRpR17uVOy9IvVK2E8X_HV3S3i_OT7CwdmctgABRptFW4d4YquWwIqMQjG8U9DJlY9FjF-eppIlikrhkn7DRpB9Qo-qC48LN-9r9YKbocF9Wkb7R4SjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
الچه
🆚
بارسلونا
🇪🇸
⏰
ساعت ۲۳:۰۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104501" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104500">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ec3ad2dc.mp4?token=bSZMNNzQDSGfXApWNZ_-IpJtO4P3D1JEHC-cIllXSXPGPTzWMxMt_giqjJUvohd0TOyosxj-rCZ4bIC-LvNf-WNzdB8Jm-Yi7oFe7zvew73qakQHrazx30sDZHbYImwf6Rlpx86xL4_yyhCVBxyi7RlAeJebguMmSDLmpwAW8LthVfg6H2t6njSwmsQ_JzC4egPVUf_VepXyrk_n0iRu20iHzyiA29plRPeJnMNXTjSWi59E71TkOYaKrC_GkueTw_Bvr867I-B2y5jVmq_L4w9k1wn2lCOltDX0n6QVKZ5MiSnbK0ht-mcKYe2o0WDnmqyW44Z0tX1KGzS6zDwb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ec3ad2dc.mp4?token=bSZMNNzQDSGfXApWNZ_-IpJtO4P3D1JEHC-cIllXSXPGPTzWMxMt_giqjJUvohd0TOyosxj-rCZ4bIC-LvNf-WNzdB8Jm-Yi7oFe7zvew73qakQHrazx30sDZHbYImwf6Rlpx86xL4_yyhCVBxyi7RlAeJebguMmSDLmpwAW8LthVfg6H2t6njSwmsQ_JzC4egPVUf_VepXyrk_n0iRu20iHzyiA29plRPeJnMNXTjSWi59E71TkOYaKrC_GkueTw_Bvr867I-B2y5jVmq_L4w9k1wn2lCOltDX0n6QVKZ5MiSnbK0ht-mcKYe2o0WDnmqyW44Z0tX1KGzS6zDwb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اعتراض شدید هواداران سپاهان پس‌از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104500" target="_blank">📅 21:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104499">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b1603e46.mp4?token=MVKSedKhOBXDP0kLEEAywe9--k1sjGCBbxUXxuB7fWVIxjHppfpxzmoju-rb9UrY6P9peJDN-mSFWeHn2HWr65ChZA7h05zWSMUfgzS_Ofbfcy0s3l84_MISZwJK9_1s_vuNM_qocJnRGkx_Rw3r_Cgi79ObNFGekrouIU-HJXGJ_DuFywId5Pusk_MOuAhN3KLo6QezstJmRcDoT_sXQb3_v7fxdMH5lndXbTi_3VNjvNKZ88IzlO0WPNOCVSGIC9owA9PstmaC0gHTGUflf_Oymv-C8hJVJqdhEwoytdjUFcuXN6IiC4N8_m9JGdC00aV3IEyZipDuTbzHMc09mHCMQKLpNdzZq1aTjmbW74APjDvFS3zONJEg7Cn4zXKynqf3WDwQXUQ-iDPXQrP_5rKPk6bv_YrV1aaaFeny38FJqUNaJNX_RR7MQdmbfWVyWJNxAsZ9qQ0paZCABvR_vZN5AYdMCEN37BIfnW-9pOuLPq87VkIQt3sbuS0ZLpfL4KMpAS4dcp39IykW5LNYXZ57HaYeYLrV4yeLNtd0voB_gjJNIVB8H3tNmS0o1kzpwTZnIhjiNm4etAoORnT7N595lvA8Ua1N8brMzBZ4UnOm1d4XV8U-6eym9Uz9CmV4Fz5mH9A_xXVf0KjELoZV_muRKJBIV4l1L7jomdigE5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b1603e46.mp4?token=MVKSedKhOBXDP0kLEEAywe9--k1sjGCBbxUXxuB7fWVIxjHppfpxzmoju-rb9UrY6P9peJDN-mSFWeHn2HWr65ChZA7h05zWSMUfgzS_Ofbfcy0s3l84_MISZwJK9_1s_vuNM_qocJnRGkx_Rw3r_Cgi79ObNFGekrouIU-HJXGJ_DuFywId5Pusk_MOuAhN3KLo6QezstJmRcDoT_sXQb3_v7fxdMH5lndXbTi_3VNjvNKZ88IzlO0WPNOCVSGIC9owA9PstmaC0gHTGUflf_Oymv-C8hJVJqdhEwoytdjUFcuXN6IiC4N8_m9JGdC00aV3IEyZipDuTbzHMc09mHCMQKLpNdzZq1aTjmbW74APjDvFS3zONJEg7Cn4zXKynqf3WDwQXUQ-iDPXQrP_5rKPk6bv_YrV1aaaFeny38FJqUNaJNX_RR7MQdmbfWVyWJNxAsZ9qQ0paZCABvR_vZN5AYdMCEN37BIfnW-9pOuLPq87VkIQt3sbuS0ZLpfL4KMpAS4dcp39IykW5LNYXZ57HaYeYLrV4yeLNtd0voB_gjJNIVB8H3tNmS0o1kzpwTZnIhjiNm4etAoORnT7N595lvA8Ua1N8brMzBZ4UnOm1d4XV8U-6eym9Uz9CmV4Fz5mH9A_xXVf0KjELoZV_muRKJBIV4l1L7jomdigE5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
یاسر آسانی پس از پایان بازی امشب، پیراهن خود را به نوجوان استقلالی اهدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104499" target="_blank">📅 21:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prQAIMpqzyXq8HsfG6DynXSicCKWpJdZgTajknci41kOtWq43y4NjjDkkbnTlqCrJP9Tu8oFYbF3jQ5deL1t5dNbfSUMZ3YrpEkuLYf7eQVW-P1APrkT9_VU7lsD5ls9S60sRk_V0iibuB0O5-uQ3py_LI9g4t9U_ZT41JB3bNZtVW9KrvUhhBurwLBYq4glM5H4oQP3FGQC7dTDaoH-8vf9KcBnA0eGjcE59G1mqHhF81jXn4SbbVzarml_W7LymLN9QlDpmLb7EpTLZ-GMtCxzNT9Ojxj4sbzbvMnilhXw9A2iQGdj1Ew-pLBirIwFvLiT4zquEnv65khlkUyfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ سومین برد سهراب و تیمش با چاشنی سومین کلین‌شیت؛ ده دقیقه توفانی برای شکست طلایی‌پوشان کافی بود؛ محرم بازهم در یک بازی بزرگ شکست خورد!
🇮🇷
سپاهان
😏
-
😀
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104497" target="_blank">📅 21:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104496">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwl9CfOPg7rbLx15gvHDUulMWPQ9MyO0qz3cj_7Gl14ut8BMWHI2iB_8Gd-hb9GfetPW7WS_dtOqzVuejbXcLv4faZZw52e9IhoCWtWhglERjLuQBUKlH0cZjbZGYRuqRF4g4nE6gkvbjrNOURprtFkO76LfkynNmtjX5_tthWo16ofAlTTshWbcJpKqL-19zSCB-fx5CeSZ1gOqVZ1mOhtDBwn8HcbLyY5Y1nct9GoB-JWVIcOOXNRtCgxGL829aDqErRW05ir-g-QRei8jIJzD011bEMYcBgjggwud_QLTrguf4QhDqUOfY7xIvWxzBBQqrviixuCjSm51iHNz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ سومین برد سهراب و تیمش با چاشنی سومین کلین‌شیت؛ ده دقیقه توفانی برای شکست طلایی‌پوشان کافی بود؛ محرم بازهم در یک بازی بزرگ شکست خورد!
🇮🇷
سپاهان
😏
-
😀
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104496" target="_blank">📅 21:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRadiS-mVWHIHHFC8_s1EFIe3XoTjggXj6FicG_BRoQ_tDxwq-oYoVwtmqTF2jgvZPql46VQrjiu2eGAPOdZmocKviEJPDVr9uNiQq6srA9IEsBN6vtWM3uBtRIWHz5F3SlSl0ZP8h35edqoTO4T6h2O4OSk77HxAbQhtusI1yTTFJvK5ODLW_Y1P5yKb3S0p0KdNlPmJn1kjRzqetBAoKvEvsOs_FqSkSU3Z8_oRDBPh87iGh9-qKrJyq4n6AE8-achkR7lqNV3ncTw4Fb1rRTmgTiM2TzjMnWNn79EYWoirz-oiRFDdH6_eWV7FF-2RXsyRp7w_E5s12f0ZpOzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل رن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104495" target="_blank">📅 21:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104494">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSYGi8bIOTEvsTGo0ef3mfqeg3708zXSUPPopNQNI3cyhOrWWbnuTKpLsz_T7VPtltEawf-NvCECMgGkqcsKRob5aa6mOSn3gad-lmUCusuK4vxqzLBNNKu2xMFVvxBApmXPNWaOsK7q7n2LmcD2Y4pP1nEF5U-p3nRrYZ5FC6vzEvbPmpbtt6OWFBTgovsjI6xvHhq8_OzOBQHo4oIqSFei7VLtKYVcHM3ZgFJ5-aVOIjA6w7MJDnRWFSwPooajsg7-2Tr_N_hBwPo_4uJdQOqpcC6almE-_RQj1r9QDgY3BMDfjNIcQJMcnU4oJ-ajwtlXcENYdGmU13a8Agi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104494" target="_blank">📅 21:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbRrNK6LqPSIYVvlaPJO5cLgEJ6oqZlAz9p0dFoTipLEh2dNlO8rnRaMu8-BJvF-uqMoAwx49M0tlOPybs4iXOUbdRDo8LGxJkrloW15VIdA95Drr9hs8otFeY7bgpb8GMqAJJ_ZMU1K_AfwGITS0VyKMYY3rgWQF8tMDEMApHnDjC1-wcQzASQOPSfFb934IFMLaUFNMJkS-Y1xe97iqodcNFIoPtHL3d4DNchM3xqDzys9Npr-Jq-52hwNI6JWaid1UnwEJGKtB39F_ZxqhYQJu5jf2LoJRo1NqxxcSQAa114TAXxbEdKA_h1jHyis76adXax_LWAV2jG3TLpEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104493" target="_blank">📅 21:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905068b238.mp4?token=IU-9KWyvD4v7lpFeoSpfDfKM-rRGLIKF9yOWS4gHmIy87iztz7VLg145wnQrhfAJih6XsUey-29KfSsja2tba3sRPiDR_3yXsNM1vN4-ESvI0C4WAhAlHmNL0dRfg7nIRMhiTkZsrLLnAYE9EOpqbYTuMd5Hk2G0BHm31bV_a3px-fWsKfDH8Qeeh7aLmf1V9f12mN01FJOdUgQ5YUgDJNMJeAujblGHK2Enxz89HG8UW_7gUOhowJVwvWZ7egYoz_cn-AmVdlPyExVgev-oUpjMih6pNar1rG7db8eDdOJFxz7Lp2gu3mjstVEE-Rx-oLoVAGLKQycWSIS4VIjMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905068b238.mp4?token=IU-9KWyvD4v7lpFeoSpfDfKM-rRGLIKF9yOWS4gHmIy87iztz7VLg145wnQrhfAJih6XsUey-29KfSsja2tba3sRPiDR_3yXsNM1vN4-ESvI0C4WAhAlHmNL0dRfg7nIRMhiTkZsrLLnAYE9EOpqbYTuMd5Hk2G0BHm31bV_a3px-fWsKfDH8Qeeh7aLmf1V9f12mN01FJOdUgQ5YUgDJNMJeAujblGHK2Enxz89HG8UW_7gUOhowJVwvWZ7egYoz_cn-AmVdlPyExVgev-oUpjMih6pNar1rG7db8eDdOJFxz7Lp2gu3mjstVEE-Rx-oLoVAGLKQycWSIS4VIjMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
وزیر نیرو: این هفته خاموشی‌ها تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104492" target="_blank">📅 21:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
خولیان آلوارز بعد سوت پایان بازی در میان فحاشی و سوت‌های اعتراضی با سرعت راهی رختکن شد و در کنار سایر بازیکنان اتلتیکو باقی نموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104491" target="_blank">📅 21:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64a302233.mp4?token=O5QscGpxU6SMW6KLQOkoBC8E6eJs42qa0mM9CqhjvJQRmhtQ3PE4H06ppCIYhAETpg1kvzAqgniyxxWOlalG0GUffyNpl_1rXgOf7KX7QhtO1uDzXXoLIm57DITasZWafM7W8wPuMYwvau5p0OxHV0CZLv8iojOrKtwiQRlrdqg63l08bjymmq_bdh6SZb6j1ruXUoWUVAMUuxfp25mGR33rUw-_awBbIAvmSSbqYvChC_ZhEyGqKkqK-ZP1JAjkq9FUZFVNCw1eDEUFPlU3yMEbYqljGG9jUbWGwJ-R4Ed890hLa1wVXXMwLlCbO21tRQbwUiSW4chFOObt3pJF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64a302233.mp4?token=O5QscGpxU6SMW6KLQOkoBC8E6eJs42qa0mM9CqhjvJQRmhtQ3PE4H06ppCIYhAETpg1kvzAqgniyxxWOlalG0GUffyNpl_1rXgOf7KX7QhtO1uDzXXoLIm57DITasZWafM7W8wPuMYwvau5p0OxHV0CZLv8iojOrKtwiQRlrdqg63l08bjymmq_bdh6SZb6j1ruXUoWUVAMUuxfp25mGR33rUw-_awBbIAvmSSbqYvChC_ZhEyGqKkqK-ZP1JAjkq9FUZFVNCw1eDEUFPlU3yMEbYqljGG9jUbWGwJ-R4Ed890hLa1wVXXMwLlCbO21tRQbwUiSW4chFOObt3pJF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇹🇷
دبل محمد صلاح در بازی امروز ترابوزان‌اسپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104490" target="_blank">📅 20:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c757fb622.mp4?token=b1Wyu3DneBvr_6KjvuFMbUh_KZ6t6hLbpBrZgaLAKoSztRirLnP31-KcEmtghZftEuaf2Sv1KE3TcwPH-a-WHMrNc3v8fej7zDkR6o7cftWKZaKuN8qGHfijey4n0JSGF6BW110MCe4bXGQrHpBdpYvYzx_sQN-uRehr-WV_b2F3OFnA1eu_2kI-E-8c1Uo93q8bFOwo-oLRtWM6H4nqpKLtYe_MEwe91lEyXHojynWXTE0GOaIGE0WJAvkYqLs_nc6hx0-ZmoHNxQ0yb0pToeLwkjH0YZcVjMoBRk686erjMqt62p1MqstIs-HRhRt3qMdtEwKjm4cZXErBgeoA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c757fb622.mp4?token=b1Wyu3DneBvr_6KjvuFMbUh_KZ6t6hLbpBrZgaLAKoSztRirLnP31-KcEmtghZftEuaf2Sv1KE3TcwPH-a-WHMrNc3v8fej7zDkR6o7cftWKZaKuN8qGHfijey4n0JSGF6BW110MCe4bXGQrHpBdpYvYzx_sQN-uRehr-WV_b2F3OFnA1eu_2kI-E-8c1Uo93q8bFOwo-oLRtWM6H4nqpKLtYe_MEwe91lEyXHojynWXTE0GOaIGE0WJAvkYqLs_nc6hx0-ZmoHNxQ0yb0pToeLwkjH0YZcVjMoBRk686erjMqt62p1MqstIs-HRhRt3qMdtEwKjm4cZXErBgeoA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
اقدام عجیب آلوارز پس از پایان بازی اتلتیکومادرید در میان فحاشی طرفداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104489" target="_blank">📅 20:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L384RgrZL634_vM-DR06smm8NCmUi41ibfDTeKkrXuNHQap42h4P8e4OgHyupFlnGOwCnvbQA8HMVKwmdUhJVmaIPWWO6w00l4ejL-6c71SaCAA75BSphh_iAZkbGPOE0NfJ7VdcKj5P6-QXSwxc9854rioMvUROQEBLHY3qABErNOGM6ozjAaLpd_etioBSCnDbZ19fpJXEPWrl7G-yOz6f7Nt3MmM4M98Iqxtyk_9ks928jJBMawjFkQH07EGTu2tKu65nO0vJUoyctBQxtMLm35siyS-MkTL7YdRN2B9wrvvXgS2y8GbYoHi47pXb_xGXct7sJ8w5bWpe2xGG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جو وحشتناک متروپولیتانو علیه الوارز هنگام ورودش به زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104488" target="_blank">📅 20:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9059eaf0a0.mp4?token=ENIq7-_QmF_a7NuYdW3LVfxhMKc0AyYSXcMX6x8sWpd-bG79Ej_2AoRXF6JANd9Sr4-SSUyk0i-cBpjvK7txFoMiGJyh8q-LWu9QRBibCZYzlWtzFKC7r8ziOdgXF457OYaRBDYPzQr34ITGpXB5y9Ee0ywGkkHLVoXCyQW5Boltb2GLA08SAS3BlUFcJmxnDr3-T3ejCuPg1iIOifa4ts6qXJ0-lWqd0IiPqtmun0CZ2AoJKba2NcEqoIflFwo9ctvERjyjkBawBXxO8aG3T1Svti93q5QLgoAbNLt0oSbHg1M6qk3IvKmJ7c_c-f1pNKqjedI5AlQhDDAexzkekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9059eaf0a0.mp4?token=ENIq7-_QmF_a7NuYdW3LVfxhMKc0AyYSXcMX6x8sWpd-bG79Ej_2AoRXF6JANd9Sr4-SSUyk0i-cBpjvK7txFoMiGJyh8q-LWu9QRBibCZYzlWtzFKC7r8ziOdgXF457OYaRBDYPzQr34ITGpXB5y9Ee0ywGkkHLVoXCyQW5Boltb2GLA08SAS3BlUFcJmxnDr3-T3ejCuPg1iIOifa4ts6qXJ0-lWqd0IiPqtmun0CZ2AoJKba2NcEqoIflFwo9ctvERjyjkBawBXxO8aG3T1Svti93q5QLgoAbNLt0oSbHg1M6qk3IvKmJ7c_c-f1pNKqjedI5AlQhDDAexzkekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
استقلالی‌ها بعد از دریافت دوگل خطاب به حسین حسینی: سید دوست داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104487" target="_blank">📅 20:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660b601000.mp4?token=j9QGEwkLXWkeblTW3ujUhMnNwzL2_5sm-FYiPZ5_A0Ca7TISAe20a5B5CIfnHgjTx9LeI25mSfPm7ENuHf1o98_yIZ0VWADPLVRY8dIOHojYL4DIBjI6AmdGP5lkEE3nEFvPleyiXjE3NvdTAnvz5yImP-NDO__RsIb0uhSLmgG-v1HcwYMKItaE45hvcvXmSwAuTrJ5YqVqksCw8uNumKIXdoJwrDPCp7Le_EFQBbO9J4iDdC4FWakxWPqM64chirwXuNMQXy6kwiKt1b4DAgiFdR0GK0_w62NN7VahRtIEpyFL-ix99rllKu305Jm8AIA3cKpZ3GknosaoQU0j4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660b601000.mp4?token=j9QGEwkLXWkeblTW3ujUhMnNwzL2_5sm-FYiPZ5_A0Ca7TISAe20a5B5CIfnHgjTx9LeI25mSfPm7ENuHf1o98_yIZ0VWADPLVRY8dIOHojYL4DIBjI6AmdGP5lkEE3nEFvPleyiXjE3NvdTAnvz5yImP-NDO__RsIb0uhSLmgG-v1HcwYMKItaE45hvcvXmSwAuTrJ5YqVqksCw8uNumKIXdoJwrDPCp7Le_EFQBbO9J4iDdC4FWakxWPqM64chirwXuNMQXy6kwiKt1b4DAgiFdR0GK0_w62NN7VahRtIEpyFL-ix99rllKu305Jm8AIA3cKpZ3GknosaoQU0j4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
سوپرسیو فوق‌العاده محمد خلیفه در بازی آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104486" target="_blank">📅 20:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd110fb25.mp4?token=Oz754A0Ayg7fX_bAyxBSdew8C9QoyAgwsXP-8BX0wM_HVEGWVR6idtbg34G1zqzPYj_nA2xnUKlXstNsRWMiTXEVdHrV30QqBpNGdUCzHdZo1J1YoIfIloJ67Nenay4m2kV_hizGCAgZYC9GHzmPucJHNa_ZYr3XfPGkuRmTDPZZ4i3TGtXGxoQwIEtAWT3l0zi8eZzj1oAWOYoE9js7FiSOF-K0kokh9h_kNyJLpG1O09JzQsD1TV98GaFuG2R4a5uZ_bhlt_I3L0D7OULnKN94Kv27Osgs4u7BiYDSW-nobnw_BEhmeCeEYEtBG6u8ziVpNUs6-GFYGBEIWrx-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd110fb25.mp4?token=Oz754A0Ayg7fX_bAyxBSdew8C9QoyAgwsXP-8BX0wM_HVEGWVR6idtbg34G1zqzPYj_nA2xnUKlXstNsRWMiTXEVdHrV30QqBpNGdUCzHdZo1J1YoIfIloJ67Nenay4m2kV_hizGCAgZYC9GHzmPucJHNa_ZYr3XfPGkuRmTDPZZ4i3TGtXGxoQwIEtAWT3l0zi8eZzj1oAWOYoE9js7FiSOF-K0kokh9h_kNyJLpG1O09JzQsD1TV98GaFuG2R4a5uZ_bhlt_I3L0D7OULnKN94Kv27Osgs4u7BiYDSW-nobnw_BEhmeCeEYEtBG6u8ziVpNUs6-GFYGBEIWrx-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🔵
شعار استقلالی‌ها: "جدول رو خوب نگاه کنید، قهرمان رو اعلام کنید"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104485" target="_blank">📅 20:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176f995cf4.mp4?token=Qs_KMY2EcF6DYVjhgceIuXWORJ1nvB0g0aRNCOuEP5MnIVTRiijJWVKmiiV_UyK4Dc_f3aRapi6MhJpYX2GYZ-ExLhIL63-9jeK9-XDQAbZSW-5kQjOIuejfxovLUGKWx4sqwFlswEnp_vApUPsqs4rPaZ66SigRs8_qkU_erIGgVg_Pw2HJmbZl_iIZQWg8IiH8H3gchunga7omXkJUL6VdmBWUf73jRwzfKnz4uq-WIshwEIu86NGHLOt59xHcBArFiK_j_UMIeXug3AbjgtQxadQbCtu5MKsL97f0U_Ad2kp8aKOMa5jtaUwNm86p_aHYkgPdb1ohlVRfS-MnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176f995cf4.mp4?token=Qs_KMY2EcF6DYVjhgceIuXWORJ1nvB0g0aRNCOuEP5MnIVTRiijJWVKmiiV_UyK4Dc_f3aRapi6MhJpYX2GYZ-ExLhIL63-9jeK9-XDQAbZSW-5kQjOIuejfxovLUGKWx4sqwFlswEnp_vApUPsqs4rPaZ66SigRs8_qkU_erIGgVg_Pw2HJmbZl_iIZQWg8IiH8H3gchunga7omXkJUL6VdmBWUf73jRwzfKnz4uq-WIshwEIu86NGHLOt59xHcBArFiK_j_UMIeXug3AbjgtQxadQbCtu5MKsL97f0U_Ad2kp8aKOMa5jtaUwNm86p_aHYkgPdb1ohlVRfS-MnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درخواست هواداران استقلال در شهرقدس
💙
جام بدید، قهرمان؛ قهرمانی حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104484" target="_blank">📅 20:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78becda813.mp4?token=R3AQ_6YEOKeLq7yNoFO7qdNPmByxNyBRL8fvWMiHIXg6JBtG8FsukxU23R2AXGG1JEXPgRd4EUEImhyHr0KXlUJlqPb47vaUO3J3xqk3Ku3z-_5CEsDsw6Q1ic45l50_aAsDu8GMAichn2LQzNZlQAgJT_oMHBcM4NqYxQWt5Gmyc-Jaw85rG-Uc6VXYkEs9Cv5Cy6cBc9EODA5-vJrFN-YnVH1q23JAjCb5texSWR7vYkZNLD0FZM4R4uU_kCUD_4hWlzcQdWqxPFMGl9y_9NliL4pnaoe0h5QrOM6TBm0o1zmJdgP05l4tQBNId0dFugZLSZ_bAto8H4bcipZi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78becda813.mp4?token=R3AQ_6YEOKeLq7yNoFO7qdNPmByxNyBRL8fvWMiHIXg6JBtG8FsukxU23R2AXGG1JEXPgRd4EUEImhyHr0KXlUJlqPb47vaUO3J3xqk3Ku3z-_5CEsDsw6Q1ic45l50_aAsDu8GMAichn2LQzNZlQAgJT_oMHBcM4NqYxQWt5Gmyc-Jaw85rG-Uc6VXYkEs9Cv5Cy6cBc9EODA5-vJrFN-YnVH1q23JAjCb5texSWR7vYkZNLD0FZM4R4uU_kCUD_4hWlzcQdWqxPFMGl9y_9NliL4pnaoe0h5QrOM6TBm0o1zmJdgP05l4tQBNId0dFugZLSZ_bAto8H4bcipZi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جو وحشتناک متروپولیتانو علیه الوارز هنگام ورودش به زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104483" target="_blank">📅 20:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEzCStUTiTCZaYc1qFgvgT-zhrKshrWTjF0UzI4L1Pi94Q63rO0gYCkwArxoJjTtHeBHqYOo078gsEZhPyc4ZqryLnFA-NWCb-AFLD4ooCWRYh7kWxZDV5PwFMAEhAQySiN_uqGn2vMOV8mWiL4ONR62BZrJILSrh_JrPod-_FfFP7o63GW2juwyDjM4HMiU8HzwMSeJyfHPWxfkeAYXmy6abIaQhSiFiQn1dnbvhmgauupHt1hdY10cHj1kbbVbzpdfYGJf-N7r-CYnYut_lWEUiYJTSeJAdG_zLoZ7uwhXOCLdRF4u1dbMi8ZEYF1O_xjr7qOpQnHvKDQgj3duTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
هواداران اتلتیکو فریاد می‌زدند: به او بگویید برود، برای همیشه برود،
کسخار
بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104482" target="_blank">📅 20:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d7870a8f.mp4?token=AiCcYRgE477zmetdvtBHI4RTMRbZIJBF7Vsdf097q9Oe_z3oT_dtjvz66IyYutJCPdmr_lO90MnuA8zvtbbZcwQk4hbVYesomHQv8o3b7iOYVrIHN-JOWpJQPJAPguzce0rWusyjcz8_ZEofU5IEWae5FgeumXdefnwcdiypU9sBigvBQ_eyELNJps9bPjWVqGbtuWCrRk7gD9UK3nZzzTWFyLVnl5o0yeCj8i2OliLK2svh2bD7O7JEs3sjtngLMFopIZVyiQR3Sl9iLVhJlWing_34gHKwyPfZi9tGqphX7ISXRPFIt1L8C-JLrHnkUKy-JNkySTdtgIfWUmGHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d7870a8f.mp4?token=AiCcYRgE477zmetdvtBHI4RTMRbZIJBF7Vsdf097q9Oe_z3oT_dtjvz66IyYutJCPdmr_lO90MnuA8zvtbbZcwQk4hbVYesomHQv8o3b7iOYVrIHN-JOWpJQPJAPguzce0rWusyjcz8_ZEofU5IEWae5FgeumXdefnwcdiypU9sBigvBQ_eyELNJps9bPjWVqGbtuWCrRk7gD9UK3nZzzTWFyLVnl5o0yeCj8i2OliLK2svh2bD7O7JEs3sjtngLMFopIZVyiQR3Sl9iLVhJlWing_34gHKwyPfZi9tGqphX7ISXRPFIt1L8C-JLrHnkUKy-JNkySTdtgIfWUmGHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
گلزنی محمدصلاح در بازی ترابوزان‌اسپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104481" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a48f53f5c.mp4?token=mcBKEyI_IcOqTCKLDrTDEClErIYxy8yRHYLDzoZ4iFMgyCc9PeXd8UnN3nmu-hasLfxnSCFusMdTLfJ8GsTfAvQnZxnOB_WwfgENoULKXiYpH1ofAkQoVruRrM_ehnbKmpxQBGW4rYF9nw7tt-hytlxtEObDuSFJ_LPM13kuh6Y0321_-G5vvzYoRA13pYes__mwlhNqFFIBLb-rsBRAsXDcnEsAdalp90pQ42_P5Zwje7dO8Bs91hCvqvHEyhWs4P9yIvyxriH7l0ENmoZeqUBgDrfMcI6mwJS_D_fZ_lEqZ-58W-32NPTWaCOYOLlIo3rm378egQnPBKHgbqsqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a48f53f5c.mp4?token=mcBKEyI_IcOqTCKLDrTDEClErIYxy8yRHYLDzoZ4iFMgyCc9PeXd8UnN3nmu-hasLfxnSCFusMdTLfJ8GsTfAvQnZxnOB_WwfgENoULKXiYpH1ofAkQoVruRrM_ehnbKmpxQBGW4rYF9nw7tt-hytlxtEObDuSFJ_LPM13kuh6Y0321_-G5vvzYoRA13pYes__mwlhNqFFIBLb-rsBRAsXDcnEsAdalp90pQ42_P5Zwje7dO8Bs91hCvqvHEyhWs4P9yIvyxriH7l0ENmoZeqUBgDrfMcI6mwJS_D_fZ_lEqZ-58W-32NPTWaCOYOLlIo3rm378egQnPBKHgbqsqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
سوپرسیو فوق‌العاده محمد خلیفه در بازی آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104480" target="_blank">📅 20:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8Hjt3nMsL7p8_ORyvSiHozxc3gH7iLyEC4wRNNgfcmSK9yKkRXe7trfLitc_0aG8yUHrJn70x_pE9sC5kme3XX5geyDtU1QSbcQt2Ht4zSzhbOP-DL9IIuxJ8dWWHe2PuG8Z59_un88-g6qV19g2V4BbCklehiMgkl4NsnR4ZjxM5boaWQygW9diFL83GYiFhfoRuIR7VHNLzH9p3h5FI1uoRI5Bzb8ebIoI3vEGBESjNFATn1jVm84ljtJ0_5SBxVGbVS6zDoXqIxal_Qde5_Q9He_ANEvoyPi59SvZNldreRkWXxaAWJhidCskHCVhFmpFYrCHGtDH6tVz_IY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
هواداران اتلتیکو فریاد می‌زدند: به او بگویید برود، برای همیشه برود،
کسخار
بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104479" target="_blank">📅 19:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j59Y1lrbayx3icCi-Fs9iupKTbbsFJSodBsZdlR2hf0Mq7fZby7x0y6dc62UQlpA5sn7H3z6jao4MriEj2smEjmzRoIOY1p_ST7-avHg8wP9JKxC2moum7dtyCeLhZdmtfdKyP66v_EgIGjkKPSwg0hZXUNTWvYjn4WO9-gV9dgXVBx1BmZ_jBH-DU5Kqp5vvxgyo8v4rRJAiPUaLRWqNcED2hryoWoy8GJ0smNuA-jeT859eOXYVW_1k8fTSpi6y0oN3KVz0a_Ug5uRyrXTYZjjgFgR3a6tSjauzykTsWCzA2Neiw7Hx6DMw2U86PIjC6MyiDAEcd1_GjMc9CKjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم استقلال به سپاهان توسط قلی زاده(10)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104478" target="_blank">📅 19:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb3d0d855.mp4?token=jeyax6f_k6XrygaGWNh6RgKSUG-xGZzSgZiaZ_lo37fTkN3Oy-H1EtuVolzL0P_h9w2zcYAvAwj-7VNfy9oUJrTYRLtY17cgD9SCsqTsP0_30k9hq5vMS4D9DJCnpUymov6zRWVanP0rZ4BS0YeAxieb3YcyYORbK1wV3yZsCGac_nFx2QXN6z8dZZuVorSnm8DB2FSEUuFFCxFVzLfJHJw9ksJA9f-1R7jlxQ1CZ0QFud5cboGYmoXdWrf6KFiysWoAybfYwpxqEF6BO2_X8xVrr0kkn1oiztKAbkwbsi-26zktVCvyesDzrQ-o7pnrw6Keh_nWjQQ8Tewnw0er2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb3d0d855.mp4?token=jeyax6f_k6XrygaGWNh6RgKSUG-xGZzSgZiaZ_lo37fTkN3Oy-H1EtuVolzL0P_h9w2zcYAvAwj-7VNfy9oUJrTYRLtY17cgD9SCsqTsP0_30k9hq5vMS4D9DJCnpUymov6zRWVanP0rZ4BS0YeAxieb3YcyYORbK1wV3yZsCGac_nFx2QXN6z8dZZuVorSnm8DB2FSEUuFFCxFVzLfJHJw9ksJA9f-1R7jlxQ1CZ0QFud5cboGYmoXdWrf6KFiysWoAybfYwpxqEF6BO2_X8xVrr0kkn1oiztKAbkwbsi-26zktVCvyesDzrQ-o7pnrw6Keh_nWjQQ8Tewnw0er2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم استقلال به سپاهان توسط قلی زاده(10)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104477" target="_blank">📅 19:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسماعیل قلی‌زاده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104476" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104475">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">استقلال دومیووووو زدددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104475" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگگلگل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104474" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f589e085ba.mp4?token=pln-Jh7fvP6dsyjD8NXWwIzNfgU62h2pg3MJvLayV7JUR7A2rVg8LnySzX70jebieawN29iSXsy1SrOoEgk3dD7PF1GMtvUZu-YxivU1LXYxLSP9PeZQjZdGU87ZNl94PKzM1v-2Qs6p1SiRXzXOOmw16QBMvJ8E5UnmeFrD3aMmtIzEvpvMKagE-Q7eeO3L1hk0FuFsk6Bn3lmLfr2n9F2hSdwhoOhJjfxoUMnWqdCbW5aKmQtYLUH0mWijyKBl2B4yO1XRFRHfuONaGBF70uv4f-DiK1l31X7Zhy77Uc0LBm3w8SdISIHOuChEIzXOH0poBEjfphucGEbemJzg7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f589e085ba.mp4?token=pln-Jh7fvP6dsyjD8NXWwIzNfgU62h2pg3MJvLayV7JUR7A2rVg8LnySzX70jebieawN29iSXsy1SrOoEgk3dD7PF1GMtvUZu-YxivU1LXYxLSP9PeZQjZdGU87ZNl94PKzM1v-2Qs6p1SiRXzXOOmw16QBMvJ8E5UnmeFrD3aMmtIzEvpvMKagE-Q7eeO3L1hk0FuFsk6Bn3lmLfr2n9F2hSdwhoOhJjfxoUMnWqdCbW5aKmQtYLUH0mWijyKBl2B4yO1XRFRHfuONaGBF70uv4f-DiK1l31X7Zhy77Uc0LBm3w8SdISIHOuChEIzXOH0poBEjfphucGEbemJzg7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
سوپررررر گل یاسر‌آسانی مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104473" target="_blank">📅 19:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یاسر آسانی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104472" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">استقلال زد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104471" target="_blank">📅 19:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگگلگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104470" target="_blank">📅 19:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCXF-hFnvFQKveRODY2pKWTFlqDnWEPrKx-tOKKEjH65VxNmBDoqpQBsTlt-JAnEKlYP4w1lSvLhAX8AbP4TSY8Y2e4k96gb7sGxQ5Vt_4etbyi1GGN9G9YNhP0-gIoUUkSYkQVQ-zbS2xgc6J-yMNGR2qP2186SoOiid1v7lT-YxxGdOtNGUmIvTO4_JHo-peO0XwcLCtdSV_tMpLCNnrRTtSTaq1qvZy9NdzDCR3h-hN4i_g8MdjlR2ZGvbhoNqegGRi7snI51Rt--Kr0t4VPk8dklkEuJW1GKdf30__ktZKYcNuwLkL-jsc_VJCPC5Fj1Wjhz5635cBqSEGb0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هو شدن شدید آلوارز در بازی امشب اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104469" target="_blank">📅 19:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=PxTF403O4LTWgzv0BvHCpG-NZQ7WG2zjM-ZY4h5Rf4wwlAgQAnu-nwcOtQjxucA8h1yZ0cM-jDsgfGm5jOcbWKtqv5W1tImYjdtRZetT4H9k6gmAOJSVA3JSKOcBMKMNGDo5DC69LidpZYkwRnJpfTfhzDvqTS9l4duTX6-_mzopLvrNWrKuQ8608t8lRFugSoQisTjgv6V2pHPyt5aM08ROj_rSxf-cvwMl9_5FRH6s4Bj_t1IfPSeLFgobvrXexjyLAxfK5biwvEzLQziivXYafiAyRRHXLoG8bMS5XXBqwoNjVKP0eDurPbM7W_6Ocwoi49-BIWJCy5XIfGOyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=PxTF403O4LTWgzv0BvHCpG-NZQ7WG2zjM-ZY4h5Rf4wwlAgQAnu-nwcOtQjxucA8h1yZ0cM-jDsgfGm5jOcbWKtqv5W1tImYjdtRZetT4H9k6gmAOJSVA3JSKOcBMKMNGDo5DC69LidpZYkwRnJpfTfhzDvqTS9l4duTX6-_mzopLvrNWrKuQ8608t8lRFugSoQisTjgv6V2pHPyt5aM08ROj_rSxf-cvwMl9_5FRH6s4Bj_t1IfPSeLFgobvrXexjyLAxfK5biwvEzLQziivXYafiAyRRHXLoG8bMS5XXBqwoNjVKP0eDurPbM7W_6Ocwoi49-BIWJCy5XIfGOyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
شعار هواداران استقلال در ورزشگاه: سپاهان دوست داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104468" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
صحبت‌های هوادار استقلالی که برای تماشای بازی تیم محبوبش، خودش را از آلمان به ایران رسانده: ما مثل بعضی تیم‌ها کاپ پلاستیکی نگرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104467" target="_blank">📅 19:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141a2ee698.mp4?token=hEuIgqs8o78mluXAj1kLN8A27n491g9bYTmAyFSIrrByDpQE10Bzc0MyJZihkqQB7eSuCGShGRXyNhEaUEBa_YPQdXP0tANpL6TQs9vk3vFc-woPDDwWXIhqrt9dctrML47BEWaKU27Q3O5ziUNfiiprCMi5zST9tV-EBx9FBh6Yp_g-1BihUuUPeONEIyFmv9A5EVg-MFIGWvTUxS_b5M9I36rxZgLEpNEF99BzFoSX8mLURqOc7GHEGu2P56tZ3TfSdIAnhGy5eQjvF85E_6J0DB1zrx7UrMbz7KXWD0RJVSeWF37HYvkgTMtM3up8irJgc2M3z8cVi-FuqOOKww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141a2ee698.mp4?token=hEuIgqs8o78mluXAj1kLN8A27n491g9bYTmAyFSIrrByDpQE10Bzc0MyJZihkqQB7eSuCGShGRXyNhEaUEBa_YPQdXP0tANpL6TQs9vk3vFc-woPDDwWXIhqrt9dctrML47BEWaKU27Q3O5ziUNfiiprCMi5zST9tV-EBx9FBh6Yp_g-1BihUuUPeONEIyFmv9A5EVg-MFIGWvTUxS_b5M9I36rxZgLEpNEF99BzFoSX8mLURqOc7GHEGu2P56tZ3TfSdIAnhGy5eQjvF85E_6J0DB1zrx7UrMbz7KXWD0RJVSeWF37HYvkgTMtM3up8irJgc2M3z8cVi-FuqOOKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول نیوکاسل به لیورپول توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104466" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d702269fdb.mp4?token=pT91E6KNQA2NifnDpyS5uAZ495H0Mk5rgKTV9LVMULRNbsn-GnsRsK67n5qnKthVGHTzECL5mILTktscDo6Qs__2nRr6QvMDjbxM6JlDSGKJNSEzxThW-RuQI7EmT_ZuOyRqFs9cYPNDoNBMsN7u7lqclZzac60hERPpbehWGS_xKANKBtBnokmHknLzOUShdaCnBRTPj2Q8vw0QMxK0Xxz-rrEmjKGdS8kEsazQ7HETAjy8yIX1DnRscH50It4_Di_uFmll93FeVJ1y_LEDGBjy5EhilifYrQA6WVrMgIYqivCxvhHBmMvCVExcfFRoAcR-CMPiCpF94beqz_q63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d702269fdb.mp4?token=pT91E6KNQA2NifnDpyS5uAZ495H0Mk5rgKTV9LVMULRNbsn-GnsRsK67n5qnKthVGHTzECL5mILTktscDo6Qs__2nRr6QvMDjbxM6JlDSGKJNSEzxThW-RuQI7EmT_ZuOyRqFs9cYPNDoNBMsN7u7lqclZzac60hERPpbehWGS_xKANKBtBnokmHknLzOUShdaCnBRTPj2Q8vw0QMxK0Xxz-rrEmjKGdS8kEsazQ7HETAjy8yIX1DnRscH50It4_Di_uFmll93FeVJ1y_LEDGBjy5EhilifYrQA6WVrMgIYqivCxvhHBmMvCVExcfFRoAcR-CMPiCpF94beqz_q63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
هو شدن شدید آلوارز در بازی امشب اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104465" target="_blank">📅 19:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr0jgVVOmkUeeljHuiJN9fXUmNpxVuGYsBO9MvGV0E0zkTXalNgTDCEtVvoAcnj88VI3qJiisNOlqJfm_qT3I72vonja8eOkqg-zxDcIp9316payKGkz3PomTv9F96q1vq1qvAHd7LWC7moEL6AYjP69yzGOWHgWQPq9TckOc6Dp5u0mA3kh_EgvT1_IP0Tbxh4pi9NafbbVQMZUfUxf8pvFrdKKINaz3Y5jhc_LZ8gmDxkWwmmhddLRPqsMuxytO41gnIoRF33wIayVTAARGoHNEWZksn5o_n3w6sErGtmY8Jvvf3Mdk7Amh67hlyRC-GPpH6A0-mCDt3DdGv4Zgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104464" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104463">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF2ORrMbu6AoLDu7xUCytupC8cTQeOQZ06ltDCSxz4CSaq-KI2cTPgcf8sro279VpchxxvN6kqwkyRlV6kUVxDaao7ZG6r_qdFjsoB3Z1cqCAORRE1-r2-nEQPxHhYcyLor9vltd469bEzsG6maWlksXA-8fU12w8b6gJMbhB79dAVnus5_ts3odb4r_a3Gli7HRtY7rXNISyzHatDhul7b_Ovfgd_b_26Nc6lfl4B5mgNqZ4SaNm4crK6_uYAASBUpfrniUrgklq82QWJn6E-7zU5SFfZtN5UOt1IJyschVO4x2UZyOET6F4HLsQDgwh2paglP_FQBSgM83DPytjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیییب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104463" target="_blank">📅 18:31 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
