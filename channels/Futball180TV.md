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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 500K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان سلام آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElJJIJaPra8QlTovgUAtvbG7eAnZvDwLenwfwSTihsP7PgOm4lLQ7S_aqTnHO25JIQWRRtw8Is0a8KlYPisYsiod-OzbzE90aWcU6v8aSHUG6tTFCMbE0qoiKJczkh3Uhtmcb-Ci5t2N6fDQK-7qc3L697LS9j9QUiYNPHiRiPUnuhfwKMOiTUGyjjaoQ-IPYHC85Y8F43Mkkn-PzNgstRKANsJTtaN0tVidMLyzWJk2NwidjMDcq2HpRJ3pfojxicUn9vpf523vxRd_Vrsav4TazvIOcwetFpgdCpzUBU0blzeVi7CQimb5cOhTuZOAhG8PHDbLbPOo6tMaJMzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5xTQOq8oF_zPg0NSJ8spYtig1t3DDRAkIozDgcNRN7sF5cMf7QjEQcs-flZ1CKlcv3uZJVAcxQTZvMLeS1ov8kBRG0nXLZek0a3adT1bUHXJdUObWtB-cWg3DrYiTqdAHRMlOUIk8Ue_dj97cP34xisjQPYGuub3K50hr6eIl6oUe39pcfFUzPNkwvv6kev5nVOtRGqr9QhBcjpcCO9dO5_6pL3jrjhNHCGQRJDFvxtXX5PGcC8WJrSLtOCx8UcMnWt6-v0bo_aFkHV2KkiT4B9mecOTUSVOxL4CCfNAwgd9KvvRfZ1ulDdUEvK_nbLEzCgxlKMS7ve-gwTAJ-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wwmUjIWLWRsqbJlCQVNJyzRo5WfK7yIOPLQoKOYRjR-VDZRYXWftL2APTK6IclJFibmlP1HVDGO4m2bpPqYP_yqwnD6NLBwQ0Ak2x6QqKc1tjBpsPig1wmJKp1hnYHFgKHsvazFcYHVVdfoZkP6c85CXjjV9XnFxZzxIt1gfVDrcw2O_KxURgsT6usI4v0LmFNn6UFe1vAM1qi2OGXkK4xcrV6Ye4oq1f4Jce_4Gh9BTch7WDCQbSRlvocqEYB8JMOARNIqSFZSw8tn7JXLbf3MwNXFVkQHmw7QDWy0WNxA_hVZfch5vGzKGyeWIm7Jmuc5w7veaFseOzr3HVISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidWYN-6zHdaT6ZPr88FheyDZpRkdvIwOoTuIl467SfZgXqANhXmEtMgL_e_qmiM6vCphsOZNz-ZEo340i_gJ5e9iVU07xqimMvQ8tJfvvHMC2NsfxBAU8utSvekurgTqEVbG-NGGH9XYPlsapTKugbo6CPqSDxUUlQHGx8YVOdltFZHsX3fgHryfZWcWbTR6HnB651w8vJTQG4Pxb8Tr59KsbvbmiHfe2_SlCfT77QmYTIF0kZuulmhQcNog__QoDVLI4-UZq6QadGs0jMvPHTf5rIUNIibL0Fc5kd7RXX5b6WJFZRDkZivw2nWjDjf-8WLMt9979fXz4Hkpwk2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce2j_5JLWu3ShREelKFxbUNpSKUPq7ksT2BSTLeQFP7Xnw1sn_U6R_Ig52OE6gx2uTTfdRjl5F70GVbuTQ7He-4Nzh_43iGpiMZKj7aXKyq_IQj-BRaNeDCMo-UmQ0H2uL6J04YzAWvFK-hif3rO0KZmGP8TTfe1w5f4P2oXTCLqNHWd2fCoAFaiZZsSs78HaR_C9NGIpeA2hlGqb29-nfdD_UUnWtD8RRk5gMDUNQVUVlbjgEaMeL7-ViEDWNJHnIAKflE7PhgiITqQDoOg_k9wQsUNYaLo-T86eIrIGDwPaC5fAKI04ze_tiT9PEag1HOZUg3EwhKmiaFDEZx6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t30fls_VuilR6tSDXxrcEZhtFqqztCGRfLraT8m7ZP3y9F4wsG84_s0h0oqQXbsWgIV9m2FW2JYou26ODDJlOHAtMJ7HjpRSUAaUEojWjke_n57LBS4UzZoCaoiWDrkxoheqcNoTR9qd7IXKtXMecnxnaSTGPiN5zHGmroJ0osANIY7pZLPeG6TwF8_WgNpJ9GCUY0nvyoj_EArXIZAm9ABuYy45UhB4IvCtGpP8ZPwJeh5KhyQiw0d5GwGFncqqGWwydNe5Xs1Y8DMXUNBwp8fGC-kHU0hv_56ILIeUjbjNupRQd7H86dXKmXwFOTpwR8hJdTWnU60v8XXSDpwUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjul3lpHp3q7ENDfyKmZ9RrIwFbbTur56-t1N3olLUO9EhaNJCcoehTtJbjBr8czMXgj1qVa9Yvt0jAwHYlfF_OPlLaIE2N3viOWLbQHBf_i8ftdcPTSHLGqjFcKx1r32qLc7Gl3hwGDf060fUFe9T7iWzvJ1EKNSDwvjDrtKiWkvZrB-27MJCbuRtJXpLa6_s-TBLXlMGYylrJfUX8apAZgcvOKzXxHXHiL0C3h8Qu0Vm6obG9StaS4hLAElthIYyHu-6GL3aISzomcgSOTZ3KDJ0UFPLSfoA-Y00P62Vx6qDFYrrbjmRmopjD5ZSXCUWl5duo12scqQuFTm-M3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUFBCnDvcbB91E7_KyoHpUsZQrVfXsMiIv8ucHrts4Cv_yb8V3Ll5LjdhVj6t1bhbrTuvRUfyCJdhyRJrt48JEKhwLMG9JYAEmR9vkXfkkxjeU1C_2Lp6zWlptbY6tPeg87VSKCPVAajfCfQquoDUsXIU9hyBiuH9KAYYDekf3ohB9FZihlBR0opuIUHJYvLtnzT1vhgjANj9C9LpqNTD43juxzLh72t1yb7rR8obVtGixUshS1Lzfe3cTruUD_dPlR7aDC4ySkBowv2l9_H7hvpX5uI3I_hSmeb4mHfghFzomzVUswjDsLrdEfAQCimYucABbXZXoopBs8FipoPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBZqillcVD2_apzjoS3sxrYxxM5Ol0rGWdn-oS25qFsEM6tHTXXGbmcfa49jwYBe9fk8_m5RooMXkNAj-DDXivLu9NUvTDmX4D4TezlHgSDmnKLL_xRPJSHMYCGl37tjpBRx8ZpRDtKsKLal_XdWDni0VFBKvPVtPaxWJVQUO6tzoL2qf7nlmngLqqx9BLxFwamrw9YK89u-fsHrlRqMQzqxBKV_CrDyEg051_YDQdDAtDYpV_5gMmyi5thBBUSmu2x9oGAhLIRIzTm3rp8iPPUvAL3Jws5vPnk7k_X7v963k1CxVelRb_9nJD0IR0hA49OalXZumDkyPDH31j4LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5GPY5T7G4CTRsrUQlWEvL11gURgwoyhZ0qFAHDt0299BJ3tcipUz2_GrRe0m7fa6ZUDwE5wdqT-hlT7YQf3P1ks4DGW49MPvWsD8rfJGEVJJbhGcqMjOU89HQWWj_9IYnDDiYR3fAfwZwh1ymR98RBrx2T1rhg1qIYy23IDKajGzS4507KjBwVJz8OTnI243eb1FAr98xc8oqCPDQa6ycfTXezjEBY1WobHNYmiOwCYbDBNPf4NV0RWCmAY3FjgnZdp_gJ8j9MlKCK0JCuwAmW1iKwiImDdXOKTAi224-dWDjXV__IYp01FL08UMcIOqr0xo3ZFbL4MQftoQzagXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-OzwQ05mh0nQ-PjOfV-RUyKwLPgsUzFzl6AjF8bZXhgcNfEC-e_gv6A-peld5WUgbmT59QzIErut_NK5YAQIGDjWklwi0oeLciFug3JRRbZ7w4bsTcHw0biW3KwtoqWoSaY---Lz3wa2VMAqzsB1jxf_9KAsFY3qT1qsHN_oQXhLXmnlt9drvYlYRJvqeBuYkyE65bfsLFe6OQEhiZHfR_i2pZ4bC2b5JJZRMoidI3FXUcNXc_OIfN0hngIOgGaMLO7USFfRPptVgSRrOJMCOQdvsW4f_Hhubf0L58gNBMMdTcvOV2nrtjvLDpFp033l9eI2yvnP27we3p7vCzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvoWGrKpkTncmSmE4W5sgwMFwKGWiTvZR74HxxgMJdeUFSwSt5KdsJjoZ-vybcB0gX7pnaF7_JsP4TsCYaJcevCJ5AvqPR5x547u8EtWLXTgnoDra9uc68ILi5zBSKkJNbM3NEkZRZK9YaKyfa4RyWMmKQZCBYGUKf2rsl9wUWRjNYF5IcmbmWUe4zPzBjdFYd9H4Om87QpSbwduqPLM35rkJf-gWre2btEfmdy3CXkGhQ321qB35sfOtQ4Fj1JNwqn0FsVjhLgg86mXfVeLqDl2wotSqbInAbgMd2fWtQlXihAw4qXtWXeMML5gw8Ca8A3pUGZ_qzvdnZBmhGzjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE3ou-csGdduQBcPL3w1dVjemzPn2as8NdND-0mJfm0k0zyEkgOuJeYqLowVZjjYk6pQsdZNeU6JJytnmym0urI6c7_FjAqLxzW4OV_98nIXR3Jb5x6XQZ9MSMmy7VKFRzCccmYoKghLCTULxePCJtMy7jgzgVLEcYnmtT6qk7xa7kWjR85ZX3JdF_0-TDDnVs48HOQ0ockObe6S_CYL9jRtzAJsHBfhz28wVFMoZXdqQy3hdq9qKLScwI_PRgslAVtuuMkRUxGYQQSKrwokmewQjbAqzG9y0wsHfgPIjqLKijeeJbq_AtlxNfJAbcYvdoRtdq50_pK2QjQX0oG5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwrjqzJZLvYeQPrWUrGgVxTc0Q2d8OepgLor2EB05Co-f_AOG9uunLGwD_EKqUXuLIhfDRhFx7HsmHVJ5JivS9qdJ0lQBbVMoOhCvQLCJF17n9AFCpOZJwUoQDAnMnfApfn1OsnwLLbFB0xpsydGEK-HM0GGSotcTxHoXNyLPa0WcLnymWb4ZhemZIcyW_d3LyrJym4uQdms4Oy5gqraQ3eQUCGc-8RtKUfqvfHu8BYV2M_kOLR7NeJs3cIYvY_Qz-FqpL9MQi6Qi0lSfjG7pN5DbbC-yUBSlDioexWekoR30clhH1Aju2S0D31Bp96ih4lK6BpUUzeF1SCObHNGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glryTqvJKAIoCivGtk5cF192CB0_AwtUdhGhBH0Tu3EousB5BpVUSM6aG5eL_UQmjD_dy1kOjKBuLr3WQ1IRoRd0lxeg5KHfJQd2HqDSuMw-l8srTJVdEOPaHjJBYZBOzYy0gQWMr0Llb4AJ3l1naP5UNqZcnB4WGHcoqXLUm1rRNPD_f3AYWKEqJqgnzbaEnO0SfYKAawXe0Uk9brS6keGm8TnJTjQq6rBA6KQUWuJ44mP3S-jQCTEN4NnkmPL41zJ98Fc5Y1bo14qoiMlWgRn6DV6vFoZBXz30Q0yXVoMXszBB3I2thvnU4oM7-6Gd9EsLvdh_zc4k9-lp6yCYkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCgWKCFaaaua0yMM7WwZVZT_LoFmW3gk69Y-KuW0Yq-t2T4YA0P-EN0zaeY79fiHVPjfgxUsj1bH0jUYZ3TYfSlEzw5XRNH-VsLlxbWrimI8YNspLi4BO5M5lPdB0_dJ55c9OuGmf9hrH6O-TWfQbEkAW4gLuneKR_Dpz7fZ8wyhKbuSvJlEf4Gl_ohRa2J1arJ6z3dZaNa3zVFryE9YOALZf7WXiF-k67oVfc0anzPpo2fnjA9D0lXg0_JdoNWeY01nbHmU0oZk3jgBJTT0pvp4vTHlH1RyouGkd84z7jjG3DzVPGNEDpRU60VYAi00y1EcjCaV91aWUZEFN8itYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtBuGxMX4z8Q4-7mtkGA1HK0mvta3V4T2H1bEOhj7v3uQvJ7uGSfSQVMunsTzwxce2-2FsGpNsKRZPp8Z8ts4Mn2ubC5ve6-vh4sf46lCnxoc2v-k59SK4rJ3vB2RZVrZccNsAyWH03Op1SFREfHM4xmUO83-ZUGuLZ-8glWLAAz94xK6DW9iA_Zq9iBdhlRzlUPTj9o9_HC8rKa4Z5Gsh1AGy_G6Gr08y2cIOl1Te9O8znxnpJitgtNVsFB1kCP-QPBOqKuv1PHj_T8iidHqaNIwZvjnDOnyVI4IOzi_pIPa_twOaLG1wdsj0WRfHvc-5v_yvYINnxKVmzs6m6YxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuwkUouDRqDTUE1FImiwbLac18WgGcd6Pfywfy49u7T7xbIJ-GqQU0LwuEQofxIGbYR7NdQHd68Xi7Ajc6q5ekwOhjxcTm3wLKKe-aUDLBbf2nqAJCW6vy-1hHVXiXwLSQhftZ5SIeMbk27VzYFVrjfdqP5aIBUpeg43336szcfi7ggSfZ85q1YUSVkjrscMtue9a6fYdQN6TlWP1wsPh1Ja0zPi0CsQh2_F0yy9l5Guehi0SPEnf5Czn45LcXjuzEsIaIJN2cYESh09liW4xvsptHoEclAzP1srLFJa7K2Snqipoxj9Xme54B8o3wwcPqV-p6IcQcOFF4k5TsmFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ofCNhZ1eXlL7KTd0qoSpbRP16wSf9NTFvZa3r1yaLxObgyMuG1DyAPqzV4cVrdkT3pshFu13rlScWl7IsakMSeEZhLOnCYRs1ucpAaabNPYuG7P7cQbV3N7XataSg64968U4W8CSIpqfT-VBIxDHaLu4pxWVrxTUWYjvG-JxLHJ-UiWYyUUQ7M4i1oRV_fcrKXzHolJ0666WGa1Y6gXLAdl8Tg73S9_jp40jxO_wffbm4EATV_YiX6mLEfWn5ejynv9YvdLydl6QHRfHRTsXW8EEze_d-PKlSlEF9j9E7fAy9I0k4tm9a82b9_g7tjwhbysa8fr2pKxYfnSb57rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxmJjOyBZ0BmweILxNdcjJGf-C7iBaQqno2sGN-ynGvbJMWxLJeSbqyVgcG3QbPDqP8ZsUCIrOS619BbMJTKFNbVjVEuHOgRmgesIK3e2UWT_M3p7kLPzjXYvG7uAalJm6qbVBJuq9kt4VGCZ0WXGs99WGzPMT-f4g8PUU6Zsx9rWhSkcKvObUAyrr97ejf8l7YiMrK-KohPlNlKddRZtZNYbW_MBBYGICTRITwgFaVndHQz0A-bUCNilOJ3iKl6lTCzDzQWqbx7-lvFLG0OaQHDBuZTPoLDOTyLJErArSq8C0YuEfskUddrXDD9c1jr1-5Sf8BDs47wVbloI4NazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNd2CdItzmWQo6TQnbKw9Brd0z29wFc-gAxOfjlDA_wsojPV0bd3tKTi5q3XreUmdeUIGMoenMYyFskj1wihTGD0hgPMlfA9PXv3eDhWHvjpRDn1Rw5S3MND4iaD9Fq5ddGWWtVQ1fF5KZyTbx62VvUmzOUkUTOceTyB3ADP_z5CP-kooq3Lz57mVK90XCluycu4P8XEnQxjbDPITS1m_Xxa92glNOvnUENhg_OzpTnF8qyFHs1XgrGnXQGVsb6vBVePUtKWBZ4h-jb5N0GL8eWfXwM9ljakaoAhmb6WG1-NiLOoYuHm8tqWEl3_g1pIlOkBhrrEgtQ2fCJ-HzXn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH_M--OTSpuK6xijkzCgM7EGKq80OhtwgVWGCmearlmC7aC1W7FFknIEq6nL_XcD2-1PRMa7TN_AvioWZgb1Y9Sw1E8lowh6vieTh8Pj8np6ZMteYWfrLAWVOR-hf2cydqxNpt5RoKdl-pDwSGaoaty0l91sblEiaxt8Z0O8zKVwaroAlkMGvzbWxUaclyhTnY7LJBWhYh5b0T3H0A_NzaUxzvLrudZfGUn9iRNmdHVbqT-qhABGowBUMuFm8THUJ9SKGkAKhzapsUIyry2AHAesAlXmkNKOcnvhwtHny1gbkn0Sqjo5bgwrHnjBoFTfKHH3SvosALF03ayGG7uAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C19gnHYhEj1VTaqLa_JsCTh_xcby803d97Nh6n4DhsNQgcavXnqfbwkMDEI42paHkYqeqZPoQ6SucfnB_FZJex5zIXOfPquHvm2Wz38IUdOeGzUGTOHxDktiv3VL-kI3MouDZ8WP1Lv8ZTJedzODGEoCXwCcmVohKL1InJw3qx_Y1_7gyL11FRNSZzdJBEXjEll2zt37BRgi3ceSpSC3-h3LOZmmwR_6wW84BBj8DuHTOh4QG3xUEuQ45FRJhnsbp9JZyfI5EVSVk_zBEiP_V4-4Dq7hNViPYIMu09llUbk-EH5TCczvdC6QRFq5KdRctf5Jbs_Iz6tXaurEgKkPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuH7kZqIo1KPVOKHCVJPbJrNzCiYbxfita9GVSnduXxjTzfi3AKR7QVqD2nd-eWJoNt7Kj_9PkQGXGn8UWeBozdYrnWboh3KRhAYx0KeZEtwFxuqq5M4jdgdPw2qB_T6l7o0U62X0tB8Jgw2fvxLiTlnGlrBI6tIUutdS2_iTbtp6rXArN_o3g-VJdo8kd6NFGJtBPwvzFJNFiou2cFRZ2_md5Uv7DzxLn74LMM7neTNxC9K9pAzd-TYLne0ZX0EjrkVdnU3VhR6E-E9IDaDHVv_A96DjcXfrIwlg3Kik3F141o20II0OP4z49ogoj43VGhubaaRIrXgQM0cjUA70A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx67Yuy0o0FTpB4N8sJK3oDGHy_j7THIM9i-YoN5yu_GjjKxTYfYbSEsz4jE-d3MGf9ANyE2U7g02H78X_ldCmpmmYOLIoA4dOqHs8HQQrMO7I4_GQHECzPawzkkhg34kDnARRD4woG5CstP6V1hkm60EMOXUkkIFpqrwpMxsR4qhAiB8vw6Agkru-xxoAc62Pvty0qRFcvNB-rTr_il0TLB2N6Fgw0mmeX9YezTAqJuZQ_-BB1wDvt4xqAsCk3xJO6zWt_xd8cimQ-HPCASFS6ls6xoogG-VEBQcedBACp85U-qpNJ1gmjuqdGhrABlv9QFfa4qGOCKoT5lxuJTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpIfQ_GT7qrU7EH7jDyci5ZkzH0ZluY8vIFWDzsuErCDf_ePXKwpNjhpQl9fv1E3eO6mhKzNe2Op6fbLgWgzAjYSI08JT0hiFkiczU0tHW6QEVs3ba0dtWkQ8xV8BR194hsE-6XagNoLDBIEqhhTolLN4hJvDd3fVRo7FgamjxCRa7fuu_bpbfWFt0-oblVoMc8anPPnKPQxvjAsd4gXgwRdZZy_fYwaE2NM9UuBttZYv80W-Oc_BSU4DEGZpg8qCV8p_qfVu21B9-GcLCXPf5jMQACbQiWW_l7A0AaKAb7AS-OtfL5IaKxjNUSk9x0iH7ohFEKTBcHIul_g0GAV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1git3DNZi4UbfRWiWLlD1mmu0NapExuNFU4qGBTdm-_vodScDPaAwNxC4nliw-K0Z8iJ4s4r5DWarkKZ6pDGbOd1FXw-jqVJYHgKotSo0cm-GfqEhQ3pQvpHatdzAIB-erj4llSZ62UtBUAZyXaLfNi2yf2mZLZk8y3sI_uHB_g6FEk4JRlcW79YR1TxjU_1UfcuZqGA5nEAJvI0g7l1-THdSkwEeVuehBoKquvSBklv699qzDuaZ8vINGtHK9-9FQzUgzcAy_RY6TpbAUsLcFKROFRoJeoL0FlTVV118_me78zNU7Re38yaFQSRnf_xCSkRFdzBCZhQ3UpJaRSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqxw2dpB7_6RnOftUfxgGryh26SRZieyb9acTGTO0cVOUvVlUS3cQ3sG22Os-jtbUyy6fYMuEL74KUgQLwMn9ll3WdtQs0nnhEWDN_ao8y7-DwaC8U6d9qI3MUVzzEeM9xivpBPieA5k0fzP9mUMPBbGdN1E59RG8w_sTWR2_AlMFt5yAv1XmQPbevwoL_vJOZebMjx4ZjCPDG_WB52jRW5jQlKil8WsgXJrA5bnpGslTbm36zkgJSBEQePz7yid-YX_LQsc2JuJxFcpzVLMyEwmLtATsZ_fN7V_L3OZQuwLVG_FMQ6eqEWoLB3LN4JOA4W61ZYrfcuycUF3qhKNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvk67k9Rea-0gNp3XUe2qugrq5vMQH_lQhBari5iUHWEl_7vakPikieaZRCiIlkYrdL2n17DEZZ-3aDSwpowhTnbwtGL1Gw67vd8vLSpvwRq1TNB8XQ5TqCcKHeXdaMPsuKkiPifUgMXty7AgnviA72FjcnEpSWN64ZmZxvDSrrBzRtMlE29dDsdvhFWKTMJs5Q8PDk9QclHOGfbfh2vDb8x3TMpMtXyiR9fz5sTeBJzc8iV-hntlp8vx0Jg8hqdW9nHCfkH8hRdV8lIAhJZYXLCksGTxy6ivsmMMNtI6bmxhXm-yV-ty4xaFxu4piUSI2sXW1yHtEAM-w06-fxQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV5dVbOUsOtIJ5NJKevE-ZS97QzCf8qmGhSAtEWuQaHK3nmo8XbkDrTJ3HLwn-zpDFueiSbifpocaC3MTwo6EhoKuLUahgGufifqWfMw4FlN6qqWUIoQi_i3aInftW9_g5NuF76YsNsWu5pGGhlik-gEIHUJeNB2accSvviBdfw6KkDsAN5beuSX4tLNkjjlFNYR58LBN-JAOYEdAJDlj7C2gx32z_LwNFP0JgIUx7XEgFCGM5eBMGCQ-bnxGoErMNMJswJXyM7siwjgccw7p-jlhMlLO1Xs5A8KoDZSD9XtxHvaDLu-SFx3F0ZbXgJpLFAp14rXT3jPmBIRzJr_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CASxAKtOjM57ZF34G1YbWNYp9B6RGizenA0jLrOqaZk6Zt0fbEoeFusB_RqqpseeeBN18Dmjs8VFdeX3wgjmU-4u5UNz7qLDPkxBnibQelyLO7NxPTciUQLqfBPLGW7-8uM6viwmrt8Bb5ufdBGN61l1_FqpBFI2bhF1FxeNE_nA_KIEs6DA1OA4BBKWpBZDVn7qKfJ-Q6vXEuwODGn_t1FdY1nVMYaVP_LRxWoF0iylXg8lIgws8km2xWJIA4Is1yjeTXYYrYmX_1UyOTn5UFmPqWNMT3OEIR4odKMKVO1cAwEFGaHjb8gLt6cm3wR0cc7gtNxJfNrLNHP8Z0C5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=JaMh7PnwC2ZgDn1c4BPoU1bj5uQm1nlB9gQbDtXjaR0XsevskcV0PlrFmH9AKWNsMk0E5pEy4JmDP7ZUyyf-MsRHtNyUBXDJosOfiyld4lOtTtT_M8SBBfa-oqWiA8mvPe9aBwtZW6A70EZ36wsoaNQbyJbZfz-vMEZcK1HPhaxm0akTFgJMxFGh01TzlM-uPWAadWLZEqCn3W6ykImPdCpHlghiVOA3Mz8RM5GBc-y__x-zqQkOZu96I_qFjUaBiXQ6x7Ci93oHsHH0EtsCWSdZge-AN8yn_5vmVjnkqWkRrXpZaKs-bRc0ZcHcb5eyBgmX0oBsFi4_BNDFT8ZfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=JaMh7PnwC2ZgDn1c4BPoU1bj5uQm1nlB9gQbDtXjaR0XsevskcV0PlrFmH9AKWNsMk0E5pEy4JmDP7ZUyyf-MsRHtNyUBXDJosOfiyld4lOtTtT_M8SBBfa-oqWiA8mvPe9aBwtZW6A70EZ36wsoaNQbyJbZfz-vMEZcK1HPhaxm0akTFgJMxFGh01TzlM-uPWAadWLZEqCn3W6ykImPdCpHlghiVOA3Mz8RM5GBc-y__x-zqQkOZu96I_qFjUaBiXQ6x7Ci93oHsHH0EtsCWSdZge-AN8yn_5vmVjnkqWkRrXpZaKs-bRc0ZcHcb5eyBgmX0oBsFi4_BNDFT8ZfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkCAhIDmlohTglzYLqKktkCpMD44xuJ5_62X3XGqmt3MuyTUH2C8JMdtoIVbIl0ttK5AqVMWf2iovZK8XI5H-cGy0__p28PatWAn1FTZFT7AEvWfdeCZMbIO9or55fNiHtflJv1JNpAtUjeZFZPh2BNTrDkmyDm5q9MnyVS0BCYddsaMzRoAp989t-DSmWl-0Mru8q9ebRfuxjL_B2uu3-NP8XyZOAtYuQZcGOIo6vQ2FbjuTurlamJ07vcp_issnrMUiESjE0_14HtIdQbd1GBbvag_h_RsQexmd76payCj-f9CNBjPnuZ3sKJX1GofO-yJ7H2fS1gZUB9Hd-VCf1N8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkCAhIDmlohTglzYLqKktkCpMD44xuJ5_62X3XGqmt3MuyTUH2C8JMdtoIVbIl0ttK5AqVMWf2iovZK8XI5H-cGy0__p28PatWAn1FTZFT7AEvWfdeCZMbIO9or55fNiHtflJv1JNpAtUjeZFZPh2BNTrDkmyDm5q9MnyVS0BCYddsaMzRoAp989t-DSmWl-0Mru8q9ebRfuxjL_B2uu3-NP8XyZOAtYuQZcGOIo6vQ2FbjuTurlamJ07vcp_issnrMUiESjE0_14HtIdQbd1GBbvag_h_RsQexmd76payCj-f9CNBjPnuZ3sKJX1GofO-yJ7H2fS1gZUB9Hd-VCf1N8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhZ4cZMHMcVdb4Fnf6ykK95eg26k7KT3aFS50A3qZViRbR-A_ZQ_ps_kjckhPAV0JC-rT47dCZPKhKAZl2FaRT1t896PoDuAGOaeVF1JafQYr6Ue5Y4Eyj-GAdFLOuGqFPC5M3Pa4x_YeGUPJLLZxsjYGWG6znxAKQSnREMze_dLiGJB5DKO5sGWs_tzLIPicvdDOTpHuKqyW_UR0Yf5cFtJwfY17_p9DUokr0VNuRqtS9MVuegdsV7S0j8Orn_h1kHBKmYX5LbsvZmyyx8XjMLFIEJSqOSzk4Glu6oqi1iEH1E2j63VNaR8hbkeAoTZ3kFbxy70bbpKYBjRHTLmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ_tkt2kWMC7EBikGyxroKcdTR6BPX2VgaC4oQcU1XwzbQwAC3HbzHMlWht8DQh0DUjDcrwZ__KWBQ5lmUFI8Y4w5AHdGK6QD1UQ3UiOzq5S2_oRK2er1GqKloFxQ5RqcJrNysyllzZYwjOgXq7mmHzJfOQEaLPORb9s5me7mPNis4b1G6LyS2oX0-Bb4N03xGFoVAxW_ZPHpR07oitiUieqDL9mMs9jRAEdhn3PUotvaE7ASPgW662u9WfIza9Jpe8l40Ffybqr8Pr2IgZC2U8sprjT8vML7CU7ANhWKZZ_giYJMvko6I5gbnKaFnDVmbb5HXYcmmccCIYUsX1uJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAb3ude1iEmvnKFdcC6mKOFOhXHFD1x5WAC-Lus7ZZVNwfIbEmRHrlwRaDqwNQnEZ90yWCjV5ITl6M4OQBcaLxzOUT1HQB1CL-RKSOJ9podHj2FqW1URJAaWk1fzYlP49TS0uoazXNxDMouKYXVInQqSYTF-JyehEBbtVxC6rOtwe9rqQDZDOXIFPHxT3uuMT9lJG-p-ZxEUdt7zbg0XlYdOhrY1P6nFJXOkQAxenDiDnJKo_xalLJ4-TseoM4YKfRfLr8-P9EfGWUfWA8pu8rHweKWzBKBC9toSzD0kgI83fTkqpre5MZibgcgkWUaR7YbdTj2AxN99icw7KrsklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2c9n9XyDs3Z60qmnAilk5KBvLd6egEzUH6VH8NuE5moJKJA2ytrVWAmoBB_DQ3qSCTrljO5u1pjbeJQivsLkKqBUgWMI2V6tHEzWB2z8ukznEARyH4lT_-Q0iIVrHffytva3K2yewumYtMp8vqSFJXWJka6MFD7XuLQIABWTewUV79Esl5Gc-GPAEkR50jX_J7i-_OBfYNhdmX8xidJzTEx9NHEeGU-YymiSh3XkfHcRIGnXC1CwGBkaJlipO1fvvBzAo7A-qcp4K_t95CJqFlOW96Lm7V6gT_ONKiHChlzFMZCvCxbavLswPF8U_HkRWXRQFwf1fkRfQig9NN65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrQ5vEMTvtim9Q2UhOw-jxt9RgWfhmhpydqyHdX1svZ65sYLYbpdqyLJsUYwdLCTYY45STJxS-blZsRA8APzAg0wAkPJVAaqxUGVenP17xZyYPo42n_KulxG21At8M_rPZzAzYowzK7MPjRjdwsScKADyBmgsKf2MB4UtEECeYWf606HmSB09LLIJVXUDdGtY2NGMOrv2ScJzUxIXDRguk4dpSSS0e7d-QmNG8D-wK4P3pb5xoQwpUtRP14xz9EAOt22-oaziWKKo26G4fWzRlzIG8xOrTDkbiNFrGUqlFuQXIH7mCCeuasmb6IfJp-vIHMI0elHCmeohzQRA_2iLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz3q50L_qSUE8eJL5M25fTRagfzBIs-DPSklFL9rZVZAELJ0mcqcy5B7XBknny7-jE1HBoph_gavCQONXwoyauBgCP-TMaRKKf-_5pama1A_Q2G6ZCOCptIfsmdxYY80S2wG-RrGpFM_8l9ZkviWh8V4Aav6bypufdbqawdLlvOhB1KePISLZRZOV7avNItdjoFy1_IYRvzlA-cD7bhpOIxtmX_QvqJjAUIFWDSlFOHop0SUiXPCzz6q-DaveFWo9zfMk565E_xrBqdfLq5iKgE2iN6iQ2Sapa5R-yDMQk-Piq-vi8qKZcsTndPnwlpR6CS9jbC-lX-mQHU_tsV64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=pluEaBNq8l4yZ1o4SnnQ-_PP6CXC5qsCzwRZ6JRt5ySPNcAwT1x1zz1lwLgxSqX3znOlXulXx4weleOgK3WTjblIBJ1CU9MmzAdjeMBY-RwHOubCgizkgWX51mbr_5s-b3nnTIH11Ol_aXWA5R3eUtNf1x8nS9fk0ghx5FVPwAcwfnvxatTjaw17Ro57u3PcX_sCsbNuMNRpy8SvXrYnRYhxXlaq9w20Reps722luJcC_K20z9sVWU238BhLzedcDl4zfwlCTjX_il6JXgdN1jtH9kQ1Lb2rexShdMVV0QjoUgQrkscBaEU6gguGSYzrarP4WBOW1nAFuCVYnKnoiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=pluEaBNq8l4yZ1o4SnnQ-_PP6CXC5qsCzwRZ6JRt5ySPNcAwT1x1zz1lwLgxSqX3znOlXulXx4weleOgK3WTjblIBJ1CU9MmzAdjeMBY-RwHOubCgizkgWX51mbr_5s-b3nnTIH11Ol_aXWA5R3eUtNf1x8nS9fk0ghx5FVPwAcwfnvxatTjaw17Ro57u3PcX_sCsbNuMNRpy8SvXrYnRYhxXlaq9w20Reps722luJcC_K20z9sVWU238BhLzedcDl4zfwlCTjX_il6JXgdN1jtH9kQ1Lb2rexShdMVV0QjoUgQrkscBaEU6gguGSYzrarP4WBOW1nAFuCVYnKnoiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=KjO7KOFblL3eaQtNgZG_wTAI6q26mQqi4uczF0nfir9Ir1ubnf55RzYLfuy6v7R5znWxX3HYQLNO1MZDIQ4yZujnmV3PR02ZaTwPiReHfS4NADqxQipUFG4blh7zWzPGNHJ9yXCtN-qEbLNi_gf_CxXHCauTVtBxTRtGjasJ4iBSCdSp2U6dKlWMQiqXg92Aw9bXkfGGVeGLIoGoPnlPSkrmub61-1f79OCwQkSKUkz-3IRw_GJClZ5ba4w29dwOPE7AAdt5w7xRQ2WPbXiroIDGkUBmsTSl7exuP777qOLLOd_ABzFBMTE9Xl6e03koK55A_dt9y7lorTKvL_Wtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=KjO7KOFblL3eaQtNgZG_wTAI6q26mQqi4uczF0nfir9Ir1ubnf55RzYLfuy6v7R5znWxX3HYQLNO1MZDIQ4yZujnmV3PR02ZaTwPiReHfS4NADqxQipUFG4blh7zWzPGNHJ9yXCtN-qEbLNi_gf_CxXHCauTVtBxTRtGjasJ4iBSCdSp2U6dKlWMQiqXg92Aw9bXkfGGVeGLIoGoPnlPSkrmub61-1f79OCwQkSKUkz-3IRw_GJClZ5ba4w29dwOPE7AAdt5w7xRQ2WPbXiroIDGkUBmsTSl7exuP777qOLLOd_ABzFBMTE9Xl6e03koK55A_dt9y7lorTKvL_Wtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=V8xvPFL41hbK9eFZMLtp-0xfkP9-ekR8JJFVZnW8s3ATNPCb5W-_8Q-qCTEZO19wdAkXkb5uKalB201IcvFd3Lw7VlZizmbEIVOs_x9jomreKaSkY2uiaStb-zUxMFOulGa0lwaoNVh3-LZ3yYCZgYfOofByRSZylXklPfGcURTqXmFJsXQmqC0UEt9tHhXwKjchBNUlifYDwwWyKMp7VKGcn4yLTod57gG_GIIiTHMoHF_xGYQYVip3czIT8xJfWC_dkxANpIYfh45VYWrXaR09_XZ8QOzHu7TEJh-P7u7GdI7wwDegSe9r6mrtPsq3FdbWppg0IWQoTJZJBzrxhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=V8xvPFL41hbK9eFZMLtp-0xfkP9-ekR8JJFVZnW8s3ATNPCb5W-_8Q-qCTEZO19wdAkXkb5uKalB201IcvFd3Lw7VlZizmbEIVOs_x9jomreKaSkY2uiaStb-zUxMFOulGa0lwaoNVh3-LZ3yYCZgYfOofByRSZylXklPfGcURTqXmFJsXQmqC0UEt9tHhXwKjchBNUlifYDwwWyKMp7VKGcn4yLTod57gG_GIIiTHMoHF_xGYQYVip3czIT8xJfWC_dkxANpIYfh45VYWrXaR09_XZ8QOzHu7TEJh-P7u7GdI7wwDegSe9r6mrtPsq3FdbWppg0IWQoTJZJBzrxhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=gv4lth1jEZXzbYYejtPuvdKg4rHLYcxwGfmLyrqrr3HEig11EKr4o0E8fOk5VIlfWyg5MV99Mkb_EQFgEchBAfqxtCuSl3hsH39f9s9ub49vgOadM9cnkTazPZz-vPUpk-jxvwxUoIY93tCviH9CfXoqCjoWl1NPgZ0PO1kuPKT_DeB1WkUTiWaPYQJ758OKvwELDnQMT4pun27C5LE3QzdCiHm-VpB4KiQG4ugErqLBo456X2QRGAxRdXNAR5y4dNilM2543iSBRaTnaN1pQEVTsUcMTCPDAb2mfwtpW0iB-lNPzfraFdbJqE8LrFVQe7QJjIxBhwXq_qJHdc6GRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=gv4lth1jEZXzbYYejtPuvdKg4rHLYcxwGfmLyrqrr3HEig11EKr4o0E8fOk5VIlfWyg5MV99Mkb_EQFgEchBAfqxtCuSl3hsH39f9s9ub49vgOadM9cnkTazPZz-vPUpk-jxvwxUoIY93tCviH9CfXoqCjoWl1NPgZ0PO1kuPKT_DeB1WkUTiWaPYQJ758OKvwELDnQMT4pun27C5LE3QzdCiHm-VpB4KiQG4ugErqLBo456X2QRGAxRdXNAR5y4dNilM2543iSBRaTnaN1pQEVTsUcMTCPDAb2mfwtpW0iB-lNPzfraFdbJqE8LrFVQe7QJjIxBhwXq_qJHdc6GRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=QobpThaFLMXk0SR3Graj4v7VJ6X1CDrGv5Z0U9y0JORMZD4jX19zqhB-Ds6ACrjpVHPzA6XpZ36yqDa0BBtIRwNA9rbgoOoqJmYjo7qJo0Kjnq14EMePz-_-hgA51jcUreJk7EBx_7M1UyN0NOzTrY_nGRV-i7bEh21wTGUdiRvG1zPZE-YQYTeTRXBFuK2hWdrtTDlj4K8gYujER4C9nOLoR4EesjXqt2b6zaDQ2HXTq1wQyL6cqn7SK_xAQC2VdNkKqOM8LEnK7SVnr_bMt7PS2ZI5yKnLme5avE_RO4pOdhl63XGfpbqXan4QisSOYZmqLb-RAviQYr2x5Zl2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=QobpThaFLMXk0SR3Graj4v7VJ6X1CDrGv5Z0U9y0JORMZD4jX19zqhB-Ds6ACrjpVHPzA6XpZ36yqDa0BBtIRwNA9rbgoOoqJmYjo7qJo0Kjnq14EMePz-_-hgA51jcUreJk7EBx_7M1UyN0NOzTrY_nGRV-i7bEh21wTGUdiRvG1zPZE-YQYTeTRXBFuK2hWdrtTDlj4K8gYujER4C9nOLoR4EesjXqt2b6zaDQ2HXTq1wQyL6cqn7SK_xAQC2VdNkKqOM8LEnK7SVnr_bMt7PS2ZI5yKnLme5avE_RO4pOdhl63XGfpbqXan4QisSOYZmqLb-RAviQYr2x5Zl2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=PfwMplR2Obfw3L0Cw5CZzzzvwPxzMdgtmB7gQtDceU67wYRhiLL5l2Pyh_y8oaGNGBL75LHo1IZJsEP3Peb8nlRpr20e9ey1YsTb2zKQXLRBHlteQRojyY-vufGFkO7d_mRlzphlZjKLpH1q8cvpgt9xdFZ-jquqI65Tk0lfcEBtSYjNxZWK-apbsACy4vWuBmHjcpFNRRxH9I6L8jrF7v3zsaUsOOnpnOnfuielmWdx3Y-ZG32wNGst_o6n_ZKUbFlUvvXNOaLSdy1xRxoQiXj2_pPl8d2BqSPO1Ol_LRZpKTZD6etYtMdCG-ch0-1nELPjdC26nUa89o89hpeQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=PfwMplR2Obfw3L0Cw5CZzzzvwPxzMdgtmB7gQtDceU67wYRhiLL5l2Pyh_y8oaGNGBL75LHo1IZJsEP3Peb8nlRpr20e9ey1YsTb2zKQXLRBHlteQRojyY-vufGFkO7d_mRlzphlZjKLpH1q8cvpgt9xdFZ-jquqI65Tk0lfcEBtSYjNxZWK-apbsACy4vWuBmHjcpFNRRxH9I6L8jrF7v3zsaUsOOnpnOnfuielmWdx3Y-ZG32wNGst_o6n_ZKUbFlUvvXNOaLSdy1xRxoQiXj2_pPl8d2BqSPO1Ol_LRZpKTZD6etYtMdCG-ch0-1nELPjdC26nUa89o89hpeQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=SpuTDKiiSAUmLvdncCO-RYuQ4GW9uuRwLqlF9WVVTliPNrSUgv1f4X-bnHk4rbBbii9Ug7mMmDGRLKFiU6kgBETOOT5ZDiL3L_4i51lLI2Oq0hm6mejTOIR98Pg4roTbflXainjb-zjY1Wsw1v-E4Osnlsf-4FHRY8ozwrw2u0bxAQjQws9t5l_PuZ-DE02I8CPBZG0QSzBDDziXVO0porvqIbg3-MtBBi2RCfcPdjmVNptwV2of1KQECyX9uY4S0ihgs4oL8vdLz86JBjYCX4-YC4gArs5DuPzV6qMoWg0P8RraxoE23dqMoikXtiaEiN0dRHWQL8NcJ6LzmLqIiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=SpuTDKiiSAUmLvdncCO-RYuQ4GW9uuRwLqlF9WVVTliPNrSUgv1f4X-bnHk4rbBbii9Ug7mMmDGRLKFiU6kgBETOOT5ZDiL3L_4i51lLI2Oq0hm6mejTOIR98Pg4roTbflXainjb-zjY1Wsw1v-E4Osnlsf-4FHRY8ozwrw2u0bxAQjQws9t5l_PuZ-DE02I8CPBZG0QSzBDDziXVO0porvqIbg3-MtBBi2RCfcPdjmVNptwV2of1KQECyX9uY4S0ihgs4oL8vdLz86JBjYCX4-YC4gArs5DuPzV6qMoWg0P8RraxoE23dqMoikXtiaEiN0dRHWQL8NcJ6LzmLqIiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smh7unY9tMMT0msbKCZQyVqbk2GBGMn_IOeF3_DunLg-YdLTktY7B42ZFZjn_oHNKYgYqXt86tSfnluikZzmnqZD5h_XDmqa_o1Y_gmp4zrewbYpKkfPg9nHpMhdjAuCQp3JPIy2TkYLgP9GuRedWgVie50v3W93Bkf8geytqGx6VVexerhUIQgCVrVomYXjoqHCo45h2YE-QNXixK6SDLAtO639vZCPdRvxwVT-K4hqcc-AclSAhnnw4pYSSDi9X-p19M5Fjp6DToKyoDwGy5c_bpFhKxGfhUQ7OuAm9zGUjxEJFdz46pQOaWPRX3D4XpcqrKJwgknncjRRe5M5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=a_Vi19M0KJuo-DMqmCTj4WR97xsk0Bm-LBkZ2LbbtZCWjsHO_2dVcs8hxQYVN500mCLU7kbSzrQ2PQMUfOQI2O6l4cvr06E1VkmR21lTpU7gbFuwAsz8zd13zT3SB9Ijykkiu_Su-8l-CtPoQfMDbE_GApWz-EUsBecAMqSwSD6nXGlNjzUK8gR02wXYYwFhYo5aTntBntsygs4F2pNYUu6nr1f2xZ65Z84PTjUGyDpaYK_Fez6blELARRhiZwtX8I3l-Mbvo3yKsZ8AYh2dSySDQuCqd_dFIyxVH5JbXqtkfW6ByC0flTPmSnofhjbjjAqZ8j1RM66Hz1ked1u9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=a_Vi19M0KJuo-DMqmCTj4WR97xsk0Bm-LBkZ2LbbtZCWjsHO_2dVcs8hxQYVN500mCLU7kbSzrQ2PQMUfOQI2O6l4cvr06E1VkmR21lTpU7gbFuwAsz8zd13zT3SB9Ijykkiu_Su-8l-CtPoQfMDbE_GApWz-EUsBecAMqSwSD6nXGlNjzUK8gR02wXYYwFhYo5aTntBntsygs4F2pNYUu6nr1f2xZ65Z84PTjUGyDpaYK_Fez6blELARRhiZwtX8I3l-Mbvo3yKsZ8AYh2dSySDQuCqd_dFIyxVH5JbXqtkfW6ByC0flTPmSnofhjbjjAqZ8j1RM66Hz1ked1u9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0NzVCgtYMMh5kHZ78NFhsgIzuUYhzwMaoYvuuaq1CUyO_y8ORSdrz0NydSNS7_Lpj_u56t9r6dHmU5Mbr-0xp2ACdb5uwr_osqRcVAb5wSoL9pEYXhK6fjw5zDqwwKaKr9JeW_uYduHj9Tk_IOITKYMrIbcNquhSxQuldLzry2d0Hx7NMSFeGY--LtA1PCXFlVqGZnt3gPaEAV8kbNqCcTGxWXRZN2JazuwR6ZKcu9KD8JZfDxauNCiA7eTPP0C2NU6U5DUO3ZL26T_rQUcizzoboyN0FifIpOvu9JB_h3TnU8IvWnHYIhcaHNz_SkQeP4ajaphOr5jOzEz340G6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=GR7qdetDDqzA5EyKrm8-T9aI3JbVsSQE0-Yrn8cu0QFQyYW-1zA1hEWAS0ksa83RfVmsdkQC0euSZIR0zDZNojR-VDHBV16ACWuQ-QcSyoyC7jBfvgaVVEFnk5p61KIm2i3PMy_BFZLazsSs9YPEQXi9CYZSMWGpGU6A7jZMRW_-k_6qwjfoNvMJrD4ilHDadKkuHEmHKRV2Ti3vVc6gmSoag5XO9KJQeWju92p80tjQx8X5XYha4IJ58s3bRugHG9U-6Ar96Kozx21P38TnXWIXEpFwIoKtKeqyHnKZaNmkvPvU0odGZ-R98MBr_mtRJovohI9QXFZAK7UeD7MpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=GR7qdetDDqzA5EyKrm8-T9aI3JbVsSQE0-Yrn8cu0QFQyYW-1zA1hEWAS0ksa83RfVmsdkQC0euSZIR0zDZNojR-VDHBV16ACWuQ-QcSyoyC7jBfvgaVVEFnk5p61KIm2i3PMy_BFZLazsSs9YPEQXi9CYZSMWGpGU6A7jZMRW_-k_6qwjfoNvMJrD4ilHDadKkuHEmHKRV2Ti3vVc6gmSoag5XO9KJQeWju92p80tjQx8X5XYha4IJ58s3bRugHG9U-6Ar96Kozx21P38TnXWIXEpFwIoKtKeqyHnKZaNmkvPvU0odGZ-R98MBr_mtRJovohI9QXFZAK7UeD7MpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqD62bC88Am1T2rgBtHVfgjMpbHDl6mbygq8Ugs539nAMJqYvH3HTkbLETlfo3id2z3BeqPOyKiOKQsExRkb1iKbq15EMzSTVFe2hMCy5aDBoLn8I6UeAN7nm8wunmPV8XDi-Y8Cteh-nK3FGLvuBtBY9Wz_PVUntT3GLN066vUCLcxfQGDxuY80Devc_8Eq4_4Z_WAOu8Zd_tI9K4nhhLNz_D91-MEnj6K6jVQZ1xMJNdxhMzIbhdTVa2qiOEahsTbXW7XJSlHPcarytB5B6yqybIRQ_f98V-dEl74BsHdgWje15VvfTIlA-eyWTICBQ7whtHFnNolygTUkFZNSH0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqD62bC88Am1T2rgBtHVfgjMpbHDl6mbygq8Ugs539nAMJqYvH3HTkbLETlfo3id2z3BeqPOyKiOKQsExRkb1iKbq15EMzSTVFe2hMCy5aDBoLn8I6UeAN7nm8wunmPV8XDi-Y8Cteh-nK3FGLvuBtBY9Wz_PVUntT3GLN066vUCLcxfQGDxuY80Devc_8Eq4_4Z_WAOu8Zd_tI9K4nhhLNz_D91-MEnj6K6jVQZ1xMJNdxhMzIbhdTVa2qiOEahsTbXW7XJSlHPcarytB5B6yqybIRQ_f98V-dEl74BsHdgWje15VvfTIlA-eyWTICBQ7whtHFnNolygTUkFZNSH0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccbjrLNslwbdW6Avuoud5IjuWjiwymnQbhxihJ_6e9kP9zfAm81BKFPRlOS5reII2YfGWWz4164heBWhPhc_X0VHK5oIg2MQumXxUrnkLKb-Jxvz3c6TodgFK7OsWYJ_dgaNfCFJynAXv1le588jsnhuZ6Etx40loTvdWIVUl2KUEsdR9VX5WrMg3JjHbl3sULLhLsz86HOIg6XLGQrqofuTDb6V0jgwYI8KoLfYT_IdBDG3cQaNUSGfYqBk0hfSj5hohc6v9L-9IbIUddat3xu2ztepfKziD3yj4SnFKRBcXuUeYvdJMQTmniZUVIQxfrZTdnA_arYqqGSALu9A0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=Nj0MNlbku9qckq_v_QMaUbmt8kkX9iXpoYrGroBhqFQL7cDMBXdDonlzEREB9o_wRY74HfLmgNNmVaCvv0wZEG6Y8VM6Gkp43lJa3QqmUnX2ljtD7sWaHxH0R1fMrLBwPiNIuh65hbm9vjIoaJpSoswSMpMnS7Dr5BDpjCM9NTFT8jbkNSzaAPeSO1jHR7COCbfTDwGWwt1Gqlm0LYv4byImq8WMS91BRlSAxq_b7_xI18j9N7f0peODWP8RP-llnq7eYS1BF6DLhUKF60jJKo1IWz-LInxll6OfUzqxaz8feW_ZUJRLks18kbn-dwz0RYSGTyZExn2DkEsrb9m0MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=Nj0MNlbku9qckq_v_QMaUbmt8kkX9iXpoYrGroBhqFQL7cDMBXdDonlzEREB9o_wRY74HfLmgNNmVaCvv0wZEG6Y8VM6Gkp43lJa3QqmUnX2ljtD7sWaHxH0R1fMrLBwPiNIuh65hbm9vjIoaJpSoswSMpMnS7Dr5BDpjCM9NTFT8jbkNSzaAPeSO1jHR7COCbfTDwGWwt1Gqlm0LYv4byImq8WMS91BRlSAxq_b7_xI18j9N7f0peODWP8RP-llnq7eYS1BF6DLhUKF60jJKo1IWz-LInxll6OfUzqxaz8feW_ZUJRLks18kbn-dwz0RYSGTyZExn2DkEsrb9m0MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJI38HSU7WSSPjQI30dnra3LqJowxCh8cXgZ21e0gbcYOkeSpnVAU2Dm0mvODeW5kUTIbK6qWnTA6uPhGTidJ2ySuTwkzJDoegWsZvzQIQRpxFP1Njphn3Z37mCi8ndlvcEM4eNilcB4NJQa6s4icZnHw6wOef_WOzS9RG3ylhKf4CnXiet5is8NuDX19gBCPU4JdUIleRXnP399_wnWmQfI9RYFI7WxC6cyHSGM5dYRGrSl6KLxnsbyLr0uqly8q_M7MKQ-msjmygtXYX1zGf2AfF_jDiva6c9aI8G2Wz6vbKwBGEiCB-5qhfGIwoXJA7QyhqMn8RAD5R8oFkZSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6L6wAxJtL0aLK1yBoG4l9UvYL2vb73bvHHZV-uxF3kXQ-al2jOO0C4U9qNR9GAksMmmV4Z4bKUjVizhAqdbop5cIGuCp-V6kt7w0H_7DK3Jpi6scL_XXztXXVzOIq4v4KPrvIJuxaLC0idHeKmaFrgYrZSVqXFdjfZwZ-JwftX0lyMYx2twyuANOzf3XowII6p2D7VXiGqCm5F2y62z9oDcI44We-sNH1oWxFuYqoKVTeKRQhYWUYgViDlI-n78Fkip6rkZum_170ahIeALJ5rUgiBz1ZzaYl6Q09riK2_jUAbCOltnVavvp1doSFp2ab9DgZHQCTlLxDW-UDBPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ii43yxlVuqVLP6Cxj6zWWiAQPQRKx9cDqNO99KKXRgXE6OeZEfAFef1LczmmfH1v-zdx2BdJV_nr9p-_EVoIwn9AVAEDb2msLnr7Yb3F4Y-FzmvTGhxCwnxdBRvZzFZkxSP6yJAjPgk9WBGl1J-j1iMyrv7L-2uEz2noze2sqX0HmnSHgu72VmtbNjzuaPDrTpz6dn79JKYVzkvfb-ierANOGy6AhARRDLJhwHyC6pa8JoNSvl70aoWF_A4VLpxQAl3rbbEHbGqXngoH-ipIqhEoRykrUjGKb4i_2c3k3iAPDjIYoabQDPBTuKlOZSr6ciYPLmiYTktVAsVBqK45Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtTLG9vQGEbgTsUjQUbXMqO91AOy6ENEuE057FYgI6oqBT41KfIYcwmqcWlZ-woSI3ptwMQYNtSnumaoQtctCH7j5i7GypKwQseL94jBHWHkLRFPOGlEUnQLGupIETsdivF1K_8uzISZplcMOfn8LrrPlzcAG8EYXLH6tfREcUDO40AtxjTSLUXLKmgj87JdcDzBnsJfMYWCp3BH7Tmzg6QHEsCundX_zRT_9xlovKuNn3nJQmS-LORydovyYgZmBfhcvZBcgNEQG8h6iO1QBRuKu7KCOau7XjSWJ7zkOZ54DSeeLwetCNNW7rlR1XgarCJG37zbnZU2JXYb1xDuoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzqLJOPevjyoFweyNNbO3cqvEIb5BoT5eLXIFB7nljBLkvGgZwMJdVKzpXiu8PzI3RugnzVrEv5mkuOzj7NcAd1tzxtgtJjc8ZOq1vtRGIB2_FhvFVw_mT-ORfH9XLiRp23FEYzsnY5hz4UfPezb2FjVHL-aOKwLtOeVReYWJYbngrQXHIErIOTjaJtPSwOmmexZxH-P-_nVomLyhMwQqDyWZ1heHg5gOefqxj-FqkaoYMbOvnkGfoV0DcANoJo_ixlfhnOLLiWOSLATrP524xGr0jsMRc3dZgcqEbc6L4TAwIVX7TuWBeIj9vwxj7CMDspBLFLWDBV1xzAxXylBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5lAiWVYLUY5LyaBNESONVSLXaQfVmN_wG5UvZQxMiDY7EgxkUEq9mAWJn5zc6ddz6Q9fXUilxK8EaNs6W-jb-HU5pQeb3W4ucp0NkX-ehXzrU_phfGqIZBLet_3scc2atlYbBn3DK28O3XY-PEMu-hxu5N2GoJVMaN3FjjfhBRdG9dIFxYaookXOgso-a5XKbgmU_JCwiXjxENzvJhW4lCEYT9tlgnlnCS0eY89dDHXmorc1x62ZJ2ybAknfVEF-tgw4fd6-M9zEK3Gv6-Yl-p18dPB4tl_6VIv0oKAwdcyoiZsfUgSR0YJxjmHiFcYpoDzqHMmWub9vmc9pfuEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBQy9Tq1EmV7SCc_cAsxmhbEBOEY29xKiZODhdU_f1j-Ejin17b1z1pAIx-lx09d6QJXFhuzrJArx5BPtKjI9ahGf1rhBcotOs3EnGOs85pff75LHmU0woMDAe-ILvDquM1MKLvEsdffJz-Fj0juXKT_wI57u8fAYiehD0TPDyInDlk2sveKUHPUYXHScdS6qB0LzYPCKGib-CBGbXldjag9ZN9c7MK28UO66_2pMFPTS3k6-CZMJE9J1ArdJ5EcIhdnoVCenYEK8hNZWIyw2cFztB2fDyeRWNwzs-kBophU2mD45ckMG0WrkeKn4n7V3hM-AAZfZ3KGgDEmkizAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0JSMrbWwlcrpoj49jBu9wpFcrI1y89TvX-fcX-ItwPyb-UVc9-8LTEsbGnjVYqNVPNzAX0Nxbw8keYduiMnbXJ6leJOOfLVaSLo11bvGy8rDDBzlZ6HNmKSQJnYuuQGKrghwKfhg90W4bDeBCazghEHcjyrSOor6W-DCJzOr-kFmZSojKMoe7qNiRd6yjksl6twDWne9D1RuWnpsEfX9Ed5cCT5MVZoT7Wh8Wh-0P3b1Mg6sBOe4Yfk5LEzkMejUURxTJkVx9uh5tcFgVsllnt5I97rF5HeOCdIZjwFEyW7wFsGIbyhj24u8OYFp0RhltjfCDWWcYlpeY4gd95cTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm4JWQ-z_S5MbPBZPlVccxG4_pwXLeMbIVQ_swcrrXgD2kOpGQCwfLQtsam6xAVquL--FZ9bjNM9en2985q2BP5SAdm0GnuoTHY4jSp9ijdIWRobPBPg64ke0OVperRqac8ozCLrPbmmH-JQGaikzkGywaRfkfsFdeV0IiZrK-kBq7OHWj8BKN0lFAQ5cHLayQdwczMjiASPS6LgpnlPpkVy5-41G_nRs0i2RZjk_2gkJFMCYhjyenH7U-QqzgpcJImADpLqC1G9Q-g157yzptpZ3Q4G2KpoGCvNEPoUU2zn3t2OW9ER0WUhjliqb5SfpXjXKESirWQhYpuRfXYcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc-FrztWjacAc46uPoQaLUh5XFcp3cvPDfM59YNvBw4lzkpVxopMglEDnrtQyG87KJOvwaGZQcYbIlHfCVF6CsKqldZHblqlLF2p7ZbJxUTQ1vCcn0Glf4VyBt51kkZK2TGCd7o-BOKBHT52B9cpcnhToQKUQvKid3dvUCnZP6EZ7slgfhOXFpIVxVjxVWuc-INk3pBioI-Lp4mu_VtS_TkSm8O-xkDmV_FWSj-v7hYtRoghZF-x5nIguHnTRS3ooOdD6sVSSoYEBcX4oL-bBxsfzi4TbEHIkYN3BLcXWwsnbzJ5eRwcrI7yXFlM3hJJbokkVMJgE9YN2EBMU4A05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPt10WEozq9QB24or4SvoyaDFxCNSzDcPfDLO_OR6vPBoeZtmgOWpED8_Ims5FC2dRyHL5pbItDc1jAM-K9AOu_Yp6wEJ3breKegikW3yx1R_Y0VN_1de0cT4T37sRrOlLxby5vHBkh9wz-eS0jovpAA_0BTC9ZYioUvJHuk6R-ZwBFeE_NQXnzRq7nNi3e9yf2gq282U0IQk90JFvwkgju3vGe_AOINUUcwhQAuFevRRMzalER7FZy_kHlBaXW1hhOS0CXeaWehbTVaeSUaoZymJOcdGjhWfd9SKghjkBwzQkewqII6iuzCccmMvSu2LRz__VoALOzQVsRBpFk5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHXULuQbwrwyrAnuIl9FzJMkkvQwCSVdzFhZKCdGUhyd8wGrZCbM9AuHuX-TMShjfx1RDdZLdXiv1NIqP-LjzXQW28tW3Ald117zQ1xaqxyoGe9fymaM-1rX82c1vRPVKRR4YLdNEp1Nn43Bv_kq0YUCi-zOEM9-yMfbT9bo8iuUKL4c3f895Og8rbCVgwiHC5yglOFv_Lxk7j5oidz4YudyINiEux6cqovN44GC-7Lcza7SIgkOh5haCYpFmKZyC7AlKsX3EFPbNcD0hA6LP45rkuI2aSl3a0V9rz6jHpG9VIbvJcGqiTTg71q0g6pFzX7xaqKe0DwpBIrulq3Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsF8cYHVV0J1eY6agYaI_6gt2fMk__iIHi3HU1qv2xLe83yMglUZIaMN3BMxhPokoL9jp8T-izU08f3dKHoIl-O0LSR8g1QEfpt3PsIYvZm3hAg0ZDVTvnFEx7o8zBbuXlOjp8kTyV2nUNAyzanju1FqzhDq4m7eIj5rsPb-Iax44HQG4Uxqelhsjb4xKJMLYq8moowtMOu9391-GPtRG8ZjqML3EpWBnBVApaO8oASHm7rFnZ5-Qz0eM6IkeifjVCFRAg8ZrFEg6DP0D7cHqwghPpQTmjlmo6Dh3pHlXCDvB2WSSsbH6afLOjGxPKvPQupCSZ-575Id8DDdR1o0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nk56pqAN5pU9LDjf2fbcnBonKrg9qawKmmNRkwZ1PAsLvWsv7U2Xv6KACDAtzg1yIkR4i7a-UZtNebdwreknJ-rEsq1gJqJasntFwNKwYLkE-4sgzb_S8zMWJQV1F4ay5C2Uzjb7VO1w0lz9KLO4qDIyKGKfwAqRxoKKuamCv5mJa1b7KDOxb_iILf6hsib-pIrlkcC5K9VoOpW6c85lqPzdhqTyuRDdw_VzIRMvun3TFiYUsy6aUUSzdQ8gm3_b2XCRpy6IRsE1CevI16zzjnIc_qqMq4e-FAiHAUGy4Sdcf91Zpe8nG8DWYveQp70FOw-9OH5IFDO7vcBQTTo9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN4KILC5624QcfYk0ex7MYdA15oejuvjKnWADdwUxn2-hrxva4acYASHB1sIGfLR3xcc7KEvqtT4oN7XJiSISNbvRCe9Om12-XIiCYY_K5P0A12PgnLnwV7CesyUua_hgQYD-yCuNTj-AhemvsQlg9TtBeSbFpZRYJxfkTEOircRPAVaZKw5HNXjyVL-ZM9xfVsjNH_K4v0yurrQqo8vaqD6biPDvzQqHPcbK7az1gVZnfsP5I6W0iAka2qv6ehG3Y0xpb8TPEdcIon8gmYARMrxZZgJ104PnRf5LyMNehDS2QXJ-T3dzRsrqL91_E6REuRuCZui9OVk9W-Tmb2V9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjboNBfE41IZYwsG1kyzUTh4o_OeQh_r9tk6HeGYcN2EVa6GiJCnYVlZ_GhDPwsbCSNSTRaCeBharfp668_jQL4TPyUuc86Bz36HEjp0L4F3hEHW01UIN2YJnUSyNNNwxq_LzJ-9qiPXqCYuMa2Sm7nqPeMm-FwEwGKfDUqhOJkwYZ3H92A1PEvFAifLEhC_psKEuyKKYqjDLQxe7GRzldm0QvFrCFRvb53yqKXq01ukJgxq3BCP5F3UoOJz6NsR8YvskfiFSWIyJCML2iuTjqmONy7OEplZVF4EUSXZLQKmMI37geE2FY9RJMrMwGi1-8r5GtJZ3hpO3JnoZVWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOCzLferHFWJIrnA3kOttROBAKp20pf9K5VVFC0u-7vUJYYSPf492PwaEfbgc5vWlyowJoGfx9MNbcR2MKmR8SsQeAPV9uF6Nl5NX2eeydopLfxIQrZIrM3CIathPThLSIaoH7Q0Vu_xGmOukTp4KijnTeUH8cWOoeKnKoSg-NacHxYkZcGKYesNm8tcQuNWLHMJhCXtrMvUa496ld1x0K4u9NykiJkT69ACyIahMp9g-fLRxQcNMW4MXL3jR_KySPKCpNmnXIQmiX9fp7O_enX7910xnSbzotxW2tuQs9CKuQW51hRO-i48uB1YwhUD9bz6FK7fLtqAbXnr3DY_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbnyxKwDWFuT3de8FC1hslYiSfP62w4_tM9zF6XZItPUQGpTAlK_0o-4TQRQVxUaU_SLAy8xUpm2y9VL6i2zgnvGb7YkwwFBm3_oK-slvzZ1yMazHG3yhwu9ioTmiAbLEufSbumih9MnsBh1zPY-hO-4QxBpPVQs-H5TiBmKVPwUcSRNesEGktF3KnrXe0V8jVeU6lctrQy2_UJTkmLqUBJ1Fj5wdGvilNU06vGOmV0uALIAXsFhdwfl7mQAg9e9aBuucalxOSXS7ngjwKK3LbbNPe3d9pQ3_BnsdL1eam_vOCecb1YMnigBdN-8xpRDdBJNsIWC27ldOVYZrifpgUEUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=QZUNn5uu2ndyuRfEHD_lROYDCIbEcpcrdsftK7vKhxcVm7oAI1rC9fgofXVrAvFelj4dXD87cVJlrTw6qF17S4AhiNPFL_dAclC4loytJ00ttlMPgDNdKkOjfoJokfDd4soa7S8WUTlxzM70Pv_jz5s2HayRJE-uJduxNnDcpZTQq_e7Pcw-vgG8ZUVqMW2JSjlEjuvmph7cfTzJmWrLLshE5CN35duxD9pWyvO5_Ue2JNammbh138Hu9cuEfn4H1cshmBZj3EVJgryobbx9hEhsxZYeptniuQ5nYlHDqeSMYF3V4eFj9tYh4QCIY83c4Hlhxrg3h-fJW2OgY8fbnyxKwDWFuT3de8FC1hslYiSfP62w4_tM9zF6XZItPUQGpTAlK_0o-4TQRQVxUaU_SLAy8xUpm2y9VL6i2zgnvGb7YkwwFBm3_oK-slvzZ1yMazHG3yhwu9ioTmiAbLEufSbumih9MnsBh1zPY-hO-4QxBpPVQs-H5TiBmKVPwUcSRNesEGktF3KnrXe0V8jVeU6lctrQy2_UJTkmLqUBJ1Fj5wdGvilNU06vGOmV0uALIAXsFhdwfl7mQAg9e9aBuucalxOSXS7ngjwKK3LbbNPe3d9pQ3_BnsdL1eam_vOCecb1YMnigBdN-8xpRDdBJNsIWC27ldOVYZrifpgUEUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTJvalF-Z25fiY-YcgQDl8y4JPJ5bZ17_iwfaHpAyBFBrRXNRdmn620iJXNhJIgg8dOTomdWMoipS_67zBv9jWOZ1QIOjWu8w-4cdtGturOSUP5rq6EeE-WaFNyTyElCLXUKZjXd-yAYm909gP8owIU4MnQSO_2VT4cYJt1lHl7SQ9LLyQDSkVniwfFpnidt17f-JEKjJCJzO7zLFXnYvm8q_GQyuQVlBT754i-qEVPAa6XT8z20e2aktosR_GX6Oh9oKRmlCDxHeWxgNVX0826a7H81dUSeVWTS6tZ7weSKL2gQHytM7VIFsUDcgwJIr-PnjW-xzY7yBSoLE0EG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tl4S3_98Xal_HnJ3I8vzhkUrUeUZCQDj1t77kVfPQYgK-u-B7N0oBnRk7wqUuIfk-t5M1VTD-V-GUiV6G2z7kOPJzqS9ekEOISTo6sjNk0k0jcKc_F-k6O32Vh4SIbEPwLQ0wb2Sdiws_Eoc0WsjzzwVLSnLXE37TagGugHsfWgjGDXikyVUlLFS21cFEANhZJASLal1vfLiNXD0lE3c37x4tyvK0TrjwSfkG0taj3hhqZnnAa1CKQAAuHcqBnB2mmFZLagcsFG7UrcHu_pLZLm_Hrg7IsFZkQjWN9BiL2hXSHLjvRfjpnw6gKZ2oy3QgNNbqVbZvqwwj-TIvhpG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzfIpU8_4OJFsPn4_1iFIZrtQBjUK65faYTALNmHeAqAz5EQmr_2v2IV6tt1eIPrT9yXQ0-Ka1aZLhw41L2keKWX6MynlOSFPOL0se5VncDrPFiyrdOBRKxIOt1NO2MNroWbcItG3h4WbaQg5_Cy_v4ug0ZnnKdleXgYEroDR1x3SVARP7I5Zt7mm8H8JkLY2Og4lJM6_HwbY5ljIoaB7jRa8XW9q2Uz4mj1QFYXao8vNMvHXtMposvn-opG7EeETtaGYda0XFR3vlQIn834u17fJse_w1KjT80KcTrLL4x0YJUlJvi5P1QUZ7yvh-vC95rCB72O5HfGdHnbQR030Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJrkZu-iCnHK_Ef2KeHvf195miIUZKAvlzShtW7uOv2PZFZWBrI3e855J-ieKY0kJbrDRMjbf5Y7xytTyzj4wgeeOlXRnT-R6mYVX3skeaq5c6o84PgxNMoGjkKO5p1-b9LMtN1W8KXj4HZf1KGpGgsWfJ04JFeGEHbJ-5UW11W1LDuGQOvdqr_03J9_m7JeowuyFRfol7aDm7SshMaGS68JQ9p9LplOp_7ylL6YC1uuHtGrqxxlqgL1FzpGeMtrPI-B-9PPptyNcacYxBQuUpAnUFfxzp-t_nHg3fd1w_6UardzjpaYjjmdGapBzica2QYfxQjuoE89xD5jwsMd0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dufXrVjjKDW6pt1gF2L6PEQLXJrys_a1b24TSXsTFDTTi4HMlwjoRD_ZvEKOX2AWDT7BXIM781PbybgkFXiIQXEff8fKxVVIbH7jWiGMmWAGBeUJ6XFllcxvMoR4T3OYq106uvrfYik0kdInkF-vB0DVUHe4tVpzK8jhqqa9NDiTHE1aJBxTDpS5ZhInCncdIfa07MNaUrXFQH0i4JSv2t_tyklfOO7hQ8MJscICq317mpUfJ27D8aCjDoVvKsaUDtEMa5LDuEP0EAzDRgQLUhkhTsgTqk8DbmouvyGnjOouhKC0tiSzCEdFLqkPA2wH6F-jqx02u0l6VLu1AM1LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=MheQj_QAe3vConI7Rg_sXLLc83gY3EBzkGpnqFNvMMQGvx254x9fvY7LCZPC_LXflrRvErZ4gYMAw_Asak1BlaU4QG09wiMZ85-dmROYZ98t0rjfrILnLZbKgpqH4xFW-uChVIgPOorF4ZfB0d15MepYCy4lLQj0AbplXX_0D6po8cphJzRNGdJn1Ul61vfds1Z82iPJVfKasYMPc8Ak_mxLb0og9L-7eTWs-_Z07OWv3KijfA1LUF3ShzkkeT5QUlFJIYhnHT1GaSDwgvNKlfTpchoqpTrS9ozso2uhwDwjEkRozqnfBx8w_UVy75oPUbZhKCiByvKFFJoPy2V9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=MheQj_QAe3vConI7Rg_sXLLc83gY3EBzkGpnqFNvMMQGvx254x9fvY7LCZPC_LXflrRvErZ4gYMAw_Asak1BlaU4QG09wiMZ85-dmROYZ98t0rjfrILnLZbKgpqH4xFW-uChVIgPOorF4ZfB0d15MepYCy4lLQj0AbplXX_0D6po8cphJzRNGdJn1Ul61vfds1Z82iPJVfKasYMPc8Ak_mxLb0og9L-7eTWs-_Z07OWv3KijfA1LUF3ShzkkeT5QUlFJIYhnHT1GaSDwgvNKlfTpchoqpTrS9ozso2uhwDwjEkRozqnfBx8w_UVy75oPUbZhKCiByvKFFJoPy2V9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjL6TUZzAGERPsXUPRi458BZxI4plCNxs27_dwMgU7TpNudKQzNPmyIcnygLQwjebcVQsov2ZMbqMs9cp4mixJUqE7edseVTyI390TZbnBGGBtkkGkkDckmhirGKioZgG_hKgTnsI2KtyQtRo9Vxxlcqhx0LryhRPEQllND7OfNvTc6DFRm_SOqsB2md5v2EqIIWYBlncHEMtI8RbLWsRiZbHIz2pFs9BMoSWgNaC-vd2fpPRZtsH8RFFMfDS1NNmziklahi6wJisEoFN3CdP3YZe4d4pLsz09PHrRpujL020QT8Dje8MMQlQO8wBV7C0_1B21tCCAEfVHJUB3Eijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N755qaSPnUHlRMjcb7BKftB33kWdNWO2G1LMbPILhlVOGuJV9wxMfztLBDheRa4EkTAiYxSESIR2vyWp85pt7EDKYh4kCrkgtWfDEnEK6V-pOqPoH705HLabOaogMZGPdp0XJrzmZ9K2AGoGDeDLSdbQ1dqnMLlFh8dtz43V3CuHeebDmw8r2gnFnk5m0zvmhRYP-FN4dbYOFEJbZLSbktZtAdcdWp58zHqXBljy7AbstAsWltiJakyxDsBzDEcl7uSDGt5EBHPrflra1Vf155FoqemvTsV_bYXWhKiJ2v7ocS2_qp970tk_2Li9ntNLEG044fJPt36uIQSr13-GbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5o0IWumPxZjBtQxLXef1JFTtndOkB5cY2xjRJX5AXDYYkkwXtxfcz_FkwE-EHUZqcxuNhx-S64mX0THE5k-bvgNBIz33uWEOH45Q7Y9fczxeFtHyYsyxChte2cQwZu6Ll_9MBYiihB44-sYWqY7qnSmL2gbZ5sKyyE41I2zobkWes25r7Zd5VtiZJhYSWN2bTB60al7RIPmVAjE1S4kzL9duxp9nzDtXc-rOlfz-cHOuUpnxa395ENNXug1KDv-9kFgZ8bNTOZ_blG59lHGfwNG5wKMBdrb_0tZ-q77fpYM6sUFMinI7OUt1Vz3c6cI1g7AcNmEKVMSQo5IbWZ8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACLX3-Xqt1GL8GroMLIG7pXis7WNXM5oP_IqilOhr1ymFWOaXWfjvA7o77_I8ZiU_8pC2wNL0JGw2w66l_e3tkL3OxQrl8mvlBLEu2K_kIkI5gC9ngJKZbYRxJLBAJzp5qyhyX2bqgRcU7U4KxE5t9uB1cB0soq3ukCWNUsLJC7pC9JMK5jLR_0dMcQMXt85Ya-xsncir2om6LJvZVnal05im5YEX07Q5x8zR3uENxmYUXRpvRQ1Mi4llYqfvc21FPp5Jk2lwlIW5vjkkag9Mldyse3YmuPOrBYaMJ2ry9JJ7lsuTtAHcwLy9rqjHg9f_NkM4RsUQ9NpjRNqd6wWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRk8e22s8M9Kl7fgPa-SM9VU0YkOjD76x5XFZG6OLPOvsn6GRD6mIsIGtLFoJu9uVZILT1qaS0dE9l23VmuL-gUmOb60iWKoWcmOn6FXsFjlVTX-0TDzp7wJMo2QPeQ75LsUS3p-XoNxZ_ui912_cOgFJo5xL7EW56_IM9oWVtwjT5Ry-s2ZgGRpWoB8niIOduH_KewLG0Iy9vVCZzA6vcapIwxbdtcSzJiWYYzqU7xXpgOIpNLNqOi3f2Yxj09qNpN0X4St0OoZOZHZgFLG8UJlLpnJKQBa_p-vwDTaC3X5WLQM0ENVgJDFuyFcXrl1YU7zuE4JHZypNRPYz2xH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JiSHb1voZOpsEya0glzYoVFgAKTkDRyqvC-AUetAVFeC7-8VA6NLi6SoC8t7ITFA85ICfEmC878ElcCYJpd69x2UTLicI23sEmU3ZQCt94oUv_0UipN-VGvp96LQtI_WZDjkXbTA7yaeqV5n4ivNHkzTyCusRTuOnm3bjRUTaB5XZYF6_f1er8la-9a93nO6mRJoy4Sg9QY8FRcWXCSnX5U9y2wKT7nvOXZ3uFGaXI56e3OCxD_Aeznh7gaFGbweCH9O6Rd-wi7CbELSBtpkhTo9ltAzXmcyTaj4r_nzJL7nSWfzH2b4n8JEGLIKlDvzZ-XGA2t68CJ0WApONB6qLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br4Qjo73VKUYX9EyaeHrxpsNPHazVD1kKvVN5sjlH6141EKGYifhJbEa5SUTVwB5N8m3job3NrG53340BOvZbAr38u5b-9YA6aKb7DiX5WZ7Vk4oxhrb4ygbHsycDa35be6AuR7Js2jNGSqCVAmTYmWYN0tqCfuPnOsTkyK2HJKSBqRWBfQD9nMJv5cmzOAnUEpqyaEQjTFFfz04pViuXPAxdj5VQ2_yys2jTHMuYUACaV8wi-48--ayYRTm2l_NT5h42g-JMNCzKfPkA74mtI9c7_I6r1v-tt3z-bAv-g_Ki0Wd92xG4YgCPC408OWCj0XqWyQ0qq_HV1EZ1LrxNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehJvDqPgzc61PkZ5aJqXitidaLpN4484n488JiXHqirKO_lS4exOf-pAVAIUG3PaO6TBonGA9efoGUujTaBk9jtpcF1Elbulji0A0KBvaG1sY93SIiUxo7GdVnkWiJEK6eyDbwOIBaOiyvw-tx6yTDaaLSk4Qc0K4v4vKp35S1tkX5bzcXxUhm3Qv7vapftcpoHX9Ratzs8LUKy02bu3ET59wf2PaGYAZkCoiRUvbskOd3Kw2d5jOw2v0sNmF54X-zqk4VZHg6MDK1r6Aa5esHnweQTX_nEU57S8NS6K-YVaIKno7X9h-hyGs-dQovQereggoCJch9Y2vitm5Fx9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WncXUJ8jLl6uTHWFpqF7oREjiXVJA-tmrE8hmaIAz1Xu8qU5LWEpGNW9vwBanZk5noU7VA5lGmsx2sDE4Pj8TVvklm4P0GtImdl2Q0aDXAWPFJN4WJ7eEYFOq1ddmy5bR2HNXfxEPUCQ0ouEcNaME4u35kOwqwf95rTTus2AQhfx48t9nukf_YH6kgjhnxL5lGogJkXrRFJoRLxzAeAivd9oCFWa1JWLkBUbRlXlEq_0ob9qQool7cznpQCo7SauFSt81N56heK0MH_fzHxrLBUoKfekM2hLtCXWGbl3lm2NQGllyS3BNr7KE6Xx-IBzc-240UKsdd4llO9ht3N9mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
