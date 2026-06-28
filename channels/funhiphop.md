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
<img src="https://cdn4.telesco.pe/file/CVfHauWoQhGIG59yfF_Ewkg5rOjCIVrgysl8a15iRQbT3HJFMQ_sBVuIq-RqTXeeVw9pDEEUn2IkvuWpZK6ROyOnuNb0tYIYQeuLz4WMdS8JZ7_8w-bHaoPm1keTnIzEVu2FRz9v2IvO2Jm2IB6PrRxGqlkmj-x-6c7ecF-MM6s1de6zcKbxWTjsyQ0GJahyzHTXmEwX7eaPlMhiGEM6ru8Z_u-2WuzRWLQcaAeJYF9OsHepOulaDxQmcc_upITG9smf3njahKyJU3XCdWiThXL5XVXQ12oIg1q7Yp1RTCzXCp9CS5MJi5u3oddEhpzw3_KuGXRwByjNhGI21EHvEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 187K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 15:42:41</div>
<hr>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTDSLs9OErkEwS_16p3ZmZkb3nXEbMP72lT_ORmouReOakZEXW2YHbl7KOWG2IfWVGIpG9IukK4Nwuf1GT4YuIwbP8Z8FEjzLRKMNaAaYgTpz3LOSeetXFby-v3lxlV-MnJRzRauSx5SGe3Ob7SgxszWcOTQ8kHqn6sN9tNhZcSW4wWA9dHUQiBaJ0gBuco21kbAZN4TkB1XMn4XFrrAroiwyCB_fMo6tQ_jpXAQeJYErzSOEkXGHNa1MHcPeyVcnnMswh3mLAV3TPOugd9YablNHy2zKmM2wNl9XecqhAwKhKhk5BuzYsEQ1x3asuC6Nq7zJL0Zx3WCTgGZwX-HvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خبر اومد که رئیس‌جمهور و نخست وزیر عراق یهو زدن به سیم آخر.
یه شبه کودتا کردن و با لشکر کشی و تانک و... حدودا ۱۵ تا ۲۰ نفر از وزرا و نماینده‌های مجلس عراق که اکثرا حامی حشدالشعبی بودن رو دستگیر کردن.
با خودم فکر کردم که یعنی چی می‌تونه عامل این اتفاقات یهویی و غیر منتظره باشه تا اینکه با این خبر شاهکار روبه‌رو شدم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/78987" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm49WzfS6ClAYOjKfWUA9DxOONoZzw4v7Ft7_cWcJ_BO_itS2pIFLSmHLkA9cSWRT168ZonqFHDXTApH3gmOp12kDqGblWI5SYPwyuUlwapgdhrrElUn9A0Db5wgKLfLh_2TjjYlBDyjJnpHEjft-Km1fsxdrboyUWj_YiaSUu-a3rBDlvmtH4QM2fHeKc9hVD_KJ5BKX-JJIrlIqgwzpOrKs8k33beFLPHLkL4WQdGJeaW0qmzsO4ypneUKw8NoTcK7ZrB1K0_rR5dUM6xGplKBeQu0CoQnROQvHgvBDAlyK23ygZ0aOiZpqtM2Xd6b8NE1Tq5P3L072DXGFFb-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میثم پیرفلک پدر کیان پیرفلک عزیز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/78986" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1wDyK_bzi88r-vMYKA_WKAODW88A36EcHhEM14kKm9DoWAOFlkjVP0gcrDOaQu46ipLZ2SZTIFC3MCCUR8GtFTpZQsEuRJpAx4fx4ZIlKE-_E6jQxuh4BoTSgpsvzHBTMAh_JBGMgf-fvY7GcwXyoWmUwnfHpeqYCarCIIpjKqz2S93oJm1mAMBvcM6iqX_aE1GP8ZoouVjs6daxZXqfD3sr6op-XIhb79bJaS6jcVEUCpdb9qaBnKUfH9Mz_3t2m0pYrZG6XIxEqxS2FGtF7UncO_mpqb6q4_nKv-FnGgfz_j4rpn845btCQg4rfRVPI8tLLkkovuKnHID9Jg9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیل زاده ببین کاراتو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/78985" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cac12d8a3.mp4?token=n8Fi8yLTJ5Jv5Nba-2ETxiRqhnsJHtxf3R_qKh7CRDLH2vr5aoz1empIyY8K6vB1cVlKMWxM5jYJpR66UrqwxWOmxhOebZI3cZUiFiF6fylfwQ-FaBiR5pPhuswIayQaFAqjVo0DjwHvs2EKF8e37rQENJbGjahEvUNtcSzWIqzuoKdsBAQeBo3UOaaCDUl1V4Hx_0rWIPHy2mCeEYl-W8r59fxZY1Lgs4gre4cHFeLK58Mx0_4kyMABlHjFLJlWFr6UIP60WSUnLglhJWstCNrr3UruOjWLs4_jpYiKCDaGH0bwDM6gyq3WuHykmPajn8r4fkfL0QHS8P6LURKKzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cac12d8a3.mp4?token=n8Fi8yLTJ5Jv5Nba-2ETxiRqhnsJHtxf3R_qKh7CRDLH2vr5aoz1empIyY8K6vB1cVlKMWxM5jYJpR66UrqwxWOmxhOebZI3cZUiFiF6fylfwQ-FaBiR5pPhuswIayQaFAqjVo0DjwHvs2EKF8e37rQENJbGjahEvUNtcSzWIqzuoKdsBAQeBo3UOaaCDUl1V4Hx_0rWIPHy2mCeEYl-W8r59fxZY1Lgs4gre4cHFeLK58Mx0_4kyMABlHjFLJlWFr6UIP60WSUnLglhJWstCNrr3UruOjWLs4_jpYiKCDaGH0bwDM6gyq3WuHykmPajn8r4fkfL0QHS8P6LURKKzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت هتل تیم فوتبال جمهوری اسلامی بعد گل سوم الجزایر
🤣
🤣
🤣
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/78984" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">"من برگشتم" رونالدو مثل "من اومدم که نرم" یلس نشه صلوات
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/78983" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جدی چرا چیزی از ارزش هامون کم نمیشه هیچوقت، مگه چقد گرونیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/78982" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قایدی زن جنده تو که قرار بود یه دقیقه هم بازی نکنی همون نمیرفتی نمیریدی به محبوبیتت دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78981" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اوووووو رامین رضاییان اووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78980" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LeQTdPjU6yfkkjc3cQispa-YzR1RciA6hBKakqnxML2lePocBlVNXeVqAwUvifS8IcyQ_okf9abf5ef5pP4NsGmT265bmzE-SNoYKUe39Meqmq0KfEt8Wkcju7FESzIuXnQkFLUB0Le5UakJ6RrlZ_RChW6d2mv15bLiqq_s8IXnIFRR5UryeRV37MYgwbwWl94OSXjTKCvdXjbgkNhPa-WT08gFiKiSO-iQovnFi0rx5be5EZJhriatvCQdu9fHzrhkO4rvUyfo2f5BQ3NAA9cU3nCXOGwyffOR-ELzoamLRTKmkYXXHPZJtrA0D9dny5vn4tXqs4x9_8tH6KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: مسی هیچ‌وقت قرار نیست بذاره من کفش طلای جام جهانی رو لمس کنم
😭
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78979" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سنگال با دو باخت صعود کرد، ایران بدون باخت سقوط</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78978" target="_blank">📅 11:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">همه دارن خط حمله های آرژانتین و فرانسه رو مقایسه میکنن، ولی بنظر من کلید بازی دست انزو فرناندز و مک آلیستره</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78977" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVwN_qJRjxzoCDFIDP8DSLtEPQ8WbpfxpRjD-xm09nrqOZ4CKUtf_Kduhsuu-bcQGyqU5Q0xwpTe-U6NoJLaklUyqghuNn_Eq-a6LYzNAGEk_lqeG5ZUVyzx49T8HKv2iJCdTsqAJ3aGlLHmous-7UkDhGCwvmiLeXu-yZGtRKfE893wp-bZZ9w9BBYmzL9BQvElxFXKzye28DVSAOBHC1NFQXam4VjuLnOZQSQQNkBMiWBWwX7R_jpAhlHmWkgzTCRQcP36-oWrxPCDZKyvg0gis1a2AcMTH3bGpu-jCDv85RsNHmakPjeHcmh4YvaZJ1iSIdPlg7r8BMCS70bIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خود فیفا هم نمیتونس همچین مسیری تا نیمه نهایی برا یه تیم بچینه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78976" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0E4vxo5VKDFpdxY5psI-t2FA_WdT_Uxd93uHeaEOFIJfpx6_q_YE1JjahHsU2sJnTc1MhYkvzZ230VrISdL_d5zdENfxzHLEXMXthYZc_ItjUY9Iy4nahXakN_r9-n0me5MD2jn2-RSpFZj9nZSYmC4si5ygk3TEUqFA1DuYtk_tbtzVQS8BoGOdNfiWDUNPFkhWlV1ObjDnttcwQpAFW37EObo7z7T3SJ1NF7DjJwrUuvNcUPmshaHL1p7CH30gd1dh4GCDMPjz_B1XIf3xFiabAEekrd29lgIROJTaatnbYnU1_IlKFjWLC2SrwKlPVRcGku0---eHraF-gb4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIm1-MXeQb72AiJ32hqgL3GhCPYIuLvwFyRGqdVZQ72_OkyknqpfS4VizHvWTUlxiAci6MbM7uIgAYaA22JvSJpPTUBGYGm0tzOKp40yzhOfh0dsCERELz9p5oVzVY4Xwo8Tz48UXxHUyHJkNSAz__v1f4LX2Rl4GZ9uIC4jmuSGUbf-7Wesf9-knkOWQV0bVowJi96EB8tdgoSJ_GfG2q5b9cT-pxOc2LijIbUQSHHcb772qJXCXw6eA5G0EUbCswq8EqO_TwHCWClw3QNnXVQC5BjB26AR60_Nv5JmMjdhD2ugyzWyn3qDXqZjE5hK_9NUB5FOG6bvyquTgAHlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78971" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78971" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSCDQngI2iQpzfEJe8KeuJZ18BeDzQCfOTun1B191eG-MMlmJBBQr2KmcGpod7LjBfkEC74rC7159OJVSbCI52GTN3beLFzn1fgBTxIUB7anXh5Qd_nBIIggTGTc3GMHeq_X7GP-z9HcTf5M59D_CmsCtHaaKYHQR1529qgTiSXGrcI6RgE4OrF9WnM4qUb7ORAJ0uCKSZlduX8iXExSLIjdSPUMjw045O2mVVS_ztx_rNpMuqEOh5Y8hOmW_781iDTLweqJw3EMV-c_QCGIY6CSLmooF67Vm_nlmPXi8FGdos-Ao0KioJQYqtTG4TDibSJ3ikEAIE2aqkkTBpwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
R7
🅰
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78970" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNUxuxFEtydx6GFqCFFsBj2-fmntYZxJlu2usJX45MJN3cl1QVaXzaJGq2rWVYF8zQWKxU90iw0HWK8B7rbw6N2YF7vVtmxF8wCET1C6RjzVpULPJ3Avc4ARWb6UAZr09ceThM6MRn78kQGN-VCe3ab07D6_UQPCoW1LnfsM0NEu_aGvSAAt9HT-ja41HLN-d4_n4T4ZyNiavQrriqTOxQLPd9FKicuzwoFVBnBj98c8n1mCllzWKv_ClfAU74GN7Dj6kvge0UxXkibEjXTX1onnlNFFiZkY7Nzk9R2D1kXN260mreE2Vn2hR3x4TGXek-j3Gnou-WA1lz3fi-7SxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpiImuadXDh55NpofBORYeQrtqx4neNeI9F97SAW4cO44Kwzyi2Ut4wA8WpaHnolrrW_GUL33DYKTEN_GofFYRjUHpH6Z9cVLYkKjJoOGPCnKoF72S0fT-VffXiAe5BmE79iAWq_xkgZ6RR16eCI97j84geeOJs9xjjZMfM16-OtmrlWYSZBwDevFs0N4KngRITsDHTrco_V_e7Y8srx9xqMPP4AlHStxdEFpMxK2XG-qJDYBntnotkucv-gMNIPZrKa0PAjt6QYAxGRCEZ4ys4bIiYDhYn6jahEnGCivY9DGqoLpwIUDkdJY2r9Uw7E1fln9lERR_-Na2qLUG8r9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCQM0o5J2-F4BFbZelcpCinXeQWiAho41Mw9Rug_ZZnS1yKjX7WDMEy1D9bcjlq446YeXa_b34qLpdR5YLnZWEZOG8BMuBr_RGikbi8NvrOpfh6fpGtLVNh1NfAS3c55GdaI4NbpVBkhFRdlMoHMgQOCJmxsrM_eqrwTs69twK_zretjsmC5q3gir-jC9oIot2HZzym9F9Iu73sQ_AFhTIoCMVIv_k0RqyI5-ZOPUviBxNOWnbHDt_FIWV12T6nAwSeOZ870-F1gNu-Zx1itQ9cdYyzeOBSttSMGhvt13PA_cgd3kVnj1PAPdLGyZTIimUNFrYGZf2nDyQvTZayL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=NO55uF5rGAqQtTYElBukWwJdXibGMRynXHW668w6qARuUAbRTyv5AXCebah5To57HlQ_brpMpnlCOjwsBU4ny3lDjNJ92nlwph73rkY9EKtfTORJfOHFOXlFUSUIipFXE8ntyqAxL1snqZzsj-XDICq4CJVy4p21Qve-4LsREIDZZM2yvcZ9smnVQjkthznt91DV1w619QXm8MC1KHZXA5t6I-3K8DkpKaM6zqx0k1YdUPUzGVPeZpZkMWhEFjaNfpJ__I1kLuTGkPlYY2XyMFkRqRO6b-7-lOPuQGNygXYqtzpt9KQiEDa9pW1lGe8FLary7BzSb02HYfnxXxCCYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=NO55uF5rGAqQtTYElBukWwJdXibGMRynXHW668w6qARuUAbRTyv5AXCebah5To57HlQ_brpMpnlCOjwsBU4ny3lDjNJ92nlwph73rkY9EKtfTORJfOHFOXlFUSUIipFXE8ntyqAxL1snqZzsj-XDICq4CJVy4p21Qve-4LsREIDZZM2yvcZ9smnVQjkthznt91DV1w619QXm8MC1KHZXA5t6I-3K8DkpKaM6zqx0k1YdUPUzGVPeZpZkMWhEFjaNfpJ__I1kLuTGkPlYY2XyMFkRqRO6b-7-lOPuQGNygXYqtzpt9KQiEDa9pW1lGe8FLary7BzSb02HYfnxXxCCYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5aDLT9pXpA8zy148zTpqWXoK6ZVFD2g4Hg3qx8kLkXKUOJIUf95LVKNJNzns4NA7AkEfQaEMqnCQJ7xfBFQ53WE0FczefNUaBNr5hWRQZhKoHVu9T8gVUXMIuE8huDAnK6SGQrxwK_rhrMCGNePn8QreCALi6SHyHWs_nFdmgSeaBj9IhJmKRYusKuFraJ0n5dqbnT0VSelJ8zcKgLA9Jwr9z0f4HSds_Fw9Z_op7QuW4u9dT0ImehiUX7xrsmZa83m6frkvuN3VXU5HEyHxVYqfaedwSo3JDDmZ9SrnwVYRvg2KxUR5LV7N7AWvPAQ1nHTwxSfBpt8gjokgDTJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6d_Wu91TtlFprSeuhfkEiy8o6lM2jIXQZp49TTYXA6ZT4s1Il6CpqZHcCANbiZ1x-2LeBP9pQF5gYKKrntxYwY2bjYI8lU-Uk9MCWmzMjQ6quAT55x5Q9bZ2XfKgwVGG9Z3t9eEC47kLuhwVDPw_UrgM1ffbFelw7qZcLXegtR63VYjzy-2piQ2BjIPvmG9EjCanpRX57wP42sxi4klvPWv6KsTNUqSuO_RknPRtNddpwtpA7cagrpVfhHYMy0P9tdPubgJHmvUTF6kPh4KfV4iQ1rOo1T7BU8ryTioeWHa2NhTXZ_iwl7kJosp1kqVHHMK-nQZRgYbw1HWAo6oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIUb2Yc-zSmD1yxjw3rNHy3wgTFqnsNfVDEY1t2o6xzdXQWGgvX60lyq8IaCCws0j4PjNgyff9Vt8L02paP_bfCq9PtwiFzbXnThojPh7-WuJyzGAOMUbnfQ_WCDFAAIl_A7_NXi64Qjlpu1gR6ta7AjDBn1BYKiKwfw_3kMSW8Pe7uH-fluZ5ivHULnpkbZ10rFI01dHhgW8WJHXd7RcPS6YOpzaDcwDu9aul8xnb8tYj0H3gx1Zn6M39_n5r4KCEYFqll1hDPkXStjI2U9yarqtKTKNIi19MbRTa1CCq8q6Jlvm2gRKaftlQKyecDh6PPJ0Y6LpVNvdFMPBlDSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43122e124.mp4?token=HwLhVa2ECPCUQJfUqKtBkLdvBA5TQ2d8jWP2YjXdFtWkG0fuk5GCdXZYFdgviIE2ZU8hBuT5QHP7TfVlLKktHDeUxK5N8edtGiqEorkFFgpWFIqzv51TrLPtv-xFsLkhBFgbWJfFbR7hnN0gFh2w6ouu-QnWTj8i5B6J-sygxZ076VsAbLVLvWiUufvcHeinj70tIO4an-j3HSPnLvL5MjDiCMqtQx5wQWxow5Jhl1jhjjkm53QwT9YOHfztWzMmlpFb4P6zzQebXznumKUbD76DWTQUNFwZcR18eNzUWEQFv16mNHMa7zeAjJ6trhprb_sAzQ4o7EDIa_7B9qgLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43122e124.mp4?token=HwLhVa2ECPCUQJfUqKtBkLdvBA5TQ2d8jWP2YjXdFtWkG0fuk5GCdXZYFdgviIE2ZU8hBuT5QHP7TfVlLKktHDeUxK5N8edtGiqEorkFFgpWFIqzv51TrLPtv-xFsLkhBFgbWJfFbR7hnN0gFh2w6ouu-QnWTj8i5B6J-sygxZ076VsAbLVLvWiUufvcHeinj70tIO4an-j3HSPnLvL5MjDiCMqtQx5wQWxow5Jhl1jhjjkm53QwT9YOHfztWzMmlpFb4P6zzQebXznumKUbD76DWTQUNFwZcR18eNzUWEQFv16mNHMa7zeAjJ6trhprb_sAzQ4o7EDIa_7B9qgLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم مصاحبه شجاع خلیلزاده قبل جام جهانی:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=h1wrcdxCpzGITv7K_dRacvfhEBCH_iyYzZCBEvmF-p7ywyQrCozOUYE6mfLkwCHTUGqUE3p6uYkWjtKD0IpxYdM-PPewuH2RbxmBpkdP45b1bEnPLXYkwFrGiRtMYXvoADH1IeXrUhD7o8pMaLiE5B1mamhoAVTSkW21SNdq-RlXHuvdR6W2iYbuyAqpu2mFMHINkRkSfHDHCf92Mzpw0HU8GIHaXeZc6hNHXADKHN_YWTiV_u6v5ozGlmifKMRRcUBtBZX5HgNegg7Ji-T09WdL2NAwurD5_vAT4HGooi1zK95A0u_RY2LyO1_UkTmwpFsn3bfYquaBejYmzBd7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=h1wrcdxCpzGITv7K_dRacvfhEBCH_iyYzZCBEvmF-p7ywyQrCozOUYE6mfLkwCHTUGqUE3p6uYkWjtKD0IpxYdM-PPewuH2RbxmBpkdP45b1bEnPLXYkwFrGiRtMYXvoADH1IeXrUhD7o8pMaLiE5B1mamhoAVTSkW21SNdq-RlXHuvdR6W2iYbuyAqpu2mFMHINkRkSfHDHCf92Mzpw0HU8GIHaXeZc6hNHXADKHN_YWTiV_u6v5ozGlmifKMRRcUBtBZX5HgNegg7Ji-T09WdL2NAwurD5_vAT4HGooi1zK95A0u_RY2LyO1_UkTmwpFsn3bfYquaBejYmzBd7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر رامین رضاییان در مورد هو شدن سرود ملی جمهوری اسلامی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvNNDJ0DsoFuguZSdqvO5OrxXRFoE3sCscvOnn5qJyxxi-_CEUCjfdAIuQXRIrHY7w34JtW1Hzxf_Kq_Z-ckkNzH_tYWfLkMVrVlAV159tXdN0Hbhcy4kJ-1a6AptLESQ3-AU_SccOIISOY8xMG3Tywtjo6QREiqjizC-s0slIhVX7w5XThGUZRIdBwb8fxufdRvWb0eWuc9jb2R5ivLgAF5Mm2DWWs2s5LIUWxySECwiSUYDqes9OXSJatri2HdEpLjibIYiuwAYryFUmV7UMgwm6iZn5cl74HrDT4ZmCXOYNYbaAY0XXgaQROSik-etEu1v6wnITcAeBVhexScng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etjC3P_wcJ4XYWoPdxymNuTfk86EhQVVsuHJwGaxweEkIqjZsv5t3lZh13ZdjAWlmKc_Nouz-2PTTaE5d1MKINuNJbwvek9LVnaTjan1jD3YJls19URkZCVwH8bm4I05dUC0WHbG_VP1iznFDeYDBL-ImMiFtLOzbw5aK7ZMQt4R8Y0NjdHQEp758eUqqZfU5CJYtcYnBxFlDlzSorVt7dGzr8SHgXk6ingRe5P7DVyfDqXf5uy2An2aMF8o1Oka93-JWVQA-EnG40TFWyr9X2g7UtOGBMWPxX17lZSZd5cVqnaDV3h2yBvaa-dxf6cm-CCtU9n7pPtkHv3KLfq9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzpgc_U6kzvsVc9SeUF8rfXn599R6wC87X5fPK9d8Bv-mzDJx1-7Bo7PYbZs6L2YWqZlvA5apMYgYWBA9ttovDmwXSHsUl8hUEsFhe2cuhw2nXjjoSHTBbiH_ix0C0TMG3EWQlDi7POhdEZfbXA8TpFMFczueyRvn1vjGzZ2N7Iw7tYXr3C1Zg8ZnuWA4w2wZ6xOzI4fXCaMGwi9CGSuXVpf9FidxU7gCTSyhHDM41xhmMLgrYIo-787cl-OIo-L-IWS13BawZpLhhqRvSkMc7itNPOEHT5c-eZK6i97l88T_lTn7ktzeZqNEDKoPWkO_3eLvxz3P6yAYLDlFmyHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEFQsbi8iQ6EKJGulEPALOtTd2F2JGHsY_eUYeM3zuvetUaA74oZTp44crRDG6N8yT7u35itM-MZ_f6ruHxkQrIPF4mFQP8FLBgDb59J5gcd-DGpN_kytUMWWWUSf-MMgLx9dbZAxSCGS4WFaDlSJ-p4hUa3_xKoMpdJtY-8B7S8dWu4EhbpifL3bRm-6A94eobjL9L-DsOJ2PdHH91jJakwK9FCuAq0fNeTk2VyDZVbe1yDTge8VClCg-w3t1TxjQOquN5IJREaGj9uwxQMT2Gx9j2Oi6gEHyfd0w_Tjl1gHW_e_ZmZuv20JHRMEW8SzhV9pCbtqQ7juyr8EHGEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78911" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78911" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUqOAeJoNY7iBw-CR0Oq65MglgTZ_TSUkYEx4CxgqU8aTSXMUegnsYE1CVyyfrlHTPQHwyi_m4soH5PGsD-Gw4M0Tg8JdzUG2NuFTx3x2ssNHWEi83WzHDTYYUkVPBBVqR_0bQlqHEqRLRMq9y5dwF7Gpsy0BLxCAHaME7Am2PFurdTiR_92unz7sn5vkf-4oHAkiiYtO0PMwlODc1-ZGf8cLRf7Htw5DfR5hRaOiS8p-5s4cDU8BuCVOvj6Z_nqPYuJAA6PgevgGUOGCISMje6f1lGcCes8s092pEEcq6a8rQ38mKREVSNTj6B5SHgGYejEafRi8Mx1BhKtWq8mQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی پرهیجان از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
کرواسی
🇭🇷
- غنا
🇬🇭
⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- پاناما
🇵🇦
⚽️
پرتغال
🇵🇹
- کلمبیا
🇨🇴
⚽️
آرژانتین
🇦🇷
- اردن
🇯🇴
🌍
امشب ستاره‌های فوتبال جهان برای صعود به میدان می‌روند؛ شما هم شانس خودتان را با بهترین ضرایب امتحان کنید.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
G6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78910" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txl8PjPXCMvObCDr79c2xUOlyb-0oSuJ3BCgi_wSacWenuY5wemWZgGo_7eUpkP8UHFc339G5x8-MwZLlkIGYVUVZA2Uoz90xK5HlSeiLquK4-uEtK8v5MVIAHlNPxdQJcRY8VPhC-L8nVhuOKYKFKqGpEop-BpuzduoJoSCB5UhSorI5sLwmWR-vh6Cypc63WPAXvs4ndMBD6Sfr_44kkrI51BqPLBCUYobNOhYiO1dAg2sztEB9brnv5feMWnUB_F5r2RtwaqQ2ePToi_XlV8LNn9fLMrtwPx3E5dgCo-MvtcZ2mSw7tx0wj8x6ARfSJQQFUSNq7NQ7bWNQ_CePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
حسام تی‌ام
و
حسین تی‌ام
به اسم "
West Side
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78907" target="_blank">📅 18:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcpRG_5keVy6kOfwn1vxBL57OUkto3u4LhBZkulOFseLszqQL55CvP1ntzBfgioz7OWJ93mWqGTg-mfjPXRhLFKBBTFyjmX1wa06UIZ0F3EFoombDQbgHX4Rk0GuvUc8ujq-EyY_UuYjlZ5z2GQ7nCs-u2VNc7nRfElUkIpVmaOJA38Tr4bzSiwzjg10GQxtiv6BmCIA3JowBuF8xvyKWV6YFaLNoDKNyaXromPHQjNs_Pi2DlFi4p396xGYnI2Ol_z2pqBZkiPZZS4tW9j-Jyudoq2q7_FwqPE_bKtBsg9MmMcRuIHxUelEOV6nVoBqqaKwrmHDyytNFc8jwyG3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید
مهیاد
و
دینا
به اسم "
ATISHSOOZI
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78905" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78904" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxEB9190hTZVp2ovLkBa5lQofRuZbFyYiW6eznsnNXnM-qhsaT3M9tPtYoCVtYgFzr99ynlsKRdU9GDFNc8LH4MEmoQHZoH_PYzCvZ4TpRDx3OF_wSsYkO41K57WRXoOtN07khBkQiTXEjuHRITYIC2vuF322EynhNABEW4S37ZoKJpzVzgyMl_R1hOUoQ-2B7DZclg3h4i7ZAzDIG-XSrKPhhVFAyaFcgBW7I49fKMtnpJ5oUKIJ_uIdp78aQ0c2Wo7zdSG5A5sPelX3LcPTx_WoWZ85hofDMS-a296mRrSdcXXhWpbeIa3FUxUunNlq6vF-VwJXBZ2LwCREnO-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-cmmu6a-F-kfs5TImxu1668Sdw1R0qgz4h-1RnL4md2A22VU5j3TNP52QI5c5ouSkul6oUtH0zyPMcv81matLfd6Oah4ufYeIz00acaaOxW4W1Nuc8jAuQgWsG-XRcJ8CbLzyvrgBOhHU6tglmpqNoEXyzOGaz-bQZd8enMChetlQrPEubiW5OY1lxpoR21QHfrkxAt6HAMBBfMdb3ONp4T75kpmjO5wx36uiuAEd2uJJbivAjuIhXoOxrdKxXhqbb8oxhgICMhTWKkkIcAqxwUFF0kcVjWpcAbkjqhN00X0TkuY_FiJXJxagynx9_IwLW3ybwnQkAdJbizq0xBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=TbUqalR80VqXZbgdErfMD65ic2TGQ1aR0ASMq2bFmPUEQc8DNgVtAGLwLGycHsrdkZde_teoeOUIozBHRMXnkrCMeigXyIYm4qyjwRkRrINI3_YJ9c8yzEH2_Uxlkt1WcXDyojnk_XBdMjUW3UWT_SLSYzHl-ZUbVeRsCT7TD_fL0qAJlfBj1r9Hw0UBZ55Po9P127_DgGW4dDlHNeGsz0q_LyutRON7uHaw3lBE8sBEV09y-fYBLyRWKaKF5kOIYcSYV-X6JUBCBmnzDUt-L_1jlg1AsQfIsgMKeVI9tTuRRT9_4ZT09ntK4WRT5-WaK24vvH3A93GGmSKSkL9jBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=TbUqalR80VqXZbgdErfMD65ic2TGQ1aR0ASMq2bFmPUEQc8DNgVtAGLwLGycHsrdkZde_teoeOUIozBHRMXnkrCMeigXyIYm4qyjwRkRrINI3_YJ9c8yzEH2_Uxlkt1WcXDyojnk_XBdMjUW3UWT_SLSYzHl-ZUbVeRsCT7TD_fL0qAJlfBj1r9Hw0UBZ55Po9P127_DgGW4dDlHNeGsz0q_LyutRON7uHaw3lBE8sBEV09y-fYBLyRWKaKF5kOIYcSYV-X6JUBCBmnzDUt-L_1jlg1AsQfIsgMKeVI9tTuRRT9_4ZT09ntK4WRT5-WaK24vvH3A93GGmSKSkL9jBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSLm66ut7lRG_ruyQ70-vHw4iqGr5HSVTXVwvXC9aCRPOE4TV3Z8APSgTeQdZ6Y_AuCdgcxOFVRucC7jvVB9LYYxgq-zVWlJBt4bS8cpQJUHFY8FGShETj5VC-W-zlv7-ZRXKNoDXAc-_bRWX12wG3OL_VFPhAOaXPE_iUD30x61WrHjiY0PM1vOSuhj8o9P5zaCFv-9Vhmk2Dy0lr0Rejuhx8okZyT4jxxfyGPmETmpS1-HpOQVAGtHeMX59Hdxt_rwbsqhPWsbTXEQWVUDpPHygjJTPBZDmsptClgs2H4RwiJMnr4eGg6EgrbFccwQyZjuywLWYREHIfGe_8Em1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUK4KJCIg2doPu4KOA1JGbhyDhSjIri8f-YO5-YEkUWTb56CWJ9s1Gx-Umtp4bCJ2NbpC4EKvk2726Svv37MbsZfA0W5UUVAdOsNt6JGg4aL-BISD7Vxm6QeytFJANbHdkjwDGJeaCcXqQGD3LsXmVTemsZHaJDWGnc9MjfrrRbftufgD7N8opKe6o7ss0KPgxlVv4Miiytx_eVKhOlbXxFxxtU_t0D1oOVEdIQTOqd9tcdvyGAnrtnoBF2PGyvbdzoeBl8Dj5BQt-sJKPMAiLbu6umObbmq7CLALO7mHUwQlGja0_xBFtrlpc764hEPzOApOrQG4drrsrVRmu4RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_o7zcnCscK_5z-FL6puS3fxt21bI_9pH8tx0-khf3pc07obtjMSIyoSIzhyPD7za8ttgdwvM1VLL7CxrHmD31aserdYKeTKnQBbESLjuqQxCYvNK4MnM7Kv3jkmw_dGcWzknQBrZEM3oi3U_GN3YJ_YzbnteA_bxWUf0Ay7VzHWwxigiXsmW4vma6vII5w173Lg0mBW5z_-E7F1kRH6Kxt0-6FOSzTArSRZOMz5G-g4AhXLC0UdnESQt3K1RNqUKdpF-c2uSKc9ueKzUbkzT7FCE7ShVt39YFrJudsaDKY7IGcvq_tZer70ZGvcLZ29xGT8EHexJ6caA3bmSpiY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
R6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78893" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du3OqGYpBHhxjb13tFf8Jajy2ZQAUltCU-qDs9NdOvKGzD5kmxtPGa5HewIeDm06dQvEYXYI6m_rc05H6wTZGPcHRjHJdBHGR9-9dMm0QxCAkCRnovsn9LU6rw5boQ6WEiAlOfWK6C8sINv_q5Sj4MNQox9-pxCDvPWtwggg9-3qiesW2uvMFtsi7h8t3obJBcpMdbZ-Iut_jbBdLRlDsYiPymWGMbSb2Z0M-u7z-LIwVI4ElQVXF58GNgU48c9IDI880h45beDcIB9sYETjmL-6C8IEwjlIOOPYptfF__F324CI7Lpz3SXZU1D6USNUR5OOqV4T_64C8HK7ILE8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حتی اگه این تیم رو دوست داشتم و حتی نتایج بهتری هم میگرفت خوشحال نمیشدم.
چون هرچی شده باشه از رو خوشانسیه و هیچ برنامه ای پشتش نیست و نتیجه ای نداره، تیمی که برنامه پشت نتیجه گرفتنشونه مراکش و ژاپنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78891" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78890" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام دوستان من تازه از خواب بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78889" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جدول حذفی جوری شده دیگه کم کم منم دارم به مسی شک میکنم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78888" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اوووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78887" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78883">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=voIpf0WwNmSpvyQDSgLFmJ9I-JejBtGSEMjhcEDXbKo_AgXDH5p2pyj6YSn1op4BpVMy6htl4UydbdUveBq2PvlUaW6gGD4T6Dz6SeRquZ7lChoi7-6fqYC6vdqfzRQxLd2tKzj6I8iE2QqdfGF0Q9HcfDurjh0MXuGqrd1e83qMR7oF3ycjz0Tvef-9iuQxY2IqH_tczHOlkh-Vd0a38k9zai1B2WJNBWTI2NZ74R6IA-0dEV9WS8-qISuH_1nwKVXkO5ldQ0eS5EiXB_wrmCy9NzYGNHvvHsemMPRk3Dncd3oOTnm_quEjrYkXOvN6wuaFMDzEz8rgYLYxq6KlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=voIpf0WwNmSpvyQDSgLFmJ9I-JejBtGSEMjhcEDXbKo_AgXDH5p2pyj6YSn1op4BpVMy6htl4UydbdUveBq2PvlUaW6gGD4T6Dz6SeRquZ7lChoi7-6fqYC6vdqfzRQxLd2tKzj6I8iE2QqdfGF0Q9HcfDurjh0MXuGqrd1e83qMR7oF3ycjz0Tvef-9iuQxY2IqH_tczHOlkh-Vd0a38k9zai1B2WJNBWTI2NZ74R6IA-0dEV9WS8-qISuH_1nwKVXkO5ldQ0eS5EiXB_wrmCy9NzYGNHvvHsemMPRk3Dncd3oOTnm_quEjrYkXOvN6wuaFMDzEz8rgYLYxq6KlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتون باشه این ما نبودیم که فوتبال رو سیاسی کردیم
و خطاب به وطن پرست های فوتبالی بگم که کاش یکبار هم که شده حافظه بلند مدت خوبی داشته باشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/78883" target="_blank">📅 10:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چین به اینترنت 10G رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78882" target="_blank">📅 09:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">می‌ثاقی:
اگه بازی تو لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات درست و درمون var نداریم الان گلمون آفساید نبود و برده بودیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78881" target="_blank">📅 09:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfOwu8OG_SEfy8Ef2Nqv0yviFCTLiacCd9ZrDpC-fuGlrhKzFCg-tYqxuPwDTMjaU-PVsNqU9M4M4scqMi2dPnmgYmWz4UVZZDF9bMtE8lCbxmyOhR3cVVNntnMJyzYjEBiuCyMiYhq78axdUb5thsffG4oqqJuIH4D0wnBlOEI4CgQlarqUgNQWxoKooB5VLYWMfVdUHJCMuZ5BBmLDkhydJV2UHGeYtRxhmTFEx7a4ejhwe-r4To4gqUqMPodJ4EjYV6L8-3ftXgThWSvuetOpPFyWkxAjK0gKglGbhc3PvurzEI5Vi7qTvNvoqNRovOROJ-Yb1oGBp9R09DAWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوست دارم بدونم این شیر ایرانی در چه حالیه الان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78880" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78879" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMPIe5aYPjk0Rd8S2JXYnktymvP3blke_wb8QwJGeblVuFHvzXLNO7ft3VP97svRZRr7gsJ8a9wlbv28xHhv84N8fuoY0LMrIF2LHN3IsOYYF6DFbPG0zSKxBg4oIk4e_qxlCR5LrmJMkoJRb353s8NgZiKmk_ApSIbbHHf9JdQm-g5yNDw-lsS6J8X_DlUuQ7P9x-RJD0T1AyHAGoRGHhCDDmA9AOynEqnHGLrBb_Pz7Yo1XlDm1njQoI-4jsYWZzrTLKHFSynhvYe-lodHLX3ZmQ1a549ZDxLsYHkHS4A1RTGzQEWh-TeXmqi1Q05YBNw2U7OgP0ZlWZTCf0gcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی عکسه رو سریع بگیر تا نفهمیدن کیری فازشو دارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78878" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
