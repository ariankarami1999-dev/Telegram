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
<img src="https://cdn1.telesco.pe/file/iHkUODvlUyIQi3Jp6V_GLOyQc--gxNticpUn6dey3T1Q-dcVVsdxk1mdI69qyIYjWWD47nC9hZznKrRhaYxBkTfLZIfiNd2jhFpOMJZoN_XMAESDq7D3yJ6ViyQiAsOKcx9EOZ2COMWsdarqD-t0uqZ1X9OubEg92ZZWhflanuFK3mmRZeQWaPT4yAQrkOFq7jbWxcr3zNx4FUOn-npfPauXZJ9oTNSRJJLO-ZmfHXPFePqaI9DnzWqcrglfmk-BqYARSSCe8ygVyh_k7X5robUD2mU8r8yFY133foLDb4zhFzwhGa0kg2ZGR9_zCOrVwXdAm91gGt2LfXkZDQwUcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 20:25:31</div>
<hr>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RMnAVc1emMfqHl5JBKAg-NC2Wpf6moc3tYYJz9LVFeTPI8AAJl1__F2RKumopTNYIr_kBLiTQMjccGGwMsgTfAbmihQzHlTJw1YtJ5c7EmEt-cLmoIEQtnpk5v49Gh_ndJB8AdiSpdOd83sdyfI5KmGQoMOSxTzLfZ_DVJnrmSnxVAujW7cj2ceibebMjNmjVSFH8Z0b5MmQJfs5oaYEtdVwLoy7iqBUMBHC1M9oqWwNeCuOe-d-nDOVfaYmf9BpoGMgos2XqbmcsKH6-ySrQsy_6RlqVJzDnnPtYbu3BMH5gPDweu70vXFSKH9LJ51kukE14sbZ1EjZUSeAvOAUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gnyG776ndYoEnOaMHmHleEL44yFk64IAjZRzBBNBzFQBaw7qwn1F7Qg6WsvW8QQFYCoEXjvHUC7KG5TlKlfQSQSPmsDLiI6r7bnncQG9q5D_npUH8meAC14-2NddAwkjHYHwvVyHiSQxwr57KvJi27i6jvVOpxwZvTf7WX_Kkv3J_9bpS5o3ukDnjPjLgYaJ9f8-Ph39nQPiIX6YxI-SWWD_b2V7mYLLX73cXATUi6EbDztxsb8S-7BMvUcoLYfIGZornZOtR02aiOgT24HTMlhk-K19cWOpr2oR5LYTxPoFnRLrl1SCRK2Ho8eXh1ync4uRaO3FW-es2a51bm5cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StvnQB8egFzBFC5alEb--I34_fXup0ie1OukkfjNuTYGC4oqNfnGhYVOsg5s8lL7Qcb_cMlHkHkWrzWfn5Sz_1IgnifcbR1sVqwRZGRAo5f8whSUzhyqKcm422-t1kDiwmWCMNA9bN45MY4x_J093-sji_fpAXr2q7r1rn7GYst8eaa--gulDl5pyOt5QhdZUKBCdpxUZO2gux7OlmXuUdGfsd9p4RROzzz1gYFKlPJp_pz0qAc8XE6rz3JbFthpxXfirNN74VldM6Gde3XER94-EVAFq7IJ4h2LUMB6T2RcTHrUHrQNOea9CbgABpuuN2KKzm-t0SptQHuiYCi_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eZ-P1mDStfZr6fEqGsA_jLC0LaNLrjjYZ4mqx53h4bV0jTvRTV7tOf5LnOhNzR8jV63wi48sbsl1YrCiqawFm8dHkUXWgMCX1tyTDbDgp9nnynOeH4ZsK4NmrKCE6OBEoPjk1cgKzy_0xQDB8pwCC4K2o77G-OnLHNrb4cMzvTLs4eqWyEmOUTZl_drQ5Pz7KkRACq0yjIC8tCJSr_pGUPDqdxo_2EGHkulAMIQ3K56s_FG3044GAztd-M44N71INHrVeo-dl6z-I5Ckqn4gKn0Wt_NBjXW6v2flu6Mq4XhBtNStYGPoW1Vkqy3it24CDBt4DQSGNUwANjiqJCuT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B5R4_1CYQWPnDavqD1cIhdK7rN5MHa-x_E9pWX1eCCyt9MQkciBZZSP8ZAXYxcHBWA65cyMcdjB5soA8YeaGw558v9jhJgogA9AKhgOEM1mNNkYt57s4FrftXmAIBxxwDE32WyRUTP_xdz3ka1YbPXougLZ8MgdK-WbEVdioVdlsIhS9xJfzo2Z7TSPe-RAWKrM_rCojibw5KZxVp4o42oPBwOq_Fxxrs_7ZHYM0HQYqHTEmBn27YsbewQEY4h5qDd-yBKmdnDct-EAs_Fm3DykSFgt4NLio4xDB6oXQSUihDpRLOJYSkcyZTY6kAwhDah9OsBB-fdgo1KV59XJTOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی ۲۵ تیر با شرح: ترمینال مسافربری فرودگاه بوشهر و باقی‌مانده‌های یک هواپیما
سخنگوی دولت، امروز: فرودگاه بوشهر دیگر قابل استفاده نیست و باید از نو ساخته شود. از یک هواپیما که تازه خریده بودیم فقط دم آن باقی مانده است.
Vahid
سخنگوی دولت جمهوری اسلامی می‌گوید فرودگاه بوشهر در حملات اخیر آمریکا کاملا تخریب شده و دیگر قابل استفاده نیست و «حتما باید از اول ساخته شود.»
فاطمه مهاجرانی روز سه‌شنبه، ۶ مرداد، در نشست خبری هفتگی‌اش با خبرنگاران گفت در بازدید از فرودگاه بوشهر «بقایای هواپیمای نوی به تازگی خریداری شده» را دیده که بر اثر اصابت مستقیم موشک، جز بخش کوچکی از دُم آن، تمام بدنه آن نابود شده بود.
این نخستین بار است که یک مقام حکومت ایران از تخریب کامل فرودگاه بوشهر بر اثر حملات به ایران خبر می‌دهد.
@
VahidHeadline
یک توییت به همراه اسکرین‌شات‌هایی درباره اطلاعات یک ایرباس ۳۱۹:
عمر این هواپیما 24 سال بوده! سال 2019 هم خریداری شده بوده.
iranimerican
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/77571" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_tlczmcM-_dDLIbLIw2_tmoDp_L0F9xIvV_FhLhi7J1DxtvgbE5zLraW3QCMUCwSAXnVpMts9DejdUOY_sGo2FXi8bCMnoX2JG5EbhhYYevkMeoQuRNF0P84KgPR5ipEuwV9Y8T_Jf_3HwNKMv9-dkPCmxNcIcQk6mI610s3InUvsvwZtEZFwYZo6Cp9I2lrV-NNjJkOHUHxg0CIjIFvFzbXjfXO6ab0ezzR1xSjBc3pFeE8tV3I8VQa_po1PR1tI0Zx0075B0X4R5jJusvwy_olAsw46GfToFSCAhvmIaYOd-TLGsTpstCPbPFvW5jbodpQWLlsxmdrD7JXc7hZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های نزدیک به حکومت و شماری از مقام‌های جمهوری اسلامی در روزهای اخیر بار دیگر بر اجرای قانون حجاب اجباری و برخورد با زنانی که از این قانون تبعیت نمی‌کنند، تأکید کرده‌اند. هم‌زمان روزنامه «همشهری» با انتشار گزارشی، از قوه قضاییه و نیروی انتظامی خواست با آنچه «هنجارشکنی» و «بدپوششی» خوانده، برخورد کنند.
روزنامه همشهری، وابسته به شهرداری تهران، در گزارشی با اشاره به انتشار ویدیوهایی از حضور زنان بدون حجاب اجباری در سواحل کیش، مراکز تفریحی، مراکز خرید و برخی رویدادهای فرهنگی، این موارد را نشانه «حیازدایی فرهنگی» توصیف کرد و مدعی شد که ممکن است بخشی از این رویدادها در قالب «پروژه‌ای سازمان‌یافته» برای تضعیف ارزش‌های اسلامی انجام شود.
این روزنامه با اشاره به ویدیوهای منتشرشده از ساحل سیمرغ کیش، برگزاری نمایش‌های مد، جشن‌های مختلط، کنسرت‌ها و تغییر الگوی پوشش در اماکن عمومی، خواستار ورود دادستانی و نیروی انتظامی و برخورد با افرادی شد که از نگاه این رسانه، قوانین مربوط به حجاب اجباری را نقض می‌کنند.
هم‌زمان، شماری از نمایندگان مجلس نیز بار دیگر خواستار اجرای قانون موسوم به «حمایت از خانواده از طریق ترویج فرهنگ عفاف و حجاب» شدند. محمدتقی نقدعلی، نماینده خمینی‌شهر، مدعی شد «برهنگی و بی‌حجابی مانند خوره به جان جامعه افتاده» و از مسئولان خواست اجرای این قانون را در اولویت قرار دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/77570" target="_blank">📅 17:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ijYRfv8i38Fuj5XP-TYkO9Md2dDhqQQVBcdhiwJ6WG2v3CFetgbJfqvDEJ8HBwNrOkqUS5VLVmWsIM_bX8rvRN1jxxnrb81XWRnUY3LjY75Ms1aVgKvtXkMDg8PocEQyy6M1XwbaO8ktlbzj54tvX6F5euVTh3ytdByFsuAFTxhlsoP3m85f1Y51OvqCEQOkZF-zPZBsr2n7arIgwI96Vlibl06zn0fFKAYr53wpO1DJiXuXCXKI9Qg1W5MMm0UV0EHC1JIBVHCbxjrzVjja4DlqPRBGwEg95XZB7HJ7DNM_iuw5WFD6gbqR1GmJMTManIK6c7D9tIFG3Kq3tstxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=jHL_VZuoUzHpf0-DW_R2YYQi58uUWZs9h6-9XHDlCjOzn94kiLEoQm0_oT0BfbQ-iQRpMkwflE4ghnJnDxZO0gyrgB3hDRf9jszeGL6-WbYnkvR3PBqpTolfYeBlMLNwR1duGicxW0dnrMU0Hc---hb2qk-P-7F-gRBlO1VDN1S1S2E-oAcRA2fJQR9YyGBcXKJ4by6MywMeGNMaqVenor91CXRHEd-xttr1DvgHxWUCK7k2zgSReMaFKCH818Qo5kHxMBsYosgY2fn0d0N1QmcGwBZWznvBL-NBxUsaIXOV1LnX0TAUSA1uHfmxG5m-yq9Yj671UTl1mKNvqeRlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=jHL_VZuoUzHpf0-DW_R2YYQi58uUWZs9h6-9XHDlCjOzn94kiLEoQm0_oT0BfbQ-iQRpMkwflE4ghnJnDxZO0gyrgB3hDRf9jszeGL6-WbYnkvR3PBqpTolfYeBlMLNwR1duGicxW0dnrMU0Hc---hb2qk-P-7F-gRBlO1VDN1S1S2E-oAcRA2fJQR9YyGBcXKJ4by6MywMeGNMaqVenor91CXRHEd-xttr1DvgHxWUCK7k2zgSReMaFKCH818Qo5kHxMBsYosgY2fn0d0N1QmcGwBZWznvBL-NBxUsaIXOV1LnX0TAUSA1uHfmxG5m-yq9Yj671UTl1mKNvqeRlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران تن به توافق ندهد، کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق را می‌زنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، روز سه‌شنبه گفت که گفت‌وگوهای خوبی با ایران در جریان است، اما بار دیگر تهدید کرد که اگر تهران با آمریکا به توافق نرسد، تأسیسات زیرزمینی در کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق ایران را هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز اعلام کرد که در صورت امکان ترجیح می‌دهد پل‌ها و نیروگاه‌های برق ایران را هدف قرار ندهد.
ترامپ توضیح داد: «من می‌توانم همه نیروگاه‌های برق آنها را ظرف یک روز از کار بیندازم. تمام نیروگاه‌های برق آنها از بین خواهند رفت. فکر می‌کنم حدود ۹۱ میلیون نفر باید بدون برق و بدون پل زندگی کنند. و این یک توازن بسیار، بسیار ظریف است.»
او تصریح کرد: «آنها می‌دانند که اگر توافق نکنند، من این کار را انجام خواهم داد.»
دونالد ترامپ هشدار داد: «می‌توانم بگویم ظرف دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همگی نابود خواهند شد و نیروگاه‌های برق هم ظرف یک روز.»
او افزود: «اگر بتوانم از انجام این کار اجتناب کنم، ترجیح می‌دهم از آن اجتناب کنم.»
رئیس‌جمهور آمریکا همچنین با اشاره به تفاهم‌نامه امضا شده بین واشینگتن و تهران در خرداد ماه که در درگیری‌های تیرماه به آستانه فروپاشی رسید، گفت: «ما دیگر نمی‌توانیم اجازه دهیم آنها توافق‌ها را نقض کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/77568" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bnOAJwslKBKbrusNK_FH6C6G_mP8g0-0M-Eb-TOkId8sEFpJhCw6Ix1woA-7Z_k0c6H5RVbzXN6tc3xOMQAc56DUd9jwbYaF5wsR_5kkN27JpFWpcJoV1K24jU-RGNmA8r4u4auSMubm4-FUq0RJIEUm5QEP4ntttSB6LeF1t_n-_Sg2dNkSZ10WLJbVoA2jnDZ7gKbU6A7J1KEayyIaInSteEMZmcoY6RnMH34AD87LMqYKY9tV9uTJuhlORWw_QFiaAR-afqNa3PU84xjkLDrga5PLFUimi5NQOsXk844AgkMFOaxX_fP49sL2zWuvwmcJuJ_M_jZjZnkz75ugvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmQFZsaeC4ERLYS4dKbxtrxMwmpJpgjCyPy8kSqmrP_ljMheZPeqodam1Fl5BbQjXOI9Xnr2Su1IAyeVEGkAFbkp4M70OC1kz-0uh4n4SfN8UyLEI5Oah7AOKOHDqQHpwK8TgbrErh1wMf4-Rt4dgiPjmddm_K2tRju3RchQsSoWJ_2Cn-iovne_TfIJp7EK1b13Szf5dEHv84DAa38mHI2apJgXrpI_XK28Z8i0n3sKE-N8pTNLPDql7vIAhLWwnJ8_ZWPeE_7MfRXJu3ZrJ_eKJw47tt1zdeGR3NmVlCu9inlG3mVqEnsw1T7iSc8GGd7DlRYVWVoM_l1571U8eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل روز سه‌شنبه ششم مردادماه در مصاحبه‌ای با کانال ۱۴ تلویزیون این کشور گفت که در هفته‌های اخیر، جت‌های جنگنده و بمب‌افکن‌های نیروی هوایی ایالات متحده از پایگاه‌های هوایی اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
کاتز گفت: «ایرانی‌ها می‌دانند» که این جت‌ها از اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
به گزارش اورشلیم‌ پست، کاتز در این مصاحبه گفت: «امپراتوری مغروری که اسرائیل را به نابودی تهدید می‌کرد، فروپاشیده است.»
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در کنفرانس امنیتی کانال ۱۴ با اشاره به دیدار دونالد ترامپ، رییس‌جمهوری آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واشینگتن گفت آمریکا در موضوع ایران منافعی دارد که فراتر از منافع اسرائیل است و افزود: «بسیار مایلیم به ایران حمله کنیم، اما آمریکا موافق نیست.»
کاتز با اشاره به آنچه دستاوردهای اسرائیل در برابر جمهوری اسلامی خواند، گفت: «امپراتوری متکبری که اسرائیل را به نابودی تهدید می‌کرد، در هم شکسته است.» او تهدید کرد: «اگر به سوی اسرائیل شلیک شود، با تمام قدرت حمله خواهیم کرد. ما آماده‌ایم با توان خودمان به ایران ضربه بزنیم.»
وزیر دفاع اسرائیل در پاسخ به پرسشی درباره واکنش احتمالی اسرائیل به پهپادی که روز سه‌شنبه از عراق پرتاب و در مرز اردن رهگیری شد، گفت: «ما می‌دانیم چگونه امور را مدیریت کنیم؛ آماده‌ایم.»
کاتز همچنین گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، «درک می‌کند که اسرائیل از مناطق حائل در لبنان، غزه و سوریه عقب‌نشینی نخواهد کرد». او افزود: «هفته گذشته از غزه بازدید کردم؛ هنوز تونل‌های بسیار بزرگی در آنجا وجود دارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/77566" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjzV6-sJOfOpJZdASU4P4cpkOCz0Fd0SodGHDZknwXd5sQuIYeM3U94kVtCyM7b9o3ZoIqwl_G9xWFJO-uWT3UwBZwLnXtEZYvvC3eRxuH9mjiPRzjf264df1s3arvA4m2YtK1Fcdj_Xi0PY6IAeHmQ2MiaqkHijj0_1A0-N3TkRDgaLsnppUSOFwlgR-QI6YiG7NEFW17oFGfFovJWsmjDq82r85A1mmRQyh_2ewP6GKaHvXybM5GHg2KpWRnBRkt-ACDuHCUDip41XFRGnQa6Y0aqlkqLRJ_yL7vHZNy9S31de4kpbXYsEoAZh8fAhr7e2SpJM0wtaggQMbp9mcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه می‌گوید که حمله اوکراین به کشتی ایرانی در دریای خزر «باید به‌عنوان حمله به خود ایران» تلقی شود.
دیمیتری پسکوف، سخنگوی کرملین، هشدار داد که این حمله نشان می‌دهد که از بین بردن «تهدید ناشی از کی‌یف» تا چه اندازه اهمیت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/77565" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFExAu33eTzsm1jAT8RJl13A58QDIcyV4PUFR1Q4L5BZgb-6rUdsFc4_MzXCEYp4lsDcWE0bI9URax_5SVvHSAz5ST2w9ASLOQIRkWjL6zePrMWdv5ItGiF3el2YYlLd9Bguuo1MGd5-eTkNi37BES8JZfNn8RraL4y4g3g7enuwOcNfh3oAsaXXmbX2UzUoJ2YciLlAp2nDWJRxYGHhNBiCuicaF7q6obqduPmgiqMAZL_weR2uLX4-pM5GESxX_GBNUf7QNWXP4soNkILbZJlEifdBvPmGZTe-pqfwK1JVI6lvvl0yjfeSwVhK5R3usy8Yp_6ZxVCKaJj-A-OElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس برنامه‌های اعلام شده از سوی کاخ سفید، دونالد ترامپ، رئیس جمهوری ایالات متحده، روز سه‌شنبه ششم مردادماه، با رئیس‌جمهوری اوکراین و سپس با نخست‌وزیر اسرائیل دیدار خواهد کرد.
دیدار ترامپ با ولودیمیر زلنسکی ساعت ۹:۳۰ و دیدار با بنیامین نتانیاهو ساعت ۱۱ صبح به وقت محلی برگزار می‌شود. برنامه روزانه کاخ سفید نشان می‌دهد که این دیدارها بدون حضور خبرنگاران برگزار خواهد شد.
با این حال انتظار می‌رود که پرزیدنت ترامپ، در لحظه آخر اجازه حضور خبرنگاران را صادر کند.
برنامه بعدی ترامپ پس از دیدار با نتانیاهو، حضور در مراسم یادبود لیندسی گراهام، سناتور جمهوری‌خواه فقید است و نخست‌ وزیر اسرائیل نیز در این مراسم حضور خواهد یافت.
پیشتر نتانیاهو اعلام کرده بود که موضوع ایران در صدر گفت‌وگوهایش با پرزیدنت ترامپ قرار دارد.
دیدار ترامپ و زلنسکی نیز پس از آن برگزار می‌شود که شامگاه شنبه سوم مردادماه، نیروهای اوکراین شناورهایی حامل محموله‌های نظامی جمهوری اسلامی به روسیه را در دریای خزر هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/77564" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GAJ0hCH6-A7R_7Yc5aXWNIG0E5UxjzKcriaaqSdcV-TikCQsf2jsDnHfp22OaEK2TUq6s3KE3YS2ZJ6MijA4sV2ry_FO0g_Tg289b-ZydgdL71S5DxfclVsOK38cdpkV1C4TpTMgmAFNAJvd7_DHvG3vegr3p_ni0TLU4Nb2_jkwW5qioID3CGixc7uoOnOv-_0d75FdOlvNzR9QxaKBwb9HAJt7Osq4isbwDmBx-5j6FFui3G1MkbtL0X25kIwq1HWUICcvOBeYAvEdxeyNdcRgic0Y9Qhoyo8klcUIqbedaoqWrOfWrnwet-BfKNMZBQ45Ff7MBnk5VfdEoWMSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاسین سرفراز، بوکسور ۱۷ ساله اهل بجنورد و عضو تیم ملی بوکس ایران، که در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت شده بود، به سه سال و سه ماه حبس محکوم شده است.
کمیته آزادی زندانیان سیاسی خبر داد، پرونده این ورزشکار نوجوان در شعبه چهارم دادگاه کیفری استان خراسان شمالی رسیدگی شده و او تنها در یک جلسه دادگاه، بدون دسترسی و حق انتخاب وکیل، به اتهام «اجتماع و تبانی علیه امنیت ملی» به سه سال و سه ماه زندان محکوم شده است. این حکم حدود پنج روز پیش به او ابلاغ شده است.
یاسین سرفراز از ورزشکاران شناخته‌شده بوکس ایران به شمار می‌رود و پیش از بازداشت، در رقابت‌های کشوری، آسیایی و بین‌المللی موفق به کسب عناوین قهرمانی شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/77563" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f473hTWC0ns_TRXrx6Ya807KXmJKjp9yelDSxboTrnhVac1vxBcMFTPLQLvkfzhRgc_HZLJTxNQATeEwABtG_VOOdYXJBeNFHOsm7u2-kNYQAi5JyK-7N-eTDv39rioELXDNObvFriObIF5g8U-M23-dkTxBsfwrbyO_PtuYzZoWltZsufejBwbCLcsqmB6BBn7PX5cKaHW-ssQRsguWtDGNLlrPBUFNDyjTC7riQo3RMtI-G9OjWfjZBIGfSAw_51-PR63HloqfVsgbcvnjwFlto0NRKlE26ILD2GwAb2rlVDOD55G-2V6FHEKUUB9OWcSjkW_od6G7wl4ZMPyp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز سه‌شنبه ششم مرداد به نقل از یک منبع آگاه در خلیج فارس گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
به گفته این منبع که نامش اعلام نشده، پیشنهاد عمان مورد حمایت کشورهای منطقه است و بر اساس آن ایران کنترل انحصاری این آبراه حیاتی را در دست نخواهد داشت.
این پیشنهاد الگو گرفته از نحوه مدیریت تنگه مالاکا بین دو کشور مالزی و اندونزی است و بر اساس آن، عبور از این آبراه با پرداخت داوطلبانه هزینه در تأمین مالی ناوبری، حفاظت از محیط زیست و جستجو و نجات همراه است.
عمان پیشتر به طور رسمی اعلام کرده است که با مدیریت متفاوت تنگه هرمز به شکلی که ایران می‌خواهد موافق نیست و پیروی قوانین بین‌المللی خواهد بود.
پیشتر مقام‌های ایران تأیید کرده بودند که مذاکراتی را با مقام‌های عمان در زمینه مدیریت بر تنگه هرمز انجام داده‌اند. سخنگوی وزارت خارجه ایران هم روز دوشنبه تأکید کرده بود که در حال حاضر تنها مذاکره‌ای که ایران در آن دخیل است مذاکره با عمان درباره تنگه هرمز است.
دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که این کشور «مذاکرات خوبی» با ایران داشته و احتمال توافق وجود دارد، اما او هشدار داد که اگر مذاکرات به نتیجه نرسد، حملات ایالات متحده از سر گرفته خواهد شد.
در همین حال، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه با همتایان عمانی و سعودی خود در مورد تنگه هرمز گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/77562" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t_6xtGPApYpVRHxQV41HSYdGdwFh0Bcq4bYRwlCIGZYoCWGAJSXDhW6yHDUNnOaKe96locB1qGhfRiid-v8K2rSeCOjQMskNAoeuTMAxczZeP6viauEmWmZ8qoATmx3YhI9QjxUbQIeb1vYdV8E6Oi_HeDyagOgql-n0L6YitnSB4C3orHls_2vM5IQCL_03r6faG1VmWnRhrtMZ4Z7uY3RG6vVhHSPwJHsxuvnPtcGYSxRh_pdQQFcI8_UcmZ_G7yaeWszAx-dTJJln2t0JSJhOCUDafO6eJKVRy-xE63LlHomf3pSS_EHJIVwjqDsWcFDb1jomo17C483uB6OQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J0-_AkqfBV15io5FcrGhEnl9pC6tw5F5zs_8QoBqmUtJM-St83Ny8IaSI8EXzYFfHWHK213Kcij4hkC40n-JRtNuj7vCdSAyAwhg3rfyr76MA0O_ovpHW-P3YsVdfmW5yVAJzbtcjOcIGDzcIqI3zza6ikGC2iHS2qOZ8H3EBR5a9R_9LsBtOraxJoADRv6EP6lK26nMD1mG1oF5mtAF6N41zXrLLUCR7SfPsWoVPmxtrImHMzw71mkRSxYxHe702_NP7DDa07oo1H2m8Pn3dBh_5BwIlv6wBylVIDXjjOwiShEorSgB3_KH-xYGo7isvHOIOIeorPYJF9ljWQhNDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قائم حسینی، امیرحسین ملکی و علی دشتی، متهمان پرونده میدان علیخانی اصفهان، در آستانه اجرای حکم اعدام قرار دارند.
از خانواده‌های این معترضان دی خواسته شده برای آخرین ملاقات به زندان مراجعه کنند.
قائم حسینی پسرعمه گل‌محمد محمدی است که ۲۸ تیر اعدام شد.
این پرونده ۱۲ متهم دارد که علاوه بر محمدی، تاکنون سه تن دیگر از آنان به نام‌های عرفان اسفندیاری، ابوالفضل سپاهی و امیرحسین صفری نیز اعدام شده‌اند.
@
VahidOOnLine
شروین باقری، از معترضان پرونده اصفهان، در آستانه اجرای حکم اعدام قرار دارد.
به خانواده‌ او گفته شده برای آخرین ملاقات به زندان مراجعه کنند. شروین باقری نیز در حال انتقال به سلول انفرادی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/77560" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cIq8k6MicziPrhMT6UJvBBvxVF5V80rvfggsFba8HuIG4VYByU4RgPAi1SqCt1jd6O6HcAWnB_qnl0sPiDtpNdVZ3ivl27hy5FSlE2CJzeSeIlKLcU2OcLZLLZ3Jqfc88dCMckgXtBW0Feqe0pvTEYY2WSqh53WpQw_QqoroEEMfFRva80MI8KFdGH00gUf9mxP3kUwf8xpqcFAy7GT3aZOu_PFnJG8FDJwrZVVTBKRlcJGKRdCMQ2VvWny2qwoGLLDdvKOZ4SHTP02zibpo5ghzEiNvNxfKIfWlCd7jMClkZl73IuLYYP_mj9XqGU1vgcWVS8iqlEJ_GwvZtn2tPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی بدون نام بردن از کسی نوشتند سه نفر از پرونده ملک شهر اصفهان اعدام شدند.
آپدیت:
بعدا ویرایش کردند نوشتند: دو نفر
آپدیت:
قوه قضاییه جمهوری اسلامی اعلام کرد بامداد سه‌شنبه حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو معترض بازداشت شده در اعتراضات دی‌ماه در اصفهان، اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77559" target="_blank">📅 05:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=rIrr5-MgLa0htOmHm42N8IFJa7A1Qhc64Y5Mmb5vVN-0Z4fpKVqivS4y5wFcYMmAvBZyxFtmxTEHjVfIEp4Sg0GCpiC3tcAjUT47YSc6wJRg3E10sDUiY4gxO-p4rMQr6vIRe-u9d-kge_2HOS0Q6qHgGw36xtZTCMZlwuDoAvid2alr6JpWYk9G9Kc5iquA_9tgVG_eE4d0oSqM5Agmdpf5O7BlmYbSDPEaH-RhLRPCUABttdOaZa_yDJNfKf3nKyDLF1A2kfAzWxfQDtCx5QOv22uXmLAUIMnT2FbFrhGaztRNt9BtFMHAHBnTSvShANAYl-IETJZmIoQxRFSDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=rIrr5-MgLa0htOmHm42N8IFJa7A1Qhc64Y5Mmb5vVN-0Z4fpKVqivS4y5wFcYMmAvBZyxFtmxTEHjVfIEp4Sg0GCpiC3tcAjUT47YSc6wJRg3E10sDUiY4gxO-p4rMQr6vIRe-u9d-kge_2HOS0Q6qHgGw36xtZTCMZlwuDoAvid2alr6JpWYk9G9Kc5iquA_9tgVG_eE4d0oSqM5Agmdpf5O7BlmYbSDPEaH-RhLRPCUABttdOaZa_yDJNfKf3nKyDLF1A2kfAzWxfQDtCx5QOv22uXmLAUIMnT2FbFrhGaztRNt9BtFMHAHBnTSvShANAYl-IETJZmIoQxRFSDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار منتشر شده در شبکه‌های اجتماعی حاکی از آن است که خانواده‌های زندانیان سیاسی محکوم به اعدام و شهروندان در میدان علیخانی اصفهان تجمع کرده‌اند و گزارش‌هایی نیز از درگیری یگان ویژه جمهوری اسلامی با معترضان منتشر شده است
این گزارش‌ها می‌گویند نیروهای یگان ویژه جمهوری اسلامی با موتور، خودروهای زرهی و سلاح‌های سنگین در محدوده محل اجرای اعدام مستقر شده‌اند و اینترنت در اصفهان دچار اختلال شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77552" target="_blank">📅 05:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SXhkZuO742YgNI254KQ6wGIoj3QE3jfmkEJvKLhpiev8QlihU4AMVRIA-NXkQ78f7ZD4ip-0Qg53OHNzSbghlcvt6GQMPe44DcCAkBKiss23U5hXVQW1chfdyIdkL5gFaDyFHOMDIPW75OnEOzBoBV8NjtM7qGCzs5I4ZfGZwdbYefbUhBEkCBZBHOeQMr4g-AlQKOJ8fTMbPfnlMl6Za5CMMw3VR08BWNDjYJKnNS3GeXsRgeEouOBWy6WtNW0WURgLOS9HZvSvzVgXImoPnWkzFeUghqPo9LhmtG2B9L0sErdjxOUn-P_DAZubyAfU8bAk2E0hFOFX-kTkmJzyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DQwAS5Q68xPG6JdmUJQ13xgZEPv7pS9LoGekD7ZeBKCljquGaxpBbVnoqSfyTS2oaHsAKJzUOfTbIO0_7FolwgLt8ixnTdv7ZvUWBBAUzwCY8uaB55pbnxE3usA7XVjyJr5gZOyDokbQxbAURE2_Kn_H57tV_XM_Bg5yu6K3BDwEBXogX6sqW1nKg4jP49uI569dnlnrj4GPsYJBXqLIBsnzOcob4SrBUbprcx7S23qYR_osGLiY_YtfmSJSmFcbn354utHE8B4bsjybdIeRNHrjTdjJ3j7VvoN2TEnnhSk_gNso-2BcqyWbwW2ohiT4kSjfeDLzHuNeN1qa-Zfb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tw8TUfpvJrllQXpTNhFGTQZc-oyWQHi2fEefUdkziE8Q_lJeLrW08xHdrhA9IjD1azBHXOEwJWXgoHGPZ2YkDUyKo1P5CaS-qIIDgUERb_wiNgx-M7wz0eNIhpHEcwFLYoohJX5bNqi8QlwMuLR_WZJTkxO6inuaWeId55xFqTHIPBs28oUbiFwtt9AM1RtDXP9Ag_5fN21J57ZOkq8kNhInGy9KoqTx1Uu7Gl_Z8AppryrTB3Tlkaw0tix2zl3rWslNDS5CcA9yjSY-dMCbBcAGyJnUmkVNrxiO3p8XiqAiLpx-6MH-J9Xl-pJazDE9NUBkFSwtBjR-jo2IrNjzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XufiJhYQedwjCis42nMDvgZOiDY9aL978Pe0CAwburIyiMWCfje7FTbpIZWeZRxZsuuxFPZRwK41dpnKPNJyl2J4IetE74wJOmYI3s9BB69ro3TfKo4QdYSn6v3SZE4QWtTEZiVDGJxAfZ_VPxqADdXjCqcxOhTpP8kQrMP2BZ7gw6Va6QZHVGIbG2NFXFBOps3Xtpetove0MMC97Z75ZC9hSrCqPteYluD5UUIHMMYJ8C8JXix46pGYuLBqvtxRCIgcFlZ8iQT6EyVFRASWarA52nZZVnhMCUU6P9D8EfY6nkfP-6ZFtL7LzhSWZbn9qmmgr20JyEg8dGSPZbwQPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faf260cfea.mp4?token=qyArcBlA4QUGc0MQpf0tBOK7nF2DrVsT7XOML-Y-bUN4dFAojQQVrwGWowCRnP9BDwD4cWA0M3eBpqHJvYOgrtjLi919iH1EaovQdrhfjDHj4gTzFsZXdNEJJ2EdUTaw1V0g-rk2iKS-TevrXAiJjz7OUgBSZy1yQPhw8yOIs9Q2c71sxF9ubqMW_FO_oQOVUuB8pTf6iPbRvBzbLJ04u69OZ6IdYSwBpGrJrn0hrudPPRxxv12xI9yY567SrTv1DEj6e2wZSfJlIjQAJGWqWKsnlxvmWbR9XN4i8McI83ba7P_2tATBh_EBflgfRjyzcZmLsgq6ielxt1269mEEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faf260cfea.mp4?token=qyArcBlA4QUGc0MQpf0tBOK7nF2DrVsT7XOML-Y-bUN4dFAojQQVrwGWowCRnP9BDwD4cWA0M3eBpqHJvYOgrtjLi919iH1EaovQdrhfjDHj4gTzFsZXdNEJJ2EdUTaw1V0g-rk2iKS-TevrXAiJjz7OUgBSZy1yQPhw8yOIs9Q2c71sxF9ubqMW_FO_oQOVUuB8pTf6iPbRvBzbLJ04u69OZ6IdYSwBpGrJrn0hrudPPRxxv12xI9yY567SrTv1DEj6e2wZSfJlIjQAJGWqWKsnlxvmWbR9XN4i8McI83ba7P_2tATBh_EBflgfRjyzcZmLsgq6ielxt1269mEEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.   «علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای…</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77545" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=dG9Vx3-whWE8su5Aw22MB4Ngtpzurannw14E6tu91uI16TIVzs_hS3UUOfOyXlUX1hfwKaXhY0IM8OP6dEuUwyVkJEddqQKePnY4B7uxy4aYXaa-ZXDqtCQq_sdEVaItGDaqGvFL7HoFL5Xkxit4lIAZo02fnDqOM23oZacaGtzreSOXKiZKmzb671Kq9yTEudzX6_2WyOlWOlOtT0NB-Kgdm8ulQ0cCK0gfIxDySYnY2WOsWsXrk9KA0W_NT3BtDLrFW49SNoY8xx0rslxWkcOzz-O6N8yNE_NYEarlU4bZ90heEnJBy35E6gtupH_05mF6QWs_730tZ9M_qSZQ1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=dG9Vx3-whWE8su5Aw22MB4Ngtpzurannw14E6tu91uI16TIVzs_hS3UUOfOyXlUX1hfwKaXhY0IM8OP6dEuUwyVkJEddqQKePnY4B7uxy4aYXaa-ZXDqtCQq_sdEVaItGDaqGvFL7HoFL5Xkxit4lIAZo02fnDqOM23oZacaGtzreSOXKiZKmzb671Kq9yTEudzX6_2WyOlWOlOtT0NB-Kgdm8ulQ0cCK0gfIxDySYnY2WOsWsXrk9KA0W_NT3BtDLrFW49SNoY8xx0rslxWkcOzz-O6N8yNE_NYEarlU4bZ90heEnJBy35E6gtupH_05mF6QWs_730tZ9M_qSZQ1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از سخنرانی ترامپ در میشیگان:
- آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
- همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
ترجمه ماشین:
ترامپ: ... ونزوئلا.. پس از آنکه تقریباً ظرف ۴۸ دقیقه پیروز شدیم، گفتند: «اوه، حرکت خوبی بود.» خب، همین اتفاق اکنون در ایران در حال رخ‌دادن است.
مردم هنوز متوجه نمی‌شوند. ما نیروی دریایی‌شان را نابود کرده‌ایم. نیروی هوایی‌شان را نابود کرده‌ایم. رهبری‌شان را نابود کرده‌ایم. تسلیحات ضدهوایی‌شان را نابود کرده‌ایم.
پهپادهایشان اکنون با حدود هفت درصد ظرفیت قبلی تولید می‌شوند. بخش عمدهٔ توانایی تولید پهپاد و توانایی تولید موشکشان را نابود کرده‌ایم.
اکنون با ما دربارهٔ دستیابی به یک توافق صحبت می‌کنند؛ اما اگر ما این کار را انجام نداده بودیم، هیچ مذاکره‌ای در کار نبود.
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
آن‌ها قلدر خاورمیانه و قلدر ما بودند. اوباما ۱٫۷ میلیارد دلار پول نقد سبز به آن‌ها داد. یادتان هست؟ پول‌ها را داخل یک بوئینگ ۷۵۷ گذاشتند و به تهران فرستادند؛ ۱٫۷ میلیارد دلار پول نقد.
او تصور می‌کرد می‌تواند به آن‌ها رشوه بدهد؛ اما آن‌ها در عوض با خودشان گفتند: «این کشور چقدر احمق است.»
نه، نمی‌توانید به آن‌ها رشوه بدهید. باید شکستشان بدهید و ما داریم حسابی شکستشان می‌دهیم. اما خواهیم دید نتیجه چه می‌شود.
اکنون مذاکراتی بسیار دوستانه در جریان است.
نیروی دریایی ما در اجرای محاصره چقدر خوب عمل کرده است؟ حتی یک قایق [نتوانسته عبور کند]. آن‌ها می‌گویند: «دیگر محاصره را نمی‌خواهیم. لطفاً، لطفاً، محاصره نکنید.»
---
ترامپ:
اکنون قیمت تخم‌مرغ بسیار پایین‌تر از زمانی است که کار را آغاز کردیم. خواهید دید پس از آنکه تهدید هسته‌ای ایران را از میان برداریم ــ که بسیار زود اتفاق خواهد افتاد ــ اوضاع چگونه خواهد شد.
اما افزایش قیمت‌ها ربطی به من نداشت.
---
یکی از سخنرانان همراه ترامپ:
۴۷ سال طول کشید تا کسی بایستد و بگوید دیوانه‌ها نباید سلاح هسته‌ای داشته باشند.
همچنین چندین دهه طول کشید تا مشاغل را دوباره به داخل کشور بازگردانیم.
---
ترامپ:
نمی‌توانستیم اجازه دهیم آنچه در ونزوئلا اتفاق می‌افتاد ادامه پیدا کند و اقدامی که انجام شد بسیار قاطع بود.
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
اما هزینهٔ عملیات ونزوئلا، همان‌طور که گفتند، تاکنون جبران شده است. به همین ترتیب، در برابر جمهوری اسلامی ایران نیز با اختلاف زیادی در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز به سلاح هسته‌ای دست پیدا نکنند.
وقتی کسی می‌پرسد: «چرا این کار را انجام می‌دهیم؟» پاسخ این است که نمی‌توانیم اجازه دهیم شما سلاح هسته‌ای داشته باشید. همین تنها چیزی است که لازم است بگوییم.
اگر قدرت سلاح‌های هسته‌ای را درک می‌کردید، دقیقاً متوجه می‌شدید که چه می‌گویم.
---
بار دیگر می‌گویم: ایران هرگز سلاح هسته‌ای نخواهد داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77544" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ویدیوی مصاحبه ترامپ با زیرنویس فارسی در پایین همین پست
متن بخش‌هایی از مکالمه، ترجمه ماشین
:
🔺
خبرنگار:
درباره جنگ ایران؛ آیا از پیت هگست، وزیر دفاع، به‌دلیل توصیه‌هایی که در اوایل جنگ به شما داد و نتیجه‌ای که جنگ پیدا کرده، ناامید یا عصبانی شده‌اید؟
🔻
ترامپ:
نه، به‌نظر من او کار فوق‌العاده‌ای انجام داده است.
ما ارتش آن‌ها را تقریباً نابود کرده‌ایم.
آن‌ها می‌خواهند دیدار کنند و ما هم داریم با آن‌ها دیدار می‌کنیم. خواهیم دید چه اتفاقی می‌افتد. این احتمال وجود دارد که بتوانیم به توافق برسیم.
بدون کاری که ما انجام دادیم، حتی حاضر نبودند با ما صحبت کنند. آن‌ها هم از طریق واسطه‌هایشان و هم مستقیماً درخواست دیدار کردند و ما داریم با آن‌ها مذاکره می‌کنیم. می‌دانید، ممکن است اتفاق‌های خوبی بیفتد.
فکر می‌کنم قیمت نفت امروز به‌شدت پایین آمد. تا حدود یک ساعت پیش هم بازار سهام سر به فلک کشیده بود. اما نه، آن‌ها درخواست دیدار کردند. اگر عملکرد ما ضعیف بود، درخواست دیدار نمی‌کردند.
تنها دلیل اینکه می‌خواهند ملاقات کنند این است که ما ضربات بسیار سنگینی به آن‌ها زده‌ایم.
🔺
خبرنگار:
چقدر دیگر در برابر ایران صبر خواهید کرد؟
🔻
ترامپ:
وقت زیادی دارم؛ وقت بسیار زیادی.
تمام نوار ساحلی‌شان نابود شده است. تنگه در وضعیت بسیار خوبی قرار دارد و همین حالا هم در حال مذاکره هستیم.
می‌دانید، آن‌ها می‌خواستند صحبت کنند. افرادشان گفتند: «لطفاً بمب نریزید. دیشب و شب قبل شلیک نکنید؛ دو شب این کار را نکنید.»
می‌دانید، گفت‌وگوهای خوبی داریم. بنابراین خواهیم دید چه اتفاقی می‌افتد.
فکر می‌کنم احتمال خوبی وجود دارد که اتفاقی بیفتد. اگر چنین شود، خوب است. اگر نشود، دوباره به همان کاری برمی‌گردیم که دو روز پیش انجام می‌دادیم.
🔺
خبرنگار:
آقای رئیس‌جمهور، ارتباطات با حوثی‌ها درباره دریای سرخ چگونه بوده است؟ آیا نگران...
🔻
ترامپ:
حوثی‌ها؟ این مشکلی بود که مدتی پیش با آن روبه‌رو بودیم و همان‌طور که می‌دانید، حسابی آن‌ها را درهم کوبیدیم. بعد از آن دیگر هیچ مشکلی با حوثی‌ها نداشتیم. اما در حال حاضر در آن موضوع دخالتی نداریم.
البته ممکن است دخالت کنیم. می‌دانید، اگر مشکل‌ساز شوند، احتمالاً مجبور خواهیم شد وارد عمل شویم.
🔺
خبرنگار:
درباره عربستان سعودی؛ آیا نشانه‌ای از عربستان دریافت کرده‌اید که به پیمان‌های ابراهیم بپیوندد؟
🔻
ترامپ:
هنوز درباره آن صحبت نکرده‌ایم.
🔺
خبرنگار:
در صورت گسترش درگیری، آیا نگران کاهش ذخایر مهمات هستید؟
🔻
ترامپ:
ذخایر زیادی داریم. انواع مختلفی از مهمات در اختیار داریم. می‌دانید، بایدن مقدار زیادی از آن‌ها را به اوکراین داد و ما اکنون در حال بازسازی آن ذخایر هستیم؛ اما همچنان مقدار زیادی داریم.
از تسلیحات رده‌میانی هم مقدار زیادی داریم؛ بیشتر از آنچه در هر شرایطی بتوانیم مصرف کنیم. مقدار زیادی داریم. صادقانه بگویم، دوست دارم مقدار بیشتری داشته باشیم، اما بایدن حجم بسیار زیادی را به اوکراین داد.
وقتی من رفتم، انبارها پر بودند.
وقتی پس از اوباما به ریاست‌جمهوری رسیدم، او مهمات نخریده بود و ذخایر بسیار کمی داشتیم. من آن ذخایر را بازسازی کردم. اما به‌محض اینکه رفتم، آن‌ها مقدار زیادی از آن را به اوکراین دادند؛ ارقامی که هیچ‌کس پیش از آن ندیده بود.
بنابراین اکنون با سرعت بسیار زیادی در حال تولید هستیم. کارخانه‌ها در حال ساخته‌شدن‌اند و تجهیزات بسیار زیادی تولید می‌شود. به‌خصوص تولید سامانه‌های پاتریوت در حال افزایش است.
ذخایر زیادی داریم. هرکدام از پیمانکاران ما همین حالا در حال ساخت چهار یا پنج کارخانه هستند. وضعیت بسیار خوبی داریم، اما قطعاً دوست داریم از برخی تجهیزات پیشرفته‌تر مقدار بیشتری داشته باشیم. بایدن مقدار زیادی از آن‌ها را بخشید.
...
🔺
خبرنگار دیگری:
شما و نخست‌وزیر نتانیاهو درباره ایران هم‌نظر هستید؟
🔻
ترامپ:
تقریباً. بله، تقریباً. اختلاف کوچکی داریم، اما در مجموع تقریباً هم‌نظر هستیم.
می‌دانید، ایران طی ۱۴ روز گذشته ضربات بسیار سنگینی خورد و آن‌ها خیلی مؤدبانه از ما خواستند: «لطفاً متوقف شوید. بیایید مذاکره کنیم.»
اکنون در همین نقطه قرار داریم. خواهیم دید چه اتفاقی می‌افتد. اگر به توافق نرسیم، دوباره همان کار را از سر می‌گیریم.
🔺
خبرنگار:
رئیس‌جمهور زلنسکی می‌گوید روسیه تصاویر ماهواره‌ای پایگاه‌های آمریکا در خلیج فارس را در اختیار ایران قرار می‌دهد تا به آن‌ها در هدف‌گیری کمک کند. درباره این موضوع چه کاری می‌توانید انجام دهید؟
🔻
ترامپ:
بررسی خواهیم کرد که آیا این موضوع حقیقت دارد یا نه. از پوتین درباره آن سؤال می‌کنم. خواهیم فهمید.
اگر چنین کاری انجام شده باشد، تأثیر چندانی نداشته است، چون ما آن‌ها را حسابی درهم کوبیده‌ایم. این‌طور فکر نمی‌کنید؟
ببینید، روس‌ها تجهیزات زیادی در اختیار ونزوئلا قرار دادند. تمام تجهیزات ونزوئلا روسی بود. نتیجه‌اش چه شد؟ چندان خوب نبود.
بنابراین ممکن است تجهیزاتی داده باشند، اما اگر چنین کرده‌اند، موفق نبوده است؛ چون آن‌ها دیگر ارتش، نیروی هوایی، نیروی دریایی یا هیچ‌چیز دیگری ندارند. بنابراین نتیجه خوبی نداشته است.
فکر نمی‌کنم روسیه چنین کاری کرده باشد؛ دست‌کم نه در سطحی گسترده. اگر هم کرده باشد، بسیار بی‌اثر بوده است.
....
🔺
خبرنگار:
درباره دارایی‌های ایران؛ گفته بودید دارایی‌های ایران برای پرداخت خسارت کشتی‌هایی که در تنگه هدف قرار گرفته‌اند استفاده خواهد شد. آیا ایالات متحده مستقیماً به شرکت‌های کشتیرانی پول پرداخت خواهد کرد؟
🔻
ترامپ:
نه، نه.
از پول ایران برای پرداخت خسارت‌هایی استفاده می‌کنیم که خودشان ایجاد کرده‌اند.
به‌عبارت دیگر، پول ایران که تحت کنترل ماست برای پرداخت خسارت‌ها مصرف خواهد شد. خوب به‌نظر می‌رسد، نه؟ بد نیست، درست است؟
همین‌طور هم باید باشد.
🔻
ترامپ:
بسیار خوب، سؤال دیگری هست؟
....
صادقانه بگویم، با بسیاری از کشورهایی که بدون ما دوام نمی‌آورند بسیار مهربانانه رفتار می‌کنیم.
می‌دانید چه کشوری بدون ما دوام نمی‌آورد؟ اسرائیل.
بی‌بی دارد می‌آید؛ خودش این را به شما خواهد گفت. اگر من دخالت نکرده بودم و آن تأسیسات هسته‌ای را که عملاً در آستانه تولید سلاح هسته‌ای بودند، به قول خودم، به خاک تبدیل نکرده بودم، اسرائیل چند ماه پیش نابود شده بود.
سال‌ها پیش هم اگر آن توافق وحشتناک اوباما را لغو نکرده بودم، اسرائیل نابود شده بود.
🔺
خبرنگار:
نخست‌وزیر نتانیاهو درباره فروش جنگنده‌های اف‌ـ۳۵ به ترکیه با شما اختلاف‌نظر دارد. نتانیاهو با تحویل اف‌ـ۳۵ به ترکیه مخالف است. آیا قصد دارید به او بگویید...
🔻
ترامپ:
نه. ببینید، ترکیه برای من متحد بسیار خوبی بوده است. فکر می‌کنم او [اردوغان] کار بسیار خوبی انجام داده؛ در سوریه هم عملکرد خوبی داشت.
او دوست من است و هیچ‌کس به من نمی‌گوید چه چیزی را باید بفروشیم یا نفروشیم.
ترکیه برای من متحد فوق‌العاده‌ای بوده است. البته ترکیه طرفدار پر و پا قرص اسرائیل نیست. این را می‌دانید، درست است؟ او طرفدار بی‌بی هم نیست، اما ترکیه برای من عالی بوده است.
ضمناً ترکیه کشور بسیار قدرتمندی است. ارتشی عظیم و بسیار قدرتمند دارد و تجهیزات بسیار خوبی در اختیار دارد.
🔺
خبرنگار:
آیا نتانیاهو از شما می‌خواهد با ایران توافق کنید یا می‌خواهد حملات را ادامه دهید؟
🔻
ترامپ:
بی‌بی واقعاً عالی بوده است. نمی‌خواهم بگویم کدام گزینه را ترجیح می‌دهد. او نخست‌وزیری در دوران جنگ بوده و ما در کنار یکدیگر عملکرد بسیار خوبی داشتیم.
اگر امروز به ایران نگاه کنید، قدرتش فقط هشت درصد چیزی است که چهار ماه پیش بود؛ هشت درصد چیزی که چهار ماه پیش بود.
خواهیم دید در نهایت نتیجه این وضعیت چه خواهد شد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77543" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: اگر مذاکرات با ایران شکست بخورد، آماده «اقدام نظامی شدید» هستم
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه به اکسیوس گفت که تصمیم گرفته است حملات آمریکا به ایران را متوقف کند تا فرصت دیگری به مذاکرات بدهد؛ اما تأکید کرد که اگر دیپلماسی شکست بخورد، ممکن است دستور ازسرگیری عملیات نظامی گسترده را صادر کند.
چرا مهم است:
مذاکرات کنونی بر دستیابی به توافقی جدید متمرکز است که تنگه هرمز را بازگشایی کند و گفت‌وگوها درباره یک توافق جامع هسته‌ای را از سر بگیرد.
▪️
مذاکرات عمدتاً میان ایران و عمان انجام می‌شود؛ اما قطر، پاکستان، مصر و فرستادگان ترامپ، استیو ویتکاف و جرد کوشنر، نیز فعالانه در آن مشارکت دارند.
آنچه او می‌گوید:
ترامپ در این مصاحبه گفت: «ما در حال مذاکراتی بسیار جدی و عمیق با ایران هستیم. اگر این مذاکرات به نتیجه نرسد، بار دیگر به اقدامات نظامی بسیار شدید روی خواهیم آورد.»
▪️
وقتی از رئیس‌جمهوری پرسیده شد تا چه مدت حاضر است به دیپلماسی فرصت بدهد، پاسخ داد: «زمان زیادی نه. یا باید سریع پیش برود، یا اصلاً پیش نخواهد رفت.»
پشت صحنه:
ترامپ گفت روز جمعه تصمیم گرفت حملات را متوقف کند، زیرا کشورهای میانجی از او خواستند فرصت دیگری به مذاکرات بدهد.
▪️
ترامپ گفت: «همه کسانی که با ایران سروکار دارند از من خواستند: "حمله نکن."» او تأکید کرد که به باورش ایران خواهان دستیابی به توافق است.
در میان سطرها:
ترامپ در توضیح اینکه چرا با درخواست میانجی‌ها موافقت کرد، گفت: «نه چیزی به دست آمد و نه چیزی از دست رفت.»
▪️
او خاطرنشان کرد که پس از توقف حملات، قیمت نفت کاهش یافت و بازار سهام رشد کرد.
آنچه باید زیر نظر داشت:
ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
▪️
ترامپ گفت: «می‌خواهم با بی‌بی درباره این واقعیت صحبت کنم که اگر من رئیس‌جمهوری نبودم، ایران تا الان به سلاح هسته‌ای دست یافته بود و اسرائیل نابود شده بود.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77542" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxu8eD4WIURdy9zrh0pegnZLETkq8vbdqqhBxx40veaaWJKAMTlewslyZEtKd0aPTLrjzKy99oJgiZToucY9A2mOPpQQcVmXgBHS56ZlRJ8lFHLBcV_BLByJh237tq018MaOTJnm9OALIfaG4FzviaUQDak04ILyk9dsDWXYTAaSRGkW8cqgmuA8BQ2E4rLUcu27TF_rVMV2ekIcaHsYxgfYobGDRwwn0C2L8uK9otgpiHiAa08gu4K3FiRtFRhoIuzY1JqBtIPVqYATh9X8j5PcEkaT92OQ9O6GzUftzUGn0XlQFH8EDgSRK-P_jW8f3CQw3oYtHlqqvIhH22tUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای «حوثی» یمن، وابسته به جمهوری اسلامی اعلام کردند با استفاده از پهپاد، تعدادی از مراکز انتقال نفت خام عربستان را در مسیر انتقال نفت از شرق این کشور به بندر ینبع هدف قرار داده‌اند.
«یحیی سریع»، سخنگوی نیروهای مسلح یمن، دوشنبه ۵مرداد۱۴۰۵ مدعی شد که این حملات در واکنش به آنچه «نقض حریم هوایی یمن توسط پهپادهای سعودی» خوانده، انجام شده است.
در مقابل، وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور تعدادی پهپاد مهاجم را که به گفته ریاض «از سوی گروه‌های مسلح مورد حمایت جمهوری اسلامی» و «از حریم هوایی عراق» به پرواز درآمده بودند، رهگیری و منهدم کرده است.
به گفته این وزارتخانه، این پهپادها قصد حمله به تاسیسات نفتی در منطقه شرقی عربستان و شهر ریاض را داشتند.
وزارت دفاع عربستان تاکید کرده که براساس «حق مشروع دفاع از خود»، پاسخ به این حملات را در زمان و مکان مناسب، حق محفوظ خود می‌داند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد. این وزارتخانه از دولت عراق خواست تمامی اقدامات لازم را L«برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی» انجام دهد. درخواستی که به نظر می‌رسد اشاره‌ای غیرمستقیم به نقش جمهوری اسلامی در حملات به عربستان دارد.
همزمان، خبرگزاری‌های نزدیک به سپاه پاسداران، از جمله تسنیم، با انتشار تصاویری مدعی شدند حملات ترکیبی پهپادی و موشکی حوثی‌ها موجب آتش‌سوزی در تاسیسات نفتی بقیق، یکی از مهم‌ترین مراکز فرآوری نفت جهان، شده است. تسنیم این حمله را «ضربه مهلک نیروهای یمن به اقتصاد عربستان» توصیف کرد.
با این حال، مقام‌های عربستان تاکنون وقوع حمله موفق به تاسیسات بقیق یا آتش‌سوزی در این مرکز را تایید نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77541" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJxAODDhtZSCZxwInt56TOXBDpX8Qu0Sa2deYBMG0-vWlOkEoh1stQAS5A1plhyUR13nGWsfcpVYgT3NRQFz2C5KwE90YRNGZHv9pX3cRMXMnryv_leoRVKbHpDaLcnumN8Izw7PgVHFqhxX8reBtaaRBaeyNme1JJX_Gke_0KdsSDJILCqmXIYzosYCPx0_dC0cLVLxewSqb59TiPi9wdd1KTREAfnTIYx99CdOc9gWWpvIzwfTr-IdG0qePsbn-690cI_mvdd9SFcZEtGS1ZDwx1TTzBOKmvxfQCLfiTqdIVr8lEkN8HesHVpJ_ipA9PkEV1uVuHpVsbTQpMDS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر امور خارجه اوکراین  در واکنش به
پست عباس عراقچی
ترجمه ماشین:
تهدیدهای ایران ناموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین سلاح برای جنگ جنایت‌کارانه مسکو ــ سلاح‌هایی که از سال ۲۰۲۲ تاکنون اوکراینی‌ها را کشته‌اند ــ به آن دامن می‌زند.
ایران هیچ جایگاهی ندارد که خود را قربانی جلوه دهد، چه رسد به اینکه بخواهد تهدیدهایش را با ارجاع‌های مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات می‌کوشد توجه‌ها را از اقدامات تروریستی روسیه علیه کشتیرانی غیرنظامی در دریای سیاه منحرف کند؛ اقداماتی که امنیت غذایی جهان را تهدید می‌کند. اما موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنشی قاطع از سوی جامعه بین‌المللی داریم.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77540" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef1qWuO9KumrVFYAEk3dr3IXAJr_NH7Nck0zFl8eMiYPFZMT7vOi94EoTHbDnMqnnqthF0KDk5Q3t6Gw_-zSs7aUKvNST6YZWzX9zu3B3XT6CLDNcToI6YGe2APJoXMVpaZwLiIpoVOgZB5CpcivfWZTPHW-Jmq4d6Y4uqwPc-DzJKiYEcYsKSS4B7--s5GhX1t6mUdO8_0mFASYBc8JnyZRfwMWk823a8G0GO3C7OBEW1eOl6CNQIXu_WwhPF6hmMiIOZjN9yQxH0u57BkhsoDnApZHbi43wa6oeD8qRzcSLyZSXOcBey1pHV_3qwHWdYKLNJQS-rZ4hF0gB7rdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی روز دوشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور، پهپادهایی را که از عراق به‌سوی تأسیسات نفتی در استان شرقی عربستان و همچنین شهر ریاض پرتاب شده بودند، رهگیری و منهدم کرده‌اند.
این وزارتخانه اعلام کرد که این پهپادها توسط گروه‌های شبه‌نظامی مورد حمایت ایران در عراق به پرواز درآمده بودند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد و بار دیگر بر حق این کشور برای پاسخ به منشأ «تجاوز» و بازدارندگی در برابر عاملان آن تأکید کرد.
این وزارتخانه همچنین از دولت عراق خواست تمامی اقدامات لازم را برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی انجام دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77539" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQrh_ZZPh8oESYH30qdQlSqnjc3ZSlqQC4kAZAVfnatahDuaUVNwYdMZ8h3ICt-RkzIzMDUnhbQtjRBANoXDTuCUFadJ0k_6cvfuGVSfNuXCaDybN0-Jbw3GEPZCisU8k2vUKNEtKOMSZq-pRlc8VetfWXDoO-dT8g9t88v_cfGPwZUtPfJ7tRbnqmtffSWQ9C9vXF81wPqcaaWKtD06w38PNDBQzHJ70VTDRfU-TKfFAQmBQ-0Oe7spQw1eY1_FQnbLvp0xBweAKR2KCRgMUp8T1qiSBDwwH32z5F8XRpx74wLFD9xn4JD9rk3-z9iaTOyQvTFz0tmDfS4AgQFECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح اردن اعلام کردند که صبح دوشنبه دو پهپاد را رهگیری و سرنگون کرده‌اند.
این بیانیه مشخص نکرده است که چه کسی این پهپادها را به پرواز درآورده است.
کمی پیشتر، تایمز اسرائیل گزارش داد که ارتش این کشور دو پهپاد مشکوک را بر فراز مرز اردن رهگیری کرده است.
در آن گزارش نیز درباره منشا شلیک این پهپادها و زمان دقیق رهگیری آنها توضیحی داده نشده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77538" target="_blank">📅 17:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThYHJ9TmiSZpZX-xNPyeuMZsvSKQ7nDPEl3CH5gf-eQPbmM9SwuKHzjhGMhdcJT-Or9hEP5SAajcqLWldHgEwblYHj-4wPSbHaNicfZ66rChKIZhkoA4d5iRyva3GXJjdk-ALn3AoXbVLI9-5GkVZl_oMLWZJCBvOQrcSccz75bNice47axYUrF5ZVR57bDKlX5yKBKLUhdXRGIFwMaJqJKE8lhBeNgHA2DMLPbQSHkFp3roFnfBYzcLEJA9oOtLahJEHw0XEYDqkORn0Oz4zS7e9ZvUHmc0hCdYrdubvuSpsidwvzhouUyBllo4D3qCLRLptuXfe_ynr6Gaasewmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«احمد الشرع»، رییس‌جمهور سوریه، روز دوشنبه ۵مرداد۱۴۰۵ در گفت‌وگو با شبکه «الجزیره» اعلام کرد دمشق با مشارکت چند کشور در حال تلاش برای دستیابی به یک توافق امنیتی با اسراییل است.
الشرع ابراز امیدواری کرده که چنین توافقی بتواند زمینه را برای دستیابی به «صلحی فراگیر» فراهم کند، بدون آنکه «حق سوریه بر بلندی‌های جولان» نادیده گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77537" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce_xiBnNeS59KZg5f9v_mZTlyRbi4cSETEhENyZNE3xLh93k_10_y_8ZhzHpzvun3R6x6y-Fx9Hvvnuf-r4qknB0m6y-VWzhH8IJ0_6pg69KmiklZwa5g3eRipaIMk1M7ub0S_778ZjEtrZ0qUlnCHO8f1Q1GCqgpGwwgmMhxP3c5d4ezkCB_7Q3nPmz9ObyOQzIb2-ykz9ju9mEAa7drayZ4wAyOpZ8Ohn_naZ1jwF_PkXU0s_kDBxRIW7IItssiKi2rA4sGCzOEbKNdVyE1jwc436Ero1UgrFxrxo3yq2E4ofCujrTUc9eWyAQSDaGbXPxHuLzAAQwrWpzIk3OoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل، می‌گوید هرگاه دوباره به نخست‌وزیری برسد، «فورا» قطر را کشوری «متخاصم» اعلام خواهد کرد.
آقای بنت در شبکه ایکس، دولت قطر را «خشن» و «سرطان یهودستیز» توصیف کرد که «شاخک‌هایش را در سرتاسر غرب و حتی در دفتر نخست‌وزیری اسرائیل دراز کرده است.»
او همچنین مدعی شد که در دوران نخست‌وزیریش، اطلاعاتی را دیده است که نشان می‌دهد قطر به سپاه پاسداران کمک مالی می‌کرده است.
این سیاستمدار راست افراطی که از چهره‌های اصلی اپوزیسیون اسرائیل است، قطر را متهم کرد به‌دنبال «نابودی» اسرائیل است.
آقای بنت نوشت که قطر «کشور پیچیده‌ای نیست، میلیاردها دلار در یک شبکه نفوذ قدرتمند جهانی سرمایه‌گذاری کرده است که صدمه زیادی به اسرائیل وارد می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77536" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWxCTSGoPu13dHkOZezvhgIVwEpeog4Zj7dWomCOJIeZrykSp8LMuWArhFHdU2-3yILvfT6VMI6f-jtMpYw89akO5Ve8qmCHaxAQIi6spn9ulk7nSoDnJlAVtB1tn8NYWHSXzCZ9Bd2RFZywW2pw1rqSr4lMPVEF2y66EPqJk7DDUL41K2hOfKPKanAoNt_ccn7XtzVJVXEjQmqy9FeaxbXLLc0P1RKuZqiS9eKccU3o5xMKr69xHeJvViEq3zQSBWvibTqFy7x2LbdMclsiyX8r2WKhS9Sdsa7Ry9A05rAPxjbPIWEJytEM5sCuOQDZ4i4Fy-8wTVJFigPqELxpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع بریتانیا گفت کشورش از اقدام تهاجمی در برابر جمهوری اسلامی حمایت نکرده و نخواهد کرد.
وس استریتینگ در مصاحبه با شبکه اسکای‌نیوز افزود این موضع را در نخستین هفته کاری خود صریحاً به پیت هگست، همتای آمریکایی‌اش، گفته است.
استریتینگ روز ۲۹ تیر و در جریان تشکیل کابینه اندی برنهام، نخست‌وزیر جدید بریتانیا، این سمت را بر عهده گرفت. او در همان هفته با هگست درباره امنیت دریایی در تنگه هرمز و تعهدات ناتو گفت‌وگو کرد.
او گفت با وجود این، زمینه‌های فراوانی برای همکاری دو کشور از تأمین امنیت تنگه هرمز و جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تا سرمایه‌گذاری در توان نظامی بریتانیا و ناتو وجود دارد.
استریتینگ همچنین گفت اروپا روزی از دونالد ترامپ، رئیس‌جمهوری آمریکا، سپاسگزار خواهد بود که قاره را از رخوت بیرون کشید و متحدان ناتو را وادار کرد مسئولیت امنیت خود را بپذیرند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77535" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rl-EupEEX4icthfNmjmf-yK2d8o9rn6g6GJ1SrgNQNCS7weGDHZEq48Cwx40ZECJbIYMUsQS62Yb59YEhWq1Yes_NN3Vppr8CfBUyaqJ89xR3bZ9aaqEXVCPVY8vwMkY2PdpJjmRltiMXMp77LWcLTzIc4S_shYihsKeOk5Z7LXu_7fjxMIALLIKSsrdqkJnfJK-teAP9OTHfr6TxOMGD3uTNyQLz2uEQKDgG4k4ROrDh9Jr2ARir5LUUJhFbG0SsL6LQK0DW1HtVt6hWDqIbAzGLsF02hBa-U_5FbGJM6JHyPniG8V11PnLLZKwzOuuo3G01GqqTdpzJBjspvXAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77534" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKzKLe585JsNDVonRAo474zzmTDipvpItnNtxvxRWGL60pxgjc6umTFZip-tODgq5KSUgoMfZ6qnl6PcgB5MH-8TbXhdS59L05iXhFNQv41jP3minjnqwyUxNn-iv-uPRL7d7LFCl5zl8ZSSoooKMxGEo975DbC0Avk3dLDlpjyr1oA9r6BL-ePheJGGZrePfCOdhq5-cJhrDxY8e1lWTy9EqVF_tC5zKbGmkRVaC6_P4-G8UUKtQRndnPgqViXR9l3v0iBIddjp44K5VgMAoHLttlbhI8iUlJeNeaCI7GIqjKftXdUCzNXfEna06eu9Fs614UDO3UzDaZlDyoLkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، دوشنبه ۵مرداد۱۴۰۵ در نشست هفتگی خود با خبرنگاران، گزارش‌ها درباره درخواست ایران برای مذاکره مستقیم با آمریکا را رد کرد و گفت: «درخواست مذاکرات مستقیم با آمریکا اصلا با ژن ما همخوانی ندارد.»
او تاکید کرد که در حال حاضر هیچ مذاکره‌ای میان تهران و واشنگتن جریان ندارد و خبرهای مربوط به درخواست ایران برای مذاکره، «خبرسازی» طرف‌های مقابل است.
بقایی با بیان اینکه جمهوری اسلامی هرگز از دیپلماسی برای صیانت از منافع ملی خود گریزان نبوده، گفت در شرایطی که آمریکا به گفته او همچنان به اقدامات «ایذایی و تجاوز» علیه ایران ادامه می‌دهد، تمرکز جمهوری اسلامی بر دفاع است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/77533" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXy1nmoIRK8rOBorbD9a1icTZjIIVY04p_Tc6uC6SOT1N3FM39Bk3Uoc0-vcbgPb79Vl2JcSub4w5Y0jTZhEugL251TceBPS3EF42sis03yU9YYznLM1pfyiJ3__61-wsvTm7kOgaVCHhFYI-yA0jrRzhe9yK8JeDegHNrorfGhsm9DcWcGDoSsGwAOjMvorDDhsGgJj6v-n7v2UA17gVIZylfWMXli3Bppk_Mso4Ss0UAbOs5qnxF858J1OekBva3hZqnigfvwo-6kiIV7cayxwKJM1MfKnotp0R8MAjZ3ldQ9GltxgnJzPo5Xms1lTGWDgPO-CaQzkUkaB4NqixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون حکومتی ایران روز دوشنبه پنجم مرداد خبر داد که سپاه پاسداران در بامداد همین روز مانع عبور شش کشتی از تنگه هرمز به قصد خروج از خلیج فارس شده است.
خبرگزاری صداوسیما در کانال تلگرام خود نوشت: «در ساعات اولیه بامداد امروز دوشنبه ۵ مردادماه، ۶ فروند کشتی متخلف با خاموش نمودن سامانه های ناوبری و موقعیت‌یاب خود... قصد عبور از مسیر غیرقانونی و نا ایمن جنوب تنگه هرمز را داشتند.»
اشاره این خبر به بخش جنوبی تنگه هرمز نزدیک به سواحل کشور عمان است که اعلام کرده تابع قوانین بین‌المللی برای استفاده از آبراه‌هاست. ایران در مقابل اصرار دارد که کشتی‌ها باید از مسیری که سپاه تعیین می‌کند عبور و مرور کنند.
خبرگزاری صداوسیما همچنین نوشته است که یکی از این شش کشتی‌ «دچار حادثه شده» است، اما تاکنون هیچ منبع دیگری این خبر را تأیید نکرده است.
روز یک‌شنبه هم خبرگزاری تسنیم، نزدیک به سپاه پاسداران، مدعی شده بود که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/77532" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIhagkiCoHnF_fdYADlsf1iQBnzVuEM3rhd674niRsiLm51r07hWi0e1fxTHm8Yzr9AvpFeW6he3N_1qcbXI07bUgowQN8N2c6neZCrkjtQ-ygVgu81nT87Wz1hgYNGYpfvtP-v_QYZI6kbiBG-zpaJzFSCi3-rqctrZ-6jCgbtuA-12ojToiuapRQHvKUSVz2txL6lwS6rIfylHKtfknhaqgACVHEbxoPFGdctBxA3miaNDnSwq7hSqeRFfPrR8Lax2i3JOYaHhogr7p0AIlr21rwOn-NIR7rzRfr8EGGDx9C62VOz4TRADcEbtwsDnbyDDZ-Yy85-R5tGa-JNxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت امتداد گزارش داد حکم محکومیت پژمان جمشیدی به تحمل ۹۹ ضربه شلاق به اتهام «رابطه نامشروع» پس از رسیدگی در دیوان عالی کشور به طور قطعی تایید شده است.
الهه محمدی، خبرنگار امتداد، به نقل از ملیکا پارسا دوست، شاکی این پرونده، نوشت شعبه نهم دادگاه کیفری یک تهران این حکم را صادر کرده و پس از اعتراض و فرجام‌خواهی، شعبه ۲۹ دیوان عالی کشور نیز رای صادره را عینا تایید کرده است.
بر اساس این گزارش، اتهام مطرح شده در پرونده بر مبنای ماده ۶۳۷ قانون مجازات اسلامی (بخش تعزیرات) بررسی شده است. طبق این ماده، مجازات رابطه نامشروع تا ۹۹ ضربه شلاق است و در مواردی که عمل با اکراه و عنف انجام شده باشد، این مجازات تنها برای فرد اکراه‌کننده در نظر گرفته می‌شود. به گفته امتداد، دادگاه کیفری یک و دیوان عالی کشور در این پرونده تنها پژمان جمشیدی را به تحمل ۹۹ ضربه شلاق محکوم کرده‌اند.
ملیکا پارسادوست با اشاره به قطعی شدن این حکم گفت صدور رای نهایی نشان می‌دهد «فضاسازی‌های دروغین» درباره این پرونده، پایه و اساسی نداشته است.
او همچنین تاکید کرد اجازه نخواهد داد آنچه بر او گذشته با روایت‌های دیگر بازتعریف شود و گفت از ابتدا این اتفاق را «خشونت جنسی» توصیف کرده است.
پارسادوست در ادامه گفت هرچند این حکم از آسیب‌های وارد شده به او نمی‌کاهد، اما در شرایطی که به گفته او اثبات خشونت جنسی در ایران دشوار است، احراز این موضوع از سوی دادگاه که رابطه «بدون رضایت و همراه با اکراه و عنف» بوده، برای او و دیگر زنانی که تجربه مشابه داشته‌اند اهمیت دارد.
او در پایان با اشاره به کاستی‌های قانونی و دشواری‌های پیگیری چنین پرونده‌هایی گفت با وجود مخالفت شخصی‌اش با اجرای مجازات‌های بدنی، پرونده را تا پایان پیگیری خواهد کرد و ابراز امیدواری کرد این پرونده زنان دیگری را که با خشونت جنسی روبه‌رو شده‌اند، به شکستن سکوت تشویق کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77531" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khyr-wjgXIcDmYGsyFV0yxBQmuUNQ2pRA49z4K1UaLPqaDa7Yvea0ozPTrApipMWL1g2gL6LQIHjs0C03zV4CWsw2zd2TjLxXswO5nW0JE66dHalqSp35Ig7EQBoSNTlKCMjuTcRrZGfSGknTl69XklPcLW9KvWihh3Dv1MDVB03XZmiO5ATBUZzGNRbaAuMPFUY1HLJ2xvjPdsYbUuZmEScoRZ6U-Zlgc4zUQKFi64EFVBLb0hmzYap2rkDWEFYnPocs7T4XdFw9HSqW2pNE8xk7VvP_UhjsUy4__pIZ8MdpoPbmw8Xyw1ym2ydZzGggroirr29T19bQip_alawxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش خبرگزاری «رویترز»، همزمان با ادامه وقفه در درگیری‌های مستقیم میان ایران و آمریکا، بازارهای جهانی روز دوشنبه با «کاهش قیمت نفت»، «افت ارزش دلار» و «رشد محتاطانه بازارهای سهام» واکنش نشان دادند؛ در حالی که داده‌های حمل‌ونقل دریایی از ادامه اختلال در مسیرهای کشتیرانی منطقه حکایت دارد.
بهای نفت خام برنت بیش از چهار درصد کاهش یافت و به حدود ۹۲ دلار در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز بیش از پنج درصد افت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77530" target="_blank">📅 16:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J2ix2fUkvhpRvIvq_F0R44mXvDABtEylk6PPeTK-D2tzUunjwNfz0s1J_UgjgFp6dYcibIMOCNyKpLpWlPEN-gjXhRV0rFvp8PTiTgiVhmi8WxHqfXkfQ0QI3d1ZYiJNfnRSGUdytjaCm8aA86DA-R78rAijuGj_PpQX-OpUUQdGuWwiVP66_hM39WHA5x5tGsr9aobk9vGdsolqt8xOjBXfnp66lkEgMuvJV38cFuGUdQj9HAjNMh1KmrdYVSF2peHKuMZXFPQOeHsRM4AdndLa8-crxVddvttC0gG8wRf_JJQyPkVxgYCOB4Ch9Tm05uewH_KVb4grSm2R0PddRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در بیانیه‌ای که به روزنامه وال‌استریت جورنال فرستاده، گزارش‌ها درباره کاهش ذخایر مهمات این کشور را رد کرد و گفت ایالات متحده «بسیار بیشتر از هر کشور دیگری» مهمات در اختیار دارد و میزان آن نیز «بسیار فراتر» از نیازهایش است.
بنابر گزارش‌های دو روز اخیر، ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، کاخ سفید را در جریان کاهش ذخایر موشک‌های رهگیر پدافند هوایی قرار داده است. این موضوع برای او نگران‌کننده است، هرچند معتقد است پایین بودن ذخایر مانع ازسرگیری عملیات رزمی گسترده علیه ایران نخواهد شد، اما خطرات آن را افزایش می‌دهد.
چند مقام آمریکایی نیز به وال‌استریت جورنال گفتند دریاسالار برد کوپر، فرمانده سنتکام، معتقد است آمریکا می‌تواند با محدودیت ذخایر پاتریوت و دیگر رهگیرهای پدافند هوایی کنار بیاید، زیرا در صورت تأیید ترامپ، افزایش حملات آمریکا توان ایران برای شلیک شمار زیادی موشک را کاهش خواهد داد.
کارولین لویت، سخنگوی کاخ سفید، و شان پارنل، سخنگوی ارشد پنتاگون، تأکید کرده‌اند ارتش آمریکا برای اجرای هر مأموریتی که ترامپ انتخاب کند، تمام امکانات لازم را در اختیار دارد.
وزارت دفاع آمریکا شامگاه جمعه کارزار تازه خود در بمباران مواضع در ایران را پس از ۱۳ روز حملات هوایی شدید متوقف کرد و تا امروز، بامداد دوشنبه حمله‌ای از سوی آمریکا گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77529" target="_blank">📅 16:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiLKrIg44xz8VLD2lE6k4vYBwdngp1e2AwfGbaRIBpW3eX5RZ0lL79kcqh8VXIOMTReMJTeZRCjnX9Hx7gduVaWnJmjGx6qjvA4xdmRRLalbUu9ecVH-2VrUCeSUoHlMYa8Qv4qgcpPn4mGp0Zr57zqy5tS1SVqmc1_Dr5j2WmUN_siYqS9nxdnPupuRhthow8TVtHFSLPYZLzHdNGEpqiPLf8J9ba5QkSFqwcubYZ4iVL_wVUFPTD1-8Eq4d0QvtRWrMHtF0TB3Qp4f7IFPdjNgdoqJmamCYlPuQL5CpTURG0m4M03-pO66BN1N3hSvtEWmZA49dKRtTlATO2leFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.
«علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای حکم آن‌ها در صبح سه‌شنبه ۶مرداد۱۴۰۵ بسیار جدی است.
همچنین به ایران‌وایر گفته شده است که «سمیه افشار»، مادر علیرضا سپاهی و مادر همسر ابوالفضل سپاهی، در همین پرونده به پنج سال حبس محکوم شده و هم‌اکنون دوران محکومیت خود را در زندان سپری می‌کند.
اطلاعات موجود در حال حاضر تنها درباره وضعیت این دو محکوم تایید شده است. با این حال، از آنجا که چند متهم دیگر این پرونده نیز با حکم اعدام روبه‌رو هستند، این احتمال وجود دارد که افراد دیگری نیز برای آخرین ملاقات فراخوانده شده و در معرض اجرای حکم قرار گرفته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77528" target="_blank">📅 16:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DQ5hSsoYKujX4YuLDh1l63JBxBJBarK1Xh8v9nOb5JahkLM-NsT6jifd-GUBZAhEBah6qWIq3y57Ypv5Qe9Q7ksFiSTjT6DhVxScA_emM5W4ihhE-RcqkCLerL9kmnpPC1hgTc0AKwInZXVWMMnftY7IbQESoAuoUUOq3a3bh6S0e6r3-DihsQfNLufU5eyAkIj3fQA6ZwTZNlvFgMcm6ng6KWyP1ixWl6Kxvk2ot-F6QNqycKlInT9dFHLqR46sZWcVbVfHTXUas62sSqAS6g2UOc5FVrr034m8Aj06dTdYnB_Teq5nvTtVMR4F7hA3WfFs1EIOrmvKDR7VIiGiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OrXIR4Do4XlilX-GvPnp3iWw0eFM5mhhjwG778Wbri8aG9aihLNvLSsPw2Dj67wHgzJ-SK3GFUH2pWmy0xSjDM5vbtFJ80zX4_LnKgAD6ySTzDx5HSfW4w5moKIe3Cytk3NH_jkisrFzl8Ik8SCjDsaYKS6tEBzC3sC_X6dflv9y2I0Na3AzM6Td2cgIul6KbbZ8iqMG43eapP7-xaBf_5pK3yjTmVUZObfFQkyYOh8F4c5ch-Hqegt6twSPtL3kRIVlKwJrMu9oFiFAp_yb8OIuzT_TlHLg1a6oWav80eBE-h7tp5YqtFwyQpdXmtITIliWJfyjdQ9eRPpw2zD6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZwZ_P-I6MA_gL8NqjNLXSySHE3JXidl8NNuWYWEZS0jyDGNZQGs83lriHoY0tFD96YRTYdUpK5pPVKDLwPFx_xZLhhBKFU89XvYTpXNYO-AJJ6T2Es1n4qLwdskBgrebVxJ50wlJYEU8M2W0aYVMEcx6OHKUATFKOAXIj0eFxvMcuCmANMpLErKIOGbSLdKGI3GdklNu2i8PIO9BXg_RiraSJP-T6H2r6u29bmbBZCXixinOdyTZKb0sfHS7MQbKMQERbTx_tLVd43WPxr5FXhjovnF0Kdsunx9bj7MmkbZkLbIr5ozTnOhvbM55nAMb5URfHf8SyZ3LTipc6qpBtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qpe_byk512XkKl1d1Al_0NUIHOj449mdNJ65ENbbSbuz3K280i_fufllPh0eHYq76ZXaE7HeWNGAghw1Ypmeyet8XrGk8qtDSsomP7EeN_mra2eNxrmrkrUmyQo8JNXMuinNoZnHQ3NAieM4BeQM7nKF_DlkCX9HoQek4MPITMuVczihSwDVi0WLkEIpsGGvWyIb7TcsKwmxKlQHadnKQ5Ta9TpBGv0GrRWnIgjJnCH5lLI9zJqfcWmN6pKu2NyuuZkYodNApUzmmE2ut4sIgU4S93Y-2-pSaFYWmeCOMm5q_CQroLNLDBnp-ilUZh-xNOiqe5CldQ4e7G7wAajwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7k-bxhkQl3gc5LHrU9ctjVUMwToZ-yDyOmvbVa0sJYaMbrF6RoSZ4ZwhQXzDKRH6nb4_YIq5xZ8U6VDsBPicC_G8WsBDsgTaENOU9HgOCtPi6OV1ftsLWvRbk3JdtKOqB8gwsnZNtgzJMVcvYCYTb88Kds42p89ebM3rOhauChIFgVOC16nQp2FbAvFaV6bkkBpDMmNQDlwsZ4enuXgIcVSV3wTTldE9tanFsMGoVo1COCgZlNeLdjhlrinudzPmDxOEyoFVAdHD42vcJJk-lz4eW48c02YRdYSMyo-RFlVgNWBPh-Z2jB_SVsK93VbtaxuAZF-xBAdl9lBTpoYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kMJeJQ1znMWiRpHrzFebqUpjrKSP4LncbKRQn4bmUevCMu49CypGFt9H-ktGecUx8sry8xwfieo4lo2_Gj729wnHCuviFTO2sNYaVtWB7l0CR6jy-55UzAO4R4X-sIZBOb0GMUsI1DIEsV5d60URUTutTHh54WghcouOz8PKnkvtedG1hwcvf9gjNXg4qMD6oRe79Q07urawQsuZBlQl-O9x_AEJ--qCu72JPhkZf92XPVpOc1ACx6079o87Cs19iPCskrPeQ7g54b2li6qOxJrdAJGNCdYqu13Sn-nTgcGI9KXCneAr0jyk8WnMpHzhFMf7qrGO3jApNVlwuNV4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y0iXKlRhSm-u71h9DbE2i03aLJWS7PYLK8i_s0oHGhBHR0m2bZhRlN0Usc1YofFYOeCxtGmXAHoHnbg8K5QwMVefcDp3bSbwdeC4Pt-C0bNgCT746xiQ3cy9mT2g3zci8aAkSjxbntos5AGFaPGAd8zITLx1PjNY-hnOELPT73NOWB9AtXiGYPf6JUV_NQq7buNwmBEqXOko24qFGiOiLnxW362JBXXWhi_QVkLH6ZyX1sIDanxTq0yYVXBd8ouC2X9Ow7I0ZNkP3OR8jCyLZMfvR7CK769kuI9wLxPY6h-ilzZoF0xVGhpX6rz4sO-ExHZ8Jd4NlHD0dwPegsSNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lHnqDZakrbJUZerTMCXpNg5o_kHNSqZYtMhBdqZ3T-wcd897sjMZsiff0IfgMVVDNrXgX3mZ2cTn9ly6BHekrWyLRCAghDR9Zkh-CHbCZK1NGyhh8h6LkLy_oGMBrWjCvZXazJ7jRcQUN7RUYYmomoBhjTg-IXQsUcVY7wAdRm40_QHvoeL4tgJw7GjPRDoplcjPVjerOl2D4gxXuiB3qmJy8DL8eMlDqbCeCMj9_J7xH0YqlbvWD0XtI5kNakWUzUvVDz9vOS6OgAvPNO_LdloQxHl-uvLG7lVVyRbj5ckacM_Goennoiy91Geg5IzXEc3W9gxYnES7-ZtJE5g6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OWTEnUBenxc9aXQjmzrXlOxuURxQdnX7htizDUp_Lhq8YPOoDW45DLksyHlnwoGW5Dxu0k4NKNJHrJxAUxX0frHnLW6QVEsJFHXp08M4hpF78Zy1BQOqB6f8eBhgq7lZjXtXlW8_4y09CBNgFlucnqms9Kz1hvc-f81jEU9TOR0CpzGS2YlmswDJmnm7MjI-YEcf3uToSs11SkgsmNPmHe0E2mJR374EDAQcGK6GgOPql_QMZELUCJG3b62QBWgPzszyItGiCzeEKEDy3rrMs9CACXhygdy0h5DyTzq93CiNv8VgmLJRQeELL5auvrBkQ-SAmpbcEYYlti7Va4zZrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه تصاویری ساخته‌شده با هوش مصنوعی را در «تروث سوشال» منتشر کرد.
در این طرح‌های گرافیکی که با عبارت‌هایی نظیر «این نفتکش اکنون متعلق به ماست»، «خداحافظ اتاق موتور» و «دیگر موتوری در کار نیست» همراه شده‌اند، صحنه‌هایی از انهدام و آتش‌سوزی ناوها و نفتکش‌های جمهوری اسلامی ایران و حضور نمادین او به همراه نیروهای آمریکایی بر روی شناورهای توقیف‌شده شبیه‌سازی شده است.
او پیش از این نیز تصویری گرافیکی از «حمله به خارگ» منتشر کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77519" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bk4j6OhvO0AJZKxn7R9Zzsfhl98LokM4QeWa7NByI-55ALSbRM2LRZ8UbnmngVHKctmtZWevFe0O94jXL3jmyoxw5JVyJ_ZMHYnO6yF024j9xtL8SuaSbE9oWuKHv1XIh_gJMdY3UpMNoxrAO5hus1jrkA31vM5G67AYr0hftpI6nh3cEZqFWW3fHnnNvmWF3qzQsWFpfzWSNTwA-SN7iDGyqM0yrG0urKORLjoTYFrHTCxB8giMg_7MDWfSrbLJxXBjfPH2LPJ20m2yS1PCIDzXJaEG5fDKLrZvKtuGJfMKBiG-Lxv7P6-OpF5ZqPVGYwEngLTubxdosVPPuNGSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C5bSQiwwojlmdKgdZXdRBuO6VB6L2qWV8a6DOpXq8Tqhqcocxp8smMH05UDFBXp2uDthAyFQM0PirAXleZbSJ_5CfVw4woURPCqb9x8oGLnNwRe57TkMSm-a6u3kBKnRQndI-3Uwg7We-r8V_B2h5Yu-9J2qjFAaIPNmDSlRZ4Pva3TirHuNm9GVMaD7ihwRmW1VBL0hWjA6OM15rxSqyrxLX-8fQ_2WJgO3huMlQly6bha-Q_S_SUJTrzAd5q61X_jzARlMbAHJZX0RjUn0pcBjnEOwbis_1_OGAsbaddaPElxwmzXyqyDkBwNEscJY1sEgDsVAO2uZ27lYuS1Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RiHO37sLExrIumEYt_LpOiv4I6oD9um7UvtHdLz2EFO03Keey2YBgQWIKwitVNU-FiUPRE3yEBG835CodANCfjYNenYaywus0BKHSJTaxaZkTOaMhcWb2b82tTE8qq95SfYouXVcN--wi5hdlKdjymkmLGXzmz7HWqtJymEQOOGsj8lclu5tMrINZ1wjqd979_-1MRLRzjdaL3PPv9ZfOMEdPbuQ69mzsAyCqt1m9v47abagoZM0X-TNvcasgt86r9i9TAOjvLztS0dKK2_R2z8i6opGpNBzI0cekll0spFVN37SHB5D82c0ataUFyyG3U_lDd3WcPl3gA5KHXLY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GtT1Hx3iUzS1U5j8-9IHO0LWyA2IsUPuQ3YT-gocw7fEWAV_ho0_1Qgns_Qk1FlUHMNEvwMsTNmWPhK68OqoU7ZxDxs3uvLUWjEMbIN5Hnt5fk4jXeM6GBndU7JsxBcfEfbpCyBca8i2EcgGK6CI3fs8TF1woTYHRPLV5sn4kmCDO8j84qc70hXCNAnYV9K0Fft_yQ7NkFwxmU1EX2VDv6y0r8bg7tt_yjS1ADXluEV6loapBNohAah9qoMQgfg-_tug_pD8153v1eNK_IXbQuyEwKWQT49AsWcFJ-hKTteGtKDoYGEEWvMvAZzdjHCo1Law4RiiYthAToNYdP4clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G4TyYbhn3gefpAJTSQW_NG-WyX_v6aUwr78RwiAOcTgLbHnUI9BDxkmk6sSYJf91BqG12W--7LoGvwRkbvYs_Hzbuc0z8oG2LpnrYrQSZDs-AxWOa-rPgDHbCu0-MfcSEK6e8744YDHgBgf6MEFI6wRglWBSB5QLjz8B8TiS4Cq1vUw2cZJ11dycua_FHWTpRNi6hb4FC5kpJiNZeLeEQwAzfnpaH1q2KQOiP5OKxbbXgSBy7cw_HxhEACpcTP5Y8LGgeSI5miAH4UMGpU9XL9qfSAKopbkbMykyQ3niKcDczvNBbGZSEvgPPV1nwwoKYFAvTh7NQYSmwy8OZS1dmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حساب کاربری خود در شبکه اجتماعی «تروث سوشال» تصویری ساخته‌شده با هوش مصنوعی منتشر کرد که یک جزیره شلوغ و ویران‌شده در میان آتش و دود را نشان می‌دهد.
روی این تصویر عبارت «حمله به خارگ» درج شده بود.
ترامپ تصاویر دیگری هم منتشر کرد که با هوش مصنوعی ساخته شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77514" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxAUpZhLK5wVWGNIAMS0tK-sM5LCirjKBRHOq27lMpAGkqO4jCY_OxyWFUChZGm0eHTnZ7LmtTyZXUwF5drSLVDsu0hRSWLSxOb3_TxA1ZIOO9s7-YNv07vqizLoJGtc73CTNJ3KFiNuk3E8WWcW2mxbsXfN2zle8mCetx2N3vmLse0_3Zrjt1SZJnLI8l7KtPeSBO9KlVXFC7U1KknZhpp-ehle4fSat1D3hiL9zLpP8SWGLziRwCSe0E4oor97SE33eNDZme6_1qfm304UIerO9ehTUHTg7HeDE3_KDKBH5p4LqWhEIqMFHJnAxrJ_gAbZ1wXrxqQG6fdAxvYKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از منابع آگاه گزارش داد برد کوپر، فرمانده فرماندهی مرکزی ارتش آمریکا (سنتکام)، به دولت دونالد ترامپ توصیه کرده است کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا به اعتقاد او این عملیات به سقف اثربخشی خود رسیده است.
به گفته این منابع، کوپر ارزیابی کرده است حملات دو هفته گذشته توانایی جمهوری اسلامی برای هدف قرار دادن کشتی‌ها در منطقه تنگه هرمز را به میزان قابل توجهی کاهش داده و بیشتر اهداف تعیین‌شده برای حملات هوایی نیز از بین رفته‌اند.
منابع آگاه افزودند کوپر به مقام‌های آمریکایی گفته است در صورت تصمیم برای از سرگیری عملیات گسترده نظامی، آمریکا می‌تواند ۲۰ درصد از اهدافی را که در عملیات «خشم حماسی» هدف قرار نگرفتند، مورد حمله قرار دهد. با این حال، او تاکید کرده است اگر تصمیمی برای بازگشت به عملیات گسترده گرفته نشود، ادامه کارزار بمباران دو هفته گذشته توجیهی نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77511" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gierOCv6Vngf_zwwpsGfvhkqx_MRZo9pFLVy_Y7YQx61bK4Y4biO_EcgZyngIZHYJSj6AvP40j32uzfxm9FlZ55uDhLlol0P3w4kbfCX0OCdVDsbQE7KoScO7Q3L766gyIbvP-ZevCkbv812KQQCEi-sIO6BI6Emb9Ar6L3hSkQYqMCn2Jro3HOJGbW6509LwkrsISGVSdBerb8tT0IqR7Jx9JbDshT-Snke0vHG-APVJj7n2u-1evCMe2WhOvG_y0R7Gn-BCvw2szAWz61bRv2Nk9N0D4w-jjs-gXZBv7FEGSLehN-07E5NlvDgZj223QR0yffzoQQFgRuzwKifKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران با انتشار پیامی در شبکه اجتماعی اکس، حمله اوکراین به یک شناور «تجاری» ایرانی در دریای خزر را «نقض آشکار منشور سازمان ملل متحد» خواند و اعلام کرد این اقدام «نمی‌تواند بی‌پاسخ بماند.»
عراقچی در این پیام نوشت که ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، با حمله به یک کشتی «تجاری» ایران که به کشته شدن یک ملوان ایرانی انجامید، به گفته او «به خواست اسرائیل» تلاش کرده است اروپا را وارد جنگ کند. وزیر خارجه اسلامی افزود که در گفتگوهای تلفنی خود با کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا و سرگئی لاوروف، وزیر خارجه روسیه، تاکید کرده است که این اقدام نباید بدون پاسخ باقی بماند.
ولودیمیر زلنسکی پیش‌تر اعلام کرده بود که نیروهای اوکراینی در عملیات‌های دوربرد در دریای خزر، کشتی‌هایی را هدف قرار داده‌اند که به گفته او برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77510" target="_blank">📅 19:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpTTIJNejSK7z6Ho5QrlmZotH8632H60MyjVZPJY1V4cpZ-3LNRmf2XLMW8CKqpKgdrDZfYL8UOUwQr1BZwyeQYpHtOuLW9W9hezGpsKsdstfN2cDDvT9Krkuq_j--EYq4l-2MheSMIR51YbSKxFP7TP1jwIXFuKjrAtrmm-A2w03ZnClIKovG9jaHQMJAt5UqoQyBeS-LQmP4i2faPFY3-mZq0LO0qVn5wUg0epijNA0KhUKr_vmOZz4BsmoEdC7RnxzFmVlyu-JVgNkndNJSdnDLgCaZlpP1Vcgjxb3KKBhTgmK4aAkrdvG_Y30wr68__veNil63fr8uQ_sm1haA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، گفت درگیری با ایران زمانی پایان خواهد یافت که حکومت جمهوری اسلامی سقوط کند یا آن‌قدر تضعیف شود که برنامه هسته‌ای خود را متوقف کند.
او در گفت‌وگو با شبکه فاکس نیوز مدعی شد جمهوری اسلامی باید به این نتیجه برسد که ادامه ایجاد «آشوب اقتصادی در جهان، کشتن هزاران شهروند خود و حمله به دیگران» هزینه سنگینی دارد. نتانیاهو تاکید کرد که برنامه هسته‌ای ایران «چه با توافق و چه بدون توافق» باید پایان یابد.
نخست‌وزیر اسراییل همچنین هشدار داد اگر ایران یا گروه‌های هم‌پیمانش به اسراییل حمله کنند، با پاسخی «بسیار قاطع» روبه‌رو خواهند شد و افزود تهران در صورت انجام چنین اقدامی «اشتباه بزرگی» مرتکب خواهد شد.
نتانیاهو درباره سفر پیش روی خود به واشینگتن و دیدار با دونالد ترامپ، رییس‌جمهوری آمریکا، گفت قصد ندارد اطلاعات تازه‌ای ارایه کند، زیرا به گفته او، همکاری اطلاعاتی میان دو کشور بسیار نزدیک است. او افزود مشتاق است دیدگاه ترامپ را درباره آینده درگیری با ایران بشنود و گفت: «در بسیاری از جنبه‌ها، این تصمیم اوست.»
او همچنین اعلام کرد که «قطعا» برای شرکت در نشست مجمع عمومی سازمان ملل در ماه سپتامبر به نیویورک خواهد رفت و گفت قصد دارد از تریبون این سازمان درباره اسراییل و ایتلاف اسراییل و آمریکا سخنرانی کند.
نتانیاهو در ادامه از زهران ممدانی، شهردار نیویورک، انتقاد کرد و او را به دامن زدن به نفرت علیه یهودیان و حمایت از حماس متهم کرد.
او همچنین گفت از کاهش حمایت حزب دموکرات از اسراییل «بسیار نگران» است و مدعی شد شماری از چهره‌های اصلی این حزب تحت فشار فعالان سیاسی به مواضع جریان‌های ضد اسراییلی نزدیک شده‌اند.
نخست‌وزیر اسراییل در بخش دیگری از سخنانش از موضع دونالد ترامپ درباره عربستان سعودی حمایت کرد و گفت ترامپ به درستی تاکید کرده که در صورت عادی‌سازی روابط ریاض با اسراییل، تنها باید با یک برنامه هسته‌ای «غیرنظامی» برای عربستان موافقت شود. او افزود آخرین چیزی که اسراییل و آمریکا خواهان آن هستند، شکل‌گیری یک برنامه هسته‌ای نظامی در عربستان سعودی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77509" target="_blank">📅 19:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhXs17RQwMuTbvaVtcxNbMZ0CIAGgcY1We2cAHBTstiuQTvD_xlfaM51myeY_nLeczqOeWWSTUiTZDnkdLOHqGpdZVCro-MOy34v8Uo6dGRNEQpF-1VvNwa3olKru_QJZ6bSeR4Gzp46SVs-kE2PtNskKS235-wD4K34QSc6jt5oYk1CVcFWG28zmg8cwfnqnY7KddQj4lsqO7GrxkaxdSZG8csW0KH0LSI6tCYqeU_7afs1vtaUXPdlvZOGiteAB8v8Nks8DFvUKVheLnUV6VrXHvjcGisOH6AkhOYoVTPokiFsMcbEs23KbwTMzSqmer2A0hICC_Jh1lx_5Xg1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل، اعلام کرد که دونالد ترامپ، رئیس‌جمهور آمریکا، حملات علیه ایران را به‌طور موقت متوقف کرده تا فرصت بیشتری برای پیشبرد دیپلماسی فراهم شود.
والتز روز یکشنبه در گفت‌وگو با شبکه فاکس نیوز گفت: «او دارد به مذاکرات فرصت می‌دهد؛ کمی فضا برای پیش رفتن گفت‌وگوها فراهم کرده است.»
سخنگوی ارتش جمهوری اسلامی نیز گفته که در پی توقف حملات آمریکا، ایران نیز حمله به متحدان واشینگتن در خاورمیانه را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77508" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHXptgo7edNQ_bJak0XKAFs7XWgy5lTrgXb1D_8sHYMKlg9YgUT_D_pa4oRy6XGxrypavmjsRZcShL5Kc9ZlX9rVTozIBmdEITX9mP9mdvcL8I85FzzgojJEZFgUVFULSvGfbid_fMkIzWE0POYeh9r5sGvmRfXyXbYrQbOth_K6eBAZYNDYetFndtFPxraAmBs90SfNpcXaTSkPmhsJVzKieXfhPwekvaiNM9x0EaZi0XIlFR92JGmXHTmcePvbGOOIuDEsbE6_zKMMQvl50isnbqvxjZyNWrW3KHS_3hj03hPV104Ji7ToBbzvpYlK8yvLu6SXSsart3NY9msmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز یکشنبه مدعی شد که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
بنابر گزارش تسنیم، این نفتکش پس از خروج از مسیر دریانوردی مشخص‌شده از سوی ایران در این آبراه راهبردی، با مین دریایی برخورد کرده است.
بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد که اواخر خرداد بین ایران و آمریکا برای تمدید آتش‌بس امضا شد، ایران متعهد شده بود طی ۳۰ روز در تنگه هرمز مین‌روبی کند تا تردد کشتی‌ها آزاد شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77507" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VX3TkVCJCKirTUxkjzjszxPGcFb5irXiiUL0Em7GXg8JXsCAZIanW5p7WDHzwTvdONXk_D6wOQqnqTPlPAeszbXYeDhiZENkZ20YAmRTGIfQbfYM6fFNDdqpSzKN_xgffH-Vr7PL_fVY_iEQ3dVVTwnGwfkaqEtcd4ciNazzvYqE3FCI1V585N85d5d22nQDnsTY_pWtXBlyIwZa-Q3O2kKEoWXwhCjHkmJgN7jnpUsYVbzU7U31sKlXSlcEz341C9miWKF6_UsTGCOBhucPKbNGq0Eif1nvLaK1eUCNfUn6SEIeUtKXcvJI4IQZY6kuXsKw2y1dfHCG_G1yWlPbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری العربیه، روز یکشنبه چهارم مرداد ماه گزارش کرد ایالات متحده آمریکا و جمهوری اسلامی ایران پاسخ‌ خود به پیشنهاد مشترک پاکستان و قطر را که با هدف ازسرگیری مذاکرات میان دو کشور ارائه شده بود، تحویل دادند.
بر اساس این گزارش، منابع آگاه در گفتگو با العربیه تایید کرده‌اند که کشورهای قطر، مصر، پاکستان و دیگر میانجی‌گران منطقه‌ای طرح جدیدی برای برقراری یک آتش‌بس ۱۰ روزه به واشنگتن و تهران ارائه داده‌اند. این طرح با هدف ایجاد فضای مناسب جهت حل بحران در تنگه هرمز و احیای توافقات پیشین تنظیم شده است.
العربیه نوشت، این پیشنهاد دو شرط اصلی برای بازگرداندن دو طرف به مسیر گفتگو دارد که شامل توقف فوری اقدامات خصمانه و بازگشایی کامل و ایمن تنگه هرمز به روی رفت‌وآمد کشتیرانی بین‌المللی است.
بر اساس جزئیات این طرح، مقرر شده است که مسیر جنوبی دریانوردی از طریق آب‌های عمان از حملات نیروهای مسلح جمهوری اسلامی در امان بماند و مسیر شمالی از طریق آب‌های ایران نیز از محاصره دریایی آمریکا خارج شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77506" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rsd2M1JJZ4BJ-ol9cwLNSweUZ7QlZ8YK5oZe_suWNd5oJ_Awk-e34AR1y_4YPX5e22lLWVUE95ucFTsiWWTm4IGcgKBCf7WsABUcv563Bg2cbdD59jgILB-io4wF9_u-6GlpKjs9eS5DWUne-jsJJmkXBfjywnhOJEB5h9lN9-N0uP8TslxvWtMnVtyreh9KIA-6Bcw6r5PQ5Rb4gZEbvZ1jJWYpcQe1n-_KVo_HiE6W5-pVNfoiEfvoMleck9ENuVj1vHy8GDwokEnsP3rDYFnX67G7GvYWEpFNby-dpBaXOwN4exHpITnLi-t4mhZkkj3lYFdKHHPT9Q67l9azJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان اویس‌قَرَن، پژوهشگر ایرانی علوم رایانه و استاد دانشگاه واشینگتن، مدال آباکوس سال ۲۰۲۶ اتحادیه بین‌المللی ریاضیات را دریافت کرده است؛ جایزه‌ای که به دستاوردهای برجسته پژوهشگران جوان در بخش‌های ریاضی علوم رایانه تعلق می‌گیرد.
کمیته این جایزه می‌گوید اویس‌قرن با وارد کردن ابزارهایی از شاخه‌هایی چون هندسه چندجمله‌ای‌ها، نظریه احتمال و نظریه طیفی گراف‌ها، شیوه تحلیل الگوریتم‌ها را گسترش داده و برای حل چند مسئله قدیمی علوم رایانه راه‌های تازه‌ای گشوده است.
پژوهش‌های او به‌ویژه در دو زمینه مورد توجه قرار گرفته‌اند: یافتن مسیرهای نزدیک به بهینه و نمونه‌گیری تصادفی از مجموعه‌های بسیار بزرگ و پیچیده.
مدال آباکوس هر چهار سال یک‌بار اهدا می‌شود و ادامه جایزه‌ای است که تا سال ۲۰۱۸ به نام رولف نوانلینا شناخته می‌شد. نامزد دریافت آن باید در آغاز سال برگزاری کنگره جهانی ریاضی‌دانان هنوز به ۴۰ سالگی نرسیده باشد. این جایزه از مهم‌ترین افتخارات بین‌المللی در علوم رایانه نظری به شمار می‌رود.
اما اهمیت کار اویس‌قرن تنها با فهرست کردن اصطلاح‌های تخصصی روشن نمی‌شود. بخش مهمی از مسیر علمی او به یکی از مشهورترین پرسش‌های علوم رایانه بازمی‌گردد: چگونه می‌توان کوتاه‌ترین مسیر ممکن را برای سفر میان چندین شهر پیدا کرد و در پایان به نقطه آغاز بازگشت؟
این پرسش که «مسئله فروشنده دوره‌گرد» نام دارد، در ظاهر ساده است. یک فروشنده، راننده یا مأمور توزیع باید از چند شهر یا مقصد عبور کند، هر کدام را یک بار ببیند و به نقطه نخست بازگردد. با افزایش شمار مقصدها، تعداد مسیرهای ممکن چنان سریع زیاد می‌شود که بررسی همه آنها عملاً ممکن نیست.
در چنین مواردی، پژوهشگران به جای یافتن پاسخ دقیق، الگوریتمی می‌خواهند که در مدت معقول مسیری نزدیک به بهترین مسیر را پیدا کند و بتوان تضمین کرد که نتیجه آن از حد معینی بدتر نخواهد بود.
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77505" target="_blank">📅 16:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN-7vJgkEPrYBx_GDu6knzx4tj0lUjLqsv-3y5eKzJFgPc_m8ZbVX-c5GOOLAhUZgeFryGQZADqErfqmtIBh1EEZo4Kd1oQ-FwOlOl2BSkPxpxDDg6Ax0g_GWbcxDDaL5rtlacADznDCkRrnjrmlrJrBoodYYDx7i2eJg3DoxIX923EtfzbiBNwcHDkBqBezki0NofN-aU-8QWmLAYq-QWwWCUioWchuA_OiazSIOViZ5jCO8lTwEIXtP4TVGY2Pli9kQyGlanZjWjYFmb0OO-0qF_DvojKyyXD5FuUs1yaUxgRhrO4PKfErfADMK0DAYAGf7v9HZv4ovhXpxPJK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید
گزارش نیویورک‌تایمز
درباره کنارگذاشتن طرح تشدید عملیات نظامی علیه جمهوری اسلامی را رد کرد.
استیون چانگ، مدیر ارتباطات کاخ سفید گفت دونالد ترامپ، رئیس‌جمهوری آمریکا، همواره گفته است راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر جمهوری اسلامی به اقدامات تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همه گزینه‌ها را حفظ می‌کند.
چانگ افزود پس از تحریم‌هایی که اقتصاد جمهوری اسلامی را فلج کرده و سیزده روز پیاپی حمله به اهداف نظامی، عاقلانه است که این حکومت به سمت توافق حرکت کند. او گفت در غیر این صورت، طرف مقابل می‌داند چه اتفاقی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77504" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j5GLwyBNey2nxW6g2qiU9YBviXqssOew8KohjBv-tYU4oETh38DwFN3Kfjr-cgK___YrjbEeswY9rJbfcas4JFAeywBXI2VMASimKwXemvZ3jcyXNraOgKPMtAEAjgtmyR8GneVuGoOFGnIxoj5InI_SExuIb_-jMY4cV6uErbSmZRf_X_h9fVgz29eE0ZpXKvJzJGqjrNeqctQlHFxAqw2ZVm-S6Bg-Sq65MYIlt6mtpHXm0sTMILDtriQms4MiBALWZaXu72kUMvxWAodOMKskBdLDvIHGrgDz22d_JQPN64N9S-NKFYfXcZmkysCf4Ln2O9qntEmFA0smeiEFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، روز یک‌شنبه چهارم مرداد بدون اشاره به جزئیات از «پیشرفت‌هایی» در مذاکرات و تبادل نظر تهران و مسقط خبر داد.
این مقام جمهوری اسلامی پس از آن در این باره اظهار نظر کرده است که یک هیئت عمانی که برای گفت‌وگو درباره مدیریت تنگه هرمز به تهران آمده بود شنبه عصر ایران را ترک کرد.
بقایی درباره این مذاکرات این طور توضیح داد: «روزهای جمعه و شنبه چند دور گفت‌وگو بین ایران و عمان در سطح معاونان وزرای امور خارجه در تهران برگزار شد که طی آن دو طرف در مورد اصول مشترک و سازوکارهای عملیاتی برای مدیریت تردد ایمن کشتیرانی در تنگه هرمز با رعایت حقوق حاکمیتی دو دولت ساحلی تبادل نظر کردند.»
مقام وزارت خارجه در ادامه اضافه کرده است که «در حال حاضر تغییری در وضعیت تردد در تنگه ایجاد نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77503" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQna2j0l7nmOe7o_bIcBRk7pswKteYWwW6sUZ4-Oj8QpN6RpyGQpCoQjGY54YzAWA_hqngLmeMUbAmez2hskyQopqmcn3Xoa2EOxMUD0mUQjb_1s2_d38dxoAmdhIqHM2W7cf9UcIhMNXRE11u6c-Nsb3QlCveg7fjxQGcdjGc9mdDw0DH-DiKn1T8cSxuCMeCepB5OyQ6JVIQXdIfX6c6VR7CGAmZcA92zEakR5kCmqAYsNeY9vFaST-Xe8IJkxxWG6HkFUchgHMMPSF-Sz1x4uT-kXSj8bdepytcE440sak5_2Rp5RezRJwNcwUkJyFpo40a49bMEvBpdGkmZd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که سال گذشته دختر ۱۷ ساله خود به نام فاطمه سلطانی را مقابل آرایشگاه محل کارش در اسلامشهر با ضربات چاقو به
#قتل
رسانده بود، با حکم دادگاه کیفری تهران به هشت سال حبس و پرداخت دیه محکوم شد.
در قوانین جمهوری اسلامی ایران، مقرراتی وجود دارد که پدرانی را که مرتکب قتل فرزند خود می‌شوند، از مجازات‌های سنگین معاف می‌کند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77502" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TbAtvblJrdghznI_-uIumS6eheqzbws5BRXNf7yLyT_0O7B57DI2MEs5WCeJa2-Tj-Lik5csaOxyuyp8J45ehKWoMC7s2PgdvRfHhButPeq0G8OIqCmh3MOfu0j8PTbOxvKBDfssvX0THPrU_jmW91KOrZLYkQ9qq1NudHTNfn1Jh95cVEiWPMEspC-pahDy5vi_P_jh_SHtVmE-11ByLCwVKKXuysfrUKp3hPgMp9dSa8bWlcb6fHxGg8sxX6vifXFEIxJUbtkvYwWU68l_yw1rrp5mouWb0YwkD7j1jj3TqB2o0kkzJSeMdkjirTUXUJuHh-66eM6DzSCIDG5eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: منابع می‌گویند ونس و کین درباره تشدید جنگ در ایران ابراز نگرانی کردند
ترجمه ماشین:
یک منبع آگاه از موضوع و یک مقام آمریکایی به سی‌ان‌ان گفتند که در حالی که دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست روز جمعه کاخ سفید احتمال تشدید جنگ در ایران را بررسی می‌کرد، جی‌دی ونس، معاون رئیس‌جمهوری، و ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، هر دو درباره این اقدام ابراز نگرانی کردند.
جمعه‌شب، پس از نزدیک به دو هفته حملات هوایی پیاپی شبانه، به نظر می‌رسید آمریکا کارزار بمباران ایران را متوقف کرده است. یک منبع در وزارت دفاع آمریکا روز شنبه به سی‌ان‌ان گفت: «عملیات فعلاً متوقف شده است.»
به گفته منابع، کین روز جمعه به‌طور مشخص درباره ذخایر مهمات آمریکا و دیگر پیامدهای منفی احتمالی ابراز نگرانی کرد. یکی از منابع گفت کین به ترامپ اعلام کرد که ارتش آمریکا می‌تواند گزینه‌های پیش روی او را اجرا کند و موفق شود، اما سپس درباره پیامدهای احتمالی آن هشدار داد.
هر دو منبع گفتند نگرانی درباره ذخایر مهمات، یکی از چندین نگرانی مطرح‌شده با ترامپ در این نشست بود. در حال حاضر مشخص نیست که آیا این نگرانی یا هشدار درباره تشدید جنگ، دلایل اصلی توقف حملات پیاپی شبانه آمریکا بوده‌اند یا اینکه این توقف ادامه خواهد یافت.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت: «با توجه به تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزهای مکرر این کشور، عاقلانه است که ایران برای دستیابی به توافقی از طریق مذاکره تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77501" target="_blank">📅 06:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gUE_L-PE3zmxHr0C7cvBwN6RCHGdq2v_XRpgr90RDnMwMayTYFvC2q9z3T-pEWz34VAQPyK6GGsofqP5k64wmFiBrNbTjAicgiJaGt3wrXPCXG0l3LbFGZqZVWaixL8uqlgLo7UyVLHCHIKvblMDk2X9nb31d5mEwPw0CElKiL22pCNQwXtt21QJAnwsFgoo3Wro3dpTq4OOObm8-lLXLYAoKVO-hQPGH2XhwZXG-5-qNi_XOjwOhjUqEOo0K3DOTV0UdF_J56LYlORd74wSgSh37Y6rHbvg2BFus95TRHigvPMN8YZSo-n-HqTFgO1pkDYWD9WhAePcyK0m9I9tIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز:
ترامپ در پی ابراز نگرانی مشاوران، فعلاً از تشدید گسترده حملات علیه ایران خودداری کرد
یکی از نگرانی‌ها این است که گسترش درگیری‌ها ممکن است ذخایر کاهش‌یافته مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
ترجمه ماشین:
رئیس‌جمهوری ترامپ، دست‌کم فعلاً، برنامه‌های تشدید شدید حمله نظامی آمریکا علیه ایران را کنار گذاشته است؛ به‌ویژه به این دلیل که نگران است تشدید جنگ، ذخایر از پیش کاهش‌یافته پنتاگون از موشک‌های رهگیر ضدبالستیک پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
به گفته مقام‌های دولت، تهدید متوجه ذخایر موشک‌های رهگیر یکی از ملاحظات متعددی است که بازگشت به عملیات رزمی گسترده را به اقدامی بسیار پرخطر تبدیل کرده است. آقای ترامپ و دستیاران ارشدش همچنین از احتمال گسترش جنگ در خاورمیانه، دور شدن متحدان کلیدی در خلیج فارس که در برابر حملات ایران آسیب‌پذیرند، فشار اقتصادی جهانی و تشدید بحران‌های انرژی و پناه‌جویان نگران‌اند.
به گفته دو نفری که در جریان این گفت‌وگو قرار گرفته‌اند، تازه‌ترین چرخش در نحوه مدیریت مناقشه با ایران از سوی آقای ترامپ پس از جلسه‌ای در روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه او رخ داد.
به گفته این مقام‌ها که برای گفت‌وگو درباره مسائل عملیاتی خواستند نامشان فاش نشود، رایزنی‌های محرمانه بر کاهش ذخایر موشک‌های رهگیر پاتریوت و دیگر سامانه‌های پدافند هوایی پنتاگون متمرکز بوده است. یک مقام ارشد آمریکایی گفت جمعه گذشته، هنگامی که یک موشک بالستیک از پدافند هوایی آمریکا ــ که در حال مقابله با موجی از موشک‌ها و پهپادهای ایرانی بود ــ عبور کرد، سه سرباز آمریکایی در اردن کشته شدند.
به گفته این مقام‌ها، ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، در محافل خصوصی هشدار داده است که ازسرگیری عملیات رزمی گسترده علیه ایران امکان‌پذیر است، اما ذخایر موشک‌های رهگیر در دسترس فرماندهی مرکزی ارتش آمریکا را ــ که مسئول عملیات در خاورمیانه است ــ به‌طرز خطرناکی کاهش خواهد داد. سخنگوی ژنرال کین از اظهارنظر درباره توصیه‌هایی که او به رئیس‌جمهوری ارائه می‌کند خودداری کرد.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت رئیس‌جمهوری «همواره به‌طور ثابت گفته است که راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر ایران به فعالیت‌های تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همچنان همه گزینه‌ها را روی میز نگه می‌دارد.» او افزود پس از تحمل تحریم‌های فلج‌کننده و حملات مکرر، «عاقلانه است که ایران برای دستیابی به یک توافق مذاکره‌شده تلاش کند؛ در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
آقای ترامپ درگیر این بوده است که در جنگ نزدیک به پنج‌ماهه خود علیه ایران چگونه پیش برود و به‌طور مشخص چگونه تنگه هرمز را دوباره باز کند؛ آن هم در شرایطی که با ازسرگیری درگیری‌ها در دو هفته گذشته، قیمت بنزین بار دیگر در حال افزایش است. دیپلماسی شکست خورده و به نظر نمی‌رسد تازه‌ترین دور حملات گسترده آمریکا توانسته باشد ایران را از لحاظ نظامی بازدارد.
به گفته آن دو نفری که در جریان گفت‌وگوها قرار گرفته‌اند، در حلقه نزدیکان آقای ترامپ، افراد بسیار کمی ــ و شاید هیچ‌کس ــ معتقد بودند طرح تشدید درگیری عاقلانه است. یک مقام ارشد آمریکایی دیگر که او نیز به شرط ناشناس ماندن صحبت کرد، درباره اینکه ازسرگیری عملیات رزمی گسترده بتواند ایران را به میز مذاکره بازگرداند، ابراز تردید کرد.
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/77500" target="_blank">📅 03:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=MsoZW2H76M7NYyQe3AEaHeEKJLqLI4NnibUFl36saWWmnb8TDA38gkNeLweguO-xbfWuDq-vt-jNu-9-rFuVfe_SmmzFzKlOpH7WK25BoYhh6H3cpLKsVJezjsulDrlPOj_purfihKW5ZeHTwzJCyMS6T1uwaameh0qtG_vq4FExeRrzj6b6DR45D40_mnp5nvuJikSUID3bFcIxOx7xPN9Au6x3ahldSViKQbsVX38-jbCS4YVWgSvUZk0XbAsf2ezj_uGLHG6nPsussdm-6bFtp3cZZn-2Pz0vcKDSEJxYEaJi-BFGgczPKQa1fa3MyO6w7Z_chl1eKZ15HZo_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=MsoZW2H76M7NYyQe3AEaHeEKJLqLI4NnibUFl36saWWmnb8TDA38gkNeLweguO-xbfWuDq-vt-jNu-9-rFuVfe_SmmzFzKlOpH7WK25BoYhh6H3cpLKsVJezjsulDrlPOj_purfihKW5ZeHTwzJCyMS6T1uwaameh0qtG_vq4FExeRrzj6b6DR45D40_mnp5nvuJikSUID3bFcIxOx7xPN9Au6x3ahldSViKQbsVX38-jbCS4YVWgSvUZk0XbAsf2ezj_uGLHG6nPsussdm-6bFtp3cZZn-2Pz0vcKDSEJxYEaJi-BFGgczPKQa1fa3MyO6w7Z_chl1eKZ15HZo_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین: 00:32
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است. تا ۲۵ ژوئیه، سنتکام مسیر ۱۲ کشتی تجاری را که قصد شکستن محاصره داشتند تغییر داده، ۲ کشتی را که از دستورات تبعیت نکردند از کار انداخته و برای اطمینان از تبعیت کامل، وارد ۲ کشتی شده است.
صبح امروز، نیروهای آمریکایی عملیات ورود و بازرسی برای راستی‌آزمایی را در نفتکش M/T Charminar با پرچم کومور، در دریای عرب، به پایان رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام روز ۲۴ ژوئیه، نفتکش M/T Lavine با پرچم موزامبیک را در دریای عمان از کار انداختند؛ پس از آنکه خدمه آن چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی
🇺🇸
همچنان کاملاً هوشیار، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/77499" target="_blank">📅 01:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_VtOMXd8mrHlu74uJIPxhO7jvAgqNW8mXpZT86vrGL_RKdlPk4ZpJa9guAxzf9HYqEMGMe2BZUC7OQFYTY6xMAcqExhZGgNXEJGndlogJZc50HIALVWnW0-GoEN5i3verG8pxwYbPw4uKG1ueX9-YBU-2W-aEnnGVTPToZKcnDHhKKOGD3oI2bIOxGh83UM47z1O81aTdw0O4OWK55c1qs96Nm-VbR_QTf5CJqNGKbyUMt7m1gqZWJXD8sj_Yg0WJOlcjM7RH0IkTLKY8t7cIqNxQFjRTXDc_NIn8KVfH5yoyElVIMv4bmjqZg6jE2GEURBeUxkKrOaQJdLlzQz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه هشدار داد که اگر دولتش به چیزی که در مذاکرات با ایران می‌خواهد نرسد، قطعا حملات گسترده به این کشور را از سرمی‌گیرد.
خبرنگار شبکه فرانسوی ال‌سی‌آی در شبکه ایکس نوشت که در گفت‌وگوی تلفنی با ترامپ از او سوال کرده که آیا در حال بررسی ازسرگیری یک جنگ گسترده علیه ایران است یا نه.
رئیس‌جمهور ایالات متحده در پاسخ گفته است: «اگر به صد درصد آنچه می‌خواهیم نرسیم، قطعاً.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77498" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoGfd0NvrSp-fP7w5KaL_qKEg7ktoFfqBWcXMUhn2SCs1CKnoSgRamyzCwCMr5QPEHLq4-ytV8JMIxQoXL1sidaSDbHKromQnVieCQnDM-1dMINrvcYiMaaJE6b5x7i7_fpbfV9HsGrevKQtBKdDOwpRHVKDAT10DjbktecIU5e6HO-TLLTBdpPMqsOw7iptxU12FMSDMS5DAZGoTCsZKnHVgm9FQBJqrV_Rsal7pItfYKKfQgfPjE1iFTO3sSBmhINImHYac-QMBMGMADwUkidhX_VRMNyWY5eOsThmeqNrT_59jn5WkMjhxR_x93aO5fSwxnfqE9ZaMek8RKY7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77497" target="_blank">📅 22:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1bueSmX64pCyP0RSqYap5HD1N-JpDKq0GWxIIrKsdWFZSjYcXQjOq_EWy2HXsPD3vALf-n9SscyCHghBIpHAmN9BfxbRBURJEQBXhqjIOyPu-BCtKQzd50ezpkav8Xqj5hxoNrgdYdgCIgjH6pUhi2hnzpQ1h5qyoGfdQ81EPt6TMQPupl2ghAjeOis_eWpA6G6glm5zJDtn6VBESFVXqA7wcn2VLxreCd0k8gB7dY_Zs49VHZOEH7TQnACMj8f_g2AbqmUAH_ZU6Zh9VxnhIakUbT7OWlx_8avJGDwdOu0TQSaGcNqlhS72Nlod6Pyl6EXMwAXm1CCO0dfZW_Ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی پری، خواننده آمریکایی، از استفاده کاخ سفید از آهنگ «Firework» (آتش‌بازی) در ویدیویی از حمله آمریکا به اهدافی در ایران انتقاد کرد و گفت این استفاده بدون اطلاع و رضایت او انجام شده است. او افزود که از این اقدام عمیقا شوکه و خشمگین شده است.
کاخ سفید روز پنج‌شنبه ویدیویی در حساب رسمی خود در تیک‌تاک منتشر کرد که در آن بخش «boom, boom, boom» آهنگ «Firework» با تصاویری از حملات آمریکا به اهدافی در جنوب ایران هم‌زمان شده است. کاخ سفید در توضیح این ویدیو نوشت: «به ایران هشدار داده شده است.»
کیتی پری روز شنبه در شبکه ایکس نوشت: «از اینکه آهنگ "Firework" به‌عنوان موسیقی پس‌زمینه ویدیوی حملات نظامی در حساب کاربری تیک‌تاک کاخ سفید استفاده شده، عمیقا شوکه و خشمگین هستم. من این استفاده را تایید نکردم، از من اجازه‌ای خواسته نشد و به هیچ وجه آن را تایید یا حمایت نمی‌کنم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77496" target="_blank">📅 22:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fsl4-NjGf5KLIsWobAiBnGyLWvg4_aeQu9ykkFQ_HZGYskgLlGdUHbDW9yHLysTZdVcLyzytC5Gr9ZlsDWu-kFe6SBsoLnterxI4COMvBUn30KlfHVMaoYj0S7z_aBBF19g7HmLiDsAsR4WkDmpTMBdyk3deQoQMQpXNTD2Q0W8Py1iFwD8rRZNXTHRn6J9NN44g-bp25DgDiOCJmFyI4t2SgowPcnLFSvSQIdEhk3cqhXfyuQW3hSkgECKt7CKwosiieFWuqqNLTwVTVxoPVrugCtnueoZD039C1hzKgk46n6WW88vLkKngmKktHE6tC6DkWVjoF_4nOrlN8grvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ دستور داد ارتش روز جمعه در ایران حمله‌ای انجام ندهد
ترجمه ماشین:
دو منبع مطلع از این تصمیم گفتند دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه به ارتش این کشور دستور داد حملات جدیدی در ایران انجام ندهد؛ دستوری که به رشته‌ای نزدیک به دو هفته از حملات روزانه پایان داد.
چرا مهم است:
دستور رئیس‌جمهوری پس از آن صادر شد که او طی ۱۳ روز گذشته، هر روز حملات را تأیید کرده بود. هنوز مشخص نیست که دستور روز جمعه ترامپ تصمیمی یک‌باره بوده یا این وقفه ادامه خواهد یافت.
▪️
تصمیم ترامپ هم نشان‌دهنده تمایل او به فراهم‌کردن فضای بیشتر برای دیپلماسی است و هم حاکی از این ارزیابی که سطح کنونی حملات آمریکا ــ مگر با بازگشت به عملیات رزمی گسترده ــ به مرز اثربخشی خود رسیده است.
▪️
اگر ترامپ دستور ازسرگیری حملات را صادر کند، ارتش آمریکا می‌تواند در مدت نسبتاً کوتاهی برای انجام آن‌ها آماده شود.
▪️
به گفته منابع، ارتش آمریکا همچنان در حال تهیه طرح‌هایی برای بازگشت احتمالی به عملیات رزمی گسترده است، اما ترامپ هنوز دستوری برای حرکت در این مسیر صادر نکرده است.
▪️
کاخ سفید به درخواست اظهارنظر پاسخ نداد.
آنچه خبر را رقم زد: ترامپ طی دو هفته گذشته، هر بعدازظهر طرح‌های حمله ارائه‌شده از سوی ارتش را تأیید کرده و این حملات ظرف چند ساعت اجرا شده‌اند.
▪️
روز جمعه نیز طرح مشابهی در اختیار ترامپ قرار گرفت، اما او با آن موافقت نکرد. در عوض، به گفته منابع، به ارتش دستور داد حمله‌ای انجام ندهد.
▪️
اندکی پس از صدور این دستور در روز جمعه، ترامپ به خبرنگاران در کاخ سفید گفت که می‌تواند حملات را ادامه دهد یا حتی آن‌ها را تشدید کند؛ از جمله با «نابود کردن هرچه آن‌ها دارند».
▪️
اما او روشن کرد که به نظرش «راهبرد هوشمندانه‌تر» این است که با ایران «به توافق برسد».
▪️
ترامپ گفت: «همین حالا با [ایرانی‌ها] در حال گفت‌وگو هستیم. فکر می‌کنم با گذشت هر روز، جدی‌تر و جدی‌تر می‌شوند. ما کاملاً مسلح و آماده‌ایم، اما در حال گفت‌وگو با آن‌ها هستیم.»
▪️
ترامپ بعدتر در روز جمعه، در سخنانش در شام انجمن خبرنگاران کاخ سفید، گفت تصور نمی‌کند ایران در حال حاضر آماده توافق باشد، «اما من آماده‌ام گوش کنم».
وضعیت کنونی:
دستور ترامپ برای توقف حملات، چند ساعت پس از آن صادر شد که یک هیئت عمانی روز جمعه برای گفت‌وگو درباره ترتیبات جدیدی به‌منظور بازگشایی تنگه هرمز وارد تهران شد.
▪️
دو منبع منطقه‌ای مطلع از مذاکرات گفتند در گفت‌وگوها پیشرفت حاصل شده و ممکن است توافقی میان عمان و ایران در تعطیلات آخر هفته به دست آید.
▪️
پس از آن، رئیس‌جمهوری ترامپ باید تصمیم بگیرد که آیا توافق پیشنهادی را می‌پذیرد یا نه.
axios
:باراک راوید
تصمیم ترامپ هم نشان‌دهنده تمایل او به دادن فرصت بیشتر به دیپلماسی است و هم حاکی از این درک که — مگر با بازگشت به عملیات رزمی گسترده — سطح کنونی حملات آمریکا به نهایت اثربخشی خود رسیده است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77495" target="_blank">📅 20:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=obogmCdFKHI8671UnB_Ai-dDZZxoFE4dTEZPztwHZlWr3EfGjmatYl5mTyWCKzMCaSDGL9vDu1oiQRknmUx7Jg0AmGKWh1mP4Tf19GlyMUQ6aHLUiENrgQDbUzVBiOI3rHHJeKRxa1-1PrFwZad2_0xnTsBOxD2kQib5RCtp_MeVD16e_d8BfZQ0g92NIsauNLpCObhnDn2VvQJGQmiPV6FwAdoBV4RSmNaAg1Rbn4MZ-zP09ucdpTrfjinwLla2Fu7zxdqZMoh3khh45xI6xpaF779e8qLKp-R7NnDBswsg5WPOHVOE4bCBR1zC0mInBXO4v2bZHsz5_sw65p5c5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=obogmCdFKHI8671UnB_Ai-dDZZxoFE4dTEZPztwHZlWr3EfGjmatYl5mTyWCKzMCaSDGL9vDu1oiQRknmUx7Jg0AmGKWh1mP4Tf19GlyMUQ6aHLUiENrgQDbUzVBiOI3rHHJeKRxa1-1PrFwZad2_0xnTsBOxD2kQib5RCtp_MeVD16e_d8BfZQ0g92NIsauNLpCObhnDn2VvQJGQmiPV6FwAdoBV4RSmNaAg1Rbn4MZ-zP09ucdpTrfjinwLla2Fu7zxdqZMoh3khh45xI6xpaF779e8qLKp-R7NnDBswsg5WPOHVOE4bCBR1zC0mInBXO4v2bZHsz5_sw65p5c5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: تغییر در قیمت یا سهمیه بنزین قطعی است
سخنگوی دولت مسعود پزشکیان اعلام کرد که تغییر در قیمت یا سهمیه بنزین قطعی است و دولت برای مدیریت مصرف این سوخت ناچار به اتخاذ راهکارهای جدید خواهد بود.
فاطمه مهاجرانی گفت دولت همچنان برای بنزین یارانه پرداخت می‌کند، اما با توجه به ضرورت ایجاد تعادل در مصرف، تصمیم‌گیری درباره نحوه عرضه این سوخت اجتناب‌ناپذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77494" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxaIa9SB00MjhYAJLrXqvz1SiqbYfUZrhuULtcJIEfHCM0BT2utPVtrAwRxaJmNN68uZqz42fLiKCjSAHi9sQ0kNsYBfn7ZvNF2kSYwiudpcXH4-GIScBC_G1SXLt_hbI1Vv9b3VAMMr6Ic_FIkZD5YoCAdu5N6EgL2Ky9ZZlvL8UCYU0LuM84NZ8GjvlbwSeW4sB_EJB0CIfw4sOsR5GPkSCaK_AuTq9bEASMkNRQcIUIW5paXFn5U472jn2w2HKN2MMKeYEEuuFmaA76CDI1O5nEjPgY3vVa41ZBX41mqizyImjx5NaqZ7NjdMdTxepHXWXmBLP-yZj7Nc3QWcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت خبری وای‌نت گزارش داد مقام‌های اسرائیلی برآورد کرده بودند حمله گسترده آمریکا به ایران، که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود در حال بررسی آن است، شب جمعه تا بامداد شنبه آغاز شود، اما با پایان روز جمعه به این نتیجه رسیدند که ترامپ فعلا حمله را متوقف کرده و فرصت دیگری به تهران داده است.
بر اساس این گزارش، در پشت صحنه، قطر و عمان فشار قابل‌توجهی بر جمهوری اسلامی وارد کردند تا مواضع خود را نرم‌تر کند و از وقوع آنچه یک عملیات گسترده و تقریبا قطعی آمریکا به نظر می‌رسید، جلوگیری شود.
این گزارش افزود مقام‌های اسرائیلی همچنان معتقدند تفاهم میان تهران و واشینگتن عملا از بین رفته و احتمال دستیابی به توافقی دائمی که حکومت ایران را وادار به پذیرش خواسته‌های آمریکا کند، نزدیک به صفر است.
بر اساس این گزارش، از نگاه اسرائیل، فرصت تازه‌ای که ترامپ در اختیار تهران قرار داده، تنها به جمهوری اسلامی امکان می‌دهد برای مدت کوتاهی زمان بخرد و تغییری در ارزیابی کلی اسرائیل ایجاد نمی‌کند.
@
VahidOOnLine
🔄
باراک راوید:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشدند، بلکه برای حمله‌ای دقیقاً هم‌اندازه حملاتی آماده شدند که طی دو هفته گذشته هر شب انجام می‌شد.
BarakRavid
رسانه‌های جمهوری اسلامی درباره این توییت نوشتند اکسیوس خبر «رسانه‌های عبری» رو رد کرد ولی باراک راوید خودش هم اسرائیلیه و علاوه بر اکسیوس خبرنگار واشنگتن شبکه ۱۲ اسرائیله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77493" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRrTUn9qzuDIziOdOtg03ozm8snP8Nn7Ff71xNXOugmW8N0u6ioIip5vYxvFGUkGx54c2ECFs0ORLlZnOKV538a9pTxcoQZsXRYOOgj8n-bPW_0uXC3k-WrJoigt5BfiyCvxROgu-yRsx7s8a6MUm5GQu7XF-JM6r9Z9A34BcH_iV-UVBEJ53PX61B6ym7tjZp4VI59uc7sGJgzSwznUiHtixCMZJ06zIyZYT3myDNe35Dk7Lmzj7DylLmfdWh4xVuOJpznX6KJenVYh51U8GCmcy0Gb0l0bDal3BN4DtBe0q5wRqrhHQzyNAH3DN0a7-UjAkcmj60-NqgySFSZilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.
زلنسکی روز شنبه، سوم مرداد، در پیامی در شبکه ایکس نوشت که اوکراین در حملات دوربرد شب گذشته در دریای خزر به نتایجی «بسیار خوب» رسیده است. به گفته او، در میان اهداف این عملیات، کشتی‌هایی نیز بوده‌اند که «با مشارکت ایران» برای انتقال محموله‌های نظامی استفاده می‌شدند. رییس‌جمهور اوکراین اطلاعات دقیق‌تری درباره هویت ناو جنگی یا کشتی‌های هدف قرارگرفته منتشر نکرد.
سرویس امنیتی اوکراین (اس‌بی‌یو) نیز همان روز گزارش داد پهپادهای اوکراینی سکوی نفتی «فیلانوفسکی»، متعلق به شرکت روسی لوک‌اویل واقع در دریای خزر، را هدف گرفته‌اند. بر اساس اعلام این نهاد، دو کشتی باری با نام‌های «پورت اولیا ۲» و «بگی» نیز در همین عملیات مورد اصابت قرار گرفتند؛ کشتی‌هایی که به گفته سرویس امنیتی اوکراین در انتقال محموله‌های نظامی میان روسیه و ایران نقش داشته‌اند.
تا کنون نه مسکو و نه تهران واکنشی به این ادعاها نشان نداده‌اند و گزارش‌های اوکراین نیز به صورت مستقل تایید نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77492" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=chRNkR7FvNX-x5k-KPmxXeAGXhETrL_gBgXDniAwBk3sozoJd4Fhlw3GMFR5kQBYESDZ02OPUnWSYbCSbeS7QfW40gKMooMrv529AQdSf0mKfXByb0ohR4FvyjFS_dYsmuaeWyKGKtwjbjqzJC0U7D2_kG-5_5TItLYZSqsWsqFaT2Mb6L9GQtcHV-ScSCFsRq1bXMjMOILDskerk9rLjqfKE2RKID6NnlE_oIW81e86UPJRbkAGaFa2zZAKnt1Io9qTxdHOgRHS2o-c_8ebll2MOErQrOZjM-WxwFEvytxLr1XzdIUKrsERj9zeRKnwICRIZ6u-0oydSfY7EKAB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=chRNkR7FvNX-x5k-KPmxXeAGXhETrL_gBgXDniAwBk3sozoJd4Fhlw3GMFR5kQBYESDZ02OPUnWSYbCSbeS7QfW40gKMooMrv529AQdSf0mKfXByb0ohR4FvyjFS_dYsmuaeWyKGKtwjbjqzJC0U7D2_kG-5_5TItLYZSqsWsqFaT2Mb6L9GQtcHV-ScSCFsRq1bXMjMOILDskerk9rLjqfKE2RKID6NnlE_oIW81e86UPJRbkAGaFa2zZAKnt1Io9qTxdHOgRHS2o-c_8ebll2MOErQrOZjM-WxwFEvytxLr1XzdIUKrsERj9zeRKnwICRIZ6u-0oydSfY7EKAB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید، بخش‌هایی مربوط به ایران، ترجمه ماشین:
... آن‌ها پرسیدند: «می‌مانی؟»
گفتم: «بله، می‌مانم. یعنی، فکر کنم بمانم.»
اصلاً چه کار دیگری دارم که بکنم؟ ایران را دارم؛ این را دارم، آن را دارم. همهٔ این‌ها هم فوق‌العاده خوب پیش می‌رود. اخبار جعلی را باور نکنید.
پیش‌تر داشتیم صحبت می‌کردیم. گفتم: «ما ایران را به‌شدت هدف قرار داده‌ایم. نیروی دریایی‌شان از بین رفته؛ نیروی هوایی‌شان هم از بین رفته است. ۲۵۰ جنگنده دیگر وجود ندارند. ۱۵۹ قایق؛ قایق‌های خوبی بودند.
در واقع گفتم: چرا آن‌ها را برای خودمان نگه نداشتیم؟ می‌توانستیم از آن‌ها استفاده کنیم. اما هر ۱۵۹ قایق در ته دریا هستند.
آن‌ها هیچ راداری ندارند. برخلاف آنچه می‌بینید، پهپادهای بسیار کمی برایشان باقی مانده است. هر از گاهی چیزهایی را به نمایش می‌گذارند، اما چیز زیادی برایشان باقی نمانده است.
ضمناً همین حالا با ما در حال گفت‌وگو هستند. آن‌ها خیلی دوست دارند توافقی انجام دهند. فکر نمی‌کنم هنوز آماده‌اش باشند. فکر نمی‌کنم هنوز وقتش رسیده باشد، اما حاضرم گوش کنم.
ولی آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. نمی‌خواهیم واشینگتن دی‌سی، هیچ‌یک از شهرهایمان، اسرائیل یا، صادقانه بگویم، خاورمیانه با یک سلاح هسته‌ای نابود شود؛ چون من قدرت سلاح‌های هسته‌ای را می‌دانم. آن را می‌بینم؛ اجازه دارم آن را ببینم. نخواهیم گذاشت چنین اتفاقی بیفتد.
بنابراین، همهٔ این ماجرا دربارهٔ این است که نخواهیم گذاشت آن‌ها سلاح هسته‌ای داشته باشند.»
[تشویق حضار]
«و اگر آن را داشتند، از آن استفاده می‌کردند. اگر داشتند، استفاده می‌کردند.»
---
ما دستاوردهای بسیار فراوانی داریم که رسانه‌ها هیچ‌وقت درباره‌شان حرف نمی‌زنند.
برای مثال، در دولت من، رژیمی قدرتمند که زمانی هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شده است. رهبران سابقش برکنار شده‌اند و اکنون دیکتاتوری همجنس‌گرا آن را اداره می‌کند که با اختلافات داخلی روبه‌روست.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77491" target="_blank">📅 06:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=KI03ENg0uCVoOQitY-i3-7K3EdCOyALdYsvcEKfKhS-qYsq8-cg-qYUnKTCywt_XwRxLzXIlN4CMQM30LV1yQ5SvMytWCOGE3npa59veUuzbUzv-_8co27Ov56lS9zuSj9xYe5kXwsnDfcGPGWPjPbTATyF0He80gmKczif65zwZIVzccnkmtB2-4qWi9jH0IVbh_VlsmMASTzzTiDh2b1_qq2wlt1UsCpykXgq0A11NJxh4gl8IZqnnmVz51iqxWtHSvfasjr7UdF_VWV2tYukN5vFwApoboiP8YUGS5vucPhryCEE4pAuXXUUCdOrszTBWCJNi0Ge7VLSme3ImQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=KI03ENg0uCVoOQitY-i3-7K3EdCOyALdYsvcEKfKhS-qYsq8-cg-qYUnKTCywt_XwRxLzXIlN4CMQM30LV1yQ5SvMytWCOGE3npa59veUuzbUzv-_8co27Ov56lS9zuSj9xYe5kXwsnDfcGPGWPjPbTATyF0He80gmKczif65zwZIVzccnkmtB2-4qWi9jH0IVbh_VlsmMASTzzTiDh2b1_qq2wlt1UsCpykXgq0A11NJxh4gl8IZqnnmVz51iqxWtHSvfasjr7UdF_VWV2tYukN5vFwApoboiP8YUGS5vucPhryCEE4pAuXXUUCdOrszTBWCJNi0Ge7VLSme3ImQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم شی‌هی، سناتور آمریکایی [و افسر سابق یگان ویژه نیروی دریایی]، با انتقاد شدید از اقدامات جمهوری اسلامی، حکومت ایران را «گروهی افراطی و تروریست» خواند که ۴۷ سال است کشور را تصرف کرده و ایدئولوژی نفرت‌انگیز خود را گسترش می‌دهند.
او گفت: این رژیمی که با آن می‌جنگیم، اهمیتی به سیاست‌های حزبی یا اینکه به چه کسی رای داده‌اید نمی‌دهد. آنها می‌خواهند همه ما را بکشند. ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
این سناتور آمریکایی در ادامه تصریح کرد که حملات موشکی پراکنده یا تحرکات قایق‌ها در تنگه هرمز نشانه قدرت نظامی نیست، بلکه «دست‌وپازدن‌های یک امپراتوری در حال سقوط» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77490" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N8TDFdS_rtwRwMz05QFOP4724oGKRpsJEQU0WsIeuHSBAfxvjHQKmpOdl-OqDPCCaTpJZq5OMMd72KVfYt2VOuBEj299w6W80C85XK1zjB3Ez9WIpMA1s1lakQn37RuoXQeJxbkpmaUPuHCc5nZzGst5IyOL9gnbAlSaC1VVPEjqASoQ42_H_KPLOPL48xFu4XR2I3-blJ4ajHHo4TE2BArm3h5o5BywpnlJfMgSgASSAjHje1UFMwVwgyOFjPJVRlKc4Wmt_v15FQX1-VPTG9OXtHEFFO2MISDD_R4CSAb6UABunG0g2odSPmHlIhQETc7tICjQ-XHedI_2h4hLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت فرانسه در تهران با انتشار پیامی در حساب ایکس ادعای روزنامه انگلیسی‌زبان «تهران‌تایمز» مبنی بر برگزاری جلسه محرمانه دیپلمات‌های اروپایی و آسیایی در اقامتگاه سفیر فرانسه را به‌شدت تکذیب کرد و آن را کنایه‌آمیز پاسخ داد.
تهران‌تایمز پیش‌تر مدعی شده بود که در ۲۰ ژوئیه، نشستی با حضور سفرای چند کشور اروپایی، ژاپن، کره جنوبی و نیوزیلند در اقامتگاه سفیر فرانسه برگزار شده که در آن موضوع خروج دیپلمات‌های بریتانیایی و هماهنگی برای فشار سیاسی بر ایران مطرح شده است؛ اما سفارت فرانسه با رد کامل این ادعا خطاب به «خبرنگاران تهران‌تایمز» نوشت:
"به خبرنگاران محترم روزنامه تهران تایمز، دفعه بعد، لطفاً اطلاعات خود را با دوستان‌تان در سرویس‌های اطلاعاتی ایران که حدود ده دوربین برای نظارت بر سفارت فرانسه دارند، بررسی کنید. متاسفانه، هیچ مراسمی در سفارت ما در تاریخ ۲۰ جولای برگزار نشد !"
FranceenIran
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77489" target="_blank">📅 03:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IgqfnytMCD129oNGU5GaQ5e9-ssrOdmPVsD0-eX8fogp5--5nffCSNLvgBXfn5ZyODnvys1-wcxEjadFJN5mgtOwAncxuJl55x2bQYBPNFetCRvU27HTZ3-CBMUtNml_Yw8NYlFaI-RPH4jzZJAU2dKtTuDI1GzMJcbgLdwjEUspRpwsZpRzSBKqoOl2c1o5k7W67iYZYCCQv1COpmQAjwITzsLb0tCWjc3xoKfhIjNYhIcHMZUxhdPr5RfUhkhYzgbJqa67Icu30_tdPvaH8XPhEJN0dtOlZkIIBHjgRpLiVgPqrpaPGgNKtOrNwosEtOkgLMXrAXT2jBwIWK7Kzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریم خان، دادستان ارشد دیوان کیفری بین‌المللی، در پی تحقیقات دربارهٔ اتهام «سوءرفتار جنسی» از سمت خود تعلیق شد.
نهاد ناظر بر دیوان کیفری بین‌المللی شامگاه دوشنبه ۱۸ خرداد ضمن اعلام این خبر افزود تصمیم به تعلیق کریم خان پس از آن اتخاذ شد که روند رسیدگی انضباطی به اتهام «سوءرفتار جنسی» در پروندهٔ او به مرحلهٔ نتیجه‌گیری رسید.
کریم خان، وکیل برجسته بریتانیایی، بارها این اتهام‌ها را که نخستین‌بار در سال ۲۰۲۴ مطرح شد، رد کرده است.
نهاد ناظر بر دیوان کیفری بین‌المللی می‌گوید کمیتهٔ اجرایی این نهاد رأی داده است پرونده خان به نشست ویژه کشورهای عضو ارجاع شود تا آن‌ها دربارهٔ آینده حرفه‌ای او تصمیم‌گیری کنند.
کمیتهٔ متشکل از نمایندگان ۲۱ کشور عضو دیوان با اکثریت لازم به این نتیجه رسیده که خان در ارتباط با اتهام‌های سوءرفتار جنسی مرتکب «تخلف جدی» شده است.
این اتهام‌ها از سوی زنی مطرح شده که در مقر دیوان در شهر لاهه برای خان کار می‌کرد.
طرح این ادعاها در سال ۲۰۲۴ باعث آشفتگی و بحران در دورهٔ مدیریت او بر بخش دادستانی دیوان شد.
تصمیم ارجاع پرونده به ۱۲۵ کشور عضو دیوان اقدامی بی‌سابقه در تاریخ این نهاد قضایی بین‌المللی محسوب می‌شود و می‌تواند در نهایت به رأی‌گیری دربارهٔ برکناری دادستان از سمتش منجر شود.
نهاد حاکم بر دیوان در بیانیه‌ای تأکید کرد که تعلیق کریم خان «به معنای تعیین نتیجهٔ نهایی پرونده نیست».
خان پیش‌تر نیز به‌طور موقت از مدیریت بخشی از دیوان که مسئول تحقیق و پیگرد افراد متهم به جنایات بین‌المللی است، کنار رفته بود.
در این بیانیه آمده است که کمیتهٔ اجرایی تصمیم خود را بر اساس گزارش یک نهاد نظارتی سازمان ملل، نظر هیئتی از کارشناسان قضایی و همچنین لوایح کتبی ارائه‌شده از سوی خان و فرد شاکی اتخاذ کرده است.
این رأی تازه‌ترین تحول در روندی است که نزدیک به دو سال دیوان کیفری بین‌المللی را درگیر کرده است.
@
VahidHeadline
کریم خان ۵۶ ساله که به دنبال بازداشت بنیامین نتانیاهو، نخست وزیر اسرائيل بود، به سوءرفتار جنسی با یک دستیار زن متهم شده است.
پیشتر آسوشیتدپرس در مجموعه‌ای از گزارش‌ها به اتهامات جنسی علیه کریم خان پرداخته بود، اتهاماتی که خان آن‌ها را رد کرده است.
طبق اسنادی که آسوشیتدپرس دیده است، خان با دستیارش وارد رابطه جنسی شد و سپس تلاش کرد مانع پیگیری ادعاهای حقوقی او شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77488" target="_blank">📅 02:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LW1-yba7rbhUoECWeGoihc5FgZuaBiGVBuDOnuevOSmk00iH4VElOTlSUvf_EIwJabLC925YOiN8V__7GLD7SNM08h8fZdCUIo0sVs5AgnrSu11z_43vK8IlVl82bomrGyIn4wy4uISXarBUwlkKcY_CjIJxXuiShLYiyeIbSznkxcGdPQVU1vpk1PHrwAOe9NMVoZ3MH1CaHbBbmcZhyYPGHqoCH2zCcfJo5SR9WGzG6CblH2wCGfUqqaKuRtYtUf-TtO0zvlCvh4famdLjv-7-bmTV_QElyt6DajMJahC20-XwpGgWGZmgU8K5LQzp0uxNHyBCYvZ1QI4T5Mw-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مشترک نیروهای ائتلاف، جمعه‌شب، با انتشار بیانیه‌ای اعلام کرد که در پاسخ به اقدامات «بزدلانه و شتاب‌زده» شبه‌نظامیان حوثی در هدف قرار دادن کشتی‌های تجاری در دریای سرخ، عملیات نظامی متناسبی را علیه اهداف نظامی مشروع این گروه در استان الحدیده اجرا کرده است.
ترکی المالکی، سخنگوی رسمی ائتلاف، با تاکید بر اینکه عملیات پاسخ نظامی طبق قوانین بین‌المللی و با تحقق کامل اهداف عملیاتی به پایان رسیده، تصریح کرد: «بندر الحدیده هدف قرار نگرفته و تمامی بنادر یمن از جمله الحدیده، راس‌عیسی و الصلیف برای کشتیرانی، ورود کمک‌های غذایی و سوخت باز هستند.»
او همچنین افزود عربستان سعودی همواره در کنار ملت و دولت یمن باقی خواهد ماند و هشدار داد که در صورت تداوم اقدامات خصمانه حوثی‌ها، فرماندهی ائتلاف برای حفاظت از کشتی‌ها و منافع ملی «بدون هیچ‌گونه اغماضی» مجددا دست به اقدام خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77487" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A6QwSetJJvvhXHHekRHRv97Jcekj1llB0RChD06-NH2Lu1dsp8K5pGZYg9-4DBnVAKMXHeyfQ9x74UV8BJHDc7OiAzZqE-KOrD6a5bGHYJuXiuG_EHv0gE17xILGXoB2blvCcW7S02fHN7knM5hw4SyLcopGC-pMI63xbZrQ_31_VRFb_4_CEJuKgKI8jXMQVNjFB8jwbSK6XYBzMJHGHX381z9U9rX30Ebflgb6wHUU84ZBSfNTFN_q418r94x6VBbPjFz7mqrn3JmBRt5qgQv9Y8WGvEb6FgCF7PjCPiM3B3qSM73Mv7uAXOFmXqw_PgjqY2kFH4PYYf4EKHlffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
اربیل، عراق (خبرگزاری آسوشیتدپرس) - ارتش آمریکا روز جمعه اعلام کرد که به یک کشتی تجاری دیگر که سعی در نقض محاصره بنادر ایران داشت، شلیک کرده است....
...
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، به خبرگزاری آسوشیتدپرس گفت که نیروهای آمریکایی کشتی M/T Lavine را در خلیج عمان پس از آنکه کشتی حداقل چهار بار تلاش کرد از محاصره عبور کند، از کار انداختند.
هاوکینز تأکید کرد که به خدمه کشتی هشدار داده شده بود و آنها از دستورات پیروی نکردند.
سپس ارتش به موتورخانه آن شلیک کرد.
این دومین کشتی تجاری است که از زمان اعمال مجدد محاصره توسط ارتش از کار افتاده است.
فرماندهی مرکزی ایالات متحده اعلام کرد که 12 کشتی را نیز تغییر مسیر داده است.
....
apnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77486" target="_blank">📅 01:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین
متن زیرنویس ویدیوی بالا
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه دوم مردادماه در کاخ سفید به خبرنگاران گفت به‌نظر او جمهوری اسلامی ایران در جریان مذاکرات با واشنگتن «هر روز جدی‌تر» می‌شود، هرچند تاکید کرد نتیجه این گفتگوها هنوز قطعی نیست.
او با اشاره به اینکه مسیر مذاکره را ترجیح می‌دهد افزود: «دو راه وجود دارد؛ یکی را عاقلانه‌تر می‌دانم، اما راه دیگر احتمالا ساده‌تر است.»
رئیس‌جمهوری آمریکا با اشاره به حضور مقام‌هایی چون جی‌دی ونس و مارکو روبیو در روند مذاکرات، گفت موضوع اصلی «پیچیده نیست» و تأکید کرد که ایران «نباید به سلاح هسته‌ای دست پیدا کند.»
ترامپ همچنین مدعی شد در صورت شکست مذاکرات، آمریکا می‌تواند اقدامات خود را «به سطح بسیار بالاتری» برساند و افزود تهران در شرایطی قرار دارد که «عملاً مجبور به توافق» است.
او در عین حال گفت عجله‌ای برای رسیدن به نتیجه ندارد و تأکید کرد که باید این روند «به‌درستی» پیش برود.
@
VahidOOnLine
گفت که به سخنان شی جین‌پینگ، رئیس‌جمهوری چین، و ولادیمیر پوتین، رئیس‌جمهوری روسیه، مبنی بر ارائه نکردن کمک و فروش سلاح به ایران اعتماد دارد.
این اظهارات در حالی مطرح شد که پیش‌تر پیت هگست، وزیر جنگ آمریکا، در نشست پرسش‌وپاسخ سنا گفته بود چین و روسیه در سطوح مختلف در حال «تسهیل» اقدامات جمهوری اسلامی هستند. با این حال، ترامپ به خبرنگاران اعلام کرد که رهبران هر دو کشور به او قول داده‌اند در این موضوع دخالتی نداشته باشند و افزود: «فکر می‌کنم به آن‌ها اعتماد دارم. آن‌ها نمی‌خواهند باعث ناامیدی من شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77485" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eCcn9qdszFD5jUSk1Wer_Ks_wV2tAuO5-3i9lrmdUwaLOQ839bv_9Qm_v8bk7m4viRCFcR4gZRib3ImwDo17BiYP9TdGTzM_wdMwsP949IVk2dWXs0Zugy5IrHTgsRBsfw-t1BGHTJwZIuHjmhriG41dykMRo5HCSMzOZzI8djADx38R7gKgWIGZevsIOO1p197Qf1gcnK7SJyFss9zTpYgAPiGFkE3qOX9mxaL4TuY5ieBzldSS1nUlbnNcBamxI6bcttisY0SP0B-eoP-U_yYfEQOgWyYfvUvouqUECRfb9ZzRrPCdFcUcZuFiXySM9sOvTI_RhcItmXbN11_5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون روز جمعه دوم مرداد در ۶۶ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77484" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qW4n8USeb35KqjMZnL2TcYNcGqRLRLGSwZmYK1cSet0e0QvvZG94WEhMyaL8JQUDH_IbK-c58bXRwRG4FRIHLSoBdBODbb9leCnkg4YotdNeVzc3nCoH3QMR33aMNHlBiUvlTXqKYotuHzCqVBcJXt6d5bg3u-aAjQiZbtcoPL90i0BdKOnzIN1_4X6rLD7HyFG_KE5IFqbMBaj7S8h96CUWueUU-ncQMaWwIEeLGzEpzKG2gA5rFs7ZDcZHKl-drhGflsf__EZHTb0rWz_OwXLjck0V5-3FqoN9csT4AwpDc3uy2F59rdeh8kiQE-8eXEiO7E8kgzfSsFx_fsh2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lc2UcJd21bpHQNVQYqx7VHGwOruH2FceXfjwIw6Ab-5i5UhY5lMZiov0vEzlfK6dWGMVc0ubgvbzwqHSHP_IgfNw2ECE3oxX8HngdxmgdxzlO-olrWciS0xUpldDfq-V8HZBFrRnTtdSUsQt3NVLv2umBQW2AbyIFx3VTUFNG_gASkaB0AW4klRloGdeWtks5QjuFUXLKhjjZ0fQRQws1zjhWuTJEfT1CgAVkREYsXyF4ZgODEUtDW4WicCVZE0WWB6HeG1V6CPijSW5s0XPz5BdvNQthIEGxk7T3MdTH5Zis2y5pEi9_9HW2hW5C_lZ8hZSKauZzo4N9oV0g-KX-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده روز جمعه دوم مرداد، از اعمال تحریم‌های جدید علیه ۹ شرکت و ۴ فرد مرتبط با بابک زنجانی به اتهام دور زدن تحریم‌ها خبر داد.
بر اساس بیانیه دفتر کنترل دارایی‌های خارجی (OFAC)، این تحریم‌ها فعالیت‌های وابسته به هولدینگ «دات وان» (Dot One) زنجانی در ایران و چند شرکت پشتیبان صرافی‌های ارز دیجیتال او در ترکیه و امارات را هدف قرار داده است. خزانه‌داری آمریکا اعلام کرد که زنجانی با بهره‌گیری از سبد سرمایه‌گذاری متنوع شامل خدمات مالی، تجارت دارایی‌های دیجیتال، طلا و پروژه‌های زیرساختی، اقدام به پول‌شویی و انتقال مخفیانه وجوه برای ایران کرده است.
@
VahidOOnLine
تبلیغاتی که در کانال‌های تلگرام نمایش داده میشن به خود تلگرام سفارش داده میشن و صاحبان کانال‌ها ازش بی‌خبر هستند.
دیروز ده‌ها بار
تصاویری
رو دریافت کرده بودم که نشون می‌دادند مجرمان تازه‌ای حتی از آوتار خودم برای نمایش تبلیغ‌شون در اینجا سوءاستفاده کردند. ولی من امکان جلوگیری از نمایش اون رو هم ندارم.
تبلیغات مجرمانه رو میشه با کلیک روی اون سه‌نقطه عمودی که زیر علامت ضربدر در گوشه کادر تبلیغ دیده میشه به خود تلگرام ریپورت کرد.
فقط کانالی که تا سطح پنجاه Boost شده باشه می‌تونه نمایش تبلیغات رو متوقف کنه. چیزی
نزدیک به غیرممکن
.
بوست‌های این کانال در
سطح صفر
هستند. حتی نمی‌تونم رنگ لینک‌های اینجا رو عوض کنم چه برسه به استفاده از ایموجی‌های اختصاصی.
باید هزاران نفر با اکانت پرمیوم کانال رو Boost کنند که برسه به سطح یک و بعد هزاران نفر بیشتر از افراد قبلی دوباره کانال رو بوست کنند و....
این رتبه‌بندی ربطی به تعداد دنبال‌کننده و میزان بازدیدکننده و آمارهای اینجوری نداره و فقط باید هر روز از بقیه التماس کنی که کانالت رو بوست کنند.
یعنی حتی اگر به سطح یک هم برسم باز برمی‌گردم پایین چون باید هر روز بخواهی دوباره بوست کنند.
با روحیه من سازگار نیست.
خیلی زور بزنم، برای درخواست ریپورت سوءاستفاده تبلیغاتی از عکسم می‌نویسم: ریپورت هم میشه کرد.
از این رو محکوم به سرنوشت مشخصی در این زمینه هستم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77482" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YUyO_BJ8VVB0qiuEpczxFq7N_9wXfhMokM16z3ay3_UET9JWAXr5DloqcU6fReTpz7-GnftVhBISi8OeQpPFe_sCOjll4OjeEL4fdXX0DoEgYmDOhNuXXl7dwrVZUjNWp1DVVHJvufycQLhkY7jbbttvefQzavfJ4sIRkkVMgU0kdQgrSCnw0a4NTQqgsar7LUB6jLfi0Q2XVR86KleW_p5nhkKrbLf1aM_xZf1ZxfjlEYUez_rUDJp1E2wyFh7iDA2tOLfGz88ETqWPx80Tb240iNuIHzTKKiXbdVkRG8ACePF-B9wfjjb_Op5cmny3V4Sb6ZK01Mex2Jb2ebKFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رئیس‌جمهور شی، در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت — و این اظهارات شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، حرف او را باور می‌کنم و علاوه بر این، من نیز لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین جریان دارد (روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز برقرار است)، به من گفت که به ایران سلاح نخواهد فروخت. او می‌داند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را پرداخت می‌کنند و اینکه آن سلاح‌ها چگونه توزیع می‌شوند، هیچ اطلاعی ندارم.
بنابراین، دو کشور بزرگی که مردم اغلب در ارتباط با ایران از آن‌ها نام می‌برند، به نظر من، در این موضوع مشارکت نمی‌کنند. اگر چنین می‌کردند، برایشان بسیار بد می‌شد — و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77481" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLLMW12TqlkwTRgm1yYsAXc5wIhgdVvXLEL3D4n1_fEVNvUzPHxTmuDyAWE_hWy34gKmbsFu1VvLMI8uS_hMRFaINcT5aLxrADtxTz0VtA37UVm4O586XU2-yy6KULYKRUuTu5KNfLTCmJ3iXiqeO4AVxE1RLkXq3KGt_TKeIZoYTNTk_eXBUv_9GMOpgYwb0BG_nz8nr11wWxuSu3FBLSgFME0u_duu4jNdS8Kf6udwU5LhVOgcrcCizd9QU3-ZO1SJ7fsl1KICO-Euw9g8P49PVVVXkeMOs9M82MJ3XL7S1bhLAL9de1AAEPsN8EH1eGe0mtBhc16A53xQsdN4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای اطلاع‌رسانی دولت روز جمعه دوم مرداد، با صدور بیانیه‌ای از اقدام سازمان صداوسیما در سانسور بخشی از سخنرانی مسعود پزشکیان در روز ملی صنعت و معدن، درباره اجازه رهبر پیشین جمهوری اسلامی پیرامون مذاکرات، به‌شدت انتقاد کرد.
در این بیانیه با اشاره به سوابق مشابه، از جمله پخش نیمه‌کاره مصاحبه رئیس مجلس شورای اسلامی، سانسور سخنان رئیس قوه قضائیه و پخش نشدن مصاحبه‌های وزیر امور خارجه در طول جنگ، رفتارهای صداوسیما «گزینشی و مبتنی بر سلایق سیاسی یک جریان خاص» توصیف شده است.
شورای اطلاع‌رسانی دولت تاکید کرد این اقدامات وحدت‌شکنانه دقیقا پس از پیام رهبر جمهوری اسلامی مبنی بر لزوم «وحدت کلمه» صورت گرفته و نه تنها شایستگی این سازمان را به‌عنوان «رسانه ملی» زیر سوال می‌برد، بلکه تهدیدی برای امنیت ملی و انسجام اجتماعی محسوب می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/77480" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IA64-HSk4UI9FVsZV6n-roEoNlA1y2oqQvBrTGSj2gcETZbnxOpwB2EAqXEcyEosJv1OLwU6ByiaOWE5meoYUm09pxv-o4E8eUsecPB7Xzkio0vSxaZvh2btLnRy9jtiJiPKUkXYWrFVdrZE9junwlvNzi1RWf6YgZ9ZGsOA10gxhwLG3nCOHpCQNpTSaDSmJ91860LOmdjCRounHwyErqFuo5DOrtraAAJr3BSJbA623yLCOx1hL82rUrV2mZmLS-yt_XuyyBp2v0cv1zEZXX9SxPELH-IdfH7ITEBA0Al0wBCH12czaMafWSGhMkIVp2841aWXoAIfVSfo0D1CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین (شاهان) علیزاده آذر، زندانی سیاسی، با اتهامات سنگینی مانند «توهین به رهبری»، «تبلیغ علیه نظام» و «سب‌النبی» به دلیل «توهین به آدم و حوا» روبه‌رو شده است. او دی سال گذشته نیز بازداشت و به «تبلیغ علیه نظام» متهم شده بود.
این شهروند ۳۸ ساله و مهندس نقشه‌بردار، با قرار وثیقه آزاد شده بود اما بار دیگر در ۱۳ تیرماه مقابل منزل خود در اسلامشهر به دست نیروهای امنیتی بازداشت و به زندان تهران بزرگ منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77479" target="_blank">📅 17:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuRJD6Eu1eNOVSPOKWL1ALZLokdjc3m6K8uO7DT2OU8i7mOS8ua4-TxiPa__PbkfNz1TnWAc7qgzs-Es5nQeeBvEajdUQmKPAr2xpvj6XSV7ygQquYRbKVbXAM0YR7PqeDfIL3FrFbKsFHan5taVKh-o2ORhZXY3G8HEYUPTaR-afNeKm8xib68DtooHLfOrzfQ3KLXfN6RJRg_uekthYz70Zu5LgN7nU6cbfxoR_JYGeLM3_YT7bCWlFZFcS-kPRVVhSmD5JTDCHhAlgvhhXpSKQCFy-4ysu6mcTdXT8TSjM4_D_-chHaVb2KF2LSwxDkoHFrzkbYPd0cY_H3iVpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی وال‌استریت جورنال روز جمعه دوم مرداد به نقل از «منابع آگاه» نوشت که دونالد ترامپ، رئیس‌جمهور ایالات متحده، در روزهای اخیر نسبت به این‌که مذاکرات با ایران بتواند به صلحی پایدار منجر شود، بدبین‌تر شده است.
یک مقام ارشد دولت آمریکا به این روزنامه گفته که «ترامپ معتقد است تنها چیزی که ایران می‌فهمد، فشار نظامی است» و افزود او در برابر تهران در «حال و هوای انتقام» قرار دارد.
این مقام همچنین گفت رئیس‌جمهور گزینه‌های مطلوب چندانی جز ادامه حملات نمی‌بیند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77478" target="_blank">📅 17:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfH6oXQlBRlSP6ztyyvdfw9ZK6f4AiCcvHWA1UEwE50blLs_LIV8MqStTHGNwmhUarpaZ3XTDBvJWf61DK9knSoq0CeQ7ldPLwKaDQ8d5M6ADPMh8yoeD5R_P2qja-ZxzK4jVox44HTo3YyHD3tMfTE1k3S9WTdwih3tXlrC-8sMi--faLc7J_ruRe2qkxdaaNei5kx4O0aA4F5fRYL6t0FYSzMRDIX4CsafA0nmvrMy1IJIB069WzgaRF_uHXZ28x4rcJczvH4v8betH-B7v09JyGdmqWkKPNB0wlkk6BpeBKsmu9kLLufFxP7qjgi3WacT92kNK59lAh-0CSUqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا اعلام کرد نیروهای مسلح آن برای حفاظت از کشور در برابر هر حمله‌ای آماده‌اند.
این موضع پس از آن بیان شد که سپاه پاسداران انقلاب اسلامی هشدار داد نباید به بمب‌افکن‌های آمریکایی اجازه داده شود از پایگاه‌های بریتانیایی استفاده کنند.
سپاه در بیانیه‌ای در روز پنجشنبه اعلام کرد آمریکا از پایگاه فرفورد در جنوب‌غربی انگلیس برای انجام مأموریت‌های بمباران علیه ایران استفاده کرده و افزود هر پایگاهی که برای چنین حملاتی به کار گرفته شود، هدفی مشروع خواهد بود.
اندی برنهام، نخست‌وزیر جدید بریتانیا، هفته گذشته در جریان این خبر قرار گرفت که لندن بار دیگر به توافقی با آمریکا برای استفاده از پایگاه‌های بریتانیا در چارچوب آنچه «دفاع جمعی از منطقه» خوانده می‌شود، رسیده است.
یک سخنگوی دولت بریتانیا گفت: «نیروهای مسلح ما آماده‌اند از بریتانیا در برابر هرگونه حمله‌ای، چه در داخل خاک کشور و چه خارج، محافظت کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77477" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzBxRwvS8BcmNNrjPDAziSWVuoh5fcRxvn6_ohQF-nNtk8eP4vZnnKlAv7dbihYwhF-cvwUrPGpE3DHXc-y8gLBbyuN0F6dmkJr84MIG6aN3BXr6_5gW8K7NtO-3sMecP5KHY1mKoH09OoAZqgxoUj56ba-iN4A3McB6pUjyV7Hztnox4VXOVDkVqiSNXDDEVvH1RhfCJFeRRMpxZRUftv4JO9vmt5ovzr0a5mEsWL4tM9OwcOJewt4u8AMLceWVt3cKwkQirdTWVM8luBhm7oYXAUvMqI6oTVApeRNLPbVhzpG30_250w3aGFRFkRGJUCqdI6D1cP5HClsWw1pX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران روز جمعه ۲مرداد۱۴۰۵ با انتشار بیانیه‌ای مدعی شد در جریان عملیات موسوم به «نصر ۲»، ساختمان باقی‌مانده مرکز داده‌های شرکت آمازون در بحرین را هدف قرار داده و منهدم کرده است.
سپاه در این بیانیه ادعا کرد مرکز داده آمازون نقش اصلی در تکمیل اطلاعات ارتش آمریکا را بر عهده داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77476" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gx1seTvxmVlxiGQXGvrfK4WMtZBArtYhhj57VyuTlyJAJycTpkaNDf6n3-KQgdMkNYVG2TZ8lAzjPHEtRsxbicqiThmi88XBLNm-fpdrn69Xe_h5Vk91aORx3S6I74tjbB3KdvrWakXKcDjviCJK7fdnYMtgO2jKYYBWdtkysRKnkPUrEi0lwT9qzBkfCtmOoAPyaVDfPomgMhNFgnHdKRSGp6aRv-vo9wcsESR4zuAkjtBzWTMU90RLpJ8CBX8bbgFsY3YcXTxhL6A7UrZvDLTQGJP28FyFEMAjxKVlmps4Tk3R8ye9ei4ZUrZPKsVDUD71XiDEd4Glgo18YYeT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NluQHRc4ZSYlavYOn_u-9Xdeg3tSqshwZt0ojRK64ET9Biqa9CgWzGfoH8jN3ka00NNKGvX1pXbg-8byWeQvRkr_r2gRxwjqMKPuPjnWdNVBIKePZTiFIJVQeMW5ke0ZWa0SpsFW2Cjpe26WI0PM8bAV2Fl_n9OwKW67Mw95SZ_7LkEK57H59sKGqQQxXZl5uksX47UKrrc1NOdznG-HTWjz2BaL2Hoq7gBUiw3BqLRpOfUUtlyjaWnz32t8_Ie-UzZ52UznE572QoSUalZRaiv3dmk4Y9sjFHBBLIh2AlWeqksc-2T1uhJqIK5LUl98Qj7taLMApStUIe6dA3SQog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه نیویورک‌تایمز به نقل از چند مقام ایرانی و عراقی گزارش داد که جمهوری اسلامی ایران پیشنهاد آتش‌بس از سوی دونالد ترامپ، رئیس‌جمهور آمریکا را رد کرده است.
بر اساس این گزارش، پیشنهاد یادشده در جریان سفر علی الزیدی، نخست‌وزیر عراق، به تهران به مقام‌های ایرانی داده شده بود.
آقای زیدی در جریان سفرش به ایران از جمله با مسعود پزشکیان، رئیس‌جمهور و محمدباقر قالیباف، رئیس مجلس شورای اسلامی دیدار کرده بود.
جزئیات این پیشنهاد آتش‌بس مشخص نیست اما مقامات ایرانی به نیویورک‌تایمز گفته‌اند که این تنها پیشنهادِ روی میز است و آن‌ها علاقه‌ای به توافق موقتی که مسئله کنترل تنگهٔ هرمز را حل‌نشده باقی بگذارد، ندارند.
@
VahidHeadline
دفتر نخست‌وزیر عراق گزارش روزنامه نیویورک‌تایمز مبنی بر انتقال پیشنهاد آتش‌بس آمریکا به ایران از سوی علی الزیدی، نخست‌وزیر این کشور، را تکذیب کرد.
دفتر رسانه‌ای نخست‌وزیر عراق روز جمعه دوم مرداد در بیانیه‌ای اعلام کرد ادعای مطرح‌شده در گزارش نیویورک‌تایمز «کاملاً بی‌اساس است و هیچ ارتباطی با واقعیت ندارد».
دفتر نخست‌وزیر عراق در بیانیهٔ خود مشخصاً گزارش مربوط به انتقال این پیشنهاد از سوی آقای الزیدی را رد کرده و درباره وجود یا عدم وجود پیشنهاد آتش‌بس آمریکا به ایران توضیح بیشتری نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77474" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=kMQjrnZcX0cNrg7lRDCVVNpRamRyrAv7Qoq96zaGMKTrToUjQkmxxn8a0-IOvx6R5j6kJpZKmMzOvWBNa27EIKuarmLJ4gLuNKMbG_xW0E7gTcXlNcVwC_l8Kgt-5anHmlreauTkuhVgwpz0rn6TaaSWDiraHuB_mwM_BYC7r2NTpjhZY09AxMFJmLDir1ar3hsn9_bIo-ynCi1tBvGIRUx8WjP4w7aufrfADMaMgIYJ1RnFt4YsL30FkufT_woZgxMAsWBK5G5kO3LMr1EZEPZQZqvLs2-5gPhC99A4G7wJbVVIvEM98am4SU38Vsx2Hhg1OPLaHhbGEXpbaTCUsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=kMQjrnZcX0cNrg7lRDCVVNpRamRyrAv7Qoq96zaGMKTrToUjQkmxxn8a0-IOvx6R5j6kJpZKmMzOvWBNa27EIKuarmLJ4gLuNKMbG_xW0E7gTcXlNcVwC_l8Kgt-5anHmlreauTkuhVgwpz0rn6TaaSWDiraHuB_mwM_BYC7r2NTpjhZY09AxMFJmLDir1ar3hsn9_bIo-ynCi1tBvGIRUx8WjP4w7aufrfADMaMgIYJ1RnFt4YsL30FkufT_woZgxMAsWBK5G5kO3LMr1EZEPZQZqvLs2-5gPhC99A4G7wJbVVIvEM98am4SU38Vsx2Hhg1OPLaHhbGEXpbaTCUsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار گیلان از حمله موشکی آمریکا به مقر نیروی دریایی سپاه پاسداران در زیباکنار، در صبح جمعه دوم مرداد خبر داد.
باقری گفت: «حدود ساعت ۷ و ۳۰ دقیقه صبح جمعه، بخشی از تجهیزات مستقر در این مجموعه در حمله موشکی آسیب دید.»
معاون سیاسی و امنیتی استاندار گیلان همچنین افزود بر اساس بررسی‌های اولیه، تاکنون «هیچ‌گونه گزارشی از تلفات انسانی» دریافت نشده است.
@
VahidOOnLine
مدیرکل مدیریت بحران آذربایجان‌غربی اعلام کرد حوالی ساعت ۹ صبح جمعه ۲ مردادماه، یک نقطه در شهرستان پیرانشهر هدف حمله هوایی آمریکا قرار گرفت.
پیشتر اخباری از حملات هوایی و موشکی آمریکا به اهواز، قشم، بندرعباس، تهران، امیدیه، اندیمشک، خرم‌آباد، خنداب در استان مرکزی، نایین در استان اصفهان، تفت و شیرکوه در استان یزد، فیروزآباد در استان فارس، کنارک و زیباکنار منتشر شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77473" target="_blank">📅 17:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mALDM6ouuqfU2n-5ipfEk7TtoCltVNV54o0JKa4qE2NYmiUoI-uieBoJY0wt59sXkVojb0Pkvydd1l_bOcJ9HthjXPbr-Ce_SpJucyO8HFfxxrqmE5yjE1hVXBHhkNIwYKxmrl28s54Mc_2cB_y9XUOXNyNfV27Nz9c8nDeRd2UC-OTM2rxub3Wb-oeYGwH6HRAYo62tiYeopYZM6ocGkk_Zf22BkwBykkFDCAUdUxDpB1QjimoLPmLNYkA22Arayrd4hPytffjULrAYsbiWAxcAl8I812Y_ogWfObgUPrNxHmvuHuTPG9xnVNTc_v60TiqCMsuLqHFAxawHuYz2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZ7Tum3SKrHGeuu5d7lP4DheeDVLM3178CsF_-Li-XB9P3ysf9dgPF2sN7Hc1cKl9OGkOUYT9LVWHTARhncmTcUOLuHg6cBuSO2JdpCOlzd4eYMY3XJaoOJOufi6ycF0q4mMen-6xold9Ydo2eSKGVw5RzAlxO_bryjzTaiICHruNn94-ujUrKN4hQBMNS_FGjQkKYqGeeMXqNBlm50CfilM60U-PPvikGHnojqeyO2L7cLeg6mtTPSUmW8MPyvuN6YUrWsBmfApHiqHZqXPkPbsm8DAQYCVjsTVU9Qn0wMRQhf8prgFdNYm0iWizDBrGc0kLVIlgJGSQ_e45WPuvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عفو بین‌الملل روز جمعه دوم مرداد از مقام‌های جمهوری اسلامی خواست که فوراً هرگونه برنامه برای اجرای حکم اعدام بنیامین نقدی، ورزشکار، را متوقف کنند.
بنیامین نقدی ۱۳ دی‌ ۱۴۰۴ در شیراز در ارتباط با اعتراضات سراسری بازداشت و به‌مدت ۵۳ روز به‌طور قهری ناپدید شد.
رسانه‌های دولتی ایران یک روز پس از بازداشت و پیش از برگزاری دادگاه، «اعترافات» اجباری او را پخش کردند.
این ورزشکار بعداً در ۲۲ اردیبهشت امسال به اتهام «افساد فی‌الارض» به اعدام محکوم شد، با این ادعا که از کپسول آتش‌نشانی علیه نیروهای امنیتی استفاده کرده است.
عفو بین‌الملل می‌گوید که حکم اعدام برای بنیامین نقدی پس از «محاکمه‌ای به‌شدت ناعادلانه» صادر شده است.
این نهاد حقوق بشری با استناد به الگوهای پیشین مقام‌های جمهوری اسلامی ایرانی در گرفتن اعترافات اجباری «تحت شکنجه و سایر بدرفتاری‌ها»، ابراز نگرانی کرده که «اعترافات» بنیامین نقدی تحت اجبار گرفته شده باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77471" target="_blank">📅 17:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6jB4DIRKXVhucP9Wap0bddIv2TOEUR_ZcaLV3ulUUJsE_IYnQ5N3OHz435-VPZbOtocX_NjoFDXgqVx73Z3cajQyT3RdrL9bKBTs19XYRAm9zE4jJfYSQ1SrQWdqDLzml8TXZTtQB1fDJLuSC7lek9bK8jwVGEOrbzgLDRBfdOwy3CaJnHaaUQ9D9_MVEzvEIUG8QInQu0lQj6mY_SWVmwKqpeObM_017McZtod7dQJAzEnHIMC9ueU2qyCiG4Ezl8zlZfDia7Re8mTQeTclzK1UDSxcVbgVJju5dv3ckFk_fq7sLWVrrnopK0foPWSfTU0gVowaTY_CZPZVb75Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته بود:
از این پس  خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
واکنش عراقچی، ترجمه ماشین:
مصادره دارایی‌های یک کشور دیگر برای پرداخت مطالبات نامرتبطِ آینده، بدعتی آتش‌افروزانه است.
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به یاد داشته باشند: وقتی دولت‌ها مصادره را به امری عادی تبدیل کنند، دیگر دارایی هیچ‌کس در امان نخواهد بود. هرج‌ومرجِ متعاقب آن نه زیبا خواهد بود و نه مسالمت‌آمیز.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 482K · <a href="https://t.me/VahidOnline/77470" target="_blank">📅 06:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZMMIv2Yf9tAok_X_77FrTqaGdTuNJVHdC84TNWtzpA2GNFeAZJzgbXkItUUg-y2iZKFU1JSCjV3lory1xKuPpxCmEfhGI9l1xFU_9gAB4bby9FsPWNWi5iK_ZRO8FrlqXg7V9CLKLIg9a0x20bTDMfLiWMEyLHrusuo3DVGb-ouoBXtPVGPUU30LmvawL_iqZSjAWSIwfDk9LJYHmt1o9rHr57cm_K9CbZrVU8QKt8QzAmCmMJIB-f1XfHGScImWDlT1YrqEFPWHxRTNedCgFE5jt-i0EQChg655TTT2twO9e6ARRdGM5U398h2gLiu70j7vGSkoLh_iYg3dTHwbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N-8g-6g_wAUM5fXh2FjASlE2-1TCm7_iOYb6reHeBelK5VxIGZCoiM9I7-Ys2XmH1zJYvLvLg3RGWKPE4Zus8KYG1_rtmWUPaI2qby_D-NwDEFoF-H-RZyG_smXV379Tz0zrGOyvMt5mXJgc0GY4HcJbcItjjg1NNzk_JdsoJmPEDYCtF8WdwVFo3hL9iG5PHcuJ8OOz9HRq-qcLeAKxjzpn1yu7KRNAiyyJM9N2Hi3ly2TmwHI8FMaShtEKpu9klE9DAXACI2Hjc2G_QNtCKLj4QvXWby5KKwsUJEtChEp7oYdwPMqgobUnPGSZsh5wiNPRA6GFC6JjDRjRQQqu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MruLXa-XwibeyyGRWguK8NOg0LJkLlUQxjG5PptUUlIEpvEqVImjq_tlaEH1_Gwctuxcz4sikVWQJjXa19I9V29XzipcC0--US8UNfV03cKMUr-OnyDvoOvzzdAjvLe8oo-DUawISslFC-8KAA0FkEvMNlEYSRYsG5wkMZnmR2r-2akgltyqR-LvqX7dr4pDVG535BdHTrp9yWYc-LnXl-QKjzR1q-77XFrWzqMNWLvSFjZPShGIWVyBhd7HwAwUl9el5KRWE6JTCi7PNpELhT-TyyHtCo9e-n6rxecbF8qv-qjjtv_X8nH9R2fzLbumKYCYSlj8o4SwXF71GCmsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ap-T3rBIcV-ALKH6VLUPakD3xFZjmBfYA5llNb5AF6E08mL5YHRf97uZrMgvdW3Sjmfz8Ng_XygG_jy6tCO9sA37fbb34Y0TfaqL6UOuOQPZrWMJJUQW1NxCVVXUfWLZVchLtjqcPF7bA_t7s3-rrJU7hHnRSFrgPoWruKADKg10Hnp7VlYICBlItCYoP9FNqcaW1OzUKyVjXGdXqXgvRR1Q-6w4Z5vmMpWo6_GvuvZFTm_jkuY98o20s7JKh52_K2DDykHHc9J_8klEPIm3IhwVzhDEawkqzeazvVAlDxaqWAj3Ojq9pJ4h43rBrlqTf6GBzO_YKAdAQQfB4PwTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pBze1NNvG3UkRBQtJ1q4mnOc-WjKHdVenK0wC_T3KFr-973sb6VcG5PPYQ2XpN1ATmrtHLjpTXRgCmNv9hGzdq7S62mu3oHlc7Ru-5OyNJQh2NuuQbSbs-MyR72h09dVcRgKnySMpxUL051T94z4H5k3pZbn7pfajiBXIUQZA_kgmY07ynm67qR1cyfH5-xL9wk_ztGU153CZjiuCm91a7zhwD7hARN64BWRnT4j5Hn7YS8sEi9_037T13qps4HvJtUsl7Dq-1JrVnXlqEXjxYHgCGdjwVl0U152pDb_CxE_ssIX2_kVsZljCn1endhof4QayXLWQ56XyoXc-5_idQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MLzog_H8rSxaSr77xQBk9QyVisqfyDrpUXYyKkItd4jQ6a8oM0yOp6_ulHO9jwWf2aXJEjPBZVjlOIxp5ivLd1jDHyyUFGwaAox6BS0IRSSjJcVxTma4USzhZ2DVjYRSAkPf1-lQGeQvNB2uJjEyxNQkyWv4Zo6KhE_AgtNqVgg3TAu8N6248chu9hZdaLREcppazbv7I-R6fNRlcOowC7HxyfBjJzZm-kDi0ySv3kYSIq6Wl4MfsUQEBFTFSKRHRuDq1bl1I4sljx9BMraTW4Zq1s7jFCMRj1FRHC2gtBs-J4YzojUCgkpMm6AP0mJCXzRba1_atm1f8UiGrx59jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=JTW-urPWcaToaMuTCCbXILwFsKrsKncK8B0Mi4wBkqTqKiUcpPeewIGx5oYtB-_rrlOryNXFZlzWn8TrBDxMql5CjwQu0vUUO8m8vkcETFG_2yc0iIPuNLLOXY0BZQABg6OCYMo2Tnde_hQDOtPJCuL0J2wePZ4kNMToq-zr-o2hjCL0hSppQ1PPfvH31gZu7taqML2Y6O6RRDCrYxDFf9EZtGFdqK-BmwzBqYUMivyNKV0L_VU2UjA2x2q4SaJTl2SnArCIus_yawKl7AJnACc209ygna1Z1daHnhAULQEqprfT7z27Eqf5_R0iHWLqGVtKi1VrdpCC6pTHHebsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=JTW-urPWcaToaMuTCCbXILwFsKrsKncK8B0Mi4wBkqTqKiUcpPeewIGx5oYtB-_rrlOryNXFZlzWn8TrBDxMql5CjwQu0vUUO8m8vkcETFG_2yc0iIPuNLLOXY0BZQABg6OCYMo2Tnde_hQDOtPJCuL0J2wePZ4kNMToq-zr-o2hjCL0hSppQ1PPfvH31gZu7taqML2Y6O6RRDCrYxDFf9EZtGFdqK-BmwzBqYUMivyNKV0L_VU2UjA2x2q4SaJTl2SnArCIus_yawKl7AJnACc209ygna1Z1daHnhAULQEqprfT7z27Eqf5_R0iHWLqGVtKi1VrdpCC6pTHHebsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: پرتاب موشک از بیدگنه، خمین، نجف‌آباد، شاهین‌شهر و...
تصاویر بالا و پیام‌های دریافتی از استان تهران:
همین الان از ملارد موشک زدن
همین الان ساعت ۵:۵۲ از بیدگنه موشک زدن
سلام وحید جان همین الان موشک از رو پرند رد شد
سلام همین الان 5:51 از ملارد موشک شلیک شد
از بيدگنه موشك فرستادن الان ساعت ٥:٥٠
شلیک موشک از بیدگنه ملارد ساعت 5:50 بامداد
۵:۵۰ دقیقه از بیدگنه موشک زدن رفت بالا
سلام وحید جان از [....] بیدگنه الان موشک هوا کردند بعد جنگ ۴۰ روزه این دومیش بود
سلام وحید ما فردیسیم همین الان از سمت بیدگنه فک کنم موشک پرتاب کردن و صدای شدیدی اومد و لرزید ساعت ۵.۵۱
5.52 از کرج موشک فرستادن ردش هم تو اسمون افتاد
اشتباه نکنم از بیدگنه
وحید جان سلام.  رد موشک از سمت اندیشه  شهریار خیلی صدای مهیبی داشت همین الان ساعت  ۵.۵۲
آقا وحید سلام ساعت 05:50  از بیدگنه ملارد موشک رفت
سلام. روز خوش از بیدگنه موشک فرستادن
جمعه دوم مرداد ساعت ۵:۵۳ شلیک موشک از [...] بیدگنه واقع در ملارد به سمت جنوب غربی
🔄
وحید جان همین الان دومی هم فرستادن ساعت ۶:۰۰
سلام وحید جان همین الان موشک از رو پرند رد شد
شلیک دومین موشک پیاپی از ملارد
از ملار یکی دیگه شلیک شد  6:00
دوباره موشک زدن از ملارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/77460" target="_blank">📅 05:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=Qu8QIPhDjN9exlSYZT2A2RBawIh5aM1cy3UJ_FP727rxMMKyBcntYUhStbYC3JdrZJYbSB5V4LgnMqJwCYn7Hm4vConIo8G4NZ4q5EfnTM-NTpCcPkRwZ3g5e4ILQEk8kDOGEem8HhzKaHttDchmEKX9qIjMTOvD3NIZSH4rBTKfJ-3axi-cP2uzHP9CxICDiRLM3hb9Mq5RaLrAiQbG4QTk3Yiy7q7F7V_vHTgG-NqZeFylNBx-cSDF1uMlR37L_6sdE4H1ZKRs21Dg4MydIPgj2mJbdDhGtrd9c-qrwIaCQlNLeZ2h-THSIHT4bqwc9WpmoPRIJUn0KJ0yvrw8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=Qu8QIPhDjN9exlSYZT2A2RBawIh5aM1cy3UJ_FP727rxMMKyBcntYUhStbYC3JdrZJYbSB5V4LgnMqJwCYn7Hm4vConIo8G4NZ4q5EfnTM-NTpCcPkRwZ3g5e4ILQEk8kDOGEem8HhzKaHttDchmEKX9qIjMTOvD3NIZSH4rBTKfJ-3axi-cP2uzHP9CxICDiRLM3hb9Mq5RaLrAiQbG4QTk3Yiy7q7F7V_vHTgG-NqZeFylNBx-cSDF1uMlR37L_6sdE4H1ZKRs21Dg4MydIPgj2mJbdDhGtrd9c-qrwIaCQlNLeZ2h-THSIHT4bqwc9WpmoPRIJUn0KJ0yvrw8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۹ شب ۲۳ ژوئیه به وقت شرق آمریکا [۴:۳۰ صبح به وقت تهران]، سیزدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندند.
سنتکام مراکز فرماندهی نظامی ایران، تأسیسات نگهداری پهپادها، شبکه‌های ارتباطی، سایت‌های نظارت ساحلی و توانمندی‌های دریایی را هدف قرار داد تا تهدید ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از تنگه هرمز را بیش از پیش کاهش دهد.
این آبراه بین‌المللی، با وجود حملات اخیر سپاه پاسداران انقلاب اسلامی ایران، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با پشتیبانی نظامی ایالات متحده همچنان آزادانه در این تنگه تردد می‌کنند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه در حال فعالیت هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77459" target="_blank">📅 04:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان همین الان صدای انفجار خرمشهر
درود خرمشهر صدای انفجار ۴:۴۰
خرمشهرو زدن
سلام وحید خرمشهرو همین الان یه موشک زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77458" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان یزد صدای انفجار اومد
سلام یزد رو الان زدن
یزد یه صدا انفجار اومد ساعت ۴/۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77457" target="_blank">📅 04:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چند پیام دریافتی از فیروزآباد در استان فارس:
سلام فیروزابادو هم ساعت ۳:۴۵ زدن
صدا اومد فیروز آباد فارس خونمون لرزید
نزدیکی فیروزآباد فارس چیزی شبیه انفجار رخ داد و موجش بد جور گرفت مارو
الان صدای انفجار فیروزاباد
ساعت ۴ صبح
انفجار مهیب
سلام  فیروزآباد در خونه داشت از جا کنده میشد
دوسه نفر  میگن پل احمدآباد بوده که راه ارتباطی هستش به سمت جنوب
آپدیت ۴۰ دقیقه بعد: صدا و سیما
شنیده شدن صدای انفجار در فیروزآباد فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77456" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت 3:43 صدا پدافند شرق تهران اومد ولی کم بود
ساعت ۳:۴۵ صدای پدافند شرق تهران فعال شد. از حکیمیه صداش میاد
پدافند شرق تهران فعال شد
سلام صدای انفجار در پردیس تهران [لابد انفجار شلیک‌های همون پدافندهای ضدهوایی است.]
الان هم پدافند زد
پدافند پردیس فعال شده.
شرق تهران صدای پدافند
[+ پیام‌های دیگری که با تفکیک اسم محلات مختلف شرق و شمال شرق تهران دارند فرستاده میشن و دیگه نقل نمی‌کنم چون همین محتواست که هی داره تکرار میشه.]
آپدیت:
بعد از چند دقیقه تموم شد.
🔄
ساعت ۴:۱۰
دوباره صدای پدافند شنیده شده در شمال شرق تهران
🔄
ساعت ۴:۲۲
پیام‌های دیگری درباره شنیدن صدای پدافند در شمال شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77455" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fHRjX4Fz0XQNaFBeW1MXJJ7h5xZtyVIZ39T6IfC1h6VtQ7kvdJkHq06skZFdtKVV6jpeDZ1ztib5U0Rj1mN7Mo5eAhGqz5zddQIPdTntqHlysO3NSsuOdctuVTIU-OilbVUOi_lL43NwgbYT2Vr50pQG4a7ChXrBOKcSy6V4ayVNLhWKBYmY6lcxlcyZNsEncYL_SRxNjAsrMwFqbLoJE54lgiJG4Hv0owGj9QJftizvpqSZzPM2k9DlIuig-beKmQavLlRV4m0OVCJwiRkVqNEIPbJk1MYUr2oPJk2Bcgdm_uk3FhKqilSyytr0TqV5R8SuWDfI8zeBhdgr_HA9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: تفت در استان یزد
پیام‌هایی دریافتی و تایید نشده درباره مناطق مرکزی کشور:
ساعت ۳.۰۵ دقیقه شهرستان خنداب صدای انفجار خیلی بلند اومد
سلام خنداب و زدن 3:05
نزدیک خنداب صداهای وحشتناکی میاد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی گفت: یک نقطه در خارج از شهر خنداب دقایقی پیش هدف ۲ پرتابه دشمن قرار گرفت.
———
سلام وحیدجان همین الان پایگاه نیروهوایی انارک نایین را زدن
آپدیت چند ساعت بعد: منابع حکومتی
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
———
تفت از یزد هستم
از سمت بام تفت - شیرکوه رو بد زدن
خیلی صداش بلند بود
ساعت ۳.۳۰ دقیقه تفت صدای انفجار امد.
دکل تفتکوه رو منفجر کرد
سلام ۳:۳۰ تفت استان یزد صدای انفجار مهیبی اومد که از خواب بیدار شدیم. از کوه های اطراف نور و گرد و غبار شدید بیرون آمده.
داخل شهر نبود
سلام وحید جان .ساعت ۳.۳۰ تفت یزد صدای انفجار شدید اومد و خونه ها لرزید.
صدا از تفتکوه محل منطقه گردشگری در حال ساخت بام تفت بود که از اول جنگ کلیه نگهبانان و پرسنل را سپاه تخلیه کرده و هیچکس اجازه رفت و آمد ندارد
خبرگزاری‌های محلی میگن موشک بوده و جنگنده اصلا صداش شنیده نشده
آپدیت: صدا و سیما
صدای انفجار در خارج محدوده شهر تفت در استان یزد
———
بروجرد انگار زدن صدای انفجار اومد. دو انفجار پیاپی
بروجرد زدنننن
صداش وحشتناک بود
بروجرد صدای انفجار شدیدی اومد
دو تا پشت هم
آپدیت:
در بروجرد فقط صدای عبور جنگنده شنیدم
اما صدای انفجاری نشنیدم
از باقی همشهریان هم پرسیدم نشنیده بودن.
صدای جنگنده شبیه  جنگ ۴۰ روزه بود که بعدش خبر بمباران خرم آباد اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77454" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtgwXIPsJl-uIo06IrXEUkHFJXVWH8Wvywz58Q6OxPF7kgyFAxq_SrFxKQjI78jCkPXIRX5Ujavek3rYfhKGLdXt6YEc4_l13fOcjelz_z35NgIt_9bFD8qvDNV0hTfVg73PaVk7HswkLk7SIHZ7ZJ4TZKMlCYFmQhTrNoKt1inLrzBJ1w5RXhLwvM_d42Qfybsf8vZFIzr5bkKCkpurN4OWY5B8ZcXox10_0eOdsTRGca7AxBVpnUzvBKVNYDdhldRxpguRiYnvPqppgF9uwRcmrC2sw36QNdO53vjYEh4AmpNnQ6y6LWfKGH9yhjoBA94kp6mU_BcJFl62GG8rXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد که ساعت ۲:۵۰ بامداد جمعه، نقاطی در اطراف شهرهای اندیمشک و امیدیه هدف حمله موشکی آمریکا قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77453" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیام‌های دریافتی:
خرم‌آباد ساعت 3:19 دقیقه صدای انفجار شدید.
خرم آباد الان انفجار شدید
همین الان صدای انفجار خرم اباد ۳:۲۰
سلام خرم آباد همین الان ساعت 3:19 دو انفجار شدید
سلام خرم اباد وحشتناک پنجره لرزید
خرم آباد زدن یه حالت لرزش هم داشت
خرم اباد وحشتناک شیشه هامون لرزید
سلام همین الان از خرم اباد موشک پرتاپ شد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان گفت: یک نقطه از شهر خرم‌آباد دقایقی پیش هدف پرتابه دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77452" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWqwn2H48tFLMXi70dhwp49a6xUMqsIjNMbouQn7fUyKSUw8RvLNsKljj2yAA5_CqadPFupWk0u-uA_g5E6Psi4EiMuOcpfZw_6w5x79Z3XhwDdrhNfieSUqXRyVppgJ_4vZRvCVyZiCZeRjkfO3mxSrdkp49uf9y2uiM9XKGXvHvsznsuDrDHIv8MDditbNTgTv8I4hQJbLxuDR5PlIiIKkNhZw8gJws2hbPB14Y12e_vqLHVqXJ3ltOtomEJ6IpL95YecSh56K8Od4kSPRenehEV9MyJNGZUkB7BbVmEEVr4hxB4hlXN1wn4tdgiwgr7pTwV6XKDmV_U36sYWYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77449" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AtyYzoyNb1sYqkOlql17Twdhcu5GtgUc5JuZW3Z5DSKJcAwW51y74_dgzu-q0UTR2O7oeTANxjNjqZLtgAK_yG1VLEbe_fI0O3yntk0TTCwV8_qc0x28w61BePTVokLDpHXn4AxWwtI5CUkfspLiRBmgWmQYwlH-ySI0b6oXBMbGp-ox6tigpQwbVAsEl-oVYscIto5B7gHEO8RkR4ysvBbEy01lO6xlZEFo7rgBiRJ-F6I5ST4xe1xTOloAt00685i08jBkT3UzjuGCHud8ZYt9-9BYtRcJ-i_XbR2GQSRKLzRoSlNU90rXKzTKwZTrsVhF_sQrE6SLuGRmfq-NlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: سیزدهمین شب حمله را آغاز کردیم
ترجمه ماشین:
نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا [۲:۱۵ به وقت تهران]، دور دیگری از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
این سیزدهمین شب متوالی حملات است که با هدف پاسخگو کردن ایران و کاهش تهدیدهای سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77448" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=VLfgAQRZZsVHQilyRuaM9HHrcT2xHl5RbYjpcREwcnU7JfnDbiO5_R6oCQpAd8_eULcwxC4JbMJvIZdNsN_NG-ROaU5gDFw-hQATs8iAyreUkJVPVzmfzx2MJVfAHs9Z3a95sMTIt1pw_Wq-56g--OLWwhyF9aDR7e9ZNF_bctGxGHgn4O81-rFohJZpzYsibsD87kBlTHHqIZEn8KO6_IR8CvwbygHM9_R8o-9r2sfULXgJlUa9u-v_LcRZccwdEdW3dobFGnd_UAVt9KK9rCV3FEE0wVsgqOSYHtPFpcX-A7k5SvG2Q7rI59oXP1dxOgJHd6oucVvTKhwERh-7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=VLfgAQRZZsVHQilyRuaM9HHrcT2xHl5RbYjpcREwcnU7JfnDbiO5_R6oCQpAd8_eULcwxC4JbMJvIZdNsN_NG-ROaU5gDFw-hQATs8iAyreUkJVPVzmfzx2MJVfAHs9Z3a95sMTIt1pw_Wq-56g--OLWwhyF9aDR7e9ZNF_bctGxGHgn4O81-rFohJZpzYsibsD87kBlTHHqIZEn8KO6_IR8CvwbygHM9_R8o-9r2sfULXgJlUa9u-v_LcRZccwdEdW3dobFGnd_UAVt9KK9rCV3FEE0wVsgqOSYHtPFpcX-A7k5SvG2Q7rI59oXP1dxOgJHd6oucVvTKhwERh-7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
داداش
بندر
زد
همین الان
بندرعباس
سلام بندرعباس همین الان صدای چندتا انفجار پشت هم اومد
ساعت ۲:۴۱ دقیقه صدای انفجار بندرعباس
سلام بندرعباس انفجار های شدید پیایی غرب منطقه ۴
بندرعباس 2 انفجار
سلام وحید بندرعباسو زدن 2:41
بندرعباس ٠٢:٤١ يه صداي انفجار خيلي بلند كه مركز شهر  قشنگ حس شد
سلام بندرعباس همین الان چندتا زدن خیلی بدد برق قطع شد صدای انفجار بد بود
🔄
بندرعباس صدای انفجار بلند ۲:۴۱
2.42 چند انفجار بندرعباس پشت سر هم سنگین
3تا دیگه
٠٢:٤٢ سه تا ديگه پشت سرهم
صدا و موج زيادي داره
سلام وحید بندرعباس انفجار وحشتناک
دوباره داره میزنه خیلی بد میزنه
بندرعباس ۲:۴۲ صدای انفجار دی در پی
دوتا دیگه پشت سرهم زدن
۵ تا انفجار شدید  بندرعباس مجدد منطقه ۴ ۲:۴۳
سلام یه صداهایی میاد بندرعباس فکر کنم صدای انفجاره اما دوره
وحید بندرعباس ۲:۴۲ صدای انفجار بدجور میزنه
ساعت ۲:۴۱ در خونه دوبار لرزید
غرب جزیره قشم
بندرعباس همین الان هفت تا هشت انفجار خیلی قوی داشت
آقا وحید بندر خیلی شدید بود بیش از ۵ تا بیشتر.</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77447" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=ZPf6eGrK4VqR7LGvBVzl7X-iLMfTBgnj0STTUueyLS5cRCp1InIMWQt3yy7foR3hgVIejps8yDPv44M0u_qScQaCZE5mUP05ItBYdw2ng82Lb8k6I4-mn7eyUMPzBosQp2VN7svfpj_z5hSfDvTf5aJmVL2zLffMWYBHGlZsPmd0fnW1mGmVVEwny_Q0MNXTWTlYZQFmAm4d9GoasBb0LLQZ0l5105SqOKa97zmpux-ObHTLGtBuEIzv8ncaLiIWRIPzgvD7ZDgFfNKYBoKDvBsuf_QLj1QvgF479mjL21RZNreaju6xD6-SIS9zWSsziuntxHkfZaHVR_P035V8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=ZPf6eGrK4VqR7LGvBVzl7X-iLMfTBgnj0STTUueyLS5cRCp1InIMWQt3yy7foR3hgVIejps8yDPv44M0u_qScQaCZE5mUP05ItBYdw2ng82Lb8k6I4-mn7eyUMPzBosQp2VN7svfpj_z5hSfDvTf5aJmVL2zLffMWYBHGlZsPmd0fnW1mGmVVEwny_Q0MNXTWTlYZQFmAm4d9GoasBb0LLQZ0l5105SqOKa97zmpux-ObHTLGtBuEIzv8ncaLiIWRIPzgvD7ZDgFfNKYBoKDvBsuf_QLj1QvgF479mjL21RZNreaju6xD6-SIS9zWSsziuntxHkfZaHVR_P035V8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌‌های دریافتی:
اهوازو زدن
شدید زدن
سلام وحید صدای برخورد اهواز
اول ۳ تا خیلی دور بود
الان هم ۳ تا نزدیک بود
اقا وحید همین الان اهوازو بد زدن
اهواز انفجار ولی دور بود
اهواز ساعت ۲:۲۰ صدای انفجار اومد
اهواز صدای برخورد اومد 2:21
وحید رگباری زدن اهواز
ساعت ۲.۲۰
ساعت ۲:۲۵ یک انفجار شدید اهواز
سلام وحید ساعت ۲:۲۰ اهواز رو زدن
داداش اهواز صدا انفجار قطع نمیشه تقریبا ۲  دقیقس پشت هم داره بمبارون میکنه یجایی رو
اهواز ساعت ۲:۲۱ خیلی زدن بیشتر از ده تا
۰۲:۱۹ اهواز زدن
آقا وحید اهوازو شدید بمبارون کردن هنوزم ادامه داره
ساعت ۲:۲۵ یک انفجار شدید اهواز
انگار یه چیزی خورد زمین و ترکید
انفجارش طنین داشت
چیزی مثل رگبار
انفجار در اهواز 2:25
سلام ۲:۲۱اهوازو زدن از گلستان اهواز پیام میدم دور بود خیلی ولی کاملا صدا و لرزشش اومد
سلام وحید جان، اهواز رو زدن
خیلی شدید بود ساعت ۲:۲۲
سلام اهواز شیشه ها کامل لرزید مثل یه باد شدید بود
🔄
ساعت 02:24 مجددا شروع شد.
مجدد ۲:۲۴ انفجار شدید
یکی دیگه دوباره زد
انفجارش موج داره
ساعت ۲:۲۴ یه انفجار دیگه شدید بود
۲:۲۴ دوباره اهواز زدن
وحید دوباره صدای چندین انفجار
اهواز هنوز داره میزنه
اهواز رو پشت سرهم دارن میزنن
درود وحیدجان، ۴ ۵ تا انفجار عجیب در اهواز رخ داد، انفجارهاش با همیشه فرق دارن، با اینکه دورن و صدای کمی دارن ولی زمین و شیشه‌ها رو میلرزونن به یه صورت دلهره‌آوری
سلام اهواز ساعت ۲:۲۴ دیقه فرهنگ شهریم صداش اومد هرچند کم بود صداش ولی مشخص بود بمبه
انفجار ها توی اهواز همچنان ادامه داره
خیلی شدتش بیشتر از روزای قبله
کل خونه و پنجره ها دارن میلرزن
اهواز زاغه مهمات انفجارات پی در پی
اصلا تمومی نداره
۲:۳۲
۲:۳۳
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77446" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_idfAIgccJNY0zLD0FWnHQ5u6Yo-b2tSxDl1Sy7JipZ29RiqcZEzD-sYPMn7msXH_g9-Gu-j2gJn6qAbwNxWQi9NvcOtRYAdUnSOnsTcmCQGDyVryTZvwzI8JU0aBEgtoURTQjXDgpLD4LszbTh0JIfNPLh1hQikdJeQFO8SDAQPih8B5DhUQG9EZh7fvZQteBje4QdxlaLEHzNj-gBPGKhky1QBJz2ta8x0ZbzShGWx6wQqAl_9eWABoPx11xUgjeU6WGGABOWJ1yjh3Fz3sUamQzTUS2o3QI-ROYZ7FGht0oYLhgrpQ_nQnt59Ys2hYK1mloIc7_n7IXrV8LATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
ترجمه ماشین:
لطفاً این بیانیه را تا اطلاع ثانوی به‌منزله اعلام این موضوع تلقی کنید که
از این لحظه به بعد، هزینه هرگونه خسارت واردشده به کشتی‌ها، محموله‌ها یا هر چیز مرتبط با آنها، از محل پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
این خسارت‌ها ممکن است بسیار قابل‌توجه باشند، اما با وجود این، این کار منصفانه و عادلانه است.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77445" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EnSGheA8K5ZvVolqAdDTapC7xZpNuAsnRvNt7310lLc3nRb4Y-E86qEDXSUiSKToOtVaXpAQAP3tzDyomuya58q_SwJ_r2GyfGnGsSjX7ySJB9vScSwo0kdX8b4W3jHEqbW6aOCuks_bLX33CLjZnqpFJbc_QKCbykmM40TPcwqRGuSbmAi9-gBDvetTlRX-jmyNAyzxIffYpX0OrDLaJsMNkMEz5A64DaX7f8Z1QCeexJq2ejWHSNkr4VxJoP18uZAZAQbeLf0r08JTR88CA-Lll0uEgZPPeyQ17oLEmZqME__nG_M7BQNo7Ph_IviurofgEhQPNC85tKOSMXrapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم: اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
گزارش خبرنگار تسنیم:
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند.
من یک پیام داشتم ولی اون رو هم ساعت ۲۳:۳۳ دریافت کرده بودم:
سلام وحید جان
ساعت 23.30 صدای دو انفجار شدید  ذوالفقار قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77444" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77443" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=VyHiZMcmkZT3lGGSqV0VtsdPvYZ8KqAfQFNko65Rpz2OZPm84m18t7XW1dUeaju9Ww_-5TkQAvk2yZosxd_-hak7iPXxI5gqBqwzmmS-gB2iHlxT12pyGEBdLbezaiqUG6AH784Ptx9X12oGjBh0pqfHDJFG5d5yjLMVs84hI6Q43TH5uf3kjvJbQMm-gREUTrOTLFTccK39a82Na0LYC64XiZ_Nym32gkPlOyLQ3xmEMytDGCrVFkrLvhe3WRKqRLNZEui8BWK-5cNfnE15BBE_tvRuWhzvrOL8boZAsi4HriCbjGXYdcSJoqGwkzLsjixNRBW1Vij3VthhscWzvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=VyHiZMcmkZT3lGGSqV0VtsdPvYZ8KqAfQFNko65Rpz2OZPm84m18t7XW1dUeaju9Ww_-5TkQAvk2yZosxd_-hak7iPXxI5gqBqwzmmS-gB2iHlxT12pyGEBdLbezaiqUG6AH784Ptx9X12oGjBh0pqfHDJFG5d5yjLMVs84hI6Q43TH5uf3kjvJbQMm-gREUTrOTLFTccK39a82Na0LYC64XiZ_Nym32gkPlOyLQ3xmEMytDGCrVFkrLvhe3WRKqRLNZEui8BWK-5cNfnE15BBE_tvRuWhzvrOL8boZAsi4HriCbjGXYdcSJoqGwkzLsjixNRBW1Vij3VthhscWzvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین:
ما در برابر جمهوری اسلامی ایران بسیار خوب عمل می‌کنیم. عملکردمان فوق‌العاده خوب است. آن‌ها دوست دارند کاری بکنند، اما من می‌گویم هنوز آماده نیستند. به مقدار بیشتری از همین رفتار نیاز دارند. هنوز آماده نیستند. نیت‌های شومی دارند.
نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند. اگر همهٔ این کارهایی را که درباره‌شان صحبت می‌کنم، از جمله کارهای مربوط به مراکز دادهٔ شما، انجام دهیم، مگر این موضوع مهم نیست؟ وقتی شروع کنند جوامع را یکی پس از دیگری نابود کنند، نمی‌توانیم اجازه بدهیم حتی به داشتن سلاح هسته‌ای فکر کنند. دقیقاً همین اتفاق در حال رخ دادن است. در دوران من هرگز سلاح هسته‌ای نخواهند داشت.
ضمناً، این کار باید به‌دست دیگران انجام می‌شد. تقریباً سه سال است که می‌گویند ۴۷ سال گذشته، اما این کار باید ۵۰ سال پیش به‌دست رؤسای جمهور دیگر آمریکا یا کشورهای دیگر انجام می‌شد. لازم نبود ما این کار را انجام بدهیم، اما ظاهراً اگر ما انجامش ندهیم، هیچ‌کس دیگری هم آن را انجام نخواهد داد. من انجامش می‌دهم و هیچ‌کس دیگری توانایی انجام آن را ندارد.
ما در دورهٔ نخست ریاست‌جمهوری من بزرگ‌ترین ارتش جهان را ساختیم. کمی بیشتر از آنچه فکر می‌کردم از آن استفاده می‌کنیم، اما اشکالی ندارد.
ونزوئلا را داشتیم. کریس در آنجا کار فوق‌العاده‌ای انجام می‌دهد. هزینهٔ آن جنگ را چندین و چند بار جبران کرده‌ایم. میلیون‌ها و میلیون‌ها بشکه نفت برمی‌داریم و آن نفت به هیوستون و لوئیزیانا می‌رود. خودتان می‌دانید؛ آن کشتی‌ها را می‌بینید که صف کشیده‌اند.
باز هم می‌گویم، هزینهٔ آن را بارها و بارها جبران کرده‌ایم و رابطهٔ بسیار خوبی با ونزوئلا داریم. مردم ونزوئلا اکنون خوشحال‌اند و نمی‌توانند آنچه رخ داده را باور کنند. بزرگ‌ترین شرکت‌ها و بزرگ‌ترین شرکت‌های نفتی جهان وارد آنجا می‌شوند و به شکلی تجارت می‌کنند که هیچ‌کس تصورش را نمی‌کرد.
ما هم سهمی برمی‌داریم؛ باید هم برداریم. آن‌ها هم سهمی می‌برند. بسیار جالب است که اکنون پول بیشتری درمی‌آورند. کریس ارقامی را به من نشان می‌داد. ونزوئلا اکنون بیشتر از هر زمان دیگری پول درمی‌آورد. ما هم پول زیادی درمی‌آوریم و فکر می‌کنم حقمان است.
بنابراین واقعاً اتفاقی بود که [نامفهوم]. یک جنگ یک‌روزه بود؛ یک روز طول کشید. مردم می‌گفتند: «قرار است آنجا برای همیشه گرفتار شویم.»
اما می‌دانید، ما ۲۰ سال در ویتنام بودیم و در آن جنگ هزاران و صدها هزار نفر را از دست دادیم؛ دست‌کم هزاران و هزاران نفر. سال‌ها در افغانستان بودیم. در تمام این جنگ‌هایی که درباره‌شان شنیده‌اید، سال‌های سال حضور داشتیم. این‌ها همان جنگ‌هایی بودند که من آن‌ها را جنگ‌های بی‌پایان می‌نامیدم.
اما این بار چهار ماه است که درگیر هستیم. دیروز روز بسیار غم‌انگیزی داشتم. به دوور رفتم. چهار میهن‌پرست بزرگ آمریکایی کشته شدند. این یعنی ۱۸ کشته در دو جنگ. حتی یک نفر هم بیش از حد است، اما شمارشان ۱۸ نفر است.
در حالی که در ویتنام ۲۰۰ هزار نفر را از دست دادیم. هزاران و هزاران نفر را از دست دادیم. در افغانستان و در هر جنگی هزاران نفر را از دست دادیم. در جنگ کره نیز هزاران نفر کشته شدند. همهٔ این جنگ‌ها سال‌ها طول کشیدند.
ما می‌خواهیم این را تمام کنیم و می‌خواهیم درست انجامش بدهیم. اما باید کاری را که برایش آمده‌ایم انجام دهیم. نمی‌توانیم اجازه بدهیم این افراد بسیار خشونت‌طلب به چیزی که می‌خواهند، یعنی سلاح‌های هسته‌ای، دست پیدا کنند.
[...]
بنابراین فقط می‌خواهم در پایان بگویم که حضور در اینجا افتخار بزرگی است. اکنون می‌روم تا دربارهٔ موضوعات گوناگون صحبت کنم. یکی از آن‌ها جنگ ایران است که باز هم می‌گویم در آن بسیار خوب عمل می‌کنیم؛ بسیار بسیار خوب. می‌گویم بهتر از چیزی که هر کسی انتظار داشت قابل انجام باشد.
نیروی دریایی و نیروی هوایی‌شان را از کار انداخته‌ایم. تمام رادارهایشان و بخش عمدهٔ توانایی‌شان را در زمینهٔ تولید از بین برده‌ایم. توان پهپادی‌شان ۸۴ درصد و توان موشکی‌شان ۹۱ درصد کاهش یافته است.
بعد روزنامه‌ای نوشت: «آن‌ها اکنون در موقعیت قوی‌تری نسبت به چهار ماه پیش قرار دارند.»
نه، این حقیقت ندارد. درست نیست. باورم نمی‌شود حتی اجازه دارند چنین چیزی بگویند. نیویورک‌تایمز نوشت: «آن‌ها اکنون در موقعیت قوی‌تری قرار دارند.»
آن‌ها ارتشی ندارند. نیروی دریایی ندارند. کارشان تمام است. ۱۵۹ کشتی داشتند که همهٔ آن‌ها در کف دریا هستند. ۲۱۲ هواپیما داشتند که همه از بین رفته‌اند. رادار ندارند. پدافند هوایی ندارند. هیچ‌چیز ندارند؛ جز اینکه خشن و باهوش‌اند و هنوز مقداری توانایی دارند.
اما چهار ماه پیش، باور کنید، بسیار بسیار قوی‌تر بودند. متوجهید؟ می‌خواهم خبر واقعی را به شما بدهم.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77442" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
افراد نفوذی در دولت آمریکا سرشان را زیر برف کرده‌اند.
آن‌ها واقعیت‌های میدانی را نادیده می‌گیرند و به نظر می‌رسد فقط روی سال ۲۰۲۸ تمرکز کرده‌اند.
تجاوزگری بی‌فکرانه‌ای که از آن حمایت می‌کنند، تنها باعث خواهد شد رئیس‌جمهور آمریکا برای توافقی که در تلاش برای دستیابی به آن است، بهای سنگین‌تری بپردازد.
Compromised individuals in the U.S. administration are burying their heads in the sand.
They ignore the realities on the ground and seem focused only on 2028.
The mindless aggression they advocate will only ensure that POTUS pays heavier price for deal he's trying to achieve.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77441" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bztwXLDbaZVKAfXkDeXLpOEfb4XoDWGKTPrQ9hjc0z4Py-kKHIAHus1pLY9B9n6B-laCeh0WK5Y4eoHMFS8BGu8d78WMmlJpk8GKmHFuHOfwOLfl2rzBm5bgCjVBhal7ixtWwJHwloEazZ7AFHieTx6sfD4cy0h-moEXypH_Z45cUYZ4u3VNy3gMtfHc9DEE6j58-fOuiGM4TekqYBhaz_Imvg8pQZ7JKJ9YZxYE2zfM9OxdPCgqsho173eKLxLwV1LORVdZazvrBy-ZZu1D29CkWqBPC_9cxwjZeDcyArYGBBa1zcTFwwB6WyGZEdYUY3XoI54QxFnW8oZJaMn60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
هم‌زمان با پیام‌های دریافتی درباره پرتاب موشک از اهواز
آپدیت:
ارتش کویت پنج‌شنبه شب اعلام کرد که نیروهای نظامی ایران بار دیگر خاک این کشور در حاشیه خلیج فارس را هدف گرفته‌اند.
رسانه‌های حکومتی در ایران نوشته‌اند که هدف این حملات تازه پایگاه علی السالم کویت بوده است.
در همین زمینه ارتش کویت در شبکه‌های اجتماعی از جمله شبکه ایکس خبر داد که موشک‌ها و پهپادهای ایران توسط ضدهوایی‌های این کشور رهگیری شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77440" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=aurxOMxNCkmpbRedmBy71RrpirJrD1KkoZZkX7zJGSB1kXIDFdni324gmgCg_8CG54rioyZZ8T69r7r4Gjd7hpCXMXtDQdaxAXId0kWLi8LWCl32ZT-hi__clImaLYFgWSHN7BtoGW-GjlXB_SNrKwhp1TbZtiu6YQngPlXuHhVjKaNe3AMLU0QDjc-C33njFLAeHFGOlF7pIYhNx4TAewfLA2rhEJkciXs4ka72lmo8GV0ahCeh23UbaPxQ9NfpIy5BOnUWmm9YivNS-4HFfRX9fN2AOgVTDNc8FE_Rb-kmWunhI_L9Nj25oGWRDXUippvs-aMMyP_CjlbQBfXgnbScyyw5sTp4sWwpjQ5BAFMKk6kWgd3b5kkgvpnLvCUKULFrVfuXVnjOHu0wTAZujxlPvl66KTeqW1M6y2OWbgWeThSUlLefoQty-Ef7rC_hI4xM4DM8R_Zb63feJBigierokL9esTbcKqZaxKUV75Bt793aJejKI8CF1etRgRnC0VhTzFnmxasOKcx7mYGAEFuma0NojsbSbfOvoPNaB7qkb7edS4WvVi9luM88-ZGNzGMevCPHASUXMjyIWZthZyPohkQtKAqO-9jUkqp_ljg5dBpbAL8e8yMXXXFHFg7pWFMyGK_YS3Gd-Dib2IwkUtXwyJ0pdv0QGFf2E6-JfaM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=aurxOMxNCkmpbRedmBy71RrpirJrD1KkoZZkX7zJGSB1kXIDFdni324gmgCg_8CG54rioyZZ8T69r7r4Gjd7hpCXMXtDQdaxAXId0kWLi8LWCl32ZT-hi__clImaLYFgWSHN7BtoGW-GjlXB_SNrKwhp1TbZtiu6YQngPlXuHhVjKaNe3AMLU0QDjc-C33njFLAeHFGOlF7pIYhNx4TAewfLA2rhEJkciXs4ka72lmo8GV0ahCeh23UbaPxQ9NfpIy5BOnUWmm9YivNS-4HFfRX9fN2AOgVTDNc8FE_Rb-kmWunhI_L9Nj25oGWRDXUippvs-aMMyP_CjlbQBfXgnbScyyw5sTp4sWwpjQ5BAFMKk6kWgd3b5kkgvpnLvCUKULFrVfuXVnjOHu0wTAZujxlPvl66KTeqW1M6y2OWbgWeThSUlLefoQty-Ef7rC_hI4xM4DM8R_Zb63feJBigierokL9esTbcKqZaxKUV75Bt793aJejKI8CF1etRgRnC0VhTzFnmxasOKcx7mYGAEFuma0NojsbSbfOvoPNaB7qkb7edS4WvVi9luM88-ZGNzGMevCPHASUXMjyIWZthZyPohkQtKAqO-9jUkqp_ljg5dBpbAL8e8yMXXXFHFg7pWFMyGK_YS3Gd-Dib2IwkUtXwyJ0pdv0QGFf2E6-JfaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان فاکس‌نیوز، متن زیرنویس، ترجمه ماشین:
مجری:
بیایید نگاهی بیندازیم به نیروگاه‌ها و مکان‌هایی که ممکن است بتوانیم هدف قرار بدهیم. لوکاس، وقتی به این‌ها به‌عنوان اهداف احتمالی نگاه می‌کنی، فکر می‌کنی اول از همه کجا را ممکن است بزنیم؟
لوکاس:
خب، نمی‌دانم نخستین هدف باشد یا نه، اما نیروگاه دماوند ۴۰ درصد برق تهران را تأمین می‌کند. نیروگاه هسته‌ای بوشهر هم احتمالاً هدف قرار نخواهد گرفت. روس‌ها آن را ساخته‌اند و هنوز هم اورانیوم با غنای پایین در اختیار ایران می‌گذارند.
مجری:
چون، لوکاس، باید بگوییم که منفجر کردن یک نیروگاه هسته‌ای خطرهایی دارد.
لوکاس:
بدون تردید. میدان گازی پارس جنوبی هم روی بزرگ‌ترین میدان گاز طبیعی جهان قرار دارد. نیروهای اسرائیلی در ۱۸ مارس، در آغاز جنگ، آن را هدف قرار دادند و ایران هم با حمله به بخش قطری همین میدان گاز طبیعی پاسخ داد.
مجری:
اگر بخواهیم در همان تنگه‌ای که آن‌ها در آن به کشتی‌ها حمله می‌کنند پیام بفرستیم، آیا آنجا جایی نیست که باید سراغش برویم؟
لوکاس:
چرا؛ فقط سؤال این است که پاسخ ایران چه خواهد بود. دیده‌ایم که ایران تلافی می‌کند. تأسیسات گاز طبیعی قطر و میدان‌های نفتی امارات، نگرانی اصلی همین است.
مجری:
یعنی اگر ما یک نیروگاه را بزنیم، آن‌ها هم پاسخی مشابه خواهند داد؟
لوکاس:
بی‌تردید. تمام این مدت ماجرا همین مقابله‌به‌مثل بوده است. نکته قابل توجه درباره اسرائیلی‌ها این است که آن‌ها پاسخ‌هایی نامتناسب می‌دهند. احتمالاً یکی از دلایلی که اسرائیل دوباره وارد جنگ نشده همین است. ایران از اوایل ژوئن به اسرائیل حمله نکرده است.
مجری:
ارزیابی تو از شیوه‌ای که اکنون عمل می‌کنیم چیست؟ فکر می‌کنی پاسخ ما نامتناسب است یا می‌توانست نامتناسب‌تر باشد؟
لوکاس:
پاسخ ما نامتناسب نیست. نکته قابل توجه این است که نیروهای آمریکا، پس از آنکه یک پایگاه آمریکایی در اردن هدف قرار گرفت، به پادگان‌های ایران حمله کردند؛ همان حمله‌ای که سه سرباز ارتش آمریکا را کشت.
مجری:
پس این همان نیروگاهی است که ممکن است هدف قرار بدهیم. این مهم‌ترین مورد است. برویم آن طرف نقشه؛ اینجا «کوه کلنگ» یا Pickaxe Mountain است.
لوکاس:
ارزیابی اطلاعاتی آمریکا این است که ایران احتمالاً چند روز پیش از عملیات «چکش نیمه‌شب» در یک سال قبل، بخشی از اورانیوم غنی‌شده خود را از فردو به کوه کلنگ منتقل کرده است.
این محل بسیار عمیق‌تر از دیگر تأسیسات هسته‌ای است. همچنین اینجا کوه‌های زاگرس است و با سنگ دولومیت بسیار سخت روبه‌رو هستیم؛ بنابراین حمله هوایی به آن بسیار دشوار خواهد بود. این یکی از دلایلی است که شاید از نیروی زمینی استفاده شود.
در واقع، چنین مأموریتی برای نیروهای مأموریت ویژه ارتش آمریکا است؛ نیروهایی مانند دلتا، تیم ششم سیل و اسکادران ۲۴ تاکتیک‌های ویژه نیروی هوایی.
ریسک ماجرا این است که هیچ‌کس دقیقاً نمی‌داند داخل آنجا چه وضعی دارد. هیچ نقشه فنی‌ای از داخل کوه کلنگ وجود ندارد.
مجری:
درست است. همین را می‌گوییم.
لوکاس:
آژانس بین‌المللی انرژی اتمی هرگز به این محل دسترسی نداشته است. بنابراین با اطمینان نمی‌دانیم آیا سانتریفیوژها و اورانیوم با غنای بالا به کوه کلنگ منتقل شده‌اند یا نه؛ اما این محل زیر نظر است.
شنیدیم که رئیس‌جمهوری ترامپ گفت به‌زودی کوه کلنگ را هدف قرار خواهد داد. بمب‌افکن‌های B-1 را دیده‌ایم که از بریتانیا پرواز کرده‌اند و البته بمب‌افکن‌های B-2 از پایگاه هوایی وایتمن در میسوری برای همان پرواز دور دنیا که در عملیات «چکش نیمه‌شب» دیدیم، برخاستند.
مجری:
و نطنز هم هدف قرار گرفته، درست است؟
لوکاس:
نطنز هدف قرار گرفته است. فردو و اصفهان هم هدف قرار گرفتند. این‌ها سه محلی بودند که در عملیات «چکش نیمه‌شب» در یک سال قبل هدف قرار گرفتند. با این حال، کوه کلنگ تا این لحظه دست‌نخورده مانده است.
[جملاتی که در ویدیو هست ولی برای جا شدن متن در پست، اینجا نقل نکردم.]
مجری:
و حالا تا جایی که می‌دانم، این نیروگاه برق [دماوند] دو میلیون نفر را تأمین می‌کند.
لوکاس:
بله.
مجری:
و خارج از تهران قرار دارد.
لوکاس:
اگر رئیس‌جمهوری بخواهد پاسخی بدهد که تا حدی نامتناسب تلقی شود، نیروگاه دماوند را هدف قرار می‌دهد. باز هم می‌گویم، این نیروگاه ۴۰ درصد برق تهران، یعنی برق پایتخت، را تأمین می‌کند.
تنها سؤال این است که آیا می‌خواهید برق میلیون‌ها ایرانی را قطع کنید که با آرمان آمریکا همدلی دارند؟
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77439" target="_blank">📅 21:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHFFakLFWvkq2t32yspX7gqHCXa1XCN0jXMvDoOcoFptlp2lqqVRvgOh7py4MX7K3jrEUjdXmPTx0lLVo1G620lw0LGKKeHeqzci5brN9F3o9RvV7K2OHtBOAd8YO8vx8Xv-myK5bey64G26rtmJPyigDlwoutx9ckn0F7oa0dMt3XU15YS82lPFOAacLfCGvjzvRBA61Gg58zxkddJzM6Gcl5XeRzfiOUuNdX7uphqGrRBHFyfkevOFPhlHKblaP3iuMCczdD3FB8wCaN_aEmJl7kySWi1S7a0FemYSVYBm8XjZi88FQI7sTgUb17j4ERxePlYbJMQ85y58IUlxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش کویت عصر پنج‌شنبه اول مرداد اعلام کرد که یکی از گذرگاه‌های مرزی این کشور با عراق برای دومین بار در یک روز، هدف حمله پهپادی قرار گرفته است.
ستاد کل ارتش کویت با انتشار بیانیه‌ای در شبکه اجتماعی ایکس (توییتر) اعلام کرد: «گذرگاه مرزی العبدلی عصر امروز بار دیگر هدف حملات پهپادی دشمن قرار گرفت که خسارات مادی بر جای گذاشت، اما هیچ تلفات جانی نداشت.»
ساعاتی قبل کویت اعلام کرده بود که آتش‌سوزی ناشی از حمله صبح پنجشنبه، مهار شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77438" target="_blank">📅 21:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i02duRF6SephCb4o3ntUj5BQsKjw0bswOqJGKOaO-hpwA-Z4uJXxVry4_LaSllGq0QBTqNk3DHOD6kYf7OcJ4MGx7zm1w-zgkAUOKE7Q2urCpWAI8hpZcujmxR9RWrHwI6FSQzUZ6aCSx3_QwfRU056dnUroIDiVgIsXqKLEPxgbUDGGljspp4oRTuOhgxKxq5DHobkRB7lGFE-7HKm0iUZIjC0Xj5b_GhsP5mrBYlcMeLEbHuQr44eGMNFo_Vt6nkkcJKK8KS-Z1fz0PV1OroduPYyATUWslE_hQ37JS6q4hbV26_3rN3WadSOCDiXiFnmSz5N2YopUYlEDNgArqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره
این پیام‌های دریافتی
:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد ساعت ۱۸:۵۰ عصر پنجشنبه در پی حمله ارتش آمریکا، یک فروند موشک به نقطه‌ای در ساحل شهر سوزا در جزیره قشم اصابت کرد.
تسنیم نوشت که بررسی ابعاد حادثه و میزان خسارات احتمالی از سوی دستگاه‌های مسئول در حال انجام است.
خبرگزاری صداوسیما نیز از شنیده شدن صدای انفجار در قشم خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77437" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXT2oXPTc9oYgCDOIta5aBjL2AoNT-EmHj02GNK1fnGJmpmtRiFEg8jQlQ45R5FSylXP9d2qrnvbdk8pQNgDEyvzizZDe6vkMMseKvR53K9RUjo8G6609TeZOPFYjL1Ie0RofDAiY7rnycvPjrIOXBgB7LQ_YYvZUk2z6ITIlnUjt4mvzhEnmaTBQzCtS6Hmv09G__25r_XQxQhGgWfidirzVCTrOLhFaxOisgpiJ_QiwKiJfAuYNGGO2UFQKze95inD4_6mIWaD34JT2KHZO_yW3NaGd6hmuF2UdzJ9SX2bDlyyJ4gPDiF28TbjwYodadwjja6ili3f1dtdTSmr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز پنج‌شنبه ادعا کرد که پایگاهی را در خاک بریتانیا که بمب‌افکن‌های ب ۱ آمریکا از آن بلند می‌شوند برای حمله «هدف مشروع» می‌داند.
وب‌سایت اکسیوس پیشتر به‌ نقل از مقام‌های دولت آمریکا نوشته بود که ارتش این کشور در دور جدید حملات به ایران، روز سه‌شنبه برای نخستین بار از یک بمب‌افکن دوربرد «ب ۱» برای حمله به اهداف متعلق به سپاه پاسداران انقلاب اسلامی استفاده کرده است.
اکسیوس نوشته بود که بمب‌افکن به‌کارگرفته‌شده در این حمله از یک پایگاه هوایی در بریتانیا به پرواز درآمده بود. اشاره این سایت خبری به پایگاه فِرفورد در جنوب غربی انگلیس است که در حال حاضر ۱۸ فروند از بمب‌افکن‌های ب ۱ آمریکا در آن نگهداری می‌شود.
حال سپاه پاسداران در پیامی این طور نوشته است:‌ «هر پایگاهی که برای حمله به خاک ایران از آن استفاده شود برای ما هدف مشروع است.»
سپاه در پیام خود ادعا کرده است که در پی ازسرگیری حملات، آمریکا ابتدا با موشک‌های کروز از روی ناوهای خود در اقیانوس هند به ایران حمله می‌کرده، اما در پی خالی شدن انبار موشک این ناوها، به استفاده از بمب‌افکن‌های خود در بریتانیا روی آورده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77436" target="_blank">📅 19:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cCpnvza6jj38U0T6FUxN6gXZPkKTyONitOnrOtbvVjqWOB1EfbMbJQneQ5IHkKecIGlpFd528a-oemj3IFIszNDqPwN6mqX7VzsLju_7moEg07erbYdCMu6svxpbNLNA7WN_zoi9e55smV58PYhgJtVRj7fcZ8qaLKBPp3qo-MAP8iYQBiFa6bseddCWyCaXsaDNhP2CycKhnGHdalPnpOZx6X9FilsohLfU-ngTpJBfH-LvaRpcDNKZ4TQFiNF_Wo5QxhLtbkg4qQBTcKLV4aZg_ovJ9GagTzQpnPsK4atPSucCIhyH9bY4j0PVmixfd6QhRpO56klsLmt6NHnkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ می‌گوید به تصمیم‌گیری درباره «حمله‌ای عظیم» علیه ایران «نزدیک» شده است
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنجشنبه به آکسیوس گفت که به‌طور جدی در حال بررسی ازسرگیری عملیات رزمی گسترده در ایران است؛ از جمله حملاتی که از عملیات «خشم حماسی» بزرگ‌تر خواهد بود.
چرا مهم است: ترامپ در مصاحبه‌ای کوتاه اذعان کرد که چنین تصمیمی پیامدهایی خواهد داشت و تأکید کرد که هنوز تصمیم نهایی را نگرفته است.
ترامپ برای تصمیم‌گیری خود مهلتی تعیین نکرد. دو مقام دیگر آمریکایی نیز تأیید کردند که هنوز هیچ تصمیمی گرفته نشده و هیچ دستور تازه‌ای به ارتش داده نشده است.
تشدید تنش‌های کنونی تاکنون باعث شده قیمت نفت از بشکه‌ای ۱۰۰ دلار فراتر برود. بازگشت به جنگی تمام‌عیار در آمریکا به‌شدت نامحبوب است.
آنچه او می‌گوید: رئیس‌جمهوری آمریکا گفت: «من در حال بررسی یک حمله عظیم هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام شده است. به تصمیم‌گیری نزدیک شده‌ام. ما کاملاً برای آن آماده‌ایم.»
ترامپ گفت اسرائیل «اگر از آن‌ها بخواهم، ظرف دو دقیقه وارد عمل می‌شود»، اما افزود که برای آغاز عملیات تازه علیه ایران «به هیچ‌کس نیاز نداریم».
او همچنین گفت پیوستن اسرائیل به این حملات «پیامدهایی» خواهد داشت و تلویحاً به احتمال تلافی ایران علیه اسرائیل اشاره کرد.
تصویر کلی: ترامپ گفت ایرانی‌ها «می‌خواهند مذاکره کنند»، اما در حال حاضر آماده توافق نیستند.
او گفت: «هنوز به اندازه کافی درد نکشیده‌اند.»
دو منبع منطقه‌ای مطلع از تلاش‌های میانجی‌گرانه گفتند رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده را نپذیرفته است.
یکی از آن‌ها گفت: «داریم تلاش می‌کنیم، اما ایرانی‌ها همکاری نمی‌کنند.»
محور خبر: آمریکا طی ۱۲ روز گذشته حملات خود را تشدید کرده است تا حملات ایران به کشتی‌های تجاری در تنگه هرمز را متوقف کند.
ایران تاکنون هیچ نشانه‌ای از تمایل به تغییر مسیر نشان نداده و خود نیز حملاتش در منطقه را تشدید کرده است.
شورشیان حوثی مورد حمایت ایران در یمن حمله به کشتی‌های سعودی در دریای سرخ را آغاز کرده‌اند؛ اقدامی که تنش‌ها را در یکی دیگر از مسیرهای حیاتی انتقال نفت تشدید کرده و بازار جهانی انرژی را بیش از پیش بی‌ثبات کرده است.
ترامپ در حساب خود در تروث سوشال نوشت که اگر حوثی‌ها بار دیگر به کشتی‌ها در دریای سرخ شلیک کنند، «ایالات متحده ایران را مسئول خواهد دانست».
او گفت حوثی‌ها نیروی نیابتی ایران هستند و بنابراین «مجازات نظامی سنگینی علیه ایران و البته خود حوثی‌ها اعمال خواهد شد».
آنچه باید زیر نظر داشت: ترامپ جداگانه گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قصد دارد هفته آینده در مراسم وداع با سناتور فقید لیندزی گراهام در واشینگتن شرکت کند.
ترامپ گفت: «روابط با بی‌بی بسیار خوب است. اگر او اینجا باشد، با او دیدار می‌کنم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77435" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید قشم صدای انفجار
الان دریابانی سوزا رو زد وحشتناک
جزیره قشم ۱۸:۴۰
ساعت 18:40 دقیقه قشم صدای انفجار شنیدیم
وحید جان قشم صدای دو انفجار از راه دور اومد ..
🔄
صدا و سیما:
شنیده شدن صدای انفجار در سوزای قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77434" target="_blank">📅 18:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxULMFPuie8Yr2r9OrHsUs4xVJw13hrHbPmqRGpl2MEM_rhz0m5nQeUlCujTy0dZkJks7QGmVtTGgVwQdBhBZQ9xcCtWAi5GJP0nxGXoVQ90GmkseBsBbO5wq53gGRc8KIsJ1YVUqRCKKmhxggC96efWObV72wxMr_cfK3r1kqg0B-d4c-DtBaF-9uOhIA_EgFpJdX4K145VppZOZYy6ZQ5rfCMUMd2w_4iLmbUaHShazi2it3i7xRqSQrxsiyJUllOe411q0oQcLLDG-CA1q-EKlfDPe7dtUn8bp9NCvBfK6RSzpm0lL_VUdHbADpHXSjuhRdnKPQSwLWZ1pOYzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
می‌خواستند ایران را تنبیه کنند.
در عوض، خودشان را با قیمت سه‌رقمی نفت تنبیه کردند.
استراتژی ۱۰ از ۱۰
👏
👏
👏
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77433" target="_blank">📅 18:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDF4l0Mzd4CtN5GZsSTqXx8B4XuJktfmPJuJPcDQQt-TJ3vbkua0BOkqEDlj1NOaVbQybUdCrocArkryMeKpH_kT9zNe4sPHRaCOmItQtQCmr8wV2anKT1v5nJGGvLIoDlbvJwaVGW_U4L7nVw4bH11HgVfDD9kIze5HDSCk-n5xKCfqRqPxe7MmlsycDCd3TY98eJ8IBW2_RSXQ99uMs5xT1jZBg2uxgLuImOXEidTmGMDQBHxDMsT-SHuyTn9bJeDfgaRYCPE-gC4E1IK0q4xNx_7Xgl9erp7N6uVDKUNm-c36V3CCGPfY_61iYzmim-DYglraeauOLhqklyUA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ روز پنجشنبه اول مرداد، در پیامی در شبکه اجتماعی تروث سوشال با یادآوری حملات نظامی ایالات متحده علیه حوثی‌ها که سال گذشته انجام شد، نوشت: «حوثی‌ها از آن زمان و در جریان درگیری با ایران، رفتار مسئولانه‌ای داشتند، اما متاسفانه با تیراندازی شب گذشته به دو کشتی عربستان سعودی، بار دیگر دست به حملات زده‌اند.»
ترامپ هشدار داد که اگر این اقدامات تکرار شود، آمریکا جمهوری اسلامی ایران را به عنوان حامی حوثی‌ها مسئول خواهد دانست. او تاکید کرد که در این صورت، مجازات نظامی بزرگی بر ایران و همچنین خودِ حوثی‌ها تحمیل خواهد شد؛ گروهی که به گفته او، تا پیش از این حرفه‌ای و هوشمندانه عمل کرده بودند اما اقدام اخیرشان مایه «تاسف» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77432" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQCJb1cReKTupGryLtyBkTB4ukZQb9gdCywpNDGnfKezVKX_BI312_FjQFuqGt7tN1Ib6ei8UyhsiEtSz3SC_y8kwndXJfe0aQQriN_Yw9j6JJ9kXhSG-QAS8Ml9Mjf5tqbhXLvIWMAxeZb-k6UddDBHkKDicM8qhEbo1qQy8xLM3uMuayQryOmgDadRl03leAtQ8RoClXHYg5NPsfSGuBy-GPqrfY8sRuIliWEfWSHfSHiJ8MjeSkPHez1k9CDQP9zQko_8fK1y8451Bovy0Il5UbOGn1JiOvRpo0PTKvPqpePpP9_tpLMCkD0nfIFR_hDs3lYdz5RlBbDn0ShxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد امیرحسن اکبری‌منفرد، زندانی سیاسی ۲۷ ساله محبوس در زندان اوین، با حکم شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، از بابت اتهام «بغی» از طریق عضویت در سازمان مجاهدین خلق ایران به اعدام محکوم شده است. بر اساس این گزارش، حکم دو روز پیش به او ابلاغ شده است.
هرانا همچنین گزارش داد امیرحسن اکبری‌منفرد زمستان ۱۴۰۳ همراه با پدر، برادر و خواهرش در کرج بازداشت شده بود و سه عضو دیگر خانواده بعدا با تودیع وثیقه آزاد شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77431" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lCXCuLbla8OFfwzsUfexH-IOHDFGudnxjRu7peh-EKPv07TDinf_r04eBIQI4hP_QD9zQ__6ZKi3WMuWAt2mNe9swASNnVTRTWnwsd1B0i98YCL3YpYaXVsTp50OiBFKzz_GPGT19ztgm22jSijuuKp8qPwZxWqxehPv9w3WN4UZ_D_J5b_fjffCCc6bM1ZLCsleUCZ2fwMIA7xxCsD7xvHHrVqi9hD5eMH8cb8oohH1p1CyOhkSDv5bNtyGCTmfV3FhvaRgip9GJ_yhqV95p3Jl7XjX1u_GwPbr1fF-MkXlNKhd2opksHUypirR7vGF_jNjskQMmlnhriYlWJn44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CFUyz7w7O9IjFKPJRccZKaO9zHnU9yfR3FBGv4d88rezggsP-OMJrwa2iNGN8A_AQiT_zQifxHqxfb0CdI5jos7BCv69n7dKPcGVewgxdACo2fd_HQATRdX6YYbW-idx71WnBfmja6HTcRF7rQT6QMzfSGo5JgQQ_BKQZPvUbnVYBmAHtgPU1sM5nCmo4-A4UXkIGhY40eKAbdQq3d1l_k845Xru_mliMoZvyTSGiU45woobQM9e1SZTaF9VzqbyeRTYMLO-ML7Du6bZ8TXM92csU-C-zYl8lk5aOh6jVNMmRjeOyzKJaLIOLW620zDKsPmboBXCz1jkCpR7T3d_jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اول مرداد ماه، در پیامی در شبکه اجتماعی ایکس اعلام کرد توافق هسته‌ای غیرنظامی میان وزارت انرژی آمریکا و عربستان سعودی تصویب خواهد شد، اما این توافق مشروط به پیوستن ریاض به توافق‌های ابراهیم است.
ترامپ در این پیام با اشاره ناگهانی به «غیرنظامی» بودن برنامه هسته‌ای ایران نوشت: «توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال انجام است، تنها به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی و دیگر کشورها دارند، مربوط می‌شود. اما این توافق کاملا مشروط به پیوستن عربستان سعودی به توافق‌های ابراهیم است.»
رئیس جمهوری آمریکا کرد در این توافق «هیچ غنی‌سازی مواد [هسته‌ای] وجود نخواهد داشت» و آمریکا با تاسیسات هسته‌ای غیرنظامی و بدون غنی‌سازی مخالف نیست
@
VahidOOnLine
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل پنج‌شنبه اعلام کرد پیوستن عربستان سعودی به توافق‌های ابراهیم، تحولی تاریخی در مسیر صلح در خاورمیانه خواهد بود.
دفتر نخست‌وزیر اسرائیل افزود اقدام نظامی مشترک آمریکا و اسرائیل علیه جمهوری اسلامی و تضعیف محور «تروریستی» تهران، زمینه را برای گسترش دایره صلح فراهم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77429" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVC3Y5CSFiUsbLGCsHP0OfC4sngWzW3yDiEe5PxHiMWG1cXmjaX-B60AYkgnwHJMnHvkGOWq_VRf_vXYfwzhd7PBg0Fs2RB6lh259Yjiq9WMn0po3F606QLXWbTncDmjL9ZPZFd2Kh3lwXf3koByknrJR3YNWdFgXYGky3ugudfFIDmyPlGCKbKMsJgnk8_gse3JjnCNmbO6T3DQvA4rXgqEz643DQISbALrhW7g_asmN39VykO89X7FNcGRuLOQ8XV3coBLRakJm6c7VoBfSfMhFqc1WHPlKBlZ2qEuF1Q8A8ZsyuYi0dY7WprMZWKGfa1pcr9J8xZi1dThy93hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایلنا در گزارشی از ادامهٔ بحران کم‌آبی در زاهدان و برخی مناطق استان سیستان و بلوچستان خبر داده و نوشته است که شماری از شهروندان در برخی محله‌های این شهر با قطع آب تا سه یا چهار روز متوالی روبه‌رو هستند.
بر اساس این گزارش که روز پنج‌شنبه یکم مرداد منتشر شد، بسیاری از خانواده‌ها برای تأمین آب ناچار به خرید آب از تانکرهای خصوصی هستند و برای هر بار پر کردن مخزن خانه بین یک تا یک‌ونیم میلیون تومان پرداخت می‌کنند.
ایلنا همچنین به نقل از شهروندان گزارش داده است که برخی خانواده‌ها به دلیل ناتوانی در پرداخت هزینهٔ خرید آب از تانکرهای خصوصی، ناچارند چند روز را تنها با چند دبه آب سپری کنند.
محمدرضا کوچک‌زایی، عضو شورای اسلامی شهر زاهدان، نیز در گفت‌وگو با ایلنا با تأیید بحران کم‌آبی گفته است این شهر با کمبود حدود هزار لیتر آب در ثانیه، معادل نزدیک به یک‌سوم نیاز آبی خود، روبه‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77428" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
