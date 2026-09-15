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
<img src="https://cdn4.telesco.pe/file/J8vVpPyR41eYPnO-i8wts9AEHrQLWq7a9SYaqqNuprZnaFUiMrBFuZS0Qx9UHVuYumyMJuKMYO6QUqvEfKjJnwDCNrqi6V2g0AgC7rlyCpbsWTjSssnLCj6Ch8Dj2-gm96ZO7gBqDnOVX9QmBpd961EKqsdkSzXU7bmYnl6b0_DBC3PC7SZY_MflMkTondqF_YEUXRTNS95LuezNZaIoH9zJ9xv7z5fBU3S3QcbNdnL4o4GZikRd-u__VFJ7lEzYxLBIxJnW_PEvrRihBQB19HVC6QJ8wJ3Oc7MOI0EH9P3fk_bRZ6ChAAe8r3nNNbrFl43qMQsn6kjQJ-fIEr51dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 509K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 09:48:57</div>
<hr>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB4nTy8pQrI4ENPSP_RHsyGZlrP82oYvTiTT4TvTN_iLNJG7Fo0QWefWEOFRT-0yNrIG4oPcNQKRrTHqkrcW1xtrw9deiEOekOB6uH9-F9NeX4EkpGypSI9odnZXQ61z6BTyHcDBjeCnj8UG50q3L6WfMXU9kjaW-1OPFHr-9KbkVIiw-T65LC_jDj9rM5oq7Wlf-o4tG4u4L7eS6I_zoSOnXDuoEB4990SqAJUP-oEepCt329rsaHJ1kwuHu5beLhzxG22-IWqm_SxIjmL0k24anO60UWFtZUNNdTM2oZlMtZZYv_RfE-ILPWQ49Gqv50CU7aUqHJ7nwho8keVmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGxGgYbbtHbUoxqZp4w2LJWk9qstNZvhyPmqMPdvC9FFe-Cx0yEk7XoJz1pm1q_8_KcGD47hZ807eEssYTth7gDzWrT-X7wO3QgPiLTA5dRJ7WFLXTicZWFp3LYzrwDWpZOfpWcArA8XgJ85WJiqjpLytVRm1JZL2rv7UIuU3gwRKBLXj7yjBET6k0zxRntUyi4epfAaaSjD8ZAaQLB79MXJhwcaLehUb9l0tClcHjf3cjoLUTBjOdUCWriJYBzKOlyKFNjNaK1QTF6YimxerNGLgHBDMiOhDactBfUPzvV8sCfEJbps2Xd7ugY326pu0voaQ8Fh5VMVY1ztVqzXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFXkCo8rF-56tR1HGJDK-OjliLgCrwLuPXaQUbIBho_GATbPqFQX1FpH4BBIGiVrOmKRMxT8u7-5cnuyWZbmgK0ofdkmMpKUKTNVDELHJAlOYJKdzdlTj62gB0QWyMjNscCNlDtOdmz6g2ofuOVxb8GzJn5O71FUwiyNB3mQ-cuRaRn8LS1oXKNCVqJs3H3xyUDLkZ6WIHcr5g7GQIzyWs9A93zCyyixyqpVi-1uhwIvWBnBBxOvVfDnqGJiwsqE4mZZ5CGCCgOQf_TR_ZgkMorpctDVzFm1CESlB2thRT15z3xwPFo_I5IPPcyq63L_xUNc7dsbJDMypXdqhMDWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPmHYryae5YPJAjhAkfc9bXrffQB2-e3dDZwVW1go-suGRVCRElMsSjXgH_F41qH2mrGSDnxqaU5_Mwo6qX6CIpHSERZlMt9aWU3Hxowu4kMitKQNmQq9j252LlsLCDtFKxQIFq14SubeuSp_URKnFdy5t6BWCUp9WrTDuW4UIj6njhYB9BwBy9ZxnOObDbprq0yvO9Z7d8ANwQpdn5bVPPRXiQrg5z4owm66Snhzhk69E6E-efAiZFPI8U079oqS5lg2nl2iZcpcNYP1VKDMWbVzybJVUNRdoFJdCjBCstxk0LnSmtdm3x4Fa6cDvLMqS-kjw18jfvjQkqsBTSp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGtzqSgNRucyCyJCTGgYyBmm5GNRAb46cU6oW7t0updO-6V_PkmKp7AxEWW4TM_RH-IYenNqHLaYvgCaQOdYxSGuA97qYqalMF3gOpVwyR0Z5rmOCriQnJvCy4y8d9AmvKKuTJLltKuTjWTmtzgrW84tWIol2htt9_qluG32G1qKXeEgKktfeVgm0JtA96J7PW3Do-6_tbBHIZCMr29ZUA-5j-0rXGXHYRnG4IsnwNjCpMKUuV2t5a3rI6u6eWdJI9D4Top0MtefVU7YHSvTfTXWfaIQmM3bvxy1-vMgWioFp2mO2UtZ2TOPULqNAYSBEs9fIKuc_TwuJT9SPzuGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29780">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkCS7iFb6z7hOF7h54RtU5xCZJ2r6FxXqPROzmhhCoJmdNTNyXEw4C1-MnYuNBZT7o8wfCKQPtj-hVWfUuGig22LoAf-EWKI3n5cccFVUjhpK9othZxazqYfnvH6POkY5Uh1Jwk9VNOzGX3JhtaC2US9J0twUWx8hBpqe-JeVqe58XgcxgK5ANV3G1f2CzxbiYg8ku2WCIG1UPtjBTj4XiIkkz1iXhwAqYXS5s-ex63U88g0zb0H89pcY9GyInXS2bYyVVrN_4RXnhUaHAQO2GCW_NiVrtatnnzQU_oxFidQOBDauCoK30pRfZ8ZPFeMelz2Gw0ewtX2LOryBWiOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
👀
🤩
🤩
🤩
پاداش ورزشی برای واریزی با روش uwallet usdt
🤩
کاربران می‌توانند پس از هر بار شارژ حساب کاربری خود از طریق یوولت usdt، معادل
🤩
🤩
🤩
مبلغ واریزی خود را تا سقف 20 میلیون ریال به‌عنوان فری‌بت ورزشی هدیه دریافت کنند.
🤩
برای دریافت این فری‌بت، کافی است پس از هر بار واریز حداقل 5میلیون ریال از طریق ارزهای دیجیتال، بلافاصله با پشتیبانی زنده سایت ارتباط برقرار کرده و درخواست نمایید.
🤩
حداقل مبلغ قابل دریافت برای این فری‌بت 1میلیون ریال می‌باشد.
🤩
حداکثر مبلغ قابل دریافت در بازه 24 ساعته 20میلیون ریال است
💥
با پین باهیس شانس بردتان را چندین برابر کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
p23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29780" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCD8Gja4WEKuJqOfoU0eZ1zit-mzIqJgBkaIwsCERTKv2-HcTHj433xAI7XueS9sh4c-FyIrgxgP4m4dcxcIn6aiP3QLazKWujvd1J3BJxaQBhhlls9Hkk6MA_7NeS0GezYwpKIBqtxh0xK7U1oDVKyY0bRAzhrkzE4531vvtRSkdoJVlNgR07URThBGftPIQQ3qDyd7Ao-ComfZLcKd0v1E5NkR7M9hn23T25zcPff-x9eGKUI6GMWtaxgDKlq6OigxPcGZ3KH1yjujPAavDv3_HyLwjkZKklIjxRPprrbKdRvwNBRQ7U6ywQrIjtsXdMS16ANJGwmFALseS8H5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw9VGvKYg8-rjN78X5z77ufrySCF5XHH8yjfS3saGqrGEiOkQm1p_Dk5srpbTU7RD7h1_PigI0hWM6fbYTV4pNlwSmh7yvPjSuXJTH8qFiHnsGvB9YXyxyUckEX8CRuXOrRS8vfOmRp_sXVZtJ5dSsc3lhspzQevPoz7ikyg4uW4V__IaeTznki58Hf90UwirZ7Lw1P2ZrZmKqwVl49h3qaNDgFvPYL-cec--YvKi3GEx8mCfKYjVY-E1j67Ig9hNGEqp9YScfYZqUnMzuZKhvaVXvqsL5m7tPBoNoddcqSSMHVjTx0DjWOnayazstlSCXWNt92TGlscAfkZ4Q8d3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRm7k_Ja4zp-GrxcT932aUnNIv6a9tadAVktqiWw8zGHLSRPCm1qU3nqiRbkJDnZK7-C1XQ_91uvVnkwTVwWfUWOvMx948MPvf3CO1HgXoisx5gAisC3d2Cb9LxrkUIILviPS3mnVqT-fJQaasFhyoF3EljkzgKPPisQ6gCnAzdGCuiCKZOMnrqNWNgQnIWj_grACLj6_Srb1iRM3C0y8SYuSmN4dUK5f0d68b8gSHqZsQYuyArqWVPr8ShO2YmGtaTPTB91UqpuzX4cICAxaOqIyi2HUV5Te73letxW6eSk7avrZ4-NRC2Jc1Q9hONrWDJ8EViwUF9SWZpq2vF-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGt6zNjh9q19f7XI1_oJbBRGiQ3r6OJSoT4pgIo8kQjAOMDWeVKWcnbQOoKB7ShvGrpXTiAiPgN_7bzjpp5AyoRfy9OCfQYccg4oeWeHi2KCKCxsaySr-v8_a_-My2d_MIPNVHjkTQGtzyAUFIpF6645pOwwceTxAcHhel1nvi36qpIz8Dcag5tHdPP_96uRO8NTExMqw2Z5_ilVzk69ATZ42BTxhDfrH_4-806JA7vt6lnC6_KoAIF0IWUsBXMlHSGOVXi58J8z7wCqE41ZVJ_63t6UTsheXA76HucEL0AJFq9B3KRwEwWVj4JOhwellD-6UkovnjcIjc5myXzGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgygiC0XvXeRpo-gEO63e3qA9d1ihGZeXbaMI2Rw9-98QjFHUdqPeyhhzAxzs-G5gcyNgxEdqviTi2g7QqRhd_brJheZZtAgUWpBy84tvn59MiVkaa2wiSVN9Meq7_pg330sDKksURU6OrEfLQ4Jmx_XpMMzqUenBw_4aMzkOG8PZnxdG01o9bQuJobLW0F88Kg0BQcw8UUqhRC2fEy-lioyTf9h-jBxpuYOhh6BJRGXrOcHVvsc06sraVPhDiha7wYYvEP7BFW4cbG2F3pb6XX6ac1bz3OZHKMplEgV6CIByraRayUg_HRisnIwgoJKRI2gZ9ReqJCz4LMR2AKzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti7834UbECJMTCCwM61PdRkG_e1sj7MCqFIJmSAI0dmsu31Qc57l9_y-ob_U_ElaWYTcaanNB2OJ8Bp_ChGH-ZBHf-5-tQPp2iSbX-Rq2DUg2MBiZpdZycKie3eLhTlNvixYXaMi-eJZEZOgk92ft9Td0vXjPBQCreOz4tsodv6OSpgZSmVn3fpBs6zOUVNGxq5xKcux24CAZJtTOJvPqti57GKu6WvLKf6a5E-fBauzMqVVhwknKVcucjszZRC7Z2QQBO2aiaKgtpTzOSVfViUJ_QuSuF7vo-pGU-RTtnQif9AF63ACqYlxN1nbFy1FY5htud-gnUxvWuwyyA6doQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e66X9vUv4VKMWC7n-nC_63QkcuPO-sGh4Mk02MC15_7UG9VyzXQrMu4C32ZjSXV8zTbqD-DvKj5xHi25Uds3jelDpMbDORTGKx2VWkHQEw22obv5PJ7CbLuIw5z3_RMFZ9Lp5A4i9ynJSc4oFN5xXuWI4N7yL--rs09-Z1I-b1PBqVcdH8mje5yxyA0MnqmgzlEx5QnERkG5C7xFbMC9vB55BfpmEWxOMrdYDoHqXMEpH0km_-foYpdFHlDdEWGe7SmedwpLEAfSWsW5zLKhDkp-VKhKWoHCnv6Zlk6OQHtNe0lTPEN5TBNu4u2Xr9n0tVTkOPdcNNAcKCV1VJcgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29773" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzQ1xssNVMMhAXuKyGTHtder_jK8tQNEj0GioSgbp6p5V4x1BptU0VzolV8OE3IjnHe-e-BtwQYjNougCHU_rie43QA_shas3X5zinh50aub1cGmepGutp0qYeRqDxUSq3dBlyx20URnWT1EfpoD-RBnJBv4Zbre6OExBlmHkGyMkGsmsqvt5_RqyVgPu1TFj0rbD74JZmiUJ97p--4RBM27HMLD0lq13iIvNPlaTQgu3d748Uxijk9LkeRHpClrmv-Q3N9xFZhwblMKlJG48pbyvUGBuxAZJmuJIZXIS-3_4gTKXKV7tqnRzxKV-CTIyI-XwsQGVj9SDLNV970sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29772" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNbGb4ql57lqf9wc_lBQFVKOAwmxq6vmqZWGqHb53tVR3_IKRSWlad4Ln5sMEOunL_rVCxK2cOovqGDwgdChuY-agjBOMZBDmhq7YCRwQPKFOhRCrcU4UN2bSDUyMjZh52Oj5gQecEru4XjURHTPCHRT1wmG4q0onPDNrwuaXzYNAjI1b6TqYabnxml-j7TbPfnjSdb_2TCQ52t44DdAXgx1IgTmF27SVk9I0giLDeS5cacjnpqKHkINV29OnulK-9ZwCJ4hxo9eJIYArvT7QU1QpcSjvogn3i1bnqfEBhdWqf0XK0i1cbnZrQ2WV7fDh2ycpuIVYAQgQ1Ep3tZRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29771" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=ehHdu3J7gCXcM--_tobByVz1Zx0928rBCRHegj-hGNuL5jVqG_TyBVmFiDRIR6mHRGvI522VM8SqR5uHO7WJH3E8K_cOyirRg6dSFMgXocfZIrdhxMJepAtealNkHd6hpI14-7c87MW1TAMcMN0sJlTFA8Nh2diovKw_md-5zDNnPt71Gp3-zXq2Y7kUIntpTHcD_w2lHnzUE-wpH-JExRNLMXmQn18heZvLfuFncK7YOd4VxaKm1qD24O0KEkqatPojyncI_X37l5Jw2XT_05tiiVqAnqWkyp7rjV5U2kCuBsPiRlbJ7f-egamsIdaB_9ovjYSPaKGQa1QTARb8bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=ehHdu3J7gCXcM--_tobByVz1Zx0928rBCRHegj-hGNuL5jVqG_TyBVmFiDRIR6mHRGvI522VM8SqR5uHO7WJH3E8K_cOyirRg6dSFMgXocfZIrdhxMJepAtealNkHd6hpI14-7c87MW1TAMcMN0sJlTFA8Nh2diovKw_md-5zDNnPt71Gp3-zXq2Y7kUIntpTHcD_w2lHnzUE-wpH-JExRNLMXmQn18heZvLfuFncK7YOd4VxaKm1qD24O0KEkqatPojyncI_X37l5Jw2XT_05tiiVqAnqWkyp7rjV5U2kCuBsPiRlbJ7f-egamsIdaB_9ovjYSPaKGQa1QTARb8bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29770" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0hyie0PGPeawug9NVECZUzVKXL06qiNXTkahXG__8VWXfuaQ6o2QzbFJoNdU09VViEsHz6h4Y3WFxbkB9dDUkrkvSM5s8clV7Y3ZUy7AXpGibtkSClc-9CiVPi2iuI_7CbqABS-Mxu6yckXOMNwdorXemgLsaevCQajksnJQFb6djicbzQ2fzsd_Bngy-F5bxx8NGtgn1EURG3T03gQm1de60iP-sgbsPEnWfjuNgAtn1-8FRyF_QyZgyZrNeeCTmpvJpPlCBlJCzbqvbxiYHRS2hwnVSpCEOuEjKQUDDXRhtOR_W7gtvyx7Sa6CjK0n3EkBQ_1bgkOEsRR7vE7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اظهارات‌ جالب لامین یامال ستاره بارسلونا درباره توپ طلا: "فکر می‌کنم امسال من لیاقتش رو داشته باشم، بخاطر چیزهایی که بردم. چون از نظر من، من و امباپه دو تا از بهترین‌های دنیا هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29769" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=DjXczo3gLtwCG779alvnMlO5_2Gr0Md2I6ixVWUhTwhwZqVm7mhhgkeWrlgCzsY_MS_ETAgDA8B7vtw0bguI-hn45SyvIdr04u5RCTF4S1cpKWbCOSt4w0hefYftFTwgg7YoHV7tHb5eQje5BG3xEXoBLBSovNfBRu5NdIaOrwSPImS3_HsapPdxYyoNJc8CYC3z23vpH2dp4UP2GE_W1lTis9jexECzTiij3uSyuIRueQ4no11Ljbx9NAiC_j0nY0FxYBMO51ibD5NJvvOAv9OABc3TcFQyTipnAnbjTSK_tQbjxawmn2TsEO9Re6ATxe_ySa9IarbtlLuk-a95R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=DjXczo3gLtwCG779alvnMlO5_2Gr0Md2I6ixVWUhTwhwZqVm7mhhgkeWrlgCzsY_MS_ETAgDA8B7vtw0bguI-hn45SyvIdr04u5RCTF4S1cpKWbCOSt4w0hefYftFTwgg7YoHV7tHb5eQje5BG3xEXoBLBSovNfBRu5NdIaOrwSPImS3_HsapPdxYyoNJc8CYC3z23vpH2dp4UP2GE_W1lTis9jexECzTiij3uSyuIRueQ4no11Ljbx9NAiC_j0nY0FxYBMO51ibD5NJvvOAv9OABc3TcFQyTipnAnbjTSK_tQbjxawmn2TsEO9Re6ATxe_ySa9IarbtlLuk-a95R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=GklPqMKHyUorhvo1Np4eRXUEF8c174pCTiuOfoWwcGo_Jl12yZr0O1zL-f6VDDCilxdjnXxepOYeNcyksiE-tKOoLd-pk7eksy0vIWUuPl6qnDto74ulefh_e2OAYYGzXneWRvC4cxrFROwt9uThRLJ5ckOGbHji2orDququO4rXPLJWUdzPI1CebJbV3dGtG3HAAaYY0Y-OJsTP-EanAQNhkLS3mMHl6YbyWmAx12W8BnI7FNMeDQ41Ap_13bAk7uagxGbvYuGCkJEGEfcpEtkWKS2Rumv9L2Nd0MnsDqo1-ppO9jgfJC8YMXUk96zBpOb7oI_Ivn7KYPEiwwMUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=GklPqMKHyUorhvo1Np4eRXUEF8c174pCTiuOfoWwcGo_Jl12yZr0O1zL-f6VDDCilxdjnXxepOYeNcyksiE-tKOoLd-pk7eksy0vIWUuPl6qnDto74ulefh_e2OAYYGzXneWRvC4cxrFROwt9uThRLJ5ckOGbHji2orDququO4rXPLJWUdzPI1CebJbV3dGtG3HAAaYY0Y-OJsTP-EanAQNhkLS3mMHl6YbyWmAx12W8BnI7FNMeDQ41Ap_13bAk7uagxGbvYuGCkJEGEfcpEtkWKS2Rumv9L2Nd0MnsDqo1-ppO9jgfJC8YMXUk96zBpOb7oI_Ivn7KYPEiwwMUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlJRhqfccgotI6JFpSSYIUfWWmKD96HiouHitcdniZQQrHjDsUsNIyd7d9ndsg3mHf_EEGCSVSP8n6TVha3BQCujxDsBjd4P55JTmA0Qxss2yFigyi8QIC7iTQT705tYNnbslfdLW0TM2ophshBivWABmej4BwOxTlpY5RCTyfwCvRuOie0wLzuvlU1gwbf6i_YyrR6g3nCq1i1Ntr8_efJ6FFrKre7TWzVBMBwrwyK_fhnHK8g9QtsIIqPIrAnpozStF86qMXzqVUDovBDGJ4RwvB-otvigyX5BjUWBjxyHaZXi4IbG_w00QM88O3R7At7RbzaBXDpdRzAvH0GQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC_cSJrCfz6NzaE4gFNxez_rwoyGDLkig8-97W4EI46yGQbakmPqwV6NjNBCOCzvjtPpd-4VIGWMfhYUYFbvx0ulLZdVYVV_Xusi69JCdRinBWtpMeRM-c5uqNvtWhBJvCVlz6UAKLCrcCrkQDoAba8yYE9qZcF8T-3Jwuw6oZRbv280Yktmdg6xbsK2gNuuGYA04fW0MA1LLrDVnsTJFsQAYAolXtSezityELe7ivt-DfZGL8MLAniwahxBXwnObSCMds2Ym5_4JnwyM5Hr57LLQ40FcgEHp8Buco_iWHmkvgsGObv4PG1ZPED0eU6mmmM5pAA5ubHhPCEHU-9M4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=Mo6zX1XgDG3us5Z9OM9giAWHBLC5bUqBOgyjeNEzmRqmsBCa_MbHg9ZHZxY6pif_bx56a1cDUxlaxv0Zl7zLP6tEElGViL5TT1VcHMDYX2KwYp34f1J1oJHF1aN1K1ey02TerPLdHI6kz2_8anLQ5XlaC4NKRQfonc-p-sDvl-qdDZXtz6Eq6V0mbNXVoxz3vV7EHAH78ztgZ1BgNbWMRjmy8RTX5WHWji2iUSx9oqkhdWIxnWKzoUs0OAL5GH9XBPAPhuDY41uZ1IzaL9Ec09IFjNOwmP3l_yEUGvHXF1OsVrHkJw7hIEX2WxWp4H0GKVSG-usjCbZswlW92QXAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=Mo6zX1XgDG3us5Z9OM9giAWHBLC5bUqBOgyjeNEzmRqmsBCa_MbHg9ZHZxY6pif_bx56a1cDUxlaxv0Zl7zLP6tEElGViL5TT1VcHMDYX2KwYp34f1J1oJHF1aN1K1ey02TerPLdHI6kz2_8anLQ5XlaC4NKRQfonc-p-sDvl-qdDZXtz6Eq6V0mbNXVoxz3vV7EHAH78ztgZ1BgNbWMRjmy8RTX5WHWji2iUSx9oqkhdWIxnWKzoUs0OAL5GH9XBPAPhuDY41uZ1IzaL9Ec09IFjNOwmP3l_yEUGvHXF1OsVrHkJw7hIEX2WxWp4H0GKVSG-usjCbZswlW92QXAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3YT42qZ9c4rqAY9X5t9kPs1uu9NKpfciYflMObK_j3_j5OwOW7dLtdWVQ1QVqV64TeT9zvjR6f1C96wYjomQmZWOCsCx9EJMR3u_7azqNHYqtECftkHmUejvXfS6bd3yzBosdyoVfHK1RdWg6nrA6bXX9FjQFWIszkbg8Nd4iKqCpOex2roUxwRTvNyy_N7XBF3e-CNa1jH9iyg0R2OREVhn713Q5EEibqMCvoQ9-cYXQDfK7A78E6rC6dIqb2p4HPPxYxG3kvPPcGdjpNxx_Ezm8Nm544NhHLRHxSyO_Cvef3PtPkQLXkC4fP6a85Iv-u2mgWac_SG2LP3ASdozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=s7YRiFsEZ94XwJ-Aa4clo_JhCvDpTUJpbMKmQX9pbz9ycE7Cm30qOdkZenyTb0I_T9YKEOJ8YMXzu9nr7gOS68bGgco_JORVxbiZeddRXqM70k-sug9GNMX2GtUyUQhIsr0C4nlIXdTaaK1K066_lCOO3Atz9_68Xwt-irbbA1J8OxtfAmIhIKKjoyNIC2hdGjLhvkKPEPl1hwpbcFWEJR8VZGnuyALRM5aKDsfrgFUcYSW9-uCb3tu_yhmOhNI7z4vzTkJbD7vEZrKtjg9WOD-ag6T333Am-kuno-qs3vZacRWET0TCRuHK1gP7o92CuU67uuUF2JMK0J3c1KuPdGceXScJpMIIoReRZ19cI9Wzh9hP_zKOOhI0JjGksTp1Wmx3Hv0UIjoZmQ-yltC0LSXj7GSAxdYIAyLKZvjcUuNjBnoFEvII1QUlIfeReWv3uR9jPcDkDol8O10IheisoJA-JrjFXw01W4VoF4TBby--pp5KAbAoS_T3kB4QRuPqDjctIw7PWLJlWtjmbUxWRxPihf5S5s4n11hXwM1F8V-9qz55dMWR99US0cwC4N-0_rMxSjGHkhL0Qsbt9IjP6rJEuTItGk_3FQ4RC0wMtNw7jsOC_moKDs6vnPguXTflCb2Ifezb14W6ikSa46_WuU4tvWYlo586Nz_bSNeyzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=s7YRiFsEZ94XwJ-Aa4clo_JhCvDpTUJpbMKmQX9pbz9ycE7Cm30qOdkZenyTb0I_T9YKEOJ8YMXzu9nr7gOS68bGgco_JORVxbiZeddRXqM70k-sug9GNMX2GtUyUQhIsr0C4nlIXdTaaK1K066_lCOO3Atz9_68Xwt-irbbA1J8OxtfAmIhIKKjoyNIC2hdGjLhvkKPEPl1hwpbcFWEJR8VZGnuyALRM5aKDsfrgFUcYSW9-uCb3tu_yhmOhNI7z4vzTkJbD7vEZrKtjg9WOD-ag6T333Am-kuno-qs3vZacRWET0TCRuHK1gP7o92CuU67uuUF2JMK0J3c1KuPdGceXScJpMIIoReRZ19cI9Wzh9hP_zKOOhI0JjGksTp1Wmx3Hv0UIjoZmQ-yltC0LSXj7GSAxdYIAyLKZvjcUuNjBnoFEvII1QUlIfeReWv3uR9jPcDkDol8O10IheisoJA-JrjFXw01W4VoF4TBby--pp5KAbAoS_T3kB4QRuPqDjctIw7PWLJlWtjmbUxWRxPihf5S5s4n11hXwM1F8V-9qz55dMWR99US0cwC4N-0_rMxSjGHkhL0Qsbt9IjP6rJEuTItGk_3FQ4RC0wMtNw7jsOC_moKDs6vnPguXTflCb2Ifezb14W6ikSa46_WuU4tvWYlo586Nz_bSNeyzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svf4qHJpGw6oy2u_ewa6afwha_xdHKVnAjYvBUp44waXYklZPVtO9CDirrorpnXU0goLgLnp6rAnO3eM6_n6FXCquQcl918w-qdf8LqGqjD5gB5R4eMvikrDRafJfdk81-dn1QwqYPK55XymgYK63iO-NE7fiAL1fxNs3EIQshyzHVTpGr7vezLOURiuMy5RhrUzswWvdOkZg5KvM35yY1nzkkKdx6zrZzRNgn3LJraHymkQX7zhmaFl92ZcDMdxPXV-HWYRRT81v5UfrVF1Ky8DvGizQrUQpNN8PbJdQS2a2WYKr7MkZZwhF9OE3pInjnwM-zpGMTOG7o1XbR3-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtYAZcBUW8aXFgsgM833eNalN34tPqQr7jODRR4jD33BbjWzuOXsHJrOFI_xrMhs_qkonhEtVlYVMI_dlHfxyNZ-2hDyDO83egc6gkpLCBihcDt8JSEM2N_WY9qOhLaPrplLy_s75jQnlZZd1IYwMLi-VQzYpdVkpvxGr9ZgrSwdzQJhDhACvzuC-5bGAcR316EfvDtiEBVc_scj8iDT19ME3grBJClYm0OE1QDxHz4pDtqdrIKBD6Ny7m-BM9xLmYS1eUABGD1kgRP_fuBwOmlljCd4n4GZHlNazvkjlVE9RDceECx-vIujzv9bjYqMZVUWwZiIV3DfSaTtkGAifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7cbHE_XuLG2MoCBARnm5A41ckuQZPCLtNksKH8_ZNXgwYp5zP7M6_3o2Sw1WTRnVA_Ebw6nXp1m8UwBZkrdRgpjBV0CpfqXe4kiI8BtilZoGQuE_K1fn6_nJraK7UAZRE0F5IX4-a0DpXuywd2v9S3YJBoeFfWaEtPj9xnLKCGw-8GZsm2lGzDKnVNEWHgAtcJ1aap8bSKBkt9UJxHCSL5-takzS-0u3xuohurWRaU68rzjV8Jlya2pgsWpJqtDtHQGa51hqjBUKzAIiqRiTfbIYmCb3ubQqIAroC4zDkWqheMP29y8RH5NFFvZ2vLMSOukEoeQJm1wKosU-xETwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29758">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKXWlEuS8n-bU_ljFkz2Wxg5HQJzhA3uW-CT8n5yayxXroFxsAW2dvA0h23X69y1kDTfADn8Q8w6lwqUaEjiKNd71GEm_a_Cf7d7icSWVHXqYjKGRrzylWBcVelpkIAMYHgqOoQO0VQiZF2Mdtj4As-odpnT2wCuu1V6v9wtFs4HlwSBkVgRs2K5p5wWbqr0YcIKWX4_FAf6UbIdrTzjy0lb2B7xbY0ytEP6uJ6bwU-zc8rmDPZtXCS7sfv3iUUg-pZe6_WaRFkyKnf5Oce4jT4YHl3JCeGQT1vsOfmOYd0JKgQB0RwOK7h3jPopJoaRrHXtx9mIj2wl8aV5tg7-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سوال خبرنگار از بلینگهام:
هنوز هم گواهینامه رانندگی نداری‌نه؟ جود بلینگهام: نه ولی به کسی نگی ها. من هنوز راننده‌شخصی میگیرم، الانم کسیو ندارم باید ببینم همیلتون بعد فرمول یک چیکارست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29758" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29757">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=lBt5wVjmIWlQj-BpWUheop49tA7roBTyIupKxFvOSGUsdNRnalwkga5PdxKdmMyp3fYhusx9ags5P0jVIT3aeMXYfcGTaqmOuJXpSLAQFRY2WnvjCGlfPgWTRRTNJcOAv1vaAp3G1sIt4mPyn1x0MY-isWyWtgTChHia3cdKwWv1u-kQqQJv_ajsUIXtm3NRYZg9tvXUg0dshnMes1cOLaGyhlmrYahtGkGIbFwvP_LEWuOR8hOnYLgMySn3b0klQJSsVafmd21MIxddyvDkAj38yamdI2AOqsQtVh_VAuRl1j4bJGqUCuu1g1svjUZ1kOYh5H_WGCmutC90k13N3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=lBt5wVjmIWlQj-BpWUheop49tA7roBTyIupKxFvOSGUsdNRnalwkga5PdxKdmMyp3fYhusx9ags5P0jVIT3aeMXYfcGTaqmOuJXpSLAQFRY2WnvjCGlfPgWTRRTNJcOAv1vaAp3G1sIt4mPyn1x0MY-isWyWtgTChHia3cdKwWv1u-kQqQJv_ajsUIXtm3NRYZg9tvXUg0dshnMes1cOLaGyhlmrYahtGkGIbFwvP_LEWuOR8hOnYLgMySn3b0klQJSsVafmd21MIxddyvDkAj38yamdI2AOqsQtVh_VAuRl1j4bJGqUCuu1g1svjUZ1kOYh5H_WGCmutC90k13N3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ضربه‌سرمحکم‌سردار آزمون‌در دقیقه 7 مسابقه که وارد دروازه تراکتورشد اماآفساید بدرستی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29757" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29756">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90deefc883.mp4?token=ubBj7lP5i8Ud_6iRwMmqMjv67tEKrXmuJsm4x8jg-hp0cPcMPHuZIsyPtZxZzTyc3uW3rFAFO7auwXsVlM7QjDmgb0A49ZbOPgswuTJDf26Q0ekN8PZMK79_dTPS5SK3DzCn3YHq0kXqzwmSWYi2vDXTrzFILjEzzl7Mpfwmwl9syfRbo0BtAfM77SdvyCs9yEPv0f-VKZIgIiIUj79EhlYP8eRCXnlsTJlpXnd__yZc8OmeH7fxzwECsNTuTGzIV5tetKNG7Zy_rKe2GGGemzi3P51EqtebIypWUf7q1rs6YoZWX7IvdZNmgkxh_yzepIhwYNecdFpZCxaelVUwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90deefc883.mp4?token=ubBj7lP5i8Ud_6iRwMmqMjv67tEKrXmuJsm4x8jg-hp0cPcMPHuZIsyPtZxZzTyc3uW3rFAFO7auwXsVlM7QjDmgb0A49ZbOPgswuTJDf26Q0ekN8PZMK79_dTPS5SK3DzCn3YHq0kXqzwmSWYi2vDXTrzFILjEzzl7Mpfwmwl9syfRbo0BtAfM77SdvyCs9yEPv0f-VKZIgIiIUj79EhlYP8eRCXnlsTJlpXnd__yZc8OmeH7fxzwECsNTuTGzIV5tetKNG7Zy_rKe2GGGemzi3P51EqtebIypWUf7q1rs6YoZWX7IvdZNmgkxh_yzepIhwYNecdFpZCxaelVUwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ایشون خبرنگار باشگاه شباب‌الاهلی هستن که پیش از مسابقه امروز با سردار مصاحبه کرده و بهش گفته مطمئن هستم امشب دو گل به تراکتور میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29756" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29755">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owr7DgnhZWzEihXDkONREjlNX5BfEviamhFIhm_czX25TcsfVGqaqoW4igKLSpNzIfo0WiwG61xKQUat7bzu2fg3Y2CZXrOOD2kxzk4xOmOw9iCkhzwpBqWij0_V5JrtZnKVHKCNlIPGc42Odu3-sAYI6dSc-FnZc5JlVsAjIC007EbSXyp8JE0rMvBPrCuZlO-2-QXio8d18PnBN2bP08NLtlF9sXsYZwruNIOPnov-uocBY3nOXENB7yd2DJOzp2WyjXEvF5Z2a-tq0YgQ_HDZ__Gx2ia3uJS2cvXkZ-UWmxId4bDd0UQ-IAcNqtEuVpImyukQxuI5moDC4yQvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29755" target="_blank">📅 19:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29754">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnU8zvAkAx8RtsmHmZsk1ryyiETESwKcH4UvX86his0jr_ztIw08DJJ54yRdRtPz90Ip0sFx-8pRQLRjCIkLCZu2yXb46SA5QJSxyyCw_igMAkEMSl7_1ao3SLX9zO-jFwRo7OCuoxmKEOWiClYTXPjhTzmtvPma6WURyLUuySAu6gyuZkWy5CnFX4Z7cX9PU35XBdmQoPRGusq090owe3XH8ck6LA8aGAZIgcZXwbzwVe9njDmVpiPfIE4waC6tWm4BxXNmH2IxC0cBvjQHIshECAepn1sZWOhOF3DQdxbgLlRjjGnbitfa751ITcvvSgfBBqSaHznwKLgiEX5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فلیپ کوتینیو فوق‌ستاره‌برزیلی سابق لیورپول و بارسا با عقد قراردادی دو ساله به سانتوس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29754" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29753">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmDrcGZe57GsdMURXmqTCfzPeRTjV6ZH6ewIv2RuFfQW3odvohv-uppZSW49OQtUgsGwVka6yPA3HJCHXfuNFrgcb4n_w188iwpY-vgBuOeAExxe1yCR60iTVpC9_m7YDeqxeWmDWj6fCNB43jTSLykYk55sx7koh-mcGYhraCMdWMAsTzAmgaWla-Y8LlZ7VfclTXv5tSKoFbR8db820y3VJvxs6MRSGMmhqHryDqnh47nbMwBORLMTqvd8LX14Yw3sfVjGz78I_x8yM4A0wcDHQW5WOxZrpjBXhm5iuZYq66SXHa_25FyummOI6-RfxDVqcqkIUjhpYRxfSTbvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛
مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29753" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29752">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWgK72HEI4DgqNtwKe0_ZAn50KKhxRnzOnFXUcKd-JXPVmcpVLlzo_2Cr6_IwKstSbyUWd0dgGl-eknq5oncX0TmrElnimfxOHAVI5XhRd-9CZ5lLuoVrTBPt66A-VAgyLC53_JEF3XgGqrmGcM2kGOr1ynhZ1gUaFtdl_2xMEE6xqZomomBA3iO3fX9IZH1U6jnqMysXpIH0er90kJhCgc30sMDU47609Ih9YiHhY1MfoACCCBF4teQ-KJxTfINWMgHpKybpyiUX9acyBTY-_JjWV7pdEvCw5bhXkrqTBrY4KCb7BKrtTcHNZgq-m85MvwPtOjr-2loGfwEznh4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29752" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29751">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpKJdsUusS8LLMx9CzrhrrM0oP1XKrWljJmttlU52WrStWSoArUQi6v1yMxUfzCN4GZE2Q_2ebE9sXSua8coTQwwEgJMKOoiSlAHZE0qAsKSWvd5LQ5yozargVGuC8gxM4A0YBSWMt8Rn_TQAjDBMh8mspo39KmjEs9x0ZIsR163NzIX3bBYpZiserctzk7bb5WX4_K83xUPVXT4shiYDJ26aZO43YB226d5DDDY7zqA4cHG3LahyYb07Dzoi5TZpVG506R-o3V5mAG2jMTjBInPEeYhYqJ0i-bxIMB0frR_U1d0KgYeEaVv0tiyVBpw-bgqcuuV2o0zilkoVjbb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤝
دوستان خود را به پین باهیس دعوت کنید و
🤩
🤩
🤩
واریزی دوست دعوت شده پاداش بکیرید
🤩
برای دعوت دوستان خود در پین باهیس بعد از واریزی دوست دعوت شده به پشتیبانی وصل شوید و همزمان با دوست دعوت شده و برای  واریزی شخص دعوت شده پاداش  بکیرید
🤩
برای آزاد سازی فری بت دریافتی میباست یک بار فری بت را با ضریب 2 به بالا کردش دربیاورید و سود حاصل از فری بت را برداشت نمایید
💬
برای اطلاعات بیشتر با پشتیبانی زنده سایت در ارتباط باشید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29751" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l23a2naAIAf88uaI0-qxiUi4TyCwOvzeP6VgudqwYBHL63QX-DhOjxczM2ahCGI-lKWDq9XzMTzDbv00y7Bi0op5Nm9sCvPNsyxrYIdAe4fau1-mAbTSeQJjcB2gPD26gbuj0g1VgJ05WpO1dKn-m-bzg-gltzCFP-DA5H_mPNnjXZZvBE85cxGnZ_bYQ_3wGXgCKYaDT4w3UtCuPXwSrFCF_gKjacP76j_Bzjv7JbOEK-ZRegR1v5SGTPWT5TsAAUdkK3qUQgzPpF_Xt0jJUg5n7gnnd3YA8pLcLXRox8i4ny9xBLIj3nxiBKeKRzhXVE5bTpoJ2jRQBQaq0WlX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDJyacazBl2btwXhmrD2hR77ZmsQNXp1MPCAnPXGNI2pNwFsd7UrG6HtHCXztnUlQYEpYVwmCFyuQKfoXGJWGHLE-7PjVkXbX4RTUWi7JmXJtuHiB2Lt0afAqmeULx88jdedhTgqIUIEsn4jhbaesWictBI8mV3lAe0b3MIHrMevif_h4kwimJGaDVVHwAsu848o6jCH6P4B5S1NpB-fViTN_gzsabbP1uCebgZpUebuZUeHYA7Mm-Y0XMbr-BSzQOgzBeT6LdWFyrNecs-tUDsqzRk0T19FVhLX39JYG2yvscR3KOGbYDmJLnwzeCVXOX0Zzbsn9j-6RK2ZgktTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTh_WuCPbBU31XY9iu0FGbTlZa0as6fxKELsH637mYlrSciXBgtDyaBJFdSlAoMmDq5MzMvMdNGjzLaLdVELepFfwtYjMqbMrKSlvEyL_VhJfkG4E-cJavHiFD_dwZUcm-PSCT5W9Ae3N56VnyrOkL8081ZNaFisZCaY3N36zd6g5kTybRoSunDjlBSYxrWxFballURpiSsoHqc9UTX3ipmYNbqxwKOF-SOm9ib6rg-UZ5qCzhjXz99l7NBd-S2RTEmHiInO_OfekugGcdc7A1lQbXOCcnbXrx9lmCRWWvPS5oRsN2fDV45pfrcThOD3fcX0Ejj5ZZtq0AejBL8mdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab3DKu2_WuxLe5wPgjZrDDuWemer4Xn2J96xdfAqwgyFdUxowpXd_IRFCDtAfM2wMnKZiUbHmQA98GFDJKugAoxXkb6lsJelQG8OlxTJZICJJXY0aqR8pNhPnTYY2ZhwW7i_D-m_aa-nHgzOy9__KyCFo5RVoB85EmMGUa_nrVwObUjP1Z_agIuRoqj69pvDwvSeYmWm5gSg0Il3fC4bwQ57cdBqjtSM-SHsmyV4F7kw5kYsYCDMyIj0dnU1wg65ZqORg8pjf3UNUkQb4rGsVGrpaHzQ6UDlLLb7g6hKZyzD_twNibq0lYgFjOyZTO7aZtbZGQqks7iugW1I8Z-7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=JojwUJWAM3snKmSJ-N-uGw2zideIY_y7bxaqSIHxzZ8dLaHGON0s_jnXa0vhacj8uVMYYRrDWsypCnQl8s3BJVLF4LmnpXBCoruGUr98-Lgu8wBXsRW3husGzW-7BJPXa6vAHPuHb3aRofmZZN58SgD1bYU4OUvmrI75xaIOCLmQACaB1JmcMXI2UckAYcVe7CpQaz6AroBqaYfXw7zTbCGDcmVwexNTOto4l-uLhjq6s0eFAmzG58Lle8FkYG6gEBfdvTmEtcd3x9e9XNybvPHjHlNiA8z5jKB4VEBeh9aZOfY8G6qyhZNwfUhOwlSWQqIKDdXyZU3Q8x4aOMrduQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=JojwUJWAM3snKmSJ-N-uGw2zideIY_y7bxaqSIHxzZ8dLaHGON0s_jnXa0vhacj8uVMYYRrDWsypCnQl8s3BJVLF4LmnpXBCoruGUr98-Lgu8wBXsRW3husGzW-7BJPXa6vAHPuHb3aRofmZZN58SgD1bYU4OUvmrI75xaIOCLmQACaB1JmcMXI2UckAYcVe7CpQaz6AroBqaYfXw7zTbCGDcmVwexNTOto4l-uLhjq6s0eFAmzG58Lle8FkYG6gEBfdvTmEtcd3x9e9XNybvPHjHlNiA8z5jKB4VEBeh9aZOfY8G6qyhZNwfUhOwlSWQqIKDdXyZU3Q8x4aOMrduQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtBsziVIpbddCG-RhIikNfKTNoG7Ss9qi3txe_CheoMefJ234vzPIzoQUzN4KYVJ0cR8T-3ldBNT7EqYGwxp52v--cbVl_QuK7zmP41AnrVQl8aqexv2v6x9DZ4cvJX3rC9MFSF6Qim8rbKHVCHU5U-0LcYh0O00NRRZjBhM_0x9yF-j3sG90ncnhVeBo9vzmZAvjkg6z7GT6JczpMMnkY4T_heD2f-QZf2WPCH9DF3iL8ukncYgWZHfe-XujSWGEHf9m0AE2wAcWZDUjOMVzzTI5tCN32exGEz_tIpUIrZTE-yMhVEj4fGxyicNffKque-HD0iO8euFv5G2UcG1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuaJNy3nGi_5sfJV5IJs1Rop-PHj00GgDIjf3PoAlZS8gSO3-1VXMIb96TlrApv70D9keJPeODDf5EjfcwpRyGhvZBFJ1qRZ9wmM1-vQw_wWYlXQXgiL3djJf_xbnpYpFljCrf4fgWl0V7Nrb5ck06Rn6Aq_MNK8Tg2hcxjXRFMVLaBnj1zJstdgyROX5MO8YGYlvfxsP6CcWCmAt8k4n6hBjSOg97YHASopfJ00KigQjtlrBDjb5rb78-OsuebT2hS1MS_Hoq6c1Qerp1DC8l8g7eWttHOCF5Y9muFpNzOfCQL5GHslQu6vEhs5HjXk6-BXzyjqeghHNV7TcTKnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگارباشگاه فنرباغچه هستن که معتقده کارتال باید درفنرباغچه‌بمونه و باید به او فرصت داد. باشگاه اون‌فردیکه بطری زده بود تو سر کارتال شناسایی کرد و از حضور در استادیوم در فصل جاری محروم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29742" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2qRnSYRxSVZXFQMzVQHxdeYmq142mnRZZq1CRnMmDFAi14qBp0FM2f6J304ub6S6Jm8b4g_3yk4nVC_cjeEAnzf6-sBiMVqNJqE1iai31ENEQlJ4UptKKxPCrIrtziONYoRuyuFT7NOivrMYwfW3yF6zZKS1U5EjMzz1Bb3KVP5scYIVpcDtrPwQs8Hr3yF_xJFAR_L4thFed2x0kjI8-d2ktQ2au9B9EgDUkySqe1lew21dJC0e6ujcZQybskUzQsA59qvELENRJfpE8NJQZgJEPyCCxZz94csaMvlV6B0XXxPujahrRZpeHMWE7qjt6_8eL1rkhpSTUnzYYzBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29741" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29740">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyrB8gMmetn_ee61WmZgv_AnyRnb4oEbDLEoRRJBc7vE0V4dCUYziyV6SyYvfmdNRMo8uDeGKpvyrE8YBnFJJ_kOlVtYIrrsHsrG7vDAD6Akrt-5edzDsSKgQXXYQM8PmtV4YpNuum-2IkCEGmULoAwsfpm9XB-MKNgNj6tRs3mxzbr2r3e9Dm9WmH1ZvHheb4GbVJo77syT9renT-3X5kktdCoC8SyYWi2-rWENhjiJhXzEsoAiU7PEBr6EbzAePNHOEvp7aRC1HscuTgNkhFFhcGFPxvQMVZBiP5O_uPxLwbzefOjHWnqQZ-n7WEAUwY_qJM3Mu4LpYscH50f_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29740" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29739">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfDbsFptyUUEJnpQVhoQbyRIzoiEwAkVjpXK3AQ3TvowAY3M7agQr5mF4gcxQL5UCsqACI3x7xhYWCgd0k-phFhZ1Z3M_lVJMUOMYZSCBCsqHDEEf21jVaAtNis43580cFm3qVns4M1GSNgzjwQW1uSD3zc_Sp5QYC6bmqEZSdLGPiMF1yG4Q9dvmq3y5ZFgBKDMBzCgk5RZZo597t3NquQwJx2U8kV8zLVmr9D2xxUedoV_4lqxzDE-ZAendXByYMdXexLC42GDeKR-n38199WQR8Lx2XMYcIyvBPKF7_Ssxe60tPykKKLj06ivXf1LSX-o4s5h7QmNoXP70HHPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29739" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29738">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU2esBlBTIHKXpzCv9hBnIYa8Z54PND27oYwI8_ZE18_5FjCKJxur9scZRo0P7IA8EaEXG64vq-tW3CJuykPhFPtO5SlPaoFCLVv3N1JFtGsYPAwbEL9PqpCemW7J04SDq9kOqpX06rd-Zv-D0g1krXuea4vTMeW3ZIwYQ0mtgm1jqrRxPu1l4AJqN-qkZy6Ux-jdwwiqppUai-G9_RJxDr6YsQDS7p9sP1Wa6KJwz384cJoXqBbUJ4LyfOVCmef0PUrDCMaCT9e7PfOX7fVH77qEmj5NhXTL8TNjjDZGFSvr5jmJR4vZ8agYGU1vUBMpzPxHBDAN05DySpYWXaofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردلامین‌یامال و رافینیادیاز باعملکرد کیلیان امباپه و وینیسوس جونیور در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29738" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29737">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vwOV3nnG8mguZWqhPBahLA-JltydjmLxaH1fC4XfmvoE6pNvgTGJDCDzH-lJVGY_Q1yZJL8Y4f0LjVgZl25E7UWxCyZ_EiPFZ5NCzF-HYd1S7eZ_12I20LCiQpjviaM2uj4Hx51kfAwVFQsVtvEVLDhOzWVbqcqnoe9MgB7mzvwcMcAu_ZY_t2WnHochz-r8V2vxc5qODOK9KEYTJLzJ8RMJG8a2aeFlqsU9cfBln4DPNH0qREebPvCL-Rhsq5iSDDubkfPEI7MpDn8EC6OUB7Wc5q_R3WxH5jAC_AX_J5lV-u1wTkUq69H45JVyB42yTxL8iFaDcCYMykOqj9wyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vwOV3nnG8mguZWqhPBahLA-JltydjmLxaH1fC4XfmvoE6pNvgTGJDCDzH-lJVGY_Q1yZJL8Y4f0LjVgZl25E7UWxCyZ_EiPFZ5NCzF-HYd1S7eZ_12I20LCiQpjviaM2uj4Hx51kfAwVFQsVtvEVLDhOzWVbqcqnoe9MgB7mzvwcMcAu_ZY_t2WnHochz-r8V2vxc5qODOK9KEYTJLzJ8RMJG8a2aeFlqsU9cfBln4DPNH0qREebPvCL-Rhsq5iSDDubkfPEI7MpDn8EC6OUB7Wc5q_R3WxH5jAC_AX_J5lV-u1wTkUq69H45JVyB42yTxL8iFaDcCYMykOqj9wyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛ تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29737" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29736">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcVTwp-QvkooRv_qRz_c75xohHt89mrWNZxp6D6uzY3mqetFJzGJ-xXuNIn21Pn9rLja451TYkiBEWfe8f3ydi0l7VKqB9NET2oFMuux5xph6XbV31if7-eZYULpkn2Hrts9J_9X_orcdbUxCI2gWuS5KDjVJR93qz0IA25a8vj09RZ4A18xlajo_aUhSASfM4YGtCfZreZwP99F-gQAAVcnMFKn5aXMyCGqLwjtGXbVnTZ054eG7QU0d_sZWiQwvQeX6neQ8I3ITNVeSDYwSi_LwQ12sR18OHZtGaJiSX91fsSvFVHCS4NFt_Yf08AEBPwMPLuYAT0udtCxQI0hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان نیم فصل و قهرمانان فصل لیگ برتر خلیج‌فارس در 10 دوره گذشته این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29736" target="_blank">📅 14:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29735">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHttzSDEhM_UTtP03Af9pIjN3uUuGe6s2gBKHjgfOedbv96woZO0oaCw2sOWYdEUAoj4tcHO0MPp8hiERFHaBdElw4C1yi3d5GFYGdCIWAc7NSYGhyZBpZDM7zY1Qkv1qlORZptpd93os3cgWTS0Sfc5733nmsFqSu7aoeIMTEQ5dyZ7ksTqj9e8wq6_WKE6pO07jxAm4ZphBf3IrCewm_XebRCgV1SG9q77T4QIkytlScFugV7Pd8_LkcaO1DDuJo6vtTRC1wdZEm2qVI8uVWYVQtSPhPLXqvugn7QLm1fCPbIQdKOBP8wo2eV6BrnqGxhNBQ2WGuf3PAZC-3ag4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29735" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29734">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2SzVBp9PY3BESHMenSn54dma39fxnIXG2bdDHDsVk2Rv0wLhSmPQSMazS2MXr9B_MNeb1FFnlvJQws8jvGPADmf4ALaOD6Wmtz7Lc--yK39FXig_c65e2rvBUJYe3DLOsLMKnYaaSPzidgzSAl1anQiO99pmDdxIBct7zE4j6jdehZo7wmo4ZZZbWHCaJJygfu_3KqeidXbinbx0TXs-x8Z8aSY5KnOenKtAkN_wbI6DU6LHuBgFzN95-eaIKbfswMQ9DAUZ5ve2nN9mVOHB_8fEFZSy15v6awxcAk9peHURc1TTUcepRlLPJcNrvISrTaCtuEGG9FQFt3TQP7aisYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2SzVBp9PY3BESHMenSn54dma39fxnIXG2bdDHDsVk2Rv0wLhSmPQSMazS2MXr9B_MNeb1FFnlvJQws8jvGPADmf4ALaOD6Wmtz7Lc--yK39FXig_c65e2rvBUJYe3DLOsLMKnYaaSPzidgzSAl1anQiO99pmDdxIBct7zE4j6jdehZo7wmo4ZZZbWHCaJJygfu_3KqeidXbinbx0TXs-x8Z8aSY5KnOenKtAkN_wbI6DU6LHuBgFzN95-eaIKbfswMQ9DAUZ5ve2nN9mVOHB_8fEFZSy15v6awxcAk9peHURc1TTUcepRlLPJcNrvISrTaCtuEGG9FQFt3TQP7aisYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایوان تونی مهاجم انگلیسی الاهلی عربستان:
من‌ عاشق این هستم که موقع پنالتی زدن دروازه‌بان حریف رو تحقیر کنم برای همینه اکثرا چیپ میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29734" target="_blank">📅 13:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29733">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0PkYjjsHHtQDGv2xiqr2XFYvwvUe7E2umcCPqa9GzX0mW7pmR4GT7qjWPVKVQ_TfSmeJKdjfkAgPkS56shZKVLWQw8dRpWI4O_SWQUJwGAeF-DVW_F5HydMC-g13YGWfuUz3tBOdWJbYoZcLybM68vBm0awP_YNAfjLGiVocDArDarxh2a0H1QODeonu6VqJHs3_1M89Z1knXA0i0vqTJysCLg-U9rMBoOl7u19oXKo0ufSRnc5De0JXeChwSbd4O-grEDnzrX6EVIGNI0wGXoKMKxBpR7CR7EjQ-Xs3C6K5P5ClRR3Z5g6fLv0iIO2XMKPm4WlQFZYVCXrs0dlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خوزه مورینیو خطاب به‌خبرنگاران در نشست خبری پیش‌از دیدار فرداشب با الچه: در فاصله 3 روز من باید 6  بار بیام جلوی شما بشینم، خدایی خودتون خسته‌نشدین؟ اصلا سوالی مونده ازم بپرسین؟ واقعا خسته‌کننده‌ست. بلند شیم همگی بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29733" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29732">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQ3m4kLsBNyuNFocs5tBATjmEBQMzd3xmMike1uSL3TOEeX1910ExIODGPMFB5JfxtPTrK7Mf3wY0eKjdDoQaI24Ddmws1VC0tq3KaxFSwcYXjr8YOvROYd_5Qe0mvXTFIBuIRJRHPoyrLOJ2x-YyWlf8bUYlJNVoihPaFHubYsFGgyYRdii-tBSJlGO7UvgwJ74sEt-x9aiwnnAJ48eEADbr5ZVery7ofRUdBfvkberH2SpZ-qioEKefNxNDv0u1HI7Z3N15-yC2Vrz9wD9TlnMqziAIGM3qAicrhSQSbA-iiOh6vHAMMD8RvR-5-Zfkcck-tkejgdTJgNYBUs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیره‌کننده رافینیا و لامین یامال زیر نظر هانسی فلیک دربارسا؛ یادتون باشه قبل اومدن فلیک سران‌بارساداشتن‌رافینیا رو میفروختن‌که فلیک اومد و با رفتن رافینیا مخالفت‌کرد و گفت احیاش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29732" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29731">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak69mADGr9jUnbJXx0LuO1m-WUA55ieYiyuyeHqlx2keExqRx-RKIRPuHeK5TefTUrBXG0aUWNFO4GMJ5GQxet1ffEI1WjASIyU-0ybNvbfxo29VqnLlJiPG365Ibzr0_CXxD2NTcVhgPyJMimcWF5RT83UxXKxtvOq0ecVhIyenjTZkSDFeCwGJMMBXvG1vBL1I6fKosneoiYYWBl_bw9G10xNBw8nPB-ZWKuTTdGq0QS7yOeWG0gjY8Etvhk30qmi7Fbsnf8Oxq67-9J84FY7vh3bW3OS6bytpJSYWGDmhlx6U4SsTcQBb8GUipZ5nXGg7oIn8Osfgnntul0UD-qPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak69mADGr9jUnbJXx0LuO1m-WUA55ieYiyuyeHqlx2keExqRx-RKIRPuHeK5TefTUrBXG0aUWNFO4GMJ5GQxet1ffEI1WjASIyU-0ybNvbfxo29VqnLlJiPG365Ibzr0_CXxD2NTcVhgPyJMimcWF5RT83UxXKxtvOq0ecVhIyenjTZkSDFeCwGJMMBXvG1vBL1I6fKosneoiYYWBl_bw9G10xNBw8nPB-ZWKuTTdGq0QS7yOeWG0gjY8Etvhk30qmi7Fbsnf8Oxq67-9J84FY7vh3bW3OS6bytpJSYWGDmhlx6U4SsTcQBb8GUipZ5nXGg7oIn8Osfgnntul0UD-qPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ بااعلام‌مدیرعامل‌فجرسپاسی؛ علیرضا بیرانوند دروازه‌‌بان‌تراکتور درنیم‌فصل‌با عقد قراردادی تاپایان‌خدمت‌سربازی به این‌تیم خواهد پیوست. بدین ترتیب بیرو تا نیم‌فصل بدون تیم خواهندماند و راهی لیگ آزادگان نخواهدشد. بااین‌شرایط باید ببینیم بیرو درجام ملت…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29731" target="_blank">📅 12:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsB9zN_5jt9nfSTRUhMFuLploxZ7XMIRO3ypYAYNrgweY2xA1QomzNdd4wGo1T_97YWUkKmI1SO0jcy12Re2u24lA3GvlaC2pDk57svU-83Ctqd3gujkA5QD0Cxr5uITQic3lMAmqFBU6nw8VgHJjHdB-jCowNOHV3pWtZAHbFcS4qtWMOatEb73wpqqco998ZWNT2Uk8RcA4ddroByAvrFJGB-QkTn8VPUaZUqg6-DUD5kTAe-cYs78ARelm3oL1CS5XQMfXCEoMq5QonuPl45ehcItLEmTId7IzG7jMBQIm0RgIIxt9Hh9fe7YAx8wjldceIkE-87z_efJrkN6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده یاسر آسانی ستاره آلبانیایی استقلال در لیگ‌قهرمانان آسیا: 10 مسابقه، 9 گل زده، 1 پاس گل، کسب میانگین نمره 9.1 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29730" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=LPXDFCmhWGD8g3S3YFfM9CTR2lcdcti9rEpMlefy4NBQCp1jaHDF4OSsmNrj3GGOtbhsX8EiGc_QHiAEuA0yRz988YViXtgzI505ldlvrNCN-10tJI_ZlTh-5YiYxrjJKifZXVMEgIPMbK4mU2jUmc-ENUt9jNNtm3GeyYftT9a_qlyuQaMJQaaQyjSAuMJX1QfDGPFz1y6qgNAgl_7grP5a-q6p_IBWpAdpoTIJ5HHg-jNy5kHLfzWz6dkf4o1sQ5LRXP0shb9NjHIMgMJTKh2foc9u-lQT_4AzNy2dgb0G7Vf7m_wd5wrVhfBhJ9ebkLLu_2tmmKsgPGpq4rsQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=LPXDFCmhWGD8g3S3YFfM9CTR2lcdcti9rEpMlefy4NBQCp1jaHDF4OSsmNrj3GGOtbhsX8EiGc_QHiAEuA0yRz988YViXtgzI505ldlvrNCN-10tJI_ZlTh-5YiYxrjJKifZXVMEgIPMbK4mU2jUmc-ENUt9jNNtm3GeyYftT9a_qlyuQaMJQaaQyjSAuMJX1QfDGPFz1y6qgNAgl_7grP5a-q6p_IBWpAdpoTIJ5HHg-jNy5kHLfzWz6dkf4o1sQ5LRXP0shb9NjHIMgMJTKh2foc9u-lQT_4AzNy2dgb0G7Vf7m_wd5wrVhfBhJ9ebkLLu_2tmmKsgPGpq4rsQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛
تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29729" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29728">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdnldCEQknoU2SJxor5HRL0ebrC-m4n9aywmQsPAngHeXmSiG572mojjHMP-syMOx_sZe-xz3Z71wZSDdgS795XzBzWBghE5XMn5CdqkdrzRNs8tgeBiBY-i837JyjsEDLbe-ivi05AFVcfSnCZzWsxipGrL0ioBJDe24p7ZnZ2l-JjTDIjXNwXLAvjBZ4ubjcz1JZOApHNRk-lH73SwOJFJPx1K97u3eLOa57kPfVkwcECh-gBatE527YarGVvmYMTnz1n7qWklOYYDznKmj_lqGK_84UZs371qhI0sI078bPV2pvYuzTRm5tJAzj9cg3oaJmqgBFMLM5t9WFtDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29728" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29727">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnr9-O2hlSsSWfdroKoD3_mvuJF0TO-S0VqE2i78gLggUd83FICp0mIKWtZb-XHZGmWgKP5I6AfHscYUfFKSqDvhLqBbdxn8nN-T3f5IADIVKIACqVBf4cMnjgx_akE3F85TPLUWSbuNl8lkSCZl0IbndTKo8LcWA4kBEmBqvYjYHkMll_gJwII4siqTJ4AEk4WCEPzu1iggLWks6SmUp7J82rb_4WUGL9iU8ONZozTI6YSxj36zGxxE1rYi5lSySmMXwLb015UxUQRZFH-CubPBAXIXWQu7o7AXJiPzhHS2oX3V_kocDG6Nqs-JNgQwpJ7qg4ZMCCLht5aJh1SjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29727" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29726">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29726" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29724">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdAPVHFYmTqqVwa8dCQuFSFl-qgJdBCM8wqd1JuF9WDZ936QDBoVPCZD49H0i7ZRG1gnd5A613lqm9JKwjbC7StD68pVSIsL26tJ43pFJg-e0fe6-G_kAAIpi3vdZEPzduWegUeKzsm8ONZL9lUkitd0MZ1V9YVHPyhe6wXFCmlWdlqh2IiYN_rXLjJ8HVjAqGKjndSVmrSdYoecVY4ThEwgumP6M6NPLKyx08-OMhx15X2h4iDvm8-Ob5L1AnUNUtTxqkYCckFi6dNcK-LHJFAoKqejo1-5wQUWjENPQAt-0z42mFHaq_STzUz44J0q48zbxgPrh3CxfpugSCUWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29724" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29723">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کل‌کل‌های وحید هاشمیان سرمربی سابق تیم پرسپولیس با پیمان حدادی مدیر عاملی این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29723" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29722">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKUgiXHybGzrMaEyZouJMiSW5adAJN1KICpF25-2tfWbxJaMX2cVY6DO0DbEH-MpIAYeKf96Ul6XrBgiekP2XcjPmlqMON4nqF1Vz6X6ZvO6MaYZG2ae41Z5WyUBQmy3SjN-ZOKXt7EziqYcl4U_jeNzwuoWH4ZcTqsyyPE6GY81-bEhPLwK7pijsOQKAGj17-UCEEA7xnBEu5mBZL6274CY_9hQy39UWX91w2DPQEW9zMOSswiy1AY01QcXuxggapW4nGr-fxcugsdkqc2k5LwxbxwQEzjL8vxJxm6EH9IFFvQnbgGmEWNcSy2398G-Jk67BLRDrx4ZqQXEYVt0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند دفترچه خدمت سربازی را ارسال کرد. دروازه بان تراکتور از اول آبان‌ماه ۱۴۰۵ دوران خدمت سربازی خود را به‌صورت رسمی آغاز خواهد کرد و به مدت ۱۸ ماه در یکی از تیم‌های نظامی خدمت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29722" target="_blank">📅 10:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29721">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-hE3TFVAgLgZycnY8_u5ylWPkZjXX2a2QpSGc4YrUMks3jJ_GKt1pPx44JfK3dcHKDCM7J5Of8xQIolIWQn0IcmJBsY23Hnl0YNuZ3a76OSmO2qmM-fPPqRNqoR6SMzfof7zYa-0JNONFV4GyLfDsXB-JzpkHv5X0YrkNQpq5HmfQl05vI8Tu6TJwbbyaJ0NgCgEfAIBi267YQI4vkSHpDO-N7_fag8-j6X3LzrtHV0YRHRMPLqwpUttpdiAEJctAs6M4CuImI4SE4hal9a3pMp7Gyr2W7CYKEZ4IzEMNsrDiMG9NQUJVirjW5yEn_iJ8a8SE57YQpg9YIzsEhhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کمک‌ داور رقابت‌های این‌ فصل‌ سری‌آ هستن که در بازی اخیر فروزینونه
🆚
فیورنتینا حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29721" target="_blank">📅 10:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29720">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1TD_UFGE1-VF-HKwZmVx2f-y7CCl2xPpzSY5lDPoXb4dpyboV9skdgU-QFG2r7VxH4nQTkO4u7__2f7pUvjwohTTD-bCcXsYhDp_ZyIxZGUmHn-nqa81kV7nSDtKVfa77jz0X8MBQPzahoIBaRzdTajUVRhEWAMxOFtoors34ob4CGYgJ7T6e_ODfIjfaE2Pvc2uoqcJ0UgP0hfb1c81R1U2YHEXmNjApEMBg9QWW4zuy0rm_Bxbi62X0M1p_w5NmY7HRaZ5Xff0J_x9v3onlRcgpLmBtwMfZVZEFB88nK4XHOByCiDk-Cai90x-rXH4VSjbdpDK7b6XaOteH9nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29720" target="_blank">📅 10:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29719">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUzkp4IgeDC84p1mEOk-PqXrhfZh14PK9CJWAHOJUGdEYYXSUH_qVotjowEDzxOCr728YvPhnm2h-NkYydQS9Wln7qCVxCs1Linh-kRyAGeTEmFf7avbs-Ug5BO0N2jGAuvVQDtOu1PpDa6_5k-cZJoDjMKmJI1gqyge2D-DBtAejctp40coSVCYDoYaU86i5pFd-lCjLEyNxl6Rlsmb3dTAQgpBnUZbA9sZcoAh3OLMC-N4bqdgeuKtCxZVLJpNrfq6sxtXz50wDu-tA--gBq_PsAE8HrnkFBwIJJXN8qJRA7AWfsq66wIQytjtxQPRgiw-o1t-6h7KUVhcrOdvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌لالیگا درپایان‌دیدارهای‌هفته‌پنجم؛ عملکرد خیره کننده بارسلونا هانسی فلیک درفصل جدید: پنج مسابقه، پنج پیروزی، 27 گل زده. 5 گل خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29719" target="_blank">📅 09:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29718">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-1_WOkhm_ZnRsj-g0cjshLhmUjntFBRI8iLedUBK1EO3sHfJPmca2DNzpoAKa1wStMo0P-DEyqcDlG_T8NpuXdEpbV_yurrK1zGTm4FV9AC3qUP64mFgx0fOrnB6l-FmncMUO2fO8JE-Ra7mezNVi1s9khcKTEmwnmkisRByD46DotI8ldfTBoi3NIThae50u7A0pwkGknT1NQiitPFCQREJls7auUug0lBOj7L6iYMw5RoDdxTeIxaZGqgrxH24weYjzdB831AtzSg0xzYxb1XUmvZTwWacYkbo1Utkayh5E7tDj10gNgGlnAMDbty9MEWDasXoVyt4JtcQxtMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
۱۰ سال‌از شبی که قلب پرسپولیس ایستاد، گذشت؛ واکنش امید عالیشاه به سال‌روز فوت هادی نوروزی کاپیتان‌ابدی‌ سرخ‌ها: از آن روز تاکنون هربار دقیقه ۲۴ نامت از سکوها بلند می‌شود، انگار دوباره برمی‌گردی به زمین، به قلب‌ها، به جان هوادار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29718" target="_blank">📅 01:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29716">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJqUNQ3Rhw9ph0mOI0MTpUOusneQjuNe4qmcnGcFWp-2JwMeOPY6Lxnr8BCixpdcIRb0Izd_9DALkVLSpyYbsibVYeN0Jsu5Q7HT1l0qfi8W4j9QjjGi3d5_SIdVtjSiicbgmpF_ippPWo3Iz1NL1QvfwHjBj9jY6m-a0n41xwKdVe3EGPQmYCD1ADz6ItHY58vF1fUyQccgONUWbuoBU5gp6f4Tmpug8Ljmv3BTPAuX5lmLBo2NL9iaGETu9ufpjPtSHSz1f2sIHtuRGOrmJ9sWPgXXAgvjeqTRS-G93aIO0dLoPlR9_DU_iRAzfZT4bBqsVWw50Rnr71BYQM8cLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ا ازآغاز فصل جدید رقابت های لیگ‌نخبگان‌آسیا با جدال مجدد یاران آزمون برابر تراکتور تا تقابل استقلال
🆚
السد قطر در عراق!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29716" target="_blank">📅 01:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29715">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkOv5ER58yq5uJNTcvGA0EEVPsbRJ1rjIYM39ZFEt_uczIWMaK7UkCvytsEdURTyliYUAONSOFAHBQOlJ_IpWOz5nMe4rZ_y32XN5VlotXf72yqZHa_k68YkA33GG06cLWtZi0xu9446X3J6GTj7WAE9oNSxw3cpt6rACI8Tp1bpEcLz7H8s2rB2Ikxid-N2VnEeJ1Cress0VTFYWDQNxrO69J2BEyqJJYmdXY1C8CosureRxaxHoR47qZX-XNd-nrtocwzfowZDR6XIlNismg5u0lFHbBmO97oQkykbxTQ7JOadi1ie1EFBjyH8twNs2mRHsXBZ8Ctojd7E0scASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌سخت و پر حرف و حدیث سیتیزن‌ها در دربی شهر منچستر تا پیروزی بارسلونا در ادامه درخشش‌ های یامال و رافینیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29715" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29714">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXgoNE4s6aILmWohGZuNTAe9PyHCE0KtaIDZFq9hTLwFxMJiroKizTsRl9KIlv7CPep33BQs3thkSpqK1BoW7lDuh4HSwq4I9XSA6iGSzsYU07yo0MbDiMkQVA4UgI8u6Q_0ctXVXEwtsKQEtRXkkb0Zdeog7WwyZ-ys4PjY08CEea0hatPRgrq9QlYy1t5AfJVd7LIIZ0L-R1BB6UOl5_zaHm5-kCwhYedQPF54Aqsnp7S_ZZLsWehAiGrl9Zk4vCT0WdRx5NtAGNt-r4mc9w3YiFWK8u9KDq6Js_eVfGXaZaKNXUY5zfSfNty_dPLR_IjQKU75mV2ZHRoBJ9utBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل تقابل‌های استقلال
🆚
السد در رقابت های آسیایی به‌مناسبت‌بازی‌فرداشب دو تیم در ACL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29714" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29713">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er3F91rYz98hBXqtf8ytaDBbcNi5l0JQcJvYOUA9Ej1Ad_9npMKT9ravkzs1LSlbNS6RXNmyXsBD21CnOvSKiddMWGFlmtr6PXVoYsSoLDfm5-mDgY1S4v9TPAca_jFhMv_-pksm9OY1owshGALxZ78Q3NRutIEIwQ6lGngZAV4Axroqu6hzoWpMzglGhUnpowtXIB_U6jzL5cl9d4xTVeOwtkqs8sQnLM85U1samhgtrjFFU0e0omkY286-7ZFEDbfabmJrO6ekdedZHyckBOMeJOqdGtrMq7MWj0HJOatyDw32_yGIB60WD_7NE2A25aVT3EBsdgIAqO-W7_O3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام مدیرسامانه هوشمند سوخت؛ خودروهای صفر "نو" بالای یه‌میلیاردتومان فقط میتونن از بنزین 10 هزارتومانی‌استفاده‌کنند و سهمیه بنزین 1500 و 3000 تومانی براشون حذف شده. حالا سوال اینجا ماشین صفر زیر یک تومن چی مونده اصلا؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29713" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czsecV5okBPJdSi6tgrL8FNMDDwyQ2-usGIFIJRu5Jqjz_4D9-SvQHAYdY7zWqYb7YXvi5qh4TojHvN0SLM4DF_cQyPJKDHpf2SJyvgeqA1WSDfPjrzcKyxHu9CI2ehnY1z4GDkj_H4IEPj63lT94dgAvZ3oVCoYFw4U9MgUXXDTygFyWx6N_tc0p9Jj2xZWH7_To0CRpKoih2Ar9yhCjlgrmQhnw8R-1YWv_sGHOu3fW_Swe9PkPiyqCNR4-x0KRcW9iUagdfwvdzSwJSNdhW6BQAGbuDKcXxA1xKkn3_Q6pu0ckAJobLeTCC2TqW3QeS1-N-IYahchJBDoja094Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPi_9shHdvo8-OfMMlcv2mLjCq7DfeQFpZ3bcaYl1byhvbesonEDwpRrQlw20a2QR_nRVChxoCfNPKU_vvMD4d6ECT9SVgGga8w632eV_VIsNqFE0xkRro2q18vd6w2b5qXMj2lSb4xOBBgS9lwG2Zlu1DUZjyHsr_56B9-Kcc2qRqz8Xny_OHhPmVhBN-e5rEeppIOCJ37R-MX-EupsaUuZ3PciLt9EKkfOck4e5dLVm22ZVWhyzIxJj4nr1gdIEpgdvu-sHJNsV-HZAE63P60s_gjycy2Poq-U-Ks-hIAphprQjdVSum4oOzzTRvNp3p0xWM5YzbJyOmVnlV0eUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCXaUYh4YYiidswSZcqrXivRE6Dw5J6QvQkIROW54JXHP_oz4xuHhWXvOsZE5-wViJkKo_CFTxHSbsGz8BMd8GAn5fF33nnlKfXYwO2qxlxhN6F4UUh2oT4kieAXK9orP0xERO6HjqnG6eJRQiEZOyFhPS7jIfv6q_RmgMrsGawHkBV_g4t8Y3CLkNeF71L7W-TpeGDUwuZBKsHa3U-Qh-IBvnICA1iAj-bYGGs-Dm4SCa_KItrL2scJqDbFnPkBk_K6-Q_TVeSzdhXwWn3KvYShqc1V-V6HCh-plfkjpMS2AR5OVNxYkA1gdqlgtfZ0In-yarYouYHEYowjO37bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29707">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyqSRM677olpPoCZ64wVwbM1kn3p5ZJoVNDRJR9wJw11zjnPnSYo3ormSU4rhY9ME-6siPKgAOyYjX-EXhlXHrk7W0Q412brMmxTiEe1ErFSnQ42NOlhxdtmL-LIJS4sl1Q7A7hBsQP1zkNe-A-5So4KGN874hfDj-dhOpgleD5gysAhq0ZFzJ3_MTch7Vg7lmbPaDq8rrWhD7L-m2HpUnt4EWgCOku3noX7-umDKTGEmnLBTUE5E3MMZwVdY-L0QWdl5GYGWVwA-lq860zIEBmVY_bRaJMt2950XgZT_8RQb6eqWqPELTPZuZICd-PMo9D4PH2gXYKL8yz1EBR8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق
؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29707" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmvRdvSkzIvilP6-eP6_iHD4VrpNmdIF3mmVRnDP-psX-pRErUf9sXazgUBazMoFUMAtwZPMM-ro5j74ZCmTKFODFKVyZxJlhurXKzgHqAoJBjt-L9BluSUBX4h-Jq3eYLCSFFLmlHuD6huIZNqjKJJUpQOA23nzeh_SKKzpB876hTdYIO1pJpKCEzFL7O3bkrx4tK0dJk2KozPO2GWZxzAbY_OI1YgjDY9lE8oTqlMamPqadTIEDW5ZYx8rjzEiiYCf_OJsuodRz1pKMTr-I_EuW9sIeED1is8YYr2ZQd-uCTmdGxcZ2cwz31sX2aNaySbHCl5uNtOz__ssMo8fsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSA_4KkME7yW7ahXLBbvBTHsPhJ5RlJPnpMf3BFcuc_ItX7BjVGOLlCRyQ6rwxoGKwIZkcOcvMEhuYsHqF-fiFQOe5uwrO3SxWm9UG45N_l0iAqCB27nOIr8qy5dh0caV0dCgqYnMDYNGdjlnLmXji8dnJyGDrCm-ID21YLUiI7cxrTJqTWOZ6xLXClzslgZPVOtvCTzF1duGJ3t_-hR4TLESACROSZgrwUPQfHgzeWP6IsPqXNqu_e6tAldg5-eSlybRVJzO8gHfu7hoUBGfgnwTeOXfzvX5r_IZDmKZM8u1jYz4bmVhigCmaCqaNM-31SDG0Hu-qTH15CHW0WM0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29705" target="_blank">📅 23:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPhWCEYc08iTWINZ9HCW0jyOuN_RB19nsUyqYIFrEXX9hMbfuR0ExO8KrXgiZBKdIzb05d3Z-AniGSesS3g8AXdh1cwIK0vA37Wp1O1kkli2J4cTcL0TbmfXQ3bffZKX7oJUzRH6J4Q1NW1vDKHQwIAqS0UIHKOBp-wtK5EgaWTXk5014QzDkO9riefOHKqbxqgqooDEwkzz4YwNPGdeclQVwcmX2Nm1YxwogEHsMhiRpuzinSnHcWJzHVDs_0ztPV-BXsMcmhphd0ZecbPrD9fz2WmKoAKypsgfofkWo7msrC2evSZ_PJMPHNsAbVfbBqGHCEsCF--wqQuXZ2EdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌ چهارم لیگ جزیزه؛ آرسنال میکل آرتتا با دوگل دیدنی گیمارش و ساکاساندرلند رو شکست داد و باچهارپیروزی‌پیاپی صدرنشینی‌اش رو تثبیت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29704" target="_blank">📅 23:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMs0jkJRT03AGjIbNykOGxzeOg_GO0pZZig5ausMhAuKuCvSg0auYdm0aevSAWIzjmUbariRsqFBulGZKz5_oCKPHr71hnQgJw3_ev4g12tu_f6lrSFiNvKTqYMYBAX8Zq0mAhbRi54wK9PMifh3CURSuMG8mbMcyoSE4UvmTrvj2lpNvoh4o7dsS4uheumxpusS8NDNQNCB8ugIlsDgbYKJFvtbLJb5HgLD2mk-_UKDVDAQWLBVIZbL1w0c3yGMBcQmRAS9CLjHIKpF2yyDP9t-mlFTQ_NCNcAkFgez__LjqOL_-tBzyhS1ndXnznwKCmp0xaMrAUVo1epXYzsM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29703" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780ec53923.mp4?token=SBcvpwIvEP5PARIiWjTjMdavfyZm33O6pU4uSYeDJxWqtInpjrG2Wy5Ie77833TVWt7ecS1Js9poKV96he97GKhtZXNoiveM2MlryvTOunQZhI-vlVO2fcVYQNTtq70jVWY0ecjFpd5-sj1h46URFRp1_IVA9XNF3EGGn1fKEciCi5ccld9Jthz3RyeUqQsd4heUW5_mlXz75E076FjfGkqt8oXsP8QEd9jVXm0CBWz6hyMjzxgz_Rd6ipQ8LXG5pEGvZGmyOn-SebNyx8WIXtISjFA36ySF7p7xIKr1d6OwaGYk2gQh95os9eR_RER_ps4SaEoZ6P6dzXC9AlQsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780ec53923.mp4?token=SBcvpwIvEP5PARIiWjTjMdavfyZm33O6pU4uSYeDJxWqtInpjrG2Wy5Ie77833TVWt7ecS1Js9poKV96he97GKhtZXNoiveM2MlryvTOunQZhI-vlVO2fcVYQNTtq70jVWY0ecjFpd5-sj1h46URFRp1_IVA9XNF3EGGn1fKEciCi5ccld9Jthz3RyeUqQsd4heUW5_mlXz75E076FjfGkqt8oXsP8QEd9jVXm0CBWz6hyMjzxgz_Rd6ipQ8LXG5pEGvZGmyOn-SebNyx8WIXtISjFA36ySF7p7xIKr1d6OwaGYk2gQh95os9eR_RER_ps4SaEoZ6P6dzXC9AlQsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29702" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY-zbcrZ-u-h7ecK63N6trunqHV9Z6G2LjSq_uynkzKtrWEb_DEUYyeI3EACTxFZVRj3uL1kooTsR4s_ONWLvXPnYeAaZPAU2Lh96CWvHWm-o7EgtOBZx3nIv-bd5q2hVdBntoCvSztGh1hB-4xm55j4GPrahCQhlGXTIN6oxKzAhrSPF9RSYdp2ZWxngyrrHGWNV0dEP48UwPrrQzQ3k89sbU2X4EUiR7qZQM5HbeYTaYbLk56JW_b_sBd_6_tO_b98XkRSgE-0UZhAqRL0b7Ko0P3KpDtrFQjwag7JTHS02e8gHaH7VANEz1CHKrf3OLqffoYf4YgXhHnyGWe-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=gYoRvRkJmqIIjHn20r4oOuR5ueX7jDgqc5RkogSWSNtaeOXu3aobQPYaQ3fuL0BBjw2AvgMkhukcQr1xa3NWzLE1KUuCxxxAbLfx5E5_lOELusvXadb4VcPnZrPZeeX3h2wyLGPOF1nMuKcZ42p7XlSipkCyY9BLcpDGaOywIysz-aFbghKtdJHr0ODl0a2DeIKyubT3S8bnOkyYn_Y8cBi7_x1OhVlwtcLGNNAf77iWuKn8VO4plKisZmUIgg_I0Jogrrn0VzoJeLNBmdTQUFf7dnL_V55m33skum1Du8ZgKOIgsGQDCofZYvVPI8_iR_eFphj6zLyScM29gbc5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=gYoRvRkJmqIIjHn20r4oOuR5ueX7jDgqc5RkogSWSNtaeOXu3aobQPYaQ3fuL0BBjw2AvgMkhukcQr1xa3NWzLE1KUuCxxxAbLfx5E5_lOELusvXadb4VcPnZrPZeeX3h2wyLGPOF1nMuKcZ42p7XlSipkCyY9BLcpDGaOywIysz-aFbghKtdJHr0ODl0a2DeIKyubT3S8bnOkyYn_Y8cBi7_x1OhVlwtcLGNNAf77iWuKn8VO4plKisZmUIgg_I0Jogrrn0VzoJeLNBmdTQUFf7dnL_V55m33skum1Du8ZgKOIgsGQDCofZYvVPI8_iR_eFphj6zLyScM29gbc5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmU0XKzE4qRaGO5H8634Lmg5CGWQKVa4PM4r9QMP4BWAi7ZlxUpOs18lzivPywxfT37TeZ1jfZF4iB-YefG9LkqQtl8fBX-p4vqG8tj2I-HxBuMGNCQyFtRyqoW44xEqTD5EEDM81lvubal5f26WuV_iz_Ku96sm5nvBMaYcKBsTT4K7wCDZvSFHnR_MFuLiir3NyHEIlrWNVprbJWzdO4vy_lL7qZ8Sk7NoFF2EuRUTGpz0kLqOkhIxTtt6mMLzj-ln86oZYeY1yGo_HxuyzGxdTkt9AjOrCIfeaZoxweUHGzikdTFe5l9rVAyZzQGLjpXKB30R_Mkgk19m4JXYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFclwxfMwwiGBC6RRF6eNohcSkPcDUSTvVp2vo02Vcz6T3gCBpe07GNyHyYaQICwxt1s4mdOvGUJ430Ffzqcr5KTSG_nmjbbW07kNrMecujIxB1d0g1B5d2Xe5V4Orc43hKZk7jLBhK7TJKeJFBBDqJzBBRf531plVY-AXfd0u3jZmqWRbL3hp2YMGtkMJZCulAYHxy5JOV7bFxoqb2D1tHVDGRn2cvPGqbChqIkMESXp7wCHdD6JVtzifO0wPLOWppPxgCVwRSNUwLZEw9YKJSJX_sMLH8HgoQ9c2cCVseAcgerq4D8U1-dACu0C5MsTBd2u5nPRlauYXKA4ANYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO_Oo5K7EQ630Gd9RglCT0R7j9Kxny47lQvdbAWkaCtRu7sa6_w07Ni_1wcC3ApOR05v0RcK_6wy_NZXnL03Jv79kyw_NHVzoypwhVpQAhFCs2zRdSsZrAvmQz6WQkkSe3j9yBBztSZrUGk0IvqYygMfpjuOzZGlDmZ4gD2gLeGpYSI19xiAJlD9rCuVVmaHfVNgO0YnTBWTbJI5lvdR3UNBQlFWRsZoVmjS8YBUtlHjaJaBS3QcVn3Gd4KChwdt9oygdlw9w0kkPQRYgjT7DL_A5iO8yckthg1ikOZ3Ga0dJGRKnvE_kLUn1B5bLDYLYQIb4cFr1OCnUb1qr4gOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29695">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=BroFCVvCI3kXqSnj89kOzWYsa8F8_mM_KxmEMOi0DDb0yqvyO-U3ZTMxCy_MQP8kJuMXin64lth7FQ-QP6y5tMPH-d-VhDIEq5mhIzT-BBXelPkwMZlSNdw2gXdEbI1RmV8lF3gtalgcByJ12EeiTsSUcOv_KzvK6JkL6ruRkoKOm6JKUxsgaFSo0xNwHx1riSfKGf1psFaTmKxv6mxoN9aNZWrKKRDfpTTjPGylfzYy2tRol1OFZoEtdOu3_I9Pu8Pk9PJrulGfxma2gtlJgeMEc8jdw2HNhf5xexQj2iASOb1T5oKEX_W1-f6FUInBGUzOs0fYp_WcaWzlbqtEUGEDG3LfVuiEgqRwnWsM6Ty0qIi-AT0dViqdxxDXPeLvfCO4pJT6x9SuDWXtFClzP825c__AZT2u20vksv42zwgZ_Sm8VdkGhKU-v8TLJTh5-lMy__oBxmKXWkrp8lnhD7XA3ntNefmN8VM4XM6hkhcZ5aBPfcIuwXZWlmHUR-_1jMtaW5oxMViqMpSkfhiMXthzbRFXxNUBzXwclCu7itfqwE18Xd8jRy67_4-z-BgPAf6Z6dl291B8VH6TCMnYH5uCsCGsisTEEaStjm6ot0uWDVfW09PAj2X6a26tGKNgmOLHYm0De3bJnPuKZziwgxT4GhoH5nCrYjfVBfk6lRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=BroFCVvCI3kXqSnj89kOzWYsa8F8_mM_KxmEMOi0DDb0yqvyO-U3ZTMxCy_MQP8kJuMXin64lth7FQ-QP6y5tMPH-d-VhDIEq5mhIzT-BBXelPkwMZlSNdw2gXdEbI1RmV8lF3gtalgcByJ12EeiTsSUcOv_KzvK6JkL6ruRkoKOm6JKUxsgaFSo0xNwHx1riSfKGf1psFaTmKxv6mxoN9aNZWrKKRDfpTTjPGylfzYy2tRol1OFZoEtdOu3_I9Pu8Pk9PJrulGfxma2gtlJgeMEc8jdw2HNhf5xexQj2iASOb1T5oKEX_W1-f6FUInBGUzOs0fYp_WcaWzlbqtEUGEDG3LfVuiEgqRwnWsM6Ty0qIi-AT0dViqdxxDXPeLvfCO4pJT6x9SuDWXtFClzP825c__AZT2u20vksv42zwgZ_Sm8VdkGhKU-v8TLJTh5-lMy__oBxmKXWkrp8lnhD7XA3ntNefmN8VM4XM6hkhcZ5aBPfcIuwXZWlmHUR-_1jMtaW5oxMViqMpSkfhiMXthzbRFXxNUBzXwclCu7itfqwE18Xd8jRy67_4-z-BgPAf6Z6dl291B8VH6TCMnYH5uCsCGsisTEEaStjm6ot0uWDVfW09PAj2X6a26tGKNgmOLHYm0De3bJnPuKZziwgxT4GhoH5nCrYjfVBfk6lRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29695" target="_blank">📅 20:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29694">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPxMt3wWADD7B8cURNk_fgZROBDQQXH2gAAU-ZYoGFekeowMNd1iGzAQFNHdUBgL7oHcz-Jy81sAnTrc_mBu7OFphS1EPpykCj5WTuW28_PKElP8UiLEL014x27wXBEYvpWwsFfdU7ORZH8dK9IY4A-yUDi0bPs3lc5sq9ZT9_Rjlk-vvQCjRTo0G5E1nIzpOTQz25oHk0xDE8xuS5DCxqHMdBCQMy2DXWAp7hPA4rmirQLBG5FgTO-qAiE6r_ojAaAHU7iRF7xb0OqyGae7rSSVfKXXQL5GBy4QdCSKZxR7G7mKr3YXJ1s_iBehZRnHvaBoR5tBt6kHw9uMQkttMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29694" target="_blank">📅 20:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29693">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmLJA0p8Y6odV7XAPqKNH1HxkTg0ocGpFGpyEt6ozohDH7wAcKflkQ5ObmDpxDhTHpe_P2KGcRE670osDk6Ba-LNy8hRTQcrCAIWWNLtSiuGEv_j-7wZzZXYvEIwMZrKtTzpmMmkjye63uVUoDBsnfBAzYzHXhUDXy1nehuZf1_hDzRwwmuvOpA-Hvmr8-Vm_w_igeRDj9bQyrnqusz6tkmku4TX_QPmDi_0fUFKaSfUK5DLA95KUIJSOWSdBY3Ed9D90h1d97DIcbdZy6h0ZmZIF-WeiDadXI9B2q4-s63swyz8TUD0YmsmnG31miOmAmnjoneQHzPjC-0cVjp8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی و عجیب اتحادیه موبایل ایران: مردم به‌هیچ‌عنوان‌برای‌خریدموبایل عجله نکنن چون قراره خیلی قیمت موبایل بیاد پایین. صبوری کنید!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29693" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29692">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=XDROIiK7h7VVgetbi_lhQqUtBFTcx6It4OgV4k8qnq3UuMvEUs6CMObDI1mDDbuYcG0sywiqeDLeFLObQV7nn_uUx_2A-seeTSnZKD92zxpHUCrO1JMclS15H8lAzmvPz02zAO50enQicylbhI-QFUf3u6OmEwU2vVr15AOhgJdjhYnULIev6oGDtKuvfiIc_-8IBYCJP3iK3z8kqP7Kz7SfDG7_cEoe8OD9NPZfrDsEl3FboNi5a1u__XeMk1qmnVTeuRhmBfuH-r4aMvLbOWh-5S4yjgzuK9O6IF7IlFtIM1XlTu6VrV_0GP_n13mTFxQQ6RDs_mPzlDp4BgL36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=XDROIiK7h7VVgetbi_lhQqUtBFTcx6It4OgV4k8qnq3UuMvEUs6CMObDI1mDDbuYcG0sywiqeDLeFLObQV7nn_uUx_2A-seeTSnZKD92zxpHUCrO1JMclS15H8lAzmvPz02zAO50enQicylbhI-QFUf3u6OmEwU2vVr15AOhgJdjhYnULIev6oGDtKuvfiIc_-8IBYCJP3iK3z8kqP7Kz7SfDG7_cEoe8OD9NPZfrDsEl3FboNi5a1u__XeMk1qmnVTeuRhmBfuH-r4aMvLbOWh-5S4yjgzuK9O6IF7IlFtIM1XlTu6VrV_0GP_n13mTFxQQ6RDs_mPzlDp4BgL36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29692" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29690">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_a61JK5Lo9grYVclDxmA5k0M_jm-SbOlAMjvn8tbiB4Z9J9t-Enj83ZVFxfQG7rTD8MVL9eEz-r0cw-wvlS_NaHruQwOml9n1Ls9ZG0r1g3n_x4nV8xwIMU3a-vTMNru-SgllzHRnEAJn7Wr_b9dHlPWkJk3TJKzZ3w43wzRn90l0ehcS9doY2bPEsLLXM-0u4SY3g3bb7ZdJ83aPqx8qyrfEIJoVAGaLE3ZGiNzKAclH0e6umST_St5s5YNuZx10KJ7zMv6gcLKh8srJCVtG-jmsXR-A7chlW6rG1tgmSbsgCG4oUMNE9hxB0ejNhzsOr2KqomckFDxil75NRIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🇪🇸
نشریه ال‌ناسیونال:
فابیان رویز ستاره اسپانیایی30ساله پاریسن‌ژرمن درخط هافبک تبدیل به اصلی ترین و مهم ترین هدف سران تیم بارسلونا در پنجره بعدی‌شده. رویز از یونایتد و چلسی‌نیز افر دریافت‌کرده اماباتوجه به‌رفاقت‌نزدیکی‌که با پدری و رودری داره به احتمال زیاد بارسا رو انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29690" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjASkXIYVAo8RK272cj0-nlsE0Tz-f0hlbAIaop_vVB38XPMEUmjw0Ne4fBFGu8_xX3SzSt4B1vQHxVuBT00R74jfMeDicSfGBvt3_JhQF2eB281926huP6ARhjaRsljeaRIkBoQa9UNo2tjgDU5LzKKIj9bC7G94ZOs2f-kQmuc5IT8ijHzT1t_tx1IGNPswVsEHM4KHdiGQtSid8_Lh9qe4ebrjrxxp-CxH_097F4gRGukJJWWhkJZJNZGeNeeoFC083aH6rd4XW74CItQbP9PUu_oyQyucTudmsKDezcxBvnzA5zhl-bYI4-K_m4h1eognuMY2DrYnD0WYfxXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWsKyLXK-iaZFEM06yOzxdU-bMTBRSHzWwdF1Lk0_U8T8_NNvgh45M3oMV4PXeIb061ljdSI9Ep4vH_GeldKS0fhpnfURuDF7a8wZcKB1klRF37cd7HDhqlIGBNNDJmjDxIKyEGs3LmePyf4CR2RWZrIm2xGn-cT4D8oQFdXCitXaVriUy1iad6779PJL8H68e2ex9Gb9aVg9N5AZiqDS_YTb7KNm_QO1HzZLA-AMP0sOyle6-aSVrzZcZ8zPx61hb5l3pHRJaFVlzOSM9CVH5ZD15aocexyeGbtAx-qIV5MDUkexyBs6ah-R1Yl9QFSb99kGJuXgxFIq_7YfgxEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-E1650ehOI96erQP7GrD-1OMJ9_I6Rn3n6G1WDVdSjdxsz1nWiduC4lDVkdxaLmMs435wFoiD6ozjvXC_Phmfc2RWtMUTCFHHBq-12Z0ZT0dWvZNq-31EI7L41r4Q7ZuY1NqneeEWIgWY1yNynRtuyjTBIIijKNpKuioJ-zPiQQNfkjjN5gDpyGDrl8AvCq6tGRDj7st4IKkR32oGaOguKTZOwSsYhZfHqZLpYRGoenQgPN-qEjrtjt1aOiK5jiw-CAWVPBDZvmRbTDfMP5-s691kyMY00_l_GiyxkE_nhzIt5m_gW94XW0Co6NLKNJvPBG1lQ9-Zh05luFnkmmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIy2LlvpLfBRRX3twzK7SDoFsiI9jTaKqjHyzvQG5jBqzVJadEYfIbzzjzMnyzxora7L5U9lCn-oxUk2IB-4iB8nJwmfffaWJMQuLQs68-iIyXSEDszFbwGsELJBmfU5wkRiw-z3Mt7qaKKZeMDCf_Og0_Rb1KGD5REzqko-zsXPlgqDisAKOni3SniWh4DSEeyvJohwbiRxPAuPnDnQJoz7FDmPq65n7k6xJQ41X8Xefz-L2Em4BWqaoReXdkUEosR4DDyxBlOQsDpG27BeTUVWwIzBQ6g24G-AUGnivXPmTL4FYF6dY5qlTPZROZBMQhuMpguA9mjNnDtUOUQo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxIDZ1uAPpcCOldAkljAXdEwTn1e8-F1PhHu8bGXfKxrqkQPI40nQgsuGfdmnbucfvcELuNXEGsWqRTkJ2UISmsHLzNVYJYE07XmahJK1sfILEkYt-72YAmFXBhmnOiOE1rIqg3Ev1V162WolGSAPp2mCW_TU6rSAvT2uC5rhNoR154-GMMP-wRPycZw1wqKdKT4dv60ad-aqkS70tHAPjMojGms4QjiZ1fJEDFniCokWP-4DwG3mc3YzFb8Nx19oXPVj8CvQ_srjLhk0XnpPoVxGYcbE926jXRflie3xj_13avNorSX0nF-GaBH3nZwpSXjto77NVnNE6TvAejJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2ka08FD7vrs9ek_Zv2RgFQrW3OKu-l1golIs89_vGusVS_1BQ8mXtqcVqeaC49fc80D4a0Hs58sbRR2yCRZl_3Ih-l3HNG7OVuGhGFqXmeNvGJT8E-sulOs2MrZFPSBgKJHI2_aAKiSwUNXNKWQLM11VAl7hVdmeaiVj5aMMBfu3BTtgCpmF8B-z9qFnHSmbk7937Qc6aYqMLkup9CHjRb3O5m08ZEKsuP-BPRRgkee7zU7zRgKFUzNvExX1hq3BvUDYuWRS5hLGJ1YTsN1Vvx6K93Jv0PUTST8cR3ZMluZ7P7xUugYjdCe5LtDyqtytYqhBEiEoFBPVraEmpy7yfXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2ka08FD7vrs9ek_Zv2RgFQrW3OKu-l1golIs89_vGusVS_1BQ8mXtqcVqeaC49fc80D4a0Hs58sbRR2yCRZl_3Ih-l3HNG7OVuGhGFqXmeNvGJT8E-sulOs2MrZFPSBgKJHI2_aAKiSwUNXNKWQLM11VAl7hVdmeaiVj5aMMBfu3BTtgCpmF8B-z9qFnHSmbk7937Qc6aYqMLkup9CHjRb3O5m08ZEKsuP-BPRRgkee7zU7zRgKFUzNvExX1hq3BvUDYuWRS5hLGJ1YTsN1Vvx6K93Jv0PUTST8cR3ZMluZ7P7xUugYjdCe5LtDyqtytYqhBEiEoFBPVraEmpy7yfXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=ahUiAlKaubw9kRAzOTf2Mqspqk4Fn0atDG-WzZ9SHElirHnr4IUIRo9RJatKusj3WPPMrdp6fcznnbLvsd8nHLcH8kuAQCxmV48qEF1KHF29QbJVA6zMKGAmBdmriyCZ6JP4Dr3CDyJZ_TpxPMQBSacGnA3vCrBc9eU2v60gx_-ODbX133pWxgsm47uQi8c3w64fJ03xuE5p7WehROeYsn7lRxEO2npQ78oI9MZI6jSnwf_vx4eBYMNAeROYkK8A7vxBFeXWiYumsqd7dBET0LUTOYZ7vUgK-y5PCA6clQf5oE8CQvnABskC1jVEyLjVOz-yQvMhVWAELzC0sNqVug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=ahUiAlKaubw9kRAzOTf2Mqspqk4Fn0atDG-WzZ9SHElirHnr4IUIRo9RJatKusj3WPPMrdp6fcznnbLvsd8nHLcH8kuAQCxmV48qEF1KHF29QbJVA6zMKGAmBdmriyCZ6JP4Dr3CDyJZ_TpxPMQBSacGnA3vCrBc9eU2v60gx_-ODbX133pWxgsm47uQi8c3w64fJ03xuE5p7WehROeYsn7lRxEO2npQ78oI9MZI6jSnwf_vx4eBYMNAeROYkK8A7vxBFeXWiYumsqd7dBET0LUTOYZ7vUgK-y5PCA6clQf5oE8CQvnABskC1jVEyLjVOz-yQvMhVWAELzC0sNqVug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhJJrjrug8UXAjYwlaOdLQ2brxLRf1CDK6wN0T7sYFEVucmi9VCcnVuvwWoGwJ7oBOvkchf6KbPZCy_gHUM2La9f8gGzqaNQukjgPHinnAhfZXkkrIzdGCliDXijW_gQZLKOq6iI_5GOAtFV7Oq7nucx0DC_gHkHJd0Xq0bnDkQ7LGbfN1iBlVLr8LiHfl1X1AL6jux1S1gThPq_TQzb5PFeuFRygdA18oQNXXJd7v1_GS5rjHa3sJM1ziZjKpjwCahTerDvPpA_Z_HblFqqG3b0eI5zB-1itZnvsDsbQr-_Mi7nUghOsc4R1md-sBSE3sp_y3eXkQZ9teopxPWvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsaA19E30z9aihGnMyOCDeK8KbBtk9Zx-yV3drFaRin-FlUIe7w1OHhw-aAxauIqo0Y2msNzgjxSlK7UpRJQI7bYmRgyiGlxiQQZW3D06kz8znSrEa6Jn_ShvrDXv-UVkVd3FgGnzwtSEcrapOayOibgSxRPkxDdTvxnD3AT-LRm028qHzjENqMhGG1L3CnY1OzKiC_eIX1JQesNl6ZneJYfFpe1P4faf9QsIEPub0SIwOTtszIT7FrO_xiAAfSPdSohMRbuuvtfgny4lYLWUo9IWi9iamA4EZtRxNC6kJ2PoNfGdlqD0EuubgJSQVztGYg6_7VDP6ggZ2Dvf0YWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szTNVucKPz8n3DlDOh_6u6qQlJibliY4G9d7wPFKuIc3y4lu4IRksS2v9DHV8t6saWAteqSVJSgq0rSzs-oUoN5d5W4wbrzXwmvCzXH1kQLQ1wjWla2NbV8shYeU_ypDGO3BVh0MyJGjOtN8Z1yaVL7A9TIkXcvD2k0JpKl9Vs-zfhOVp-mUem7Bx41b50cnwrXWtG7aFKDYR40wW59dvLI6lG5W9aNuPF7d78-w72F-ksFpWW8HKXWSenE_8ci08JUnMEU6kHBD-jRR_grjfFq2NZfhoVYZFc6o3xsSLVqRNwpldlrctuILErj_FTYzCgmovqMzRJvepJpvhZTZCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUgw_57YI3DMKV9fHiM4x0jTUqsNRjoGAGtqFgpKRsU7tm7ab2Qryp91_Y4YKI642YYAU8_rpsyfAlXJz-gJL_xXJTqdpdtYsfsKr5PyLbTWLgtnXDfSVe29kgEzkJ3yBrWft8v3Nk76DtnMWq0EKakfv-8AeGInSORdLXL0pEkkW3BBN29c8FQwOjQh9hHTs8aNyGfUj3QS2OxYvOWX6iewyNa_sTaw9pQ3VCuTBuGkuAzi5zSDvkV83X76yvsy0c_mwmD0EOPhOI5M4BXarg8g_ul3oWnZmcje91Wq9N2C_ibCkzc5ky-UaK8PZfFK2baqL_MmjySZP9QW4tVMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=pZFmb9EUpjNBwgltUI7Y0DE3S2pypHgl6ajkCsdye3ELVkZGnYXJt19ITzdzjD0jD_TGEekDgVV_ctfxTXgEeQlE9PLDg5NQg7gvp610ELLrmQ5NsRgqhlrd18xo0qJDIfrULLbZLMrqbNuFGdWOGxGI_mR1I9tWO2rgL6dU2h8FG3jHuTlhJQtZ6UKkeGikcH-gVE05YxQdnKkX24NCHJBoa8ODXuyB6xi0_5ylKfkLGP6nMy8mgVE2Z_eN-YhktpficO2tGTHp3j9aBD0Xn-bVcdfeWOAL8dD5EWyN3jIrEX5_HX1hkwlJs-BFCuuonT1H4nm3kFwQK8XO5PMSFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=pZFmb9EUpjNBwgltUI7Y0DE3S2pypHgl6ajkCsdye3ELVkZGnYXJt19ITzdzjD0jD_TGEekDgVV_ctfxTXgEeQlE9PLDg5NQg7gvp610ELLrmQ5NsRgqhlrd18xo0qJDIfrULLbZLMrqbNuFGdWOGxGI_mR1I9tWO2rgL6dU2h8FG3jHuTlhJQtZ6UKkeGikcH-gVE05YxQdnKkX24NCHJBoa8ODXuyB6xi0_5ylKfkLGP6nMy8mgVE2Z_eN-YhktpficO2tGTHp3j9aBD0Xn-bVcdfeWOAL8dD5EWyN3jIrEX5_HX1hkwlJs-BFCuuonT1H4nm3kFwQK8XO5PMSFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=VZU1usg9D2PdO7JFzb4UObmSdcFVq2n9l304XnP50WfhUNEwNrEhK0_Z3e1H70UCiY7Qblg8LybOZ55Ky4d2PWe_aTK9fanpPimVqu0-8I-bRcBKbzxzhqxZzymsg_zqHRvgHDjjat3MTSnzYasLPYRQDoJKWXY8tCtLW_fiVhJO0CARhnWxIdr_VT7I2a187gwO6Xqaj0woiZzQ8VS4Cn-mfOMNEKiUxC7zdSusUzF3c62qZLq9pVtoTFgkCswP0TKpmbgxv7ReFaCm34G8Qx_k39lotYbgPPOwZETjsliCMnQgpoyPPM0-Oh4m6q1rKFEhCHRpu0iNtb2mu4Abqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=VZU1usg9D2PdO7JFzb4UObmSdcFVq2n9l304XnP50WfhUNEwNrEhK0_Z3e1H70UCiY7Qblg8LybOZ55Ky4d2PWe_aTK9fanpPimVqu0-8I-bRcBKbzxzhqxZzymsg_zqHRvgHDjjat3MTSnzYasLPYRQDoJKWXY8tCtLW_fiVhJO0CARhnWxIdr_VT7I2a187gwO6Xqaj0woiZzQ8VS4Cn-mfOMNEKiUxC7zdSusUzF3c62qZLq9pVtoTFgkCswP0TKpmbgxv7ReFaCm34G8Qx_k39lotYbgPPOwZETjsliCMnQgpoyPPM0-Oh4m6q1rKFEhCHRpu0iNtb2mu4Abqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu4Om3OitdLE7apnsWCPg1iWo3_Tu3M0eXq_J24C1lfD89F_HWlYrjVWx6fejejPrUaVK97gGClO-eOf42CnkbEbSLExrerEs8N6UyvIQHoMyrLC63woOMCgYQ079ItPOIVZNdVz5gASFke93BrWkWz221pVBGBSaHJs_6JOd76dsUqCVuxX4ENrD7XfzaoJ-LI0TEzRKv52HSzzkuCB85bJiiq4U59c9ZjIilV6jI-m-J1gC2FFA3h5KKp3uZYlLhTp1ASDFVCpRpFhEMdrK7AKN1W9W9eCSUFqve6ktgV_c78L_GECRsbIYW2CxAr0dooFg1cOlTsmliCmiL3EEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
