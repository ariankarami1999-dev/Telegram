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
<img src="https://cdn4.telesco.pe/file/YkBAmxpM1qMvavHojMnzuxqEjN_7pE690vnV_H_QW8qGWMps_-_QYuTsV-6d8QVbOAkJMAE6ce5mKVlaxaEyokhSNiiD4kJ9-_COQVmWISry7w0CB1ElwxQvUWtFWN9N_n5nyXx6svPTL8p-dxCnmveoRea48AdOaaHn5u9EhU-e7MMEOt2CoA7DnavPLPoKy7-2fU9EOKRD0TA4zofJ1YB5ChTJnT72jzWEzrByXPTHzPMVxW7aq9RD0fdhneJNo5hiiuwtsh_WN_LUzazI69lSKDef2dQBru2safT95mwX93cMaWsWyz-NBuMi0ybTDIdBSYaaHQgMoJ0hU9kckg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 04:45:16</div>
<hr>

<div class="tg-post" id="msg-461198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ded3bb5c.mp4?token=Bt-shynPI9H2cB4xY1v2qX5LC_Lvnugd4K6o6L7JpYEA6Er83CaT-Uu0NU0oQMx2zBiTYEQlyIMXVcEeFQ7dkG7zGeExCrx_RAds0ddyjQeHYr8BsFGGFwCbvsVzZDeOv2s33zxGeEacdk64hqknYgce1ckfsw3wZJZ3CPfRMsdsxCCK00LQ0jeYhC_t2O-SX-1K-eU5VcLrKSsbJJG8XdYVio5lmlUVTKi3rKOwyI9a3PgRXEaKbjQdlWtLysIWlmVEXdxxulugNM8bASMo1_M-3NbZcQjh9XOtwy41mrzRAfxr3dQSz9ztJIbfQ6QdNcDqjLg0f_kdPV1GKVYd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ded3bb5c.mp4?token=Bt-shynPI9H2cB4xY1v2qX5LC_Lvnugd4K6o6L7JpYEA6Er83CaT-Uu0NU0oQMx2zBiTYEQlyIMXVcEeFQ7dkG7zGeExCrx_RAds0ddyjQeHYr8BsFGGFwCbvsVzZDeOv2s33zxGeEacdk64hqknYgce1ckfsw3wZJZ3CPfRMsdsxCCK00LQ0jeYhC_t2O-SX-1K-eU5VcLrKSsbJJG8XdYVio5lmlUVTKi3rKOwyI9a3PgRXEaKbjQdlWtLysIWlmVEXdxxulugNM8bASMo1_M-3NbZcQjh9XOtwy41mrzRAfxr3dQSz9ztJIbfQ6QdNcDqjLg0f_kdPV1GKVYd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌ها از تسلط نیروهای یمنی بر شهر «الخوخه»
🔹
گزارش‌های اولیه حاکی از ورود نیروهای مقاومت یمن به شهر ساحلی «الخوخه» در استان «الحدیده» است.
🔹
از سوی دیگر خبر می‌رسد که نیروهای یمنی بعد از به دست گرفتن کنترل پایگاه «خالد»، به کوهستان «النار» رسیده و با مزدوران…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/461198" target="_blank">📅 03:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش‌ها از تسلط نیروهای یمنی بر شهر «الخوخه»
🔹
گزارش‌های اولیه حاکی از ورود نیروهای مقاومت یمن به شهر ساحلی «الخوخه» در استان «الحدیده» است.
🔹
از سوی دیگر خبر می‌رسد که نیروهای یمنی بعد از به دست گرفتن کنترل پایگاه «خالد»، به کوهستان «النار» رسیده و با مزدوران سعودی درگیر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/461197" target="_blank">📅 03:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
خسارت سیل به ۷۷۲ واحد مسکونی در مازندران
🔹
مدیریت بحران مازندران: در برخی نقاط مازندران بیش‌از ۲۲۰ میلی‌متر بارندگی ثبت شده است.
🔹
تاکنون ۷۷۲ واحد مسکونی درپی بارش‌های سیل‌آسا خسارت دیده‌اند که بیشترین آسیب در ساری گزارش شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/461196" target="_blank">📅 01:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برخی منابع عربی مدعی شدند،
چندین انفجار پایگاه هوایی ملک‌فهد در عربستان سعودی را لرزاند
.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/461195" target="_blank">📅 01:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJhjvaX2Ijd2wf6BxvM90v3jhqVhjBG8gt4YGwRDdXFDG_8qnw5BrckocxzXzhVNuupnNtO0Z2U7z7uzgtWJ7Iz3bqBafnCqcQgbOQEgvoih0_8CG557rlZFtTBchq2-pRXS_mvPY_dQKt4h0NgK-WSFs_KA-JZXH9YmyzfYwSuI-c0YZyF4cmqMkiH20woO9wa0SweC7OIPkXPyUEh9TrEj7xTLeWFeViSj_fIZLky3ip-iVRkVghoDK5Xu45epJSUEa4Nxc4-JKLXxYpiWXKx46KEUNRL1CGHkChywBBZ22oHHJ_8bUJRnP8d8IwSmKBoOpm-mDobSouRuDqJVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1P9Kg_GMhvkMrqyyW1wALR6WLnmL8sCFz23gSp0kR2UBVoI93y7IIC25LwiFqmUNexCcgHFnaslVsbfowaYJcO5DIoZGRb_EAe8AZ3jKFBe7JicD9yAiHectaj83evyErJejq0w7-GuFU-O_UQ__7a-baZCH5qvr6EqcxSxzBHuPUpxg1g8Xmpj5rG5JTqjfUscvh-l-4htbUxdr3jk2wa5-dQ1pHXxjFJ_WCNrcg11tsZLzseVcLCYeuQ2gwss8tQUH-3AYT8HD3Lc7tvzF2P3C331YNHgGmCsiRFAGwt9OBnIcTBBI6K0kB9tEtabRsH0eaf-uFS5XSK0rnjCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIwqMKqbaUJ5M0kyvibNvsIzVA7tjNfBz124tMG0Xs8sOUATHcEDdaBB72sK1k0W7UUNjkYaUeZh-DEXiygEd8Y6Dt3cZXQBDH46J-uhDaUYc_SWZ2vvg9PqrnviVFhb7dMUiQ4tiCOqp8O3hkSuUMLyjUFU_dum86q4b_ZjrXtVtB83xWWNcAEYf0b_PpqNIyxl97v2gY1_CEK0x4wftoE8TM1pzQhtnUHzkCbOj-mXQGnLP8jokZgMueIErNsxul1QShl_Pw2Rt_vcd6T3rBe4Muvs5jxgkh85ZbK3K3CY6odzmsqz_MgmICelY2mf_cUlPMp_A2N13CANRC0ZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q847adB6iJOMgI6ncSFH01qf9DYsSjgGLQXdklXm4uTDeI4B65nFbXUq4Jvy5ReJCOs3t2vKTFNHyuUbId29u2IQwbkvb8VMf58AWZ_rpoQ_jPgtwdnifM7VB_myHobiV4-0rLs6PFGZ4EkpUkieTQXiWHwIG167OVnKkJV2QaP3yug3S49UdSyTcne2nAFoqYV3dr-xYhhea5qH00-N_YQTuWJHXOzq77PuTBfxHFV8OVpWzCRqX0ACVNBmCk6x0WqGX5b1CVXhuscTckAtRVkkVk76zCIaH-JeCkJtAimB3ZFQb2ljayICPppWpC4lwkRMGtlZIist-A0Gx0BMWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۹ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/461191" target="_blank">📅 01:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNtayaibfOfwLqxwyLPF1mD7nozHF3nyGsY_D6wS_p5PgBx-qedIx6AWEcGTQGZEoDYvnrFHZ9DuNTB4Ca48NnAy9UHOXKsBcm34zAvDOm5JiMY6r6kqe57EpS4DCAViIACJkM8wMD2Erjf9E5DEeWf0kGQVZXE-lXox4uAK8Mhfz0zPu5wZ9uFOfnYx0gTqwDHWp28GeVuTlh8R_i5Fd53whg8Dm-3tHFKVa2hto9xy8iqEiSooIxibYI3YWjF8n8JrZfkvUnSaGIEZS-df9sV_DUJEpwD0p5tfZ6FYKmvsoFvat7q14NqwscRwg7ro5_RfRVePkiRhfiWBB6zQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pd_-sH3Q3RYavOOueMpZlc6WU4cYkV6A9yFCiVDQX05neOb9I45I5TCN3QXuyHEq22Qw3x4sNZR-U-qIpw2SAxpm0viIFAdfDGfb7-pbdPH1aaHY5PHS3vapqAioVtBrG9nX7giA9sxFlBtEWBzWXbi5PACynebHzB_JEelVz6YAfuBfG_3zgGOkvG6qV4NrczggnInx2xUHJkYAPOOG-K0ZWePbEP-3FdhtYegamr8A3tpu_8AA5Npzc5jLPSWmiNr-MklcgjxlW_kYSDtNglCDlSAVkWWAh8A_qP7hTO2huVOoAf9oG9SIooSyW5JcSbP0k_pXEp9cGluIxJZKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnBvdMs0rgjZuaMA10FBlhiXS0WG8TZIvfZ3TsYE4t_oSwnciibBcPLi4il5vySPqueigCDJ10KCIzSejYKicNUsr392tVazuLrOdlhus15ybJq_fLk3PmBM4saShUyMR1sGVSfweTwfckAg02fox8LxuDvYyiO3CnsU5_px71u6ACCMLwiP5-9AkPg95X1YPkEMS3MQq-5QeBRLGIG3NY7B0fiHeOalhq5hwla8i7aGeiZIDVCtSY7KbrxrL9j6lIrtpnn6-g9YGnb0os-A9C4GZqRJrNaXGCtE6GvKQnNm6SAJkqRaKRYyNKBTL42IzXPfasiIHQVW9K8iTK_VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkQrZPGNYFAaiv225HUPhSYc2Sck73Z243PCNpSuEbi2EOFwEeDYFDRGOQ6xEusmErkLc6-2alAlAqaZuS1J2f_VgpRf0LMRg0_0ZpjmVDbmj9m7yNQ6GLVPfVHwjLF6ZIOh_jkeYTZ69JnzVypwkxi-yJivbCye7TGxx0YM9o3QXgPbWRA5ob8z8ROqm6p2exZLyqPAQdD1sJ3JMjW_FnDnBpc8pUC5K58wO2fhlhArV3f4t-w73cpugk-R-0Zp9i7KPAF7tH9s6_si0AIfmemq0IhARACP7VozlwsNuvNldoBqGEQJQN9WWrFjeDr3_kgcsvw2YAjwK9EA5WTgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3wzzZ0YGLCEDf-stuohJJn_2vtL-yH4TOC0XTKy32-NeqJmm8JLm3cwlpGeb9fQyyUTmKt73RYes2JTw7X-YhfFkwogr5q3VzijOvLGOK_6WDilbNyu8-B0bd4VXR79I1pPIy29lFxZqVMjq1HDmYje2cDYJFNLWJbltxs2a-i8UXIQAVhdAPHzFSo7sQgq1Bdb-8X4Fr23beL0ht-mZjnzyVMtO-9vSpE6YGQqgMeUS3j5IPSnujNRF98mPA1OlwtRul4HBDdmr398AwEahljNauuGSHpDd95BpXGLkh7PaJ8XG6IkOamceY6FYekl47hKJJgWCr9KEZEH0xFBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jD7bC69SYaSKTPJ39PYqj38NEnTOQqWTttbX1adfi76iqxwDMrJHZj1qk9fLbcS5f1dM6t-vBpKww18Q9rHS94LP0z49b6kG2ac5BYH97as6sNuoMQPyrWHyrX7Qcvqn7gJwLASEo_saTFFwFO6LYbLf9hGcV-jESUe1KGxep4zm1mG3wQu9rASymeAQyXd_IAcHSZD5PAzzVe2KJFtjV6h32jihL41jJimYehr1uYmLACnQVOiJi6fatUXWJog9xGutsnqKY7VEHuZK_aRn_BnRI9hqYb-_q-oWppmiFHw8w5qZy5cvxnSEh2cbL_jA8UIDX4f5WT_QZA52KPh6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SF0UYIpozHL6jTgh21TuLFy1-luR5WJLynYTRkcGZZoWAdrxhSudaUifxFSDwkZuHfgWoIz1Un6CmVQCE9inEPAfvFJObJagS1qpmre_KDusq8VUwQJrFH8oxl3hG90BJFnSYKGx5MHctdM60ZlgSVdvGQzYGtg1tCspkxv9sYenaMDUfOQaoT0ZA74bKj0A0hYDq7pNFBhwcJFwRoKPUAWyIgOORYuWElt9yobBU8qYxNyRRKTQwIY5NpFyCMq8SZGeN57eTmCPAIyh4ZPGRUtgCtZcWCkBrZuW-nZQN__mHv_FIMgw9-lPMGgouXnnFZYrJ7nVTKSb-Z3BPSoOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB2lJdHSiU6k6nrzhfTHnu_2_MHbQjXTW4FMORdt__TYdONINkfmnPXEeXYc9SIZDSTX58zYNJoYIzwJNtTa02gtuNWttHFS6BQ-PniDjgP4akaGMagTPyBaV0ByofektVFRPN-JDxS8Rl3NwKwgVcQDD4dVaMvnyF6CiuZYrPMsM7EDT7dp12RrFu4Mtpsmf_3F0iVya6XODmoVh5x7nz1PIgnO4jJtnymovsSGzNOrRv0ApBWloEjDYmberQk4QBQyIVmczjHnAqOnWs0aL-5BMrKlMN4p7EIe5dc6ZEkzunz3xsWwnBjIL8CBBjId_ZS5aJpP2s0wAMfERuk2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-MouBFJuedEaDBagE0taiwq6RBDCCPiqFpsw9F4_xQQOp_b8F-SOmLdQPgtsxRhnIKh-N_xKj-B2PpKAKTZJImb8KBIPY3HcLaAkDL0aE77GpAjc9oLTwixzvQvrtXPHq4IMDniSBIWxG_WbQN5dMXI2NIE7qlT6rxRE22pG3LKmC3doGgieTrvLa5XEoI9fkzxXLKMMb5mB76KgiaV4eMgk3xnP3syIiDC2MRLeaMCSXo_E3LHn5yd1pWb8G5RpOeUFKDIDfZZmz_El06Os4vhTrJ7BRq8kKPaE8OkB_OORMCwL88km0t3nqo-UJJiTXmH4iRRHvfS86vgMJg0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4kjrhx2DnQYZ_7ETQdSiRrhxidAbo2WbjlewyDlKbUjPuHSEh4_-ZzSGDmUk91Fuli7NhKltW2BiEkqIa8ERzHUxkNRLXFf2mBzAGLzPgMERQr5ABsjrxG0U_QqcXbDCpEwJaNxzm5cUMUY2Dqs6YwrJ5jINZJmVDLobC4bmi0DVWFSpB47BODo7-wP1olNP87tzHMpJjrahROqhfdTgKIXbknpqydZhDlUUSmxiXHRMOWMUPuDTMiGmWOVrNTDp5HhRr83BMV3p4e2xdkwsSEpFO4ajN4mqPvnLjreLMOGHBHKsXNcK7bTwitbOYEhiqEKAssvjRk-RXs5VhJ1VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/461181" target="_blank">📅 01:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLBlHK6nd2G5U7uLUZcOLe1EWKjSH4bhWDmn9-I5LrjcTip6PtoFic6oW_24ogF4GJzcXqZXtghlJB1SZL2EaIR2mppQ8yX1xEdaERvbMYhzdQaD0QCuIzQycP_dNonomnQGKbngFxCkk_Cjn-l2Km6LX_hTx62qAGJALFr-z97Ro5_o9Lu8nhdWo4vAzcMfhosVQmDmRgHzRXtM2zl46pofjH9CpWX9LE5BvBMYJ22aisCuNjkE22SYM5NvOkJcrVqrkNlXx0NLKnAFLtHLV19Lz9M-ryiosmkD1MMqWxkN-MI7fLbwRPsW54n5HKaY5zqzT2M6eRoScK1BkHMAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: دروغ‌های وزیر خارجۀ آمریکا در رابطه با مداخلۀ ایران در موضوع یمن-عربستان، نمی‌تواند جای واقعیت‌ها را بگیرد
🔹
سخنگوی وزارت خارجه در واکنش به ادعای بی‌اساس وزیر خارجۀ آمریکا مبنی‌بر مداخلۀ ایران در موضوع یمن، نوشت: دروغ‌های مارکو روبیو نمی‌تواند جایگزین واقعیت شود. انصارالله بازیگری مستقل است که خود تصمیم می‌گیرد؛ نه از کسی دستور می‌پذیرد و نه نیابتی دیگران است.
🔹
ریشۀ بی‌ثباتی در منطقه را باید در مداخلات نظامی آمریکا و سیاست‌های سیطره‌طلبانۀ آن جست. اگر واشنگتن واقعاً خواهان صلح بود، تنها یک گام ساده برمی‌داشت: به بدسگالی‌ها و مداخلات بی‌ثبات‌کننده خود در منطقه ما پایان می‌داد.
🔹
صلح در یمن با بمب و فشار خارجی حاصل نمی‌شود. صلح با مذاکرات صادقانه بر اساس نقشه راه مورد توافق طرفین آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/461180" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زلزلۀ ۴.۲ ریشتری ششتمد خراسان رضوی را لرزاند
🔸
ساعت ۲۳:۴۷ دقیقۀ چهارشنبه، زلزله‌ای به بزرگی ۴.۲ ریشتر ششتمد در حوالی سبزوار را لرزاند.
🔹
قبل از این هم زلزله‌ای به بزرگی ۳ ریشتر، این نقطه را لرزانده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/461179" target="_blank">📅 01:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzq6pT-_3Fc4HNlKOs7SercoCKV4_zDPkdLmLfIT3Qo5tknTI4Qqu5tpp18ODcMGMQBFxcDUX0vv-4BHDjgA-3Xep44szSn1Ch-CvcCNBiQGO7prbN_Z6RlW0dRM-koWupQkdahsYPHTIepVVbEkxRguoTngFKe_XxW5BaVvehHpN6Bn4Ktn_rzEPBkHPINUHta4BqlHhZpLz53juP9M-8NkEi8GsQYYv6kP5VpSfkFkPMN57FHs-SD6_Jl1Q53jkpif6LUqSQzo6Bt3fxXLzTcuah1Zehz7YKOfx1bRNYhuUK9i4TuFlJEx14eWd6WVbNLB_N9_3TL6vhaZHTVAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار در شمال فلسطین اشغالی
🔹
رسانه‌های صهیونیستی از فعال‌شدن آژیرهای خطر در پی حملۀ پهپادی به شهرک‌های شمال فلسطین اشغالی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461178" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">احتمال لغو چند دیدار از هفتۀ هفتم لیگ برتر
🔹
برخی باشگاه‌ها از جمله پرسپولیس و سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند.
🔸
از این‌رو، ممکن است دیدارهای باشگاه‌هایی که درخواست تعویق بازی‌هایشان به‌دلیل حضور ملی‌پوشان زیاد در تیم امید را داشته باشند، لغو شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/461177" target="_blank">📅 00:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در قشم و سیریک
🔹
دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
🔹
استانداری هرمزگان اعلام کرد طبق گزارش‌ها، صداهای شنیده شده در میناب، سیریک و قشم از سمت دریا بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461176" target="_blank">📅 00:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opv6gcEKS17aN-vnTwmWGs_YcHMyWbQxI7KlabTFW8BGU1q4iox3Il7FH0eG0k_5IVVY2p8eYau4UR2Yd0fTVySpuPZ1l9DIMNr9ZiQpn8xU53gTKoRPcCJmcP1_VxfgWhb8EyppRQTxI4pusXocTlZ6jPEO52zbej8dkVUpsErYyPvNSh91ojT78r5fdCfKNbkV-xp22BCUyeVWhhOdD76_LO2PpTlH8X8ORnb17-d9tbdZi8nmVI-aGHjnb36w764hqSlzbPgCwPjKymgo1fF4dYz-AEhvPKLNb0nJ5L--sb9jKYXWdYKSW-GWRPueYqKlbcXV58eGPo5LrlmbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پناهیان: فقط یک نفر در دنیا گفته جنگ ۲۰ سال طول می‌کشد
🔹
حجت‌الاسلام پناهیان: اغلب کارشناسان دنیا می‌گویند جنگ آمریکا با ایران طولانی نخواهد شد، اما تنها یک آدم در دنیا گفته که جنگ ۲۰ سال طول می‌کشد.
🔹
این حرف که می‌گوید از مردم بپرسید راضی هستند جنگ ۲۰…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461175" target="_blank">📅 00:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQGxCYJT5lWatvvjsDmOmKMe4C_E2HDrIDCWHDy-MoObUXRsVZ4kJ24c6bUQemRoIy2MuaE56CIHZ3vDDQ5i4Ugq5edp2b3g2qpDqLGa1JnWClU3O0d3YCoeD71XtBpt6NMNcl-W3HHtOYMz1Pga6dOoUQznRTpcCrHXXZ7WQs_rW2x4GDE3R36OvIrC7cKUUFKwwWs7gBI9KrAiox5TXMEr2Xo8LEykpH9k4usG_D3qsj8-Dfi-EM4tehwTnIu-EVTAynHu5_siGPh8bjPlUAb-WBA3k1WSM2ebLU5oxFqmR_rca5k-VbuhLbUqHmLJUTFvDeeyMJi42la3fZsfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی تغییر را می‌شود در عددها دید
🔹
بعضی خبرها قرار نیست فقط یک اتفاق را روایت کنند؛ پشت هر عدد، تغییری در زندگی مردم جریان دارد. از کوتاه‌شدن زمان توقف کامیون‌ها در مرز و تقویت شبکه برق گرفته تا ساخت مسکن، ایجاد شغل، گسترش خدمات درمانی و حمایت از تحصیل دانش‌آموزان. در کنار اینها، پیشرفت در سلول‌درمانی و بازگشت یک بازار صادراتی هم نشان می‌دهد مسیر توسعه فقط از یک حوزه عبور نمی‌کند.
🔹
در این «بسته خبری امید امروز»، سراغ خبرهایی رفته‌ایم که نتیجه آنها را می‌توان در زیرساخت، اقتصاد، علم، فرهنگ و زندگی روزمره مردم دید؛ اتفاق‌هایی که شاید هرکدام یک خبر باشند، اما کنار هم تصویری از حرکت در بخش‌های مختلف کشور می‌سازند.
کشف و انهدام شبکه فساد ۷۰ میلیارد تومانی در خرید گندم
🔸
با رصد و اقدامات اطلاعاتی پاسداران گمنام امام زمان(عج)، یک شبکه فساد ۷۰ میلیارد تومانی در فرآیند خرید گندم شناسایی و منهدم شد.
تقویت شبکه برق سلماس با ۲۲۲ کیلومتر شبکه جدید
🔸
تاب‌آوری شبکه برق سلماس با توسعه ۲۲۲ کیلومتر شبکه و احداث ۶ پست جدید افزایش یافت؛ اقدامی برای تقویت پایداری برق و پاسخ‌گویی بهتر به نیاز منطقه.
۲۲۳۳ واحد مسکن روستایی در گیلان به بهره‌برداری رسید
🔸
بنیاد مسکن گیلان ۲۲۳۳ واحد مسکن روستایی را به بهره‌برداری رساند؛ طرحی که به بهبود کیفیت سکونت و توسعه زیرساخت مسکن در روستاهای استان کمک می‌کند.
ظرفیت درمان قلب در خوزستان افزایش یافت
🔸
با افتتاح بخش ۱۶ تخت‌خوابی CCU و نوسازی تجهیزات بیمارستان سینای کارون، ظرفیت ارائه خدمات تخصصی قلب در خوزستان افزایش پیدا کرد.
صدور آنی کارت سوخت در ۲۴۰ مرکز تا پایان شهریور
🔸
برای کاهش زمان انتظار شهروندان، ۲۴۰ مرکز تا پایان شهریور به سامانه صدور آنی کارت سوخت مجهز می‌شوند.
۸ روز از زمان توقف کامیون‌ها در مرز بازرگان کم شد
🔸
زمان ایستایی کامیون‌ها در مرز بازرگان ۸ روز کاهش یافته است؛ اتفاقی که می‌تواند روند جابه‌جایی کالا و تجارت مرزی را روان‌تر کند.
ایجاد بیش از ۶ هزار شغل در شهرکرد
🔸
طی دولت چهاردهم، بیش از ۶ هزار فرصت شغلی در شهرکرد ایجاد شده است؛ ظرفیتی که به رونق تولید و تقویت فعالیت اقتصادی در شهرستان کمک می‌کند.
۱.۵ همت اعتبار برای تسهیلات اشتغال جوانان
🔸
سامانه تسهیلات اشتغال‌زایی جوانان با تخصیص ۱.۵ همت اعتبار از سوی وزارت ورزش و جوانان رونمایی شد؛ اقدامی برای تسهیل دسترسی جوانان به حمایت‌های اشتغال‌زایی.
حمایت از ۳۳۴ هزار نوزاد با «کارت امید مادران»
🔸
بیش از ۳۳۴ هزار نوزاد متولد سال ۱۴۰۵ با شارژ و فعال‌سازی «کارت امید مادران» مشمول حمایت‌های این طرح شدند.
ایران در جمع پنج کشور برتر تنظیم‌گری سلول‌درمانی قرار گرفت
🔸
ایران به جمع پنج کشور برتر جهان در حوزه تنظیم‌گری سلول‌درمانی رسید. همچنین با تولید داخلی، هزینه درمان‌های مبتنی بر سلول‌های بنیادی تا ۹۰ درصد کاهش یافته است؛ دستاوردی که می‌تواند دسترسی به این درمان‌های پیشرفته را افزایش دهد.
۵۰ هزار بسته آموزشی برای دانش‌آموزان کم‌برخوردار اصفهان
🔸
کمیته امداد استان اصفهان با توزیع ۵۰ هزار بسته آموزشی، حمایت از تحصیل دانش‌آموزان کم‌برخوردار را گسترش داد.
۱۶۰۰ نفر از خانواده‌های ایتام خراسان رضوی راهی عتبات می‌شوند
🔸
با مشارکت خیران و مراکز نیکوکاری، اعزام ۱۶۰۰ نفر از خانواده‌های ایتام خراسان رضوی به عتبات آغاز شد.
ظرفیت میزبانی زائران حرم حضرت معصومه(س) افزایش یافت
🔸
شبستان ۸ هزار مترمربعی حضرت زینب(س) در حرم حضرت معصومه(س) افتتاح شد تا ظرفیت میزبانی از زائران افزایش پیدا کند.
سهمیه عمره دانشجویی به ۱۰ هزار نفر رسید
🔸
در گام تازه نهاد نمایندگی مقام معظم رهبری برای تسهیل عمره دانشجویی، سهمیه این سفر به ۱۰ هزار نفر افزایش یافت و وام سفر نیز در مسیر دوبرابرشدن قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/461174" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df592991.mp4?token=ReQCryMM8z8XH6d74-Bv9cBTS5e9G2uI-wK-1z8KOrCM8cXwPzkNpKAp5aRJJf6yT8cq_7Mvbn7zuNYx7n6VMu-BMxCFWONdMhWbais1eIPlPI9NgwU32hE153zIQaSmRvtL1LcSUl89VCqbrNO-WjQdVsYTztafoysW9fmXrlAA-IN51bFWKC09GnQS8xhEgF8e3dJ6mC33nLdHiU47-ElVW--Z2NdulRxp_BtEYEmaGXJpuOXBvvgf_mDSIjsWspa04xSQoLA5Hx1P4VpQ7Xus5Hfzvtg-cH5LsivvZxAue7p9HSZvysKxIacyVqdaLpuKJsPe2KeD_2mF4R5jnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df592991.mp4?token=ReQCryMM8z8XH6d74-Bv9cBTS5e9G2uI-wK-1z8KOrCM8cXwPzkNpKAp5aRJJf6yT8cq_7Mvbn7zuNYx7n6VMu-BMxCFWONdMhWbais1eIPlPI9NgwU32hE153zIQaSmRvtL1LcSUl89VCqbrNO-WjQdVsYTztafoysW9fmXrlAA-IN51bFWKC09GnQS8xhEgF8e3dJ6mC33nLdHiU47-ElVW--Z2NdulRxp_BtEYEmaGXJpuOXBvvgf_mDSIjsWspa04xSQoLA5Hx1P4VpQ7Xus5Hfzvtg-cH5LsivvZxAue7p9HSZvysKxIacyVqdaLpuKJsPe2KeD_2mF4R5jnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۹۳ میدان‌داری مردم فلکه صادقیه تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461173" target="_blank">📅 23:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs_FE2xrFhmgegUvXTincHjWr2F54HoCaXqOPiJhal9Au5Te2gpgaCno3tjgnur5tflFEeMA0uzI5S3vZtrTBF07BJYtGlSmaHguOwVka3q5vnzM4BeGCiyQkMv42-bsIcwOjYvZ1IFSiYxtolf-k6BJ24_6nEpigPZVQ1NZF93V3YgAhz_MQpIBIRfMeuhlUCgCx4wb4gGslpulRr-qlyDDkDVI4rnaamc0kduFy56rtTWuzSztSfewh6Jab5ceTaF3OxBFHhzkkbBD2gsXFRwuWIjTKURDJlFXJCtBcBSGCxivGwNpZZJew5_ZPyo3skMe6dI24sE87dEDEF10-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وزارت خارجه: ادعاهای اتحادیۀ عرب علیه ایران مردود است
🔹
جزایر سه‌گانه بخش جدایی‌ناپذیر قلمروی ایران است و تکرار ادعاهای بی‌اساس تغییری در واقعیت ایجاد نخواهد کرد.
🔹
ادعاها دربارۀ مداخلۀ ایران در یمن هم مردود است؛ ایران همواره بر ضرورت حفظ وحدت و تمامیت سرزمینی یمن تاکید کرده.
🔹
امنیت خلیج‌فارس و تنگۀ هرمز باید بدون مداخلۀ قدرت‌های خارجی  انجام شود و ایران دراین‌باره تدابیر دفاعی را برای صیانت از منافع خود اتخاذ کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461172" target="_blank">📅 23:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac07f4e91.mp4?token=ucpozVOv-_S7iXqyOpaQ8AZXOp4v7i6DOLopqY_fzT5lvPxMBXRqN4F44cKg0ewl9yfOtHf1Z9Mq0f9rb8Y-Sy6u1rBcCaYtWvnPoQmM5X0BBZSEsH-mIMkbAKEd00tREX24zCUsHzngmDKthNzjn29Jy2LSjW2vWKDt_iDDxHplLraORvsf2WcC0npVUVSVTt4jpJqQEc5mqydI-a6lxg6jzv0c17wrBzKrz9Ngp96wPNnnjljlXep3xabZCc37M34bd5yq4J8nZcb7txSVSeBDdqPON2GJYA07zeSHr5poFY3lIirAZ7QR7zhg-hD5ljBuDZSLE7cTx9hMJWLwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac07f4e91.mp4?token=ucpozVOv-_S7iXqyOpaQ8AZXOp4v7i6DOLopqY_fzT5lvPxMBXRqN4F44cKg0ewl9yfOtHf1Z9Mq0f9rb8Y-Sy6u1rBcCaYtWvnPoQmM5X0BBZSEsH-mIMkbAKEd00tREX24zCUsHzngmDKthNzjn29Jy2LSjW2vWKDt_iDDxHplLraORvsf2WcC0npVUVSVTt4jpJqQEc5mqydI-a6lxg6jzv0c17wrBzKrz9Ngp96wPNnnjljlXep3xabZCc37M34bd5yq4J8nZcb7txSVSeBDdqPON2GJYA07zeSHr5poFY3lIirAZ7QR7zhg-hD5ljBuDZSLE7cTx9hMJWLwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار مزدوران سعودی از دو جبهه حیس و الخوخه در نزدیکی باب المندب پس از پیشروی‌های انصارالله
🔹
بر اساس گزارش‌ها، نیروهای انصارالله تنها حدود ۳۰ کیلومتر با بندر المخا فاصله دارند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/461170" target="_blank">📅 23:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNcRijN17fR7ZkNpqJw0HNjUJq143ohGWgVYoFPrqBKVnGjzchq6ZMagUqerptk8vq2_pchZ3aIIlt_v_XnwESz74W6ikB5JKqIgLR3erCWJ88nSS9NRM8K0Ia43nqglKqtWv9KWej_JEj6or8J-zTx5vN_ch2BSiiphMWHwaZ8B1SGITeSmSjN-XbuhYByd3L02brw2zX87ZX0QyxThqzl-8eF9xQpLcfePQAkbVnu8rJY1tqt0c_e8lkksL4IXIhDTn2o9i5fJUcv9kjK5wu9ciEX96VXE-lKaVub4BYZkQR8V2mf3m_XdEjdg5VTLx7Xjsj_8t98mPgIKm56hcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر نروژ: به هواپیمای زلنسکی حملۀ پهپادی شد
🔹
هواپیمای زلنسکی هنگام برخاستن از مولداوی به ‌سمت نروژ، هدف حملۀ پهپادی قرار گرفت و تا آستانۀ برخورد با یک پهپاد پیش رفت.
🔹
مقامات اوکراینی هنوز دراین‌باره اظهارنظر نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461169" target="_blank">📅 23:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGC8BC1Hvb1pQft6GQ_8dJAlnAMmYbeZCQaqEZQNv4wfI5gOm3bQd3f7Ze33Thtmi4zkNg6oSbk6MzJtzQkf2idvDIpd1E2vNfZa7hYXgLYXmf2YtgodMecx05UvXwFYRvL6tOvIoI5pMDdb2vjAmMxCnZSOCrbPXjZdzGp4W0tSk6fijTcwiHGyD5S8xF04QoX4w7VIRGmfAPD91-DUI6l15Xel_sNCJZWltkuyqlSUuI0QEDMEMbBYcjvihMjQnIYQAojkCi2kSjNFelqnUZUT4SW9gd4B79FvyzKgnlwivepmSUgqoiLMJubU2UfBJSqDOeaNMIrX4BV0ABzw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت «ساواکی دوست‌داشتنی» و «آمریکای قهرمان» چگونه ساخته شد؟
🔹
یک آتش‌نشان زیر بمباران آمریکا در جنگ رمضان، برای دختر ۱۲ ساله‌اش فیلمی وصیت‌گونه می‌گیرد تا چیزی را به او ثابت کند که پیش‌تر نتوانسته بود؛ چهره واقعی آمریکا که دخترش تصویری فانتزی از آن در ذهن داشت.
🔹
او بعدها در مصاحبه‌ای توضیح می‌دهد که دخترش حرف‌های او درباره شرارت آمریکا را باور نمی‌کرد؛ چون رسانه‌ها تصویر دیگری از آمریکا به او داده بودند.
🔹
این یعنی بخشی از جنگ امروز، در ذهن نسلی اتفاق می‌افتد که هر روز با انبوهی از روایت‌های رسانه‌ای روبه‌روست و حالا نبرد اصلی بر سر ذهن نسل آینده است.
🔗
ابزار رسانه‌ها و راه مقابلۀ ما در این جنگ شناختی چیست؟
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461168" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGwNqnj44R0NVQSs2EJIgcltRGXqJyf_ga0shpqT7MDgL7k8kAtS_6EQ5OR-BDGWOYKd9M082TMHwbkHwZhCK2LeUWN8ndDW3XGQcyxF0CLEzBo30yFIwxMgiiOhpMzTet1DyVqcEbH3h7DFPvdZH7wi7XJAQt3l6yOgrN0YLyoMWn3NgjAWrPr7uC5eEgPeujxv8Cxcdb6ZOeGqexyxycVNx25IszY1s2Au9XcavdNyE8ymY83M5L27bPscYU9qXfomdCyjwhS5MQI3htE3LU5HEyFLB08B9OuGQXfsRGr6WzSdBBFRBfWGghrxmT1VxUQs6fjlk1IKNEBiiUv-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب: بهترین سال‌های جوانیم با محبت و ارادت به جلال آل قلم گذشته است
🔹
جریان روشنفکری ایران که حدوداً صد سال عمر دارد با برخورداری از فضل آل‌احمد توانست خود را از خطای کج‌فهمی، عصیان، جلافت و کوته‌بینی برهاند و توبه کند: هم از بدفهمی‌ها و تشخیص‌های غلطش و هم از بددلی‌ها و بدرفتاری‌هایش.
🔹
یک نهضت انقلابی از «فهمیدن» و «شناختن» شروع می‌شود. روشنفکر درست آن کسی است که در جامعه‌ی جاهلی، آگاهی‌های لازم را به مردم می‌دهد و آنان را به راهی‌نو می‌کشاند. و اگر حرکتی در جامعه آغاز شده است؛ با طرح آن آگاهی‌ها، بدان عمق می‌بخشد.
🔹
در روزگاری که من او را شناختم به هیچ‌وجه ضد مذهب نبود، بماند که گرایش هم به مذهب داشت. بلکه از اسلام و بعضی از نمودارهای برجسته‌ی آن به‌عنوان سنت‌های عمیق و اصیل جامعه‌اش، دفاع هم می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461167" target="_blank">📅 23:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461166">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5emOncCSrPocWClLDyWA66SvhY_seO3NL9ceIkeKhkFg6JKbZ4N_-4qD0d7L6EzeEm800IiM2dwwfOglo_pmPQtZaFqU_tet1FzXE1AxIFlFacuZDaJA9oIgr5DzPMyMGIvLclKClRlMUahw2neXTQ5yza73WEVMc_RfVYe1-GvOBzxRnJR08MkXveyEGOUUNgvvN1f2WnpMcu6kkA7lmh4l1wzEEeumtUUgSuQI6CaEZuwUhoCBNvcbdhV4UxCIm8MmmeIQu43DPuVsptSwEyzuhXEVn0evzhP03SRukyeuR9Z3w_1QenMStatF7qE2dymY4MxOOliCbRpuYlo-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: تهدیدکنندگان زیرساخت و تمدن ما صلاحیت داوری ندارند
🔹
تصویب قطعنامه شورای حکام علیه برنامه صلح‌آمیز هسته‌ای ایران به پیشنهاد صاحبان بمب اتم، عاملان هیروشیما و ناقضان برجام، نماد استانداردهای دوگانه جهان امروزاست.
🔹
تهدیدکنندگان زیرساخت و تمدن ما صلاحیت داوری ندارند. ملت ایران بر حقوق قانونی و راهبرد انرژی صلح‌آمیز هسته‌ای ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461166" target="_blank">📅 23:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJt3ZGW7AUhXB6esC6K4lLfSM4cviPUdTyVYePoY14-7x69yqgP0Wft22DEXuXJM8YHrJU8a4fwTTYGCTIxGUmvUpalXMV1zmu1lWjQmE7kRyw2QlXXYey8TaCzp-Ufe6LDk2d2x8SiAHywjw5VXk9PvWnsO-zCajbcer1cNP0U2rblt-DUH3_coMz87KrysJ6DAmk9ZNmPeP00SBbdgs3P5Y1eGp4qRbd-1uNxrMid4pmUO1CIN4F7SFYP1_VHPuxB0hMBlZa-LIEWBtA32nIkPIMe75ZgOpVpSMch2emdmyGezTzdPvKu9uval88SLXeCYTNtsMsnqU0P_vg-K8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq9n3LzvYwMzhj1iLdqw-Ti9BfuKMCY_TCUjkQb5m4qfJcRMaVIXMTbVgXv5lFQgQ4H2ABvcSYdmrxiZ1Uz0HqjEB5X6x-O08NuxlXne_d6QJiDHleBniklC56kpp8hVYAmOUHlbGQov7Cii7XIcT88A_5zOYaIItl5mmtGIWcba66Jurb91tRqUZ8Fnr5YlWUMuvzdqe7lX3yA8C7Rl_56LeW-whS-hQKjvTdaizyf1QAYUin2pjbWsHP6suWsJi-nxVaVB4NS_Lrlu1djiRqNteyzi_qFj6xsAY4lhnyW7eOSJjPNtod-CB8-IrRQwsvnbqrn0ex0wIeH-hvchqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2JzCQKKG01vLEJftHERta6znSWNZI_5fVjttRFBEXW552d8IzT4vFaYoYUDs-LUgIYbjwht3xkUBco0XOiNtRBnSONLUn47lMWi6P8P9EZ87T2nZp48BJOhbBFDlA3DksFenztoe71ErGS95zvFNt8IYLvopby0uYaQC1_oyBv0Y5LRL2eYAuMCb3UEh6WiBXi6Mlona2efBLs4nZWCFkl-ffw0MH1reTR0QMkZ5gMGhOHFFs0tR3Ay7o9xHJA3Fxu2aLFE3TRGYwLiev8ffEOSMe_KZMoTawIRh4-M6E0kgQSLoF2RyAvgT_9vIGdp-bjtiZ_UPxGqA5x93lwmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF9YC6IqgEBSZhAURJSKJ6hZotLg8ydW3VC7AT1BvAISGfPk6YBOO90HpN6-Dh46A2_n_I9mNQbuWR82osHJoS3eMdhLfTglTgPHliFAOy2nrhJlbhgWgcbuXgiWxt_eLoxDQmH4q_SyKvf9j5M_ByChLNc7d9JM31mteMTKPji4l7xCW5Fo2yIHi2C3cNRApGuzkmrlILP35dSr9JL4gJJDBY4Rx3MEwRGWvckAJPfqzIaE8IeyTH0Ch6yVH8qHVkxwMwkpfwJJYEWYYj-Kq_AITcDZRnSTj1bk0fj5haV_7ZMcBFsSv2_qPpndw8Nm57GP97axY5av5lgBpn1ucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOk0Thj1Rl1CS0n6WYQOWv09qIOlSWCTI8SMwhe43ZF8-HOksxD0ywqyJESD5cpSpSj_UupQG7G9MbyhErNishTXIu7bkva7qZd_sGv6d8_D0CvcYt88m1K8PfzPoWuvvVsLug02_LmPN0Svk6C2lQpO6tdXttV7C_RwL2lbA8P4MQxi1Lg8NbJU8_Y0zbI_2XWTBhs2-O1e0hQMrblTJv3jShcNsGBMDKU8FcsRg0dteRFs2ZDxrPaZKSsr2UxCapDX9VFeemWYcA-LQEVJqogO1bmDlyhYBRoNE4Vksvhnfl_7fUW8LWec6CO8exSq-RRk33dRxwkaJv87M3bi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9hdgMRtu82YxZah19fBhLq_Gx_36I6jrG-nlawMfGkxiY4QvOmcnQuDE-UjEPquLgmyOFJ6GTWJRLhaChtWunqymSDgsR6QbGakINFHGFN6tmUtOGKhZo4Q8G5Sv-zw5c0Hx7wzF-twNgwpYuGnvYVAxBmqik3mU-EFqFyw01xgx7u1f2JWkYXzO6GJ9C7fmIbybC1im2lwKpyphayqxWCEx1EgF6I-us5ZwUKJ5p1h07Ag71HUR1ygv8UVH7unYtR5gYtB6CBxoRxbbkvG_I1Awxl_7TLUImysJILE8o2DIDQXGTqnMrv9Jb9e3WgRZSHD0W_rMs8-spoArUkmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7TRG8BOJIpbsioDdSWlDKqSfssQYbdou0izTd0USKIRt_nP1Q1Y_fxhERQ3t27njDuFr0IfApsE3dXCnyviXKieMrOY7N47WPKtQjTFymEucClsue82bIeROGUF53cSj9On1KsNCZOOqNQ4QOCNdqUk1eZnJwDQbAKAPIaBXxJlpXTF1qSCd6dxLkBsBeN968KF4eSdt6QEZxmMNDOlv5vLWc1pYoce_zm89dbkEl5d5A69OLgy0EG-Kr-AYdFaVWlU1DeJFbeD-hA2HK8vBDdxg8eHz4ejP5h41Iet79zT4NJkaO0l5Ad7HlGEVTeW00Ua1HQ2hjhUitt-zY4vgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازگشت شکارچیان آسمان به تالاب
🔹
۱۳ پرندۀ شکاری شامل ۲ عقاب، یک سارگپه و ۱۰ دلیجه پس از درمان توسط کارشناسان محیط‌زیست، در محدودۀ تالاب بهشت معصومه قم در دامان طبیعت رهاسازی شدند.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461159" target="_blank">📅 22:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ad2398b8.mp4?token=b_URKZJVLRmOyHoJ9HzYdk-i_DQQo76t7n3ONIozjg_DZg3eaCOTtf4UdqUO4wu7ad1QmbgdtP2TGQ55SmBBB3Q_PfiNhaI99wDt4Usz16O-IjubXmQfYwH7QJpdziPA_npBqViwLWAph06UDeKK2R0xZ09heSDTWjgI_YCviPcVxOLRD4VowGhuf7J3hX82QJMdvYBIN9sXRb4XyW-mvAIHR4JvqttMXljCMKTn3m2_6rI32x8ufgD5ulTcczEK16mdLfgMqOiSohovyQ2VQNHmmobd5Dpsam4qwhSvqbWHsdtZL311vl8ADOBf9NSw1aLFUrJ0cytZtUR6tocfhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ad2398b8.mp4?token=b_URKZJVLRmOyHoJ9HzYdk-i_DQQo76t7n3ONIozjg_DZg3eaCOTtf4UdqUO4wu7ad1QmbgdtP2TGQ55SmBBB3Q_PfiNhaI99wDt4Usz16O-IjubXmQfYwH7QJpdziPA_npBqViwLWAph06UDeKK2R0xZ09heSDTWjgI_YCviPcVxOLRD4VowGhuf7J3hX82QJMdvYBIN9sXRb4XyW-mvAIHR4JvqttMXljCMKTn3m2_6rI32x8ufgD5ulTcczEK16mdLfgMqOiSohovyQ2VQNHmmobd5Dpsam4qwhSvqbWHsdtZL311vl8ADOBf9NSw1aLFUrJ0cytZtUR6tocfhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌ها: طبق نظرسنجی‌ها حداکثر قیمتی که مردم برای بنزین با آن موافق بودند ۱۰ هزار و ۱۰۰ تومان بود
🔹
۷۰ درصد مردم با نرخ سوم ۸۷ هزار تومانی برای بنزین در کرمان مخالف بودند. @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461158" target="_blank">📅 22:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ed4989b4.mp4?token=kqhHpCxr-SYwsbhSH3Iy2dVdn50m9BUqOI6C9dnJVn2tkwj5z01wWM3dbnxmObG6JLKrgls_doxyjbtI9_R3w_HOKBDTZBe00umL9uTsWQRwGcya3U8dPpewdzv6GvWXHZCaALwtrV88bMKx2SDpHRikBkG09gqItPOjwHRnb4GAKsfgX3pCt6FQ6CjG5oo-euiEUHEmfhCf4htk0zHqsxZ1QFAbg1841E1GxiLRmN1vcVdii-Uyp3mD67I0P3veAmIBpRZxDCSpN1l7X2ODrwiABXVDuCK3QwZ447asW1fU-CSn_GlIe4j2qarawjj_G3OYLjKfAbeqBIckZsxJAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ed4989b4.mp4?token=kqhHpCxr-SYwsbhSH3Iy2dVdn50m9BUqOI6C9dnJVn2tkwj5z01wWM3dbnxmObG6JLKrgls_doxyjbtI9_R3w_HOKBDTZBe00umL9uTsWQRwGcya3U8dPpewdzv6GvWXHZCaALwtrV88bMKx2SDpHRikBkG09gqItPOjwHRnb4GAKsfgX3pCt6FQ6CjG5oo-euiEUHEmfhCf4htk0zHqsxZ1QFAbg1841E1GxiLRmN1vcVdii-Uyp3mD67I0P3veAmIBpRZxDCSpN1l7X2ODrwiABXVDuCK3QwZ447asW1fU-CSn_GlIe4j2qarawjj_G3OYLjKfAbeqBIckZsxJAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: قیمت‌ بالای بنزین در آمریکا، هزینه‌ای است که برای جلوگیری از دستیابی ایران به سلاح هسته‌ای پرداخته می‌شود
🔹
قیمت بنزین پس از انتخابات میان‌دوره‌ای به زیر ۲ دلار برای هر گالن خواهد رسید. @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/461157" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad6b1db62.mp4?token=gRdvdwAJCCgj5_zDq8-lr5Mt0fDkpQBZp3Xj4tSPDLCj5gtYwWZHqiuNUgSNzo64pHScEM0trAgT4NRN0B-fNo8hCJAznLZSD_hfhXHzIaoqtS9lXJPFe2PX9FMEPV7o4Wob3P4daKIqYnRINB4vo6c5RfXqo34TyjZ-KJ_mSiGu2MTOmYW3ZVRT_qatZf8V5zKR-e8T-T0c3NlGOucTEkuueTJbWargBNIfwZxoOQ3-AJFCazC0udK403Joc3pkTEBz-Cn6xWd0CbtbBpnB7-z2aCl3dhbr2sxBK6beiCMEZFemjK1vYANKtNtmFMKHMWxw7fdCdi4s-QJX8yxfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad6b1db62.mp4?token=gRdvdwAJCCgj5_zDq8-lr5Mt0fDkpQBZp3Xj4tSPDLCj5gtYwWZHqiuNUgSNzo64pHScEM0trAgT4NRN0B-fNo8hCJAznLZSD_hfhXHzIaoqtS9lXJPFe2PX9FMEPV7o4Wob3P4daKIqYnRINB4vo6c5RfXqo34TyjZ-KJ_mSiGu2MTOmYW3ZVRT_qatZf8V5zKR-e8T-T0c3NlGOucTEkuueTJbWargBNIfwZxoOQ3-AJFCazC0udK403Joc3pkTEBz-Cn6xWd0CbtbBpnB7-z2aCl3dhbr2sxBK6beiCMEZFemjK1vYANKtNtmFMKHMWxw7fdCdi4s-QJX8yxfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: [ایرانی‌ها] تمام تلاششان را می‌کنند تا روی نتیجه انتخابات ما اثر بگذارند، به این امید که یک گروه ضعیف روی کار بیاید تا کاری به کار آن‌ها نداشته باشد و بگذارد به سلاح هسته‌ای برسند.  @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/461156" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cd5330b8.mp4?token=jBrIYrSFxtXTuEGUwUU0xY_Q418jJcF1PVALpTjTjPJsuo0l_YHJ5I-tm-dIJBPYZlCR4Vlt8Y5Pp-GlPto0N4vufGmJA0dgKEUnsswXKyifUMuwIClQA6KFa2u7CDSM1f6CFwqN7lV-7BdN-CGwEJMWjRhcrw2dTSabQZMRdDSnL1dYuRCyOgAozvmgeZYIfNKXOcgFLhoL7XMZa4Lcf9ULzcJk-ntnAa2ifB2LyCnwQHJRW55zo8afRq5k2sHhXskukhJq0I-X-FoZqWXouteGmmcN5L0MVlf2VLd5RvFGh__qyuTKvFvlgwQIpa_suqGyDObTnBxiRqnY_ata5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cd5330b8.mp4?token=jBrIYrSFxtXTuEGUwUU0xY_Q418jJcF1PVALpTjTjPJsuo0l_YHJ5I-tm-dIJBPYZlCR4Vlt8Y5Pp-GlPto0N4vufGmJA0dgKEUnsswXKyifUMuwIClQA6KFa2u7CDSM1f6CFwqN7lV-7BdN-CGwEJMWjRhcrw2dTSabQZMRdDSnL1dYuRCyOgAozvmgeZYIfNKXOcgFLhoL7XMZa4Lcf9ULzcJk-ntnAa2ifB2LyCnwQHJRW55zo8afRq5k2sHhXskukhJq0I-X-FoZqWXouteGmmcN5L0MVlf2VLd5RvFGh__qyuTKvFvlgwQIpa_suqGyDObTnBxiRqnY_ata5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌ها: باید کشورهای منطقه را به‌گونه‌ای به خود وابسته کنیم که فاصله‌گرفتن از ایران هزینه داشته باشد
🔹
دستگاه دیپلماسی باید بیشتر از مذاکره با آمریکا، بر مذاکره با کشورهای منطقه دربارۀ نظم نوین منطقه تمرکز کند. @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/461155" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257aa999a8.mp4?token=ELBTAB0iyi_YjkPsJioI1Wp2E5USFvGZ_HuWZwra8tsMlWxKp91umIAh29RIV1s8P6y_Z2K3_GlgDX3utFPXSXPIcWXLkDSXeUwv1B89y_4pSu9YFA8JZNs2GeZXUw-e1G1zLxkT7-xw0CvxyA_Yv4MuDSHIg1bU_famDGXKJn6M6m2HK8wvDiPRz8KPQ9oy_IcL1YK0WdBWzT55krrqde4L0G3IS4WeYMNNu09R1X_j4rkykRJpQQvHdjp5BtkX06nqsAj38VZ60yEJwvmwkvfQ4Zu_c0Z9kezvOlrRacFHAqx1yMRnQuPeAkLSPud8pGnbWwDfPcXjD2K6n7DkTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257aa999a8.mp4?token=ELBTAB0iyi_YjkPsJioI1Wp2E5USFvGZ_HuWZwra8tsMlWxKp91umIAh29RIV1s8P6y_Z2K3_GlgDX3utFPXSXPIcWXLkDSXeUwv1B89y_4pSu9YFA8JZNs2GeZXUw-e1G1zLxkT7-xw0CvxyA_Yv4MuDSHIg1bU_famDGXKJn6M6m2HK8wvDiPRz8KPQ9oy_IcL1YK0WdBWzT55krrqde4L0G3IS4WeYMNNu09R1X_j4rkykRJpQQvHdjp5BtkX06nqsAj38VZ60yEJwvmwkvfQ4Zu_c0Z9kezvOlrRacFHAqx1yMRnQuPeAkLSPud8pGnbWwDfPcXjD2K6n7DkTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گناباد برای وطن خستگی نمی شناسند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/461154" target="_blank">📅 22:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd079a17d.mp4?token=YxOOK18blfygvORSO97wFF3PthyGjrlYFqHP_QJ21uz52IYNoJxMO2rjAKZ9Afng2noMPdOCTdEx9mrTbegITYGX_oRGhO0_P3LvmcPK5YiSBqKh7fBRQz76eq75jnt4aDmF-oplikGvTKQTnkyweydYx8itMxJ4IrZ45w5Vf_7JI5zn3-QFfgYgm9eMq8WOVhiZGBYz9hRVIVMeUJVfhJWuK3TrHLYsqD3gBbqyWO0qdTjIO_wynpAWsUtAHCK5N1WuTq-xXw81jbfsxuRAOrdALDzWPYP-ocVlsyEbjM51qo7HcAF1mxAGoDyBcKKQmrW1OdFGSxL5lGrvb1s0S1ByLOKgLY14K6GbBRbPDsyKoAaCZAFGYFLbpnJPVDjXgovUSCu0sOyp8-AGyuv4BGXcB3V0BRC7-Pp6mSvyxnuJ5Trt9FwQmaJ7ZekBj2F-E2JcSYvj7rFm-3z9Ds0NZrwVxwRFS4QZo_s2WlLNTWETJdeWav39Vf0mE2cTDBbFwAdo84kqSAdX97jTOK2Vpl_ictz2ypD056m7tK68PYKfPGT87ARuZv3tnPb4pXkoq-b6hMUsX6Rnjnm7xj2dexNKbtazSYMfBVL8kTLdkrp1k0lhguNSithYOp3f6Pds7I1WdEVpAy65mXRXgzjV57M-uxV8ag0S4pYyL9-HSSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd079a17d.mp4?token=YxOOK18blfygvORSO97wFF3PthyGjrlYFqHP_QJ21uz52IYNoJxMO2rjAKZ9Afng2noMPdOCTdEx9mrTbegITYGX_oRGhO0_P3LvmcPK5YiSBqKh7fBRQz76eq75jnt4aDmF-oplikGvTKQTnkyweydYx8itMxJ4IrZ45w5Vf_7JI5zn3-QFfgYgm9eMq8WOVhiZGBYz9hRVIVMeUJVfhJWuK3TrHLYsqD3gBbqyWO0qdTjIO_wynpAWsUtAHCK5N1WuTq-xXw81jbfsxuRAOrdALDzWPYP-ocVlsyEbjM51qo7HcAF1mxAGoDyBcKKQmrW1OdFGSxL5lGrvb1s0S1ByLOKgLY14K6GbBRbPDsyKoAaCZAFGYFLbpnJPVDjXgovUSCu0sOyp8-AGyuv4BGXcB3V0BRC7-Pp6mSvyxnuJ5Trt9FwQmaJ7ZekBj2F-E2JcSYvj7rFm-3z9Ds0NZrwVxwRFS4QZo_s2WlLNTWETJdeWav39Vf0mE2cTDBbFwAdo84kqSAdX97jTOK2Vpl_ictz2ypD056m7tK68PYKfPGT87ARuZv3tnPb4pXkoq-b6hMUsX6Rnjnm7xj2dexNKbtazSYMfBVL8kTLdkrp1k0lhguNSithYOp3f6Pds7I1WdEVpAy65mXRXgzjV57M-uxV8ag0S4pYyL9-HSSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار امشب مردم پیشوا: فریاد ملت حسین چنین است، سازش با آمریکا ضد دین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461153" target="_blank">📅 22:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96074dc5fb.mp4?token=e8iZ0zlDzYadvgohsBpAAR-2XnPdv9CmZmQTotrHweg9A1wKAh5nEVOvxMoflFztSAin1CI1k3P95NbtXa0IwhoUQT-fGa_0wtmmVwCI42y40GB3cotM5jyo00Xs8jTn6TmRx0Aki7wLW6CvcaVmN4mSQi0j7GdFP1B0I6AoOuPacNiZnKrMlLAya8TIHl6TgFxgggbswWTww55bBiufx7zqtMgzS4avKlwwZlBwIXQGOz1O328ad18oWYUV0KyMeN4Tk7bKuCuOKe2kcQ1_GBbyV-XfTq4kQa_nAYCAxc2NTLYwXa4aTh-YkilaxQDgVyZxvSzmqy6gOHIRt9YSkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96074dc5fb.mp4?token=e8iZ0zlDzYadvgohsBpAAR-2XnPdv9CmZmQTotrHweg9A1wKAh5nEVOvxMoflFztSAin1CI1k3P95NbtXa0IwhoUQT-fGa_0wtmmVwCI42y40GB3cotM5jyo00Xs8jTn6TmRx0Aki7wLW6CvcaVmN4mSQi0j7GdFP1B0I6AoOuPacNiZnKrMlLAya8TIHl6TgFxgggbswWTww55bBiufx7zqtMgzS4avKlwwZlBwIXQGOz1O328ad18oWYUV0KyMeN4Tk7bKuCuOKe2kcQ1_GBbyV-XfTq4kQa_nAYCAxc2NTLYwXa4aTh-YkilaxQDgVyZxvSzmqy6gOHIRt9YSkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به کشتی‌های ایران حمله کردیم و حملاتمان بیشتر هم خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/461152" target="_blank">📅 22:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbjct_v9hIGn0_uhGAfmyWfokGo-o11uhhzMnIr-3dY9sFW-Y_gFCvruaRPw_PWj-k8b7czk5nH94XNCOrOlQcRc9i_UR-xAz56CcOW5JHAK_sM2cT8yx_D8pQn_SX-hKqwwrMFoRINVubLfaPjHPhhicpXC9iCj81W0rWta_uLUZEb5KaI3LMhJO4eiAoHX9Ju_9DdElO6tY3WKCr19yNkrhMHFCF9IxPZ5meikEHzie2-GW70-vuGh33YG46Vg_kYo7bwv6e_jelBkYDfjVL1kA5_DXRoAtb7ND8cdz91Aowbw2KIzYdQorugBwjBzfj2o_TfTgXOsLUez_HsTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمسیون امنیت ملی خطاب به آمریکایی‌ها: تا دیر نشده به کشور خود برگردید تا بلکه بتوانید حداقل از مرز های خودتان دفاع کنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/461151" target="_blank">📅 22:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905e322c38.mp4?token=fHCX1_OGXkt1a3uQzb3CRz61DI9hae9w3mXQedBsfSWPV_IDLS9kD-fAvCaj-N0vRU6WZh3-U-ZcQfEx1Gfh2mvfZo6787tErv2keEx1gG1ZqvurFOtUYyZYpeMG-UvsmXNJ4dSM__JuhB842b3l9k6V7S7912Ic0MxBM8wDSnDcdOzS2c7puGctgGsI7a__zQM1Byy6dHtdyrqINB5O8Xz4AZe3HcZLi9DpPQUVc1e47bUytZlUdGedvtrBuw4OzgtNQ5FLt-AmmFLouLLxOJeDLCV8OxI6dfVzWtjUuTVgmLj7er3BpcfStXP72SJ0702laSAG_mWn4xcNQfZ-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905e322c38.mp4?token=fHCX1_OGXkt1a3uQzb3CRz61DI9hae9w3mXQedBsfSWPV_IDLS9kD-fAvCaj-N0vRU6WZh3-U-ZcQfEx1Gfh2mvfZo6787tErv2keEx1gG1ZqvurFOtUYyZYpeMG-UvsmXNJ4dSM__JuhB842b3l9k6V7S7912Ic0MxBM8wDSnDcdOzS2c7puGctgGsI7a__zQM1Byy6dHtdyrqINB5O8Xz4AZe3HcZLi9DpPQUVc1e47bUytZlUdGedvtrBuw4OzgtNQ5FLt-AmmFLouLLxOJeDLCV8OxI6dfVzWtjUuTVgmLj7er3BpcfStXP72SJ0702laSAG_mWn4xcNQfZ-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌های مجلس: نبرد هرمز تعیین می‌کند که نظم ایرانی حاکم همیشگی منطقه شود یا نظم آمریکایی
🔹
غرب آسیا آن‌قدر ظرفیت ندارد که بتواند ۲ نظم را تحمل کند و در نهایت یکی باقی می‌ماند.
🔹
با ایستادگی ملت ایران نشانه‌های پیروزی نظم ایرانی به مرور دارد نمایان…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/461150" target="_blank">📅 22:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
من از اهالی روستای پشگ، بخش چاه‌دادخدا، شهرستان قلعه‌گنج هستم. ما از نبود آب آشامیدنی، جاده مناسب، خدمات بهداشتی و درمانی، دوری از مراکز درمانی و نبود فرصت شغلی رنج می‌بریم. لطفاً مسئولان برای جابه‌جایی روستا و نزدیکی به جاده و مراکز درمانی و همچنین واگذاری زمین مسکونی به اهالی اقدام کنند.
🔹
خرمای سال گذشته ما به‌دلیل شرایط جنگی فروش نرفت و
خرمای امسال
هم دوباره به‌دلیل همین شرایط،
توسط واسطه‌ها با قیمت پایین خریداری می‌شود
. واسطه‌ها می‌گویند راه صادرات بسته است.
🔹
لطفاً صدای چایکاران باشید. از خردادماه چای سبز تحویل داده‌ایم اما دولت هنوز
مطالبات چایکاران
را پرداخت نکرده است. اگر از کشاورزان حمایت نمی‌کنید حداقل پول دسترنج و محصولشان را به‌موقع پرداخت کنید.
🔹
با نزدیک شدن به آغاز سال تحصیلی جدید در مورد تعیین تکلیف
استخدامی نیروهای شرکتی نهضت سوادآموزی
و جبران کمبود معلمان مقاطع تحصیلی از میان این همکاران پیگیری فرمایید.
🔹
لطفاً وضعیت
تحویل خودروهای برقی توسط پرشیا خودرو
را پیگیری کنید. با وجود گذشت یک سال و نیم هنوز خودروها تحویل داده نشده‌اند و کسی پاسخ‌گو نیست.
🔹
لطفا دربارۀ پایین بودن حقوق و مزایای استادان حق‌التدریس دانشگاه‌ها هم پیگیری لازم و اطلاع‌رسانی انجام شود. استادهای حق‌التدریس نه بیمۀ مناسبی دارند و نه حقوق کافی دریافت می‌کنند.
🔹
تو رو خدا صدای ما را به گوش مسئولان مرتبط با شرکت
سایپا
برسانید. این شرکت
به وعده‌های خود عمل نمی‌کند
و خودروهای ما را با وجود گذشت یک سال هنوز تحویل نداده است. هنگام تماس هم پاسخ درست و مناسبی دریافت نمی‌کنیم. الان ۹ ماه از موعد تحویل وانت پراید ما گذشته و با اینکه ۳ ماه است فاکتور شده، هر بار پیگیری می‌کنیم فقط وعده‌های جدید می‌دهند.
🔹
من از حاجی‌آباد
زرین‌دشت فارس
پیام می‌دهم. خواهشمندم پیگیری کنید چرا
زمین‌های طرح جوانی جمعیت
به متقاضیان تحویل داده نمی‌شود. نزدیک به ۵ سال است که ثبت‌نام کرده‌ایم اما هنوز زمین‌ها را تحویل نداده‌اند.
🔹
لطفاً خبری از آموزش‌وپرورش درباره
شهریۀ مدارس دولتی و هیئت‌امنایی
بگیرید. از یک طرف اعلام می‌شود دریافت شهریه در مدارس دولتی و هیئت‌امنایی ممنوع است اما از طرف دیگر برخی مدارس از والدین درخواست شهریه می‌کنند. لطفاً پیگیری کنید که دریافت چه مبالغی قانونی است و مدارس بر چه اساسی شهریه دریافت می‌کنند.
🔹
مسئولین به
معضلات اجتماعی و فرهنگی
علی‌الخصوص بی‌حجابی و بی‌حیایی در شهرها و برنامه‌ها بپردازند. جامعه اسلامی آندلس با گسترش  بی‌بندوباری از بین رفت.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/461149" target="_blank">📅 22:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db4f0dd22.mp4?token=aEW4dWb0mgwDDHMYfFiMoD8aYrk7tOS3SbBBZEKfLs8zoT7qqYLunQZx7rs9VxVTz9dU2S4No2yXVKWk_72GMAhMY_rGWVI8EsBZetLU8ucmkGi9wdm1Okkwnm5bNRt3TcCOEU6RCVsNhNFEbuVtDPCsFWFw0EpTdHrHnHPXDSskWqr_eJ5Q2tF-hmNGMp797cw3E3yy2lkCkvaQmLgQ-nayBvPlGyaI0t8F_7dtJonvSfpDbhgxrkyOY1k1azOs5cxCLZUgeokcWYYDf-lmlyGJf9_2mr28PMW7zSygwW_i0X8tTCGClbvF1koDm6VW1Cid8e_Sgv3hwuLyM5VDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db4f0dd22.mp4?token=aEW4dWb0mgwDDHMYfFiMoD8aYrk7tOS3SbBBZEKfLs8zoT7qqYLunQZx7rs9VxVTz9dU2S4No2yXVKWk_72GMAhMY_rGWVI8EsBZetLU8ucmkGi9wdm1Okkwnm5bNRt3TcCOEU6RCVsNhNFEbuVtDPCsFWFw0EpTdHrHnHPXDSskWqr_eJ5Q2tF-hmNGMp797cw3E3yy2lkCkvaQmLgQ-nayBvPlGyaI0t8F_7dtJonvSfpDbhgxrkyOY1k1azOs5cxCLZUgeokcWYYDf-lmlyGJf9_2mr28PMW7zSygwW_i0X8tTCGClbvF1koDm6VW1Cid8e_Sgv3hwuLyM5VDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به کشتی‌های ایران حمله کردیم و حملاتمان بیشتر هم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/461148" target="_blank">📅 22:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954e22293b.mp4?token=MOiLFrtTmFOJtNGSsiAm_ddeYiYdLF6kCDR2Mhy7rDvcN_yHEInI0xnCUj-1lYnZDgVXp_SFA561jEpcuRVG8XP--5387-Ztlzak2ESnJM3ecvqa4HuiKXDzhJFE9Ri5lT9hnVcQ-CibvoNzB-YvUJhvBrlF59rjla3MrdYdOWqBVuAERNv0Ge3vJSdbAy99iGgzAN8aAHbBeM7CXSY5tx_KDhXKx0wY9bkCo5_Uq93CGNyDsMnAfbnXPO8ZPEjFsUDDFF-64zOo6LTH2lrbR1hijGiuXjIYVLF06b_0SWLLil9XeBzCqDSNFA7YtoR0jxjUUyLNEIVFUsRJpPVc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954e22293b.mp4?token=MOiLFrtTmFOJtNGSsiAm_ddeYiYdLF6kCDR2Mhy7rDvcN_yHEInI0xnCUj-1lYnZDgVXp_SFA561jEpcuRVG8XP--5387-Ztlzak2ESnJM3ecvqa4HuiKXDzhJFE9Ri5lT9hnVcQ-CibvoNzB-YvUJhvBrlF59rjla3MrdYdOWqBVuAERNv0Ge3vJSdbAy99iGgzAN8aAHbBeM7CXSY5tx_KDhXKx0wY9bkCo5_Uq93CGNyDsMnAfbnXPO8ZPEjFsUDDFF-64zOo6LTH2lrbR1hijGiuXjIYVLF06b_0SWLLil9XeBzCqDSNFA7YtoR0jxjUUyLNEIVFUsRJpPVc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌های مجلس: نبرد هرمز تعیین می‌کند که نظم ایرانی حاکم همیشگی منطقه شود یا نظم آمریکایی
🔹
غرب آسیا آن‌قدر ظرفیت ندارد که بتواند ۲ نظم را تحمل کند و در نهایت یکی باقی می‌ماند.
🔹
با ایستادگی ملت ایران نشانه‌های پیروزی نظم ایرانی به مرور دارد نمایان می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/461147" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461146" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3jp6SQA4LlCUcfki70TE-qlV-fViMljdjfTfNj6BeK4HqYAuYUL-zhyOa4VvpRZAs7_duy4YlVl8C3Rx4GqycaLPnKOnk_w1EdlsenDrSvO0yATkfb5h2EPe-6dL9o-pcpSrBjEHqE9hI2okdvfEApHZZ4u0u_m7XhRtgzrKcO-CVQyNJEbIaj2g9uC1A-3jxbfbyK4SmTPSUCj1VNtTb_FqJOXnFovK7peBw99P3Ln8V2sMt7Ijz2hjKkWMiKjAAoJTHN7ImOpxE0rBZYobsKtscT_Z1cIWeLPY1eLmUs221hhFln_ltKiH0ZHYeXV2uqt1_B9m5dqbm93VvR4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461145" target="_blank">📅 22:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38fef9656c.mp4?token=WgKoxARVBWMvyZM4h-9NZyhfmdoj899MwyShQBDRIMPqA6NgmhGPtCZ1wkFucgkW1jyFbc5zD_-BhMkUx15auorQflq8PR-nw1XanPmYPCacwxYP669vYaJ4Vg5RcbIc1Y-OOpo8ExOA2Mm3TnUoqfokca0gqbMbYBYpfTOmq1wdcdD_1AsuQ5tLq_V6y9gW4Ym9_iGz45Px67zfBBlLIgE5SewQYWsZSv4Po3A04SZs12fUYurVrbIODrDDYusSD4MS_DQADG-G11SjuhRB0cWBMhhfjaJJn1ButVIb05xQRaxFjBTzdPfiydu9R_QlZPz7wt3zXCsHzeUCT3vjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38fef9656c.mp4?token=WgKoxARVBWMvyZM4h-9NZyhfmdoj899MwyShQBDRIMPqA6NgmhGPtCZ1wkFucgkW1jyFbc5zD_-BhMkUx15auorQflq8PR-nw1XanPmYPCacwxYP669vYaJ4Vg5RcbIc1Y-OOpo8ExOA2Mm3TnUoqfokca0gqbMbYBYpfTOmq1wdcdD_1AsuQ5tLq_V6y9gW4Ym9_iGz45Px67zfBBlLIgE5SewQYWsZSv4Po3A04SZs12fUYurVrbIODrDDYusSD4MS_DQADG-G11SjuhRB0cWBMhhfjaJJn1ButVIb05xQRaxFjBTzdPfiydu9R_QlZPz7wt3zXCsHzeUCT3vjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهرم در شب ۱۹۳ همچنان پای کار مقاومت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461144" target="_blank">📅 22:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئیس دانشگاه سمنان: شایعۀ تعرض دانشجویان عراقی، دروغ بزرگ است
🔹
رئیس دانشگاه سمنان: بامداد دوشنبه میان چند دانشجوی عراقی و ۳ رهگذر، شامل یک زن و دو مرد درگیری رخ داده و به زد و خورد منجر شده است.
🔹
براساس گزارشاتی که در اختیار پلیس است، آن ۳ نفر حالت عادی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461143" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce568ac68b.mp4?token=ohUu9Ri0G8G9_gb6EL0w6HvYBCJz6BTBdxz-XGc3GylD_Hk2eSKy-QXEHmmvns007NMByosbCYU9a3YZajHGcDWs-MDxIWUmR3b34Oe2-L0dvA7x2N-FTAg0ZKFgYbFEjZhDT5gFHjR-qWw7Q1cQWX6Y4puLKE3sjiDvZfaQcJKr6WZSLloXD57syCkZ5ewyF7xDyUbaizX7atwwumwkXbWkCOLu_zjgmK6P6__PruW3lKMJJasAKHhsFHwuWgG74xkBbxlX7aNMVM-rMWbTcbKQz9fHkCcmF2LRdoRGpk_-cwYploT4I7dnQFGgpdd8LpQYsUCaMRqu71X_NSk44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce568ac68b.mp4?token=ohUu9Ri0G8G9_gb6EL0w6HvYBCJz6BTBdxz-XGc3GylD_Hk2eSKy-QXEHmmvns007NMByosbCYU9a3YZajHGcDWs-MDxIWUmR3b34Oe2-L0dvA7x2N-FTAg0ZKFgYbFEjZhDT5gFHjR-qWw7Q1cQWX6Y4puLKE3sjiDvZfaQcJKr6WZSLloXD57syCkZ5ewyF7xDyUbaizX7atwwumwkXbWkCOLu_zjgmK6P6__PruW3lKMJJasAKHhsFHwuWgG74xkBbxlX7aNMVM-rMWbTcbKQz9fHkCcmF2LRdoRGpk_-cwYploT4I7dnQFGgpdd8LpQYsUCaMRqu71X_NSk44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌به‌خودی جدید ترامپ در تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461141" target="_blank">📅 21:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌ سخنگوی وزارت خارجه: کشورهای متخاصم با الگوی رای گله‌ای علیه ایران رای دادند
🔹
تاسف‌بار است که کشوری مثل ژاپن که قربانی سلاح هسته‌ای بوده به قطعنامه علیه ایران رای مثبت داده. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461140" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌سخنگوی وزارت خارجه: اقدام شورای حکام علیه ایران یک تناقض آشکار است
🔹
عدم دسترسی آژانس به تاسیسات هسته‌ای ایران ناشی از حملات آمریکا و اسرائیل بوده و ایران مرتکب عدم پایبندی نشده. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461139" target="_blank">📅 21:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Illxirs7dONBcCvyMXW-G19L4Om43dh983qkMRYe9A_FviE1kGkty_Iyd6z0I4_2rpXdg85KFPfgLTPwnNsbxSJYImTjC2-VaRU18iajsfTy6wpsC2kZ4uagLy4ivbC0KuWoyzS9QS8SSO-DU4LSGMIm5IGTvpp1z5lcEIZrQpPJWNGpTxyRLcmol9M7L2P7TXn7_89xVg7Qm7YqTA57JEA2cJvHlnVzjxOd9LpF06t97Mbu4btlpCHLDCsSoXb-jinHNzMffTvC7MDVcs3lz2qQOs3TaKc-V9JGZnHwQc-vWA1qCJRNSN8sz-sqorrTkRnfwLAgsNb7iN6N4Wbc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نمایندۀ ایران در آژانس: این قطعنامه مبنای قانونی ندارد و نتیجه‌ای درپی نخواهد داشت  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461138" target="_blank">📅 21:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceeb4b5605.mp4?token=FYOISLkwfuzvPd7OH6cLIvdy3E7go6ECol0I35CONBHxAwlVHMCse-iRSR_eGsEkVd5_kVbBCqL1pkRMREOp_lT0UH0jApn6WADAJsKU-LrXqIAMEQDFtVcTYR9m3Ocvx9sLil2a8Z-UC57GGJ5CyD1cTi3vCi9Dw-HZ4fpzu3ZunMTBEvU7rNAPca-5_pP8rU9LoPJcetKjyvWHRRxxObMjCcRgEK4Ky-fM6vuJAGbwQ2mt6UlplazGlzjbMma7T8jPBpAI1NSRwox_2zYITGVLRqJMI21b_eRzEb9qoivXziLIBozFeZrzqS4yIZu05c6wz7UXPJnBG2hXx-4l_08a2DYCIai_vpfODkx0daOtbTGOZ7c30ewHUa8DWupJoZggIyTXaVL-ZT1-3JbfcNFOGWOEPXlHQAtllE8bbcmnf-G7OC9rxGbFAc3HPJwhS6MHMvgBuFBxjIVtze0WX4TVbMmiVKkiWvYXoFvjUffM7kXZ3D5MqmxBnxGa-BY7TIZDY859VrCaFIr4V0O3W_CCK-4lAwwXpzNqmRVqot0pLrA0Hq_Et6agCnCR8BH2D0YtppDLHVf1jXYSzcYX4aXXaW7RCrzvEvql7_UCQp0Vxgl3XT42UFgXEdng8hK2NjuOi2CkgkL-otojfOtkU712VoHZ3lYpyYjgVUResIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceeb4b5605.mp4?token=FYOISLkwfuzvPd7OH6cLIvdy3E7go6ECol0I35CONBHxAwlVHMCse-iRSR_eGsEkVd5_kVbBCqL1pkRMREOp_lT0UH0jApn6WADAJsKU-LrXqIAMEQDFtVcTYR9m3Ocvx9sLil2a8Z-UC57GGJ5CyD1cTi3vCi9Dw-HZ4fpzu3ZunMTBEvU7rNAPca-5_pP8rU9LoPJcetKjyvWHRRxxObMjCcRgEK4Ky-fM6vuJAGbwQ2mt6UlplazGlzjbMma7T8jPBpAI1NSRwox_2zYITGVLRqJMI21b_eRzEb9qoivXziLIBozFeZrzqS4yIZu05c6wz7UXPJnBG2hXx-4l_08a2DYCIai_vpfODkx0daOtbTGOZ7c30ewHUa8DWupJoZggIyTXaVL-ZT1-3JbfcNFOGWOEPXlHQAtllE8bbcmnf-G7OC9rxGbFAc3HPJwhS6MHMvgBuFBxjIVtze0WX4TVbMmiVKkiWvYXoFvjUffM7kXZ3D5MqmxBnxGa-BY7TIZDY859VrCaFIr4V0O3W_CCK-4lAwwXpzNqmRVqot0pLrA0Hq_Et6agCnCR8BH2D0YtppDLHVf1jXYSzcYX4aXXaW7RCrzvEvql7_UCQp0Vxgl3XT42UFgXEdng8hK2NjuOi2CkgkL-otojfOtkU712VoHZ3lYpyYjgVUResIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرسایشی‌شدن جنگ به نفع ایران است یا آمریکا؟
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461137" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461135">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به چندین شهرک در جنوب لبنان
🔹
رسانه‌های لبنانی از حملات جنگنده‌های رژیم صهیونیستی به شهرک‌های صربین، حداثا، حاریص، النبطیه الفوقا‌ و الخیام خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461135" target="_blank">📅 20:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec7416fcb.mp4?token=NSSy_csfL62TgqBtTpzhFEqTm3EoFVXHvxe4nkj-G8oXts0Obtu3yzF5aMO17sGb4-NP1QkY_o9izj8e8TlQuWfu_XtAdw1TRp76GMaVa5M_eDA_Qpp0FdXB4oo18Wtv2AYrfRIAbZjpw9WCdKifuRA1ls3BEiNHJHSnmhw52iGDx5XhY2MiMXkKBVKp-J23TSdp12pvFDNyveL7Va58rreqo0GcWgdVLNkoB9lpRrpLtp3He-enmqTMURAb1N0fQ3_BoRmEzgH9WjsDV1OXJPFOQTk96kyj8j_7gLHomhKqz3dn5MQUp5hnxfc0i77rt7Pk6unw4HURc4d7zFr7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec7416fcb.mp4?token=NSSy_csfL62TgqBtTpzhFEqTm3EoFVXHvxe4nkj-G8oXts0Obtu3yzF5aMO17sGb4-NP1QkY_o9izj8e8TlQuWfu_XtAdw1TRp76GMaVa5M_eDA_Qpp0FdXB4oo18Wtv2AYrfRIAbZjpw9WCdKifuRA1ls3BEiNHJHSnmhw52iGDx5XhY2MiMXkKBVKp-J23TSdp12pvFDNyveL7Va58rreqo0GcWgdVLNkoB9lpRrpLtp3He-enmqTMURAb1N0fQ3_BoRmEzgH9WjsDV1OXJPFOQTk96kyj8j_7gLHomhKqz3dn5MQUp5hnxfc0i77rt7Pk6unw4HURc4d7zFr7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
واکنش معاون وزیر خارجه به تصویب قطعنامۀ ضدایرانی: در شورای امنیت هم نمی‌توانید کاری از پیش ببرید
🔹
غریب‌آبادی: به تأسیسات هسته‌ای تحت پادمان ایران حمله می‌کنند، روند عادی راستی‌آزمایی را مختل می‌کنند و بعد همان اختلال را دستاویز صدور قطعنامه در شورای حکام…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461134" target="_blank">📅 20:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461132">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnOO4FSgbZrCFPS7hwA1RHRoiA8lSU2IK2fdyYk60kUL-nehyLHR4QjUEVEQ7ghngsCbdTmtkzPoBgnjOO1v7a7v7o_o0f8sVpLexQde9JFib_A0Fy9Oiz_7-r4la1qoimgFcnzapjbsAgqaiJb2JnNJKYny3QT3VF0NZectWUWoOR84aP9z1xqKdbTMN7_KuftMSkfhmEOSQxpvB5hU8J0Upb7r05SWjraAMdb4tdD7_x9RdiUmT1HJuYMGLZ_kMjfaFJKQ0yzy-CmpPNckZM5RALWWJvsjppQAwk_Y9sw5t6krOY-9XF3udIQebAJwSaQ_U52Tjt6ub9LQ8RXT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: به گسترۀ ایران، از اعماق زمین تا اوج آسمان، به زودی خواهید دید
...
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461132" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461131">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96386b7e8.mp4?token=omX-6IWb8CNaI6nFDm3dSKygMLDtwSJKPQw1z0g7Eu5zo3GPmoqxvciTo6XiNeAmRfXeEWHjw5jglgbmIiylP9dopj71sBNLMydPteqyoOlSWOjnfCPQoI344xtpEAIpJniLKIiYcUyaK7ifB8a4rh_SW_PVf6fG9586W0d9YcHAbfuk9kOaa3pri9shA5Z-G5n2kjrkHl9Cm4fvsSxyR3JmG4cid2iFnLy8tPT6-oAk_d0GdPXD5NeCNkm9V1-WegDdw6CdIusvnWX2GIrdsP7cnzcI1-9LCDaPVkA0GyEVGu1TUq3T4uGkx03-mMd23yMCyODDqEdJVTq0ggV0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96386b7e8.mp4?token=omX-6IWb8CNaI6nFDm3dSKygMLDtwSJKPQw1z0g7Eu5zo3GPmoqxvciTo6XiNeAmRfXeEWHjw5jglgbmIiylP9dopj71sBNLMydPteqyoOlSWOjnfCPQoI344xtpEAIpJniLKIiYcUyaK7ifB8a4rh_SW_PVf6fG9586W0d9YcHAbfuk9kOaa3pri9shA5Z-G5n2kjrkHl9Cm4fvsSxyR3JmG4cid2iFnLy8tPT6-oAk_d0GdPXD5NeCNkm9V1-WegDdw6CdIusvnWX2GIrdsP7cnzcI1-9LCDaPVkA0GyEVGu1TUq3T4uGkx03-mMd23yMCyODDqEdJVTq0ggV0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی روحانی بر «تسلیم» لباس رونق می‌پوشاند
🔹
حسن روحانی، رئیس‌جمهور سابق، به‌تازگی در اظهاراتی گفته: تنگه هرمز نباید تنگه جنگ باشد؛ ما که نمی‌خواهیم همه‌اش بجنگیم؛ تنگه هرمز باید تنگه پررونق باشد؛ اگر رونق نداشته باشد آن را می‌خواهیم چه کنیم؟
🔹
این اظهارات…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461131" target="_blank">📅 20:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461130">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW-VWbRUXUbn244fpCQnSsgYKA4KUFlPKn_ISQeXAURxGUNKv80xG-BDCM5-xrgEHxhFylq4uLmlYHET3GCpFAkXzGdOgaU8l6xLl1p0JfipJqvBci8g0kIV0SV0_Y6kcgzJEe_cEUjzW6MY8JmKC1Eo9oPutNi62JvGDBEs06kN4rqvYBhqgGfoS_Pn7ZRwod0gfXQIdEd4dp37gof3hWwPxKpeEhdZvNmGgJmZxY21MDXWFZKsRe5rhiS-maNy9suRY88Uh3RILQD2AtmoXQl8PeUXanoBZPTEf5LsVNPHyPnKOjmaOql2M8PYpbCiIeHg5OLV5PSwDGvNw8FTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آژانس پروندۀ هسته‌ای ایران را به شورای امنیت ارجاع داد
🔹
رویترز به‌نقل از دیپلمات‌ها خبر داد که شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
🔹
این قطعنامه…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461130" target="_blank">📅 20:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guQ-9BlOmah84VwwcToRVAhz-BcC8r7fKV5VEeiYl4nJznY5ILC0tcFjxJ52EjBakwxEnZvHH-xuqWkahNXNAgsR5duXmmi5EyS5t0uy9_fWgVmm4415XqkzOzsufGbba84vwqAcQnLLo-vpDya_cYuRnSPBFeLSfIPEd_V_qZuRPeP2I8-yWz8om-rX5kK8sptFJreoOEYlV_c7mNta0p9nhwp7etTno3ffhSQQZe9QCaVyUaAxdn6aPMQ5cZmAF_IuE1spFxeuJqcrIxepH3PXnUJUOJVAbGPACd6yFhKi2iEaPLh5IjV8gM8KgSbz5CvGi4Lg8qVZQ-evlki83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون پس از ۲۰۰ روز یاد شهید مدرسه میناب افتاد
🔹
«ماکان جان تو باید امروز پشت نیمکت مدرسه‌ات می‌نشستی، مشق می‌نوشتی، بازی می‌کردی، می‌خندیدی و برای فردایت رؤیا می‌ساختی». سردار آزمون، مهاجم شباب الاهلی امارات، چهارشنبه عصر، ۱۹۴ روز پس از ۹ اسفند و آغاز جنگ، در استوری اینستاگرامی از ماکان نصیری، دانش‌آموز شهید مدرسه میناب نوشت.
🔹
آزمون در بحبوحه جنگ آمریکا و اسرائیل علیه ایران در استوری‌های اینستاگرامی از شیوخ دبی تمجید کرد. امارات در این جنگ ضد منافع ایران عملیاتی انجام داد و از مقرهای اصلی اطلاعاتی اسرائیل بود.
🔹
معاون رئیس‌جمهور در امور توسعه روستایی و مناطق محروم دوشنبه درباره بازگشت آزمون به تیم ملی گفته بود: «آقای پزشکیان خودش شخصاً موضوع را پیگیری کرده و می‌توانم بگویم که ۹۰ درصد مسائل او حل شده.»
🔹
حالا آزمون در استوری‌اش با بیش از ۶ ماه تأخیر بدون اشاره به عاملین این حمله نوشته: «کاش هیچ کودکی در هیچ جای دنیا، معنای جنگ را با جانش یاد نگیرد».
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461129" target="_blank">📅 20:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf0NOzJrU5NasH3FgHtx_lPpXgL_r0Vartx2NKZ6qrUqycGvPZrO4ldzPfDMIbAuGCTVtHbH9aGdTrhSOtrQ2We8OvFBJWamJDfYLA1MrudsATDbzj1OI5pMS0QB6WuHCnd-vHhdZzWKRWqpsNaOVxbTS_hZEEFKAt9aoABOT8hLGsoIfF2Tmt6zgaFiHUmmeCzJKxi0zblkMuZFmdGFdKw8DVi2vm2steqpmvjiHtNmnDzkuMVJSVPeMllZP3O9q5S6cyymdFjBP-BFNXUw_M-FOKJUSZorhii88bLPr2jDktveCvF3kz1PHcLAgFdQutF8naDSBg91LJQtws8GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله جنتی: هر تجاوزی با پاسخ محکم‌تر روبه‌رو می‌شود
🔹
اقدام سپاه در به غنیمت‌ گرفتن یک زیردریایی پیشرفتۀ آمریکایی جلوۀ دیگری از قدرت ایران است؛ ایران قرار نیست در برابر زورگویی و تهدید سر خم کند.
🔹
همان روحیه جهاد، تحرک، سرعت‌عمل و فرماندهی که در میدان نظامی وجود دارد، باید در عرصۀ نبرد اقتصادی نیز دیده شود.
🔹
دشمن اگر نتواند ملت ایران را با جنگ شکست دهد، ممکن است از راه فشار اقتصادی و سخت‌کردن زندگی مردم وارد شود؛ بنابراین مقابله با این جنگ فقط با سخنرانی و توصیه نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461128" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌ ایران، روسیه و چین: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد
🔹
ایران، روسیه و چین در بیانیه‌ای مشترک در نشست شورای حکام آژانس، پیش‌نویس قطعنامه آمریکا، انگلیس، فرانسه و آلمان برای ارجاع موضوع هسته‌ای ایران به شورای امنیت را فاقد مبنای…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461127" target="_blank">📅 20:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461126">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6djHlbeMY9JF05L1VkMrWh6iylKaUdCU0BJdPHmnKRYGpvbBjv5qK-QQxE08a3kmSiA0bkDO_P_9iRMDA1XZ5T4qEyLX6KJ80tSoJ-sKykQZ9Q_vn3Q8Q72QE3yBd4cOZn-288GwQTsLWNBqyN75i82_AcWvR8TXRdytnDzjwEg0SLkrpf8XV36Rw0fSyzhoFlnPiCVInJmQBJ2Bhcxnmyl3zAT8LMbNCT0saxgP42PSj_fWSGZzSsRl8g3ZEJ0uMg_U-4y-10hqyPhglyuN_S8N8ZO9PBTHX_V_R_Pz3CDOz-wRMd5_L3DSOL9EtWfiASHX2iGNW4D0Gf09GFi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۹ هزار نفر از بانک مرکزی اوراق سکه خریدند
🔹
در نخستین عرضه «اوراق سلف سکه» توسط بانک مرکزی، ۴۱ میلیون و ۴۰۰ هزار ورقه در بورس فروخته شد.
🔹
هر ۱۰۰۰ ورقه معادل یک قطعه سکه است؛ یعنی مجموعا معادل ۴۱ هزار و ۴۰۰ قطعه سکه از کل ۱۰۰ هزار سکه‌ای که بانک مرکزی در این طرح قرار داده بود پیش‌فروش شده است.
🔹
سررسید این اوراق ۳‌ماهه است و پس‌از آن دارندگان امکان دریافت سکه فیزیکی یا فروش با بازدۀ تعیین‌شده را دارند.
🔹
قیمت هر قطعه سکه در این طرح حدودا ۲۳۵ میلیون و ۷۰۰ هزار تومان است و ۷ درصد سود هم برای خریداران تضمین شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461126" target="_blank">📅 20:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شنیده‌شدن صدای انفجار از سمت دریا در جنوب جاسک
🔹
حوالی ساعت ۱۹:۲۰ امشب صدای انفجاری از سمت دریا در مناطق جنوبی شهرستان جاسک شنیده شد.
🔹
براساس گزارش‌های محلی، شماری از مردم ساکن در مناطق ساحلی جاسک این صدا را شنیده‌اند.
🔹
تاکنون جزئیاتی درباره منشأ، محل دقیق و علت این انفجار در دست نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461125" target="_blank">📅 19:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnYm8B2-PxhWB0-jjDPugoggznu98sKfpr0UX_jVE9rdL3_wvCHlsDTFE4oUjPBRmDVnwSp1dYBoKDrOwBv-ywv4-fhgjAka13zkhEe6s99f3i09kb2avRH8-Dg9pOgluwRI9rLngOeBysXJLACWyJNYAqq6qCpXxOgB3rfrvObrRxsZEBAdl2RDdQGIjFHdCQTWucN6PWBjd61zHGt__-T017J7UKW6HS-27b_NdqUf6EqYJHifO4N8xi8Mt3Bt5OLrxZkAtojfHdi0fAHl8SUKDK7WrJi5bR4mNfLwXopwOwN5czIwsRuukj3l_2OWv8sppTjnRJnbSt7CxhE4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۷۷۰۰ بار توافق با دولت لبنان را نقض کرده است
🔹
ارتش لبنان: نظامیان صهیونیست از زمان امضای توافق آتش‌بس با دولت لبنان حدودا ۷۷۰۰ بار آن را نقض کرده‌اند.
🔹
هدف نهایی اسرائیل، ضربه زدن به اعتبار ارتش در داخل لبنان و در برابر جامعۀ بین‌المللی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461124" target="_blank">📅 19:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKuijd4tyVdW4HAYxtCnU2Ea_BA40zilhPnq26p6S0yFu210cw9eaUrlZeWIOQxiWL4D1iYtn6kcgYpG0lRL4EwFBI8RzhV_2rJ_6srSgmrtuB_hLk7WJKg3sOFfgE69Ds-Q0vESIAxU-Vw6kSC0VBnDq723U5MdIjYqWwZ6oRm-S1zKa-qPayI_d_AeHCPTSLgmZtNpSnTN4XSpBxwxw-hvja3on2t9bOw0sQ9hl6fpb1iE0XVxwluMbPT5qjVX3oy7eJ_-3VLBCA1U8t1s_Ti55uNhH_qOj2eN5CmyAuTeGLfnquFrCR1CWA63q6fiaa-GGZPzfUq861cQdzseZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
راهی جز جهاد و مقاومت پیشِ ‌رو نمانده است
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461123" target="_blank">📅 19:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
فرمانده‌ای که این روزها نامش با تنگۀ هرمز گره خورده است
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461122" target="_blank">📅 19:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: رفتار آژانس و گروسی یادآور داستان حکیم عضدالدین ایجی و خان مغول است
🔹
هرجا که در حوزه‌های دیگر کم می‌آورند، سراغ آژانس و شخص مدیرکل می‌روند و بالعکس، مدیرکل خودش را عرضه می‌کند برای سوءاستفادهٔ طرف‌های اروپایی و آمریکا علیه ایران برای…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461121" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe01945e1.mp4?token=SjoizEciBBqYfKgHF72W_6vcGddFok4dFKUCgheJ690c5pv63dSBJGUPwyhzukm8vSZEg6FKK3NgeK2FpPtZVpBKU-EIg3sLnIGbBrmZdhmawV8zlkpjQ_DayLJK5m9xEV_eNlIl_6fA3fHPvvmYfbjc_wEyeIhh_ITftjuzr38gx7qwchMgtcHc7eJqKLMtoQuknTRV21mcBFscn1orl00FTGLV_7fsXSu3C3geKVH6Ba-VjM-BCt70rSwV47LmGFoPa-eiuVKQRHj0GEzSa_Fl00P38-DBvYZqUoosrOKXZ9NGdIxaplpBilDU_Wxty93QRtWgjMxxjqOReneSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe01945e1.mp4?token=SjoizEciBBqYfKgHF72W_6vcGddFok4dFKUCgheJ690c5pv63dSBJGUPwyhzukm8vSZEg6FKK3NgeK2FpPtZVpBKU-EIg3sLnIGbBrmZdhmawV8zlkpjQ_DayLJK5m9xEV_eNlIl_6fA3fHPvvmYfbjc_wEyeIhh_ITftjuzr38gx7qwchMgtcHc7eJqKLMtoQuknTRV21mcBFscn1orl00FTGLV_7fsXSu3C3geKVH6Ba-VjM-BCt70rSwV47LmGFoPa-eiuVKQRHj0GEzSa_Fl00P38-DBvYZqUoosrOKXZ9NGdIxaplpBilDU_Wxty93QRtWgjMxxjqOReneSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب منازل مردم جنوب لبنان به دست صهیونیست‌ها
🔹
ارتش رژیم صهیونیستی در شهرک بنی‌‌حیان در جنوب لبنان چندین ساختمان مسکونی را منفجر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461120" target="_blank">📅 18:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smhmeuspk_YA7KngJWzdNpwJfZnf1hXdr62ib2GaH_YUMDDEV-3K-yvbiQKaOKxxSUI1sta3RDZ-QVPzuTU-5vx1yR0qx4eYMNPVJ4V4ee9RvpvBCaQvcvo4zhOxsC5qdewTO0bk_7zKPzJ5SiSpM1J5MD0qW31FdelkM7K9K3GQsTF-NL_BQJcgAIQs5cZF21JO_uF_Kow_xDldqZYz0ISNT2DZQsrfxhZyVED9VhRykaVdd4D8JjQr-Xxz7Vapf-cuTmzFA2HMSqyNMXHYpaN4jnpBTqSjrpAvmotg5VXJ9ps0SHth4G0RtZzyUSgSBhs39pGukQDsSrPfAD5gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: شکار زهپاد آمریکا می‌تواند فرصت جهش در سامانه‌های خودمختار باشد
🔹
اوایل دهه نود، ایران«RQ-170»را تصاحب کرد و کمتر از یک دهه بعد، به قدرتی اصلی در عرصه پهپادی جهان تبدیل شد. حالا یک زهپاد آمریکایی می‌تواند به فرصتی برای جهشی تازه در سامانه‌های خود مختار تبدیل شود.
🔹
ترامپ کاش پیش از اخراج ژنرال‌های باتجربه پنتاگون از آنان می‌پرسید طرف حسابش کیست.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461119" target="_blank">📅 18:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b0723c32.mp4?token=NJjT9Lmap44C35KsvVWCt-tTJLG_jPf7OtYrHVzANHd7Mjc_hQPImgZvanqOlsahKMRD451_Qfdx2fOyZbHM78fAUI1UmCQqZ1eOBtMNWhFye_IOrl-yutL3CsHXUPZKLgXrM7nVaBWv_FrwUggQ0pshrMWVKD2Rw-9fvhDGb9hh1jDVcSBCjuWVxl0iT6Z0i0HYgAmezK01Le4ggsPpvKqWTQqKo3xdFOjfviaY1D8bCizeMU7XwS6_BFukIjb29GuKMGeWgUbBgREM9sRvfLh_T5tmJqq2DK5Pg6OiG4_LqxmWHDI4JMZA1JnKfu4xtEUb3lx3vy4p0mTTtxI7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b0723c32.mp4?token=NJjT9Lmap44C35KsvVWCt-tTJLG_jPf7OtYrHVzANHd7Mjc_hQPImgZvanqOlsahKMRD451_Qfdx2fOyZbHM78fAUI1UmCQqZ1eOBtMNWhFye_IOrl-yutL3CsHXUPZKLgXrM7nVaBWv_FrwUggQ0pshrMWVKD2Rw-9fvhDGb9hh1jDVcSBCjuWVxl0iT6Z0i0HYgAmezK01Le4ggsPpvKqWTQqKo3xdFOjfviaY1D8bCizeMU7XwS6_BFukIjb29GuKMGeWgUbBgREM9sRvfLh_T5tmJqq2DK5Pg6OiG4_LqxmWHDI4JMZA1JnKfu4xtEUb3lx3vy4p0mTTtxI7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه‌هایی در اردن و اربیل که آمریکایی‌ها فکر می‌کردند از آن خبر نداریم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461118" target="_blank">📅 18:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJQhShroPnYKobS2nrBe5xM64Sb6CwD8_EWraLvXhhd7GymTz7f0mrfWqClk1LrGUbDCylVvIUxPgdC0YqIXrwRAkm5gciG01dYQO5i-WaBHPBvN-gz8mvZ0584kx8ikerAafg0h1rzbr5TxBwpRIPU8iJ7hkjeCaQtv57GC4mBK-fLnawXvU8O_rZY8lapXfqzZNawvxqzy5gnn5SZre9CrPCWvLIQcrbzO2yvjcC80dx99yQ1LZLXYQs4340TgzxCksVMpNCcN-a6ANQ1-y_Nh2zqgVYJjMOI68N3qhYnIBYq1jPJN4gy9sv3SAw5OpVrhyMmzoIl1JLJ39HCLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانه‌ای که ۱۲۰ روز خالی بماند، مشمول مالیات سنگین می‌شود
🔹
براساس قانون، هر خانه‌ای که بیش از ۱۲۰ روز خالی بماند، مشمول مالیات بر خانه‌های خالی می‌شود؛ «سال اول ۶ برابر، سال دوم ۱۲ برابر و سال سوم به بعد ۱۸ برابر».
🔹
طی ماه‌های گذشته، با اتصال سامانۀ بانک…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461117" target="_blank">📅 18:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c8a3f97f.mp4?token=qModi0i53JtyOqv-Hpj52dRgmjadS_0ePwnDeHU7V-pQ3tIWQfISVpJpzQRefZVdstWQjk4K83nRgsnGAq0u6wt-_1rhN_5M9KZ4sUvjPfNO2dkiuwUU8UIO2RwEELEoEo1BQfPQn8Pl8yqQtQkDYedI3UDcB3CE1tmEvrolCQRSV_Eal5y-RoLNPE-LZ1bRkh9f7kYyV1NYXXNytNbrEt975e_Bv1dRobqJfbZjQ5fh5vMOAvOesF-ZTpOGTH3NpX7pW6WZgveJgxwu2a3G3oMhZM3BGOcM3_9W3z33aiEPFQD1aFr3ySynF12YIy8mtCh3yRVjlsIFK5NaioiSww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c8a3f97f.mp4?token=qModi0i53JtyOqv-Hpj52dRgmjadS_0ePwnDeHU7V-pQ3tIWQfISVpJpzQRefZVdstWQjk4K83nRgsnGAq0u6wt-_1rhN_5M9KZ4sUvjPfNO2dkiuwUU8UIO2RwEELEoEo1BQfPQn8Pl8yqQtQkDYedI3UDcB3CE1tmEvrolCQRSV_Eal5y-RoLNPE-LZ1bRkh9f7kYyV1NYXXNytNbrEt975e_Bv1dRobqJfbZjQ5fh5vMOAvOesF-ZTpOGTH3NpX7pW6WZgveJgxwu2a3G3oMhZM3BGOcM3_9W3z33aiEPFQD1aFr3ySynF12YIy8mtCh3yRVjlsIFK5NaioiSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر فقط می‌توانستید یک نفر را ساکت کنید او که بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461116" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkNEwztw3xMl2bMJyTtppIVZYvNRaTbSt9RUPFAtalB06qahn77a0dgqS8Bsn_BOS_2ZysM74W0hfMNKiA_KjCclBDIvF8r9_XXsBJBpZnL-Tsl28kW3zXyLQOMVX5CjAmgZTLO1COiYseK9zv2Rjc6egnGTKmTUbfKtLS0ZDpvsgocIHXjm-j78fj06KKpE8sOho7z9_-XOlDYQy2cugs1OCGwhsKNN_0xTzylUjUS88-U7alR38-Crz19ejE4trRXTWmCgDwsHJkAEhGm21SC1VQrOfqFFNOJz-Gp7VT-IXxz5Rr9McJznPIeYjavBoGP6BLGMtEEI9xJou33tlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمه گوشی، قسطی روی قبض همراه اول
🔹
همراه اول با راه‌اندازی سرویس «همراه بیمه»، امکان خرید اقساطی بیمه موبایل را بدون نیاز به چک و ضامن فراهم کرده است. مشترکان می‌توانند بیمه‌نامه گوشی خود را با سقف پوشش دلخواه تهیه و هزینه آن را در ۱۲ قسط بدون سود، از طریق قبض تلفن همراه پرداخت کنند.
🔹
فعال‌سازی این سرویس با ارسال عدد
۰
به سرشماره
۸۱۱۸
انجام می‌شود و مبلغ اقساط در صورتحساب با عنوان «خدمات دیجیتال» درج خواهد شد.
🔹
نکته مهم اینکه بدهی مربوط به این سرویس، باعث قطع میان‌دوره یا پایان‌دوره سیم‌کارت نمی‌شود.
http://mci.ir/-06YRG5
@mcinews</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/461115" target="_blank">📅 18:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | Moallem.ins</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n34NIeNRBfZSEAM99_Z5l8QUzz1QTaIK_bbTmrolFUAIzDEhloksqb45iRGEuxfE6kbcyAXvA0-ho1nXAXtZB6EdPcYeY0g_JVn8OBIcNiuxHnsk1jT3phOmXKnqtrDcFDv-glv9XLkCFpoo5K_nQd4F3JRipK0sFIcG8J2-UqGIwKVqJMcviZJJhyi0HUPbXSP2miS8QldkJza0Fwbc5SRJHoReYw2gCPshLHlXkWkjsLemLmaDVKFE6n9aKl9Jn4WlKGTbaMiA9oqNACC9AY8WOR3_hyN9754nbVSh39rn47WSLldW0n1uDiqo7I9CRTexdBjgepDZuONtgiuaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میدانی بیمه معلم در مناطق سیل‌زده
مازندران آغاز فوری ارزیابی خسارت و تسریع در پرداخت به سیل‌زده‌گان
🔹
در پی وقوع بارش‌های شدید و  طوفان‌های پیاپی و جاری‌شدن سیلاب در بخش‌هایی از استان مازندران، بیمه معلم ضمن ابراز همدردی عمیق با هم‌وطنان و آسیب‌دیدگان این حادثه، بلافاصله تیم‌های تخصصی ارزیابی خسارت خود را برای رسیدگی فوری به وضعیت بیمه‌گزاران به کانون‌های آسیب‌دیده اعزام کرد.
🔹
به گزارش روابط‌عمومی بیمه معلم، به‌دنبال ورود سامانه بارشی ناپایدار و وقوع طوفان‌ها و سیلاب‌های اخیر که منجر به آب‌گرفتگی معابر و خسارت به برخی از منازل مسکونی، واحدهای تجاری، مراکز آموزشی و زیرساخت‌های منطقه شد، بیمه معلم به‌عنوان بیمه‌گر پیشرو و حامی جامعه فرهنگیان و عموم شهروندان، با تشکیل فوری ستاد مدیریت بحران، اقدامات ویژه‌ای را جهت حمایت همه‌جانبه از آسیب‌دیدگان آغاز کرده است.
🔹
بر اساس این گزارش، با ابلاغ دستور ویژه مدیرعامل بیمه معلم به سرپرست استان مازندران، کلیه کارشناسان و تیم‌های ارزیاب خسارت بیمه معلم به حالت آماده‌باش کامل درآمده‌اند و عملیات پایش میدانی، بازدید از اماکن خسارت‌دیده و تشکیل پرونده‌های خسارت از نخستین ساعات پس از فروکش نسبی آب با جدیت در حال انجام است.
🔹
علیرضا بزرگمهر، مدیر مجتمع ساری بیمه معلم، با تشریح آخرین وضعیت اقدامات میدانی اظهار داشت: اولویت اساسی ما در این شرایط بحرانی، ایجاد امنیت‌خاطر و ایجاد آرامش در بیمه‌گزاران است تا ارزیابی و پرداخت خسارات در کوتاه‌ترین زمان ممکن صورت پذیرد و مبالغ غرامت به حساب حادثه‌دیدگان، مدارس و مراکز تحت پوشش واریز شود.
🔹
او افزود: بیمه معلم از تمامی دارندگان بیمه‌نامه‌های این شرکت که در اثر سیل و طوفان دچار خسارت شده‌اند خواهشمند است برای تسریع در اعزام کارشناس و تشکیل پرونده با مراجعه حضوری یا ارتباط تلفنی با شعبه سرپرستی و شبکه نمایندگی‌های بیمه معلم در سراسر استان مازندران اقدام کنند.
🔹
بیمه معلم در راستای تعهدات حرفه‌ای و ایفای رسالت مسئولیت اجتماعی خود، تا برآورد نهایی، تسویه کامل خسارات و بازگشت شرایط به حالت عادی، تمام‌قد در کنار مردم شریف مازندران و جامعه معزز فرهنگیان کشور خواهد بود.
#بیمه_معلم
#ارزیابی_خسارت
#سیل_مازندران
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/461114" target="_blank">📅 18:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/461113" target="_blank">📅 18:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f75710fa.mp4?token=Jy8VJMKr_-RqWW2MRZxVAcsD6qjW-I2lb5hmbpPYJ07iM31EKSXEtKo25aWquZGck1WcZI-D16T0wQz2WEov1DyTyprdD8WUuJun-lRaD3L7VmeoHFj0P218hVWGXf1_vO1y4nPLuKAkhr8kNrs59jH5_FPfdeW025_IdskcEsbBQMQloJWX4GheYsWZiQfsiSQYXQQ4QUzfoa9odbwMB_lBJHzYPMgU2YYWRUQ7-ZLcw_t89BvBg3BCtVDU9F-aVlLr0dxP1bmCtVSI8SASJ0e6IqNQ3tIZzDo_rNIwNPfkyILZEBMKtQzayjM7dx1AnWWRlg0-W74XYBBmLxNhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f75710fa.mp4?token=Jy8VJMKr_-RqWW2MRZxVAcsD6qjW-I2lb5hmbpPYJ07iM31EKSXEtKo25aWquZGck1WcZI-D16T0wQz2WEov1DyTyprdD8WUuJun-lRaD3L7VmeoHFj0P218hVWGXf1_vO1y4nPLuKAkhr8kNrs59jH5_FPfdeW025_IdskcEsbBQMQloJWX4GheYsWZiQfsiSQYXQQ4QUzfoa9odbwMB_lBJHzYPMgU2YYWRUQ7-ZLcw_t89BvBg3BCtVDU9F-aVlLr0dxP1bmCtVSI8SASJ0e6IqNQ3tIZzDo_rNIwNPfkyILZEBMKtQzayjM7dx1AnWWRlg0-W74XYBBmLxNhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار و قدرت بازدارندگی لازمه جلوگیری از تکرار حملات دشمن است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461112" target="_blank">📅 18:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۹.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/461111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۸.pdf</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461111" target="_blank">📅 18:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در ابها و پایگاه هوایی در خمیس مشیط در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461110" target="_blank">📅 18:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546c5b3993.mp4?token=nWnDTkKN6dAs07BnYiOx-f_7EjwD2oXy1Nze47aQcHyAw7NOTRbD6AedIapNa6qLFY1d8pRa9p-novCfC5nTX_6whpAPhtXXIrxqEpTY6VgCD5WQMPGcZf1D6ALhDlmBy0pG6TxpShHtUtba3zrXE13xckSCE1ts-WYXeVTatXjzyeIoFOox7MPfUASSrJ_4xj_TgprTccanMXyUenKs9aS80ObDUqxQRCG4j9Glsbt20pY6Av9m_1taNWZzXi54osVXMqD1TcLik-VttkiNWQmkzv3G5ZAYTVwGVJENhliumHcpQVCW6qhbOrArxomwekgsmihevTWim74RWzSEOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546c5b3993.mp4?token=nWnDTkKN6dAs07BnYiOx-f_7EjwD2oXy1Nze47aQcHyAw7NOTRbD6AedIapNa6qLFY1d8pRa9p-novCfC5nTX_6whpAPhtXXIrxqEpTY6VgCD5WQMPGcZf1D6ALhDlmBy0pG6TxpShHtUtba3zrXE13xckSCE1ts-WYXeVTatXjzyeIoFOox7MPfUASSrJ_4xj_TgprTccanMXyUenKs9aS80ObDUqxQRCG4j9Glsbt20pY6Av9m_1taNWZzXi54osVXMqD1TcLik-VttkiNWQmkzv3G5ZAYTVwGVJENhliumHcpQVCW6qhbOrArxomwekgsmihevTWim74RWzSEOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم آمریکا از پیروزی‌های خیالی ترامپ خسته شده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461109" target="_blank">📅 17:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امسال ۱۰ هزار دانشجو راهی عمره می‌شوند
🔹
معاون فرهنگی نهاد رهبری در دانشگاه‌ها: طی دو هفته آینده ثبت‌نام عمره دانشجویی آغاز می‌شود , سهمیه امسال به ۱۰ هزار نفر رسیده است.
🔹
نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها رایزنی‌هایی را برای افزایش تسهیلات وام عمره دانشجویی دنبال می‌کند؛ پیش‌بینی ما حداقل افزایش ۲ برابری وام است.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461108" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461107">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279caefb98.mp4?token=BpdykumtPCn7qzGaUJxtrfjrlAyL9aVjMYVVPE0MiCxDkSdGk1ELPXpH1bEav8G7DaT1D-hW9NPoiK8RoWs2IJbL1PgOi9XNY8NI1Rwr2JA8f7wauOZX4hLrk82y-AvaEom3d969tn1cR_fNLARUwakr0t2xoRt0fZ67dBLEe_WHxAJ1Sg1AuKrVhGC_WH5QC8ax1y0tvKZMDofkr4M5g-6L3kSifluUMD9xH2ccFrre1SLQ2A08XjZI5f1YSFnTea2TtnquAWDdvJIXsQ60fdjIxMFo-NhN4cgmu9ITyaBmwXIpL4DKHHgETvjkug6QByScnNW-sX_SIcDvhi3oMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279caefb98.mp4?token=BpdykumtPCn7qzGaUJxtrfjrlAyL9aVjMYVVPE0MiCxDkSdGk1ELPXpH1bEav8G7DaT1D-hW9NPoiK8RoWs2IJbL1PgOi9XNY8NI1Rwr2JA8f7wauOZX4hLrk82y-AvaEom3d969tn1cR_fNLARUwakr0t2xoRt0fZ67dBLEe_WHxAJ1Sg1AuKrVhGC_WH5QC8ax1y0tvKZMDofkr4M5g-6L3kSifluUMD9xH2ccFrre1SLQ2A08XjZI5f1YSFnTea2TtnquAWDdvJIXsQ60fdjIxMFo-NhN4cgmu9ITyaBmwXIpL4DKHHgETvjkug6QByScnNW-sX_SIcDvhi3oMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکنیک مذاکره‌ای آمریکایی‌ها برای جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461107" target="_blank">📅 17:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461106">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-rHScSgvfV1nUW1wDhSI-zZ3piNi_QwiSn0bq6LC0QNyCl8L9Xz5Aglbucnba91d4ihEXrBq_6CV3SWrIx-S6DtibgcTfU3TnioFyERYShNA3VcAmwDZyptrkvPegQkuot_ivBm7ONKoN3KoEYOlcL_muLMDZR76qDk0x5XoK-HVRkV27qcFbhaIpMiOvHKoUdERdzB2ngHrAuwkMmnXTCC4M2-5OdKmo5UnGOYWvcqN7FJ4pXYI-wnWlh5UiFal0BER4tH_6tDYqlZW0TYelaHOsL8G6X-ZmCntOt2sRUsWovU4Q_P6J7HjEhvoyNIsUjwTPTUMVp7Of8UeNNEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف هزار تُن فرآوردهٔ نفتی احتکارشده در چهارمحال‌وبختیاری
🔹
فرمانده انتظامی چهارمحال‌وبختیاری: ۱۰۰۰ تن فرآوردهٔ نفتی به‌ارزش ۲۵ میلیارد تومان در شهرستان سامان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461106" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
انفجار انبار تسلیحات در شمال غرب سوریه؛ دست‌کم ۱۴ نفر کشته شدند
🔹
در پی انفجار یک انبار سلاح و مهمات در شمال غرب سوریه، دست‌کم ۱۴ نفر کشته و ۱۱ نفر دیگر زخمی شدند.
🔹
روزنامه واشنگتن‌پست به نقل از رسانه‌ دولتی سوریه نوشت که این انفجار امروز در نزدیکی شهر
سرمدا
در استان ادلب رخ داده است. علت وقوع انفجار هنوز مشخص نشده و تحقیقات درباره این حادثه ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461104" target="_blank">📅 17:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انهدام چهارمین پهپاد سعودی در ۲۴ ساعت گذشته توسط یمنی‌ها
🔹
نیروهای مسلح یمن: یک پهپاد شناسایی تهاجمی CH4 متعلق به دشمن سعودی در استان الجوف سرنگون شد.
🔹
این دومین پهپاد از همین نوع است که در ۱۲ ساعت گذشته و چهارمین پهپاد در ۲۴ ساعت گذشته است که توسط نیروهای…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461103" target="_blank">📅 16:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
روایت صیادان ایرانی از وضعیت تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461102" target="_blank">📅 16:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b202f4951.mp4?token=JNmT9jxnGxmT9HYb3VSR22WTprGRj-QaBLnJVeJTka6tVSR5YFWQWzXx6TNTdn6USwgF_WFaahW2HDvn3Bd35PMD2lbhKpiOn-ZT1h9Uul4K0x3pMzSYJXQ2JUoOFNfBV7v1tvO5sa2yOa8LlF887nH_8wenhdpVJwB7Jv_tsZmhEWwjlh5yuGcOpLsMhl7U7_ox-tN73ngiG_MVCFkFpFlSLu2PC-XFtuUmwTEnxDBZ9f9bqvt8YiFe1hi_G-CzeuhOkQ84Sm_gTfvU4PUIHSnLFdKGeB_fYRZ3kG_mi-RqkgQGLYdt9bCNXYCZvKP6p9B_Gg-vW-jVFQJ_AEiCVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b202f4951.mp4?token=JNmT9jxnGxmT9HYb3VSR22WTprGRj-QaBLnJVeJTka6tVSR5YFWQWzXx6TNTdn6USwgF_WFaahW2HDvn3Bd35PMD2lbhKpiOn-ZT1h9Uul4K0x3pMzSYJXQ2JUoOFNfBV7v1tvO5sa2yOa8LlF887nH_8wenhdpVJwB7Jv_tsZmhEWwjlh5yuGcOpLsMhl7U7_ox-tN73ngiG_MVCFkFpFlSLu2PC-XFtuUmwTEnxDBZ9f9bqvt8YiFe1hi_G-CzeuhOkQ84Sm_gTfvU4PUIHSnLFdKGeB_fYRZ3kG_mi-RqkgQGLYdt9bCNXYCZvKP6p9B_Gg-vW-jVFQJ_AEiCVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده مجلس: دستگاه‌های نظارتی به بحث ارز تخصیص یافته به مونتاژکارها و خودروسازها ورود کنند
🔹
طی پنج سال ۳۰ میلیارد دلار ارز به مونتاژکاران خودرو داده شده که سهم مدیران‌خودرو ۶ میلیارد دلار، کرمان‌موتور ۲.۸میلارد دلار، بهمن‌موتور ۱.۸ میلیارد دلار و باقی شرکت‌ها زیر یک میلیارد دلار بوده است.
🔹
ارز را دادیم و خودرو را دوبرابر تحویل گرفتیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461101" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
بازار گران‌فروشان لوازم‌التحریر در آستانهٔ مهر گرم شد   @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461100" target="_blank">📅 16:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461099">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0329723d7d.mp4?token=Uw3vZavUv_OQV9obmnSMQ3HzoKc1fjs6_FjZ-3gUF0yMdRW3WBDIlN3z_j2GE7QytkinCPoEMrR8kvCSvwOKQUooI2Tni1QOLn-YcRQNsAeKD_4tQKIM_y5VGT0AlTXi6V6gvJSfRXGS0vMxJy20g4xpIvc2uGMue4shKtRVroHqps4NX9bl3PD8YucO2wg6X_q3JL4NrmBXqGadZWWGvOBpB8IeUCdbjLDEWlZBuEoJQL4UNCAqRUMCqdgbsVGq1-xx9LDDdQkUpzjihDcblgp4thCjRzUocsxIymQNy0ppnKSD-wx7kzg6kqJ_n_4u4gsnnWpk8agooKqfcfymPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0329723d7d.mp4?token=Uw3vZavUv_OQV9obmnSMQ3HzoKc1fjs6_FjZ-3gUF0yMdRW3WBDIlN3z_j2GE7QytkinCPoEMrR8kvCSvwOKQUooI2Tni1QOLn-YcRQNsAeKD_4tQKIM_y5VGT0AlTXi6V6gvJSfRXGS0vMxJy20g4xpIvc2uGMue4shKtRVroHqps4NX9bl3PD8YucO2wg6X_q3JL4NrmBXqGadZWWGvOBpB8IeUCdbjLDEWlZBuEoJQL4UNCAqRUMCqdgbsVGq1-xx9LDDdQkUpzjihDcblgp4thCjRzUocsxIymQNy0ppnKSD-wx7kzg6kqJ_n_4u4gsnnWpk8agooKqfcfymPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶۸ بار حمله به یک پایگاه؛ چرا العدید مهم بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461099" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461098">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciJe5CIVE9CFJ6qwA5u3SSPO5TQ7-zh_mH9qabQDP8TRB_18Vo4NJdDAjtSIHoiphC7fGUqiEXOkiJy1UdbRYSBuEdWFaI8hlfBHvNl4GIh0i83MC_HEzpZVeHef4BabIJLYf21iluPa2aM9G-u0Ytvw2HolhKbuHVw_FprWYQrfv4EjE1pf0SLOSjw7phu4jHVR4rXa1w50zhcZDjxngbGAvLxe33RnQRYBKSh8YWExPOs_KRh4olePPB9z-EIodfqDd70HHh30pO-G4dwNaJHe2x1DDiiGf6DlL-avPAyzzh5ZuQXykyRyujYtPszId8KnaF3boHVADboa0Wl0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  تلاش آمریکا برای کنترل روایت در ماجرای شکار یک زهپاد توسط سپاه
🔹
یک مقام آمریکایی به رویترز گفته که یک زیردریایی نظامی آمریکا «بیشتر از یک روز قبل» هنگام فعالیت در زیر آب با یک نقص فنی مواجه شد.
🔹
وی که به شرط عدم افشای نام با این رسانه گفت‌وگو کرده،…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461098" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f36b2c83.mp4?token=cUfclegIY09P1gknuXdffJwKur0deciaiBTfKlzBj1bNjGSNqpqXUFDef626zHA3Qmu2tA4F1BosKOM74krjmGWRvzinV6cZ-hzquoW1onE3ukGfAIbT-jjjqiBWxeQJfboJ71EBi0AynRjvqspnkOxtuz-NYSO4dWYzr0knEvUemb6U_OXJgEJabKzw0LW9gQdkrkcbHSzhgdhUoHCnEPup6UWIcdhJqcJMuUXZM1S-J_gC3hOs9usmf5SCKsXAiwAwzHHDaiyiKW6zYFIrrz-76_SR-cLYtBI0E8eCRsbxcMjA-rqZfju-AeJS-Uyq169f-YZS0gNtu1AW8Fhk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f36b2c83.mp4?token=cUfclegIY09P1gknuXdffJwKur0deciaiBTfKlzBj1bNjGSNqpqXUFDef626zHA3Qmu2tA4F1BosKOM74krjmGWRvzinV6cZ-hzquoW1onE3ukGfAIbT-jjjqiBWxeQJfboJ71EBi0AynRjvqspnkOxtuz-NYSO4dWYzr0knEvUemb6U_OXJgEJabKzw0LW9gQdkrkcbHSzhgdhUoHCnEPup6UWIcdhJqcJMuUXZM1S-J_gC3hOs9usmf5SCKsXAiwAwzHHDaiyiKW6zYFIrrz-76_SR-cLYtBI0E8eCRsbxcMjA-rqZfju-AeJS-Uyq169f-YZS0gNtu1AW8Fhk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نفت، صنعتی که بدون وقفه در کشور ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461097" target="_blank">📅 15:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461096">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzogmJcmHhdMHLBLvZ6EIzGLJL2OKfUaaAR3oVHR8RuWMJ0p6z-oU-ItlIRpxUfJlhkxlIjVmHZ6bgfpQsZqz2OyfUAtigucGfvgU_ICrekveLyl0elchiOpivxg0c5EUY0ZR4HwNbb6yfocs0RPBysIhf1qy0-DdHpMpE6E8a_wx7n3LntsfjnMMCpgtgkQh38BgE9ARQiMcjv6LUpl80QyoqvJ4s6n6kLruKZpXo_uichn86Dq3Ywz45vL8LjpD1P9bvfS_mQW83Fqmxon57BU94KRkItye5J0fGnHLOleAW3_C61tQiJheTieSXM0Skae61plbCzoMtOMD5Tt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
🔹
جنگ تحمیلی با بزرگ‌ترین قدرت‌های ظاهری جهان در مقاطعی به‌پایان رسیده، اما ماهیت جنگ همچنان ادامه دارد.
🔹
این جنگ برای اولین‌بار، آسیب‌های راهبردی را مستقیماً به خود آمریکا منتقل کرده و معادلات امنیتی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461096" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtsAPGWlc0unsfxU0pfuJ4_ylV7xCTNw8STFPqXlqOQBWMtWdDL99WzW0ruYAe7CCYj2kmcJShuah3i-FJPvRbeC_JENHxPXqzgI87PYJ4LqDi5d0cFpR7D1vD1koA12ZzX_W3DEQG-Dm7h0ROa5kQDqKi2h-7SFlL3XLtbYfXQpSJNTD6KZ7GKM94Gka7FxIbiPEk_syLaCnLkGXjQj4S6WXP-hgfT06dgSp73KnFNdAon6TVFohuwCc_7FW6p2p9SP3psGTGivWCCjwTvYROYFdR0EcU-OPIwpLt7KFLD_UXezQPLe3W1cNtR8jWXJAE3ipgzFcBiV6QEanHfAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش‌ها از هدف‌قرار‌گرفتن چندین کشتی در خلیج فارس
🔹
سازمان تجارت دریایی انگلیس: چند کشتی تجاری در شمال خلیج فارس و دریای عمان در جریان فعالیت‌های نظامی منطقه هدف شلیک قرار گرفته و از کار افتاده‌اند.
🔹
همچنین یک شناور لنگرانداخته در ۲۴ مایل دریایی شمال غربی…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461095" target="_blank">📅 15:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7391170a.mp4?token=uWHsxYEvcsj1J1iVxkqxAx-8Dh7SRUK0GaojpP1Vdf2jf4p22VLnCyhQo_Ay2XpRcieyDkJ7te7RWYvUnJNx9t8BS02GGWKbzoahuutdphluO3WabNgD4K2hl7QCFUlCE5VHyRZH3xX5wYvKqwocvASqrXCcygOx6GxYZlOZsGgPX-LhouCudkTSwdhDX64tXC3iii2ctJy21THxbo3aGxck4vQbOYbcu99fkHo1A7aOJViFyyD-4WhK5gYWYEkTd-WHxSc1Lib6uAasERC3vHQ28YP4p9kQrJOl2-sw9GLXqNpCMLrgjs2IrbuhffKG6CnnoVOhCAYVwTiGKkyT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7391170a.mp4?token=uWHsxYEvcsj1J1iVxkqxAx-8Dh7SRUK0GaojpP1Vdf2jf4p22VLnCyhQo_Ay2XpRcieyDkJ7te7RWYvUnJNx9t8BS02GGWKbzoahuutdphluO3WabNgD4K2hl7QCFUlCE5VHyRZH3xX5wYvKqwocvASqrXCcygOx6GxYZlOZsGgPX-LhouCudkTSwdhDX64tXC3iii2ctJy21THxbo3aGxck4vQbOYbcu99fkHo1A7aOJViFyyD-4WhK5gYWYEkTd-WHxSc1Lib6uAasERC3vHQ28YP4p9kQrJOl2-sw9GLXqNpCMLrgjs2IrbuhffKG6CnnoVOhCAYVwTiGKkyT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشرفت ۹۷ درصدی بخشی‌از جادهٔ الموت-قزوین-تنکابن
🔸
این طرح با طول ۱۶۴ کیلومتر، زمان سفر به شمال کشور را نصف می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461094" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fe26b148.mp4?token=On4e5twa0FLTBQQbPG2rwsZ0xuHjJeB1D1a5GOsD0GUak4X7PutvIB3rZk1Z9dPIlxeXxtE8JDgkHF9I_vX32Wu6QVRycbePZsGVADEOeXV5srgEm-IEeLVoxWZMsXvlhlEkox3YQpbX5SL6XVLkqxLgQsmZMFFoJOeYIahXaUt7i3rvdz-EA5lWjZYLQwSXjXYb2luF-kmLODAky-lg6QeAfJD1wN17y_3lKOfAH7obPB36LLIhsc8pWrQckKknM8efx4oAnClXOMaCOu6zA95IAzZckxDcW9JqB-ouDWamocrziKiiLSKjXspkcHa8x1WWoGqfvK4WPXKUiTtZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fe26b148.mp4?token=On4e5twa0FLTBQQbPG2rwsZ0xuHjJeB1D1a5GOsD0GUak4X7PutvIB3rZk1Z9dPIlxeXxtE8JDgkHF9I_vX32Wu6QVRycbePZsGVADEOeXV5srgEm-IEeLVoxWZMsXvlhlEkox3YQpbX5SL6XVLkqxLgQsmZMFFoJOeYIahXaUt7i3rvdz-EA5lWjZYLQwSXjXYb2luF-kmLODAky-lg6QeAfJD1wN17y_3lKOfAH7obPB36LLIhsc8pWrQckKknM8efx4oAnClXOMaCOu6zA95IAzZckxDcW9JqB-ouDWamocrziKiiLSKjXspkcHa8x1WWoGqfvK4WPXKUiTtZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری طرح میدان گازی پارس شمالی: به‌اندازهٔ ۲ فاز پارس جنوبی از ۱۴ چاه میدان گازی پارس شمالی، گاز تولید می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461093" target="_blank">📅 15:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2b194c0e.mp4?token=jk4ljaSSi_eL1HSWm9t9Lj_jGSCmLNkAxUSViSscGLOebSFXLdyNBeKQA7FZnsbI5XGQ7asf643SHs6R2GLG9_xPXeoebmm1XBKKadOSrp24L4XhdMx_MFXXQAl11duWxsDbs2DgmPY9CT4vHKCSm4H73gRzy5kHJc6PFg6awBxAzK7-gHQrdG-5aPgC5QprFIQMqPX2fq6Tj-HiX9oD-G7KRxX74VAGKOCvQaAHMYX8kTXLt15QCMyS4cVyvr9kHlc9UdFxkfz0DKQO2-E09AFgq6qR_-3TL_awNQ4EfcY-Phher6LsQ0qCcZR6CENSCOwOI2oZEcJ4_8HFlBbIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2b194c0e.mp4?token=jk4ljaSSi_eL1HSWm9t9Lj_jGSCmLNkAxUSViSscGLOebSFXLdyNBeKQA7FZnsbI5XGQ7asf643SHs6R2GLG9_xPXeoebmm1XBKKadOSrp24L4XhdMx_MFXXQAl11duWxsDbs2DgmPY9CT4vHKCSm4H73gRzy5kHJc6PFg6awBxAzK7-gHQrdG-5aPgC5QprFIQMqPX2fq6Tj-HiX9oD-G7KRxX74VAGKOCvQaAHMYX8kTXLt15QCMyS4cVyvr9kHlc9UdFxkfz0DKQO2-E09AFgq6qR_-3TL_awNQ4EfcY-Phher6LsQ0qCcZR6CENSCOwOI2oZEcJ4_8HFlBbIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار گران‌فروشان لوازم‌التحریر در آستانهٔ مهر گرم شد
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461092" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f256a249.mp4?token=bqx3-xAFAhJ8aT3VhP92XZ6wiB4uQB7PrIEl4sQOtkJ9gAZZ-QmRpXPCy99LJfFvOb2X3k-7Z4e0zzvLAvJBy07obEwN75CLYhqjsTa1TahZTrbcTvEX-lHNyDMxgn8Ls0Jx60FwKNY48mIkuJABy_IDBNRkXKEGdKe3seZcAfPt9jdQ-jRlOapkuA6j3G7V4z9Lo50JueXQSU_C9Qe4E7ZAIea8AAMEHTMl52HFAqVL74zJs4h85sBC9PFg-kY241Od0YLipJ2XFL-lVMNprUSRsJpq-ya-knt66ObYtD5xj1jwQMg9yxrq9PtPoUO5U8qBJQz6YidqyPRGdCN3nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f256a249.mp4?token=bqx3-xAFAhJ8aT3VhP92XZ6wiB4uQB7PrIEl4sQOtkJ9gAZZ-QmRpXPCy99LJfFvOb2X3k-7Z4e0zzvLAvJBy07obEwN75CLYhqjsTa1TahZTrbcTvEX-lHNyDMxgn8Ls0Jx60FwKNY48mIkuJABy_IDBNRkXKEGdKe3seZcAfPt9jdQ-jRlOapkuA6j3G7V4z9Lo50JueXQSU_C9Qe4E7ZAIea8AAMEHTMl52HFAqVL74zJs4h85sBC9PFg-kY241Od0YLipJ2XFL-lVMNprUSRsJpq-ya-knt66ObYtD5xj1jwQMg9yxrq9PtPoUO5U8qBJQz6YidqyPRGdCN3nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب گستردهٔ شکار زیردریایی آمریکا توسط ایران در رسانه‌های دنیا
🔹
کارولوسکی، تحلیل‌گر آمریکایی، شکار این زیردریایی پیشرفته را تحقیر آمریکا دانست.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461091" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28sS-a_ooC6sKffZtrnGo5TjKMd68jL3msycW2j5zCmYNrJh3i-BRDVGvTpUmv-khFIDNHAIgHBU_Cib8zQp8x6VudK5JIav-Us9p_KwbGJbsu8POIJMp5gLT6zeQJWkO7QlLP4B6gsDzldNe_qTE9o4kQW929HWP45F9RTXwq_oezYcTXXP-WryuzTI2DTivDy5YEEi7pqd8IfUsGvdNKKwjPRyiwPlAB2zfNcBG9AK2tXyoLrMBySUAAJNwZFpWtRwNVWrs87Co1s_oPOMhEOav2PE_oDyzZvc61MsyJZRy5GWDSKBgJLMx561Knu1bM1yF-beoojsYFv_fnx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
🔹
جنگ تحمیلی با بزرگ‌ترین قدرت‌های ظاهری جهان در مقاطعی به‌پایان رسیده، اما ماهیت جنگ همچنان ادامه دارد.
🔹
این جنگ برای اولین‌بار، آسیب‌های راهبردی را مستقیماً به خود آمریکا منتقل کرده و معادلات امنیتی و اقتصادی این کشور را تحت تأثیر قرار داده است.
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد، ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند، محاصرهٔ یمن پایان یابد، ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
🔹
به‌جایی رسیده‌ایم که اگر دشمن ۲ یا ۳ هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461090" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461089">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5910e1c.mp4?token=ssN87vkZNl0icDGd7Hwm2JlwMe0tE2q1Z-WJ9DT_92E3v0LsRUkeYCwdO24XkWibBYwKgdlVg_Ey_V3rFO1BVA5lnUKHh9mq0d6Fclfq8h4y6qByH2_M8BbFGOHKIfYnU6QKBCqt81lIg8qO_yMnd3j51ubT4cbvIajnvWbeDk0U4h-27O4owdIjXptAurIixeoJ554ioQZL6LnQ2BUyKhObp5VWZen0AM-d2cW2ly1j6mh0dU9_TwA49JeTljt4pHIBNcfJMzEtfPCO0B0GKQouHpZ3_RKhvZzhgOTI-9HH5JrxbBPbimsU6xfr0DONI54HDA3FMxKrMPNYEEpszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5910e1c.mp4?token=ssN87vkZNl0icDGd7Hwm2JlwMe0tE2q1Z-WJ9DT_92E3v0LsRUkeYCwdO24XkWibBYwKgdlVg_Ey_V3rFO1BVA5lnUKHh9mq0d6Fclfq8h4y6qByH2_M8BbFGOHKIfYnU6QKBCqt81lIg8qO_yMnd3j51ubT4cbvIajnvWbeDk0U4h-27O4owdIjXptAurIixeoJ554ioQZL6LnQ2BUyKhObp5VWZen0AM-d2cW2ly1j6mh0dU9_TwA49JeTljt4pHIBNcfJMzEtfPCO0B0GKQouHpZ3_RKhvZzhgOTI-9HH5JrxbBPbimsU6xfr0DONI54HDA3FMxKrMPNYEEpszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461089" target="_blank">📅 14:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCSNu01Lc-PSafPyAqpecbNP6Aa7ROIfWj2CFMTGH7A1QcOZhtyUGYu5Cxzkmv6-RvD9nh_72LvMEI6iiTtTG06jCKbdj4wwsg55QO0iGA6pFuzpARY98xNimSnwsaGLcy5_PGIVbvdvNpFFYYk2iD4Jat4mRNCdNKADxdrVu6HscgvGKyXkw5V7irfA50dwzBNK3zyqIIQk4oO1dwXeHMBinWm7cCJom6AgbQ-9r-agXio7sFmixwrErdJRNYkJpKZ4_p3A3rNTBMdaKL4iXKtcELWD-WSpBkxi7PKJ8RKn16KHvQL7SnDkE0i0IPgrwgsAjNsCrBdMxWIbWkR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گویندگی؛ هنر نفس‌ها و مکث‌ها
مهدیقلی، گوینده و مجری تلویزیون: «گویندگی فقط صدای خوب نیست؛ صدای کنترل‌شده‌ای است که با معنا و موقعیت هماهنگ شود.»
گوینده کسی است که نفس‌هایش را می‌شناسد، مکث‌ها را اندازه می‌گیرد و می‌داند هر کلمه را با چه انرژی ادا کند.
انتخاب لحن، مثل قاب‌بندی در عکاسی است؛ بعضی کلمات را برجسته می‌کنی و بعضی را آرام می‌گویی تا مفهوم درست به گوش برسد.
📢
دانشکده رسانه خبرگزاری فارس، تو را به دنیای حرفه‌ای گویندگی می‌برد.
آموزش همراه با تجربه‌ی عملی در باشگاه خبرنگاران «توانا».
🔹
بدون کنکور | مدرک معتبر | اساتید باتجربه | معرفی به بازار کار
⚠️
ظرفیت محدود
📲
عدد ۱۴ را به ۵۰۰۰۱۰۱۴ ارسال کن
🌐
یا ثبت‌نام در:
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461088" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cebd3b25.mp4?token=KTZKC-06NifEq29LT6oS0McBAebiBsotkuaXo_M_82XrMDn0BanTdnU0wQ4eVRydTYgax58V1oxipUvbTX3TQg--KTkO5uv6iaLRYdLCjLP_fLt8jOC64Ayk2ArcdWZomE-c5Hd4oiQ9ci9lhCEFgmUT6j0RCrAPG8gNjK2TrWGvrR2X1_aQZiGcfJa8AO1iUjvL4ocWdqX02wcXRqq8q7Y0PGuPNLtOy9lgZd-YAl9PhSE44UF6c8l8kPMZ7YKTX5ZzPL9JSe8Cpt0iBEQNZ77zdIhzR-dgEe9QcVR0_r05l_Bg_QwORaurRTsGNL9wFVCG13fPBVC92PQHLfbvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cebd3b25.mp4?token=KTZKC-06NifEq29LT6oS0McBAebiBsotkuaXo_M_82XrMDn0BanTdnU0wQ4eVRydTYgax58V1oxipUvbTX3TQg--KTkO5uv6iaLRYdLCjLP_fLt8jOC64Ayk2ArcdWZomE-c5Hd4oiQ9ci9lhCEFgmUT6j0RCrAPG8gNjK2TrWGvrR2X1_aQZiGcfJa8AO1iUjvL4ocWdqX02wcXRqq8q7Y0PGuPNLtOy9lgZd-YAl9PhSE44UF6c8l8kPMZ7YKTX5ZzPL9JSe8Cpt0iBEQNZ77zdIhzR-dgEe9QcVR0_r05l_Bg_QwORaurRTsGNL9wFVCG13fPBVC92PQHLfbvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
🔹
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461087" target="_blank">📅 14:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lX_cF-ErM-khMGrg__n0x7hPLiFSJGZ5E8xzq59Kn3D7PO-GVOSpmPw16tYTf8EdpmSvtfCPZ3yLXP-v5uf2LEP7T4g75SAxt2AxEO5gQPgNRK5HdLW5RRbyRiXQSqnEi7Q6lUyS1Gtm9BcKgsRla6KY7bk5r9w3rJD-PdZfJjEbzon7N-pLVX4GNvGLVD-vcUiKGDi6GZ7M9tImc3UxGVLFWvXvT4GHp0R7Q-iN5RZlL-2mhzXHkd92fcZ-IolT_N85_lF8I-04tDgUHSWx8iM7JgBppXr19y3HFnOic3Y7wk_-N66y4vPZWR47Szmjj0O4SqXD16oXwjw_T0SeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FaX1_Us3G_7Nuw6-EseG1mFw9_U31Wx-WGkYdDNLX_-RHlgjPE3ij8kT2OjGFreSYDn0saKWAdIuBi6zh0swsxooqirt49zy2M8HEYHWmzawMEK7L8m0-AyBfuomAygOXo5l-Iz3uw4fTqxO7uSI4d6xsdoyrgNWpdGVeeC_RK8jKhR92SR_TUwUPgu3cknVyD54xmz7JOkrqPaaIHZmh1gyCpwuQYjcOSPnbA-9PnwKa0ZrX48AmabUwqherEk8zc53lo3gUeoPeTeWJ9PVSfh9Q-QQOL-OON8zdzg4WOEq_NdbVXYPN-sGrr5tyhJCKuVLNoZkTXBFSRQBi4pwXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با کره‌جنوبی روابط خوبی داشته‌ایم اما هر مشارکتی در اقدامات تجاوزکارانهٔ آمریکا برابر با هم‌دستی در تجاوز خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461085" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrO8iXxOyWNbmhl8vh6jzb4Xc5PJqIoZSfWpTkzGCCvbCYaJYnNIXixLCveDr_nGhVAo2A2lxG2pPNuBofKsTszI6ye04V_Wc-pW1i6VcIQywgE893H9ScTUMpi26sEThWcY_fF3KRGy8RpQQWelRhjllxCyz4ahItEkx3P3-OzKorA4KMFi2wsm-Cai9PjxHdCIQnxKckBNWMKL9CK37MLUFHEFvGAFAZUGP97JS00-uDF2NocxV5TxGWaQY7ykfR-4N0GW4ZVg8NKevUYV9z2rpYyIW0B7na-a_neAQ2C7OY1OYpyhUVsRZLNz1wRoc3AyJdvEYTi4SfGu1prp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نرخ سوم بنزین رسما ۱۰ هزار تومان شد
🔸
از راس ساعت ۰۰:۰۰ بامداد ۱۷ شهریور، نرخ سوخت سهمیۀ جایگاه‌ها از ۵ هزار تومان به ۱۰ هزار تومان افزایش یافت.
🔹
نرخ ۱۵۰۰ تومانی سهمیۀ اول و ۳۰۰۰ تومانی سهمیۀ دوم تغییر نکرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461084" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6mqYma6l-gSUi9P-Ys4tR30P2rzTo9KvSoWN5DNfxiHcvy1gTFuRkGlgNM-XAZlQQhKjvIIHr_65xBGY1zcbjX-yIuiPjTJ_6GAcGs7SXKp23eEQMQ2s5tBN_BaH8nlZ5rBKPh_Dil7ohdM3dP6FfYAZR_r8c-9Q5rizck0CC1frRG-wyxqiyxY1sfJVqEj_oEtUnR9mg65ARqrzKl9YmQ62Jrv1lNfhnxcvdeN3gsCww8NBRJEKAx7iLIha6PKM564FuUVejCS5_5aVdL1VKGeDgvpVmfcDSpG7IeAp1kgOvoK5_2GCH5Xv0zI7aQA5Tn3gx7Lklk7urM_m9cF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461083" target="_blank">📅 14:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ccdbf695.mp4?token=gxk_ggnVi59MEKBlry18orkcmDztGwsAYupLf22h7xGB4tN9DaPB2cbIj5kHE7i6D-82NvEy-nwzh4Jj1qFHf4qj-ifwZtrvdTPaoywHLMMtx8K-4z-dsgavWk-pO71RyaMRJImjQyUs7DVE0-8lVLZh6mCs22-rJtQuAVX1xv9LVplZ8xfp0w20cS430GsE1TC2rrwz_Gfhl0pPx-j-tqlOnOAKz6xc2DYIWi2frIeaFnM_p4QFSHUzzVL9k4Ba3NkU4sXlt9w_9_hKPTIQXKQWvukNyqWVh1LzEwmxizozZVt2i_OljyI2sIlwszSdazm3s4UfrMZ_KOgzShEdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ccdbf695.mp4?token=gxk_ggnVi59MEKBlry18orkcmDztGwsAYupLf22h7xGB4tN9DaPB2cbIj5kHE7i6D-82NvEy-nwzh4Jj1qFHf4qj-ifwZtrvdTPaoywHLMMtx8K-4z-dsgavWk-pO71RyaMRJImjQyUs7DVE0-8lVLZh6mCs22-rJtQuAVX1xv9LVplZ8xfp0w20cS430GsE1TC2rrwz_Gfhl0pPx-j-tqlOnOAKz6xc2DYIWi2frIeaFnM_p4QFSHUzzVL9k4Ba3NkU4sXlt9w_9_hKPTIQXKQWvukNyqWVh1LzEwmxizozZVt2i_OljyI2sIlwszSdazm3s4UfrMZ_KOgzShEdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالیِ مردم از شکار زیردریایی آمریکا توسط سپاه  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461082" target="_blank">📅 13:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سپاه استان تهران: صدایی که دقایقی پیش در ملارد شنیده شد، ناشی‌از خنثی‌سازی مهمات بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461081" target="_blank">📅 13:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پاداش جام جهانی برای هیئت‌رئیسه گران تمام شد
خبری از نام تاج نیست
🔹
«شکایت سازمان بازرسی از برخی مدیران فدراسیون فوتبال ظاهراً در دادسرا منجر به صدور کیفرخواست شده و این تصمیم قضایی مقدماتی است». رئیس دپارتمان حقوقی فدراسیون این را چهارشنبه ظهر گفته.
🔹
برخی فعالان رسانه چهارشنبه مدعی شده‌اند در «پرونده فساد فوتبال» نام مهدی تاج، رئیس فدراسیون هم در این کیفرخواست آمده.
🔹
بااین‌حال پیگیری خبرنگار فارس نشان می‌دهد موضوع شکایت سازمان بازرسی کل کشور پاداش ۲۰ هزاردلاری به اعضای هیئت‌رئیسه فدراسیون پس از برد برابر ولز در جام جهانی ۲۰۲۲ قطر است و مهدی تاج، منصور قنبرزاده، احمدرضا براتی، بهرام رضاییان و میرشاد ماجدی از دریافت این مبلغ خودداری کردند یا همان زمان آن را برگرداندند
🔹
مهدی محمد نبی، طهمورث حیدری، احسان اصولی و خداداد افشاریان دیگر اعضای هیئت‌رئیسه در آن زمان بودند.
🔹
حالا رئیس دپارتمان حقوقی فدراسیون مدعی شده تشریفات اداری پرداخت پاداش در آن زمان به‌دقت انجام شد. دیوان محاسبات این موضوع را بررسی کرده و اقناع شده و تخلفی را احراز نکرده است.
@Sportfars</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461080" target="_blank">📅 13:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-dhLPVetX12KraZ0hn-IUfFB9GPUZZVQr2WDFyq7bpYF-Sdisozm_Iq0d2h4Z8xxyOMXo0vp6eHptykuVF1jwgEhEQLF2H4BwowHrMz8p9FGSrFwoP9ledIjrTRFGQNEye9TLZ-2z0Z9rJJpQtUw2NHW-kEDucEtQ7xz0AqT50MWSZBfQUypUuHZqTPK1urhVO3ZrOrtEyEk6eW2sEpuZAdgCf_zWjKa3ZRi6uAhseomIGWIHqv9SBKcvFSZIlDg1wZYsOu0exG-d0tf6oM87WKrAG4kFRHqAPA2SBosK6LDlyh_mEGcnqHCCiUyV0Z8sIenh7nvvGnjpYQ9vsIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی شاگردان پیاتزا مقابل چشم‌بادامی‌ها
🔹
تیم ملی والیبال کشورمان در آخرین مسابقهٔ مرحلهٔ گروهی مسابقات قهرمانی آسیا با نتیجه ۳ بر یک مقابل چین به برتری رسید و به‌عنوان صدرنشین راهی مرحلهٔ حذفی شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461079" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrazUUi3DJdQqEJGu7O8oPy4Y7t3lwKdiPzkrnGDLDy7zkDLNz-nKEh1He_hFhKVqR8QlWOj6R6jr0zuIQCuk8e0ksoUeWHSnMKX0xcw5OywRQzxHgI9_nVnUmBIZWD4rBo43abJpqNP-FpRpQeL4xDSmlW_12dd2pwlqPG4CfcihczTk2nrcIMLvkAifWWP-CgMVkOcT-RhzRjRuikC_a-lkqJg9GFVsGGRlF8pzpASN0lNEngsZV8MHr9iSJELE4RSG9c8iSN3ymYzdvWqJFr0YWc3ZNdaaf1IaL2imBefO_GGn9r6Px9Ubk0bykDPb5AFydT9pk4mT4fi8p8vxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش‌ها از هدف‌قرار‌گرفتن چندین کشتی در خلیج فارس
🔹
سازمان تجارت دریایی انگلیس: چند کشتی تجاری در شمال خلیج فارس و دریای عمان در جریان فعالیت‌های نظامی منطقه هدف شلیک قرار گرفته و از کار افتاده‌اند.
🔹
همچنین یک شناور لنگرانداخته در ۲۴ مایل دریایی شمال غربی بندر راشد امارات، احتمالاً پس از اصابت پرتابه‌ای ناشناس و ورود آب دچار کج‌شدگی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461078" target="_blank">📅 13:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e1466598.mp4?token=AapEv4YFg3AFQev7fE91ml0PfCOmmQIPa1iasiHU6On9uCOJjV-8sGbU3QT10bTS4w-UkJAOjhGi4pU7d0YBXT2U3iM0Mix-WItWDN1qkLHlt1pZ_prMybqrPDRaf-C7xomAQQDoOyM36OkGjaSpaqRHBHIu_JpJmgKBF6fn0xRlT7k0F-c8WiV_2ldsMfLlaiWnW3xkU681_X0KYx6IJzQobRKPhlf1OYy99ZDHAQTHr4DoXiKanY6-nQyhg4r200NphWmRmq6Rju4in2itNalUAsE2ZOAmWZe7npasoMBCsa-Ya5mgGyuviTBhP71TfRVwtSwsCKdfBMPyV-O7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e1466598.mp4?token=AapEv4YFg3AFQev7fE91ml0PfCOmmQIPa1iasiHU6On9uCOJjV-8sGbU3QT10bTS4w-UkJAOjhGi4pU7d0YBXT2U3iM0Mix-WItWDN1qkLHlt1pZ_prMybqrPDRaf-C7xomAQQDoOyM36OkGjaSpaqRHBHIu_JpJmgKBF6fn0xRlT7k0F-c8WiV_2ldsMfLlaiWnW3xkU681_X0KYx6IJzQobRKPhlf1OYy99ZDHAQTHr4DoXiKanY6-nQyhg4r200NphWmRmq6Rju4in2itNalUAsE2ZOAmWZe7npasoMBCsa-Ya5mgGyuviTBhP71TfRVwtSwsCKdfBMPyV-O7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی امید راهی بازی‌های آسیایی ناگویا شد
⚽️
از میان ۲۳ بازیکنی که عبدی، سرمربی تیم امید از آن‌ها دعوت کرده فعلا تنها ۱۵ بازیکن در کنار تیم حضور دارند.
🔸
استقلال و تراکتور فعلا از تحویل بازیکن به تیم ملی امید خودداری کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461077" target="_blank">📅 13:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461075">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPyQvhSXY7eGF-Pwa84M6hFpzF_bZMMxWi8xFhLiHOpxgldAMXpPKD_uQqWGYngr6dYjdKGUmNXyDpMvN8PxUMCcpmXh-t_b97X1_6PTE6vEHfl6VS6xdr4cNpBAH4vGVRG_3836PxsB7p26TRqvyzI0XfZkqVtQD3Pfhu1guDjXhOf0gyllBXMA-8unw-selcm1XNjc95XPRgEl0zRGc2V8c8a0pbv342QX2ZqsAY1HPJQ55dro7zP8BmzJozpvFWpD4siOQFNNnRqQAIBOJUfhgc1OtSZLgrokZgsN_9HPGq_8kdj4WmTVIDNUR3TrUd5MUw1lYtAR4MmWzlBqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه عجیب ترامپ به دستیار زن خود؛ ۴۵ هزار دلار نقد!
🔹
هدیه کریسمس دونالد ترامپ به یکی از نزدیک‌ترین دستیارانش خبرساز شده است؛ رئیس‌جمهور آمریکا ۴۵ هزار دلار پول نقد به ناتالی هارپ پرداخت کرده؛ رقمی که تقریباً یک‌سوم حقوق سالانه اوست.
🔹
این مبلغ در اسناد افشای مالی کاخ سفید فاش شده است؛ اسنادی که نشان می‌دهد ترامپ در مجموع به چهار نفر از کارکنان نزدیک خود ده‌ها هزار دلار هدیه نقدی داده است.
🔸
هارپ ۳۵ ساله از نزدیک‌ترین دستیاران ترامپ محسوب می‌شود و تقریباً همواره در کنار رئیس‌جمهور دیده می‌شود. او به دلیل اینکه معمولاً یک چاپگر قابل‌حمل همراه خود دارد و مطالب رسانه‌ای مطلوب ترامپ و پست‌های شبکه‌های اجتماعی را برای او چاپ می‌کند، به لقب «چاپگر انسانی» معروف شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461075" target="_blank">📅 12:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaBerpwsfndxgC4uCtif_voPc41xia51BDE2yD6ekMZpfzIAQktbha5bMJ1VNHJw8a_ltuJCvZQUI7HIFhFgyPfa8GzuDdsh2A2kGLVLfq35onZ4UGS60cwpKxPL8KR07TUcga2oS6Yba3hCeT-fvuoQndWv-3r_1n8bhPJrqHEo_qtpl95QNe28vQWFpB1Gm7UmW9F3rpKZRTlv5r6-TP4YMWSU0Vo7zKGonbjbhWRS3xUwP3taOotMpLLh6XxpQvee7o1cR_MZRAPpJw-ug_w1nt31ExNhmL-FA5QVvCGSVOZJSEj4MrGxMVgXf8mZSW9dL44Mx9vMDmQ5KO7uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس همچنان رکورد می‌زند
🔹
شاخص کل بورس در پایان معاملات امروز با افزایش ۴۷ هزار واحدی به ۷ میلیون و ۱۲۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/461074" target="_blank">📅 12:31 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
