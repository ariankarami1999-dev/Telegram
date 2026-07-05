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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 634K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-98319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2674c1bb.mp4?token=CNw7eoPo4qRxQAouWR0a-Om6tJ5LphkkrQooguYFGMyp0eORHZAnBBG8wJy_c1CZwx9-AFZCpI_VVdkShpNkLUKdNVSiTQLjoUZxHDGCyMvtSUR0q1WH7tTjy_4vF1OJ-Gf0xFTe5NKJ1qnwRzLUyWHpBSFEe7i36tSjEUqssqxLKNqGXP5oKqriMDXspfQc3aa_ZrczSmj6x0D5_ngfqwgfqAxt9-qCL3yu1_v1656pZkcf5PZkWuYdx8LYq0BMaaFgKa8kFoXlLORAVXo3kgsiP8FwG1Yo7EhngAx1ZHOmLBsIwrbllwq9e7bS-2geosdDOUzGy9FZ7cinR6pymjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
🇧🇷
هوادار برزیلی و آرژانتینی کف مکزیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/98319" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/98318" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
👤
⚪️
#اختصاصی_فوتبال‌180؛ در صورت حضور مهدی تاتار در باشگاه پرسپولیس، جواد نکونام به احتمال بسیار زیاد جانشین وی در باشگاه گل‌گهر برای فصل‌بعد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/98317" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD2smHWO8AKjH2V4M7NKFOquvojr6_lV1H-V-zvEX0u58GpNRmbGHMz3JRtEVpOoQRnIR928z2Wy_ZUAp3uGaRJ5vn7ZjuaH9qRuKmMob18ALjvJRoc4l1kEBIZAeJWzf8j_k1pgOsFeRaXupBMaOZRpvgx61f0wtuniNU7Je1RXURKMpEdMPgOkoT-4_V-40yC6C2VXQWhs1RUZmSJUNgw1-ILVXlwczaU_w2wUbd3Z5QgMFvy7mU6YoPOJlEy8XmH9QssfscVt8m6YQVsxZDrBNmGRtS9Zf0vMSRzoYq1IXMtCK2ywLxoYqNJ00FqPax9IlTJuCGVCRpGyK1y0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
💥
گلر کیپ‌ورد و یکی از هواداراش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/98316" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcqEzPzJTxW3MCkvJVgb3LELmLm0nWXHmeu4u0CNgb5RPXZ5yZF7ZKzC1OLyBuzAmWtGJVPguLG2J2WOX8pkw4TyLSdIHnqhxClyMMWGLc9_0zlgFypZXhPOhVCTGzmvHv98CoYZpbZAcXYpiQ4EcO-qNjS4MVZDa-jxizaomoqepJXEd2d8TUqGFWMf5AdClBeELX9KqstRLOrBqJSGr9F3V0VgfCtDMVxXJlyK6pJpvqh8mTyS89rbTbAtog391ahUvDEOGsqSNcJ6y4Pv66KmQhQ_kg0oJLI-jOv6CyQQ1Jyvf13aoq0SAavY9XQDg1Mqye-c6zDo3s6tnRr5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
دختر اینفانتینو رئیس فیفا دیشب حین بازی مراکش و کانادا با کیت مراکش رویت شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/98315" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98314">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=KMO-BS8AU38sHv39yxtPla1RqYQrtiPhbb7lrXyeFh8-PfMoVYSBms2lqsKmLp_N8utp372D2bJ21TQ5uATMG9UqNEUCzAAG4mSFhZm7RQyb0d3yIyddGoE9aaaUV96XggIyD5Zgnlo5G9gKkI63YAMmk4DCN1tppsd2ph3_NLvuNzZF36F1NhaZVJfd7_o30Tf2AsZPdUFKrQJ7gL3jxMV653L_B3ymmuFFNRgKc9gCOthxCKxtUhBMXYhpxHtpfrhWw8wKwk6-ud95ZYOV9ZNGJQsvov8cHLmXT-8OKhL5nIRgcHwu91ipmR6tEpf7s-QPmqPwHBjA0PWPe_NnWx72ay3RO98nqGZN2Cyqxr8s0liUSrLiv9e-GLExuSFCox51uREmIB3nblDHLZE5FL5idV5KBGVIZprCaYC_uaBpuetY5yBTPKBmOYQUsN1tRWJwlrdZ8kmke6xo-hMcZIhsGf5fHMdmjP_o9QnwtOQM7VkqkGxRo_7wLv5djledsLZygx4txj8CUrRtB9yHHDzQh8Y1kX5WSNABWkvZ5uOihldiNKMepL9VkVATQRdEWMLFHtRQD_7VHnerp5u_cf9_1uPPNTbFGg143BJuUDRJgtUMKukk5A5pNXcCG_FaQBiENBhFGjPWpzJ22mJha0c0dMk4Yx3gXbWI1H57vbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f320acc5d.mp4?token=KMO-BS8AU38sHv39yxtPla1RqYQrtiPhbb7lrXyeFh8-PfMoVYSBms2lqsKmLp_N8utp372D2bJ21TQ5uATMG9UqNEUCzAAG4mSFhZm7RQyb0d3yIyddGoE9aaaUV96XggIyD5Zgnlo5G9gKkI63YAMmk4DCN1tppsd2ph3_NLvuNzZF36F1NhaZVJfd7_o30Tf2AsZPdUFKrQJ7gL3jxMV653L_B3ymmuFFNRgKc9gCOthxCKxtUhBMXYhpxHtpfrhWw8wKwk6-ud95ZYOV9ZNGJQsvov8cHLmXT-8OKhL5nIRgcHwu91ipmR6tEpf7s-QPmqPwHBjA0PWPe_NnWx72ay3RO98nqGZN2Cyqxr8s0liUSrLiv9e-GLExuSFCox51uREmIB3nblDHLZE5FL5idV5KBGVIZprCaYC_uaBpuetY5yBTPKBmOYQUsN1tRWJwlrdZ8kmke6xo-hMcZIhsGf5fHMdmjP_o9QnwtOQM7VkqkGxRo_7wLv5djledsLZygx4txj8CUrRtB9yHHDzQh8Y1kX5WSNABWkvZ5uOihldiNKMepL9VkVATQRdEWMLFHtRQD_7VHnerp5u_cf9_1uPPNTbFGg143BJuUDRJgtUMKukk5A5pNXcCG_FaQBiENBhFGjPWpzJ22mJha0c0dMk4Yx3gXbWI1H57vbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇻
بازیکنان کیپ ورد در بازگشت به کشورشان مانند قهرمانان مورد استقبال قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/98314" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98313">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=H7nXAoXOzyKzbFVTmZYWqhdia_v5NmSe6N4KZ4vmZVn95mdygUD1hMe61vvscVjwAi1RfqebE5PMlCwH4n0y7FcU3mnEZnquer1a6H4aG3xBkdaFEFDGFaRxizWrUAOmjhLgCVzMdW1BnW32mPpbyEBvwfumMPXK8dhpUKtgOnHjWvwoDZF_nk5LZQR24gwsow8FahpEsCtgdhC60L0JCxRQipOM_fXrLkihyuvuJ-vd032fzI9rQEGpkqBZZntvkKb8VG8OkYjZjP-fGeOrci-qNnBqSVU8taBDYxZjIi81TlTE5j2PciMkMsIR7XqALxj42J6Qck7eFmSiUWKZcgRNev1gq4CAiScj67kpn3sbjN8FNfOVS57R7KAFfIZU0DLVCvrXd48TtXsLzQpVeOUAZ48AMuyjGyoZfIIw7VkDfE0sbI0nhnDqpVaBn-x1GCvfMXak_nlTcbTfmLhn3NKUEr0cbCX2A3eIENmuPZ1pTIiG46vXWGzh7F4i5r-cjxXdHli2mxRUuE3ewJjlXG4J1Wre2NpYU7pARY3_7fsa-uGFSVORZIvwuVo3QYv7Ew2Svyi6cY8rgDTzXhncXgQeqMf1zBWSaahkvBVhm5g7m9epk7Jq3muZ3oSWEduM227NDmAe1OUYDEW0xFMbwEV46RlegM3608ah6uW8VCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605fe2f1d.mp4?token=H7nXAoXOzyKzbFVTmZYWqhdia_v5NmSe6N4KZ4vmZVn95mdygUD1hMe61vvscVjwAi1RfqebE5PMlCwH4n0y7FcU3mnEZnquer1a6H4aG3xBkdaFEFDGFaRxizWrUAOmjhLgCVzMdW1BnW32mPpbyEBvwfumMPXK8dhpUKtgOnHjWvwoDZF_nk5LZQR24gwsow8FahpEsCtgdhC60L0JCxRQipOM_fXrLkihyuvuJ-vd032fzI9rQEGpkqBZZntvkKb8VG8OkYjZjP-fGeOrci-qNnBqSVU8taBDYxZjIi81TlTE5j2PciMkMsIR7XqALxj42J6Qck7eFmSiUWKZcgRNev1gq4CAiScj67kpn3sbjN8FNfOVS57R7KAFfIZU0DLVCvrXd48TtXsLzQpVeOUAZ48AMuyjGyoZfIIw7VkDfE0sbI0nhnDqpVaBn-x1GCvfMXak_nlTcbTfmLhn3NKUEr0cbCX2A3eIENmuPZ1pTIiG46vXWGzh7F4i5r-cjxXdHli2mxRUuE3ewJjlXG4J1Wre2NpYU7pARY3_7fsa-uGFSVORZIvwuVo3QYv7Ew2Svyi6cY8rgDTzXhncXgQeqMf1zBWSaahkvBVhm5g7m9epk7Jq3muZ3oSWEduM227NDmAe1OUYDEW0xFMbwEV46RlegM3608ah6uW8VCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
هواداران مراکش پس از بازی با کانادا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/98313" target="_blank">📅 17:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98312">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqN-NiPDiz5v4olc0DtaoSr5cLjkMgQl4yacAVAj47EZltHOmOnxku3nq_C596-JzYVCuTOz8iQXVU67ydAI9mXJsDNXfDfLradCdZJ91iYxmu3-537N4t2AuWY13Xzxr9_fRalXvl5-pG9pXQoZzhQlUztsXqqSEGK65hCWo8-iiwjLyrxf4Laqqv_tcK6jDLfgH99ME7g6Wg2XPSxi_EW21wIYn_hwxeFTs5D5lnBlu3fO6mRo-s-bRv2VnN00GFU83UmikELjnzGnLORl-ZfGTaQUdm8fWvOXM4ipW0ZEAqQ9uFec3JJzIU8pZvWB160IfSn6WZRmkFSh0xr6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
💥
دشان، اولین مربی در تاریخ جام جهانی شد که 10 بازی حذفی را برده است:
— در سال 2014:
✅
مقابل نیجریه (مرحله یک‌هشتم نهایی)
— در سال 2018:
✅
مقابل آرژانتین (مرحله یک‌هشتم نهایی)
✅
مقابل اروگوئه (مرحله یک‌چهارم نهایی)
✅
مقابل بلژیک (مرحله نیمه‌نهایی)
✅
مقابل کرواسی (فینال)
— در سال 2022:
✅
مقابل لهستان (مرحله یک‌هشتم نهایی)
✅
مقابل انگلیس (مرحله یک‌چهارم نهایی)
✅
مقابل مراکش (مرحله نیمه‌نهایی)
— در سال 2026:
✅
مقابل سوئد (مرحله یک‌شانزدهم‌نهایی)
✅
مقابل پاراگوئه (مرحله یک‌هشتم نهایی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98312" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98311">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔥
🔥
🔥
▶️
🏆
برزیل
🇧🇷
🆚
🇳🇴
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98311" target="_blank">📅 16:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98310">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6IpgpBlEmUda0DhgZiKFGzH4_CEBqrW2q9sYNuCm_mHpGg183cIaSbgv1y8iZYAgfJCEewnroVhtPbVTqKkk9mVFyVALzSJkKfZkf9JOFYFbSf6ODCwsufa3-SDUCOXDuLW91PxaIkwqAS1HhQVUiAJd03Y-1lczg8d7INb9V-pAvnHDxbNTRLI03UFd-4N6rCIzVmTjtK4jxPrDE7RVwdFFtVc8E3PlWZaSYSkxF8QQsenXh86X1OCSGLdOFiGavkq1zN8AllmLIiVNp1Qivr3lelgiSPMJPJjzWEdc0DkI6GD_70ATwJRcTAYXoViGBX-EpGua2TkY_Uh4cCb1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
📱
بیشترین فالوور از بین دروازه‌بان فوتبال؛ گلر استثنایی کیپ‌ورد صدرنشین شد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98310" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98309">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyh8UmyoFTiOMZDcMEpE3TXxLfgrkSlH3r-lpXrVBSutja2A28Bga-xwY_AxKsXCyXDJ4qsO99r12ER4TkSpEE_uUmTH6bPDTLT5_Q_97VewGM1ooRkoP_zC6XnYJpgRyRQLeLkZiL5X1pVl3-RB9pQBHKOgki7eQR93d-HnFim5fPSPGz61waBwQfb4500MfRyCQaLpFPyDWH5pkfjR9oHhDEa728pE4VPe217Np0-3WpHTOn6gAn1CJNYqTO-aPqdgQRlGjtvzQQaZqsbHX6BQZpAQ4qUPZg44GuoC_FvgMYAk3s10i4zFQ1yWn-FlUmeTCuVf7NH6mJLtW32mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🏆
صفحه رسمی مجله فرانس فوتبال
:
امکان برنده شدن جایزه توپ طلایی بدون بازی در یک باشگاه اروپایی وجود دارد.
👀
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98309" target="_blank">📅 16:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98308">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
انتقادات شدید مجتبی پوربخش از رویکرد عجیب صداوسیما پس از حذف ایران از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98308" target="_blank">📅 16:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98307">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuA_4gqxMSs-pzxNn584Kryil4aNBRlnPpMDczuxmXVyfsNNP3YF0SuGZxNGZEehvNk7UhqDnQyEzDgUTbk9eSws-l1rRDLpsmOMNBK9GpTP0e77Q3SiqshfxY8lJdp84EZnoK0hoZTVDyToo_L0UYVh85Wz1SXJnlpAVom-jnp-wgy4v1nIDU8k1fgzaC13MURm1_WAg1DL5Sh_ut4iI-C20CBTQ34YO9g-BNtDKTZAWvUJjU0YHu0EQmxNwQh7sMpSlVQKoM2TJqBIvMERYr5QiadJbKnfrkl5CzaDolCf9UorzRt7NmBAAEWXQFLcizBUCMoPc7LK8QX2iMjXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98307" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98306">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98306" target="_blank">📅 15:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98305">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🤩
✅
#رسمیییییی؛ مهدی تارتار با عقد قراردادی رسما سرمربی پرسپولیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/98305" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98304">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaXN0KR8xhTxhz2GTBQYQKGIFYKFouASZiydjQFQ1EK723h2kPY_3GRoqH-7N-QG5DuNEwgVwlxnqo2FxdroBWOxDNLOi_bjezE8enB4yxmoRHoUXJg09a28jYvwZRMqZBRddCReuOctCloC-1y8iT7sDT3R25THmFfqVbW_o_wOOUalVree-jAScaRMzAmBF085wXBwARaMxt2jitc9c7Tz4ACQU4o-zcA4aMmPOV9v24qEAQCOJKTkjp_4XbrSmyZMzxNhYfdLTxHGTQk8wTX3WG9U3kHtK6JPd6Xl2vnHEg0YkoTRUlBOtYG4mvMiNFO2-9mRcESmarx-DLU3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
یکی از دستیاران مهدی‌تارتار در گفت‌وگویی کوتاه با رسانه فوتبال180 اعلام کرد که مذاکرات پرسپولیس با این سرمربی درحال انجام است و پس از توافق نهایی با گل‌گهر و در صورت رخ ندادن اتفاقات عجیب از سوی بانک شهر، این سرمربی به آرزوی دیرینه…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98304" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98303">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8c9137cf.mp4?token=aJJrWX9vOXcvDmXoB2YVJXYC3iIuKb0pgPZg_JLnAqjrTefYhNEBPOpVXEPlAHsS0CemAf6zLlTdk_CHR4vgTVYQ9W0MT4VKB7S4J8K8JKdA1w3yOVbqcp-UCZvTXX_UDAb16mhICSG098nSfYo32gFQ2h7L9ULx5hzSFjj0vUjzDXAllNui2J9wKO-RIBT_10KcT-3IfvR9F1HeDaNVgVDykIj_yTOg3ppE-qkr31hOuqmbEgktE8nn2NOj-9W59ph_m92KsCWLmlA5gIMbD5kINl3oJ9iW3uwrfCh8rzbV_oWP88eYWsOx-23XfR5UeQvCTBGBRwzWmutVMTDBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8c9137cf.mp4?token=aJJrWX9vOXcvDmXoB2YVJXYC3iIuKb0pgPZg_JLnAqjrTefYhNEBPOpVXEPlAHsS0CemAf6zLlTdk_CHR4vgTVYQ9W0MT4VKB7S4J8K8JKdA1w3yOVbqcp-UCZvTXX_UDAb16mhICSG098nSfYo32gFQ2h7L9ULx5hzSFjj0vUjzDXAllNui2J9wKO-RIBT_10KcT-3IfvR9F1HeDaNVgVDykIj_yTOg3ppE-qkr31hOuqmbEgktE8nn2NOj-9W59ph_m92KsCWLmlA5gIMbD5kINl3oJ9iW3uwrfCh8rzbV_oWP88eYWsOx-23XfR5UeQvCTBGBRwzWmutVMTDBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
هرچی از این سیو بگم کم گفتم. گلر تو ۴۰ سالگی اینجوری جلو مسی غافلگیر نشد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98303" target="_blank">📅 15:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98302">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek4y4_dUdF0nXxBKmDg6YkDXROBBs3OnlLOL-4LeUYqoMKiwn2m4DzctPj3KgMdYcrEZTaJ1g8WDM-DqlZIGbLa1lwUMNJmCZM5XpfMudLfyMq-VVn9MMNQVWIX8yh4nCQ4nWylgUcyBRNn6tE8wqFYydLTtdhl6Jkqn8C-itHNmUxarS1B2JcIxwkIwUaqEHZWdWXD2RgkQbMon11Y4pY9qxmBBBsugqK172jFssRoXn6q-zHkGEHkrFsQSngzMEm6U7t5XN2YLBZWdQfPnN8JxDXRUtd6Haep-53W3-uR9hbeuqNBL_4xrb9EBCCczeQim8SKDYy-1RYAZAPJotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل 3 سال پیش تو دسته 2 پاراگوئه بازی میکرد و با درامد فوتبال از پس هزینه های خانوادش بر نمیوند
حالا بعد 3 سال اون دروازه بان اصلی پاراگوئه شد و مقابل فرانسه و ستاره هاش فقط از روی نقطه پنالتی دروازه‌اش باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98302" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98301">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98301" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98300">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98300" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98299">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743a223544.mp4?token=Jy6oeDml0ZLuMFKBtT-XxdjtCzlbRObgSVIblaZCbtkrPthJZH8aA2d51lQ55Z6A7n3ybB3quQvq6KC85aj8TXpJNkpYzlvPjfK5YJhbqNt-wvBxOJpQNm7crlF-KDULzf8MF_XcLBQ-Cry9095uieU_8bsl5DAbq9qZ1m7vJ-DsyJySS8BMHMsjFD96KlXxGA9ZBSWr16IjOUhp3twyJk3sN_rOuBbxz4fs55sEIIvgcD9Eb0-noQ6wSWrfAwnRkBPNjQt0qdKrXiVN7GPoT425AySV6_qcMi0GEERXE7kI2gRm2lXGaaniDtz5qtlv6eP6394mAuofcwOY1qC4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743a223544.mp4?token=Jy6oeDml0ZLuMFKBtT-XxdjtCzlbRObgSVIblaZCbtkrPthJZH8aA2d51lQ55Z6A7n3ybB3quQvq6KC85aj8TXpJNkpYzlvPjfK5YJhbqNt-wvBxOJpQNm7crlF-KDULzf8MF_XcLBQ-Cry9095uieU_8bsl5DAbq9qZ1m7vJ-DsyJySS8BMHMsjFD96KlXxGA9ZBSWr16IjOUhp3twyJk3sN_rOuBbxz4fs55sEIIvgcD9Eb0-noQ6wSWrfAwnRkBPNjQt0qdKrXiVN7GPoT425AySV6_qcMi0GEERXE7kI2gRm2lXGaaniDtz5qtlv6eP6394mAuofcwOY1qC4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق کیپ‌وردی‌ها توسط هواداران آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98299" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98298">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=vmE2aGSljjaJoePrHTEfs2x9ZcCmr0XvSiHndyDm7if0r2aqrOz_l4pNqwFfUC2T7TGtJ43jEh77wl-A560mTisa539ZqzeSCfkCwopvHjrgLThSVtsCD6ybeyYm6cotjmK7SYR2UzzbOR-5qoBYJegq6yagDyCsgrBMVjG1GwGUIHgPY9S05M5uYvEIA8DZ2-d2Qpl7_KPJkG55WQ4pAcCqUdVYgCr9A4qrj6PrPc7eIcXRQVlWORsTTjsBdv9RA8r13srgIhHPzOWcB62sOsumJgBezDwlQ0VZnCj6k-wUO1W2Xfpl2zqsRS1HBvXF5mB2pUe_k9h2Yu1l7Jwv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d4df0d8d.mp4?token=vmE2aGSljjaJoePrHTEfs2x9ZcCmr0XvSiHndyDm7if0r2aqrOz_l4pNqwFfUC2T7TGtJ43jEh77wl-A560mTisa539ZqzeSCfkCwopvHjrgLThSVtsCD6ybeyYm6cotjmK7SYR2UzzbOR-5qoBYJegq6yagDyCsgrBMVjG1GwGUIHgPY9S05M5uYvEIA8DZ2-d2Qpl7_KPJkG55WQ4pAcCqUdVYgCr9A4qrj6PrPc7eIcXRQVlWORsTTjsBdv9RA8r13srgIhHPzOWcB62sOsumJgBezDwlQ0VZnCj6k-wUO1W2Xfpl2zqsRS1HBvXF5mB2pUe_k9h2Yu1l7Jwv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
خسرو حیدری: یه بار تو تمرین تیم‌ملی سر توپ زدم کی‌روش نزدیک بود کونم بذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98298" target="_blank">📅 14:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98297">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUSIen-fR0sElnH5UE7tsr6qKtXuJapS4QU9S_DTKf-60EObrmMCCTGoI3ZWOD8kx1v8MZK0wNTeOOTBdHUnih6bECpqH9ByrW5gLc51Tx-aPBEe7UFuaNaPFBlc4foZJ-1OEXNb1KWeFvUsNuIgRZuJZYlF2v9K5HFajuyFWL2SlPQdvN4n0XWtlUw56YbSVpRzNyEUIQaHsjlsebN1cU7sPJtkJsyJZMhoXdeqRjIqBZDUNIxpHCcbmJgXZH90RwSDDdEH5skiLqDxaHQcwclkUBG2CLTdfDVAsH1BZiyI5VRahD6b5MrvuV6V2tepQJ6ulnrHzYE3Lz6uschWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
محمود خردبین اسطوره پرسپولیس و دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98297" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98296">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj67DE_06XHTjDitDTe_2iaEQDxnJKfCXn3RXAF7Citg-r-czqoiWeb3lEYUH_0ZhIDkQwMB-EeBqDuBf9MIPPhjSukQDiVNSeoo7tkm0yEx-HZakoFdnJ5IPll-RXgzPetjJ7HhzFqJrkd0aqRPl5ScYQrrw4g-WzyLpq6yjEi1LX76I8oZ2EkeIsySSWPqmcI15DZsQ0tMR4OvQ0JbBD8G1cbxkfhSh7XnslrGSPGsJCSHPubyXPPzOIdpwXMVioCvWh-KprbItMKmFuTgjs2hVDVUR94o20A86wAVfIToMDXjUlm-yUofCtTj9KlKw1OUuLYlDHO5LvEd302sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
پیشرفت چشمگیر مراکش طی ۱۶ سال اخیر...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98296" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98295">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meBBpRcmlraLoE7jh8AaLjdnO-sBowvrVs4NWpuDYho5DHiInRklFvUDEqMQjhjtclKEYcFSrDpGSaj1-jw7zuElQx08BpQ-x9k5QCQ0YWc4R76CYf3LtjmyfDaFNa8ogD6ccEY-qDnTOH5xiR9YwUQgrsLWX9H9JdOhqRaWAkKYMdu9BArDBNkJu2eXWzkI_YdCqSCHsBqRu7AcsFQ2Jd77FBF0_1FUGAGAL_0YUKjcdnl_BX2hn32A7BXGKNT0a8DnoL7bwpqxCIso7aB1-fIAjHV1xV6nHLuP5_kYAcfDYeF9_kgBdAsTFHPHpEfQCPy08vRwuROhR02w5xsrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گریه‌های علیرضا دبیر در مراسم علی خامنه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98295" target="_blank">📅 14:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98294">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqWP_FYf3MAJVSzpaTwskltNVFU0PytGzXGDrnq6XzXTr2icrLn6cc-2enUDWJndpEc_8pL7S6_4SiZkIobLoFGQ54fJHhvThe3k7YtbH4tuMOCwblhsMcUuQzLdqAnmBRRB5On9QGibB5eJ9CNdTJ-SyO6S1ufukH6b1GTbVme-VK8QHOxwP0WZ6d0340xvmqeuNG_lns2SbW7Q_XSR09RSnDh9gkZLxwwBRoE0nTqsQPsnDvAbvVpkH46tLY_FKaR19oGXO8i9416mN40p1jf2OC-HYswu0JVw2VR9qVv0IOsPwDiratOQuQHEpKB3joLzBAt-kL1FG39t8MuJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ دومفریس مدافع تیم‌ملی هلند با عقد قراردادی به رئال‌مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98294" target="_blank">📅 13:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98293">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماجرای درگیری معروف علی فتح‌الله‌زاده و مجتبی جباری را یکبار از زبان خود فتح‌الله‌زاده بشنویم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98293" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98292">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP5MOl29kAnpu1nvU9Lgqa7iXwDMgEawYVEXuTSJ2IL46-gT41rSTIJFE9mNMgf7o_4J5iNQvKuwu0k4fpQsIVgnZx14ONaXXnw45O5eBVXYeey73106AkMTN30HI3jj90jVpFCyj0BpShKjtt1xNblecCnjJpbRhQg60Gp5fwiGleCbpGIiDUuXTq7YitjwiQX8FPiIBx8DalBBOH9oB8RlM2WC9twXNQyp_c5cmsxA9mcy_FxJoeOfRkcYJ1qhmmcOR3HnFviONseN0_7Hib-_g7r6m2aLeBs2AziJMUGRLjaJ8oBkFLkxBUNdFp0ItMnOFemrRMNUT2n11MeWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کلوپ به عنوان سرمربی جدید تیم ملی آلمان انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98292" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98291">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=dGb_l8K4h9qFqKjnuIXo5mM_8_DC6iRMZP_5Ea2H8yTAIEWq7LNYRChBukQWyw_xv-_ZQPRkr85BTf_xIXD85JhZrn1Y1LUO---Is5ENxX-0-lXT0q-6kgbGvl80pastowN5mgykc5_ffCrKnAxcoO6rwwTnBr37DpjM020ZOKCv4mZIK_IgHtGuA_i6l4JHs9-d5hjH6L2WhVQtaf2ks6RWHMGv42MxrKFl0NISZdInK3SkY58pnmezhUPSnfwHOtrDTnc-MZIvHRf4Rv46Dh0_vWwdyjSGFCkQ2ez6Ofr4P77Z53_X_hg6p4OmzkQCvKW71TEDvK7rnCCSPkbBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=dGb_l8K4h9qFqKjnuIXo5mM_8_DC6iRMZP_5Ea2H8yTAIEWq7LNYRChBukQWyw_xv-_ZQPRkr85BTf_xIXD85JhZrn1Y1LUO---Is5ENxX-0-lXT0q-6kgbGvl80pastowN5mgykc5_ffCrKnAxcoO6rwwTnBr37DpjM020ZOKCv4mZIK_IgHtGuA_i6l4JHs9-d5hjH6L2WhVQtaf2ks6RWHMGv42MxrKFl0NISZdInK3SkY58pnmezhUPSnfwHOtrDTnc-MZIvHRf4Rv46Dh0_vWwdyjSGFCkQ2ez6Ofr4P77Z53_X_hg6p4OmzkQCvKW71TEDvK7rnCCSPkbBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از حماسه تاریخی محمد مایلی‌کهن در گفتگو با عادل فردوسی‌پور
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98291" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98290">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار کیپ‌ورد: «ووزینیا شوهر آینده‌مه»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98290" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98289">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0306de1296.mp4?token=fKcRWip9bp6FvIheC11QC3aMr2ski-IKf_80CDGqPpycSWI5cqTAdDYP1kUO1UbIrhdp6QoKL4qjYlnRzCw8wWgQQLJUKoPv46frgD3b5qYyQtElpx-woxvpvqbPWC5pQaiYUntGMYiyhw7aj-DqNQLTVuUr5J-MMiNbgg_nQUzNqzhbIHO8B-zAM6h-6rjqmyelvbiFhS3_Vxc0ej2dam_DPpZOwnS0AH2FLSlw642WSICqtoW08Choav9ECBnMj0ghjlNdMMqTjaIy24HcVJ5wnt8ahcBREdNB0uXolVduWUVrojRUz4cStF3CrV66SFGgxpZ7ugl9Cv-_nx25sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0306de1296.mp4?token=fKcRWip9bp6FvIheC11QC3aMr2ski-IKf_80CDGqPpycSWI5cqTAdDYP1kUO1UbIrhdp6QoKL4qjYlnRzCw8wWgQQLJUKoPv46frgD3b5qYyQtElpx-woxvpvqbPWC5pQaiYUntGMYiyhw7aj-DqNQLTVuUr5J-MMiNbgg_nQUzNqzhbIHO8B-zAM6h-6rjqmyelvbiFhS3_Vxc0ej2dam_DPpZOwnS0AH2FLSlw642WSICqtoW08Choav9ECBnMj0ghjlNdMMqTjaIy24HcVJ5wnt8ahcBREdNB0uXolVduWUVrojRUz4cStF3CrV66SFGgxpZ7ugl9Cv-_nx25sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇻
نام ووزینیا تا ابد در تاریخ جام جهانی خواهد درخشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98289" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98288">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شادی فوق‌العاده سمی هوادار کلمبیا بعد بازی با غنا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98288" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98287">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98287" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98286">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7kWIz8YqysUp_tfgpKdGZH8_iOd2taTJm885NgdE6Z_y3N6zJ9vYIkQ8lOKIA1wTNBgAyytHspCHEuiILyj8nEmH8VKy1sHX6WOdb433EQCCUHAjgv7IshUE4a7xQg7_t5q-mkSlHkhLWxlmz4F6vbLtBO5QpHU7SS1llrHng-ougD0WN7nw8Rmf3HLRl8qmM9L7BAWli16_J2iUzm4uRiDctPIozQtdhhYL7RYENCEIqdutEo7--i8pOcTu1g7gplFJbto3ByQODeoEBNCwy4unXQsqkXT0WsvEOl-Z8FreVl9rdcBibU0SZeAqoh1O99Ixeb0fQ9uxhhW3VB_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
🇪🇸
گاوی‌قبل از بازی با پرتغال:
برخلاف اخبار و شایعات، بنظرم بازیکنان پرتغال با احترام فراوانی با کریس‌رونالدو برخورد می‌کنند. اینکه می‌گویند رونالدو در رختکن محبوبیت ندارد اصلا درست نیست. همواره واقعیت‌های یک‌تیم در رسانه‌ها بازتاب داده نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98286" target="_blank">📅 11:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98285">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
جادوگر غنایی در بازی با کلمبیا!
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98285" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98284">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GffH_tjK31GGdCRUXpjb9g76eGU0VmzSsUprV2ENK0jkhDVBNwjVWcSm94RsjDFETRmoE_dSwn-8vqViUQ29fRqoxb5Wfot6Xh6jFfX_JLV8zcLBbnB7AAxJ0FqJslLWOhdmzWoa2QQbvMn8skP_u3osWErE_BGt4NoXk2eeZdNv1z1KuhjJUfHjlSTz7OHbbMBxk3ZmDCv0Z2p1eMqKh9li0F0SM1cCHLtIAddVHVMogiysDgx78FmX-vA7ZRsqi8vQ8cMkemwo7KfSQB6tSdoPWL_N4IzLpTRpuIMET08hw-PQDgI569oT9Q_dQXuklYPbdms5vad-3K3QZJHSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
دیدیه‌دشان
:
من خیلی حال میکنم وقتی مردم به امباپه میگن دیکتاتور. دیکتاتور همیشه کلمه منفی نیست و وقتی راجب امباپه اینجوری صحبت میشه، ذوق میکنم و بهش افتخار میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98284" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98283">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=CtTB1kKXxsf7xh_Cj7GQY7m0pUNVgEkIxWINnUKbXaNX4ZUVfjnBFCl7wkc-DEut1NMarLqqJzLQ6uLIX3yMS8Cm80k4JeEONtkg1jqf1ziIpxK_qEjvPdAtpbb1JZKa58aIXahU5eKNCjJgn2hr6Zu2gPPqwWglf3Hx5QmmOpWxKpZnlVuqLyguoHgs3OfOLDZx2C6bjAnlOVEiEDDq8397qWsGhNbgLfkWpU4h7ZoywgVZ1ZTuMdd_qz4ZwP0eiwnWwG3IOwT1_fqss3FZzFb1D5ushZ92375v2xiy-dNFmBPwkl7kcBVIcPPE95peRYWZilMF4HbmIzYtNR35_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=CtTB1kKXxsf7xh_Cj7GQY7m0pUNVgEkIxWINnUKbXaNX4ZUVfjnBFCl7wkc-DEut1NMarLqqJzLQ6uLIX3yMS8Cm80k4JeEONtkg1jqf1ziIpxK_qEjvPdAtpbb1JZKa58aIXahU5eKNCjJgn2hr6Zu2gPPqwWglf3Hx5QmmOpWxKpZnlVuqLyguoHgs3OfOLDZx2C6bjAnlOVEiEDDq8397qWsGhNbgLfkWpU4h7ZoywgVZ1ZTuMdd_qz4ZwP0eiwnWwG3IOwT1_fqss3FZzFb1D5ushZ92375v2xiy-dNFmBPwkl7kcBVIcPPE95peRYWZilMF4HbmIzYtNR35_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: بعضی از بازیا دقیقه ۱۰ تلویزیون رو خاموش میکنم  و در این مرحله از زندگیم تا ساعت ۳ نصف شب بیدار نمیمونم که بازیای بدرد نخور رو ببینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98283" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98282">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfO9wEecFZT1TICqOUb3iezoSCExIhrVOFt7uyt4BOFA6JHjWbfHOBHOYaN43_NnhOHtivN6uZofmQNEbCpxtmPEca7IimuA9ONLVxO2ygqYtu2e0BvaKHkPFE7j9OuPK2YqB9psngMCA0LNGdQ97BDSXn9Jw4LI3EiLrUg_AbJufeibpVtQbs55SSgkL8DS3F4VBp1gJDRpH4YbmQ9eHARjeGmYRgvABI7ZJr6YQzTbnjepoTQR9fUXDIvbZYzC20eSEUypmkMFl5pOw4S-RQpA3c22VxjNa6BXzyILPZsA_zOOImd__g9OAoX4fTWxqMPxjPP9uAvWgE9f-2P4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
📊
گلر کیپ‌ورد در جام‌جهانی از حیث دریبل موفق از رونالدو کاپیتان پرتغال پیش است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98282" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98281">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
خاطره مهرداد صدیقیان از تماشای بازی لیورپول و چلسی در استادیوم استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98281" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98280">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=aTnNDf6xwrJHDIIQlaiOYtTuFKuEC-3nsDdtunZNKDd0ILigxRRPy4lHSUsBRfvmoYDCDYSQw2xX8xnxYmW_DPAPeMcZEGza8s8pW8lb_Bf1PwmU_zvZ866abKskpIP4Gzxnu0X-g89rFwFV7exU6rhPdhMCbRH9NYnvt8o9I4Se8ramV3kUS4OLl4uW8eke-T1W64RN2nfWBa62JxfrFZKFUtOnXvRs5l1x-2b5N28jZ4W6jbGSfmMkDnFqCvXYcjZI8MIXWhTXR3NJYaojZA3-0iCAPeU3cWR4F25FlClyzekw32wUTeX7uH_ilkRuKloeZz6aIXc308mOC7YDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=aTnNDf6xwrJHDIIQlaiOYtTuFKuEC-3nsDdtunZNKDd0ILigxRRPy4lHSUsBRfvmoYDCDYSQw2xX8xnxYmW_DPAPeMcZEGza8s8pW8lb_Bf1PwmU_zvZ866abKskpIP4Gzxnu0X-g89rFwFV7exU6rhPdhMCbRH9NYnvt8o9I4Se8ramV3kUS4OLl4uW8eke-T1W64RN2nfWBa62JxfrFZKFUtOnXvRs5l1x-2b5N28jZ4W6jbGSfmMkDnFqCvXYcjZI8MIXWhTXR3NJYaojZA3-0iCAPeU3cWR4F25FlClyzekw32wUTeX7uH_ilkRuKloeZz6aIXc308mOC7YDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گارد ملی مکزیک درحال تامین امنیت هتل محل استقرار بازیکنان انگلیس پیش از بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98280" target="_blank">📅 10:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98279">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522d669236.mp4?token=aLgZkvza-zmsjdOdi1ZXB0wkLDKa0plazI71F5tMC7B4xusJG_u-6tdbANj-4iGQzA0bxaGX1wwF2EMs7b6GTxFs-0YSQaM7F8DJi-1ppigcJhku0G4SKyN-wMFODN4jtVdLChuOEFyfHcdlkhDlDZzyJVwzMQfgEUF6XJYs3UnMXto-FWiL32P-k6UfWkB_iszj3xh8jw38_iFXbF2kYtL_peHNzHFxC-aaOZmeCzznd41VoWvshS7s2o2SIi_oMxsI8AltuHD1tD5C_aExILzxf28_sIxfavTai4hAi4wBxlXhITQnBg8wazHB3X25lCHASnBo526fV5XIKS44LbgOH2S73rCIa8W9v_fHuIdhu8O4G8EdG3T78LJcELPNXpuD0zmqgNlNuExFw9g1gqtgeRjK2ous0aEF19MICnGfsxVYvFZJfuf-wCO0dn5RL06uIQh3NzuDuADo5RweE10JMGL9NXlpddiUE6Eys2U1YG4A3hdx7LKuFghLrROQsUlNc03Qi0_8CAiZJX20DlZlVVmDzHwDPk09bFp2WJV5W3mq8ENVjapwJe7wQgPLYW0xhG_jd2N_EomzkGanswlowiWykyT6Zn5C8bYKRabELBRO964_T3pHfkQemDnlJc2yZPQ4M6xTQqPbjfc1BpxLZ97o6OPXjv1rV1XqdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522d669236.mp4?token=aLgZkvza-zmsjdOdi1ZXB0wkLDKa0plazI71F5tMC7B4xusJG_u-6tdbANj-4iGQzA0bxaGX1wwF2EMs7b6GTxFs-0YSQaM7F8DJi-1ppigcJhku0G4SKyN-wMFODN4jtVdLChuOEFyfHcdlkhDlDZzyJVwzMQfgEUF6XJYs3UnMXto-FWiL32P-k6UfWkB_iszj3xh8jw38_iFXbF2kYtL_peHNzHFxC-aaOZmeCzznd41VoWvshS7s2o2SIi_oMxsI8AltuHD1tD5C_aExILzxf28_sIxfavTai4hAi4wBxlXhITQnBg8wazHB3X25lCHASnBo526fV5XIKS44LbgOH2S73rCIa8W9v_fHuIdhu8O4G8EdG3T78LJcELPNXpuD0zmqgNlNuExFw9g1gqtgeRjK2ous0aEF19MICnGfsxVYvFZJfuf-wCO0dn5RL06uIQh3NzuDuADo5RweE10JMGL9NXlpddiUE6Eys2U1YG4A3hdx7LKuFghLrROQsUlNc03Qi0_8CAiZJX20DlZlVVmDzHwDPk09bFp2WJV5W3mq8ENVjapwJe7wQgPLYW0xhG_jd2N_EomzkGanswlowiWykyT6Zn5C8bYKRabELBRO964_T3pHfkQemDnlJc2yZPQ4M6xTQqPbjfc1BpxLZ97o6OPXjv1rV1XqdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
غیرضروری‌ترین بحث تاریخ:
خداداد: گزارشتو بکن
خیابانی: توام فوتبالتو بازی کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98279" target="_blank">📅 09:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=Zd7R7X8KBqYYnSdHYi0VpWvbK2W7p-eQtR_7ou--o4Pcz4Jo23zgxJuSbeBWZabROPIGJHFMS-NwB2HxJxL00rf0F7-xkJvpJGddzYb87A562Fefm4DfPObhaOu0V7C28Qxu0Zf3jpzJlGpymDMvfkjXaJwfggAa_AYF81vACaRi6pUfzzZPl1UzAZnvtNCRUklV-QxdKfq0RrDoV6M03_UTFAu11szgMVy0QesMj8Tk6UJ6ilm6UXFKU0lhHvclG8Zkjrstzmfa_73jFDl3RmmpXIaqdsBY0SB-VFmU3kQLKmgp6l9blKmvBY7OcW5FpHQdnO9b1wpKkjXdn_6I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=Zd7R7X8KBqYYnSdHYi0VpWvbK2W7p-eQtR_7ou--o4Pcz4Jo23zgxJuSbeBWZabROPIGJHFMS-NwB2HxJxL00rf0F7-xkJvpJGddzYb87A562Fefm4DfPObhaOu0V7C28Qxu0Zf3jpzJlGpymDMvfkjXaJwfggAa_AYF81vACaRi6pUfzzZPl1UzAZnvtNCRUklV-QxdKfq0RrDoV6M03_UTFAu11szgMVy0QesMj8Tk6UJ6ilm6UXFKU0lhHvclG8Zkjrstzmfa_73jFDl3RmmpXIaqdsBY0SB-VFmU3kQLKmgp6l9blKmvBY7OcW5FpHQdnO9b1wpKkjXdn_6I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه فوق جنجالی از بی‌توجهی کیلیان امباپه به گلر پاراگوئه در پایان بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98278" target="_blank">📅 09:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98277" target="_blank">📅 09:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897a264b10.mp4?token=rHLLvOitQFlsqqlGcnhzHmQCEtZS8jlIFMAeA3u8LisWhBzLSYuLNCSCzp6EhZfX3D1TtMmAT49AIh2JZYZBY1CjG5oYCUyGNS1vb_BHhOO_P6mJpiFrDmZeZ9QQns-BnefsaC4fw7zBqMynpKl8CNgWzPNMLIj8EP2uR8V5mvoZb0isU46hoUQbrjXwKYyKViOIvPw4pyL7vDDoE7axwetQm8O3vQiqnNZ4522LBLVJEMvmzldQyD94ySBePq5JkobEHEmoUAFR-zXsmaBUmB3ueZIwrE4GfZp9IEc-2pFcjOlNyyDbAI2-EBm2_SansVNQlYXJAYlr73K942J9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897a264b10.mp4?token=rHLLvOitQFlsqqlGcnhzHmQCEtZS8jlIFMAeA3u8LisWhBzLSYuLNCSCzp6EhZfX3D1TtMmAT49AIh2JZYZBY1CjG5oYCUyGNS1vb_BHhOO_P6mJpiFrDmZeZ9QQns-BnefsaC4fw7zBqMynpKl8CNgWzPNMLIj8EP2uR8V5mvoZb0isU46hoUQbrjXwKYyKViOIvPw4pyL7vDDoE7axwetQm8O3vQiqnNZ4522LBLVJEMvmzldQyD94ySBePq5JkobEHEmoUAFR-zXsmaBUmB3ueZIwrE4GfZp9IEc-2pFcjOlNyyDbAI2-EBm2_SansVNQlYXJAYlr73K942J9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
در پایانِ مسابقه، امباپه بسیار شاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98276" target="_blank">📅 09:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98273">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRCDxs5jjiXtko0q9SXbsdq31O6kOKQwgXq4DmtptIxh_5ZedbuARIhGJFWlRhV0haSo-ojQ5YcQe0CVqOVmSal-56nUdSEGCLJ_19za7S7U-ho5yW4wlAy_XYt8McGw1GyhWJRyPUN92X6lKr98sms8OEZ-kfusLxnMS6FFh5pYg83HCnlMF2TkKI7wSEZqsYhM5WmVxh9Di-y2xhvPZHudF9inNNiruksLWkZsoiOQ9Edkc4qoBprA_HWQkey04IreomPRm60moi0fDDVBvpFCBJzMkuo8Lv5lqivCu0ga_morlVSTVLsuZPL91IyYofgXYd4rCkbe8SjNyfiqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAFQPryxVkkaV9tTigZeBHDOfqUGuNqnZj0lHDdPGxN8USorCSgyyJCiQhz9YoksxmgRzdRcF6XqcF0mUQZpt7L7k9aTCoUYBtgKW2WtNOH8h6NgbwQyJW5iFXbHTNw94yetreKa_xtwG8eWvo3w-ePFnsV0p2gUNkaLa8QqBmivPeWtmP61WVjif2T7j5VoovF7W71v8HwR_TQpSEt9Oeky-cannno4q7F6KHeU9ZMsMLYFGlRZvdS-Pqi1gLiW59nQKYqh_TbG2VU2e7Z_kjEA5wrbRgKmUREudGw7moRKcs9fVQymvm7zgvK4Y-ATYApBQNw6ha2ws6tTVbi55g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98273" target="_blank">📅 05:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98272">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98272" target="_blank">📅 04:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE-IBcUMbgMhNUZMf2d25DjJMnms_Kaz2xkwOEmUVL_wt-qn8B9afyAj5DvvuZCl42XhKXQ4bKJ9zldcxvLQ0HDyYXpb6OLMqyW868p4-5cWTg4DVOC4hO91w-jt6DXiwy6SnvrRO-cZ8sTXrX6ny60O6DayBiKwJN-V7a_-K6YsAUa-cWF12IQUY2Bdglf8yiRN6KZCl1gzHUj84-681mM4RHDgS3zdOZY_OGKWE__1SaRgJ1wUGHK265c6mcWAEzzjH91U8rf35qTFk8pjcxK2uR-Uo24lHiQy1KYb6_n1qII7zXIb-S6UNDpuKVw-DfTUfqo4_bUIs83Y3jR1DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrP0KP8bI5XfS_CyCMe5nK-sq1yYZCdg34bSqlaJpKAuJzTfdbLGPmbyIoHDX4DVZ6Iy41G_Bh_dtKKXUa174wCJtGHXLxHqj6Abvx2FnAv5R-J5SDFqkBcrrUtOiy3T1a818fm5fLnNgbSG9sMGuklj-Hjc5vmJEeUGjXFsUa5e15J0G1zJhMRthCg7e87BgEWwsJh-Km6zhvVwQzmSGT61yiJkA4QXp4SOtnZQwk6KpnKjPZy1t1kWorzgPumRRmcA7kCO2VHZZgk_HdQu2XCYAPr9NRAX67x_k2afRgpXdFKwdciYc_R3xuYdcD3Df-gmhlsYjRsEQ0cfzRzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wbEydqJJ3J3ChwWlMAA8o5H8lrwE5lCCwOAgWETRKmIr23tgmGReVaFltGDuDTZkZ-AOIXFtARAnhIJ6TJZuiUMIdAQW9pJoPprUnFzEXYNerx9SDiWRJBoUMeWjMu6wx6iYxhVpIwJshi-u4HbKhgTnhL_m6unMduFHQFTdSGhlqURUtHrup6LGWOsHctjFTC-lzLQmRTPoZT_MP_ALvc3wXI1598Qs2gC5xRQ8lIGMObUVqS7mb-9Ti5NJGpHiPC8KoBCmJ56obbuX21O-QZUIZw4FSj-Acl9rpMouL4v2LmrTHe1Bes4PpIqG8uDOgzaBN3C2MjyYhp5usgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUQgbwUbB6_83TDEUElC3k450HHRppv56eWYxi6yWz0VaEu0pI0Hd8Smvh03jcGhMkNwgIipwlqUwGSKb97pQooakAn-tKFl_T-gAOwBco_IKhXCJTQe5oAylbnB3PlPTD1BQ4YruhfmIOo-hBt-syuTxXyKQruDaqYH9GkCN2OTXrCn-Vh0rRY9k5-0SQlBIJ2amk1RDJgVP4LFLZ4pABr__RLpyoI0Qnwgu-mKpPoya-VisFJrdwntxCHGRn3y5UjpT1OKxbiW_APMjfDsCENTpjBFOys0FxmaFJ7lqbI6Pcukw0CAd9FSJqNihPcsFldBwDxvfPPY26Pn6kaubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIA_X5Pb3Hll4BPS9yBquyeKixhZXZkgGjxJ7qd-HtwbPwqPpuhiocZX9xMsyQgPdJ83bPbBRJMonvFLpDxGzNCfarTPFKVJtaugdvQF_t-CfcNeef3d_cFvzn5UlDHJhUFJIvfPAymrhCELZiz-Q_qfSApF094CJu-mihG5LQzAS3GpgQxaHNzshTKcFPDITH_yvueHwn-rL9tAqwuoh1ZhkNFM0t1ZmlGp7jTgqFkniDRrTiOYPJJEM4XchSnic69st_1nolUynMvnC_UQfswnAuXDPswk1oNbHsSOkS2nSLBLUYHqSLX2z9k4RdbjG5Uf5TC6Bb3DtDasUYoiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2KLyuThRYnNqoUwjenJBOclYzA3NAlfkpyO0BemSegRDgNazJhEkhiVUjLjKsuhkUEG4I_rCbY7gwGO68jF5T7-0VHouelgjgEjP8NbEv_zw9wDXq76_bCNKbenYoC9OT8LylLNd2Tw6zwXadC1lFtD697WbplPg5wH6G4vUU7N1GHaSzYUhErb4krBGwyGcOpAS22kEoZWxZa2vXMyt39zKUqJ5T-Y1VfhWyxfIbdT1b4ekkjwLv2KT8iEcFYK2nMKxH0O3SfiyFONsmjpS9Yi9RR4N8gUOU7NJHlBLCKuMau6V-lGbG3ESBL8cHaPjvMBIp08c_9vMwaqOkj2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBiKEu8PHllL7zOPfpRWVnzuhuhI-m5_0uTqNxckwfaiuICBjDxDE7c7A0SC0o22VtgV5HSL_QuMXtqlZtl5aGtp2UGWOF2aUr6vzR-M01Cvund3_0gUYw_by-FXh_6iozBjZfe6_IcxxUMOZcwX6OFAEpOFgeLNecFvxEooA4BfG-ZslqO1flGAt4GKKESVlKpcLRFTEjUOmM7PtmOG01q-_eMZVRCVAifhiv0eHEHiZCqV-i6RjYJjESkWVhry4fb_FLZeXkqRTfU2392mCfZSxfrHS4AsRwkYvXTgj71CEhkTqA_l8jJEczY2e82Iqham_shnundZKVmA6_E83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxTLRXRVArKWiN0mtN2XsDrRmqRvIadihgDyiumINFVQInUZwLlrDqouzUgMBkeODVx2PWeV75f1Nn8_0zaUvs4tEFh-tAu-Uuy8xaoQfShCQetM2K0c2Wy8ii5PVClnf4qpEK6AbP8Eo4GVSTh1JqOv9q_XfxBecJUXrcfDp77XiUQRFKtIzrjdetjAwJOsg4VwcnzwoDp0meX2maOJGigl-BSI734wcvNbNEcDWHSuFGEjQ3L2ya_330qTSnbKJXMuHaCJXVTsy0v-leqMqGSg5hc2K8Vs1qlnlu5D1q8JPxTVvRMRpJ2jwPkEEN5V3SnGE5C_VLs71gMa_mhTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDATdFfoK4bUHhB1CMnwXK4NCmphtiP8VNZcnuLuMjcpuXs3eNi8PV4O3FwdcIrSbZe2VeE4RPRs42H0smVxYdGjKh3VBaMic-vhprGGxKfwlucVe-k0Iktj5hyN2akULUId8mUCgZfZHnKuRrbTyrH49EDlRnjyiPt3nYh70QuVsOMDZCTj5H0Z2Yi0x518MY8j7F6Lq-yfCNaolKMDYJuXxkq0kPqTCG6Cq2KPh_WiQcktvd11VOambA_kVQiBdYOzx2RQKwNMDsHWgp5pLqbSfe1QuLX1rgBCQbBgc4ds44I7asBbsdTtT3OcRH150ZOYOQhrG5U7V0PgEUmTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP2PzxJE6NY42U1ocHU8T1bjS8eBc96OdyZgVwSVsM5_MjYcKlVl-gGFkdy-iZuYUciXtx6onojYcy7FR5BR_XTjN-6EkRcIkr2zPXSgZp2H1Jxm4xgQVNK79RKQTRLY-YSVxmdj-LPP1f6AICvhcGZDQaWO559-y6ZPYCDwQt86E4fyqLFopTqTCUmWdaz-ad8U1nlkptDLTs5XiS0e02kbvg7NqZURJPfE1C6Kf5wgpsUu95_tx39DWTYHmBQFc6m98G1xZirHXfUF8lIhl_eRh60XTAUuBxkXIc5BeRhOCIT4RvCYSxv-j2E_E9fCKhC6uTc61nNqtea8soGKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX5D2eNDu3JUsshuhQ6qG2S0Hm0w4XXYICebi9CQLYgtCZBn32q-_try4yKloIhBg_hZzoFU6JD_dLips-UOXPIsLUUyLqNbliMW5-fKOnXpkLTz_Zj8kUso8NJ8dQPvkUC4zerGB7sIVR36syjegcDnzBPbHoMCmkNbFc7bdXH91FQPd-OWrrp8d--ZNMrcYtSVTCXWulbZt3WAURtHc5d_9cBNxrg3cmQ990h1drtTJQ_3hQH9ADP42bwSwznS-SYA4YFGCW8IJakqDJ5UE0Klm0Ej4ckVdeFrer30b8HB-VWKFOu9ehNwSLPjbhp4I8A4J_VHQfPjN9TRG72BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcQxZ0p4L3rW8nCSnRCwBoJ0gz-cuR3WnRhgTsOu3WdzqRGO0g2r8dERoBRBta_cZpA_4Tc-Y_rfI56lBDivj6J1UujnkndH7ZyUCimR9pg-abOidzhKwzYThRUHAbEDSnvnHoGofRtsnOkWTYObDD53XMBfeuSHITCsVVadRqfkGbsxeyFTKTZls2U2GIp3X_mcJojM354RZxsCELqCPL4Nzf58gWhg1TdHa6lGcx2VWHWQzb663_gR_KqomTVoJ_U_qvcIHjubhYKv5alKe-uh6C1ZI9ZkcRFifsxDvN_de3fYdbSgREeDYS4GEl--3TfgtiZWEnf4ADedxk0iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwnS_yr0tTWQwrZWn4F7ZpooAqZMgHjlf1HMULYoAAAlLPTYzHoNlN6kO4C6huaeKUYdnSzMndK_A8fewmv9YXz3ODr7u_GqaXDpd4POkQPzTAp6mt6Rp6eTqta-rO32H1YvFcrjCjaYl-bBxj76SUJIEm48csBQQwSSVaYZ0wXP7lnDnlsF7AbAMe5DvNSqzCL6OPoPF_cL1cXUnDYrQaeckWD60rqRqaClplvcFra8CkY3qwJilaJmCXctr1bxj-4qaZGlmqTBN6Xi0kjC9mO2uh9jBYTVf7tJGIqoIVcqJ4tw0Jbue6NowSUKw8T0KeCIig_JCPfyTAGsf7xv3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LukKrL_NiEdM_BmB_pYbqebP09HNt-BkYyOjnHhs_bltoUmdKNPuhxFLg0iCTd95liiPGoxhemVVifKJ04nV9Bpbg_MO1zpv8yOVx3ov-1MBmlnY33N_24AhgyPL9Kw4DXkW0YgPLub1uQc0zLrRHHPZRKbrqRRZ2Yof3f5OOe2Zh-NPD87pBOdX4QN9ZQXf7olSIkoiJNTz4eabge6hQfNkcXuxhfTLvnb7PWJW3NjdqLuI_DH6TlpLvHe7_JBLOvFW8XhiE9QRmB8oRemdsQn7TUvF-HNNsvhPNkndZf5i8jAI2PXeUYv9ZxHA3f3vZNfPOrXk5pjT-lId1XK8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C35t5XPYcIobQJF96LxAJ2L4JGPfZhc_W3BmkxEaro3eJDAXY2UIUsXjQhR3lhrLuMW2QQY28ieyvaHtEipVHV3QocN6Niop9MUmgryPVjlY9ulruKRjCByoF9yNYQYbSwTRWuJ-sAik2qfhIJvstGjSCXb2iTOQiOGCM2GK4m0iPv4De1_rZ0wd4csaq1snFh_MeHINcrtw953jM55fSaBVwrljoy63EZlcVcGWRRykkV2h0t3jnI_0TVV2VaNQFTOahQts_NclNTwOT8NsWBNzwNllepBiaVmhUgJi35VgE1Wshi1J36x_TzWkMw3IwYMkbVylvrtZSDl3BZMGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVOI8z3PUWh7OXjHfI9h4ojG275JgHhbJq9QOnnJsK7zjuYqn_WYaezvvhs7zp8-Os0GpwlKrLiuYxJpOwNL_mTX0Qf_cmVFdKKysazcrlAk5G_IgcnwTYNnBY1xlWCjDKVOchr-i91zhjT70rk2GpzeSs3tVhqDqJ9WbPx173YC8mpPbf_eFtFGPEBCPzcvwU_6n4Z_KS_3aoSo-Ujhr1WlHclgh1Ao4Qximx_bfNX0LFRyFlZZ1RzliLUgnA2vGs6pEfFbwsQ6xeVHOSgQYTVGIbnWxeJ9BtG15tNidN6oZVrqavMl7ebUXITXPijiUM5A82_76QWK5i_9Eli2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyVyWrrfY6pOFCDDTkFJXQfXGQ9m6wLas92j1FQCy_Q2uoE3CgPpKYx3ItyFpjfhV2LaecCOyTlCaIekyFQO_pNppinJpscQKg2_CdFH8T-tK6CLd2fC3mezBl1TZsNF3YBiySrcs0-K377I_PzcTziY9RlpFi0nOueRDB9YySFuyaMDMdgkY844MwPeUlBejnhsOl9LPIpx35BCwgfVV6S3gT-tU6nHPiKwYcp24HWT5N3pavOIq6xCqWX9kG4EV3lV-AKnkDKFMo9fW1lO2HAVgH-WgnKQ3xGpu_vySw1TCWqUHGw2lA-ViQpakcsjEAumqYJBalGvkbEwyC4TiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJpANK-LJclw1xliaGxDotT1k6JJGChDBYSU_p5kDiRjCYK7UAbsQRFj3lEUMNVityZ8z5CLpecagfAl8nWbrs-jplF3icy82-LynLby9kPpGvgmC8hRQiC8s6XfwRIPCZI7WAMjzYJ3cwLsC-855hXEL7n_n8UJlkoAE02frSn9F1H25I9PUKL3gvSnv9SQY9uYh-VyqigsnvQZE3PKLp_WDm0EXAcobtvd1rScm44uYSIumedg6eBXBP9PJ1juJyzASc3MBKiKgWAIvXFNUyYqrPtxBpRf3IaKV5SPAsU35BMoCl7UIbBb2AgfdU7LrDTzJFAIm2VeXSn3hZ6BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mTRRgk2jH0efk7GncaC1xZd_fucMANBiFvsSeEWflQwY9B4JqJFUrez8wsimOSi4cAP4yYd10xntIK0WrqOpURJ53wAwJZ_KvPHuE7uX8gAWEc-UVpHq98hlACtUhjtOsXu0nqzJ0xbKFAg5GeGeuWpypwUq681DeR0dgdzLGbD25mBf5gdaKdE4-iWyy6DoyeOeLCuVIWtyaaAQPPOGxA8XSns0WBuN83Po5Iyw_vLdgQgllXB5SijrsTqjAPNY8aFmbcdLyQ_OO30HHxmMJudPQ6TWaFsB9iKQx-r5cz_8Mmw3IVVSvVHMO-On9WXarddUoDJap4cphdU9fnIAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f5OyJrVRUgYJC_63Mqgtn57ZOBsvbmQNeQS-WkxahuV5Wz7I4VIEjmUiRLQVoUQectoPtWlJdhMgBnEKhHXbC9cOYaP-tGBYQRydlRW1l45EHTsr8vtMU4UcXeG8c729E3Urz9c4KzGU_cs6jv7WvSNfZR9sLj5NyBuBNOG0KZrbpSsoRGz7uK7XrHgNWLt6xdpY46N80pdlTYdPBpxTh_k9aJSEHEUNFmq1XWiFmzT_FlPeNjKb1pFj_KhhBTBukLV3g-vqsKMs3jjHnAhtNe9fq0s3WWG0T1HO8wK3iYUVDqWXQQFmTsHgmoaAIXuRVDQbX36zlEjDkvuJqdt_0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrIDAtCd6Si9RakYFBQLI9xSy14CerNqj7pQQzbMyshVNZI6Y6lUZD7BtvmMZ38jJRgD2ceUwIRCV8C1G--TEqz5vOapDqaax0b1Dpn6NJN9sSPGHNGuENBUuVxIBDmrs921cjvs9zQN4ckWDuqMT35feTsK7zoQy-TgXLsVhUjH0fmM9DK2sCzcI3B7Qye2ZwG11KkcCWB1IH1jt4KpM06ZJ6opodUI0g6LsBEPyPg2tK7exG7-R5L-p_1Un-SHqC0NDb8_OciDe9obwArCuNyFHxgIsp4iahzhhuJpLUh1JwVjcASVwy-H8_TUIfE1hhkIxWfw7McmtZkICmMF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3YCdPIZQCM54vol0vAL8HKNUwHn8eIkDv7qRV5GrIkPrj5ccPYswunXgmGe6YV2Fz_RYbcGBrncg1mdoTp47yLzix-Lr7MNsMjwiRoxOglE6My2_7fvwD-7HdfOndBhtucyPwJNszRtAW-lKrlGj3acq5666j-E4a0F2IbrJ11ZhcbPZmWdN7NVROyeiKGODWH8RA_ovS6daPERYFd7Sam4PKAdcj5KcIpmFHC36kFX6xc16svv2tbWN0wyWVue-iBtxiaWzU46QWae2ernVHR1OsJaXaxHIG1lZigr7rr4TmIL3jF_6C9sE4dhHXjBmdYtcU3ldpVS-Ln9kDotyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oudNW_nXBxpER8CMsrHTg2y5yB8cjFUYnmS4rud6iPMmpxtPCLxm9vJHiHibofbnxIvJQCAcYnlVHKbbRy6FjGi700chjeOdZzhEwOyTzCczW6NWhxVKS0mRe8mug5yv2Kjp3Nw1C783_0QtX1ATsEGZGfluNBE-JV_s-gUhDDqDG7uvwRNwclqsNJZWcbhApkPEsfLonzt_J_a1TALTSJFIRgaHDKdScXq3s1ugBTI8_Gfe2FrEOch_lmYly999qjOG1UY1a6sEcv5_mC-6vvrUdK0kd81VIfdaYUDSutLS-AojhzOS9GSclzuM3QaQu2-EZ8aVWwlABJREMNU3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SslEVu-t_C89TqtCHpoZig38ES3ouiEhtH4WCgW9sy4cu-Z7GgZ-tEIUozghhXqPZywx0nTzTe1nsZdAuPcD_LFuqtd_uOEY-xVjMEAf-wOt3UuvAXtzK6eeBW9VUGHO1hkD3fWlDT4FcOx7ISAA5aIhmCG7uWeNZm-Jswblnlmvz0wT1VdGEBDO_qlY8RSM1y7Kz_CNJDx5yaAsCXXh3qJK7Zq6UDg-SfKruWvgmI2wLfGLeq2s8ImTCx0MtK0T5JXxBGK6qfMFO3kEfC2y_WjDv9vs3gJMZb11djqSPke0wZ-_IvQrMZ3fq13qdPTdn1BcQLSUHOh7UTweJhm1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MoX9n6Umlzc5lgrh5cOc-cVAB6ZENU-YmgV5XXvrH4SMnpLykP6D0qzZcJ03EMqCOomkEnep1Y1-OIEqzhMQeM61veSdJdjtZlTcbnod-nUgYEck_vMFTySzVNGl_cFgVCnW2faxj71364c-3CmTpZV7JQOwNs3C4LTqMC1cpf1xIbvIDt-wSe_9y_dcyl45fgEvfNh_58C0UMI808QbWNntWzVJTPuVG12L3mCurQ56nnpMUIkEjhux6YleupyyCApfngECIgWXQGafAphUwso19wq33lNcBrjTOStEP0zFhGZ2cTknchRoE1MzJ91Haz0zf-9Q5kChB6-vVK6Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-sNnHYNQOe7IgeedHFfY9dVvR4WX55yyjb-UwvmdLAGxUykjHLPlZvT1xdmykmuYoDMGJi0VYULSwZBbL4hxeE7uG3rp0uGGhJL_dR1YYJzP2H5Kly2HDWqDmGJWlHIUH62ZTZufCe-va8Pr8WD89qbWd3uPb-DXEwndxjUNcmsuOqK3XMX35L-NTHuyLU6eoVFxBiaTURC88QYtFUqygftOlPBv4dQ0CZuH24G_J2IZvdsmt8-_nMXlyq1YSJ-RkhwBnkbG7bBHeSE3AyBFKpGiZ-B6PWHAkPm6up8yXobWjc8IUel48ilSZBNKCppSncpiaPBc4xHLr5V_NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0fENN8bzoFSkuUKRWMFYpjrokZDu_hKKsmyxzWTH2GlpUIoUDOSVFfj1eVy3r3DqDcr8f_-NDrQKfcEh6WX9tPWsspWJH10Dc2XtzfnMXDn1jFrOBj67rj4Pxp-kbKnRngo2xZgQC1uN8Ao_ED-S4Iarp4hHxtCrlndjqjnQptiQzoENYJOj9InUSnd3q-NMjVw5lVgK7VQjWCVZ3ovVl1OoLoCUpuuGLPCKX5B5O1SVhvQu-pgD22ENa77Fh9KLRSSa0hCSGd9SL1u9p_JW97DRAGD1coHHZMUq2Cxgi-Rjqwq7JSYebIM9EJcvkWvx4s7XJl5myalmTta8VzEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN2MdvhQQzT1tT9DFzaulge7Gr6sL_ceH27zOKaF755tGQ5LMuYbQuzepGjJ2WJSj8pJQ7NQntjkmTlRyE7rV8zQeSOiqTxqHOrbwX1tMxibOV5ijVmklxku1r6RFQDxqBpPBVdR5rGyo1L8RejJ9haBBfQYbl5K9sSbLrBEORKtuzYdo3F1SP-30bntioSZVp1V82AksTaj8cfL0UEWbCWKRpW-CkhX8qKpZdmmND4zMm7upqAkXBjctJ3p-DKV-6wiE5XOhoxXtIR1qnWxaiG6GoCONnKx1Jpn3pET4xZ-VugT3TBMR-vVjiH7M_fwZfbwFo6x7qRbSBZ_7pEXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMxP3l4jUe4h60PKUdUWK8e-ki9scK06t4VMMZxlrgzh1IVha_-vPr6cRGoXHt90wmDEaIdw5cN1AxY6n8nDxUC_iJYOpBlkpBVzg5oWXK4qtn5o0QedkKNTwMpUz6lYsIowLKBlIqcRf_kgpcsBU3G7W3Zv9r9Szvn2RCpAARcWxkvsTT2OeMQYn684gHVxYQjsL8ATigHjTGr5TctjXSlXe6IDJuiNK-uKpSHSGhGVh73fyAD2XR9qqKuVSgmGSPQjA0NtOORI_o3qLqMLxrfW0qDSaK5FVlV17RmwV3uaUuVGZnF9z4Q7SZQ-tdDNjiR0YNypE67rqSOL7RWo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doSoCjZchqGCIC3IJDOOGitdiCTK3PAlJpeY7J9bhv50Ij01nS0_wTFDpN4C6Wl5vuFSbxHEsh1h1Z0qj-E6CvWUGEnK-LoRB026J_2lykwaHva3HLNJ0rVy1DU5ClI_oWPKjV3flDkiS138OD2uCi_EM30BGtX8mMwST4tUjkH-7ma5604xJP_8mizj4X0kANNtePD1rJ4cfV0mFfH_o4rX_sKKIs_-oTLSXT9nu483tAuZTBm1sYEaCd_VJhtkDALv5HHEUrRNS64_1lf-qDw29aQJIEHAYiONFdgbld-nOFdskrxQ2Ul1uZDQKszzH6ozFqbe7F18WjlKk5xOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnLq5pRBpzWvmpJ3s_nWRyFDeMot1x_vvpRYeU8HdfCQq8dSy1CFAXI5ZozNsZpzsZgMtaq_abDSU6Uo4rBIkv1PJ5nVOKmb3ds0m4Yq1ZcBIR3AMccmXNYA-sC9Qrc1VcUCmfrIDeaTwBVwztQf4wTWuP4h3kkr5CmsLO6Enpl8qVL1whQGYV6Wxr2Xj0GBWeCqelKf9gTcuDuubf-ACoC1r6Gwr8jxEHawdHQ-qrlKEn7mDXJbaB4feAkW_3OnlrqFNF8jXcrtyEAUzBiH2daiTDA8T1nc8q6ux-DPab7BIX-NTUqy7SnJwss8Ns2i9kEQZ5dOccpvqhIX1emDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmbzT3faLLnfRdrdOtPop1II1Uf01oD5mp2S8OKaUaRjYQFgRaOz4jqKZZ-2uUx0uMdEhC0pXLi7UVfgdndYygoXU9yWVDfetW_47VF-ukMsSK10FHkU1_lW7gZpnyADGjYfOAbbgWr7I3KcHFsh9QYpZ16NDBgClNtcQK-JvW6uQhXvOYIZ15SCR-YIxfLV2P223EULBwNzQ-xlaVlBPwJIh8jwrnD1-ezLUJm2cPkaMKAlvYN3siyr63ED7mqSywC6sD1kdH7U19YyMF5lbDc2COMOklvVlGAkS-W2R_dUtXDx9qabaoVubVQ79Uz71TTpG0cDC4XRT45sCq0Xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_fsulOL8cuoUuSuyWxhOJDGyeGpQYhhvDUDLFy62AxXiw2qMCMkfQ2pg4GcfjwkxcrG36bE3g3knGpXeO-AhUBX1cbfYsuWkESop1pfAbnRCx47AIzpKOnS2Vv_2Lmz6R6QXU0bMMoNeS6iM-9Ozx9nZ6IKrafWPXvrQlKPGyeKiTAx0Pv9NvwCOmh7-0ySBiYcfnh3INcKPaTvoquCQmv6Z9F2dOsOqyEIRaQYDCUfHOQpmJTlw-bAJTShid1LelIbFkv3gn6woIzM-FO4nAfPB63SkvI58LVypUUvPgsPYTFJ1hYzFkEp0FYPoGt6dfH5ajkAZM5yA9kG-BCNmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNQqm40WzmuMKnIxLqr4Rxk-0B0eF1WJU1wdSiopJMoWY_Yr1_H8tgA_74jXkcIcjr8-Rlf8oOsCUEwYv_jTOfE2dy5Mk9cV8es1F_UwOooKiKfIqVKkpH2N5XSb4Ca57oZ2h118IVex83MSRTpYcBPeTHqM8txeqcO-_ccXzWSsmbTC8CBE93AS-LkxNE-z-ltcff88mOJrdSvrn_JuwsCbBiFjy7Cx-Nu0royKMCq5p8qM7DcBPUWW6N6j6e53REUj0ZHNV6guNJ3ZoGFNIAK9dSBCx9FUQj1uKf3SxCa9pEzX1QEpEhAcqiuMNgVLAQ3pszepUZqGBi0sMh3MLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7T4U9c2apTsjsmleUQbQcJYDkDoWNiibklovnF8DN3wglomo0o3zsAQH4d9lEaTVOGZabMaqj0qZb8D11Uwg-IBG_R7SUB6bKYDYyEECiDdsGYlbAKziuQM0ZpGOelfoz6BkA_0m3BqwlYVaD4QnFL7vylA8_-EoITxZjI4IpcZzD9Nt-wWK1JdKfJj7bNLZRL0UNb_sjTaRTsb2DnGlS22Ndk-33KdXemUuP934p5l22173hLjonA-Uuqks9UeygcQydQe_Fv686JE_MIHK64__XE00Mp1Eq8VfbDsDcYKEHNvbL7pPZGtReIvE9-1lFUpNwzCTzvDytJxD-ECxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKrkjnEOKfgSNkthuK1xF1jxSsOpgb4WeJP3W77bEBo4dbXu6BaT9NVds_DTQunRxgRXBA3KlXGwCfi0W5GXCsYlexGrNEc9OEn1MjEHoxtHEe5yA6BYyADbCCn9pgMnVQPunsyJPhY7AHQ6N753shI5z10fIgyDCso8TLh3ejiUfz9f07VoR1onxB97PHNKnRIiERMqaGhxyGMnYTV3m0mgPFGIvCShdK9vIauNdXw30jVaXcm4oJoSF4r6YGfaKKV4KnGKSQyzAyLTV8zV2MB5dbhVlx3X2IAKxm6xXbh3YaRH7_tmirfe8VSo3F7eoZNqHG7F-oKDjRgTJih_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4CMtn2tdyoC71C4VUxSt2JMduV0Czkw5vBntmP_GXaLaJ4vJ4uPKevwv7kLYP7-DiqlOlBxqVYXdH47CNb5TtDPS2W-9AHeLJltgK2FE8FkduG47L3HCy8ErKXnUtE_zvkSyWKOZBfJoDAI0yAJFB2sDPU6IcrCefrq5ej7LemXJMZLCR4nD6QKe9h918UIKOOCFgAJwbODH2vxq8KYcWRVCkastnxVfnR42d1pK-2rSfpp35bNedZOTAIsJcnb-AgJzRVsmjWgOzDamDfJ3MubQLyAfm3atcWWBbRxWfc6ZIP1reeng9XHMt3hvCDnFKgfecvOHeFEEHQ0e-lXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4rW12Ie-RRzGq2XH8-0QyhEfBD6KAhLOX7E5OmFTXTihosYHnqVQPPisZnjC7ZVMtKIzWFbOqLWupmcPPCb9XeC35_Ydq9C2qwrwfG49CrnaseklXTYQYCskccC3rG6MTYobkDnKX0c1S7t0t0RfDHvug8wgtqv037fbQFznQyLRrW0fhceUjP6G-68iJSrWRDOIhSRQaRLY-Slyk1lLA2JxXQAOnL8kSphBHd8j9eUF1qQqyc3Q6DxLGi-pUuBvxwhWcLX5dzQRN7S89MUK5cfx0_4IiA_tKDVK1ZOyDa5JytJjIPv-uY0XKS9G3BHMRDpcaKs1DGuXXJ5ohTVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI8RsvZ2WgFp36WY6s8AeeR5Pya64FSziDgTLkQSllFnZkgwznf9WiDRYUkCMOEkaIfd_pleOODHlVfRT-7L70RkJt-O35_sHXa9-28MafR1Ah5iJSj6VmJHO7nA9gUaZU4MwqBPSdbvRvzl-767a9OYxRGJZ7rXfw5zksRs6VuM2Re3ZUrJrSMB7uNbQcpxbQZeG8WQT5WPURmxKG7e9cc35qVAPY6UGeb-xFRsYPg93gitNDThV2l8lIxQUR2D05m0o09IM2wQRBcTRlOzE8NxyItkEIJKSivDQJpk7KsdWFuI6VOY7vpNt0ycavsDC4VRK5SSkVPw3kHLq9mDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVVmYX-58g_FKRJ9Td2pdgppx7MRDDf3KHJz31N0WxcFx-jgDPC_p0nDRi8RZTbwobCLIOJeaNGgcC1tx6LTVQ68rGPdlzXHl7i7HL1uZwgaq5Hvu2seQo7btlBCUJQvSaw-nZAv_943tjZOI5zq9nZeafFzU-s_MpnKHzK3xsL_WCQjADtWWodRmjQCpia4I0o4liu-_kkp463f3OWQiYc5fdzOJUs9CR6A17bvg70sFh2fZ6_Fqj05Q1rxs8NtNmO3G-LGQugiHDiPA71XvcnupHQoFrX8T5yeVw8MjCs9-aLBErNkxV4___2iynZ7WBgW91WJPXM1kifKiCiJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
