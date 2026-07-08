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
<img src="https://cdn4.telesco.pe/file/jlemP-NkJMeld-NrjcZ2hpCIXiVA0hYpupmLE_Ekvk2_dDYlNKEQ4hfwXNm4p6PGp45AG6stlAOY6Efg3HXkMLXdmbrJPsK5DoQjYwpDpkisPttTCCeBq8PxVxhhUqCXUUKc9zkglhruVM3N9gq8UZPHaeuNFs8VjPAJOeR-NDU0GYt4x_qX_GixzgbEOq2bTMjDaGnzL9TAfQAuZ-xF5QtLHiaLRYkaccLJcSDIOokOBlDDkUvL2vQPMzaVaxFmeBk8WEmimr3o2IlXc9pPPGu1XEX6kKiPbdJwpowFy3kUOWVJfobTFW0hA0Wx2oWeMRYo02kLJo5M0wlEiUN83w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 197K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-79707">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbb43a3fb.mp4?token=iB88aTsaOfAciY4vYFl_HR19USb02B5w9TcKnbObHYbAI3o_sErHvRYdOav9a_GaC0jz-evIDc_BPAuJE0JFpQXSKlcKD4XbNqjSiaTrvNz8Zlj1ebFjeg0vQoLGKX6PBXYBHH4sa1cia_08pfTDKWQaFfmwVJptXKPQ0dNN4wyVkeJF5dUYuGcaqV_qwoFYlZTOyq-L6VXMR_rHoiQxPc-niGB0750J9envPgT5sDISSleKYu7Rn2q1kdFv6O6yruHzR9uKUV8HcyuuP9feZQx9szxIb6KyQLvwPAjyRKZksVmSUQJUrqhrg_qTSqTXsMi2dty1I4B6m2wpCdgFNzBd9E8AutVjM7kheKX_7PBT1GSC_HG7huRJcpRul0uOGcowDMTPnchvqOkA7xtm_TWq1OZoDUUjEy3yp99OlUtw_ATTqcX0m7dNEfTZfKE9D8Z9J1XK-Yo1IHNI7DP3q2yH4zfQOdd41u8Z9KjR0Ax2XqsF7gv0Tzd_uVXvA3GKhqCZy0Dc9fXMzqAX___oOyNwcJ63e3TQNQYxjGBvFSzvldk9NPx_hhqAC6RT6Fc6NsydvJqGtvfBCGT6kKpIrA55dBz977cu9TnZRkXrDqXAylpl8orBR35ZE22bNDCIqVVpWoWhFpWGu8X8hrl6Z8evl7WvwdIKoeBddfhIw80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbb43a3fb.mp4?token=iB88aTsaOfAciY4vYFl_HR19USb02B5w9TcKnbObHYbAI3o_sErHvRYdOav9a_GaC0jz-evIDc_BPAuJE0JFpQXSKlcKD4XbNqjSiaTrvNz8Zlj1ebFjeg0vQoLGKX6PBXYBHH4sa1cia_08pfTDKWQaFfmwVJptXKPQ0dNN4wyVkeJF5dUYuGcaqV_qwoFYlZTOyq-L6VXMR_rHoiQxPc-niGB0750J9envPgT5sDISSleKYu7Rn2q1kdFv6O6yruHzR9uKUV8HcyuuP9feZQx9szxIb6KyQLvwPAjyRKZksVmSUQJUrqhrg_qTSqTXsMi2dty1I4B6m2wpCdgFNzBd9E8AutVjM7kheKX_7PBT1GSC_HG7huRJcpRul0uOGcowDMTPnchvqOkA7xtm_TWq1OZoDUUjEy3yp99OlUtw_ATTqcX0m7dNEfTZfKE9D8Z9J1XK-Yo1IHNI7DP3q2yH4zfQOdd41u8Z9KjR0Ax2XqsF7gv0Tzd_uVXvA3GKhqCZy0Dc9fXMzqAX___oOyNwcJ63e3TQNQYxjGBvFSzvldk9NPx_hhqAC6RT6Fc6NsydvJqGtvfBCGT6kKpIrA55dBz977cu9TnZRkXrDqXAylpl8orBR35ZE22bNDCIqVVpWoWhFpWGu8X8hrl6Z8evl7WvwdIKoeBddfhIw80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/funhiphop/79707" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79706">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3gUgacTuCrUPuwAvt75hfjbeJNNK2kTQtLmKH9EYJJRrF7zGiRXOuc8PW0aAbxF_l_G7nk5KTamyEWbxChiZlVhpHIwvmI5k8mto5RdCYsn6dmvrxBBPdH8bKtk3rwOciHzZU3-3zdAOQ3EjTR0OzBUy4dt2oj09HBBGg0EQgdSPUgXvRIJXHG32vnXJ8CfDyISlpFWZv87TzGZirHQ8z0DRNW3bymb0AU_q-r4_vw1Frt-OJgoDf5ckvrGVCLYAWVLZ4wfbvcIKXw1ke3OPn3JV-kGR8sOanfwz8_f8V6YjclQ7ZCkefRiToeGMuWPJmb0Qg5bIizkyYUm0gRRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتما باید مثل نیمار چارتا حرکت نمایشی میزد که یکمم به این توجه کنید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/79706" target="_blank">📅 14:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ بزودی، به درخواست یانگ آرش ادمین محترم فان هیپ هاپ آتش بس را دوباره برقرار میکنیم و فرصتی دیگر به افراد باهوش در ایران میدهیم.
از توجه شما به این مطالب متشکرم.
پرزیدنت دونالد مادر جی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/79705" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79704">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دسخوش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/79704" target="_blank">📅 14:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvx5TpNr_tn91-xJKmO4T5wib8Fh4tVjw2kU-joHJpcbPbPn3AEsPUadT3IPKia0HeJp_0efgTgn1ZquoDALg2p7GtQy95WVCs-i8LGM1uD9IXwpDz1CzDxGSd0Gi6SlTf9hb4LZa6krSO54Pi8Lkb1OZ42srqhR8eY-RS92MastLhHqvirMucowrPHhSCZAPxO2zYkcRrj45JkxhudbJ5qJHue6UaHrsLtXPXSt8geaPzWHiCRDEEwCaf-o7ChzlZmGRaq2vK9BwbIqfRk-TmfWJo8UaubZfOgt1AHh55zi9XcD5w768ZtXMwFEOb-1nDiBm11kflxcxl4UciJsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/79703" target="_blank">📅 14:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O83PNc2PIVJDi-kDOygEDVe-BCvixB5hNJxV_9tD9JGh7TRcefNlRkohuiiN66tofqOb9mzPi_-RlcLP9IYLMQH0kK4PwtgCtOb5hjSWfml5yAW7KimJ8NRdvAP2Cde8MHcHdlvRMz6ecHw9dYEBFH52a_d5RD7G5NMpY0jRgucUU1UPwK4iMnkmwkMNIBUQuA77oYen44MnziB58fQwKq0tLBH-sX1Z_SKkGNRFAt9Fl06Ac53ML90Sp6Dwcce8vYJJXKpKkq3jaXOlJ-Z5vJlF1Fybj7LK96auYQCPBwoBAJaMg9cx08tJDdydVEFPZgfY5BBRjsaZwsaFO9PkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب ساعت ۴ صب وقتی شما داشتید اخبار میخوندید من داشتم این شاهکار رو میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/79702" target="_blank">📅 13:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79700">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBveTpZGdZfVE4NrNAmYEzD0pG7kqUdxk5FIbZP9-Cu7I2G6yNeaF5JJ0Vqy8IRWDMI0Dl4GOFNYJjWdVIpG2JzAvq2FDNqj_pMTRn1ReCKj-D6MK4zu5fd-drngZJG9SsNQObdG4zqPve3Ts81D5ZApwUOpGQFLe63sOdE-KqAW8PLnHeEdp5ck5L76VvuKhI1kHEELUS_L257OIzRJ7ZRMDA8ScaXEPOVOAm4BB8w5dOvRBJ8yEYMsShr9qADR2ySXXn4v5zcch6F1gBR2j2T1raIVZZh-KdAxVyHs_rjKEnV8d1YSBM-c-M1c5WWAlRlXNStVKYSP5YMXiE-zGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدمممممم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79700" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79698">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb4956b2d.mp4?token=tyZkCxYB-LpoORRXe7vVwgC-pLwmm5lC-Xd-ktZKgpPTGy9bs9hpsuxQMUXVySeSRTCskh15tni0joBlFUeeKRtCG1NnDxHmeBx9FxXCbt1lbfc2EzjxGtHmEtw-wK8PSSe0GQzQJ4LkRTyeRTaLnxNvqUQtZv_W4GY6WnaYTtP27qh-e_AtgWm_ewl0QXVdJlunebACwoPPi7AHCHwJNcYM7F05uCssxAidONjioQNz2aIt7CrxAMHRaydYw3Ry-cpIUP8TbuHH4TdXHTlDoe16Rp_U3wbibpPouwf-VT0jZ9NrbH296N7YJzxfuBeWsuH4hsNfrzT5DVjyDv3AOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb4956b2d.mp4?token=tyZkCxYB-LpoORRXe7vVwgC-pLwmm5lC-Xd-ktZKgpPTGy9bs9hpsuxQMUXVySeSRTCskh15tni0joBlFUeeKRtCG1NnDxHmeBx9FxXCbt1lbfc2EzjxGtHmEtw-wK8PSSe0GQzQJ4LkRTyeRTaLnxNvqUQtZv_W4GY6WnaYTtP27qh-e_AtgWm_ewl0QXVdJlunebACwoPPi7AHCHwJNcYM7F05uCssxAidONjioQNz2aIt7CrxAMHRaydYw3Ry-cpIUP8TbuHH4TdXHTlDoe16Rp_U3wbibpPouwf-VT0jZ9NrbH296N7YJzxfuBeWsuH4hsNfrzT5DVjyDv3AOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
آتش بس با ایران به نظرم تموم شده!
دیگه هم هیچ علاقه‌ای ندارم باهاشون سر و کار داشته باشم؛ اونا کثافت، مریض، خشن و وحشی هستن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79698" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79697">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ2EIzrRM_22VYCsqq7mfIdyixi2OWQIwmJUdeE37jV824t6U02t7TviImPxLkZC9qL99uIzrLh8YhxkqKcvZRSRRyC9p1R6iLNmTEThzEGCUvRNW42FnBkM65LTnrZ4MFevBoWj3wbLidLCE4N4387-lURiMw7OO1fk484wYymmMV_NSopTe5rTlSticnqmXf8sxPOKi1aViyTEY7RNzHPkxaBSDlc9oQUXT9KvE4B6HiYlxhRIIlNm4c6afhNggW16mAhR6uxeIxDzyHK4Ysv517CQZ_6OcmEd--cxy3Zz4boTgNDu-C6FK3Yww3LDxg9xijlR4PnMUAbqo67PMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف شد واقعا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79697" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79696">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxl6s_yHGA8Jgnc1rTaok8DDXPlXOLCUTMNruq7H3rdk65NBKZiT2tEjx0_v85V2pJDh4ngzhdkuItYmUjWtvgCOWUaLePdxhEjc8UKsthqhPHk-wFx0SegytLtVGEMNm-rW2x3Omlr9ISS8MqCKgDaUZV5SfR5KATqQXo5jNuFivCfnxo2ZzGhhkRaOh1LcZ1M6aSJk4iY_pcH-Rw0k1Ek_1W0UiVZeOWmNJGAaYJqLYHd4XXbPm8ILcbVpox402ccdvMEK99CIKpM1Rmek5UfgrolGgqUzHuM52-fHRJ0JuoWqS2a6HhKZLUPOaVYJJgbo-7a3MXGd_caJCLhgz0Jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ccec9119.mp4?token=DK_QDY8JXhPjlHp7UsP8gyQROceZWoQwDvyin8HaNKvwZOzdwGh78yLwc4YZbHVO6gbtYb4RBljp6FyrQAXBH1rcmRahAMy8ukeh5Bs7fuTl1nsGYi0SbM5e4707-FpY59ATr4Gl1sKaCYfejor8p1UpX-XO_aV9f1HH6VWKbmeWNXmdR7B_KNqUs4nPKWGT8bQRmi9v0ipXrJRP_EYwtUEgpYxoZN0x907TekG-oEj2anPRBVgNWw1N4j1MO8E7zZtf9JWoqTeOZ-XMNQTrvtj8tMpWgGjghE8Gji5J8S3ZUE9MZk9x9euOZ6WMeK2YVZUp9ABN2lZosQ44uH-sxl6s_yHGA8Jgnc1rTaok8DDXPlXOLCUTMNruq7H3rdk65NBKZiT2tEjx0_v85V2pJDh4ngzhdkuItYmUjWtvgCOWUaLePdxhEjc8UKsthqhPHk-wFx0SegytLtVGEMNm-rW2x3Omlr9ISS8MqCKgDaUZV5SfR5KATqQXo5jNuFivCfnxo2ZzGhhkRaOh1LcZ1M6aSJk4iY_pcH-Rw0k1Ek_1W0UiVZeOWmNJGAaYJqLYHd4XXbPm8ILcbVpox402ccdvMEK99CIKpM1Rmek5UfgrolGgqUzHuM52-fHRJ0JuoWqS2a6HhKZLUPOaVYJJgbo-7a3MXGd_caJCLhgz0Jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
کانال گزارشگر زنده بت‌فوروارد
🎤
⏩
جام‌جهانی ۲۰۲۶ را لحظه‌به‌لحظه دنبال کنید.
⚽️
گل‌ها، نتایج، آمار، ترکیب‌ها، لحظات حساس و مهم‌ترین حواشی مسابقات را به‌صورت زنده در «بت‌فوروارد لایو» دنبال کنید.
● پوشش لحظه‌ای تمامی مسابقات توسط تیم بت‌فوروارد
● همراه با جوایز، برنامه‌های ویژه
● سریع‌تر از همه در جریان مهم‌ترین اتفاقات بزرگ‌ترین رویداد فوتبال جهان قرار بگیرید.
👍
برای ورود به کانال گزارشگر کلیک کنید
کلیک کنید BetForward.com
کلیک کنید BetForward.com
🅰
r17
💻
@BetForwardLive</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/79696" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79695">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الاناس که عاصم و شهباز بیان تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79695" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79694">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79694" target="_blank">📅 12:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79693">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اوه اوه ترامپ: این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند. آن‌ها مثل سرطان هستند و باید این تومور را هرچه سریع‌تر از بین برد. این احساسی است که امروز دارم. ایرانی‌ها رهبران…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79693" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اوه اوه ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه سریع‌تر از بین برد. این احساسی است که امروز دارم.
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
فکر می‌کنم تمام شده است.
نمی‌خواهم با ایرانی‌ها معامله کنم.
ایرانی‌ها دروغ می‌گویند و تقلب می‌کنند.
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79692" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ-UOr0RAJbP-3DCOczswVRIlbbPZNuNifRaIPF6AmNGkFqQu9ySlIGy9fANRWFPVO6ejQp_33ibpjN9voW8YR1TlGnjZbu8X-8MLFnYmpqSLC8Q3Hu1GNw4_teeQShfMDXcVDK8oiiucC2cHwoF5QozEIMmTM5qA1HZfkue7oPFHUGAZKJkCb_0TeVBMl_inyydjvmDUMaYds0i0wO5u7qMMuS3ijMK8PQePA2kIbmgd-VqNE2dswuwTqKCMYUAG5JxwtIi4xGl8cqvVN7fcIbyAwYFSei1XHeWw_U68kS10QlGFKmGzH8Bbx864lDv3H8mUaFPHbD2aXews3SLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب هواداران آرژانتین با نشون دادن پرچم اسرائیل سرمربی مصر رو فشاری کردن
😂
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79691" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=cii83K-Wcfl54G5VYUZYETtKMcDYlnd5B4KsMpEhhcoN5wj6tdQYghxSXGA5TMc3Cojk4tboFd9QNaN82sGN7D9N9xVFraR_OWCxPYwO2RBuh4gFi40MwGh3_34djDiau383CUrtyDQ0VQOfPMDhD1uw0zsOyyJAH3Svs6rjJgGFLMyyYt-Y0pk0eHu27Q2bXn8M6JCVymBwVBmQ4oOBrAYZBB83TsweD4Wleh6uH09MIsOUfelNwI0P8tqJGIXtPAvLDgZNDp2SYq-IYPYgTN4W5tx1el7pD7AWnOfjHGfHcZL4jHFDMFQD4KnJOEFP8SMO87VV59QrLzwWHlVKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fab96f279.mp4?token=cii83K-Wcfl54G5VYUZYETtKMcDYlnd5B4KsMpEhhcoN5wj6tdQYghxSXGA5TMc3Cojk4tboFd9QNaN82sGN7D9N9xVFraR_OWCxPYwO2RBuh4gFi40MwGh3_34djDiau383CUrtyDQ0VQOfPMDhD1uw0zsOyyJAH3Svs6rjJgGFLMyyYt-Y0pk0eHu27Q2bXn8M6JCVymBwVBmQ4oOBrAYZBB83TsweD4Wleh6uH09MIsOUfelNwI0P8tqJGIXtPAvLDgZNDp2SYq-IYPYgTN4W5tx1el7pD7AWnOfjHGfHcZL4jHFDMFQD4KnJOEFP8SMO87VV59QrLzwWHlVKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 3
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79690" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79689">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوباره انفجار و دوباره جنوب کشور.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79689" target="_blank">📅 03:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی. تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم. #منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته #منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79688" target="_blank">📅 03:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79687">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در مقابل دوتا کشتی اینهمه اسکله و جزیره یکم اور ریکت نیست؟
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79687" target="_blank">📅 02:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79686">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79686" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79685">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خاورمیانه داره برمیگرده به نسخه پرایمش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79685" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79684">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Na5Z-eKYoJ03Seg6nEfUZOf1tggXrMPRJ16RqBSHHROPpTjrB4dKSt1MQxXgV9pkHfQD-obDdmgBDY9AvuIIty_yjGGYVerHBkwQfdHAeVPpjBQG-vAcj_LYR_XXd6stYjU8rLJO7LH0HbYewa3ufx1F8L1FnjSjANA4pMa7ucgAOwn9QEjUcuDmBD6qBAGUv_nTeVyZ1TRUKsQinDqXFcyuHKklbdrl_jmQEqUdDi_sKh7jPGkSI1z4k-dAxugCTAaNAiVDarC8uUxi2tHkzeySyD_p5ETTAKK3bZuJn6TNKHKjPRr5cPrIeIbJqKp7jhvTYCQpkJ6y7aaNEItBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Na5Z-eKYoJ03Seg6nEfUZOf1tggXrMPRJ16RqBSHHROPpTjrB4dKSt1MQxXgV9pkHfQD-obDdmgBDY9AvuIIty_yjGGYVerHBkwQfdHAeVPpjBQG-vAcj_LYR_XXd6stYjU8rLJO7LH0HbYewa3ufx1F8L1FnjSjANA4pMa7ucgAOwn9QEjUcuDmBD6qBAGUv_nTeVyZ1TRUKsQinDqXFcyuHKklbdrl_jmQEqUdDi_sKh7jPGkSI1z4k-dAxugCTAaNAiVDarC8uUxi2tHkzeySyD_p5ETTAKK3bZuJn6TNKHKjPRr5cPrIeIbJqKp7jhvTYCQpkJ6y7aaNEItBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجا که یارو میگه خارشه گانوم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79684" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79683">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سد مجید بیدار شد
ابوالفضل ناصری، عضو فراکسیون مجلس:
‏ ‏آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
﻿
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79683" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79682">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79682" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=gjRXCHLxSoOETP_12WjJannqpZ2SlICwn-ltjG0o59nXWCmsPA4323v7lzKL7ZwkRZneX3GiY200iViM1r6EismnCjqUcYZdGgOKhBzG2A1t-OuYsHgFZTWDKmSCNRvsB4Cd9thauJ0vTVu5CVQgH-T3NH0LqTIpQQ4A648NlLfi6lOkEsvP-5z3CGSlGtUgnRjBZctkoDRAkUXamI7_272Yb-Xv1_nQPj-LjctI2F7_NH5hiGFj2FBxp6SPmP8Vcqxsr-IWVovXHVaO2l1_1bQTCUbe1PXh2s_LZxEcZk_IU7tI-IUK8IKDna7DiiAQwFeKwYrFIQJCeAyEKv0fpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd7843a1.mp4?token=gjRXCHLxSoOETP_12WjJannqpZ2SlICwn-ltjG0o59nXWCmsPA4323v7lzKL7ZwkRZneX3GiY200iViM1r6EismnCjqUcYZdGgOKhBzG2A1t-OuYsHgFZTWDKmSCNRvsB4Cd9thauJ0vTVu5CVQgH-T3NH0LqTIpQQ4A648NlLfi6lOkEsvP-5z3CGSlGtUgnRjBZctkoDRAkUXamI7_272Yb-Xv1_nQPj-LjctI2F7_NH5hiGFj2FBxp6SPmP8Vcqxsr-IWVovXHVaO2l1_1bQTCUbe1PXh2s_LZxEcZk_IU7tI-IUK8IKDna7DiiAQwFeKwYrFIQJCeAyEKv0fpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم دیگه ای از حمله امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79681" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=teDfDjkVfi1HwmnPj2yL9Mp_sS5-oZypbC7P2_o_4zugxByjvTLpWwxl2FR9cqGLxjGPo_jWFJAJCRSiTDQpACRNHK_wzAaly4ZVMsrbHf-5OipgcFqEfFL10FWqM4WnTDdH9Ku3lGFEMIMaGa2lvyYyRFDYEEHuy_Y1SJXyop1W-n8lQME3O_HklpSqQose9d3-lOiOi5inE5v2UIW11yjJev7Du-G4Uaez9JDUhwfjS778LWEEOeFTKqRgusleL9P9iJOs_9MCgqKYX8CUb4s3LeBhVrYm4Llvh_TzMqwhi4pozmpGLDYO2WpHG0tEdoV_RqQSn9wkrKQ4C34gpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087708ce6d.mp4?token=teDfDjkVfi1HwmnPj2yL9Mp_sS5-oZypbC7P2_o_4zugxByjvTLpWwxl2FR9cqGLxjGPo_jWFJAJCRSiTDQpACRNHK_wzAaly4ZVMsrbHf-5OipgcFqEfFL10FWqM4WnTDdH9Ku3lGFEMIMaGa2lvyYyRFDYEEHuy_Y1SJXyop1W-n8lQME3O_HklpSqQose9d3-lOiOi5inE5v2UIW11yjJev7Du-G4Uaez9JDUhwfjS778LWEEOeFTKqRgusleL9P9iJOs_9MCgqKYX8CUb4s3LeBhVrYm4Llvh_TzMqwhi4pozmpGLDYO2WpHG0tEdoV_RqQSn9wkrKQ4C34gpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا پایان جام‌جهانی ای که پیش بینی میکردن، برای ترامپ حذف شدن آمریکا بود نه فینال
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79680" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قیمت نفت به واسطه ناامن شدن تنگه هرمز دوباره کشید بالا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79679" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=ZU1J6cHpa0s6_XzorlTLbgeoHpdSyXmUWQuur10ZWWoBgXuxwP8opiHMQoCBHL3juj_xQUnOUG1zDxgVwTps47jTM-RKf-WGRB_3ACHE_qDF78PVe4PIOBqv6WP_X141Sr8pPpDi6-FUugCmG_I_8Ml-7nV3W5D7SPK2o1J8YDVi883k2725wSE4qYT52qRlcbXihtuyGn22oW2GN3PW_TAZBpYMUD9uDSHJHlgh5Uf1hnOic01_M4YVzezmPwxk1MMQ7V6eU1OjIL68QSBYea6IK6K8D3jonv1XYgzBJfY51r4WxWcnw5nNUcoojN8qsFEHsHEVG-vYZvqnL6la2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8b205f33.mp4?token=ZU1J6cHpa0s6_XzorlTLbgeoHpdSyXmUWQuur10ZWWoBgXuxwP8opiHMQoCBHL3juj_xQUnOUG1zDxgVwTps47jTM-RKf-WGRB_3ACHE_qDF78PVe4PIOBqv6WP_X141Sr8pPpDi6-FUugCmG_I_8Ml-7nV3W5D7SPK2o1J8YDVi883k2725wSE4qYT52qRlcbXihtuyGn22oW2GN3PW_TAZBpYMUD9uDSHJHlgh5Uf1hnOic01_M4YVzezmPwxk1MMQ7V6eU1OjIL68QSBYea6IK6K8D3jonv1XYgzBJfY51r4WxWcnw5nNUcoojN8qsFEHsHEVG-vYZvqnL6la2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید امریکا به بندرعباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79678" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79677">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سیریک و قشمو باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79677" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79676">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تنگه هرمز ارزونیتون، ذرت نمیدیم بهتون.
@FunHipHop
| USA</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79676" target="_blank">📅 01:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79675">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انقدر اسکله زدن که از بندرعباس فقط عباسش مونده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79675" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79674">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این دیگه بخاطر کشتیا نیست
داره حرص حذف شدن از جام جهانیو خالی میکنه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79674" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79673">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سی‌ان‌ان گزارش می‌دهد که حملات نیروهای سنتکام علیه ایران ادامه خواهد داشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79673" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79672">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فعلا اوضاع ارومه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79672" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79671">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس:
به گفته مقامات آمریکایی، این حملات به سیستم‌های پدافند هوایی ایران، سامانه‌های نظارتی ساحلی، سامانه‌های موشکی زمین به هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تاسیسات بندری هدف قرار گرفتند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79671" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79670">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ تا ساعات آینده هستند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79670" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79669">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بندر لنگه انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79669" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79668">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdbU1nVWbmw2_M24AAfp8DqNSfn5D_JV7l_vu1NNL0ojPg2ZvFMfpa1sLR1xVEDLFk9gLbwCu2QTrCcCC26U4xGN2Diff7xGtMxO8NLlX7C-DUhLZVZxCNfyz-bBQsuYKUifEn92Jb890MsPlVY7Kk5SBCaqwChY9PxY9Y7eTdLQmqKArR-WO3jTAdUeAqwZslLV-0LoQEfvqCozHQ2TtE1BGARhxCk3TgU6_zjKW8hj9T4SJHLgDYbgKjhrm-PafFzI9ofZDirxV9jtMY3byMDwmeeHLxZDCd0pZZhNb1r5VSUCNdb-InFQnG6oo4E67H7l7oXCS87dgZoCD_zfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا صبحتون بخیر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79668" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79666">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=Cp2t_QhnECU4H06EJsEqioYTYIz3f-GwuVG7_FRSoUVaPwlBMTu_3W4DKR7BWNSchpvTa2AdqizGVCzcdyWn4dCe6UUNKMaoPS2SJeH3TDE1UvNkwJIoZCzZFKWFcPwsDMtJeRcmvr9tU44zDK_D4w6SjteJI_MMIaS9Pft_t5YXlzEozPMlKisdagXv7_cMV6XeqsyJDcruQm50bRKqiAZjPVYN_NTlUnGSM25_V72GS6eLNQH9KoUKpSyPoDGqo4KxYuzTVFjISvWNznNAr4PD5ehkn_kaNM3W8EdBhydJgFihs0fMONuvL3MazrtAV-m3WNnA78fVYDhnjNeZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80819d7cf.mp4?token=Cp2t_QhnECU4H06EJsEqioYTYIz3f-GwuVG7_FRSoUVaPwlBMTu_3W4DKR7BWNSchpvTa2AdqizGVCzcdyWn4dCe6UUNKMaoPS2SJeH3TDE1UvNkwJIoZCzZFKWFcPwsDMtJeRcmvr9tU44zDK_D4w6SjteJI_MMIaS9Pft_t5YXlzEozPMlKisdagXv7_cMV6XeqsyJDcruQm50bRKqiAZjPVYN_NTlUnGSM25_V72GS6eLNQH9KoUKpSyPoDGqo4KxYuzTVFjISvWNznNAr4PD5ehkn_kaNM3W8EdBhydJgFihs0fMONuvL3MazrtAV-m3WNnA78fVYDhnjNeZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا کی قراره در ازای ۴ تا کشتی یه زیرساخت پتروشیمی و چنتا رادار شوهر بدیم و آتش بسم برقرار بمونه خدا میدونه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79666" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79664">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بندرعباس هم زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79664" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79663">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام بیانیه داد که مهم نیس توش میگه اونا زدن مام زدیم اصن هم اتش بس نقض نشده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79663" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79662">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بندرعباس هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79662" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79661">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوباره صدای انفجار از قشم و اطراف روستای تهرویی شهر سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79661" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79660">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سلام فرید جان وقتت بخیر اول بابت برد پروردگار فوتبال حضرت لیونل مسی بهت تبریک میگم دوم اینکه ما قشمیم و صدای انفجار اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79660" target="_blank">📅 00:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79659">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیل هم حزب الله رو انگشت کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79659" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79658">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سلام فریب جان توپی که یامال دیروز شوت کرد همین الان افتاد تو جزیره هنگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79658" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79657">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پایگاه دریایی سپاه تو سیریکو کوبیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79657" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79656">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان نیاز به تعجب نیست، آمریکا خیلی شفاف گفته با خوردن هر یدونه کشتی تو تنگه هرمز یدونه زیرساخت جنوبو میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79656" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79655">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قشم هم سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79655" target="_blank">📅 00:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79654">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امشب سیریکو میزنن بماند به یادگار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79654" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79653">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lji-cKP3fidWJY7Hm5PMHAgxL_33Zg4yE3wXifhvPoxHn6AS5WXlLqhAET8D9gcdSjycu9HP4-MonhAessLBfnCaVIimxePlY9nr_uq44fcQyPRJJwYBCOjsa8cGkZy11L5t6XENh4Cw9lAzdS2GF7m2k5NuxzoF7a6tJQsL5bRqGmvepSnArTuZNhy9vfEGLWCSCDyCDQN-1_3kjFTGgot_vMsWeFjlO3Vz0wR6kOHRwOXBX6eP6ky85TxJA_wbIKi2KHmBEhNQU_BtbYZtoK-6a7SLkvIORuM7YOLUehFF8OENqT3k429lNR5WfyHtXXjDvVhFqgbe2yoxBrpYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79653" target="_blank">📅 00:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79652">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwpS6h_-dihN7W6uIm7sebB1aNvXUwA6TB9bB9BuvoXtRw_-kUBe0E2x2XuK9oY8OogmbEEJGyryuvfPtJoddqNqMzvmUKOOO9Qw6_wuHCZC9EswZ2g0M5nrDvWLnJ7FhTsDOOWlclRmFVJPU36rSbfT-1u_SKagtovf1zSZ0HIsNiU_MhLZheQbZuTvIWHpTY8KdHETHfz9tJxBjNCIuDrwYeKe_-nhMPAXuvRvonCC4lc3Gr_Wvl_-U7ppqgww5i5tNa0BUAK_DgokKbkAROuNw_lExx4q8pV4EBD4vpmTqecESgmo6RVss3OcrAqpa3kfNOxToUgqYgYQfnROHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "پاکار" به نام CML منتشر شد
🟠
SoundCloud
✅
Download</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79652" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79651">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خامس چرا دیگه خوشگل نیست</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79651" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زیر این پست آهنگای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79650" target="_blank">📅 23:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امروز سپاه 4 تا کشتی رو زد امریکا هم معافیت تحریم نفتیو لغو کرد و یکی از مقاماش گفت که بزودی چند تا سایت نظامیشونو مورد حمله قرار میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79649" target="_blank">📅 22:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYd9XqQS7qluplcPQkDhBWUYLuvluRKYfbAVsC2hE6Bz06eEFCZepw_WqqQw_j_zYl7kiHIFAU_z6BS_0xjBKjIfGIrBUDUht7BLjrv581CRKVsTJV_FOFMLABOAka5X5dDSHP6esNaChoIxY6D2aSIscWWzA9z5hRxg0vKi0bbckTjyY3JxD4hdR_-GkAFvZZFyywUK7yp6EXly3AmvTSqaSTxVpvRAyIR5w0X4AlI1RE9FfkolCAofkmov6FafhFmMPJ68fUz1bzb07k3_StPEHa2N8IFHrOIXRT9VQ7rEJCzHaqivJKhegDVgtgkye6OQPJ_7an_LARwON_q0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2HV3G1K8cE62tj0N00ZavOoAxLiNuIocVFYhOSi-0sH7Xct1-j-TKU3SPSdoc-uCR_fOOQYQ-DIR4rEcb0USZ7lvgBiFwCZsOYEKbP9Vnpnw111afZY0Sud9KGc9q2M7CVMuFrSY2yWVdNF9BLl2w1G9PwHAolzWdwTdx5CfaX-Y6keeJC6KfdU7sz385XWwgUKP2xzp_me_NA-k_CK4yHn7lgPTpmHR3boJREsfG4zvVhgFjDoBWC77IjVDiRgmI0gL3v6Ce7f6ptYVu610D9fGohh1O5K4djxyV8B8FHFODPjBL_ahQcsSh4HoETPblTWddbnUGtVOdPfI2VcOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این صحنه چندتا فحش به برونو و نوس تو ذهنتون پلی میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79647" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حالا به رونالدو فنا ربطی نداره ولی بنظرم آرژانتین یا یک چهارم یا نیمه نهایی حذف میشه، خیلی کیرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79646" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس رفع محدودیت و کاهش پینگ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_GClM3W7v7-EyczpPQ32OR1qEbIyN4Ndpw94JzJDNfhvopjIWviHo-dQ8pKRQ91zwJJGH_K2uiZxAyMt5kElPJ9vGIWE5PZkX3zmwEY6je9gll9ISs-4IaufLTu3vGdp6pjVXjV7EeLSCXRX0iTgvNtalDxuFeSbeHUpkUT3g-wsUfLfNkPLEu2xRoqr2aueCIrKSQx3sEXVTva2W7U99ChjVn8xfGaMOJl5X1wMh4qOOt-kuCYJd5xZAnDoeDcbwz5Tv2DhXiOxHSIY-rTQpMDAWqR9H8qXg9N_1aqEfPme3cKQWYtsMSAQbiIviLsqppClnt64My6M32oPISREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
یه اینترنت پایدار، تفاوتش رو از همون دقیقه اول حس می‌کنی
😎
✅
سرعت بالا
🌎
سرورهای متنوع
🎮
سرورهای Gaming
🛡
اتصال پایدار و امن
🚀
اگر هنوز از هاب شل اشتراک تهیه نکردی، وقتشه تفاوتش رو تجربه کنی.
🤖
خرید آنی از طریق
ربات
🧑‍💻
پشتیبانی تلگرام
@HUBSHELL</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79645" target="_blank">📅 22:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79644" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝒉𝒔𝒂𝒏</strong></div>
<div class="tg-text">ایران چی میگه؟
😂
سوئیس</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79643" target="_blank">📅 22:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حریف ارژانتین امشب تو بازی کلمبیا ایران مشخص میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79642" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79641">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR11iMIRcHSy1mTE51mb0aVLQwmNjoP6H_pAcRhRT38Q_-H_LtORV-jU7-8Xs_sBxrDpoM8Em_6mdx1q_l0IgS8dmpue3o9Gn8og-x6IMsHhqx-O8fi52q7UZzrgeA0xL130F4QwKoybeRxP5NYQ2MiPlazSuKXJdFX8f_8A_YdcXCk5reWeexQpEQDA2xhdYFXzWYpunh97uthIutwua39njBCo8NDc1FngsYjgiEFRPU3tLB_UVBO5mABOtb83Z7vTI3ZSdx1rrBD7euYQj8yF_rcwJ5w1IDERysLQHBrXrevgf-HTH5wEXxutv3hbeXzlVbaMoW2C87KGi3JdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی روزگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79641" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ولی دیگه مثل قدیما استرس بازیا مسی رو ندارم، فینال ۲۰۲۲ تا نزدیک سکته رفتم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79640" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آره دوستان، مسی منتظر نمیمونه پاس بدن، خودش پاس میده گل بزنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79639" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz7oPchOJaMwgSvovXsAoG4Pda114BsX-S0RGXnZjIMG4RqB_9GrxkL4kC82x5eotMuJeZ_0rV1Tfy5KGLurBUQgUeKp4i-gM6XNcGZmlyzZ8lWr8qzL_JhOeBO1icJSmdrS_naJgMZEPAPMq5Ayfx0S0QD-68IuOmccVE1TXH8chx2NC649V9cN-fBFYl30yvQysGkH8aHmJPCq0ZIGDVKxFEXyHE-IAOq5iJOaWdGUqzqWuYqWByES-WgykaVyGKEAIQGkTCcUqgqHLbgRbpkednWa4tmp-hcK_xs73PWUFP01A90y3QuxtrMEMItA77oL59JTn4iGfDXDvP8vYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79638" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پروردگارم
💙
🤍
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79637" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO9EagrMnvtbcwEZ5K_K8l9Yh-hTST2qkYAGhpzt8RJ8Je0QJzQX-DtdM3LqI-oCfivB9kt_N-y2pRw6TdotRzecknDjtyLH_CC4Jo15cNIjBa5VQqk-cbrmOwKMTVutrJSRSUOqBuoi0Kk37eDu6fwvitG83-mSkMSBLZxojmnrecmPsaLjMO6xSRvxHJoEFZ_tVwxf1ydoAYD1J3VOORgMKnXT4xsFHD5cG5z8JWhT5MQpYuswZUkyqTvqPHG0o-3xIn8OEorBnUOoiDorf_poPKOLgvg-MdBQWMrnh7SiqJDurhkW2hMsukRrMOllygCjXo3qaC05H3GChopohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنای رونالدو رو نا امید نکرد، داره گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79636" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF51GZGzmJyyHT9SuROMc3KRuUDW2WUBBY0o8CBdlazPQGsNDOrTsYMnHZVymMdvQdi60FHs9N_NMQUw_MN4gPGelfxHEau4FOuOoL7pG56oZISehLT3RpgLEEdJPjIPenan0yGbILXOGzlEEHGqfwG6K7mw87pgFCS7_YGQ3WeGIMtURJsW-QPInf1rISlieCl0Lm8wsVQVqMx7LOStaiA3OSt7wpKEor8kjzxjzXkMpJpxHRLt9vnlSVGTEDIB0eFY4-N91xZC5X-XsGoWsbfoEhITTzqyAc-ZTCEGF-fcS4-9w-ZEGWmnoF74ZS_hhCrXsfiwuGmFeFtsr6Olqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79625" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عجب کیری خوردی
😂
😂</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79622" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=J-4nfC_DBGpH9hvCBE3PuY6x8Q2Jeipgs1kjSjFWHz3Ko4U0qZ76kMhRo3NmP5tq8mBUI1hznlciC0Ebe0wCb85iWEjS-64KXkmTOa6Qr45hlaUId8PJcVGfmfq21jAOvEvo3D8t1iQ7IoZKdI8aK4cmGYnp3gkf-DubLptSTjJF5GU6ASH5hXsDDVKA4RLGzWH96q-XRHVQbUMuns4caC2fiUBQiIfMB7ZoJWQqndQI3SW5Ct7F4njKXHbWMOO7MnGi_qyHU2QeIgl4v6JZtZNoki76e_9rqEF1ZK9W9-RJoLFt0V0QrR7y4TAX9fY--9TSCkbk93DKAsw8oYAKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=J-4nfC_DBGpH9hvCBE3PuY6x8Q2Jeipgs1kjSjFWHz3Ko4U0qZ76kMhRo3NmP5tq8mBUI1hznlciC0Ebe0wCb85iWEjS-64KXkmTOa6Qr45hlaUId8PJcVGfmfq21jAOvEvo3D8t1iQ7IoZKdI8aK4cmGYnp3gkf-DubLptSTjJF5GU6ASH5hXsDDVKA4RLGzWH96q-XRHVQbUMuns4caC2fiUBQiIfMB7ZoJWQqndQI3SW5Ct7F4njKXHbWMOO7MnGi_qyHU2QeIgl4v6JZtZNoki76e_9rqEF1ZK9W9-RJoLFt0V0QrR7y4TAX9fY--9TSCkbk93DKAsw8oYAKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79621" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79618" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه گل یه پاس گل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79617" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسیییی</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79611" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79610" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لاشی
امام
حافظ
زیکو
چیزی نیس اسم بازیکنای مصره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79607" target="_blank">📅 21:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79606" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آرژانتین بخواد اینطوری بازی کنه قطعا حذف میشه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79602" target="_blank">📅 21:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgKyCtKIOb12XZkn5lVyYXoM5R3D_7DihZ2HMXDrTZUHOrGU3QYdx1SBU6Ruw4_c0o3cF2skEeqyVDEpvXZhYvqHvnXVhJr7dr4retaosBlVhjK5o2PIjLkCM_TqyV2-ZXpTgY8jOY8voo3gu64gG6ekLYbt0mxRQxUZUn2OyednpGmzER0YejtuGlq6yo1W1WaJCFcCCZ9n-lrRtwkf1dAy7rTxc6ehkpYHgsKk0lvRYy_tGiNIB5oIhMRydkThDS8dnP-Rt1NX7BOnf6TPQbyl6kb7e7d9mKT_EGHQLrK7lbqFTc3QwsW3467jR9O_RxcFA1b8Ywmh76Z0jO3CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو ادوار جام جهانی 8 تا پنالتی زده که 4 تا رو گل کرده و 4 تا رو خراب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79598" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd042</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79597" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شما چرا از حذف رونالدو خوشحال بودید؟
😔</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79596" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یجوری خوشحالید انگار مسی حذف شه جام جهانی قبلی رو هم پس میگیرن</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79595" target="_blank">📅 20:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndF7cLJ9G0VRYuYGzQyHE28L8XVHa7M7OTtYmtQBuo-b-7hvPLYfJRRgVFXNoUIC24wFXSXR2bFImv20txqiRMHckaWxod438_uR5NYyGKmZFyuyC_iscqOsS9kddHXLGOX9cLd52Ko0U5zCqZHAkaMTn8SAiLzU7X8NR2q3ahIIk2xPgUL_cRonhcCdD6Lhvc8aDkBvDXaURYyajJpybGlRXZTNA67bpQn9sJlxQlBWciPzGrQqxuFLSCvHMW7U-juvllv4cUv1De6gU6s0epmwuvezHElBL5bvFq0z9foDiwDEraWK24V_huv81025bBPQPWHDN5HjBE7unmIizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل عکس مسی بعد از بازی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79594" target="_blank">📅 20:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این دومین پنالتیه که دروازه بان مصر تو این جام جهانی گرفته</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79593" target="_blank">📅 19:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این دومین پنالتیه که دروازه بان مصر تو این جام جهانی گرفته</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79592" target="_blank">📅 19:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به گزارش بابک تقوایی نویسنده و خبرنگار حوزه نظامی: متاسفانه چند کماندوی تیپ 65 هوابرد نوهد ارتش که از اعتراضات حمایت کرده بودند بازداشت و در خطر اعدام به جرم قیام مسلحانه و کودتا هستند. نام دو شخص از این کماندوها: سرهنگ حمیدرضا خلیلی و سرگرد حسین مجیدی است. این عزیزان از حق تماس با خانواده های خود نیز محروم شده اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79587" target="_blank">📅 19:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79586">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kARNrSU8eUA7x9jA1abti7nCyMIoPwzWcVyhO7av77bgz4WueSnlKkpHgGsQvGHu6N1kSTihvd99Z7A83kbB9CiAcYSsOq8d9TL4Dftdk5RdIGhKtJPUbSiLQ0nXPKIddNvGExR9Ku9SUXSgrKBZzgHHjwN9RYCKZfvZ2LC_-uBzgteFiX59dXPyEpCD8Xzfvq9n6eQeSq7W1q-7KENB3walRhyMmpLrsSHjoW4s0Dvce9vsNduYSrVgyBafGShAQM-L_fT4kLxzag6eSceTT55K9IcOQ9BDhrerdx_SfhvFjsPoajlOXHszgCByiNFqWcZmjsRLDJCmx7HFnkUGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط مخصوص نابینایان پیاده روی شهرداری که مستقیم میره تو تیربرق.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79586" target="_blank">📅 19:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljTkEnzINXg1nJqDEgMbsX-4qEmyAGDyFV5LPKCFLho3MtiVYF6D8XwVHrRJxVfnWqpDZx2qMqVp2pXS7KC6rEiRZoY5JqVSrWBPXufwwJfDDlUOQ7qdDs4gd9kaef7TczcvqKZsrToAhxM99QohO8aXYbUl8F4Sf8nVPrxBl9FIbmZphZXqX1SlTMD0Byd9HtbULdYZKBv4sgmSYbxCEKRrLYtthZPnyJ_SG-QsYJys3vQ23zyq9oqWddMVuGbhh7zOS0p93LgEKuHwZYfbnCGOQkJGzCC1FL1g193XP_ss0LjebWXC7nuB-i4KwBfJzeMRfGsd1vJhIwVurD95zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیدار به نام “بریدم” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79585" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSPKAau-6yJH9zzN5nmaAGm4kMPpagT0GpUySzq56ciP_3HHq0MjaGNlhZ6gPUNqTCgHDsorQ3_Wuik9Xniuo79a_-Y-d35sonV0Dl3j23PUuSxZd3XYiGMq3579Au_g3KtlD_zMgn9lKGfoR14n4bFj1MBmfaHI44ncP_v9VR771any8gYD2_S3dYC2P6y93S06hiUUNx0HTsep9K2YlQhdXXaEeC8OWLgd0eu5GlekXz2EFFkMOsn1C0ODn3t2b-T6t9cACquDY967YZnGnYo0grmN-hAfqM10--gKGXxeXK0dNR6Lj11s7Ks_9-HI0UciKw3Q6Zfd_Wop2VHTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: بغل لامین یامال؟
کریستیانو رونالدو: چیز خاصی نبود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79584" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79583">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS6C9gLy3mYL4xJcYofZVOvEeYNosr_BMFnJ7y0MYm9vjR16htCTe70lkOia-vjh8ZjAhWSvcNuoey0Hxr-WpHImFxXkWDvNWNKjd5CegDCopvY0oCO-fWlkIoFaasMe20Wc8ETYPtZ1mnVW1vDCkERbZoFs7PLz7LNJooa_nr4fFJtcWR-YOKJZvHA9Si02n3NVrKvhi5tKv5Wu-fINAZktL2LuYlL4aWhl-44px8CRFNe6la8605dsdy2WzbHf1yrXMRVqyvUKgWo0xIVWADZ2CCkW5cIfmsuFYttWIxsqMxEczW2vs0n8x5kGyxAkAdUoc-HGUXt0QoNet3WFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا رونالدو کاپیتان تیمه موقع باختا اول خودش گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79583" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=StnAtD_siUAG1kvH4bc4GEJgYnB_w-5dTzkcq3cSfG0mfLXZIylM6S_Py-ndEsIjZWL8FEFfbVNpXRhbuSm9TIn1lnuUcDkmobsvlg58yDXMku7ogdL9xKpd3jH91Ec2e5xt0xyBFLuq88mea3ltV3GUEn1U1C43JWkik3I00DLmPUr0oNNy3cd5br59w2GE5Ojc59lA7hAXyntpzoi3ASXDl8p2-HmJXJ96BzlRr2dOt9irTD5f_SGKy0ui_btJl2spiBL2ON3C1TiUvCfYAv2ofVz3jyL5uCv55jE1a06DrTyguy9pLSZ9egZsir-9IUNu7WxknUhjg-I4wuvdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=StnAtD_siUAG1kvH4bc4GEJgYnB_w-5dTzkcq3cSfG0mfLXZIylM6S_Py-ndEsIjZWL8FEFfbVNpXRhbuSm9TIn1lnuUcDkmobsvlg58yDXMku7ogdL9xKpd3jH91Ec2e5xt0xyBFLuq88mea3ltV3GUEn1U1C43JWkik3I00DLmPUr0oNNy3cd5br59w2GE5Ojc59lA7hAXyntpzoi3ASXDl8p2-HmJXJ96BzlRr2dOt9irTD5f_SGKy0ui_btJl2spiBL2ON3C1TiUvCfYAv2ofVz3jyL5uCv55jE1a06DrTyguy9pLSZ9egZsir-9IUNu7WxknUhjg-I4wuvdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی.
تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم.
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79581" target="_blank">📅 16:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6VqqUSezNZ70oJ-09COp15VKYJi5O_Z2e1yyM58rhIHKSKtowuF2rea8lszjFS76MdoxzUvmzlL3WNlG5jZN5byireDpSmDcphzzdna6XTPmHuUJPO31KjRViRongQIqE6tdgOOUCq3xm5H3DdJ5hESntGqYdVuwKaqsoAzlwizjfw02e-GcC7_e8QMgHaxn4HVZWClWCW4AJlBHDnDm7-kvuW2wRjWYdd8-jcwIaEkqOYO1EWiHmj1lzWA3A10BJQ241Kz_ADWjGduGqUNg7w6155witW8uul7puKVSJmf8QAZTieDQSzqbBS6od3bylwC3Je61olqpFpVbLyXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79580" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUjnmw2dkQ-5pOvBoAWHDWbaGwq7YboAKFy_8fCPnAKqpzmC6TcbL53zFv6D4ls1toIK08lUVav12up2zKZ4fZejIXXFQqQyXxNnBs1dpPtZYy-FRyRQCsNi1iZDNG8WMVO74V8h96atQvC53yIQBWzzAUHr4gu_adq4v0llHbtsU1bnrfAeC0VMP8nWS4waFforaRFvQKr7ovoLCabuTWIPpsZxaFbP7h3ufYWzuWd8mlsl0bPGTmwi3QtO7n4gbfKhb6slDKs9XMQ77Vp-cao9hVT6Bj2ajn8TFSMYM4NQXR3_CSyBvgyfCCpjDtjG0z_2sABRPF4M7y-8wtyOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79579" target="_blank">📅 16:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یادش بخیر ی زمان هر چی میخواستیم هلدینگ میخریدش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79578" target="_blank">📅 14:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79576">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQX9foWNpCCWapRI6H07wTrvwiji0ourndEDYas3JktMEOIBSZ7WcbHu107JmonZ_kG2pE1JN54EiUaLU5pXXHlCGoQWSTQ0IXKImTecWiHTwbQPuioy-Xgkg7FW8fj6b4AoFdbJhZ5plaauolnf-zoCVIaC_ImL0W0erX1nqvQIN0rDdrVztYC3VnmFizdVupfQZ2RW1v7m1riJAncOqzSKKkC2Rz8npkzkTtNSK9fhZfXE0SD4aI-VdFXI1CNxNkr7UfMSPwBkdhStuwyKmqjITvifyY83Y9ImELv-HeGHukIvUsqRN_sBSuJMZcf9-gYk-B2DCvZcJRg0AGXCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuBrMFlBSPQZ7aqJCSwVG1SuG0PIeSBTDAPpQtuNdtiNwX38chhqxuYy0sjf0LMcQR_pA79a5mcR4Zz_-7fJgBUvIqSq5Ml7u-oppQ-TTMKXiPCxRW23SecDUsVhuqZHWDjiS-zlfktLmFUfChKvbIwacaiA29gyjoSmQ52aLozI2u18WFuqhtIG4VFyzZyx-6PDak3ZBiP1o109PVbxHc3zDA2LBVYnQaLY6RfQ4GMlnd_pIVTE0lV7Tht5QnoQiAOH1f3uULhjbhln3IDMFL57vzMNlkumH-3yK7BC0vfNekd6kk9p3XM7ae8mB97tD-UuX63Z5b6g67-UDpCiMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیوید کیس مشاور نخست وزیر پیشین اسراییل و از افراد نزدیک به موساد:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79576" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79575" target="_blank">📅 14:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dozk-lDEDY2kzFpGUON1mEmOThADLqZCd7XBH4pMS9aI_20grMSuffQgW6j1EKV6M6dmJ3iaQPeLX_1-DEh8oOVhzoKw6smU9iHJa86VUbOM7gb02j9u70DyPwYlq40VSXV47aJfNfjEO1Z81WoGToOgKFGG54W4zgRwxA9_Ny2R40VEMWZKmksp_k857hadwf9ckl1eEjHhgOY0kdcoqMH1H6Vvx24-DeOO6LLvrWa0NGALXzcV3kgeHR2KFQapFpZlaTctaRtUTgMAojkzgyvLJDoc9Ub69b9O2CYgP1-MyrMiNORACBNHO_9zTXQoFDceU0ovWRIGOemKL5AbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی میتونی با کلاهبرداری از ۱۰۰ هزار نفر که ۲۰ دلار دارن ۲ میلیون دلار در بیاری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79574" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هیپهاپولوژیست ی فوت فتیش دزده که بعضی وقتام آهنگ میخونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79573" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه دکی لباسا و کارت صدا عمرانم برداشته نمیده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79572" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX6Uxxfp_9ZpcBb49rLa-7AissvPddJTWY2HVkLlnxy2ZcEZ-ZG_Yg5ztAsi3wa-a_BpAXsF-3h9yGh0c-9yLARmH41McA_ivJlcJuY72L2L3KNjo8L7hGMJxngIdO3a-eeFvel90EWupvPtX-e0HMaU4wWvByqC_sXPJERDl_vi75PdALq3N5vmun3X2fiZxpYk5K9YuknAlJtFgi055daZSUmzy5BzxZzKfm0SMiosGEeRhxrvlxDKPbAJNcqE927dXuJDAQJpDP7S0BN8UcdUwyOhmz4rX1Sf3VTffvs6jeNiA9RhJ9kH90_m7Evdo-J2cHV5Tw00N2jQ0XZK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه
دکی لباسا و کارت صدا عمرانم برداشته نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79571" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsdkL7ofuWYhORGFCra-siwqxOH-BiHBDVRgkboSTOImg8_7WBkgTEhdYLC7i4264HUlleMGoE64_5ukUmKK9PKNQWfTpJf-T6SPaBIx8zBqCUqevcqYIkhrQ5oGGcB0EbNzIlAQvyih2pa06IHZ0ZcsmA4JURpB-SaKc2v-VR8v-_hd7bnLZWdYHJwdY1to7Nivj6eC56vALgbfuBcd9mY3MeYIuqTLV_w_kCPu4H15nlavkVQ-565opVDggkdA96V7gBvlmPJDPJbKcEQbcQIsYUaLcpQH3TAYhbkbDlfCs3xg6Z4dW0hc2NDuhGPMIgnntFVVnSo1xePK8DatvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق این نقشه باز هم میشه نتیجه گرفت که سمنان چیزی جز یک تئوری توطئه که ساخته دست دولت ها برای کنترل انسان هاست، نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79569" target="_blank">📅 13:16 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
