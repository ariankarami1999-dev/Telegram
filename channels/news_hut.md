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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 214K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m880LGFQ7ETwVsVWyYdn6CwjoXnzDJYiBh_ZQQpiXTyKdHRy4LcA-IFD8J77EjiouuNXXV4xt1IJDkTWXUAP_7etjxzwrPmpGSFyS8GaqnQh2mWgpTaL-aucmXXHzbE-M1zAIxNjm4fysUYnRX8DYqZELuaa48J1Vv-_BCWuZw5bAYvoqmzLhr_x3kgACTxK_O-5zVud6vrZWNahgJr-EbclUKMJrRcB2FUEcMXvo070WpHZ6awizS7uQlv1UEFNE8iVr_ZtXorvJNf2mMAkL4KCjaHUHx8zQBn6hNruV7vd1_U4ZwOt9ktlBUBq_ky68clWo7jTKCUnhsMRsU7C7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=fdv7NrbZU3GGtLpOqz5jLp3j-73fUaxLdqWSo-oWMAGoSxCNQcR-9r_WtPiwuQrZ238Gz-1sOQVPj78KbrbCnhzwkH600UMxCb_TsKSbAr5gcVz6-qllreCT9oyBrtnXE62SdAtJvQfGJYsuq7gW4Sx305XvncF6mMDb8Nr2PvKGUteMeRG77GIWRzv5CNQ9ByQQjKB8idw2jo7HKSMoGcB-cGVkrIc9xbcVRRqUTxUia7itx5uBDff_Aw1IgPlOi0I9U0ZaLAs8Jb9YDj_9SgawIG8H-jmAYBA1poQALzZFCequ8ot7RVqrO4l0XunHIP6LO8nrkKVGMZaT6KM4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=fdv7NrbZU3GGtLpOqz5jLp3j-73fUaxLdqWSo-oWMAGoSxCNQcR-9r_WtPiwuQrZ238Gz-1sOQVPj78KbrbCnhzwkH600UMxCb_TsKSbAr5gcVz6-qllreCT9oyBrtnXE62SdAtJvQfGJYsuq7gW4Sx305XvncF6mMDb8Nr2PvKGUteMeRG77GIWRzv5CNQ9ByQQjKB8idw2jo7HKSMoGcB-cGVkrIc9xbcVRRqUTxUia7itx5uBDff_Aw1IgPlOi0I9U0ZaLAs8Jb9YDj_9SgawIG8H-jmAYBA1poQALzZFCequ8ot7RVqrO4l0XunHIP6LO8nrkKVGMZaT6KM4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=XZln5zzFH2RkUlm_kzkry2K8zj7xlwqSsPuTtaOOi_i0PcXYoI32pyyH9dNXMWMM7-cJbHsUOCjOiZ7nxV7p5DRqnpWnx0JKAKogJgtWnH-vDV4Ouzsf5X3jIWsomV2eCN3Nm2qHJFKqRF5jwqDa0JCQdN1YuxKr0MlFfS1m1SE3OKrTvHkOJhKlpgyDoJmssOD4PmZj6BOO19sdB5Su2bObLlTNXP3IWobjo8PPTaQ0OXDbjKk-T-8ueSMIoQacUzLubpE0TuOFkcneqV-rQw47XOiTtlZfedC9yPRNic5UbNGLSaFA8r-IPgS_YGC_q2Xi5l-OEzNAf_aUiuqe4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=XZln5zzFH2RkUlm_kzkry2K8zj7xlwqSsPuTtaOOi_i0PcXYoI32pyyH9dNXMWMM7-cJbHsUOCjOiZ7nxV7p5DRqnpWnx0JKAKogJgtWnH-vDV4Ouzsf5X3jIWsomV2eCN3Nm2qHJFKqRF5jwqDa0JCQdN1YuxKr0MlFfS1m1SE3OKrTvHkOJhKlpgyDoJmssOD4PmZj6BOO19sdB5Su2bObLlTNXP3IWobjo8PPTaQ0OXDbjKk-T-8ueSMIoQacUzLubpE0TuOFkcneqV-rQw47XOiTtlZfedC9yPRNic5UbNGLSaFA8r-IPgS_YGC_q2Xi5l-OEzNAf_aUiuqe4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLkMlisL9Lh8vG3w12oCoM1P0OTvaKT7nSzLJQl4FjjA0gxQA0ikvaa8LsKbVPyqjSU0kwdm_TcPzcWkpf7niEtqO7NjjexK8L2p-K67wwP0OL0SXl3dBYpVtY3EID-pjcKofm07ijxV1tBmaLNNA6gEl4GAAbfxZaDo2Nio4GmcjLvV_2sCTkUaImgLp4oWcuy7gdcK2kYD8RDDX5R5vYwZEr5SrkHfbvaeg8nVXVL6t8g58v9x3XZ1v1kL9949HpL5r58Myss1vbORtJOC4vlWaT9JSoshXqT_evy5GAf3FoxVji_4eu3FkqvAfW8rcc-J-Zf5V1HWOrlI0XAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f10MIMpcOz0kGdTQbmkTzry4i1l4gRfUf8gtOELDdqeIdfZF36YTSDY9LZkyLn35Iabmq66whEmSwMgMK55z8aOnCi2dQv1F1bDNxcVTibRMkIfUx8sjfiL9NFJoCRdlMQxRVKzix4Er-OxPUEsf8cifWpb7LZeBUjjdEt8ffUVeSvZ6trFAHCqEjJBAjgNOTksf2AF-nwBmtCHT618CThl2ZQZ3tve8KM9WMd7tovCuJosfd5TOSDWV2LtZIyBOB2nn4bcDa1EsGWb16DTamj7o3ukvz7yGWPTUOM6p3puoPvOU2jeFjwC4N8InoHqKba-MUYFKw0xRiFAbgj0Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OteJF0hYRGEzUIQ9egwX3RlFqS2WK8-hIEknzis_US2kKPDCpMNNGP31P9WgUwAKhdT5oFSlr-Jk_pbP5kHnuPuuYlAtAUDxHJABLeR0nkEem9E3Sf9S5Tn6ImyqnHMJSgoyekC7SVMuV_XCyho9M2vaMjwAmk15ynYVpDUbbsX_yLZ__qRRo2mI3XyJmPjY9xEjtstM1JAO3nkuDLflgafviO2znihGK_KfUU9y7yDlmJpGrCk6zQp-lpYw5eaH95Y8U3ghLZ-LoDjmDoLDNwad43MPE70Mun1QLp7M6K76toYv7CjDF3epUzv0GV0LHIVcBFDU9on2BNXXqLbU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeEbQi8T2PC_sQqd4hKtH5vzOSgidP3JASufOrlidF1eEZaY4o-yRsCLKsjT_3fsH-K5zptddt4LtVRZ-ioni_Y9E6UbclXyeuRixzMGabj5ChOKHV5V5qSkdn0mX4IzM34HopQfn2DffcN59hq_qWfbvHSs4ExMnLPsIbYkDB2xUeBWhE4SuJUDLWvuoIXfaK7bpN1TYEtJ616qILHX7IStR-60MRKgkqH0wkfyobryJ0wKaeGm8K8fk40BzqS-ypFN8nSHfGw4wBiinMsnt70YY-MhmmaOhguLJFvOs7KgtfgDp5_HeiGHf_G0NkheESvTscOdaiPUnpa41kv0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=PHssyFlr7vHHtly-1-v5aImoxnF21OaULXiKzH-q8Wa0V6aTg9keNrfo3s0pQiuqyHV01H7VlWwgIj53HP6mJpnvWvrTeJ6F7svT0fzqZAqgbbjGfTyn0Wydo7sw2qOXORY_eP9QJduFcKgHogiNGaoswpta343n5nmZECiRXG-lUXrJ-6OAs1y-BrQWYYcnH0g9NOazYQyasE-ITESoBczrjpZ9Srf9v5TfAk_6vTTon5X3cZWe1lmttLu6CStHkR-yhOUcCFpZSAqY_eKePZSgASKlL0UTgf13H80CmoSS7VAbGY0qIYpPzL7QJUa-zw6MtetHvvJa51mVYH59Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=PHssyFlr7vHHtly-1-v5aImoxnF21OaULXiKzH-q8Wa0V6aTg9keNrfo3s0pQiuqyHV01H7VlWwgIj53HP6mJpnvWvrTeJ6F7svT0fzqZAqgbbjGfTyn0Wydo7sw2qOXORY_eP9QJduFcKgHogiNGaoswpta343n5nmZECiRXG-lUXrJ-6OAs1y-BrQWYYcnH0g9NOazYQyasE-ITESoBczrjpZ9Srf9v5TfAk_6vTTon5X3cZWe1lmttLu6CStHkR-yhOUcCFpZSAqY_eKePZSgASKlL0UTgf13H80CmoSS7VAbGY0qIYpPzL7QJUa-zw6MtetHvvJa51mVYH59Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4nBp4wZ3YCU_VVtZHrFQaXUXunLFrPW7IGexFPw-TJzztshtQe6ifA7OI_BoICYJAq5NPuSeir7hF3ZZTt8DLjCRGCyxM0hLEOgOGZh4vOcL6NzOWtOkXa-bK3OhIB2t8YZkTNRz_e8OadBR947PwPfe-KDkR03AtmTUsOUbJi3n-fyTjQiXVaxcel-dfvUCHV-jeSpZ54NGfhxE63PWz6krDUnbeL2zjWadSrW1VrRwSWSOcxGEm2ymp_pOvbJjIm5Kl0gvMVLWs8xMfQx-7If_kOThHYdyqN5P94tLoN3GMNfbtTvA1JNU3Ux7Sz_u1yI-vJTZASrC1liiHqzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=V8id6SuS9c3LMKWcF7oZplnZrWZE0rJ1SO355Ht7cpdEvpK6i0Uc9nDmYRiuSygW-zUVljmsH6vgj-zMjTV8_rYwekJY0mOoWDN2hj3XHIkbKNocIjIRt7Jic0MJJ1aX8wWgZFZNfY1hETDWyCKkeBta7kvpeIokbukf-z1AZUIVZ-_LSQKmPBJIe3FC8lJ8aY-s8wykXPXrjyy9m3sYAQPqhj3OAYuvhhSbK9ECVzuEXQhOitHiZrl_guy7K_Q8DFiBk8-nwTkrzmRQqvPVOYzJlPekBj-wgF23N601VlLgatSQM-JeYdzItuVigJusyi27L6vCqSlG_FZUyOx5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=V8id6SuS9c3LMKWcF7oZplnZrWZE0rJ1SO355Ht7cpdEvpK6i0Uc9nDmYRiuSygW-zUVljmsH6vgj-zMjTV8_rYwekJY0mOoWDN2hj3XHIkbKNocIjIRt7Jic0MJJ1aX8wWgZFZNfY1hETDWyCKkeBta7kvpeIokbukf-z1AZUIVZ-_LSQKmPBJIe3FC8lJ8aY-s8wykXPXrjyy9m3sYAQPqhj3OAYuvhhSbK9ECVzuEXQhOitHiZrl_guy7K_Q8DFiBk8-nwTkrzmRQqvPVOYzJlPekBj-wgF23N601VlLgatSQM-JeYdzItuVigJusyi27L6vCqSlG_FZUyOx5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=uPtJSeUR_MfbOLcE1wH1eozdIRXRKaN7Pia1jVKw4mxv2dHc92SWu2FokSObc-0XJ4aMNFE5ceGZGqGw6ulDyYqj7xQKAA4BVFtNNhLIj5CyGFVonZaH39_EPMjqBTQJ592Z-eYqYahUPucgggCkkH8c43fuZoeOAlnmOB9h1Fc3436WnNh13XEVc_XeEbsmiWH4pomrMaiuhwBs93vSnuPSejkk9EQ3ttdJ26BZ9KQA2QAT-nathTNfhulfKDj18KSDxsrI-B5UcPpa9OLs7o7Mce4-FsgJEG1sbwLmx22mAS875cwGqOdOM5nAoIQY0XZTxY1SDdNGApOHzYA3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=uPtJSeUR_MfbOLcE1wH1eozdIRXRKaN7Pia1jVKw4mxv2dHc92SWu2FokSObc-0XJ4aMNFE5ceGZGqGw6ulDyYqj7xQKAA4BVFtNNhLIj5CyGFVonZaH39_EPMjqBTQJ592Z-eYqYahUPucgggCkkH8c43fuZoeOAlnmOB9h1Fc3436WnNh13XEVc_XeEbsmiWH4pomrMaiuhwBs93vSnuPSejkk9EQ3ttdJ26BZ9KQA2QAT-nathTNfhulfKDj18KSDxsrI-B5UcPpa9OLs7o7Mce4-FsgJEG1sbwLmx22mAS875cwGqOdOM5nAoIQY0XZTxY1SDdNGApOHzYA3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=p0zThU-xwLhWLMchLLA7HadfXE-COhG8ZY8AX3lwrFej_FswFNSKdTI4HBpgSEDzvv1o9OfX4czokqWRoIww-_eoJknNe_w4yCFChPLqehE6d39HY7Ca873jPzH9mLyGnFdnHSY0YGjjKORVDyYppUeVP-UaxjBW4zFiG2uL-XTOYwyZWeEHVZd2X-c7M6FdpcVAbh6oLIJS4bG3lUM10AYNwvjFxM7dZph3TqiGG0bSlATcHTo2ZDepaC1434W9AhX8nUamBKiqTLQU43-B5Bw9Q2yW2KVQSBGQxbRMZ9nH-csvh4kNG8i68N0lFGnMTaRc5Fk3b4mxF8uxU7YfQnNDGnLwdaPVGg2r3XKbk8yNuNdRU9RloYRZt-SeqHrhW7hmes3qS_7Y2WqNbrzaPn6iN3JQ9ysxTkngYK9T6Bf0adEaId_mUN-F0U1_DITk8VEhiglgqmv22agXIZ_Ypf92SgHPTZ8Tvsi4h79aHVzHIAyZrjmym9bXOZjwINRDK7VVtfxLaFqAIwZKdCsLgQ5Ie10wMjR7l_qI5_1_mn0QyYXH0fw4CKquijMr8wan7NcZpTslHk5uYdfE9nJei9qOc9aBBKvBsh03SH4rTT6abZ7GdbB8_-MgDX1CJYTf04fz8zlnjdIZFp7iEZPse0US6FpX2AGTTQ9HZmOwc7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=p0zThU-xwLhWLMchLLA7HadfXE-COhG8ZY8AX3lwrFej_FswFNSKdTI4HBpgSEDzvv1o9OfX4czokqWRoIww-_eoJknNe_w4yCFChPLqehE6d39HY7Ca873jPzH9mLyGnFdnHSY0YGjjKORVDyYppUeVP-UaxjBW4zFiG2uL-XTOYwyZWeEHVZd2X-c7M6FdpcVAbh6oLIJS4bG3lUM10AYNwvjFxM7dZph3TqiGG0bSlATcHTo2ZDepaC1434W9AhX8nUamBKiqTLQU43-B5Bw9Q2yW2KVQSBGQxbRMZ9nH-csvh4kNG8i68N0lFGnMTaRc5Fk3b4mxF8uxU7YfQnNDGnLwdaPVGg2r3XKbk8yNuNdRU9RloYRZt-SeqHrhW7hmes3qS_7Y2WqNbrzaPn6iN3JQ9ysxTkngYK9T6Bf0adEaId_mUN-F0U1_DITk8VEhiglgqmv22agXIZ_Ypf92SgHPTZ8Tvsi4h79aHVzHIAyZrjmym9bXOZjwINRDK7VVtfxLaFqAIwZKdCsLgQ5Ie10wMjR7l_qI5_1_mn0QyYXH0fw4CKquijMr8wan7NcZpTslHk5uYdfE9nJei9qOc9aBBKvBsh03SH4rTT6abZ7GdbB8_-MgDX1CJYTf04fz8zlnjdIZFp7iEZPse0US6FpX2AGTTQ9HZmOwc7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=qlKOtOKujml6vrg2bZ4IDthfAjDpE_rQqEpkqj_OC2hIzOBPMDEV3BW3bo7JHEeYsRUVrWWaZ_CxyBhQUVBGuPC1lPazKRZlf9kgwa1gQHD00kLoQSxtPdCk79ax-aVc9MBd93miXoPYZYzK7CuxkZonpjkW9pH1N_5Yxk6MPvLIXGNIghYKSYAj_kbLVSAUHeBkWqSaMTYFlk4RHFpcI95WmTpcWmGFZwbidXsEA4DW436T5Kf7JZjf3_dzvsPtxH3oO2ei8ExIzNutyxSu-18TV7tppnMUjc_g0cpVSIjJCZOQ-MwHrtHDdsRQsO4R6s3SFSkE8OFiIhoKXJ0aTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=qlKOtOKujml6vrg2bZ4IDthfAjDpE_rQqEpkqj_OC2hIzOBPMDEV3BW3bo7JHEeYsRUVrWWaZ_CxyBhQUVBGuPC1lPazKRZlf9kgwa1gQHD00kLoQSxtPdCk79ax-aVc9MBd93miXoPYZYzK7CuxkZonpjkW9pH1N_5Yxk6MPvLIXGNIghYKSYAj_kbLVSAUHeBkWqSaMTYFlk4RHFpcI95WmTpcWmGFZwbidXsEA4DW436T5Kf7JZjf3_dzvsPtxH3oO2ei8ExIzNutyxSu-18TV7tppnMUjc_g0cpVSIjJCZOQ-MwHrtHDdsRQsO4R6s3SFSkE8OFiIhoKXJ0aTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=GUheJ42tHJK0lXudTitClsqR-8QZupCSXsVK3d5n0L5n2Qu-_XrN6rAMo-Se5lN8wHp8mQJk3w8IdzOzFTPk0KEAI6pnr7Os9YvOF5VTr3dhi_W0WEDsRQ2LwoV40z1RN5EWE8IaYQ2dkrsQJFO45SLBa8RHzUOp4yLMWiyYE8Qy9gq5rXYY4j7leLTj98EGgcuhGtD6UCNIuq5XoabbxcR9jNBf8OkzxepxfeECzmf3bOPQ-7hzOGY_dqXr_SrqqPKURGMQsxmHBGB86TNFhWv1AlEoOJR7YkH_po7Hz5Ah1MvcdJNBCIrT11KF6nY01wn8VJbL7FH-PMb1rGCeXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=GUheJ42tHJK0lXudTitClsqR-8QZupCSXsVK3d5n0L5n2Qu-_XrN6rAMo-Se5lN8wHp8mQJk3w8IdzOzFTPk0KEAI6pnr7Os9YvOF5VTr3dhi_W0WEDsRQ2LwoV40z1RN5EWE8IaYQ2dkrsQJFO45SLBa8RHzUOp4yLMWiyYE8Qy9gq5rXYY4j7leLTj98EGgcuhGtD6UCNIuq5XoabbxcR9jNBf8OkzxepxfeECzmf3bOPQ-7hzOGY_dqXr_SrqqPKURGMQsxmHBGB86TNFhWv1AlEoOJR7YkH_po7Hz5Ah1MvcdJNBCIrT11KF6nY01wn8VJbL7FH-PMb1rGCeXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=qEkiBpCl94BgqLWLK6Gqp6_5Ig76bL5vnSjDjZ74uX46ZdUIwHiy7QmZg2mVVjh_rIf57Rev5zG3WTrxzaHv-uxoIaNAuMf_L-MyMiaCgt-oGv_YOivHT-Ad2PE9PlZ7yjkCn_pHdSx1uTPNR1hbBtJeSWlycIhgQI43ZcFTaMbZ5rFKaoc2V-IWKaZ0D2ug6jRkZ1VNeH5BWyPLpde21gOOOuKzwLeaW1mGNjhqIvKpv84geph8D7YyUS-n3YLP_gvZrxDd6rISnLxpx3vAWb5yRlGd2J--0Z9bAIJ89uPkVICcdoc7SOO8bRTZY2bmBSvgISXyZEKuQgUuujWCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=qEkiBpCl94BgqLWLK6Gqp6_5Ig76bL5vnSjDjZ74uX46ZdUIwHiy7QmZg2mVVjh_rIf57Rev5zG3WTrxzaHv-uxoIaNAuMf_L-MyMiaCgt-oGv_YOivHT-Ad2PE9PlZ7yjkCn_pHdSx1uTPNR1hbBtJeSWlycIhgQI43ZcFTaMbZ5rFKaoc2V-IWKaZ0D2ug6jRkZ1VNeH5BWyPLpde21gOOOuKzwLeaW1mGNjhqIvKpv84geph8D7YyUS-n3YLP_gvZrxDd6rISnLxpx3vAWb5yRlGd2J--0Z9bAIJ89uPkVICcdoc7SOO8bRTZY2bmBSvgISXyZEKuQgUuujWCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=u5hfpdqSnxwjNj9fcww6vUbxBNlNref9nkphV4iLzeMpCXmT9KNPZHJuAc2W2TnW7Y3cm68jm8Y-4cv6vcv9lWaIZZsIuSTrmpGqHayA0O0JCxslt3wC5DcmrqDlOiR9CSyjACoXleoY2e-LRpvys0fyg7bhASRs3jvaLEqMHww3f9jiTlVqmDA5GMbb1nzukoOGYoXnpMH7h9PhtI7Uuzm6kcg90T2Gsm8U4On-sQWFRWxTYs69zOdBcj6ej9T3lC3x4x5sZRezgKrOcuP8kj_FVFmo3N9EpW4lu-p9EP4Kf7-Hdp2BzJ1q8XDvRdRP2RlPWrEaODG14uNNBOs7lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=u5hfpdqSnxwjNj9fcww6vUbxBNlNref9nkphV4iLzeMpCXmT9KNPZHJuAc2W2TnW7Y3cm68jm8Y-4cv6vcv9lWaIZZsIuSTrmpGqHayA0O0JCxslt3wC5DcmrqDlOiR9CSyjACoXleoY2e-LRpvys0fyg7bhASRs3jvaLEqMHww3f9jiTlVqmDA5GMbb1nzukoOGYoXnpMH7h9PhtI7Uuzm6kcg90T2Gsm8U4On-sQWFRWxTYs69zOdBcj6ej9T3lC3x4x5sZRezgKrOcuP8kj_FVFmo3N9EpW4lu-p9EP4Kf7-Hdp2BzJ1q8XDvRdRP2RlPWrEaODG14uNNBOs7lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V84D5nCOMiH8VTulVQV1um3FlhHLwDJpcAIPhPB9sFVSHJ78LKxTCahSegEJ2dbWql7dXMgZ7HfwNdej702sPZgaWNjyfsiarYixcGrQX43dWQXiLoqE4DgxPYjRpoqQKD-O3Z8mJ5ubcyQ6Rlpjta4l6DxvVMm6gsR8ypRhd7dBvjobJMLsheMBrVd6-REV0niEitLRgh032ogo4UiLwksRMVVFwM4V4pOWwXEzjewy9JTHjefcsOJoKQkhbELuPwUjReJOZXWV5Cec8wApXbYoUNrVGSLCvM3zvyZyqNmu85_sYBd3RIvpjAeEDaFt9z779_qDKFGXDsWuD6pdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=sGABAn0liuMpHMfOW3L3-b2iS4vLcRRRVxnNd8TPLOWbKa-H9I_mtlexq1bQdw8dbkfjUdv9dgb4YVxIhULE_Tw0l0YMQ7jm9AJhy8RFmkch7O1GUEeltWkYVFf2wzqNwKcEPLVD1dk-TJXcUBhCxPos7olgIwyXe-vZS7Av8OdKZZQ9HCKwGrNxvWR3pyG7m66yUw1lbHXcJSwTV2NkEWUUtDjIYNzHa6ckpXfg44D48JBwJlDj3nhYkwUSOZSaAjs5CA7ETI6Z2aLuJQs5j6ayASVuAEnOcUWiZj-aulsFxuQ3mRbVDWnnd6VVVIj8aHeoJTw67QJmT1FmYuxmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=sGABAn0liuMpHMfOW3L3-b2iS4vLcRRRVxnNd8TPLOWbKa-H9I_mtlexq1bQdw8dbkfjUdv9dgb4YVxIhULE_Tw0l0YMQ7jm9AJhy8RFmkch7O1GUEeltWkYVFf2wzqNwKcEPLVD1dk-TJXcUBhCxPos7olgIwyXe-vZS7Av8OdKZZQ9HCKwGrNxvWR3pyG7m66yUw1lbHXcJSwTV2NkEWUUtDjIYNzHa6ckpXfg44D48JBwJlDj3nhYkwUSOZSaAjs5CA7ETI6Z2aLuJQs5j6ayASVuAEnOcUWiZj-aulsFxuQ3mRbVDWnnd6VVVIj8aHeoJTw67QJmT1FmYuxmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=tqs4iZboSzjg7MME8ktJbyN9_G8t3DCWrVg5epEtGX1zyzJTSfGIaxU5JiJ6X8BRH6yKTzOI2YhIlEiccmEG0kxEouHxVFKwxe3YKHh5fTOFv3IZ8fh5RmkMy1skdaFSUkOs64iC04uTlgatC9HpLFUj6sUZvtLyeSrPqm3z_OnpbQbr_Nv5DvPOcXKrMl99NqRmF2IJoigLhTNAYLDT3der6FA0mGzpxo7kn3NIicEV1HepgYM7DR3NcKvxQDDrukDYVY9YpVnCEywiuEM6hzNh_XteOiVDZIOK-GnSEhtisWIMuefIhfc-sIoe27akrJpYT2GqUtZDlUXb4u0JHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=tqs4iZboSzjg7MME8ktJbyN9_G8t3DCWrVg5epEtGX1zyzJTSfGIaxU5JiJ6X8BRH6yKTzOI2YhIlEiccmEG0kxEouHxVFKwxe3YKHh5fTOFv3IZ8fh5RmkMy1skdaFSUkOs64iC04uTlgatC9HpLFUj6sUZvtLyeSrPqm3z_OnpbQbr_Nv5DvPOcXKrMl99NqRmF2IJoigLhTNAYLDT3der6FA0mGzpxo7kn3NIicEV1HepgYM7DR3NcKvxQDDrukDYVY9YpVnCEywiuEM6hzNh_XteOiVDZIOK-GnSEhtisWIMuefIhfc-sIoe27akrJpYT2GqUtZDlUXb4u0JHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=XgGipyb93Bh5LzUtt0jlK6VkV629E3tcwFBgtVa73GuqSm-0gjK1SUgIwyR064ISIRBV_ulWD0AulC6pygZzJMO3QbITuO1XeL3TyYH2SKSm2v3EAlF0Jk4HkjUgtTCZTLucwiCFUyFvRdlOGS_Osbe-H6ZMrA6KXtbJGh8ssKKyavUoRvONIi8wmpNLA5tkt3oXdpI01YIxGcyfuQM_Q0jKmiNBx-l_5YM7G6v_efxAySiLyqsOZSI4wv6WQ9wElyKWwlEVgLLifSN4oAaeMKlPx0whKWrU3V_EPGmImx5-cnKRh-8hUJkQ28G74ypkJmGiuM6HjMfNFT4Ah-MnUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=XgGipyb93Bh5LzUtt0jlK6VkV629E3tcwFBgtVa73GuqSm-0gjK1SUgIwyR064ISIRBV_ulWD0AulC6pygZzJMO3QbITuO1XeL3TyYH2SKSm2v3EAlF0Jk4HkjUgtTCZTLucwiCFUyFvRdlOGS_Osbe-H6ZMrA6KXtbJGh8ssKKyavUoRvONIi8wmpNLA5tkt3oXdpI01YIxGcyfuQM_Q0jKmiNBx-l_5YM7G6v_efxAySiLyqsOZSI4wv6WQ9wElyKWwlEVgLLifSN4oAaeMKlPx0whKWrU3V_EPGmImx5-cnKRh-8hUJkQ28G74ypkJmGiuM6HjMfNFT4Ah-MnUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=lkCTn8m4PlmaqkMYljHPg6GP6cABDEByrgbnGR9FULRyLc1YWws8wcZPGjghNNy1IYP_tOBgFM-_gWOItQTaRnwxvpkqimdDWhSNoGPdweslLeBqrN7XOG8sKCzKJ06e2DcYvkykry3ypSwm1_SyCwxQ5bUnpzya3sLe4y85SPMWmcKmdg_kojzLYWhbIqD4GoLnQU0vQj-TM4OlHQCmyumDfjTUUWhpdS18fxC2byTeYTEAMAQHystgrZw0QudMfr1MEPlEIuF-S-oh4AJuS2lMxiocvF4QHo9j2qgsW5yiyI9965NtD-NIUiOY7INtBFMtUbveHJ39pXjyOKto6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=lkCTn8m4PlmaqkMYljHPg6GP6cABDEByrgbnGR9FULRyLc1YWws8wcZPGjghNNy1IYP_tOBgFM-_gWOItQTaRnwxvpkqimdDWhSNoGPdweslLeBqrN7XOG8sKCzKJ06e2DcYvkykry3ypSwm1_SyCwxQ5bUnpzya3sLe4y85SPMWmcKmdg_kojzLYWhbIqD4GoLnQU0vQj-TM4OlHQCmyumDfjTUUWhpdS18fxC2byTeYTEAMAQHystgrZw0QudMfr1MEPlEIuF-S-oh4AJuS2lMxiocvF4QHo9j2qgsW5yiyI9965NtD-NIUiOY7INtBFMtUbveHJ39pXjyOKto6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8Kk66S5rlM3qZ-3nKmboyxSJ4Y8NBRq5pcwyK2FaNx1oasWfL6bJ_JpBfKFTCe2WQATfMt4s1QQmVCCOyIgC8T0tF1B7S41Ni8n26VjkSqLOSdZekenxSEhlwoOEtmGO-EwoxTlK7niIxp384pTu-WGy6lS8Qr1yL_O4vU-TvZ2hwFBOxlYebTNUGJBaszGWuN7jSXhYfI3GNwhxVC7qa0fYchKt85DUUYn-_s7wAnyjZ3QZnL3vjpOMK3_oh7bKube2vOdqX-bE80S_nvOb7985J_2WhT7f9Hi9FkH15hjRKYsi1jU3n3C7iTxFxld0_MomQSfzzNXTHDV0KjVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHBkyR-nnX_nAcTctUWjUaymjFoLodb6z9flE0Coa7PRgNTTvk6fZh-JzbgLthMrzQyHwAvMoIAlC7skC5WIA_8ysvw1lkvxbu6sDq06Vqt0XRNykP0b2aPZQ12fMT1jO1gdtfCEvVHyBDVAVQO2BxrH_q1sFr43EQetRMheX2tDALZ5_OYBjCiw76HuHUWFla7H7uHJosgYo5whp8GTcIFWGtNHeT11zfuM3Yq0tOrAaz59RzZVYXblqlXdtYy6iFtbkmUiSnwsSjDqZ0TPi2X7vVb8M80TRqJmp1_DTV40ECuwAhkNAzRvhm0dxwe9sDSVl8EBoUagWHIodP2Uag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAmeOSrF0Y32PJ-VrPVJC8CJMfpSfz1byUEVAVhoeLQwY_BKnrvaIwtBATCW2QCLEQK85mdgt_th0lAP5qXa5AmU0z64IwfN0QJ7pUqu13I0vRnCBeOJ2MGirPk8-VNABo3WIyh7J0G-mvuUksyIRUjD-_txGTAvt5me6B9h4V8Phyi_mZFJ04X0P-SUzdmHBN6x93c8gPZM9LpbKa7HeUnEPKt4NuWQOYcrlMYCEC557Ub-d4kEGV4JEQQjDI3gEcC22yj4HqZSM2afKuXTt2Ds9COg6ykNgKScnXHvod_6wU0cgSqiOcUKyJBdfCHhEanTbCRF1-XcsA0yL2pQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7UistQr8fbW28jrK4qK1Bf_8jDyxA1da1k16dchkGGWrvG5U5_ZzjMe_CalkrVpgWBdMyHYJE2WSWyVnsjxdYUWp8dgqLgnh-L8eIIG65w7UCS7UAD0wd_a2iTLf10LajoecgjaYFGLMNqSSmg-8a7h5wkxBag10RdzTgrOq_k8j7HUDeoGhxGRSmvvc4dkclV0vxpmRFgutU0oic7WiQuRjO2Xs3xBAOSEVqvoY65NC27-YA4qnEXbKkJotlG6CktCLw4NVD_RP2MRJmgKlQlby7RulrgqU6lgZk2u7lozOWwP2FBFE9jw6HGlWg3AVvD3HVAHIu4wSLKVU9_aVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM7tWxbmcnd36TtJ-mDv8HpS8r8xwt40LBVcXVBHk5JJFwOP3cy3STgJETWSu6GEeyPchfI9RZgD4EjFGjH8jGBJVHzrHUmDVcFFIsBNv3GrlX8Q3xRAjGBhzsc5mmastKnUu4vQu6LmGqZOYGdiweyB4luvd6rBVBYLt6tz8L-iQfichRwuK0q8JLbPLg1xGUTo4kMGG5_m2jF779NRATo1ZqrOb-VvbxMBQQMtPicHT-5wsmFXDFJOBtCcIMzR_CO89QbQSArWYNVlJX8T04PVXqozJPVhXU3chrheCnd2YGVsNXk9fmtiviHJNx1V6HDU_6rXa2KOhL22Aoezcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=ZAsSY3Di2xLhNWi2hSiX_F6ZClbh2rdqaFUJ4ADIxuo6yu9jn-aMcpOpIcOaQ1Tt3ss8GyusNwdEBDg6QpZkPk9I1kQj5mVklG1KaBuyrPCgJeU_UOJHttXqRnCMwQdWE88Djbiw1-6epMExAHshN7Dqu53tV9pQEvCS48MwICe9NJ1VySvEOe8U8Pr8IqVf4IM2zhg1b3Kaj9sLjuTKKo4dKpX0kHpL45wHl_HSSHDvLrRmp2lmYgjRyBgRr8Xx_2RnB-X3JDyZU9XWDnQ07ctaY5dmMElCd7cwSwD9cbkWCRM6MGjcIN0_oDcxO-dlrqc7_RL5o3oxS2dxEMD3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=ZAsSY3Di2xLhNWi2hSiX_F6ZClbh2rdqaFUJ4ADIxuo6yu9jn-aMcpOpIcOaQ1Tt3ss8GyusNwdEBDg6QpZkPk9I1kQj5mVklG1KaBuyrPCgJeU_UOJHttXqRnCMwQdWE88Djbiw1-6epMExAHshN7Dqu53tV9pQEvCS48MwICe9NJ1VySvEOe8U8Pr8IqVf4IM2zhg1b3Kaj9sLjuTKKo4dKpX0kHpL45wHl_HSSHDvLrRmp2lmYgjRyBgRr8Xx_2RnB-X3JDyZU9XWDnQ07ctaY5dmMElCd7cwSwD9cbkWCRM6MGjcIN0_oDcxO-dlrqc7_RL5o3oxS2dxEMD3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJfC5PCsRWlIlZRBucSbYv7HutrcWlIJKZW_Sx3L7yDqJou0MrU_pqwPrM6qQyYGv-UE9_7Y0j-vKaLNFtfH1stEv-JayXDsFrxPtPPiVU6s-BPojHznoAVbnSK2EvsBU7YhPlC-cnq0gGekdSPhLJoLLhlN23ahjWhCn9On8loReY_aBGpwNXBIujqdfKFRc4oLLiUXe6BKx7HxMhDhXioGqBy63jjCM8jbKlCFm0fKh5hGls3Xu5KPvAuWxu-vs5VNoBAbKTPOnGj6fu2dllaRjheMVd4L1SKrBLM9SPA5SNvpzli8TTjNGFu0lUJl_Y7UbkRC69C9H3b2kjStKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiDhTNASRROz1W4ws_v0TEA5ApbPw3GcfnWUHmQrUrqD-ewn-BizmdoC8R-hx2N-UNv9WSDJmzQlv7wA2eWHxpO-VFUPugfOqQnEg1k2jCHugqYua0qleqfY4n_KeKesrsSXvstpTtVNEi0gIU_tdHsUXsKvFfF_tCOpUVFgik8Z4IVfHdp12cEe_BzmyTi3CVEj8pVdGHDNr4uyQQ3osfbahogbp5GCJ9iV1Ud3nb8gr9DvVwEfqe7g6i5nSXNsuT52WLlL2R1XgLYqv5sD_pK7s4YhvuMRHekUa_EEVQg0MPRVLlYnLHTgfMtrzSZGNLRsKgAFip65T6lE1A41AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=BfWDVad6FcHZpmlCkyGss5REQXDmeTRjz0XhI46DsDTgF_QG0biMNes_GIImwArOB9UlA7WM6kOdVyiIW4OUj4iKVUhWs2cvqfd7CVkwf_VHqFmatAAh8Iv1G8h4EbpkxGyPdqwbeTdXKWWD7LXptKkXaSjJpDR0Uop1WXu_Hz6Kqtjt_LvdsL9cqIaMVcx25KVf_BxgXLE2WHXnZuMQhRemwL_MLAjvtn2Akdq-i8qDxdE358jypdke0DHR0UxMQe8xkIn9miFIOlZAwQN7g5-F7Ngl9hbw7LNR9W9WqTxD-UoX5buQ2teYmTSoYWhJ6b7J2QR0RX0UtA_Gtz7-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=BfWDVad6FcHZpmlCkyGss5REQXDmeTRjz0XhI46DsDTgF_QG0biMNes_GIImwArOB9UlA7WM6kOdVyiIW4OUj4iKVUhWs2cvqfd7CVkwf_VHqFmatAAh8Iv1G8h4EbpkxGyPdqwbeTdXKWWD7LXptKkXaSjJpDR0Uop1WXu_Hz6Kqtjt_LvdsL9cqIaMVcx25KVf_BxgXLE2WHXnZuMQhRemwL_MLAjvtn2Akdq-i8qDxdE358jypdke0DHR0UxMQe8xkIn9miFIOlZAwQN7g5-F7Ngl9hbw7LNR9W9WqTxD-UoX5buQ2teYmTSoYWhJ6b7J2QR0RX0UtA_Gtz7-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=uZ6XgN1UXkcmfUskTj8yYe30NVo1Sv1I_jI22CEu_xeKNHTgkuGV89bwI6B_804KEv3aFqEhvylJ3-DEiCIsMBTNsaBroSXKKC3dnDmmlSOD4kE9PMK0m109oB-zd1-58qANnS9DuY4zOhCcv2G8dliaGyPflpylCs6Jkj9YsA2Wco5_FVa4rSGkuVeVhVPHx1NhYTjgSjF7W3hvwt71D2RyXAFTgFHr3mXlE7JYYzYURhaO6hl8x-QjF6QcJ556yYELZXIcdcZNP4p15UWLh01AA_sVptLyvZARZ6Gw5CHomiRG-ktY3H7ZD_CW3XmqJ-cMEoBYiSMdnuAko6SJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=uZ6XgN1UXkcmfUskTj8yYe30NVo1Sv1I_jI22CEu_xeKNHTgkuGV89bwI6B_804KEv3aFqEhvylJ3-DEiCIsMBTNsaBroSXKKC3dnDmmlSOD4kE9PMK0m109oB-zd1-58qANnS9DuY4zOhCcv2G8dliaGyPflpylCs6Jkj9YsA2Wco5_FVa4rSGkuVeVhVPHx1NhYTjgSjF7W3hvwt71D2RyXAFTgFHr3mXlE7JYYzYURhaO6hl8x-QjF6QcJ556yYELZXIcdcZNP4p15UWLh01AA_sVptLyvZARZ6Gw5CHomiRG-ktY3H7ZD_CW3XmqJ-cMEoBYiSMdnuAko6SJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=l-UNsxTsIh5sm7b9CqnUr3K92gvGurS-wy4uSEHUGKROlC-h-ZTwNbeMpCaGWeTBTlqxoi3B13nB0jTZnwjvMkf9bhCjSJKHyujF9UyvqIIa_oPyEqloh_kFs7LwKq0MKcPxKHyhztTd1_-1rRfkUDlYrm2v8PcS9_4cOIppYm2LMqh-e2v60LkVJiyPl1NfmsOlktpMC1ONLdiY8UKkbRgJiZFLSVdE39lIKjj6suqS9aQz_fokwbUqjGZiU5L2vnupeuNOAUIz5x1232xTk9nvPfxSM7BouSgHDdEdOIM2AWDko3xjWtfruwjkpp3fN2RHpVNpCa3rSTmQ0UCOmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=l-UNsxTsIh5sm7b9CqnUr3K92gvGurS-wy4uSEHUGKROlC-h-ZTwNbeMpCaGWeTBTlqxoi3B13nB0jTZnwjvMkf9bhCjSJKHyujF9UyvqIIa_oPyEqloh_kFs7LwKq0MKcPxKHyhztTd1_-1rRfkUDlYrm2v8PcS9_4cOIppYm2LMqh-e2v60LkVJiyPl1NfmsOlktpMC1ONLdiY8UKkbRgJiZFLSVdE39lIKjj6suqS9aQz_fokwbUqjGZiU5L2vnupeuNOAUIz5x1232xTk9nvPfxSM7BouSgHDdEdOIM2AWDko3xjWtfruwjkpp3fN2RHpVNpCa3rSTmQ0UCOmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=FDBQ21YVT1L3zHrLb1ipebbrfk7fy3qaL2WjeqBM4Om8LbMdRwBKcRBCskQch5PClRCVAj35L60CoOJibxwNBnBEGP_3OrXgSPrPrKBz0mkwXvLMV2az-FG8gzjbkSSulWCks1kuZ3a_gbVtsnFZdRV0jqdMay9PHp-YwggglDmcowm5HyTpBSKCrTnTHgY7LtNrgOEG0XWSsvOUXFdmtVmtAAMEKynW-rwVUqHVJWJ0T_okeQ0yPp1yauAUTBvxIBsQ1VWwYoA3QC1Ag1TWDYQwsWioLcWhJtwESf4ylDUZrAsb6Mof5di32-VjhuL782zznqcimS7RjCz2ER8EAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=FDBQ21YVT1L3zHrLb1ipebbrfk7fy3qaL2WjeqBM4Om8LbMdRwBKcRBCskQch5PClRCVAj35L60CoOJibxwNBnBEGP_3OrXgSPrPrKBz0mkwXvLMV2az-FG8gzjbkSSulWCks1kuZ3a_gbVtsnFZdRV0jqdMay9PHp-YwggglDmcowm5HyTpBSKCrTnTHgY7LtNrgOEG0XWSsvOUXFdmtVmtAAMEKynW-rwVUqHVJWJ0T_okeQ0yPp1yauAUTBvxIBsQ1VWwYoA3QC1Ag1TWDYQwsWioLcWhJtwESf4ylDUZrAsb6Mof5di32-VjhuL782zznqcimS7RjCz2ER8EAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=TaT4J9rSz_hQlRPyYN4C7bfdct0ppRocCPQVePpHYzN2rNmAw83vbaojzlXnl8Be-pvfu4DXi00jzFFEAjly--H8qrthVxNbXYcKzsgYKYSC8hQ6w7fZZtNhb5l4X5ZtaTezEKrtzyfoGmkGxjw89H2GY8obx1SDqmQgHkW3HNZrYEmOXInnU-cF9PFhKOq83-_rSgcNZ0Ma7X1WFJEKZZwtOcvsBemumnpHN1aTasaTr-InSCjjgO1cDcEK7lKdnal-OFgEFV_E18bToq-Y38IBuTH3Rphzd5b5Cnc9WDzLqRpvOrxCM2-Hzkcd6lCiiWvrOjTZoXeDcHYPjPGNiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=TaT4J9rSz_hQlRPyYN4C7bfdct0ppRocCPQVePpHYzN2rNmAw83vbaojzlXnl8Be-pvfu4DXi00jzFFEAjly--H8qrthVxNbXYcKzsgYKYSC8hQ6w7fZZtNhb5l4X5ZtaTezEKrtzyfoGmkGxjw89H2GY8obx1SDqmQgHkW3HNZrYEmOXInnU-cF9PFhKOq83-_rSgcNZ0Ma7X1WFJEKZZwtOcvsBemumnpHN1aTasaTr-InSCjjgO1cDcEK7lKdnal-OFgEFV_E18bToq-Y38IBuTH3Rphzd5b5Cnc9WDzLqRpvOrxCM2-Hzkcd6lCiiWvrOjTZoXeDcHYPjPGNiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhBF7i0PumFnsLFJHnkqLIi4pKGIGVq1dut0V1X9v11g_FsUxv4BJjJgijZZloYzDm6O9aCgJ9jh83NRtHsamqLzeozhSpeDg9MUXTjvoL8bjY_3oSkt1D73NGmszGB1yGiE1hV_A8H9GCs6hgqrUbe9oMrHAk0PfIJ0ZDy-YsI3dlemMe-7tKpImPfB2YZ8q2_sBb27Y6UecVk2XafPavvq8lHhUK5kkNTX_6E5g-9ov48zd1IgMMCsCKmcu0tnZwUuMDmbGqh7eX0g-ftrf1F_H-g2PlWlUX7wFFJB90tJIIRtBTPzuhmVu6pz19AA7wdjcEJcC6F7D-xgVZn1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPRm5mtplIx1-JYKzhqiMynWYlU0mX6Pq1wesZhyb73bKTcPxPiBX-9W1UPKO_7PVCKJTVx2cBky-vY7qF9S1kkh319dO8nWrGVohNyZ2oXmB5yGXsrLSJsLUU6XUDbb7EnxAAmLxR7kVywW1QMeJ7zziAIHYUT6ZEbgLYeC40hVbxPnaeBNB7J4Eruz2AQwWVcz3VZJcinN7noUUpkJsVh1l7S6plKiMnXLUyn1DEHb2bb6W0A7BuPYeJOvTOHmM1q7sJgI18YX8TMHAoYqMJ1msKwm3fpeWdrS1oo2oGONif5x4ryS1rrl9_M0U76HshSRc1Wv0NA6dXKRbkSB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D-WpiVBEJk7R8DEPX_WiCZAYwQiXUU1at5U4gdJ8waSum1GmOUk_9vGLLKEdq-q7GfxpaepbzK5atQjraK5LUy9wBIw7X2TUkklHyjUmEwM2jlDmSQ960cjcymSb_KEiaOZ4pjfb1TXQNspHDc715BvVLHJZm58ralWIz_kEeyATlPsnZrbHRi4kDHX9SRr17WhOoy-i7_-Ug4Ql1Hi52Pg5DyXU1kCFbIEr5akncov0sHjMEKOr770akDE6T7iX6ZB_tb7Yf-n6YjVJkhCMvjoH_bIBhy0tIoegUvA8JvZPH6LCMNduZe8ejnBpvMJ5KZVk6OYTKnyQI3ZT_zTTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=qd8rkZRQTwBpZY7LVdtsRl4CFX9hH18kCFGCCWsTlOblBHZQZDB8zh0FCVtrOq6x57UmKoJ0-491JyF8vFa4ksbRpxWqCtLuuvEYRjFx1XN-LV4edlM-TiVNWuay8HrR7PdsjQO8cpfACqdod7s9mXNhW8Ncay7l6I3RwEhu8diBGWlIhLmIjabzgIr4lbs_LghazvLeCudVitQtOMZFXDsj8LxUzCP9fyMCJplstryWd4kp6RtJMQDQ6SJDCwyCiTNsdXM8Ce2U27t2n6V__2fhViIGGe05DIsbl256wpt3zqelZOC0vYkGw9NaZ_H_q992UsVDPLcfjOb8a63Kdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=qd8rkZRQTwBpZY7LVdtsRl4CFX9hH18kCFGCCWsTlOblBHZQZDB8zh0FCVtrOq6x57UmKoJ0-491JyF8vFa4ksbRpxWqCtLuuvEYRjFx1XN-LV4edlM-TiVNWuay8HrR7PdsjQO8cpfACqdod7s9mXNhW8Ncay7l6I3RwEhu8diBGWlIhLmIjabzgIr4lbs_LghazvLeCudVitQtOMZFXDsj8LxUzCP9fyMCJplstryWd4kp6RtJMQDQ6SJDCwyCiTNsdXM8Ce2U27t2n6V__2fhViIGGe05DIsbl256wpt3zqelZOC0vYkGw9NaZ_H_q992UsVDPLcfjOb8a63Kdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGSw4H9DLQeLQhKDE6fsHvezR0ufTCKJOGFiuFRtslu9QVd23XW7YXta3_bGOc1xN1TE0yXJULZaH9oBoncO5UO2vOg-PPZMSmbz0kGVradRdA62v5EQYnPqdi9AKp7DxMaoFB8bneeCxqJKH-kv-g4wLRqqZQxlWNyvn_g_mFNxP0Juda6QQ_9FP0U3GxR8Odm_XCQLPBhDEbpr4ykjhtIElGGWGFyYJ7ISThuAVdamXfXojSYuP2TsocYmXpCwtw6mIFB0CBrv37R9GIJvkYhIEZOoL2CetG6iCfjixX1VgdJAMd9zPZDYBT-7yiJX9pCmaEB-H7UzpsCNkRTJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=I-2As6CZdfITj2V7MITxjaaTTkMeSS-xsHdr8oDp-VpNSg8COIRJ70-mGKgNLUJLvzm7wxsN9K8alFUhEWWxiX6T0lOKqHmwPPzbzMy2MOndtBaO_DLDNAK8WJ6t92w6OcDSqOaG_tsQhMGi_p0Q1piSkkx3H110aUW5yv9a2LelKQ5O7PgvpauXJCMZUn3wCIahxwQ5a_tH5M4svLx_cpucdwA_OkiCYt0uU06KdtHNReMC99pgPzAFmQAo_cdV0ZLKy6fAmy4C5ZTE578KPWzVzmQE_YajPrchQxf7_7hPNvjDyp9KAGx0T6D9Z0EvOHT7zHSpYJscj594Ha_Fxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=I-2As6CZdfITj2V7MITxjaaTTkMeSS-xsHdr8oDp-VpNSg8COIRJ70-mGKgNLUJLvzm7wxsN9K8alFUhEWWxiX6T0lOKqHmwPPzbzMy2MOndtBaO_DLDNAK8WJ6t92w6OcDSqOaG_tsQhMGi_p0Q1piSkkx3H110aUW5yv9a2LelKQ5O7PgvpauXJCMZUn3wCIahxwQ5a_tH5M4svLx_cpucdwA_OkiCYt0uU06KdtHNReMC99pgPzAFmQAo_cdV0ZLKy6fAmy4C5ZTE578KPWzVzmQE_YajPrchQxf7_7hPNvjDyp9KAGx0T6D9Z0EvOHT7zHSpYJscj594Ha_Fxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=kJMzfXjIhRjs5N5SxJ9wce50FxtL9a-siAb_E2etcKdhyJ9SH5W_OvpqsCOzYLZjzvsKjoTl30YM4NG09mHoRcY-U9yZD1W7GCoG-InZuQtkUrAq43Pbig1ljlyMwHg1uiEnTR4ZjmiZy1veCASYK2pR1jCk8m_LPYK7PgpnOPgAH9OzF5GGx8FIKKy1AtuMR7KG_drQXO92t2E9gsBT-uXucWqoC9L6S7ngiLoi7puXIgCrd98NnVIXvGiNW84Etr-NRY1JmxbLwlp4QjL6H3PmqGWC-RguoY5YGK9R4qioMmeepMldGK7mFjZ6QYIaRG8KcB4S6s83aKQKadKRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=kJMzfXjIhRjs5N5SxJ9wce50FxtL9a-siAb_E2etcKdhyJ9SH5W_OvpqsCOzYLZjzvsKjoTl30YM4NG09mHoRcY-U9yZD1W7GCoG-InZuQtkUrAq43Pbig1ljlyMwHg1uiEnTR4ZjmiZy1veCASYK2pR1jCk8m_LPYK7PgpnOPgAH9OzF5GGx8FIKKy1AtuMR7KG_drQXO92t2E9gsBT-uXucWqoC9L6S7ngiLoi7puXIgCrd98NnVIXvGiNW84Etr-NRY1JmxbLwlp4QjL6H3PmqGWC-RguoY5YGK9R4qioMmeepMldGK7mFjZ6QYIaRG8KcB4S6s83aKQKadKRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=hY28E6Kz2ba8ZIPFH_Uj-SdscmFjd1jh-Ax55xCD0nItnvnOIjGu4JX5VyG3URaIptUPbr71GVvc83wLsL8JuMPDdL0GCR8NaVJnh62G4NnjV5a_6yvC3NbcpSdppKYPOtrqnPcAFGqyzET9_rc0vvykBKp49wNBQNDEHJt2sMoyXnAKDXkodizYVL2fVwHRmF24bVcr1SMZpApqZSTuaOMclNNPiuQf64Ph3I-efdenkxZ7dv2Pznu-Y-ZH2aaUzhDJDRUomEvGYuEmQ17pfcET2vostc1L7r4jtfHDgfGk4CaENsOmFWmP4blqmOLeMArySW_7vj2Qr9RyWK4iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=hY28E6Kz2ba8ZIPFH_Uj-SdscmFjd1jh-Ax55xCD0nItnvnOIjGu4JX5VyG3URaIptUPbr71GVvc83wLsL8JuMPDdL0GCR8NaVJnh62G4NnjV5a_6yvC3NbcpSdppKYPOtrqnPcAFGqyzET9_rc0vvykBKp49wNBQNDEHJt2sMoyXnAKDXkodizYVL2fVwHRmF24bVcr1SMZpApqZSTuaOMclNNPiuQf64Ph3I-efdenkxZ7dv2Pznu-Y-ZH2aaUzhDJDRUomEvGYuEmQ17pfcET2vostc1L7r4jtfHDgfGk4CaENsOmFWmP4blqmOLeMArySW_7vj2Qr9RyWK4iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=Gfy7qEqfRtnPuRwt6S_-gAIbfxifp64hRsmmJxBjK98f9-dJRtUQvmDhOeW4M80WgUNOp1bNhr80mjyNPHOLx7jCVPhaHvlKsprN_SUh11su-QitsDUesvmP_O4PFSRHX0XOL3f8mo0FH69zxYcU35eXTvqSWvdo61h5DPT6uWEws_TTwUfEP5jlu_iW7aNM7p1wCiHKjWs4I5uKodmYT7n6JF5utPxbfUUk1dXgTNuUYT7vOv8NkSD-FiVg5XgAUgOD0-D75CQdEukccV8BBtg2VPnMu_ayughBnOwwDUELxG-ajf9TuuPumPM8bk9PACtxOmtkX8kK6rkdI1yhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=Gfy7qEqfRtnPuRwt6S_-gAIbfxifp64hRsmmJxBjK98f9-dJRtUQvmDhOeW4M80WgUNOp1bNhr80mjyNPHOLx7jCVPhaHvlKsprN_SUh11su-QitsDUesvmP_O4PFSRHX0XOL3f8mo0FH69zxYcU35eXTvqSWvdo61h5DPT6uWEws_TTwUfEP5jlu_iW7aNM7p1wCiHKjWs4I5uKodmYT7n6JF5utPxbfUUk1dXgTNuUYT7vOv8NkSD-FiVg5XgAUgOD0-D75CQdEukccV8BBtg2VPnMu_ayughBnOwwDUELxG-ajf9TuuPumPM8bk9PACtxOmtkX8kK6rkdI1yhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=kMhLIROb9piFtr6FHDpnv8uwHulx3BppRcECe1w3QZRIenJ5j6h50Z2AYHbIhCoIcXhuwzXo05SXfuU-Cy-LOOEA91JOub0ktRdwxAebT7sIiufy0k_0rHfV2CxZUoT6cK2SYe31fu2870bMt_Qc9UVu8Zg-WXIvmmjeChJBN3PTzYS6quOZW7owvKGEvvRlYv5khvJmBtKv1y1dQlDgNy09k5nDl0xpkrtVUwiyX-Bu9e-pMV9lDj3GZDIFc2dKzXztynYFAQugtr2PLS3gY20LK-8MeDanIFE5mFejAa23VI7YAse912V6LMZckr5dVsybQ7fftagUf874sRxU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=kMhLIROb9piFtr6FHDpnv8uwHulx3BppRcECe1w3QZRIenJ5j6h50Z2AYHbIhCoIcXhuwzXo05SXfuU-Cy-LOOEA91JOub0ktRdwxAebT7sIiufy0k_0rHfV2CxZUoT6cK2SYe31fu2870bMt_Qc9UVu8Zg-WXIvmmjeChJBN3PTzYS6quOZW7owvKGEvvRlYv5khvJmBtKv1y1dQlDgNy09k5nDl0xpkrtVUwiyX-Bu9e-pMV9lDj3GZDIFc2dKzXztynYFAQugtr2PLS3gY20LK-8MeDanIFE5mFejAa23VI7YAse912V6LMZckr5dVsybQ7fftagUf874sRxU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xwu5GKsPRlgA9V6dsyeCosFgoWFhEr-7-pcoz87GHqiDw5feS9qxn8sLw-YzUO8e7yXmUC9rutMH9vhzdOSyZHa4veR3rgKFY6uWl1hW58Ugzc8LhIcFjYnXyP4ge_DNnSind64LAnV_jjRO2dMWZ6ckkiFDs8lUURqPe466i4-GrRxQhO-90WQVM9SZx-i-PWdONJR38Pe7-OyX18jKU3r8B1Q_QQ6jVzltl6kMrtXekVACXcph34Ee_x6y-uMebr6HSERgf8Y-kHzaVCWdpOwNzTujgLvvy-h--pCiBThQe0atcQZuH3H2LrjHDx-ak8gYT4A0a-X3jB2XJk8tMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY2hCsFZotWuWzYwHXSfwlsgYt2rZBOg7dHlvDwtPqzkkvRuQtRAGzRNwQZOUc0uiJWn8eXfjf7kv4LKAneOsGwS_XAoTFH_v5K7LwgATC3pSZ4H_glnzRzOsiSn3F35RiZwGjWThoLdxRJQJ4vbH1SnQU_5pfZbMMOsbdEUMZt6t83K5tUPpnHvyZm89MPLXhX41p-oy7cHdnX8WGE9CuP7Hyvb8ZlcLQJOlfd8RSaQpWRzZ_S0VlMt2kGPqjGJ-VJYXCSFb9X7wwUWcqz5ML-2mFuAMGVwkmCGtFm00hooLgWgWQXXCvlmJAFV3CU66PF815aKJqxvpn0na5lu17-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY2hCsFZotWuWzYwHXSfwlsgYt2rZBOg7dHlvDwtPqzkkvRuQtRAGzRNwQZOUc0uiJWn8eXfjf7kv4LKAneOsGwS_XAoTFH_v5K7LwgATC3pSZ4H_glnzRzOsiSn3F35RiZwGjWThoLdxRJQJ4vbH1SnQU_5pfZbMMOsbdEUMZt6t83K5tUPpnHvyZm89MPLXhX41p-oy7cHdnX8WGE9CuP7Hyvb8ZlcLQJOlfd8RSaQpWRzZ_S0VlMt2kGPqjGJ-VJYXCSFb9X7wwUWcqz5ML-2mFuAMGVwkmCGtFm00hooLgWgWQXXCvlmJAFV3CU66PF815aKJqxvpn0na5lu17-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=L9sggPsNYTUg2Owr9JIg5ukT-kEHql5XKDHfr7B8vSWVm2xfbG-LBap2jDq5oc9oUAxOpVHfPATbTQJXekxnTPr_2NipQ0WlMTsftLOH5SUJmXqQ0TsrlazuhcX-zXv7GPm1uDXL3HRv-iqW9JVoUTSsZqo1QgY3eLNVY9mqynB1KJaibUFRn60lsTYyB_3kCUd53k4WsGWPxefDmUFzxYlGKKAcdkfZp0xwhnSgfqtrcwVy5TKqQ8LiPHjWZqnAukATPYuDlPPgwAxfSU0P77hhnVpABXGOHcZENnoi7zydG-s_uzLxVetDNfNYWionTqEBEOpopsEF4FnIF49jZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=L9sggPsNYTUg2Owr9JIg5ukT-kEHql5XKDHfr7B8vSWVm2xfbG-LBap2jDq5oc9oUAxOpVHfPATbTQJXekxnTPr_2NipQ0WlMTsftLOH5SUJmXqQ0TsrlazuhcX-zXv7GPm1uDXL3HRv-iqW9JVoUTSsZqo1QgY3eLNVY9mqynB1KJaibUFRn60lsTYyB_3kCUd53k4WsGWPxefDmUFzxYlGKKAcdkfZp0xwhnSgfqtrcwVy5TKqQ8LiPHjWZqnAukATPYuDlPPgwAxfSU0P77hhnVpABXGOHcZENnoi7zydG-s_uzLxVetDNfNYWionTqEBEOpopsEF4FnIF49jZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=cUPqhC7EdyDrjB9VkbkykSewmFm-6CDaEdxkWmpdiocy3cajTDVwYs1rxm-eLSNALWembRM5Q432janY_ymCfXMbibDzDHBa3Nhx1dIxv6QpSieX3cuhNxMukTEY45QHR3CLAqoIOODkzvuV7mUDlXFA6_OpidZzfXZOcucxQUw9v8VaZvtCpKfrIgvgU7Xv7QJQMgjVRmNrwLxKhaCh5wA_WiPJFxLemIbK7okegmYJfpfKxpGU6r5AyjMZ1l2SkBbqZ3wBYdAxf3cP3kpETb3A4M8orH6emNLwVXy7KbiuCebkvc1Gqqv1b5q2ot00j3xzdfbo3f9Lwp-SM0Sys0lcT68Qpp5sSxRhrTh0cBxHQh0OcHcPB2RWRIxXwmmi9nANbd5YEokCqVHu98YI59_pPd7DwJYy8TP9DNrm1HWcefczOwXXHSsBe3_56EwDxF7GStQg6PYvWeW9L8LgYN1q0T5eK2UXixkkvBnbChO9dEqJo3bfwgRzMAk7tw6YN-TjZpxPtO_LmDx_XPPIO9OxfJf8Ky9NXaVmVLfDyuZRcHz2SDmx2BnhbCCE3yGDPz_dHl9SQCpU-7oE6io2Kb493mvn7_deAQIVyzTZvqn8hFjYW288u0ySaM5eQGpJ8zHRyUSn9wz5gWWH2PiMbAruPQlpfUfYrpjqu5SQlyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=cUPqhC7EdyDrjB9VkbkykSewmFm-6CDaEdxkWmpdiocy3cajTDVwYs1rxm-eLSNALWembRM5Q432janY_ymCfXMbibDzDHBa3Nhx1dIxv6QpSieX3cuhNxMukTEY45QHR3CLAqoIOODkzvuV7mUDlXFA6_OpidZzfXZOcucxQUw9v8VaZvtCpKfrIgvgU7Xv7QJQMgjVRmNrwLxKhaCh5wA_WiPJFxLemIbK7okegmYJfpfKxpGU6r5AyjMZ1l2SkBbqZ3wBYdAxf3cP3kpETb3A4M8orH6emNLwVXy7KbiuCebkvc1Gqqv1b5q2ot00j3xzdfbo3f9Lwp-SM0Sys0lcT68Qpp5sSxRhrTh0cBxHQh0OcHcPB2RWRIxXwmmi9nANbd5YEokCqVHu98YI59_pPd7DwJYy8TP9DNrm1HWcefczOwXXHSsBe3_56EwDxF7GStQg6PYvWeW9L8LgYN1q0T5eK2UXixkkvBnbChO9dEqJo3bfwgRzMAk7tw6YN-TjZpxPtO_LmDx_XPPIO9OxfJf8Ky9NXaVmVLfDyuZRcHz2SDmx2BnhbCCE3yGDPz_dHl9SQCpU-7oE6io2Kb493mvn7_deAQIVyzTZvqn8hFjYW288u0ySaM5eQGpJ8zHRyUSn9wz5gWWH2PiMbAruPQlpfUfYrpjqu5SQlyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=YyFOq6kzhdC50-Juw7bNjh1Ac1xFUJpinhHSC30m4fUP3w7d5ZtGqRaAKs6IAux6pm3D25QbVa1N88S3Xd-CPSAhKuKhbYYBh2Y5YFTNIvqbjKVqFCIJVBQWipdhKQ_gHeN26OyH0bBb-LxTyGydAyEo47_m77IjIZDFM-NR2NOPXNAWA5QzpM477gD2urR4jQchp76KfyCHw5g-G4TlMsUt3Fyostxncf2C5BwhU5SoL8TGpFyq7w2oO-auBYnmcVN1GqbOTHvvhe5xP9wQe5gAf5rIe9qAqNtuI5qbopdYF3sVJFr9Sb80JYNANP8OImmN88kM4G931-8ALXw6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=YyFOq6kzhdC50-Juw7bNjh1Ac1xFUJpinhHSC30m4fUP3w7d5ZtGqRaAKs6IAux6pm3D25QbVa1N88S3Xd-CPSAhKuKhbYYBh2Y5YFTNIvqbjKVqFCIJVBQWipdhKQ_gHeN26OyH0bBb-LxTyGydAyEo47_m77IjIZDFM-NR2NOPXNAWA5QzpM477gD2urR4jQchp76KfyCHw5g-G4TlMsUt3Fyostxncf2C5BwhU5SoL8TGpFyq7w2oO-auBYnmcVN1GqbOTHvvhe5xP9wQe5gAf5rIe9qAqNtuI5qbopdYF3sVJFr9Sb80JYNANP8OImmN88kM4G931-8ALXw6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=GHMwDm5fOjZXaj-V7vhycxTTXdcSXo-DaMRypfEhxv6vdkCnCe5zHotP96c7igMn7_6lnzEmH-fSZbQRfWeh18R4HT7vs5_QfV7vbl_b0BZfB3Ft7ZZCYR4MFXVS_wVCjf5Y8sIzdgDU5ZB6ugjbeGjsS1U3j5ehthDFG7Q1CEBn0EH19I_2F14Po5-soSLXRYYp_fRGSnXRpMYocnGDBOgJXJAwr8hduw_yYz6XkmLL_7cfoRueRkPo0-eXxGwgdFlNS8M0aEzYNZYcwXjFHiBAcyoC-4vPAYnTxbrJJuClqsv85PpTRSKC9QBISF976X6Fc1F3Gcut2D-5ccJvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=GHMwDm5fOjZXaj-V7vhycxTTXdcSXo-DaMRypfEhxv6vdkCnCe5zHotP96c7igMn7_6lnzEmH-fSZbQRfWeh18R4HT7vs5_QfV7vbl_b0BZfB3Ft7ZZCYR4MFXVS_wVCjf5Y8sIzdgDU5ZB6ugjbeGjsS1U3j5ehthDFG7Q1CEBn0EH19I_2F14Po5-soSLXRYYp_fRGSnXRpMYocnGDBOgJXJAwr8hduw_yYz6XkmLL_7cfoRueRkPo0-eXxGwgdFlNS8M0aEzYNZYcwXjFHiBAcyoC-4vPAYnTxbrJJuClqsv85PpTRSKC9QBISF976X6Fc1F3Gcut2D-5ccJvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=AMQl6fb_UTiX-qWXdWeAr4-Kqw1gq-i2sj5761wWGrZJM6y0G-UYFEkfqkZ1SNepXIRSjYiDcWDB9orS9Eo7xye1lxDlQN_md3wUlTm54Ure2Dor2NTspWYBsjlxRE3EoRZp03YxXadGEfeTA1cWTs-0LEGoLzPonpXaNpYUG_aA1poWaHhm5OfaxLwcpEuETApSB2ioEJyDo7dRuIj6AUWz2jHyUyfkeGyzmBK-warYojx89AB8cTO-RdfLoGRqKYiqCRjsXk6R1jOaQ1VeGN6t-4TMhyo76nzLJXo6si15n1-qajsZklvCS_d0xAZYXbKcCGMh3OpFaiOxxQBSNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=AMQl6fb_UTiX-qWXdWeAr4-Kqw1gq-i2sj5761wWGrZJM6y0G-UYFEkfqkZ1SNepXIRSjYiDcWDB9orS9Eo7xye1lxDlQN_md3wUlTm54Ure2Dor2NTspWYBsjlxRE3EoRZp03YxXadGEfeTA1cWTs-0LEGoLzPonpXaNpYUG_aA1poWaHhm5OfaxLwcpEuETApSB2ioEJyDo7dRuIj6AUWz2jHyUyfkeGyzmBK-warYojx89AB8cTO-RdfLoGRqKYiqCRjsXk6R1jOaQ1VeGN6t-4TMhyo76nzLJXo6si15n1-qajsZklvCS_d0xAZYXbKcCGMh3OpFaiOxxQBSNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLGFZmRzQ6KG1hecOjstwnDQ8TJkacw5VByK8eDkf-60ZoGAhYJAnaApQ_sVumdA8vzcqVf91Pc3VlkDtZtcKE1RzVAoWIE_psZKzUWsyD6N_TJHIjGOLe7AmWxKWD9ymE_C7LkMg5hanspkWEre7cTDaxUI-lYjtwe6d7DmU7FTQJo8e9L4isfdX7OvvrZISWmL6Cu7BlxstQCucyBYk1TwfFy6A_UL5eVguYSxOvn6DAa7DKUKOSl2BRF9ciHoxX5x6uT4e0f5DAMX-H_UBH_4YzOBHHqRR-O-Y914t0gG9bcl42jkzBwojYkZoSImIHzswtm6h-ilnYl-TXN3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiS4Ou26yG1C1DARk3XBVExS__uWVdYspEisyWWKC0cmk3bBx_qsH-QhJX1yi1aIZHYmJ7bF-BM6wpoE5ZtY2oAE214243G7CA7-CXlXqHQkm6c28hkCl37f3mqm9lIKy-YPHPz-XGzDaIkARtWP-CjohuY3XsBiwt_B2wPyrJtwK97L3wYFzpxso7YBj7VPbB1eK1ec7Yud9W7XgviNkKwPD0tGc-VUT2UTa_bYf5B5XLYjf1Bythw2wZWiiVEwxUegDVLWOIrRMEJWlSc027rLaeTujSvDh03EhG_QWEKgiaX9fSvGkCVy86CSlzGn7-k_vikLIg_-YzrIjK0GuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQlsOiKrSU0y04YxcM3ll9fSD6PQyfSPbq2LqO_II5p2VDe3y1LvoSf4xkXxocpHNNmP4H-OCwrPKcTQvGvrJeJAVMCAeMjLCNFqufhSFf9IL6kfm47NoKE9GIDHtn7bMYrjAjOMas_xVxv4MmLCzvnZKUXRDPKKW8IKPv5mY5wbOxxHgkIkxAWYgn3sDtI3CE_Y9U-cJMi47etsWUTNkvV-31iZjVNtOIZywFxt7LKTXO16WgPTVy8RqYSIAbSzOQZcDFk6ca9o9OBrpTCieV7cv9jVC67zf9g2q_DBTQLt8l8ADEYHtiWghlQ2bh7FLFnqdRkpytd-9qshad74LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zhey8p0usVzDIU3WofEH9d5JY08rRglmz40a1eKzSxr0AyHqg5HRFOEQLdsLTeBp7vTiq7MZjtdZIaUtKP5HeMiO0PUqxTBu3AJXqrP49_VAutOMTUZMbqF4zFfn1VOqfyr3LnNPY9CHVTGD6ZTlkYRdJAoSrwPohag-d_QMn7H23fyVqDECNMJX0iZNJ8arWyRe43ofgqCP00zbIlLaaWblHGCX0gPGwCMopho0_A6ReYuW6vl3-NMxUsctXlhsMzqrPbOL2JSaw245AH3Mx_LEn4cHh7t3oJ_IzqmFij-9nh94X1cM-fJLx6XvBylvFHB9tir0Xi4Izq8d6HD21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOKvGuXhRAfaZDGW2ZDAadqPURWlxi3aefn_wJ0Py3J0LKq4FmM1bQji2Qf9Mlpg53knyZ3ZixKMz2of4wLTIV0BucKkLmR5Zu0iGBK-qjLhb-4uKoYpxUeMSHPkp9eLMZzG3JD-OmFErj6_C5iKRigtHzwx4lzHTC_RpY7KhR-Z-C_EVPpl7M4htqPa0u67CxeoQX1NuT3OJ8ghToG_YBW77XrEGylcuIgWaFd0jGt7b6LESxki-lwUroqyCyCpurljpmZvx73O8ZPqc5eP-ptFufmZU6T6pX2-7Rf3co1nf7muK7xN1Sx-hHmadsBgXxoYYATthGshr9vuDUZzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJVEPOhd-kqkLh2mQYLre2-dU3QZiMhIyOceBFwXLXB0cAdJ_ahM1PEnxfoaaxySR4EUFX-9h6H6eWcC7RDh_L2jv75I2dHD5Kzp0xDd-L3TJLyXQNKugRLmfSff7B-8w-rK5dJDZB38-X6z30TqSdf6K-Pjn3HxR3uNe2a9nONch_10-GCdcaQawpbHh5jSTlpODXrgi7Kvrmn2yoTq9ZNE7WPrzfhlMw1MeVxOKgvDD8jPxS93GXs3LCA55cqwK0NPyHRVIXNy4gJvqRwn_SY1roo4ebScZZXcLoCE3BT-EgLAXkoEHj0GuqG87eumVWMxpUC_Wrd872_xzsC8tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=sgZdNa1vtKe6mfS0KQ1vnVVBkAfbta10vq8n1ZDXlcwve7Q7QpQHGlsToTo3FeUNo1QzZPTZ4xL6s3ykkGGpLJ1Imw7v1GPDQO-dPGWdA4M7PsV3L_4pKYjcvYSGLklb8Q1IPg3GZ7pIEI3jSOJjv3qm4SMOnAK0N6WtT8UZuzt-fC9UA3sn_wZFt4I0elARo-BXFSvjkuI8Z_PkRLIqlJCz2K0O7E4MLvaUkiXBH45UZ8A0Fvw7imXkPtnMXIWxEGrRkJntsP39qMx9LCSbnbc8kH7wvSrrDO4DPhHDbCvMKpQJVJWKFOh2vF0164hDutClgmbbAu8fdUKtMSxQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=sgZdNa1vtKe6mfS0KQ1vnVVBkAfbta10vq8n1ZDXlcwve7Q7QpQHGlsToTo3FeUNo1QzZPTZ4xL6s3ykkGGpLJ1Imw7v1GPDQO-dPGWdA4M7PsV3L_4pKYjcvYSGLklb8Q1IPg3GZ7pIEI3jSOJjv3qm4SMOnAK0N6WtT8UZuzt-fC9UA3sn_wZFt4I0elARo-BXFSvjkuI8Z_PkRLIqlJCz2K0O7E4MLvaUkiXBH45UZ8A0Fvw7imXkPtnMXIWxEGrRkJntsP39qMx9LCSbnbc8kH7wvSrrDO4DPhHDbCvMKpQJVJWKFOh2vF0164hDutClgmbbAu8fdUKtMSxQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=uiFqbamBWdtvDlTlNyf8ru6e_QMPK87ejbG5zhhmMMzrb30xNwZpYF6hF_7GpNHa1pvWjpdc2-u9gq-20TuRtbHEul2CFgxo-w8pDoQUoxyrHnNPJtEWzWxm1D_G1cW9BgxAKbMx1glSE768Z9GPHKgam51DrzAUQfJkCLO2dyDK_PI7EHr8wmDetYLK872tWOcjZrxoeB4Xl7auIB8OZYq9CDe7yOeAr9PA2Op57bhqh8zFeRRvnBD-xjBcI-rkL20fd4JV4P_sDebwf0Ls1V-lj5d6dZa0T97RZwv7TwX1FfuwmZ7eoYNInY9BowdXUAQhPmXQAmqwkBECLyvCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=uiFqbamBWdtvDlTlNyf8ru6e_QMPK87ejbG5zhhmMMzrb30xNwZpYF6hF_7GpNHa1pvWjpdc2-u9gq-20TuRtbHEul2CFgxo-w8pDoQUoxyrHnNPJtEWzWxm1D_G1cW9BgxAKbMx1glSE768Z9GPHKgam51DrzAUQfJkCLO2dyDK_PI7EHr8wmDetYLK872tWOcjZrxoeB4Xl7auIB8OZYq9CDe7yOeAr9PA2Op57bhqh8zFeRRvnBD-xjBcI-rkL20fd4JV4P_sDebwf0Ls1V-lj5d6dZa0T97RZwv7TwX1FfuwmZ7eoYNInY9BowdXUAQhPmXQAmqwkBECLyvCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvDwmp6LFsvpIuBVBV4Ood_f6tHq1_KgstxpkD6uw1zT4ERWYjvkkc7vZXt9AHz08Y4gaULqr1nVeGRR4-OZ-L5TRlGR5B6T8crAEbz5u6-_ZR3tg5JKzOVa9zymmAb0ja88g3ntw6opUHr4CyYmIAZXCpIANxvNwB-660WWvxeswrTlnBQP5ux7ToUlrbw6P1jHDXx0wjN2OS9lTDkmjVO4_KRuk6JlPbIPGrkCHnlTfZj7d12uamvPefQp7xdPGwxhNkvpxs-vm-4pwds-z1QRogzQ83nb_tYIYVtSYYLOFDxt8-cj2VlUP_T0j8-mNnt448N8KxNNc4tyfmHhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ1BO3Mh8rfP90ZmP3hDAAfhexdRb9iIzEE9VbLERv9i6r0Wh7iRkGIZmPCYh7mVJ3rzLpFiHB_J4qX7NzjxewtMrfrTs5iJRI3Qif7WAqP3yznR8UikzqNfOUSBDfIaZ2FgzMl9VuOhNmaOrUuPtUWNjVijCF8EGiG7D1DNX2iPTm0T-j0Wr8z5orzuXPi5fV3EHoUGUltrNSeBJBZ3G4i3DKObRsMiDKFHDGChghb2o4CmD7XaF9N2cZKV4H2_decQpayoOsDJBsnVmf0ZQClHiWVLRWUowXDJsDMIEZydnDvQE1LUTvEAdvIj4JcCe0F2AU9q8E9oaIYcFtcLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=JR-UJWnUpiDNbOkglbaPoGAJ5gXrI_cYPAj7CnQcTat8l0RSv37axCEGK8300m8e22aGc5RSFld3WBsMc9b3i5e2FcScbiiCtIst6rICldVsluYiJq0l3udUtYNIqHuNxD3Oy7gA-l71sHziNRE4hkq54nEXwvXmtv12XWI54d74a4IIZAZhcJT9DacNpWFigPJpzSo_YBWoi0qi-QtE7IV3pTYAhcmCP02HlVydyhK3HSBY8WSTBeMUZ9sEgfemViTbhj87qK_pGXuKisMyLdnxCj5u9KW4oc5iSrZ3jC_hOMIHzGNgTaUQlQRsVlHjUF3YK8aarkjxJOy-J5PW8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=JR-UJWnUpiDNbOkglbaPoGAJ5gXrI_cYPAj7CnQcTat8l0RSv37axCEGK8300m8e22aGc5RSFld3WBsMc9b3i5e2FcScbiiCtIst6rICldVsluYiJq0l3udUtYNIqHuNxD3Oy7gA-l71sHziNRE4hkq54nEXwvXmtv12XWI54d74a4IIZAZhcJT9DacNpWFigPJpzSo_YBWoi0qi-QtE7IV3pTYAhcmCP02HlVydyhK3HSBY8WSTBeMUZ9sEgfemViTbhj87qK_pGXuKisMyLdnxCj5u9KW4oc5iSrZ3jC_hOMIHzGNgTaUQlQRsVlHjUF3YK8aarkjxJOy-J5PW8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=pSooYiNT-adfP18gXQ1ENf1Ls_zXy-RK2b10Y-xjNgCmb6InMu3fv-99UKb1-Zu2oNUbJJcMIjeyKl4PSTeTFLCrxZT_rqjskeL4cQIcxBpbtmfeCR4X_YsopxTTRgobOonMhpKzXApJvz4hmPbwrtntr2qUlWErrXw9h23ToL7QzMpYXnVmkeY9tZZ43DYC3opscuUgtaYjNukGg5niyh8Xaqzj-KEnIYRbfGVj96h13acIFI_CDDvyWZH6uhtAt91ZmblfoqjSdKgKvrs6bcCG9VIT2etz0fTggdMzDU4ZFIVem7S9h700hRm2xI-8fll_Nu7cxdWBW49pes-eAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=pSooYiNT-adfP18gXQ1ENf1Ls_zXy-RK2b10Y-xjNgCmb6InMu3fv-99UKb1-Zu2oNUbJJcMIjeyKl4PSTeTFLCrxZT_rqjskeL4cQIcxBpbtmfeCR4X_YsopxTTRgobOonMhpKzXApJvz4hmPbwrtntr2qUlWErrXw9h23ToL7QzMpYXnVmkeY9tZZ43DYC3opscuUgtaYjNukGg5niyh8Xaqzj-KEnIYRbfGVj96h13acIFI_CDDvyWZH6uhtAt91ZmblfoqjSdKgKvrs6bcCG9VIT2etz0fTggdMzDU4ZFIVem7S9h700hRm2xI-8fll_Nu7cxdWBW49pes-eAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=P0IbQvaQuDbl8RYolrWgWV0SWft2a4m__Kce3v5UtsQa9tJD0AMqBSS7cVQKDluZ-Y14z6dXCe8-RuzvesW8oxQ8OVNQ4htcDZMoer-BNOrlmhj6YST1mvpKFdHpWne6Gob5dOWC0bXwjfOVBQ9KKSkUTls2jPJu2YlUZH4FIFSw5ZYLgrApeUNBd8Ng5SjRUiNVTolgxnWjgawdeKVaezKMd92dumhz44fshQgYXY3Kp3MkwfAkhBPazHW0NGDgQkHV1bh2zjMsdKbFT_gJ-VFW_4-2Xam5his6jP8gWvO_d6sSONwPRoEcq98n8TF5m_IopOivGj6DbeC-vpwzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=P0IbQvaQuDbl8RYolrWgWV0SWft2a4m__Kce3v5UtsQa9tJD0AMqBSS7cVQKDluZ-Y14z6dXCe8-RuzvesW8oxQ8OVNQ4htcDZMoer-BNOrlmhj6YST1mvpKFdHpWne6Gob5dOWC0bXwjfOVBQ9KKSkUTls2jPJu2YlUZH4FIFSw5ZYLgrApeUNBd8Ng5SjRUiNVTolgxnWjgawdeKVaezKMd92dumhz44fshQgYXY3Kp3MkwfAkhBPazHW0NGDgQkHV1bh2zjMsdKbFT_gJ-VFW_4-2Xam5his6jP8gWvO_d6sSONwPRoEcq98n8TF5m_IopOivGj6DbeC-vpwzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=mwqLNC_PdGRROUequOShPNCtpCLnyhKicslbk9dpDA8p21mB3VqOKdCmJb4jkaFletbpPpgdyf0jpeQEa3ZPOVFZX5GtRzUCjZ7yIi11Se-grsSy-i-bHPmzybVDvjjD4c6a9CpsJhMhf8KvSioZkjBjxHcQU7tWfJgAHyUVMhBrDTwUEl-ohwPVOujrrBlIMNVFF4ehl-juR_PYP2CccVawgYVNZqPiCxQPvOTWnYpjWGgUAmGQzgm9pzzRraNLF0dAkgVn8IstvSUXq58vzpQJ1W2r9Pj10sBFM2vHHeOpCcL0SPhRdukaD3fm-W4RvKGkFTU_xaCjZbR5KFI0CozwXKtckpwvj57V1xIMuY4EA2w1ea5UphoPNbF1y4dkRtCaelX17kzFkRtGX4A09Z0KDY6SA6KNw-j8VCW1G34M7iohuHbBzKrqpoTXX-kUxZdgbnuSGiDRwlk-5e4nIJwOvkqiPposXIoLAZh7aC2jK3YK0LEZ1xp6zj5PT1y0djGE-yox0l2QWnkNKJky2JGUO-SzmYjIf-p6XLHfcW5_eTkVJz4rY3xxJqwk8fhodsLc9DSFnJyXIGTMkHZJICm73vW5kqKOtaG6cgc84sUhRNfQqEUJqIZyaL2Ss_j8HAIimL0BtRZVrA7TSultUD4qTqS6oWQXisDeRv4AN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=mwqLNC_PdGRROUequOShPNCtpCLnyhKicslbk9dpDA8p21mB3VqOKdCmJb4jkaFletbpPpgdyf0jpeQEa3ZPOVFZX5GtRzUCjZ7yIi11Se-grsSy-i-bHPmzybVDvjjD4c6a9CpsJhMhf8KvSioZkjBjxHcQU7tWfJgAHyUVMhBrDTwUEl-ohwPVOujrrBlIMNVFF4ehl-juR_PYP2CccVawgYVNZqPiCxQPvOTWnYpjWGgUAmGQzgm9pzzRraNLF0dAkgVn8IstvSUXq58vzpQJ1W2r9Pj10sBFM2vHHeOpCcL0SPhRdukaD3fm-W4RvKGkFTU_xaCjZbR5KFI0CozwXKtckpwvj57V1xIMuY4EA2w1ea5UphoPNbF1y4dkRtCaelX17kzFkRtGX4A09Z0KDY6SA6KNw-j8VCW1G34M7iohuHbBzKrqpoTXX-kUxZdgbnuSGiDRwlk-5e4nIJwOvkqiPposXIoLAZh7aC2jK3YK0LEZ1xp6zj5PT1y0djGE-yox0l2QWnkNKJky2JGUO-SzmYjIf-p6XLHfcW5_eTkVJz4rY3xxJqwk8fhodsLc9DSFnJyXIGTMkHZJICm73vW5kqKOtaG6cgc84sUhRNfQqEUJqIZyaL2Ss_j8HAIimL0BtRZVrA7TSultUD4qTqS6oWQXisDeRv4AN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=lnLPJLJRAkP4eR7ooqhWVwq-TcnXs6v4Ywq2wDj3NyvDBym5s7Ob4okMcwDln3uKW9wF9QO_GeFJKAhBChFJ7DvvU7bC5_X9LIBNTnqpxK5eeA8DjuV5MfMhmyZBX8RpKxGT7-nrgWI_Tb0VNv_r9Adr9XMuiq4w0fyrXPjnZEYxHAeoCRMYNScabympXvT0DBjVgsVJfa1sGpOuPWA0TcdTNaDeQVsuKIXbXnjWWVgTxFdozA9pt_sg0CRdxQvK66ugbuSbyM1rVpcwq_QhT2HXQJSSYjYjuIxW_OjEGa1lkzgpK_cwMJibuk1ppoGkycAFEJuJMO3pE96pwjvI_IBzrTDSG6ZTUWmunwl8qDgFCmVHglzUnNw0nzsakGjnCOS0qp1QIuclDVS4ShTy5DPF4ucvKbtpqPCTb8_AamvkOZ97-ZdwP-betsUy4-KAwTmEQsZA9mLeyK01YaOJbtzMYFPFOLWeEbrSTQglmZPt9haXj969uPk5lW23qeXBglJJc_jlY2ruqurr75D9SPTj9lR6ICkN5Ux2dMMAOjtvBuzgfAJ-uwmRt_YKPGQbcyDRU1PlBSSU5xxLFKTjTubYu5pB-Bz5sKK8V4wa_zEmzz1tYTfEi91HiFcdaSsYs3JvE7yRmtfuPcK0tGGh5uUN70UTGsGbUwowv9V67rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=lnLPJLJRAkP4eR7ooqhWVwq-TcnXs6v4Ywq2wDj3NyvDBym5s7Ob4okMcwDln3uKW9wF9QO_GeFJKAhBChFJ7DvvU7bC5_X9LIBNTnqpxK5eeA8DjuV5MfMhmyZBX8RpKxGT7-nrgWI_Tb0VNv_r9Adr9XMuiq4w0fyrXPjnZEYxHAeoCRMYNScabympXvT0DBjVgsVJfa1sGpOuPWA0TcdTNaDeQVsuKIXbXnjWWVgTxFdozA9pt_sg0CRdxQvK66ugbuSbyM1rVpcwq_QhT2HXQJSSYjYjuIxW_OjEGa1lkzgpK_cwMJibuk1ppoGkycAFEJuJMO3pE96pwjvI_IBzrTDSG6ZTUWmunwl8qDgFCmVHglzUnNw0nzsakGjnCOS0qp1QIuclDVS4ShTy5DPF4ucvKbtpqPCTb8_AamvkOZ97-ZdwP-betsUy4-KAwTmEQsZA9mLeyK01YaOJbtzMYFPFOLWeEbrSTQglmZPt9haXj969uPk5lW23qeXBglJJc_jlY2ruqurr75D9SPTj9lR6ICkN5Ux2dMMAOjtvBuzgfAJ-uwmRt_YKPGQbcyDRU1PlBSSU5xxLFKTjTubYu5pB-Bz5sKK8V4wa_zEmzz1tYTfEi91HiFcdaSsYs3JvE7yRmtfuPcK0tGGh5uUN70UTGsGbUwowv9V67rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=daKv9nmnMVweRIOJo7mVmDY50csw_Xz-hC3PxJFukg0Uq_by9ZPCZNg25XKFF6CeJVqlbTimf7Fu1NCeqgNgqqs36PudHuVYHhL632GimozZ7Ht8ZZjyDBhE1efMtMzV7XDOfKLZMXnQcORVV6nem2QhmLH9K16sTttr3pa7d2MYLHZsq6sR7k-nckUko8iatr6dNiwSI_ahD-tsoYyRkzPJdNKJ68_3YUc-s89gOk_frqzxzUTuJ2zRiu59DemntSLDhrIuaC5Na_iYR2rnRCAEP1jAIwme0OD3rD0iYT1_7a_6Be2wLUL3LaQVrO8zYOiF_S0b4qza4DkmX25iQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=daKv9nmnMVweRIOJo7mVmDY50csw_Xz-hC3PxJFukg0Uq_by9ZPCZNg25XKFF6CeJVqlbTimf7Fu1NCeqgNgqqs36PudHuVYHhL632GimozZ7Ht8ZZjyDBhE1efMtMzV7XDOfKLZMXnQcORVV6nem2QhmLH9K16sTttr3pa7d2MYLHZsq6sR7k-nckUko8iatr6dNiwSI_ahD-tsoYyRkzPJdNKJ68_3YUc-s89gOk_frqzxzUTuJ2zRiu59DemntSLDhrIuaC5Na_iYR2rnRCAEP1jAIwme0OD3rD0iYT1_7a_6Be2wLUL3LaQVrO8zYOiF_S0b4qza4DkmX25iQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANvvhS1HDctqfUASYbq5_ux6VBF0_IQgA80Vs4YsShFg0KALPdyGTnGGpbtQDwEZx-IoAke7jaxa6JF2zJSoQqH98LvvrnUl_5vbR-S4Dk4hSW_joxnr3ndIXqez4sL1CeQvq4u2NE3pSiNCyuBBXIhb7Mgot2Q71PSoLuFBHCBcqMqJckX7X0re-rmwNbqDHa0KhxZQMfMe6Ls-XQWIJEHG6Fup1Ib5f4tVqwSa42gzNMXWf4PG2SZze826T3Vppz1vlScAgEbRUGz6ERFi-H_RoeQYo1fJpMiZTbi9fXZFPazDRB2BZtydSSELuKc0FzMpxgU3kWIoP9YPtXW24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7A5qkgbXaCeXL0jr1KRoNF9ppZ54h4XcWDkk-THgqSSCoEQFGTginXsoSdVZqeONaMCb8uT9ZzTsRQ_BKhJQ7pumTh9shQOtY0IVAyAoTrlpB4bOMDdFyqxvym3rlagLYlYW7xHysdArG7IcjYKMVjBgbae4Fw6Aj5ACqtVw3KwNHAsrpmoljIxA1RgSXrpWZ4uAz00P6FBtS-yzAiwsuni3DzJwodETcJZYt-5PhUopHSkIxkcxwdThL3g0ZlTe-K63sTC0B18FSvzWsFST0y3INoJ5mrAO70QW9A-bhunuD_2QMuxPx8oIbDaI9Luy_YyxiyODeCKYaG_DoBjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=P3oPeTuHYKPlItnSbxGW-j7OLbYaifCJCOGJERCdBaToXbOMvMSntdUVPxOk5ELux6kr8vIYTCwoZiTGD_M8DCMFf2rTZzBas3gFca3Kfb1sQ0twCQZRWUo-nlYN8KOK-IhQKywT4xuisZc65yrj44S6RCEe-3jfwCQiWPuvwy_Rybr_qOk6KbvDbySnmU_BU2UmQKruRLIJqx_w4xEVGpLoQVTtEWTgVfH6qrJJbCMetIkjoIGS4U9ptCMiboFozXfvUZXuH7_pggnLG-7bmRoF_PytGdHoDRvcZ-2c4pv9L0OB1PH6hL1KU_X-0w5jmwBZCjVq0I9rRXO47Bfk6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=P3oPeTuHYKPlItnSbxGW-j7OLbYaifCJCOGJERCdBaToXbOMvMSntdUVPxOk5ELux6kr8vIYTCwoZiTGD_M8DCMFf2rTZzBas3gFca3Kfb1sQ0twCQZRWUo-nlYN8KOK-IhQKywT4xuisZc65yrj44S6RCEe-3jfwCQiWPuvwy_Rybr_qOk6KbvDbySnmU_BU2UmQKruRLIJqx_w4xEVGpLoQVTtEWTgVfH6qrJJbCMetIkjoIGS4U9ptCMiboFozXfvUZXuH7_pggnLG-7bmRoF_PytGdHoDRvcZ-2c4pv9L0OB1PH6hL1KU_X-0w5jmwBZCjVq0I9rRXO47Bfk6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPT-UFe0alBpr3m7YsYffzefy50btPuVG_-l-vFT1Nfufi9B-tSzPf-b61pr6prhKYBfQO3Am2HCPry2FNzoX6wtmAqjeKgvsg-S6zp365fp3XOVxGe1GWvaEAeaPxNHd_prxBLV9x_kwT9avIvFzdtpCz4wcvAS8SVNlIWpMuAVnZClYFZ_gzRItvX--LZFKkhLOQ7_GlQzocZnBbViVLDcOw-mTTRH3FOpZQWo7WtpYzGEKIr2FisuHhF_E5oiuRvXT8LpICjqD1YWxN4WrOwkfIb29Tyc70AFRvwVLrSPrG1OVfl_0efd65BQToiFxpyIUzUEK64YkubAK_21yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfiuT-WCmHY222MlGwbnfqGB7Ym7x1E3j0Mg8dKYvN8QEc14YdisPUKj7pXlBgwfsdUxbmdQcqXwO9cBthxLhIgEPX93xh6ZSOYnKt1bH9j8kqctcrlDvGTHkYSnbaB6jAANMGlsb1Tu9zuvm510yVdukOi7xcQTngi7q11dNd6hgYpPW548Fnbnv8sKe7X_x56uvyI6PbHxmAFar0HziEotc-dq-XB8Lj9cBKM7YZZoYug6b4ozXHJaQxC_cn5eRTqRILGAfVx_FM7UhDA15HsoAvas7AACHsE8FDzbo2IN-23kks5mJlX5RDz9O2N96f_2N4WgYsNGUMoC8CEIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTk0gtVOv-0SxbHPm97fy_w9eyl9Vl-_XrPCyUUrAU4wS5Ww2WkFgV0RWSPS47FPjXJxI27mW-DdA1v2O-7MF9VL0ODeiI7FxN3-0pBwWHTE-038Fe3iUfxO5k4dm3Q5K4_QPUw6TXzumNVPgAuwr14V3iMhP9oPwHjivukTnn65FFOihcPRzV7aj5r-Zqpt_7Avx6W6LzLkWrh7jWcZxWgT3abPvuALkKAnK3fiANIFJNDOandf59zsJjCs0obVrGXsm9AhNNmLlNd1HB3r3g5fFLKPyawN8MIzTkkoPDyc_oasMmd9UJQn0Pbg1gLtcoZQ--kXbEuuM4S4Hg36QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQywHMeGPCYh8kSHtIanjd9VjE_Rqsa6r6zYk1zlxTErLQyPL7fh5l_1ZTKpDROuWZbX18RJSPFI2M5bxkCurAwgrN3EdPePCkXtdIfKlJdSGQzwNqkSxv9Wix0_s1RlE_qw1rpGYUH9OU70S9A-dNkL1utg41WrICauNwfsGzX9_hg-hIpVi6ACFM7EpZ64ePSk7YUc5mXM9qza9Sdg1NjHGQ-tL7h9BA3osnPhokMsDFw8lVPlDhPDlsZoefe0uZqewNs9LEYK9dG-kaUhsM8CGWlFPq_DP-y6E6Yf2rroBWHP-bvl5xma158VYk6AE-heGnRocy7EDh5ah-iT1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gogU2n_wGZAoXyj5_golGw_PNoML79by-QmhV7xUYo8D_hONlfy_13ggi8oVkdKB7UsEwUhyGe9ZvfePDC0CPJN12u5ms5L1L4LQdVTtZOd84oRGuzgEmQQDLpX_QxjtHVApla40JRek8oUL09DwMXBUWjqz8GeuZyOa1sWYZFOkVVoQHQhvMwoi5f-PwcwtMBt5V5gQxXNiSvZWTe_-LdNrTKORH1c5etXWDSesWqklzh2o0IO1OHxTNVXJJAEBzqBqNp3KWuCiA3T_w6lB76AFEUy4dhS6wLme54LjtpninPRvu9OmYLvEyO79je9wN4pEO0KGQbva4o23S1RZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lynvk4UK-0Dci02DxIwCxXuMmS1urLAMaZfGn1nCfKBnA9kWvjZaVOpqVBNM_BdtQFzYzNLIpmMqIUDv-I7olGQxZOzlavoY0Zdcj4IDim2QJmynQRYRbcGR9meCQ4o1K5BHSg7J3TWHwUBWgJZGNjGIowug0MZNRhPYgZEnAbtUkWw0JG_aWbftz6EZrx3m62NjToBFDEGvKG9GiT8AU1M0x0LTU24DNsUam4dtya355V03EFVIelX4LmE2yahee7KoiWeJ-s4Zg6epyo2556Cq8wi9v-HSvNgVC3BrVIWIElVrOfrOKxhUg9-H8F_wC_UG_zE2OtKKizDIYS4rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH_LQCzfYT5iMu0H_HCYrMnSRXcVS7Fd8HB1rucBjytYVaT1ebRWDA2ZnJ_rGDqL6hb9y2pNkIq1bSF3vEX4hhXN-So-lTuqbOw9ciIrtcPSq72hucGObEdKciTNyAgPn38-HEDHQckLdNWYdU7g6exBDgAzxuMkiZ7Nn3Ia967LuccSTQj--r6HMMQPCh8ejODCJZTitKEsKpvoJJXI-hwY1gYF1gi4Fz5NL7oAzclDxDsLo0cdMyCpGuwXoa_c_iIKC7pwwC19U55sc8YJmvW7GnvKyhnk_jgmeQI1Cm6w9iNnRAB7KdCgonE--b8cI4by6_p4yXKxhl1_eun_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK3WLBfl4XDN0u9tU1gbpmkjLlCamA05eKySBmtR6IK6Ohrp570TpfMkIPg1mIgSQMkK9BPz3K-QDl9NvJ8chOkntcxipPh9TFdOrmCAExibrj3-qSuV-HxUhQAaTpGs8cXbBSKC9NcnojidOnodl895o73WURDLVcTJ5fk-Krxtnvjcvs-IRyes0a0bmEg91iOJXgFGPF0s8pDI1AFXIe76mIDJxcSzyqK0eq5S_HrP9AM3Y_cX-2WOT7bLVdLHgBcQelkl3UcxkWfnMK--_ArL9ja2Am5buvH5hH2u4pavKfRy-tKHnbBzSaMlr5_YIbo5rC5CI94tvg43RYMsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIdJpPRz-9QdvFRujEtYjzuuFo2ghR7DUxdnizY_SYGRLuHkrWxkgV9wueLYJT33Vmjx4XKzDlVEhMkUlJwiPfc27_2Kkey6w2vwZnzEGxL9J_Z14YmMov53Hqh1Oy2iaFUBtn7A49Tr6g9f4InJeAWEYJwjU7zMkYQ4aBER1fwMILoIGG0Q_y-6a_6uKXrizDd2ssIhRZMhAalJUEpKDJilm9Un1sW9plYld5LynqOWWw6WwFqut2TbgyIGBhfS8W-_VKNPRDPwvOY8aFqx5ReHEq4JkCjgSboeBoSJ3MHwRCVjFl9xobngwMiCnY1_Y-GU7MKZqmNInIbTMEDsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tsnnp50R_gP0sPL-fbXLQNahCkFdbxml-0V_v7ZBWJ1WSZAupS6j3d7R5Xvd7Vq5l5KunIQcpt8V5Ib7pUakWL2dYtnCV93OcZLyRUqqz6j-cj9EnW1naobshYGd1ffIQPwj2W8EDS1sJpiYvYnU8bDFp6dMiP9FAdMSmYs0ZypvJR7Mc6EQ780aauKEkMzG0ib8I0t2-9_mWUPp2fwE7DZKNhjwKyUCvTWjkknT4kcTQpVgm0W41QRpWD0NlaoJqTLdKFswXhav0bzg4wdWRSV_UHA4PqKaKlei2kpcC9fUhoZcY3SDfQnrcX7nnACafdxQOzkHXLtuA2ACprQLpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pivn9i3Qxee99cem8SqOVxmkDU_E2hnDnJs1RI_-mUE5FOyM1Q_LpPs3MwXrXxBnFP7FFUOm_UXQKKsAKz0hlCw1okDpoTE_F19ClLPKScs2ik0NJdHVB3ZpvQwd9RrZBJT94iwj-z8VHbumUZDluvY7IYCk4t1Q80A753VzvsXqWEpEjtvHeENfNbTxe5AH82TBJ5d7wH-fHePm93ptc0ttFUjBCopZe-BT5ix5D-3p7W3P8fmLz0wzcYUtQSRydzZR7Z97nclg9kIFvYP4dbnzEJDLsHmus5yVQeVTSIoyHSKs_eGT45RAL8lQ-w6ewP7NaeRmGBm9yBbndtRGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=jpp-Klb6VPvl28eAl2e7GI0AVMY983g9GVL_baWqzIb8oir0Q7jzACEve4wTNGg5Fc-lJEQ5TICHfv-nrAthoKuZHddpoOq7OkUJMcDkjHvxwRXIwStNxs8B0PWInHh4Ordm77WTmS4Z-Zou8rFilzEdp7WxG-uKsMdWTWtQ3hbuNdLWL2xnzWIZywO8BG_xllvOnRvnDs4CLKa7dYA5cXC8WJQuA-CSW_kHZrJ2r8GJZc2ewE5hqK6EAPk3fjtEkhDhf37z8Vrzh4veNO7OMggpFmXKs1GOx5KWARGR1kBb93lKC2vgwTZlvzNLlRj0jZtQ_vQaoG9dN8izJZGB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=jpp-Klb6VPvl28eAl2e7GI0AVMY983g9GVL_baWqzIb8oir0Q7jzACEve4wTNGg5Fc-lJEQ5TICHfv-nrAthoKuZHddpoOq7OkUJMcDkjHvxwRXIwStNxs8B0PWInHh4Ordm77WTmS4Z-Zou8rFilzEdp7WxG-uKsMdWTWtQ3hbuNdLWL2xnzWIZywO8BG_xllvOnRvnDs4CLKa7dYA5cXC8WJQuA-CSW_kHZrJ2r8GJZc2ewE5hqK6EAPk3fjtEkhDhf37z8Vrzh4veNO7OMggpFmXKs1GOx5KWARGR1kBb93lKC2vgwTZlvzNLlRj0jZtQ_vQaoG9dN8izJZGB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=TyWruDrQC6LmCOKyHl_odXtuQ6wfCNgcP7PH9UGugmZwHthVqLWcN9l25k5HSzWw96WZL8bYvwnpwJgYTExiVNF8fuBjNjOqtWQgKPokHPjXEF1Hx5PIzmEUvel5j_YZa2i0MYWlwZ5-4xqtkur7Jv1bdZrZrrNE3aRsaueX4C_8tH6ppDjieIWK-21q0nhYLlYSYSpqglEQNFuhXKQPkMUoKVFR9DaI0Szjbhsn6WK7IZ2BqG3xrtztF88WKjt5CAlPx5hiDiUPD_dpWBZ7lV9dWoQThSsNCcEmXbYmAxOpO1xLzuFc1WslfR-j8OiFvvp1lLURlZFoJhmsdbMUNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=TyWruDrQC6LmCOKyHl_odXtuQ6wfCNgcP7PH9UGugmZwHthVqLWcN9l25k5HSzWw96WZL8bYvwnpwJgYTExiVNF8fuBjNjOqtWQgKPokHPjXEF1Hx5PIzmEUvel5j_YZa2i0MYWlwZ5-4xqtkur7Jv1bdZrZrrNE3aRsaueX4C_8tH6ppDjieIWK-21q0nhYLlYSYSpqglEQNFuhXKQPkMUoKVFR9DaI0Szjbhsn6WK7IZ2BqG3xrtztF88WKjt5CAlPx5hiDiUPD_dpWBZ7lV9dWoQThSsNCcEmXbYmAxOpO1xLzuFc1WslfR-j8OiFvvp1lLURlZFoJhmsdbMUNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=I3FBoHlAdapPkisgtXAJI_3-jY9BUdXwt8hwhCYNrrZHDq7dFesq4ImJvp--1VDJRfkW3Vn-3zKottYiJcZoVhBdQ_kx7M4rUTEVNNM6CKhJLbHyjJSIOyCsHSlR-I3t2ipD0dAJZHY6irL5Gu2tu2s1VGFfpHOSsIdN1hpbKpt_yH-TkGSvrRmMtmba_uRPoINln-hJ_WZoVeUkMPXeBUdS9ASa4qvX0NLNJv3-nZ3__PWd-JYM2cwJB_T4ZD3brRjFCCmiLCPRWSOg-nO3PoG6GvZpXEXTXSNeiS53DS5XvCAME-myk5RDVrsX4lzzBG_IBUfTEdtnb2oc1dHyyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=I3FBoHlAdapPkisgtXAJI_3-jY9BUdXwt8hwhCYNrrZHDq7dFesq4ImJvp--1VDJRfkW3Vn-3zKottYiJcZoVhBdQ_kx7M4rUTEVNNM6CKhJLbHyjJSIOyCsHSlR-I3t2ipD0dAJZHY6irL5Gu2tu2s1VGFfpHOSsIdN1hpbKpt_yH-TkGSvrRmMtmba_uRPoINln-hJ_WZoVeUkMPXeBUdS9ASa4qvX0NLNJv3-nZ3__PWd-JYM2cwJB_T4ZD3brRjFCCmiLCPRWSOg-nO3PoG6GvZpXEXTXSNeiS53DS5XvCAME-myk5RDVrsX4lzzBG_IBUfTEdtnb2oc1dHyyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
