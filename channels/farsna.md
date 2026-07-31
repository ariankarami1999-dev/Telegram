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
<img src="https://cdn4.telesco.pe/file/Gp3qmQy6DC_021UOMH26IRfSipgIgLWN7FYgSfbCq5M2Dx78dIXXYe3fE_LWgMkUTS2C0etB6YMRUfNa_ZAubv2ofnXIPCg1LRl3kGbQyoJXawEayspiS1FqUQnbmulePoIvaaP7MJr-1w_9Ohxd7q_kdmoD9QqymROvreta6cR_XOkATh2fpaDtZy83-u_iNZ7_CAH94akpM0bgEZ9gO_a3ejpmsLxZWDuyV3y3CEV-qvsiQ9jA3W_kbWBAncPnUzKbekGXkLTcXuZibti09wnzIm3OM68KrVAXsbUefAcz8QqD9uyNCW6Wtc1k3ZrcPiy05pMNijZsWpC18pACrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-453755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۹.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/453755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۸.pdf</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/453755" target="_blank">📅 21:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7590dc25b1.mp4?token=ddUaEccCKgJyfVswQHay66G15FxvJKgLR1MvvAamdUbq1ebr1X-9J-IfFFSDDe89Z8VvDv5ZujdhnLR0o4R4Ao_yppTGuM8IhNylj19qf2MzlvsPyJp_xPWwFQmn9vTGrw3vtJwnFiIpQfd9JIE-_bCAIFTSrkgRjb7PVZX8YdaE_HAnDFsR6VyNZQ_dtRyAgBL9qxH4qBgsXp0XcEDiQt8rnqfHYofz_QnxlSKIuhU6DILFFCzqiO2cF2pHp8eTqd1IN1a1dMtCjdRKIYdTHrujtJLa2_lbp7g8qyeyV_mtS2vpAM8UZEvM7w5lRt4vQtqjoMGQygEIIow_iGsIMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7590dc25b1.mp4?token=ddUaEccCKgJyfVswQHay66G15FxvJKgLR1MvvAamdUbq1ebr1X-9J-IfFFSDDe89Z8VvDv5ZujdhnLR0o4R4Ao_yppTGuM8IhNylj19qf2MzlvsPyJp_xPWwFQmn9vTGrw3vtJwnFiIpQfd9JIE-_bCAIFTSrkgRjb7PVZX8YdaE_HAnDFsR6VyNZQ_dtRyAgBL9qxH4qBgsXp0XcEDiQt8rnqfHYofz_QnxlSKIuhU6DILFFCzqiO2cF2pHp8eTqd1IN1a1dMtCjdRKIYdTHrujtJLa2_lbp7g8qyeyV_mtS2vpAM8UZEvM7w5lRt4vQtqjoMGQygEIIow_iGsIMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط اف-۳۵ آمریکایی در سن‌دیگو
🔹
یک جنگندهٔ اف-۳۵ در پایگاه هوایی میرامار سن‌دیگو دچار سانحه شد و بقایای این جنگندهٔ بیش از ۱۰۰ میلیون دلاری هنوز در آتش می‌سوزد.
@Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/453754" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515709c4e4.mp4?token=Sx-3evW5GPVBEbxQPZHvg04rbisxLKXBS_7S5hrOzZtxOoiJRKEyR7rRS2wZgaAwLCLdV2RHIvGGeKpvJ3Q160RxhQ4w0EpXCLBmeBAcn4vZQatR9LFIRG1Kpq10y4ydPuE2uXJnwPovdHsAkmIDmkNP2h-Dyqv54JcBqiLB3eZVce6PJZ84DnA3JZJrPcehUF33BDhlqkIuqiMi3arwCDFFYIvda4jnb7LoaipIxHjUiixH1F2I6QnfF2GM7WnsQ4O7wJGVHxUJfZHtsu94hqnYsxTrU81-B_28BRLDEoLPwO4HcTnJRBwU1zp-9vaaKJqcPaMugr9hqkjC7acPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515709c4e4.mp4?token=Sx-3evW5GPVBEbxQPZHvg04rbisxLKXBS_7S5hrOzZtxOoiJRKEyR7rRS2wZgaAwLCLdV2RHIvGGeKpvJ3Q160RxhQ4w0EpXCLBmeBAcn4vZQatR9LFIRG1Kpq10y4ydPuE2uXJnwPovdHsAkmIDmkNP2h-Dyqv54JcBqiLB3eZVce6PJZ84DnA3JZJrPcehUF33BDhlqkIuqiMi3arwCDFFYIvda4jnb7LoaipIxHjUiixH1F2I6QnfF2GM7WnsQ4O7wJGVHxUJfZHtsu94hqnYsxTrU81-B_28BRLDEoLPwO4HcTnJRBwU1zp-9vaaKJqcPaMugr9hqkjC7acPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده عملیات هوایی حمله به پایگاه آمریکا: به ما گفتند که دو گردان پاتریوت در مسیرمان است و هیچ برگشتی وجود ندارد
🔹
برای جلوگیری از رهگیری مجبور بودیم از بین دره‌ها با ارتفاع‌های کمتر از ۱۰۰ پا و ۵۰ پا پرواز می‌کردیم.
🔹
وقتی روی پایگاه آمریکا شیرجه زدیم…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/453753" target="_blank">📅 21:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4c1af480.mp4?token=HVgA3jnTFZdspoOwMjaQH_AeuqFwCHCk5CfTqWL2iwaT2LoLsG6eaeJcdxeCdkNn3HRKPoCbmzIk_ZWFpAkd9bvZKQi5U69AvRUE31MHKWzy9VX3O6v17iopOmvstHK0IRmtZ2E0jxUStRt6bYAQgvixY_7bVLExpnBz0vm6JtZr15fqovlQUOPpLCVKhhd9uhwsakAC7M9yXAgqruzYuhr0f6IoKBr39kLaUrXWeD-GStxjELmGcBbqIN1EE6AUC60cNYW2mEovX60_TK1SUool9ako-6oTr1vyKJug0MUWXgJmBhLVZbRs77yMjkxc9tzl60EPTERFzfEU3LxRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4c1af480.mp4?token=HVgA3jnTFZdspoOwMjaQH_AeuqFwCHCk5CfTqWL2iwaT2LoLsG6eaeJcdxeCdkNn3HRKPoCbmzIk_ZWFpAkd9bvZKQi5U69AvRUE31MHKWzy9VX3O6v17iopOmvstHK0IRmtZ2E0jxUStRt6bYAQgvixY_7bVLExpnBz0vm6JtZr15fqovlQUOPpLCVKhhd9uhwsakAC7M9yXAgqruzYuhr0f6IoKBr39kLaUrXWeD-GStxjELmGcBbqIN1EE6AUC60cNYW2mEovX60_TK1SUool9ako-6oTr1vyKJug0MUWXgJmBhLVZbRs77yMjkxc9tzl60EPTERFzfEU3LxRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون‌تعارف با دلاورمردان نیروی هوایی ارتش همراه با تصاویر منتشرنشده از حملهٔ عقابان تیزپرواز نیروی هوایی به پایگاه آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/453752" target="_blank">📅 21:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
بدون‌تعارف با دلاورمردان نیروی هوایی ارتش همراه با تصاویر منتشرنشده از حملهٔ عقابان تیزپرواز نیروی هوایی به پایگاه آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/453751" target="_blank">📅 21:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453750">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06dbcb972.mp4?token=LlCTWUtjcYHCbSs3ErfQ_Ru5ukjuuyFCE533Xg5r-EkwWPidh-8cUjOxm1VBdKGXh24_1fIonCN2YpwancQQcHHUBH67AvTG4qwFhW7jjdmQ0dQJdZVYvBZkHT5x9b3MJCv7hZyB82WqIXtR5QlOqZq9PCmKehLmKVXdTfuM_zVfIcSmtS_UNgj9CrNNwYn2yWELc2vgX_rWenBdIED7yIeI-TyaNhHFAPpOIe8b8LzQvAk8vBAJUjWUbsRm9D2eJX9pbGBc10d3yEuUemKa2kf3b4NwWizPE9UfIN42rJzu-N9vKWJokc5sOqVadwrgvbwXQgoCDyOl96amstQ_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06dbcb972.mp4?token=LlCTWUtjcYHCbSs3ErfQ_Ru5ukjuuyFCE533Xg5r-EkwWPidh-8cUjOxm1VBdKGXh24_1fIonCN2YpwancQQcHHUBH67AvTG4qwFhW7jjdmQ0dQJdZVYvBZkHT5x9b3MJCv7hZyB82WqIXtR5QlOqZq9PCmKehLmKVXdTfuM_zVfIcSmtS_UNgj9CrNNwYn2yWELc2vgX_rWenBdIED7yIeI-TyaNhHFAPpOIe8b8LzQvAk8vBAJUjWUbsRm9D2eJX9pbGBc10d3yEuUemKa2kf3b4NwWizPE9UfIN42rJzu-N9vKWJokc5sOqVadwrgvbwXQgoCDyOl96amstQ_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی عبدالرضا هلالی در رویداد محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/453750" target="_blank">📅 20:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA-0xRaeFP74rNKjIzbDWkVTwoL__S0OjZMhaW2I0-Qm6NREFpwiGTq88-V_oNMZFTzKdsNwHLNz1oUd-KRPO_Mhrv14v4aLQkgBxA7bCHAJ_MoaEaOqtzHPSP75TIijNWEVpCJn3phWfsWcnbepuocjcFjOBJEZDRIbMYoGnJkOnqpXte2ChSPBhGl5lnhQPQqkHmnHopbGVH0UeBCV0ya315mdr0v1F9c7y_SA4EoQ2H-cOiv_BYf5eYY7oAVoBW6nZO3s5DKaqM5Rlb8FwJCNy4VEa8oS7HF4RTrv5tt7une9so4QyG3LbV70SU2L0t11a4_31mr5HAaYwSXK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: دولت لبنان باید کاری کند، وگرنه صبرمان لبریز خواهد شد
🔹
حزب‌الله لبنان گفت که دولت بیروت با سکوت و انفعال خود در برابر جنایات رژیم صهیونیستی، مردم جنوب را بی دفاع رها کرده است و صبر مردم نیز حدی دارد.
🔹
در این بیانیه آمده است: «دولت لبنان با سکوت، غیبت و حتی همراهی خود و نیز با امضای "توافق‌نامه چارچوب"، به اشغالگری و اقدامات متجاوزانه دشمن مشروعیت بخشیده است. مسئولان لبنانی گویی صدای گوش‌خراش انفجارها را نمی‌شنوند و در برابر این فجایع هیچ واکنشی از خود نشان نمی‌دهند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/453749" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTk_sYWdp4vcvYcR0jEmG6B-QV9F0b8Ip0jDRzJ23aMO3Riin4b-QseyYQgrA5olgiciITZI-l9w6pvbtJanoyVT3YFvv0QUj15Q76oEwYbeVSLEA9XNddnP79x3f3wbnlBESb9ACNOcY_sTGZ5hHiqYS6q5U7q1tnX-WRKBF4OxZ81XtrMOJgIEx_drTXrVsTr8AvSftsCzyqJUSYczsJrEoJ-8xKuYrsW5btjCinD-32SkfaLbGj6U2tdbCIMdZP5OhUbiEGnv7cFjCXVKTUBAGCfjNfW33PPL2Dy5S9eRiYIcNvHcfjzUHUXmVMZ6NbqbyHUREE_IgQ3nkKfpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjzxiWiGlVzOKkmRvx0-5vRk0BA_dlukYAL6qpuqXwfnFma34MryL0igfOHBh1zveRZp2VklNArBkIFofeapMQaOxP2eDtP3QAQpImfpPKOzPff_yJ6qIH7zREZ28kVT6hAEz8aJ-5FlpC51gGIZTbM1lSKwVVKpXjFhHNuZ0C86VIdNW_T8Psl_Rec67L_YFtqEgl7svXdLVtoZ4pIG8KK3elidtJm2RLcYiaxfIFGjQOmNL8162xsFa0aR3v9418Au_DtlhgjgFEXQTImif03dL0ewBKY2oZEX7q1tCXK0f-7HoGAVf_BprK7_8et3t3tB_A51nMn1CSvfqoKuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcVZXyRENvdFlEWAu2In-9tUL3fLri_ypxqHPRygFzdbKAUKfzxu0a7GR1biSklqc8ENqF8AxMhj_xFH7-MA_YbMp-xMtBXxv1xZ6lhtxo-_pVU5ckU5mIjF-KYVjopmwwuCpoycHd0teJPEOqmt_b9RI72tGq2g5oHkqSQsX2mBcALeubDi2GWZqqH1sHSCLa_gaJjFn5SanYA-FAn5MNXvr-IO38KnT-OVytENFNk7KGoC8Bp7KW_I3syQyoUwWA3GqnTfQvTa99UopggWjVFqCN9EkmJpDdGv6qwr6lx8uT5vdIkhuPdmxnP6Y7-GdnwM9P4pSThBePX13H3ylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dC6UUBHZC_IVEEBcRt6mLfroS3W2WEEZtqhlmDqP-ANU5naT0XoeJ5S8xO8FfKtb4dumxJ27_0uXGBhWn0zjKefV0d9H3qXpR2b4_bSknHdLH2wIsqfIqmLz6r21Qk9CqqHBKZGflMEJIzsOc2I8H0Ecs8FqpMMofXa5NeCS-eXZwG6vec3F--sKAcAX8k9pgT5aaRJLrVu8LgenBorlsUpHurAUt9W1HNFDMXA-MUatcH8YMkc0xG09XYBxp3PbgRzLuejS5w5TUBDPDJTg7UmWNem1KBLekLHCyybLjLhTRqNnOb7G7h1xYQlIeaOgH0UHg98FvVOly16sA8bNEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بین‌الحرمین در آستانهٔ اربعین
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/453745" target="_blank">📅 20:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4de050bc1.mp4?token=JKaoIjygrBWPCVqMHmJjvpNbxpl23oFbtfTlGL4HspGCv-L2I-CgCmbKUdJYhdXjyj5sd-xvOi2UqhxxneHdYdFRBi6z3doEhhlVdKzf1boeOizk7Mne_g1ej8T-D-HbWJO1iUHZsQT4ahvjJfzQyOnE749ssFBz1qCghfhsI5oULaYnTx9MIsqMS7o5Nuz70zIAjVCEjAP_SkZYwvqnBsHzIIzXIO4AlGJ1f5zykQEJKxXQhtRWKwYU5ylGNELTvx9skVKSPprQ0k_Km4j-2MPrt64uaEq2lBwCc8xt0hhwWRobpL70jU0B5jDeNcW2IpLT1UmG0o8p_t5b4wcAwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4de050bc1.mp4?token=JKaoIjygrBWPCVqMHmJjvpNbxpl23oFbtfTlGL4HspGCv-L2I-CgCmbKUdJYhdXjyj5sd-xvOi2UqhxxneHdYdFRBi6z3doEhhlVdKzf1boeOizk7Mne_g1ej8T-D-HbWJO1iUHZsQT4ahvjJfzQyOnE749ssFBz1qCghfhsI5oULaYnTx9MIsqMS7o5Nuz70zIAjVCEjAP_SkZYwvqnBsHzIIzXIO4AlGJ1f5zykQEJKxXQhtRWKwYU5ylGNELTvx9skVKSPprQ0k_Km4j-2MPrt64uaEq2lBwCc8xt0hhwWRobpL70jU0B5jDeNcW2IpLT1UmG0o8p_t5b4wcAwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنار ما حسین، شما کنارتون کیه؟
پناه ما نجف، شما پناه‌تون چیه؟
🔸
مداحی محمد اسداللهی در محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/453744" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261429c1dd.mp4?token=t6-4MbOa8_ATFLz82TnDNyR1Pdq9P9y1NcbeR8AKe-q9uksJOyxPzHJ506zL3YZooJOvORb2IrebjtIrkRH0zR3LjkdXmUeTzmsY36nF1h2dIKQgLL7wJZ2RJxxARkMKKdTGfAD8tNBO1IiaaZOHr3xL9nVraFkhHOqYZWtJv9bhTkfiyEr5JE9WyJM-oDeOOIj34QzjW_a_0zkihNsOL5jXJvTes44_9UqHBEWykJp7mee91kWGH3DKiAlgW9qdzjI1ek3Fn0BK3RWyiQzg1UeALH6HbUpdLxyodwKPwGbm_ynuaMRZ58LPDa9JgmIwe02qCgHNFyPdwZYLt4MjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261429c1dd.mp4?token=t6-4MbOa8_ATFLz82TnDNyR1Pdq9P9y1NcbeR8AKe-q9uksJOyxPzHJ506zL3YZooJOvORb2IrebjtIrkRH0zR3LjkdXmUeTzmsY36nF1h2dIKQgLL7wJZ2RJxxARkMKKdTGfAD8tNBO1IiaaZOHr3xL9nVraFkhHOqYZWtJv9bhTkfiyEr5JE9WyJM-oDeOOIj34QzjW_a_0zkihNsOL5jXJvTes44_9UqHBEWykJp7mee91kWGH3DKiAlgW9qdzjI1ek3Fn0BK3RWyiQzg1UeALH6HbUpdLxyodwKPwGbm_ynuaMRZ58LPDa9JgmIwe02qCgHNFyPdwZYLt4MjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ از تکرار ادعای «نابودی توان نظامی ایران» خسته نمی‌شود!
🔹
درحالی که ادعاهای ترامپ دربارهٔ نابودی توان تسلیحاتی و نظامی ایران بارها پس‌از حملات دقیق به پایگاه‌های آمریکا در منطقه به چالش کشیده شده، او امروز بار دیگر همین ادعا را تکرار کرد.
🔹
ترامپ گفت: ما فقط ۵ ماه است که وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
🔸
ترامپ این ادعای نخ‌نما را در حالی تکرار کرده که پایگاه‌های ارتش تروریستی آمریکا در منطقه هرروز زیر ضرب حملات ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/453743" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e5f41929.mp4?token=cDxBxuylvKZTewd76scM8OpTdz4JtidaQUcFajQEwlYUzVyAr60o630dZsOfh9TOzTBe4Ra-13wFQdqzfnyvTCOUoNXSzNt4QlCvOJQrZ-SDOz82X3MmUXNPHaPLZ6t55bi6GOOq8yUc9wov4dKlQyCrYs8xCuIyarFYmdj_Our0TXhRdoVkE7Rco6yreuYAAe7-nZRjv6xrJGu1GBPqBXTAHdu91EOPVSB0PEUfwHrleDZD8ER3R42-42Tra6Tvi4hleu5QxVEbAGrdwQ_yIXK9r5KZlwOd6YCZUqV7R4Yk7lJ0IEsb8xtpyCqXnjgutjKAct2rN2AeqbZzzX86OLRLJgi_d5DlJrPnRKAqZ0lRnBBUqCHlNBz9YsjVgX9JjKJUZAePNGtVqhCsB5q-IeOPrNKsD9i3wqQtJ1-sgM7jO1rAnWYz2P1CJxvdtB-uGmi3bpBW4UstTQhijzbEO6Lw9V57oMIt_nLie7QFxxSskyz9kbAz2izC3PFIhmmilUim0PVnR58foZDjDLhz10zf92G34R_TB_crtmXTin6PH9kmqITrpDkPniooFUDCWcGF4ExEhxWnF6Netv_zRysN230cT7QtpJMUFawfTg57jKg3tBCYXBENuTAGH5cSW9AUEyEBYm6gDM3UKpnlUxRrXqZUW6yfeugAkax8VMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e5f41929.mp4?token=cDxBxuylvKZTewd76scM8OpTdz4JtidaQUcFajQEwlYUzVyAr60o630dZsOfh9TOzTBe4Ra-13wFQdqzfnyvTCOUoNXSzNt4QlCvOJQrZ-SDOz82X3MmUXNPHaPLZ6t55bi6GOOq8yUc9wov4dKlQyCrYs8xCuIyarFYmdj_Our0TXhRdoVkE7Rco6yreuYAAe7-nZRjv6xrJGu1GBPqBXTAHdu91EOPVSB0PEUfwHrleDZD8ER3R42-42Tra6Tvi4hleu5QxVEbAGrdwQ_yIXK9r5KZlwOd6YCZUqV7R4Yk7lJ0IEsb8xtpyCqXnjgutjKAct2rN2AeqbZzzX86OLRLJgi_d5DlJrPnRKAqZ0lRnBBUqCHlNBz9YsjVgX9JjKJUZAePNGtVqhCsB5q-IeOPrNKsD9i3wqQtJ1-sgM7jO1rAnWYz2P1CJxvdtB-uGmi3bpBW4UstTQhijzbEO6Lw9V57oMIt_nLie7QFxxSskyz9kbAz2izC3PFIhmmilUim0PVnR58foZDjDLhz10zf92G34R_TB_crtmXTin6PH9kmqITrpDkPniooFUDCWcGF4ExEhxWnF6Netv_zRysN230cT7QtpJMUFawfTg57jKg3tBCYXBENuTAGH5cSW9AUEyEBYm6gDM3UKpnlUxRrXqZUW6yfeugAkax8VMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی جدید بنی‌فاطمه منتشر شد
🔸
تیتراژ برنامهٔ اربعینی «مخاطب خاص» با صدای سیدمحید بنی‌فاطمه
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/453742" target="_blank">📅 19:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZUselM6OqshQARdbjRbdo_LimDcHASuby9UAURE-dNh86eFqBlw8U_h2tZKKkxja8U-2uYpNjb76ZYv4ogU3KlrKRg_IXonD22Wq1e2gfS-c-_oV-T30XX4M2jMvJfPyO7K1-MzzVh_dGZvWkIyfN5-X__LsoQQ8Xlf3S3cyEZ_XIcA9m70n_W5eUGg37ah6tTB96-aWYLhkYKtlyCy3MoRUchMtsH-ltCPbHsx6ZI_JziebcxeivF_llzQETFlFMhoLht-FbloNBk1nEKOiduD-zkLIA-iCE970LH2lmsB9wjhajVlnnvmKPX-2rf5Nh1tGkhMPJnpzCTq6Jezig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سيل جمعيت در صنعا در میان سیلاب باران
🔹
صدها هزار نفر از اهالی صنعا و مناطق اطراف امروز در میدان السبعین همراه با بارش شدید باران گردهم آمدند و در دفاع از مقاومت و نیروهای مسلح یمن شعار دادند.
🔹
آن‌ها با شعار «محاصره در برابر محاصره» و «تشدید حملات در برابر…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453741" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6dfac1cc1.mp4?token=vPpAn27XHwsMq1LwcAF9B1JMu0Cu3Wc2WuZdMVvXBTc9dx1zf7y9RuqfDbBDkS-BE5o_W0Drnss4mckisTQJrcbrMCi8HJmwucuigmpcuMpc6hDdt8olLGvT-Y0PIQ-qUKJ0iLOqq1OQ57attxMmAdmtRCjSPRMwssSWxw26oIDh5aWwIjlgULkE5lSs51DAUyWBmoWOOp7_THc6vjNjJAfDj5L3y6yc9FJabAeEOIlZP3bWLpuptxnVXVwD2sIZZEWmnIUmhKEDutvrJO3NTJ0xD3XDZvA5lrQR-3LOdEUBTknWc6mXtSAkl0FBA0zOd7HSCjl3SFlr-cPXlMz-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6dfac1cc1.mp4?token=vPpAn27XHwsMq1LwcAF9B1JMu0Cu3Wc2WuZdMVvXBTc9dx1zf7y9RuqfDbBDkS-BE5o_W0Drnss4mckisTQJrcbrMCi8HJmwucuigmpcuMpc6hDdt8olLGvT-Y0PIQ-qUKJ0iLOqq1OQ57attxMmAdmtRCjSPRMwssSWxw26oIDh5aWwIjlgULkE5lSs51DAUyWBmoWOOp7_THc6vjNjJAfDj5L3y6yc9FJabAeEOIlZP3bWLpuptxnVXVwD2sIZZEWmnIUmhKEDutvrJO3NTJ0xD3XDZvA5lrQR-3LOdEUBTknWc6mXtSAkl0FBA0zOd7HSCjl3SFlr-cPXlMz-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همسفران رهبر شهید...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453740" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fb4494f8.mp4?token=VZWSrUsSWLZXnmoDkOqDUdoLncpGSX8SkPuQ45b4DKofJkCGftHMiT3N1BWdX28L1NrnGh_TMZe3tG_cVQ5QJbIxFDKQLe7O1VSrxzn23DOFM0ZJNiJQpfGj7XEvmkdqKMLb3sw8Ytu4h359JFzwOe3PSZp_vGvOmM2dCvKdeeGqFlyPuC10G091BGRA__doQiq9LtOmd6DHx8m7d6bQ3VlkmhD0HQRZChXpDA6BW8fVVwAGgZWpwUqhWIzL7duwuOSsb9yvtAcVDVtsbGCuEGFB4lKTENN6PsrMmiap2ojF8wnLIAqE0H8WmfChM4knYXQ8WzKN7suswUBs1cM3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fb4494f8.mp4?token=VZWSrUsSWLZXnmoDkOqDUdoLncpGSX8SkPuQ45b4DKofJkCGftHMiT3N1BWdX28L1NrnGh_TMZe3tG_cVQ5QJbIxFDKQLe7O1VSrxzn23DOFM0ZJNiJQpfGj7XEvmkdqKMLb3sw8Ytu4h359JFzwOe3PSZp_vGvOmM2dCvKdeeGqFlyPuC10G091BGRA__doQiq9LtOmd6DHx8m7d6bQ3VlkmhD0HQRZChXpDA6BW8fVVwAGgZWpwUqhWIzL7duwuOSsb9yvtAcVDVtsbGCuEGFB4lKTENN6PsrMmiap2ojF8wnLIAqE0H8WmfChM4knYXQ8WzKN7suswUBs1cM3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواداران پهلوی این فیلم را نبینند!
🔸
یادبود کودکان شهید ایرانی در حملات آمریکا و اسرائیل در حاشیهٔ رویداد محرم‌شهر
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453739" target="_blank">📅 18:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0fqyl-NWZQeRSi1_LFXZd-PKY6c_XlYWgUBLRvQKDFIU8xkud2O382lHX2ZZUlZT0b48G59LUFQ0_esegyZ1Cr1rvfv3Sil7aaS3gmlDMOLQKWHz8ZIywxpvKK9cXZRPo54pB3SujvLqTK95DnfNA9lTi1RcqpHObjCN_DBIUSieRrCPrajsbaRotCnxOi0q8urBfn3cHWq-K1iqDCQs1gxfduPEAyJKhJojJpFYsA7Ji2hp2Neq9Uf--ePs26GZK0XGkm5y-lBgeWCafP0hBfYs6sg9LDACgq_eIBXo_PpcyW6reolqXhgsvPFJVBkkYV7wpxxNgJqhqzw6v5LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnflCH_PsMLeoxlK18ScgoeQuBRKaoIDbfvGOzqBCRUCBdj9hMlUmb7GIYzOCUf-P-e6KgK4XlN-YDpKDVI5_bxtm9eU3_WqLCHiBTIHajEyCnqukpHz08WG3CDo4mz02Ttn3FiOK0Zkit0h-aZckN_7PRPjHxavzAkM6f5mTr2fJ97VVHbUyJBGLjK9xwMKJ1mluDEiO-p9TKxlGxfVr5X5pyqGI--aiLSHTR0012UGTdLBk-uJF35xl4V8lDcOaeKY8qer-ThILjq4zSdPMQZNfW4yFWN8Krr_OEsVqUh0jXf0kTc8r6pPsgSk-bH8WWtOz_y6D5ttS-dpdmVQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jb3Aug3SFu8yeGv-BhAKCLixZKgRNkpuSiUwUOYXj0s1eTcQILu5sJzgFYzTAhAvHGAUYcu3RkFOh8W-AvV5FW_qfkhDh_x1XlbBOKwt9oz8sIOJu7CifdOuRIEcE2swwYsompG7Ou8AxC1NDgs2hdslkhocR86ROeszkv8PvBGEJsh31o0SxNaQs99qg_6bBeu0GOC0sBsc-TMKR-um04gcM61Evs1JIIVcqg6BHjybxtrZrW4tv3Z6eFEQs3JyKWJaRvUCIfTUifs33KjxgQiIIOmhBzh1JfQb1cagDJJ_HGGfJJ3t0YuVVoO5fOGDuZIl4eUdEUT2wqOBRrAdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpTKSGu7qk5dosR507HsyQ2sjVGLy4ekyXmP8VPfBxgM5aYAHv3c-DcTbOovQ4adQN6Nq2-EUDKDvEr24uWL_uXXVWyR0LNQD1-yLPtXx7gdx1wgyJeNaTIBGsb0I8wzNE3PZG_yZuJ2VL6th-H8WDmVSJ2N9jBf73-NK6dW9l2r4Es66q5HKFnk6ShXqp6tjsu2bdseTl_oJST2mbyRQrsxpvCPpP8yB2wGb_RXpAaUaXkg52RzOKL-IAlaOguKxTO9dv7xw5Jh9LcseGUceXKmqUbitjMwtP-vFFxVja2Cgq8D1yfaNp1G4DMH5uSz5rAptz8mmRuzsKxJtUcRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqtLw6x7rmkQQ1gI19t6MFzizB-Qr5gjXZTe2ozLnuizjs-fVChbluCU1slU8vgjq9xcuyrcZu6EtAbxk1kEsjHU3DbMob83j7EDsgzcNgOyFYSjnIZnEb0uDUxpwLznK_5RXOJCx29rRNwGfcrbM8TN9_in9tj3ythFyqiR9HDsqGVx4yg53_UnGajClSjpJAGU1CRYzvu2pL2Sew4hxMg8NRoPXdg6I6DyKE0-_ZaUpT_X40D_DX6Pi_bPpGtkRGb_cZ0P4Pzvc59rVOiOvAZgZvBVsDa_ovLc8-Urebrtzd6nySpdxZTCSZWBcwkwfXf27TN7BuQKWtryQV6Aqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22128b0209.mp4?token=lb8Ee5PufKdCa3hkmeYc-J8OkKeVoBqTvFi86AfH55ytuvvJB0KnqyBUl9FiHk3A9gOjAovjw8gB3DecamwrpBzckzrN8cH3VG9-Nj-xUYbuOSVqBpYAd8pKdm4tXC4Z4g5M8uIzFkUKnZq1KIcduX-OTnr5zmsxokAM5oKkDVB0zajz_SZYoBrmyIqZqwID6FEt6pqTYbkzcoVv1IL6dloGKbD5gUA62n5a_izFctpPJh3SeWw16-826ic3gDXM70b08Zo889lU1ES0aBKiUnY4DHYCykml8sdJPSkC8yBNOH-YlutpHCMO1Vt8j-LsxW_1_1vSc2GtwIUhHpVFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22128b0209.mp4?token=lb8Ee5PufKdCa3hkmeYc-J8OkKeVoBqTvFi86AfH55ytuvvJB0KnqyBUl9FiHk3A9gOjAovjw8gB3DecamwrpBzckzrN8cH3VG9-Nj-xUYbuOSVqBpYAd8pKdm4tXC4Z4g5M8uIzFkUKnZq1KIcduX-OTnr5zmsxokAM5oKkDVB0zajz_SZYoBrmyIqZqwID6FEt6pqTYbkzcoVv1IL6dloGKbD5gUA62n5a_izFctpPJh3SeWw16-826ic3gDXM70b08Zo889lU1ES0aBKiUnY4DHYCykml8sdJPSkC8yBNOH-YlutpHCMO1Vt8j-LsxW_1_1vSc2GtwIUhHpVFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيل جمعيت در صنعا در میان سیلاب باران
🔹
صدها هزار نفر از اهالی صنعا و مناطق اطراف امروز در میدان السبعین همراه با بارش شدید باران گردهم آمدند و در دفاع از مقاومت و نیروهای مسلح یمن شعار دادند.
🔹
آن‌ها با شعار «محاصره در برابر محاصره» و «تشدید حملات در برابر تشدید حملات» به خیابان‌ها آمدن و از ادامه محاصرهٔ دریایی علیه عربستان سعودی حمایت کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453733" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsr5NdYMsfqNrec46Yu1KApwC46IlRxE6A9XnFCRvwq-mQDWk5l2Z8PO8P5v5L8IRgccGKdU4DojAKeucfo5OBH0H8LfcUTQH1W0byBvGJR2oi4Vcarhvt-50fH-9Xb-GWPqQH2__9Qfb_Ng6G2P7nEaJRQ3e550SvwBv1WKU0mcfku5Rdd4WQhgtI-198ThjK_gSNvJeoO_RLCgwWABk1OHvasC_SnhaYdr556GeYMXvr9slInfmkRsHGzwmTuZYhA52v4J1_iepDNJxOKy6-cocH0gCzFYPbXLrEuu905oDBq7ThqFRVQnjDAEqh0w06RDkDfF-q1cGBrbshdOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با همتای انگلیسی گفت‌وگو کرد
🔹
وزیر خارجهٔ ایران با میلیبند، وزیر خارجهٔ انگلیس در خصوص موضوعات دوجانبه و آخرین تحولات منطقه‌ای و بین‌المللی به‌صورت تلفنی گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453732" target="_blank">📅 17:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d276028d.mp4?token=kvke8fK7CK_vn5h0eteB33A3AHC_CtMoF5IIrZRjcQexraqcWeYt44ElWCVV7QarOm5owESCE8d0ekrQ1P-CS83lGlq8iJ1DF71QARa5Y2-ONixSI8_jdMAKUVO3ifWFfE1psb-F4ZPVgOGUra1cgn7wB46arl5pfTRVRjsFRfKB8NKJe5M9E8H7PbPsQWYKndpk6b5mddr-RgJO9co9mheJ7WFqKxsNU2lRnoh4Bj-iddqZIgGyrbD91d1Wcv0sSfibmr_eebIvwkhsoJZmAhzbUP2zo6D9sf_YK9FC_5MvhRZ5T1dxcvfuuXReBPAhOSDSFycUp5k1kiX5auezaoQBm5WbrVWIx5Jx7GUQc6lrWmbWu2j9qjFpKCmkoYhfFcQaMziEjHbf3tOxHlcMa0PnXQ0dK04YIyweiSk0R4NFOm-n-RSD1xgdY0cVHOx5zm_pQjnP0vDjqm9WR-VUhMjgDn_yWGDLMGmp8COJw94A2yZ80hZkr5amt4Bcs_gIk4TQCEm3NL6aPEoI54wpq4khauzNyGBJ-CyWVcWJkSLlgeQQ13jTNPXlq4SrqeW82tzXMG_LrzhFSy61AI0rU-9BVuizxjK-_92vCMb-K1R_61LFbbLEvKYSmo8P3PgM4ukY1MZowWOG-0NY8_JY61UgdOG3F8pinWVG2wIFmVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d276028d.mp4?token=kvke8fK7CK_vn5h0eteB33A3AHC_CtMoF5IIrZRjcQexraqcWeYt44ElWCVV7QarOm5owESCE8d0ekrQ1P-CS83lGlq8iJ1DF71QARa5Y2-ONixSI8_jdMAKUVO3ifWFfE1psb-F4ZPVgOGUra1cgn7wB46arl5pfTRVRjsFRfKB8NKJe5M9E8H7PbPsQWYKndpk6b5mddr-RgJO9co9mheJ7WFqKxsNU2lRnoh4Bj-iddqZIgGyrbD91d1Wcv0sSfibmr_eebIvwkhsoJZmAhzbUP2zo6D9sf_YK9FC_5MvhRZ5T1dxcvfuuXReBPAhOSDSFycUp5k1kiX5auezaoQBm5WbrVWIx5Jx7GUQc6lrWmbWu2j9qjFpKCmkoYhfFcQaMziEjHbf3tOxHlcMa0PnXQ0dK04YIyweiSk0R4NFOm-n-RSD1xgdY0cVHOx5zm_pQjnP0vDjqm9WR-VUhMjgDn_yWGDLMGmp8COJw94A2yZ80hZkr5amt4Bcs_gIk4TQCEm3NL6aPEoI54wpq4khauzNyGBJ-CyWVcWJkSLlgeQQ13jTNPXlq4SrqeW82tzXMG_LrzhFSy61AI0rU-9BVuizxjK-_92vCMb-K1R_61LFbbLEvKYSmo8P3PgM4ukY1MZowWOG-0NY8_JY61UgdOG3F8pinWVG2wIFmVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدبشیر حسینی: آمریکا با ترور رهبری، پدر ایرانی‌ها را به‌شهادت رسانده و ما با آمریکایی‌ها پدرکشتگی داریم.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/453731" target="_blank">📅 17:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5cde0fb8.mp4?token=BWNSN1VxhLMGyBLf2o_eTKPJONePDEMBWxNDNgyhYhMFqEpCVt6NRbxMjjYrzdqhkAmCL3hGg47W0CkXkaokI2lRIU0Xujt8ssN3RSm-TigBUnba1QR2jIvhvhmKsHmcyxXtlfgR-83Ns_alk-S0s6AUH43ZswRqB0832uNklwsZmaVoll0rOHt9pcj0YqqwbbEqsuM5VXd7DW3fS8V85rnWAuk3F1pM74kLByoBO8LJpQrSrgRPTeIhPli_gtGP2s9n84kUywlgYOPhATMnkZd-v9k54yuVIUaWt8HHi5XnDn0HC94JlEdnawkpnESCVoxvatkr85CzM5xM9cz7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5cde0fb8.mp4?token=BWNSN1VxhLMGyBLf2o_eTKPJONePDEMBWxNDNgyhYhMFqEpCVt6NRbxMjjYrzdqhkAmCL3hGg47W0CkXkaokI2lRIU0Xujt8ssN3RSm-TigBUnba1QR2jIvhvhmKsHmcyxXtlfgR-83Ns_alk-S0s6AUH43ZswRqB0832uNklwsZmaVoll0rOHt9pcj0YqqwbbEqsuM5VXd7DW3fS8V85rnWAuk3F1pM74kLByoBO8LJpQrSrgRPTeIhPli_gtGP2s9n84kUywlgYOPhATMnkZd-v9k54yuVIUaWt8HHi5XnDn0HC94JlEdnawkpnESCVoxvatkr85CzM5xM9cz7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: هرچه جنگ با ایران طولانی‌تر شود، موقعیت آمریکا ضعیف‌تر می‌شود
🔹
استاد علوم سیاسی دانشگاه شیکاگو، با انتقاد از اینکه ترامپ چند فرصت پایان جنگ با ایران را از دست داد، گفت: ادامهٔ این جنگ موضع چانه‌زنی آمریکا را تضعیف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453730" target="_blank">📅 17:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3qJRG7ZKZQ_RYbqPFQAd41Szp3gBK_xiNiyaAxCJvdoX8MtoQNx4QFl4ToKyPfBg1TECLufomDhPqksvv1f2yXlpMaTu2dtHEDzVF-yEQkh_cvceRAB0BDhwgKCerLv6j7tD6XSOtUbqhg7Nm8yFN9Pw2YH9G_udurafwYhM-yki9v3r-y5r2ERPWQNTul9YGQjDnykdcOIsWabShtFX_JJUMldsDHywQPilia8kw2AvIzjwIhUcAvsS0mkgGLfe40hQ_sO89J0oDi9BWkojutE-_5eM-j8s4dqS_iAvNHzIOME232q2nAjVIVL5TAJenzqHGLFUSdw7aCXQe46hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
به‌دلیل اقدامات تجاوزکارانهٔ آمریکا، تنگهٔ هرمز همچنان بسته است!
🔹
نهاد مدیریت آبراه خلیج فارس: به‌علت تداوم اقدامات تجاوزکارانهٔ نیروهای نظامی ایالات متحده در منطقه، تردد از تنگهٔ هرمز امکان‌پذیر نیست. به‌محض برقراری ثبات و آرامش، کلیهٔ درخواست‌ها براساس ترتیب و زمان‌بندی بررسی و مجوزها به‌مرور صادر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453729" target="_blank">📅 16:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyaip3YLBWKee6IO3YCkMX0JP6Prxww1BMNginC7aZWADBY_XUAHwM1_3TlFuQgYDVoSkiAM1QMWuHMj58DPORmz89EY3nOvEHZ6XYHpcrbJSB5N62DK4M3qJvssOqcxtLgXbXmzfsrLxn5sjd-NqKzNyDUE-kaNq_s8WFSuakC50Rk1IiPOh8StqprGkhJ-i6aMCmN2e3GhLxhEMdJrSGdoLrVeZBZsimV_4hYWS3wIiWlXem1YSfxX-qgZciOd9L6bQxUkoI2PAhz28DWJV3PRqZUROel16aqW7PbL3JfsxGSUJypfHOExbixsheTQ2JqKHWLDWvkbB-1kJ-qhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دل‌نوشتۀ معاون ارتش برای قهرمان ایرانی سوخو ۲۴
🔹
امیر سرتیپ علیرضا شیخ، معاون اجرایی ارتش ایران، با انتشار یادداشتی در رثای سرتیپ خلبان شهید مجید کاظمی نوشته: اسطوره‌ها ساخته نمی‌شوند بلکه در بزنگاه‌های تاریخی یک سرزمین، از دل حوادث، متولد می‌شوند.
🔹
ادای احترام می‌کنم به تجلی واژه مردانگی، شجاعت و غیرت در شولای قهرمانی بر قامت خلبان شهید مجید کاظمی و ۳ هم‌رزم ایشان در خلق حماسه ۱۱ اسفند ۱۴۰۴ منعکس شد.
🔹
خلبان شهید مجید کاظمی از نخبگان پروازی نیروی هوایی ارتش بود که نامش را  تا همیشه بر نیزه افتخار این خاک حک کرد.
🔹
او می‌دانست هرچه بیشتر اوج بگیرد حلقه محاصره موشک‌ها و چشمان بی‌خواب پهپادها، مسیر او را چون خط سرنوشت خواهند خواند اما با چشمان باز به حلقه دشمن زد و هواپیما را چون اسبی تیزتک، در دل اژدهای فناوری فرو برد و نام سرباز ایرانی را بار دیگر به رخ جهانیان کشید.
🔹
این حماسه زمزمه مادران این مرزوبوم خواهد بود در گوش نسل آینده، با ترنم این اشعار بلند تمدن کهن ایران:
به پاس هر وجب خاکی از این ملک، چه بسیار است آن سرها که رفته!
زمستی بر سر هر قطعه زین خاک، خدا داند چه افسرها که رفته!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453728" target="_blank">📅 16:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM3L88ObyH5Nt2BUYNn22nC8TlCHRnY90dDa1VmIudQOOpvj1FX5wTVLZjuL4XXJbvkSKzZtIxySMKdrr9KnJoTV7Cj1k3dS3mB9Pc2CY5WihlkjIBQICsruSqdO-aPiFUr6rrsnk-_aaixPXKQ7fttvdzgQh90dIlYNWskXzQkcXB4TIUeG-bXDrCXkIKAnOmOFmk1O_6nylEisamm8yk9llmkGU5BDEGdFdemjfzGCuM2TZwkf9LKr5fyA-I___ArPNn_5jULx810A3iOcw2eUmO8s8M7tLGonwidzE1gNUXsq1EjY_JvvZ2HhQ5PWvwD7jKe1pNAjOuNZVWgEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاتز، وزیر جنگ اسرائیل: اگر ترامپ از ما بخواهد، به جنگ علیه ایران خواهیم پیوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453727" target="_blank">📅 16:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453720">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0FrinV6-m8U0RLIxCx77BPYF8Bo9osugrmkIGleTnXAnJ_F3zYr2rytwuo-rTouFn1XR3luQ9Adaq9Cd9NonZlupRqtUxXDHzDLnd7Pjyg3tbZ2MFpwh86cLywtR7-47MRqTQP4qGn_U2H123gpM2_rcVGhhrK_EVceZIzajIJojidFubACGeSV-lD47GLIRmW-r6faSOtjNUCPRdwhdbpsVxZ2NuejLDValE__Hpk6AeFHPi7ynMPV80LIYqaDSbBge3wiGAbYUZJTCa0SCqq2NkZZBX-vAykNvL0GQVwQOckVITj2Vu84OYRslqvmguTySIIpqXLVsgScF3Lsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hj4pDJ3uuvCaBLHb7kQiy2xxdIwDUsp2pERwLxXZ1haFBFyLhvNtDfb8NnQGdk80AVmNJVhhuz4tD-oLL7wNoAP8mFtK0rn_RekhqEqDKDjCijr2ii_iaww3MtnX4oaz18foWakEjwiN2jF9aODHNLEmcK2JoqaPACewJVj62DyyPsiRPdqMMPowqOqoBwJr_ymK8f6YyxyDjIq37jow_lZuNHrg3hOsk2c5eIO2TXc4TmsHAfN_IHLi0qm4iZSY8RQ9IxMpXKEi7TegbUjRnNcdFg9JEMNSOyp893NeH9ywr14LXF18tsq_P6KnHpddr1D711rSIx1E3oJK8klbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0ubDXNvmsTt57oe6AwLptDSC5lmn7sRHXCMaI5d8P3ORfJiyAjAun2VGm0fbHTe2CcpZLgaO0xdQ06fwg8gRBV-Is4DlfmNGcrqbLTLcNjk9wFmyy_mEnhLO4cg0nxjnsA1to73KAOo7xKLp-oNOK9fOi0PTw27Urbzgjd8JAf7MYxrF_knfGQM6koZZB2j6rZ1_d3wrskJ0EudG3PEWSZD9yPfeJU8OhQ3NNKQg2fJqCUmv6nuI8AzroT15-yX95UPqEVdimwdXsChCt5sXWDxPea6UHhfKF-M_Ere5Yj8NPI1fCFkdiyYs-hORZdEDuF0crH55Kd_qUqVtx0jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpCzjnOZwoOTW1VcIO_iokfEEzgcH4eKxjPGgLDkslZG-2_5UlMpw9jetgi7Y0kIm464oDFqVosokARvyCpQPr-ZPa80EHu2IGfnXcnuhfEg78THoIk-_83qV9rCBqtTyq_Dcp3YNi-iBe5vZj4Ml_s1izEewsL5t7Evl8d5i6GPmbGCiCxkdZMAp52k9z_6iD7RSNpUhcVdKvSxfXhFilnhDcTpeFQEk-Ff5b3Z2GaPSgmEAwTgJTjiRJ2BK6gYaYcJ39kHdjtDhWTzCPZfq8KOKdFg78UCjcx3I0ZT4__eI7tBynadTm-NSeSAhnMrkOiv1NurMdtjn8pxT8gVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxdWkMj-XZwYKNmbBb7zlbPXSQHN37iPmTevNRKc1daEzYmTvAuE6ynyIWZKqvLMWKjV6d0xfKC0kiRCEg7cVNA36RVvFNP6rGmNKhZ7ca8z8K4YlVtPQaBUnjlTs7-cFdvV-DFKI6mHjwTtbxYIU6EvwexYyQfkA0m3hq3xuO03pLeWfT7dYQcXl4pJ60oW6ua5xWhuLO-GZaMplP3r8MS_hUroUhyezEgWkBuoUUNlRTYvW7a2-V43xDOq0sVS3A9oQa6lN1d4h6ShF2oZ_w0_02WDdXUm5NHzGvhzCWU8ybJWQ8Nw59AiB4XuFVWa3WPxu0oucJvpZkLJclBWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oyx31_n2wszL5vxxHONRD-4qkk9EjdeFaBaZqLZmIkf4d776lMBBVzyDoD9aXnv2_Nd1SnG0T-Mi_dlO7YVaD8K38JQCJ9NQcppftaDKL1xbMOZsAvAC_u99w6TImcexKqviD9bPXR0jztS2VyKHvp9Ls93qAPgDdESTC_f0L9pK1CONs0_GDjiEfz9zJ7FzWP0zF6cik9mPBRC0Jj3fRaUxJFiYv810MCMrnu4EcJnCYJHGdiEfs3e_uPn_-UXC9QUY5xW6ZwmszBs4TNuZPtz3SEMXcLBuwazrITj4ezjZFp8depPb45QA6b6cd_TKr_aljN531n6umznQ8tF8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwm-2r0LdXqqNGYiyHq1tjTF1cIoWnuq_LJKjlGN6EmwOqDx2F1Obs5ACUKE5q2ZFg9PGQbDYJLJwLADOYEKUOT4qAZyyctHPzxTo3iJl_EhULNAEN6N0psKvbQdFOtJL-fMqI9pXNsRts2wuylDzgb1DBSmcgPU1L9OSBcWc6tNgf7v2XRypGEjFUDerL4MJ9SdAPKf1BAgL9_q4ySoU0huP17c6EI6ZZDUemPo_l-_zaYzi00StcqsD6I0fMh_XbV0IKNzf-UGLvYTTQO1sqjRVbd1zOoPi2WIe8GoHxdaFUdVGZyFvOPYY_U3QmlgcYczzrL9eiIlT4maO3ufXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد زائران اربعین از مرز خسروی-منذریه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453720" target="_blank">📅 15:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453719">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqh2_vfo1Sf8GO2atxCW1uaeRtsrDyJeZJbW36v3e1PTU5P9LfZK84jTaQsOITRYvkwiQD100WNfPfc3bd2YJJRcNa8mUjrHF81hotBewLkZ9vnsmL6cZBA7BUQ77O5qLG9DMcQLm5nQVjuhraBKNHvMs4NfhhotMO1P_Wr2Mjoiky8cPkQZd24xBPKOAH-Tdfp_CWPwfxpXGEIw44NbSzQ3XWG8TLxtcSouR0RI3TM5vySTyvWpQ4iu1_XCt3ej2p21435ikh9E9v6T08Yvrug0JX_1jy8e9Z0z_IeCj4GzeOVdWLZI25SGBpxcZWnIYQEGrRoBGioitXy43J35Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار کره شمالی به آمریکا درباره جنگ‌افروزی در ژاپن
🔹
کره شمالی امروز هشدار داد که گسترش فرماندهی نظامی آمریکا در ژاپن، خطر جنگ در شبه‌جزیره کره را افزایش می‌دهد.
🔹
خبرگزاری مرکزی کره شمالی (کِی‌سی‌ان‌اِی) در بیانیه‌ای به نقل از دولت پیونگ‌یانگ، گفت که واشنگتن، نیروهای آمریکایی مستقر در ژاپن را به «فرماندهی جنگی بالفعل» با هدف درگیری منطقه‌ای تبدیل کرده است.
🔹
کره شمالی با اشاره به اولین آزمایش موشک کروز تاماهاک با قابلیت حمله به این کشور توسط ژاپن، توضیح داد: «درگیری نظامی در شبه جزیره کره دیگر مسئله احتمال رخ دادن نیست، بلکه مسئله زمان وقوع آن است».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453719" target="_blank">📅 15:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453712">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSWQNedgq0b96oo10Bnu11LYikf5rt_fhboekNeGtDprsDLIBVcF-sdbF8f4AoAiZPplyXqso0lM-Bo_u1bicUdlH8cC_YjNyLqt_4yWN9iUhFyhIOjDHb8l0BrTR2Dab79v08MOgn0UQ9XQ5IWIse247lT5AunqKi-KlTBpmdPhGzOp3oSVKdg1ovjDv72E4h52TVkVJyw5ZvMOx184Nr7VOgQWfcHSHyQ83fCCjRwDDuN9c0KfEvXr19BRTGJTjiKjYKkZQLP5AjgtKTMQRKnLDjed2h4c1DjvT2dL2DQ6dEypQJd8hvzdY6uAhOBqGDADe50HszGxRbLSe055TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0ATSCyiwjJ0tGVXNcmT0BZxCzpUCP06-fNXzQzsY61a2aCcG2L-4dVi52xEOR91URYvtb3mWFya5yDJTnyve9k5dLd0_3ZnqeoZctzC07uzdfyNe20hbQ--W4z4wZ-eZ24fWqDtvzEeIiOuf7IxzaiXpHSR6b4vq2poEqgKdY1v5U-9ghHyP1Yc6xly8bk-DqPPrheYixfnIa4d7sYXMRrioJPtsbRiwdk8eyM1uqnDgJQsk3g02DFvSfJ2bAxXepP_4mBk6VYgsizTecjc4o0nDZAqpM9dSVYO-ld9SnIY3vQIh2I8-mszgUB5cio1a5LRddedClQLMqYgklXIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jpk5NdChYqopPFp0_mZs22f8z_rgjkuYww776ksx4o7QCHVu6e2TXRvtJNQZwpFP-VCwIAcM-_IBxFqVm7TkmaqH9hiEUMIESVCpRca0keM37N3qBydaswo0brD74wSrnhtQCGWxguSXgwGdp-5yUAoIjIr1Eg69OnjBb7nmAfq5JHwvZgfpmyk8LKShfiYNYRkhWEYvYjBgYw_8q0wkv6azZWBBt5XBS43gQp9VYuB2QUxzmk_8Y1TMW4g-RIkRV8EFbQth07wN74Zp0EEEejfvTqUM_1b8CYUxZwBm6nH6irssaWijgdobHMlcmKZ1ZKF9hNxBWLnOHnK5P_6uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/If-NZ4wZONhbSchv27jaKb9YkQCS2h5eDI5f8hcZJHc_n8y3u2gHK9djfUsVzqzshfrdw2BkksaGfnYNVOdKgMk4HmNTEk-cQAZeLUnXX4oqsQRBK0AxVay_YFQdLNQN2Xi7DF3ko3SmSu4U1aHcPV-Ckwge-c5QBQIlmvIYrw8m-ex_1T1MHstVwR7gCQZinmLpCRkybzEQy-uSuYKUNfRvnTXEUHClLgY75VEvH9v42-Tk1X6wisukGBjBy2BC2S4YUEtr4Z87Gre9Yppwf2iwbaY2WPVlmNTpw91y_niINbKuLnIDIydXeI3OK_7FJGyLB1C1QvR_yF_7_dxE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caiRFPaNVbaUs9DtVH0hSR-OzJth6KZT9orje89WVBBR9ypYCJF2wQCwiU-PJCJ_DcMlnh8Zth5YaiHrr09rL7iNunxbNY_pkKXPuA0l-87ptrRbNPLBoq0U9ofDDHNCsPiIhnC1Kb8i0faVI_UW6QnBQBkWfL_An6xxNb6_aQ8ltcIypaIfs8-laPq9IRE7QuEJmQzAP2dFWBXJjGnsKH2vkeRL5o2Cc3xQs1oyTblnqQWHcxQrdcTSHiJ9kpD0RGGWFNGQGvUlyaYU_YePysT0Tzod36Fp-LTDnfjAdEKXHRhTxZsX3pE5eu40TVAfyDjguYYvcwf0BkNhupq-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjBTiJuQkpfYLVF7vSzdB62hP_0d8mEj_ghJbvNwrjE578hbUTRLmTtbgizO5jiJIsL8vNnkzj3sJB_cEIAqvvASdj3CzGjVUro2MNdtLsabA2JL6UQua8AtdiARNB4f9QwtSxUukGFU1pW380IF3TNig7ssTLQkfV_mdfuVcrLw4Rp1d6Z-MaTE6QHSXDL2dOkaXBNRjaySa4YOEDbBW0iKRgvRjsuaITHja9I4kIGkSWTBN86rvEMxuvbf_AO3ZIBEKjzbEckBPjbBmkD11TeIkz9nNfHDlOpnlm9jMfL6vrIAku1CFnv3VYJ2aaPVaHfx7HboLxgK-SyjyXCX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm6L0UD6RVD5Qb6x-_Eg3VbP4ngYvyhhxFl5q_GeuwgIphreM3z57biiCLd95TeDTK-RDjWlILGNwQwyc1jG7_R9yHmT--3MRxJcOXW_9dF0QeZ5V78E9Ajg45XJDqJfPqQRK0zFRHI5XzgFhu3vj1crbWujIQdXUEJZn7Fa4nP-Pvp1Gxf0vflScwypVMwPShGDikChZqAkiRs6FNNOy6wV_jJtqa-hioLlxX0e8O9pEQUHEuiGR9qN8hjYzPj1Uv6fmqtybcZFkITV7Kkw2XnXN2Su2dxD_dPDk4kW1lFiQq4YmXKqbAGwUs4pskXEGWTdTMNKsm9sT8is5SNdnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیوند موکب‌های مشایه و تجمعات شبانه ایرانی‌ها در مسیر اربعین
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453712" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453711">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8NjwTbWQFpDwHrK7BfjdvE-EfduJS2yZwC3FL4RIcMplrlFc-Bnh1nqln27He1AX7FGAuXcj0zAOvq_5B6RLpZCEfSd_eGMZ79-Np1fndHGTJk2qtyOY6LogNe7aUyewmzI_MV2n4m3_BQBEv9OzRolhvl0x0lY3jrBfXifwzLJA8srSVFwiDkMoHNUFOGhOjppSvHXuU1lh99QaF5U8aFxqRyfCD4GzQMulrhkVor5c-blW_H1h-ebZUt_DQkOgslLRkfEBsd9X6FVHlM9e7LbZAcepipG6ULW_9kPcSut6LPVRBfH78JpJY_iCl0Dw8avw8KBLx2ecA64PJ3cmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایدۀ «محاصره زمینی ایران» خبرنگار اسرائیلی را هم به تمسخر واداشت
🔹
باراک راوید، خبرنگار اسرائیلی آکسیوس در واکنش به گزارش‌های ادعایی دربارۀ بررسی امکان محاصرۀ زمینی ایران نوشته:
🔹
«آیا کسی پیش از آن‌که همه رسانه‌های خبری اسرائیل اعلان‌های فوری درباره اینکه اسرائیل و آمریکا درحال بررسی اعمال محاصره زمینی علیه ایران هستند را منتشر کنند، زحمت کشید نگاهی به نقشه بیندازد یا حتی یک لحظه از عقلش استفاده کند؟».
🔸
پیش‌از این  مک‌فارلند، ژنرال سه‌ستاره بازنشسته آمریکایی در واکنش به این خبر، محاصره زمینی ایران را غیرممکن توصیف کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453711" target="_blank">📅 15:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453710">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-gL92pU1GrKH-0ATM6rQ8lkOOW3ZjifMFYrBICaX2PpHLispqngbVwBMHskx3faG1eztwX3NXHqKFrjbDAKb4X2kcyyAK5tg71yTit87qvOhYzcdJsQFzkjBk3E3W_STi4JyfHeKpRA291vxAzTVh1Lh_tKzbxfW-zG85EI_YFFpVRpKBmZ8fDA-b2XFAKjlDKHnzMJp7t_7eMp71K9DUfgtEYP3xakrgbkuV7_wvStiqJMhOyD-xevDntISkXeBptz5E8YSWaFkK_ykZ2nhrO-rSwKJ03DoBanzPZaBJPRYxUbpBn6ONeSNWejEp24KFI78L4ZNCOzwC_hlb_D6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ارزان‌تر چت‌جی‌پی‌تی از راه رسید
🔹
اپن‌ای‌آی در واکنش به افزایش حساسیت شرکت‌ها نسبت به هزینه‌های استفاده از هوش مصنوعی، قیمت مدل‌های کوچک و میان‌رده خود را به‌طور قابل توجهی کاهش داد؛ اقدامی که می‌تواند رقابت بر سر ارائه مدل‌های ارزان‌تر را در بازار هوش مصنوعی وارد مرحله تازه‌ای کند.
🔹
بر اساس قیمت‌گذاری جدید، هزینه استفاده از مدل جی‌پی‌تی ۵.۶ لونا تا ۸۰ درصد کاهش یافته و قیمت مدل ترا نیز حدود ۲۰ درصد پایین آمده است. در مقابل، اپن‌ای‌آی تغییری در قیمت مدل پرچم‌دار سول ایجاد نکرده است. اکنون هزینه پردازش یک میلیون توکن ورودی در مدل لونا از یک دلار به ۲۰ سنت رسیده و هزینه‌های خروجی نیز کاهش یافته است.
🔹
اپن‌ای‌آی اعلام کرده است که بهبود بهره‌وری در مدل جی‌پی‌تی ۵.۶ و بهینه‌سازی زیرساخت‌های پردازشی، امکان کاهش قیمت‌ها را فراهم کرده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453710" target="_blank">📅 15:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSDOeMhtkShOjPMTnvTg20sSA6n6fvEIksLqVrqTdGrS2KrHVIKB1bqfAknhSbpon5azIB_Q2ir79dDnLstTmaHHUG4uqm3It4IrSfXN2OWLYmW1tchAqPRsLCY4kU1PCoVuxE0pzkH5yyixRKYRi5FiKBGcMK0dZUMNBk-y58UsHQm12ZREY4h-2VmBKKNw5PrU2CVImpqd5DbW5ZtMXrGMYNAYIRnaw8fXOWST0QVWsobwdEwK3oUH2qkricusqv_0Pmo1G009Z-XYYtctqc5j59jJ7R4Tm-CuUuAENj09LEQQPqYRxiz85Z2QQ13rpIz9qt3_ymCcUmIeiVeRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFi2Qujs70QTenRvEWHet7I8Lc1jwDuZ-RVxDP10XLKRYEaDXyEon6HXGSe9KwLDv8V-xBAkCYWKWlGcUo4FPrRoPF5-GB0xyisarmxLdh4AG_odrRywCN2va4BXNtAGrNrSe9hQLdQ8_Tp_-T4dkIuEg4EeNzJkIeQzzapJAEiAiZ8LvxGw-E92KlXH1n5x48Th5bnFVFM7fGgX_XzQqTSmNn4Gc9LAqAwYUk8SNzJYFaVP0A-VQE2qujh5rKoRCJcSFqZpDeFyHlv0voyMU0rRc7bs_OYmmTO4A89T0je1jNg6_nJgdvq9uzrJSh5sb-co8u--XSBtJzX02JYGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbFrDyP8Y0MmIscAJDuEMGeiKRFTlrP8SLrz_wyqbwW-iIpvT4Ir2DAlUlqxcX5pOor5-1Q0zQD_G8Bc42lEv8UG-6yP8-CZ67eZ3EdGPVm5JdU8TbFCNSaJB60gq1IRITvu6p6lkh7BMJmFD6ehwPD7NZ96mD7j7sZtFas9iz-F7B8SrHBbN0CGzw9aP6dqnSQoTJqVmGRH6OHOMoSgzaWB7Jp_hBhcaMSpXku5vVOK3HBTV0-2X_kNNURtXW8s090PQfYWPuHN1aoS-sbbC1t5DzmkXUNtnEXw6BObLHTXhPa-908rwx6MrO56FRbe1dmFJHmbvCQZgyHHj2_4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6NJe6PQAKHPTC0x4RuGnWtbhREp2DmQoGSsUtsc6M0-R94GS_L1sfH9C1BnELq3qo6npUyTuFuYubCKSSXw2Sxj9yGAWDP8QxYOBiujE1eIzt-6kBZQI1xkuvqYueSVoC6IbR9ZI2jnX2Tbn7v5FrMZSlwDbOTfarZIjoHwfkMgMv7kTn3dgzpWDof_neGdAPjtCC1t2au6Gun7m-6PABO-h153u4853B8prrR5qPWZy13BjEvDqGgi2jkQJOVbmo_oXQOBwyf1KFdIhPmem4AaQtgFP1cyeo5ktejg9FOuGWqJWtrm7rJGd1CzHcn-C_DR2rUlFG-mLCREHo0dyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uj2cE6kG_KY4H1qA5aI_FxIWyMuuIU3yKEbIb0EOyPZkBBJsZEQsiNh7yXJm8SmLTm5cBWNlN-0WgndhS5Cj9QdenJSAwDDiq5T4A1cpthXBUnDU8VztProbokxfRIYGASffNxdbdPL4qjnYIZJQb0qF86TaQeKJ7SJNDG0xD3RO9su550k5apqYp7744wZmFCPJf392KcRgBjcwV3Vy2QnakDkAe4r-CC0P77E-A6OfdPoFe1Ih_VJKjhhvVhmdGWR1m6yEDZq4523UNHuZSytoGXdKdFGk3L7GDUyJC6AlRUGN2xhtKgJpuwQcrupobK-D7Ti9kQcN_UMljh6fcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-CtyO3TnXv0qsr20qMGXrUaURHy4f8HL2ChS0PoLUzySFh0tVC_2t-k_LT73yW0AcIKuGY1HaqHlylZg1qytMMGds54huEcwGWYhZkw5g8WAUBpcCyWti36ZdRwm9OIa3cC9DzBdCy2Ev4D-74TJKxfpccfTCP1qU-9EojCw0F-IwMxotIw5UCfvLFij9y2Ie_JilR9d_gWSz_LzdKA-1zKnDQpbQbJyijD2hHzilj26NxxVv140OsrMV8uQnLPJI_QxNhD1gsyhv1k_3w2e0TKRCuqk3rKz047Q85eiFF2P3HvJIwKryVC29Yj-fZyHdFA5Hw03fOcNF0sgjkbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPV5PkbEwImckttG2fHQFuwfXKg9lq9JUIOxUQaBTdsN7IsQVzRGGyIhzUFfUWkIpDTnLe3RwrsgoRf-wUinrg4yXZ3E8zFvMcQ_LgnpBpa36ESv8RmylljttMdLDbKUrdVlG_txQ-3bSDZl12JvE70xojk_FQfhPp3WlNNFs3zbHT9b--ZENfM8Yi17BfATxKLy_iAP6L9F1YJQY56J4zCH1iNj8YIp1QvEP9DMAf8uqacfx_3OmB5955qypAelJL7DRb2i7Q0bhx-XDuc67WNOEaLzorTgvyHItxmQkw4jtJe2AgJPDt1TagCy56h28rYZAvOuyddtAQOZw_L5Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع ۳ شهید در زنجان
🔹
پیکر پاک ۳ شهید که در حملۀ ۸ مرداد دشمن آمریکایی به شهادت رسیده بودند امروز بر دستان مردم زنجان تشییع شد.
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453703" target="_blank">📅 15:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247bdfee34.mp4?token=HV9bCfYqugtNQXlnmYq14i9oXlWs7JVoqBEh2vo4CurozFkx2Zp79ygAM0NWKqUsSR2mzOtdgxV-3uzvKbyLtzEYsrC2-20ZpNFCzmNwA76cFwyMi22oY0Bcmrog5Y2SZcT0GECNW7ETQQnf2zcGEnQni6A-2X2lNCAevb58CfaRCSSvcrrgR380UJqntR3DLEIiAqJp5mQeyGVYYvouMgl0rcF76KLAAR4qeKrrGybM1gfbh3ExcnZcptZ6qyOxTMH9hhljgo5aaEJT5-WoU7ENqspKuElqews7RCcQNPvbIO_KvmF94mmzHuW-EXbmnoBwyJ_WhlDDBTBu2KumhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247bdfee34.mp4?token=HV9bCfYqugtNQXlnmYq14i9oXlWs7JVoqBEh2vo4CurozFkx2Zp79ygAM0NWKqUsSR2mzOtdgxV-3uzvKbyLtzEYsrC2-20ZpNFCzmNwA76cFwyMi22oY0Bcmrog5Y2SZcT0GECNW7ETQQnf2zcGEnQni6A-2X2lNCAevb58CfaRCSSvcrrgR380UJqntR3DLEIiAqJp5mQeyGVYYvouMgl0rcF76KLAAR4qeKrrGybM1gfbh3ExcnZcptZ6qyOxTMH9hhljgo5aaEJT5-WoU7ENqspKuElqews7RCcQNPvbIO_KvmF94mmzHuW-EXbmnoBwyJ_WhlDDBTBu2KumhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرگ ۱۸ نفر درپی هجوم مهاجران از مراکش به قلمروی اسپانیا
🔹
دست‌کم ۱۸ مهاجر در جریان تلاش هزاران‌نفری برای ورود از کشور مراکش به سَبته، شهر خودمختار در جنوب اسپانیا، جان خود را از دست دادند.
🔸
اسپانیا یکی از اصلی‌ترین مسیرهای ورود مهاجران به اروپاست؛ آن‌ها برای رسیدن به سبته، معمولاً از شهر فنیدق در مراکش شنا می‌کنند و با پیمودن حدود ۵ کیلومتر خود را به قلمرو اسپانیا می‌رسانند.
🔹
قرار است پدرو سانچز، نخست‌وزیر اسپانیا، امروز به همراه وزیر کشوش به سبته سفر کند تا اوضاع را از نزدیک بررسی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453702" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
مراکز راهبردی آمریکا در کویت هدف پهپادهای ارتش قرار گرفت
🔹
ارتش: در بیست‌وهفتمین مرحله از عملیات صاعقه و در پاسخ به تجاوزات اخیر ارتش تروریستی آمریکا به کشورمان و حملۀ وحشیانه به منزل مسکونی در جزیرۀ قشم، ساعاتی قبل، آشیانۀ جنگنده‌ها، سامانه‌های ارتباطات…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453701" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453700">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLfwo-jwBCWh6uUPJwztPHud0ENw1Xxc9VAKYyERuulcsYdxtOCFlRvPwrHQtqNsbei5tTQHB7ETnCzwIo_NMNQkbGSSuG7PUubS9xHE02Shm11wNBSVKIVjGCYH6VETUMzZmrGSu8GGKT2KuBORJazU5YBqrRegpgkswZAnrotTAyV3rShonXXMSUVw-tgK0D9U1_7HnF_Z2JsyO-nheoNUCiXdPCM0cD1BbAy_fxZ33wpFrTcmaVqoz07ENAfwoZXPr26tVxJFBqnGUmpsDWXSlpSI2F5NHyTbZWBmjQ1TpfKqOOkU-uv2v4uVIzQuiP8-l7CkwiY53C_Y3zyH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حماس: فقط به شرط عقب‌نشینی اسرائیل  سلاح خود را تحویل می‌دهیم
🔹
درحالی‌که ترامپ مدعی شده حماس و سایر گروه‌های فلسطینی با «خلع سلاح کامل» موافقت کرده‌اند، غازی حمد، از مقامات ارشد حماس در گفت‌وگو با رویترز گفته حماس تنها در صورتی حاضر به تحویل سلاح‌های خود می‌شود که اول اسرائیل به تعهداتش عمل کند.
🔹
به گفته او اسرائیل بایدکه حملات خود به غزه را پایان دهد، نیروهای خود را به مواضعی که تا پیش از ماه اکتبر در آن قرار داشتند، بازگرداند و همچنین جریان کالاها و کمک‌های وارداتی به این منطقه را افزایش دهد
🔸
حماس درحالی خواستار پایبندی اسرائیل به تعهداتش شده  که دیروز، یک مقام اسرائیلی گفت که این رژیم تا پیش از خلع سلاح حماس و غیرنظامی‌سازی نوار غزه با عقب‌نشینی به پشت «خط زرد»، موافقت نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453700" target="_blank">📅 14:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_9OBV4TZsxR2M7IQxxRIEYYWfTXZ70vS_vigGk0gwLYdU3kJehwnLkUUyVFo2SP0PriTzH1WZVEdHJe6t1vTuE2WIwlV7yg739uF8uAzZpuE6g0OByKxyi7u6Mj2etqXr6-vcoO6YlXGS2QlbAMcHN33KpMQmZ0blwRsiSNh5zdAyNkt3YVeqW3uvYimFcyAaqhux_pZ7-ax5r-84UWWE-44fD8NeqePEByyP50VAi64EZzYhU4GMizzgRhUfWh_2MYT32aETKkS9flRwliwkHJIIGTsDOTrYxVe-Z_Br-rxvfNA79U63ZxJZZjiIgKcZCpzoSvsMwnD-IZ2WuqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعه تهران: حملات موفق ایران نشانۀ این است که ابتکار عمل در دست ماست
🔹
ابوترابی‌فرد: عملیات‌های موفق نظامی و  اقدامات پیش‌دستانه برای برهم زدن آرایش نظامی گواه روشنی بر این حقیقت است که امروز ابتکار عمل در دستان توانای ایرانیان و هم‌پیمانان آنان قرار دارد.
🔹
آمریکا دیگر بازیگر اصلی منطقه نیست و نمی‌تواند بدون دریافت پاسخ مناسب، دست به ماجراجویی بزند.
🔹
غیرت مردمان جنوب بخشی ماندگار از حافظه تاریخی ملت ایران است؛ امروز که دشمن استان‌های جنوبی ایران را هدف حملات ناجوانمردانه قرار داده بازهم شاهد ایثار مردمی هستیم که همیشۀ تاریخ پیشانی مقاومت ایران بوده‌اند.
🔹
باید با همبستگی دستاوردهای خود را تقویت کنیم؛ نقشه راه اصلی دشمن تمرکز بر کاهش سرمایه‌ی اجتماعی، با اختلافات سیاسی و کاهش اعتماد مردم به مسئولین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453699" target="_blank">📅 13:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np2gC3EA5vqnm96MOO8q9nrZXVWb99Z8g5dSLq6-R-cRb2l5JFxCD_Dj9KFH2OurccUQrR36kEe_mFGvk1dXOu6J0quE1MqcYGnQCDyqDte9Txgl33ciB4uYZATCYVmIZ2xDXLewBZelU5h14-h9gUXlCJVkKXQihGv45msn2xfSCilL2DXowXnSRf4rJXQ0LSUvX24nUycz5VkdTNc8qTxD8fJ2GlhVk1nFjt0tSwRD_FQhd-aQSEEwbqhqEAkjEimm2yxdEohFMmLFbXOd7iKqCUcv6qMXqUoPGYyGGuA2ymYbLr37CU5QaPwiRmS2EPLrteQiWEPWDPbdh_Oiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر مجبور به دلالی گاز شد
🔹
قطر به‌عنوان یکی از بزرگ‌ترین تولیدکنندگان گاز جهان، برای تامین قراردادهای فروش گاز خود مجبور به خرید گاز شده است.
🔹
دولت قطر ۳۳ محموله ال‌ان‎جی خریداری کرده تا آن را به مشتریان خود تحویل دهد.
🔸
این اقدام درپی ان رخ داده که بزرگ‎ترین پالایشگاه گازی جهان در قطر توسط ایران هدف قرار گرفت و تنگه هرمز بسته شد.
🔹
قطر مجبور است برای فرار از جریمه قرارداد تامین ال‌ان‌جی با مشتریان خود از هر راهی این حامل انرژی را تهیه کند و با دلالی به دست مشتریان برسد.
🔹
طاهری، کارشناس انرژی می‌گوید که اگرچه دولت قطر خسارت زیادی متحمل شده  اما فرار از بن‌بست تنگه هرمز حتی با راهکار دلالی رویکرد قابل‌تاملی ازسوی قطری‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453698" target="_blank">📅 13:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴.۶ ریشتر حوالی شهر دیباج در مرز استان‌‌های سمنان و مازندران را لرزاند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453696" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usE2X2B5OJnt3QpAYbo_DQoWqeNrfZENEG3OfhhaieY0hcmVluMSIjbzeQM2kd4NrsaTK7dOXq6awh8bIyfJSyo-I_hjULXXqejmzA64UviTmB81PzJBqw0Wu3HkP3MU2oc2SbErCTuWBJh4AJJg2zNck2dWC_JG85KPe7uqMLA0TL2ij5b38qgUelvhhgFojDNvksX02tXJX0ibcHGOfYR6JuQBi9w4fcv29vVxhcYGd5udnKVgJ7E6S8Sgf3XZtgIOmxxL0Qh9-YlEL48VyssV8s1yo3gddt3KiOCDxDA3QPFV9xjc-EY0NFbQi_NyZ-izQbLhMaCmGZzyBREQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عاقبت عدم توجه به هشدارهای نیروی دریایی سپاه و حرکت به اعتماد سنتکام  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453695" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19002cccb9.mp4?token=P26p3luvnxuTz88CAlOWOCRCSotXSqqmEG83w65KH00TNnUTVJvD1wD7d0zUjY0p6BnF2CA1LjO3d1vyzUAATfinZHCjFufYvVBGs1InbOmxF6OK67DhB6T8DcfA4gy7ky-4if18snRPwS0ULPNX2iActTsagL9B4NlB5FwMMxNbpeN2Df9zXnNCbqR0Y6q3n8EG0JK-RQNaqdFhktD7bGBKa1BuvgNM5mi0VzlQl5rxB1hPC-ewBslQz0PF28S1NzKlFtJhg8_tTi_pSD674Zrkhw60-rueeH4icDD5f6c_txOGa3UDTZAW5-F6PIWhRA4t0Hh2Drcptnswcqxgig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19002cccb9.mp4?token=P26p3luvnxuTz88CAlOWOCRCSotXSqqmEG83w65KH00TNnUTVJvD1wD7d0zUjY0p6BnF2CA1LjO3d1vyzUAATfinZHCjFufYvVBGs1InbOmxF6OK67DhB6T8DcfA4gy7ky-4if18snRPwS0ULPNX2iActTsagL9B4NlB5FwMMxNbpeN2Df9zXnNCbqR0Y6q3n8EG0JK-RQNaqdFhktD7bGBKa1BuvgNM5mi0VzlQl5rxB1hPC-ewBslQz0PF28S1NzKlFtJhg8_tTi_pSD674Zrkhw60-rueeH4icDD5f6c_txOGa3UDTZAW5-F6PIWhRA4t0Hh2Drcptnswcqxgig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران: ۲ نفتکش متخلف مورد اصابت قرار گرفتند و ۴ نفتکش به سرعت برگشتند
🔹
روابط عمومی سپاه پاسداران: ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453694" target="_blank">📅 12:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سپاه پاسداران: ۲ نفتکش متخلف مورد اصابت قرار گرفتند و ۴ نفتکش به سرعت برگشتند
🔹
روابط عمومی سپاه پاسداران: ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
🔹
۴ نفتکش دیگر به سرعت تغییر مسیر داده و به محل خود بازگشتند.
🔸
شب گذشته در پاسخ به بیانیه کذب سنتکام به اطلاع همه مالکان شرکت‌های کشتیرانی و بیمه رساندیم که به اطلاعیه‌های سنتکام توجه نکنید و از کسانی که فریب خورده‌‌اند و دچار حادثه شدهاند سوال کنید.
🔹
نیروی دریایی سپاه بار دیگر اخطار می‌کند، مداخلات و امر و نهی‌های غیرقانونی ارتش کودک‌کش آمریکا به شناورها در منطقه بی‌پاسخ نخواهد ماند.
و ما النصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453693" target="_blank">📅 12:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453692">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJXEzeiCRttNtvwEv0Y8rbS07O2nfay77rzGz9tPTqAgssyMX8deHdlyRh8I-GWPut0-kwcWd42t1woY8YV84bd7qGrP7LjYK28B_wJmgVHaHiG79oefe_ME7fNqcI4N3HL5vdyO02HbEZxQFjUawwuz4APJpxiJZ8i7DVNP4lGcNgC4sjthaIv2Mkff1MI0sp-f1XGfEMpXIBg_HpyGhGAYxqfEc_gMTeOPIkUPepi5JU_odgl-r2QqkG2CCQjir8jIFsbm9oqoGazLYL_OGPMnw23MrgtAW5j8qacBfxcqOii7PP0xTiWLcChoUAmJ-SWeM9HxmHqyHguPJTaAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استراماچونی جای قلعه‌نویی می‌نشیند؟
شایعه است
🔹
روزنامه ایتالیایی توتواسپورت مدعی شده فدراسیون فوتبال ایران هفته گذشته با مدیر برنامه‌های آندره‌آ استراماچونی، سرمربی اسبق استقلال تهران تماس گرفته و پیشنهادی به ارزش سالیانه ۲.۵ میلیون یورو تا پایان جام جهانی ۲۰۳۰ برای هدایت تیم ملی ارائه کرده است.
🔹
بااین‌حال طبق پیگیری‌ها از فدراسیون فوتبال، تاکنون هیچ‌گونه تماس یا مذاکره‌ای با استراماچونی یا مدیر برنامه‌های وی انجام نشده و چنین موضوعی در دستور کار مدیران فدراسیون قرار ندارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453692" target="_blank">📅 12:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453691">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHz_QHPzy9j1zeU6iXsQWGzKETf_7Hp4at1ItUd6zP4aDyioZvAg81GWPESQGLrzv4FLLue3qzxQn7Cocy7Few8UPNGTGdP5P12kGJj-DNnMYs1uowzkkllhoXmp0kUKB6q9vmv1ZM-Nv5j-PvHvZ9fmS43XXJpdJTAUegHt3zfWSspAScw4ZCIQTtdJP59MkIiSD4xzCwFPXCvTQ9epTpnyEG61Bu2L16z_TzMNM3A3WmHPeQ8_UZbd5DfqwK2un_iAr4e4R2O5h66LvZ_2uLfxOM5lNkfjtPt1p-IBdTTqYmsCoXnLN6fJR46d815zHgqspJjNUQugrb03WEKkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار ترامپ برای عقب‌نشینی اسرائیل از غزه
🔹
بعد از انتشار گزارش‌های ادعایی از موافقت حماس و گروه‌های مقاومت فلسطینی با خلع سلاح، رسانه‌های آمریکایی می‌گویند که دولت ترامپ از رژیم‌صهیونیستی انتظار عقب‌نشینی از نوار غزه را دارد.
🔹
یک مقام آمریکایی «نیوزنیشن» گفته که اگر نیروهای اسرائیلی بعد از خلع سلاح حماس، از نوار غزه عقب‌نشینی نکند،  ترامپ ناراضی و مأیوس خواهد شد.
🔹
نیوزنیشن همچنین نوشته طبق متن آنچه توافق صلح در غزه نامیده می‌شود، نیروهای بین‌المللی تثبیت‌کننده با ۵ هزار عضو از کشورهای مختلف، جایگزین نظامیان صهیونیست در نوار غزه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453691" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453690">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2aba7a874.mp4?token=hL85nL0P3VuGcOWZWccx2Vo8Ve6CZyKpH-psA1zlD-DdwKdIxGgUN6ZjAJTrm-2xPU0lDbX5zBZftj86Fh-wnWNQlcHZErSRtG2RR226GC6F4uEXs3uVwSKScoiMitEcurGhfAO-n-BPeilT65h3nYOHkCpR7NjQjO8D4-nr4_sGCb_Zq5a3WX_T36fWWhfWBX6SLr3FTOWYynh1V3dBJwNV1z_D-j_Q3-GEI94s7H_693bNvZfEftooIIcUVW_MljYIeQ7YaXKr9QTp3B_J0_bgypmzyHTlg8MRDUDp8yRbl6bAyWnwle2WFiWd2tfGwOH1I15FMr1g95tmyLmjEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2aba7a874.mp4?token=hL85nL0P3VuGcOWZWccx2Vo8Ve6CZyKpH-psA1zlD-DdwKdIxGgUN6ZjAJTrm-2xPU0lDbX5zBZftj86Fh-wnWNQlcHZErSRtG2RR226GC6F4uEXs3uVwSKScoiMitEcurGhfAO-n-BPeilT65h3nYOHkCpR7NjQjO8D4-nr4_sGCb_Zq5a3WX_T36fWWhfWBX6SLr3FTOWYynh1V3dBJwNV1z_D-j_Q3-GEI94s7H_693bNvZfEftooIIcUVW_MljYIeQ7YaXKr9QTp3B_J0_bgypmzyHTlg8MRDUDp8yRbl6bAyWnwle2WFiWd2tfGwOH1I15FMr1g95tmyLmjEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماد کوله‌پشتی کودکان شهید میناب در نجف اشرف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453690" target="_blank">📅 11:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453689">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lccmSnoeeyAOFCwWBhOViAdVNWOk_h5PMc8N1caNdVCPZZshzWZ7f2RZY07gI6wrdUXJP7bnvGRNmbv9_dGl06jaT-tx68hMO7hfaJ6_ifrMwD4tBepGW1T565-X7Dm0Fxo2i0aOIzNJk7nx-n1l9ZXXSMzofRwKj322S_a6Y8bdkpDw313UlGOObbank2Vshd0uncxzwAhf8e-C2YTSGUV5o9AakKfUmX04By9bf9rLdDm2cXrkQ3SlQETI54zpV0Ku_hJYEc4-c2A3QwB-5QIHBsbpoNATKaEpcr5ZxB2mqcd52SYzw-sEusaps9UQMjZKU5NPyIpFrMPUI1kS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خصوصی ونس با نتانیاهو درباره ایران
🔹
مقام‌های مطلع می‌گویند که معاون رئیس جمهور آمریکا جلسه‌ای صریح و دوستانه با نخست‌وزیر رژیم صهیونیستی درباره اختلاف‌نظرها حول جنگ با ایران برگزار کرد.
🔹
مقام‌های آمریکایی و صهیونیستی مطلع درباره این جلسه، به وبگاه آکسیوس گفتند که هر دو طرف توافق کردند که به همکاری درمورد اولویت‌های مشترک در غرب آسیا ادامه دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453689" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453688">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7tokvwNst4lQgZiMg1Fza3ONpMgWsXF11t9pvwcWYwss12WW3fBMLWSMdmGs1TFkRSNcuMBv4eLCgIY5La_Mgbk-ldjK890SRcEH74jGlD7JGnmMa-v77Z9Mt8w6w6Lbnd6uKOPrG8RLWYaNrJeDI3lh33m06iJ7lf4ON_-WJZ8ycURvSwCC-YHA_jAmE51pUvTCLfqIBUBLlMCdrwEZq_ZoNlyz5q6CDdXqZSaOIkqnxlkwRXnYh14x0m-j5zBvKxnLZ4JgPHSz2Gey72VhBOIjsyp2mUVNy6i98h8KXF2pBIrtoMy3zE_BuYpx3sMwGpz21r3eTUQ9l6AvgX7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان به عون: در توافق با اسرائیل شتاب نکن
🔹
روزنامه «الاخبار» نوشته اردوغان در گفتگو با عون، رئیس‌جمهور لبنان، به او توصیه کرده در توافق با اسرائیل شتاب نکند زیرا اسرائیل هدفش صلح با هیچ‌کسی نیست.
🔹
اردوغان به عون توصیه کرده که سعی کند با سفر به دمشق و دیدار با الجولانی، سرکردۀ شورشیان حاکم بر دمشق، روابط خود با سوریه را تقویت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453688" target="_blank">📅 11:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453687">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff8f2865b.mp4?token=Pcjxj0dUb170BMD9Tewyve9tr_G-VB5Bf4loe_V9yYR-Jh3tfclyIi5oUHhIqXbT9VaYzBsAS0VKVSANp0isB45DiCcXSS2nSH1iaHPzrSCE6UL2VcHiCx-iLwG_ob-eqelIdKruFWdP9_TBVlaEoEDv69n7GdeDRSzRYzrsmxZlfYEHtuwgl8KGVfmItbtftCMQMfxiSzKrm7MFzO1MMsqLVqZHB2Ngj36h2ACoLsCpb8mB6PFOfEpHWrL47f39Qppw8Jx-84Rb5NX61zCnAK9hGIEo0pU3QwC3LIryn6dVdLYxbUuWyN60FDzEGdVkg1v5pYIvT9vJ7ocW5sBEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff8f2865b.mp4?token=Pcjxj0dUb170BMD9Tewyve9tr_G-VB5Bf4loe_V9yYR-Jh3tfclyIi5oUHhIqXbT9VaYzBsAS0VKVSANp0isB45DiCcXSS2nSH1iaHPzrSCE6UL2VcHiCx-iLwG_ob-eqelIdKruFWdP9_TBVlaEoEDv69n7GdeDRSzRYzrsmxZlfYEHtuwgl8KGVfmItbtftCMQMfxiSzKrm7MFzO1MMsqLVqZHB2Ngj36h2ACoLsCpb8mB6PFOfEpHWrL47f39Qppw8Jx-84Rb5NX61zCnAK9hGIEo0pU3QwC3LIryn6dVdLYxbUuWyN60FDzEGdVkg1v5pYIvT9vJ7ocW5sBEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریان‌های حیاتی جهان در دستان ایران؛ اقتصاد آمریکا و عربستان در لبه پرتگاه
مرضیه حسینی، خبرنگار اینترنشنال: تبعات اقتصادی ناشی از جنگ علیه ایران جهانی است!
هم‌اکنون به دلیل انسداد تنگه هرمز، اقتصاد عربستان ۵ درصد کوچکتر شده‌ و از طرفی ۲۵ درصد از صادرات نفت این کشور نیز کاهش پیدا کرده‌ است؛ اوضاع برای آمریکا نیز مشابه است.
اگر ایران بخواهد باعث ناامنی در کانال سوئز شود، اوضاع فاجعه‌بار اقتصادی ناشی‌ از انسداد تنگه هرمز و باب‌المندب تشدید خواهد شد.
@Fars_plus</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453687" target="_blank">📅 10:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453686">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بازداشت یک انگلیسی به اتهام جاسوسی برای ایران در پایگاه‌ هوایی انگلیس در قبرس
🔹
دادستانی سلطنتی انگلیس اعلام کرده یک شهروند ۴۴ ساله انگلیسی به جرم به اشتراک گذاشتن اطلاعات مختلفی با ایران از پایگاه هوایی آکروتیری انگلیس در قبرس، دستگیر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453686" target="_blank">📅 10:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453685">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApqmXG29SjqLz9zh_aTgwMibXzJvFxWyiTkbysejr4uzbjF_bmDhNofWzzv_cXo41n8iyQksaJuKHu9qgJCjxZ68FAiZmF9uJLZbmmQAwArnjtESxe8-GAPoZ2hrG_t-dcvQTLYAEKLN8Pp9ajhsXhkptx4K5mDc3Zkju_2iRW8NFrYfUM7mkDW8D00ZWnjIhDDOXay8ceqpuNeHu88wVjeAXp67RN8n5A3UYfofjAWGKZI8MUv14FNDm-zuafaMYm-Zmb56OHx2HOsMK_S7D1lQ3ABmJOsgZXQZEYAkwgykpbDJiv1I6aJhQQ8jSDspjEolLz2-4vBj1_pER29PZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار جان حداقل ۳۲ معدنچی پاکستانی را گرفت
🔹
در پی انفجار در یک معدن زغال‌سنگ در استان بلوچستان پاکستان، دست‌کم ۳۲ معدنچی جان باختند؛ گفته شده امیدها برای زنده یافتن سایر معدنچیان بسیار اندک است.
🔹
به گفته بازرس معادن این منطقه، هنگام وقوع انفجار ۳۶ معدنچی در داخل معدن حضور داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453685" target="_blank">📅 10:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453684">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9f1bc0e5.mp4?token=IbAYLTEjQ-y0OsYCmuvZ7uUfrzM6eQED-3HrPH1wyC3EhI2tkQQ8mzJNq3u7I6wScw8ik1vo6mpyyU-6baddXCBmWZmLF_EQVgdiR9GF326SoV_HPHP1FEVf4mUHslklG8vBJmWLA7gW2ajZOlecX4za11Hx_2ByJD4aeI2Xhwl4HI6TheCbfD9FLY0G-XWv-xVgSe8O0RaiBUvO1VNgy-QFzF-PT-JH-5K9RVXK1tvDXC4x6BEtrGaMZPCmsrkqctZX-nFx8acHLkH3c3xpS3GrLVpeajoi3gnu5LXtgN8aQPPX8T1fY6JHP5cs3Lv4NJQupDP8azuINYnz69E4xa82fpOf4zu3tDTWytqWxyL216dQo3IWXoN4fQoXgoB8Ktvc_ox05vAVq1QmThAlMxqs7wp857maR54ich527izGB7dBCFtDLjXu4HIeYQuWX-ZCdtuzjBShvATRbVK-lxqzMh-fAjUZy32zv1RjyLYtLXwKS8AqUItugtz_EDHVgY-MQjjX1rc99zeuyDUQZu8-uMCkBIaxgvqHH-mm8oh26Fx6JbDiwGLwxoR1DggSTZps9p6iq2Vue7mjoUK8z4GT25IzboG6Qi31HktvgzZ_qSarjR_G7nDoDdOw8YhSKMHTGw-HGg5fKIaV4cXr0adukiBhz_fBI2f5KLSGZtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9f1bc0e5.mp4?token=IbAYLTEjQ-y0OsYCmuvZ7uUfrzM6eQED-3HrPH1wyC3EhI2tkQQ8mzJNq3u7I6wScw8ik1vo6mpyyU-6baddXCBmWZmLF_EQVgdiR9GF326SoV_HPHP1FEVf4mUHslklG8vBJmWLA7gW2ajZOlecX4za11Hx_2ByJD4aeI2Xhwl4HI6TheCbfD9FLY0G-XWv-xVgSe8O0RaiBUvO1VNgy-QFzF-PT-JH-5K9RVXK1tvDXC4x6BEtrGaMZPCmsrkqctZX-nFx8acHLkH3c3xpS3GrLVpeajoi3gnu5LXtgN8aQPPX8T1fY6JHP5cs3Lv4NJQupDP8azuINYnz69E4xa82fpOf4zu3tDTWytqWxyL216dQo3IWXoN4fQoXgoB8Ktvc_ox05vAVq1QmThAlMxqs7wp857maR54ich527izGB7dBCFtDLjXu4HIeYQuWX-ZCdtuzjBShvATRbVK-lxqzMh-fAjUZy32zv1RjyLYtLXwKS8AqUItugtz_EDHVgY-MQjjX1rc99zeuyDUQZu8-uMCkBIaxgvqHH-mm8oh26Fx6JbDiwGLwxoR1DggSTZps9p6iq2Vue7mjoUK8z4GT25IzboG6Qi31HktvgzZ_qSarjR_G7nDoDdOw8YhSKMHTGw-HGg5fKIaV4cXr0adukiBhz_fBI2f5KLSGZtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از روضه‌خوانی محسن محمدی‌پناه به‌یاد رهبر شهید در یادبود حسینیه امام‌خمینی(ره) در مسیر نجف به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453684" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453683">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duT2UuyL5gcZj14Gvszl-h72COTBu1BfWW21WxrSWRAt86-3Ai_02FroHPlKIzNwTlK5ojytpUrOPNJrNtI2mHfzM92gMyLV_Npq_X4JtfW613q06dfOkPd35-o-PMYe5HYWCAN9T54IsLFEezXmrGx8OQfJYdhFdYqg1WEaEb-5seNxSiqg14pFYzDh-Beo7C3P8LshQ8npJWqQf1yxBw4bDIG3-Ev8poVsgv_329-kCJ67vrUwje4CiG_YxFOb0O3NQBW7ISGVpHYpUuV5Ft3FCrjKKdcD1ZMW_B4G5KXkFYHjJvekdF7womX-Bi78gw0Y5bknxOY5UqUuK8PoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطورۀ آث‌میلان درگذشت
⚽️
فرانکو بارزی، اسطوره تاریخی فوتبال ایتالیا و باشگاه میلان در ۶۶ سالگی درگذشت.
⚽️
بارزی که یکی از برترین مدافعان تاریخ فوتبال شناخته می‌شود، تمام عمر فوتبال خود را در آث‌میلان سپری کرد و با این باشگاه ۳ قهرمانی لیگ قهرمانان اروپا و ۶ قهرمانی سری‌آ کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453683" target="_blank">📅 10:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453682">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLh87eNKzPwxlF8q7t27WDgDqp8cXMe3vF70rpVhpzcIzrhFlFQ-J-bLbVmkANPpNUHRusv31SHSzDP_MI5j6amYIVIR0sD1zZL3ecTa9NffCfWh48zsXjhLSzxnZlN-PhJ8c4-oAsqg0-N174gZnjj_eEmpwsIhyr-2cL7fb85_YlzMv-QUtlpc-BFs9G_nh0nWn8BKlwI2OfD_gqlwZNv-9wvHHsA1tM37kMf9MOhaQnxtbgVgXGGag5ZXi0h_Tp6JlkwhDcUv9IYrq2-CGp1KZ-pyw7r1vC0kUF2K-j2K63rdso-dNUDg623Ma_3spvxO8FSSri03aLby_jug6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: ۷۰ درصد نفت خاورمیانه جایگزینی برای تنگه هرمز ندارد
🔹
رسانۀ قطری الجزیره در گزارشی نوشته اختلال‌ها در تنگه هرمز باعث شده تولید نفت کشورهای منطقه به میزان بیش از ۱۴ میلیون بشکه در روز کاهش یابد و این موضوع فقط در هقته‌های اول جنگ علیه ایران بیش از ۱۵ میلیارد دلار به آن‌ها ضربه زده.
🔹
الجزیره نوشته  برخی از کشورها مانند عربستان و امارات تلاش کرده‌اند با استفاده از خطوط لوله موجود، اثرات این بحران را تعدیل ببخشند اما درنهایت بیش از ۷۰ درصد نفت کشورهای حاشیۀ خلیج‌فارس راهی برای دور زدن تنگه هرمز ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453682" target="_blank">📅 09:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJv3ENKWy7ch26tjonsuJFW7elzqIAo4gvwX8SO23eqN17vZN-5H5Bc_yOiIUANVcrzF7qPWNg7j8_5ZYPUMwWUWyZl87KExlxadVxjK9uNwofxjLkhuGi_rFigPHuo-T7vIQRXflWlbB8yF5HV20mBqOL7hxY0ufR4cCNN9TeGd_bjgXTf74N7dGXzi_fj4MOd1BrnpXtunV5F1u0h3WqRmXEJNPkszzfBcFPo2yD_QvfepaDaqsVxdmmbj7NYVlzoeFc5B3-N72PiiV67PpRL_VuGl1B-2k3XT6W5e3PJbooOb6xbLr0f9S7tF-wfOzVocprj4BLmXhKkwDpAoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عجیب‌ترین صحنۀ لیگ ملت‌های والیبال
🔹
در دیدار شب گذشتۀ تیم‌های ملی والیبال لهستان و اوکراین که با برتری ۳ بر ۱ لهستان و صعود آن به نیمه‌نهایی لیگ ملت‌های والیبال همراه شد، یکی از امتیازات حساس بازی با صحنه‌ای میلی‌متری همراه شد.
🔹
درحالی که بازیکنان لهستان نیز تصور می‌کردند اسپک بازیکنشان به خارج زمین رفته است، بزرگ‌نمایی تصویر بازبینی ویدیویی نشان داد توپ به‌طوری باورنکردنی با خط مماس شده و آن را لمس کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453680" target="_blank">📅 09:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30549b220.mp4?token=aUD4zw6gtrrX8oAbHf0WFjmm92sUcHaPqtS3wgw4hgElBqzgu98GdfMh2KvBH2Fb7CIcghH_IT6hQ6k56qKXwnXVJ_lSSDUzNSrpB4boSGa5kZXpjk4hWMhTNG3xBQOzwni_wBFaMblrjFHxj93-4f1jYDb2k8o5-V4QUr_lQkj7r7t9g1ZYwaKeo3IFWTttEPnSlHHMzqr_hiHcM3Woi11CphHZlbutPQos8WKJrc4KyLkU3Cn5sG08NyHNJrvTdY8I2GtnKxGHhjTOsK3YV2pDMR5GdlBPVA5Qkxm7Rqo-Na4ivOXvNLPep470W8GAMM5YDgyUCrzBRrVpC5IiyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30549b220.mp4?token=aUD4zw6gtrrX8oAbHf0WFjmm92sUcHaPqtS3wgw4hgElBqzgu98GdfMh2KvBH2Fb7CIcghH_IT6hQ6k56qKXwnXVJ_lSSDUzNSrpB4boSGa5kZXpjk4hWMhTNG3xBQOzwni_wBFaMblrjFHxj93-4f1jYDb2k8o5-V4QUr_lQkj7r7t9g1ZYwaKeo3IFWTttEPnSlHHMzqr_hiHcM3Woi11CphHZlbutPQos8WKJrc4KyLkU3Cn5sG08NyHNJrvTdY8I2GtnKxGHhjTOsK3YV2pDMR5GdlBPVA5Qkxm7Rqo-Na4ivOXvNLPep470W8GAMM5YDgyUCrzBRrVpC5IiyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیشترین پرچمی که در اربعین دیده می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453678" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453677">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae415fca5.mp4?token=TDDDf0hW5HH4iGUGtr34ZHoEPh33AXY8oNrGIH1OBCx9tIOVwAXxno4e2VEYyK1TtLonjg4O4w5Ipmf1JdUTj-qdEQeREKEQLhmYP9yWJdfWnWVW490y0F-E1yRa6X3j53_gGIzrzs325MZmW5zMZyelatZVJk_6tJZSJao_mzy5G-UClmMQ5JCVzLsUQkXZjonWw6EpVJjHYRf61njX6vDKAifH-tzbTIkceozZWFl1zNTIidFew6cnRKC5K6uxb_Bsz8ZwIbFRCzgm4c83ybdDHIVGgxYoaig6IlMSXFbKe-6UOZ0aW9Qzuuu_Ayv7-_DP2472D2LdTr8hWufyjwdOr_g-ChMWLRA194K9FPBWKyeAsIC1NccUBIjtoU-yAZG3Q2ECFQVBxF0CvzICGjikPmvfytTEThv18RKntxzhpnCKnH_SgF8JRk0k-v3SNfK75JeP_0V1f9IDy8wR9ZpcYyUpiO64OK35crFfhxip-y7qW2euywOUV8jeMPbQralmef5gKfQbSLBdjW5SuRDuiIISY8mnsGXn3ZK1ahHL59Ix_RpYCPE3ZOi4wZIMRgn2VKXCr_I3tdS-qeKdRNVIqwrK_1sDlIUsKzfDdoxbKByVD_M0AXgfXNbr41GNq8MZof96aXb427oQ_GBhbsppMy7vSqJSKJfTabiw63I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae415fca5.mp4?token=TDDDf0hW5HH4iGUGtr34ZHoEPh33AXY8oNrGIH1OBCx9tIOVwAXxno4e2VEYyK1TtLonjg4O4w5Ipmf1JdUTj-qdEQeREKEQLhmYP9yWJdfWnWVW490y0F-E1yRa6X3j53_gGIzrzs325MZmW5zMZyelatZVJk_6tJZSJao_mzy5G-UClmMQ5JCVzLsUQkXZjonWw6EpVJjHYRf61njX6vDKAifH-tzbTIkceozZWFl1zNTIidFew6cnRKC5K6uxb_Bsz8ZwIbFRCzgm4c83ybdDHIVGgxYoaig6IlMSXFbKe-6UOZ0aW9Qzuuu_Ayv7-_DP2472D2LdTr8hWufyjwdOr_g-ChMWLRA194K9FPBWKyeAsIC1NccUBIjtoU-yAZG3Q2ECFQVBxF0CvzICGjikPmvfytTEThv18RKntxzhpnCKnH_SgF8JRk0k-v3SNfK75JeP_0V1f9IDy8wR9ZpcYyUpiO64OK35crFfhxip-y7qW2euywOUV8jeMPbQralmef5gKfQbSLBdjW5SuRDuiIISY8mnsGXn3ZK1ahHL59Ix_RpYCPE3ZOi4wZIMRgn2VKXCr_I3tdS-qeKdRNVIqwrK_1sDlIUsKzfDdoxbKByVD_M0AXgfXNbr41GNq8MZof96aXb427oQ_GBhbsppMy7vSqJSKJfTabiw63I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ‌جا کربلا نمی‌شود
!
🔹
روایت دلدادگی زائران کربلا را از دریچه دوربین خبرگزاری فارس ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453677" target="_blank">📅 08:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae919478b.mp4?token=fFbxQkZ2OtWfWsQXmJku6UEc6VfSP4AntLc8jiuHmBzg-IYcVm7CypQptKp2lNH3Yuup_fE6v7wFGizPTHN9yj03ta4U4W7UVWsw9zTBg_2WUyDU16OrIgDLUyIdrH1AhhI5j8bmZa3HGLvDYq_krrcUT1zLAYxWn3UsjbADA8gPcxQtvPGtNFIrhkut5IYOrax6EYXZh04IHaALWKR5d5g6rrAniIx8hGw8H3jFEVVrpLHBoZF4krMAkV_cbICYjrStYak1ReQUe3kj37kDcaxe4jCC2zND7WgTjk56i6nGVhTqKAiv6ulkWCjGBgekf3L1NbU3Fji9yIlguYDrIBcJ10NWuJP-hgeM6YPQQ01_vvh77ZE35rrI_cWpEIpQdyzbLHwEdAqPAgC0D7zHTfjMiWq6YxdrefvxJc5ImHV0kWMP9vIw_lMvwcKQFIo-moxllheIOXLE5JhHqurjN6BkKyAO_u1qv1rTMs53picnYiqZ4yQRmWDA61FO54Pad8GLlG6ct5Ip_m7XC-nfzOCnA_imiabBWr03-_jV5S5Qm_WF1W_lYzHfCiAlKZq1WVfsUK6-HHcfTsS4onj36ftF8r_A1PKddDpzizs8_CeDgIvmIN9TRRtjsGD_cxAKI21BNDsCtQhfhacJvN1Y93tqO-FdhfRqqy03dumLaxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae919478b.mp4?token=fFbxQkZ2OtWfWsQXmJku6UEc6VfSP4AntLc8jiuHmBzg-IYcVm7CypQptKp2lNH3Yuup_fE6v7wFGizPTHN9yj03ta4U4W7UVWsw9zTBg_2WUyDU16OrIgDLUyIdrH1AhhI5j8bmZa3HGLvDYq_krrcUT1zLAYxWn3UsjbADA8gPcxQtvPGtNFIrhkut5IYOrax6EYXZh04IHaALWKR5d5g6rrAniIx8hGw8H3jFEVVrpLHBoZF4krMAkV_cbICYjrStYak1ReQUe3kj37kDcaxe4jCC2zND7WgTjk56i6nGVhTqKAiv6ulkWCjGBgekf3L1NbU3Fji9yIlguYDrIBcJ10NWuJP-hgeM6YPQQ01_vvh77ZE35rrI_cWpEIpQdyzbLHwEdAqPAgC0D7zHTfjMiWq6YxdrefvxJc5ImHV0kWMP9vIw_lMvwcKQFIo-moxllheIOXLE5JhHqurjN6BkKyAO_u1qv1rTMs53picnYiqZ4yQRmWDA61FO54Pad8GLlG6ct5Ip_m7XC-nfzOCnA_imiabBWr03-_jV5S5Qm_WF1W_lYzHfCiAlKZq1WVfsUK6-HHcfTsS4onj36ftF8r_A1PKddDpzizs8_CeDgIvmIN9TRRtjsGD_cxAKI21BNDsCtQhfhacJvN1Y93tqO-FdhfRqqy03dumLaxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله صفایی بوشهری: قصاص جنایتکاران بزرگ وظیفهٔ همهٔ مسلمانان جهان است
🔹
هر مسلمانی که شرایط و توان این را دارد که قصاص خون رهبر شهید را بگیرد باید دست‌به‌کار شود.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453676" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp2I9cm93nA2nCbwoq9sCPNHzcGLjbR0HOBSPoGianPkClgcTxoQ928fnFb70h9JDxKy_NDmMg6QinEwW1ml_Ss5om9WAlKjTL1KVj4WH3MCt47qw0jDfLzXVSYPE-Ki2KYNV7Qtlc7EHLnZKFiQqSf0DDUjnwfZ5Q8KRKN3ZcuW0lrDYRJm5r8cufBbDBC2WyA535yaGpE20c6kzv-UU4AEnF-bD0G_XdZ4f6XTNLMDwTTAhqZ-iJMkhhD_ZFvoEawmWU4O5071jgnypTQ1TBtbr66_sGfU1zIUr07MCWZ0glahJjz_I4XGv54ncs5Y6FwZiZYpNwycw0_qC2n84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان سفیرش را از کابل فراخواند
🔹
روزنامهٔ «نیشن» پاکستان: اسلام‌آباد در واکنش به تحولات امنیتی افغانستان، سفیر خود در کابل را برای انجام رایزنی‌های سطح بالا فراخوانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453675" target="_blank">📅 08:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1b6f1ea1.mp4?token=cR9L-_VS7NCsHnyCAiU0t2CqaQR_3WHgP1eu8G8x41kA_dLQK9kGfYbfaGXxJ9RYsQCpxcCdq0Ot0taFghi2SqSTVnNUhDVbM3Y74vczqAo1GLglS-qFCfSLKG4L01nhu-TO4V77iuKqNlf1uRMeHjjdc9wqfBNKwNpXsfWN1839zVzRTB9ItIAdzriaQnij77eOEDVLK_w2mjsdd49jdY63fl_WgPyYgfPoUUpVWg6_wSlWGRCu0fLQqUgKTSZBc2BsK8m2-_dQwugne17cUl_LzEHWOFVI17r0777AyHXXWw4OSMhPkJGpwbI2IVolLuHW91V8FDw-FC7PHEH6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1b6f1ea1.mp4?token=cR9L-_VS7NCsHnyCAiU0t2CqaQR_3WHgP1eu8G8x41kA_dLQK9kGfYbfaGXxJ9RYsQCpxcCdq0Ot0taFghi2SqSTVnNUhDVbM3Y74vczqAo1GLglS-qFCfSLKG4L01nhu-TO4V77iuKqNlf1uRMeHjjdc9wqfBNKwNpXsfWN1839zVzRTB9ItIAdzriaQnij77eOEDVLK_w2mjsdd49jdY63fl_WgPyYgfPoUUpVWg6_wSlWGRCu0fLQqUgKTSZBc2BsK8m2-_dQwugne17cUl_LzEHWOFVI17r0777AyHXXWw4OSMhPkJGpwbI2IVolLuHW91V8FDw-FC7PHEH6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اصابت پهپاد انتحاری به پایگاه تروریست‌های ضدایرانی   @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453674" target="_blank">📅 08:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLaaq5rwNS45udjP9BfkFjp3WKjAFXrB4hzh__rPELM1PURH2_-XvjYgpywGRaE2ZciWbSu8nRRIJeNbd45sD4h1Up0dpsVT3jeUTRCiltfeGymrbPd_4GoaSKamMFdk28bp7JXDxVPWnDgzNWPG3nWwecak7k65ean970Yt0RDeNobdSbS-Pl0LldH119PGMmsqvnSnwt3b73mdvgiQBC5eipMa76eaf-1FSVWobqnmBatCeLkitr4lP3SLt0NP6nraNzs83p0ap8qLhUOf1LKJdGwA5_QUa3uVDX9o4unzcxIwjqghDP5FRlisIfJUBb_CxykC91wtko4sBT3wzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمارستان تخصصی صحرایی سپاه در مهران به خدمت زائران درآمد
🔹
فرماندۀ سپاه امیرالمؤمنین(ع) استان ایلام: این مرکز درمانی مجهز با حضور پزشکان متخصص تا پایان اربعین آمادۀ ارائه خدمات درمانی به زائران می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453673" target="_blank">📅 07:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453672">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972d98a60d.mp4?token=lpeq_hAKfYg75o-fdS9JQlT1P8Ix9vPosHoU-EsnVHvJV-XIoYvBAVf1UQMKrXwo-nH5Ku8ffbXgx_5rgplCHYPLl8QC_yaCuhYFsK5_dDgqGbu4rD98FZMS0blURmIAFRPa9tF6cLwKSwUHYlZtlJ0aBVdND_cFnP-5LQisne_tlnictF3l9B7hzBqFc1NKWqQaY1JXKahslpPep_EIZuK5qxpWL6ec7JtXV613YAN4zyu8ZedztZpxZ4P7aEjzRCdIsjq4tYDDlTp6wvUIiZ_29eHX0Rb9A_FnCmARuS4Or7A1nCFhDMSShFWcVEglHdW7TZJfVv8yRMV8C7RD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972d98a60d.mp4?token=lpeq_hAKfYg75o-fdS9JQlT1P8Ix9vPosHoU-EsnVHvJV-XIoYvBAVf1UQMKrXwo-nH5Ku8ffbXgx_5rgplCHYPLl8QC_yaCuhYFsK5_dDgqGbu4rD98FZMS0blURmIAFRPa9tF6cLwKSwUHYlZtlJ0aBVdND_cFnP-5LQisne_tlnictF3l9B7hzBqFc1NKWqQaY1JXKahslpPep_EIZuK5qxpWL6ec7JtXV613YAN4zyu8ZedztZpxZ4P7aEjzRCdIsjq4tYDDlTp6wvUIiZ_29eHX0Rb9A_FnCmARuS4Or7A1nCFhDMSShFWcVEglHdW7TZJfVv8yRMV8C7RD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراکز راهبردی آمریکا در کویت هدف پهپادهای ارتش قرار گرفت
🔹
ارتش: در بیست‌وهفتمین مرحله از عملیات صاعقه و در پاسخ به تجاوزات اخیر ارتش تروریستی آمریکا به کشورمان و حملۀ وحشیانه به منزل مسکونی در جزیرۀ قشم، ساعاتی قبل، آشیانۀ جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات این ارتش کودک‌کش در پایگاه احمدالجابر کویت، هدف پهپادهای انهدامی ارتش قرار گرفت.
🔸
پایگاه احمدالجابر کویت، نقش عمده‌ای در عملیات های هوایی و نظارتی آمریکا ایفا کرده و فراتر از نقش عملیاتی، از کانون های حیاتی پشتیبانی هوایی برای ارتش تروریستی آمریکا محسوب می‌شود.
🔸
حملات قاطع، گسترده و پرحجم ارتش و سپاه، رهگیری پهپادها و موشک‌های ایران را برای دشمن با وجود بکارگیری پیشرفته‌ترین سامانه‌های پدافندی و تقویت آن، بسیار پرهزینه و دشوار ساخته، و دشمن خبیث مجبور است با سانسورهای شدید، مانع انتشار اخبار آسیب‌ها، کشته‌ها و مصدومان شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453672" target="_blank">📅 07:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453671">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f6a42e11.mp4?token=KIbRo77pUN2-UG7z4A0CNszXbL5-IXd2zk8cg2B4tKwFF8QLz9-UNQeYW-wxE7dOChn15D8MP1eFtN1e9E9uKvY__Oaa1X8Vau6W-fEurncms1xDwmObeTSQD0vFSHGyW43Ldc44AEezvkmXVcTbsae3c7oDGU42vY60BqzDXdeVRe616_LkO7kxz0h-iAxzLfmyyfAufi5hMGRPmzMUdTF8MuXiM9-rDrApJ-d4Y-4O1i2_xarGT7mmowRwjQCsFuh1ZDLiBCz_Ya2vbqVjK2pfbJOcPGrEY1lfnXu_cS5Y0du_48Q7IFoius4ZsjUlGfco08_ZVYSCI8wPVwE7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f6a42e11.mp4?token=KIbRo77pUN2-UG7z4A0CNszXbL5-IXd2zk8cg2B4tKwFF8QLz9-UNQeYW-wxE7dOChn15D8MP1eFtN1e9E9uKvY__Oaa1X8Vau6W-fEurncms1xDwmObeTSQD0vFSHGyW43Ldc44AEezvkmXVcTbsae3c7oDGU42vY60BqzDXdeVRe616_LkO7kxz0h-iAxzLfmyyfAufi5hMGRPmzMUdTF8MuXiM9-rDrApJ-d4Y-4O1i2_xarGT7mmowRwjQCsFuh1ZDLiBCz_Ya2vbqVjK2pfbJOcPGrEY1lfnXu_cS5Y0du_48Q7IFoius4ZsjUlGfco08_ZVYSCI8wPVwE7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای جدید از آسیب به بخش نظامی پایگاه «علی السالم» کویت
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453671" target="_blank">📅 06:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453670">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وال‌استریت‌ژورنال: آمریکا کاهش حضور در کویت را بررسی می‌کند
🔹
روزنامۀ وال‌استریت‌ژورنال گزارش داده که ایالات متحده آمریکا در پی تحولات جنگ علیه ایران در حال بررسی گسترۀ حضور خود در کشور کویت است.
🔹
اقدام آمریکا در حالی انجام می‌شود که مقام‌های کویتی اعلام کرده‌اند که همچنان نیازمند تعهد قاطع آمریکا به حمایت از کشور خودشان هستند.
🔹
به نوشتۀ این روزنامه، تأسیسات و پایگاه‌های آمریکایی در طول جنگ بارها هدف حملات ایران قرار گرفته‌اند.
🔹
تحلیل‌گران می‌گویند آنچه به احتمال زیاد باعث تغییر در این روابط خواهد شد، درک این واقعیت از سوی آمریکا است که حضور نظامی دائمی و بزرگ در کویت دیگر حیاتی یا از نظر نظامی عاقلانه نیست.
🔹
مقامات فعلی و سابق آمریکایی مدعی شده‌اند پنتاگون حتی قبل از آغاز جنگ ایران نیز در فکر کاهش نیروهای خود بوده است.
🔹
مقامات آمریکایی به وال‌استریت‌ژورنال گفتند پنتاگون در پاسخ به حملات موشکی و پهپادی ایران به پایگاه‌های آمریکایی، حضور خود را در کویت کاهش داده تا ریسک را به حداقل برساند.
🔹
طبق گزارش این روزنامه مقام‌های کویت مانند دیگر کشورهای خلیج‌فارس از این‌ که ترامپ جنگی را بدون مشورت آنها آغاز کرد که آن‌ها را در تیررس قرار داد، ناراحت و آشفته شدند؛ حسی که با طولانی شدن منازعه و بلوکه ماندن صادرات نفت شدیدتر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453670" target="_blank">📅 05:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع چند انفجار شدید در استان دهوک در شمال عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453669" target="_blank">📅 05:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4792668f.mp4?token=ACGrSXw0lcUsw3bxHG_heQTjORfUNPGxf1hliIFmeHzgC4F8rAE1CPfAh9xtdT3MMB7bGmTxRik6j6sIsR6A4BWrGpLFw2UEVSNftmBzh2zaIsejwVqtkqeriKGk9aXbjXJQfDNG6Y0yUX4T5vQbNgDuo0VhMs0k7R44ySR0Fnck-I3XF84qAOTWCYoRWvSD1FX0tagmnYlpvY_c4SKe7_ssXMV13gfbR0M_qNWxn29x7cGQdrJWxdGCTcB-Bmx1PoebG7gkv9GGQxtdK8ZxYPFIKgln2_ed9-IDoZRDqs8oIVYlJSxmLS5zjt6rrKh10qqFZy6dYcspk3aOhnipcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4792668f.mp4?token=ACGrSXw0lcUsw3bxHG_heQTjORfUNPGxf1hliIFmeHzgC4F8rAE1CPfAh9xtdT3MMB7bGmTxRik6j6sIsR6A4BWrGpLFw2UEVSNftmBzh2zaIsejwVqtkqeriKGk9aXbjXJQfDNG6Y0yUX4T5vQbNgDuo0VhMs0k7R44ySR0Fnck-I3XF84qAOTWCYoRWvSD1FX0tagmnYlpvY_c4SKe7_ssXMV13gfbR0M_qNWxn29x7cGQdrJWxdGCTcB-Bmx1PoebG7gkv9GGQxtdK8ZxYPFIKgln2_ed9-IDoZRDqs8oIVYlJSxmLS5zjt6rrKh10qqFZy6dYcspk3aOhnipcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع محلی از آتش‌سوزی گسترده در پایگاه‌های تروریست‌های ضدایرانی در اربیل گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453668" target="_blank">📅 04:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c17263c56.mp4?token=UM2Gza4e6TbjfXpkA_lzXBLhYsRA47VIc2Tx9yrD8DjEpr_QH636c8k_-RxEn18qB8bLK_ZCBdYMOmXwUXE-kYCtHLgOPBHRP33r8CQ0ygUNb3vbDdqoe9BD7qtHNyj16JcliXu6-ieONe4xqxE41J6C-w42CUpyyBf7xCzVv3jrOPRWm1LOyiwUyjX7dARt-kYBTadagCcSs_vj2l8UbUqwnAsKA_-xh55oOt9Skvzx9m6iaDsXy6zgzRDNEALsuuXHMgTJ2sWhjgIxa_ttpium6Uv9Q1xeDPbvTpYPxYr8yfJLfacfCyBJYDqcSeTw8f9u78O-mP2zKqFCFUAGYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c17263c56.mp4?token=UM2Gza4e6TbjfXpkA_lzXBLhYsRA47VIc2Tx9yrD8DjEpr_QH636c8k_-RxEn18qB8bLK_ZCBdYMOmXwUXE-kYCtHLgOPBHRP33r8CQ0ygUNb3vbDdqoe9BD7qtHNyj16JcliXu6-ieONe4xqxE41J6C-w42CUpyyBf7xCzVv3jrOPRWm1LOyiwUyjX7dARt-kYBTadagCcSs_vj2l8UbUqwnAsKA_-xh55oOt9Skvzx9m6iaDsXy6zgzRDNEALsuuXHMgTJ2sWhjgIxa_ttpium6Uv9Q1xeDPbvTpYPxYr8yfJLfacfCyBJYDqcSeTw8f9u78O-mP2zKqFCFUAGYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع محلی از آتش‌سوزی گسترده در پایگاه‌های تروریست‌های ضدایرانی در اربیل گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/453666" target="_blank">📅 04:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
منابع عراقی از حملات جدید به مواضع تروریست‌های تجزیه‌طلب در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453665" target="_blank">📅 04:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTUPZh9S7OnjztqlARi6EuiYymccbvYyPy-UNZ1ik8OciXZFOvShF0EkLSU7U8hbt-oExXnNU4z7N5PvgsajR2bPdii8xbECJBV1ypqzIBFxe9wGKeQe2qG27mM7P_knHYnBvxtnY27X_YUNRqZs76S29PnOEzp5srzjORAVe6LQy9iCeZGMT4MxZVqfoGmE0ys3Tq1P7ai5-WD_U3HROcJJK5er_e68Od0iXav8Bm0VcO9FJW-DmaDOXmrQ1E3vGA-yJS8s6l1z-_j5L_xxS_WhfyTK8lxr3CyPQgpdMpTRy5_0cWlkFWlJvLNc-FD26kiGtv4F-TXKur_ScRhoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صهیونیست‌ها با ۷۰۰ تن بمب جنوب لبنان را بمباران کردند
🔹
بنیامین نتانیاهو و اسرائیل کاتص وزیر جنگ رژیم صهیونیستی در بیانیه‌ای مشترک مدعی شدند که ارتش اسرائیل سیستم تونل‌های حزب‌الله در زیر منطقه کوهستانی بوفور در جنوب لبنان را منفجر کرده است.
🔹
همچنین آن‌ها مدعی شده‌اند ارتش اسرائیل برای تخریب این تاسیسات زیرزمینی از ۷۰۰ تن مواد منفجره استفاده کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/453664" target="_blank">📅 02:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35df706702.mp4?token=gCO6z7dfM5HpGJE7Xfyu865TKvNbVD-yPTW3qZsMFIIfjQR3ugZQqnzCPQspNcNqL7nTnpT7ZgutR1Fb-N3nxMNyzUUaPLhxGoJIe-bMjtZthc21aSpwIg-e5txr3lw96mfvVDA_UvGSYT-jHvFgJkAEWoUeo2jvfZdCUP5rBYlRiUcN_0b_ee86_X5p1ly2WU8raHzBvoEflRYBtDs_NBe1dNVTS3J9wEvuA7HT8OUyWOQXlYu0cdmvfP0ypbCJgOBv2YkYqgtxd7e0TrlqNOEj5hcCMmhjpXaD1_OaQiHgs3ZaF-KnlH1sK-BoMIqtPLJoJcRRZQhpoRexkLjQnW2R0bOLf9DptjoTW6aVbfHHO-dIdVGqsqjfCA-4F0M5skbUN4FuyvUIgKTtYx39hH-aXnvH1a7EYhb9dIyv93NMacVtjmMFFxKfc5q4JE5lo6OchhxD4UuqLb99aB9MLi4gQ-8JV6mQ5DahMe6x5V1xWHszJnE97sOzgec8KgeQ7wo6TIO_B30H55L0gNsapoafacI6-0L6GAh50jOHzo6PxAkv7FxWB5OIQsGuJU-iM3w2zBy--giElU60AgpzuBSBo5dajxij-AwA8A5KPXmDgIPC9e5pFdgLUJ0YUabQ7FJvzofM-rJpSzROmj4PU3gvbWLpN81bGRlK-QemS3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35df706702.mp4?token=gCO6z7dfM5HpGJE7Xfyu865TKvNbVD-yPTW3qZsMFIIfjQR3ugZQqnzCPQspNcNqL7nTnpT7ZgutR1Fb-N3nxMNyzUUaPLhxGoJIe-bMjtZthc21aSpwIg-e5txr3lw96mfvVDA_UvGSYT-jHvFgJkAEWoUeo2jvfZdCUP5rBYlRiUcN_0b_ee86_X5p1ly2WU8raHzBvoEflRYBtDs_NBe1dNVTS3J9wEvuA7HT8OUyWOQXlYu0cdmvfP0ypbCJgOBv2YkYqgtxd7e0TrlqNOEj5hcCMmhjpXaD1_OaQiHgs3ZaF-KnlH1sK-BoMIqtPLJoJcRRZQhpoRexkLjQnW2R0bOLf9DptjoTW6aVbfHHO-dIdVGqsqjfCA-4F0M5skbUN4FuyvUIgKTtYx39hH-aXnvH1a7EYhb9dIyv93NMacVtjmMFFxKfc5q4JE5lo6OchhxD4UuqLb99aB9MLi4gQ-8JV6mQ5DahMe6x5V1xWHszJnE97sOzgec8KgeQ7wo6TIO_B30H55L0gNsapoafacI6-0L6GAh50jOHzo6PxAkv7FxWB5OIQsGuJU-iM3w2zBy--giElU60AgpzuBSBo5dajxij-AwA8A5KPXmDgIPC9e5pFdgLUJ0YUabQ7FJvzofM-rJpSzROmj4PU3gvbWLpN81bGRlK-QemS3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاجر اندونزیایی از آثار عجیب بستن تنگۀ هرمز می‌گوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/453663" target="_blank">📅 02:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای رسانه‌ها درباره موافقت حماس و گروه‌های فلسطینی بر سر سلاح‌های مقاومت
🔹
شبکه خبری الجزیره و المیادین ادعا کرده‌اند به پیش‌نویس سندی دست یافته است که نشان می‌دهد حماس و سایر گروه‌های فلسطینی در خصوص سلاح‌های مقاومت در غزه، به توافق رسیده‌اند.
🔹
طبق ادعای…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453662" target="_blank">📅 02:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای رسانه‌ها درباره موافقت حماس و گروه‌های فلسطینی بر سر سلاح‌های مقاومت
🔹
شبکه خبری الجزیره و المیادین ادعا کرده‌اند به پیش‌نویس سندی دست یافته است که نشان می‌دهد حماس و سایر گروه‌های فلسطینی در خصوص سلاح‌های مقاومت در غزه، به توافق رسیده‌اند.
🔹
طبق ادعای الجزیره این پیش‌نویس بر آغاز فرآیند جمع‌آوری و انبارسازی تسلیحات سنگین، مراکز تولید نظامی، زاغه‌های مهمات و تونل‌ها تأکید دارد.
🔹
طبق این پیش‌نویس، فرآیند جمع‌آوری و انبارسازی سلاح‌ها پس از اجرای کامل تمامی تعهدات باقی‌مانده از پروتکل شرم‌الشیخ آغاز خواهد شد.
🔹
در این پیش‌نویس، شروع فرآیند جمع‌آوری سلاح به ورود «کمیته ملی» و استقرار «نیروهای بین‌المللی تثبیت استقرار» در نوار غزه مشروط شده است.
🔹
طبق پیش‌نویس، گروه‌های فلسطینی در فرآیند جمع‌آوری و انبارسازی سلاح‌ها مشارکت خواهند داشت.
🔹
در پیش‌نویس تأکید شده است که هیچ سلاحی به اسرائیل یا هیچ طرف غیرفلسطینی دیگری تحویل داده نخواهد شد.
🔹
پیش‌نویس توافق، مدیریت پرونده سلاح را به یافتن مسیری موثق و قابل اعتماد به سوی حق تعیین سرنوشت فلسطینیان و تشکیل کشور مستقل فلسطین پیوند داده است.
🔹
پیش‌نویس توافق، مراحل کنترل سلاح را به خروج تدریجی اسرائیل از مناطق تحت کنترل خود در غزه مشروط کرده است.
🔹
این پیش‌نویس مقرر می‌دارد که «کمیته ملی» تنها نهادی است که حق مالکیت، انبارسازی یا کنترل سلاح در غزه را دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453661" target="_blank">📅 01:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc030dfef.mp4?token=FwusSpiYZeKpcl4oirlJ-iJ_xmmHMUKgWrptMsDlgWFR6eaf1_keVEIHvq_WHs6GFcKTNEf7f7wHiPb40nudFPM0wgbqrcUtfIgTd6R9lFB-grtlEuA29XklZVFmISPxlvxz4PAqxjneSUADSZ4KECz035n0h8qUonAJhlbQsVOKh_1lxKMUzXmZq_A9fgmfm3lXTGvG5c8IOCNfIvIMLr_cZSdxD0eCmiESFYYF0SbTpTMRIUAAvGDLPhUWK0HrpRrgcem8YvcukTRKEedxMmtOd1gjsqvbwqhh7OKsgT1yBuAefiJsz1S6msFRl7IODqNPLugFVCuM1C4dPadZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc030dfef.mp4?token=FwusSpiYZeKpcl4oirlJ-iJ_xmmHMUKgWrptMsDlgWFR6eaf1_keVEIHvq_WHs6GFcKTNEf7f7wHiPb40nudFPM0wgbqrcUtfIgTd6R9lFB-grtlEuA29XklZVFmISPxlvxz4PAqxjneSUADSZ4KECz035n0h8qUonAJhlbQsVOKh_1lxKMUzXmZq_A9fgmfm3lXTGvG5c8IOCNfIvIMLr_cZSdxD0eCmiESFYYF0SbTpTMRIUAAvGDLPhUWK0HrpRrgcem8YvcukTRKEedxMmtOd1gjsqvbwqhh7OKsgT1yBuAefiJsz1S6msFRl7IODqNPLugFVCuM1C4dPadZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی مرز چذابه
🔹
تردد زائران اربعین حسینی در پایانۀ مرزی چذابه به‌صورت روان در حال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453660" target="_blank">📅 01:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دقت حملات ایران، آمریکایی‌ها را به تحقیق واداشت
🔹
دلیل حملات دقیق نیروهای مسلح ایران به مواضع دشمن آمریکایی در منطقه یکی از سوژه‌های گمانه‌زنی در رسانه‌های غربی طی روزهای گذشته بوده است.
🔹
پایگاه محافظه‌کار نیوزمکس در گزارشی نوشته که حملات دقیق ایران مقام‌های آمریکایی را به انجام تحقیقات دربارۀ نحوۀ ردیابی نظامیان این کشور وادار کرده است.
🔹
این پایگاه به نقل از یک مقام اطلاعاتی ادعا کرده که ایران ممکن است از فناوری‌های تبلیغات دیجیتال برای تعیین محل دقیق نیروهای آمریکایی در سراسر خاورمیانه استفاده کرده باشد.
🔹
رویترز هم روز گزارش داده بود عالی‌ترین فرماندۀ آمریکایی در خاورمیانه به نیروها هشدار داده است که فعالیت تلفن‌های همراه‌شان به ایران در انتخاب اهداف کمک می‌کند و ممکن است به‌زودی به برخی از نیروهای مستقر دستور داده شود که تلفن‌های همراه خود را به‌طور کامل تحویل دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453659" target="_blank">📅 01:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453658" target="_blank">📅 01:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsWVIqUZkn3IWqHm8a7Mbus-dwsKhtzAU31DHPukVf0YpfO37mj-FIO_JHf0eyM8QS63fhy29G355xuQO5Lj7ZIVWktotiuujO2WmMVZvplloVb8bi6QtWSvE2Y6paM2G_xu3J-Aa67HV1hsQ1u3QJiubwXopVIYX54K_MzbE3PoXScSgSbHVLsgA79bVJJkD2vbbCmNe_RIJvaU9llm8VkYkN0lifv86mvhAjeLPbc8ZuPYbjdAQ47xmyo-vY95DtIJgvA1YO8zmtn21InNc31PR07FEuNIYrl9pZk9HKDg52bnvOUZ8IM5aZjAR63_S9ObuZYbCasX7HMbVfqe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین آمار از تردد زائران اربعین
🔹
رئیس ستاد مرکزی اربعین: تاکنون حدود ۲ میلیون و ۷۰۰ هزار نفر از مرزهای کشور برای زیارت اربعین امام حسین(ع) خارج شده‌اند و حدود ۹۰۰ هزار نفر نیز پس از زیارت به کشور بازگشته‌اند.
عکس: دانیال همتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/453657" target="_blank">📅 01:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=eWp5Fkce16schysUkDJjjn1bXoubUJ1SRYIU9RIVPDoQ3tkXKo4K3TmTYxafCbcfnfHxTFeVMliT4ibGyXxy9eZkAVU4U-Nvl9MfTFqeYRH0vlVk8J_ANbHkJDDheDU4dBZZYDOwSIbH6PVRc81cMxvhwxhCi-agD5WrWcwHMwBzWNWVpLEm6P8PrIeAGxuPGOaevNQneKlWa1XsBc15sLyLr1bBGv4a8yCqq4qjBzMGSqm8SG2_-CBpbPJffOxT-BfOKqtO0VbtFCA2SOgS6gYVsCZmZ1bcCtMyA5xymFYN9V9cVEDmDughKYy5IAymPRsW9Q384WyrUueWFxr2N51-l47L8XOwBNxb7juKvsi-pCYVDU2BCqH9QT6YpAOu0ZKm1hB5gW3DrI6BbjgxTDcS0RwcIJH-Hg3-rBGSsb2bTsaNg0T1U_jg2uMCny6WUNm6vlrG0QMsGU1EbLWiIvknFRgjtqRCNGcR7ePNR46Qp-xT7ZHSurW6VyUZtZp1gL1A1knaZOuXHSNxtIBed1sYuFrDqpfGxQhc3MxyzmAL5c15bltMrtseLRyih5ZJ4_mW3vSuW8PP1qeehdtwPUuXMcrilrfWRFprpKOXMentB3lhoALzbvRDB9rA-d_if1q1T-VEUMZVO6UsxgDf3DkgoJAhJkKtrvX36Rg4_Us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=eWp5Fkce16schysUkDJjjn1bXoubUJ1SRYIU9RIVPDoQ3tkXKo4K3TmTYxafCbcfnfHxTFeVMliT4ibGyXxy9eZkAVU4U-Nvl9MfTFqeYRH0vlVk8J_ANbHkJDDheDU4dBZZYDOwSIbH6PVRc81cMxvhwxhCi-agD5WrWcwHMwBzWNWVpLEm6P8PrIeAGxuPGOaevNQneKlWa1XsBc15sLyLr1bBGv4a8yCqq4qjBzMGSqm8SG2_-CBpbPJffOxT-BfOKqtO0VbtFCA2SOgS6gYVsCZmZ1bcCtMyA5xymFYN9V9cVEDmDughKYy5IAymPRsW9Q384WyrUueWFxr2N51-l47L8XOwBNxb7juKvsi-pCYVDU2BCqH9QT6YpAOu0ZKm1hB5gW3DrI6BbjgxTDcS0RwcIJH-Hg3-rBGSsb2bTsaNg0T1U_jg2uMCny6WUNm6vlrG0QMsGU1EbLWiIvknFRgjtqRCNGcR7ePNR46Qp-xT7ZHSurW6VyUZtZp1gL1A1knaZOuXHSNxtIBed1sYuFrDqpfGxQhc3MxyzmAL5c15bltMrtseLRyih5ZJ4_mW3vSuW8PP1qeehdtwPUuXMcrilrfWRFprpKOXMentB3lhoALzbvRDB9rA-d_if1q1T-VEUMZVO6UsxgDf3DkgoJAhJkKtrvX36Rg4_Us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ دشمن آمریکایی به دانشگاه اهواز از زبان شاهدان عینی  @Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/453656" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtlqvNT0kvdacFtleQzHfJ7wnsPjic6LpW7VcicOghuA9UT5X_SosxJKT8rWb3t2gaMCpcRpDf0X8jIWjoPgnzYltLTZQwfvDXGOryJ7TyRkLo-p1PTNG-7UsBGMs1kyliRt7ov3cpB2vG3D21OFraOvmsb4vxszN-XhV2-S1YFLpZJ9TxjeKMi2AmibCkyYXidEJTayQEUC23wcp8Mg7pKqqUd7N3esXCRDKcuDOrO41GyLUWC8mBmuCWb8lS3ZKxYgoQifsWLM_zIG1rjnnRP0XvKFdR0R-lLktsLUdzZEipq10ORWgnY69Yb2e8xjHS9rs1FV5Yp55V3SGl5UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار مهیب در باب‌المندب
🔹
منابع عربی از انفجار با صدایی مهیب در تنگۀ باب‌المندب خبر دادند.
🔹
به گفتۀ منابع خبری، این انفجار در حوالی یک کشتی با پرچم کامرون در میانۀ باب‌المندب رخ داده و این کشتی هم‌اکنون متوقف شده است.
🔸
بیش از یک‌ هفته است که یمن اجازۀ عبور کشتی‌های مرتبط با عربستان از تنگۀ باب‌المندب را نمی‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453655" target="_blank">📅 00:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453650">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1DLVa5QQLG-dvuqaWPoDBxUfdaFmhBkTWR1sTBxENnZT0vJnzab2GGxSJk4yV4yeI3aCp4vC1GdapLyNhBjFJP_hc-8-gReBI1kJIWL7CxS6XhP_koYauPHxVaDbvmv-b2aWEGFn0t04dJjIBxvkmNTFOsf8AmXvciBXI-ZrNipoJBI3OQUwCJ_ebqFbG1KDgrcdN1LWxwNDRj9Rgq1vXFoz0XvQYtwiRWQXNfG19s6mJo74WHwd6nFSwUNMs5lWx45KNPBwBWvjtuSTbPAz-Ni9LZKdAKjgfXmzvLu6s5BbxZbZ1FmeykG28bKshSZVjc8JDe6M5K4dsgFeD7IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF4uDdeluOkrQ7atDUNIKqJEa6KBktpqZ4NqbJ36CSOmROSzJsi7uOJnfnIc5mfgDANcFJ8BOGImhohmr-UUkRiyFBETv8Fv7rO8d7r1OLj1Ln_fgSXEMJaYg1-O75ziHOOKzloH601ofZQL-GeryqUMZDSTo4OpEUp2bK6uEmP7utp0nB_nAgkQjEgQwArc47o_FCzlEP1sbQyhd8Y86wbneG_FPz2fMGkrlK8C6a4VYF67XIoQx5L24od3iokpo_Dh-yIkKN7n0xwkBZD69jUuOdOrqXkKkSWh0vMcVFHyTzeEJ1chbdWw24rScjyF0kHZiCxpVtEcqd4jF87_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wlwi4vMRvGbTeqImbvQwwzbvIeF2FZ49ksiI4e_K7moQWzHliMrVXdBiJuSkK4XLNbwFP4tLQ0s1aIZTyOk3IL4pytDz0D5XeVRN5_h5-UR_BQRwpX5gvg6MlA5lgXt7ZhTvXUqR57YtnVckKTB9669ytbP5-9c4MNSsQ0bd0EsEYzHCJ1f83BCpnbQeJt0Crtf414y4vMMXEyMoFSlkIx9SeXJ9jT3YP4BASIMSKi5nHfePU1TSa_JNjUGmaD37EcSpWpd_mqTmtLg0hed667ytNuVBTvhYOaDqN7ivVnsb98cVn-qqFDO4rkARFWPegpFgodfxjUMFqV7DSLouMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABptKxXXINx-7ifP10BdTvXtaqWXXcpXejTDr3C-uePiEyEopxb-DIH8iLwHH6wwzYzvITeoR3OHWVMyYdct5uOiJHgq63EqSkvRcT_Jg1Slp8zVBDtOib_2gL5NczwKFumu5wGuzUA9tiLuF7YAGdNSmj8MrTnE5rIr4Zeej145fk4rRvHD8aRJtmxIk8kBHmKk50c0Yj7FFBFB6E5hdAaqH6qK8vuf_OwnoNU4mM8Vx2pgrIwdJ9ihdUyyw7Tvu3ytqhkC-ge0T7ehIu2-rUWDrKSiN_peznpPOoM89PLduB5e3oOtCLwgB0ivxVlS9hS-9qdXZ_-pnz1ZmyzB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDltUI60xwAzIf_C9hVpaefL-Q2PQjzHFMHR-7jGZq2El_AIO1B52nM8Ofu-NNGhwDWjc1imu5tEXM3bH83yhjYe8XexwYF54probKzclWNt-qJ1qLj8XUT8mrkz4gdAMuseo__9VlGgoqiPWw5hLyxJ-_u1DMvJSx0Sgb0rJCU1mM5dzzgabFnZNTzIVK8eRR-JH6spPKx7Iwifk-3Z8tjVyUTHiFwORbeJCHSilKA_IRDcS-cbESQ3372fH08E2ckeBKMP_0BCMTpQoNdLoQwP8lbHMJmDlchTkCUbddway3BdXmVX7jTu-vYZS4FsIcRlRdHtlRF35ALl5YziUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غروب زیبای مسیر طریق‌العلما به کربلا
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453650" target="_blank">📅 00:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453649">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919084637b.mp4?token=CgbXiOjZbh18foK4ftCHZFKMUxOoxieLUD_2RIgHJTCQJXBJuqiW5YXRmf5OW1eMBkPyyGn58lSKlZjkW3CEOcIGScF7kGLGaK0kU16L0RDKHQPULsnfe_z04BGLrvO52mxikfu_ZMTLTlqpBoaOf1rb2z6ejDDHz1IKahmzPbqIYDh__ZjStYGd3aHE4aQwMpvLdXdjsnpKX7Gb9bsmHL1ES45_y911BYS_A_2Loa098j3TsEruGlWXYrWHFjZeF-u03yF5hV1ClsuGX5F6Z6SQBg1BGC03YE7ctX4TD357uptOaFw6VPKoqWOb38JhB7lohJHdojjSAgFio-ImkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919084637b.mp4?token=CgbXiOjZbh18foK4ftCHZFKMUxOoxieLUD_2RIgHJTCQJXBJuqiW5YXRmf5OW1eMBkPyyGn58lSKlZjkW3CEOcIGScF7kGLGaK0kU16L0RDKHQPULsnfe_z04BGLrvO52mxikfu_ZMTLTlqpBoaOf1rb2z6ejDDHz1IKahmzPbqIYDh__ZjStYGd3aHE4aQwMpvLdXdjsnpKX7Gb9bsmHL1ES45_y911BYS_A_2Loa098j3TsEruGlWXYrWHFjZeF-u03yF5hV1ClsuGX5F6Z6SQBg1BGC03YE7ctX4TD357uptOaFw6VPKoqWOb38JhB7lohJHdojjSAgFio-ImkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پارکینگ مهران، علی‌رغم افزایش تردد‌ها همچنان دارای ظرفیت و پذیرای خودروهای زائران حسینی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453649" target="_blank">📅 00:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emJiWhBNPhkhC4Uy4-rkT9YedYMUsA1vwmL5475ydgHH3iaZy55bpS7I_v-fFy4EasMw5SQWgq_CY0zF748elXaRiog31-LUFryv2R9CYfJnzwF-pout7kBBuOpF8ZiU5fpWdzcrTd-LvDXNEi1JSjLYPqYsSk7o83ePdLoqq20QEK-fjTrrxUVLznEuEKFFDv0pbS7uXtXU7wGUIMzXvx-wKCr7F_5qalUs2xBOcYr2tvMUi38WGRuar7fBufcBF8-Tf43-F8YiGbkQGj608_h1g_01R_eSr1d03ELEw8rEHDudni2cdQtjHocA-M2QzR4J4FA7Mpbq4mBzGKoJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: آمریکایی‌ها تاوان‌ حمله به مناطق مسکونی قشم را خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/453648" target="_blank">📅 00:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/614a5bd431.mp4?token=GZ_w7E-rZfk54dWZEJBuiB4hqWxHlv8XqltmdR7j7r3zxBcK7OS0-WrrSnPbHSMvhDUjDUwZrDHtzwT96qeAytSn1eez73casttHVH717iX0iHTqpkt9mTEsFvfrTGguGLq1WB9a992qvqTK6opjnjONDoQ0sVJG_0GpHtiiDtHuMvILX9dYhsTz3ZvKnjQQTCTPu5uKlL-q2d9L3JqsOazyU20j13tjH8bDxmLrL4_GMT-T2Wg7_ZOkMAMuDJ5ECi1Fk5yZMOGZK_0wnOFukMQnEdHBllZ1pWl9xVPFQFCNvdvErBdXEQAWasTkFb0JpWxGv5Kmh7uxnGJSsHdxZrAda5i_PfA0uDyQKFe_AuJmSSg_gIgb5ZOOyMnHzj-EGFntFAs-QuCw_6Nug93T_8SxtSmWljcSHSKCUE2Uxk2HwKqeAKfW2HOTBG783eIKnbddNSPexQS4gp9GoWiNnUL071HPFiAothTPGic9mV2u7YhAWxIeDBOc8ihXu5sr01B6t8mdhZ1b5pz79f5XRNsBTsuo3hgIP88XGeU3qk00lrrOskn0mfZzVR9SO5IqaYJ9BrXS5PyYI2PU-6ktYx_u4z7IrHxrhk8R-MfjQgbFm4EuvtX-BiZWehTUjcj545y_d264CTz2hTg8uDW2gKouNgZAtNS9wmV5cyOS1mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/614a5bd431.mp4?token=GZ_w7E-rZfk54dWZEJBuiB4hqWxHlv8XqltmdR7j7r3zxBcK7OS0-WrrSnPbHSMvhDUjDUwZrDHtzwT96qeAytSn1eez73casttHVH717iX0iHTqpkt9mTEsFvfrTGguGLq1WB9a992qvqTK6opjnjONDoQ0sVJG_0GpHtiiDtHuMvILX9dYhsTz3ZvKnjQQTCTPu5uKlL-q2d9L3JqsOazyU20j13tjH8bDxmLrL4_GMT-T2Wg7_ZOkMAMuDJ5ECi1Fk5yZMOGZK_0wnOFukMQnEdHBllZ1pWl9xVPFQFCNvdvErBdXEQAWasTkFb0JpWxGv5Kmh7uxnGJSsHdxZrAda5i_PfA0uDyQKFe_AuJmSSg_gIgb5ZOOyMnHzj-EGFntFAs-QuCw_6Nug93T_8SxtSmWljcSHSKCUE2Uxk2HwKqeAKfW2HOTBG783eIKnbddNSPexQS4gp9GoWiNnUL071HPFiAothTPGic9mV2u7YhAWxIeDBOc8ihXu5sr01B6t8mdhZ1b5pz79f5XRNsBTsuo3hgIP88XGeU3qk00lrrOskn0mfZzVR9SO5IqaYJ9BrXS5PyYI2PU-6ktYx_u4z7IrHxrhk8R-MfjQgbFm4EuvtX-BiZWehTUjcj545y_d264CTz2hTg8uDW2gKouNgZAtNS9wmV5cyOS1mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/453647" target="_blank">📅 00:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cedf8c9dd.mp4?token=UzRmAFErm_8CFjPT5ODRmJnecFA5tCFAVPehY5aWnexSY0BJ-gnUVfRDZmkPowBNBcfxAhdPbYSFXPaZ2jLgTUAZevEr60XoLF4nxVA6d1ptcCbvAu3s0gEuHu9joxeqxfx1hjGKzHEUTi1BbPBK7plyCUglQQwyn44v0PA-NgyOhdV4fET7sWQ2RvIRNPjD0U-3OtNVZk0Y1SvnTJZ4mlxD4qjV7hsbEOaSw6ZZ55ANL_mjHvgb3jZBJjQr2vn85y85Hgrlo7aQZv_b_2z6cjmmuzY0uaAF86jb7z1qE37lEWs_69xQAzXAtS7TFeux5KjSv7S0rGoaZXSloWLTqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cedf8c9dd.mp4?token=UzRmAFErm_8CFjPT5ODRmJnecFA5tCFAVPehY5aWnexSY0BJ-gnUVfRDZmkPowBNBcfxAhdPbYSFXPaZ2jLgTUAZevEr60XoLF4nxVA6d1ptcCbvAu3s0gEuHu9joxeqxfx1hjGKzHEUTi1BbPBK7plyCUglQQwyn44v0PA-NgyOhdV4fET7sWQ2RvIRNPjD0U-3OtNVZk0Y1SvnTJZ4mlxD4qjV7hsbEOaSw6ZZ55ANL_mjHvgb3jZBJjQr2vn85y85Hgrlo7aQZv_b_2z6cjmmuzY0uaAF86jb7z1qE37lEWs_69xQAzXAtS7TFeux5KjSv7S0rGoaZXSloWLTqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از رگبار باران در جنگل‌های مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453646" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراق ادعای ترامپ را تکذیب کرد
🔹
حیدر العبودی، سخنگوی دولت عراق اعلام کرد دولت این کشور هیچ‌گونه اطلاع قبلی از حملات انجام‌شده به خاک عراق نداشته است.
🔸
پیش‌تر رئیس‌جمهور تروریست آمریکا ادعا کرده بود که بغداد را پیش از انجام تجاوز مشترک با سعودی به این کشور، باخبر کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453645" target="_blank">📅 23:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT4sr5tU8UVsr-VR5wuzt54uLTgCFPmDJ9_J6CfjCbEaWGCaopN1g7qE9ejcg2VkpS07Q-GypLh-nim53lcnSoFGAGeDP_8EeVGFvhkGYTJ77w6HGjtcrydHtv7_LWMsb1JUO8v6k_OZl4x_-dm1TJBnxT5zvxOqt-YEnhRgNsCL5OBd3rQCMGd6_doW-OCmE2f10jQOjlcEawBXL3gYrfQ_pEEaHYV8XPzC4SSe6dS-S5sBhEQT95QXtg3JgAbZMhyaVPv9X_daevWN6TaMwKkMLb9CuPEdA1Hv4QWcTKYsLulx8OBINx6I3answarTx-tOYP9eL4Lt3VIQ-4eHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ یمن: به مصر حمله نکرده‌ایم؛ فقط عربستان را می‌زنیم
🔹
یک منبع مسئول در وزارت خارجۀ یمن: شایعات دربارۀ حمله به تأسیسات گازی توسط انصارالله در بندر دمیاط مصر را تکذیب می‌کنیم.
🔹
موضع یمن روشن، علنی و صریح است و فقط رژیم سعودی را به‌دلیل محاصره و تجاوز مستمر…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453644" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366698c896.mp4?token=NWuvsV08VehNFMDQQVYFTiGwkeyde1ljDfS2fB1h07mAQpgBdxmeYtIHqXDS_DOEmGlXFU2P5gH0qqouXnDSDE6kL2DplnoamnQtaglvtqkNosnwFKKFXQwKUREIZkuUVkUSaOUU34ULLS4z_QzwtjC5Redinc9kNrNmyWSKxCvsVvBLqormYdO-KoFM8YgrXLQRsoMvlkOOgQhsvai486IclkA0AxGcmqojSTmp8lN_d93QX5APkL0dPlqD8u3qcvKg4b43iB-PBf66lAgzdsWiUmCVS0w0HhhU_C-9Cdo0oJ4rqkLyiepjEYwk69MrPOqMEUSaRSbZ136wpEn-ih-jUCvks0LOVDl_e_dzY_ddfg0Com3hYDubvuBJWaK7ogELfSNd8DkPRzc4cczAD2oNT6Knyi2j5p0NfWyxHte_Diz7Rg0tP4AXO3PSR576U3mMdAmJfW1WWDar37xZmss6lp8oQlVq_FG-ROPSFvI4OH80bTM0FCAMdpAMw6lFSV_HsbHaO0ebJKB-rA9UYCylWKv2DXG2izF9Vt3Xo6HpHpMba2FFtn3giA9Klpehypb_91fQgcNaCU0rNv67I-ViWZ6CDfA345s6TC2w6ZgIBcQo13-oho3u89aOg8NmZaf34kF-xLZZLZtOzP8rRwPKr5CF1w1etJNT96zuOXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366698c896.mp4?token=NWuvsV08VehNFMDQQVYFTiGwkeyde1ljDfS2fB1h07mAQpgBdxmeYtIHqXDS_DOEmGlXFU2P5gH0qqouXnDSDE6kL2DplnoamnQtaglvtqkNosnwFKKFXQwKUREIZkuUVkUSaOUU34ULLS4z_QzwtjC5Redinc9kNrNmyWSKxCvsVvBLqormYdO-KoFM8YgrXLQRsoMvlkOOgQhsvai486IclkA0AxGcmqojSTmp8lN_d93QX5APkL0dPlqD8u3qcvKg4b43iB-PBf66lAgzdsWiUmCVS0w0HhhU_C-9Cdo0oJ4rqkLyiepjEYwk69MrPOqMEUSaRSbZ136wpEn-ih-jUCvks0LOVDl_e_dzY_ddfg0Com3hYDubvuBJWaK7ogELfSNd8DkPRzc4cczAD2oNT6Knyi2j5p0NfWyxHte_Diz7Rg0tP4AXO3PSR576U3mMdAmJfW1WWDar37xZmss6lp8oQlVq_FG-ROPSFvI4OH80bTM0FCAMdpAMw6lFSV_HsbHaO0ebJKB-rA9UYCylWKv2DXG2izF9Vt3Xo6HpHpMba2FFtn3giA9Klpehypb_91fQgcNaCU0rNv67I-ViWZ6CDfA345s6TC2w6ZgIBcQo13-oho3u89aOg8NmZaf34kF-xLZZLZtOzP8rRwPKr5CF1w1etJNT96zuOXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر ایران در عراق: آنچه در مراسم تشییع پیکر امام شهید در عراق دیدیم، فراتر از تصور بود.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453643" target="_blank">📅 23:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUgbjEF3xiNYbzDqnTomzLker_cnWgX6e8YLmCAyX9FdAhs66_tW4HZD7_h4_dPNnxQmM6mxrX5LP2KGinxoFIFoD9kcv_3bgDeXGBRBerGQqJoXJpt37UGrQO7DZEyh9Qc965Ieao9ZnBFFuj8umjt4LavFI4thFU-jrzhfZiNsO6AckP7un0Aq3qARPxnKUrXY3pvB1xAHqYAR2wLJr97Wbg5dgX36Wh0vlGZFVc5jm_LUytiqesCZzIJsq7-cE3QzaARTODt5T2T5e8PJwiPL3_EAqmph1IzZ2J9lJL6OgV1SgfmlsZctVPfvbtsj3GK5H_fC7dqyj2ZRMoqHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاکمۀ سرمربی کره در پارلمان به‌خاطر حذف از جام جهانی
🔹
هونگ میونگ‌بو، سرمربی سابق تیم ملی کره، به‌همراه مدیران فوتبال این کشور برای توضیح درباره عملکرد تیم و تصمیم‌های مدیریتی فدراسیون در مجلس حاضر شد.
🔹
در این جلسه، نمایندگان کره درباره روند انتخاب سرمربی، برنامه‌ریزی تیم ملی و دلایل ناکامی در جام جهانی از مسئولان فوتبال توضیح خواستند.
🔹
هونگ میونگ‌بو که با شکست و یک برد در جام جهانی پیش از این با انتقادهای زیادی از سوی هواداران و کارشناسان روبه‌رو شده بود، در این نشست تلاش کرد از تصمیم‌های خود و کادر فنی دفاع کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453642" target="_blank">📅 23:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syUF8md5tPExbflJsGlYpyk6qeHPEUXS7HT9hovj4n9CRHazBRagj8vntOSSNYcX4lI0izgn5XGFSg-zJagKU52AOhGNo7a4_7miUha0qr6wS9uw7FdNOaB_HPFZOSAhYmE7Jt4iQQKjrJP1oBWenfGgKazqr5ZxbpJHkVeEVk0JJ9SBFhX4TT_XszS9h1VIgOLc5xezvYSOFJbCkkSTBNd1ilL9FUY5zUIPXg4wJ4MqB-V7omx48GmGoVa96AZzkOSMkdyL2o3VOhdtlyMidyeohmz8_fpUk19hTmplszWnXbut9LbUfrKiKGyUngzWYMTAQjhhyAxhVYmHK6mUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlVMLlqzkxHNOS2MQGQccM-8z6WqU88bYT0LFiB82usfV_-Nb6nRZJHXxHlUQkWXEcEsvpEDMfpMc3czYOnLj7mSafxDp0MpMElTI-wfARxSzQJCeMtzFHV-rzsrc0M6cmCUVWYwTc8marKF4LCjaOM_sO49l5ogEeTPYJ3T4tBtxjVpMAY38dRxroxU-2jIMPp91NWo8pkvQRaiwspqGxW5uJaYRfAC1oMIJIl7BGL6bdEq55BoROaO7u7xEM0pCp5-wk10N0yG17JWE_rXrMTcEcBBfgaB03NzA1LS6C_rDs4NM0wa73gw2h--gT5BSdpJ6UYRYyHfafrky4xW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KX5gFKsftJMCCZuN5RU7F1cBkreL-unHe138bzfsJlbm5h0kZeWInpYdjttnsz1NsCgjASN2uw1TVheV72nW8_YIHmTm4qd-EnrzHd2jMltKZ7D1CQQlv_552WbGI0k5iqW8m91lYtwHsdjfVAcC200nFdT1DmIkmf_62-wx4lFi2xOQZDlApdPwNyQRGwvIa_yuH-NTXIxAXulJL9ZfXcl57Qg_xFcT386mi6nzLvjmy4SHHCd0PooYLlr2ZeXYM0pjoWURyN7T7csn6Cl96XW_mZ0XfQUk5FaJglIWdxz4vz9-dZVQt10hHuHsAw-hb6CwPYO3XjQG9gWnIrqQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7J4uSGY7d4A5gpcFIzVyHYSO3ChcniSadZxtX2YbdKr27nkrAUl8wvtYRnmY3f5pjIj8qGfxAsLQljkhiA6dGQm-dDjJWfd1L7eRz3GlN9Cd89jsZnr4mFTfnVmc6HBqO0jjqGFQyf2FAhFH5IinwaDUzRUpNZdT_dK7hYOzcJjpePmyThZYVuq2uCReR3ZlptfGuV8aH1uK0E8Ypk-VI8NpjN8W6qlRWo_oNgtuLEEV5fic2Gfw3GfORqCs4T9ulvEiArXnMF8QADc7dAeoPr0HFlfVCKXYXFAkz7si3Oj1j-wNH1u80NlG34qRh3IKdEeHfOUSjvf4-pPAbcgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wb_Rw-W9U9zLrlj76wK6OAGvjlrJLEsZLZdl2uldSAsYK6WP31iir40dXpU8DIG8sbVNujqSx2ReIfcCCdSPkOSYS_c43jIqeoWlpBCZRHjEG5-HtSddLdeIeiahyxQOi4V4Xl9MbgLmHVOPMsfvaq24UDBPStVdfoVozMdAL8YPXrBEOS7cX41vCLLirTxTDy9eOnmgdUzgG3-usMNi7tqpGfjy2YENCy7jjlPLq6D4Fb7-qM8kFJbuzxAHXlj8jEsB6ZlD3UXs8vbd2Jy5kwuF2XfiU2Ft6YhhLeCB2DsLy_cyPlSozez_OZUCsAOzQOEbMX4M4eFNTaJSWyTDtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۲۰۰ متر از خط ریلی گرگان-تهران زیر گل‌ولای رفت
🔹
مدیرکل راه‌آهن شمال شرق ۲: به‌دلیل بارش‌های رگباری در بندرترکمن و بندرگز ۲۰۰ متر از مسیر ریلی دچار گل‌ولای و رسوب شده. عملیات پاکسازی برای بازگشایی در حال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/453637" target="_blank">📅 23:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZekmMwkjE9XS9tV5c_E5rJkeHTJGSdnt9JXJ4wK1d8ip2ri2uSe32c7Ac-_k4Tyn5ljVgCmqjaG5neIRNifDaGC1yYvu2YwHKyne-l4HTEGjp8Xh3t89kBrFVN-51X3YksIj2FDyzXxm09MgMVRk-ELPClNFCtkc-ai6GeKXfqmccHwj0OXvFDSMRUbo7cTZgysdUvLKhrveYjtyXcbIuQ7k-49PXQPF1kdM9sNVPJkamTdvuAUdnMTodlYe7fzmxcB8jbgqNQ4oQQToR3C44JtzWuSwgsUuQj0xyCgjT9wZQFuSIcr_dHy8tv0PJrPAtuDfrp6eNz7agdU-usYFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش بذرپاش به توییت کذب یک فعال سیاسی تفرقه‌افکن
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453636" target="_blank">📅 23:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دادستانی علیه افراد حامی محکومان بی‌رحم و سنگدل کودتای دی‌ ۱۴۰۴ و جنگ رمضان اعلام جرم کرد
🔹
پس از اجرای احکام قانونی تعدادی از عناصر کودتاگر دی ۱۴۰۴ و عوامل دشمن در جنگ رمضان عده‌ای قلیل از چهره‌ها و افراد با اتخاذ مواضع دور از انتظار به طرفداری مستقیم و غیرمستقیم از چهره‌های اغتشاشگر سنگدل و بی‌رحم آن وقایع پرداختند.
🔹
در پی اتخاذ مواضع مورد اشاره و حمایت از کودتاگران وقایع خشن دی ۱۴۰۴، دادستانی تهران ضمن دریافت گزارش از مراجع امنیتی و اطلاعاتی و رصد فضای مجازی برای تعدادی از این افراد پرونده قضایی تشکیل داده و پرونده به مرجع صالح ارجاع شده است.
🔹
دادستانی تهران عنوان کرده با افرادی که به حمایت مستقیم و غیرمستقیم از کودتاگران و عوامل دشمن در داخل بپردازند و در برابر احکام قانونی رسیدگی شده در مراجع مختلف قضایی اقدام به تکرار مواضع معاندین و‌ شبکه‌های وابسته به سرویس‌های جاسوسی کنند، ضمن بررسی دقیق محتوای منتشر شده اقدام قانونی قاطع و بدون ارفاق خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453635" target="_blank">📅 22:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار ایلام</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e49f71821.mp4?token=Y-VpGZ9DHhH8POR5D-4ckvRP39kHVfOSbWXiMFm8GSEydpEo8rmHaue_LqWEh2Lg-m91gst-p5eGYHWP1j0H7oI4xX_s-t6LFxSUBhOHn26_SHbusUk4A0_rC78bInnl_3HHdj_2HBdgs_aNypOM3GXGZUSVq558MSSk7nqBV5_SIG7nYkIzABZbcamh37hfQt61jSZtm49FuKSwQTMEP_rRBswXYtCLKETc9XAsmkPKYi5Ju8IRQZXgDPq5FHieHfXCTMvtJ0Ji4QOOV2jI5m2_PxOUIK04Y6nI41T86YK93vm952ntHw6xYMXhINSs8PQ1QX1gA9kBqPzJZurB-alm2vVpd-m8YPXPyCDKleWRAMnRJPNd-tjty2aLVR2r1R9W5j88AFpKwz_-YHmau9wTR0_pXWJGHoB59Rj0W15_Z16ovqAwzg9TXdmVEwR0RfyBkkDoTS0VU7qmoYjZBB7A1TnHOSu5qURkdRNEs8q4M_Jd49wcHA2d8dV5tj9DhCy1SSVvGiw5rJ5AnbvZzrukwtkc8bHLKzPmN1Mpxgb3NI4AYX1bcbqpcau9JA4aK5T3oyDif8Ct1LjXAsO-aRia45R3xebukBOGlhaTLA5lrZ_3OWTvjtMEPltNPnpXKzDd2fBHOcS0mETuXnJqlPDG4jbJESB8D6746W95Rxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e49f71821.mp4?token=Y-VpGZ9DHhH8POR5D-4ckvRP39kHVfOSbWXiMFm8GSEydpEo8rmHaue_LqWEh2Lg-m91gst-p5eGYHWP1j0H7oI4xX_s-t6LFxSUBhOHn26_SHbusUk4A0_rC78bInnl_3HHdj_2HBdgs_aNypOM3GXGZUSVq558MSSk7nqBV5_SIG7nYkIzABZbcamh37hfQt61jSZtm49FuKSwQTMEP_rRBswXYtCLKETc9XAsmkPKYi5Ju8IRQZXgDPq5FHieHfXCTMvtJ0Ji4QOOV2jI5m2_PxOUIK04Y6nI41T86YK93vm952ntHw6xYMXhINSs8PQ1QX1gA9kBqPzJZurB-alm2vVpd-m8YPXPyCDKleWRAMnRJPNd-tjty2aLVR2r1R9W5j88AFpKwz_-YHmau9wTR0_pXWJGHoB59Rj0W15_Z16ovqAwzg9TXdmVEwR0RfyBkkDoTS0VU7qmoYjZBB7A1TnHOSu5qURkdRNEs8q4M_Jd49wcHA2d8dV5tj9DhCy1SSVvGiw5rJ5AnbvZzrukwtkc8bHLKzPmN1Mpxgb3NI4AYX1bcbqpcau9JA4aK5T3oyDif8Ct1LjXAsO-aRia45R3xebukBOGlhaTLA5lrZ_3OWTvjtMEPltNPnpXKzDd2fBHOcS0mETuXnJqlPDG4jbJESB8D6746W95Rxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طریق‌الحسین؛ جاده‌ای که عشق را معنا می‌کند
@Fars_ilam
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/453634" target="_blank">📅 22:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYQC99oZ6v-nuQkuSR6xvhyQcrHekv81nbsrpj7qCx2sXrj8zR_iNBwoMQ1zcI9T6F9BkcVVVFZM8gzXzpjQuBKjnOYLCV4AwSXAigwWvjKgm6396QkynmZz5v09vtkdmTP5Uy6_NycYJIDNXSKxd9KZvrJBV8DNzJBKOYYhcpQm1Vnp0ZRjANVXieBvLfxF9NBQfGZdjAu3kIb7tosjgTXihg3Zv3-jntDJ3Cw1sU5guDfEi6t5HoDfn6hEcDeEQzUTIwt1Uut0B7yfUIZscNyUpzGSWUs6jyByZTUQJgXpkuFBuZC3Y8Z1mtsYI1J-9keirAX7qt-63El2PnnF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
۳ شهید و ۲ زخمی در حملۀ آمریکا به محله چاهتنگو شهر قشم
🔹
دانشگاه علوم پزشکی هرمزگان: در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و ۲ فرزند ۷ و ۹ ساله بر اثر این حملات زخمی شده و به بیمارستان…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/453633" target="_blank">📅 21:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad5499559.mp4?token=eRb4MjNazdAgeOc5PDlrHeebkm-fnqSpLyOySXb85WZFC5aBJboZ9ilxT3pq-vjPF5ZGWMfeBubTQmpg6NxqG8ooTJoO9Pi-3jYXpCpaq19dQc80az6M8x2sAfzjsxWW6pv5Yk8l-aU424_bONKzMdUlRuZDI0lpyodIMs7boLhzBDqIfQcYDKZ1pXa_OQLs7PHXheh5_X03WKJw7BdfzLnebTPrZ9ZweNBh-raVzNrX5xmTsF3nCRJOrAqnXoz5enKRFGWeL25gyGBqQgBZjsOrkWOUWfS8_r-qmpuKWmuA6lQ8_-IUYZ7a9vUa_NDRniEaYr_k89hHpcbQn3aBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad5499559.mp4?token=eRb4MjNazdAgeOc5PDlrHeebkm-fnqSpLyOySXb85WZFC5aBJboZ9ilxT3pq-vjPF5ZGWMfeBubTQmpg6NxqG8ooTJoO9Pi-3jYXpCpaq19dQc80az6M8x2sAfzjsxWW6pv5Yk8l-aU424_bONKzMdUlRuZDI0lpyodIMs7boLhzBDqIfQcYDKZ1pXa_OQLs7PHXheh5_X03WKJw7BdfzLnebTPrZ9ZweNBh-raVzNrX5xmTsF3nCRJOrAqnXoz5enKRFGWeL25gyGBqQgBZjsOrkWOUWfS8_r-qmpuKWmuA6lQ8_-IUYZ7a9vUa_NDRniEaYr_k89hHpcbQn3aBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  آسیب به ۲ خوابگاه دانشجویی در اهواز در حملات بامداد امروز
🔹
استاندار خوزستان: در حملۀ شب گذشتۀ دشمن آمریکایی به شهر اهواز ۲ مجموعۀ خوابگاهی دانشجویی آسیب دید.  @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453632" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453625">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQ6pfMSOa-XrWdVBE4PLQ51A2xhzQQYfsP1fVL5MG2cCRIFmFKOvlL8fCkWEXMeCSTSrGvocdovfzXfAe6Sv_NedgHWF384K3eaqRkJaG00R8kdAEaa5FClj5Va_BKv97iSU8G89G9IWwB1iK8UYjkoueI1bWDi3eR8YP6A7u_dROKp9-TmLNa403CzSkkleSH0PmDxE7-LlUYAgZsWJ6PUJes9hKtEIJRcgDErqwRYDJ32q9lcpwn2i8A8b2GrOO45Z0e5-oH9joRVgGjfIlP1vVGreix6bws9d6mzy-pSd_9EIhAE5jNX6buugDtw8jJZ2qZ_vNh-qFuIctGLLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4r8a0r939qScSoZfA6y1XZNvv-P2BrBGqLFhU-KTXHquZLSWFIPXSgE7vF1wiT3_ww9HTM-J5TJ-frGfQaPDNYmHkiSywWxtr-9NdV54c0guW1ulaCh3CC_d67eQez4QAbJX2H-3qFU_NLdhBi5n4ylhwzA1i7RPkqA8pOzgFv3s_o2jwBNtaqI55XnUM2S9HItL4SM_YpOPqkUd4K6R33-mprc1W3EQalI1pwF26RvF4wFrfPjPGJpBXJeZLPcJtL8yTVD7Kw3CzzHF0Paz1Ili1B9hFgJ5cV96kHiOWQb65r8PHEmDcwlbqkiVuhleebng31uaT3jEy75SPC3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lId04duESrq3DqjlVucI-HLX3PuugWBQQ9Tax0Srxv5Ed60SgBg0C3KvQMC1hZMZnBC-cPkYUDGWGBWS2GwPCi43T3s5xuYUHoTVS0v2sLzNgqnKlVId0TdETxrSR4_7aSUR7vp4fNMtb2pnhlrcKBBlA0AR-JN8Iw6BgWaSRXV5xRHxbtoJqUF59Pkl7Vzj315thFPJ6xW-ofgFV6OBhVxEeB7xVHLKtqrKvPAD6bb3Tc9W_qvQp0aBUhcaWqZpjjXcr1Ql1ItZh27eLbinphFXNkRevB4mYHhqEslEvAbdpIHPyePNd4_DFT3ewqA9Ko40apFIdSL8EI5j5nl2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMRnKJyCnP5xUkMabBjdZ9KFwgsrLoIyvLh9yx4-FJxFhM2JVXLzEgknA_ka3VIojcqqwVmoRz9isRy2WzDAZh1xaBzKQqoLxekZHLZQ92MFAl7K9jwS-xmu6LY22btrwa-wR1u0NYGcow0pjbzwUKffdxMEYEczB25vzgNFhea_nyqTJbyu00cvgT_T1anCXIfrgMmekZvAPzqjAWCj0dGiGnlhkdzSxR0bxFgJuwbzp-kSiuap7ofsHuHDD2x9otNwGJRd-LsQATR0lNeiG65OlYfvdfYBhjumewiMNvsY9f56meU-FfX7hshxtkwQWl7DW7X13GIaorI33H5e3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8l1CINp-0G7BRj4NIaJvmdhed0E02gLJ-rbdsNeb6NJrhv2wb6NaTm8EvJ2I9zm17V4iC-arANHWzGnWlcaNK9On9s94eAmntqTIWb97CVfMULJrnOZwSWiDXdUe6Ga8q2zHH6VvRkHDAQsNIY3j5wOZDSuRQwoMy0l3ftPJr4pN6aRZbtoLaIzhHG2HblfOqmEmdEnPN3GlwdZNbaGohsqBAidzFKoo2rcBcO5u-QPrS61z5JPYZIqWQFGHaWmAh5muMNhnkA8GB1W06pIc5tAnLxTzmpOB7dztjOKxTouVr-fZFu9-0Ar0_fgygrXGEn8_J1GSC5x0GrNEseYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyROC6VXt7uphVg6wNHlfWCkZU7RXTv1kPrW-StadnNuZ72PSI1HXpaXrWk-HsrSondLoDr-o5nooSskFNU-nCAMup-qUwI26SUKuBo72ZcuzgsO6mIBxPN9hC4sjw1k14-qTTWxnnKQTqrIQW8iSmSQAz6yegy-P9-2_UFzYVNizjg2J01RBYj15MHTEU4qv1c8glxbhOZc7qp1VH3ZY7VTtP1wELUAkgoEMuvF68bH60UItujSwNezZ5aL-4J7zKf9vFw99WTfd-Wbr7V3_JecFtEzNZMDShZZYZkPLK7dJz8d4jwJFc67bHk3b_kG4HawNb7qviG0Yw4q2Cz9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wAz69hRMvSLYuGsH3zOrCSYw8jA6akk3uEBHNK1oxI3tb_mHzZq5bimQnvwMIQYPIHA_ZsNKE2GvBoTeyp02p173iy6v-NP-BC0ic_0gAe2uUIz0m2JgZWtOvXQydjdASo9hAYy176k8OEvx8kHylZtVdbt8hidSMaCejBrlkOy5KKgpydWAib8Lquo8yrwMXBZ-Jv2UEuFiYS5C03PJAcjrASrAX42oHMfZeBh6IrX948eYO0VvUegIFFu9zXS-4PFCc8sikBDan6q_HDSy_otxCeLiAqXJ-pH90wie6bVXR7qbBpykczja03otF9C94XLrT7oCaN3hxqCd4M2m_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تشییع شهدای حملۀ تروریستی آمریکایی-سعودی به عراق در کربلا  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453625" target="_blank">📅 21:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453624">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34983a6e00.mp4?token=eXC724WqVTVM9k6sxC43zfWRXvUGY75URkUwZ0NuCz4aElOih_li12682Ww_GBmmKgiEXWMvs0mDz9-QVrENQ_z6D6u0E6_OKRUixbJy-m4JFFVQLYadQO_Z1-q_8ibccLork7Surr731jteM9HY2fYIGLvYCfccI4_wocY6_iCQqqtKsP14cFF3HmrbRNow9iAu4U_dBl2J25QBVDAcYP_BYLAv1M1ud8rUVUeLQ2grm8HfppKiVLDvJ2Y62iq7L-TXkCWyooI-UKE3t3Fx07vhScOFHPw_skZDGlswXQicZzZy8QGltmeqjhw1RzPuQtIIeANO1iBEgyKgOBVmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34983a6e00.mp4?token=eXC724WqVTVM9k6sxC43zfWRXvUGY75URkUwZ0NuCz4aElOih_li12682Ww_GBmmKgiEXWMvs0mDz9-QVrENQ_z6D6u0E6_OKRUixbJy-m4JFFVQLYadQO_Z1-q_8ibccLork7Surr731jteM9HY2fYIGLvYCfccI4_wocY6_iCQqqtKsP14cFF3HmrbRNow9iAu4U_dBl2J25QBVDAcYP_BYLAv1M1ud8rUVUeLQ2grm8HfppKiVLDvJ2Y62iq7L-TXkCWyooI-UKE3t3Fx07vhScOFHPw_skZDGlswXQicZzZy8QGltmeqjhw1RzPuQtIIeANO1iBEgyKgOBVmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد شبانۀ زائران در عمود ۲۸۵
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453624" target="_blank">📅 21:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453623">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tED6XOYjBfVqFv2u9vJn4SZcNHIlWFfN0aBDSgDlY7665UhVJX4x6WPrYVsB2qVL-MbHEbQ7DsTQ3wUZ8KEwOj9jztUKFqSN7aLj6imMMBB3ZPFPT8KYHHVxCKen1jrbJuTAcPMxSEwRlVXEjPVqYyAm5qMzDd3gbDFH9vyuiX63Q8hKb2x_SW0TDTL5PzY_6ymXD2CeA5-wmwLY_f4NslaQO0gAy-4C3L_M_zTW_Ab_SVps_8VpxUyy9vDWw9nebNXmm-CoDRQMdGhxaS76EXPvlZFmwSEmC22O3eos_EYFDoQh9wnVzkTntJkc31Fxpe1aqxyTRMFc_WEG7Pke4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر عبداللهی: آمریکایی‌ها و مزدورانشان، امروز تا اعماق جان ‌دریافتند که تابوت‌هایشان جزئی از تجهیزاتشان در منطقه است.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453623" target="_blank">📅 21:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مجلس سنای آمریکا بار دیگر به قطعنامۀ توقف عملیات نظامی علیه ایران رای منفی داد‌‌.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453622" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453621">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15bfb7bca.mp4?token=D8eiFRmWhlul9YgPY3qI7QsAgBaSxwLEAmu2sm7DW90LzaWa_rjh1hxOvDFqTYEU1oRR0e8vgYic_nl3-oSRgE9ysPvZehg6UxOuGv9oYflYQRjtk-mK2Hpf46zlT7HXSyQ2LDHvH6vT3n-CmHp1XFynvbxpbSj9_NbMtO90iyUCM6uqk7GZYlflqk7ZejBNo7DXezFO4YDtQ1qtV76hz-Z1gmcxN6iCRSeMk2flZddIQf161-0cG09YDqsYwVJOoLgNV73Kv3BThuCPlOgDpECC34SrvbIl2iB0yFchEsZTO_kN98UEcm1fRxyVQdGXa_CxlVVZh712RI9j5YRWIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15bfb7bca.mp4?token=D8eiFRmWhlul9YgPY3qI7QsAgBaSxwLEAmu2sm7DW90LzaWa_rjh1hxOvDFqTYEU1oRR0e8vgYic_nl3-oSRgE9ysPvZehg6UxOuGv9oYflYQRjtk-mK2Hpf46zlT7HXSyQ2LDHvH6vT3n-CmHp1XFynvbxpbSj9_NbMtO90iyUCM6uqk7GZYlflqk7ZejBNo7DXezFO4YDtQ1qtV76hz-Z1gmcxN6iCRSeMk2flZddIQf161-0cG09YDqsYwVJOoLgNV73Kv3BThuCPlOgDpECC34SrvbIl2iB0yFchEsZTO_kN98UEcm1fRxyVQdGXa_CxlVVZh712RI9j5YRWIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یورش آرش‌های ارتش به مراکز و پایگاه‌ آمریکا در بحرین
🔹
روابط عمومی ارتش: در مرحلۀ بیست‌وششم عملیات صاعقه  و در انتقام خون پاک شهید امیر سرتیپ دوم خلبان مجید کاظمی، خلبان دلیر سوخو ۲۴ نیروی هوایی ارتش، پهپادهای انهدامی ارتش، ژنراتورهای برق، سامانه ناوبری و ساختمان‌های اداری و پشتیبانی ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین را هدف قرار دادند.
🔹
حملات روزهای گذشته و همچنین امشب به پایگاه‌های آمریکا در منطقه، با وجود سامانه‌های دفاعی متعدد و تجهیز پایگاه‌ها، تاکنون خسارات قابل توجه به تجهیزات و مراکز استقرار نیروهای ارتش کودک‌کش آمریکا وارد ساخته است.
🔹
پایگاه شیخ عیسی بحرین یکی از مهم‌ترین و حساس‌ترین پایگاه‌های آمریکا در منطقه خلیج فارس و میزبان هواپیماهای شناسایی، از مراکز مهم تعمیر و نگهداری بالگردها و قطعات پهپادهاست که با حملات متعدد نیروهای مسلح، آسیب جدی به توان رزم و پشتیبانی رزمی نیروهای متجاوز دشمن در آن پایگاه وارد شده.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453621" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453620">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b780c515.mp4?token=I-bIVcjpEn4Y5jgGeC9kdMz3chSHJVTwLalnKT_cYQrVDWlq5Ji5oJV0-dxrpPDky52J0Le_NQL8xLflMlJkgxLCzPFYe_zvzrX8pEyCe4YvWzoq6cS5HVmNMdKEdNCAcd3jUxvHpvTH2rkjuTfjekAsjU_5SyvXxRPqSm4S75EpuTOch9eeixKkub2aNYzC1NFBE9Nqw0yPesh8iskE1oAjUa2ww67HY9owB5I2H1A1y65ZgaXwHoeq2zD9twvpdM_czvOm_AVyU3ukGZAU-ih5etL8vttdO6ak6GVUMyk_fhimdneSjwFZrV-KgLBQfutB0px5W9rQi8rKS0g9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b780c515.mp4?token=I-bIVcjpEn4Y5jgGeC9kdMz3chSHJVTwLalnKT_cYQrVDWlq5Ji5oJV0-dxrpPDky52J0Le_NQL8xLflMlJkgxLCzPFYe_zvzrX8pEyCe4YvWzoq6cS5HVmNMdKEdNCAcd3jUxvHpvTH2rkjuTfjekAsjU_5SyvXxRPqSm4S75EpuTOch9eeixKkub2aNYzC1NFBE9Nqw0yPesh8iskE1oAjUa2ww67HY9owB5I2H1A1y65ZgaXwHoeq2zD9twvpdM_czvOm_AVyU3ukGZAU-ih5etL8vttdO6ak6GVUMyk_fhimdneSjwFZrV-KgLBQfutB0px5W9rQi8rKS0g9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزهای عراقی چه دلبری کردید
برای مردم ایران برادری کردید
آهای اهل عراق، آبروی شیعه شدید
🔹
شعر تازۀ احمد بابایی در وصف حماسۀ مردم عراق در حمایت از ایران
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453620" target="_blank">📅 21:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453619">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4074816569.mp4?token=PoW7Qy5px_HienejS3DW-glm5mtZwgS6dgpTz8UhDyz1Fne1WeK8FbcgFOWx7SleMFmhJNsjUzHSz7s-CHdJRLzsjBSi9kILAs0MQbrK5okxkboQ0aMiCotT0AxOLfzUFJGg8yd68Z-owoXaSkhE098V5ejP_BVJgBHKpsrGit7jz14J4utAP3QHBRWgZV5ex7kk6qql0nCgIh43J-ZmipzGe75rHR29Z3cRdN80mddhhFw3TNcTI-1KRVc5cZ5wGL-jA6jUJBiY_4nVHK0aMnGbI5MhEiQ9gdPqwohdBLv3fCPapblVp76gJ2Lk35WfaVOiwAvPZdA_baYeeyFanzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4074816569.mp4?token=PoW7Qy5px_HienejS3DW-glm5mtZwgS6dgpTz8UhDyz1Fne1WeK8FbcgFOWx7SleMFmhJNsjUzHSz7s-CHdJRLzsjBSi9kILAs0MQbrK5okxkboQ0aMiCotT0AxOLfzUFJGg8yd68Z-owoXaSkhE098V5ejP_BVJgBHKpsrGit7jz14J4utAP3QHBRWgZV5ex7kk6qql0nCgIh43J-ZmipzGe75rHR29Z3cRdN80mddhhFw3TNcTI-1KRVc5cZ5wGL-jA6jUJBiY_4nVHK0aMnGbI5MhEiQ9gdPqwohdBLv3fCPapblVp76gJ2Lk35WfaVOiwAvPZdA_baYeeyFanzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب موشکی در عراق
🔹
موکبی در شهر سماوۀ عراق که تصاویرش[ساخت موشک بالستیک مزین به پرچم ایران و عراق برای پذیرایی از زائران اربعین حسینی] این روزها در فضای مجازی دست‌به‌دست می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453619" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453618">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تحریم‌های ضدایرانی آمریکا علیه یک شرکت هواپیمایی
🔹
وزارت خزانه‌داری آمریکا در جدیدترین فهرست تحریمی ضدایرانی خود نام یک فرد و ۵ شرکت را ثبت کرده است.
🔹
طبق ادعای خزانه‌داری آمریکا فرد مذکور تبعه چین است و به‌دلیل ارتباط با شرکت هواپیمایی ماهان در فهرست تحریمی قرار گرفته است.
🔹
اسامی ۵ شخص مرتبط با این فرد و شرکت هواپیمایی مذکور نیز به فهرست تحریم‌ها اضافه شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453618" target="_blank">📅 20:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aad6f861f.mp4?token=Kv0j3feOopoGgJeU1m3na5ttH0gOsmTV5-1Y_i715EgLCZ5_FCS58uMB86yyiLtn_eb3L-UIu684iZRCV_E0aLiKuP7KNVCqWZ9egNJx2ZHZHwYbqV5RVtIj7DhMQud3JPmasAIe7TvUYT7mZRyfD8BggxDE1FtMBGbJDbVRByMkzBhYZE1UGiGXibNQE0YAQH0CPQA9yHJHau_AlEbwZjHx9OfeYTI7sd6JsHN5gbyw_q5pxEE7otyecxjqz76-UhqavxhUlbUESXjIti0eJDozrj64ZwJg2QQmkBrFD9nmo6GD-ti6713oQNyxkP9LtGEK2tfvdKB7tpRx4PH13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aad6f861f.mp4?token=Kv0j3feOopoGgJeU1m3na5ttH0gOsmTV5-1Y_i715EgLCZ5_FCS58uMB86yyiLtn_eb3L-UIu684iZRCV_E0aLiKuP7KNVCqWZ9egNJx2ZHZHwYbqV5RVtIj7DhMQud3JPmasAIe7TvUYT7mZRyfD8BggxDE1FtMBGbJDbVRByMkzBhYZE1UGiGXibNQE0YAQH0CPQA9yHJHau_AlEbwZjHx9OfeYTI7sd6JsHN5gbyw_q5pxEE7otyecxjqz76-UhqavxhUlbUESXjIti0eJDozrj64ZwJg2QQmkBrFD9nmo6GD-ti6713oQNyxkP9LtGEK2tfvdKB7tpRx4PH13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از دعوت به حضور مسلحانه در خیابان تا چرا قاتل را اعدام می‌کنید
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453617" target="_blank">📅 20:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3_oL6nG-DSzDnSyNLI_xMPNTq-hjotS6tl8RUjBgWWCQmE_JyJms5PVRzn2EUoltGfee4bDX944rf1m6MNRYONWJt-jyOgPbevS4OGIJ1WbttWqImuCJcfR1qBwkBjyS2wajy5ngBTm-y4y8GbmFV786vZZn-7pPHzeaXZPgt9ZNX0B7zeIS2TOPrNiqZ5OpY-xzukkkkzOSd8XmnGPyGdQQEAMht8D5qJM70aAWmmP-SbeDFZqSLWP6w20xd7KTd5em4L0YKTiJQT9JyrOh_8L-5VogJAvki5_maufyHPttcCb_SnQlzA_9BvfMmk4MKTYIrDIJpM7OYRQbxElgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال در بصره میزبان رقبا
🔹
پیش‌تر با برگزاری بازی‌های استقلال در شهر بصره برای لیگ نخبگان مخالفت شده بود تا بغداد به جدی‌ترین گزینه آبی‌ها تبدیل شود.
🔹
بعد از پیگیری‌های فدراسیون تاییدیه لازم برای ورزشگاه بصره از عراقی‌ها گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453616" target="_blank">📅 20:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cea330b48.mp4?token=E20y6YV__BB7QJVPoSJR8e1KKHTsPmHVmL1FsWXHObPyUko8WnX0M-RvZi9S5voTdGqlJ6Pa6iBIiePa4Lj_xjSepLzNsnqr6pv_z8gkxiHQUSFll2pO6vUA0GjOvG2qmbxfGsEuPn1MHZu5Z9kv0bhdMENf_QdEDfvlCA-9tSHW6Whns3OPLIPwZMSFdnKKydYt8LjsRuI92K2FH3bLYJdVPAuAxvi35qvCWx-bcPlJGAebe3wEkwnxF3Ga0zbKvK1APr0T0AnH1lgoqLhyBgl8YZMYPEm7DHeckydYHqUnLQE6kIbF0SLHlPwx9c1GQG4PHX-AMWbie3HS9pNqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cea330b48.mp4?token=E20y6YV__BB7QJVPoSJR8e1KKHTsPmHVmL1FsWXHObPyUko8WnX0M-RvZi9S5voTdGqlJ6Pa6iBIiePa4Lj_xjSepLzNsnqr6pv_z8gkxiHQUSFll2pO6vUA0GjOvG2qmbxfGsEuPn1MHZu5Z9kv0bhdMENf_QdEDfvlCA-9tSHW6Whns3OPLIPwZMSFdnKKydYt8LjsRuI92K2FH3bLYJdVPAuAxvi35qvCWx-bcPlJGAebe3wEkwnxF3Ga0zbKvK1APr0T0AnH1lgoqLhyBgl8YZMYPEm7DHeckydYHqUnLQE6kIbF0SLHlPwx9c1GQG4PHX-AMWbie3HS9pNqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر اولیه از سولۀ تعمیر و نگهداری جنگنده‌های آمریکایی در پایگاه موفق سلطی
🔸
این درحالی است که سنتکام مدعی رهگیری تمام موشک‌های ایرانی و همچنین عدم آسیب به هواگردها و تجهیزات درون پایگاه شده است.
🔹
سپاه خطاب به سنتکام: بهتراست دست از سانسور شدید بردارید…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453615" target="_blank">📅 20:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSgYg6wEgEI9HZweQZrb2Hthcc6KMJS2vvvGDePfEjfCRjNFtMISkny756GZlYMVtQUomuxHQ9FouaNZCskMP399I6AHsOrulssPU3bEZPyMVVlYDmz4XuKJT91xenua9lcpbXjPcfCj1_YKJwwMAi07AJ78wh4-U0ZOOYEs91squokdSgpzI7GGcRPc3mTWBLHnxHdHppY16Xc91LffVvDpprDDWsQb5rEaCwSxiDXcxiNZmRfsPQBvHp6OK13A_sXOsPv_TvKYYJiB6CaB-KLxD_6taieCqndpwvD_S5ksgXoPyFT4O0dzHeeD6Yt_9J7QMXeIwRrD3-gRM2MkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از عملیات صبح امروز سپاه پاسداران که منجر به انهدام سه هواپیمای F-35 ارتش تروریستی آمریکا شد  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453614" target="_blank">📅 20:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453611">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQlwEfkIhw4ZQVOb3---qjxTeZhoAn-G2Z0eP9eRkmWxWfRDdoqabCMkp5c_YVUw8KWxaUhm6XkMowu_FUl6_V7XdYPARs9puHaYrTGQS9MUFB5Pw36TfaOh3prFouQ5qd6Bw5siROUf-xup4QT3k3-UXCJjvDMlI4rgNiEJYKSBKpLnP3T5nqGN0mlv-x29eJbcbWPlbviIFBU345dLZA4ER5MotqJtjAbxYJUWzbgg8CSo9PhmJLm6k0dgnUaNtL3Vy4BcC4XYiOXjjycPyAw_TeKI9tnN4CcG4icRrLKWkUCIUiQZccBc2oJFW5qoDEke_ztkpVpEwPyESbsbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKlCJdVfrdxCHKoFr5KUKCHOunM44bNhoft35x0qmc30Spsu_vWDJS2HFy8CssY8uRJ90dLJ7AVw81WZox6UxyhmZRlPeiydU1DtqcV5NGcDfZsEmDiCDwBD5xk92ta8pTKry8WnegfKgpJTtbGFHK3C40CO1sZiWKrY9f9cGYHisir5-kaMidE_F7ikwCZArUzyXDG5_BS8UdOgEVMtTgzcQKiTJZRw_kSuHClbp6i79tWex3B9fPUEOUNQDB1zxIwkIjswnRDspH-smDC8HGjeUbbH5v1-145Zpy8bQ2EDvPMiq4tuXphonqjQmth2ktZtgBUIEkWb0X2f6z8cWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vP8yEoOWUKk8hu7GAxj_e2FitIwCGXK3PZXsSq5qPDo1RhdJXDi-KDgtuUEKnGge-BVQHioEBKid2weOcMDJENM_1Hoq6wQPRpcDrZZNXR5u1Vl3gOWXr5JOu4ZaVipNq-DZ1EZ99w-pFK3rCFVpT3nwU0WGdTzmtA-zPStzL2SXTK8wMfciJCHtEbZ8TRLIi07V3nqH3VBF64-aSMLNQQwqS1QUPc5s7LbH1XCFE7U4EK08SpU-8Sq_1W5Tdtiv9OC83VasgN0JCejtPlA6sqdVgk9UuTG98lvmANbpkKOjUTAOVIdrH99_vQpkURR0in9vn-Rj0M7JmDJ-iaSuJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453611" target="_blank">📅 20:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453610">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv-yLhGGPAMYttKKyhpZHmoRCiWbCBIFcbg4qbkblb4IkwTLJcJhCdYsfRlkGBq-0EFzl6mT_NY1havYdOmsGmmizYhM-GBOess6E5hiF6t182QRYDJB1Ih5HAw13UNrD_1UwkWbIaRzTrdgsoIzevk52D3zIIYcONle3osdCBwoKGMS4lAttoJo2gFVH7uQIfXOeWYk2TFe6JEtKz32fmEQpfZVZeY9ZVFdaggYZGV8kZ5v74w_Y6cJvopRXty_bufAYNBzmONQHxtAFeWEIkib-9E5cnlsZSjK6fFDCaTC4qJRNvalCDhrsoyaJCPUDsF8Zico7uc3v2K3Tn7GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوفا، فیفا را تحریم کرد
🔹
اتحادیۀ فوتبال اروپا و ۵۵ عضو آن در واکنش به پیشنهاد فروش سهام فیفا به سرمایه‌گذاران خصوصی، بیانیه‌ای منتشر کردند و اعلام کردند که در صورت انجام این‌کار در مسابقات جام جهانی ٢٠٣٠ شرکت نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453610" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
