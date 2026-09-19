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
<img src="https://cdn1.telesco.pe/file/ezWKuvR8l2H8Irog3eiQ8AT0NPvA5nfPXeqKEIZ5LQ1uaKIRL62NGceBBZ24KZ9kCDbCPncvlQ_CepwN8x4iUXll3Q-FA86pXPJaklORvfCmBi75tA9tnv1inFogg8w1-usmI7a5kRaLPZfabLah7M1-KQ0-EXqBfPX_0X2Ds9TOYLuAif-ziO21thZS6xy5uzcRsfF6Stm7THes1-dolkZs-olPFpDD-CROaV557_gSi6EIxLc6AXau3Cnv6hWEgEVL1PKSnYRVXT1s_hvGzHqkhluZT6nCv4OHEsqMgY4bL59UJSZZ9kUplXUUBgChDznjb4Xn7S0fgwbyKftTQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cajxZws99EpjuNCE7ApPnvJTY_zm2QtOQVoDOa_M4nr_sYlm4_R3yfF_V0kGznxi1_pSgOn2kc_XfI8Bwyvezb7CfiOQGFn-uOolCbbY9mkX4cHVt6IRtudbA8nGj4U-ZrGrtwTUaVbRqvl0zryZFiYuH_nh1azuJS2SnHKRnqC8IIlsWU70_mDDWpm5g0rEAVbhMx-7RDjaR-jMQY9fjqUHV7aKd_7kj95y_Q6oZA0Cvu0yxZ2JI6MaNzTtTREvMtEp_ieBOcedLn9Ma16_tHyKDVwJrpnkFHacSmH_9QiO2vsuib2vMVklbOc_xgLCK3pWuw1OCT9Yrka_c6_TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=Wm40UQKFLK6v5i7h1Ga9DibQqbiV0i7ayQTv5uw4WI7EuHikOga-TM_QXYB8OB3SN_x4tFrIwOV2StPlU0tZNDQtAONPL8vRUAccffERXdTtJIDgxbXkyazzgDDq2Tc4ii6mPyep0gI2_5D2yRoKDpJRpNGrUPvNW_UkxofEpMXpq7N44oV6xpZtaMjBrVkhppJr6ZDXQ2Vd185mT8XhZTaQlJqUDlw4uXMrhhf0KKi9l82CN4SLG2fYmsymto0pwcwR_SFLxgdZxI3IW1QGDSVmqnWjmq4fE05oNSwqpr3r3s5TixLJLPoq9WRCATEqI3Ymd7kxAWFJ_lH3N2-gUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=Wm40UQKFLK6v5i7h1Ga9DibQqbiV0i7ayQTv5uw4WI7EuHikOga-TM_QXYB8OB3SN_x4tFrIwOV2StPlU0tZNDQtAONPL8vRUAccffERXdTtJIDgxbXkyazzgDDq2Tc4ii6mPyep0gI2_5D2yRoKDpJRpNGrUPvNW_UkxofEpMXpq7N44oV6xpZtaMjBrVkhppJr6ZDXQ2Vd185mT8XhZTaQlJqUDlw4uXMrhhf0KKi9l82CN4SLG2fYmsymto0pwcwR_SFLxgdZxI3IW1QGDSVmqnWjmq4fE05oNSwqpr3r3s5TixLJLPoq9WRCATEqI3Ymd7kxAWFJ_lH3N2-gUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=TPrzoF0Qzg8VNxkVfB_rmGcpQulVD5lrFe1HgjGdGJH9J3puboQ_wDyQ39vLgRrW3LZQNckLBybUgiPD7XarYLhU3vYkVcxYwBGleH8OofQXuTdIkoSvHb7NchQnHsIyykG_yv-Vi-HfT31KBofXtd5VY7LMxb3SUZ9z6Tu5iQTxl2FgNbXES6DcFQ1qb1gRROfef8ltcwYAexFQJ6Gt2EPozntK3Suhqtublks90X2bJaKVDEj5QnAYFwzOY_FypMmF0pm09Rt5zjzORdsS0szI6ArucYafMOHmIYYbNXQVHupPMkHOMOtvaL__PcIzvcZmqVVVqm1INDTwUE-ieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=TPrzoF0Qzg8VNxkVfB_rmGcpQulVD5lrFe1HgjGdGJH9J3puboQ_wDyQ39vLgRrW3LZQNckLBybUgiPD7XarYLhU3vYkVcxYwBGleH8OofQXuTdIkoSvHb7NchQnHsIyykG_yv-Vi-HfT31KBofXtd5VY7LMxb3SUZ9z6Tu5iQTxl2FgNbXES6DcFQ1qb1gRROfef8ltcwYAexFQJ6Gt2EPozntK3Suhqtublks90X2bJaKVDEj5QnAYFwzOY_FypMmF0pm09Rt5zjzORdsS0szI6ArucYafMOHmIYYbNXQVHupPMkHOMOtvaL__PcIzvcZmqVVVqm1INDTwUE-ieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yu6qga-vJG5_OR_2uejnUEo0jGKC9JMzgBPwS6oRzQae0HBs64UBV5MpI-HBam4HM6vuK-sGYNzPQew6MLun42pA9-0mlSgsQ2m8WdjuQ7kmru0NY9uAym1JtA-mUBNSpoPUj25hbqIxJff56_eOJCAU26wrUUrvW1TGyj60RVcm4hodZTQrfj_Y5xscPnUMhMQiJ2J7Ztgv8pYLqOJDAxbDqqNV2AHZfztOojyvKcrjjele76WDr1CO1DDeO5JXqe3_kTCPNFSRMmge_4pTogQfrq8THFEfvY4yKFKKLIsJdiYhX80fxPFrq2LRTUwVqxpvkQ3YvEwA8e3O85_tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bMUv5y3F0hD4p71GHld9JmIPmsR2z-yPZcVrHb_zh_vBNPM4woNM0Cj0snEhQSShgFkl-NSthd3vTZtzj-ZqGCaXLyNus4dIN0dfq793FBE5v49U1lHPB3WyLU4-QmRm9NjDxhglVbraVjRk_L67-onYhCsB--lkwRAvmXwtoje_nOmYc89sfF1gCPZW_5RtK1kB3fW12NNRyHiFdRft2dlSPy98nu3gSbeAicHzVUZJHkqXip6fub0ZKFQP7Ou4K_W6vo3didnzCiZ9oYeaEMJEeJ_ieyB2i2Ck0wB74TWkD7f-ZdFqns_oBzwjMrEtmX6o4ol_c__VUq4AcZD-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oFB2VZYIOwk0FBkoUYXkTsqmuU6E443TUuvm-a_cN6wrAQsuepOoG9EJKs-9ezYgDo8y_PZzM-SDNNjbuNJyYzIOSpcj5KHVfVv8jHm3g6JqKl1a4-ThiGvIsc6ZK0EMrFThxF4T6tcE2LsWEFZHF4umVcArkNf7rc8NfmTc2w9FCN7_hXqYxCEScbk2yKdjDq0laNBAVoOh0OQNj9tOVVdAkK1T4TyYmtjSqNWvXcoQQvdr7_3kzfv5D4fZ6yxzr9UXVKiN5CPWYPTxLxIew0qdRiiz_0t9qyTQhiiLCnHBi6Rr749dsfDCbMH_HTwto1EpmpBJo-ZfrLGw6ujt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sqyrnxxdHK3HziiqJxYo2CxNNNsK8RCXcck89B_q2VZksbZC2uMNwmJ5QZ89xkoFQkgLJZSEvgWMjd2jUJM6aVxb0v7GFFkvNadhSWd9mGeeKaz6TsgLKrB6wj7JEgCvVRGWWJzJBObWpSRHkRQsnFJmxZiCyvgfN8Ht3BQBlgI_3IPFPv4uf_Iao4KGq62HRRPQHUEzJ-joq-GaFUupvvNNQzrUYWv836gX1PZaJ8sAFsmwHjiZbrr-6YUeuNzuJ2l5t5_lhPqkQp6rim53XxLkJYPt_a2LYTfnMa0hmenWP-0zt04dZga0moxgowAX7vgYxJdw3KHuTQb6DJUM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/epcJH3WWOv7o22ykXgyJDjSMEt8ypQDOMROsQqiQaCBpiUp3MiuhOvX9Va4fxUTZnRswhQ6RTaaEbpeMAqeMb4F7WjjZQcbmfQpc-iYBqqTdnZkIJTseg-N-WPfStBejRcQ5YG2Dj0dhSIwI-hMuua48iK2k_hSjveKm8wdD9ns8AfwsvbpFkT3_pLHZQmpLmv6RcKBPuNSslx5DjXV5VR1FkXkskm1rz4gPOSYWSbmEGDbG6jQW_P7rPws3V9NXBPrgWXmaM3hwAFB7pV1i30MEMI3z2XFnmCGxEykas4INhcTSQ79dwsrV1XMnTX5ngKI_nwoIRI-QJpr0Wa9lvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=pz5Culr2m5h_2L1wRDN51vgJvnrEBZNZbnLuw2EKVnDr0BDRwwgNGU40oAdMjm2BeDP_8-h_LYsQ6hV9wUgjlMcHJ3_Olv9NT6gouWCyhkaYnGekGnFuaXVA4ANOYPV6cxLivScVE0uXQGcg_nGDIR7ngkmimHrzD4Mv_dsfAqoiBUWjytVJ47TPTNYI9IKZ4umzqZOTjFmAJuiLG7KHJ5TPLfK-pEP0eKJUh9fj5DJAEvE4Ddi4gh_Tg7v2ayAGRWOtRnHNdfokaFU0Gq7x0rHELpqsv3X6xIJGgeg0bXcKE4_LB0ZlHkgtrJfwJ2rRchWhleBZD1yO9O1iF-0UXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=pz5Culr2m5h_2L1wRDN51vgJvnrEBZNZbnLuw2EKVnDr0BDRwwgNGU40oAdMjm2BeDP_8-h_LYsQ6hV9wUgjlMcHJ3_Olv9NT6gouWCyhkaYnGekGnFuaXVA4ANOYPV6cxLivScVE0uXQGcg_nGDIR7ngkmimHrzD4Mv_dsfAqoiBUWjytVJ47TPTNYI9IKZ4umzqZOTjFmAJuiLG7KHJ5TPLfK-pEP0eKJUh9fj5DJAEvE4Ddi4gh_Tg7v2ayAGRWOtRnHNdfokaFU0Gq7x0rHELpqsv3X6xIJGgeg0bXcKE4_LB0ZlHkgtrJfwJ2rRchWhleBZD1yO9O1iF-0UXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZizVrRMGHW2yppRLcET-x9hjVWRe1K-m9xeLHQO78waKmTJHsgKeKkSQFwd_sb5C3WY0L7S4OwxmXwdn3Jmt8V3Gtarer1D04psFCElPRjYDSwSpnuNTJn-wbY1CBZdiw32zKXyw-yoGW-dqt_M2c_3tzcHZXB0kVbRcOB1xFmYYEEybyYUTSe9TtUgjZaQ8CYLv6wk5HU0yP-88A0uoY6EDd4m8Pk8wGc8dfBjpJMUhJBGx2noX4yiVJZf4y4Ykc-GgPAektiZovGUYg2rcFJt7s9q2HHOvNr5SNxqf0b6fHOoAoaZ8y1ArCcVPs52J8-Yxc1-OQZI9tKOHhRcp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QY05ZUFhKQtUEEDPgyZbVeW7enfKO_XV3k4ZqCnlQtHLm2KIYG4Us4CXXXdIJBQw_CKRCYEMENvN3qFdgs5me38XCXHFrOYtfE_75uGu-tqCdL9KR1-u31VxCmOvy1o-YyCVqMcZThw4jXFM0l2H58tSS4tOC8Ilr1ZS6ZGce-NeAy8Zx7V9NhuJECyaKL5vrPGR58rztw7yeKgwQj_k9wz-ETzH2gmzH8XMI6pUMcBQCuntj3QGmbxoSxWl0bNE0fS2WXRpvnCRUsN8R9OgBoT0QiNDRKIwMMDmeLPvno3Ti1Q2KiAGoBajfV--IODgR1mkwMHHyYu-BtLE3qCiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsNMfHSkokqtiyykg6_sW3f0AMRcujY5oitFDTudGB19XOA2WEWXXIBNPrgu2eC7EAaOQ20_qyF2lIVNos78K77pZ7sHu9-vsbHf_M6f6CroGn_PL00i_0IQEtNyrFOe-sf-XM1g_FURGz-YIt20a8__0XzK8-m_Oe01DNy0zCeIttR2sqJ8J8JYgoNZOQAQRif5N7Tcr5SOrEpVV3V30B7GTBz6HXC08_PKEqUVKQg_YH_Ms6G0vTQPKOGKB8PTjOYgNiJXf07USfuiAfB8atC3K9HTOSk5p1uMy0X7R9CSyAAIwWFpRxsMG2AgWvwozrZhjetOCaRy5fZysYLkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ph4EiguTQGz08yCzR9cpRqDymzrccu4NkEuTi5-V6VQXw7febVKhVraQRuFh4yPTnvzb77jQYvGNYzpEDVZHMdLdWEfXpO98E2yWf8iFnA_AJXAuJIZf6AlujQHKzBUwb7y9VDmexnkmLW7FwMJiofWi9Eqhq6M3ei-I7RmC1IFgsiXH34mBT6E0eP2ujw6M-AdO8xWlZ1BGNHz0rUqDO4J7P-deIN5Ebfhi3c6M5eS5_82Aa5lx86mjL8Ux6FLeymkssTTaNGiXmPKhAeX_-mrhoWiXkCdSffDZNaGK25m9mygQ71fuLodJu59icWhnEeUwM8IQz-OtulFDpypYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=n2vVT950JFSdNWWGaQPtIR1D_9XYFKbjbnHzSrYD7gVHp-XWIksaeVV3ZINNJ2Y1R7GAwoeIhCEigNczT6ABgtIe3iAsfMHnwJupvnU8Y2O5pHNRsrh5EkBV82K60na5ncAVnxebA5dMeERzTr3pRq5AzXFU6SWQOMVPnSWRqzTYFU3YBgrXcr1OFZCc-Gg6GknxOzr7Q_ArGZxesH7gJUVQixDwdCZ61-m5DbMvyeocdW-vP5QB-_R3yYeGsmnKmuh2MNCVRMDvQiNFGhFZwHST5iWMz7V4dYwBPl10CW7cipEYdF2M0KfETdkYRdOieAZuvZLOMxfsibpdGV2Xbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=n2vVT950JFSdNWWGaQPtIR1D_9XYFKbjbnHzSrYD7gVHp-XWIksaeVV3ZINNJ2Y1R7GAwoeIhCEigNczT6ABgtIe3iAsfMHnwJupvnU8Y2O5pHNRsrh5EkBV82K60na5ncAVnxebA5dMeERzTr3pRq5AzXFU6SWQOMVPnSWRqzTYFU3YBgrXcr1OFZCc-Gg6GknxOzr7Q_ArGZxesH7gJUVQixDwdCZ61-m5DbMvyeocdW-vP5QB-_R3yYeGsmnKmuh2MNCVRMDvQiNFGhFZwHST5iWMz7V4dYwBPl10CW7cipEYdF2M0KfETdkYRdOieAZuvZLOMxfsibpdGV2Xbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ1k2VW1S0OTmw3sGq76V39tsYP6TGDtsaBlEOXJX-bF2kOfmb_vKtTIB_3D5gfheG97H9JqC-5m0-_5DTzbrnoXJ76uzz0NDWFccdEHESvYA4pFOycdHgqUa7WOsrkJ-iGEl_LYrcqy2oPfcXpwvSxUHBgV5rIDHqNonzI-3aaoUcOEwo5we-IhaKLzWqSJaoCmwXV4iR_zVndaFTxYg--gUuznI1hhkoSKYTEGKCTpOaSXT9g89OA5UykZ5-0v_WmSaNYaUQVsW3qv6JzJdPhNU6CugSL4wv_IwvWlhl6b1aq8Uhyfl2DPk4458HYpT3MowWu7SkB3s8N6W1p4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJg4w0h9JG7oRjwU42N1NzbSRtpzYMyxI928QtxzLW2VWONoA_qv2t63Zvc0Ng8DHNqkD4hNDet-aQCMwBc4kK4dvoUYMh54NB6vqp6BMvITOpnb8F0KfI2Lv6cEubGKlzTKg5CPlAexSfZLG8vCUAT4hmCJAby4DCFnsVxo3o4tpRngmhIMlRwvAEhfNnMCkOb-wT-NRRUwyHFRJV1SAaAupZusIQLPV2nYv55KEu1iLQUPM3pZMnUNtNc6Cxtu5jY4MOlVlfQIG7lq7yo0YOPRHA8JCdOt7AePr3O8FagmUxQaeZlkzC65Cl-5K33BWDpymqU9jYcB53LO6fCgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOwhqOc-teV0kQAq89RxFed2CZ8jEKsg_xXkovCxAvT24GDE5LEjUjZCnfz8fjPrUi-QGXP1VcsgXHQGa2yfYL6KmxjjBPmET9b9kdp8jyCFBaG16BTZjw9b0JKLRj9hC8k9pyTdImpxPBmt0QqyUpyry_wX005IEbLWVdG54ef07R9cjXlGuNoiBByb97Hvr-w4Hj8BtapaQwwfFCAMQPoXZYZn8pkGrsP1LMZzIMg28su615bxmFa3nCdnJRH-wAtYGQgUlHNvUJtNFzaJv-yJGcMJtx2kBsH-mNor-wj_YDism_kOppeQmAecJxuJk_-7YILqJ-pyNyAL28sUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrMC9jfOOiFP3iQZajymI5yv6N-yQet0h0Q36Vk9ROLQc0JF1MbDOjLlw7Lc2qA89w17myfma6Xpi8aTCYhDGZg80any_Md_boY2gH8XM2Dxu7AZ_LRRgowtEo8ohz_V40uJiSYqbCT3P1GUDka6XGK27GT6YDAMw7PXVhGvazo_lto8QfqOcJLGNrSH6phgdCk943PCebW3LfhD2yr8RRG8WwK1DkKxSlkyT6TS7JLUyj_Qh5CY9wjKIlFtPnlqHSaGAMazcCnqZcafoHhPVTzG-hKl5N3huyC7dQ6J_cP0MkCcujjKHAfb4kAn2jirjidb0H8XfxHZld5ivaR3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X93wLR1J3cWiy6XovazHW3uil2E2w2QbJyiIM04rLQrKZsi7yOhOddl4MoiCiQg6_iZno5ViT9X-DboR71rTeDZISe_nkxhtqftIif4Q0dmbfTcRVQWcQcBCLoE0KCBaTq7Ja3ORtt8gn0CcaiRuaALuqgB7LQ_Z1JnhR-4kri97qFCqE8RYxKOHAkVDrPGncDiVokESlgqX4_yAM8UTvANs1pH4pxj3FvOLYr2fXoomcM4iwER-wBbB5_VsCsjaj2CD0qVjYbaIOBKiqpPL4OpjBkzOxyTTfrwfCOKTGuuw-tsf2h9EbhlH3pINMVaJLlRLHdhWgm9560PVHTGjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=H5TtkAzEQ1DAeO1XVieKcLR5NfwwZRvuHXvfu5Y71zEsTNkNqiKIivxBoirF43-J1M8araUaH9tK75QInKOGEjAqbLi6oy1S_l5eWrLJDnquatujmgir_hcL1YZHHW0KuLhNwTbFsdlj3FvcIanfs3M6kfoGUrWaHQculLk3mXJvND8aho9xvjyxcxHbCD7wxrNXCe041oTTbHeWQyiYt2CjZGSVn2Uu9Kl6jlU-AVDfkTLGgOYMHkceeATMjhFboiudoAkYEYiMwg_awFMOf9BC4KGoARGoGXFK_sK4U6ugi451FRPFqRaxuubRWZzsLA9RGaMLuYPfr5j8x4idNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=H5TtkAzEQ1DAeO1XVieKcLR5NfwwZRvuHXvfu5Y71zEsTNkNqiKIivxBoirF43-J1M8araUaH9tK75QInKOGEjAqbLi6oy1S_l5eWrLJDnquatujmgir_hcL1YZHHW0KuLhNwTbFsdlj3FvcIanfs3M6kfoGUrWaHQculLk3mXJvND8aho9xvjyxcxHbCD7wxrNXCe041oTTbHeWQyiYt2CjZGSVn2Uu9Kl6jlU-AVDfkTLGgOYMHkceeATMjhFboiudoAkYEYiMwg_awFMOf9BC4KGoARGoGXFK_sK4U6ugi451FRPFqRaxuubRWZzsLA9RGaMLuYPfr5j8x4idNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D464MfHi6ZhPUSi7RGBDOgwWlsgP_v4nbBs0AlCu3tncVM-07wxwNWkiFVvXw8fz4bq3hSe4KonxCiVgeW15X53gTcLcUIGPfCOfra6uBbSnhIOXgbYoDENBE-Pitmp4Qb9m2QWJzCvgAVCQeO8Fnb1TO9QmSq_F1DZQ5fZ5IXq4IoZOc5bLGWaLtEZHyEEmrcOZj-DTd3roQTSx9ELJTJZs0gcrQRKvnATcO9yyytONBMJ4z-oNItIG3y_UwL1KebsBy8-w1wSqZG1L0PSXF9X9J-cNZtwAjXbCo1hG_6-mUsQRGI5_q9QO_CUsJTB_cmpsUZaLfkFFa8fhGJdAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilQLjfQD6L_hW1MxZss8TRSCCeiBFzXxTIyADpV7f0YyRwLnS2JpdKFny3UjN9tt0Mu45AP0AGzzC-_Ge_hwEcXgfc7SslhG72WzJQo29lCM9TGe6iT_NaXlETcvfkDcDnn71BSOOc7Wue9ierqxJfBNYgI0KQkrBYa4dN21LmENPv4AFnOSY_YHuo8X6EwFph9b1RLbTdMCd5kF3WvY8u8zLvIkRmYrMAjAg6NFoW3HmU13grs2S4-qbYsE_MBaA_zQm3nB9dPxM-p_2dw0w6UTt3q7GGiCUltSENiYMwjZXP39XWlFPxp3leY4i1lNv52a3huugePNLD4R4P8k1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=aFDrLXyD9icESI4a1BKUSD-g2X4Ej5CSI7DwEiOqBFu8C8BQ7ifNVjzqLpBqav0o9-dy3WLa_WV-5jrVjROz3PSl43bof1g2va28mVXP-iOyEjRPlZDFTvPX5Osr0JZ09NcQo8ccZ8cCyn2WXvxof4P0687hJiYUZCPHyja6VhB2Jxncvp6gOSiX0Jt4w2aeITWJK3egZfqTQIv1eS2905DVuNJziXtojPoP0OWB3vQ66xT_hKmgihVaCWN_FpZbJ3y_aAQm-QbQjaoq0DRRtlB9cnKPYyhYkyqmKzhECOId3jmVdBvXa2Wc_nxjZ105pPLJlzYVabxfJMLG9G-jqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=aFDrLXyD9icESI4a1BKUSD-g2X4Ej5CSI7DwEiOqBFu8C8BQ7ifNVjzqLpBqav0o9-dy3WLa_WV-5jrVjROz3PSl43bof1g2va28mVXP-iOyEjRPlZDFTvPX5Osr0JZ09NcQo8ccZ8cCyn2WXvxof4P0687hJiYUZCPHyja6VhB2Jxncvp6gOSiX0Jt4w2aeITWJK3egZfqTQIv1eS2905DVuNJziXtojPoP0OWB3vQ66xT_hKmgihVaCWN_FpZbJ3y_aAQm-QbQjaoq0DRRtlB9cnKPYyhYkyqmKzhECOId3jmVdBvXa2Wc_nxjZ105pPLJlzYVabxfJMLG9G-jqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsLfLCLEW9S4V8tVBGZJVHCrl2eeLP31LrJp1tisOjYpTj-NbTRqfnlNaxsf2j8Qsvm4Ou7RPe-q_GuUKjGXgR6IPDYhvGDEDXuwXwH1KN4ZFmlI3bCq5hJb4wyS8sfLaoKTvLIxPy-F61drZiIPF5SGYc5r8MEpyyEyBZSC3HI4dVeECutybCNl4vvt6mE2WP8pskCcnyZdJAKhtH7RkuRL9fKcCRMi3U-gF9tTou_-tLkM9Fg3rOP1m1_8qCqOYAF6I5rpD-u3xe2j6ZdosRYrwZfHKCo_3iWy5p8v8PPrdnnElIGHfrj-VIU09pPkKv3jlQ0jELp9wPeiwtvILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M5G8g75UUZDI0QnsvSbjhy1-j7EfCqc0jZtVKW0Rc0gye47LmbxDSyk07xSk0GYOpoYYC4blaGXDhKoCIWhJ3vnaSNZeDkivYyAusOmw8BIatczhJxPGl18DarhhYB9eNdDTk3jTzwwxSYXSTteo5w5dtSbq0u6d-XDGhi42cK5Y80JheFdwdhY6iR2SY-j4g9d3SSEzcFC6pZZw3HN8t57HqRmdqCoysayrM4cmZ4d-zA_Hl-NUJ3TdT3048Zzjr85MuRbeWJ0OjVy6Ivpk2BT8D5BArf4dVsIzfWwtDkMSrnFyDqOafqkUORpvJ8uQzdcfFXmC8FB75DyuPseosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DLn2g57B1SDJnTfcGffF7qKPFY_i1Y5qpzH-WOrTNjFEMnwMaisq4FDcaFRMgwIn5Lfkl_dZ4Nr0xGnAuK0NF6x-Z8f-_bmX-TktXCutM7kI7PD24rWeOkIN9rV_r3lwmlSloikeO6HNkcV-BeghUQ2mTjExeYyJE5Gc9hKY62I3DU2zoFJ08oWG9vMpQ4P9GhJfJqHJb0KH8-PhKIOClVPPx7RZ1dKkZ419Zj2j-Pige3sPQ14KO3Q7Q7bgyTlyJcimZ_yv7SvbEYwVmKsLSJ8baBLE4t_e7koNRnqwewaxGNZx5bfgjjGWEw1DvVVyR1ngzuPBgaE4Ic8xMbhMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIIbskmGHfoMjEiVGXBGzq-gUBIek8PrlVMwn83qG0lvbwps-SQXhd07zA5K3PuZhT89Y-QvSee2fl5SJeh8emoND_jMNalpXbwcwFYUFWLtGumtTLYZEOSoE4OM0QafGHI05YmQuoQ-rFfAqrERcGDKSHHGK0A_6H8Un50GaP71LLPoloZFcpHPD7Fie5z9-8dyGvuZaMqdAIf5Dn17HjySPs8ArJzxbmP_eCTon-SjUWnicCJIdisb-CmKzVT0gT4wBgNCep6NDG4yomX9LTfzU7HZKQLqtEHvCyElN1aVOM4dhvt-SOJYuZVpLTwXsEPu1lH8niDRnPEzJEHqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNmUshLrGVrTjTPRItdoDukHWm2jaqkpXZ5HAWCTnGMQhievbhTAnXsomxC-8VylKT3WGoZvoqvxbPL3L4actxevWTE-Pzc3_nyyzX1FlfLbutf3aR0lJQcbqFk0KBhSrJH7lf2pY6khYT_Ahfh_rk8OZFVolbWuh4YwVhXJ6d_zLx07f0QDF77z00ySzakcnf0JXYI5NtufBveF7SHb6YwfsluUmnswmNvoOC-1RlMaVUG46l2Zx1cjeFibmw_ljmyRAeu99R_a2KrxXdGeQOzUQvfspZBQfXFj7UIpaKHc4gJkJ1-1DWW4BvW4GdHQv3h0mYzdQ9A8Gzdbu_rezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlE_KsfOdjafwCepo64eaHcf9s8CklygUVP0uNUkucMl5XFYfHHadf4j0dpIFRCSdgsawR00L8TwIgMM2rokHpd_Mmt4RYFxE3-iRYN37GNwHBSrfZRf8ysxIi_ae7QhtZR8iHmX5hGWVbgNOA3PjoeJVz7-gO2VX5FCSC8AZUwFQyxY5ho3zpuoMndIjFd8KhW1xH0sFgwuWvLmQVLsSTfcg6yXZrQwnIU3rPKjjaJ0ivcpFyamWna6-VUxZowvnn38miCMyODodd5eG25HrerkcIJEsIchQuYarJCTA6X_o8pYCXsb8CywRjea4XHP0bLmQbhxNcklrcah6tFDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CGYn_oi0e2-0LJoVPp-buNqokrJR3hwF1l4pcM_73xmRXss_kF5VRXlUsgi2CEEHN6w_xw0WIhDl8_V9pspr6bmZkXMf7QptUK-ND-ZXpD6-qDmfxh2qonsDWrdRx3AYNw6sb4x4JkXtB3RX49BqhHAqCHGTV8kFYj0kizLAo8IgisKaHeeeZ2ulv5YgfLMT6aY3GUUOTonqDsg8RIagAzM7evqsI1vK9CKS3hHpryj8HQjYfLkCOsIocKkXboNnhXKjO36d0y0MN-VP4YSdyKhrfUI2zeO1IJ27R3AOAjNO53I3h-ydLyOhD8Ck-S-Twx8C5fcVuigrTv_1cUnoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=Klb6jxPWqvVBpqTMI0jNEvU7sXe3jb3gVtV48m5M-W-ZtfzXmtMgfqZfGEthexyoJDBziKkIZHTLp98MAPe3O15gpvgIdVVKJxXE-v7p2fEYJACfCK37N1SOfE0aBj6pBQP4ZPiqgmH__bY98yNeX73IVl2D1tBA6gT7Fzj_TsncNioU2CTVKDNJc-uTdSrnze_CX8Udtieia4JlA86ztLZEHH-UPaP9NY57Nghp2Dq_m9Xf-LWV4r6vu3PM_By4v_RAoN97IIfpiHd-TE_UXqCdA_Dk4BmDbbpnj12UcH4dGYkB5slbFGBwpPnuWenDGq4H2ff_Z26fAEUc7-O__3xirlmpbcJKRBc-_9GQi5OzU_N_TxSzKjmmj5tTr6-_YLU-rqATS4axqMMM5C1I59yGSWr6T1c8vs2NoxY-UxNIewJeI5jBO7yZi0nk3BAJtaF6SuKinSl1zRhqCLZ3ecIyo1dl6WmzPRdhORcoDge2oj-SH4wsVH9QG7-o4xhYf0nV1CdrYYHOBcqK5S8RBfxyDKIb9T3-aIVE-kcaP1KTQ9-uP_FaDiwf_r-8eUwPobOIRubqIQ_5EpCtmibMbc3T0NY-xmRzmqSoCti4i2xu41i0pE6sP6JK462uI5oIP75alLq1ie-eaFcf9qDcK90mcA_FisPuZRsmii4t3w8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=Klb6jxPWqvVBpqTMI0jNEvU7sXe3jb3gVtV48m5M-W-ZtfzXmtMgfqZfGEthexyoJDBziKkIZHTLp98MAPe3O15gpvgIdVVKJxXE-v7p2fEYJACfCK37N1SOfE0aBj6pBQP4ZPiqgmH__bY98yNeX73IVl2D1tBA6gT7Fzj_TsncNioU2CTVKDNJc-uTdSrnze_CX8Udtieia4JlA86ztLZEHH-UPaP9NY57Nghp2Dq_m9Xf-LWV4r6vu3PM_By4v_RAoN97IIfpiHd-TE_UXqCdA_Dk4BmDbbpnj12UcH4dGYkB5slbFGBwpPnuWenDGq4H2ff_Z26fAEUc7-O__3xirlmpbcJKRBc-_9GQi5OzU_N_TxSzKjmmj5tTr6-_YLU-rqATS4axqMMM5C1I59yGSWr6T1c8vs2NoxY-UxNIewJeI5jBO7yZi0nk3BAJtaF6SuKinSl1zRhqCLZ3ecIyo1dl6WmzPRdhORcoDge2oj-SH4wsVH9QG7-o4xhYf0nV1CdrYYHOBcqK5S8RBfxyDKIb9T3-aIVE-kcaP1KTQ9-uP_FaDiwf_r-8eUwPobOIRubqIQ_5EpCtmibMbc3T0NY-xmRzmqSoCti4i2xu41i0pE6sP6JK462uI5oIP75alLq1ie-eaFcf9qDcK90mcA_FisPuZRsmii4t3w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UFxYiDfMahcB0TMNr7mw5Nsp45FF6LR9ZJXEnVpQa75cbVOS9EUJWvKZtUDjOlggoTG672uAPSN0h3UxZDuczpDeY9-xqKgGZrTulDr5Q5nx2Vr7F_BFpPRMTb3VPKEBW4-SF-YhzscoPMVr23iE05mSNaGna_oJvoEkIsQDArkyFcengpXR8nsAH0GFpFXorRCSYA2Ro5AiI_P8ivI0RyWZ6oFL3-XOPX_8pl9AIw_yWzUpef2TDxqAopmnAsTfeP3fQytivxdaCUm1tBW9dTCcRhZkGE16Vk3qRA9r-HKTkfExa3D0ErnGyAhezTmdjzF0xc4cSyWmJI3If99PQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kn75cP4Pp-pktvWUQpI-MEBVNPC5f1LZPLQbZA6lhf_tpHUDZ_xV_pITdqqm49ZYcMiAJ-PX3w8ouhy9-Fx0_hJHsuDDqahDcRHf4cfSXbcAwMas1qyI63wlGCIdiKCNd8_5-wzkQDlu1e1H7CVgWQfk1erfD0FFGS-Zxd-5AhJUAl4Tq6Cr16l3gKteN9OYZ_LLWj1yYmvQk7Qw_huveJLIb4RERj1LviDluFwc7ghDiHW3PCJRMR5_KzccMG9-BsezZXhaSMsI6FSYXLIbQ17Ohn7CBOvtoOMZ_rJ9zSp9kXMqo6Fd29ALsxihcBk-ffc3iKlfg3qhdJp_AeuAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fMniRjj2xPt5Fwpku4cxRD8Y-IclNJaWYXyVM30mrjaHZmi7-2iaNXUF_zLp7JCx-vRqaidiUHvnLk9iRdYTW3DTkwk-lVDVyqyV2zkhwseDT76C63sj34UmMIJqEcb9em8ctRLhtMeyCVSAbqZsYEzErhkGFafVsKjwj57LKm3IDTE-MG0mCnjx-NsQ_SX-QH_50R0ZbnxKBLuA_IWnOEs91EtvOyYJYGhAQiXE0R8tgk_u1eIC8zcvxaH5Ic_6esSrQzFdzP-AJlh4HIMf6SOfbgHZSEOjI2wI8CO8Sq3ybqafbJsuMw_6yCi5JPsaDlJFJvzjv9q4s9itZaOW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UDPi5eouZqptbPHKX8Ex-QHnKK54hhFDSyWLqWQdoWT3SxskjL9rq3esFTbJ5nB02Eg11t1dGQQl-gLB65sXZvXyGkPcnU-GxUlh9PZRBjCdCfzvq7TO_Gq02ggJAsrC3Pu5oSWTvraL0WQb3r1wxu8iDOSv5XegXUL5FM5ZlnptzYchgJMCYZSYU4n9KSSPI80aJyrf2C2Mtvm3mmSvKnlN7s5nLBWbyI-tHXij6ILCX3FgNKmyuhEBJOKDxNeGCYHfVz3-7hIRxPG5g2Cnbm93oUnEezcPyPackJGYlhTp9ndc6orTyYY0qnuWZ5b0isZF49C3WNeU1iq5CWSBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pll6F3C2Nmf-FUsOqLFiNPJjMgO3U9lwowUhW87nYsIbXDKtnLVnLtwRDbjy4HHGgmU9dKSnM2O3bCHVANZpOF_3pzWRxYTMAfLXdikwfwkvY4FLmxcFM5_LSwSia8bI6_Ih33s08j-kIc4pIo_JB4Up-uRlSumUgJa0UAr8IdoFprrCpW14xNSaLLMxgndo2OPSEbsdAtODh3QtL7ZSPFpDuixoZ3xkKZH0ha1Oyj4aro6K6jOCAWjezyvWFlqJYr1upFKwDlIhNhbbhlu7-kY3p-48p9b2gLwSqw44mZuTlHvUDa4_oyhQaJ7BRTA2eVItUiblRQhVbxQzt3midw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Etd_Exvq3NX485hBIVe-Py_dPzHF4azUlTzA4c24IhtHO2iLRTI_ccSi-E3TMnazhPDop8oN3MMBgmpuSdOcfyFLp_2gI6E0dCMiMR-9f2iWWVQRjNkimHi6WNwD9kSYxAUo2AdVVNqT7IDPqt_iyBIyCyoASWi06OB73zcCPV6KcY2enzNWmGQIJeZKdAV8Vxy3Pqv9gFlmFRqYiic-VhKFUPkbDFoznD0vJcwhs_6cH0pNpt21AzXfMO-uKBTevexTs3u55yyu7l6W5s1WWGuJcrjkgN-yEkxyrCV30iL73QAmbvqLhdJaGxGTEe0EBMUMjYZ88Bzq9pdP7cjR6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj9TNEZVsJg_-eoCZr_3rxNj8u4W1xRfWGVM_KhSe09Ez8Rm6zUglc8LLNTD9xZjNZqOj9HwCntK0jQ2UjxVmtHrgjLdd3V4uvlKFMPNxmqpF7JNO9Q6Rbhx27eoMO6G97WxSWtlS2I470_NhAcTCUQrkBjYt1YvGOBJEWxYYzVXmXlxegJFGK7rGqEu-ihmZmt8AyvJhVZteUE2SuRJkLqIjYY4MNJ9rVkfqHx7zThghI7SLSnWQiVsA-YErILCq8IEnqiLtPeANGxgaXCGPCa9FUqiKw4V5-vMP5VpzWPpEwzuXmJKBRAR4SAg8VELJwFLaWrMKoBSjOku9ZTNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8iGxrB7DezDdI34zSlacFaogYc_NtO0Bfu-Wn2-Jt72BLfOojyYrF5EbIBrRcBf8w7qqXUZt_1mQY96Ck6EX_vkjuTMCkIrQSXkcBS4yElbzmTrJ_GZEJBrY7g8zpjSffPFSDCSvIKsw2AUlOh7pTxls4QpxBCOEitKnHkewQAVaNLR0w1naz5hbGUx_bPSTSvYKVxjP3vu3iX8QHlJzin_7D_sivdNtgNjJvGndpizd7JM_E2ZfOllOWd_Y7lG856Ky_U_mJjBMVfjR1DVxqNaTYar3hDjHwOGCYfIFAv5mAxOlgOW-_z8qQGoMkT1jg51kB717qFGI-K6gl_pZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=b8BRXheFgzb2xf4zCJsoIfgMqP8hO7--qPqHyvpRRySe8evp4C1p1PWN8j2Zwxel9Nx94F9gKG33QECup5hkMLYFi0KqBa2jriE7Qib6e51Ttb4Nyn-B8ULcUUICq-nTB6s1NXxitaTZh88EJ1ujhlQCLmwDZ8mGHyIqNvr_jK7dgpO5aEGo_4ld1QahOiU2qzluYdf7lOn4Uo_zV4TvXM0G5i6DcM5IpHHJu9Fjjsw_tAKgKToqzQw4QWFt9XHmdMKxotb--GydAUGo3Vq7RNDi1hovZxMCI1XWer4tht-CJVWLR3JQk1vJES183_wDPqsFS6HFOQGVHrfTNt7CIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=b8BRXheFgzb2xf4zCJsoIfgMqP8hO7--qPqHyvpRRySe8evp4C1p1PWN8j2Zwxel9Nx94F9gKG33QECup5hkMLYFi0KqBa2jriE7Qib6e51Ttb4Nyn-B8ULcUUICq-nTB6s1NXxitaTZh88EJ1ujhlQCLmwDZ8mGHyIqNvr_jK7dgpO5aEGo_4ld1QahOiU2qzluYdf7lOn4Uo_zV4TvXM0G5i6DcM5IpHHJu9Fjjsw_tAKgKToqzQw4QWFt9XHmdMKxotb--GydAUGo3Vq7RNDi1hovZxMCI1XWer4tht-CJVWLR3JQk1vJES183_wDPqsFS6HFOQGVHrfTNt7CIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spjhaiK3jxPZe9YP80ur4_Ju76N002kiCKYjxPw6SbMhA-t_qIHRmCCRRrLZohItWbbXOG3ewgnQhKRHoQfvoRNX16ryyOMfF4s2b8PI-ogiHJ1Q32-mqz88DrddPESX35DjjtkH2fZqJqdY7m7eheuOrFmeTeefg3V8Dj6rIxEeRg5SECp44vDuytiLGT8hKPnmfTX0sH1RhUN6ekxQrna4SRvX1GkpoKbmp5qLPN2Vdr_zf21FuT6i1Bu9eCI_yKXluYQyFgmu4h529yRQ-Poz29lZ4mSR-Mye1xgq_PoVctMQVAQIqnePt26m4kH0Mdq5ntCTbiZQm6xoMvck4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=BrtNmDv8ZOtIpweM5lpycS4D_DzaVgOhQlOGdvGQvHbbZzyl-sNrRYxPwj8GMDhbdRZ8TDigNR5R5-Yg1ZUM96ktdZ0J0daG1ta6Tyd2K0_fDnt3Y_PDgXtXaXQIg55xHvcjJSZ_3ey-gKopGMUVDFz21uRg-CA7qQnSIkObPmsJM70gwtEwtswvfh9Syy5PBBJlTjhxAgPpNuWynuqSFzWbykvplxd0PGWl1-d4pcw18--9vqiSJSIBcvk81JKIFso7Kj7e1UA6UEuRTFuVTKAmN8yceB2wC_QJktZRDbXclruBx-Cfkab5P0ApYXgF-ClnOZONmCpsmLmuRcVFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=BrtNmDv8ZOtIpweM5lpycS4D_DzaVgOhQlOGdvGQvHbbZzyl-sNrRYxPwj8GMDhbdRZ8TDigNR5R5-Yg1ZUM96ktdZ0J0daG1ta6Tyd2K0_fDnt3Y_PDgXtXaXQIg55xHvcjJSZ_3ey-gKopGMUVDFz21uRg-CA7qQnSIkObPmsJM70gwtEwtswvfh9Syy5PBBJlTjhxAgPpNuWynuqSFzWbykvplxd0PGWl1-d4pcw18--9vqiSJSIBcvk81JKIFso7Kj7e1UA6UEuRTFuVTKAmN8yceB2wC_QJktZRDbXclruBx-Cfkab5P0ApYXgF-ClnOZONmCpsmLmuRcVFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQtsvCaPk3XPs9EqVnIia1C5dhIQQojEUqt677zRo5VS6Y2ESXmNjxYQd5fq7C_b7iaWegsY_7VRLK1mfcDX7wDpD1hLeZ-ngu510_ZxO-SGrxguI75NEd1Y-kGYmE7Mv2yAdl74FCMtdQv8dZrP2QojIDyuwP4w44iyo28BOazOcsiCWNkm7jsBmgK37xqDA7Cc4QitCllZ_RCSo0NqMHWW4vGmSGzCVovMcZpWfyynrw_SDJOoBJ6Zm9STakVKVqmbTi5u28b23D3BV8J0WRAVUZyMW6Cu2cJ3nIuyTUvtJhTwaBGUWv7rVagOKevT2ZRO0Wwu6nJasj-wWCShDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnt354CgIcRMfUcGxkgewKYZXVJQx7F4kjkgb_io-zg1GYMJQ43mN5Ri8jLik7WGgvA8igLIjmrMcHh3H1OBVFdHc4CBSfuN0qxSlTn9vbaIMDakLn-fEFFr92k8DrFxySsReQfg_hx2di4ijNkJDI-m3KlHYlqLCTkhIjBiBgMpDDOh_EHRQYZTB_pSmqIhPhPYYQePK08A35nOJ8G7bpLi_w2GSRB_wxfM3DUvUwphw4LmAMz6LiVOb7-DzjrjggMYE3liM4UUCTMlr1UGM9fP29bM8iQ65N5q9V_4VUeK3pow69p3W6aNfC_w6-ZO8H6Pa9Gf_NQythYm8HP95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mAkkpwESQ50fJfFO8PfiWdK6dAe2sMWDDr0epihTWYGwJ5FYu9yBN3EvBMOEnhy4KQEraLdXmlcassUUtM95QzBauqwId2XxGoDTkeuz6bp3lrtex8LEIO5psF2kFX8r66eHrBUt0kDY3t_UEjVK6hXjJ3wZBet5l-zDIxy8xzWoyX-52utw6e6RhLmq_S9mwldMvXWm8DM3PaOywVjAaHQx1PnCFqdt9kKcTe2fiHCLfeM2TJfFknjJ9Og9Ira-BNeidz3WnBxL5VzakaDt2ixyIln2Dte8SqNhooOz2OzPhHy5BpMfHbpjvrHI-NiFg4iXzj3J9SjkWPb9sPgQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/utDGtejroSQU_8iCpAyBUjZ2NCUX5SQJdDqSrb4MUPtJc_iP6gMk6xgmLcWMQLvDzPIYwJsJ3p6EKneiXlizwLz5e4d_6OyPkQ0kj4kAaEeAuK9jeMmFypOTFvUAHgBq3WfMgWFN9BSISPPMA6m98DdnSvVCv2O3NAQBp-ccOoGZhHZbUOIdu4PrKn8FmTFmHHmj3YrvxPQkJ38VGQol314bznQq-5alam2bOgOjE3kKsVPqhGyV9ikmPbn9XoFCK0Qv9gL8fIW4gCgqUy2_9QeZ0sxupWS3R0V5vKewfVZ5k94fapQGDxRQEMGlzIoQtKPolYTcPVrzdKhVSa33eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ7_pVn5LA-NErRNepeQ4OTfMMLhFxs9tS20RSqQNK3lLB_IIj1b3HpUK1dSyoAxm4VPJmkUi-WwH2yDdh4RwuAiVjveqKAA9cxzShWZeJQuvEuQKvAeYNbBrRfNFPbdPVxyOSQY9ehw20EYdCrBHwchd2GXl-Ku-ag9mMcezMGTptYUlgzDzCbj5jr0qsq6PQSr0SDVja8mm7k0SOQWQIe8q3mgUx2VXtV8f0hbQ-KjZjZoSF3x_CDLzH7C0y5mmi175ZXIwJa7vWRa6q9A9Pp-_YzBGDEGhdE3OyC_ZLTOoE-Qc6s5fPsq4D2GSJIVVRc1OzfDFYIWzgBltM6nsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MwSw1vFg085qE4gnvwfkfqjYtNfS0vPJehTqKtN0n83Q0PC6QaMIhlI90KklwUARpMTq6H8jHsPSqGIBn1RVLpKZnbzuRBn38_c8a9GrW2qI2Mp_tRYdAmHMsGNJECcpH1MJzRlRcgV5Qe0lfbYGLP0RKzs-6XuK5c4Sz9VFMAvb2wMY1ijhUY2oCDSb-b4SWzn-D5n49S19rS7gv0JN4VcMiT702sD0Hn9GcBJbW_WFr1rfKEldp6c_x9BoC1-h-OsXxsa-WXo0KrPiGX9XRtc_-k1Teu1u6aF4_Kp8FbT8kbe94coMb11Bii3s7h3ks4cEeQedxoRnD8o5eo5GKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uv5gX5O9gleKxqi1mX5frIoMtP5xm7ONr_SScbAmPb0jMtnGitw0I4fM0TV5vXggU3MeJiriVXjrJia8-dU4ZUSXt_UIFqD4VpNrkbygwtltGa4XtCsIUQrr_L-BZuIQSFMYunq25axT7NiYjWHyLdcKyomA5uv1bwu8mIYLGy5WPJIzpRhpr7l3eF8kiRLjCyAd7EqZgLRGXeiAGyDYYctlea_xvNYneqga9vnBruPj3LCNmQxW5Vg6oCWVuNV1djfT4YjkkFMIv_B0eePI4b4gIby7XCcEf_fF4CtVlDu9RZWBeKHaibTMfu89JVtM4CBJzfKpXo8h8xUezOrqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IWkd4kXzAo-kQ0EZcY4tpJ7g8nvGPL7uRRbZ95iwaNcNcrSxasrTQTVQC3gANmGuKSX1W00t3vSuqqpySTveIjgFOXh3GnAkGeUpY4-1YSlSTY76SqJ1C4Q1kqpRiY0-FTF8vorNJh6IG8TnMYkIzsFPtK-SgkQCwKlF0nX9dMcG2kj_pwNKQBIugYtC0li3klBILbzSw-X2TjYCREnMgLnrb5_8G18OxprapcZo7XkBqza_Zof9CrBJdhtYRu9gs_gMeKYPjlPqwUHHJHnzOKLc5H2q-rrRSN3pRzHxYlAu4UKMbUL9VY1coXanKuMv2zHH_IVqv_fJSJ_dzoaZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u0mc0SelzRw5jHbMbEkFtjis7rjmrX1pO7l59pCWuVqPREP2dkEcHnXmsJeYXxx-4ex5bOTy8etPYd27wIWmWmg5FIdnmFfvK4qH8ZaEoH_DmDFW5vZswenelFoMiJMToxHmJO7Pa4r0ZpA4EU4rCr1gj-WNiEbEzQF2mnBd219Xd2z23yq-Llq7I3CHMwqW8gpnSAPwmTU9cVh6SYuhu79bH8htn7_cr5qskMWiqA2i6PXQyapbZMg704-VhpigrDl8UKlnE_PjToYREjq-O8O3Tl4y4nMR2qcqbxyk0cV5Xg08YSqH7dhXfGmJpZFOifhpzt8PDXG3_enhkF5dgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d7MvS8HSART-SWBynMDHMPpHRqYnl7GUYEWyr5Z874rji7NurkiVXP2Z-_pc0kNjWAZ210B3UlYSSAgyrxwbNIQpRIMw5K4XRb5SPsqQ14oqlw0JYAnarkuNE6-qryEXpt8twYGPtOZHcZyL0hlv_xDJi8ccbIxASWLrt43jBTBMRicEZfnj4tyicQ5Xtqf1DEvEAxjBXtPWid-t21AA7TutPA9P6Rnotx4NGn1ujRD5elLiREtqhuaGud5ZeKF0qQSp8lo3joYinRxkJwNb2wUIgu9UiKsu7anbixRI5LfEw-Wiplw3OZi-iHGFA0RXi9t3_ekoy4aNyH9bx_8sAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dJTqrCfsqR50ZaQ216Hh7PSbYkPo8aVPJ1ooq0yqSTXcC9y2s5Mr4BmZnmRgDytEMC3CfTvrJ21xYn_K25i9WfJ09TO66jehmaK-bV4t_avlAL64B7QhL3kmxES2noc_qXZs12EMIpTKnZc9eSKy0nxus5kvpfBNtJpoa5CiyqL2uD83897hBlGXvO48uydGCFlabR3MC2k7Jxk8Exq15HtjCOaGv5Z_nOusbkS6JqiAj2WgcRiVqvSBLGyd5NoSmEEKxEHah7J9EjTPrRbUia7ASdMiV0YYo3iDq8Ird3uC7oDub_XiRVsoOUfkss81HyHcCD9XGlnidGuj8AjQ9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amx8ftlczabuoukdisVr5pUt5-pavgSXw5gDighWvNQf23dJRpdWy5rrXc3rPLoLe4nMgjuvyjwZUsb21FJvEr2Cg5WWcEGMwwX14EUhImUPv5Kl_zuBm3DqYVXS2-lmK50Uw3--AmGfPiLKccg5mGiaxmCGQ3u1L1ads4ABiUVQALhlzJsEgvkZoKn2n2E_YYPCZ-68VqcxQRBfzhUmZ883yOl_f1BBGByXZDiErmRxkXYPnFSrzqEgeF_mk37l992c1vL-gHxHatoNnB2RrCyM676fLCPUKB83jqvIHe9x9MaS35qrSUVdG8FQrFmYhLaASzaKghgBHGfobnuxIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1no3rIEttb-5q5nqP38mGQX_PPiTe4DjOhcUYvBp2UTkLYKnoeeXzBluNSpo1uKnV_UhRwJz8ItylXcbpw-IEKg_CQSJjiFwmjYEwWQXWWLg1J-qxE-7IYMkzpno8zspH_iPpAEvcD7be5_tl9RFg5TXbs5QRfKBmxWN1SOnX9QrvIYf-OZeDTud4gMQ9tEGma9bwlUP0spnKb-bTlPxw_lo6YP13-3MWjDf4x0d9P1mq7reSUZ91Kdbh75m1XDoedsdK1fWwhNSZ4zhHwRzHyfNFMn9yOAx9oqnhu1VmGwZiuw9jXwKwZdueFiC_rN4Wti4_9g5M9YesiC88m8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_cK_47TttvFqG8oynxpB_zzdOO4Ip1dDWShjiOi8gO682TUmm3sjLFg0wv8WdMYP5cV23o5kLgDYG57thtXb7-p8CquhjnLanMABdBdKipyZd3RC1FXNaYfThA9_CBppgqLtL-0Gjbh-pfBk3MhEz8z70vrUvoXIr4v3L5mwSU7HAJc1d5AHN148phOtp2lVZzECZb54S7Zyt7FUxtQcaLVoojariIeLI-7fvNUocqkttqZBGqyd8ULQxhXYhdY80_5Y1Hs59c9b68bRQ-AO2mhO27IprkUf5U_lrEKrvhIjPkWRxWNXQCyaakFYGZ1PqIhauskAmdQBTbHWwuBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vw4EaIsg1yRPU25ZsJBJ6UFrR1VIkSzFLjXLfuYOZn1jkY-wR_0mZHNuJvwKe1WMe9SF01qGsClgUbzzCDJM56NG2SoM6u-IoVvTnQ4-GCZSNbRG6QgFqY2m32oAEEjHNiiNC3yZKlC7VmZ3oFphK9xeW3gu67e2Tf948-iaxYKP01rKMiTtg9ci9WlP4Jzu_OV8xswjgv8v4v5ckldDQR7z1VvriPit_qL846fCRdpNX1VmXBNiNs2yGB7z_LGTLzjprMqSu0WLB_AEoBazq4rkK-FSDN7e4seLnMb7VH4ShH3W1IFHHYXUiBJKiSfrrpzAC2TZ36ZXOjV1irY2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkTAGmL0X5Zk-Pq3mFhBLStV-SgsDLt_jx8yatpitm8yVEKW3IIFp89bQjqNN0ie69Cea1mDmuC3f48eQr382vbM3EG_urj7Mdx3E2Yu03a3UhtTTVh-76CrYsPPcpcI7NJ3oBL5UeOgnLAeOmljDriYaUZIVx7W7FY3nC9q41dyuyXsl4yLnctoAQwNCaurppYcbzfPAUKmPEPo2jj-q6zuOfeZKLrnsi2cOBXtbSMHfQq2L5QYZyvoDSrZ-QY71L-KmJ9eG7CtDUnZC5JDSo2oWXViJ-oNcLrF5Fdwoy0iko-38fshm9g9B4c811GNRAfkebtcTiQklF9VqnOzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dja8JLja3L67Z5OUwknDrRjZIqxmk6SvCPC_5dvZJywoIHOlZPbEEqZnr9472Oe_8ixCrND_g6CbriX_ulZ4otsnbcwU7jcNxB2HgJF96jJ_n_FGGJXXauPnORUaamWDTLw88Nn9h7wCunDMKP_VMv3whPNslNZk_UZvH-SCbBav7xPIQJGyG1F3io6yzvdzNhtSoAW0m44VKPGt7jw1rCYS1uhgfxGmOGxZyWGHsWogf58BF9xfDggsnGz1BQbQKUeM1wgFNGjiFZB4vLD3H43_pN0L_v1Qn1emQH9_jD4d_M5uAzodhV-UeXEjJL6nXFgQUXgJGXhYDNP_LfhfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gY4rTBLaqxHxM8MS6qnautjcB8Sj6k5pQjkJXQjIeA6S8nrIKQGibqNCKLLjguBzXaNZpUN31CIIK6gChNNZr9vjNpNknTc2GL2lLKkSbqeVEKRvXRfyu9vopGZNE_lZPySjdQe0e8eucdq26aYMywWdQ_C2MBdsU3qJs2nhVHLts-h4vVmAD85WhTHOTuzSpkqGLqzlUZm_ke-bKssdDUCqT4R2vckRbZJDwch9ZUDn4QxY0gNuTTxDCAXXEyI9lPo_kUWug_kEAfi6RzEvpwPcsDd_5qSV3mLEQaykTjNkormE17LrSW1B77qGaqGou8uyHw2pn6-RbnhQRIN6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V7IwZ1oD-OZBHZm0ykrfB7BEhSORQHWTT1XiNsmetiFqwnIXy6I4kWyPVkwE4fuavZhiXz_wNWCTT0H4v6oiwC_MJMGrKzsJWBEb2IIz_kllXZz7WEnTeP1EUDpg6hkfXZZQnK-stIBWo6o12MfX8vKRFtamcJTwOMteh2mHHTNuSVm4LWLQ8uNGNGXhuMm3XGsCVOjbRkxSvfJdHJ1pMEKDyjZTJudn0nuk_ktGlSJIYim2zf7zcdXvRZfxw2vf4FYG7YVP-9GQx9IkoBY2dE15nIiHQMk9M1ykimoDaQLlrRBn6Vp3BhM8Th4v0-enhhlTn2goq_HSbiX5st94GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G9GB6JnqXWch3ej6jw8genRssxgVnRYTRjxUqnpfaXkQ5Anc7at2JvGpw-FTAkcsWsvL_7wpmvLPvuigfnj9IW2SNLo9JctI5Xl4UiW7q0QSHDPTceiaLru_hgQ17jOE1k0CuU5yjqumH9WraS9mk9uZgBbVm0bGzLz3ugv_EtJamqO3opouMzxvA2n56H3aEsW4NkaBsqE9KzQwZlk_8zyTF0Xj4INYqbSczxnV71MFwkznqebgT-voBJsdm4EOCzZ1Wz_Q_ZAJhMm8y3ouOxRXcx19jnKq7E7pbg-3G8MmZsJ_ZHuuzsEqwLxxMzMQBa6AMKT6LHGReIqoqnrH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=iEq3bB-VCzxwNt6_S9WJ9BfOReNHBXW1pX4lXtqVr913rg4YiEsdzHuGmKhQtFt_jmgwsy9FApANj_MhlD5BL4G9ZteuvEFMpQ48q9YcYTIEQrjsEor6sBWRrjUDyC71Y2mtXT7pTNGSdzD-dQPzd63St5x68E34EmmyLgcK7uxlBSrOpUBjdrUih7l8PdnqfafmI4fLyz5yv4TGYAOJhhOGrg1Y7zs7TbnmHOMZz7NglrotWulotFUKnuUrBfyJJjeNBiY6KsH8fOHvpLOfxzFBx-aFv5pLa9Z90hlMPxeNvsIIWHirkjrVEpSfumjen_E00SNTMbUqB9YenQK8iA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=iEq3bB-VCzxwNt6_S9WJ9BfOReNHBXW1pX4lXtqVr913rg4YiEsdzHuGmKhQtFt_jmgwsy9FApANj_MhlD5BL4G9ZteuvEFMpQ48q9YcYTIEQrjsEor6sBWRrjUDyC71Y2mtXT7pTNGSdzD-dQPzd63St5x68E34EmmyLgcK7uxlBSrOpUBjdrUih7l8PdnqfafmI4fLyz5yv4TGYAOJhhOGrg1Y7zs7TbnmHOMZz7NglrotWulotFUKnuUrBfyJJjeNBiY6KsH8fOHvpLOfxzFBx-aFv5pLa9Z90hlMPxeNvsIIWHirkjrVEpSfumjen_E00SNTMbUqB9YenQK8iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuUN4M74OCkJGyaLd7T6FecSpKTiT764c-NVtC5ftiLu5VbVlKJUJdyoEcY97r2hDi3w0Kk_OHNjGjuP1e4sIr77T2LQb28GKEUqMffc597Px8i-WqajaAC_CSt4Nnw_j2o8dLSvALwytUuVlT5cETglPR5CQOCmU0szA35FyXZnjbtoi7wbZSMLVVT3lN-8T2yv2zRkQ9w-JLCZYBjHQZaJYLaoxkI-nidvkveaFFmIra8CxkosSTn5YOsM44HciTuhbgMY4jzCkK1XVRC-Be7jULDYhIFrkuI5JoYyycdd0Hh8_9jDzXE0v7IexHsTxSUz0wK8qEcPqIxZXRkXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=MMjX94WmSgAqZ6j1pkUF2wg3tfTdZE0TtGkPsMb2j_eKTMCXwHAsiituBaqrrYDiDCHg899JHQNtAy8YF2ICAWVL_Y-TQO1GPeo_NSNQEf4Wzxz8wpeaZWyyS0NQpbvOQ8XOKv9_JXzWJMAsSMGGwJDB5_jW0yHvAzj-maiyddZTU-_k5x-u6iMcEq4hPSNAeFlwBSNSKoGwbDO6vCTRZQC5RxjL8mn8EMLfllAnanAfqcR1R3LQ4_TEl0nK6GWQ0YbVHoSDSiBZFquKHSJo4AxyEwl8LvPlVHYGX-W17ePx7TtCVWqVUi0iXbEj0_SFyQcmMKv8MkC6EUpsEBIAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=MMjX94WmSgAqZ6j1pkUF2wg3tfTdZE0TtGkPsMb2j_eKTMCXwHAsiituBaqrrYDiDCHg899JHQNtAy8YF2ICAWVL_Y-TQO1GPeo_NSNQEf4Wzxz8wpeaZWyyS0NQpbvOQ8XOKv9_JXzWJMAsSMGGwJDB5_jW0yHvAzj-maiyddZTU-_k5x-u6iMcEq4hPSNAeFlwBSNSKoGwbDO6vCTRZQC5RxjL8mn8EMLfllAnanAfqcR1R3LQ4_TEl0nK6GWQ0YbVHoSDSiBZFquKHSJo4AxyEwl8LvPlVHYGX-W17ePx7TtCVWqVUi0iXbEj0_SFyQcmMKv8MkC6EUpsEBIAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jCvDjSARdB2KG1pVHQCyHa80CGnV3u8vIrJWcdoVc4oWbeqUrfpxESlxDy_cUtCbwMSocCVK5GLFIrAqmdeRSm1aKtHDbiWQuxFHTTEF45xr-RUTHSJYNKN1xmbYSqQT6PuIbOVwLoEMRNtz4D55s9X7lWeaAKngOQM_3irdeKX_H8u6Fw40o6TaNSXh3ak8TluygjZD6QfankdHUeILn_Dkp3Xzr_BYAFYwBaIwPpJ4gOM-q2mGIzDo8nBR6_FD0WArQXfS-5TzQH7-ObMZI4gypy-PMDeqW_JZt8tS8m92eRciydBkv8GqsnXc8sa1bhYUUATHTgFEQgM-gQ-rEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxewM0iUx1mttOZoYCr6WW7ukm1Z5dy6cW64i6YK6dBtD6gCE275fhsL7GzkdPhcstIaNQj0CoOvvfm4f5ShTqJdZDuOUgF5-Vuff0rV8-usWnVnmz1Ko46Gg9VoPxrQz3qFBy7us6qMKc2ezSWe3y4RIFYg_fWEeGZhY7HnqY_Nk6aPHNYGfrJ4UrnJwPXEGfhHKJGdMxHN3yIV6jU-8pWghlKVK_byKWUmrfPSbND2Z-w9OFoRwH7I6hjyBF4MTzFU-OTV-21YK8JjA7U9cvuAt3PvXeLFYfZrbSacrtbcFamAPlic-UQjFp5L2_HCmp_tNNnOZzefBwTfTIfyyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oybm5_aFyAhpK2_lANmoqkw18lDbIzUkxmJNgqJXZn22HVPs00GiinmFrZ_wiPTD3Uc_PagHUEtapxNXsnZiUP-sLzHSKoa4ZsYDl24WXPp883F9FYLMxQOHLFZVpmpcmbMfmA7wQoZiyDoZdkjGAcOjiaI3ZzkvJ7o9YujUrqRv0Sybs5Mgb3Kn8J9t2RMC5x4zHg3piSMbCzEJ6oR7Or6_txj9Z795bs0gg81d7ja9RYVvLuA2UEumkcwrUftpqoqvQ2Q0WigwTSkg6Tmwp7_bm453KhGla9rgvCCCKoYO-QpiuUd_SetHnqfwGyD5ELYPt2DmxGJXQXx4HrojJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dA2_niAiydzhPYp_kc6_0YihX0Cno65mNAueck75-PzRjodZudrJk5Aka9YT69-azn1Gs0E6iaszBUGbogNGKRJltqaVPyDnfHgtX18-OlDXGD2GO0rqX6zpkovpPTSdUvL-ffVjah4-cPW0f5UW4dAmSb8m4LTmG2D2DOC_QihLzOVjXcrhE9qgUUvzsykZiB6LnH5DGbD_LsW_fXl0t8p2sbtnlIIYm9Lioeeg7gAocM0498Zs2BJA_825sb8oP1ofR1UuojKp-bLTqm-2GsjqnaTCyAHr1V-lMaoW-bIfrYIQtF61KPeAFXScJWwReQKPhsLcKzUcE-l_Md2d4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jv1RX0ADNBJTg47r2nYCvJH-7kajWe8zI-hfRaOFjC4cVTyl27MXTYlGHolTj4z3DGqqJ9DjkLSbIqLCUg5jLBvFgHJaPkYZ34nnnC-WKlNOPxDmx6t4Njs0XgjIbpYPn1IqafKQf1hNhxu0fYUiZcyPrUQd_74gaJ7TehUwarZtgQmoZ9Td3U2Sp8otltDzgIA7YNcONiSOsIC9TIvKztu4lvySd2Xgoo7roiM0V4ujqfCOsYM3aZJzXYuswPUnd7jwJnAYcAHyq2orBq12cuq6X91jYOX3VOh2DOX2-Wi21YPEguIPVwShcLYzckSZk2PXWqL89OwRgfSdOeKYTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gc9HgvEgdlc27IugF22jI4bgy-FV_4e5B618DB0WhPs7wnCx5la4oxVB-gc27bWas-neLihD7EPw0PN9eRiJ6Hb0y-zfeQwyKaQRCNsRYiFyd5Elj-r07CkCbxBaLZI_cnUUW3_l3LHIu-vN_F1rL47NwHt0j-MLhpKySB5ErwIsfA9eYB42VFwGpzk5ChFrLfyC2HtSBxAsfhWjGKosBVLJKH-4nGC6y1fmTqSpTIHVadLFyMTgzWpmOBnINtc_ZwV19gBQI0vFEHAwm5E2jIb5DnseyQt3TN6dfJ8zYMvMMWasLk0GJhoYqbU1smKx8vdYf2mBWXmkhDhQ9ApTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=r1F9D3QiDkxwQo_lLSfguYy9yn-QnNCGLp5DgeC5KvcndKoRTtnNUHJzDMpS8fFOtMWVaxozrWjG_dB6mr_LEntLhGxc9pTYwqpnNzt1jdxd2LEKNOZK3svHY1zvrVrSOgNkco78hgC7PUXu-GlwbAf059qGCwoYTxdbJCPaoOx3W3AdLCF6c1IMmMnGlAjWJMTaq8VWKxHOSeZ_79rony6lywEMIr_fONdUoUy-30bkOnaxfcQwCjP1HscsGXteJZTU8-ZC9oepXdQROyEElFLGtQvWyMnO4g8A4fh8N2Emvj1ieA8YgS3elfBdXRxUw6q23BbFp6lhQekQ7h7YXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=r1F9D3QiDkxwQo_lLSfguYy9yn-QnNCGLp5DgeC5KvcndKoRTtnNUHJzDMpS8fFOtMWVaxozrWjG_dB6mr_LEntLhGxc9pTYwqpnNzt1jdxd2LEKNOZK3svHY1zvrVrSOgNkco78hgC7PUXu-GlwbAf059qGCwoYTxdbJCPaoOx3W3AdLCF6c1IMmMnGlAjWJMTaq8VWKxHOSeZ_79rony6lywEMIr_fONdUoUy-30bkOnaxfcQwCjP1HscsGXteJZTU8-ZC9oepXdQROyEElFLGtQvWyMnO4g8A4fh8N2Emvj1ieA8YgS3elfBdXRxUw6q23BbFp6lhQekQ7h7YXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWp4cT457BLK9s6Cluz-nb7szEsSPib7b0gZdS6-Xx523KZUihVYjKCXAVZ4yUHidPjIzl0gDLuqd8AJpB6oqKx46iNxlV6g-kx5TWyY0YFyBL6DMDDL5DnBt47cqH39CoW_A4fG-dMiR5biNq45x4rNwx4sC2M_UVQ1Q0-w4qZbNHqIcBzo2n_WQa7TLXHESfPpIAkUxHIasp28OjuPwx2zzlv0xXNg9GiRUCgmDPLg3y9sd4A4wXRfGFYz9sLnQU8qTNC81AanLCAsMuriWL1IFu1N-7_euE_8YBIOdNVOLPjXwFNEg4pR45xyU_yQpb9jGJ-it53WKo3oGF-hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhXL9HBEIBJM0_zZ6S8Zxs69qAWHGrMnTHVT1r6msziha4MMbBjDFSBF1FSpeIOF1HGEZTh3MsBRZfZcD8bLOR7ag_3lnbEWNPpAVHcljE52S8mo3Hqe-k_fX2sXbxd4LY0_ZNjQh6b9W7tLeDaX0lJ8GJEi6elzWg2cxtFj0Y4wGrqiGO6g52KAjpdhrNejtzTi9P-iFmZ96b4nHzIEC_uynbjI9mjK5zJuh68Ls_nPic9F30MOAf1VWyoji1N6stQj04WYiDfwQeU16TkTbtiiLpff_lwxtOMI__-NYf4k4j_lnqyYvrOt6_WEZ43AXqMHZXWFHR5u5i8pk_-ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=nsqooaPMx8l3kzmznwk3CbccRilnZVaWRmy8gHCy47gSyLS_BDnwKhUY7fUQYC38W_2qiXVTfGJmj7gS0jiPPOc3nN8rfZGOLg3i4l3rFXaNauT0c56Z7-P51iP5sRTSR_kvBxKBRJpLXznWFWuLOEgOp6FvR9YPyzram4Uxd33xXxuO5mwcI24ROC_rmyBqB0lqxLa4hicjrmnzyqR02NaHMM0d6x_L9k8YOpzHFAsYkzDP-CIk0dSIuMMNI6YelVkagSk-S6uK4Ch24uLRcNop3j4k-5NZZE56YoM8LKUTUKCbO_YEc20X8YPKdHMPIf1X5F_8GemCpo7NIjGNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=nsqooaPMx8l3kzmznwk3CbccRilnZVaWRmy8gHCy47gSyLS_BDnwKhUY7fUQYC38W_2qiXVTfGJmj7gS0jiPPOc3nN8rfZGOLg3i4l3rFXaNauT0c56Z7-P51iP5sRTSR_kvBxKBRJpLXznWFWuLOEgOp6FvR9YPyzram4Uxd33xXxuO5mwcI24ROC_rmyBqB0lqxLa4hicjrmnzyqR02NaHMM0d6x_L9k8YOpzHFAsYkzDP-CIk0dSIuMMNI6YelVkagSk-S6uK4Ch24uLRcNop3j4k-5NZZE56YoM8LKUTUKCbO_YEc20X8YPKdHMPIf1X5F_8GemCpo7NIjGNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkTgsLcrNnGL9KhEl5-OrMJ3eS2lN0lxiyoiCDxVfJMfHIhLrFslMx4p0hUi0f4zwUS6YnG11wR6zBrhAptPztNw9djLCMkxX2Vx3ogBUauP5jlRTlTd3poh_m7AcBst4cSQCDslsRgSIJLYR0pmppAFAFK4f1Sn5gspAUxemHKkcuaJ0jtWe2MNZiX2DG-UgEoROybSaZC8Y39xBcLMYkiRMSjmHlFKXyFs4vSDhv1RcwuMCuLQoh56H0qLPWwF6Y_KXdw4iemq-qDNJ0to8AjNVaRjAgIoRA6dMeplndXXzOJ43qRm9lUL5lWU3mN7UoQCwXbWA-inTYmNYs4yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kmM9b4hsR6wS4BsN616fPY0WcINHxftSSc7iY3YwjOaMAAsA8hL7R416f8Zh7oUGq7O1lx9FV0_tAcEPrRcK9ahlZptHqoFs7gyecDb3IdLyZ_Hje6OeWyuSOHxGRQdyIqR7B1zSg4LqrKwRTNsPUDdTIp2LBua_2V0sPRjC6avUzZ0TXn9p9vf1ZNhwKEPd16Q9TNlD80vLildDQi_7Odi8Y9Vew5Xg-SSK57GreF1EqMqlO0MsgcV0-CSdVQFw58qhhatkNIx7wx4VqSpnsKgUoNOOtBUNtoU1Nti73WB-DDtt-faupP_y1VbLNpGKOzzdG2E9wpKPNHOcZCt3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJurdsyQzW2FgDe_4_emQdXU95Htu6XEm_nmkYYCVgcQmryiX6ZwA_pGqNMPWqW0mFtPmTg6JomaMYprsYMu8dY0UC-z8wdCdVXxDSEyDEaXnBv3A3frr8drCI0qu28qLX6cujy8EADAYrz4KefXTQkAXHJlqE3H2_-DYNdk0Ji1QSjZllPK-p_qK8knfcBqX95vwcBl52WKeeC9ilZRJfO7puwpyeQYwv48LQUgMM9pNeI_BsrPtBc3D95bflP56xJeU5HOyXQH24A_02GDc9PRmIpqWr6Mkx7QK0zlYWqqQIu-nNVWuk9LI3HdY7jisWveHl7P6jcsq2R9vTSztQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPx4NcM8D-a1f2LRCtyGJ4Z5OzqzJNoF0jALPAqa-3zdmS_hljrVjyOE9kygPCRByhzcVM0geMmjSj3sjZDLHuHkDdNx1ateI_DLe2g1J1RLNVJfq5jjLOk0_mm20TpsAH0g6YEJGGLBjHcnAAnMJcvIA4EmG-J-rYxLE5IEBgaMHOAJ7wnEkuouxrvqIbfuXA-n2rPM9Q63lK6_2Rcc9Nf4_NFK-b7KR-aBjARs5TshvWckyenXffCW6IvWYEY7Ui_uPJGItRrc3AuWe3ZXp1LHVa_qw5E2a5g7-HtFafVURGnujLRzPLwjLNdwOZC_uS8zcZx6EGH9rdZ_EthSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WKjYeU2-EEMpq49hGaWHgeMQhxSbJoAxYz8_DESv69joYlznin1XZJMDc5bZ_X9t6JpE1lmk7o5UfpmfNy32F58vCVU9_FQ9JeTQBaLxm7XaSHVhuUJsd_I-kFW4F-sbZbpm8-VDEAdB8Qu4ORUK70JEvgO_O2zHJvpsOjXhfOCqhenxtPNwfgI4QvSNJM8BQx-oDnOf5Pe6W4hGkMVNAj0bOwqc_00uYEbXwZygURes39H-01ES7TRrHb2L0tovYcu9po2dH8u6O3-Ls3swgLguRFDl2zmgGJkhRqoxmtJYYPAOajpjGWldqFiQhc3a4b7pPjhsqbvAg7Q1EJZbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WdoLXGtYCWL3LW54oM6vlN2Ik9HfoT8i4FVamkk6iant13Z6YqRzaI0y_XKe9RZgaKh4_e8HP3_5-79xiRsnwKFoj_ndhCV9mpWbjq0w_sSr8gPBF6Xt32MQ1AAGuSV9A8AQ6ldH9kJHBOmlLWQ7hQ1GlTXLR1CtXNAxropycq4F5ySZyBIp8KoClp_YYU1TiLTaDHEhY5eqmL7-ecI4NfnPJeRd5i8LCMcQDkVILt3Zl8eTQxPn8TJJPeYWcjiGokewdvqxccqC34D617ejr0jmWC1ErwcvLFfMfALl27vFUS_QOlpZKy0R4caMvdEPTOSRrvMWK2JW3E51JpWBMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=JUveC4bSA-0nrzl_LDoDnYUZoheyEiMQCccEicQDjUKaN6ACtraSQYpBy85eByEMdtheSXtr2LJqFNEWu5-ktQhS4ngCSA3j3rGahKh2bHNXju3Kbof7qxvFwvk5qbPf06QYibb7Kr94oBotTIHqzXsHRZddT3gs6u9M1TafJNVIIl6fWj021RewDisBmpLjNqGn0RbMBpr2JeDrmfzGO9n2E_1r_AW3m-eqJ7hEG_sTwVqCqFStlmFELpJn1aEhi9LLN3r1f6uHkgGzJTcbrco6UWeEElNOS5hGhUkBieStV9j2mzp0oNbvQLpNfp_VKqsOTF0m9GxTuNXucHVgMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=JUveC4bSA-0nrzl_LDoDnYUZoheyEiMQCccEicQDjUKaN6ACtraSQYpBy85eByEMdtheSXtr2LJqFNEWu5-ktQhS4ngCSA3j3rGahKh2bHNXju3Kbof7qxvFwvk5qbPf06QYibb7Kr94oBotTIHqzXsHRZddT3gs6u9M1TafJNVIIl6fWj021RewDisBmpLjNqGn0RbMBpr2JeDrmfzGO9n2E_1r_AW3m-eqJ7hEG_sTwVqCqFStlmFELpJn1aEhi9LLN3r1f6uHkgGzJTcbrco6UWeEElNOS5hGhUkBieStV9j2mzp0oNbvQLpNfp_VKqsOTF0m9GxTuNXucHVgMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=jQ7iBvZ-BrO82c1MdQv7o5HyLjGiMny3ouPRAbvmYDXgQhuYNS5zD3BA6V_88TBbvJjRweS4cqCkOx5LHJGCnnZ1KFRXmeG0mNfZnjk_iva-7JmeBEHUj6f8sYK4eqddvB3Ffs2wyXzsibgGtvu2pAEoh3dLo_FABBp35gvdMR2hjzcPA3IMjLl2PFdIKk8K7l_4EqTfP1aQJwoCM2mfSpAS72PGNpfKD-ul6ITLN0vFH1U2zUg5XQfzHoiIQF3aHZfFUPPY1M1rkheUQMgbAZ3Y6ZVoSZB9yW0xGAChEzvekxVzoJcDo_1bKkaUK1GeFtF43OzM4GhXINiWaQ1m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=jQ7iBvZ-BrO82c1MdQv7o5HyLjGiMny3ouPRAbvmYDXgQhuYNS5zD3BA6V_88TBbvJjRweS4cqCkOx5LHJGCnnZ1KFRXmeG0mNfZnjk_iva-7JmeBEHUj6f8sYK4eqddvB3Ffs2wyXzsibgGtvu2pAEoh3dLo_FABBp35gvdMR2hjzcPA3IMjLl2PFdIKk8K7l_4EqTfP1aQJwoCM2mfSpAS72PGNpfKD-ul6ITLN0vFH1U2zUg5XQfzHoiIQF3aHZfFUPPY1M1rkheUQMgbAZ3Y6ZVoSZB9yW0xGAChEzvekxVzoJcDo_1bKkaUK1GeFtF43OzM4GhXINiWaQ1m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3mMjfgzhBk9GBjqDihP6jr-olKMuubNhreA7bqxGvZAHCtkcIwLQfasFf9-R3TwNNG5TkhWWpBnKxOfRi6K-_ljhNh1MSeL3ODLsEJkmVNV2ZH5asZOHlYwZFtWc5zrDtYfns_1eY7sGEF5Ui6BBBrz9fBpIrhwg46b_kQ3fdZ9sBhZ_mYy2CS6lpKxjatWaCPAZMOveMyiMHdBhRpux2PdpXz7_WYCdciRmN5RZ1eETBzhP1IxF2F5VGiwPQ9ZjJYf0_U2iITgq17A4DE3hRpFOZawStyAemnVOm-TwGlctp0FvGp0jz6E_yx9GuDhsmZC1Y4MqwSHKN55CQFQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh928axT8g1irXaQtRjid8QbaqsKQSMrTtcHFo9I3_yNq27ga_qZD6FoGtdntYZfP3yB3AQnlLX630YNWJiCGxVI9vqn5bKdBKVKsQT78tCKpKC0AHDD4YFNK50XeQ3PmyXH7zy2inGB-LJQ3eR2_TFjcTJpuqRNwQYTlMaRH6q48rgyiVmxzlq7JE12xYqhyJGInTBpW-WpDPjTk-uwB174v_X6XyNCCrykpYu2RTkIaWifgrTZRTuYXDSoKQFMU2lioQ8K8xEcHOHevB9Fg5bSm-B9mmAtVBZSftAr_E56QiY4uCyI3de4pA3yYtqdfQj4HaclTkRkT1UQo-kR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZvvmjbZcFmq1_tyOOzb-kp3NuiraRmT_V7OQx7KjOHFmToN2O0XcgoeWQm5nsQYkYyiVtBGSpplK_HAtZWPxlvsHAV0TSpn74eXk8aJSnOw8CLurC4VPB-7qczJFULR0gEfVYpMdYPjEOHV4ON_-N-AUcCqNJx5rqIx0oTinuzK7GIot4If1aZEnN5UyDOld3iYWhMv2mMI5tjMvp2u-H_2zo8yOxnb_2QWDz9HhP2pSxqFaG7keruxN15MqSKYYAuyuBTgIMQYwfvohXszNQ2jyd0oD_bmnKgNlqYwJY1Vmtp-ni48UKZb6gwnQdBAq6kjjadCxN909aK-EJ49LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=LufavVIyAacY2vXHtFH19cMP2Fm2h7OSxYLgDtveaqUObKN_CddCMU5PQ11Y4pXrdxihlH56Ql-Fh7uKkVm8VPdJZjg902BZySpLPjw2IgSSWFtw67ZQYKPNgnHkruOr3eXotlXabGnoOdLCnjs0FZRzXFhw86BKegHpOvMfR1QtTwJYiaTH7gIBqHgy17Qll1icBHZ9DZAPM5WB5__L5yfKFZ7JO-Lir-VKi6E5MQ1I8a4-RyhLkmSLmAWcbXUKiGTiNVCqrtMbgCtXHHBEs9dLaCw0nwtlPvR75XXP9zV8rOUozGnPgOGiOUKuBwhGKjpFNiftgdkndbIflyGYIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=LufavVIyAacY2vXHtFH19cMP2Fm2h7OSxYLgDtveaqUObKN_CddCMU5PQ11Y4pXrdxihlH56Ql-Fh7uKkVm8VPdJZjg902BZySpLPjw2IgSSWFtw67ZQYKPNgnHkruOr3eXotlXabGnoOdLCnjs0FZRzXFhw86BKegHpOvMfR1QtTwJYiaTH7gIBqHgy17Qll1icBHZ9DZAPM5WB5__L5yfKFZ7JO-Lir-VKi6E5MQ1I8a4-RyhLkmSLmAWcbXUKiGTiNVCqrtMbgCtXHHBEs9dLaCw0nwtlPvR75XXP9zV8rOUozGnPgOGiOUKuBwhGKjpFNiftgdkndbIflyGYIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6YNJMJlme_QkH7ISn3L8UuTyttJ0sVhdwBeskiZcj_AqEVJxIoEdOapNdO6p8HY8ZUte__xBLNE7NGS62dflnCvn54goepjAskCD-2bdIZgGAQ3PkLt9tV20oOzK1XVoGkMLZ_NRLA-srtiD-ZNH1LKnuc7ZPMcjRV_9S900DNSo40syK-cfLHqCaU5F1P3ybguZRKVGgYsei2SXVQV4hP-kgpVUqox4OSJyO_SsgRSjuhZrbeYURkUOOZPwQp42JPs0Hn0hzZDipXZ-D5p9FV89Vv9BdUEAI3-OZ65OCiRofXfogWevgM2_Z3U2_WJO1fP6fAofsYlQtJ293ND1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Q9EOvBHHt6TX-qjg-RhzLb6f-2ggm7H_y0raVLAYN1CJbquqlZL-AhjWL2GAp5xXFBZHmQJ6SabiqeFF_1FLj4X29fIbot_e1DX2VINv-z7sn6n8ppbr1UzkMO3KKwSiIomiGSULx60iQ5tHP8UTa-zAvLh5LdxHtnm8IEMF2fOqi1R3FhsaPPuzzT7u9WgGwOFlorrAVik9jHx-4URPmS7Ng-CU80dNTAOuvw0g_b709pVJZrfokuiLm_-nXBcAqxxK76D2hpE533rUXAwbC6zYPr0vo5RXHZuYE0YyH9D_930s6QrYLEussz-J_pCibx8J0Ap7h-N7eJCvI_BOzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=Q9EOvBHHt6TX-qjg-RhzLb6f-2ggm7H_y0raVLAYN1CJbquqlZL-AhjWL2GAp5xXFBZHmQJ6SabiqeFF_1FLj4X29fIbot_e1DX2VINv-z7sn6n8ppbr1UzkMO3KKwSiIomiGSULx60iQ5tHP8UTa-zAvLh5LdxHtnm8IEMF2fOqi1R3FhsaPPuzzT7u9WgGwOFlorrAVik9jHx-4URPmS7Ng-CU80dNTAOuvw0g_b709pVJZrfokuiLm_-nXBcAqxxK76D2hpE533rUXAwbC6zYPr0vo5RXHZuYE0YyH9D_930s6QrYLEussz-J_pCibx8J0Ap7h-N7eJCvI_BOzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPvs7YrMwI7iOdL8G4Xu7jhrm35p-VmO2ZOttUxemuhrMLNTVEbWx0IVZfSNjb-DMbE8ax_DuBw_r6Ks2M3a2E1k-axpeBuoLakHmjtGH8K81NfUmsNLomC9pFrphMQjDyIQR7KTGP3BRK5VVm2EiUA9OLcfuY5TkjOEkYCVr6lD4K-mWGrK5t2G4tUS_17jRAO3pUX07SnCx_z_wILYwcPUsgwY7m0AiIN5xtWmBYAXqPmuKdQI8vJbC_wMg9yY1_h1gapt89D-Me6l9t_y9bWYxGwzqIjgsDpYiKzLdyWCvo-X_AisBvko4TcP7Zz44or6g408aR3pDAdDqavTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KiNW_uE_aZ4deb4BcCTyJmArahwTkzqiSKrUPQbQ-FoviZ-17FmPkpYRJ3icD1oedJG5xm1bk2YgFuj42zulD9WpiV6L7az-p40MdMWf1LF_QMFg4R7JzLiIgd3WPTTXpfWMvVZcM0ZaEXpNOe8F8w3R2SudX0b0chvdkGpmitmU9ET6SQFmMRXL4rVvRV2V-RmbUF0SzUz6Lr5ZGZBez0m2t_2S11ENLd2gVOhALiCIrC-1YnUPVbW-04b7Hug8gvGzGbZEZ4MtHRvDvlX6KWB-3H_19_b8BM_pekEE-yxfm5W1mj0BseApz6OtoyNZ1JJB7DzQDd4laR8H7viyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mxNc-STzbbI9uAOEHkl9KDZOONlE0z3If-EhJLegXNQ_y4Xh5_EbXOYhmSaAx2SwnB-_9oTTylr_l0N9um9RQDSEwjbKqxqxgO8vkoH_Cvy3aQDQQBLl0Ez7rb9nigEJ9KuVKG9FygA-IrJdERoqpF5C92CfnoUGnAPRWd0C1l0CFXAbNJnBijDqHWlz96kEjhvQj061Fc4MuN29rULsLhL1B-sPg60LI1aqrtNU-PBVRvlnsP8M3pO5fCQu8VLofrrNXeT4I1abO49jbJt9JOyVIrTlabODhHJhzLitkoSPXKRvXbMGvEW0fVPtjTXYDPHPsf2pgxgq4y9C6C5vHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhUXEyJ9myWzbAj5G_4jOc3R-ErPDQSUHOX8MUD4YYZyLEJuyrJhMdM7b3ccrzycmH00XInQcLL6qP636RT0XRmYHebz8ka5CMgMZLcZKCw92wdj5zp9pH8tno_Z0aDWxzZSwnhXq8aQK5rq5ueB4OUazyv-HtbPr2kJOKMPmNJqYZf4WXB_0JEMdCSJXTz1mt67MQoRMcInomg0skNv02AsnnO_a7f-KSWdK3HmcKBNlPJYChICTEKTxsObn2G1ITL8lWd0Um-MjQl8MdLdhJgSK9-IqkYfzXHimAOZNilAOUtq01AmwKUNG6mdJvltEPwuDtpgsTqWOY6FnQW0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qVw1wDqkzi1BtJ4i5mrq5lbdNdvgFzeQRIKyCj7BVGTJCan7cjyV8MLE1LYWL_IQAcxaqMZYvIX5mItIDeBsSKT2wbsrjdbfF4wvw5AUDZ0q47nLrBJjvl-Gd_UJRe-p5vWguFWJ-TepDd2JWoaq0DYiHOCdlFLyJg3Xm9TEAb_UZleglAcOcvZX8nfcrbzQ_ZHMckwbRqVFoCZPA924zh9sR0etfNqKJvE9kwKkgu3KBr947RlbSHHCTd-90HwcSDvZnlx95dqWrs7XA-FJYhFWsCdnFSRVjWF53BuLP8-2Q4euhLyuYyRg5tWPiBG386AHB1FV1QQOwSCak8JK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B8Q3hHGizqwy_x97lS9JcfSnz1HW59a99KZ8Gk-v0B_Uv3j3rrbkfotFNjUIIDs2Xga3XbiEZu1pcZuS73wtcjNqb4LsmRJ_v67HVi6akXIZ59hprUmvbCx8tIO2hCJV1ZCNOO_TRFxmJTLCP-VgjSJa_BPPsT_xVXA2bVG3EK6qbBECkhdVfFdnVGEgO_4DlU1EKwlGNP0D_1WXni3Te9ZAWRbl5nc0CBjaklwb2QpBQjQe2VxgSYUi3qSd03-y8H_LVqR-h4e1qKZLJkxUrVEN1CGbNpVr3jP6WqzR6clgJUCA2aCvzQUK3oXQ9AezoZtQ0j-CYqkxVFkg3L7mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUkNeazAVRsq1OO9UvDrmelVpNjeUIL1i1pvUYyIStt5J_dl-B-lGYc032etSslvRzvQrXtCsblp5w-3n2-Kootvog2kYTzcgpgL9j8JfvIk5BLB3Twlk-0xvhLdq8TmcxnBZTwy2w1TUFQhvtX2OPsQuqLXoXTrVI0Lyf6EUIp6YZBYYh-SlT94JyTsG3kJ_hkLAV4Mrlv1IrNtj6viNHF8NKe1x__ukGl9BuQg_bxQm0DBL4cjqodQF_twjcw9I-VeL8FAszAnMbrDoZzhtbZkfAaWYBOmLsErXXwYW9cBDi2YteX3-Cfvy0fFhfb4jDd5bwWVW-peqlDlFA21Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBLyj5UcCN6z2OJizmV-t7YM8HIgdutGkrkTI4cBZaGffLmRcokeTTc7osle-nFa9sKYNmqejVjO6-WuY7y5NFtrrlHkuDI3su8uvQh1y-iCkX6qd7nEMhpSpiMBawc7wjauZ_rVg3h1wGJN441FeSnDawV8SHdLg2cZs0Go7hjInXUBgte0Esq02xaCOrlzI8O2Aa6Xl7QcrUz6vph7UZaiaY69tJjQDn9F8_LcuWT1Xi00H0HU08l9F4rkmvSgKTBfCyJUTz46k2t-NAfb3HdONpcagu7V5vrePxYsNc8_Q7cgNc7TNrbTHvwjdOUb1hR39kxa2ebGiw2xwjxLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=kDwFJCh3yKNNVyfBBujTCbVP7E7Dt0H7hI7GeUV6cAiemEJuv71kDWMwwdCCqt3J2oaBiJK8QtQ8Thn-Q4_DsXzyZQUruumXGI8B8SBvL0Ts9XEFMQ_9XbBi-oJ_FToPogslE8UqvWTrRDgjR-Omelyp9suz3aOVoIJmeXvA7f2CxqtpG1lq1gKeEM_t__jyiByfmP1zZnFP7sk8WJUKDLym6c4F2NVLmAqXerkAZeIa7wF0QAChNHVfbQrdfotZbqb3cf8Ouje40REfciCOC35qjqhBonFx8tHnHsY6xUcddt35_TlQBDjg7B6a7qpxuKiISqyUD5j4F1WXYg1PEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=kDwFJCh3yKNNVyfBBujTCbVP7E7Dt0H7hI7GeUV6cAiemEJuv71kDWMwwdCCqt3J2oaBiJK8QtQ8Thn-Q4_DsXzyZQUruumXGI8B8SBvL0Ts9XEFMQ_9XbBi-oJ_FToPogslE8UqvWTrRDgjR-Omelyp9suz3aOVoIJmeXvA7f2CxqtpG1lq1gKeEM_t__jyiByfmP1zZnFP7sk8WJUKDLym6c4F2NVLmAqXerkAZeIa7wF0QAChNHVfbQrdfotZbqb3cf8Ouje40REfciCOC35qjqhBonFx8tHnHsY6xUcddt35_TlQBDjg7B6a7qpxuKiISqyUD5j4F1WXYg1PEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=gUoyFBdfBFpyizw8B5rPp2zuygoKu6Jtz7j8gzEbyBVLBya--T2YF5wgZ2oyzvitOyY95fbI7-YGaiUJDG-nJi8AZZFUk_ZuFVLhfA7KXmaq5EXhlU-W-nB2-kbdVHo74PrE_8-3M5vwKSQwZxrDsEIl_I5-Oq4zYxNcXt9zGiPIUklXU2IsbcNLQaDPBE2cGxpoaWUuM8oPysA-o1_87DM-1-RAihjfrIT_lGRvRXKpb08V609eMr0N_66nntagh2ibI67nQiJc5SCIyNffdLH3PCxw0ZtktJJR6BKyHZNMiZs6794lWYRUhvYWhR0fIz4Yzor2x4NbDUzv2xbKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=gUoyFBdfBFpyizw8B5rPp2zuygoKu6Jtz7j8gzEbyBVLBya--T2YF5wgZ2oyzvitOyY95fbI7-YGaiUJDG-nJi8AZZFUk_ZuFVLhfA7KXmaq5EXhlU-W-nB2-kbdVHo74PrE_8-3M5vwKSQwZxrDsEIl_I5-Oq4zYxNcXt9zGiPIUklXU2IsbcNLQaDPBE2cGxpoaWUuM8oPysA-o1_87DM-1-RAihjfrIT_lGRvRXKpb08V609eMr0N_66nntagh2ibI67nQiJc5SCIyNffdLH3PCxw0ZtktJJR6BKyHZNMiZs6794lWYRUhvYWhR0fIz4Yzor2x4NbDUzv2xbKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqXAf4OZuSKYiIcMNkfj51V5uGZqZleDmSSIykPSVV7uissuIzEal6pHmOm8X7E9eIn24zULtxcrvteRGrX46P2vDI_mwgLp41wTwpgdewcmH_ZMtfKYGB9XDnxZ90W3QsFnv3ZH7jWU6Y3x7fc8__ijlci_PTrDPwsLEB283xUiZTn5Q9YMHuVaxYElJlfs1SPylCPEmumFs3syPlQJqghOWcfrsd-Nh-i1HRJWN3r7xuakPDZXoe9Ppf3qcCQaYQx40RxJ7qgQ5Lln9P17xPhYy9uFzne5oQJzpIRSzGqAkXgQWFreQNiDIUPplpr2wzi5K4e_tsyN60Qu0Z0b5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1m9rsHS2clrUmHnCYHP1OuKB1EmG34dBbTZorEGTpcp9FfEDih2r4IKII0NJaaoZgHGBSyU4HXHuVXhwN1aZsKKOB8ogaD0w7FhAPOZU-As1Lpi3GOZqyFBp6a4N5pCgsnbhOCe9G8vgFbmgh9UhvcLpoSKIy-eiE_TbLJn6WkVs28o2-yr2YoekNoXwm-4rgnvZp6_KpderleCTCPcxHaa3zLjyD1xwcPTzTDrFnjOyKd0t_XQCtFMBC_gGqoQ88HxBpztA-cP1v24ByjEXqzEdBif1wbDGXRgpcesObndYuX6yKzFxU4ZXL4qYsTPAgDZN2PxGHu_gAj3qD52bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzoeeDXbvWoOCXrwFEBkj_llvJX5Fg395Sjr1LWxpyMHzTEOWAsxqg5cPlv8Pda_CenQl9jPrPAorAjBiYqzaJfxDcfmL_Dh-kv03J54-ZxXc3m4f63o-oRWYoEFOUhPa_eoI-fu_JR1OHs4W3b3wV81vDS7nnmZ07IdzWLSqEnZBV6AvHtOZvysromgBqq4MJALSaCiGlxFg22oFH-D_yfXcnsoGafqa44UBDFf_Gj1jVKGO9Ul9qk3wtwCNhRDMqF3Q6PQznQJ5l4mBh-ltTn4Obku9969DTgusAXqMCoHLX7s7f0pEiMEq23XItDibYSgekiiHOMgkQr3mU4CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=lRPpcl2jJOU-S9k1XQt9txoUQUinLozWYI3ui6TImGZAyT2lOYabBYHGOoAYRrn4urYftIXwUvBc7RrC0T65v0gTJqC4fwFg3JpWKkO1ZjAntHdlXCWbxaquV-1UHKfaBENuW17i5GvwRrbcn7C6sLwS28MLoC5Xv7qsBUuYaVeeZwpUyFDVMuFrfDUWDqrMm6FxsfEzqUc2wzX_6Rx2sPoH55X1JbPNuzlxfW6JJXwU5gqpYhVvHE7EwA9FTn2JRSNO3vEc8tGoZWYSShAkJ8JPqr9hIE7QEwDOo4baFRwXUFX_Jjvc5P1_bY33OOcZcjfsidmX6lfk-UdbCejvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=lRPpcl2jJOU-S9k1XQt9txoUQUinLozWYI3ui6TImGZAyT2lOYabBYHGOoAYRrn4urYftIXwUvBc7RrC0T65v0gTJqC4fwFg3JpWKkO1ZjAntHdlXCWbxaquV-1UHKfaBENuW17i5GvwRrbcn7C6sLwS28MLoC5Xv7qsBUuYaVeeZwpUyFDVMuFrfDUWDqrMm6FxsfEzqUc2wzX_6Rx2sPoH55X1JbPNuzlxfW6JJXwU5gqpYhVvHE7EwA9FTn2JRSNO3vEc8tGoZWYSShAkJ8JPqr9hIE7QEwDOo4baFRwXUFX_Jjvc5P1_bY33OOcZcjfsidmX6lfk-UdbCejvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqoZt_qg5E01UuwQFT5KyN0EXO2Moc26aO5PkHnc3TfqeBZpZTukxE9Hc9RNKmwFnG8U1mZx2f8u0lwA83Fh80bPH5Lk3R-aS4ET5sfdrfqVvV2w6Wyhkw8fcwNh6GeDRV2qFlQ-0QmW9-37LNrewkQAy9HQ6IyqXHG6WYcP-LGz9ak-43hgYiJgJAwi93UFwCU9kju6IeolBxpY5x3A1NlvjyUvSQv4hATPN_8dfSllDJKPdkgVMvXAhw9mR5UxQbjKMEKSOUYyF4JqLyhp0hTLN2YXk_zWt8hR4qd92OWdcV_muDfqk2k1pJzNV880uZX6LGmdup9R8LwafylTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF_t59ddxDCXLv51o4a51mHIwZ1TIghZC373Z33Mz7fCt-AFmG9WVpbde54IlD97yBslmSZb75Q1i2FKk_slxeLiRi2gRJaQZpIFsMRo4_Ahy9qd2d3nJVhnQvsFQzuuPnLlNEKpvXN6yUFD6foZXSiSN1zWCdpXKYRKxdgyx3BG1FPb8M95wRZJPvo9pDqmoJY-u14a3DitdhZX6Q1StEoU7-mrNC4Oy9IEkGXOkGIYkiT1qeMVGzntofQh2A6Z8C3lG2NIB_xQkZssEwzREoPAVVvHLnpRDLgwiyY1S-QkshgKNAKgf4XXn2k6k8ZYSDLKF06MAw6yOnZOM3n2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRgKJFdtMR2WFTSQYf-v33f33i3UOBahfU3ZrcJh3LaDlSz1rGELWglXXivEWQBdKTXKqcyFg0NQz5QBWsijgi7vkWdfTL5K7LJkjQZ49W43SKI65rvVoeQiz9luE_jAQSaIodtaeQu85t1EyZTV04229n875hhKzJE6BGubNt7oKrUICJDXo28iV_WjArA2wXa8SxG32Y4iXU3hKwuAY1PZ1U9_LwtvckIv765W9cBQQz3ceLaGLN7ujCZqDQEDJzzGiJkDhW353o1n_E_O9Ia15EBfcwqK9rG9PYwXBUEl12ZzK65mnZ2nBzV4Fsdantnj3R9JzS1-ztSQQqOXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=T19-ny_aIEA6uZq6lx1vXIMmDsUHGjrD7aysHFqShbFoBwLujAqJkC22WYNKZEHeBDo9utLJvKmClyVFOdrmVUeVON3y2xcFT8rGFoXK94XEvM2Sjp1AFMGd_kIzx2LDhp0iIfttlLWUa513ZbL8mkrsUHTZ_T2isPPzd04QpShI0DxIqxTkU2DoC4ufwo1jNJPyAgMZcTVpaBAiYSuSGIaKhXmAHax-Z8_NDw4kkv5iAH8zUTj8Wzd5kV-fs623UzcwsPXrLyNNBckPt7KvGlhmVwYWyoLvx9GkaGg2NUub64RDs-S45dGKl3VEWQxeLsSek8JO8j25XalUBNwegQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=T19-ny_aIEA6uZq6lx1vXIMmDsUHGjrD7aysHFqShbFoBwLujAqJkC22WYNKZEHeBDo9utLJvKmClyVFOdrmVUeVON3y2xcFT8rGFoXK94XEvM2Sjp1AFMGd_kIzx2LDhp0iIfttlLWUa513ZbL8mkrsUHTZ_T2isPPzd04QpShI0DxIqxTkU2DoC4ufwo1jNJPyAgMZcTVpaBAiYSuSGIaKhXmAHax-Z8_NDw4kkv5iAH8zUTj8Wzd5kV-fs623UzcwsPXrLyNNBckPt7KvGlhmVwYWyoLvx9GkaGg2NUub64RDs-S45dGKl3VEWQxeLsSek8JO8j25XalUBNwegQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6FZfduQE4B4qUKJke6457ZFLxoLxXEYgy3lRtA__bXs3sCgNMb3vOCwGJCQJsw5KWDDqIfOyYn7-7ekIk703qsGEvT_DqbktjsFo3hOXXXugGEtSv8Mpmi-fFIhnDumKPv2jSXayGjQIHYNRfnGWUmKzxwwnw37G3kEEDlBOHow_tt3VZSnmGazM1Rc55iEVPCW3fwwPXnSpZ_-M6Jk5tPhXtw2EI6elcyFt0JyFujNraLnOnNpkAtiCIBCa-efpdbCGx5GzHO8ADmuw0Vcgu6gjW_DPDKIt0h7vw5CLyFxuuIZL1Uz8ocvmVCW_jepYvIuWAm9K0-pyqcRqMCIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=Le8nbTWJs74NceCED6p3sxiT5s_Pi6p5L4GbPwea3WRkGyliT60ubr5JAcQdDcuWIsWwgkOBLif6wxriqygHq6JxXLioBvw6WPgyAcGACnJ9UCIevW9OqaqVCaR1Gr1XDQYnMLV5oTbldj-Wzx9WiJn1OmbCVq1-Chd1kJqlXuHIs8YkZlw-RsLdT6lgLLywgEsTTSTMgrPB0XzPH97DuL2YJ4slfiGIvOH86cib9kPyuNmkc2Bmojm4n4_tdndGPuWud_cifkW3pTQYrQ4AnDhjw__51ILHhE4ocae_h56UYOGkKOuAmSkKWgRVSSVRaxyU9PIoakzALKbebZ-Csw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=Le8nbTWJs74NceCED6p3sxiT5s_Pi6p5L4GbPwea3WRkGyliT60ubr5JAcQdDcuWIsWwgkOBLif6wxriqygHq6JxXLioBvw6WPgyAcGACnJ9UCIevW9OqaqVCaR1Gr1XDQYnMLV5oTbldj-Wzx9WiJn1OmbCVq1-Chd1kJqlXuHIs8YkZlw-RsLdT6lgLLywgEsTTSTMgrPB0XzPH97DuL2YJ4slfiGIvOH86cib9kPyuNmkc2Bmojm4n4_tdndGPuWud_cifkW3pTQYrQ4AnDhjw__51ILHhE4ocae_h56UYOGkKOuAmSkKWgRVSSVRaxyU9PIoakzALKbebZ-Csw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IC6Tqnjp3aODrQu7UDugRAPwsfkTt4SLQvD-q-ctokQdAk7DH6s22dCRnUd_2KBOg38CsLVS1FIGb273wt1hB4qWB0rsxGrsSZJQcLRNePVOiHzNWd7D9qDCxR8G_VTIGFAvZBJBBFTWQ9elCjNmxR7MMjSmmWBffN4uwZbFuXJHAXJ2_yWtXPz0lTA2Vy-8dBSJyl1F7CAct2cky2CVgHssKMMduxUSEXk-zPpfUtmvaWapL4UDbl7v_inMv5a9RDQ1b5e-korgnHB0GvaK5m5oQLq6zuf9vPqJeyphbw4K_-U2D2PflzlFBhdo6qRNx2olVH0WydcPKO7snNn1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMcACmmx3kRQVRryDUYYLMxj8GjR418GKGyH1jsEChPvbpI-8ZQdEMTdhXVGHvaC-XJE7AUmhdxBLHPz_UbpIMMqwqBx6OljP4k-9eEYly0WlIKwNdoIfLuEAnSJ0EF8dLY4p0P-8dxL9lI5y4R73kfbKJIZx83yd_ymAsrZhfkYuefH7jgKuLQIIpKVJO2Yu5_mCpUjPW7Ym0q--f9lQ2EWqU8oamWOH62k7gQgR_tuofGdNBSi46o_KOHi82Gd-4QwEwgxSHTjpwAxxvUS8I2_V3uT8arTMBTMpF9hpAo5E6D4JWhwXHh8DnIrXuYpWb4wje5HnrYHGASmq9nPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9gnK75cMbQ65VBxMyoSioAuBGIVgItLYkOZwFuQwNaiwA9lNoAbFXoQuuBEM0ygKC4n7a78sE3XC874G98xOUXrlLzN6GUDKDW_S_yxgALcJ65WoumlrEyYetQdTlxDxM_4JL3ZDlAqHmLcck2jJkUr8fYZk2_uS3TApSxMkKRjTrnn-CjvQiF2nMHuJ3R8Dg0LVzH0nfwlNAwwFGoGQoI6ZX58ADEZ1Oeqak1Q2t1V7oVe5p6Jfflgyo0d_BXgMPCwvgqWcojxA9TQFq6FtKx8iDSj1jmq6Tm19yU0nHkF5LnODmkZ1g2TagUyjnssWvcYZtaN6KRRN0iZCwljnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MATtVoWRvqdOGuDDqQCYGvW4MZoGAIHMEaDdaSF5UlRekZh6aO8Baz8afbB0frgwRDGBMy73B-h6pOBg9CQU6l8s_8Hj7US1VFQGrpK3iS9H-edpqpgQY7zl_0FSBZ7x0q0kv6RaUjTkpiI0kdeqvsOZ3v3A1BozDJeyj8b7hZ-_1PaFnAylX7M5fPEeyEuQF9vmJUHL9RlPBFvg26t3VMj5MMEvHcC4V0u3mf5pWDYbNMr47LJY-jlpMDMA2kM3VDSBAZ9PPsBQugT32miuNg-HMGB3Nid2lpdaF1dNJfSnhcmNYilbe-rrIb3qFgGNikpmZdzjM97tps1eyzv9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a8adZQlgxx0hDEYcdhzi9sJdFTVNV4iSXlxM2nPEKPZsBt-BP8115SEi5nxOD6_GHm8FzzkElsneTDzjCswL_ue_WhwtUEe045d8dftAZQ8vDWm1pSLuzgJfX1HYyPDuwJNY8dyx2d0KDDF0SGdWG_FXVTSievQ3O5mN-FuWdHSSjNadb-sxC3xZGkF7ua9hDDQMpcSiGT8IPDGXV-4uOBhrrnZgypBbZs9CxbgdK83t5UCv16-u9oj7u1R6gF7K3-OeEBhlq334kXpZ0DiGJsyCeakF3ySUlycLABMvuIHh3Bgwu5StDszWS6KGuhgm2It9Bz8ru5xjLxHoc1laQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NG2fUL2oBk6SWcqlUQV45iJDdFt2HzOsLyqiU91OrHqvwWO7RpmCJLkl-LpFPYYc5eNpyvJU9KXUjrzke83IQO8OhXVHOQt7181nxtNqC84NxBkW2D0-s_GQ_9v4Xu6gEdasxgpRoQg4E0lol90x19dYFHTz1kj50XUB_pquucLsgVgpp5sj8Yc2j6BvwKy0zIq7pNjthdrSdd5XvSXDPhWY7ZXiW9TiUQNEHfE7nPunF1ctkIhOsTVRexQbhOgkAdJL_cb18Nv4Yk9oqlv-BEhE98Lm9CUTd6dscum78dih9xiGcEIp5dqKYdLbvTgUlmOeKjPirKE4K860dzTrFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O7Dm3bG21gazA0_6AaTZ8jmSMBiuL5ab1rndiY52CBVGaqCSoYZz4-rjhqS-m49tdWydKF_N1AX61zzjl7MAr1hnl-ldFKntaHnpJW43Qn9QwPxYRCFJb8d0ljbfEpVJ0s4ND6m8hrQPe3aD90uxNRfjiBpkCH02o60P5Pg1xHEXNEQA_L9o8RtTK90Z59sHEju8zrtfRKINkkXaj3wEmZOLfw0Guv7V0r89MygurCiWyCI99fbCiqX30Lno3jsPhx1ob3HFgkS0FwJJFdwk5mEsvI5dE_-Ien2cJk3bhSLQCZfixqp3k2DmcBRU_O6gbxoCVqbYJsfURvtJnkEfKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oqw4lN_O6UOdnJdvB9N9ua58TiJ0KckdXGe0ETAonHybb6EkgjW-bldrBmiOCYjeiMUEFnrvPknyRRMuJBcurCwuD4zdI7udf-SVJKc2CXSVCE30lUJfkofAt6geiXieVejxBHbcm3RTVlZAt3MfK4VQpxlArR_JU1DBE1kZokXFvBYlmGdu7wA2ZI8PdQe75bNZG4QPLEJtPKS9UCZXEODIeDly6j2d98b82csPMFYkYydSbPJdda794U7_7-sa0A3ABn-I36PwPF_xHKa3l24gqpv2cQujHAaPNFePSMvPRcXbgWEpCG7dTwwt6JYd9wRuKZGHuC7CGoXI86iocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcPldkt7JI5k5K_k6Wrsm4E01zZDaBvpcjGIFPaV2brp-3Z7VN05zJN-Djxk6xNO_v55r_qOIGYYM0PXUigZ-yZilU8CiqWHj52UZMCSoMef34OYL-0HpQQcRpo3x4ZhQ7V3iHonVWzyJ0tQJ-p4CiSgWwdQIn2fnvdf_pGc-bHvm0HdwUuJnIYLBndAtow3NVT0Zk94yIyoCjtgo3os6P6Jn_xywMPHFxJxJafJNUFec-RPtAE3jpCy2QS3NIdKNeEZHr0CFPWBHryt0UlKymwzZ7DHdyiZbv7Um8GY37IwH0Ow8bokVr1SbrjX00v-njfcWXDThfGgjA_FSCdDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMfacgk6f1ENlkf1dYARTggmLm96eCxlBcef28DwzoH-WOPqdHQF5jBY_ec_hfHr-xpuxyjapGIhsi9WPrda6L3xa0PxB0dwsK5EfA3fVykdIS-aJjUR8KYG6jA8aDkI0xo6lHW2QZR0tgtgRzyK1-OZheSAZZpxltVTMZ3xy7lfXjtSIsYLSKcrqFjefQbP-No5n5Wju4BIJwg8_8IZwuEodIabq_1yrFYupTqvFbbd8UOD9eGtdCx83FI84XI5PttNaaQjeXYkCELLMBsQGmBtAFuxeUFDgQ9n7CtRdx_UvwHE4j9uqzdOqrWBogiYXzxCPzyIms2JDwLITLoiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=aidQWvIuizInwg0S3X9BMmx5WU81oF1aYyP5ttJrfGUs8h3V3RfafY59WNZij7vz56IVU2I6TCbGNFGMeBUC9ZIx6REUNtbNAp5myuT6Dv0amYUrpcb_6pKKLuIrbDExQd8cvP4lKY40BAiFISLiXxXbqXHqNFXO2dL0YYhtKvjxCeR9vwKSNTVP5i7uUmSS6HHrcr-wMRMdnmMGHklynhlpJ-lf-I18vGsemA43O80EqSYcwembDnEJBwju_KvJ_5vpB2xKNW3P3DjwwicpK4xwnGoLZHVnpLbP7bhBofafJcSgM_E_xa1GlvLg7HNFpfEsp09Mwvi4zZxC51mnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=aidQWvIuizInwg0S3X9BMmx5WU81oF1aYyP5ttJrfGUs8h3V3RfafY59WNZij7vz56IVU2I6TCbGNFGMeBUC9ZIx6REUNtbNAp5myuT6Dv0amYUrpcb_6pKKLuIrbDExQd8cvP4lKY40BAiFISLiXxXbqXHqNFXO2dL0YYhtKvjxCeR9vwKSNTVP5i7uUmSS6HHrcr-wMRMdnmMGHklynhlpJ-lf-I18vGsemA43O80EqSYcwembDnEJBwju_KvJ_5vpB2xKNW3P3DjwwicpK4xwnGoLZHVnpLbP7bhBofafJcSgM_E_xa1GlvLg7HNFpfEsp09Mwvi4zZxC51mnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juTzcG_12p1TgL0Vh-wbYLnxeghf9Bi8_2xZyozQgfL0O6Izmn-17G8f86XylMp5POdiTLwn_u1svnLDJ938dgRosQx_nr3l4Sh58gOWa_iTF1Ub3lfJikG_pctyHoe9B0ghV-bimRB8RuEM-uUaVuQRYczPbOcq5O1CKXHKMxzvcPRz5_Gilby2zaY7jWZGIxbM6g_q-4fE2fTQNGKIiSDRMVBwJ6dNJt-bE6k_ynCrhEq0yCC081UcCEucJ2AIM8mzlr0nvdygaB5qh1eaiNx8F45avHPvUmXlztXnD83gJyqBVqwWztGjnaV8H5Jmd4_ysQLN7flFcpV4uRMYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NChTdM6ntPPsz0CW06JCNyqxZkcTEVhdKN2eN_GCOz21pxct6KmWpF668NcxiarhfYhSbriit6ENqzItPoNzoxGzvf06s5THEJ0k10JJh8nZpxIzUyZSXMondMlqBUA928Epc0SxFhmCWsNYJA3US5a-kJ7qznmsqY6AprhxYbDklqfUaE3vTTnytZ91y3jo7VLQQyPwzDvY18nmU9-dswyD4M5amsdUsAnOtaksxs7xG85OHeudf07BjzdytTr3bejd6rCo-cgy8RvKDvI5bJhx59N8Jf6pbeA-qtwYOok-eZqYc3Uf2Mbzzsk5HC4DLo7N6oDwxoOXKAnb0RCnsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
